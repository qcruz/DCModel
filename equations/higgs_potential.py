"""
Higgs potential from S³ fiber geometry.

In the Dimensional Folding Model, the Higgs field is the squashing parameter ε of the
weak-force S³ fiber. The Mexican hat potential emerges from:
  - Negative mass term: pressure from the squashed SU(3) fiber (destabilizer)
  - Quartic term: intrinsic curvature of S³ resisting deformation (stabilizer)

The Higgs mass derivation separates two regimes:
  Above the closure scale M_c: geometric — the quartic is suppressed to ~0.013 by the
    gauge-Higgs unification structure (Higgs as metric modulus, protected by symmetry)
  Below M_c: field-theoretic — top quark loops radiatively generate λ(v) ≈ 0.129

Result: m_H = 125.1 ± 1.5 GeV  (observed: 125.25 ± 0.17 GeV)

The tree-level estimate (~91 GeV) was incorrect because it used λ_tree directly as the
physical quartic without RG evolution. See foundations/higgs_mass_derivation.md.

DERIVATION STATUS (important):
  - m_H prediction: semi-genuine. DFC identifies M_c with M_Planck and assigns the
    S³ geometry as the origin of λ₀ ≈ 0.013. But λ₀ = 0.013 is itself taken from the
    SM vacuum stability analysis (Buttazzo et al. 2013) — it is the value of λ at M_Pl
    for which SM RG evolution yields m_H ≈ 125 GeV. This is a consistency identification,
    not an ab initio derivation. The RG running (Δλ = 0.116) is also SM-derived.

  - W and Z masses: SM formulas m_W = (1/2)g₂v, m_Z = m_W/cos(θ_W) with SM inputs
    for g₂ and sin²θ_W. These verify that DFC reproduces SM relationships, but are
    not independent DFC predictions.

  - Weinberg angle: NOT derived from DFC geometry. The main() section reverse-engineers
    the required ratio from the observed sin²θ_W. The formula tan(θ_W) ≈ r_S³/r_U1 is
    schematic with the exact relation TBD (see weinberg_angle_from_fibers docstring).

  - Vacuum stability: the simplified top-only beta function in vacuum_stability() gives
    a stability scale ~10^3.8 GeV, inconsistent with the actual SM result (~10^9 GeV)
    and the claimed DFC scale M_c ~ 10^18 GeV. This function is a placeholder.

Usage:
    python equations/higgs_potential.py

    Or import:
        from equations.higgs_potential import potential, rg_improved_higgs_mass
"""

import math

# Local copies of the constants we need (avoid circular import)
HIGGS_VEV_MEV = 246220.0    # MeV
M_TOP_MEV     = 172760.0    # MeV
M_W_MEV       = 80377.0     # MeV
M_Z_MEV       = 91187.6     # MeV
M_H_OBS_MEV   = 125200.0    # MeV  (observed Higgs mass)
YUKAWA_TOP    = math.sqrt(2) * M_TOP_MEV / HIGGS_VEV_MEV   # ≈ 0.995
G2            = 0.6514       # SU(2) coupling at M_Z


# ─── Tree-Level Geometric Potential ──────────────────────────────────────────

def potential(epsilon, mu_sq, lam):
    """
    The Mexican hat potential V(ε) = -μ² ε² + λ ε⁴

    In the geometric picture, ε is the squashing parameter of the S³ weak fiber.
    This is NOT a conventional Higgs field potential — ε is dimensionless.
    The potential energy is in units where the electroweak scale sets the normalization.

    Parameters
    ----------
    epsilon : float
        Squashing parameter of S³ fiber (dimensionless). ε=0 is the unbroken phase.
    mu_sq : float
        Effective mass-squared parameter (MeV²). Positive = unstable at ε=0.
    lam : float
        Quartic self-coupling (dimensionless). Must be positive for stability.

    Returns
    -------
    float
        Potential energy V(ε) in MeV²  (unnormalized)
    """
    return -mu_sq * epsilon**2 + lam * epsilon**4


def vev_from_params(mu_sq, lam):
    """
    Compute the vacuum expectation value ε₀ = √(μ²/2λ).

    This is the value of ε at the minimum of V(ε).
    """
    return math.sqrt(mu_sq / (2 * lam))


def tree_level_higgs_mass(mu_sq, lam):
    """
    Tree-level Higgs mass from the potential curvature at the minimum.

    m²_H,tree = 2μ² = 4λ v²    (where v = ε₀ × [electroweak normalization])

    In this model, the geometric quartic λ is near zero at tree level (protected
    by moduli symmetry), so the tree-level mass is nearly zero. The physical mass
    comes from radiative corrections.
    """
    epsilon_0 = vev_from_params(mu_sq, lam)
    # Second derivative of V at minimum = 4 λ ε₀² = 2 μ²  (in potential units)
    return math.sqrt(2 * mu_sq)


# ─── Radiative Higgs Mass (Top Quark Dominated) ───────────────────────────────

def higgs_mass_radiative(
    m_top_mev=M_TOP_MEV,
    m_closure_gev=1.0e16,
    g2=G2,
    vev_mev=HIGGS_VEV_MEV,
):
    """
    Simple one-loop radiative Higgs mass estimate (leading top quark contribution).

    Uses λ_tree ≈ 0 at the closure scale (protected by moduli symmetry) and
    generates the effective quartic purely from the top loop. This is superseded
    by rg_improved_higgs_mass() for quantitative comparison with observation.

    Parameters
    ----------
    m_top_mev : float
        Top quark mass in MeV. Default: PDG value 172,760 MeV.
    m_closure_gev : float
        Closure scale in GeV. Default: 10^16 GeV.
    g2 : float
        SU(2) gauge coupling.
    vev_mev : float
        Higgs vev in MeV. Default: 246,220 MeV.

    Returns
    -------
    dict with keys:
        'lambda_eff'   : effective quartic coupling at electroweak scale
        'm_higgs_mev'  : predicted Higgs mass in MeV
        'm_higgs_gev'  : predicted Higgs mass in GeV
        'observed_gev' : observed value for comparison
        'ratio'        : predicted / observed
    """
    y_top = math.sqrt(2) * m_top_mev / vev_mev

    m_closure_mev = m_closure_gev * 1000.0
    log_ratio = math.log(m_closure_mev / m_top_mev)

    lambda_top = (3 * y_top**4) / (8 * math.pi**2) * log_ratio
    lambda_gauge = -(3 * g2**4) / (64 * math.pi**2) * log_ratio
    lambda_eff = lambda_top + lambda_gauge

    m_higgs_sq = 2 * lambda_eff * vev_mev**2
    if m_higgs_sq < 0:
        m_higgs_mev = None
    else:
        m_higgs_mev = math.sqrt(m_higgs_sq)

    return {
        'lambda_top':    lambda_top,
        'lambda_gauge':  lambda_gauge,
        'lambda_eff':    lambda_eff,
        'm_higgs_mev':   m_higgs_mev,
        'm_higgs_gev':   m_higgs_mev / 1000.0 if m_higgs_mev else None,
        'observed_gev':  125.25,
        'ratio':         (m_higgs_mev / 125250.0) if m_higgs_mev else None,
    }


def rg_improved_higgs_mass(
    m_top_gev=172.76,
    lambda_0=0.013,
    lambda_0_uncertainty=0.007,
    vev_gev=246.22,
):
    """
    RG-improved Higgs mass prediction from geometric boundary conditions.

    Implements the two-regime derivation from foundations/higgs_mass_derivation.md:

    Regime 1 (above M_c): geometric description.
      The Higgs quartic at the closure scale is suppressed by gauge-Higgs unification:
      λ₀ = λ_tree(M_c) ≈ 0.013, from the SM vacuum stability analysis.

    Regime 2 (below M_c): field-theoretic RG evolution.
      Top quark loops drive λ from λ₀ ≈ 0.013 up to λ(v) ≈ 0.129.
      Using SM RG results from Buttazzo et al. (2013), Degrassi et al. (2012).

    The quartic runs according to the one-loop beta function (top-dominated):
      dλ/d(ln μ) ≈ (1/16π²)[24λ² + 12y_t²λ − 12y_t⁴]

    We use the well-known SM numerical result: running from M_c ≈ 10^18 GeV
    down to v = 246 GeV with λ(M_c) ≈ 0.013 yields λ(v) ≈ 0.129.

    Parameters
    ----------
    m_top_gev : float
        Top quark mass in GeV. Default: 172.76 GeV (PDG).
    lambda_0 : float
        Tree-level geometric quartic at the closure scale. Default: 0.013
        (center of the SM-running consistency interval [0.006, 0.020]).
    lambda_0_uncertainty : float
        Uncertainty on the geometric boundary condition. Default: 0.007.
    vev_gev : float
        Higgs vev in GeV. Default: 246.22 GeV.

    Returns
    -------
    dict with full results and uncertainty breakdown.
    """
    # Top Yukawa at the electroweak scale
    y_top = math.sqrt(2) * m_top_gev / vev_gev

    # RG running from closure scale to electroweak scale.
    # The SM running is computed numerically by Buttazzo et al. (2013).
    # Key result: for m_t = 173 GeV, running from M_c ~ 10^18 GeV to v
    # with λ(M_c) = 0.013 gives λ(v) ≈ 0.129.
    #
    # We parametrize the RG amplification as:
    #   λ(v) ≈ λ_0 + Δλ_top + Δλ_gauge
    # where Δλ_top is the top loop contribution over the full running range.
    #
    # From SM vacuum stability analyses:
    #   λ(M_Pl) ≈ 0.013 for m_H = 125.25 GeV, m_t = 173.0 GeV
    #   Running from M_c = 10^18 GeV to M_Pl changes λ by < 0.002
    #   Running from v to M_c: Δλ ≈ -0.116 (dominated by top loop)
    # Therefore λ(v) = λ(M_c) + 0.116 ≈ 0.013 + 0.116 = 0.129

    # Top mass sensitivity: δλ(M_Pl)/δm_t ≈ -0.006/GeV (Buttazzo et al.)
    # So δλ(v)/δm_t ≈ +0.006/GeV
    delta_top_gev = m_top_gev - 173.0
    delta_lambda_from_top = 0.006 * delta_top_gev

    # Central RG contribution (SM-derived, top-dominated)
    delta_lambda_rg = 0.116 + delta_lambda_from_top

    lambda_v = lambda_0 + delta_lambda_rg

    # Higgs mass
    m_h_gev = math.sqrt(2 * lambda_v) * vev_gev

    # Uncertainty propagation
    # δm_H from top mass uncertainty (±0.4 GeV → ±1.2 GeV in m_H)
    sigma_top = 1.2  # GeV
    # δm_H from α_s uncertainty
    sigma_alphas = 0.6  # GeV
    # δm_H from geometric boundary condition λ₀ uncertainty
    # δm_H ≈ (v / √(2λ_v)) × δλ = (m_H / (2λ_v)) × δλ
    sigma_geom = (m_h_gev / (2 * lambda_v)) * lambda_0_uncertainty
    # Two-loop matching
    sigma_twoloop = 0.3  # GeV

    sigma_total = math.sqrt(sigma_top**2 + sigma_alphas**2
                            + sigma_geom**2 + sigma_twoloop**2)

    return {
        'lambda_0':              lambda_0,
        'delta_lambda_rg':       delta_lambda_rg,
        'lambda_v':              lambda_v,
        'm_H_gev':               m_h_gev,
        'm_H_observed_gev':      125.25,
        'residual_gev':          m_h_gev - 125.25,
        'sigma_top_gev':         sigma_top,
        'sigma_alphas_gev':      sigma_alphas,
        'sigma_geom_gev':        sigma_geom,
        'sigma_twoloop_gev':     sigma_twoloop,
        'sigma_total_gev':       sigma_total,
        'within_1sigma':         abs(m_h_gev - 125.25) < sigma_total,
        'note': ('RG-improved prediction. Dominant uncertainty: top quark mass. '
                 'See foundations/higgs_mass_derivation.md.'),
    }


# ─── W and Z Masses from Fiber Geometry ──────────────────────────────────────

def gauge_boson_masses(vev_mev=HIGGS_VEV_MEV, g2=G2, sin2_weinberg=0.23122):
    """
    Predict W and Z boson masses from the S³ fiber squashing.

    When the S³ is squashed (ε ≠ 0), rotations perpendicular to the squashing
    axis acquire mass. The photon remains massless (rotation along squashing axis).

    m_W = (1/2) g₂ v
    m_Z = m_W / cos(θ_W)

    Parameters
    ----------
    vev_mev : float
        Higgs vev in MeV.
    g2 : float
        SU(2) gauge coupling.
    sin2_weinberg : float
        sin²(θ_W), the electroweak mixing angle.

    Returns
    -------
    dict with predicted and observed masses in MeV.
    """
    cos_weinberg = math.sqrt(1 - sin2_weinberg)

    m_w_pred = 0.5 * g2 * vev_mev
    m_z_pred = m_w_pred / cos_weinberg

    return {
        'm_W_predicted_mev': m_w_pred,
        'm_W_observed_mev':  80377.0,
        'm_W_ratio':         m_w_pred / 80377.0,

        'm_Z_predicted_mev': m_z_pred,
        'm_Z_observed_mev':  91187.6,
        'm_Z_ratio':         m_z_pred / 91187.6,

        'rho_parameter':     (m_w_pred / (m_z_pred * cos_weinberg))**2,
        # ρ = 1 in the Standard Model (custodial symmetry of S³)
    }


# ─── Weinberg Angle from Fiber Geometry ──────────────────────────────────────

def weinberg_angle_from_fibers(r_u1, r_s3):
    """
    Predict the Weinberg angle from the ratio of fiber radii.

    In the product geometry, the mixing between the U(1) and SU(2) forces is
    determined by the relative sizes of their fibers. The Weinberg angle is the
    geometric mixing angle between the two fiber spaces.

    tan(θ_W) ≈ g₁/g₂ ≈ R_S3 / R_U1  (schematic — exact relation TBD)

    NOTE: The main() section does NOT derive r_S3/r_U1 from DFC geometry. It
    reverse-engineers the required ratio from the observed sin²θ_W = 0.23122.
    This function is a forward map (ratio → angle); the inverse map is what
    main() uses. The Weinberg angle is a known correspondence, not a DFC prediction.

    Parameters
    ----------
    r_u1 : float
        Radius of U(1) electromagnetic circle (any units).
    r_s3 : float
        Radius of S³ weak force sphere (same units).

    Returns
    -------
    dict with predicted Weinberg angle.
    """
    tan_theta = r_s3 / r_u1
    theta = math.atan(tan_theta)
    sin2_theta = math.sin(theta)**2

    return {
        'tan_weinberg': tan_theta,
        'theta_rad':    theta,
        'theta_deg':    math.degrees(theta),
        'sin2_weinberg_predicted': sin2_theta,
        'sin2_weinberg_observed':  0.23122,
        'ratio': sin2_theta / 0.23122,
    }


# ─── Vacuum Stability Check ───────────────────────────────────────────────────

def vacuum_stability(
    m_top_mev=M_TOP_MEV,
    m_higgs_mev=M_H_OBS_MEV,
    vev_mev=HIGGS_VEV_MEV,
):
    """
    Check where the effective Higgs quartic coupling crosses zero (vacuum stability boundary).

    In this model, the quartic crossing zero corresponds to the closure scale —
    this is a prediction: the stability boundary should coincide with M_c.

    Returns the scale (in GeV) where the effective quartic runs to zero.

    NOTE: This implementation uses a simplified one-loop beta function keeping
    only the top quark contribution (β ≈ -3y_t⁴/8π²). This omits the positive
    gauge boson contributions that partially cancel the top loop. As a result,
    this function underestimates the stability scale by several orders of magnitude.
    The full SM calculation (Buttazzo et al. 2013) gives ~10^9-10^10 GeV.
    This function is a placeholder and its output should not be used as a DFC
    prediction until the full RG running is implemented.
    """
    # Initial quartic from observed Higgs mass
    lambda_0 = (m_higgs_mev**2) / (2 * vev_mev**2)

    y_top = math.sqrt(2) * m_top_mev / vev_mev

    # One-loop beta function coefficient for λ (top quark dominates)
    # dλ/d(ln μ) ≈ (1/16π²) × [24λ² - 6y_t⁴ + ...]
    # Simplified: when top loops dominate at high scale
    # λ(μ) ≈ λ_0 - (3 y_t⁴)/(8π²) × ln(μ/m_t)

    # Find scale where λ = 0
    # 0 = λ_0 - (3 y_t⁴)/(8π²) × ln(μ/m_t)
    beta_top = (3 * y_top**4) / (8 * math.pi**2)
    log_ratio = lambda_0 / beta_top
    m_stability_mev = M_TOP_MEV * math.exp(log_ratio)
    m_stability_gev = m_stability_mev / 1000.0

    return {
        'lambda_at_mz':          lambda_0,
        'stability_scale_gev':   m_stability_gev,
        'stability_scale_log10': math.log10(m_stability_gev),
        'model_prediction':      'M_c should coincide with stability scale',
        'note':                  'If M_c ~ 10^16 GeV, check log10 ~ 16',
    }


# ─── Main Output ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("HIGGS POTENTIAL — GEOMETRIC DERIVATION")
    print("Dimensional Folding Model")
    print("=" * 60)

    print("\n--- RG-Improved Higgs Mass (Primary Result) ---")
    rg = rg_improved_higgs_mass()
    print(f"  Geometric boundary λ₀:      {rg['lambda_0']:.3f}")
    print(f"  RG running Δλ (M_c → v):   {rg['delta_lambda_rg']:.3f}")
    print(f"  Physical quartic λ(v):      {rg['lambda_v']:.4f}")
    print(f"  Predicted m_H:              {rg['m_H_gev']:.1f} ± {rg['sigma_total_gev']:.1f} GeV")
    print(f"  Observed m_H:               {rg['m_H_observed_gev']:.2f} GeV")
    print(f"  Residual:                   {rg['residual_gev']:+.2f} GeV")
    print(f"  Within 1σ:                  {rg['within_1sigma']}")
    print(f"  NOTE: uncertainty dominated by σ_geom = {rg['sigma_geom_gev']:.1f} GeV (λ₀ not derived).")
    print(f"  higgs_mass_derivation.md quotes 125.1 GeV using m_t=173.0 GeV (Buttazzo ref).")
    print(f"  This code uses PDG m_t=172.76 GeV, giving 124.4 GeV. Both within uncertainty.")

    print("\n--- Simple One-Loop Estimate (for comparison — NOT physically meaningful) ---")
    result = higgs_mass_radiative(m_closure_gev=1.0e18)
    print(f"  Top Yukawa y_t:             {math.sqrt(2)*M_TOP_MEV/HIGGS_VEV_MEV:.4f}")
    print(f"  λ_top:                      {result['lambda_top']:.4f}")
    print(f"  λ_gauge:                    {result['lambda_gauge']:.4f}")
    print(f"  λ_eff:                      {result['lambda_eff']:.4f}")
    print(f"  m_H (one-loop):             {result['m_higgs_gev']:.1f} GeV")
    print(f"  WARNING: 397.9 GeV is not physical. This formula runs λ from 0 at M_c")
    print(f"  to v with only top/gauge loops — it is not the RG-improved derivation.")
    print(f"  The correct derivation is the RG-improved result above (use rg_improved_higgs_mass).")

    print("\n--- W and Z Masses from S³ Fiber Squashing ---")
    masses = gauge_boson_masses()
    print(f"  m_W  predicted:  {masses['m_W_predicted_mev']/1000:.2f} GeV   "
          f"observed: {masses['m_W_observed_mev']/1000:.3f} GeV   "
          f"ratio: {masses['m_W_ratio']:.4f}")
    print(f"  m_Z  predicted:  {masses['m_Z_predicted_mev']/1000:.2f} GeV   "
          f"observed: {masses['m_Z_observed_mev']/1000:.3f} GeV   "
          f"ratio: {masses['m_Z_ratio']:.4f}")
    print(f"  ρ parameter:     {masses['rho_parameter']:.4f}  (expected: 1.0000)")

    print("\n--- Weinberg Angle (correspondence, not derivation) ---")
    target_sin2 = 0.23122
    target_theta = math.asin(math.sqrt(target_sin2))
    required_ratio = math.tan(target_theta)
    print(f"  NOTE: r_S3/r_U1 ratio is REVERSE-ENGINEERED from observed sin²θ_W.")
    print(f"  Required r_S3/r_U1 ratio:   {required_ratio:.4f}  [fitted to data]")
    print(f"  Gives sin²θ_W:              {target_sin2}  [input, not output]")
    w = weinberg_angle_from_fibers(1.0, required_ratio)
    print(f"  Verification sin²θ_W:       {w['sin2_weinberg_predicted']:.5f}  [circular]")
    print(f"  Status: tan(θ_W) ≈ r_S3/r_U1 is schematic — exact DFC derivation TBD.")

    print("\n--- Vacuum Stability Boundary ---")
    stab = vacuum_stability()
    print(f"  Stability scale (simplified formula): 10^{stab['stability_scale_log10']:.1f} GeV")
    print(f"  NOTE: This uses top-only beta function — underestimates scale by ~6 orders.")
    print(f"  Full SM result (Buttazzo et al.): ~10^9 GeV.  DFC claim: M_c ~ 10^18 GeV.")
    print(f"  Status: placeholder — not a reliable DFC prediction.")
