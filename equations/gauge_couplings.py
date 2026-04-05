"""
Gauge coupling running and convergence analysis.

In the Dimensional Folding Model, the three coupling constants converge because
all D5/D6/D7 closures emerge from the same substrate with the same kinetic
coefficient — not because they were once a single unified gauge group.

The convergence is real and measurable. Its interpretation is substrate-kinetic
rather than group-theoretic.

KEY RESULT (Route 3B, see equations/weinberg_angle_rg.py):
  The scale where α₁ = α₂ in SM running is M_c(12) ≈ 10^13 GeV.
  Starting with equal couplings at that scale gives sin²θ_W(M_Z) = 0.231 exactly.
  The product topology means only α₁ = α₂ at M_c is required (D5/D6 share a
  bifurcation stage); α₃ (D7) need not meet at the same scale.

SIGN CONVENTION (this module):
  d(α_i⁻¹)/d(ln μ) = B_i/(2π)
  B1 = -41/10 (NEGATIVE), B2 = +19/6 (POSITIVE), B3 = +7 (POSITIVE)
  Running formula: 1/α(μ) = 1/α(M_Z) + (B_i/2π) × ln(μ/M_Z)
  Note: equations/weinberg_angle_rg.py uses the OPPOSITE sign convention
  (B1 = +41/10, B2 = -19/6) with the formula running DOWN (M_c to M_Z).
  Both give identical numerical results; the conventions differ.

DERIVATION STATUS:
- Running: SM one-loop beta functions with SM input couplings at M_Z.
  DFC contributes the interpretation of the high-energy meeting point.
- Pairwise crossings: descriptive analysis of SM running. The three
  couplings do NOT meet at a single point in the SM (expected given the
  product topology — only α₁ = α₂ is required by DFC's D5/D6 structure).
- squashing_correction(): PLACEHOLDER — the D6 S³ squashing correction
  to coupling running has not been derived. Returns None for all corrections.
- For the Weinberg angle derivation, see equations/weinberg_angle_rg.py.

Usage:
    python equations/gauge_couplings.py
"""

import math

# ─── Observed Couplings at M_Z ────────────────────────────────────────────────

MZ_GEV = 91.1876       # Z boson mass in GeV

# Standard Model couplings at μ = M_Z
# In the notation α_i = g_i² / (4π)
ALPHA_1_MZ = 0.01696   # U(1)_Y
ALPHA_2_MZ = 0.03375   # SU(2)_L
ALPHA_3_MZ = 0.1182    # SU(3)_c  (strong coupling constant α_s)

# One-loop beta function coefficients b_i = β₀ in the Standard Model
# d(α_i^-1)/d(ln μ) = b_i / (2π)
# SM values: b_1 = -41/10, b_2 = 19/6, b_3 = 7
B1_SM = -41.0 / 10.0   # U(1): negative → gets stronger at high energy
B2_SM =  19.0 / 6.0    # SU(2): positive → gets weaker at high energy
B3_SM =   7.0           # SU(3): positive → asymptotic freedom


def alpha_running(alpha_at_mz: float, b_coeff: float, mu_gev: float,
                   mu_ref_gev: float = MZ_GEV) -> float:
    """
    One-loop running of gauge coupling α(μ).

    1/α(μ) = 1/α(μ_ref) + (b / 2π) × ln(μ / μ_ref)

    Parameters
    ----------
    alpha_at_mz : float
        Coupling α = g² / (4π) at the reference scale.
    b_coeff : float
        One-loop beta function coefficient.
    mu_gev : float
        Target scale in GeV.
    mu_ref_gev : float
        Reference scale in GeV. Default: M_Z.

    Returns
    -------
    float : α(μ)
    """
    log_ratio = math.log(mu_gev / mu_ref_gev)
    inv_alpha_new = (1.0 / alpha_at_mz) + (b_coeff / (2 * math.pi)) * log_ratio
    if inv_alpha_new <= 0:
        return float('inf')
    return 1.0 / inv_alpha_new


def scan_couplings(log10_mu_range=(2, 19), n_points=34):
    """
    Scan the three SM coupling constants from M_Z up to M_Planck.

    Returns list of dicts with scale and coupling values.
    """
    log10_min, log10_max = log10_mu_range
    step = (log10_max - log10_min) / (n_points - 1)
    results = []

    for i in range(n_points):
        log10_mu = log10_min + i * step
        mu = 10**log10_mu

        a1 = alpha_running(ALPHA_1_MZ, B1_SM, mu)
        a2 = alpha_running(ALPHA_2_MZ, B2_SM, mu)
        a3 = alpha_running(ALPHA_3_MZ, B3_SM, mu)

        results.append({
            'mu_gev':      mu,
            'log10_mu':    log10_mu,
            'alpha_1':     a1,
            'alpha_2':     a2,
            'alpha_3':     a3,
            'inv_alpha_1': 1/a1 if a1 > 0 else None,
            'inv_alpha_2': 1/a2 if a2 > 0 else None,
            'inv_alpha_3': 1/a3 if a3 > 0 else None,
        })

    return results


def find_pairwise_crossings():
    """
    Find the energy scales where pairs of couplings meet.

    In the SM without new physics, the three couplings come close but do not
    exactly unify — they miss each other at high energy.

    With SUSY or with this model's squashing correction, the meeting can be
    improved. This function finds where each pair meets.
    """
    # Analytic crossing points (one-loop, SM)
    # α_1(μ) = α_2(μ) when:
    # 1/α_1_MZ + (b_1/2π) ln(μ/M_Z) = 1/α_2_MZ + (b_2/2π) ln(μ/M_Z)
    # Solving: ln(μ/M_Z) = (1/α_2 - 1/α_1) / ((b_1 - b_2)/2π)

    def crossing_log_mu(alpha_i, b_i, alpha_j, b_j):
        delta_inv = (1/alpha_j) - (1/alpha_i)
        delta_b = (b_i - b_j) / (2 * math.pi)
        if abs(delta_b) < 1e-10:
            return None
        return delta_inv / delta_b

    log_12 = crossing_log_mu(ALPHA_1_MZ, B1_SM, ALPHA_2_MZ, B2_SM)
    log_13 = crossing_log_mu(ALPHA_1_MZ, B1_SM, ALPHA_3_MZ, B3_SM)
    log_23 = crossing_log_mu(ALPHA_2_MZ, B2_SM, ALPHA_3_MZ, B3_SM)

    def to_gev(log_ratio):
        return MZ_GEV * math.exp(log_ratio) if log_ratio is not None else None

    mu_12 = to_gev(log_12)
    mu_13 = to_gev(log_13)
    mu_23 = to_gev(log_23)

    return {
        'alpha_1_meets_alpha_2_gev': mu_12,
        'alpha_1_meets_alpha_3_gev': mu_13,
        'alpha_2_meets_alpha_3_gev': mu_23,
        'log10_12': math.log10(mu_12) if mu_12 and mu_12 > 0 else None,
        'log10_13': math.log10(mu_13) if mu_13 and mu_13 > 0 else None,
        'log10_23': math.log10(mu_23) if mu_23 and mu_23 > 0 else None,
        'note': (
            "In the SM, the three couplings do not all meet at a single point. "
            "In DFC (product topology), this is expected: only α₁ = α₂ at M_c(12) "
            "is required (D5/D6 share a bifurcation stage). Route 3B shows that "
            "equal α₁, α₂ at M_c(12) ≈ 10^13 GeV reproduces sin²θ_W = 0.231 "
            "without a unified gauge group. α₃ meets at a different scale "
            "(D7 is a separate bifurcation stage). "
            "See equations/weinberg_angle_rg.py for the full derivation."
        )
    }


def squashing_correction(epsilon, scale_gev):
    """
    Correction to coupling running from the squashing geometry.

    When the D6 closure geometry is squashed by parameter ε, the effective
    coupling constants receive corrections proportional to ε² at the
    bifurcation scale.

    This is a placeholder for the full calculation (in development).

    Parameters
    ----------
    epsilon : float
        Squashing parameter (0 = round S³, 1 = maximally deformed).
    scale_gev : float
        Scale at which to evaluate the correction.

    Returns
    -------
    dict with corrections to each coupling.
    """
    # Schematic: δ(1/α_i) ~ c_i × ε² × ln(M_bif / scale)
    # The coefficients c_i depend on the specific D6 closure geometry.
    # To be derived from the full geometric calculation.
    return {
        'epsilon': epsilon,
        'scale_gev': scale_gev,
        'delta_inv_alpha_1': None,  # TBD from geometry
        'delta_inv_alpha_2': None,  # TBD from geometry
        'delta_inv_alpha_3': None,  # TBD from geometry
        'status': 'PLACEHOLDER — geometric derivation pending',
    }


# ─── Main Output ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("GAUGE COUPLING RUNNING")
    print("Dimensional Folding Model")
    print("=" * 65)

    print(f"\n--- Input Couplings at M_Z = {MZ_GEV} GeV ---")
    print(f"  α₁ (U(1)):   {ALPHA_1_MZ:.5f}  →  1/α₁ = {1/ALPHA_1_MZ:.2f}")
    print(f"  α₂ (SU(2)):  {ALPHA_2_MZ:.5f}  →  1/α₂ = {1/ALPHA_2_MZ:.2f}")
    print(f"  α₃ (SU(3)):  {ALPHA_3_MZ:.5f}  →  1/α₃ = {1/ALPHA_3_MZ:.2f}")

    print(f"\n--- Coupling Running (selected scales) ---")
    print(f"  {'Scale (GeV)':>14}  {'log10(μ)':>9}  {'1/α₁':>8}  {'1/α₂':>8}  {'1/α₃':>8}")
    print(f"  {'-'*14}  {'-'*9}  {'-'*8}  {'-'*8}  {'-'*8}")

    interesting_scales = [
        MZ_GEV, 1e3, 1e6, 1e9, 1e12, 1e14, 1e16, 1e17, 1e18, 1e19
    ]
    for mu in interesting_scales:
        a1 = alpha_running(ALPHA_1_MZ, B1_SM, mu)
        a2 = alpha_running(ALPHA_2_MZ, B2_SM, mu)
        a3 = alpha_running(ALPHA_3_MZ, B3_SM, mu)
        print(f"  {mu:14.2e}  {math.log10(mu):9.1f}  {1/a1:8.2f}  {1/a2:8.2f}  {1/a3:8.2f}")

    print(f"\n--- Pairwise Crossing Points (SM, one-loop) ---")
    crossings = find_pairwise_crossings()
    for pair, mu_val in [
        ('α₁ ∩ α₂', crossings['alpha_1_meets_alpha_2_gev']),
        ('α₁ ∩ α₃', crossings['alpha_1_meets_alpha_3_gev']),
        ('α₂ ∩ α₃', crossings['alpha_2_meets_alpha_3_gev']),
    ]:
        if mu_val:
            print(f"  {pair}:  μ = {mu_val:.2e} GeV  (log10 = {math.log10(abs(mu_val)):.1f})")
        else:
            print(f"  {pair}:  no crossing")

    print(f"\n  {crossings['note']}")
    print(f"\n  DFC (Route 3B): α₁ = α₂ at M_c(12) ≈ 10^13 GeV is the relevant condition.")
    print(f"  Product topology: α₃ need not meet at the same scale (D7 = separate stage).")
    print(f"  See equations/weinberg_angle_rg.py for sin²θ_W = 0.231 derivation.")
