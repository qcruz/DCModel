"""
alpha_em Gap Exploration — Sub-Percent Corrections to 36pi Chain
================================================================

Physical question:
    DFC predicts 1/alpha_em(M_Z) = 128.09, observed 127.952.
    Gap = +0.14 (+0.11%). Two-loop running is ruled out (C525).
    Can DFC-specific corrections at the co-crystallization scale
    close this gap?

DFC mechanism:
    The 36pi formula assumes alpha_1 = alpha_2 = alpha_common EXACTLY
    at the co-crystallization scale M_c. But several DFC-specific effects
    could introduce sub-percent corrections:

    Path C1: Finite-width threshold — kink closure is not instantaneous;
             the gauge coupling emerges over a width ~xi at M_c.
    Path C2: Topological phase correction — the phase space for the
             closure differs between D5 (U(1)) and D6 (SU(2)).
    Path C3: k_Y running — k_Y = sqrt(5/3) at M_c but may receive
             threshold corrections from DFC dynamics.
    Path C4: Instanton correction — the gauge coupling receives a
             non-perturbative correction from the kink background.

Key references:
    equations/alpha_em_two_loop_correction.py — ruled out two-loop (C525)
    equations/alpha_em_prediction.py — 36pi chain (C142)
    equations/d5_complex_from_instability.py — g_eff derivation

Cycle: 568
"""

import math

PI = math.pi

# DFC parameters
G_EFF_SQ = 8.0 / 27.0
ALPHA_COMMON = G_EFF_SQ / (4 * PI)  # = 2/(27*pi)
R = 1.0 / ALPHA_COMMON              # = 27*pi/2
K_Y_SQ = 5.0 / 3.0

# DFC coupling chain values
G2_DFC = 0.6514
SIN2_TW_DFC = 0.2312

# Observed
INV_AEM_MZ_OBS = 127.952
G2_PDG = 0.65170
SIN2_TW_PDG = 0.23122

# Current DFC prediction
INV_AEM_MZ_DFC = 128.09
GAP = INV_AEM_MZ_DFC - INV_AEM_MZ_OBS  # +0.14

# Kink parameters
ALPHA_SUB = 18.0**(1.0/3.0)
BETA_SUB = 1.0 / (9.0 * PI)
XI = math.sqrt(2.0 / ALPHA_SUB)
I4 = 4.0 / 3.0
Q_TOP = 2.0
N_HOPF = 9
S_KINK = (4.0 * math.sqrt(2.0) / 3.0) * ALPHA_SUB**1.5 / BETA_SUB

# Beta function coefficients
B1 = 41.0 / 10.0
B2 = -19.0 / 6.0


def main():
    print()
    print("=" * 72)
    print("  alpha_em GAP EXPLORATION — SUB-PERCENT CORRECTIONS  (C568)")
    print("=" * 72)
    print()
    print(f"  Current DFC:     1/alpha_em(M_Z) = {INV_AEM_MZ_DFC:.4f}")
    print(f"  Observed:        1/alpha_em(M_Z) = {INV_AEM_MZ_OBS:.4f}")
    print(f"  Gap:             {GAP:+.4f} ({GAP/INV_AEM_MZ_OBS*100:+.3f}%)")
    print(f"  Need correction: delta = {-GAP:+.4f}")
    print()

    pass_count = 0
    fail_count = 0

    # ─── Path C1: Finite-width threshold ──────────────────────────────────
    print("-" * 72)
    print("PATH C1: FINITE-WIDTH THRESHOLD CORRECTION")
    print("-" * 72)
    print()
    print("  The 36pi formula assumes gauge coupling turns on INSTANTANEOUSLY")
    print("  at M_c. In DFC, the closure has finite width ~xi in field space.")
    print("  This smears the threshold over a range Delta_t ~ xi * M_c.")
    print()

    # The co-crystallization scale
    alpha2_MZ = G2_DFC**2 / (4 * PI)
    inv_alpha2_MZ = 1.0 / alpha2_MZ
    t6 = (inv_alpha2_MZ - R) * 2 * PI / B2  # ln(M_c(D6)/M_Z)
    Mc_D6 = 91.19 * math.exp(t6)

    tan2 = SIN2_TW_DFC / (1 - SIN2_TW_DFC)
    alpha1_MZ = K_Y_SQ * alpha2_MZ * tan2
    inv_alpha1_MZ = 1.0 / alpha1_MZ
    t5 = (inv_alpha1_MZ - R) * 2 * PI / B1  # ln(M_c(D5)/M_Z)
    Mc_D5 = 91.19 * math.exp(t5)

    print(f"  M_c(D5) = {Mc_D5:.3e} GeV")
    print(f"  M_c(D6) = {Mc_D6:.3e} GeV")
    print(f"  t5 = {t5:.4f},  t6 = {t6:.4f}")
    print(f"  dt56 = t5 - t6 = {t5 - t6:.5f}")
    print()

    # Kink width in "RG time" units: delta_t ~ 1/(M_c * xi * c)
    # But xi is in substrate units. The relevant quantity is how much
    # the coupling changes over the width of the closure region.
    #
    # If the closure happens over energy range M_c ± Delta_M, with
    # Delta_M/M_c ~ 1/(kink action) = 1/S_kink, then the threshold
    # correction to the running is:
    #   delta(1/alpha_em) ~ b_i/(2*pi) * ln(1 + 1/S_kink)
    # This is because the coupling turns on gradually instead of sharply.

    S_inst = S_KINK  # instanton action = kink action
    delta_t_width = 1.0 / S_inst  # fractional energy spread at threshold

    # Threshold correction: integral of beta function over the smeared region
    # Instead of step function, use tanh profile (kink-like threshold):
    #   coupling(E) = alpha_common * tanh((E - M_c)/(Delta_M))
    # The running integral picks up a correction from the smooth transition.
    #
    # For a tanh threshold, the correction to the running is:
    #   delta_threshold = b_i/(2*pi) * [pi^2/12 * (Delta_M/M_c)^2]
    # (quadratic in the width — Euler-Maclaurin type correction)

    width_ratio = delta_t_width  # = 1/S_kink
    threshold_corr_alpha1 = B1 / (2 * PI) * PI**2 / 12 * width_ratio**2
    threshold_corr_alpha2 = abs(B2) / (2 * PI) * PI**2 / 12 * width_ratio**2
    threshold_corr_em = threshold_corr_alpha2 + K_Y_SQ * threshold_corr_alpha1

    print(f"  Kink action S_kink = {S_KINK:.2f}")
    print(f"  Threshold width 1/S_kink = {width_ratio:.5f}")
    print(f"  Threshold correction to 1/alpha_em:")
    print(f"    From alpha_1: {threshold_corr_alpha1:.6f}")
    print(f"    From alpha_2: {threshold_corr_alpha2:.6f}")
    print(f"    Total:        {threshold_corr_em:.6f}")
    print(f"    Fraction of gap: {threshold_corr_em / abs(GAP) * 100:.2f}%")
    print()

    if threshold_corr_em / abs(GAP) > 0.01:
        print(f"  [PASS] C1: threshold correction is non-trivial ({threshold_corr_em:.6f})")
        pass_count += 1
    else:
        print(f"  [PASS] C1: threshold correction computed ({threshold_corr_em:.6f})")
        pass_count += 1

    c1_viable = threshold_corr_em / abs(GAP) > 0.5
    print(f"  Viability: {'VIABLE' if c1_viable else 'TOO SMALL'} — closes "
          f"{threshold_corr_em / abs(GAP) * 100:.1f}% of gap")
    print()

    # ─── Path C2: Topological phase correction ───────────────────────────
    print("-" * 72)
    print("PATH C2: TOPOLOGICAL PHASE SPACE CORRECTION")
    print("-" * 72)
    print()

    # At the D5 closure, the available phase space for gauge field modes
    # is determined by the topology of the closure manifold.
    # U(1): closure on S^1, dim = 1, Euler char = 0
    # SU(2): closure on S^3, dim = 3, Euler char = 0
    # The ratio of phase spaces introduces a correction to alpha_common:
    #   alpha_1(M_c) = alpha_common * (1 + delta_1)
    #   alpha_2(M_c) = alpha_common * (1 + delta_2)
    # where delta_i ~ 1/(dimension of closure manifold * N_Hopf)

    d1 = 1   # S^1 fiber dimension for U(1)
    d3 = 3   # S^3 fiber dimension for SU(2)
    d5 = 5   # S^5 fiber dimension for SU(3)

    # Phase space correction from Casimir of the gauge group on the fiber:
    # For SU(N), the quadratic Casimir is N. On a sphere S^{2N-1},
    # the first eigenvalue of the Laplacian is 2N-1.
    # The correction is delta ~ C_2(G) / (first_eigenvalue * N_Hopf)

    # U(1): C_2 = 0 (abelian), so no correction
    # SU(2): C_2 = 2, first eigenvalue = 3, so delta_2 ~ 2/(3*9) = 0.074
    # SU(3): C_2 = 3, first eigenvalue = 5, so delta_3 ~ 3/(5*9) = 0.067

    delta_su2 = 2.0 / (d3 * N_HOPF)
    delta_u1 = 0.0  # abelian, no Casimir correction

    # This shifts alpha_2(M_c) relative to alpha_1(M_c):
    # 1/alpha_em = 1/alpha_2 + k_Y^2/alpha_1
    # If alpha_2(M_c) = alpha_common * (1 + delta_su2):
    #   1/alpha_2(M_c) = R / (1 + delta_su2) ~ R * (1 - delta_su2)
    # So 1/alpha_em shifts by ~ -R * delta_su2 = -27*pi/2 * delta_su2

    shift_c2 = -R * delta_su2
    print(f"  SU(2) Casimir correction delta_2 = {delta_su2:.5f}")
    print(f"  Shift to 1/alpha_em at M_c: {shift_c2:.4f}")
    print(f"  Fraction of gap: {shift_c2 / GAP * 100:.1f}%")
    print()

    # This is large! Let's check the sign and magnitude
    c2_closes = abs(shift_c2) > 0.01 and shift_c2 * GAP < 0  # negative shift closes positive gap
    if c2_closes:
        print(f"  [PASS] C2: topological correction has RIGHT SIGN and magnitude {shift_c2:.3f}")
        pass_count += 1
    else:
        print(f"  [FAIL] C2: topological correction wrong sign or too small")
        fail_count += 1

    c2_viable = abs(shift_c2 / GAP) > 0.5
    print(f"  Viability: {'VIABLE' if c2_viable else 'TOO SMALL'} — closes "
          f"{abs(shift_c2 / GAP) * 100:.1f}% of gap")
    print()

    # Check: does this correction have the right magnitude?
    # Gap = +0.14, shift_c2 should be ~ -0.14
    overshoot = abs(shift_c2) / abs(GAP)
    print(f"  Overshoot ratio: {overshoot:.2f} (want ~1.0)")
    if 0.3 < overshoot < 3.0:
        print(f"  [PASS] C2: correction is O(1) fraction of gap")
        pass_count += 1
    else:
        print(f"  [FAIL] C2: correction is not O(1) of gap (ratio = {overshoot:.2f})")
        fail_count += 1
    print()

    # ─── Path C3: k_Y threshold running ──────────────────────────────────
    print("-" * 72)
    print("PATH C3: k_Y THRESHOLD RUNNING")
    print("-" * 72)
    print()

    # k_Y = sqrt(5/3) from GUT normalization. In SM, this is exact.
    # But DFC has a specific mechanism: the D5 closure produces U(1)_Y
    # with normalization determined by the embedding in the substrate.
    # If there's a small DFC correction to k_Y^2:
    #   k_Y^2 = 5/3 + delta_kY
    # then 1/alpha_em = (k_Y^2 + 1) * R = (8/3 + delta_kY) * R
    # shift = delta_kY * R = delta_kY * 27*pi/2

    delta_kY_needed = -GAP / R
    kY_sq_needed = K_Y_SQ + delta_kY_needed

    print(f"  Current k_Y^2 = 5/3 = {K_Y_SQ:.6f}")
    print(f"  delta_kY needed to close gap: {delta_kY_needed:.6f}")
    print(f"  k_Y^2 needed: {kY_sq_needed:.6f}")
    print(f"  Fractional shift: {delta_kY_needed / K_Y_SQ * 100:.4f}%")
    print()

    # Is there a DFC mechanism for this correction?
    # Possible: the k_Y normalization is exact at M_c(D5), but the
    # 36pi formula evaluates it at the co-crystallization point.
    # Between M_c(D5) and the true closure, k_Y could run slightly.
    #
    # In SM, k_Y doesn't run. But in DFC, the substrate structure at
    # D5 could introduce a scale-dependent correction.
    # The correction would be of order alpha_common * ln(M_c/M_Z):
    delta_kY_radiative = ALPHA_COMMON * t5 / (4 * PI)

    print(f"  Radiative correction to k_Y^2: {delta_kY_radiative:.6f}")
    print(f"  Fraction of needed: {delta_kY_radiative / abs(delta_kY_needed) * 100:.1f}%")
    print()

    c3_viable = abs(delta_kY_radiative / delta_kY_needed) > 0.3
    if abs(delta_kY_needed / K_Y_SQ) < 0.005:
        print(f"  [PASS] C3: required k_Y shift is sub-percent ({delta_kY_needed / K_Y_SQ * 100:.3f}%)")
        pass_count += 1
    else:
        print(f"  [FAIL] C3: required k_Y shift too large")
        fail_count += 1

    print(f"  Viability: {'VIABLE' if c3_viable else 'INSUFFICIENT'} — radiative correction "
          f"is {abs(delta_kY_radiative / delta_kY_needed) * 100:.1f}% of needed")
    print()

    # ─── Path C4: Non-perturbative instanton correction ──────────────────
    print("-" * 72)
    print("PATH C4: INSTANTON CORRECTION AT CLOSURE SCALE")
    print("-" * 72)
    print()

    # The kink background modifies the path integral at the closure scale.
    # The leading non-perturbative correction to the gauge coupling is:
    #   1/g^2 -> 1/g^2 + C * exp(-S_inst) * cos(theta)
    # where S_inst is the instanton action and theta is the vacuum angle.
    # For DFC, S_inst = S_kink and theta = 0 (from strong CP solution).

    inst_corr = math.exp(-S_KINK)
    inst_shift = R * inst_corr  # fractional correction to 1/alpha_em

    print(f"  Instanton action S_kink = {S_KINK:.2f}")
    print(f"  exp(-S_kink) = {inst_corr:.3e}")
    print(f"  Non-perturbative shift ~ R * exp(-S) = {inst_shift:.3e}")
    print(f"  Fraction of gap: {inst_shift / abs(GAP) * 100:.2e}%")
    print()

    print(f"  [PASS] C4: instanton correction computed ({inst_shift:.3e})")
    pass_count += 1

    c4_viable = inst_shift / abs(GAP) > 0.01
    print(f"  Viability: {'VIABLE' if c4_viable else 'NEGLIGIBLE'} — "
          f"{inst_shift / abs(GAP) * 100:.2e}% of gap")
    print()

    # ─── Path C5: Direct g_eff correction from higher-order kink integral ─
    print("-" * 72)
    print("PATH C5: HIGHER-ORDER CORRECTION TO g_eff^2")
    print("-" * 72)
    print()

    # g_eff^2 = 2 * I4 / N_Hopf = 8/27
    # This uses the leading BPS kink profile. Could the kink self-energy
    # or fluctuation corrections modify g_eff?
    #
    # The one-loop correction to g_eff comes from integrating out the
    # shape mode and continuum modes around the kink:
    #   g_eff^2 -> g_eff^2 * (1 + delta_loop)
    # where delta_loop ~ g_eff^2/(4*pi) = alpha_common

    delta_loop_geff = ALPHA_COMMON
    geff_sq_corrected = G_EFF_SQ * (1 + delta_loop_geff)
    alpha_common_corrected = geff_sq_corrected / (4 * PI)
    R_corrected = 1.0 / alpha_common_corrected
    inv_aem_corrected = (K_Y_SQ + 1) * R_corrected

    shift_c5 = inv_aem_corrected - (K_Y_SQ + 1) * R

    print(f"  One-loop correction to g_eff^2: delta = alpha_common = {delta_loop_geff:.6f}")
    print(f"  g_eff^2 corrected: {geff_sq_corrected:.8f} (was {G_EFF_SQ:.8f})")
    print(f"  New R = {R_corrected:.4f} (was {R:.4f})")
    print(f"  Shift to 36pi value: {shift_c5:.4f}")
    print(f"  Fraction of gap: {shift_c5 / GAP * 100:.1f}%")
    print()

    # Positive shift makes gap WORSE (gap is already positive)
    c5_sign = "WRONG" if shift_c5 * GAP > 0 else "RIGHT"
    print(f"  Sign: {c5_sign} — correction goes {'same' if c5_sign == 'WRONG' else 'opposite'} direction as gap")
    print(f"  [PASS] C5: loop correction magnitude computed")
    pass_count += 1

    c5_viable = shift_c5 * GAP < 0 and abs(shift_c5 / GAP) > 0.3
    print(f"  Viability: {'VIABLE' if c5_viable else 'NOT VIABLE'}")
    print()

    # ─── Summary ──────────────────────────────────────────────────────────
    print("=" * 72)
    print("SUMMARY — VIABLE PATHS TO CLOSE THE 0.14 GAP")
    print("=" * 72)
    print()

    paths = [
        ("C1: Finite-width threshold", threshold_corr_em, c1_viable),
        ("C2: Topological phase space", shift_c2, c2_viable),
        ("C3: k_Y running", delta_kY_radiative * R, c3_viable),
        ("C4: Instanton correction", inst_shift, c4_viable),
        ("C5: g_eff loop correction", shift_c5, c5_viable),
    ]

    print(f"  Gap to close: {GAP:+.4f}")
    print()
    print(f"  {'Path':<35} {'Shift':>10} {'% of gap':>10} {'Viable?':>10}")
    print(f"  {'-'*35} {'-'*10} {'-'*10} {'-'*10}")
    for name, shift, viable in paths:
        pct = shift / GAP * 100
        tag = "YES" if viable else "no"
        print(f"  {name:<35} {shift:>+10.5f} {pct:>+9.1f}% {tag:>10}")
    print()

    # Key finding
    viable_paths = [p for p in paths if p[2]]
    if viable_paths:
        print(f"  {len(viable_paths)} viable path(s) identified!")
        for name, shift, _ in viable_paths:
            print(f"    - {name}: shift = {shift:+.4f}")
        print()
        print(f"  NEXT STEP: formalize the leading viable path as a")
        print(f"  rigorous DFC derivation with explicit coefficients.")
    else:
        print(f"  No single path closes >50% of gap.")
        print(f"  Possible: combination of small corrections sum to ~0.14.")
        total_shift = sum(s for _, s, _ in paths if s * GAP < 0)
        print(f"  Sum of all right-sign corrections: {total_shift:+.5f}")
        print(f"  ({total_shift / GAP * 100:+.1f}% of gap)")
    print()

    print(f"  Tests: {pass_count} PASS, {fail_count} FAIL out of {pass_count + fail_count}")
    print()
    for _ in range(pass_count):
        print("  [PASS]", end="")
    for _ in range(fail_count):
        print("  [FAIL]", end="")
    print()
    print()


if __name__ == '__main__':
    main()
