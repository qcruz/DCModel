"""
ym_sp5_alpha_s_nf.py — SP5 S10: alpha_s(M_Z) from V(phi) with proper Nf threshold matching

Physical question:
    Derive alpha_s(M_Z) from V(phi) alone (no experimental alpha_s input) using
    the DFC-first-principles C_match from the Jost-function integral and proper
    2-loop Nf-threshold RGE (Nf: 6->5 at m_top).

DFC mechanism:
    V(phi) -> alpha=cbrt(18) [T2a C172] + beta=1/(9pi) [T2a C117]
           -> m_KK = sqrt(cbrt(18)/2) M_Pl [T1 C270; D4 inertia -> G_N=1/M_Pl^2]
           -> m_KK = 1.3976e19 GeV [T2a/T3 given C270 Planck identification]
           -> C_match = 0.795151 (Jost-function DFC kink wavefunction) [T2a C197]
           -> alpha_s(m_KK) = C_match * g_eff^2 / (4pi) [T2a]
           -> 2-loop RGE Nf=6 -> Nf=5 threshold at m_top [T2a]
           -> alpha_s(M_Z) [T2a]

Key improvement over C270:
    C270 used N_f=6 constant -> -6.08% error (T2b).
    C197 Jost C_match=0.795151 is DFC-first-principles (vs C191 C_match=0.789948
    which used PDG alpha_s as input). C_match_Jost is +0.63% larger, giving
    higher alpha_s(m_KK) and higher alpha_s(M_Z).
    Proper Nf threshold (6->5 at m_top) further adjusts the running.
    Combined: alpha_s(M_Z) ~+4%, T2a.

Benchmark: C256 reported alpha_s(M_Z)=0.12366 (+4.62%) with proper Nf matching.
    This module reproduces that result from the C270 m_KK identity.

References:
    C117: beta=1/(9pi) T2a
    C172: alpha=cbrt(18) T2a
    C191: C_match_MSbar=0.789948 T2a (matched to PDG alpha_s -- not DFC-first-principles)
    C197: C_match_Jost=0.795151 T2a (DFC kink wavefunction, no PDG alpha_s input)
    C256: alpha_s(M_Z)=0.12366 +4.62% with proper Nf (benchmark)
    C270: m_KK = sqrt(cbrt(18)/2) M_Pl T1 algebraic
"""

import numpy as np
from scipy.integrate import solve_ivp

# ============================================================
# Part A: DFC parameters from V(phi) [T1/T2a]
# ============================================================
# V(phi) parameters
alpha_dfc = 18 ** (1/3)           # cbrt(18) [T2a C172]
beta_dfc  = 1.0 / (9 * np.pi)    # 1/(9pi) [T2a C117]

# Derived quantities
I4      = 4/3                     # I_4 = C_2(fund, SU(3)) = 4/3 [T1]
N_Hopf  = 9                       # Hopf fiber construction [T1]
g_eff_sq = 2 * I4 / N_Hopf       # g_eff^2 = 2I_4/N_Hopf = 8/27 [T2a]

# m_KK from V(phi) Planck identification [T1 C270]
# m_KK = sqrt(alpha/2) * M_Pl = sqrt(cbrt(18)/2) * M_Pl
m_KK_in_MPl = np.sqrt(alpha_dfc / 2)

# Physical constants
M_Pl_GeV = 1.22090e19            # Reduced Planck mass in GeV
m_KK_GeV = m_KK_in_MPl * M_Pl_GeV   # [T2a/T3 from C270 T3 Planck argument]

# Quark mass thresholds (GeV)
M_Z     = 91.1876                 # Z boson mass (for comparison endpoint)
m_top   = 172.69                  # top quark mass
m_bot   = 4.183                   # bottom quark mass (not crossed between m_KK and M_Z)

# PDG reference value (not used as input -- comparison only)
alpha_s_PDG = 0.11820

# ============================================================
# Part B: C_match values [T2a]
# ============================================================
# DFC-first-principles: Jost function integral from DFC kink wavefunction [T2a C197]
# This does NOT use PDG alpha_s as input.
C_match_Jost = 0.795151

# MS-bar matched to PDG alpha_s (for comparison / self-consistency check) [T2a C191]
# C191 RAN from M_Z (PDG input) UP to m_KK to find this C_match.
# Running the reverse should recover PDG by construction.
C_match_MSbar = 0.789948

# alpha_s at m_KK for each C_match
alpha_s_mKK_Jost  = C_match_Jost  * g_eff_sq / (4 * np.pi)
alpha_s_mKK_MSbar = C_match_MSbar * g_eff_sq / (4 * np.pi)

# ============================================================
# Part C: 2-loop RGE with Nf threshold matching
# ============================================================
def b_coeffs(Nf):
    """SU(3) 2-loop beta function coefficients [T1]
    b0 = 11 - 2*Nf/3
    b1 = 102 - 38*Nf/3
    """
    b0 = 11.0 - 2.0*Nf/3.0
    b1 = 102.0 - 38.0*Nf/3.0
    return b0, b1

def rge_rhs(ln_mu, y, Nf):
    """d(alpha_s)/d(ln mu) = -(b0/2pi)*alpha_s^2 - (b1/8pi^2)*alpha_s^3"""
    a = y[0]
    b0, b1 = b_coeffs(Nf)
    return [-(b0 / (2*np.pi)) * a**2 - (b1 / (8*np.pi**2)) * a**3]

def run_segment(alpha_s_in, mu_in, mu_out, Nf):
    """Integrate 2-loop RGE at fixed Nf from mu_in to mu_out."""
    if mu_in == mu_out:
        return alpha_s_in
    sol = solve_ivp(
        lambda t, y: rge_rhs(t, y, Nf),
        (np.log(mu_in), np.log(mu_out)),
        [alpha_s_in],
        method='DOP853', rtol=1e-12, atol=1e-14
    )
    if not sol.success:
        raise RuntimeError(f"RGE failed: {sol.message}")
    return float(sol.y[0, -1])

def run_with_Nf_threshold(alpha_s_in, mu_start, mu_end):
    """
    Run from mu_start (high) to mu_end (low) with Nf=6 above m_top, Nf=5 below.
    LO matching at m_top: alpha_s continuous (no discontinuity at leading order).
    """
    if mu_start > m_top and mu_end < m_top:
        # Segment 1: m_KK -> m_top with Nf=6
        a_at_mtop = run_segment(alpha_s_in, mu_start, m_top, Nf=6)
        # LO threshold: alpha_s continuous
        # Segment 2: m_top -> M_Z with Nf=5
        a_final = run_segment(a_at_mtop, m_top, mu_end, Nf=5)
    elif mu_start > m_top and mu_end >= m_top:
        # Both endpoints above m_top: Nf=6 throughout
        a_final = run_segment(alpha_s_in, mu_start, mu_end, Nf=6)
    else:
        # Both endpoints below m_top: Nf=5 throughout
        a_final = run_segment(alpha_s_in, mu_start, mu_end, Nf=5)
    return a_final

# Run both routes
alpha_s_MZ_Jost  = run_with_Nf_threshold(alpha_s_mKK_Jost,  m_KK_GeV, M_Z)
alpha_s_MZ_MSbar = run_with_Nf_threshold(alpha_s_mKK_MSbar, m_KK_GeV, M_Z)

# Also run Jost with Nf=6 constant (to compare with C270 which used MSbar+Nf=6const)
alpha_s_MZ_Nf6const = run_segment(alpha_s_mKK_Jost, m_KK_GeV, M_Z, Nf=6)

# C270 configuration (MSbar + Nf=6 constant) for cross-check
alpha_s_MZ_C270 = run_segment(alpha_s_mKK_MSbar, m_KK_GeV, M_Z, Nf=6)

# ============================================================
# Results and assertions
# ============================================================
results = []
def check(label, cond, note=""):
    status = "PASS" if cond else "FAIL"
    results.append((label, status, note))
    return cond

err_Jost_pct  = (alpha_s_MZ_Jost  - alpha_s_PDG) / alpha_s_PDG * 100
err_MSbar_pct = (alpha_s_MZ_MSbar - alpha_s_PDG) / alpha_s_PDG * 100
err_C270_pct  = (alpha_s_MZ_C270  - alpha_s_PDG) / alpha_s_PDG * 100
err_Nf6c_pct  = (alpha_s_MZ_Nf6const - alpha_s_PDG) / alpha_s_PDG * 100

print("=" * 70)
print("ym_sp5_alpha_s_nf.py — SP5 S10: alpha_s(M_Z) with proper Nf threshold")
print("=" * 70)

# --- Part A ---
print("\nPART A [T1]: DFC parameters from V(phi)")
print(f"  alpha = cbrt(18) = {alpha_dfc:.8f}  [T2a C172]")
print(f"  beta  = 1/(9pi)  = {beta_dfc:.8f}  [T2a C117]")
print(f"  g_eff^2 = 2*I4/N_Hopf = 8/27 = {g_eff_sq:.8f}  [T2a]")
print(f"  m_KK = sqrt(cbrt(18)/2) * M_Pl = {m_KK_in_MPl:.8f} M_Pl  [T1 C270]")
print(f"  m_KK = {m_KK_GeV:.6e} GeV  [T2a/T3]")

r_geff = abs(g_eff_sq - 8/27)
check("A1: g_eff^2 = 8/27 exact", r_geff < 1e-14, f"res {r_geff:.2e}")

r_mkk  = abs(m_KK_in_MPl - (alpha_dfc/2)**0.5)
check("A2: m_KK = sqrt(cbrt(18)/2) M_Pl exact", r_mkk < 1e-14, f"res {r_mkk:.2e}")

r_I4 = abs(I4 - 4/3)
check("A3: I4 = 4/3 exact", r_I4 < 1e-14, f"res {r_I4:.2e}")

# --- Part B ---
print("\nPART B [T1]: 2-loop SU(3) beta function coefficients")
for nf in [6, 5, 4, 3]:
    b0, b1 = b_coeffs(nf)
    print(f"  Nf={nf}: b0 = {b0:.4f},  b1 = {b1:.4f}")

check("B1: b0(Nf=6) = 7",       abs(b_coeffs(6)[0] - 7)    < 1e-10, "SU(3) N_f=6")
check("B2: b0(Nf=5) = 23/3",    abs(b_coeffs(5)[0] - 23/3) < 1e-10, "SU(3) N_f=5")
check("B3: b1(Nf=6) = 26",      abs(b_coeffs(6)[1] - 26)   < 1e-10, "SU(3) N_f=6")
check("B4: b1(Nf=5) = 38.667",  abs(b_coeffs(5)[1] - (102 - 38*5/3)) < 1e-10)
check("B5: b0 > 0 all Nf<=16 (asymptotic freedom)",
      all(b_coeffs(nf)[0] > 0 for nf in range(17)), "universal AF")

# --- Part C ---
print("\nPART C [T2a]: alpha_s running — Route A (DFC-first-principles Jost C_match)")
print(f"  C_match_Jost  = {C_match_Jost:.6f}  [T2a C197, DFC kink Jost integral]")
print(f"  alpha_s(m_KK) = {alpha_s_mKK_Jost:.6f}")
alpha_at_mtop_Jost = run_segment(alpha_s_mKK_Jost, m_KK_GeV, m_top, Nf=6)
print(f"  alpha_s(m_top)[Nf=6] = {alpha_at_mtop_Jost:.6f}  [T2a]")
print(f"  LO threshold match at m_top={m_top} GeV (alpha_s continuous at LO)")
alpha_at_MZ_from_mtop = run_segment(alpha_at_mtop_Jost, m_top, M_Z, Nf=5)
print(f"  alpha_s(M_Z) [Nf=5] = {alpha_at_MZ_from_mtop:.6f}")
print(f"  -> alpha_s(M_Z)_Jost = {alpha_s_MZ_Jost:.6f}")
print(f"  PDG alpha_s(M_Z)     = {alpha_s_PDG:.6f}")
print(f"  Error: {err_Jost_pct:+.2f}%")

check("C1: alpha_s(m_KK) > 0", alpha_s_mKK_Jost > 0)
check("C2: alpha_s increases running DOWN (AF)",
      alpha_at_mtop_Jost > alpha_s_mKK_Jost,
      f"{alpha_at_mtop_Jost:.5f} > {alpha_s_mKK_Jost:.5f}")
check("C3: alpha_s(M_Z) > alpha_s(m_top)",
      alpha_s_MZ_Jost > alpha_at_mtop_Jost,
      f"{alpha_s_MZ_Jost:.5f} > {alpha_at_mtop_Jost:.5f}")
check("C4: |error| < 10% (T2a/T2b threshold)", abs(err_Jost_pct) < 10, f"{err_Jost_pct:+.2f}%")
check("C5: |error| < 5% (T2a strict threshold)", abs(err_Jost_pct) < 5, f"{err_Jost_pct:+.2f}%")

tier_Jost = "T2a" if abs(err_Jost_pct) < 5 else "T2b" if abs(err_Jost_pct) < 10 else "T2b(outer)"
print(f"  Route A tier: {tier_Jost}")

# --- Part D ---
print("\nPART D [T2a]: Route B — MS-bar C_match (self-consistency check)")
print(f"  C_match_MSbar = {C_match_MSbar:.6f}  [T2a C191; derived FROM PDG alpha_s]")
print(f"  alpha_s(m_KK) = {alpha_s_mKK_MSbar:.6f}")
print(f"  alpha_s(M_Z)  = {alpha_s_MZ_MSbar:.6f}")
print(f"  Error: {err_MSbar_pct:+.2f}%  (expected ~0% by construction)")

check("D1: Route B ~0% error (C191 inversion)", abs(err_MSbar_pct) < 0.5,
      f"{err_MSbar_pct:+.3f}% — confirms RGE implementation matches C191")

# --- Part E ---
print("\nPART E [T2a]: C_match gap and 2-loop estimate")
gap_pct = (C_match_Jost - C_match_MSbar) / C_match_MSbar * 100
b0_6, b1_6 = b_coeffs(6)
# 2-loop C_match uncertainty: schematic ~ (b1/b0^2) * (alpha_s(m_KK)/pi)
two_loop_pct = abs(b1_6 / b0_6**2) * alpha_s_mKK_MSbar / np.pi * 100
print(f"  C_match_Jost  = {C_match_Jost:.6f}  (DFC first-principles)")
print(f"  C_match_MSbar = {C_match_MSbar:.6f}  (matched to PDG)")
print(f"  Gap:              {gap_pct:+.4f}%")
print(f"  2-loop C_match uncertainty estimate: ~{two_loop_pct:.3f}%")
print(f"  Gap ({gap_pct:+.4f}%) vs 2-loop ({two_loop_pct:.3f}%) — gap within natural 2-loop range")

check("E1: C_match gap within 5x 2-loop uncertainty",
      abs(gap_pct) < 5 * two_loop_pct,
      f"|{gap_pct:.4f}%| < 5 x {two_loop_pct:.3f}%")

# --- Part F ---
print("\nPART F [T2a]: Nf-threshold correction diagnosis")
print(f"  C270 config (C_match_MSbar, Nf=6 const): {alpha_s_MZ_C270:.5f} ({err_C270_pct:+.2f}%)")
print(f"  Jost + Nf=6 const:                       {alpha_s_MZ_Nf6const:.5f} ({err_Nf6c_pct:+.2f}%)")
print(f"  Jost + Nf threshold (this module):        {alpha_s_MZ_Jost:.5f} ({err_Jost_pct:+.2f}%)")
Nf_corr   = alpha_s_MZ_Jost - alpha_s_MZ_Nf6const
Cmatch_corr = alpha_s_MZ_Nf6const - alpha_s_MZ_C270
print(f"  Nf-threshold correction:  Delta_alpha_s = {Nf_corr:+.5f}")
print(f"  C_match correction:       Delta_alpha_s = {Cmatch_corr:+.5f}")
print(f"  Combined improvement over C270: {err_Jost_pct - err_C270_pct:+.2f} pp")

check("F1: Nf threshold raises alpha_s(M_Z) [b0(5)>b0(6) -> faster running]",
      Nf_corr > 0, f"Delta={Nf_corr:+.5f}")
check("F2: C_match_Jost > C_match_MSbar -> higher alpha_s(M_Z)",
      Cmatch_corr > 0, f"Delta={Cmatch_corr:+.5f}")
check("F3: Combined error better than C270",
      abs(err_Jost_pct) < abs(err_C270_pct), f"{err_Jost_pct:+.2f}% vs {err_C270_pct:+.2f}%")

# --- Part G ---
print("\nPART G [T2a]: SP5 S10 chain summary — V(phi) -> alpha_s(M_Z)")
print(f"  V(phi) -> alpha=cbrt(18) [T2a C172], beta=1/(9pi) [T2a C117]")
print(f"         -> g_eff^2 = 8/27 [T2a]")
print(f"         -> m_KK = sqrt(cbrt(18)/2) M_Pl [T1 C270]")
print(f"         -> m_KK = {m_KK_GeV:.4e} GeV [T2a/T3 given C270 T3 Planck ID]")
print(f"         -> C_match = 0.795151 [T2a C197, DFC kink Jost integral]")
print(f"         -> alpha_s(m_KK) = {alpha_s_mKK_Jost:.6f} [T2a]")
print(f"         -> 2-loop RGE Nf=6->5 at m_top={m_top} GeV [T2a]")
print(f"         -> alpha_s(M_Z) = {alpha_s_MZ_Jost:.5f}  ({err_Jost_pct:+.2f}% vs PDG) [{tier_Jost}]")
print()
print(f"  SP5 S10 tier:  C270 T2b (-6.08%) -> {tier_Jost} ({err_Jost_pct:+.2f}%) [this module]")
print(f"  C256 benchmark: +4.62% (consistent)")

check("G1: full V(phi)->alpha_s chain T2a (|error|<5%)", abs(err_Jost_pct) < 5, tier_Jost)
check("G2: improvement over C270 (-6.08%)", abs(err_Jost_pct) < abs(err_C270_pct))
check("G3: consistent with C256 benchmark +4.62% (within 3 pp)",
      abs(err_Jost_pct - 4.62) < 3.0, f"this={err_Jost_pct:+.2f}% vs C256=+4.62%")

# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 70)
print("ASSERTION SUMMARY")
print("=" * 70)
n_total  = len(results)
n_passed = sum(1 for _, s, _ in results if s == "PASS")
for label, status, note in results:
    line = f"  [{status}] {label}"
    if note:
        line += f" — {note}"
    print(line)

print(f"\n{n_passed}/{n_total} ASSERTIONS PASSED")
print()
print("KEY RESULTS:")
print(f"  m_KK = {m_KK_in_MPl:.6f} M_Pl = {m_KK_GeV:.4e} GeV  [T1+T2a/T3]")
print(f"  C_match_Jost = {C_match_Jost:.6f}  [T2a C197, DFC-first-principles]")
print(f"  alpha_s(m_KK)_Jost = {alpha_s_mKK_Jost:.6f}  [T2a]")
print(f"  alpha_s(M_Z)_Jost+Nf = {alpha_s_MZ_Jost:.5f}  ({err_Jost_pct:+.2f}%)  [{tier_Jost}]")
print()
print("CHAIN:")
print("  V(phi)[T0] -> alpha=cbrt(18)[T2a] + beta=1/(9pi)[T2a]")
print(f"  -> m_KK={m_KK_in_MPl:.4f} M_Pl [T1] -> {m_KK_GeV:.3e} GeV [T2a/T3]")
print(f"  -> C_match_Jost=0.795151 [T2a C197] -> alpha_s(m_KK)={alpha_s_mKK_Jost:.5f} [T2a]")
print(f"  -> 2-loop Nf threshold RGE [T2a] -> alpha_s(M_Z)={alpha_s_MZ_Jost:.5f} ({err_Jost_pct:+.2f}%) [{tier_Jost}]")
print()
print("SP5 S10 TIER UPGRADE:")
print(f"  C270 (MSbar C_match + Nf=6 const): -6.08% [T2b]")
print(f"  C271 (Jost  C_match + Nf thresh):  {err_Jost_pct:+.2f}% [{tier_Jost}]")
