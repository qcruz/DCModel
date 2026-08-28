"""
Neutron Star Maximum Mass from DFC String Tension (C443)
=========================================================

Physical question:
    Can DFC predict the maximum mass of a neutron star from the string
    tension sigma = Q_top * Lambda_QCD^2 (T2a), without relying on the
    mean-field Walecka model (which gives M_max = 1.42 M_sun, too low)?

DFC mechanism:
    The maximum neutron star mass is set by the competition between
    gravity (pulling inward) and the nuclear equation of state (pushing
    outward). The stiffest possible EOS is the causal limit: the speed
    of sound equals the speed of light, v_s = c.

    The QCD string tension sigma sets the energy density scale at which
    nuclear matter transitions from hadronic to deconfined phases. Above
    the deconfinement density, the EOS softens dramatically. The string
    tension therefore bounds the maximum stiffness of the nuclear EOS.

    Three independent approaches all use sigma as input:
    (A) Dimensional analysis: M_max ~ M_Pl^3 / sigma
    (B) Rhoades-Ruffini causal limit with DFC matching density
    (C) String tension as maximum energy density -> TOV scaling

    The key DFC input: sigma = Q_top * Lambda^2 = 185,441 MeV^2 (T2a)
    In SI: sigma = 940 MeV/fm = 1.506e5 N (about 15 metric tons)

Tier assessment:
    sigma = Q_top * Lambda^2:    T2a (C243, -2.2% vs lattice)
    Causal limit M_max:          T3 (structural bound, not exact prediction)
    Dimensional scaling:         T3 (order-of-magnitude)

Key references:
    Rhoades & Ruffini (1974): Phys. Rev. Lett. 32, 324
    Koranda, Stergioulas & Friedman (1997): ApJ 488, 799
    equations/ym_string_tension.py — sigma derivation
    equations/nonlinear_walecka_eos.py — mean-field TOV (C375)
    practical_applications/maximum_tensile_strength.md — tensile limit
"""

import math

# =============================================================================
# Assertion infrastructure
# =============================================================================
n_assert = 0
n_pass = 0
n_fail = 0


def check(label, condition):
    global n_assert, n_pass, n_fail
    n_assert += 1
    ok = bool(condition)
    tag = "PASS" if ok else "FAIL"
    if not ok:
        n_fail += 1
    else:
        n_pass += 1
    print(f"  [{tag}] {label}")
    return ok


# =============================================================================
# Physical constants
# =============================================================================
PI = math.pi
HBAR_C = 197.3269804         # MeV fm
C_LIGHT = 2.99792458e10      # cm/s
G_NEWTON = 6.67430e-8        # cm^3 g^-1 s^-2
M_SUN_G = 1.98892e33         # g
M_SUN_MEV = M_SUN_G * C_LIGHT**2 / 1.602176634e-6  # MeV (1 g = c^2/eV)
KM_TO_CM = 1e5
FM_TO_CM = 1e-13
MEV_PER_FM3_TO_DYNE_PER_CM2 = 1.602176634e33  # 1 MeV/fm^3 = 1.602e33 dyne/cm^2
MEV_PER_FM3_TO_G_PER_CM3 = 1.7827e12  # 1 MeV/fm^3 = 1.7827e12 g/cm^3

# Neutron mass
M_N = 939.565       # MeV

# DFC parameters
Q_TOP = 2            # T1
LAMBDA_QCD = 304.5   # MeV, T2a
N_C = 3              # T2a

# DFC string tension
SIGMA_DFC = Q_TOP * LAMBDA_QCD**2   # MeV^2

# Convert string tension to various units
SIGMA_MEV_FM = SIGMA_DFC / HBAR_C   # MeV/fm (energy per length)
SIGMA_N = SIGMA_MEV_FM * 1.602176634e-13 / 1e-15  # Newtons

# Observed NS masses
M_MAX_OBS = 2.08     # M_sun, PSR J0740+6620 (Cromartie+2020, Fonseca+2021)
M_MAX_OBS_ERR = 0.07 # M_sun
M_14_R_OBS = 12.45   # km, NICER for 1.4 M_sun NS (Miller+2021)

# Nuclear saturation
RHO_0 = 0.16         # fm^-3, nuclear saturation density
E_SAT = 923.0        # MeV, energy per nucleon at saturation (M_N - 16.3)


# =============================================================================
# Part A: Dimensional analysis — M_max from string tension
# =============================================================================
print("=" * 72)
print("Part A: Dimensional Scaling — M_max from String Tension")
print("=" * 72)
print()

# The string tension sigma has dimensions [Energy^2] in natural units.
# It sets the characteristic energy density of confined QCD matter:
#   epsilon_QCD ~ sigma^2 / (hbar*c)^4  [energy/volume in natural units]
# But more directly, sigma/hbar_c = energy/length, and the energy density
# at deconfinement is:
#   epsilon_deconf ~ sigma^(3/2) / (hbar*c)^3  [not quite right dimensionally]
#
# Better: sigma has units MeV^2. The QCD energy density scale is:
#   epsilon_QCD ~ Lambda_QCD^4 / (hbar*c)^3
# And sigma = Q_top * Lambda^2, so Lambda^2 = sigma/Q_top.
# epsilon_QCD = (sigma/Q_top)^2 / (hbar*c)^3

epsilon_QCD = (SIGMA_DFC / Q_TOP)**2 / HBAR_C**3   # MeV/fm^3
print(f"DFC string tension: sigma = Q_top * Lambda^2 = {SIGMA_DFC:.0f} MeV^2  [T2a]")
print(f"  = {SIGMA_MEV_FM:.1f} MeV/fm  = {SIGMA_N:.0f} N")
print()
print(f"QCD energy density scale:")
print(f"  epsilon_QCD = Lambda^4 / (hbar*c)^3 = {epsilon_QCD:.1f} MeV/fm^3")
print(f"  = {epsilon_QCD * MEV_PER_FM3_TO_G_PER_CM3:.2e} g/cm^3")
print()

# The maximum NS mass from dimensional analysis (Landau 1932):
# M_max ~ M_Pl^3 / m_n^2 where M_Pl = sqrt(hbar*c/G)
# This gives the Chandrasekhar/OV limit for free neutron gas.
#
# With interactions, the relevant scale is:
# M_max ~ (hbar*c/G)^(3/2) / epsilon_match^(1/2) * c^2
#
# More precisely, the TOV limit for a maximally stiff EOS
# (P = epsilon - epsilon_match for epsilon > epsilon_match) gives:
# M_max = 4.09 * (epsilon_0 / epsilon_match)^(1/2) * M_sun
# where epsilon_0 = c^2 / (4*pi*G*r_0^2) with r_0 = standard nuclear radius
#
# The Rhoades-Ruffini result: for a causal EOS (v_s <= c) matched to a
# known low-density EOS at some matching density rho_match:
# M_max ~ 3.2 * (rho_0/rho_match)^(1/2) * M_sun  [their Eq. 1]

# DFC approach: the matching density is set by deconfinement,
# which occurs when the interquark distance ~ 1/Lambda_QCD
# i.e., rho_deconf ~ Lambda_QCD^3 / (hbar*c)^3

rho_deconf_fm3 = LAMBDA_QCD**3 / HBAR_C**3   # fm^-3
n_deconf = rho_deconf_fm3   # number density in fm^-3
epsilon_deconf = n_deconf * M_N   # energy density MeV/fm^3 (rough)

print(f"Deconfinement density estimate:")
print(f"  n_deconf ~ Lambda^3 / (hbar*c)^3 = {n_deconf:.3f} fm^-3")
print(f"  n_deconf / n_0 = {n_deconf / RHO_0:.2f}")
print(f"  epsilon_deconf ~ n_deconf * M_N = {epsilon_deconf:.0f} MeV/fm^3")
print()

check("A1: deconfinement density > saturation", n_deconf > RHO_0)
check("A2: deconfinement at 2-5 x saturation", 1.5 < n_deconf / RHO_0 < 8)
print()


# =============================================================================
# Part B: Causal limit — Rhoades-Ruffini bound with DFC matching
# =============================================================================
print("=" * 72)
print("Part B: Causal Limit (Rhoades-Ruffini) with DFC Matching Density")
print("=" * 72)
print()

# The Rhoades-Ruffini (1974) upper bound on NS mass:
# For an EOS that is known below a matching pressure P_match,
# and satisfies causality (dP/depsilon <= 1) above P_match:
#
# M_max = 3.2 * sqrt(epsilon_0 / epsilon_match) * M_sun
#
# where epsilon_0 = 2.67e14 g/cm^3 (a reference density) and
# epsilon_match is the energy density at the matching point.
#
# Modern refinement (Koranda, Stergioulas & Friedman 1997):
# M_max^causal = 4.09 * (2e14 / rho_match)^(1/2) * M_sun
# for matching at rho_match in g/cm^3.
#
# We use the standard form: for a maximally stiff causal EOS
# (P = epsilon - epsilon_0 for epsilon > epsilon_0, P = 0 below),
# the TOV solution gives:
# M_max = 4.09 * M_sun * sqrt(epsilon_nuc / epsilon_0)
# where epsilon_nuc ~ 2.67e14 g/cm^3 is nuclear density.
#
# More directly, the formula from Lattimer (2012):
# M_max ~ 2.2 * (P_max / (200 MeV/fm^3))^(1/2) * M_sun
# where P_max is the maximum pressure the EOS can sustain.

# DFC approach: the maximum pressure in nuclear matter is bounded by
# the string tension. The pressure can't exceed the confining force
# per unit area, which is sigma / A_nucleon.
#
# However, this gives the TENSILE limit (~10^34 Pa), which is far
# above any density accessible in NS. The relevant constraint is:
# at what density does the EOS transition from stiff (hadronic) to
# soft (deconfined)?

# Standard approach: TOV with causal EOS matched at DFC deconfinement density
# P = epsilon - epsilon_match for epsilon > epsilon_match
# P = 0 (or known EOS) for epsilon < epsilon_match

# The maximum mass for a causal EOS matched at energy density epsilon_m is:
# M_max = 4.09 * sqrt(epsilon_nuc / epsilon_m) * M_sun  [Rhoades-Ruffini]
# where epsilon_nuc = 2.67e14 g/cm^3 = 150 MeV/fm^3

# DFC matching density: deconfinement at n ~ 2-3 * n_0
# Use the string tension to set the transition pressure:
# P_deconf ~ sigma / (4*pi*r_N^2)  where r_N ~ 1/Lambda is nucleon size
# But this is the tensile limit again.

# Better: the deconfinement energy density from DFC is when the
# average interquark spacing equals the confinement radius 1/Lambda:
# epsilon_deconf = (B_MIT)_DFC where B is the bag constant
# In the MIT bag model, B^(1/4) ~ Lambda_QCD
# B = Lambda^4 / (hbar*c)^3  [same as epsilon_QCD above]

B_MIT = LAMBDA_QCD**4 / HBAR_C**3   # MeV/fm^3 (bag constant)
B_MIT_g_cm3 = B_MIT * MEV_PER_FM3_TO_G_PER_CM3  # g/cm^3

print("DFC bag constant (from Lambda_QCD):")
print(f"  B^(1/4) = Lambda_QCD = {LAMBDA_QCD} MeV")
print(f"  B = Lambda^4 / (hbar*c)^3 = {B_MIT:.1f} MeV/fm^3")
print(f"  B = {B_MIT_g_cm3:.2e} g/cm^3")
print()

# Standard MIT bag: B^(1/4) ~ 145-170 MeV -> B ~ 57-100 MeV/fm^3
# DFC Lambda = 304.5 MeV gives B ~ 1115 MeV/fm^3 — much larger!
# This is because Lambda_QCD in DFC is the confinement scale, not the
# perturbative MS-bar scale. The physical bag constant should use the
# CONFINEMENT scale, not Lambda_QCD directly.
#
# Better estimate: use the gluon condensate / string tension directly.
# The bag constant in terms of string tension:
# B ~ sigma / (pi * R_had^2)  where R_had ~ 1 fm (hadron radius)
# or more precisely, B ~ sigma^2 / (16 * pi^2 * hbar_c^4)

# From lattice QCD: B^(1/4) ~ 200-250 MeV (depends on method)
# The DFC string tension sigma = 940 MeV/fm gives:
# sqrt(sigma) = sqrt(940 MeV/fm) ... not quite right dimensionally

# Let's use the simplest physically motivated route:
# The deconfinement transition occurs at rho ~ (2-3) * rho_0.
# DFC string tension determines WHERE this transition occurs via
# the flux-tube breaking criterion: when the average inter-nucleon
# distance d ~ (rho)^(-1/3) equals the flux-tube breaking length
# L_break = 2*M_q / sqrt(sigma) where M_q is the constituent quark mass.

# Constituent quark mass from DFC Regge: M_q = M_N / N_c = 311.6 MeV
M_Q = math.sqrt(3 * PI) * LAMBDA_QCD / N_C  # constituent quark mass

# Flux tube breaking length: when sigma * L = 2 * M_q (pair production)
L_break = 2 * M_Q / SIGMA_MEV_FM   # fm
print(f"Constituent quark mass: M_q = M_N/N_c = {M_Q:.1f} MeV")
print(f"Flux-tube breaking length: L_break = 2*M_q/sigma_lin = {L_break:.3f} fm")
print()

# Deconfinement density: when mean spacing ~ L_break
rho_deconf_flux = 1.0 / L_break**3   # fm^-3
n_deconf_ratio = rho_deconf_flux / RHO_0

print(f"Deconfinement density (flux-tube criterion):")
print(f"  rho_deconf = 1 / L_break^3 = {rho_deconf_flux:.3f} fm^-3")
print(f"  = {n_deconf_ratio:.1f} * rho_0")
print()

# Energy density at deconfinement
epsilon_match_MeV = rho_deconf_flux * M_N  # MeV/fm^3 (non-relativistic approx)
epsilon_match_g = epsilon_match_MeV * MEV_PER_FM3_TO_G_PER_CM3  # g/cm^3

print(f"Matching energy density:")
print(f"  epsilon_match = {epsilon_match_MeV:.0f} MeV/fm^3")
print(f"  = {epsilon_match_g:.2e} g/cm^3")
print()

# Rhoades-Ruffini formula:
# M_max = 4.09 * sqrt(epsilon_ref / epsilon_match) * M_sun
# where epsilon_ref = 2.67e14 g/cm^3 is the nuclear reference density
# (this is the energy density at nuclear saturation: rho_0 * M_N)
epsilon_ref = RHO_0 * M_N * MEV_PER_FM3_TO_G_PER_CM3  # g/cm^3
# = 0.16 * 939.565 * 1.7827e12 = 2.68e14 g/cm^3

print(f"Reference density: epsilon_ref = rho_0 * M_N = {epsilon_ref:.2e} g/cm^3")
print()

# But the RR formula uses a SPECIFIC known low-density EOS below the match.
# The simplified version (Lattimer & Prakash 2016 review):
# For a maximally stiff causal EOS above a transition density n_t:
# M_max ~ 2.2 * (n_0/n_t)^(1/2) * M_sun   [approximate]
#
# For our DFC transition density:

M_max_causal = 2.2 * math.sqrt(RHO_0 / rho_deconf_flux)

print(f"Causal limit with DFC matching density:")
print(f"  M_max^causal = 2.2 * sqrt(rho_0 / rho_deconf)")
print(f"              = 2.2 * sqrt({RHO_0:.2f} / {rho_deconf_flux:.3f})")
print(f"              = 2.2 * {math.sqrt(RHO_0 / rho_deconf_flux):.4f}")
print(f"              = {M_max_causal:.3f} M_sun")
print()

err_causal = (M_max_causal - M_MAX_OBS) / M_MAX_OBS * 100
print(f"  Observed: M_max = {M_MAX_OBS} +/- {M_MAX_OBS_ERR} M_sun (PSR J0740+6620)")
print(f"  Error: {err_causal:+.1f}%")
print()

check("B1: flux-tube deconfinement at 2-6 * rho_0", 2 < n_deconf_ratio < 6)
check("B2: causal M_max > 1.4 M_sun", M_max_causal > 1.4)
check("B3: causal M_max within 30% of observed", abs(err_causal) < 30)
print()


# =============================================================================
# Part C: Sound speed bound from string tension
# =============================================================================
print("=" * 72)
print("Part C: Sound Speed and EOS Stiffness from String Tension")
print("=" * 72)
print()

# The speed of sound in nuclear matter: v_s^2 = dP/d(epsilon)
# At saturation: v_s^2 = K / (9 * M_N) where K is incompressibility
# DFC Walecka gives K ~ 545 MeV (too stiff)
# Observed: K = 240 +/- 20 MeV

K_obs = 240.0    # MeV
K_dfc_walecka = 545.0  # MeV (from nuclear_walecka_prediction.py)

vs2_sat_obs = K_obs / (9 * M_N)
vs2_sat_dfc = K_dfc_walecka / (9 * M_N)

print(f"Sound speed at saturation:")
print(f"  v_s^2/c^2 = K / (9*M_N)")
print(f"  Observed: K = {K_obs} MeV -> v_s^2/c^2 = {vs2_sat_obs:.4f} -> v_s/c = {math.sqrt(vs2_sat_obs):.3f}")
print(f"  DFC Walecka: K = {K_dfc_walecka} MeV -> v_s^2/c^2 = {vs2_sat_dfc:.4f} -> v_s/c = {math.sqrt(vs2_sat_dfc):.3f}")
print()

# The conformal limit: at very high density, QCD approaches the conformal
# limit v_s^2 = 1/3. The string tension determines HOW the EOS transitions
# from soft (low density) to stiff and then back toward conformal.
#
# DFC constraint: the string tension sets the scale at which the EOS peaks.
# The maximum of v_s^2 occurs near deconfinement and is bounded by:
# v_s^2_max ~ 1 - 4*B/(epsilon_peak)  where B is bag constant and
# epsilon_peak ~ sigma^2/(hbar_c)^4 is the transition energy density.

# A simpler and more robust approach: use the Bedaque-Steiner (2015) result.
# To support a 2 M_sun NS, v_s must EXCEED 1/sqrt(3) (conformal value)
# at some density. The string tension tells us WHERE this happens.

vs_conformal = 1.0 / math.sqrt(3)
print(f"Conformal limit: v_s/c = 1/sqrt(3) = {vs_conformal:.4f}")
print(f"Bedaque-Steiner (2015): 2 M_sun NS requires v_s > 1/sqrt(3)")
print(f"  at some density between 1-5 * rho_0")
print()

# DFC consistency: the mean-field Walecka EOS already exceeds the conformal
# limit (v_s/c = 0.36 > 0.577? No, 0.36 < 0.577).
# Actually v_s/c = sqrt(0.0284) = 0.169 at saturation — well below conformal.
# The stiffening occurs at higher density.

print(f"DFC EOS stiffness summary:")
print(f"  At saturation (rho_0):    v_s/c ~ {math.sqrt(vs2_sat_obs):.3f} (observed)")
print(f"  Conformal limit:          v_s/c = {vs_conformal:.3f}")
print(f"  Causal limit:             v_s/c = 1.000")
print(f"  DFC deconfinement at:     {n_deconf_ratio:.1f} * rho_0")
print()

check("C1: v_s at saturation subcausal", vs2_sat_obs < 1)
check("C2: v_s at saturation sub-conformal", vs2_sat_obs < 1.0/3.0)
print()


# =============================================================================
# Part D: Direct TOV scaling from string tension
# =============================================================================
print("=" * 72)
print("Part D: TOV Scaling — M_max from sigma Directly")
print("=" * 72)
print()

# The TOV maximum mass scales with the central energy density as:
# M_max ~ c^4 / (G^(3/2) * epsilon_c^(1/2))
# where epsilon_c is the central energy density.
#
# For nuclear matter, the relevant energy density is:
# epsilon ~ sigma * n^(4/3) where n is baryon density (dimensional analysis)
# The central density of a maximum-mass NS is typically 5-8 * rho_0.
#
# A cleaner approach uses the Tolman VII solution (analytic TOV):
# M_max = 0.7104 * sqrt(P_c / (G * epsilon_c)) * R_c
# where P_c and epsilon_c are central pressure and energy density.
#
# For the causal EOS (P = epsilon - epsilon_0):
# M_max = 0.0851 * sqrt(c^4 / (G * epsilon_0))  [Koranda+1997]

# In natural units (hbar = c = 1):
# epsilon_0 in MeV/fm^3, G in MeV^-2 * fm
# G_N = 6.674e-11 m^3 kg^-1 s^-2
# In natural units: G = G_N * hbar * c / c^4 = G_N / (hbar * c^3)
# G in MeV^-2: G_MeV = G_N / (hbar_c_SI^3 * c^2)

# Let's use SI and convert
# epsilon_0 in g/cm^3
# M_max in M_sun

# Koranda+1997 formula for maximally compact star:
# M_max = 4.09 * (2.67e14 / rho_c)^(1/2) * M_sun  where rho_c in g/cm^3
# This is for matching at surface density rho_c.

# DFC: the matching energy density is set by when flux tubes overlap,
# i.e., when the baryon density reaches the deconfinement threshold.
# We computed rho_deconf above.

# Alternative: use sigma to set the bag constant directly
# In the MIT bag model with massless quarks:
# epsilon = 3 * (3*pi^2)^(1/3) * n_q^(4/3) / (4*pi) + B
# P = (epsilon - 4*B) / 3
# M_max ~ 1.8 * (B_standard / B)^(1/2) * M_sun  [Witten 1984]
# where B_standard = 56 MeV/fm^3 (standard MIT bag)

# DFC bag constant from string tension:
# B = sigma / (4*pi*R_had^2)  where R_had is the hadron radius
# R_had ~ 1/(2*Lambda) * hbar_c = hbar_c / (2*Lambda)
R_had = HBAR_C / (2 * LAMBDA_QCD)   # fm
B_from_sigma = SIGMA_MEV_FM / (4 * PI * R_had**2)  # MeV/fm^3

print(f"Hadron radius: R_had = hbar_c / (2*Lambda) = {R_had:.3f} fm")
print(f"Bag constant from string tension:")
print(f"  B = sigma_lin / (4*pi*R_had^2) = {B_from_sigma:.1f} MeV/fm^3")
print()

# Standard MIT bag: B^(1/4) ~ 145 MeV -> B ~ 57 MeV/fm^3
B_standard = 57.0  # MeV/fm^3

# The MIT bag model maximum NS mass (Witten 1984, Haensel+2007):
# M_max = 1.96 * (B_std/B)^(1/2) * M_sun  [for strange quark stars]
# For neutron stars with phase transition:
# M_max ~ 2.0 * (B_std/B)^(1/2) * M_sun  [approximate]

M_max_bag = 2.0 * math.sqrt(B_standard / B_from_sigma)
err_bag = (M_max_bag - M_MAX_OBS) / M_MAX_OBS * 100

print(f"MIT bag model scaling:")
print(f"  B_standard = {B_standard} MeV/fm^3")
print(f"  B_DFC = {B_from_sigma:.1f} MeV/fm^3")
print(f"  B_DFC / B_standard = {B_from_sigma / B_standard:.2f}")
print(f"  M_max = 2.0 * sqrt(B_std/B_DFC) = {M_max_bag:.3f} M_sun")
print(f"  Observed: {M_MAX_OBS} M_sun")
print(f"  Error: {err_bag:+.1f}%")
print()

check("D1: bag B_DFC reasonable range (10-500 MeV/fm^3)", 10 < B_from_sigma < 500)
check("D2: M_max from bag within 50% of observed", abs(err_bag) < 50)
print()


# =============================================================================
# Part E: Combined DFC prediction
# =============================================================================
print("=" * 72)
print("Part E: Combined DFC Prediction for NS Maximum Mass")
print("=" * 72)
print()

# Best DFC prediction: use the causal limit with flux-tube deconfinement
# This is the most self-contained (uses only sigma and Lambda_QCD)

print("Three DFC estimates for M_max:")
print()
print(f"  {'Method':<40s}  {'M_max (M_sun)':>14s}  {'Error':>8s}")
print("  " + "-" * 66)
print(f"  {'Causal limit + flux-tube deconf':<40s}  {M_max_causal:>14.3f}  {err_causal:>+7.1f}%")
print(f"  {'MIT bag scaling (B from sigma)':<40s}  {M_max_bag:>14.3f}  {err_bag:>+7.1f}%")

# Geometric mean of the two approaches
M_max_combined = math.sqrt(M_max_causal * M_max_bag)
err_combined = (M_max_combined - M_MAX_OBS) / M_MAX_OBS * 100
print(f"  {'Geometric mean':<40s}  {M_max_combined:>14.3f}  {err_combined:>+7.1f}%")
print()

# The key DFC formula:
# M_max is bounded by the string tension through the deconfinement density.
# rho_deconf = 1 / L_break^3 = (sigma_lin / (2*M_q))^3
# M_max ~ 2.2 * sqrt(rho_0 / rho_deconf) M_sun

print("DFC derivation chain:")
print()
print(f"  sigma = Q_top * Lambda^2 = {SIGMA_DFC:.0f} MeV^2     [T2a]")
print(f"      |")
print(f"  sigma_lin = sigma / (hbar*c) = {SIGMA_MEV_FM:.1f} MeV/fm  [T2a]")
print(f"      |")
print(f"  M_q = sqrt(3*pi) * Lambda / N_c = {M_Q:.1f} MeV      [T3]")
print(f"      |")
print(f"  L_break = 2*M_q / sigma_lin = {L_break:.3f} fm        [T3]")
print(f"      |")
print(f"  rho_deconf = 1/L_break^3 = {rho_deconf_flux:.3f} fm^-3")
print(f"  = {n_deconf_ratio:.1f} * rho_0                          [T3]")
print(f"      |")
print(f"  M_max = 2.2 * sqrt(rho_0/rho_deconf)")
print(f"        = {M_max_causal:.2f} M_sun                       [T3]")
print(f"  Observed: {M_MAX_OBS} +/- {M_MAX_OBS_ERR} M_sun")
print(f"  Error: {err_causal:+.1f}%")
print()

# Also predict the radius of a 1.4 M_sun NS
# R_1.4 ~ 10 * (rho_0 / rho_c)^(1/3) * km  [approximate scaling]
# where rho_c is central density for 1.4 M_sun ~ 2-3 * rho_0
rho_c_14 = 2.5 * RHO_0  # central density for 1.4 M_sun
R_14_est = 10.0 * (RHO_0 / rho_c_14)**(1.0/3.0)  # km
# This gives ~7.4 km, too small. The radius depends strongly on the EOS.
# A better scaling (Lattimer & Prakash 2001):
# R_1.4 ~ 9.3 + 0.7 * (P_1/P_0)^0.25  [km]
# where P_1 is pressure at rho_0 and P_0 = MeV/fm^3

# For the causal EOS, R scales with M as R ~ (M/M_max) * R_max
# R_max ~ 10 km for a typical M_max ~ 2 M_sun NS
# Not enough DFC information to predict R precisely here.

print(f"  Radius prediction: NOT COMPUTED (requires full EOS integration)")
print(f"  The mean-field Walecka EOS gives R(1.4) ~ 8-10 km")
print(f"  (see nonlinear_walecka_eos.py)")
print()

check("E1: DFC deconfinement density in expected range (2-6 rho_0)",
      2 < n_deconf_ratio < 6)
check("E2: M_max prediction within 30% of observed", abs(err_causal) < 30)
check("E3: causal M_max > mean-field M_max (1.42)", M_max_causal > 1.42)
print()


# =============================================================================
# Part F: Comparison with observations and other models
# =============================================================================
print("=" * 72)
print("Part F: Comparison Table")
print("=" * 72)
print()

print(f"  {'Model':<30s}  {'M_max (M_sun)':>14s}  {'Status':>10s}")
print("  " + "-" * 58)
print(f"  {'Observed (PSR J0740+6620)':<30s}  {'2.08 +/- 0.07':>14s}  {'---':>10s}")
print(f"  {'DFC mean-field Walecka':<30s}  {'1.42':>14s}  {'too low':>10s}")
print(f"  {'DFC causal + flux-tube':<30s}  {M_max_causal:>14.2f}  {('OK' if abs(err_causal)<20 else 'off'):>10s}")
print(f"  {'DFC bag scaling':<30s}  {M_max_bag:>14.2f}  {('OK' if abs(err_bag)<20 else 'off'):>10s}")
print(f"  {'Free neutron gas (OV limit)':<30s}  {'0.71':>14s}  {'too low':>10s}")
print(f"  {'NL3 parametrization':<30s}  {'2.77':>14s}  {'too high':>10s}")
print(f"  {'APR EOS':<30s}  {'2.20':>14s}  {'OK':>10s}")
print()

check("F1: DFC causal limit above OV limit (0.71)", M_max_causal > 0.71)
check("F2: DFC causal limit below NL3 (2.77)", M_max_causal < 2.77)
print()


# =============================================================================
# Part G: Tier assessment
# =============================================================================
print("=" * 72)
print("Part G: Tier Assessment")
print("=" * 72)
print()

print("  INPUTS:")
print(f"    sigma = Q_top * Lambda^2:    T2a (-2.2% vs lattice)")
print(f"    M_q = M_N / N_c:            T3 (from baryon Regge)")
print(f"    rho_0 (saturation):          observed input")
print()
print("  DERIVED:")
print(f"    L_break = 2*M_q / sigma_lin: T3")
print(f"    rho_deconf = 1/L_break^3:    T3")
print(f"    M_max (causal):              T3 ({err_causal:+.1f}%)")
print()
print("  OVERALL: T3 — the causal limit with DFC deconfinement gives")
print(f"  M_max = {M_max_causal:.2f} M_sun ({err_causal:+.1f}%), compared to the")
print(f"  mean-field Walecka result of 1.42 M_sun (-32%).")
print()
print("  OPEN GAPS:")
print("  - Full EOS integration (not just causal bound)")
print("  - Beyond-mean-field corrections (RPA, 2PE)")
print("  - NS radius prediction requires full EOS")
print("  - Deconfinement transition order (first vs crossover)")
print()


# =============================================================================
# Summary
# =============================================================================
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()
print(f"  Total assertions: {n_assert}")
print(f"  PASS: {n_pass}")
print(f"  FAIL: {n_fail}")
print()
if n_fail == 0:
    print("  ALL ASSERTIONS PASSED")
else:
    print(f"  {n_fail} ASSERTION(S) FAILED")
print()
print("  KEY RESULT:")
print(f"    DFC string tension sigma = {SIGMA_DFC:.0f} MeV^2 (T2a)")
print(f"    -> deconfinement at {n_deconf_ratio:.1f} * rho_0")
print(f"    -> M_max = {M_max_causal:.2f} M_sun (causal limit)")
print(f"    Observed: {M_MAX_OBS} +/- {M_MAX_OBS_ERR} M_sun")
print(f"    Error: {err_causal:+.1f}%")
print()
print("  NEGATIVE RESULT: The naive flux-tube deconfinement criterion gives")
print("  rho_deconf = 21 * rho_0 (far too high) and M_max = 0.48 M_sun")
print("  (far too low, worse than mean-field Walecka at 1.42 M_sun).")
print()
print("  DIAGNOSIS: The string tension sets the MAXIMUM confining force,")
print("  not the deconfinement threshold. Physical deconfinement occurs by")
print("  percolation at ~2-3 * rho_0, well before flux tubes actually break.")
print("  The DFC string tension alone is insufficient to predict M_max --")
print("  the nuclear EOS at intermediate densities (1-5 * rho_0) is needed,")
print("  which requires many-body physics beyond the string tension.")
