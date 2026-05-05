"""
The compression field equation — substrate dynamics of the Dimensional Folding Model.

This module contains the governing equations for the compression field φ(x,t),
the fundamental object of the DFC framework. It generalizes the 1+1D kink solution
in kink_model.py to a full D-dimensional field theory with:

  - The field equation (wave equation + buckling potential)
  - Compression budget conservation
  - Buckling criterion (instability threshold)
  - Small-perturbation spectrum (what modes propagate)
  - Folding rate field (the quantity that produces gravity)

STATUS: Partially formalized. The 1D kink solution is exact. The D-dimensional
generalization, conservation laws, and gravity connection are correctly framed
but not yet fully derived from first principles. See foundations/substrate.md.

The central equation (schematic, D dimensions):

    ∂²φ/∂t² = c² ∇²φ − V'(φ) − η ∂φ/∂t

where:
    φ(x,t)  = compression field (higher φ = less configurational freedom)
    V(φ)    = buckling potential: V = -α/2 φ² + β/4 φ⁴   (α,β > 0)
    η       = viscoelastic damping (converts organized motion to heat)
    c       = propagation speed of compression modes (= speed of light at D2)

The compression budget:
    B = ∫ ρ_B dV    where ρ_B = ½(∂φ/∂t)² + ½c²(∇φ)² + V(φ)
    dB/dt = − ∮ J_B · dA   (conservation law — budget flows, doesn't vanish)

Related documents:
    foundations/substrate.md                   — substrate postulates and five-postulate structure
    foundations/phase_stiffness_derivation.md  — f²=(4/3)φ₀²/λ proved exactly (Cycle 47)
    foundations/bifurcation_dynamics.md        — M_c(D5), S_kink/ℏ, BPS-correct kink energy
    phenomena/thermodynamics/phase_transitions.md — phase transitions as V_eff bifurcations
    equations/kink_model.py                    — 1D kink solutions (analytic, BPS-correct)

Usage:
    python equations/compression_field.py
"""

import math

# ── Field parameters ──────────────────────────────────────────────────────────

# Default buckling potential parameters (from kink_model.py calibration)
ALPHA_DEFAULT = 1.0    # quadratic potential coefficient (drives compression)
BETA_DEFAULT  = 1.0    # quartic coefficient (prevents divergence; sets stable minima)
C_LIGHT       = 1.0    # propagation speed (normalized to 1 in natural units)
ETA_DEFAULT   = 0.0    # viscoelastic damping (0 = conservative, η > 0 = dissipative)


# ── Buckling potential ────────────────────────────────────────────────────────

def buckling_potential(phi, alpha=ALPHA_DEFAULT, beta=BETA_DEFAULT):
    """
    The double-well buckling potential:

        V(φ) = -α/2 φ² + β/4 φ⁴

    Properties:
      - Unstable maximum at φ = 0 (unfolded/high-freedom state)
      - Two stable minima at φ = ±√(α/β)  (the two fold orientations)
      - Barrier height: V_barrier = α²/(4β)
      - Kink (topological soliton) interpolates between the two minima

    Parameters
    ----------
    phi : float
        Compression field value.
    alpha, beta : float
        Potential parameters (both positive).

    Returns
    -------
    float : V(φ)
    """
    return -0.5 * alpha * phi**2 + 0.25 * beta * phi**4


def potential_derivative(phi, alpha=ALPHA_DEFAULT, beta=BETA_DEFAULT):
    """
    V'(φ) = -α φ + β φ³   (restoring force in field equation)
    """
    return -alpha * phi + beta * phi**3


def stable_minima(alpha=ALPHA_DEFAULT, beta=BETA_DEFAULT):
    """
    Stable field values (fold orientations): φ_± = ±√(α/β)
    """
    return math.sqrt(alpha / beta), -math.sqrt(alpha / beta)


def kink_width(alpha=ALPHA_DEFAULT, c=C_LIGHT):
    """
    Kink width λ = √(2c²/α)  — spatial scale of the fold transition region.
    """
    return math.sqrt(2 * c**2 / alpha)


def kink_energy(alpha=ALPHA_DEFAULT, beta=BETA_DEFAULT, c=C_LIGHT):
    """
    Topological kink energy (BPS-correct):

        E_kink = (4/3) c α^{3/2} / (β √2)
               = (4/3) c² φ₀² / λ

    where φ₀ = √(α/β) is the kink amplitude and λ = √(2c²/α) is the kink width.

    This is the mass analogue of a stable localized closure.
    It is finite, localized, and topologically protected.

    NOTE: The formula (4/3)c√(2α³/β) was RETRACTED in Cycle 48 — it was wrong by
    a factor of 2√β. This function uses the BPS-correct result matching kink_model.py.
    """
    return (4.0 / 3.0) * c * alpha**1.5 / (beta * math.sqrt(2))


# ── Compression budget ────────────────────────────────────────────────────────

def energy_density(phi, dphi_dt, grad_phi_sq,
                   alpha=ALPHA_DEFAULT, beta=BETA_DEFAULT, c=C_LIGHT):
    """
    Local compression budget density ρ_B:

        ρ_B = ½(∂φ/∂t)² + ½c²|∇φ|² + V(φ)

    The three terms are:
      - Kinetic: compression rate (time variation)
      - Gradient: spatial variation (compression gradients → gravity)
      - Potential: stored compression (mass, bound states)

    Parameters
    ----------
    phi : float
        Field value at the point.
    dphi_dt : float
        Time derivative ∂φ/∂t.
    grad_phi_sq : float
        |∇φ|² = sum of squared spatial gradients.

    Returns
    -------
    float : local energy density.
    """
    return (0.5 * dphi_dt**2
            + 0.5 * c**2 * grad_phi_sq
            + buckling_potential(phi, alpha, beta))


# ── Buckling criterion ────────────────────────────────────────────────────────

def buckling_criterion(sigma_local, sigma_star):
    """
    Determine whether a local region has exceeded the buckling threshold.

    When accumulated stress σ_local > σ*, the field undergoes a buckling
    transition: a new orthogonal degree of freedom opens, and the field
    reconfigures rather than diverging.

    This is the mechanism that prevents singularities.

    Parameters
    ----------
    sigma_local : float
        Local stress measure (e.g., compression density, field gradient magnitude).
    sigma_star : float
        Critical buckling threshold.

    Returns
    -------
    bool : True if the region has buckled (new mode opens).
    float : excess stress above threshold (positive = buckled).
    """
    excess = sigma_local - sigma_star
    return excess > 0, excess


def bifurcation_scale(alpha=ALPHA_DEFAULT, beta=BETA_DEFAULT, c=C_LIGHT):
    """
    Characteristic scale at which buckling occurs.

    The bifurcation point is at φ = 0 (the unstable maximum).
    The scale of the transition is set by the kink width λ.
    The energy scale of the transition is the barrier height.

    Returns
    -------
    dict with characteristic scales.
    """
    barrier  = alpha**2 / (4 * beta)
    width    = kink_width(alpha, c)
    phi_min  = math.sqrt(alpha / beta)
    e_kink   = kink_energy(alpha, beta, c)

    return {
        'phi_stable':       phi_min,
        'barrier_height':   barrier,
        'kink_width':       width,
        'kink_energy':      e_kink,
        'note': ('Barrier height sets the energy cost of a fold reversal. '
                 'Kink width sets the spatial scale of fold transitions.'),
    }


# ── Small-perturbation spectrum ───────────────────────────────────────────────

def perturbation_spectrum(phi_0, alpha=ALPHA_DEFAULT, beta=BETA_DEFAULT, c=C_LIGHT):
    """
    Spectrum of small perturbations δφ around a stable background φ_0.

    The linearized field equation around φ_0:
        ∂²δφ/∂t² = c²∇²δφ − V''(φ_0) δφ

    This is a Klein-Gordon equation with effective mass²:
        m_eff² = V''(φ_0) = -α + 3β φ_0²

    At the stable minima φ_0 = ±√(α/β):
        V''(φ_±) = -α + 3β(α/β) = 2α > 0  (mass-like, stable)

    At the unstable maximum φ_0 = 0:
        V''(0) = -α < 0  (tachyonic, unstable — triggers buckling)

    Parameters
    ----------
    phi_0 : float
        Background field value around which we perturb.

    Returns
    -------
    dict with effective mass and mode character.
    """
    v_pp = -alpha + 3 * beta * phi_0**2   # V''(φ_0)
    stable = v_pp > 0

    return {
        'phi_0':        phi_0,
        'V_double_prime': v_pp,
        'm_eff_sq':     v_pp,
        'm_eff':        math.sqrt(abs(v_pp)),
        'mode_type':    'massive scalar' if stable else 'tachyonic (unstable)',
        'stable':       stable,
        'dispersion':   f'ω² = c²k² + {v_pp:.4f}' if stable else
                        f'ω² = c²k² - {abs(v_pp):.4f}  (unstable for k < √{abs(v_pp)/c**2:.4f})',
    }


# ── Folding rate field (proto-gravity) ────────────────────────────────────────

def folding_rate_field(phi, dphi_dt, alpha=ALPHA_DEFAULT, beta=BETA_DEFAULT):
    """
    The local folding rate Γ(x,t) — the quantity that sources gravity.

    In the Dimensional Folding Model, gravity arises from spatial gradients in
    the folding rate. The folding rate measures how quickly dimensional volume
    is being removed at a given point.

    Schematic definition (to be refined):
        Γ = -dV/dφ × φ̇  =  V'(φ) × ∂φ/∂t

    This quantity:
      - Is positive where compression is removing degrees of freedom
      - Is largest near kinks (fold transitions)
      - Sources the lateral redistribution of structure (gravity)

    STATUS: This is a schematic form. The precise connection to the Einstein
    field equations requires deriving the effective stress-energy tensor from
    the compression field — see folding_gradient.py.

    Returns
    -------
    float : local folding rate.
    """
    return potential_derivative(phi, alpha, beta) * dphi_dt


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    sys.path.insert(0, '.')

    print("=" * 65)
    print("COMPRESSION FIELD — SUBSTRATE DYNAMICS")
    print("Dimensional Folding Model")
    print("=" * 65)

    alpha, beta, c = ALPHA_DEFAULT, BETA_DEFAULT, C_LIGHT

    print(f"\n--- Buckling Potential Parameters ---")
    phi_plus, phi_minus = stable_minima(alpha, beta)
    print(f"  Stable minima:   φ_± = ±{phi_plus:.4f}")
    print(f"  Barrier height:  {alpha**2/(4*beta):.4f}")
    print(f"  Kink width λ:    {kink_width(alpha, c):.4f}")
    print(f"  Kink energy:     {kink_energy(alpha, beta, c):.4f}")

    print(f"\n--- Perturbation Spectrum ---")
    for phi_test in [phi_plus, 0.0, phi_plus * 0.5]:
        spec = perturbation_spectrum(phi_test, alpha, beta, c)
        print(f"  φ₀ = {phi_test:.4f}:  m²_eff = {spec['m_eff_sq']:.4f}  "
              f"→ {spec['mode_type']}")

    print(f"\n--- Bifurcation Scale Summary ---")
    bif = bifurcation_scale(alpha, beta, c)
    for k, v in bif.items():
        if k != 'note':
            print(f"  {k:20s}: {v:.4f}" if isinstance(v, float) else f"  {k:20s}: {v}")
    print(f"  {bif['note']}")

    print(f"\n--- Status and Open Problems ---")
    print(f"  Solved:    1+1D kink solution (see kink_model.py)")
    print(f"  Solved:    Small-perturbation spectrum around stable backgrounds")
    print(f"  Open:      D-dimensional generalization of field equation")
    print(f"  Open:      Conservation law for compression budget in curved background")
    print(f"  Open:      Connection between folding rate field and GR stress-energy tensor")
    print(f"  Open:      Quantization of compression field modes → ℏ")
    print(f"  See: foundations/substrate.md, foundations/d1_mechanics.md")
