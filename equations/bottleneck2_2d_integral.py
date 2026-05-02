"""
Bottleneck 2 — 2D Coupling Integral (Cycle 96)
===============================================

Physical question:
  Does the 2D coupling integral of the D6 kink zero mode ψ₀(x)=sech²(x/λ)
  with the D5 vortex phase profile g(ρ) produce the required mode normalization
  9/(64π) ≈ 0.04476?

  From worldvolume_coupling.py (Cycle 88): the required KK mode normalization
  follows algebraically from the compact form g²=2πβI₄ and the worldvolume
  normalization N_wv=(64π/9)M_c:
      mode_norm_required = 9/(64π) = 1/N_wv  [in units M_c=λ=1]

  This module:
    (a) Derives mode_norm = 9/(64π) algebraically (zero free parameters)
    (b) Solves the D5 vortex BVP for g(ρ)
    (c) Computes seven candidate integrals from the vortex profile
    (d) Identifies which (if any) equals 9/(64π) exactly
    (e) Quantifies the discrepancy for each candidate
    (f) States the residual open gap precisely

STATUS (Cycle 96):
  ALGEBRAIC ROUTE: mode_norm = 9/(64π) confirmed exactly from:
      g²×(2πr_U1)×N_wv×M_c = (2π)² → mode_norm = (2π)²/(g²×2πr_U1×N_wv×M_c)
  PHYSICAL ROUTE: The 2D vortex integral closest to 9/(64π) is the
      normalized vortex core integral (see Candidate E below).
  GAP: No vortex profile integral has been shown to equal 9/(64π) exactly
      from the substrate field equation alone.

Key references:
  equations/worldvolume_coupling.py      (Cycle 88: gap statement, N_wv derivation)
  equations/bottleneck2_coupling_integral.py (Cycle 85: compact form g²=2πβI₄)
  equations/complex_substrate.py         (Cycle 75: vortex BVP, r_v≈1.099ξ)
  foundations/phase_stiffness_derivation.md (Cycle 47: f²=(4/3)φ₀²/λ exact)
"""

import math
import numpy as np
from scipy.integrate import solve_bvp, quad
from scipy.interpolate import interp1d

# ─── Parameters ────────────────────────────────────────────────────────────────

BETA     = 0.035          # quartic coupling (Tier 3 reference)
ALPHA    = 2.0            # quadratic coupling (g² is β-only; α checked)
PHI0     = math.sqrt(ALPHA / BETA)
LAM      = math.sqrt(2.0 / ALPHA)   # kink half-width λ = 1/M_c
MC       = math.sqrt(ALPHA / 2.0)   # closure scale

I4       = 4.0 / 3.0      # ∫sech⁴(u)du = 4/3 (exact)
G2_DFC   = 2.0 * math.pi * BETA * I4   # = 8πβ/3 (compact form, Cycle 85)
R_U1     = 3.0 / (4.0 * BETA)          # r_U1/λ = 3/(4β) (algebraic identity)
N_WV     = 64.0 * math.pi / 9.0        # worldvolume normalization (Cycle 85, in M_c units)

TARGET   = 9.0 / (64.0 * math.pi)      # required mode_norm = 9/(64π) ≈ 0.04476


# ─── 1. Algebraic derivation of mode_norm = 9/(64π) ─────────────────────────

def algebraic_mode_norm():
    """
    Derive mode_norm = 9/(64π) from the KK matching formula.

    The gauge coupling from KK reduction satisfies:
        g² = (2π)² / (2π r_U1 × N_wv × M_c × mode_norm)

    Solving for mode_norm with g²=8πβ/3, r_U1=3λ/(4β), N_wv=(64π/9), M_c=1/λ:
        mode_norm = (2π)² / (g² × 2π r_U1 × N_wv × M_c)

    In natural units where λ=M_c=1:
        numerator   = (2π)² = 4π²
        denominator = (8πβ/3) × 2π × (3/(4β)) × (64π/9) × 1
                    = (8πβ/3) × (π × 3/(2β)) × (64π/9)
                    = (8πβ/3) × (3π)/(2β) × 64π/9
                    = 8 × 3 × 64 / (3 × 2 × 9) × π³ × β/β
                    = (8 × 64)/(2 × 9) × π³
                    = 512/18 × π³  = 256/9 × π³

        mode_norm = 4π² / (256π³/9) = 4π² × 9/(256π³) = 36/(256π) = 9/(64π)

    This derivation uses ONLY:
      (i)   g² = 2πβI₄ = 8πβ/3      [compact form, Cycle 85]
      (ii)  r_U1 = 1/(βI₄) = 3/(4β) [algebraic identity, Cycle 47]
      (iii) N_wv = (64π/9)M_c        [worldvolume normalization, Cycle 85]
    No free parameters beyond β.
    """
    # Numerical verification
    Mc   = MC
    lam  = LAM
    r_U1 = R_U1 * lam          # in physical units
    N_wv = N_WV * Mc            # in physical units
    g2   = G2_DFC

    numerator   = (2.0 * math.pi)**2
    denominator = g2 * 2.0 * math.pi * r_U1 * N_wv
    mode_norm   = numerator / denominator

    exact_val   = 9.0 / (64.0 * math.pi)
    error       = abs(mode_norm - exact_val) / exact_val

    return {
        'mode_norm_computed': mode_norm,
        'mode_norm_exact':    exact_val,
        'error':              error,
        'formula':            '9/(64π)',
        'inputs_used':        ['g²=8πβ/3', 'r_U1=3/(4β)', 'N_wv=(64π/9)M_c'],
        'free_parameters':    0,
    }


# ─── 2. D5 vortex BVP solution ───────────────────────────────────────────────

def solve_vortex(rho_max=30.0, N=1000):
    """
    Solve the D5 vortex equation (dimensionless, ρ in units of ξ=λ):
        g'' + g'/ρ − g/ρ² + 2g(1−g²) = 0
    with boundary conditions g(0⁺)=0, g(∞)=1.

    This is the n=1 winding vortex of the complex DFC potential
    V = −α/2|Φ|² + β/4|Φ|⁴ (Cycle 75: complex_substrate.py).

    In the DFC model, ξ = λ = √(2/α), so the vortex and kink widths are equal.
    All integrals below are in units where ξ = λ = 1.
    """
    rho_min = 1e-3
    rho = np.linspace(rho_min, rho_max, N)
    # Initial guess: hyperbolic tangent profile
    g0  = np.tanh(rho)
    gp0 = 1.0 / np.cosh(rho)**2

    def rhs(r, y):
        g, gp = y
        gpp = -gp / r + g / r**2 - 2.0 * g * (1.0 - g**2)
        return np.vstack([gp, gpp])

    def bc(ya, yb):
        return np.array([ya[0] - rho_min, yb[0] - 1.0])

    sol = solve_bvp(rhs, bc, rho, np.vstack([g0, gp0]), tol=1e-10, max_nodes=10000)

    # Interpolated functions for integration
    g_interp  = interp1d(sol.x, sol.y[0],  kind='cubic', fill_value=(0.0, 1.0), bounds_error=False)
    gp_interp = interp1d(sol.x, sol.y[1],  kind='cubic', fill_value='extrapolate', bounds_error=False)

    # Vortex core radius: where g = 1/√2
    thresh = 1.0 / math.sqrt(2.0)
    idx = np.where(sol.y[0] >= thresh)[0]
    r_v = sol.x[idx[0]] if len(idx) > 0 else float('nan')

    return sol.x, sol.y[0], g_interp, gp_interp, r_v


# ─── 3. D6 kink zero mode ────────────────────────────────────────────────────

def d6_zero_mode_normalized():
    """
    D6 kink zero mode:  ψ₀(x) = √(3/(4λ)) × sech²(x/λ)

    Normalized: ∫_{-∞}^{+∞} ψ₀(x)² dx = 1

    In units where λ=1:  ψ₀(x) = √(3/4) × sech²(x),  N = √(3/4)

    Normalization check:
        ∫ (3/4) sech⁴(x) dx = (3/4) × I₄ = (3/4)(4/3) = 1 ✓
    """
    N_ψ   = math.sqrt(3.0 / 4.0)     # normalization coefficient (λ=1)
    N_ψ_sq = 3.0 / 4.0               # N_ψ²

    # Verify ∫ N_ψ² sech⁴(x) dx = 1
    I4_num, _ = quad(lambda x: (1/math.cosh(x))**4, -100, 100)
    norm_check = N_ψ_sq * I4_num

    return {'N_psi': N_ψ, 'N_psi_sq': N_ψ_sq, 'norm_check': norm_check,
            'profile': 'ψ₀(x) = √(3/4) sech²(x)  [λ=1 units]'}


# ─── 4. Seven candidate integrals ────────────────────────────────────────────

def candidate_integrals(g_interp, gp_interp, r_v, rho_max=30.0):
    """
    Compute seven candidate mode normalization integrals from the vortex profile.

    All integrals in natural units (λ = ξ = 1).
    Target: mode_norm_required = 9/(64π) ≈ 0.04476.

    Candidates and their physical interpretations:
    A. Vortex angular gradient:     ∫₀^∞ g(ρ)²/ρ² dρ
       = integral of (phase gradient magnitude)² over radial distance.
       [Expected: finite, ~ O(2); vortex core dominates]

    B. 1D candidate (Cycle 88):     (3/4) ∫₀^∞ sech⁴(ρ) × g(ρ)² dρ
       = 1D approximation using kink and vortex on same axis.
       [Known: ≈ 0.08965 ≈ 2×target; wrong geometry]

    C. Gradient energy (no measure): ∫₀^∞ [g'(ρ)]² dρ
       [Expected: finite but not 9/(64π)]

    D. KK mode: vortex phase winding / r_U1
       = (1/(2πr_U1)) × ∫₀^{2πr_U1} dφ = 1/(r_U1)
       [Tests: does simple KK formula give target?]

    E. Normalized angular energy:    (1/(2π r_U1)) × 2π ∫₀^{r_U1} g(ρ)²/ρ dρ
       = (1/r_U1) × ∫₀^{r_U1} g²/ρ dρ
       [Logarithmically regulated at r_U1 = 3/(4β)]

    F. BPS-type integral:            (1/(4π)) × ∫₀^∞ [g'²+g²/ρ²+2(1-g²)²] ρ dρ
       = vortex energy / (4π)
       [Tests: does vortex energy relate to mode_norm?]

    G. Angular × amplitude:          (1/(2π)) × ∫₀^∞ g(ρ) × g'(ρ) / ρ dρ
       [Mixed gradient-amplitude integral]
    """
    target = TARGET
    r_U1   = R_U1   # = 3/(4β) in units of λ=1

    # Numerically integrate each candidate
    # A: ∫₀^∞ g²/ρ² dρ  (integral from rho_min to avoid divergence at 0)
    rho_min = 1e-3
    def integrand_A(r):
        return g_interp(r)**2 / r**2
    I_A, err_A = quad(integrand_A, rho_min, rho_max, limit=200)
    # Near-zero correction: g ~ C×ρ, so g²/ρ² ~ C² (constant at 0)
    # Extrapolate: C = g(rho_min)/rho_min
    C_lin = float(g_interp(rho_min)) / rho_min
    I_A_correction = C_lin**2 * rho_min  # integral of constant from 0 to rho_min
    I_A += I_A_correction

    # B: 1D candidate (3/4) ∫₀^∞ sech⁴(u) g(u)² du  [known ≈ 0.08965]
    def integrand_B(u):
        return (3.0/4.0) * (1/math.cosh(u))**4 * g_interp(u)**2
    I_B, _ = quad(integrand_B, 0, rho_max, limit=300)

    # C: ∫₀^∞ [g'(ρ)]² dρ
    def integrand_C(r):
        return gp_interp(r)**2
    I_C, _ = quad(integrand_C, rho_min, rho_max, limit=200)

    # D: Simple KK: 1/r_U1  (no vortex profile, just the geometry)
    I_D = 1.0 / r_U1

    # E: (1/r_U1) × ∫₀^{r_U1} g²/ρ dρ  (regulated by r_U1)
    def integrand_E(r):
        return g_interp(r)**2 / r
    I_E_raw, _ = quad(integrand_E, rho_min, r_U1, limit=300)
    # Correction near 0: g ~ Cρ → g²/ρ = C²ρ → integral from 0 to rho_min = C²×rho_min²/2
    I_E_corr = 0.5 * C_lin**2 * rho_min**2
    I_E = (1.0 / r_U1) * (I_E_raw + I_E_corr)

    # F: Vortex energy / (4π)  =  (1/(4π)) ∫ [g'²+g²/ρ²+2(1-g²)²] ρ dρ
    def integrand_F(r):
        g_val  = float(g_interp(r))
        gp_val = float(gp_interp(r))
        return (gp_val**2 + g_val**2/r**2 + 2.0*(1.0 - g_val**2)**2) * r
    I_F_raw, _ = quad(integrand_F, rho_min, rho_max, limit=300)
    I_F = I_F_raw / (4.0 * math.pi)

    # G: (1/(2π)) ∫₀^∞ g(ρ) × g'(ρ) / ρ dρ  [mixed integral]
    def integrand_G(r):
        return g_interp(r) * gp_interp(r) / r
    I_G, _ = quad(integrand_G, rho_min, rho_max, limit=200)
    I_G /= (2.0 * math.pi)

    candidates = {
        'A_angular_gradient':   I_A,
        'B_1D_candidate':       I_B,
        'C_gradient_energy':    I_C,
        'D_simple_KK':          I_D,
        'E_regulated_angular':  I_E,
        'F_vortex_energy_4pi':  I_F,
        'G_mixed_gradient':     I_G,
    }

    results = {}
    for name, val in candidates.items():
        ratio  = val / target if target > 0 else float('inf')
        error  = abs(val - target) / target * 100.0
        results[name] = {
            'value':          val,
            'target':         target,
            'ratio_to_target': ratio,
            'error_pct':      error,
        }
    return results


# ─── 5. Full 2D factorized integral ──────────────────────────────────────────

def full_2d_integral(g_interp, rho_max=30.0):
    """
    The 2D factorized coupling integral in the (x, ρ) plane.

    Physical setup:
      D6 kink zero mode:  ψ₀(x) = √(3/4) sech²(x)   [in x direction, λ=1]
      D5 vortex profile:  g(ρ)                         [in ρ direction, ξ=1=λ]

    When D6 kink and D5 vortex are in ORTHOGONAL directions (correct 2D geometry),
    the coupling integral factorizes as:

        J_2D = [∫_{-∞}^{+∞} |ψ₀(x)|² dx] × [∫₀^{∞} K(ρ) dρ]
              = 1 × ∫₀^{∞} K(ρ) dρ

    where K(ρ) is the vortex coupling kernel in the transverse (ρ) direction.

    Key candidates for K(ρ):
      K₁(ρ) = g(ρ)²/ρ²           [angular phase gradient squared]
      K₂(ρ) = g(ρ)²/ρ / r_U1     [regulated by holonomy radius]
      K₃(ρ) = |g'(ρ)|²           [radial gradient energy]
      K₄(ρ) = (1-g(ρ)²)/ρ        [condensate deficit; diverges at 0]
    """
    r_U1 = R_U1
    rho_min = 1e-3

    # K₁: ∫₀^∞ g²/ρ² dρ (dominant for small ρ)
    C_lin = float(g_interp(rho_min)) / rho_min
    def K1(r):
        return g_interp(r)**2 / r**2
    I_K1, _ = quad(K1, rho_min, rho_max, limit=200)
    I_K1 += C_lin**2 * rho_min

    # K₂: (1/r_U1) ∫₀^{r_U1} g²/ρ dρ
    def K2(r):
        return g_interp(r)**2 / r
    I_K2_raw, _ = quad(K2, rho_min, r_U1, limit=200)
    I_K2_corr = 0.5 * C_lin**2 * rho_min**2
    I_K2 = (I_K2_raw + I_K2_corr) / r_U1

    # K₃: ∫₀^∞ g'² dρ
    def K3(r):
        return float(np.gradient(g_interp(np.array([r-1e-5, r, r+1e-5])), 1e-5)[1])**2
    # Better: use gp from BVP
    # (We'll use the analytical gradient from the BVP itself)

    # K₄: The "double-cover" candidate: (1/2) × 1D = (1/2)×0.08965 ≈ target?
    def K_1d_half(u):
        return (3.0/4.0) * (1/math.cosh(u))**4 * g_interp(u)**2
    I_1d, _ = quad(K_1d_half, 0, rho_max, limit=300)
    I_half_1d = 0.5 * I_1d

    return {
        'K1_angular_gradient':      I_K1,
        'K2_regulated_angular':     I_K2,
        'K4_half_1D_candidate':     I_half_1d,
        'target':                   TARGET,
        'ratios': {
            'K1/target': I_K1 / TARGET,
            'K2/target': I_K2 / TARGET,
            'K4/target': I_half_1d / TARGET,
        }
    }


# ─── 6. α-independence verification for mode_norm ───────────────────────────

def alpha_independence_mode_norm():
    """
    Verify mode_norm = 9/(64π) is exactly α-independent.

    Since mode_norm = (2π)²/(g² × 2πr_U1 × N_wv × M_c) and all factors are
    β-only (by the α-independence proof of Cycle 85), mode_norm must also be β-only.

    Direct check: mode_norm depends only on I₄ = 4/3 (exact) and β.

    From mode_norm = 9/(64π):
      - Independent of α? YES: derived from g²=2πβI₄, r_U1=1/(βI₄), N_wv=(64π/9)M_c
        and M_c×λ=1 — no α appears.
    """
    results = []
    for alpha in [0.5, 1.0, 2.0, 5.0, 10.0]:
        phi0 = math.sqrt(alpha / BETA)
        lam  = math.sqrt(2.0 / alpha)
        Mc   = math.sqrt(alpha / 2.0)
        f2   = (4.0/3.0) * phi0**2 / lam
        g2   = 2.0 * math.pi * BETA * I4
        r_U1 = 3.0 * lam / (4.0 * BETA)
        N_wv = (64.0 * math.pi / 9.0) * Mc

        mode_norm = (2.0*math.pi)**2 / (g2 * 2.0*math.pi * r_U1 * N_wv)
        exact     = 9.0 / (64.0 * math.pi)
        error     = abs(mode_norm - exact) / exact

        results.append({
            'alpha':      alpha,
            'mode_norm':  mode_norm,
            'exact':      exact,
            'error':      error,
        })
    return results


# ─── 7. Gap statement ────────────────────────────────────────────────────────

def bottleneck2_status(candidate_results, r_v):
    """
    Precise Bottleneck 2 status after Cycle 96.

    ALGEBRAIC ROUTE (closed):
      mode_norm = 9/(64π) follows from g²=2πβI₄, r_U1=3/(4β), N_wv=(64π/9)M_c.
      All derived from substrate with 0 free parameters beyond β.
      This is a self-consistency check, not an independent derivation.

    PHYSICAL ROUTE (open):
      Show that the vortex BVP integral giving the KK mode normalization
      independently produces 9/(64π) from the field equation alone.
      This requires identifying which vortex integral (if any) equals 9/(64π).

    From numerical computation (Cycle 96):
      Best candidate: [reported below from candidate_results]
      Discrepancy: [reported below]

    FUNDAMENTAL OBSTACLE:
      The vortex angular gradient ∫₀^∞ g²/ρ² dρ ≈ O(1-2) >> 9/(64π) ≈ 0.045.
      The 1D candidate gives ≈ 0.0897 ≈ 2×target (wrong geometry, factor 2 off).
      No pure vortex integral has been shown to equal 9/(64π) from the field eq.
      A derivation would need to show how the DFC geometry selects this specific
      combination of integrals from the substrate field equation V(φ)=−αφ²/2+βφ⁴/4.

    REMAINING GAP (precisely):
      Compute the D5-D6 worldvolume coupling integral in the full 2D (x,ρ) geometry
      with correct metric factors, show it equals 9/(64π) × (normalization factors),
      and verify the normalization factors themselves from the substrate.
    """
    best_name  = min(candidate_results, key=lambda k: abs(candidate_results[k]['ratio_to_target'] - 1.0))
    best       = candidate_results[best_name]
    return {
        'best_candidate':         best_name,
        'best_value':             best['value'],
        'best_ratio_to_target':   best['ratio_to_target'],
        'best_error_pct':         best['error_pct'],
        'target':                 TARGET,
        'algebraic_route':        'CLOSED (mode_norm=9/(64π) derived algebraically)',
        'physical_route':         'OPEN (vortex BVP integral not yet matched to 9/(64π))',
        'tier':                   'Tier 4 (algebraic consistency shown; physical derivation open)',
    }


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('=' * 72)
    print('BOTTLENECK 2 — 2D COUPLING INTEGRAL (Cycle 96)')
    print('D6 kink zero mode × D5 vortex phase gradient')
    print('=' * 72)
    print(f'β = {BETA},  α = {ALPHA},  φ₀ = {PHI0:.4f},  λ = {LAM:.4f},  M_c = {MC:.4f}')
    print(f'g² = 8πβ/3 = {G2_DFC:.6f},  r_U1/λ = {R_U1:.4f},  N_wv/M_c = {N_WV:.4f}')
    print(f'Target mode_norm = 9/(64π) = {TARGET:.8f}')

    # ── 1. Algebraic derivation ──
    print('\n── 1. Algebraic derivation of mode_norm = 9/(64π) ──')
    alg = algebraic_mode_norm()
    print(f'   mode_norm computed = {alg["mode_norm_computed"]:.8f}')
    print(f'   mode_norm exact    = {alg["mode_norm_exact"]:.8f}  (= 9/(64π))')
    print(f'   Error              = {alg["error"]:.2e}')
    print(f'   Inputs: g²=8πβ/3, r_U1=3/(4β), N_wv=(64π/9)M_c  [β-only, 0 free params] ✓')

    # ── 2. D6 zero mode ──
    print('\n── 2. D6 kink zero mode ──')
    zmode = d6_zero_mode_normalized()
    print(f'   ψ₀(x) = √(3/4) sech²(x)  [λ=1 units]')
    print(f'   Normalization check ∫ψ₀² dx = {zmode["norm_check"]:.8f}  (target: 1.0) ✓')

    # ── 3. Solve vortex BVP ──
    print('\n── 3. D5 vortex BVP (solving...) ──')
    rho_arr, g_arr, g_interp, gp_interp, r_v = solve_vortex()
    print(f'   Grid: ρ ∈ [0, {rho_arr[-1]:.1f}], N={len(rho_arr)} points')
    print(f'   g(0⁺)  = {g_arr[0]:.4f}   (target: ~0)')
    print(f'   g(∞)   = {g_arr[-1]:.6f}  (target: 1.0)')
    print(f'   r_v/ξ  = {r_v:.4f}   [vortex core radius; target ~1.099]')
    C_lin = float(g_interp(1e-3)) / 1e-3
    print(f'   C_lin  = {C_lin:.4f}   [g(ρ)≈C×ρ near origin]')

    # ── 4. Seven candidate integrals ──
    print('\n── 4. Candidate mode normalization integrals ──')
    cands = candidate_integrals(g_interp, gp_interp, r_v)
    print(f'   {"Candidate":30s}  {"Value":12s}  {"Ratio/target":14s}  {"Error%":10s}')
    print(f'   {"-"*72}')
    for name, res in cands.items():
        marker = '← MATCHES ✓' if abs(res['ratio_to_target'] - 1.0) < 0.05 else ''
        print(f'   {name:30s}  {res["value"]:12.6f}  {res["ratio_to_target"]:14.4f}  '
              f'{res["error_pct"]:9.2f}%  {marker}')
    print(f'   Target (9/(64π))               {TARGET:12.8f}')

    # ── 5. Full 2D factorized integral ──
    print('\n── 5. Full 2D factorized integral ──')
    print(f'   D6 kink (x) ⊥ D5 vortex (ρ) — orthogonal geometry')
    print(f'   J_2D = [∫ψ₀² dx] × [∫K(ρ) dρ] = 1 × ∫K(ρ) dρ')
    two_d = full_2d_integral(g_interp)
    print(f'   K1 (angular gradient g²/ρ²):   {two_d["K1_angular_gradient"]:.6f}  '
          f'  (ratio {two_d["ratios"]["K1/target"]:.2f}× target)')
    print(f'   K2 (regulated angular /r_U1):  {two_d["K2_regulated_angular"]:.6f}  '
          f'  (ratio {two_d["ratios"]["K2/target"]:.2f}× target)')
    print(f'   K4 (½ × 1D candidate):         {two_d["K4_half_1D_candidate"]:.6f}  '
          f'  (ratio {two_d["ratios"]["K4/target"]:.4f}× target)')
    print(f'   Target:                         {TARGET:.6f}')
    print(f'')
    ratio_K4 = two_d["ratios"]["K4/target"]
    if abs(ratio_K4 - 1.0) < 0.01:
        print(f'   FINDING: K4 = ½ × 1D candidate ≈ target (ratio={ratio_K4:.4f}) ✓')
        print(f'   Physical interpretation: the 1D candidate double-counts because it')
        print(f'   uses BOTH the kink sech⁴ profile AND the vortex g² on the same axis.')
        print(f'   In the correct 2D geometry (x ⊥ ρ), the x-integral gives 1 (normalized),')
        print(f'   and the ρ-integral should give the VORTEX contribution only.')
    else:
        print(f'   FINDING: K4 ≈ target to {abs(ratio_K4-1.0)*100:.2f}% — see gap analysis below.')

    # ── 6. α-independence verification ──
    print('\n── 6. α-independence of mode_norm ──')
    ai = alpha_independence_mode_norm()
    print(f'   {"α":>8}  {"mode_norm":>12}  {"exact 9/(64π)":>14}  {"error":>10}')
    print(f'   {"-"*50}')
    for row in ai:
        sym = '✓' if row['error'] < 1e-12 else '✗'
        print(f'   {row["alpha"]:>8.1f}  {row["mode_norm"]:>12.8f}  '
              f'{row["exact"]:>14.8f}  {row["error"]:>10.2e}  {sym}')
    print(f'   mode_norm = 9/(64π) is exactly α-independent (β-only) ✓')

    # ── 7. Gap statement ──
    print('\n── 7. Bottleneck 2 status ──')
    status = bottleneck2_status(cands, r_v)
    print(f'   Algebraic route:  {status["algebraic_route"]}')
    print(f'   Physical route:   {status["physical_route"]}')
    print(f'   Best vortex candidate: {status["best_candidate"]}')
    print(f'     Value = {status["best_value"]:.6f}  (ratio = {status["best_ratio_to_target"]:.4f}×target,'
          f' error = {status["best_error_pct"]:.1f}%)')
    print(f'   Tier: {status["tier"]}')
    print()
    print('── Summary ──────────────────────────────────────────────────────────────')
    print(f'  PROVEN (Cycle 96, algebraic):')
    print(f'    mode_norm = 9/(64π) = {TARGET:.8f}  from g²=2πβI₄, r_U1=1/(βI₄), N_wv=(64π/9)M_c')
    print(f'    α-independence: exact, 0 free parameters beyond β')
    print(f'    Verification error: {alg["error"]:.2e}')
    print()
    print(f'  KEY FINDINGS from vortex integrals:')
    print(f'    1D candidate (3/4)∫sech⁴g² dρ = {cands["B_1D_candidate"]["value"]:.6f}')
    print(f'       ≈ {cands["B_1D_candidate"]["value"]/TARGET:.4f} × target  (factor ~2 excess from co-linear geometry)')
    print(f'    ½ × 1D candidate             = {two_d["K4_half_1D_candidate"]:.6f}')
    print(f'       ≈ {two_d["ratios"]["K4/target"]:.4f} × target  (closest candidate)')
    print(f'    Angular gradient ∫g²/ρ² dρ  = {cands["A_angular_gradient"]["value"]:.4f}')
    print(f'       ≈ {cands["A_angular_gradient"]["ratio_to_target"]:.1f}× target  (too large; vortex core dominates)')
    print()
    print(f'  OPEN GAP (Route B, Cycle 96):')
    print(f'    The ½×1D candidate is close to target but derived from wrong geometry.')
    print(f'    A physical derivation must show the D5-D6 worldvolume coupling integral')
    print(f'    in orthogonal 2D geometry (x ⊥ ρ) produces mode_norm = 9/(64π) exactly.')
    print(f'    Required: compute ∫_{{x,ρ}} ψ₀(x)² × K_vortex(ρ) dx dρ from V(φ)=-αφ²/2+βφ⁴/4')
    print(f'    where K_vortex(ρ) is the vortex coupling kernel consistent with mode_norm=9/(64π).')
    print()
    print(f'  [Module: equations/bottleneck2_2d_integral.py | Cycle 96 — Bottleneck 2]')
