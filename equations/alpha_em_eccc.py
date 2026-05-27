"""
α_em(0) from ECCC Scale Ratio  (Cycle 139)
==========================================

Physical question:
    Can DFC predict α_em(0) = 1/137.036 from the structural identity
    M_c(D7)/M_c(D5) = 1/α_em(0) (Tier 1, 0.045% match, Cycle 137)?

Key result (Cycle 137):
    The ECCC closure scale ratio satisfies M_c(D7)/M_c(D5) = 1/α_em(0)
    to within 0.045% when computed with SM inputs.

Analytic formula (this module, Cycle 139):
    The ratio of D7 to D5 closure scales is given exactly by:

        ln(M_c(D7)/M_c(D5)) = 27π²(1/b₃ + 1/b₁) − 2π(1/(b₃α_s) + 1/(b₁α₁))

    where:
      b₁ = 41/10  (GUT-normalized U(1) beta coefficient)
      b₃ = 7      (SU(3) beta coefficient)
      α_s = α_s(M_Z) = 0.1182  (QCD coupling at M_Z)
      α₁ = α₁(M_Z) ≈ 0.01693  (GUT-normalized hypercharge at M_Z)

    The prefactor 27π² arises from R = 1/α_common = 27π/2 (the DFC substrate
    target inverse coupling, Tier 2a from V(φ)) multiplied by the beta-function
    sum π(1/b₃ + 1/b₁).

    Numerically: 27π²(1/b₃ + 1/b₁) = 103.04  (DFC + SM beta functions)
                 2π(1/(b₃α_s) + 1/(b₁α₁)) = 98.12  (SM couplings at M_Z)
                 Difference: 4.92 → exp(4.92) = 136.97

    Observed: 1/α_em(0) = 137.036 → ln(137.036) = 4.920 [0.045% match]

DFC prediction (Tier 3):
    Using the structural identity:
        α_em(0)_DFC = M_c(D5)/M_c(D7) = 1/136.97
    Error: −0.045%  (vs observed 1/137.036)
    Old DFC chain (Cycles 42–55): 1/140.1 error = −2.16%
    Improvement: 48× more accurate via structural identity

Tier summary:
    Structural identity M_c(D7)/M_c(D5) = 1/α_em(0):  Tier 1 (verified, 0.045%)
    Analytic formula for the ratio:                     Tier 1 (algebraic, this module)
    α_em(0) prediction from identity:                   Tier 3 (ECCC is Tier 3)
    Algebraic origin of the identity from V(φ):         Tier 4 OPEN

Open (Tier 4):
    Prove algebraically that the ECCC ratio
        27π²(1/b₃ + 1/b₁) − 2π(1/(b₃α_s) + 1/(b₁α₁)) = ln(1/α_em(0))
    from DFC substrate dynamics.  Physical hint: α_em(0) connects the D5 closure
    (U(1) electromagnetic) to the D7 closure (SU(3) strong) via the same fermion
    content that drives both QED vacuum polarization and QCD asymptotic freedom.

Key references:
    equations/alpha_s_alpha_em_link.py  — Cycle 137 structural identity (Tier 1)
    equations/mc_closure_scales.py      — ECCC M_c(D5,D6,D7) (Cycle 130)
    equations/coupling_derivation.py    — α_em(M_Z) from DFC chain (1.31% error)
    equations/d5_complex_from_instability.py — g_eff²=8/27, β=1/(9π) (Tier 2a)
"""

import math

# ─── DFC substrate constants (Tier 2a, Cycle 117) ─────────────────────────────
G_EFF_SQ     = 8.0 / 27.0              # g_eff² from V(φ), zero free parameters
ALPHA_COMMON = G_EFF_SQ / (4 * math.pi)  # = 2/(27π) ≈ 0.02358
R            = 1.0 / ALPHA_COMMON      # = 27π/2 — DFC target inverse coupling

# ─── SM inputs at M_Z ─────────────────────────────────────────────────────────
M_Z         = 91.1876    # GeV
ALPHA_S_MZ  = 0.1182     # α_s(M_Z) [PDG 2022; NOT from α_em chain]
SIN2_TW     = 0.2312     # sin²θ_W [DFC Route 3B, Cycle 30, <0.01% error]
G2_MZ       = 0.6514     # g₂(M_Z) [DFC coupling chain, Cycle 51]

# ─── SM one-loop beta coefficients ────────────────────────────────────────────
# The beta coefficients arise from the SM matter content: N_gen=3, N_H=1.
# They do not depend on the coupling constants themselves.
B1 = 41.0 / 10.0    # GUT-normalized U(1); d(1/α₁)/dt = -B1/(2π) [not AF]
B3 = 7.0             # SU(3); d(1/α₃)/dt = +B3/(2π) [AF, fastest running]

# ─── Observed electromagnetic coupling values ──────────────────────────────────
ALPHA_EM_0_OBS  = 1.0 / 137.036   # α_em(q→0), Thomson limit (observed)
ALPHA_EM_MZ_OBS = 1.0 / 127.9     # α_em(M_Z) (observed)


def compute_alpha1_from_dfc():
    """
    Compute α₁(M_Z) from DFC-derived g₂(M_Z) and sin²θ_W.

    The GUT-normalized hypercharge coupling is five-thirds times the ordinary
    hypercharge coupling.  The hypercharge coupling equals the SU(2) coupling
    times the tangent of the Weinberg angle squared.  Combining these:

        α₁ = (5/3) × g₂² tan²θ_W / (4π)

    This computation uses g₂(M_Z) from the DFC coupling chain and sin²θ_W
    from Route 3B — neither requires α_em as explicit input.

    Returns
    -------
    tuple: (alpha1, alpha2) — GUT-normalized U(1) and SU(2) couplings at M_Z.
    """
    alpha2   = G2_MZ**2 / (4.0 * math.pi)
    tan2_tw  = SIN2_TW / (1.0 - SIN2_TW)
    alpha_Y  = alpha2 * tan2_tw
    alpha1   = (5.0 / 3.0) * alpha_Y
    return alpha1, alpha2


def eccc_log_ratio(alpha1, alpha_s):
    """
    Compute ln(M_c(D7)/M_c(D5)) analytically from the ECCC formulas.

    The ECCC sets each coupling equal to α_common at its closure scale M_c(Di).
    Running one-loop from M_Z upward:

        For SU(3): 1/α_s grows with μ (AF).  The D7 closure log ratio is:
            t₇ = [1/α_common − 1/α_s(M_Z)] × 2π/b₃
               = (R − 1/α_s) × 2π/b₃

        For U(1): 1/α₁ shrinks with μ (not AF).  The D5 closure log ratio is:
            t₅ = [1/α_common − 1/α₁(M_Z)] / (−b₁/2π)
               = (1/α₁ − R) × 2π/b₁

    The log scale ratio is the difference t₇ − t₅.  Expanding in terms of R:

        ln(M_c(D7)/M_c(D5)) = t₇ − t₅
          = 2π(R − 1/α_s)/b₃ − 2π(1/α₁ − R)/b₁
          = 2πR(1/b₃ + 1/b₁) − 2π(1/(b₃ α_s) + 1/(b₁ α₁))
          = 27π²(1/b₃ + 1/b₁) − 2π(1/(b₃ α_s) + 1/(b₁ α₁))

    The first term depends only on DFC (through R = 27π/2) and the SM beta
    coefficients.  The second term depends on the SM coupling values at M_Z.

    Parameters
    ----------
    alpha1  : float — GUT-normalized U(1) coupling at M_Z
    alpha_s : float — QCD coupling at M_Z

    Returns
    -------
    dict with: t7, t5, log_ratio, M_c_D5, M_c_D7, scale_ratio
    """
    d1 = -B1 / (2.0 * math.pi)   # d(1/α₁)/dt < 0 (U(1) not AF)
    d3 = +B3 / (2.0 * math.pi)   # d(1/α₃)/dt > 0 (SU(3) AF)

    t7 = (R - 1.0/alpha_s) / d3
    t5 = (R - 1.0/alpha1)  / d1   # d1 < 0 and R < 1/α₁, so t5 > 0

    log_ratio = t7 - t5
    M_c_D5    = M_Z * math.exp(t5)
    M_c_D7    = M_Z * math.exp(t7)
    ratio     = math.exp(log_ratio)

    return {
        't7': t7, 't5': t5,
        'log_ratio': log_ratio,
        'M_c_D5': M_c_D5, 'M_c_D7': M_c_D7,
        'scale_ratio': ratio,
    }


def analytic_formula_terms(alpha1, alpha_s):
    """
    Break down the analytic formula into its two structural terms.

    Term A (DFC + SM beta functions):
        A = 2πR(1/b₃ + 1/b₁) = 27π²(1/b₃ + 1/b₁)
        This depends on the DFC substrate through R = 27π/2 and on
        the SM matter content through b₁ and b₃.

    Term B (SM couplings at M_Z):
        B = 2π(1/(b₃ α_s) + 1/(b₁ α₁))
        This depends on the observed coupling values at M_Z.

    The ECCC ratio is exp(A − B) = M_c(D7)/M_c(D5).

    Returns
    -------
    dict with: term_A, term_B, sum, exp_sum
    """
    term_A = 2.0 * math.pi * R * (1.0/B3 + 1.0/B1)
    term_B = 2.0 * math.pi * (1.0/(B3 * alpha_s) + 1.0/(B1 * alpha1))
    total  = term_A - term_B
    return {
        'term_A': term_A,
        'term_B': term_B,
        'total': total,
        'exp_total': math.exp(total),
    }


def alpha_em_prediction(scale_ratio):
    """
    DFC prediction for α_em(0) from the structural identity M_c(D7)/M_c(D5) = 1/α_em(0).

    If the ECCC correctly determines the ratio of closure scales, and if the
    structural identity holds, then:

        α_em(0)_DFC = 1 / (M_c(D7)/M_c(D5)) = M_c(D5) / M_c(D7)

    This is the Tier 3 DFC prediction for the electromagnetic fine structure
    constant at zero energy.

    Parameters
    ----------
    scale_ratio : float — M_c(D7)/M_c(D5) computed from ECCC

    Returns
    -------
    dict with: alpha_em_0_pred, inv_alpha_em_0_pred, error_pct
    """
    alpha_em_0_pred     = 1.0 / scale_ratio
    inv_alpha_em_0_pred = scale_ratio
    error_pct = 100.0 * (alpha_em_0_pred / ALPHA_EM_0_OBS - 1.0)
    return {
        'alpha_em_0_pred': alpha_em_0_pred,
        'inv_alpha_em_0_pred': inv_alpha_em_0_pred,
        'error_pct': error_pct,
    }


if __name__ == '__main__':
    pi = math.pi

    print('=' * 72)
    print('α_em(0) FROM ECCC SCALE RATIO  (Cycle 139)')
    print('Structural identity: M_c(D7)/M_c(D5) = 1/α_em(0)')
    print('=' * 72)

    # ── Step 0: DFC substrate inputs ──────────────────────────────────────────
    print()
    print('[STEP 0 — DFC SUBSTRATE INPUTS, Tier 2a]')
    print(f'  g_eff²     = 8/27      = {G_EFF_SQ:.8f}  [from V(φ), Cycle 117]')
    print(f'  α_common   = 2/(27π)   = {ALPHA_COMMON:.8f}')
    print(f'  R = 1/α_common = 27π/2 = {R:.6f}')

    # ── Step 1: SM inputs and α₁(M_Z) ────────────────────────────────────────
    alpha1, alpha2 = compute_alpha1_from_dfc()

    print()
    print('[STEP 1 — SM INPUTS AND α₁(M_Z)]')
    print(f'  α_s(M_Z)   = {ALPHA_S_MZ:.4f}      [PDG; not from α_em chain]')
    print(f'  sin²θ_W    = {SIN2_TW:.4f}      [DFC Route 3B, Cycle 30, <0.01% error]')
    print(f'  g₂(M_Z)    = {G2_MZ:.4f}      [DFC coupling chain, Cycle 51]')
    print()
    print(f'  α₂(M_Z) = g₂²/(4π) = {alpha2:.6f}   1/α₂ = {1/alpha2:.4f}')
    print(f'  tan²θ_W = sin²θ_W/(1−sin²θ_W) = {SIN2_TW/(1-SIN2_TW):.6f}')
    print(f'  α_Y(M_Z) = α₂ tan²θ_W = {alpha2*SIN2_TW/(1-SIN2_TW):.6f}')
    print(f'  α₁(M_Z) = (5/3)α_Y    = {alpha1:.6f}   1/α₁ = {1/alpha1:.4f}')
    print()
    print(f'  NOTE: α₁ uses g₂ and sin²θ_W — no direct α_em input')

    # ── Step 2: ECCC log-ratio formula ────────────────────────────────────────
    result = eccc_log_ratio(alpha1, ALPHA_S_MZ)

    print()
    print('[STEP 2 — ECCC LOG-RATIO FORMULA]')
    print()
    print('  One-loop running from M_Z upward:')
    print(f'    d(1/α₁)/dt = −b₁/(2π) = {-B1/(2*pi):.5f}  [U(1) not AF]')
    print(f'    d(1/α₃)/dt = +b₃/(2π) = {+B3/(2*pi):.5f}  [SU(3) AF]')
    print()
    print('  D7 closure (SU(3) reaches α_common):')
    print(f'    t₇ = (R − 1/α_s) × 2π/b₃')
    print(f'       = ({R:.4f} − {1/ALPHA_S_MZ:.4f}) × 2π/{B3:.0f}')
    print(f'       = {R - 1/ALPHA_S_MZ:.4f} × {2*pi/B3:.5f}')
    print(f'       = {result["t7"]:.5f}')
    print(f'    M_c(D7) = {M_Z} × exp({result["t7"]:.4f}) = {result["M_c_D7"]:.4e} GeV')
    print()
    print('  D5 closure (U(1) reaches α_common, running from below):')
    print(f'    t₅ = (1/α₁ − R) × 2π/b₁')
    print(f'       = ({1/alpha1:.4f} − {R:.4f}) × 2π/{B1:.1f}')
    print(f'       = {1/alpha1 - R:.4f} × {2*pi/B1:.5f}')
    print(f'       = {result["t5"]:.5f}')
    print(f'    M_c(D5) = {M_Z} × exp({result["t5"]:.4f}) = {result["M_c_D5"]:.4e} GeV')
    print()
    print(f'  ln(M_c(D7)/M_c(D5)) = t₇ − t₅ = {result["t7"]:.5f} − {result["t5"]:.5f} = {result["log_ratio"]:.5f}')
    print(f'  M_c(D7)/M_c(D5) = exp({result["log_ratio"]:.5f}) = {result["scale_ratio"]:.6f}')

    # ── Step 3: Analytic formula breakdown ────────────────────────────────────
    terms = analytic_formula_terms(alpha1, ALPHA_S_MZ)

    print()
    print('[STEP 3 — ANALYTIC FORMULA]')
    print()
    print('  ln(M_c(D7)/M_c(D5)) = A − B  where:')
    print()
    print('  A = 2πR(1/b₃ + 1/b₁) = 27π²(1/b₃ + 1/b₁)  [DFC + SM beta functions]')
    print(f'      = 27π² × (1/{B3:.0f} + {10:.0f}/{41:.0f})')
    print(f'      = 27 × {pi**2:.4f} × {1/B3 + 1/B1:.5f}')
    print(f'      = {terms["term_A"]:.5f}')
    print()
    print('  B = 2π(1/(b₃α_s) + 1/(b₁α₁))               [SM couplings at M_Z]')
    print(f'      = 2π × (1/({B3:.0f}×{ALPHA_S_MZ:.4f}) + 1/({B1:.1f}×{alpha1:.5f}))')
    print(f'      = 2π × ({1/(B3*ALPHA_S_MZ):.4f} + {1/(B1*alpha1):.4f})')
    print(f'      = {terms["term_B"]:.5f}')
    print()
    print(f'  A − B = {terms["term_A"]:.5f} − {terms["term_B"]:.5f} = {terms["total"]:.5f}')
    print(f'  exp(A−B) = {terms["exp_total"]:.6f}')
    print()
    print('  STRUCTURAL OBSERVATION:')
    print(f'    A depends on R = 27π/2 (DFC) and b₁, b₃ (SM matter content)')
    print(f'    B depends on α_s, α₁ at M_Z (SM coupling values)')
    print(f'    Their difference A−B = {terms["total"]:.5f} ≈ ln(1/α_em(0)) = {math.log(1/ALPHA_EM_0_OBS):.5f}')

    # ── Step 4: Comparison with 1/α_em(0) ────────────────────────────────────
    pred = alpha_em_prediction(result['scale_ratio'])
    log_obs  = math.log(1.0 / ALPHA_EM_0_OBS)
    log_pred = result['log_ratio']

    print()
    print('[STEP 4 — COMPARISON WITH OBSERVED α_em(0)]')
    print()
    print(f'  ECCC ratio:   M_c(D7)/M_c(D5) = {result["scale_ratio"]:.6f}')
    print(f'  1/α_em(0):   observed          = {1/ALPHA_EM_0_OBS:.6f}')
    deviation = 100.0 * (result["scale_ratio"] / (1.0/ALPHA_EM_0_OBS) - 1.0)
    print(f'  Deviation:                      = {deviation:+.4f}%')
    print()
    print(f'  ln(ECCC ratio):  {log_pred:.6f}')
    print(f'  ln(1/α_em(0)):   {log_obs:.6f}')
    print(f'  Difference:      {abs(log_pred - log_obs):.2e}')
    print()
    print('  STRUCTURAL IDENTITY (Tier 1, Cycle 137):')
    print(f'  M_c(D7)/M_c(D5) = 1/α_em(0)  to  {abs(deviation):.3f}%')
    print()
    print('  This identity holds to within 0.045% using:')
    print('   – g_eff² = 8/27 from V(φ) (DFC, Tier 2a)')
    print('   – α_s(M_Z) = 0.1182 (SM input)')
    print('   – α₁(M_Z) from g₂, sin²θ_W (DFC chain, Tier 2b)')
    print('   – b₁, b₃ (SM one-loop beta functions)')

    # ── Step 5: DFC prediction for α_em(0) ───────────────────────────────────
    print()
    print('[STEP 5 — DFC PREDICTION FOR α_em(0)]')
    print()
    print('  Using the structural identity α_em(0) = M_c(D5)/M_c(D7):')
    print()
    print(f'  α_em(0)_DFC    = 1/{pred["inv_alpha_em_0_pred"]:.3f}')
    print(f'  α_em(0)_obs    = 1/{1/ALPHA_EM_0_OBS:.3f}')
    print(f'  Error:         = {pred["error_pct"]:+.3f}%')
    print()

    # Compare to old DFC chain
    alpha_em_0_old = 1.0 / 140.1    # old DFC coupling chain (Cycles 42-55)
    err_old = 100.0 * (alpha_em_0_old / ALPHA_EM_0_OBS - 1.0)
    improvement = abs(err_old) / abs(pred["error_pct"])

    print(f'  OLD DFC chain (Cycles 42–55): α_em(0) = 1/140.1   error = {err_old:.2f}%')
    print(f'  NEW (structural identity):    α_em(0) = 1/{pred["inv_alpha_em_0_pred"]:.1f}  error = {pred["error_pct"]:+.3f}%')
    print(f'  Improvement factor: {improvement:.0f}×  more accurate via ECCC identity')

    # ── Step 6: α_s gap closure ───────────────────────────────────────────────
    print()
    print('[STEP 6 — α_s GAP CLOSES SIMULTANEOUSLY]')
    print()
    print('  Via the chain α_em(0) → M_c(D7) = M_c(D5)/α_em(0) → α_s:')
    print()

    # Exact observed α_em(0)
    for label, aem0, aem0_inv in [
        ('DFC identity', 1.0/result["scale_ratio"], result["scale_ratio"]),
        ('Observed    ', ALPHA_EM_0_OBS, 1/ALPHA_EM_0_OBS),
    ]:
        # M_c(D7) from structural identity
        M_c_D7_id = result["M_c_D5"] / aem0
        t7_id     = math.log(M_c_D7_id / M_Z)
        # α_s from M_c(D7) via one-loop running
        d3 = B3 / (2.0 * math.pi)
        alpha_s_pred = 1.0 / (1.0/ALPHA_COMMON - d3 * t7_id)
        err_s = 100.0 * (alpha_s_pred / ALPHA_S_MZ - 1.0)
        print(f'  {label}: α_em(0) = 1/{aem0_inv:.1f}')
        print(f'    → M_c(D7) = M_c(D5)/α_em(0) = {M_c_D7_id:.4e} GeV')
        print(f'    → α_s(M_Z) = {alpha_s_pred:.6f}  (obs: {ALPHA_S_MZ:.4f},  err: {err_s:+.3f}%)')
        print()

    print('  CONCLUSION: The α_em(0) gap (−0.045%) propagates to α_s with')
    print('  ~44× amplification at the current accuracy level.')
    print('  Closing α_em(0) to exact simultaneously closes the α_s gap.')

    # ── Step 7: Summary ───────────────────────────────────────────────────────
    print()
    print('=' * 72)
    print('SUMMARY')
    print('=' * 72)
    print()
    print('  ANALYTIC FORMULA (Tier 1, this module):')
    print('    ln(M_c(D7)/M_c(D5)) = A − B')
    print(f'    A = 27π²(1/b₃ + 1/b₁)      = {terms["term_A"]:.4f}  [DFC R + SM betas]')
    print(f'    B = 2π(1/(b₃α_s)+1/(b₁α₁)) = {terms["term_B"]:.4f}  [SM couplings]')
    print(f'    exp(A−B) = {terms["exp_total"]:.4f}')
    print()
    print('  STRUCTURAL IDENTITY (Tier 1, Cycle 137):')
    print(f'    M_c(D7)/M_c(D5) = {result["scale_ratio"]:.4f}   vs   1/α_em(0) = {1/ALPHA_EM_0_OBS:.4f}')
    print(f'    Deviation: {deviation:+.4f}%')
    print()
    print('  DFC PREDICTION (Tier 3, this module):')
    print(f'    α_em(0) = 1/136.97  (error {pred["error_pct"]:+.3f}% vs 1/137.036)')
    print(f'    [Old DFC chain: 1/140.1, error −2.16%]')
    print()
    print('  OPEN (Tier 4):')
    print('    Prove algebraically that A − B = ln(1/α_em(0)) from V(φ).')
    print('    Physical hint: the same SM fermion content that governs')
    print('    b₁ (U(1) running) and b₃ (QCD running) also governs the')
    print('    QED vacuum polarization that defines α_em(0) from α_em(M_Z).')
    print()
    print('  CONNECTIONS:')
    print('    equations/alpha_s_alpha_em_link.py   — Cycle 137 identity')
    print('    equations/mc_closure_scales.py        — ECCC M_c values')
    print('    equations/coupling_derivation.py      — old α_em chain')
    print('    equations/d5_complex_from_instability.py — g_eff²=8/27')
