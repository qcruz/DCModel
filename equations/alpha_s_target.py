"""
Strong coupling constant α_s(M_Z): target M_c(D7) calculation.

PHYSICAL QUESTION:
  What value of M_c(D7) — the D7 closure scale — reproduces the observed
  strong coupling constant α_s(M_Z) = 0.1182, given the DFC common coupling
  g_common = √(8πβ/3) at the closure scale?

DFC MECHANISM:
  1. All three gauge closures (D5, D6, D7) emerge from the same substrate.
  2. Equal-coupling initial condition: g₃(M_c(D7)) = g_common = √(8πβ/3).
  3. SM one-loop RG running from M_c(D7) down to M_Z gives α_s(M_Z).
  4. The current M_c(D7) estimate (8×10¹⁴ GeV from equal-coupling crossing)
     gives α_s(M_Z) = 0.1049 — 11% below the observed 0.1182.
  5. This module computes the target M_c(D7) that closes the gap.

KEY REFERENCES:
  - foundations/alpha_s_derivation.md  (full formal analysis of the gap)
  - foundations/coupling_derivation.md  (g² = 8πβ/3 derivation)
  - foundations/depth_running.md        (two-scale model; M_c(D7) not derived)
  - equations/coupling_derivation.py    (coupling chain from β)
  - equations/gauge_couplings.py        (SM RG running; M_c crossing)

Usage:
    python3 equations/alpha_s_target.py
"""

import math

# ─── Physical Constants ──────────────────────────────────────────────────────

MZ_GEV        = 91.1876   # GeV  [Z boson mass]
ALPHA_S_OBS   = 0.1182    # observed α_s(M_Z)  [PDG 2024]

# ─── DFC Parameters ──────────────────────────────────────────────────────────

BETA          = 0.0351    # substrate quartic coupling [Tier 3 reference value]

# g_common² = 8πβ/3
G_COMMON_SQ   = 8 * math.pi * BETA / 3.0
G_COMMON      = math.sqrt(G_COMMON_SQ)
ALPHA_COMMON  = G_COMMON_SQ / (4 * math.pi)   # ≈ 0.02344

# Current M_c(D7) estimate: equal-coupling crossing in SM running
MC_D7_CURRENT = 8.0e14    # GeV  [from gauge_couplings.py α₁∩α₃ crossing]

# SM one-loop SU(3) beta function coefficient
# Positive = asymptotically free (coupling weakens at high energy)
# 1/α_s(M_Z) = 1/α_s(M_c) − [b₃/(2π)] × ln(M_c/M_Z)
B3            = 7.0        # SM one-loop SU(3) coefficient


# ─── Core Functions ───────────────────────────────────────────────────────────

def alpha_s_at_mz(mc_d7_gev, alpha_common=ALPHA_COMMON, b3=B3, mz=MZ_GEV):
    """
    Compute α_s(M_Z) from M_c(D7) using one-loop RG running.

    The inverse of the strong coupling at M_Z equals the inverse at the
    D7 closure scale minus the product of the one-loop beta coefficient
    (b₃ = 7) divided by two pi, times the log of the scale ratio.

    Parameters
    ----------
    mc_d7_gev    : float  D7 closure scale in GeV.
    alpha_common : float  Strong coupling at M_c(D7) [= g_common²/(4π)].
    b3           : float  One-loop SU(3) beta function coefficient.
    mz           : float  Z boson mass in GeV.

    Returns
    -------
    float  α_s(M_Z), or None if Landau pole reached.
    """
    if mc_d7_gev <= mz:
        return None  # scale below M_Z — formula not applicable
    inv_alpha_mc = 1.0 / alpha_common
    ln_ratio = math.log(mc_d7_gev / mz)
    inv_alpha_mz = inv_alpha_mc - (b3 / (2.0 * math.pi)) * ln_ratio
    if inv_alpha_mz <= 0:
        return None  # would hit Landau pole
    return 1.0 / inv_alpha_mz


def find_target_mc_d7(alpha_s_target=ALPHA_S_OBS, alpha_common=ALPHA_COMMON,
                      b3=B3, mz=MZ_GEV):
    """
    Solve for M_c(D7) that gives α_s(M_Z) = alpha_s_target.

    The target scale satisfies:
      1/alpha_s_target = 1/alpha_common − [b3/(2π)] × ln(M_c/M_Z)
    Solving:
      ln(M_c/M_Z) = [1/alpha_common − 1/alpha_s_target] / [b3/(2π)]
      M_c = M_Z × exp(ln ratio)

    Returns
    -------
    float  Target M_c(D7) in GeV.
    """
    inv_diff = 1.0 / alpha_common - 1.0 / alpha_s_target
    b3_factor = b3 / (2.0 * math.pi)
    ln_ratio = inv_diff / b3_factor
    return mz * math.exp(ln_ratio)


def alpha_s_running_table(mc_d7_gev, scales_gev=None):
    """
    Compute α_s at multiple scales from M_c(D7) via one-loop running.

    This allows comparison with lattice QCD measurements of α_s at
    various scales (m_b, m_c, 2 GeV, etc.).

    Parameters
    ----------
    mc_d7_gev  : float         D7 closure scale.
    scales_gev : list of float  Scales at which to evaluate α_s.

    Returns
    -------
    list of (scale_gev, alpha_s, alpha_s_obs_if_available)
    """
    if scales_gev is None:
        scales_gev = [MZ_GEV, 10.0, 4.18, 3.0, 2.0, 1.5]

    # Observed values at selected scales (PDG 2024 / FLAG 2022 averages)
    obs_dict = {
        MZ_GEV: 0.1182,
        10.0:   None,
        4.18:   0.1147,   # m_b [PDG 2024 running from M_Z]
        3.0:    None,
        2.0:    0.1185,   # rough lattice average ~2 GeV
        1.5:    None,
    }

    results = []
    for scale in scales_gev:
        a_s = alpha_s_at_mz(mc_d7_gev, alpha_common=ALPHA_COMMON,
                             b3=B3, mz=scale)
        obs = obs_dict.get(scale)
        results.append((scale, a_s, obs))
    return results


# ─── Main Output ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 68)
    print("α_s(M_Z) TARGET CALCULATION")
    print("Goal: find M_c(D7) that gives α_s(M_Z) = 0.1182")
    print("=" * 68)

    print("\n--- DFC Common Coupling from β ---")
    print(f"  β         = {BETA:.4f}  [quartic coupling — Tier 3 reference value]")
    print(f"  g_common² = 8πβ/3 = {G_COMMON_SQ:.5f}")
    print(f"  g_common  = {G_COMMON:.4f}")
    print(f"  α_common  = g²/(4π) = {ALPHA_COMMON:.5f}   [= 1/{1/ALPHA_COMMON:.2f}]")
    print(f"  [This is α_s at the D7 closure scale under equal-coupling IC]")

    print("\n--- Current Status: M_c(D7) from SM crossing ---")
    alpha_s_current = alpha_s_at_mz(MC_D7_CURRENT)
    err_current = 100 * (alpha_s_current / ALPHA_S_OBS - 1)
    print(f"  M_c(D7) current   = {MC_D7_CURRENT:.2e} GeV  [α₁∩α₃ crossing, gauge_couplings.py]")
    print(f"  α_s(M_Z) current  = {alpha_s_current:.4f}  (DFC prediction)")
    print(f"  α_s(M_Z) observed = {ALPHA_S_OBS:.4f}")
    print(f"  Error:              {err_current:+.2f}%  ← 11% gap (Bottleneck 2)")

    print("\n--- Target M_c(D7): inversion of RG equation ---")
    mc_target = find_target_mc_d7()
    ratio = mc_target / MC_D7_CURRENT
    alpha_D7_target = 2.0 * mc_target**2
    print(f"  α_s(M_Z) target   = {ALPHA_S_OBS:.4f}  (observed)")
    print(f"  1/α_s(M_Z) target = {1/ALPHA_S_OBS:.3f}")
    print(f"  1/α_common        = {1/ALPHA_COMMON:.3f}  [starting point at M_c(D7)]")
    print(f"  b₃/(2π)           = {B3/(2*math.pi):.4f}  [RG slope per unit of ln(μ)]")
    print(f"  ln(M_c_target/M_Z) = {math.log(mc_target/MZ_GEV):.3f}")
    print(f"  M_c(D7) target    = {mc_target:.3e} GeV")
    print(f"  Ratio to current:   {ratio:.2f}×  (target is {ratio:.1f}× larger than current estimate)")
    print(f"  Required α_D7     = 2 × M_c(D7)² = {alpha_D7_target:.3e} GeV²")

    # Verify
    alpha_s_check = alpha_s_at_mz(mc_target)
    print(f"\n  Verification: α_s(M_Z) from target M_c(D7) = {alpha_s_check:.6f}")
    print(f"  [Should equal {ALPHA_S_OBS:.6f} — error: {100*(alpha_s_check/ALPHA_S_OBS-1):+.2e}%]")

    print("\n--- Depth-Running Interpretation ---")
    mc_d5 = 1.02e13  # GeV  [D5 co-crystallization scale]
    mc_ratio = mc_target / mc_d5
    n_steps_d5_d7 = 2    # D5 → D6 → D7
    gamma_per_step = math.log(mc_ratio) / n_steps_d5_d7
    print(f"  M_c(D5) = {mc_d5:.2e} GeV  [D5/D6 co-crystallization]")
    print(f"  M_c(D7) target = {mc_target:.3e} GeV")
    print(f"  Ratio M_c(D7)/M_c(D5) = {mc_ratio:.1f}")
    print(f"  If D5 → D7 is {n_steps_d5_d7} depth steps:")
    print(f"    γ per step = ln({mc_ratio:.1f}) / {n_steps_d5_d7} = {gamma_per_step:.3f}")
    print(f"    This is the substrate depth-running coefficient required at D7")
    print(f"    (vs γ_space >> 0 and γ_weak ≈ 0 in the two-scale model)")

    print("\n--- α_s Running Table from M_c(D7) ---")
    print(f"  One-loop running; M_c(D7) = {mc_target:.3e} GeV")
    print(f"  {'Scale (GeV)':>12}  {'DFC α_s':>10}  {'1/α_s':>8}  {'Observed':>10}  {'Error':>8}")
    print(f"  {'-'*12}  {'-'*10}  {'-'*8}  {'-'*10}  {'-'*8}")
    table = alpha_s_running_table(mc_target)
    for (scale, a_s, obs) in table:
        if a_s is None:
            print(f"  {scale:12.2f}  {'NON-PERT':>10}")
            continue
        obs_str = f"{obs:.4f}" if obs is not None else "    —   "
        err_str = f"{100*(a_s/obs-1):+.1f}%" if obs is not None else "   —"
        print(f"  {scale:12.2f}  {a_s:10.4f}  {1/a_s:8.2f}  {obs_str:>10}  {err_str:>8}")

    print("\n--- Scan: α_s(M_Z) vs M_c(D7) ---")
    print(f"  {'M_c(D7) (GeV)':>16}  {'α_s(M_Z)':>10}  {'Error vs 0.1182':>17}")
    print(f"  {'-'*16}  {'-'*10}  {'-'*17}")
    scan_scales = [4e14, 6e14, 8e14, 1.0e15, 1.5e15, mc_target, 2.5e15, 3e15]
    for mc in scan_scales:
        a_s = alpha_s_at_mz(mc)
        if a_s is None:
            print(f"  {mc:16.2e}  {'—':>10}")
            continue
        err = 100 * (a_s / ALPHA_S_OBS - 1)
        mark = " ← target" if abs(mc - mc_target) < 1e12 else ""
        mark2 = " ← current" if abs(mc - MC_D7_CURRENT) < 1e12 else ""
        print(f"  {mc:16.2e}  {a_s:10.4f}  {err:+14.2f}%{mark}{mark2}")

    print("\n--- Summary ---")
    print(f"  CURRENT:  M_c(D7) = {MC_D7_CURRENT:.1e} GeV  →  α_s = {alpha_s_current:.4f} ({err_current:+.1f}%)")
    print(f"  TARGET:   M_c(D7) = {mc_target:.3e} GeV  →  α_s = {ALPHA_S_OBS:.4f} (0.0%)")
    print(f"  GAP:      factor {ratio:.2f}× in M_c(D7); factor {ratio**2:.1f}× in α_D7")
    print()
    print("  BLOCKING STEP: derive α_D7 = 2 × M_c(D7)² from the substrate.")
    print("  OPTIONS:")
    print("    1. Depth-running: γ_D7 ≈ 5.3 per step from D5→D7 compression dynamics")
    print("    2. Non-pert threshold: factor-2.5 shift in matching condition at D7")
    print("    3. Direct SU(3) closure geometry: three-kink binding energy at D7")
    print()
    print("  Until α_D7 is derived, α_s(M_Z) is consistent but not predicted by DFC.")
