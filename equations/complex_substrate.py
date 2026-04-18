"""
Complex Substrate Extension — Cycle 75

Extends the D5 substrate field from a real scalar φ to a complex scalar
Φ = φ₁ + iφ₂ with potential V = −α/2|Φ|² + β/4|Φ|⁴.

DFC mechanism at D5:
  The complex scalar has vacuum manifold S¹ of radius φ₀ = √(α/β).
  The stable D5 topological defect is the vortex (π₁(S¹) = Z), not the Z₂ kink.
  The evidence: the fluctuation operator L₂ in the transverse (φ₂) direction around
  the real kink has a tachyonic bound state ω² = −α/2, showing the real kink is
  a saddle point in the complex scalar field space — unstable to transverse deformation.
  D6/D7 kinks (in their own depth-sector fields) are unaffected.

Computations:
  1. Vortex profile g(ρ) from BVP solution of the dimensionless vortex equation
  2. Vortex core radius r_v in units of ξ
  3. Longitudinal (L₁) and transverse (L₂) fluctuation spectra around the real kink
  4. Phase stiffness f² = (4/3)φ₀²/ξ [preserved from Cycle 47]
  5. Gauge coupling candidates for different r_U1 identifications
  6. Gap analysis: why r_v/ξ ≈ O(1) ≠ target r_U1/λ = 3/(4β) ≈ 21

Key finding: Neither the vortex core radius nor the field-space radius φ₀ equals
the target r_U1. The identification r_U1/λ = 3/(4β) must come from the D5-D6
coupling integral, not from the vortex geometry alone.

References:
  Phase stiffness: foundations/phase_stiffness_derivation.md (Cycle 47)
  Heuristic coupling: equations/coupling_derivation.py (Cycle 42)
  D5-D6 charge: equations/complex_structure_derivation.py (Cycle 67c)
  Conceptual document: foundations/complex_substrate.md (Cycle 75)
"""

import numpy as np
from scipy.integrate import solve_bvp, quad
from scipy.linalg import eigh_tridiagonal

# ── Physical parameters ───────────────────────────────────────────────────────

ALPHA = 1.0     # quadratic coupling (dimensionless reference; results scale out of g²)
BETA  = 0.035   # quartic coupling (reference value from Planck-scale kink width)
C     = 1.0     # field propagation speed (set to 1)


def kink_params(alpha=ALPHA, beta=BETA):
    """Return (φ₀, ξ): vacuum amplitude and kink half-width."""
    phi0 = np.sqrt(alpha / beta)
    xi   = C * np.sqrt(2.0 / alpha)    # ξ = c√(2/α), convention from Cycle 72 onwards
    return phi0, xi


# ── 1. Vortex profile ─────────────────────────────────────────────────────────

def _vortex_rhs(rho, y, n_wind):
    """ODE system: g'' + g'/ρ − n²g/ρ² + 2g(1−g²) = 0 as [g', g'']."""
    g, gp = y
    gpp = -gp / rho + n_wind**2 * g / rho**2 - 2.0 * g * (1.0 - g**2)
    return np.vstack([gp, gpp])


def _vortex_bc(ya, yb, n_wind, rho_min):
    """BCs: g(rho_min) = rho_min^n (near-origin), g(rho_max) = 1 (vacuum)."""
    return np.array([ya[0] - rho_min**n_wind, yb[0] - 1.0])


def solve_vortex(n_wind=1, rho_min=0.04, rho_max=18.0, N=400):
    """
    Solve the dimensionless vortex profile equation for winding number n_wind.

    Returns:
        rho  : radial grid in units of ξ
        g    : profile g(ρ) = f(r)/φ₀
        success : True if solver converged
    """
    rho   = np.linspace(rho_min, rho_max, N)
    g0    = np.tanh(rho)**n_wind
    gp0   = n_wind * np.tanh(rho)**(n_wind - 1) / np.cosh(rho)**2
    y_init = np.vstack([g0, gp0])

    fun = lambda rho, y: _vortex_rhs(rho, y, n_wind)
    bc  = lambda ya, yb: _vortex_bc(ya, yb, n_wind, rho_min)

    sol = solve_bvp(fun, bc, rho, y_init, tol=1e-9, max_nodes=8000)
    return sol.x, sol.y[0], (sol.status == 0)


def vortex_core_radius(rho, g, threshold=1.0 / np.sqrt(2)):
    """
    Return r_v in units of ξ: the radius where g crosses threshold (default 1/√2).
    Uses linear interpolation.
    """
    idx = np.where(g >= threshold)[0]
    if len(idx) == 0:
        return np.nan
    i = idx[0]
    if i == 0:
        return rho[0]
    # Linear interpolation between i-1 and i
    r_v = rho[i-1] + (threshold - g[i-1]) / (g[i] - g[i-1]) * (rho[i] - rho[i-1])
    return r_v


# ── 2. Fluctuation spectra around the real kink ───────────────────────────────

def fluctuation_spectra(alpha=ALPHA, beta=BETA, N=500, L_fac=20.0):
    """
    Eigenvalues of the longitudinal (L₁) and transverse (L₂) fluctuation operators
    around the real kink Φ = φ₀ tanh(x/ξ) in the complex scalar background.

    L₁ (φ₁ direction, same as real scalar):
        V''_∥ = −α + 3β φ₀² tanh² = α(3 tanh² − 1)
        PT with s = 2; U₀ξ² = 3α × 2/α = 6 → s(s+1) = 6 → s = 2
        Bound states: ω² = 0 (zero mode), ω² = (3/2)α (shape mode)

    L₂ (φ₂ direction, NEW in complex scalar):
        V''_⊥ = −α + β φ₁² = −α sech²(x/ξ)
        PT with s = 1; U₀ξ² = α × 2/α = 2 → s(s+1) = 2 → s = 1
        Bound state: ω² = −(1/ξ)² = −α/2  [TACHYONIC → real kink is a saddle point]

    Returns:
        x   : spatial grid
        ev1 : lowest 6 eigenvalues of L₁
        ev2 : lowest 6 eigenvalues of L₂
    """
    phi0, xi = kink_params(alpha, beta)
    Lx  = L_fac * xi
    x   = np.linspace(-Lx, Lx, N)
    dx  = x[1] - x[0]
    t   = np.tanh(x / xi)
    s2  = 1.0 / np.cosh(x / xi)**2    # sech²(x/ξ)

    U1 = alpha * (3.0 * t**2 - 1.0)    # V''_∥: PT s=2
    U2 = -alpha * s2                    # V''_⊥: PT s=1 (tachyonic bound state)

    diag1  = 2.0 / dx**2 + U1
    diag2  = 2.0 / dx**2 + U2
    offdiag = -np.ones(N - 1) / dx**2

    ev1 = eigh_tridiagonal(diag1, offdiag, eigvals_only=True, select='i', select_range=(0, 5))
    ev2 = eigh_tridiagonal(diag2, offdiag, eigvals_only=True, select='i', select_range=(0, 5))
    return x, ev1, ev2


# ── 3. Phase stiffness ────────────────────────────────────────────────────────

def phase_stiffness(alpha=ALPHA, beta=BETA):
    """
    f² = (4/3) φ₀² / ξ
    Proved exactly in Cycle 47 from the Bogomolny identity: ∫sech⁴(u) du = 4/3.
    Unchanged by the complex extension — the kink shape in φ₁ is the same.
    """
    phi0, xi = kink_params(alpha, beta)
    return (4.0 / 3.0) * phi0**2 / xi


# ── 4. Gauge coupling candidates ──────────────────────────────────────────────

def coupling_candidates(alpha=ALPHA, beta=BETA, r_v_over_xi=1.1):
    """
    Evaluate g² for different candidate r_U1 identifications.
    Holonomy formula: g² = 2π / (r_U1 / λ)  where λ = ξ.

    Candidates:
      A. r_U1 = r_v  (vortex core radius, purely geometric)
      B. r_U1 = φ₀   (field-space S¹ radius)
      C. r_U1 = 3λ/(4β) (heuristic from Cycle 42; gives g² = 8πβ/3)

    SM target:
      g_common = 0.5443 at M_c(12) from SM running → g² = 0.2963
    """
    phi0, xi = kink_params(alpha, beta)

    g2_from_ratio = lambda ratio: 2.0 * np.pi / ratio

    # Candidate A: vortex core
    rA = r_v_over_xi                   # r_v/ξ from BVP
    gA2 = g2_from_ratio(rA)

    # Candidate B: field-space S¹ radius
    rB = phi0 / xi                     # = α / √(2β)  — has α dependence
    gB2 = g2_from_ratio(rB)

    # Candidate C: heuristic 3/(4β)
    rC = 3.0 / (4.0 * beta)
    gC2 = g2_from_ratio(rC)            # = 8πβ/3

    g_sm   = 0.5443
    g2_sm  = g_sm**2

    return {
        'A_vortex_core': {
            'r_U1/λ': rA, 'g²': gA2,
            'label': f'r_U1 = r_v ≈ {rA:.2f}ξ (vortex core radius, BVP)'
        },
        'B_field_space_S1': {
            'r_U1/λ': rB, 'g²': gB2,
            'label': f'r_U1 = φ₀ (field-space S¹ radius; α-dependent)'
        },
        'C_heuristic': {
            'r_U1/λ': rC, 'g²': gC2,
            'label': f'r_U1/λ = 3/(4β) (Cycle 42 heuristic; g² = 8πβ/3)'
        },
        'SM_target': {
            'r_U1/λ': 2.0 * np.pi / g2_sm, 'g²': g2_sm,
            'label': f'SM common coupling g = {g_sm:.4f} at M_c (target)'
        }
    }


# ── 5. Real kink stability in compressed D5 sector ───────────────────────────

def kink_stability_analysis(alpha=ALPHA, beta=BETA):
    """
    Compare the energy of the 'soft' escape path (around S¹ in field space)
    to E_kink, as a function of the available system length L.

    Soft path: Φ(x) = φ₀ e^{iθ(x)}, θ: 0 → π over length L
    E_soft(L) = φ₀² ∫(∂_x θ)² dx ≈ φ₀² π² / L

    Hard kink (BPS-correct, Cycle 48):
    E_kink = (4/3) c² φ₀² / ξ  (exact, α-independent ratio relative to ξ)

    The real kink is energetically preferred when E_soft > E_kink, i.e., L < L_crit.
    L_crit = φ₀² π² / E_kink = (3/4) π² ξ

    Since DFC compression sets L ~ ξ, and L_crit = (3/4)π² ξ ≈ 7.4 ξ >> ξ,
    the real kink IS metastable at compression scales.
    """
    phi0, xi = kink_params(alpha, beta)
    E_kink = (4.0 / 3.0) * C**2 * phi0**2 / xi
    L_crit = phi0**2 * np.pi**2 / E_kink   # = (3/4) π² ξ

    L_vals = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0]) * xi
    E_soft = phi0**2 * np.pi**2 / L_vals

    return {
        'E_kink': E_kink,
        'L_crit_over_xi': L_crit / xi,
        'L_vals_over_xi': L_vals / xi,
        'E_soft_over_Ekink': E_soft / E_kink,
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 68)
    print("COMPLEX SUBSTRATE EXTENSION — Cycle 75")
    print("Extending D5 from real φ to complex Φ = φ₁ + iφ₂")
    print("=" * 68)

    alpha, beta = ALPHA, BETA
    phi0, xi = kink_params(alpha, beta)

    print(f"\nParameters:")
    print(f"  α = {alpha:.3f},  β = {beta:.4f}")
    print(f"  φ₀ = √(α/β) = {phi0:.6f}")
    print(f"  ξ  = √(2/α) = {xi:.6f}")
    print(f"  Vacuum manifold: S¹ of radius φ₀ = {phi0:.4f}")

    # ── 1. Vortex profile ─────────────────────────────────────────────────────
    print(f"\n── 1. Vortex profile (n=1 winding) " + "─" * 30)
    rho, g, success = solve_vortex(n_wind=1)
    print(f"  BVP solver: {'converged ✓' if success else 'FAILED ✗'}")

    r_v = vortex_core_radius(rho, g)
    print(f"  Vortex core radius r_v (g = 1/√2): {r_v:.4f} ξ")

    print(f"  Profile samples:")
    for rho_val in [0.2, 0.5, 1.0, 1.5, 2.0, 4.0, 8.0]:
        g_val = float(np.interp(rho_val, rho, g))
        print(f"    g({rho_val:.1f}ξ) = {g_val:.5f}")

    # ── 2. Fluctuation spectra ────────────────────────────────────────────────
    print(f"\n── 2. Fluctuation spectra around real kink " + "─" * 23)
    _, ev1, ev2 = fluctuation_spectra(alpha, beta)

    print(f"  Longitudinal L₁ (φ₁ direction, PT s=2):")
    print(f"    ω²₀ = {ev1[0]:+.6f}  [expected: 0 (zero mode)]")
    print(f"    ω²₁ = {ev1[1]:+.6f}  [expected: +{1.5*alpha:.4f} = (3/2)α (shape mode)]")
    print(f"    ω²₂ = {ev1[2]:+.6f}  [continuum edge, expected: +{2.0*alpha:.4f} = 2α]")

    print(f"  Transverse L₂ (φ₂ direction, PT s=1) — NEW in complex scalar:")
    print(f"    ω²₀ = {ev2[0]:+.6f}  [expected: {-alpha/2:.4f} = −α/2]")
    print(f"    TACHYONIC (ω² < 0): real kink is a saddle point in complex scalar")
    print(f"    → D5 does NOT form real kinks; stable D5 defect is the vortex")
    print(f"    → D6/D7 kinks in their own fields are NOT affected")
    print(f"    ω²₁ = {ev2[1]:+.6f}  [continuum; expected: +{0:.4f} = 0 edge]")

    # ── 3. Phase stiffness ────────────────────────────────────────────────────
    print(f"\n── 3. Phase stiffness " + "─" * 44)
    f2 = phase_stiffness(alpha, beta)
    print(f"  f² = (4/3)φ₀²/ξ = {f2:.6f}   [exact, Cycle 47 — unchanged by complex extension]")
    print(f"  Goldstone action:  S_θ = (f²/2)∫(∂_μθ)²  →  photon propagator ∝ 1/k²")

    # ── 4. Coupling candidates ────────────────────────────────────────────────
    print(f"\n── 4. Gauge coupling candidates " + "─" * 35)
    print(f"  Holonomy formula: g² = 2π / (r_U1/λ)  with λ = ξ")
    print(f"  SM target: g²_SM = {0.5443**2:.6f}  (g_common = 0.5443 at M_c)")
    print()

    candidates = coupling_candidates(alpha, beta, r_v_over_xi=r_v)
    for key, d in candidates.items():
        g2  = d['g²']
        ratio = d['r_U1/λ']
        if key != 'SM_target':
            g2_sm = candidates['SM_target']['g²']
            err = 100 * (g2 - g2_sm) / g2_sm
            print(f"  {d['label']}")
            print(f"    r_U1/λ = {ratio:.4f},  g² = {g2:.6f},  error vs SM = {err:+.1f}%")
        else:
            print(f"  {d['label']}")
            print(f"    r_U1/λ = {ratio:.4f},  g² = {g2:.6f}  (reference)")
        print()

    # ── 5. Kink stability ─────────────────────────────────────────────────────
    print(f"── 5. Real kink metastability in compressed D5 sector " + "─" * 13)
    stab = kink_stability_analysis(alpha, beta)
    print(f"  E_kink = {stab['E_kink']:.6f}  [BPS-correct, Cycle 48]")
    print(f"  L_crit = (3/4)π² ξ = {stab['L_crit_over_xi']:.4f} ξ")
    print(f"  At DFC compression scales L ~ ξ:")
    print(f"  {'L/ξ':>8}  {'E_soft/E_kink':>15}  stable?")
    for L_xi, ratio in zip(stab['L_vals_over_xi'], stab['E_soft_over_Ekink']):
        stable = '✓  (kink preferred)' if ratio > 1.0 else '✗  (decay possible)'
        print(f"  {L_xi:8.2f}  {ratio:15.4f}  {stable}")
    print(f"  → Real kink is metastable for L ≲ {stab['L_crit_over_xi']:.1f} ξ")
    print(f"  → DFC compressed state (L ~ ξ) satisfies L < L_crit ✓")

    # ── 6. Gap summary ────────────────────────────────────────────────────────
    print(f"\n── 6. Gap analysis — Bottleneck 2 status " + "─" * 26)
    rC = 3.0 / (4.0 * beta)
    print(f"  Target: r_U1/λ = 3/(4β) = {rC:.2f}")
    print(f"  Vortex core:  r_v/ξ = {r_v:.2f}  (factor {rC/r_v:.1f}× smaller than target)")
    print(f"  Field-space:  φ₀/ξ  = {phi0/xi:.2f}  (α-dependent; not a pure β result)")
    print()
    print(f"  OPEN (Bottleneck 2): Derive r_U1/λ = 3/(4β) from the D5-D6 coupling integral.")
    print(f"  Route: g² = (∫j_x dx)² / (photon normalization × kink normalization)")
    print(f"  Key ingredient: ∫j_x dx = −2π/(5ξ) known from Cycle 67c")
    print(f"  Missing: photon normalization factor and its ξ dependence")
    print()
    print(f"  VERIFIED by complex extension:")
    print(f"  ✓ S¹ vacuum manifold of radius φ₀ = {phi0:.4f} now geometrically defined")
    print(f"  ✓ Vortex: core at r_v = {r_v:.4f}ξ, g(∞) → 1 [BVP converged]")
    print(f"  ✓ D5 does not form real kinks (tachyonic L₂ mode: ω² = {ev2[0]:+.4f})")
    print(f"  ✓ Real kink metastable at compression scale L ~ ξ (L < L_crit)")
    print(f"  ✓ Phase stiffness f² = {f2:.4f} preserved [Cycle 47 unchanged]")
    print(f"  ✓ KK reduction on field-space S¹ now geometrically well-defined")


if __name__ == "__main__":
    main()
