"""
Quark-Gluon Plasma Phase Transition — DFC Stub Module
=======================================================

Physical question:
    At what temperature does nuclear matter undergo the deconfinement phase transition
    from a hadron gas (bound D7 quark closures) to a quark-gluon plasma (free D7 modes),
    and what does DFC predict for this transition?

DFC mechanism:
    In DFC, quark confinement is the D7 SU(3) closure behavior — quarks are D7 kink
    configurations that cannot propagate independently because the D7 substrate produces
    a linearly rising potential between separated color charges (the confining string).
    Color confinement is the statement that only color-singlet (D7 winding-zero) composite
    configurations can exist as isolated particles.

    The deconfinement transition (QGP phase transition) occurs when the thermal energy
    k_B T becomes comparable to the string tension energy per unit length times the
    hadron size. Above T_c, the D7 substrate configuration loses its long-range confining
    structure: individual D7 kinks (quarks) become free to propagate over distances larger
    than the hadron scale.

    In DFC language: below T_c, the D7 substrate at long wavelengths is in the confining
    phase (the D7 field has no propagating massless modes — gluons are confined). Above T_c,
    the D7 field restores a propagating-mode phase — quarks and gluons become free.
    This is a phase transition in the D7 substrate configuration, analogous to the
    electroweak crossover at D6 depths (see phenomena/particle_physics/forces/phase_transitions.md).

    DFC-specific prediction: the deconfinement temperature T_c is set by the D7 closure scale.
    The DFC value for M_c(D7) is not yet derived from the substrate (α_s error = 11%),
    so T_c cannot yet be predicted from first principles.

Key data (from lattice QCD):
    T_c ≈ 154 ± 9 MeV    (crossover temperature for deconfinement; Aoki et al. 2006)
    Above T_c: quark-gluon plasma observed at CERN-SPS, RHIC, LHC
    QGP quark-number susceptibility rises sharply near T_c
    Chiral symmetry (quark mass → 0) approximately restores near T_c

Status:
    STUB — T_c is not yet derived from DFC substrate parameters.
    Primary blockage: α_s(M_Z) = 0.105 (DFC) vs 0.118 (observed): 11% error.
    M_c(D7) ~ 8×10¹⁴ GeV is from equal-coupling running (depth_running.md), not
    from substrate dynamics. Connecting M_c(D7) to T_c requires the running of α_s
    from M_c(D7) down to the hadronic scale — a 15-order-of-magnitude extrapolation.

Key references:
    - Aoki et al. (2006): T_c ≈ 154 MeV from lattice QCD
    - phenomena/particle_physics/forces/phase_transitions.md — DFC account of QCD confinement
    - equations/coupling_derivation.py — α_s(M_Z) from DFC (11% error)
    - equations/depth_running.py — M_c(D7) from equal-coupling running
"""

import math

# ─── Observed values ───────────────────────────────────────────────────────────

T_C_OBSERVED_MEV = 154.0       # Deconfinement temperature (MeV); lattice QCD
T_C_UNCERTAINTY_MEV = 9.0      # Uncertainty (MeV)
SIGMA_STRING_MEV_FM = 170.0    # QCD string tension (MeV/fm ~ 0.18 GeV²); empirical

# ─── DFC inputs ───────────────────────────────────────────────────────────────

ALPHA_S_DFC_MZ = 0.105         # DFC α_s at M_Z (11% below observed 0.1182)
ALPHA_S_OBS_MZ = 0.1182        # Observed α_s at M_Z
M_C_D7_GEV = 8.0e14           # DFC M_c(D7) from equal-coupling running (depth_running.md)
LAMBDA_QCD_MEV = 217.0         # QCD scale Λ_MS-bar (5 flavors, empirical; MeV)

# ─── QCD running coupling ─────────────────────────────────────────────────────

def alpha_s_running(mu_gev, alpha_s_ref, mu_ref_gev=91.1876, n_f=5):
    """
    One-loop running of α_s from reference scale μ_ref to scale μ.
    α_s(μ) = α_s(μ_ref) / (1 + b₀ α_s(μ_ref) ln(μ²/μ_ref²))

    The strong coupling decreases at higher energies (asymptotic freedom) and grows
    at lower energies, eventually becoming of order 1 at the QCD scale Λ_QCD.

    b₀ = (11 - 2n_f/3) / (2π)    (one-loop beta function coefficient)

    Args:
        mu_gev: target scale (GeV)
        alpha_s_ref: reference coupling at mu_ref
        mu_ref_gev: reference scale (default: M_Z = 91.2 GeV)
        n_f: number of active quark flavors at scale mu

    Returns:
        float: α_s at scale mu
    """
    b0 = (11.0 - 2.0 * n_f / 3.0) / (2.0 * math.pi)
    log_ratio = 2.0 * math.log(mu_gev / mu_ref_gev)
    denom = 1.0 + b0 * alpha_s_ref * log_ratio
    if denom <= 0.0:
        return None   # Landau pole — one-loop formula breaks down; non-perturbative regime
    alpha_mu = alpha_s_ref / denom
    if alpha_mu > 1.0:
        return None   # Strong coupling O(1) — perturbative expansion not reliable
    return alpha_mu


def estimate_t_c_from_lambda_qcd(lambda_qcd_mev):
    """
    Rough estimate of deconfinement temperature from QCD scale.
    Empirical relationship: T_c ≈ Λ_QCD × factor (factor ≈ 0.6-0.7 from lattice)

    Args:
        lambda_qcd_mev: QCD scale in MeV

    Returns:
        float: Estimated T_c in MeV
    """
    # Empirical ratio T_c / Λ_QCD ≈ 0.63 from lattice QCD
    RATIO_TC_LAMBDA = 0.63
    return RATIO_TC_LAMBDA * lambda_qcd_mev


def lambda_qcd_from_alpha_s(alpha_s_mz, mu_ref_gev=91.1876, n_f=5):
    """
    Infer Λ_QCD from α_s(M_Z) using one-loop running.
    Λ_QCD is defined as the scale at which one-loop α_s diverges.

    Args:
        alpha_s_mz: strong coupling at M_Z
        mu_ref_gev: M_Z in GeV
        n_f: active flavors at M_Z scale

    Returns:
        float: Λ_QCD in GeV
    """
    b0 = (11.0 - 2.0 * n_f / 3.0) / (2.0 * math.pi)
    # One-loop Λ: Λ = μ_ref × exp(−1 / (2 b₀ α_s))
    lambda_gev = mu_ref_gev * math.exp(-1.0 / (2.0 * b0 * alpha_s_mz))
    return lambda_gev


if __name__ == "__main__":
    print("=" * 66)
    print("Quark-Gluon Plasma Phase Transition — DFC Module (STUB)")
    print("=" * 66)
    print()
    print("STATUS: STUB — T_c not derived from DFC substrate.")
    print("        Primary blockage: α_s error 11%; M_c(D7) not from substrate.")
    print()

    # DFC α_s error
    alpha_err = 100.0 * (ALPHA_S_DFC_MZ - ALPHA_S_OBS_MZ) / ALPHA_S_OBS_MZ
    print(f"DFC α_s(M_Z):   {ALPHA_S_DFC_MZ:.4f}  (observed: {ALPHA_S_OBS_MZ:.4f},  error: {alpha_err:.1f}%)")
    print()

    # Λ_QCD from DFC α_s vs observed α_s
    lambda_dfc = lambda_qcd_from_alpha_s(ALPHA_S_DFC_MZ) * 1000   # convert to MeV
    lambda_obs = lambda_qcd_from_alpha_s(ALPHA_S_OBS_MZ) * 1000
    print(f"Λ_QCD from DFC α_s:       {lambda_dfc:.1f} MeV")
    print(f"Λ_QCD from observed α_s:  {lambda_obs:.1f} MeV")
    print(f"  (Empirical Λ_QCD^(5) ≈ 217 MeV)")
    print()

    # T_c estimate
    t_c_dfc = estimate_t_c_from_lambda_qcd(lambda_dfc)
    t_c_obs_est = estimate_t_c_from_lambda_qcd(lambda_obs)
    tc_err = 100.0 * (t_c_dfc - T_C_OBSERVED_MEV) / T_C_OBSERVED_MEV
    print(f"T_c estimate from DFC Λ_QCD:       {t_c_dfc:.1f} MeV")
    print(f"T_c estimate from observed Λ_QCD:  {t_c_obs_est:.1f} MeV")
    print(f"T_c observed (lattice QCD):        {T_C_OBSERVED_MEV:.1f} ± {T_C_UNCERTAINTY_MEV:.0f} MeV")
    print(f"DFC T_c error (from α_s error):    {tc_err:.1f}%")
    print()

    # α_s running from M_Z to hadronic scale
    print("α_s running from M_Z to hadronic scales (DFC vs observed):")
    print("  [None = past Landau pole or α_s > 1: one-loop formula breaks down]")
    for mu_gev, n_f_here in [(91.2, 5), (10.0, 5), (4.2, 4), (1.0, 3), (0.3, 3)]:
        a_dfc = alpha_s_running(mu_gev, ALPHA_S_DFC_MZ, n_f=n_f_here)
        a_obs = alpha_s_running(mu_gev, ALPHA_S_OBS_MZ, n_f=n_f_here)
        fmt_dfc = f"{a_dfc:.4f}" if a_dfc is not None else "NON-PERT"
        fmt_obs = f"{a_obs:.4f}" if a_obs is not None else "NON-PERT"
        print(f"  μ = {mu_gev:5.1f} GeV (n_f={n_f_here}):  α_s(DFC) = {fmt_dfc:>8},  α_s(obs) = {fmt_obs:>8}")
    print()
    print("OPEN: Derive T_c from DFC substrate:")
    print("  1. Resolve M_c(D7) from D7 SU(3) closure dynamics (not from SM running)")
    print("  2. Run α_s from M_c(D7) to hadronic scale using DFC beta function")
    print("  3. Identify confining-to-deconfining transition as D7 phase transition")
    print("  4. Compare resulting T_c to lattice QCD value 154 ± 9 MeV")
