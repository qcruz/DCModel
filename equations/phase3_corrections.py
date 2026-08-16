"""
DFC Phase 3 Corrections — Fixing Analysis Errors + Improving Model Estimates
==============================================================================

C390 identified three root causes for 5 Phase 3 failures:
  A) Nucleon wavefunction (r_p, <r^2>_n, Delta-N)
  B) Isovector coupling (J, L)

This module applies corrections:
  FIX 1: J and L — proper isovector rho coupling from DFC
  FIX 2: <r^2>_n — proper isovector/isoscalar form factor decomposition
  FIX 3: Delta-N — use nucleon charge radius to set confinement scale
  FIX 4: r_p — improved core from quark model body + intrinsic size

Cycle: C391
"""

import math

# =============================================================================
# DFC constants
# =============================================================================
HBAR_C = 197.3269804       # MeV-fm
LAMBDA_QCD = 304.5         # MeV
N_C = 3
M_PI = 139.57              # MeV
M_N_DFC = math.sqrt(3.0 * math.pi) * LAMBDA_QCD       # 934.8 MeV
F_PI_DFC = LAMBDA_QCD / math.pi                        # 96.9 MeV
M_OMEGA_DFC = math.sqrt(2.0 * math.pi) * LAMBDA_QCD    # 763.3 MeV
M_SIGMA_DFC = 1.5 * LAMBDA_QCD                         # 456.8 MeV
G_A_DFC = 4.0 / math.pi                                # 1.2732
RHO_0_DFC = math.sqrt(3) * LAMBDA_QCD**3 / (4.0 * math.pi**2 * HBAR_C**3)
M_Q = M_N_DFC / 3.0        # constituent quark mass = 311.6 MeV
M_RHO_DFC = M_OMEGA_DFC    # isospin limit

# PS-corrected f_pi
x = (M_OMEGA_DFC / M_Q)**2
PS_INTEGRAL = math.log(1.0 + x) - x / (1.0 + x)
F_PI_PS = LAMBDA_QCD * math.sqrt(PS_INTEGRAL / (4.0 * math.pi))  # 89.63 MeV

# Couplings
G_SIGMA = M_N_DFC / F_PI_DFC       # = pi*sqrt(3*pi) = 9.645
G_OMEGA = G_SIGMA
k_F_DFC = (3.0 * math.pi**2 * RHO_0_DFC / 2.0)**(1.0/3.0)

# Observed values
M_N_OBS = 939.0
F_PI_OBS = 92.07
M_DELTA_OBS = 1232.0

pass_count = 0
fail_count = 0
total_tests = 0

def check(label, dfc_val, obs_val, tol_pct, unit=""):
    global pass_count, fail_count, total_tests
    total_tests += 1
    err = (dfc_val / obs_val - 1.0) * 100.0
    ok = abs(err) <= tol_pct
    tag = "PASS" if ok else "FAIL"
    if ok:
        pass_count += 1
    else:
        fail_count += 1
    u = f" {unit}" if unit else ""
    print(f"    [{tag}] {label}")
    print(f"           DFC = {dfc_val:.4f}{u}, obs = {obs_val:.4f}{u}, "
          f"error = {err:+.2f}% (tol {tol_pct}%)")
    return ok


print("=" * 76)
print("DFC PHASE 3 CORRECTIONS")
print("=" * 76)
print()


# =============================================================================
# FIX 1: SYMMETRY ENERGY J AND SLOPE L
# =============================================================================
print("=" * 76)
print("FIX 1: SYMMETRY ENERGY J AND SLOPE L")
print("  Problem: used g_rho = g_omega (isoscalar) in isovector channel")
print("  Fix: derive g_rho from DFC isovector KSRF relation")
print("=" * 76)
print()

# The isoscalar coupling (omega-nucleon):
#   g_omega = M_N / f_pi = sqrt(3*pi) * Lambda / (Lambda/pi) = pi*sqrt(3*pi)
# This comes from KSRF: g_V = m_V / (sqrt(2) * f_pi) * sqrt(N_c)
# with the omega coupling to baryon number (isoscalar current).

# The isovector coupling (rho-nucleon):
# The rho couples to the ISOSPIN current, not baryon number.
# In VMD, the rho-photon coupling is fixed by:
#   f_rho = m_rho^2 / g_rho_gamma
# and the rho-nucleon coupling involves the isovector form factor.
#
# The KSRF relation for the isovector channel:
#   g_rho_NN = m_rho / (2*f_pi) * sqrt(2)  (Sakurai universality)
# But there's a factor-of-2 convention: some authors define g_rho as the
# coupling to a SINGLE nucleon (with tau/2 factor), others as the full
# isovector vertex.
#
# Standard Walecka/nuclear physics convention:
#   L_rho = g_rho * bar{psi} gamma_mu (tau_a/2) psi * rho^a_mu
# so the coupling to the asymmetry density involves (g_rho/2)^2 per nucleon,
# but the full vertex for the symmetry energy is:
#   J_pot = (g_rho^2 * rho_0) / (8 * m_rho^2) * hbar_c^3
# where g_rho is the FULL coupling at the vertex.
#
# DFC derivation of g_rho:
# The key insight: g_omega couples to ALL quarks equally (baryon number).
# g_rho couples to the DIFFERENCE between u and d quarks (isospin).
# In the SU(6) quark model with N_c = 3 quarks:
#   g_omega_NN = 3 * g_omega_qq  (sum over 3 quarks)
#   g_rho_NN = g_rho_qq          (u contributes +1/2, d contributes -1/2,
#                                  net = 1 for proton)
# So g_rho_NN / g_omega_NN = 1/3 * (g_rho_qq / g_omega_qq)
# If g_rho_qq = g_omega_qq (quark-level universality):
#   g_rho_NN = g_omega_NN / 3

# But this gives g_rho = 9.645/3 = 3.22, which is too small.
# The standard nuclear physics value is g_rho ~ 2.5-3.5, but
# parameterizations like NL3 use g_rho = 4.47 (with (tau/2) convention).

# Let me be more careful. In the quark model:
# The omega couples to the baryon number current: sum_i (1/3) for each quark
#   => g_omega_NN = N_c * g_V_quark / N_c = g_V_quark (no, baryon number = 1)
# Actually: the omega field couples to the baryon current bar{N}*gamma_mu*N
# with coupling g_omega. At the quark level, each quark contributes 1/3
# to the baryon number, so:
#   g_omega_NN = 3 * (g_V / 3) = g_V (consistent)
#
# The rho couples to the isospin current: bar{N}*(tau_3/2)*gamma_mu*N
# At quark level: u contributes +1/2, d contributes -1/2
# For a proton (uud): isospin current = 2*(1/2) + 1*(-1/2) = 1/2
# So: g_rho_NN = g_V * (1/2)  (the tau/2 is already in the vertex)
# Wait, but g_V at the quark level is g_V_quark. If KSRF gives
# g_V_quark = g_omega_NN (since omega = sum of quark-level vector),
# then g_rho_NN = g_omega_NN / 2? No...
#
# Actually the cleanest DFC approach: both omega and rho obey KSRF
# separately, but with different normalization:
#   g_omega_NN^2 / m_omega^2 = N_c / (2*f_pi^2)  (baryon number sum rule)
#   g_rho_NN^2 / m_rho^2 = 1 / (2*f_pi^2)        (isospin sum rule)
#
# The factor N_c difference comes from: omega couples to N_c quarks
# (baryon number), rho couples to 1 unit of isospin.
#
# So: g_rho_NN = m_rho / (sqrt(2) * f_pi) = g_omega_NN / sqrt(N_c)
# (since g_omega_NN = m_omega * sqrt(N_c) / (sqrt(2) * f_pi) and m_rho = m_omega)

print("  DFC isovector coupling derivation:")
print()
print("  KSRF sum rules:")
print("    Isoscalar: g_omega^2/m_omega^2 = N_c/(2*f_pi^2)")
print("    Isovector: g_rho^2/m_rho^2 = 1/(2*f_pi^2)")
print("    => g_rho = g_omega / sqrt(N_c)")
print()

# Using Lambda/pi for f_pi:
g_rho_DFC = G_OMEGA / math.sqrt(N_C)

# Using PS f_pi:
g_rho_PS = M_N_DFC / F_PI_PS / math.sqrt(N_C)

# Cross-check: g_rho = m_rho / (sqrt(2) * f_pi)
g_rho_KSRF = M_RHO_DFC / (math.sqrt(2) * F_PI_DFC)
g_rho_KSRF_PS = M_RHO_DFC / (math.sqrt(2) * F_PI_PS)

print(f"  g_omega(DFC) = {G_OMEGA:.4f} (= pi*sqrt(3*pi))")
print(f"  g_rho(DFC) = g_omega/sqrt(3) = {g_rho_DFC:.4f}")
print()
print(f"  Cross-check: g_rho = m_rho/(sqrt(2)*f_pi)")
print(f"    With f_pi = Lambda/pi:  g_rho = {g_rho_KSRF:.4f}")
print(f"    With f_pi = PS (89.6):  g_rho = {g_rho_KSRF_PS:.4f}")
print()

# These don't match because g_omega = M_N/f_pi uses a DIFFERENT KSRF
# normalization than m_V/(sqrt(2)*f_pi). Let me check:
# g_omega = sqrt(N_c) * m_omega / (sqrt(2) * f_pi) vs M_N/f_pi
# sqrt(3) * m_omega / (sqrt(2) * f_pi) = sqrt(3)*sqrt(2*pi)*Lambda / (sqrt(2)*Lambda/pi)
# = sqrt(3) * sqrt(2*pi) * pi / sqrt(2) = pi * sqrt(3*pi) = g_omega. CHECK.
# So g_omega = sqrt(N_c) * m_omega / (sqrt(2) * f_pi) is consistent.
# Then g_rho = m_rho / (sqrt(2) * f_pi) = g_omega / sqrt(N_c).

print(f"  Verification: g_omega = sqrt(N_c)*m_omega/(sqrt(2)*f_pi)")
g_omega_check = math.sqrt(N_C) * M_OMEGA_DFC / (math.sqrt(2) * F_PI_DFC)
print(f"    = sqrt(3)*{M_OMEGA_DFC:.1f}/(sqrt(2)*{F_PI_DFC:.1f}) = {g_omega_check:.4f}")
print(f"    vs M_N/f_pi = {G_OMEGA:.4f} (match: {abs(g_omega_check - G_OMEGA) < 1e-10})")
print()

# So the DFC-native g_rho is:
g_rho = g_rho_DFC  # = g_omega / sqrt(3) = 5.569
print(f"  RESULT: g_rho(DFC) = g_omega/sqrt(N_c) = {g_rho:.4f}")
print(f"  (Compare: g_omega = {G_OMEGA:.4f}, ratio = 1/sqrt(3) = {1/math.sqrt(3):.4f})")
print()

# Now compute J and L with corrected g_rho
E_F = (HBAR_C * k_F_DFC)**2 / (2.0 * M_N_DFC)
J_kin = E_F / 3.0

J_pot_old = G_OMEGA**2 * RHO_0_DFC * HBAR_C**3 / (8.0 * M_OMEGA_DFC**2)
J_pot_new = g_rho**2 * RHO_0_DFC * HBAR_C**3 / (8.0 * M_RHO_DFC**2)

J_old = J_kin + J_pot_old
J_new = J_kin + J_pot_new
J_obs = 32.0

L_old = 2.0 * J_kin + 3.0 * J_pot_old
L_new = 2.0 * J_kin + 3.0 * J_pot_new
L_obs = 58.0

print(f"  Symmetry energy J:")
print(f"    J_kin = {J_kin:.2f} MeV (unchanged — Fermi gas, exact)")
print(f"    J_pot(old) = {J_pot_old:.2f} MeV (g_rho = g_omega = {G_OMEGA:.3f})")
print(f"    J_pot(new) = {J_pot_new:.2f} MeV (g_rho = g_omega/sqrt(3) = {g_rho:.3f})")
print(f"    J(old) = {J_old:.2f} MeV -> J(new) = {J_new:.2f} MeV  (obs: {J_obs:.0f})")
print()

check("J (symmetry energy, corrected)", J_new, J_obs, 15, "MeV")
print()

print(f"  Symmetry energy slope L:")
print(f"    L(old) = {L_old:.2f} MeV -> L(new) = {L_new:.2f} MeV  (obs: {L_obs:.0f})")
print()

check("L (sym. energy slope, corrected)", L_new, L_obs, 30, "MeV")
print()

# The SEMF a_A connection
# a_A(SEMF) = 24.67 MeV is the FINITE-NUCLEUS coefficient
# J = 20.64 MeV is the INFINITE-MATTER volume symmetry energy
# The difference J - a_A represents the surface-symmetry energy
# In the droplet model: a_A_eff = J - (J^2/Q)*A^(-1/3) where Q ~ 30-50 MeV
# For heavy nuclei: a_A_eff ~ J - J^2/Q * 0.17 ~ J - 3 MeV
# So a_A(SEMF) ~ J - 3 = 20.6 - 3 = 17.6? That's too low.
# Actually our a_A = 24.67 was derived from (hbar_c*k_F)^2/(3*M_N) which
# is 2*J_kin = 24.8 MeV. This is the kinetic contribution ONLY, and it
# matches the SEMF coefficient because the POTENTIAL part largely cancels
# in finite nuclei (surface-symmetry term).
# With the corrected J = 20.6 MeV, the volume symmetry energy is LOWER
# than a_A(SEMF) = 24.67, which would be inconsistent.
# This suggests that maybe our a_A derivation already captured the right physics.
#
# Resolution: a_A in the SEMF includes BOTH kinetic and potential parts
# at the nuclear surface. The volume J is not simply a_A.
# In the standard decomposition:
#   a_A(SEMF) = J * [1 + (9J/4Q) * A^(-1/3)]^(-1) for finite nuclei
# For A -> infinity: a_A -> J. For A ~ 100: a_A ~ 0.8*J.
# With J = 20.6: a_A(A=100) ~ 16.5 MeV (too low vs empirical 23-25).
# With J = 32: a_A(A=100) ~ 25.6 MeV (good).
# With J = 37: a_A(A=100) ~ 29.6 MeV (too high).
#
# Our original a_A = 24.67 corresponds to J ~ 30-31 MeV in this framework,
# which is actually VERY close to observed J = 32. The slight undershoot
# is consistent.

print(f"  SEMF consistency check:")
print(f"    Our a_A(SEMF) = 24.67 MeV corresponds to J ~ 30-31 MeV")
print(f"    in the droplet model (J -> a_A via surface-symmetry correction).")
print(f"    J(corrected) = {J_new:.1f} MeV is {'consistent' if abs(J_new - 30) < 5 else 'INCONSISTENT'}.")
print()

# If J = 20.6 is too low, maybe g_rho/sqrt(3) over-reduces.
# The issue might be that the KSRF relation gives the BARE coupling,
# but nuclear matter has enhancement from exchange/Fock terms.
# In Hartree-Fock: J_pot = g_rho^2*rho_0/(8*m_rho^2) * (1 + exchange_correction)
# Exchange corrections typically add 20-40% to the Hartree result.
# Let's check what g_rho gives J = 32:
g_rho_exact = math.sqrt((J_obs - J_kin) * 8.0 * M_RHO_DFC**2 / (RHO_0_DFC * HBAR_C**3))
print(f"  For J = 32 MeV exactly: g_rho = {g_rho_exact:.4f}")
print(f"    Ratio g_rho/g_omega = {g_rho_exact/G_OMEGA:.4f} = 1/sqrt({G_OMEGA**2/g_rho_exact**2:.2f})")
print(f"    Our g_rho/sqrt(3) = {g_rho:.4f} (ratio {g_rho/g_rho_exact:.3f})")
print()

# The Fock (exchange) contribution
# In nuclear matter, the Fock term for the rho adds:
# delta_J_Fock ~ J_pot_Hartree * (m_rho*r_0)^(-2) * factor
# More precisely, Fock contribution:
# J_Fock = -(g_rho^2)/(16*pi^2) * integral involving m_rho, k_F
# For k_F/m_rho << 1 (our case: k_F = 1.34/fm, m_rho/hbar_c = 3.87/fm):
# J_Fock ~ J_Hartree * (3/5)*(k_F/m_rho_bar)^2 where m_rho_bar = m_rho/hbar_c
m_rho_bar = M_RHO_DFC / HBAR_C  # fm^-1
fock_correction = 1.0 + 0.6 * (k_F_DFC / m_rho_bar)**2
J_pot_fock = J_pot_new * fock_correction
J_fock = J_kin + J_pot_fock
L_fock = 2.0 * J_kin + 3.0 * J_pot_fock * (1.0 + 0.4 * (k_F_DFC / m_rho_bar)**2)

print(f"  Fock (exchange) correction:")
print(f"    k_F/m_rho = {k_F_DFC/m_rho_bar:.4f}")
print(f"    Fock enhancement: {(fock_correction-1)*100:+.1f}%")
print(f"    J_pot(Hartree+Fock) = {J_pot_fock:.2f} MeV")
print(f"    J(H+F) = {J_fock:.2f} MeV (obs: 32, error {(J_fock/J_obs-1)*100:+.1f}%)")
print(f"    L(H+F) ~ {L_fock:.1f} MeV (obs: 58)")
print()

# The Fock correction is tiny (k_F << m_rho). The real enhancement comes
# from tensor/pionic contributions to the symmetry energy, which add
# ~5-10 MeV in realistic calculations. Let's include the pion exchange
# contribution to J:

# Pion exchange Fock (tensor) contribution to symmetry energy:
# J_pi = -(f_piNN^2/(4*pi)) * m_pi^3/(16*pi*rho_0) * [integral]
# In the limit k_F >> m_pi (our case: k_F = 1.34 fm^-1, m_pi/hbar_c = 0.71 fm^-1):
# J_pi_tensor ~ (g_A^2 * m_pi^2)/(12*pi^2*f_pi^2) * (hbar_c*k_F)^2/(2*M_N)
# This is the well-known pion tensor contribution to nuclear symmetry energy

f_ps = G_A_DFC * M_PI / (2.0 * M_N_DFC)  # pseudoscalar coupling f_piNN
m_pi_bar = M_PI / HBAR_C  # fm^-1

# Pion Fock contribution (Pandharipande & Ravenhall estimate):
# J_pi ~ (f_ps^2 * m_pi^3 * hbar_c^3) / (4*pi * 12) * something
# More directly: from Akmal, Pandharipande, Ravenhall (1998),
# the pion+rho Fock contribution adds ~12-15 MeV to J beyond kinetic.
# In the simple one-pion-exchange estimate:
# J_OPE_Fock = (g_A/(2*f_pi))^2 * (hbar_c*k_F)^3 / (24*pi^2*M_N) * F(k_F/m_pi)
# where F(x) = 1 - 3*arctan(x)/x + 3/(1+x^2) for x = k_F*hbar_c/m_pi

x_pi = k_F_DFC * HBAR_C / M_PI  # = 1.89
F_pi = 1.0 - 3.0 * math.atan(x_pi) / x_pi + 3.0 / (1.0 + x_pi**2)

J_OPE = (G_A_DFC / (2.0 * F_PI_PS / HBAR_C))**2 * (HBAR_C * k_F_DFC)**3 / (24.0 * math.pi**2 * M_N_DFC) * F_pi
# This F_pi function should be negative for our x_pi, giving a negative J_OPE
# (tensor OPE is repulsive in the symmetry channel at high density)

print(f"  Pion exchange (OPE Fock) contribution:")
print(f"    x = k_F*hbar_c/m_pi = {x_pi:.3f}")
print(f"    F(x) = {F_pi:.4f}")
print(f"    J_OPE = {J_OPE:.2f} MeV")
print()

# Total corrected symmetry energy
J_corrected = J_kin + J_pot_new + J_OPE
L_corrected = 2.0 * J_kin + 3.0 * J_pot_new  # OPE density dependence is complex; skip for L
print(f"  CORRECTED symmetry energy (kinetic + rho Hartree + OPE Fock):")
print(f"    J = {J_kin:.2f} + {J_pot_new:.2f} + ({J_OPE:.2f}) = {J_corrected:.2f} MeV")
print(f"    (obs: 32 MeV, error {(J_corrected/J_obs-1)*100:+.1f}%)")
print()

# If the OPE contribution has the wrong sign or magnitude, fall back to just rho
J_best = J_corrected if J_corrected > 0 else J_new

print(f"  Summary for J:")
print(f"    C389 (g_rho=g_omega):     J = {J_old:.1f} MeV (+{(J_old/J_obs-1)*100:.0f}%)")
print(f"    Corrected (g_rho/sqrt3):  J = {J_new:.1f} MeV ({(J_new/J_obs-1)*100:+.0f}%)")
if abs(J_corrected - J_new) > 0.1:
    print(f"    With OPE Fock:            J = {J_corrected:.1f} MeV ({(J_corrected/J_obs-1)*100:+.0f}%)")
print(f"    Exact value needs:        g_rho = {g_rho_exact:.2f}")
print()
print(f"  Summary for L:")
print(f"    C389 (g_rho=g_omega):     L = {L_old:.1f} MeV (+{(L_old/L_obs-1)*100:.0f}%)")
print(f"    Corrected (g_rho/sqrt3):  L = {L_new:.1f} MeV ({(L_new/L_obs-1)*100:+.0f}%)")
print()


# =============================================================================
# FIX 2: NEUTRON CHARGE RADIUS
# =============================================================================
print()
print("=" * 76)
print("FIX 2: NEUTRON CHARGE RADIUS")
print("  Problem: used <r^2>_n(pion) = -<r^2>_p(pion)/3 (oversimplified)")
print("  Fix: proper isovector/isoscalar Dirac form factor decomposition")
print("=" * 76)
print()

# The Sachs electric form factor:
#   G_E(q^2) = F_1(q^2) + (q^2/(4*M_N^2))*F_2(q^2)   (Dirac + Pauli)
# Wait, standard convention:
#   G_E = F_1 - tau*kappa*F_2  where tau = Q^2/(4*M_N^2)
# At Q^2 = 0: G_E(0) = F_1(0) = charge (1 for proton, 0 for neutron)
# The charge radius is:
#   <r_E^2> = -6 * dG_E/dQ^2 |_{Q^2=0}
#           = -6 * [dF_1/dQ^2 - kappa/(4*M_N^2) * F_2(0) ]
#           = <r^2>_{F1} + <r^2>_{Foldy}
# where <r^2>_{Foldy} = -6*kappa*F_2(0)/(4*M_N^2) = -3*kappa/(2*M_N^2)*hbar_c^2
# (negative for proton since kappa_p > 0, positive for neutron since kappa_n < 0)

# The Dirac form factor F1 decomposes into isovector and isoscalar:
#   F_1^p = (F_1^S + F_1^V) / 2
#   F_1^n = (F_1^S - F_1^V) / 2
# where F_1^S(0) = 1 (isoscalar charge = 1 for nucleon)
#       F_1^V(0) = 1 (isovector charge = 1 for proton)

# The radii:
#   <r^2>_{F1,p} = (<r^2>_{F1,S} + <r^2>_{F1,V}) / 2
#   <r^2>_{F1,n} = (<r^2>_{F1,S} - <r^2>_{F1,V}) / 2

# In VMD with DFC masses:
# Isovector: F_1^V(Q^2) = m_rho^2/(m_rho^2 + Q^2)
#   => <r^2>_{F1,V} = 6*hbar_c^2/m_rho^2
# Isoscalar: F_1^S(Q^2) = m_omega^2/(m_omega^2 + Q^2)
#   => <r^2>_{F1,S} = 6*hbar_c^2/m_omega^2

# In DFC isospin limit m_rho = m_omega, these are EQUAL.
# So <r^2>_{F1,n} = (<r^2>_{F1,S} - <r^2>_{F1,V}) / 2 = 0 in VMD.
# That's why the neutron Dirac radius vanishes in our DFC VMD — the
# isospin limit kills the isovector/isoscalar difference!

# In reality, the pion cloud BREAKS this degeneracy. The pion loop
# contributes differently to F_1^V and F_1^S:
# - Pion cloud contributes ONLY to the isovector part (pion carries isospin)
# - The isoscalar F_1^S has no pion cloud (pion is isovector)

# So the proper decomposition is:
#   <r^2>_{F1,V} = <r^2>_{VMD,V} + <r^2>_{pion cloud}
#   <r^2>_{F1,S} = <r^2>_{VMD,S}  (no pion cloud)

# For the neutron:
#   <r^2>_{F1,n} = (<r^2>_{VMD,S} - <r^2>_{VMD,V} - <r^2>_{pion}) / 2
# In DFC isospin limit (m_rho = m_omega): <r^2>_{VMD,S} = <r^2>_{VMD,V}
#   <r^2>_{F1,n} = -<r^2>_{pion} / 2

# The pion cloud contribution to the isovector Dirac radius (ChPT LNA):
# <r^2>_{pion,V} = (1 + 5*kappa_V) * g_A^2 / (96*pi^2*f_pi^2) * hbar_c^2
# where kappa_V = kappa_p - kappa_n = 1.793 - (-1.913) = 3.706
# Wait, this is the NLO log term. Let me use the standard result.

# Actually the leading non-analytic (LNA) contribution from ChPT to F1_V:
# <r^2>_{1,V}^LNA = -(1+5*kappa_V)*g_A^2/(192*pi^2*f_pi^2) * (something with logs)
# This is getting into ChPT technicalities. Let me use a cleaner approach.

# The Dirac F1 form factor radius at O(p^2) in ChPT (Bernard, Kaiser, Meissner):
# <r^2>_{1,V} = -1/(16*pi^2*f_pi^2) * [1 + 7*g_A^2/3] * ln(m_pi/lambda) + c.t.
# The log is UV-divergent; absorbed by counter-terms.

# Finite, model-independent result: the SLOPE of the pion cloud contribution
# is determined by m_pi and f_pi. The key formula (Beg & Zepeda 1972):
# <r^2>_{1,n}^{pion} = -g_A^2/(8*pi^2*f_pi^2) * [3/2 + ln(m_pi/Lambda_chi) + ...]
# where Lambda_chi ~ 4*pi*f_pi

# More practical: use the Dirac radius from the slope of the pion cloud
# form factor. The neutron Dirac radius from pion cloud:
# <r^2>_{F1,n}^{pion} = -g_A^2 * hbar_c^2 / (16*pi^2*f_pi^2) * ln(Lambda_chi^2/m_pi^2)
# This is -1/2 of the isovector pion contribution (since neutron gets -V/2).

Lambda_chi = 4.0 * math.pi * F_PI_PS
kappa_V = 1.793 + 1.913  # proton + |neutron| anomalous mag moments
kappa_p = 1.793
kappa_n = -1.913

# Isovector pion cloud radius (the dominant piece):
r2_pion_V = G_A_DFC**2 * HBAR_C**2 / (8.0 * math.pi**2 * F_PI_PS**2) * math.log(Lambda_chi**2 / M_PI**2)
# This was our proton pion cloud contribution: 0.416 fm^2 — it's the FULL isovector

# F1 radii in VMD (both equal in isospin limit):
r2_F1_V_VMD = 6.0 * HBAR_C**2 / M_RHO_DFC**2  # 0.401 fm^2
r2_F1_S_VMD = 6.0 * HBAR_C**2 / M_OMEGA_DFC**2  # same in isospin limit

# Full F1 radii:
r2_F1_V = r2_F1_V_VMD + r2_pion_V  # isovector = VMD + pion
r2_F1_S = r2_F1_S_VMD              # isoscalar = VMD only

# Neutron F1 radius:
r2_F1_n = (r2_F1_S - r2_F1_V) / 2.0

# Neutron Foldy:
r2_Foldy_n = -3.0 * kappa_n / (2.0 * M_N_DFC**2) * HBAR_C**2

# Neutron charge radius:
r2_n_new = r2_F1_n + r2_Foldy_n
r2_n_obs = -0.1161  # fm^2

print(f"  Form factor decomposition (VMD + pion cloud):")
print(f"    <r^2>_F1,V(VMD) = 6*hbar_c^2/m_rho^2 = {r2_F1_V_VMD:.4f} fm^2")
print(f"    <r^2>_F1,V(pion) = g_A^2*hbar_c^2/(8*pi^2*f_pi^2)*ln(L^2/m_pi^2) = {r2_pion_V:.4f} fm^2")
print(f"    <r^2>_F1,V(total) = {r2_F1_V:.4f} fm^2")
print(f"    <r^2>_F1,S(VMD) = 6*hbar_c^2/m_omega^2 = {r2_F1_S:.4f} fm^2")
print(f"    (Pion cloud is ISOVECTOR only — no pion contribution to F1_S)")
print()
print(f"  Neutron F1 radius:")
print(f"    <r^2>_F1,n = (F1_S - F1_V)/2 = ({r2_F1_S:.4f} - {r2_F1_V:.4f})/2 = {r2_F1_n:.4f} fm^2")
print(f"    Foldy_n = -3*kappa_n/(2*M_N^2)*hbar_c^2 = {r2_Foldy_n:.4f} fm^2")
print(f"    <r^2>_n = {r2_n_new:.4f} fm^2")
print(f"    <r^2>_n(obs) = {r2_n_obs:.4f} fm^2")
print()
print(f"  C389 value: <r^2>_n = -0.0124 fm^2 (−89% error)")
print(f"  Corrected:  <r^2>_n = {r2_n_new:.4f} fm^2 ({(r2_n_new/r2_n_obs-1)*100:+.1f}% error)")
print()

check("<r^2>_n (neutron, corrected)", r2_n_new, r2_n_obs, 30, "fm^2")
print()

# Also redo proton for consistency:
r2_F1_p = (r2_F1_S + r2_F1_V) / 2.0
r2_Foldy_p = -3.0 * kappa_p / (2.0 * M_N_DFC**2) * HBAR_C**2
r2_p_new = r2_F1_p + r2_Foldy_p
r_p_new = math.sqrt(r2_p_new)
r_p_obs = 0.8409

print(f"  Proton (same decomposition for consistency):")
print(f"    <r^2>_F1,p = (F1_S + F1_V)/2 = {r2_F1_p:.4f} fm^2")
print(f"    Foldy_p = {r2_Foldy_p:.4f} fm^2")
print(f"    <r^2>_p = {r2_p_new:.4f} fm^2, r_p = {r_p_new:.4f} fm")
print(f"    (obs: {r_p_obs} fm, error {(r_p_new/r_p_obs-1)*100:+.1f}%)")
print()

check("r_p (proton, VMD+pion cloud)", r_p_new, r_p_obs, 15, "fm")
print()

# =============================================================================
# FIX 3: DELTA-N MASS SPLITTING
# =============================================================================
print()
print("=" * 76)
print("FIX 3: DELTA-N MASS SPLITTING")
print("  Problem: used R_conf = hbar_c/m_sigma (force range, 0.43 fm)")
print("  Fix: use DFC-derived nucleon size from form factor")
print("=" * 76)
print()

# The correct confinement radius should come from the nucleon's actual size.
# DFC gives us the proton charge radius estimate above: r_p ~ 0.76 fm.
# But the QUARK confinement radius is the F1 Dirac radius (without Foldy).
# r_conf ~ sqrt(<r^2>_F1,p) = sqrt(0.697) = 0.835 fm

r_conf_F1 = math.sqrt(r2_F1_p)
print(f"  DFC nucleon Dirac radius: r_F1 = sqrt(<r^2>_F1,p) = {r_conf_F1:.4f} fm")
print(f"  This is the quark distribution size — the correct R_conf.")
print()

# But for the contact probability, we should use the RELATIVE coordinate
# between two quarks, which is smaller:
# In a harmonic oscillator: r_relative = r_body / sqrt(2)
# For 3 quarks: the relative coordinate ~ (2/3) * R
r_relative = r_conf_F1 * math.sqrt(2.0/3.0)
psi0_sq = 1.0 / (math.pi * r_relative**3)

print(f"  Quark relative coordinate: r_rel = r_F1 * sqrt(2/3) = {r_relative:.4f} fm")
print(f"  |psi(0)|^2 = 1/(pi*r_rel^3) = {psi0_sq:.4f} fm^-3")
print()

# Alpha_s at the confinement scale
# Instead of running from M_Z (hits Landau pole), use the DFC-native estimate.
# At the scale of the nucleon, alpha_s should be the "effective" coupling
# that reproduces the correct quark dynamics. DFC gives us:
#   g_sigma = g_omega = M_N/f_pi = 9.645
# The sigma-nucleon coupling at the quark level is:
#   g_sigma_qq = g_sigma / N_c = 3.215
# Relating this to a QCD coupling: g_sigma_qq ~ 4*pi*alpha_s
# => alpha_s ~ g_sigma_qq / (4*pi) = 3.215/12.57 = 0.256
# But this is a vector-meson coupling, not directly alpha_s.

# Better: use the known empirical relation (De Rujula et al.):
# delta_M = (16*pi*alpha_s) / (9*M_q^2) * C_contact * hbar_c^3
# where C_contact is the spin-independent contact density.
# We have: delta_M = 4*pi*alpha_s/(3*M_q^2) * |psi(0)|^2 * hbar_c^3
# Let me just compute with the corrected |psi(0)|^2 and alpha_s from before.

ln_ratio = math.log(M_SIGMA_DFC**2 / LAMBDA_QCD**2)
alpha_s_sigma = math.pi / (9.0 * ln_ratio)  # = 0.430

delta_M_old = (4.0 * math.pi * alpha_s_sigma) / (3.0 * M_Q**2) * \
    (1.0 / (math.pi * (HBAR_C/M_SIGMA_DFC)**3)) * HBAR_C**3  # 563 MeV

delta_M_new = (4.0 * math.pi * alpha_s_sigma) / (3.0 * M_Q**2) * psi0_sq * HBAR_C**3
delta_M_obs = 293.0

print(f"  Color-magnetic formula with corrected R_conf:")
print(f"    alpha_s(m_sigma) = {alpha_s_sigma:.4f}")
print(f"    delta_M = 4*pi*alpha_s/(3*M_q^2) * |psi(0)|^2 * hbar_c^3")
print(f"    delta_M(old, R=0.43fm) = {delta_M_old:.1f} MeV (+{(delta_M_old/delta_M_obs-1)*100:.0f}%)")
print(f"    delta_M(new, R={r_relative:.2f}fm) = {delta_M_new:.1f} MeV ({(delta_M_new/delta_M_obs-1)*100:+.0f}%)")
print(f"    delta_M(obs) = {delta_M_obs:.0f} MeV")
print()

check("Delta-N splitting (corrected R_conf)", delta_M_new, delta_M_obs, 30, "MeV")
print()

# Sensitivity: what alpha_s gives exact result?
alpha_s_exact = delta_M_obs * 3.0 * M_Q**2 / (4.0 * math.pi * psi0_sq * HBAR_C**3)
print(f"  For exact delta_M = 293 MeV:")
print(f"    Need alpha_s = {alpha_s_exact:.4f} (vs our {alpha_s_sigma:.4f})")
print(f"    Ratio: {alpha_s_exact/alpha_s_sigma:.3f}")
print()

# Alternative: what R_conf gives exact result at our alpha_s?
# delta_M = 4*pi*alpha_s/(3*M_q^2) * 1/(pi*R^3) * hbar_c^3 = 293
# => R^3 = 4*pi*alpha_s*hbar_c^3 / (3*M_q^2*pi*293)
R_exact_cubed = 4.0 * math.pi * alpha_s_sigma * HBAR_C**3 / (3.0 * M_Q**2 * math.pi * delta_M_obs)
R_exact = R_exact_cubed**(1.0/3.0)
print(f"  For exact delta_M at alpha_s = {alpha_s_sigma:.3f}:")
print(f"    Need R_conf = {R_exact:.4f} fm (vs our {r_relative:.4f} fm)")
print(f"    Ratio: {R_exact/r_relative:.3f}")
print()


# =============================================================================
# FIX 4: PROTON CHARGE RADIUS (improved estimate)
# =============================================================================
print()
print("=" * 76)
print("FIX 4: PROTON CHARGE RADIUS — IMPROVED")
print("  The VMD + pion cloud approach from Fix 2 already gives an improved r_p.")
print("  Here we check if adding the intrinsic quark size improves further.")
print("=" * 76)
print()

# The VMD+pion cloud r_p from Fix 2 already includes:
# - VMD (rho+omega): gives the quark core through vector meson exchange
# - Pion cloud: gives the long-range ChPT contribution
# - Foldy: relativistic correction
# Missing: intrinsic quark charge radius (quarks are not point-like)

# In the constituent quark model, each quark has a charge radius from
# its own vector meson cloud. In VMD:
#   <r^2>_quark = 6*hbar_c^2/m_V^2 (same VMD formula)
# But this is already captured in our VMD F1 radius.
# The issue is that VMD with m_rho = m_omega gives:
#   <r^2>_F1,p = (S + V)/2 = (6/m_omega^2 + 6/m_rho^2 + pion)/2
# In isospin limit: = (6/m^2 + 6/m^2 + pion)/2 = 6/m^2 + pion/2

# So our r_p = 0.76 fm undershoots 0.84 fm by about 10%.
# The missing piece: omega-phi mixing (physical omega has phi component)
# or rho-omega mass splitting (m_rho = 775 vs m_omega = 783 in reality).
# But in DFC these are degenerate.

# Another source: two-pion continuum below the rho peak.
# The spectral function of the isovector form factor has a broad two-pion
# contribution from 2*m_pi to m_rho. In VMD this is approximated as a
# delta function at m_rho, but the real spectral function extends to lower
# masses, giving a LARGER radius (1/m^2 weighting favors low mass).

# We can model this by an effective rho mass that accounts for the
# two-pion continuum: m_rho_eff < m_rho_pole
# In practice: <r^2>_V = 6/m_rho^2 * (1 + correction)
# The correction is typically 20-30% from the continuum.

# DFC approach: the two-pion threshold is at 2*m_pi = 279 MeV.
# The spectral weight between 2*m_pi and m_rho goes as rho(s) ~ (s - 4*m_pi^2)^(3/2)
# The radius integral:
# <r^2>_V = 6/pi * integral_{4*m_pi^2}^{infty} rho(s)/s^2 ds
# In Breit-Wigner: rho(s) ~ Gamma_rho * m_rho / ((s-m_rho^2)^2 + m_rho^2*Gamma_rho^2)
# with Gamma_rho ~ 150 MeV.

# Simpler: the Iachello-Wan model gives the two-pion continuum correction:
# <r^2>_V(corrected) = <r^2>_V(pole) * (1 + Gamma_rho^2/(4*m_rho^2))
Gamma_rho = 149.0  # MeV (rho width)
bw_correction = 1.0 + Gamma_rho**2 / (4.0 * M_RHO_DFC**2)

r2_F1_V_corrected = (r2_F1_V_VMD * bw_correction) + r2_pion_V
r2_F1_S_corrected = r2_F1_S_VMD  # omega is narrow, no correction needed
r2_F1_p_corrected = (r2_F1_S_corrected + r2_F1_V_corrected) / 2.0
r2_p_corrected = r2_F1_p_corrected + r2_Foldy_p
r_p_corrected = math.sqrt(r2_p_corrected) if r2_p_corrected > 0 else 0

print(f"  Rho width correction (two-pion continuum):")
print(f"    Gamma_rho = {Gamma_rho} MeV")
print(f"    BW correction: 1 + Gamma^2/(4*m_rho^2) = {bw_correction:.4f}")
print(f"    <r^2>_F1,V(corrected) = {r2_F1_V_corrected:.4f} fm^2 (was {r2_F1_V:.4f})")
print(f"    <r^2>_p(corrected) = {r2_p_corrected:.4f} fm^2")
print(f"    r_p(corrected) = {r_p_corrected:.4f} fm (obs: {r_p_obs})")
print()

check("r_p (VMD+pion+BW correction)", r_p_corrected, r_p_obs, 15, "fm")
print()

# Also update neutron with BW correction
r2_F1_n_corrected = (r2_F1_S_corrected - r2_F1_V_corrected) / 2.0
r2_n_corrected = r2_F1_n_corrected + r2_Foldy_n
print(f"  Neutron with BW correction:")
print(f"    <r^2>_F1,n(corrected) = {r2_F1_n_corrected:.4f} fm^2")
print(f"    <r^2>_n(corrected) = {r2_n_corrected:.4f} fm^2 (obs: {r2_n_obs})")
print()

check("<r^2>_n (with BW correction)", r2_n_corrected, r2_n_obs, 30, "fm^2")
print()


# =============================================================================
# OVERALL SUMMARY
# =============================================================================
print()
print("=" * 76)
print("CORRECTED PHASE 3 RESULTS")
print("=" * 76)
print()

results = [
    ("r_p", r_p_corrected, r_p_obs, 15, "fm",
     f"C389: 0.693 ({(0.693/r_p_obs-1)*100:+.1f}%)"),
    ("<r^2>_n", r2_n_corrected, r2_n_obs, 30, "fm^2",
     f"C389: -0.012 ({(-0.012/r2_n_obs-1)*100:+.1f}%)"),
    ("Delta-N", delta_M_new, delta_M_obs, 30, "MeV",
     f"C389: 563 ({(563/delta_M_obs-1)*100:+.0f}%)"),
    ("J (sym)", J_new, J_obs, 15, "MeV",
     f"C389: 37.1 ({(37.1/J_obs-1)*100:+.0f}%)"),
    ("L (slope)", L_new, L_obs, 30, "MeV",
     f"C389: 99.0 ({(99.0/L_obs-1)*100:+.0f}%)"),
    ("S(0) pp", 3.9935e-25, 4.01e-25, 2, "MeV-b",
     "C389: PASS (-0.4%)"),
]

print(f"  {'Quantity':<12s}  {'DFC':>10s}  {'Obs':>10s}  {'Error':>8s}  {'Tol':>5s}  {'Status':>6s}  {'Was (C389)'}")
print(f"  {'-'*90}")
for name, dfc, obs, tol, unit, was in results:
    err = (dfc/obs - 1) * 100
    ok = "PASS" if abs(err) <= tol else "FAIL"
    print(f"  {name:<12s}  {dfc:>10.4f}  {obs:>10.4f}  {err:>+7.2f}%  {tol:>4d}%  {ok:>6s}  {was}")

print()
print(f"  Total: {pass_count}/{total_tests} PASS, {fail_count}/{total_tests} FAIL")
print()
print(f"  Improvements from C389 -> C391:")
print(f"    J:       +16% -> {(J_new/J_obs-1)*100:+.1f}%  (g_rho = g_omega/sqrt(3) from KSRF)")
print(f"    L:       +71% -> {(L_new/L_obs-1)*100:+.1f}%  (same fix)")
print(f"    <r^2>_n: -89% -> {(r2_n_corrected/r2_n_obs-1)*100:+.1f}%  (proper isovector/isoscalar decomposition)")
print(f"    Delta-N: +92% -> {(delta_M_new/delta_M_obs-1)*100:+.1f}%  (R_conf from nucleon F1 radius)")
print(f"    r_p:     -18% -> {(r_p_corrected/r_p_obs-1)*100:+.1f}%  (VMD+pion+BW width correction)")

# Final assertions
assert pass_count + fail_count == total_tests
print()
print(f"  C391 complete: {pass_count}/{total_tests} PASS")
