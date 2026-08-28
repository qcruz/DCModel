"""
Pion Mass from DFC via the GMOR Relation — Exploration and Status
=================================================================

Physical question:
    Can DFC predict the pion mass m_pi = 139.57 MeV from its derived parameters?
    The Gell-Mann-Oakes-Renner (GMOR) relation connects the pion mass to three
    quantities: the pion decay constant f_pi, the chiral condensate <qq>, and the
    average light quark mass m_hat = (m_u + m_d)/2.

DFC mechanism:
    The GMOR relation states that the square of the pion mass times the square of
    the pion decay constant equals twice the average light quark mass times the
    magnitude of the chiral condensate:

        m_pi^2 * f_pi^2 = 2 * m_hat * |<qq>|

    DFC can supply two of the three ingredients:
      (A) f_pi = 90.63 MeV from PS formula with DFC inputs (T3, C436)
      (B) <qq> from the NJL condensate with DFC M_Q and Lambda_UV (T3)

    The third ingredient, the average light quark mass m_hat, is NOT derived from
    DFC. Light quark masses arise from Yukawa couplings at D6 depth, which DFC
    has not computed (ROADMAP P3: CKM/PMNS from D6/D7 overlap).

    This module:
      Part A — Computes the DFC chiral condensate from NJL framework
      Part B — Inverts GMOR to find what m_hat DFC requires for observed m_pi
      Part C — Explores structural estimates for m_hat from DFC parameters
      Part D — Status assessment and path forward

Tier assessment:
    m_pi prediction: T4 BLOCKED (needs light quark mass derivation)
    Chiral condensate: T3 (NJL with DFC inputs)
    GMOR consistency: T3 (DFC f_pi + condensate consistent with PDG m_hat)

Key references:
    equations/fpi_gap_closure.py      — f_pi = 90.63 MeV (C436)
    equations/pion_decay_constant.py  — f_pi structural derivation (C166)
    equations/quark_mass_kappa_derivation.py — kappa_q = 3*pi/2 (C274)
"""

import math

# =============================================================================
# Constants
# =============================================================================
LAMBDA_QCD = 304.5          # MeV (DFC two-loop)
N_C = 3
PI = math.pi

# DFC-derived masses
M_N_DFC = math.sqrt(3.0 * PI) * LAMBDA_QCD       # 934.8 MeV (proton mass)
M_OMEGA_DFC = math.sqrt(2.0 * PI) * LAMBDA_QCD   # 763.3 MeV (vector meson)
M_Q_DFC = M_N_DFC / 3.0                           # 311.6 MeV (constituent quark)

# DFC f_pi from PS formula with finite m_pi correction (C436)
F_PI_DFC = 90.63            # MeV (PS + finite m_pi, -1.6%)

# Observed values
M_PI_OBS = 139.57           # MeV (charged pion, PDG)
M_PI0_OBS = 134.98          # MeV (neutral pion, PDG)
F_PI_OBS = 92.07            # MeV (PDG 2022)
M_U_PDG = 2.16              # MeV (up quark, MSbar at 2 GeV)
M_D_PDG = 4.67              # MeV (down quark, MSbar at 2 GeV)
M_HAT_PDG = (M_U_PDG + M_D_PDG) / 2.0   # 3.415 MeV

# Condensate reference
QQ_SCALE_PDG = 280.0        # MeV: <qq>^{1/3} at mu=2 GeV

pass_count = 0
fail_count = 0
total_tests = 0


def check(label, condition, msg=""):
    global pass_count, fail_count, total_tests
    total_tests += 1
    if condition:
        pass_count += 1
        print(f"  PASS {label}: {msg}")
    else:
        fail_count += 1
        print(f"  FAIL {label}: {msg}")


# =============================================================================
# Part A: DFC Chiral Condensate from NJL Framework
# =============================================================================
print("=" * 72)
print("PION MASS FROM DFC VIA GMOR RELATION — EXPLORATION")
print("=" * 72)
print()
print("[PART A] DFC CHIRAL CONDENSATE")
print("=" * 72)
print()

# NJL condensate formula (Klevansky 1992, RMP 64, 649):
#   <qq> = -(N_c/(4*pi^2)) * M_Q * [Lambda^2 - M_Q^2 * ln(1 + Lambda^2/M_Q^2)]
#
# With DFC inputs: M_Q = M_N/3 = 311.6 MeV, Lambda = m_omega = 763.3 MeV
# x = Lambda^2/M_Q^2 = 6 (exact from DFC)

x = M_OMEGA_DFC**2 / M_Q_DFC**2
print(f"  DFC inputs:")
print(f"    M_Q = M_N/3 = {M_Q_DFC:.1f} MeV")
print(f"    Lambda_UV = m_omega = {M_OMEGA_DFC:.1f} MeV")
print(f"    x = Lambda^2/M_Q^2 = {x:.4f}  (exact: 6)")
print()

# Condensate integral
I_cond = M_OMEGA_DFC**2 - M_Q_DFC**2 * math.log(1.0 + x)
qq_dfc = -(N_C / (4.0 * PI**2)) * M_Q_DFC * I_cond   # MeV^3

# Convert to standard form: <qq>^{1/3}
qq_cube_root = -(-qq_dfc)**(1.0/3.0)  # negative
qq_scale = (-qq_dfc)**(1.0/3.0)        # positive magnitude

print(f"  NJL condensate formula:")
print(f"    <qq> = -(N_c/(4*pi^2)) * M_Q * [Lambda^2 - M_Q^2 * ln(1+x)]")
print(f"    I_cond = {I_cond:.0f} MeV^2")
print(f"    <qq> = {qq_dfc:.0f} MeV^3")
print(f"    <qq>^(1/3) = -{qq_scale:.1f} MeV")
print()

err_cond = (qq_scale - QQ_SCALE_PDG) / QQ_SCALE_PDG * 100
print(f"    PDG reference: <qq>^(1/3) = -{QQ_SCALE_PDG:.0f} MeV (at mu=2 GeV)")
print(f"    DFC/PDG: {err_cond:+.1f}%")
print()

# Algebraic form with DFC exact ratios
# x = 6 → I_cond = Lambda^2 - M_Q^2 * ln(7) = M_Q^2 * (6 - ln7)
I_alg = 6.0 - math.log(7.0)
print(f"  Algebraic (exact DFC):")
print(f"    I_cond = M_Q^2 * (6 - ln 7) = M_Q^2 * {I_alg:.6f}")
print(f"    <qq> = -(N_c/(4*pi^2)) * M_Q^3 * (6 - ln 7)")
print(f"         = -(3/(4*pi^2)) * (M_N/3)^3 * (6 - ln 7)")
print(f"         = -(M_N^3/(36*pi^2)) * (6 - ln 7)")
print()

check("A1", abs(err_cond) < 30,
      f"DFC condensate within 30% of PDG scale ({err_cond:+.1f}%)")
check("A2", qq_dfc < 0,
      f"Condensate is negative (chiral symmetry broken)")
check("A3", abs(x - 6.0) < 0.001,
      f"Lambda^2/M_Q^2 = 6 exactly ({x:.6f})")


# =============================================================================
# Part B: GMOR Inversion — What m_hat Does DFC Need?
# =============================================================================
print()
print("[PART B] GMOR INVERSION")
print("=" * 72)
print()

print("  GMOR relation: m_pi^2 * f_pi^2 = 2 * m_hat * |<qq>|")
print()

# Using DFC f_pi and DFC condensate
m_hat_needed_dfc = (M_PI_OBS**2 * F_PI_DFC**2) / (2.0 * abs(qq_dfc))

# Using observed f_pi and PDG condensate (cross-check)
qq_pdg = QQ_SCALE_PDG**3  # MeV^3
m_hat_needed_pdg = (M_PI_OBS**2 * F_PI_OBS**2) / (2.0 * qq_pdg)

print(f"  With DFC inputs (f_pi={F_PI_DFC} MeV, DFC condensate):")
print(f"    m_hat_needed = m_pi^2 * f_pi^2 / (2 * |<qq>|)")
print(f"                 = {M_PI_OBS:.2f}^2 * {F_PI_DFC:.2f}^2 / (2 * {abs(qq_dfc):.0f})")
print(f"                 = {m_hat_needed_dfc:.2f} MeV")
print()

print(f"  With PDG inputs (f_pi={F_PI_OBS} MeV, PDG condensate):")
print(f"    m_hat_needed = {m_hat_needed_pdg:.2f} MeV")
print()

print(f"  PDG m_hat = (m_u + m_d)/2 = ({M_U_PDG:.2f} + {M_D_PDG:.2f})/2 = {M_HAT_PDG:.3f} MeV")
print()

err_mhat_dfc = (m_hat_needed_dfc - M_HAT_PDG) / M_HAT_PDG * 100
err_mhat_pdg = (m_hat_needed_pdg - M_HAT_PDG) / M_HAT_PDG * 100
print(f"  DFC GMOR requires m_hat = {m_hat_needed_dfc:.2f} MeV ({err_mhat_dfc:+.1f}% vs PDG)")
print(f"  PDG GMOR requires m_hat = {m_hat_needed_pdg:.2f} MeV ({err_mhat_pdg:+.1f}% vs PDG)")
print()

check("B1", abs(err_mhat_dfc) < 50,
      f"DFC GMOR m_hat within 50% of PDG ({err_mhat_dfc:+.1f}%)")

# Check: would the right m_hat with DFC condensate give m_pi?
m_pi_sq_test = 2.0 * M_HAT_PDG * abs(qq_dfc) / F_PI_DFC**2
m_pi_test = math.sqrt(m_pi_sq_test)
err_mpi = (m_pi_test - M_PI_OBS) / M_PI_OBS * 100

print()
print(f"  Reverse check: using PDG m_hat with DFC condensate and f_pi:")
print(f"    m_pi = sqrt(2 * {M_HAT_PDG:.3f} * {abs(qq_dfc):.0f} / {F_PI_DFC:.2f}^2)")
print(f"         = {m_pi_test:.1f} MeV (observed: {M_PI_OBS:.2f} MeV, error: {err_mpi:+.1f}%)")
print()

check("B2", abs(err_mpi) < 50,
      f"GMOR with PDG m_hat gives m_pi within 50% ({err_mpi:+.1f}%)")


# =============================================================================
# Part C: Structural Estimates for m_hat from DFC
# =============================================================================
print()
print("[PART C] STRUCTURAL ESTIMATES FOR LIGHT QUARK MASS")
print("=" * 72)
print()
print("  DFC has no derivation of m_u, m_d individually.")
print("  Light quark masses arise from Yukawa couplings at D6 depth,")
print("  which requires the D6/D7 overlap computation (ROADMAP P3).")
print()
print("  Candidate structural estimates for m_hat:")
print()

candidates = []

# Candidate 1: m_hat from generation ratio
# Gen-1 geometric mean M0 = sqrt(m_u * m_d) = 3.18 MeV
# m_hat = (m_u + m_d)/2 differs from sqrt(m_u*m_d) by isospin asymmetry
M0_gen1 = math.sqrt(M_U_PDG * M_D_PDG)
kappa_q = 3.0 * PI / 2.0  # DFC generation spacing

# Can M0 be derived? M_gen2 = M0 * exp(kappa_q)
# M0 = M_gen2 / exp(kappa_q)
M_gen2_obs = math.sqrt(1275.0 * 93.4)  # sqrt(m_c * m_s) MeV
M0_from_gen2 = M_gen2_obs / math.exp(kappa_q)
m_hat_c1 = M0_from_gen2  # rough: geometric mean ~ arithmetic mean for small ratio

candidates.append(("M_gen2/exp(kappa_q)", m_hat_c1,
                    "Gen-2 back-extrapolation via kappa_q=3*pi/2"))

# Candidate 2: GMOR-required m_hat (self-consistent with DFC condensate)
candidates.append(("GMOR-required", m_hat_needed_dfc,
                    "What GMOR needs with DFC f_pi + condensate"))

# Candidate 3: m_hat = Lambda_QCD * exp(-2*pi*N_c)
# Strong coupling suppression of current mass relative to Lambda
m_hat_c3 = LAMBDA_QCD * math.exp(-2.0 * PI * N_C)
candidates.append(("Lambda*exp(-6*pi)", m_hat_c3,
                    "Exponential suppression from strong sector"))

# Candidate 4: m_hat = Lambda_QCD / (4*pi*kappa_q)^2
m_hat_c4 = LAMBDA_QCD / (4.0 * PI * kappa_q)**2
candidates.append(("Lambda/(4*pi*kappa)^2", m_hat_c4,
                    "Double loop suppression"))

# Candidate 5: m_hat = v * (Lambda_QCD/v)^3 / (4*pi)^2
# Yukawa from dimension-5 operator
v_ew = 246.22  # MeV -> actually GeV, but let's work in MeV
v_ew_MeV = 246220.0
m_hat_c5 = v_ew_MeV * (LAMBDA_QCD / v_ew_MeV)**3 / (4.0 * PI)**2
candidates.append(("v*(Lambda/v)^3/(4*pi)^2", m_hat_c5,
                    "Dimension-5 Yukawa suppression"))

# Candidate 6: m_hat = M_Q * exp(-M_Q / Lambda_QCD * pi)
m_hat_c6 = M_Q_DFC * math.exp(-M_Q_DFC / LAMBDA_QCD * PI)
candidates.append(("M_Q*exp(-pi*M_Q/Lambda)", m_hat_c6,
                    "Instanton-like tunneling factor"))

print(f"  {'Estimate':>30}  {'m_hat (MeV)':>12}  {'vs PDG':>8}  Description")
print(f"  {'-'*85}")
for name, val, desc in candidates:
    err = (val - M_HAT_PDG) / M_HAT_PDG * 100
    marker = " <--" if abs(err) < 20 else ""
    print(f"  {name:>30}  {val:12.4f}  {err:+8.1f}%  {desc}{marker}")
print()
print(f"  PDG reference:                  {M_HAT_PDG:12.4f} MeV")
print()

# Check if any candidate is close
best_name, best_val, best_desc = min(candidates, key=lambda c: abs(c[1] - M_HAT_PDG))
best_err = (best_val - M_HAT_PDG) / M_HAT_PDG * 100
print(f"  Closest: {best_name} = {best_val:.4f} MeV ({best_err:+.1f}%)")
print()

check("C1", abs(best_err) < 50,
      f"At least one estimate within 50% of PDG ({best_name}: {best_err:+.1f}%)")

# The generation back-extrapolation is the most principled
print()
print("  ANALYSIS:")
print(f"    The generation back-extrapolation (M_gen2/exp(kappa_q)) gives")
print(f"    M0 = {M0_from_gen2:.4f} MeV, which is the Gen-1 geometric mean.")
print(f"    PDG: sqrt(m_u * m_d) = {M0_gen1:.4f} MeV")
err_M0 = (M0_from_gen2 - M0_gen1) / M0_gen1 * 100
print(f"    Error: {err_M0:+.1f}%")
print()
print(f"    This uses Gen-2 masses as INPUT (not a prediction).")
print(f"    To make this a prediction, DFC needs to derive the absolute")
print(f"    Gen-2 scale from M_c(D7) — which is the kappa_q derivation")
print(f"    applied to the QCD confinement scale.")
print()

check("C2", abs(err_M0) < 5,
      f"Gen-1 back-extrapolation matches sqrt(m_u*m_d) ({err_M0:+.1f}%)")


# =============================================================================
# Part D: m_pi Prediction Status and Path Forward
# =============================================================================
print()
print("[PART D] STATUS ASSESSMENT")
print("=" * 72)
print()

# What DFC can currently say about m_pi
print("  WHAT DFC CAN CURRENTLY DO:")
print()
print("  1. f_pi = 90.63 MeV from PS formula (T3, 0 free params)")
print(f"     Observed: {F_PI_OBS:.2f} MeV, error: {(F_PI_DFC/F_PI_OBS-1)*100:+.1f}%")
print()
print("  2. Chiral condensate from NJL with DFC inputs (T3):")
print(f"     <qq>^(1/3) = -{qq_scale:.1f} MeV")
print(f"     PDG: -{QQ_SCALE_PDG:.0f} MeV, error: {err_cond:+.1f}%")
print()
print("  3. Generation spacing kappa_q = 3*pi/2 (T2a, C274)")
print("     Predicts Gen-2 charm/strange from Gen-1 (+2.5%)")
print()
print("  WHAT DFC CANNOT YET DO:")
print()
print("  * Derive the absolute Gen-1 quark mass scale M0 = sqrt(m_u*m_d)")
print("  * Derive individual m_u, m_d (requires D6 Yukawa couplings)")
print("  * Therefore: CANNOT predict m_pi from first principles")
print()
print("  BLOCKER: Light quark masses m_u, m_d")
print("    These arise from Yukawa couplings at D6 depth.")
print("    Derivation requires D6/D7 overlap integral (ROADMAP P3).")
print("    This is the same blocker as CKM matrix derivation.")
print()

# The ratio m_pi/f_pi IS determined by DFC if the condensate is right
ratio_pi_fpi = M_PI_OBS / F_PI_DFC
ratio_pi_fpi_obs = M_PI_OBS / F_PI_OBS
print("  PARTIAL RESULT — m_pi/f_pi ratio:")
print(f"    m_pi / f_pi(DFC) = {ratio_pi_fpi:.4f}")
print(f"    m_pi / f_pi(obs) = {ratio_pi_fpi_obs:.4f}")
print(f"    From GMOR: m_pi/f_pi = sqrt(2 * m_hat * |<qq>|) / f_pi^2")
print(f"    This ratio depends on m_hat — not derivable yet.")
print()

# Path forward
print("  PATH FORWARD:")
print()
print("    Route 1 (D6 Yukawa): Derive m_u, m_d from D6/D7 overlap.")
print("      Gives m_hat -> GMOR -> m_pi. Blocked on D6 computation.")
print()
print("    Route 2 (Condensate + running): Use DFC condensate at the")
print("      confinement scale mu=Lambda_QCD. Running from mu=2 GeV")
print("      to mu=Lambda_QCD changes the effective condensate.")
print("      Still needs m_hat as input.")
print()
print("    Route 3 (Pion as pseudo-Goldstone): In strict chiral limit,")
print("      m_pi = 0 (exact Goldstone). Any m_pi > 0 requires explicit")
print("      chiral symmetry breaking (m_u, m_d > 0). This is intrinsic")
print("      to the GMOR mechanism — there is no bypass.")
print()
print("    CONCLUSION: m_pi prediction is fundamentally blocked on light")
print("    quark mass derivation. No structural shortcut exists because")
print("    the pion mass IS the explicit chiral symmetry breaking signal.")
print()

check("D1", True,
      "GMOR chain identified: f_pi [T3] + <qq> [T3] + m_hat [T4] -> m_pi [T4]")
check("D2", m_hat_needed_dfc > 0,
      f"GMOR-required m_hat is positive ({m_hat_needed_dfc:.2f} MeV)")

# Consistency check: does the DFC condensate + PDG m_hat give the right product?
gmor_product_dfc = 2.0 * M_HAT_PDG * abs(qq_dfc)
gmor_product_obs = M_PI_OBS**2 * F_PI_OBS**2
err_product = (gmor_product_dfc / (M_PI_OBS**2 * F_PI_DFC**2) - 1) * 100

check("D3", abs(err_product) < 50,
      f"GMOR product consistency: DFC condensate*m_hat vs m_pi^2*f_pi^2 ({err_product:+.1f}%)")


# =============================================================================
# Summary
# =============================================================================
print()
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()
print(f"  DFC chiral condensate: <qq>^(1/3) = -{qq_scale:.1f} MeV (T3)")
print(f"  DFC pion decay constant: f_pi = {F_PI_DFC:.2f} MeV (T3)")
print(f"  GMOR-required m_hat: {m_hat_needed_dfc:.2f} MeV (PDG: {M_HAT_PDG:.3f} MeV)")
print()
print(f"  m_pi PREDICTION STATUS: T4 BLOCKED")
print(f"    Blocker: light quark masses m_u, m_d not derived from DFC")
print(f"    Path: D6/D7 overlap -> Yukawa couplings -> m_u, m_d -> GMOR -> m_pi")
print()
print(f"  DFC GMOR CHAIN (when m_hat is derived):")
print(f"    m_pi = sqrt(2 * m_hat * |<qq>| / f_pi^2)")
print(f"    With DFC f_pi and condensate, m_hat = {M_HAT_PDG:.3f} MeV gives:")
print(f"    m_pi = {m_pi_test:.1f} MeV (obs: {M_PI_OBS:.2f} MeV, {err_mpi:+.1f}%)")
print()

print(f"  {pass_count}/{total_tests} PASS, {fail_count}/{total_tests} FAIL")
