"""
ECCC + 36π Self-Consistency: Joint prediction of α_em(0) and α_s(M_Z)
======================================================================

Physical question:
    The ECCC identity M_c(D7)/M_c(D5) = 1/α_em(0) connects the QCD and EM
    sectors. Combined with the 36π formula (Tier 2a) and Route 3B sin²θ_W,
    this forms a self-consistent DFC prediction for both α_em(0) and α_s(M_Z).

DFC mechanism:
    At D5 depth: α₁(M_c(D5)) = α_common.  At D7 depth: α₃(M_c(D7)) = α_common.
    ECCC ratio = M_c(D7)/M_c(D5) = exp(t₇ − t₅) where t_i are RG intervals.
    Structural identity (Cycle 137, Tier 1): exp(t₇−t₅) ≈ 1/α_em(0) (+0.044%).

    α₁(M_Z) is derived from the DFC coupling chain (g₂=0.5443→0.6514, sin²θ_W=0.2312)
    — NOT from the 36π α_em(M_Z) value. Using g₂ gives α₁ precisely; using the
    36π α_em(M_Z) introduces a small discrepancy (~0.01 in 1/α_em) that shifts
    the ECCC ratio from 0.044% error to 0.19% error.

    This 0.01 tension between the g₂-derived and 36π-derived α_em(M_Z) is the
    internal DFC inconsistency that keeps the α_em sector at Tier 2b rather than
    having a fully closed first-principles chain.

Key results (Cycle 144):
    DIRECTION A — given SM α_s → predict α_em(0) [uses g₂ for α₁]:
        1/α_em(0) = 136.976  (+0.044%, Tier 2b)
    DIRECTION B — given SM α_em(0) → predict α_s [uses g₂ for α₁]:
        α_s(M_Z) = 0.11821   (+0.006%, Tier 2a candidate)
        Closes the α_s gap from 8.1% (wrong M_c(D7) condition) to 0.006%.

    The 8.1% α_s error came from using α₁∩α₃ crossing for M_c(D7) instead
    of the correct ECCC condition α₃(M_c(D7)) = α_common.

Open (Tier 4):
    Prove that the 3-gen SM quantum numbers (from D6/D7 DFC topology) make
    the ECCC identity M_c(D7)/M_c(D5) = 1/α_em(0) exact — i.e., close the
    0.044% gap without using SM measurements as inputs.
    Equivalently: close the 0.01 tension between 36π and g₂ routes to α_em(M_Z).

References:
    - equations/alpha_em_eccc.py         (ECCC ratio, Cycle 139)
    - equations/alpha_em_prediction.py   (36π chain, Cycle 142)
    - equations/alpha_s_target.py        (α_s gap analysis, Cycle 119)
    - equations/d5_complex_from_instability.py  (g_eff²=8/27, Cycle 117)
"""

import math


# ─────────────────────────────────────────────────────────────────────────────
# DFC substrate constants
# ─────────────────────────────────────────────────────────────────────────────
R            = 27.0 * math.pi / 2.0   # 1/α_common, from V(φ), Tier 2a
B1           = 41.0 / 10.0            # U(1)_Y one-loop beta, 3-gen SM, Tier 1
B3           = 7.0                    # SU(3)_c one-loop beta, Nf=6, Tier 1
SIN2_W       = 0.2312                 # Route 3B, Tier 2a, <0.01%
COS2_W       = 1.0 - SIN2_W
G2_MZ        = 0.6514                 # DFC coupling chain, Tier 2b

# 36π prediction for α_em(M_Z) — Tier 2a, +0.15%
INV_AEM_MZ_36PI = 128.09

# SM/PDG reference values
ALPHA_S_OBS   = 0.11820
INV_AEM_0_OBS = 137.036
INV_AEM_MZ_SM = 127.9   # SM measured


def inv_alpha1_from_g2(g2=G2_MZ, sin2w=SIN2_W):
    """
    Derive 1/α₁(M_Z) from the DFC coupling chain (g₂) and Route 3B (sin²θ_W).
    This is the α₁ input used in the ECCC module (alpha_em_eccc.py).
    Non-circular: g₂ comes from V(φ)→g_eff→g₂ chain; does not use α_em(0).
    """
    alpha2  = g2**2 / (4.0 * math.pi)
    tan2_w  = sin2w / (1.0 - sin2w)
    alpha_Y = alpha2 * tan2_w
    alpha1  = (5.0/3.0) * alpha_Y
    return 1.0 / alpha1


def inv_alpha1_from_36pi(inv_aem_mz=INV_AEM_MZ_36PI, cos2w=COS2_W):
    """
    Derive 1/α₁(M_Z) from the 36π α_em(M_Z) and Route 3B sin²θ_W.
    Differs from g₂-route by ~0.01 in 1/α₁ — the source of internal tension.
    """
    return (3.0/5.0) * cos2w * inv_aem_mz


def eccc_predict(inv_a1, inv_as):
    """
    ECCC forward: given 1/α₁ and 1/α_s, return (exp(t7-t5), t5, t7).
    """
    t5 = (inv_a1 - R) * 2.0 * math.pi / B1
    t7 = (R - 1.0/inv_as) * 2.0 * math.pi / B3
    return math.exp(t7 - t5), t5, t7


def main():
    print()
    print("=" * 70)
    print("  ECCC + 36π SELF-CONSISTENCY  (Cycle 144)")
    print("=" * 70)
    print()

    inv_a1_g2   = inv_alpha1_from_g2()
    inv_a1_36pi = inv_alpha1_from_36pi()

    print("DFC inputs:")
    print(f"  R = 27π/2 = {R:.6f}   [1/α_common, V(φ), Tier 2a]")
    print(f"  sin²θ_W   = {SIN2_W}   [Route 3B, Tier 2a]")
    print(f"  g₂(M_Z)   = {G2_MZ}   [DFC coupling chain, Tier 2b]")
    print(f"  b₁ = {B1}, b₃ = {B3}   [3-gen SM, Tier 1]")
    print()
    print(f"Two routes to α₁(M_Z):")
    print(f"  From g₂ (ECCC route):  1/α₁ = {inv_a1_g2:.4f}")
    print(f"  From 36π (alt route):  1/α₁ = {inv_a1_36pi:.4f}")
    print(f"  Tension: {inv_a1_g2 - inv_a1_36pi:+.4f} in 1/α₁  ←  source of internal DFC inconsistency")
    print()

    # ─── DIRECTION A: α_s → α_em(0) ─────────────────────────────────────────
    print("-" * 70)
    print("DIRECTION A: SM α_s → predict α_em(0)  [uses g₂ for α₁]")
    print("-" * 70)
    eccc_A, t5_A, t7_A = eccc_predict(inv_a1_g2, ALPHA_S_OBS)
    err_A = 100.0 * (eccc_A / INV_AEM_0_OBS - 1.0)
    print(f"  1/α₁ (from g₂) = {inv_a1_g2:.4f}")
    print(f"  t5 = {t5_A:.5f},  t7 = {t7_A:.5f}")
    print(f"  ECCC ratio = exp(t7−t5) = {eccc_A:.4f}")
    print(f"  → 1/α_em(0) = {eccc_A:.4f}   (obs: {INV_AEM_0_OBS},  err: {err_A:+.3f}%)")
    print(f"  Tier: 2b  (0 DFC free params; α_s from SM)")
    print()

    # ─── DIRECTION B: α_em(0) → α_s ─────────────────────────────────────────
    print("-" * 70)
    print("DIRECTION B: SM α_em(0) → predict α_s(M_Z)  [uses g₂ for α₁]")
    print("-" * 70)
    # t5 same as above; t7 = t5 + ln(1/α_em(0)) if identity holds
    t7_B = t5_A + math.log(INV_AEM_0_OBS)
    inv_as_pred = R - t7_B * B3 / (2.0 * math.pi)
    as_pred = 1.0 / inv_as_pred
    err_B = 100.0 * (as_pred / ALPHA_S_OBS - 1.0)
    print(f"  t5 = {t5_A:.5f}  [same DFC-only inputs]")
    print(f"  t7 = t5 + ln(1/α_em(0)) = {t7_B:.5f}")
    print(f"  → α_s(M_Z) = {as_pred:.6f}   (obs: {ALPHA_S_OBS},  err: {err_B:+.3f}%)")
    print()
    print(f"  KEY RESULT: α_s gap 8.1% → {abs(err_B):.3f}%")
    print(f"  Old error: wrong M_c(D7) from α₁∩α₃ crossing condition.")
    print(f"  Correct ECCC condition α₃(M_c(D7)) = α_common → α_s <0.1%.")
    print(f"  Tier: 2a candidate  (0 DFC free params; α_em(0) from SM)")
    print()

    # ─── INTERNAL TENSION ────────────────────────────────────────────────────
    print("-" * 70)
    print("INTERNAL TENSION: 36π and g₂ routes to α_em(M_Z)")
    print("-" * 70)
    # g₂ implies α_em(M_Z):
    alpha_em_from_g2 = G2_MZ**2 * SIN2_W / (4.0 * math.pi)
    inv_aem_from_g2  = 1.0 / alpha_em_from_g2
    print(f"  36π chain:         1/α_em(M_Z) = {INV_AEM_MZ_36PI:.4f}  (+0.15% vs SM 1/127.9)")
    print(f"  g₂-implied:        1/α_em(M_Z) = {inv_aem_from_g2:.4f}  ({100*(inv_aem_from_g2/INV_AEM_MZ_SM-1):+.3f}% vs SM)")
    print(f"  SM observed:       1/α_em(M_Z) = {INV_AEM_MZ_SM}")
    print(f"  36π vs g₂:        Δ(1/α_em) = {INV_AEM_MZ_36PI - inv_aem_from_g2:+.4f}")
    print()
    print(f"  This 0.01 tension propagates to α₁, then to t₅, then to the ECCC ratio.")
    print(f"  Using 36π for α₁: ECCC ratio = {eccc_predict(inv_a1_36pi, ALPHA_S_OBS)[0]:.4f}  (+0.19%)")
    print(f"  Using g₂  for α₁: ECCC ratio = {eccc_A:.4f}  (−0.044%)")
    print()
    print(f"  Closing the internal tension would:")
    print(f"    (a) make the 36π chain exactly match the g₂ chain at α_em(M_Z), AND")
    print(f"    (b) close the ECCC residual 0.044% simultaneously.")
    print(f"  Algebraic route: derive WHY 36π × (EW correction) = g₂² × sin²θ_W/(4π)")
    print()

    # ─── SUMMARY ─────────────────────────────────────────────────────────────
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    w = 34
    print(f"  {'Prediction':<{w}} {'DFC':>10}  {'Obs':>10}  {'Err':>8}  Tier")
    print(f"  {'-'*w}  {'-'*10}  {'-'*10}  {'-'*8}  ----")
    print(f"  {'α_em(M_Z) [36π]':<{w}} {'1/128.09':>10}  {'1/127.9':>10}  {'+0.15%':>8}  2a")
    print(f"  {'α_em(M_Z) [g₂·sin²θ]':<{w}} {f'1/{inv_aem_from_g2:.2f}':>10}  {'1/127.9':>10}  {f'{100*(inv_aem_from_g2/127.9-1):+.2f}%':>8}  2b")
    print(f"  {'α_em(0) [ECCC, α_s input]':<{w}} {f'1/{eccc_A:.2f}':>10}  {'1/137.04':>10}  {f'{err_A:+.3f}%':>8}  2b")
    print(f"  {'α_s(M_Z) [ECCC, α_em(0) input]':<{w}} {f'{as_pred:.5f}':>10}  {'0.11820':>10}  {f'{err_B:+.3f}%':>8}  2a*")
    print()
    print(f"  * Tier 2a candidate: 0 DFC free params beyond SM α_em(0) input.")
    print(f"    Closes the α_s bottleneck: 8.1% off → 0.006% off.")
    print()
    print(f"  Internal DFC tension (Tier 4 open):")
    print(f"    36π ↔ g₂ route to α_em(M_Z) differ by 0.01 in 1/α_em.")
    print(f"    Resolving this closes BOTH the ECCC 0.044% gap AND")
    print(f"    the 0.15% discrepancy of the 36π chain simultaneously.")


if __name__ == "__main__":
    main()
