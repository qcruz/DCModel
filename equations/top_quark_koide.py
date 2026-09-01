"""
Top Quark Mass from Koide Formula — DFC Exploration
=====================================================

Physical question:
    Can the Koide formula, which works spectacularly for leptons (m_tau to 0.006%),
    predict the top quark mass from (m_c, m_b) or (m_u, m_c)?

DFC mechanism:
    The lepton Koide formula uses the circulant matrix phase t = 1/sqrt(Q_top),
    derived from the canonical normalization of the D5/D6 phase zero mode (T2a).
    If the same mechanism applies to quarks, it should predict m_t from lighter
    quark masses.

Key finding (C494):
    The naive extension FAILS. K = 2/3 does not hold for quarks:
    - (u,c,t): K = 0.849, m_t predicted = 19,848 MeV (−88.5%)
    - (c,b,t) pole masses: K = 0.649, m_t predicted = 203,198 MeV (+17.7%)
    - (d,s,b): K = 0.731, m_b predicted = 2,208 MeV (−47.2%)

    The quark mass hierarchy is too steep for the lepton Koide phase to work.
    The (c,b,t) grouping with K=2/3 gives the closest result (+17.7%) but this
    is well outside the 1% target. The actual K for (c,b,t) implies t = 0.688,
    which is 2.8% below the lepton value 1/sqrt(2) = 0.707.

Cycles: C494
"""

import math

PI = math.pi

# ── Lepton masses (MeV) ──
m_e = 0.51100
m_mu = 105.658
m_tau_obs = 1776.86

# ── Quark masses ──
# Running masses at 2 GeV (PDG 2024)
m_u_run = 2.16
m_d_run = 4.67
m_s_run = 93.4
m_c_run = 1270.0  # at m_c scale
m_b_run = 4180.0  # at m_b scale

# Pole masses (for heavy quarks)
m_c_pole = 1670.0
m_b_pole = 4780.0
m_t_pole = 172690.0  # top pole mass

# ── DFC parameter ──
Q_TOP = 2
t_DFC = 1.0 / math.sqrt(Q_TOP)  # 0.70711

results = []
pass_count = 0
fail_count = 0


def check(label, condition, msg):
    global pass_count, fail_count
    if condition:
        pass_count += 1
        print(f"  PASS {label}: {msg}")
    else:
        fail_count += 1
        print(f"  FAIL {label}: {msg}")
    results.append((label, condition, msg))


def koide_K(m1, m2, m3):
    """Compute Koide K parameter."""
    S = math.sqrt(m1) + math.sqrt(m2) + math.sqrt(m3)
    return (m1 + m2 + m3) / S**2


def koide_t(K):
    """Extract t from K = 1/3 + 2t^2/3."""
    val = (3.0 * K - 1.0) / 2.0
    if val < 0:
        return float('nan')
    return math.sqrt(val)


def predict_m3(m1, m2, K_target):
    """Predict m3 from (m1, m2) using Koide formula with given K."""
    a = math.sqrt(m1)
    b = math.sqrt(m2)
    M = m1 + m2
    # (1-K)x^2 - 2K(a+b)x + M - K(a+b)^2 = 0 where x = sqrt(m3)
    A = 1.0 - K_target
    B = -2.0 * K_target * (a + b)
    C = M - K_target * (a + b)**2
    disc = B**2 - 4.0 * A * C
    if disc < 0 or abs(A) < 1e-15:
        return float('nan')
    x = (-B + math.sqrt(disc)) / (2.0 * A)
    return x**2


# ════════════════════════════════════════════════════════════════════════
print("=" * 72)
print("TOP QUARK MASS FROM KOIDE FORMULA — DFC EXPLORATION")
print("=" * 72)
print()

# ── Part A: Lepton Koide (verification) ──
print("PART A — LEPTON KOIDE (VERIFICATION)")
print("-" * 72)
print()

K_lep = koide_K(m_e, m_mu, m_tau_obs)
t_lep = koide_t(K_lep)
m_tau_pred = predict_m3(m_e, m_mu, 2.0/3.0)
err_tau = (m_tau_pred / m_tau_obs - 1) * 100

print(f"  Lepton masses: m_e = {m_e}, m_μ = {m_mu}, m_τ = {m_tau_obs} MeV")
print(f"  Koide K = {K_lep:.6f} (2/3 = {2/3:.6f})")
print(f"  Phase t = {t_lep:.6f} (1/√Q_top = {t_DFC:.6f})")
print(f"  m_τ(Koide) = {m_tau_pred:.2f} MeV ({err_tau:+.4f}%)")
print()

check("A1", abs(err_tau) < 0.01,
      f"m_τ(Koide) = {m_tau_pred:.2f} MeV ({err_tau:+.4f}%)")

# ── Part B: Up-type quarks (u, c, t) with K = 2/3 ──
print()
print("PART B — UP-TYPE QUARKS (u, c, t)")
print("-" * 72)
print()

K_uct_run = koide_K(m_u_run, m_c_run, m_t_pole)
t_uct = koide_t(K_uct_run)
m_t_pred_uct = predict_m3(m_u_run, m_c_run, 2.0/3.0)
err_uct = (m_t_pred_uct / m_t_pole - 1) * 100

print(f"  Masses: m_u = {m_u_run} MeV (2 GeV), m_c = {m_c_run} MeV, m_t = {m_t_pole} MeV (pole)")
print(f"  Actual K = {K_uct_run:.6f} (2/3 = {2/3:.6f})")
print(f"  Actual t = {t_uct:.6f} (vs lepton t = {t_DFC:.6f})")
print(f"  m_t(Koide K=2/3) = {m_t_pred_uct:.0f} MeV ({err_uct:+.1f}%)")
print()

check("B1", abs(err_uct) < 5,
      f"m_t from (u,c) with K=2/3: {m_t_pred_uct:.0f} MeV ({err_uct:+.1f}%)")

# ── Part C: Cross-family (c, b, t) with K = 2/3 ──
print()
print("PART C — CROSS-FAMILY (c, b, t) POLE MASSES")
print("-" * 72)
print()

K_cbt = koide_K(m_c_pole, m_b_pole, m_t_pole)
t_cbt = koide_t(K_cbt)
m_t_pred_cbt = predict_m3(m_c_pole, m_b_pole, 2.0/3.0)
err_cbt = (m_t_pred_cbt / m_t_pole - 1) * 100

print(f"  Pole masses: m_c = {m_c_pole} MeV, m_b = {m_b_pole} MeV, m_t = {m_t_pole} MeV")
print(f"  Actual K = {K_cbt:.6f} (2/3 = {2/3:.6f})")
print(f"  Actual t = {t_cbt:.6f} (vs lepton t = {t_DFC:.6f})")
print(f"  t_actual / t_lepton = {t_cbt/t_DFC:.4f}")
print(f"  m_t(Koide K=2/3) = {m_t_pred_cbt:.0f} MeV ({err_cbt:+.1f}%)")
print()

check("C1", abs(err_cbt) < 5,
      f"m_t from (c,b) with K=2/3: {m_t_pred_cbt:.0f} MeV ({err_cbt:+.1f}%)")

# What K gives exact m_t from (c,b)?
K_exact = koide_K(m_c_pole, m_b_pole, m_t_pole)
t_exact = koide_t(K_exact)
print(f"  K needed for exact m_t: {K_exact:.6f}")
print(f"  t needed: {t_exact:.6f}")
print(f"  Deviation from 1/√2: {(t_exact/t_DFC-1)*100:+.2f}%")
print()

# ── Part D: Down-type quarks (d, s, b) with K = 2/3 ──
print()
print("PART D — DOWN-TYPE QUARKS (d, s, b)")
print("-" * 72)
print()

K_dsb = koide_K(m_d_run, m_s_run, m_b_run)
t_dsb = koide_t(K_dsb)
m_b_pred = predict_m3(m_d_run, m_s_run, 2.0/3.0)
err_dsb = (m_b_pred / m_b_run - 1) * 100

print(f"  Running masses: m_d = {m_d_run} MeV, m_s = {m_s_run} MeV, m_b = {m_b_run} MeV")
print(f"  Actual K = {K_dsb:.6f} (2/3 = {2/3:.6f})")
print(f"  Actual t = {t_dsb:.6f}")
print(f"  m_b(Koide K=2/3) = {m_b_pred:.0f} MeV ({err_dsb:+.1f}%)")
print()

check("D1", abs(err_dsb) < 5,
      f"m_b from (d,s) with K=2/3: {m_b_pred:.0f} MeV ({err_dsb:+.1f}%)")

# ── Part E: Summary of K values across sectors ──
print()
print("PART E — KOIDE K VALUES ACROSS ALL SECTORS")
print("-" * 72)
print()

print(f"  {'Sector':<20} {'K':>8} {'t':>8} {'vs 1/√2':>10} {'Status':>12}")
print(f"  {'-'*20} {'-'*8} {'-'*8} {'-'*10} {'-'*12}")
print(f"  {'Leptons (e,μ,τ)':<20} {K_lep:>8.6f} {t_lep:>8.6f} {(t_lep/t_DFC-1)*100:>+9.2f}% {'EXACT':>12}")
print(f"  {'Up (u,c,t)':<20} {K_uct_run:>8.6f} {t_uct:>8.6f} {(t_uct/t_DFC-1)*100:>+9.2f}% {'FAILS':>12}")
print(f"  {'Down (d,s,b)':<20} {K_dsb:>8.6f} {t_dsb:>8.6f} {(t_dsb/t_DFC-1)*100:>+9.2f}% {'FAILS':>12}")
print(f"  {'Heavy (c,b,t) pole':<20} {K_cbt:>8.6f} {t_cbt:>8.6f} {(t_cbt/t_DFC-1)*100:>+9.2f}% {'CLOSE':>12}")
print()

# ── Part F: DFC interpretation ──
print()
print("PART F — DFC INTERPRETATION")
print("-" * 72)
print()

print("  FINDING: The Koide formula with t = 1/sqrt(Q_top) = 1/sqrt(2)")
print("  works for leptons (0.006%) but FAILS for quarks.")
print()
print("  Why quarks differ from leptons:")
print("    1. QCD corrections: quarks interact via gluons, modifying the")
print("       effective Yukawa matrix. Leptons have no strong interaction.")
print("    2. Mass running: quark masses run strongly with energy scale.")
print("       No single scale gives K = 2/3 for any quark triplet.")
print("    3. CKM mixing: quarks mix between generations (CKM matrix).")
print("       The Koide circulant assumes no mixing between the three")
print("       states. CKM mixing could shift K away from 2/3.")
print()
print("  The closest result is (c,b,t) pole masses: K = 0.649, t = 0.688.")
print(f"  This is {abs(t_cbt/t_DFC-1)*100:.1f}% below the lepton value.")
print(f"  A QCD correction of order alpha_s(m_b)/pi ~ 0.07 could account")
print(f"  for this shift, but this has not been derived from DFC.")
print()
print("  CONCLUSION: Top quark mass from Koide is NOT a viable DFC")
print("  prediction at the <5% level. The formula works for leptons")
print("  because they lack strong interactions; quarks do not satisfy")
print("  the same circulant structure.")
print()

check("F1", abs(t_cbt/t_DFC - 1) < 0.05,
      f"(c,b,t) t within 5% of lepton value ({(t_cbt/t_DFC-1)*100:+.1f}%)")

# ════════════════════════════════════════════════════════════════════════
print()
print("=" * 72)
print(f"TOTAL: {pass_count}/{pass_count+fail_count} PASS, "
      f"{fail_count}/{pass_count+fail_count} FAIL")
print("=" * 72)
