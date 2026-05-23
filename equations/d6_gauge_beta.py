"""
D6/D7 Gauge Theory Beta Function Survey (Cycle 133).

PHYSICAL QUESTION:
  The DFC hierarchy problem requires a mechanism that generates
      α_D6 ≈ 1070 GeV²   (= β v² / 2)
  from the D6 closure scale M_c(D6) ≈ 9.70×10¹² GeV.

  The non-perturbative condensate route (Cycle 132 Route D) writes:
      v = M_c × exp(-8π²/(b₀ g²))        [if v = Λ_confinement]   ...(I)
  or equivalently:
      α_D6 = M_c² × exp(-16π²/(b₀ g²))   [if α_D6 = Λ²]           ...(II)

  Either way, we need to identify which gauge theory (gauge group + matter content)
  gives the b₀ that reproduces the observed EW scale v = 246 GeV.

APPROACH:
  Survey one-loop beta function coefficients for:
    - SU(N) pure gauge
    - SU(N) + various fundamental matter content
  in both interpretations (I) and (II).

KEY CONSTANTS:
  g_eff² = 8/27  [Tier 2a, Cycle 117 — equal at each M_c(Di) by ECCC]
  M_c(D6) = 9.6978×10¹² GeV  [ECCC, Cycle 130]
  v = 246 GeV  [experimental target]

DERIVATION CHAIN:
  Tier 0 (β) → Tier 2a (g_eff²=8/27, β=1/(9π)) → Tier 2a (M_c(D6) ECCC)
  → THIS MODULE: which b₀ matches v=246 GeV?

REFERENCES:
  - equations/ewsb_mechanism.py (Cycle 132): root-cause analysis
  - equations/mc_closure_scales.py (Cycle 130): ECCC scales
  - foundations/vev_derivation.md: Bottleneck 3 documentation
  - foundations/coupling_derivation.md: g_eff² = 8/27 derivation chain
"""

import math

# ─────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────
PI     = math.pi
PI2    = PI**2
BETA   = 1.0 / (9.0 * PI)            # Tier 2a, Cycle 117
G_EFF_SQ = 8.0 / 27.0               # Tier 2a, Cycle 117
I4     = 4.0 / 3.0                   # Bogomolny, Tier 1
Q_TOP  = 2.0                         # topological charge, Tier 1
N_HOPF = 9                           # = 1+3+5, Tier 1

M_C_D6 = 9.6978e12   # GeV, ECCC [Cycle 130]
M_C_D7 = 1.5663e15   # GeV, ECCC [Cycle 130]
V_EW   = 246.0        # GeV, experimental target

# ─────────────────────────────────────────────────────
# 1. WHAT b₀ IS NEEDED?
# ─────────────────────────────────────────────────────
def required_b0():
    """
    Compute the one-loop beta function coefficient b₀ required to produce
    v = 246 GeV from M_c(D6) via dimensional transmutation, in two
    interpretations of the NP condensate formula.

    One-loop formula:  Λ = μ × exp(-8π²/(b₀ g²))

    Interpretation I:  v = Λ_D6  (v is the confinement energy scale)
    Interpretation II: α_D6 = Λ_D6²  (α_D6 = Λ²; v = √(2 α_D6/β))
    """
    print("=" * 70)
    print("[1] REQUIRED ONE-LOOP BETA COEFFICIENT b₀")
    print("=" * 70)

    # ── Interpretation I: v = M_c × exp(-8π²/(b₀ g²))
    delta_I = math.log(M_C_D6 / V_EW)            # = ln(M_c/v)
    # 8π²/(b₀ g²) = delta_I  →  b₀ = 8π²/(delta_I × g²)
    b0_I = 8.0 * PI2 / (delta_I * G_EFF_SQ)

    print(f"\n  Interpretation I: v = M_c(D6) × exp(-8π²/(b₀ g²))")
    print(f"    g_eff²                    = {G_EFF_SQ:.6f}  [= 8/27, Tier 2a]")
    print(f"    Δ = ln(M_c(D6)/v)         = {delta_I:.4f}")
    print(f"    b₀ needed                 = 8π²/(Δ × g²) = {b0_I:.4f}")
    print(f"    Equivalent:               = 27π²/Δ = {27.0*PI2/delta_I:.4f}")

    # ── Interpretation II: α_D6 = M_c² × exp(-16π²/(b₀ g²))
    alpha_d6_req = BETA * V_EW**2 / 2.0
    # exp(-c/g²) = α_D6_req/M_c² where c = 16π²/b₀
    ratio_II = alpha_d6_req / M_C_D6**2
    delta_II = -math.log(ratio_II)    # = 16π²/(b₀ g²)
    b0_II = 16.0 * PI2 / (delta_II * G_EFF_SQ)

    print(f"\n  Interpretation II: α_D6 = M_c(D6)² × exp(-16π²/(b₀ g²))")
    print(f"    α_D6_required             = {alpha_d6_req:.4f} GeV²")
    print(f"    ratio = α_D6_req/M_c²     = {ratio_II:.4e}")
    print(f"    c_needed = -g² ln(ratio)  = {-G_EFF_SQ*math.log(ratio_II):.4f}")
    print(f"    Δ = 16π²/(b₀ g²)          = {delta_II:.4f}")
    print(f"    b₀ needed                 = 16π²/(Δ × g²) = {b0_II:.4f}")

    print(f"\n  SUMMARY:")
    print(f"    Interp I  (v = Λ):    b₀_needed = {b0_I:.4f}")
    print(f"    Interp II (v² = Λ²):  b₀_needed = {b0_II:.4f}")
    print(f"    Note: b₀_II = 2 × b₀_I  (trivially, factor 2 from Λ vs Λ²)")
    print(f"    Note: SU(2) pure gauge  b₀_max = 22/3 ≈ {22/3:.4f}")
    print(f"    Note: SU(3) pure gauge  b₀     = 11")
    print(f"    → b₀_I ≈ {b0_I:.2f} EXCEEDS SU(2) max — SU(2) CANNOT drive EWSB")
    print(f"    → b₀_I ≈ {b0_I:.2f} ≈ 11 (SU(3) pure gauge)  ← candidate")

    return b0_I, b0_II, delta_I


# ─────────────────────────────────────────────────────
# 2. ONE-LOOP b₀ FOR GAUGE THEORIES
# ─────────────────────────────────────────────────────
def one_loop_b0(N_gauge, n_weyl_fund=0, n_cmplx_scal_fund=0,
                n_weyl_adj=0, n_cmplx_scal_adj=0):
    """
    One-loop beta function coefficient for SU(N) gauge theory:

      b₀ = (11/3) C₂(G) - (2/3) T_f n_f - (1/3) T_s n_s

    where:
      C₂(SU(N)) = N  [adjoint Casimir]
      T(fundamental) = 1/2
      T(adjoint) = N

    Parameters:
      N_gauge           : gauge group SU(N)
      n_weyl_fund       : number of Weyl fundamental fermions
      n_cmplx_scal_fund : number of complex fundamental scalars
      n_weyl_adj        : number of Weyl adjoint fermions (gauginos in SUSY)
      n_cmplx_scal_adj  : number of complex adjoint scalars
    """
    C2G = float(N_gauge)
    T_fund = 0.5
    T_adj = float(N_gauge)

    b0 = (11.0/3.0) * C2G
    b0 -= (2.0/3.0) * T_fund * n_weyl_fund
    b0 -= (1.0/3.0) * T_fund * n_cmplx_scal_fund
    b0 -= (2.0/3.0) * T_adj * n_weyl_adj
    b0 -= (1.0/3.0) * T_adj * n_cmplx_scal_adj
    return b0


def survey_gauge_theories():
    """
    Survey one-loop b₀ for candidate gauge theories and compute
    the predicted v (Interpretation I) and c = -g²ln(α_D6/M_c²)
    (Interpretation II) for each.
    """
    print("\n" + "=" * 70)
    print("[2] GAUGE THEORY BETA COEFFICIENT SURVEY")
    print("    Interpretation I: v = M_c(D6) × exp(-8π²/(b₀ g²))")
    print("=" * 70)

    candidates = [
        # (label, N_gauge, n_weyl_fund, n_cmplx_fund, n_weyl_adj, n_cmplx_adj)
        ("SU(2) pure",            2, 0,  0, 0, 0),
        ("SU(2) + 1 Weyl doublet",2, 1,  0, 0, 0),
        ("SU(2) + 2 Weyl doublet",2, 2,  0, 0, 0),
        ("SU(2) + 4 Weyl doublet",2, 4,  0, 0, 0),
        ("SU(2) + 8 Weyl doublet",2, 8,  0, 0, 0),
        ("SU(2) + 1 Higgs doublet",2,0,  1, 0, 0),
        ("SU(2) N=1 SYM (1 adj Weyl)", 2, 0, 0, 1, 0),
        ("SU(2) N=2 SYM (1 adj Weyl + 1 adj cmpx scl)", 2, 0, 0, 1, 1),
        ("SU(3) pure",            3, 0,  0, 0, 0),
        ("SU(3) + 1 Weyl quark",  3, 1,  0, 0, 0),
        ("SU(3) + 2 Weyl quarks", 3, 2,  0, 0, 0),
        ("SU(3) + 3 Weyl quarks", 3, 3,  0, 0, 0),
        ("SU(3) + 6 Weyl quarks (3 Dirac)", 3, 6, 0, 0, 0),
        ("SU(3) + 12 Weyl quarks (6 Dirac)", 3,12, 0, 0, 0),
        ("SU(4) pure",            4, 0,  0, 0, 0),
        ("SU(5) pure",            5, 0,  0, 0, 0),
    ]

    # b₀_needed for Interpretation I
    delta_I = math.log(M_C_D6 / V_EW)
    b0_I_needed = 8.0 * PI2 / (delta_I * G_EFF_SQ)

    header = f"{'Theory':<40} {'b₀':>7} {'v (GeV)':>12} {'err %':>8}"
    print(f"\n  {'g_eff²':} = {G_EFF_SQ:.6f},  M_c(D6) = {M_C_D6:.4e} GeV")
    print(f"  b₀ needed = {b0_I_needed:.4f}  (for v = 246 GeV)")
    print(f"\n  {header}")
    print(f"  {'-'*72}")

    results = []
    for label, N, nwf, ncs, nwa, nca in candidates:
        b0 = one_loop_b0(N, nwf, ncs, nwa, nca)
        if b0 <= 0:
            v_pred = float('inf')
            err = float('inf')
        else:
            exponent = -8.0 * PI2 / (b0 * G_EFF_SQ)
            v_pred = M_C_D6 * math.exp(exponent)
            err = (v_pred - V_EW) / V_EW * 100.0
        results.append((label, b0, v_pred, err))
        v_str = f"{v_pred:.3e}" if v_pred > 1e4 or v_pred < 0.01 else f"{v_pred:.2f}"
        print(f"  {label:<40} {b0:>7.4f} {v_str:>12}  {err:>+8.2f}%")

    # Best match
    finite = [(l, b0, v, e) for l, b0, v, e in results if abs(e) < 1e6]
    best = min(finite, key=lambda x: abs(x[3]))
    print(f"\n  Best match: '{best[0]}'")
    print(f"    b₀ = {best[1]:.4f},  v = {best[2]:.2f} GeV,  error = {best[3]:+.2f}%")
    return results


# ─────────────────────────────────────────────────────
# 3. SPECIAL DFC VALUES OF b₀
# ─────────────────────────────────────────────────────
def dfc_special_b0():
    """
    Check whether any DFC-derived numbers (I₄, Q_top, N_Hopf, g_eff², etc.)
    produce a b₀ close to the required ≈ 10.92.
    """
    print("\n" + "=" * 70)
    print("[3] DFC SPECIAL COMBINATIONS FOR b₀")
    print("    Looking for b₀ ≈ 10.92 from DFC constants")
    print("=" * 70)

    delta_I = math.log(M_C_D6 / V_EW)
    b0_target = 8.0 * PI2 / (delta_I * G_EFF_SQ)

    candidates = {
        "N_Hopf + 2 = 11":                N_HOPF + 2,
        "N_Hopf + 1 = 10":                N_HOPF + 1,
        "N_Hopf     = 9":                 N_HOPF,
        "11 C₂(SU3)/3 = 11 (pure SU(3))": 11,
        "3 × Q_top + N_Hopf = 15":        3*Q_TOP + N_HOPF,
        "Q_top × N_Hopf / I₄ = 27/2":     Q_TOP * N_HOPF / I4,
        "1/(β g²) = 27/(8π/9)":           27.0 / (8.0 * PI / 9.0),
        "27π²/Δ":                         27.0 * PI2 / delta_I,
        "2π²/g² / Δ":                     2.0 * PI2 / G_EFF_SQ / delta_I,
        "8 I₄ g²":                        8.0 * I4 * G_EFF_SQ,
    }

    print(f"\n  b₀ target (needed) = {b0_target:.4f}")
    print(f"\n  {'Combination':<40} {'Value':>8} {'Δb₀':>8} {'Δv %':>8}")
    print(f"  {'-'*70}")

    for label, val in candidates.items():
        delta_b0 = val - b0_target
        if val > 0:
            v_pred = M_C_D6 * math.exp(-8.0 * PI2 / (val * G_EFF_SQ))
            err_v = (v_pred - V_EW) / V_EW * 100.0
        else:
            err_v = float('inf')
        print(f"  {label:<40} {val:>8.4f} {delta_b0:>+8.4f} {err_v:>+8.2f}%")

    # Highlight N_Hopf + 2
    b0_best = N_HOPF + 2   # = 11 = SU(3) pure gauge
    v_best = M_C_D6 * math.exp(-8.0 * PI2 / (b0_best * G_EFF_SQ))
    print(f"\n  CLOSEST: b₀ = N_Hopf + 2 = {b0_best}")
    print(f"    v = M_c(D6) × exp(-8π²/({b0_best} × {G_EFF_SQ:.6f}))")
    print(f"      = M_c(D6) × exp(-27π²/{b0_best})")
    print(f"      = {v_best:.4f} GeV   (target: 246 GeV,  error: {(v_best/V_EW-1)*100:+.2f}%)")
    print(f"\n  STRUCTURAL NOTE:")
    print(f"    b₀ = N_Hopf + 2 = {N_HOPF} + 2 = {b0_best}")
    print(f"    This equals the one-loop coefficient of PURE SU(3) gauge theory")
    print(f"    (b₀ = 11C₂(SU(3))/3 = 11×3/3 = 11).")
    print(f"    The DFC D7 depth corresponds to SU(3), which has C₂(G)=3.")
    print(f"    The '+2' could reflect: 2 = Q_top (topological charge of D6 kink),")
    print(f"    or 2 = d_1 + d_1 = n(D5) dimensions, or the 2-sidedness of the Z₂ topology.")
    print(f"    → Physical hypothesis: the D7 SU(3) PURE GAUGE theory,")
    print(f"      evaluated at the D6 scale (g²=g_eff² by ECCC), generates v via")
    print(f"      v = M_c(D6) × exp(-27π²/(N_Hopf+2))")
    print(f"      with a residual error of {(v_best/V_EW-1)*100:+.2f}%.")

    return b0_best, v_best


# ─────────────────────────────────────────────────────
# 4. EXPLICIT FORMULA CHECK
# ─────────────────────────────────────────────────────
def formula_check():
    """
    Verify the formula v = M_c(D6) × exp(-27π²/11) and compare
    to the alternative v = M_c(D7) × exp(-27π²/b₀_D7).
    Also checks whether the gap could be closed by two-loop or
    normalization corrections.
    """
    print("\n" + "=" * 70)
    print("[4] FORMULA VERIFICATION AND GAP ANALYSIS")
    print("=" * 70)

    # ── Formula A: D6 scale, SU(3) pure b₀=11
    b0_11 = 11
    v_A = M_C_D6 * math.exp(-8.0 * PI2 / (b0_11 * G_EFF_SQ))
    print(f"\n  Formula A: v = M_c(D6) × exp(-8π²/(11 × g_eff²))")
    print(f"           = M_c(D6) × exp(-27π²/11)")
    print(f"    exponent = {-8.0*PI2/(11*G_EFF_SQ):.4f}")
    print(f"    v_A = {v_A:.4f} GeV   (target 246, error {(v_A/V_EW-1)*100:+.2f}%)")

    # ── Formula B: D7 scale, SU(3) pure b₀=11
    v_B = M_C_D7 * math.exp(-8.0 * PI2 / (b0_11 * G_EFF_SQ))
    print(f"\n  Formula B: v = M_c(D7) × exp(-8π²/(11 × g_eff²))")
    print(f"    v_B = {v_B:.4e} GeV   (too large by {(v_B/V_EW-1)*100:+.0f}%)")

    # ── Formula C: correction factor from 19% gap
    # If v_A = 293 GeV = 246 × 1.19, we need an extra suppression of 1/1.19.
    # What correction closes the gap?
    correction_factor = V_EW / v_A
    extra_exp = math.log(correction_factor)
    print(f"\n  Gap analysis (A vs target):")
    print(f"    v_A / v_target = {v_A/V_EW:.4f}  (gap: {(v_A/V_EW-1)*100:+.2f}%)")
    print(f"    Extra suppression needed: exp({extra_exp:.4f})")
    print(f"    This extra factor could come from:")
    print(f"      - Two-loop correction to b₀: δb₀ = {extra_exp/math.log(M_C_D6/V_EW)*11.0:.3f}")
    print(f"      - A prefactor A in v = A × M_c × exp(-...): A = {correction_factor:.4f}")
    print(f"      - Matching condition at the D6/D7 boundary")

    # ── Formula D: v = (I₄/N_Hopf) × M_c(D6) × exp(-8π²/(11 × g²))
    # I₄/N_Hopf = (4/3)/9 = 4/27
    prefactor_D = I4 / N_HOPF
    v_D = prefactor_D * M_C_D6 * math.exp(-8.0 * PI2 / (b0_11 * G_EFF_SQ))
    print(f"\n  Formula D: v = (I₄/N_Hopf) × M_c(D6) × exp(-27π²/11)")
    print(f"    Prefactor I₄/N_Hopf = {I4:.4f}/{N_HOPF} = {prefactor_D:.6f}")
    print(f"    v_D = {v_D:.4f} GeV   (error: {(v_D/V_EW-1)*100:+.2f}%)")

    # ── Formula E: v = (g_eff)^Q_top × M_c(D6) × exp(-27π²/11)
    g_eff = math.sqrt(G_EFF_SQ)
    prefactor_E = g_eff**Q_TOP
    v_E = prefactor_E * M_C_D6 * math.exp(-8.0 * PI2 / (b0_11 * G_EFF_SQ))
    print(f"\n  Formula E: v = g_eff^Q_top × M_c(D6) × exp(-27π²/11)")
    print(f"    Prefactor g_eff^2 = {G_EFF_SQ:.6f}")
    print(f"    v_E = {v_E:.4f} GeV   (error: {(v_E/V_EW-1)*100:+.2f}%)")

    # ── Formula F: include instanton measure factor (2π)²
    # In some conventions, the instanton measure includes extra factors
    # of 2π from zero modes.
    # For k zero modes: measure ~ (2π)^{-k} × ...
    # Try: v = (2π/b₀)^{1/2} × M_c × exp(-8π²/(b₀ g²))
    from_measure = math.sqrt(2.0*PI/b0_11)
    v_F = from_measure * M_C_D6 * math.exp(-8.0 * PI2 / (b0_11 * G_EFF_SQ))
    print(f"\n  Formula F: v = √(2π/b₀) × M_c(D6) × exp(-27π²/11)")
    print(f"    Prefactor = {from_measure:.4f}")
    print(f"    v_F = {v_F:.4f} GeV   (error: {(v_F/V_EW-1)*100:+.2f}%)")

    # Find which prefactor closes the gap
    needed_prefactor = V_EW / v_A
    print(f"\n  Prefactor needed to close 19% gap: A = {needed_prefactor:.6f}")
    print(f"  DFC candidates for A:")
    for name, val in [("I₄", I4), ("1/I₄", 1/I4), ("g_eff²", G_EFF_SQ),
                      ("1/g_eff²", 1/G_EFF_SQ), ("√β", math.sqrt(BETA)),
                      ("β", BETA), ("2/(N_Hopf)", 2.0/N_HOPF),
                      ("Q_top/N_Hopf", Q_TOP/N_HOPF),
                      ("I₄/Q_top", I4/Q_TOP), ("2I₄/N_Hopf", 2*I4/N_HOPF),
                      ("g_eff", math.sqrt(G_EFF_SQ)),
                      ]:
        err = (val/needed_prefactor - 1)*100
        marker = " ←" if abs(err) < 5 else ""
        print(f"    {name:<22} = {val:.6f}   Δ = {err:+.2f}%{marker}")


# ─────────────────────────────────────────────────────
# 5. SUMMARY
# ─────────────────────────────────────────────────────
def summary():
    print("\n" + "=" * 70)
    print("SUMMARY: D6 GAUGE BETA FUNCTION SURVEY (Cycle 133)")
    print("=" * 70)

    delta_I = math.log(M_C_D6 / V_EW)
    b0_needed = 8.0 * PI2 / (delta_I * G_EFF_SQ)
    v_su3_pure = M_C_D6 * math.exp(-8.0 * PI2 / (11 * G_EFF_SQ))

    alpha_d6_req = BETA * V_EW**2 / 2.0
    c_needed = G_EFF_SQ * math.log(M_C_D6**2 / alpha_d6_req)

    print(f"""
  CORE FINDING:
  The DFC EW scale hierarchy requires a confinement-like mechanism with
  one-loop beta coefficient b₀ ≈ {b0_needed:.2f}, evaluated at g_eff² = {G_EFF_SQ:.6f}.

  No SU(2) gauge theory can supply this b₀ (SU(2) max = 22/3 ≈ 7.33).
  The required b₀ ≈ {b0_needed:.2f} matches SU(3) PURE GAUGE (b₀ = 11) within:
    v = M_c(D6) × exp(-27π²/11) = {v_su3_pure:.2f} GeV  (target 246, err {(v_su3_pure/V_EW-1)*100:+.2f}%)

  TIER ASSIGNMENTS:
    b₀_needed = 27π²/ln(M_c(D6)/v):    Tier 4 OPEN [c depends on v=246 GeV input]
    SU(3) pure gauge b₀ = 11:           Tier 3 CANDIDATE
    v = M_c × exp(-27π²/11):            Tier 3 CANDIDATE  (19% error, no free params)
    c_needed ≈ 15.65:                   Tier 4 OPEN
    8π²/5 ≈ 15.79 (b₀=5 interpretation): 0.9% from target  [interpretation ambiguous]

  DFC STRUCTURAL INTERPRETATION (Tier 3 candidate):
    The D7 depth = SU(3). At D7 depths, the substrate produces SU(3) gauge dynamics.
    By ECCC (Cycle 130), g₃²(M_c(D7)) = g_eff² = 8/27.
    The D7 SU(3) pure gauge theory generates a confinement scale:
      Λ_D7 = M_c(D7) × exp(-8π²/(11 × g_eff²)) = {M_C_D7 * math.exp(-8*PI2/(11*G_EFF_SQ)):.4e} GeV
    This is ~{M_C_D7 * math.exp(-8*PI2/(11*G_EFF_SQ)):.0f} GeV — too large by {(M_C_D7 * math.exp(-8*PI2/(11*G_EFF_SQ))/246-1)*100:+.0f}%.
    BUT: using M_c(D6) as UV scale (D6 closure sets the physical IR scale):
      Λ_D6-SU3 = M_c(D6) × exp(-8π²/(11 × g_eff²)) = {v_su3_pure:.2f} GeV   (19% from 246 GeV)

  STRUCTURAL IDENTITY FOUND:
    b₀_needed ≈ N_Hopf + 2 = {N_HOPF} + 2 = {N_HOPF+2}
    where N_Hopf = 1+3+5 = 9 (Tier 1, Cycle 107) and 2 = Q_top (Tier 1, Cycle 111).
    This gives: v = M_c(D6) × exp(-27π²/(N_Hopf + Q_top))   [Tier 3, 19% error]

  OPEN GAPS:
    1. The 19% residual between Formula A and v=246 GeV requires a
       DFC prefactor A ≈ {V_EW/v_su3_pure:.4f}. No clean DFC value found yet.
    2. The identification "D6 uses D7 SU(3) beta function" needs derivation
       from substrate field equations — currently Tier 3 structural.
    3. SU(2) (D6) alone cannot produce b₀ ≈ 11; the mechanism must involve
       D7 dynamics modifying D6 mass generation.

  NEXT STEP:
    Derive the prefactor A = {V_EW/v_su3_pure:.4f} from DFC geometry.
    Check if A = (I₄/N_Hopf)^(something) or A = (M_c(D6)/M_c(D7))^(fraction).
    """)

    print(f"  Numerical verification:")
    print(f"    g_eff² = 8/27 = {8/27:.6f}  (error {(G_EFF_SQ - 8/27):.2e})")
    print(f"    N_Hopf + Q_top = {N_HOPF} + {int(Q_TOP)} = {N_HOPF+int(Q_TOP)}")
    print(f"    b₀_needed = {b0_needed:.6f}")
    print(f"    b₀(SU(3) pure) = 11")
    print(f"    |b₀_needed - 11| / 11 = {abs(b0_needed - 11)/11 * 100:.3f}%")
    print(f"    v (Formula A) = {v_su3_pure:.4f} GeV")
    print(f"    v error = {(v_su3_pure/V_EW-1)*100:+.4f}%")
    print(f"    c_needed = {c_needed:.4f}   (for α_D6 = M_c² × exp(-c/g²))")
    print(f"    8π²/5 = {8*PI2/5:.4f}  (Δ = {(8*PI2/5 - c_needed):.4f}, {(8*PI2/5/c_needed-1)*100:+.3f}%)")


if __name__ == "__main__":
    print("=" * 70)
    print("D6 GAUGE BETA FUNCTION SURVEY (Cycle 133)")
    print("Dimensional Folding Compression model")
    print("=" * 70)

    b0_I, b0_II, delta_I = required_b0()
    survey_gauge_theories()
    dfc_special_b0()
    formula_check()
    summary()
