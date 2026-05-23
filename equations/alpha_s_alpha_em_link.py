"""
Alpha_s — Alpha_em Structural Link (Cycle 137)
===============================================

Physical question:
    Can the strong coupling constant α_s(M_Z) = 0.1182 be derived from
    DFC substrate parameters without circular input from SM running?

Key discovery (Cycle 137):
    The ECCC closure scales satisfy M_c(D7)/M_c(D5) ≈ 1/α_em(0) to 0.045%:
        M_c(D7)/M_c(D5) = 136.974  vs  1/α_em(0) = 137.036  (−0.045%)

    Structural implication: IF DFC derives α_em(0) = 1/137.036 exactly,
    THEN α_s(M_Z) = 0.1182 follows to 0.05% accuracy via:
        M_c(D7) = M_c(D5) / α_em(0)

    This reduces the α_s gap to the α_em(0) gap:
    Current α_em(0) error: −2.16%  (from α_em(M_Z) 1.31% error)
    Current α_s error (via old wrong M_c): −8.1%  (Cycle 119)

DFC mechanism:
    Both the D5 (electromagnetic) and D7 (strong) closure scales are fixed by
    the ECCC condition α_i(M_c(Di)) = g_eff²/(4π). The ratio M_c(D7)/M_c(D5)
    is determined by the SM running rate difference between U(1) and SU(3).

    The identification M_c(D7)/M_c(D5) = 1/α_em(0) may have a structural
    origin: the electromagnetic coupling α_em(0) connects the D5 closure
    scale to the D7 closure scale, relating two different depth behaviors
    of the same DFC substrate.

Status:
    - M_c(D7)/M_c(D5) = 1/α_em(0) to 0.045% — verified numerically (Tier 1)
    - Origin of this identity: NOT YET DERIVED from V(φ) (Tier 4 open)
    - Implication: closing α_em(0) gap closes α_s gap simultaneously

Key references:
    - equations/mc_closure_scales.py — ECCC closure scales (Cycle 130)
    - equations/alpha_s_target.py — α_s target M_c(D7) (Cycle 119/130)
    - equations/coupling_derivation.py — α_em(M_Z) = 1/129.6 (1.31% error)
    - equations/ewsb_cocrystallization.py — v = 247.83 GeV (Cycle 136, Tier 3)
"""

import math

# ─── DFC substrate constants (Tier 2a, Cycle 117) ─────────────────────────────
G_EFF_SQ = 8.0 / 27.0               # = 2I₄/N_Hopf, from V(φ), zero free params
BETA = 1.0 / (9.0 * math.pi)        # quartic coupling, Tier 2a
ALPHA_COMMON = G_EFF_SQ / (4 * math.pi)  # = 2/(27π) ≈ 0.02358

# ─── ECCC closure scales (Tier 3, Cycle 130) ──────────────────────────────────
MC_D5 = 1.1435e13    # GeV — D5/U(1) closure, from α₁(M_c) = α_common
MC_D6 = 9.6978e12   # GeV — D6/SU(2) closure, from α₂(M_c) = α_common
MC_D7 = 1.5663e15   # GeV — D7/SU(3) closure, from α₃(M_c) = α_common (circular)
M_Z = 91.1876        # GeV

# ─── Coupling constants (observed) ────────────────────────────────────────────
ALPHA_EM_0_OBS  = 1.0 / 137.036    # α_em(q→0), observed
ALPHA_EM_MZ_OBS = 1.0 / 127.9     # α_em(M_Z), observed
ALPHA_S_MZ_OBS  = 0.1182           # α_s(M_Z), observed (PDG 2022)

# ─── DFC α_em predictions (from coupling chain, Cycles 42→55) ─────────────────
ALPHA_EM_MZ_DFC = 1.0 / 129.6     # DFC prediction; −1.31% error
DELTA_1_OVER_ALPHA = 10.46         # QED running from M_Z to q=0 (lepton thresholds)
ALPHA_EM_0_DFC  = 1.0 / (1.0/ALPHA_EM_MZ_DFC + DELTA_1_OVER_ALPHA)  # ≈ 1/140.1

# ─── QCD running coefficient ───────────────────────────────────────────────────
B3_OVER_2PI = 7.0 / (2.0 * math.pi)   # d(1/α_s)/dt = b₃/(2π), b₃=7 (nf=6)


def mc_d7_from_alpha_em(alpha_em_0):
    """
    Compute M_c(D7) from the structural identity M_c(D7) = M_c(D5) / α_em(0).

    The ratio M_c(D7)/M_c(D5) = 1/α_em(0) holds to 0.045% in the ECCC.
    This function evaluates the α_s(M_Z) prediction that follows from this identity.

    Args:
        alpha_em_0: electromagnetic fine structure constant at q→0

    Returns:
        dict with M_c(D7), α_s(M_Z), and errors
    """
    mc_d7 = MC_D5 / alpha_em_0
    t7 = math.log(mc_d7 / M_Z)
    alpha_s_pred = 1.0 / (1.0/ALPHA_COMMON - B3_OVER_2PI * t7)
    err_alpha_s = 100.0 * (alpha_s_pred / ALPHA_S_MZ_OBS - 1.0)
    err_mc_d7   = 100.0 * (mc_d7 / MC_D7 - 1.0)
    return {
        'mc_d7': mc_d7,
        'alpha_s': alpha_s_pred,
        'err_alpha_s_pct': err_alpha_s,
        'err_mc_d7_pct': err_mc_d7,
    }


def verify_identity():
    """
    Verify M_c(D7)/M_c(D5) = 1/α_em(0) numerically.
    Returns the ratio and its deviation from unity.
    """
    ratio = MC_D7 / MC_D5
    inv_alpha = 1.0 / ALPHA_EM_0_OBS
    deviation = ratio / inv_alpha - 1.0
    return ratio, inv_alpha, deviation


if __name__ == "__main__":
    print("=" * 70)
    print("α_s — α_em Structural Link  (Cycle 137)")
    print("=" * 70)
    print()

    # ── Step 1: DFC substrate inputs ─────────────────────────────────────────
    print("DFC substrate (Tier 2a):")
    print(f"  g_eff²    = {G_EFF_SQ:.6f}  = 8/27   (from V(φ), Cycle 117)")
    print(f"  α_common  = {ALPHA_COMMON:.6f}  = 2/(27π)")
    print()

    # ── Step 2: ECCC closure scales ──────────────────────────────────────────
    print("ECCC closure scales (Tier 3, Cycle 130):")
    print(f"  M_c(D5) = {MC_D5:.4e} GeV")
    print(f"  M_c(D6) = {MC_D6:.4e} GeV")
    print(f"  M_c(D7) = {MC_D7:.4e} GeV  [from α₃(M_c)=α_common; circular]")
    print()

    # ── Step 3: Structural identity ──────────────────────────────────────────
    ratio, inv_alpha, dev = verify_identity()
    print("─" * 70)
    print("STRUCTURAL IDENTITY: M_c(D7)/M_c(D5) ≈ 1/α_em(0)")
    print("─" * 70)
    print(f"  M_c(D7)/M_c(D5)   = {ratio:.6f}")
    print(f"  1/α_em(0) (obs)   = {inv_alpha:.6f}  [= 137.036]")
    print(f"  Ratio             = {ratio / inv_alpha:.8f}")
    print(f"  Deviation         = {dev:.5f}  ({100*dev:.4f}%)")
    print()
    print("  Interpretation: The ratio of D7 to D5 closure scales equals")
    print("  the reciprocal of the electromagnetic fine structure constant")
    print("  at zero energy, to within 0.045%.")
    print()

    # ── Step 4: α_s implications ─────────────────────────────────────────────
    print("─" * 70)
    print("IMPLICATION FOR α_s(M_Z):")
    print("─" * 70)
    print()

    cases = [
        ("DFC α_em(0) = 1/140.1  (current, −2.16% error)", ALPHA_EM_0_DFC),
        ("Obs α_em(0) = 1/137.04 (if DFC derives this)", ALPHA_EM_0_OBS),
    ]

    for label, aem in cases:
        res = mc_d7_from_alpha_em(aem)
        print(f"  Case: {label}")
        print(f"    M_c(D7) = M_c(D5)/α_em = {res['mc_d7']:.4e} GeV  "
              f"(ECCC: {MC_D7:.4e}, err {res['err_mc_d7_pct']:+.2f}%)")
        print(f"    α_s(M_Z) = {res['alpha_s']:.4f}  "
              f"(obs: {ALPHA_S_MZ_OBS:.4f}, err {res['err_alpha_s_pct']:+.2f}%)")
        print()

    # ── Step 5: Gap analysis ──────────────────────────────────────────────────
    print("─" * 70)
    print("GAP ANALYSIS:")
    print("─" * 70)
    err_aem_mz  = 100.0 * (ALPHA_EM_MZ_DFC / ALPHA_EM_MZ_OBS - 1.0)
    err_aem_0   = 100.0 * (ALPHA_EM_0_DFC  / ALPHA_EM_0_OBS  - 1.0)
    print(f"  α_em(M_Z) error:  {err_aem_mz:+.2f}%  (DFC 1/129.6 vs obs 1/127.9)")
    print(f"  α_em(0)   error:  {err_aem_0:+.2f}%  (propagated through QED running)")
    print()
    print("  CHAIN: α_em(0) error → M_c(D7) error → α_s(M_Z) error")
    print(f"  α_em(0): −2.16%  →  M_c(D7): {(ALPHA_EM_0_OBS/ALPHA_EM_0_DFC - 1.0)*100:+.2f}%  "
          f"→  α_s: ~{100*(mc_d7_from_alpha_em(ALPHA_EM_0_DFC)['alpha_s']/ALPHA_S_MZ_OBS-1):+.2f}%")
    print()
    print("  NOTE: The current 'DFC α_s = 0.1086' (−8.1% from Cycle 119) used the")
    print("  OLD wrong M_c(D7) = 8×10¹⁴ GeV (α₁∩α₃ crossing, Cycle 130 corrected).")
    print("  Via M_c(D7) = M_c(D5)/α_em identity:")
    print(f"    DFC α_em(0) = 1/140.1 → α_s = {mc_d7_from_alpha_em(ALPHA_EM_0_DFC)['alpha_s']:.4f}  (+0.29%)")
    print(f"    obs α_em(0) = 1/137.0 → α_s = {mc_d7_from_alpha_em(ALPHA_EM_0_OBS)['alpha_s']:.4f}  (+0.01%)")
    print()

    # ── Step 6: Summary ──────────────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  RESULT (Tier 1 structural): M_c(D7)/M_c(D5) = 1/α_em(0) to 0.045%")
    print()
    print("  IMPLICATION:")
    print("    IF DFC closes α_em(0) gap (currently −2.16%),")
    print("    THEN α_s(M_Z) = 0.1182 follows to 0.05%.")
    print()
    print("  CURRENT STATUS:")
    print(f"    α_em(0) DFC: 1/{1/ALPHA_EM_0_DFC:.1f} (−2.16% from 1/137.04)")
    print(f"    α_s via identity: {mc_d7_from_alpha_em(ALPHA_EM_0_DFC)['alpha_s']:.4f} (+0.29%)")
    print()
    print("  OPEN STEP (Tier 4):")
    print("    Derive M_c(D7) = M_c(D5)/α_em(0) from V(φ) — show algebraically")
    print("    that the D7/D5 closure scale ratio is the EM coupling inverse.")
    print("    Physical hint: α_em connects the U(1) (D5) and SU(3) (D7) closure")
    print("    behaviors at the substrate level.")
    print()
    print("  CONNECTIONS:")
    print("    equations/mc_closure_scales.py  — ECCC; M_c(D5,D6,D7)")
    print("    equations/coupling_derivation.py — α_em(M_Z) chain")
    print("    equations/alpha_s_target.py      — α_s target M_c(D7)")
    print("    equations/ewsb_cocrystallization.py — Cycle 136 v=247.83 GeV")
