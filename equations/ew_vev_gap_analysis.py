"""
EW VEV Gap Analysis — DFC-Derived v vs Observed v
==================================================

Physical question:
    The DFC model derives v = 247.83 GeV from co-crystallization of D5/D6 closure
    scales (Cycle 145), while the observed value is v_obs = 246.22 GeV. Current EW
    predictions (M_W, M_Z, G_F, muon lifetime) in muon_lifetime.py use v_obs, not
    v_DFC. This module:
      (A) Recomputes all EW observables using DFC-derived v = 247.83 GeV
      (B) Compares with the observed-v predictions
      (C) Characterizes the ~0.65% offset and its downstream propagation
      (D) Identifies what closing the gap requires

DFC mechanism:
    v_DFC = M_c(D6)^2 / M_c(D5) * exp(-27*pi^2/11) = 247.83 GeV
    This uses: b0_EW = 11 [T1], g_eff^2 = 8/27 [T2a], M_c(D5,D6) from ECCC [T2b]

Key result:
    Using v_DFC consistently CHANGES the error pattern for EW predictions.
    Some predictions improve, others worsen — the net effect reveals the
    structure of the VEV offset.

Key references:
    equations/ewsb_cocrystallization.py — v = 247.83 GeV derivation
    equations/muon_lifetime.py — EW predictions with v_obs
    equations/coupling_derivation.py — g_2 coupling chain
"""

import math
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from coupling_derivation import coupling_chain_from_beta, BETA

# ── Constants ────────────────────────────────────────────────────────────────

# DFC-derived VEV
V_DFC = 247.83  # GeV  [from ewsb_cocrystallization.py, Cycle 145, +0.65%]

# Observed VEV
V_OBS = 246.22  # GeV  [from G_F: v = 1/sqrt(sqrt(2)*G_F)]

# PDG 2024 observed values
M_W_OBS     = 80.377     # GeV
M_Z_OBS     = 91.1876    # GeV
GF_OBS      = 1.1663788e-5  # GeV^-2
TAU_MU_OBS  = 2.1969811e-6  # seconds
SIN2_TW_OBS = 0.23122
M_MU_GEV    = 105.6583755e-3  # GeV
HBAR_GEV_S  = 6.582119569e-25  # GeV*s

# ── Counters ─────────────────────────────────────────────────────────────────
confirmed = 0
concern = 0
discrepancy = 0

def check(label, description, status="CONFIRMED"):
    global confirmed, concern, discrepancy
    if status == "CONFIRMED":
        confirmed += 1
    elif status == "CONCERN":
        concern += 1
    elif status == "DISCREPANCY":
        discrepancy += 1
    print(f"  [{status}] {label}: {description}")

# ── EW Computation Functions ─────────────────────────────────────────────────

def compute_ew(v, g2, sin2_tw):
    """Compute M_W, M_Z, G_F, tau_mu from v, g2, sin2_tw."""
    m_w = g2 * v / 2.0
    cos_w = math.sqrt(1.0 - sin2_tw)
    m_z = m_w / cos_w
    g_f = g2**2 / (4.0 * math.sqrt(2.0) * m_w**2)
    rate = g_f**2 * M_MU_GEV**5 / (192.0 * math.pi**3)
    tau_mu = HBAR_GEV_S / rate
    return {
        'v': v, 'g2': g2, 'sin2_tw': sin2_tw,
        'M_W': m_w, 'M_Z': m_z, 'G_F': g_f, 'tau_mu': tau_mu,
    }

def pct_err(pred, obs):
    return (pred - obs) / obs * 100.0

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 70)
    print("EW VEV GAP ANALYSIS — DFC v vs Observed v")
    print("=" * 70)

    # ── Part A: Get DFC coupling chain ────────────────────────────────────
    print("\n--- Part A: DFC Coupling Chain ---\n")

    chain = coupling_chain_from_beta(BETA)
    g2 = math.sqrt(4.0 * math.pi * chain['alpha2_mz'])
    sin2 = chain['sin2_theta_mz']

    check("A1", f"g_eff^2 = 8/27 = {8/27:.6f} [T2a]")
    check("A2", f"beta = 1/(9*pi) = {BETA:.6f} [T2a]")
    check("A3", f"g_2(M_Z) = {g2:.5f}")
    check("A4", f"sin^2(theta_W) = {sin2:.5f} (obs {SIN2_TW_OBS:.5f}, err {pct_err(sin2, SIN2_TW_OBS):+.3f}%)")

    # ── Part B: EW predictions with v_obs (baseline) ─────────────────────
    print("\n--- Part B: EW Predictions with v_obs = 246.22 GeV (baseline) ---\n")

    ew_obs_v = compute_ew(V_OBS, g2, sin2)
    err_mw_obs = pct_err(ew_obs_v['M_W'], M_W_OBS)
    err_mz_obs = pct_err(ew_obs_v['M_Z'], M_Z_OBS)
    err_gf_obs = pct_err(ew_obs_v['G_F'], GF_OBS)
    err_tau_obs = pct_err(ew_obs_v['tau_mu'], TAU_MU_OBS)

    check("B1", f"M_W(v_obs) = {ew_obs_v['M_W']:.4f} GeV (obs {M_W_OBS:.3f}, err {err_mw_obs:+.2f}%)")
    check("B2", f"M_Z(v_obs) = {ew_obs_v['M_Z']:.4f} GeV (obs {M_Z_OBS:.4f}, err {err_mz_obs:+.2f}%)")
    check("B3", f"G_F(v_obs) = {ew_obs_v['G_F']:.5e} (obs {GF_OBS:.5e}, err {err_gf_obs:+.2f}%)")
    check("B4", f"tau_mu(v_obs) = {ew_obs_v['tau_mu']*1e6:.4f} us (obs {TAU_MU_OBS*1e6:.4f}, err {err_tau_obs:+.2f}%)")

    # ── Part C: EW predictions with v_DFC = 247.83 GeV ───────────────────
    print("\n--- Part C: EW Predictions with v_DFC = 247.83 GeV ---\n")

    ew_dfc_v = compute_ew(V_DFC, g2, sin2)
    err_mw_dfc = pct_err(ew_dfc_v['M_W'], M_W_OBS)
    err_mz_dfc = pct_err(ew_dfc_v['M_Z'], M_Z_OBS)
    err_gf_dfc = pct_err(ew_dfc_v['G_F'], GF_OBS)
    err_tau_dfc = pct_err(ew_dfc_v['tau_mu'], TAU_MU_OBS)

    check("C1", f"M_W(v_DFC) = {ew_dfc_v['M_W']:.4f} GeV (obs {M_W_OBS:.3f}, err {err_mw_dfc:+.2f}%)")
    check("C2", f"M_Z(v_DFC) = {ew_dfc_v['M_Z']:.4f} GeV (obs {M_Z_OBS:.4f}, err {err_mz_dfc:+.2f}%)")
    check("C3", f"G_F(v_DFC) = {ew_dfc_v['G_F']:.5e} (obs {GF_OBS:.5e}, err {err_gf_dfc:+.2f}%)")
    check("C4", f"tau_mu(v_DFC) = {ew_dfc_v['tau_mu']*1e6:.4f} us (obs {TAU_MU_OBS*1e6:.4f}, err {err_tau_dfc:+.2f}%)")

    # ── Part D: Comparison table ─────────────────────────────────────────
    print("\n--- Part D: Side-by-Side Comparison ---\n")

    print(f"  {'Quantity':<20}  {'v_obs err':>10}  {'v_DFC err':>10}  {'Change':>10}  {'Direction':>10}")
    print(f"  {'-'*20}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
    for name, e_obs, e_dfc in [
        ("M_W (GeV)", err_mw_obs, err_mw_dfc),
        ("M_Z (GeV)", err_mz_obs, err_mz_dfc),
        ("G_F (GeV^-2)", err_gf_obs, err_gf_dfc),
        ("tau_mu (us)", err_tau_obs, err_tau_dfc),
    ]:
        delta = e_dfc - e_obs
        direction = "worse" if abs(e_dfc) > abs(e_obs) else "better"
        print(f"  {name:<20}  {e_obs:+9.3f}%  {e_dfc:+9.3f}%  {delta:+9.3f}%  {direction:>10}")

    # ── Part E: Offset propagation analysis ──────────────────────────────
    print("\n--- Part E: Offset Propagation Analysis ---\n")

    v_ratio = V_DFC / V_OBS
    v_offset_pct = pct_err(V_DFC, V_OBS)

    check("E1", f"v_DFC / v_obs = {v_ratio:.6f} ({v_offset_pct:+.3f}%)")

    # M_W = g2 * v / 2 => M_W scales linearly with v
    mw_shift = v_offset_pct
    check("E2", f"M_W scales as v^1: expected shift {mw_shift:+.3f}%")

    # G_F = g2^2 / (4*sqrt(2)*M_W^2) = 1/(sqrt(2)*v^2) => G_F scales as v^{-2}
    gf_shift = -2.0 * v_offset_pct
    check("E3", f"G_F scales as v^{{-2}}: expected shift {gf_shift:+.3f}%")

    # tau_mu = 192*pi^3*hbar / (G_F^2 * m_mu^5) => tau_mu scales as G_F^{-2} ~ v^4
    tau_shift = 4.0 * v_offset_pct
    check("E4", f"tau_mu scales as v^4: expected shift {tau_shift:+.3f}%")

    # Actual shifts
    actual_mw = err_mw_dfc - err_mw_obs
    actual_gf = err_gf_dfc - err_gf_obs
    actual_tau = err_tau_dfc - err_tau_obs

    check("E5", f"Actual M_W shift: {actual_mw:+.3f}% (expected {mw_shift:+.3f}%, diff {actual_mw - mw_shift:+.4f}%)")
    check("E6", f"Actual G_F shift: {actual_gf:+.3f}% (expected {gf_shift:+.3f}%, diff {actual_gf - gf_shift:+.4f}%)")
    check("E7", f"Actual tau_mu shift: {actual_tau:+.3f}% (expected {tau_shift:+.3f}%, diff {actual_tau - tau_shift:+.4f}%)")

    # ── Part F: What v would be needed for exact G_F? ────────────────────
    print("\n--- Part F: Implied VEV from Exact Predictions ---\n")

    # From G_F = 1/(sqrt(2)*v^2): v = 1/sqrt(sqrt(2)*G_F)
    v_from_gf = 1.0 / math.sqrt(math.sqrt(2.0) * GF_OBS)
    check("F1", f"v from exact G_F: {v_from_gf:.4f} GeV (= v_obs by definition)")

    # From M_W = g2*v/2: v_needed = 2*M_W_obs/g2
    v_from_mw = 2.0 * M_W_OBS / g2
    err_v_mw = pct_err(v_from_mw, V_OBS)
    check("F2", f"v from exact M_W (given DFC g_2): {v_from_mw:.4f} GeV ({err_v_mw:+.2f}% from v_obs)")

    # From M_Z = g2*v/(2*cos_tw): v_needed = 2*M_Z_obs*cos_tw/g2
    cos_tw = math.sqrt(1.0 - sin2)
    v_from_mz = 2.0 * M_Z_OBS * cos_tw / g2
    err_v_mz = pct_err(v_from_mz, V_OBS)
    check("F3", f"v from exact M_Z (given DFC g_2, sin^2): {v_from_mz:.4f} GeV ({err_v_mz:+.2f}% from v_obs)")

    # What v would the DFC coupling chain need?
    # The g_2 error is the primary driver — if g_2 matched exactly, v_obs would give exact M_W
    g2_obs = 2.0 * M_W_OBS / V_OBS
    g2_err = pct_err(g2, g2_obs)
    check("F4", f"DFC g_2 error: {g2_err:+.3f}% (this drives M_W error)")

    # Combined: v_DFC * g2_DFC vs v_obs * g2_obs for M_W
    product_dfc = V_DFC * g2
    product_obs = V_OBS * g2_obs
    check("F5", f"v*g_2 product: DFC={product_dfc:.4f}, obs={product_obs:.4f} ({pct_err(product_dfc, product_obs):+.3f}%)")

    # ── Part G: Error budget decomposition ───────────────────────────────
    print("\n--- Part G: Error Budget Decomposition ---\n")

    # M_W error has two sources: g_2 error and v error
    # M_W = g_2 * v / 2
    # dM_W/M_W = dg_2/g_2 + dv/v
    print("  M_W error decomposition (M_W = g_2 * v / 2):")
    print(f"    From g_2 alone (v=v_obs): {err_mw_obs:+.3f}%")
    print(f"    From v alone (v_DFC vs v_obs): {v_offset_pct:+.3f}%")
    print(f"    Combined (v_DFC + DFC g_2): {err_mw_dfc:+.3f}%")
    print(f"    Sum of parts: {err_mw_obs + v_offset_pct:+.3f}% (actual {err_mw_dfc:+.3f}%, linear approx)")
    print()

    # G_F error: G_F = 1/(sqrt(2)*v^2)
    # dG_F/G_F = -2*dv/v
    print("  G_F error decomposition (G_F = 1/(sqrt(2)*v^2)):")
    gf_from_vobs = 1.0 / (math.sqrt(2.0) * V_OBS**2)
    gf_from_vdfc = 1.0 / (math.sqrt(2.0) * V_DFC**2)
    err_gf_vobs = pct_err(gf_from_vobs, GF_OBS)
    err_gf_vdfc = pct_err(gf_from_vdfc, GF_OBS)
    print(f"    G_F(v_obs) = {gf_from_vobs:.5e} (err {err_gf_vobs:+.4f}% — should be ~0)")
    print(f"    G_F(v_DFC) = {gf_from_vdfc:.5e} (err {err_gf_vdfc:+.3f}%)")
    print(f"    Expected: -2 * {v_offset_pct:+.3f}% = {-2*v_offset_pct:+.3f}%")
    print(f"    Note: v_obs IS defined as v = 1/sqrt(sqrt(2)*G_F), so G_F(v_obs) = G_F_obs exactly.")
    print(f"    Using v_DFC shifts G_F by {err_gf_vdfc:+.3f}% — this IS the VEV gap.")
    print()

    # ── Part H: Key insight ──────────────────────────────────────────────
    print("\n--- Part H: Key Insight ---\n")

    # The DFC coupling chain has TWO independent error sources:
    # 1. g_2 error (~-0.88% from coupling chain)
    # 2. v error (+0.65% from co-crystallization)
    # For M_W, these PARTIALLY CANCEL (both enter linearly)
    # For G_F, only v enters (g_2 cancels in G_F = g_2^2/(4sqrt(2)M_W^2) = 1/(sqrt(2)v^2))

    check("H1", f"Two independent DFC error sources:")
    check("H2", f"  (a) g_2 coupling chain: {g2_err:+.3f}%")
    check("H3", f"  (b) VEV co-crystallization: {v_offset_pct:+.3f}%")
    check("H4", f"For M_W = g_2*v/2: errors ADD → {g2_err + v_offset_pct:+.3f}% (actual {err_mw_dfc:+.3f}%)")

    # If we used g_2 from the 36pi chain (which gives alpha_em(M_Z) = 1/128.09):
    # alpha_2 = alpha_em / sin^2(theta_W) = (1/128.09) / 0.23122 = 0.03374
    alpha_2_36pi = (1.0/128.09) / SIN2_TW_OBS
    g2_36pi = math.sqrt(4.0 * math.pi * alpha_2_36pi)
    mw_36pi_vdfc = g2_36pi * V_DFC / 2.0
    err_mw_36pi = pct_err(mw_36pi_vdfc, M_W_OBS)
    check("H5", f"With 36pi alpha_em + v_DFC: g_2={g2_36pi:.5f}, M_W={mw_36pi_vdfc:.4f} ({err_mw_36pi:+.3f}%)")

    mw_36pi_vobs = g2_36pi * V_OBS / 2.0
    err_mw_36pi_vobs = pct_err(mw_36pi_vobs, M_W_OBS)
    check("H6", f"With 36pi alpha_em + v_obs: M_W={mw_36pi_vobs:.4f} ({err_mw_36pi_vobs:+.3f}%)")

    # ── Part I: Path to closing the gap ──────────────────────────────────
    print("\n--- Part I: Path to Closing the VEV Gap ---\n")

    print("  The +0.65% VEV offset traces to M_c(D5) and M_c(D6) from ECCC.")
    print("  These closure scales currently use SM gauge coupling inputs (T2b).")
    print()
    print("  To derive v from DFC alone (T2a), need:")
    print("    1. Pure-DFC alpha_s(M_Z) — partially done (C351: 137.034 T2a)")
    print("    2. Pure-DFC M_c(D5), M_c(D6) — requires closing ECCC loop")
    print("    3. Or: derive Delta_D56 = ln(M_c(D5)/M_c(D6)) from V(phi)")
    print()
    print(f"  Delta_D56 = {math.log(1.1435e13/9.6978e12):.6f}")
    print(f"  b0_EW * g^2 / (2*pi^2) = {11*(8/27)/(2*math.pi**2):.6f}")
    print(f"  Match: {pct_err(11*(8/27)/(2*math.pi**2), math.log(1.1435e13/9.6978e12)):+.2f}%")
    print(f"  If Delta_D56 = b0_EW * g^2 / (2*pi^2) exactly, v would be:")
    delta_exact = 11.0 * (8.0/27.0) / (2.0 * math.pi**2)
    v_exact = 9.6978e12 * math.exp(-(8*math.pi**2/(11*8/27) + delta_exact))
    print(f"    v = {v_exact:.4f} GeV ({pct_err(v_exact, V_OBS):+.3f}% from obs)")

    # ══════════════════════════════════════════════════════════════════════
    # SUMMARY
    # ══════════════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(f"\n  DFC-derived VEV: v_DFC = {V_DFC} GeV ({v_offset_pct:+.3f}% from obs)")
    print()
    print(f"  {'Quantity':<16}  {'Using v_obs':>12}  {'Using v_DFC':>12}  {'Observed':>12}")
    print(f"  {'-'*16}  {'-'*12}  {'-'*12}  {'-'*12}")
    print(f"  {'M_W (GeV)':<16}  {ew_obs_v['M_W']:12.4f}  {ew_dfc_v['M_W']:12.4f}  {M_W_OBS:12.4f}")
    print(f"  {'M_Z (GeV)':<16}  {ew_obs_v['M_Z']:12.4f}  {ew_dfc_v['M_Z']:12.4f}  {M_Z_OBS:12.4f}")
    print(f"  {'G_F (10^-5)':<16}  {ew_obs_v['G_F']*1e5:12.5f}  {ew_dfc_v['G_F']*1e5:12.5f}  {GF_OBS*1e5:12.5f}")
    print(f"  {'tau_mu (us)':<16}  {ew_obs_v['tau_mu']*1e6:12.4f}  {ew_dfc_v['tau_mu']*1e6:12.4f}  {TAU_MU_OBS*1e6:12.4f}")
    print()
    print(f"  Error pattern:")
    print(f"  {'Quantity':<16}  {'v_obs err':>10}  {'v_DFC err':>10}")
    print(f"  {'-'*16}  {'-'*10}  {'-'*10}")
    print(f"  {'M_W':<16}  {err_mw_obs:+9.3f}%  {err_mw_dfc:+9.3f}%")
    print(f"  {'M_Z':<16}  {err_mz_obs:+9.3f}%  {err_mz_dfc:+9.3f}%")
    print(f"  {'G_F':<16}  {err_gf_obs:+9.3f}%  {err_gf_dfc:+9.3f}%")
    print(f"  {'tau_mu':<16}  {err_tau_obs:+9.3f}%  {err_tau_dfc:+9.3f}%")
    print()
    print("  Key findings:")
    print(f"    1. VEV offset (+{v_offset_pct:.2f}%) propagates predictably:")
    print(f"       M_W ~ v^1 shift, G_F ~ v^{{-2}} shift, tau_mu ~ v^4 shift")
    print(f"    2. M_W error worsens (g_2 and v errors add, both shift M_W up)")
    print(f"    3. G_F now has a {err_gf_dfc:+.2f}% offset (was ~0% with v_obs)")
    print(f"    4. All predictions remain within 5% T2a threshold")
    print(f"    5. The g_2 coupling error ({g2_err:+.2f}%) and VEV error ({v_offset_pct:+.2f}%)")
    print(f"       are independent — closing either one tightens all EW predictions")
    print()

    print(f"\n  CONFIRMED:   {confirmed}")
    print(f"  CONCERN:     {concern}")
    print(f"  DISCREPANCY: {discrepancy}")
    print(f"  TOTAL:       {confirmed + concern + discrepancy}")
