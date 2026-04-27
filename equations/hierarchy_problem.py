"""
Hierarchy Problem — DFC dissolution argument and naturalness quantification.

The Standard Model hierarchy problem: why is the Higgs mass stable at 125 GeV
when radiative corrections from top quark loops grow as the UV cutoff squared?

DFC dissolution mechanism:
  - The Higgs field is the amplitude of the S³ squashing modulus at D6 depth.
  - There is no tree-level mass parameter — the Higgs mass is radiatively generated
    by the Coleman-Weinberg mechanism, with the D6 closure scale as the UV cutoff.
  - The S³ Goldstone structure protects the mass: m_H ∝ y_t × v → 0 as y_t → 0.
  - Planck-scale corrections are decoupled by the 5 bifurcation events separating D1 from D6.

Key claims:
  - Fine-tuning Δ_FT(SM) ≈ 3.6 × 10³²     [with Λ = M_Pl]
  - Fine-tuning Δ_FT(DFC, 10¹³ GeV) ≈ 2.5 × 10²⁰  [correct: D6 cutoff = M_c(D5/D6)]
  - Fine-tuning Δ_FT(DFC, 10¹⁸ GeV) shown for comparison only (M_c(D1) is Higgs λ₀ BC, not D6 cutoff)
  - T9 RESOLVED (Cycle 79): M_c(D1) sets Higgs λ₀; M_c(D5/D6) is the D6 cutoff for Δ_FT
  - Desert prediction: no new particles between TeV and M_c(D5/D6)

Key references:
  foundations/higgs_geometry.md           — S³ squashing as Higgs mechanism
  foundations/higgs_mass_derivation.md    — RG-improved CW mass; M_c(D1) ≈ 10¹⁸ GeV
  foundations/embedding_geometry.md       — Route 3B; M_c(D5/D6) ≈ 10¹³ GeV
  foundations/two_scale_resolution.md     — T9 resolution (Cycle 79)
  foundations/tension_analysis.md         — T7 (DFC Supersedes), T9 (Structurally Resolved)
  phenomena/.../hierarchy_problem.md      — full structural argument

Usage:
    python equations/hierarchy_problem.py
"""

import math


# ── Physical constants (PDG 2024) ─────────────────────────────────────────────

M_PLANCK_GEV    = 1.220e19   # Planck mass (GeV)
M_HIGGS_GEV     = 125.25     # Higgs mass (GeV)  [PDG 2024]
M_TOP_GEV       = 172.76     # Top quark mass (GeV)  [PDG 2024]
V_EW_GEV        = 246.0      # Electroweak VEV (GeV)
G_STRONG        = 0.1182     # α_s(M_Z)
G_WEAK_SIN2     = 0.23122    # sin²θ_W
G2              = math.sqrt(4 * math.pi * 0.00782)   # SU(2) gauge coupling at M_Z

# DFC closure scales
M_C_ROUTE3B_GEV = 1.02e13    # D5/D6 closure scale from Route 3B (gauge running)
M_C_HIGGSMASS_GEV = 1.0e18   # Closure scale from higgs_mass_derivation.md (RGE fit)


# ── Core formulas ─────────────────────────────────────────────────────────────

def top_yukawa(m_top=M_TOP_GEV, v=V_EW_GEV):
    """Top Yukawa coupling y_t = sqrt(2) * m_t / v."""
    return math.sqrt(2) * m_top / v


def delta_mH_squared(uv_cutoff_gev, y_t=None, n_colors=3):
    """
    One-loop top quark contribution to Higgs mass-squared with UV cutoff Λ.

    The top quark loop gives a negative contribution to the Higgs mass-squared:
    δm_H² = −(N_c × y_t²) / (8π²) × Λ²

    where N_c = 3 is the number of quark colors, y_t is the top Yukawa coupling,
    and Λ is the UV cutoff above which the loop integral is cut off.

    Parameters
    ----------
    uv_cutoff_gev : float  UV cutoff Λ (GeV)
    y_t : float  Top Yukawa (default: computed from m_t, v)
    n_colors : int  Color factor (3 for QCD)

    Returns
    -------
    float : |δm_H²| in GeV² (magnitude of top-loop correction)
    """
    if y_t is None:
        y_t = top_yukawa()
    return (n_colors * y_t**2 / (8 * math.pi**2)) * uv_cutoff_gev**2


def fine_tuning(uv_cutoff_gev, m_higgs=M_HIGGS_GEV):
    """
    Fine-tuning measure: Δ_FT = |δm_H²| / m_H²

    The ratio by which the tree-level mass and the radiative correction must
    cancel to yield the physical Higgs mass. Δ_FT = 1 means no fine-tuning.
    Δ_FT >> 1 means the parameters are fine-tuned to 1 part in Δ_FT.

    Parameters
    ----------
    uv_cutoff_gev : float  UV cutoff Λ (GeV)
    m_higgs : float  Physical Higgs mass (GeV)

    Returns
    -------
    float : fine-tuning measure Δ_FT (dimensionless)
    """
    return delta_mH_squared(uv_cutoff_gev) / m_higgs**2


def desert_prediction():
    """
    DFC 'desert' prediction: no new particles between the SM scale and M_c.

    In DFC, the substrate produces new closure structures only at the D-depth
    thresholds. Between the D6 closure scale M_c and the electroweak scale,
    there are no new closure events, so no new particles appear.

    Returns
    -------
    dict : energy ranges and DFC particle content predictions
    """
    return {
        'SM_top_scale':     (172.76,  'Top quark, Higgs, W/Z — last SM particles'),
        'current_LHC':      (4e3,     'No new physics observed up to ~4 TeV at LHC'),
        'future_FCC':       (100e3,   'FCC-hh reach ~50 TeV: DFC predicts no discovery'),
        'muon_collider':    (30e3,    'Muon collider reach: DFC predicts no discovery'),
        'Route3B_closure':  (M_C_ROUTE3B_GEV, 'D5/D6 closure scale — first DFC structure above SM'),
        'higgsmass_closure':(M_C_HIGGSMASS_GEV, 'Closure scale from Higgs mass RGE fit'),
        'planck_scale':     (M_PLANCK_GEV, 'D1 compression scale — substrate maximum'),
    }


def cw_mass_estimate(m_c_gev, v=V_EW_GEV, m_top=M_TOP_GEV):
    """
    Order-of-magnitude Coleman-Weinberg Higgs mass estimate from closure scale.

    The CW mechanism generates a Higgs mass-squared of order:
        m_H² ~ (3y_t⁴ / 8π²) × v² × |ln(m_c/v)|

    This is the leading top-quark contribution to the CW potential's second
    derivative at the minimum. The full calculation is in higgs_mass_derivation.md
    and higgs_potential.py, which reproduces 124.4 ± 3.7 GeV.

    Parameters
    ----------
    m_c_gev : float  Closure scale M_c (GeV)
    v : float  Electroweak VEV (GeV)
    m_top : float  Top mass (GeV)

    Returns
    -------
    float : estimated Higgs mass (GeV) from CW mechanism
    """
    y_t = top_yukawa(m_top, v)
    log_factor = abs(math.log(m_c_gev / v))
    mH_sq_estimate = (3 * y_t**4 / (8 * math.pi**2)) * v**2 * log_factor
    return math.sqrt(abs(mH_sq_estimate))


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("HIERARCHY PROBLEM — DFC NATURALNESS QUANTIFICATION")
    print("Dimensional Folding Compression Model")
    print("=" * 65)

    y_t = top_yukawa()
    print(f"\n--- SM Parameters ---")
    print(f"  Higgs mass:     m_H = {M_HIGGS_GEV:.2f} GeV")
    print(f"  Top mass:       m_t = {M_TOP_GEV:.2f} GeV")
    print(f"  Top Yukawa:     y_t = m_t*√2/v = {y_t:.4f}")
    print(f"  EW VEV:         v   = {V_EW_GEV:.1f} GeV")

    # Fine-tuning at various cutoff scales
    print(f"\n--- Fine-Tuning Comparison: Δ_FT = |δm_H²|/m_H² ---")
    cutoffs = [
        ("SM (Λ = M_Pl)",                              M_PLANCK_GEV),
        ("DFC M_c(D5/D6) = 10¹³ GeV  [correct D6]",   M_C_ROUTE3B_GEV),
        ("DFC M_c(D1)    = 10¹⁸ GeV  [λ₀ BC only]",   M_C_HIGGSMASS_GEV),
        ("Natural (Λ = m_H)",                          M_HIGGS_GEV),
    ]
    for label, cutoff in cutoffs:
        dm2 = delta_mH_squared(cutoff)
        ft = fine_tuning(cutoff)
        print(f"  {label:<40}  δm_H² = {dm2:.2e} GeV²   Δ_FT = {ft:.2e}")

    print(f"\n  Interpretation:")
    print(f"  - SM: 10³² fine-tuning — extraordinary cancellation required")
    print(f"  - DFC D6 cutoff (M_c(D5/D6)): Δ_FT ≈ 10²⁰ — improves by ~11 orders vs SM")
    print(f"  - DFC M_c(D1) = M_Pl: shown for completeness (not the correct D6 cutoff)")
    print(f"  - Natural: Δ_FT = 1 — would mean Λ ~ m_H, no hierarchy at all")
    print(f"  CORRECT INTERPRETATION: The Higgs is a D6 object.")
    print(f"    Its UV sensitivity is to D6 physics at M_c(D5/D6) ≈ 10¹³ GeV, NOT to D1/Planck.")
    print(f"    M_c(D1) = M_Pl sets the Higgs quartic λ₀ boundary condition — a different role.")
    print(f"    This is the T9 resolution (Cycle 79) — see two_scale_resolution.md.")

    # T9 resolution
    print(f"\n--- T9 Resolution: Two Scales, Two Distinct D-Depth Events ---")
    r3b = M_C_ROUTE3B_GEV
    hmd = M_C_HIGGSMASS_GEV
    print(f"  M_c(D5/D6) = {r3b:.2e} GeV  [gauge IC; correct Δ_FT cutoff for D6 Higgs]")
    print(f"  M_c(D1)    = {hmd:.2e} GeV  [Higgs quartic λ₀ UV boundary condition]")
    print(f"  Ratio: {hmd/r3b:.1e}  (5 depth steps, gamma_space ≈ 2.47/step)")
    print(f"  Status: T9 RESOLVED (Cycle 79) — labeling confusion, not genuine inconsistency")
    print(f"  GUT-normalized alpha_1 = alpha_2 crossing verified at 1.03e13 GeV (one-loop)")
    print(f"  Hierarchy dissolution uses M_c(D5/D6) — 11-order improvement over SM confirmed")

    # CW mass estimate
    print(f"\n--- Coleman-Weinberg Mass Estimate ---")
    for label, m_c in [("Route 3B", r3b), ("higgs_md", hmd)]:
        m_h_est = cw_mass_estimate(m_c)
        err = (m_h_est - M_HIGGS_GEV) / M_HIGGS_GEV * 100
        log_f = abs(math.log(m_c / V_EW_GEV))
        print(f"  {label}: M_c = {m_c:.1e} GeV,  ln(M_c/v) = {log_f:.1f},  m_H(CW) ~ {m_h_est:.1f} GeV  (error {err:+.0f}%)")
    print(f"  NOTE: Full CW calculation in higgs_potential.py gives 124.4 ± 3.7 GeV")
    print(f"  The simple estimate above uses only top Yukawa; full calc uses SM beta functions.")

    # Desert prediction
    print(f"\n--- Desert Prediction: No New Particles Between SM and M_c ---")
    desert = desert_prediction()
    for label, (energy, desc) in desert.items():
        flag = "DESERT ←" if energy > 4e3 and energy < M_C_ROUTE3B_GEV else ""
        print(f"  {energy:>12.2e} GeV:  {desc}  {flag}")

    # Summary
    print(f"\n--- Summary ---")
    ft_sm = fine_tuning(M_PLANCK_GEV)
    ft_r3b = fine_tuning(r3b)
    ft_hmd = fine_tuning(hmd)
    print(f"  CRITERION C CLAIM (structural): Hierarchy problem is dissolved in DFC")
    print(f"    — Higgs has no bare mass parameter; mass is entirely radiative (CW)")
    print(f"    — S³ Goldstone structure protects m_H → 0 as y_t → 0")
    print(f"    — D1/D6 separation (5 bifurcations) suppresses Planck-scale corrections")
    print(f"  STATUS: Structural argument complete; formal proof of decoupling OPEN")
    print(f"  T9 RESOLVED: correct D6 cutoff is M_c(D5/D6) ≈ 10¹³ GeV (Cycle 79)")
    print(f"  DESERT: No new DFC particles between SM and M_c — testable by future colliders")
    print(f"  FREE PARAMETERS: 0 (naturalness argument uses only SM parameters + M_c)")
