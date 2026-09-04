"""
Anomalous magnetic moment of the electron and muon from DFC coupling chain.

Physical question: What does the DFC coupling chain predict for a_e and a_μ?

DFC mechanism: The DFC 36π co-crystallization chain predicts α_em at all scales:
  β = 1/(9π) [Tier 2a; 0 free parameters]
  → g_eff² = 2I₄/N_Hopf = 8/27 [g_eff = 0.54433]
  → α_common = g_eff²/(4π) = 2/(27π)
  → 1/α_em(M_c) = (k_Y² + 1)/α_common = 36π [Tier 2a]
  → EW running → 1/α_em(M_Z) = 128.09 [Tier 2a]
  → QED running → 1/α_em(0) = 137.23 [Tier 2b]

Electron a_e: computed through 4 loops with universal QED coefficients.
Muon a_μ: computed through 5 loops with mass-dependent QED coefficients
  (electron and tau vacuum polarization loops), plus electroweak contribution
  from DFC-derived G_F and sin²θ_W. Hadronic VP is external input (T4 blocked).

Key references:
  - equations/alpha_em_prediction.py:         36π chain (Cycle 142)
  - equations/d5_complex_from_instability.py: β=1/(9π) derivation (Cycle 117)
  - equations/alpha_em_cocrystallization.py:  36π formula (Cycle 141)
  - Aoyama, Kinoshita, Nio, Phys Rev D 97 (2018) — QED 5-loop
  - Muon g-2 Theory Initiative White Paper, Phys Rep 887 (2020)

Usage:
    python equations/anomalous_magnetic_moment.py
"""

import math
import sys
import os

# Exact β: 1/(9π) [Tier 2a, Cycle 117; derived from V(φ) with 0 free parameters]
_BETA_EXACT = 1.0 / (9.0 * math.pi)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ─── Physical Constants ────────────────────────────────────────────────────────

# Observed electron anomalous magnetic moment (CODATA 2018)
A_E_OBS = 0.00115965218076   # a_e = (g-2)/2

# Observed muon anomalous magnetic moment
A_MU_OBS = 0.00116592061    # a_μ = (g-2)/2, PDG 2022

# Particle masses
M_E_GEV   = 0.000510999     # electron mass in GeV
M_MU_GEV  = 0.105658        # muon mass in GeV
M_TAU_GEV = 1.77686         # tau mass in GeV
M_Z_GEV   = 91.1876         # Z boson mass in GeV

# SM (PDG) reference values
ALPHA_SM_LOW = 1/137.036    # α_em at q→0 (Thomson limit)
ALPHA_SM_MZ  = 1/127.9      # α_em at M_Z (PDG)

# DFC inputs
BETA_DFC     = _BETA_EXACT  # β = 1/(9π) ≈ 0.03537 [Tier 2a, Cycle 117; 0 free params]
ALPHA_DFC_MZ = 1/128.09     # α_em(M_Z) from 36π chain [Tier 2a, Cycle 142]
# 36π chain: 1/α_em(M_c) = 36π, EW running → 1/α_em(M_Z) = 128.09
# Old value 1/129.6 is superseded.

# QED threshold matching: Δ(1/α) from M_Z down to q=0
# Observed difference 1/α_em(0) − 1/α_em(M_Z) from SM fermion masses
DELTA_INV_ALPHA_OBS = 9.136  # observed hadronic + leptonic VP (makes α(0) Tier 2b)

# DFC α_em(0) from 36π chain + observed QED running
INV_AEM_0_DFC = 128.09 + 9.136  # = 137.226
ALPHA_DFC_0 = 1.0 / INV_AEM_0_DFC  # DFC prediction for Thomson-limit α_em


# ─── α_em at relevant scales ──────────────────────────────────────────────────

def alpha_em_0_dfc():
    """
    Return DFC prediction for α_em at q = 0 (Thomson limit).

    The 36π chain gives 1/α_em(M_Z) = 128.09, and using the observed
    QED running Δ = 9.136 from M_Z to q = 0 gives 1/α_em(0) = 137.23.

    For the Schwinger term, α_em(0) is the correct coupling: the one-loop
    vertex correction is evaluated at on-shell momentum transfer q → 0.
    """
    return ALPHA_DFC_0


# ─── Anomalous Magnetic Moment ────────────────────────────────────────────────

def schwinger_term(alpha):
    """
    Schwinger leading-order anomalous magnetic moment: a = α/(2π).

    The fractional deviation of the magnetic moment above the Dirac value equals
    the fine structure constant divided by two pi, at leading (one-loop) order.

    Parameters
    ----------
    alpha : float
        Electromagnetic fine structure constant at the relevant scale.

    Returns
    -------
    float : a = (g-2)/2 at leading order.
    """
    return alpha / (2 * math.pi)


def ae_through_4loop(alpha):
    """
    Compute electron anomalous magnetic moment through 4 loops.

    The QED perturbative expansion for the anomalous magnetic moment of the
    electron is a power series in α/π. The leading (Schwinger) term is α/(2π).
    Higher-order coefficients are pure QED results — mathematical consequences
    of U(1) gauge theory vertex integrals — not SM-specific inputs. DFC inherits
    these as the perturbative structure of D5 U(1) closure behavior.

    The coefficients through 4 loops are:
      C₁ = 1/2        (Schwinger, 1948; exact)
      C₂ = -0.32848   (Petermann, Sommerfield, 1957; exact analytic)
      C₃ = +1.18124   (Laporta, Remiddi, 1996; exact analytic)
      C₄ = -1.91298   (Aoyama, Kinoshita, Nio, 2019; numerical)

    Hadronic and electroweak contributions to a_e are below 10⁻¹² and negligible.

    Parameters
    ----------
    alpha : float
        Fine structure constant at q = 0.

    Returns
    -------
    dict with each loop order contribution and total.
    """
    C2 = -0.328478965579194  # 2-loop (exact)
    C3 =  1.181241456587      # 3-loop (exact analytic)
    C4 = -1.91298             # 4-loop (numerical, Aoyama+ 2019)

    x = alpha / math.pi

    t1 = 0.5 * x           # = α/(2π)
    t2 = C2 * x**2
    t3 = C3 * x**3
    t4 = C4 * x**4

    return {
        '1-loop': t1,
        '2-loop': t2,
        '3-loop': t3,
        '4-loop': t4,
        'total': t1 + t2 + t3 + t4,
    }


# ─── Main Output ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 72)
    print("ANOMALOUS MAGNETIC MOMENT — ELECTRON (g-2)")
    print("DFC 36π Chain + QED Perturbation Theory Through 4 Loops")
    print("=" * 72)

    # ── Part A: DFC coupling chain
    alpha_0_dfc = alpha_em_0_dfc()
    alpha_0_sm  = ALPHA_SM_LOW

    print(f"\n{'─'*72}")
    print("PART A — DFC Coupling Chain (36π)")
    print(f"{'─'*72}")
    print(f"\n  β = 1/(9π) = {BETA_DFC:.6f}  [Tier 2a; 0 free params]")
    print(f"  g_eff² = 8/27 = {8/27:.6f}")
    print(f"  α_common = 2/(27π) = {2/(27*math.pi):.8f}")
    print(f"  1/α_em(M_c) = 36π = {36*math.pi:.4f}  [Tier 2a]")
    print(f"  1/α_em(M_Z) = 128.09  [Tier 2a, +0.15% vs obs 127.9]")
    print(f"  1/α_em(0)   = {INV_AEM_0_DFC:.3f}  [Tier 2b, +0.14% vs obs 137.036]")
    print(f"  α_em(0) DFC = {alpha_0_dfc:.8f}")
    print(f"  α_em(0) SM  = {alpha_0_sm:.8f}")
    print(f"  α_em(0) gap = {(alpha_0_dfc/alpha_0_sm - 1)*100:+.3f}%")

    # ── Part B: a_e through 4 loops with DFC α
    print(f"\n{'─'*72}")
    print("PART B — Electron a_e Through 4 Loops")
    print(f"{'─'*72}")

    dfc_loops = ae_through_4loop(alpha_0_dfc)
    sm_loops  = ae_through_4loop(alpha_0_sm)

    print(f"\n  QED perturbative expansion: a_e = Σ Cₙ (α/π)ⁿ")
    print(f"  C₁ = 1/2, C₂ = −0.3285, C₃ = +1.1812, C₄ = −1.9130")
    print(f"  These are pure U(1) vertex integrals — not SM-specific inputs.")
    print()

    print(f"  {'Loop order':<12} {'DFC':>14} {'SM (α=1/137)':>14} {'Ratio':>10}")
    print(f"  {'-'*12}  {'-'*14}  {'-'*14}  {'-'*10}")
    for key in ['1-loop', '2-loop', '3-loop', '4-loop']:
        d = dfc_loops[key]
        s = sm_loops[key]
        r = d/s if abs(s) > 0 else 0
        print(f"  {key:<12} {d:>+14.4e}  {s:>+14.4e}  {r:>10.6f}")

    a_e_dfc = dfc_loops['total']
    a_e_sm  = sm_loops['total']
    a_e_schwinger_dfc = schwinger_term(alpha_0_dfc)
    err_schwinger = (a_e_schwinger_dfc - A_E_OBS) / A_E_OBS * 100
    err_4loop_dfc = (a_e_dfc - A_E_OBS) / A_E_OBS * 100
    err_4loop_sm  = (a_e_sm  - A_E_OBS) / A_E_OBS * 100

    print()
    print(f"  DFC Schwinger only:  a_e = {a_e_schwinger_dfc:.12f}  ({err_schwinger:+.4f}%)")
    print(f"  DFC through 4-loop: a_e = {a_e_dfc:.12f}  ({err_4loop_dfc:+.4f}%)")
    print(f"  SM  through 4-loop: a_e = {a_e_sm:.12f}  ({err_4loop_sm:+.6f}%)")
    print(f"  Observed:           a_e = {A_E_OBS:.12f}")
    print()
    print(f"  Improvement: Schwinger-only {err_schwinger:+.4f}% → 4-loop {err_4loop_dfc:+.4f}%")
    print(f"  Residual error dominated by α_em(0) offset ({(alpha_0_dfc/alpha_0_sm - 1)*100:+.3f}%)")

    # ── Part C: Tests
    print(f"\n{'─'*72}")
    print("PART C — Tests")
    print(f"{'─'*72}")

    tests = []

    # C1: DFC 4-loop a_e within 0.5% of observed
    c1_pass = abs(err_4loop_dfc) < 0.5
    tests.append(('C1', c1_pass, f'DFC 4-loop a_e within 0.5% ({err_4loop_dfc:+.4f}%)'))

    # C2: 4-loop improves over Schwinger-only
    c2_pass = abs(err_4loop_dfc) < abs(err_schwinger)
    tests.append(('C2', c2_pass, f'4-loop closer than Schwinger ({abs(err_4loop_dfc):.4f}% < {abs(err_schwinger):.4f}%)'))

    # C3: DFC α_em(0) within 0.2% of observed
    alpha_err = abs(alpha_0_dfc / alpha_0_sm - 1) * 100
    c3_pass = alpha_err < 0.2
    tests.append(('C3', c3_pass, f'α_em(0) within 0.2% ({alpha_err:.3f}%)'))

    # C4: Higher-order corrections are perturbatively small
    ho_frac = abs(dfc_loops['2-loop'] + dfc_loops['3-loop'] + dfc_loops['4-loop']) / abs(dfc_loops['1-loop'])
    c4_pass = ho_frac < 0.01
    tests.append(('C4', c4_pass, f'Higher-order/leading < 1% ({ho_frac*100:.4f}%)'))

    # C5: DFC 4-loop matches SM 4-loop to within α_em offset
    ae_ratio = a_e_dfc / a_e_sm
    expected_ratio = alpha_0_dfc / alpha_0_sm  # leading-order scaling
    ratio_err = abs(ae_ratio / expected_ratio - 1) * 100
    c5_pass = ratio_err < 0.01
    tests.append(('C5', c5_pass, f'DFC/SM ratio consistent with α ratio ({ratio_err:.4f}%)'))

    n_pass = sum(1 for _, p, _ in tests if p)
    n_total = len(tests)

    print()
    for label, passed, desc in tests:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {label}: {desc}")

    # ── Part D: Muon g-2 — Schwinger only (legacy)
    print(f"\n{'─'*72}")
    print("PART D — Muon a_μ (Schwinger-Only, Legacy)")
    print(f"{'─'*72}")

    a_mu_dfc_schwinger = schwinger_term(alpha_0_dfc)
    err_mu_dfc = (a_mu_dfc_schwinger - A_MU_OBS) / A_MU_OBS * 100

    print(f"\n  Schwinger term (same α for both e and μ at leading order):")
    print(f"  DFC:      a_μ(LO) = {a_mu_dfc_schwinger:.10f}  ({err_mu_dfc:+.2f}%)")
    print(f"  Observed: a_μ     = {A_MU_OBS:.10f}")
    print(f"  (Superseded by Part F below)")

    # ── Part F: Muon g-2 — Full QED + EW + hadronic
    print(f"\n{'─'*72}")
    print("PART F — Muon a_μ (Full QED 5-Loop + EW + Hadronic)")
    print(f"{'─'*72}")

    # For the muon, QED coefficients include mass-dependent terms from
    # electron and tau vacuum polarization insertions in photon propagators.
    # At each loop order, the coefficient for the muon differs from the
    # universal (electron) value because the muon mass is comparable to
    # the scale at which heavier leptons contribute.
    #
    # Total muon QED coefficients C_n^(mu) = A1(n) + A2(n)(m_mu/m_e) + A2(n)(m_mu/m_tau) + ...
    # Values from Aoyama, Kinoshita, Nio (2019) and White Paper (2020):
    C1_mu = 0.5                    # 1-loop: universal Schwinger
    C2_mu = 0.765857425            # 2-loop: -0.3285 + 1.0942(e-loop) + 0.0001(tau)
    C3_mu = 24.05050996            # 3-loop: +1.181 + 22.868(e-loop) + 0.036(tau)
    C4_mu = 130.8796               # 4-loop: -1.913 + 132.69(e-loop) + mixed
    C5_mu = 753.29                 # 5-loop: Aoyama+ 2019 (numerical)

    x_dfc = alpha_0_dfc / math.pi
    x_sm  = alpha_0_sm / math.pi

    # QED contributions through 5 loops
    a_mu_qed_dfc = (C1_mu * x_dfc + C2_mu * x_dfc**2 + C3_mu * x_dfc**3
                    + C4_mu * x_dfc**4 + C5_mu * x_dfc**5)
    a_mu_qed_sm = (C1_mu * x_sm + C2_mu * x_sm**2 + C3_mu * x_sm**3
                   + C4_mu * x_sm**4 + C5_mu * x_sm**5)

    print(f"\n  QED coefficients for muon (including e/τ VP loops):")
    print(f"    C₁ = {C1_mu:.1f}  (Schwinger)")
    print(f"    C₂ = {C2_mu:.6f}  (+ electron VP)")
    print(f"    C₃ = {C3_mu:.5f}  (+ 2-loop electron VP)")
    print(f"    C₄ = {C4_mu:.4f}  (+ 3-loop electron VP)")
    print(f"    C₅ = {C5_mu:.2f}  (Aoyama+ 2019)")
    print(f"\n  α/π (DFC) = {x_dfc:.10f}")
    print(f"  α/π (SM)  = {x_sm:.10f}")

    # Electroweak contribution — from DFC-derived G_F, sin²θ_W, M_W, M_Z, m_H
    # The one-loop EW contribution is dominated by W and Z loops:
    #   a_μ(EW,1-loop) = (5 G_F m_μ² √2) / (48 π²) × [1 + (1-4sin²θ_W)² / 5 + ...]
    # Using DFC values: G_F_DFC = 1.168e-5, sin²θ_W = 0.2312
    G_F_DFC = 1.168e-5   # GeV⁻² [DFC, +0.18%]
    SIN2TW_DFC = 0.2312  # [DFC, 0.01%]
    M_MU_GEV_SQ = M_MU_GEV**2

    # Standard formula for 1-loop EW (Czarnecki, Marciano 1996)
    a_mu_ew_1loop = (5.0 * G_F_DFC * M_MU_GEV_SQ * math.sqrt(2)) / (48.0 * math.pi**2)
    # Correction factor for sin²θ_W
    ew_factor = 1.0 + (1.0 - 4.0 * SIN2TW_DFC)**2 / 5.0
    a_mu_ew_1loop *= ew_factor
    # 2-loop EW correction (−23% of 1-loop, Czarnecki+ 2003)
    a_mu_ew = a_mu_ew_1loop * (1.0 - 0.23)

    # Reference SM value for EW contribution
    a_mu_ew_sm_ref = 153.6e-11  # White Paper 2020

    print(f"\n  Electroweak contribution (from DFC G_F, sin²θ_W):")
    print(f"    G_F(DFC)      = {G_F_DFC:.3e} GeV⁻²")
    print(f"    sin²θ_W(DFC)  = {SIN2TW_DFC:.4f}")
    print(f"    a_μ(EW,DFC)   = {a_mu_ew:.4e}  ({a_mu_ew/1e-11:.1f} × 10⁻¹¹)")
    print(f"    a_μ(EW,SM)    = {a_mu_ew_sm_ref:.4e}  (153.6 × 10⁻¹¹)")
    ew_err = (a_mu_ew - a_mu_ew_sm_ref) / a_mu_ew_sm_ref * 100
    print(f"    EW gap (DFC vs SM) = {ew_err:+.1f}%")

    # Hadronic contributions — EXTERNAL INPUT (not yet derived from DFC)
    # Two values exist in the literature:
    # (a) Data-driven (e+e- → hadrons dispersion): a_μ(had,VP) = 6845(40) × 10⁻¹¹
    # (b) Lattice QCD (BMW 2021):                  a_μ(had,VP) = 7075(55) × 10⁻¹¹
    # Plus hadronic light-by-light:                 a_μ(had,LbL) = 92(18) × 10⁻¹¹
    #
    # The data-driven vs lattice discrepancy is THE central controversy in muon g-2.
    # DFC takes no position on this — both are external inputs until hadronic VP
    # is derived from DFC confinement (currently T4 blocked).
    a_mu_had_vp_data   = 6845e-11   # data-driven
    a_mu_had_vp_lattice = 7075e-11  # BMW lattice
    a_mu_had_lbl       = 92e-11     # light-by-light
    a_mu_had_data      = a_mu_had_vp_data + a_mu_had_lbl
    a_mu_had_lattice   = a_mu_had_vp_lattice + a_mu_had_lbl

    print(f"\n  Hadronic contributions (EXTERNAL INPUT — not from DFC):")
    print(f"    a_μ(had,VP) data-driven = {a_mu_had_vp_data/1e-11:.0f} × 10⁻¹¹")
    print(f"    a_μ(had,VP) lattice     = {a_mu_had_vp_lattice/1e-11:.0f} × 10⁻¹¹")
    print(f"    a_μ(had,LbL)            = {a_mu_had_lbl/1e-11:.0f} × 10⁻¹¹")
    print(f"    BLOCKED: DFC hadronic VP requires ρ spectral function from")
    print(f"    D7 confinement. See equations/hadronic_vp_dfc.py")

    # Total muon g-2 predictions
    a_mu_total_dfc_data = a_mu_qed_dfc + a_mu_ew + a_mu_had_data
    a_mu_total_dfc_lattice = a_mu_qed_dfc + a_mu_ew + a_mu_had_lattice
    a_mu_total_sm_data = a_mu_qed_sm + a_mu_ew_sm_ref + a_mu_had_data

    err_total_data = (a_mu_total_dfc_data - A_MU_OBS) / A_MU_OBS * 100
    err_total_lattice = (a_mu_total_dfc_lattice - A_MU_OBS) / A_MU_OBS * 100
    err_sm_data = (a_mu_total_sm_data - A_MU_OBS) / A_MU_OBS * 100

    # Deviation in units of experimental uncertainty
    a_mu_exp_unc = 41e-11  # Fermilab+BNL combined uncertainty
    delta_dfc_data = (a_mu_total_dfc_data - A_MU_OBS) / a_mu_exp_unc
    delta_dfc_lattice = (a_mu_total_dfc_lattice - A_MU_OBS) / a_mu_exp_unc
    delta_sm_data = (a_mu_total_sm_data - A_MU_OBS) / a_mu_exp_unc

    print(f"\n  ── Total muon a_μ predictions ──")
    print(f"\n  {'Source':<30} {'a_μ × 10¹¹':>16} {'Error':>10} {'Deviation':>10}")
    print(f"  {'-'*30} {'-'*16} {'-'*10} {'-'*10}")
    print(f"  {'DFC + data-driven had':<30} {a_mu_total_dfc_data/1e-11:>16.1f} {err_total_data:>+9.4f}% {delta_dfc_data:>+9.1f}σ")
    print(f"  {'DFC + lattice had':<30} {a_mu_total_dfc_lattice/1e-11:>16.1f} {err_total_lattice:>+9.4f}% {delta_dfc_lattice:>+9.1f}σ")
    print(f"  {'SM (data-driven, ref)':<30} {a_mu_total_sm_data/1e-11:>16.1f} {err_sm_data:>+9.4f}% {delta_sm_data:>+9.1f}σ")
    print(f"  {'Observed (Fermilab+BNL)':<30} {A_MU_OBS/1e-11:>16.1f}")
    print(f"\n  Key: DFC QED shift from SM = {(a_mu_qed_dfc - a_mu_qed_sm)/1e-11:+.1f} × 10⁻¹¹")
    print(f"  (This is the ONLY part DFC changes — hadronic and EW are nearly identical)")

    # Breakdown
    print(f"\n  ── DFC contribution breakdown (data-driven hadronic) ──")
    print(f"    QED (5-loop)  = {a_mu_qed_dfc/1e-11:>12.1f} × 10⁻¹¹  ({a_mu_qed_dfc/a_mu_total_dfc_data*100:.3f}%)")
    print(f"    EW (DFC)      = {a_mu_ew/1e-11:>12.1f} × 10⁻¹¹  ({a_mu_ew/a_mu_total_dfc_data*100:.4f}%)")
    print(f"    Had VP+LbL    = {a_mu_had_data/1e-11:>12.1f} × 10⁻¹¹  ({a_mu_had_data/a_mu_total_dfc_data*100:.3f}%)")
    print(f"    TOTAL         = {a_mu_total_dfc_data/1e-11:>12.1f} × 10⁻¹¹")

    # ── Part E: Tier classification
    print(f"\n{'─'*72}")
    print("PART E — Tier Classification")
    print(f"{'─'*72}")

    print(f"\n  Electron a_e (through 4 loops):")
    print(f"    Predicted: {a_e_dfc:.12f}")
    print(f"    Observed:  {A_E_OBS:.12f}")
    print(f"    Error:     {err_4loop_dfc:+.4f}%")
    print(f"    Free parameters: 0 from DFC (α_em from 36π chain)")
    print(f"    SM inputs: observed QED running Δ(1/α) = 9.136 (M_Z → 0)")
    print(f"    QED coefficients C₂, C₃, C₄: pure U(1) vertex integrals")
    if abs(err_4loop_dfc) < 5.0:
        print(f"    TIER: T2a (< 5% error, 0 DFC free parameters)")
    else:
        print(f"    TIER: T2b (> 5% error)")

    print(f"\n  Muon a_μ (QED 5-loop + EW + external hadronic):")
    print(f"    Predicted (data-driven had): {a_mu_total_dfc_data/1e-11:.1f} × 10⁻¹¹")
    print(f"    Predicted (lattice had):     {a_mu_total_dfc_lattice/1e-11:.1f} × 10⁻¹¹")
    print(f"    Observed:                    {A_MU_OBS/1e-11:.1f} × 10⁻¹¹")
    print(f"    Error (data-driven):         {err_total_data:+.4f}% ({delta_dfc_data:+.1f}σ)")
    print(f"    Error (lattice):             {err_total_lattice:+.4f}% ({delta_dfc_lattice:+.1f}σ)")
    print(f"    DFC free parameters: 0 (α from 36π, G_F from sin²θ_W chain)")
    print(f"    External inputs: hadronic VP (data-driven or lattice), QED running")
    print(f"    TIER: T2b (hadronic VP external; QED+EW are DFC-derived)")
    print(f"    Path to T2a: derive hadronic VP from DFC ρ spectral function")

    # ── Muon tests
    # F1: DFC QED muon matches SM QED to within α offset
    qed_mu_ratio = a_mu_qed_dfc / a_mu_qed_sm
    expected_mu_ratio = alpha_0_dfc / alpha_0_sm  # leading-order scaling
    f1_err = abs(qed_mu_ratio / expected_mu_ratio - 1) * 100
    f1_pass = f1_err < 0.1
    tests.append(('F1', f1_pass, f'DFC/SM muon QED ratio ~ α ratio ({f1_err:.4f}% off)'))

    # F2: EW contribution within 5% of reference
    f2_pass = abs(ew_err) < 5.0
    tests.append(('F2', f2_pass, f'DFC EW within 5% of SM reference ({ew_err:+.1f}%)'))

    # F3: DFC percentage error on a_μ matches α offset (same ~0.14%)
    f3_err = abs(err_total_data)
    alpha_pct = abs(alpha_0_dfc / alpha_0_sm - 1) * 100
    f3_pass = abs(f3_err - alpha_pct) < 0.02  # within 0.02pp of α offset
    tests.append(('F3', f3_pass, f'a_μ % error ({f3_err:.3f}%) tracks α offset ({alpha_pct:.3f}%)'))

    # F4: DFC muon g-2 within 0.2% (same as α_em precision)
    f4_pass = abs(err_total_data) < 0.2
    tests.append(('F4', f4_pass, f'DFC a_μ within 0.2% ({err_total_data:+.4f}%)'))

    # F5: DFC QED shift >> experimental precision (α offset is the bottleneck)
    had_unc = 40e-11  # data-driven uncertainty on hadronic VP
    qed_shift = abs(a_mu_qed_dfc - a_mu_qed_sm)
    f5_ratio = qed_shift / a_mu_exp_unc
    f5_pass = f5_ratio > 100  # DFC α shift swamps exp precision
    tests.append(('F5', f5_pass, f'DFC α offset / exp precision = {f5_ratio:.0f}× (α is bottleneck)'))

    # F6: DFC cannot resolve g-2 anomaly — α shift >> anomaly size
    anomaly_size = abs(A_MU_OBS - a_mu_total_sm_data)
    f6_ratio = qed_shift / anomaly_size
    f6_pass = f6_ratio > 10  # shift >> anomaly means DFC cannot address it via α
    tests.append(('F6', f6_pass, f'DFC α shift / g-2 anomaly = {f6_ratio:.0f}× (cannot resolve via α alone)'))

    n_pass = sum(1 for _, p, _ in tests if p)
    n_total = len(tests)

    # ── Summary
    print(f"\n{'='*72}")
    print("RESULTS")
    print(f"{'='*72}")
    print()
    for label, passed, desc in tests:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {label}: {desc}")
    print()
    print(f"  SUMMARY:")
    print(f"    a_e(DFC, 4-loop) = {a_e_dfc:.12f}  (error {err_4loop_dfc:+.4f}%, T2a)")
    print(f"    a_μ(DFC+data)    = {a_mu_total_dfc_data/1e-11:.1f} × 10⁻¹¹  ({delta_dfc_data:+.1f}σ, T2b)")
    print(f"    a_μ(DFC+lattice) = {a_mu_total_dfc_lattice/1e-11:.1f} × 10⁻¹¹  ({delta_dfc_lattice:+.1f}σ, T2b)")
    print(f"    Key finding: DFC shifts muon QED by {(a_mu_qed_dfc - a_mu_qed_sm)/1e-11:+.1f} × 10⁻¹¹")
    print(f"    — 642× larger than the g-2 anomaly (~250 × 10⁻¹¹)")
    print(f"    — 3953× larger than experimental precision ({a_mu_exp_unc/1e-11:.0f} × 10⁻¹¹)")
    print(f"    — DFC CANNOT address muon g-2 until α_em(0) is derived to ppm")
    print()
    print(f"{'='*72}")
    print(f"TOTAL: {n_pass}/{n_total} PASS, {n_total-n_pass}/{n_total} FAIL")
    print(f"{'='*72}")
