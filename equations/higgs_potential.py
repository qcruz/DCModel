"""
Higgs potential from S³ fiber geometry.

In the Dimensional Folding Model, the Higgs field is the squashing parameter ε of the
weak-force S³ fiber. The Mexican hat potential emerges from:
  - Negative mass term: pressure from the squashed SU(3) fiber (destabilizer)
  - Quartic term: intrinsic curvature of S³ resisting deformation (stabilizer)

The observed Higgs boson mass (125 GeV) comes primarily from radiative corrections,
with the top quark loop providing the dominant contribution.

Usage:
    python equations/higgs_potential.py

    Or import:
        from equations.higgs_potential import potential, higgs_mass_radiative
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
    m_compactification_gev=1.0e16,
    g2=G2,
    vev_mev=HIGGS_VEV_MEV,
):
    """
    Estimate the physical Higgs mass from one-loop radiative corrections.

    The leading contribution is from the top quark loop. The geometric quartic
    coupling λ_tree ≈ 0 at the compactification scale (protected by moduli symmetry).

    The effective quartic at the electroweak scale:

        λ_eff ≈ (3 y_t⁴ / 8π²) × ln(M_c / m_t)

    And the physical Higgs mass:

        m_H² ≈ 2 λ_eff v²

    Parameters
    ----------
    m_top_mev : float
        Top quark mass in MeV. Default: PDG value 172,760 MeV.
    m_compactification_gev : float
        Compactification scale in GeV. Default: 10^16 GeV (estimate).
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

    # log(M_c / m_t) — ratio of compactification scale to top mass
    m_compactification_mev = m_compactification_gev * 1000.0
    log_ratio = math.log(m_compactification_mev / m_top_mev)

    # Leading top-quark contribution to effective quartic
    # (3-color × 4-component loop factor × Yukawa⁴)
    lambda_top = (3 * y_top**4) / (8 * math.pi**2) * log_ratio

    # W, Z, and Higgs loop corrections (smaller, stabilizing)
    lambda_gauge = -(3 * g2**4) / (64 * math.pi**2) * log_ratio

    lambda_eff = lambda_top + lambda_gauge

    # Physical Higgs mass
    m_higgs_sq = 2 * lambda_eff * vev_mev**2
    if m_higgs_sq < 0:
        m_higgs_mev = None  # vacuum instability signal
    else:
        m_higgs_mev = math.sqrt(m_higgs_sq)

    return {
        'lambda_top':    lambda_top,
        'lambda_gauge':  lambda_gauge,
        'lambda_eff':    lambda_eff,
        'm_higgs_mev':   m_higgs_mev,
        'm_higgs_gev':   m_higgs_mev / 1000.0 if m_higgs_mev else None,
        'observed_gev':  125.2,
        'ratio':         (m_higgs_mev / 125200.0) if m_higgs_mev else None,
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

    In this model, the quartic crossing zero corresponds to the compactification scale —
    this is a prediction: the stability boundary should coincide with M_c.

    Returns the scale (in GeV) where the effective quartic runs to zero.
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

    print("\n--- Radiative Higgs Mass (Top Quark Loop) ---")
    result = higgs_mass_radiative()
    print(f"  Top Yukawa coupling y_t:    {math.sqrt(2)*M_TOP_MEV/HIGGS_VEV_MEV:.4f}")
    print(f"  λ_top (top quark):          {result['lambda_top']:.4f}")
    print(f"  λ_gauge (W,Z loops):        {result['lambda_gauge']:.4f}")
    print(f"  λ_eff (net quartic):        {result['lambda_eff']:.4f}")
    print(f"  Predicted m_H:              {result['m_higgs_gev']:.1f} GeV")
    print(f"  Observed m_H:               {result['observed_gev']:.1f} GeV")
    print(f"  Ratio (pred/obs):           {result['ratio']:.3f}")

    print("\n--- W and Z Masses from S³ Fiber Squashing ---")
    masses = gauge_boson_masses()
    print(f"  m_W  predicted:  {masses['m_W_predicted_mev']/1000:.2f} GeV   "
          f"observed: {masses['m_W_observed_mev']/1000:.3f} GeV   "
          f"ratio: {masses['m_W_ratio']:.4f}")
    print(f"  m_Z  predicted:  {masses['m_Z_predicted_mev']/1000:.2f} GeV   "
          f"observed: {masses['m_Z_observed_mev']/1000:.3f} GeV   "
          f"ratio: {masses['m_Z_ratio']:.4f}")
    print(f"  ρ parameter:     {masses['rho_parameter']:.4f}  (expected: 1.0000)")

    print("\n--- Weinberg Angle from Fiber Radii Ratio ---")
    # If r_S3 / r_U1 gives the correct Weinberg angle:
    target_sin2 = 0.23122
    target_theta = math.asin(math.sqrt(target_sin2))
    required_ratio = math.tan(target_theta)
    print(f"  Required r_S3/r_U1 ratio:   {required_ratio:.4f}")
    print(f"  Gives sin²θ_W:              {target_sin2}")
    w = weinberg_angle_from_fibers(1.0, required_ratio)
    print(f"  Verification sin²θ_W:       {w['sin2_weinberg_predicted']:.5f}")

    print("\n--- Vacuum Stability Boundary ---")
    stab = vacuum_stability()
    print(f"  Stability scale:            10^{stab['stability_scale_log10']:.1f} GeV")
    print(f"  Model prediction:           M_c (compactification) ~ 10^16 GeV")
    print(f"  {stab['model_prediction']}")
