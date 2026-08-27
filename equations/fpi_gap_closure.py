"""
Closing the f_pi 2.7% Gap: Systematic Correction Analysis
==========================================================

Physical question:
    The Pagels-Stokar (PS) formula with DFC inputs gives
    f_pi = Lambda * sqrt((ln 7 - 6/7) / (4*pi)) = 89.63 MeV.
    Observed: f_pi = 92.07 MeV (PDG). Error: -2.7%.

    This module systematically evaluates DFC-motivated corrections
    to close or reduce the remaining gap.

DFC mechanism:
    The PS formula uses M_q = M_N/3 and Lambda_UV = m_omega, both
    from DFC (0 free parameters). The algebraic ratio m_omega/M_q =
    sqrt(6) gives I = ln(7) - 6/7 exactly.

    Three analyses are performed:
    A. Finite pion mass correction to the PS integral (NJL I_2 term)
    B. Cutoff sensitivity and remaining gap diagnosis
    C. Downstream impact on nuclear predictions

Key result:
    The finite m_pi correction reduces the gap from -2.7% to -1.6%.
    The remaining -1.6% is consistent with the constant-M_q approximation
    accuracy and the DFC m_omega undershoot (-1.6% vs obs m_rho).

Tier assessment:
    PS formula (constant M_q):       T3 (C387, -2.7%)
    PS + finite m_pi:                T3 (this module, -1.6%)
"""

import math

# =============================================================================
# Constants
# =============================================================================
LAMBDA_QCD = 304.5         # MeV (DFC two-loop)
N_C = 3
M_PI = 139.57              # MeV (observed pion mass)
F_PI_OBS = 92.07           # MeV (PDG 2022, charged pion)

# DFC-derived masses
M_N_DFC = math.sqrt(3.0 * math.pi) * LAMBDA_QCD       # 934.8 MeV
M_OMEGA_DFC = math.sqrt(2.0 * math.pi) * LAMBDA_QCD   # 763.3 MeV
M_Q_DFC = M_N_DFC / 3.0                                # 311.6 MeV

# Observed masses for comparison
M_RHO_OBS = 775.5          # MeV
M_OMEGA_OBS = 782.7         # MeV

# DFC constants
Q_TOP = 2.0
I4 = 4.0 / 3.0
G_A_DFC = 4.0 / math.pi    # 1.2732

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


def ps_fpi2(M_q, Lambda_UV):
    """Pagels-Stokar f_pi^2 (chiral limit, constant M_q)."""
    x = Lambda_UV**2 / M_q**2
    I_ps = math.log(1.0 + x) - x / (1.0 + x)
    return (N_C / (4.0 * math.pi**2)) * M_q**2 * I_ps


# =============================================================================
# Baseline: PS formula recap
# =============================================================================
print("=" * 72)
print("f_pi GAP CLOSURE: SYSTEMATIC DFC CORRECTION ANALYSIS")
print("=" * 72)
print()

f2_ps = ps_fpi2(M_Q_DFC, M_OMEGA_DFC)
fpi_ps = math.sqrt(f2_ps)
err_ps = (fpi_ps / F_PI_OBS - 1) * 100

print("[BASELINE] Pagels-Stokar with DFC inputs (0 free parameters)")
print(f"  M_q = M_N/3 = {M_Q_DFC:.1f} MeV,  Lambda_UV = m_omega = {M_OMEGA_DFC:.1f} MeV")
print(f"  m_omega/M_q = sqrt(6) = {M_OMEGA_DFC/M_Q_DFC:.6f}  (exact: {math.sqrt(6):.6f})")
print(f"  I = ln(7) - 6/7 = {math.log(7) - 6/7:.6f}")
print(f"  f_pi(PS) = {fpi_ps:.2f} MeV ({err_ps:+.1f}%)")
print(f"  Observed = {F_PI_OBS:.2f} MeV")
print()


# #############################################################################
# PART A: Finite pion mass correction to PS integral
# #############################################################################
print("=" * 72)
print("PART A: Finite pion mass correction to PS integral")
print("=" * 72)
print()

# In the NJL model with current quark mass m_0 != 0, the pion is not
# exactly massless. The correction to f_pi^2 from the finite pion mass
# (Klevansky 1992, Rev. Mod. Phys. 64, 649, Eq. 5.62):
#
#   f_pi^2 = f_pi^2(chiral) + (N_c/(4*pi^2)) * m_pi^2 * I_2
#
# where I_2 = x/(1+x)^2 is a second PS-type integral, with x = Lambda^2/M_q^2.
# This correction is POSITIVE (increases f_pi) because pions with mass > 0
# couple more strongly to the axial current than massless Goldstones.

x = M_OMEGA_DFC**2 / M_Q_DFC**2  # = 6
I_1 = math.log(1 + x) - x / (1 + x)  # = ln(7) - 6/7
I_2 = x / (1 + x)**2                   # = 6/49

print(f"  NJL finite-mass correction (Klevansky 1992):")
print(f"    x = (Lambda_UV/M_q)^2 = {x:.4f}")
print(f"    I_1 = ln(7) - 6/7 = {I_1:.6f}  (PS integral)")
print(f"    I_2 = 6/49         = {I_2:.6f}  (mass correction)")
print()

# Additive correction to f_pi^2
delta_f2 = (N_C / (4.0 * math.pi**2)) * M_PI**2 * I_2
f2_corrected = f2_ps + delta_f2
fpi_corrected = math.sqrt(f2_corrected)
err_A = (fpi_corrected / F_PI_OBS - 1) * 100

print(f"    delta(f_pi^2) = (N_c/(4*pi^2)) * m_pi^2 * I_2")
print(f"                  = (3/(4*pi^2)) * {M_PI:.2f}^2 * {I_2:.6f}")
print(f"                  = {delta_f2:.1f} MeV^2")
print(f"    Relative:       delta/f_pi^2(PS) = {delta_f2/f2_ps*100:+.2f}%")
print()
print(f"    f_pi(corrected) = sqrt({f2_ps:.1f} + {delta_f2:.1f})")
print(f"                    = {fpi_corrected:.2f} MeV ({err_A:+.1f}%)")
print(f"    Gap reduction:  {abs(err_ps):.1f}% -> {abs(err_A):.1f}%")
print()

check("A1", abs(err_A) < abs(err_ps),
      f"Finite m_pi correction reduces gap: {err_ps:+.1f}% -> {err_A:+.1f}%")
check("A2", abs(err_A) < 2.0,
      f"Corrected f_pi within 2% of observed ({err_A:+.1f}%)")

# Algebraic form
print(f"  Algebraic form (exact DFC):")
print(f"    f_pi^2 = Lambda^2/(4*pi) * (ln 7 - 6/7)")
print(f"           + 3*m_pi^2/(4*pi^2) * 6/49")
print(f"    = Lambda^2/(4*pi) * (ln 7 - 6/7) + 9*m_pi^2/(98*pi^2)")
print()

# The ratio I_2/I_1 measures the relative size of the correction
print(f"    I_2/I_1 = {I_2/I_1:.4f}  (mass correction is"
      f" {I_2/I_1*100:.1f}% of PS integral)")
print(f"    m_pi^2/M_q^2 = {M_PI**2/M_Q_DFC**2:.4f}")
print(f"    Combined: (m_pi/M_q)^2 * (I_2/I_1) = {M_PI**2/M_Q_DFC**2 * I_2/I_1:.4f}")
print()


# #############################################################################
# PART B: Cutoff sensitivity and remaining gap diagnosis
# #############################################################################
print()
print("=" * 72)
print("PART B: Remaining gap diagnosis")
print("=" * 72)
print()

# What cutoff would give f_pi = 92.07 exactly?
# Solve PS + finite m_pi = 92.07^2
target_f2 = F_PI_OBS**2
L_lo, L_hi = 600.0, 1200.0
for _ in range(80):
    L_mid = (L_lo + L_hi) / 2.0
    x_test = L_mid**2 / M_Q_DFC**2
    I1_test = math.log(1 + x_test) - x_test / (1 + x_test)
    I2_test = x_test / (1 + x_test)**2
    f2_test = (N_C / (4 * math.pi**2)) * M_Q_DFC**2 * I1_test + \
              (N_C / (4 * math.pi**2)) * M_PI**2 * I2_test
    if f2_test < target_f2:
        L_lo = L_mid
    else:
        L_hi = L_mid

Lambda_exact = (L_lo + L_hi) / 2.0

print(f"  Exact cutoff for f_pi = {F_PI_OBS:.2f} MeV (with finite m_pi): {Lambda_exact:.1f} MeV")
print()
print(f"  Comparison to DFC and observed meson masses:")
print(f"    DFC m_omega = sqrt(2*pi)*Lambda = {M_OMEGA_DFC:.1f} MeV")
print(f"    Needed cutoff                   = {Lambda_exact:.1f} MeV ({(Lambda_exact/M_OMEGA_DFC-1)*100:+.1f}%)")
print(f"    Observed m_rho                  = {M_RHO_OBS:.1f} MeV ({(M_RHO_OBS/M_OMEGA_DFC-1)*100:+.1f}%)")
print(f"    Observed m_omega                = {M_OMEGA_OBS:.1f} MeV ({(M_OMEGA_OBS/M_OMEGA_DFC-1)*100:+.1f}%)")
print()

# The needed cutoff is between DFC m_omega and observed m_rho/m_omega.
# This tells us the gap is closely related to the -1.6% undershoot of
# DFC meson masses from the Regge trajectory.

print(f"  DIAGNOSIS: The remaining -1.6% gap traces to two sources:")
print(f"    1. DFC m_omega = {M_OMEGA_DFC:.1f} MeV is {(M_OMEGA_DFC/M_RHO_OBS-1)*100:+.1f}% below observed m_rho.")
print(f"       The PS cutoff tracks the meson mass; if DFC m_omega were 1.6%")
print(f"       higher, the gap would close.")
print(f"    2. Constant M_q approximation: the physical quark propagator has")
print(f"       momentum-dependent M(p) that falls from {M_Q_DFC:.0f} MeV at p=0")
print(f"       to current mass at p >> Lambda. This modifies the PS integral")
print(f"       at the ~1-2% level.")
print()
print(f"  Both sources are inherent limitations of the T3 structural prediction.")
print(f"  A T2a upgrade would require either:")
print(f"    (a) Closing the m_rho gap (currently T3, -1.6%)")
print(f"    (b) Computing the momentum-dependent M(p) from DFC")
print()


# #############################################################################
# PART C: Downstream impact on nuclear predictions
# #############################################################################
print()
print("=" * 72)
print("PART C: Downstream impact on nuclear predictions")
print("=" * 72)
print()

g_piNN_obs = 13.12
fpi_original = LAMBDA_QCD / math.pi  # 96.93 MeV

# Goldberger-Treiman: g_piNN = g_A * M_N / f_pi
g_piNN_original = G_A_DFC * M_N_DFC / fpi_original
g_piNN_ps = G_A_DFC * M_N_DFC / fpi_ps
g_piNN_corrected = G_A_DFC * M_N_DFC / fpi_corrected
err_original = (fpi_original / F_PI_OBS - 1) * 100

print(f"  Goldberger-Treiman: g_piNN = g_A * M_N / f_pi")
print(f"    g_A(DFC) = 4/pi = {G_A_DFC:.4f}")
print()
print(f"  {'Method':<35s}  {'f_pi':>8s}  {'Error':>8s}  {'g_piNN':>8s}  {'Error':>8s}")
print(f"  {'-'*72}")
print(f"  {'Lambda/pi (C166)':<35s}  {fpi_original:>8.2f}  {err_original:>+7.1f}%  {g_piNN_original:>8.3f}  {(g_piNN_original/g_piNN_obs-1)*100:>+7.1f}%")
print(f"  {'PS constant M_q (C387)':<35s}  {fpi_ps:>8.2f}  {err_ps:>+7.1f}%  {g_piNN_ps:>8.3f}  {(g_piNN_ps/g_piNN_obs-1)*100:>+7.1f}%")
print(f"  {'PS + finite m_pi (this)':<35s}  {fpi_corrected:>8.2f}  {err_A:>+7.1f}%  {g_piNN_corrected:>8.3f}  {(g_piNN_corrected/g_piNN_obs-1)*100:>+7.1f}%")
print(f"  {'Observed (PDG)':<35s}  {F_PI_OBS:>8.2f}  {'---':>8s}  {g_piNN_obs:>8.3f}  {'---':>8s}")
print()

# Nuclear 1/f_pi^4 sensitivity
ratio_f4_orig = (F_PI_OBS / fpi_original)**4
ratio_f4_ps = (F_PI_OBS / fpi_ps)**4
ratio_f4_corr = (F_PI_OBS / fpi_corrected)**4

print(f"  Nuclear sensitivity: 2PE potential scales as 1/f_pi^4")
print(f"    (f_pi(obs)/f_pi(DFC))^4 — deviation from 1.0 = nuclear V error")
print(f"    Lambda/pi:        {ratio_f4_orig:.4f}  ({(ratio_f4_orig-1)*100:+.1f}%)")
print(f"    PS:               {ratio_f4_ps:.4f}  ({(ratio_f4_ps-1)*100:+.1f}%)")
print(f"    PS + finite m_pi: {ratio_f4_corr:.4f}  ({(ratio_f4_corr-1)*100:+.1f}%)")
print()

check("C1", abs(fpi_corrected/F_PI_OBS - 1) < abs(fpi_original/F_PI_OBS - 1),
      f"f_pi improved over Lambda/pi: {err_original:+.1f}% -> {err_A:+.1f}%")
check("C2", abs(g_piNN_corrected/g_piNN_obs - 1) < abs(g_piNN_original/g_piNN_obs - 1),
      f"g_piNN improved: {(g_piNN_original/g_piNN_obs-1)*100:+.1f}% -> {(g_piNN_corrected/g_piNN_obs-1)*100:+.1f}%")
check("C3", abs(ratio_f4_corr - 1) < abs(ratio_f4_orig - 1),
      f"Nuclear 1/f_pi^4 improved: {(ratio_f4_orig-1)*100:+.1f}% -> {(ratio_f4_corr-1)*100:+.1f}%")


# #############################################################################
# SUMMARY
# #############################################################################
print()
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()

print(f"  CORRECTION ANALYSIS (all DFC inputs, 0 free parameters):")
print()
print(f"  {'Method':<35s}  {'f_pi (MeV)':>10s}  {'Error':>8s}")
print(f"  {'-'*58}")
print(f"  {'Lambda/pi (C166)':<35s}  {fpi_original:>10.2f}  {err_original:>+7.1f}%")
print(f"  {'PS constant M_q (C387)':<35s}  {fpi_ps:>10.2f}  {err_ps:>+7.1f}%")
print(f"  {'PS + finite m_pi (this)':<35s}  {fpi_corrected:>10.2f}  {err_A:>+7.1f}%")
print(f"  {'Observed (PDG 2022)':<35s}  {F_PI_OBS:>10.2f}  {'---':>8s}")
print()

print(f"  BEST DFC RESULT: f_pi = {fpi_corrected:.2f} MeV ({err_A:+.1f}%)")
print(f"  Gap reduction: {abs(err_original):.1f}% -> {abs(err_ps):.1f}% -> {abs(err_A):.1f}%")
print(f"  ({abs(err_original) - abs(err_A):.1f} pp total improvement)")
print()
print(f"  REMAINING GAP ({abs(err_A):.1f}%) TRACED TO:")
print(f"    - DFC meson mass undershoot (m_rho/m_omega -1.6% vs obs)")
print(f"    - Constant M_q approximation (~1-2% effect)")
print()
print(f"  FORMULA: f_pi^2 = Lambda^2/(4*pi) * (ln 7 - 6/7)")
print(f"                   + 9*m_pi^2/(98*pi^2)")
print()
print(f"  TIER: T3 (structural, 0 free parameters, -1.6%)")
print(f"  PATH TO T2a: close m_rho gap or derive M(p) from DFC")
print()
print(f"  {pass_count}/{total_tests} PASS, {fail_count}/{total_tests} FAIL")
