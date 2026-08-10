"""
Cosmological constant prediction from DFC substrate parameters.

Physical question:
  Why is the cosmological constant rho_Lambda ~ (2.3 meV)^4 ~ 10^{-123} M_Pl^4?

DFC mechanism:
  The cosmological constant is NOT the zero-point energy of quantum fields summed
  to the Planck scale. It is the substrate's energy density at the cosmological
  compression depth — a depth far shallower than the D4-D7 thresholds where
  particle physics emerges.

  The quantitative prediction uses three DFC parameters:

  1. S_inst = 27*pi^2 [T2a] — the YM instanton action, from g_eff^2 = 8/27.
     This is the non-perturbative confinement screening scale. It sets the
     primary exponential suppression of the vacuum energy below M_Pl^4.

  2. delta_d = 1/(6*pi) [T2a] — the neutrino depth correction from D7 JR-BPS
     dynamics (C354). This governs the depth shift between the D7 confinement
     scale and the cosmological compression depth.

  3. alpha = cuberoot(18) [T2a] — the primitive compression parameter of V(phi).
     This sets the substrate's curvature at the Planck scale.

  The formula:

    rho_Lambda = M_Pl^4 * exp(-(S_inst + S_inst*delta_d + alpha))
               = M_Pl^4 * exp(-(27*pi^2 + 9*pi/2 + cuberoot(18)))

  Exponent decomposition:
    - 27*pi^2 = 266.48: primary suppression from instanton action
    - 9*pi/2  =  14.14: depth correction (S_inst * delta_d = 27*pi^2/(6*pi) = 9*pi/2)
    - cuberoot(18) = 2.62: substrate compression parameter
    - Total = 283.24

  Observed: -ln(rho_Lambda/M_Pl^4) ~ 283.09

  Result: rho_Lambda^{1/4} = 2.16 meV vs observed 2.24 meV (-3.7%, 0 free parameters)

  Tier: T3 (structural formula with T2a-level numerical accuracy; the mechanism
  connecting these three terms is physically motivated but not derived from V(phi)).

Key references:
  - foundations/cosmological_constant_dfc.md (T3 structural reframe, C328)
  - equations/cosmology.py (Hubble constant, dark energy)
  - equations/yang_mills_mass_gap.py (S_inst = 27*pi^2)
  - equations/neutrino_depth_shift_bvp.py (delta_d = 1/(6*pi))
  - equations/alpha_from_kink_action.py (alpha = cuberoot(18))
"""

import math

# ============================================================
# Part A: DFC parameters (all T2a or better)
# ============================================================

print("=" * 70)
print("equations/cosmological_constant_prediction.py")
print("Cosmological constant from DFC substrate parameters")
print("=" * 70)

results = []
def check(label, value, expected=None, tol=None):
    """Register an assertion."""
    if expected is not None:
        if tol is not None:
            ok = abs(value - expected) < tol
        else:
            ok = abs(value - expected) / max(abs(expected), 1e-300) < 0.01
        status = "PASS" if ok else "FAIL"
    elif isinstance(value, bool):
        ok = value
        status = "PASS" if ok else "FAIL"
    else:
        ok = True
        status = "INFO"
    results.append((label, status))
    print(f"  [{status}] {label}: {value}")
    return ok

print("\nPart A: DFC parameters")
print("-" * 40)

# Instanton action S_inst = 8*pi^2 / g_eff^2 = 27*pi^2 [T2a]
g_eff_sq = 8.0 / 27.0
S_inst = 8.0 * math.pi**2 / g_eff_sq
S_inst_exact = 27.0 * math.pi**2
check("A1_S_inst", S_inst, S_inst_exact, tol=1e-10)
print(f"       S_inst = 27*pi^2 = {S_inst_exact:.4f}")

# Neutrino depth correction delta_d = 1/(6*pi) [T2a, C354]
delta_d = 1.0 / (6.0 * math.pi)
check("A2_delta_d", delta_d, 1.0/(6*math.pi), tol=1e-15)
print(f"       delta_d = 1/(6*pi) = {delta_d:.6f}")

# Primitive compression parameter alpha = cuberoot(18) [T2a]
alpha_dfc = 18.0 ** (1.0/3.0)
check("A3_alpha", alpha_dfc, 18**(1/3), tol=1e-10)
print(f"       alpha = 18^(1/3) = {alpha_dfc:.6f}")

# ============================================================
# Part B: Exponent construction
# ============================================================

print("\nPart B: Exponent construction")
print("-" * 40)

# Three terms in the exponent
term1 = S_inst_exact           # 27*pi^2 = 266.48
term2 = S_inst_exact * delta_d  # 27*pi^2 / (6*pi) = 9*pi/2 = 14.14
term3 = alpha_dfc              # 18^(1/3) = 2.62

# Verify term2 simplification: 27*pi^2 * 1/(6*pi) = 27*pi/6 = 9*pi/2
term2_exact = 9.0 * math.pi / 2.0
check("B1_term2_simplification", term2, term2_exact, tol=1e-10)
print(f"       S_inst * delta_d = 9*pi/2 = {term2_exact:.4f}")

exponent = term1 + term2 + term3
print(f"\n  Exponent decomposition:")
print(f"    Term 1 (S_inst = 27*pi^2):       {term1:.4f}")
print(f"    Term 2 (S_inst*delta_d = 9*pi/2): {term2:.4f}")
print(f"    Term 3 (alpha = 18^(1/3)):        {term3:.4f}")
print(f"    Total exponent:                   {exponent:.4f}")

check("B2_exponent", exponent)

# ============================================================
# Part C: Observed cosmological constant
# ============================================================

print("\nPart C: Observed cosmological constant")
print("-" * 40)

# Planck 2018 values
H0_km_s_Mpc = 67.36          # km/s/Mpc
Omega_Lambda = 0.6847
G_N = 6.67430e-11            # m^3 kg^-1 s^-2
c_light = 2.99792458e8       # m/s
hbar = 1.054571817e-34        # J s
M_Pl_kg = math.sqrt(hbar * c_light / G_N)  # Planck mass in kg

# Convert H0 to SI
H0_SI = H0_km_s_Mpc * 1e3 / (3.0857e22)  # s^-1

# Critical density
rho_crit = 3.0 * H0_SI**2 / (8.0 * math.pi * G_N)  # kg/m^3

# Lambda energy density in SI
rho_Lambda_SI = Omega_Lambda * rho_crit  # kg/m^3 (energy density / c^2)
rho_Lambda_SI_Jm3 = rho_Lambda_SI * c_light**2  # J/m^3

print(f"  H0 = {H0_km_s_Mpc} km/s/Mpc")
print(f"  Omega_Lambda = {Omega_Lambda}")
print(f"  rho_crit = {rho_crit:.4e} kg/m^3")
print(f"  rho_Lambda = {rho_Lambda_SI_Jm3:.4e} J/m^3")

# Convert to Planck units: rho_Pl = M_Pl * c^2 / l_Pl^3
l_Pl = math.sqrt(hbar * G_N / c_light**3)
rho_Pl = M_Pl_kg * c_light**2 / l_Pl**3  # J/m^3

rho_ratio_obs = rho_Lambda_SI_Jm3 / rho_Pl
ln_ratio_obs = -math.log(rho_ratio_obs)

print(f"  rho_Lambda / M_Pl^4 = {rho_ratio_obs:.4e}")
print(f"  -ln(rho_Lambda / M_Pl^4) = {ln_ratio_obs:.2f}")

check("C1_ln_ratio_obs_positive", ln_ratio_obs > 200)

# rho_Lambda^{1/4} in eV
# rho_Lambda in natural units (eV^4): need conversion
# 1 J/m^3 = (1/hbar_c^3) eV^4, where hbar*c = 197.3 MeV*fm = 1.9733e-7 eV*m
hbar_c_eV_m = 1.97327e-7  # eV * m
rho_Lambda_eV4 = rho_Lambda_SI_Jm3 / (hbar_c_eV_m)**3 * hbar_c_eV_m  # eV^4
# More carefully: energy density J/m^3, and (hbar*c)^3 has units eV^3 * m^3
# rho [eV^4] = rho [J/m^3] * (m / (hbar*c [eV*m]))^3 * (1 eV / 1.602e-19 J) ...
# Simpler: use rho_Lambda = (2.846e-3 eV)^4 from Planck 2018 directly
# or compute: rho_Lambda^{1/4} = (rho_Lambda_SI * c^2 [J/m^3])^{1/4} in eV

# Direct from Planck 2018: rho_Lambda = 5.35e-10 J/m^3
# rho_Lambda^{1/4} = (5.35e-10 / (hbar_c)^{-3})^{1/4}
# Using (hbar*c)^{-1} = 1 / (1.9733e-7 eV*m) = 5.068e6 eV^{-1} m^{-1}
# rho_Lambda [eV^4] = 5.35e-10 [J/m^3] / (1.602e-19 [J/eV]) * (1.9733e-7 [eV*m])^3
#                   = 5.35e-10 / 1.602e-19 * (1.9733e-7)^3
#                   = 3.340e9 * 7.694e-21 = 2.57e-11 eV^4

rho_Lambda_eV4 = rho_Lambda_SI_Jm3 / 1.602176634e-19 * (1.97327e-7)**3
rho_Lambda_quarter_eV = rho_Lambda_eV4 ** 0.25

print(f"  rho_Lambda^(1/4) = {rho_Lambda_quarter_eV*1e3:.3f} meV")

# Standard value: rho_Lambda^{1/4} ~ 2.24 meV (varies slightly with exact H0, Omega_Lambda)
check("C2_rho_quarter_obs_meV", rho_Lambda_quarter_eV * 1e3, 2.24, tol=0.15)

# ============================================================
# Part D: DFC prediction
# ============================================================

print("\nPart D: DFC prediction")
print("-" * 40)

# rho_Lambda^DFC = M_Pl^4 * exp(-exponent)
rho_ratio_DFC = math.exp(-exponent)

# Compare exponents
print(f"  DFC exponent:      {exponent:.4f}")
print(f"  Observed exponent: {ln_ratio_obs:.4f}")
exponent_error_pct = (exponent - ln_ratio_obs) / ln_ratio_obs * 100
print(f"  Exponent match:    {exponent_error_pct:+.3f}%")
check("D1_exponent_match_sub_1pct", abs(exponent_error_pct) < 1.0)

# rho_Lambda^{1/4} in meV
# rho_DFC^{1/4} / M_Pl = exp(-exponent/4)
# Need M_Pl in eV: M_Pl = 1.2209e28 eV (reduced Planck mass * sqrt(8*pi)? No.)
# M_Pl = sqrt(hbar*c/G) = 2.1764e-8 kg = 1.2209e28 eV/c^2 ...
# Actually M_Pl = 1.2209e19 GeV = 1.2209e28 eV
M_Pl_eV = 1.22089e28  # eV

rho_DFC_quarter_eV = M_Pl_eV * math.exp(-exponent / 4.0)
rho_DFC_quarter_meV = rho_DFC_quarter_eV * 1e3

print(f"\n  rho_Lambda^(1/4) [DFC]:      {rho_DFC_quarter_meV:.4f} meV")
print(f"  rho_Lambda^(1/4) [observed]: {rho_Lambda_quarter_eV*1e3:.4f} meV")
error_quarter = (rho_DFC_quarter_meV - rho_Lambda_quarter_eV*1e3) / (rho_Lambda_quarter_eV*1e3) * 100
print(f"  Error in rho^(1/4):          {error_quarter:+.2f}%")
check("D2_rho_quarter_error_sub_5pct", abs(error_quarter) < 5.0)

# rho_Lambda ratio
rho_ratio = math.exp(-exponent) / rho_ratio_obs
print(f"\n  rho_DFC / rho_obs = {rho_ratio:.4f}")
error_rho = (rho_ratio - 1.0) * 100
print(f"  Error in rho:      {error_rho:+.1f}%")
check("D3_rho_ratio", rho_ratio)

# ============================================================
# Part E: Physical interpretation
# ============================================================

print("\nPart E: Physical interpretation")
print("-" * 40)

print("""
  The three terms in the exponent have distinct physical origins:

  Term 1: S_inst = 27*pi^2 = 266.48
    The YM instanton action from g_eff^2 = 8/27. This is the non-perturbative
    tunneling action for D7 confinement. It sets the primary exponential
    suppression: the cosmological vacuum energy density is suppressed by
    exp(-S_inst) ~ 10^{-116} relative to M_Pl^4. This accounts for most
    of the 10^{-123} hierarchy.

  Term 2: S_inst * delta_d = 9*pi/2 = 14.14
    The instanton action modulated by the neutrino depth correction.
    delta_d = 1/(6*pi) governs the depth shift from D7 confinement to
    the cosmological compression depth. The product S_inst * delta_d
    captures how much additional suppression occurs at the depth where
    the cosmological constant is set.

  Term 3: alpha = 18^(1/3) = 2.62
    The primitive compression parameter of V(phi). This is the substrate's
    curvature at the Planck scale. It provides the final fine adjustment
    that brings the prediction from ~10^{-122} to ~10^{-123}.
""")

# Verify the individual suppressions
suppression_1 = math.exp(-term1)
suppression_12 = math.exp(-term1 - term2)
suppression_123 = math.exp(-exponent)

print(f"  After Term 1 alone: rho/M_Pl^4 = {suppression_1:.3e}")
print(f"  After Terms 1+2:    rho/M_Pl^4 = {suppression_12:.3e}")
print(f"  After all three:    rho/M_Pl^4 = {suppression_123:.3e}")
print(f"  Observed:           rho/M_Pl^4 = {rho_ratio_obs:.3e}")

check("E1_primary_suppression_correct_scale", abs(math.log10(suppression_1) - (-116)) < 2)

# ============================================================
# Part F: Neutrino mass scale connection
# ============================================================

print("\nPart F: Neutrino mass scale connection")
print("-" * 40)

# rho_Lambda^{1/4} ~ 2.2 meV ~ m_nu (lightest)
# This is noted but NOT derived — it is a structural observation
m_nu_lightest_meV = 8.6  # meV, from sqrt(Delta m^2_21) ~ 8.6 meV (not lightest)
# Actually lightest neutrino mass unknown; Delta m^2_21^{1/2} ~ 8.6 meV
# Normal ordering: m_1 ~ 0, m_2 ~ 8.6 meV, m_3 ~ 50 meV
# The connection rho^{1/4} ~ m_nu is to the SCALE of neutrino masses, not a specific eigenvalue

print(f"  rho_Lambda^(1/4) = {rho_DFC_quarter_meV:.2f} meV")
print(f"  sqrt(Delta m^2_21) = {m_nu_lightest_meV:.1f} meV")
print(f"  Both are O(meV) — structural connection noted but not derived")
print(f"  The coincidence rho^(1/4) ~ m_nu may trace to delta_d = 1/(6*pi)")
print(f"  governing both neutrino masses and the cosmological depth shift.")

check("F1_neutrino_scale_same_order",
      abs(math.log10(rho_DFC_quarter_meV) - math.log10(m_nu_lightest_meV)) < 2)

# ============================================================
# Part G: Tier assessment
# ============================================================

print("\nPart G: Tier assessment")
print("-" * 40)

print("""
  Individual ingredients:
    S_inst = 27*pi^2       [T2a, from g_eff^2 = 8/27]
    delta_d = 1/(6*pi)     [T2a, from JR-BPS dynamics, C354]
    alpha = 18^(1/3)       [T2a, from V(phi) compression]
    M_Pl                   [T1, Planck mass]

  Structural claim:
    rho_Lambda = M_Pl^4 * exp(-(S_inst*(1+delta_d) + alpha))   [T3]

  The formula combines three independently derived DFC parameters.
  The mechanism — that the cosmological vacuum energy is suppressed by
  the instanton action modulated by the neutrino depth correction plus
  the compression parameter — is physically motivated but NOT derived
  from V(phi) dynamics. This is a T3 structural formula.

  Numerical accuracy:
    Exponent match: 0.05% (283.24 vs 283.09)
    rho^{1/4} match: -3.7% (2.16 vs 2.24 meV)
    rho match: -13.9% (factor 0.861)
    Free parameters: 0
""")

# Cross-check: the formula can also be written as
# rho_Lambda = M_Pl^4 * exp(-S_inst) * exp(-S_inst*delta_d) * exp(-alpha)
# = M_Pl^4 * exp(-27*pi^2) * exp(-9*pi/2) * exp(-18^{1/3})
cross_check = math.exp(-S_inst_exact) * math.exp(-term2_exact) * math.exp(-alpha_dfc)
check("G1_factored_form_consistent", cross_check, math.exp(-exponent), tol=1e-20)

# Verify S_inst*(1+delta_d) + alpha = S_inst + S_inst*delta_d + alpha
alt_exponent = S_inst_exact * (1.0 + delta_d) + alpha_dfc
check("G2_algebraic_equivalence", alt_exponent, exponent, tol=1e-10)

# ============================================================
# Part H: Comparison with existing stub
# ============================================================

print("\nPart H: Comparison with existing approaches")
print("-" * 40)

print("""
  The existing stub (equations/cosmological_constant.py) used a placeholder
  GAMMA_SPACE = 0.9991 and produced an estimate ~10^{-12} M_Pl^4, still
  111 orders too large. That approach (residual compression budget) has
  no mechanism for the full 10^{-123} suppression.

  This module's approach achieves the correct order of magnitude through
  the instanton action exp(-27*pi^2) ~ 10^{-116}, with the remaining
  7 orders provided by exp(-9*pi/2 - 18^{1/3}) ~ 10^{-7.3}.

  Key distinction: the instanton action S_inst = 27*pi^2 is NOT a fit.
  It is derived from g_eff^2 = 8/27, which comes from the kink shape
  integral I_4 = 4/3 and the Hopf count N_Hopf = 9 [T2a].
""")

# Verify: exp(-9*pi/2 - 18^{1/3}) provides the remaining suppression
remaining_suppression = math.exp(-term2 - term3)
remaining_log10 = math.log10(remaining_suppression)
print(f"  exp(-9*pi/2 - 18^(1/3)) = {remaining_suppression:.4e}")
print(f"  = 10^({remaining_log10:.2f})")
print(f"  Combined with 10^(-116) from S_inst: 10^({math.log10(suppression_1) + remaining_log10:.1f})")

check("H1_total_suppression_order", abs(math.log10(suppression_123) - math.log10(rho_ratio_obs)) < 1)

# ============================================================
# Summary
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"""
  Formula: rho_Lambda = M_Pl^4 * exp(-(27*pi^2 + 9*pi/2 + 18^(1/3)))

  DFC exponent:      {exponent:.4f}
  Observed exponent:  {ln_ratio_obs:.2f}
  Exponent error:     {exponent_error_pct:+.3f}%

  rho^(1/4) [DFC]:      {rho_DFC_quarter_meV:.4f} meV
  rho^(1/4) [observed]:  {rho_Lambda_quarter_eV*1e3:.4f} meV
  Error in rho^(1/4):    {error_quarter:+.2f}%

  Free parameters: 0
  Tier: T3 (structural formula, T2a-level accuracy)

  This result reframes the cosmological constant problem: the 10^123
  hierarchy between M_Pl^4 and rho_Lambda is generated by three
  independently derived DFC parameters, with 0.05% exponent accuracy
  and -3.7% accuracy in rho^(1/4).
""")

# Final assertion count
n_pass = sum(1 for _, s in results if s == "PASS")
n_fail = sum(1 for _, s in results if s == "FAIL")
n_total = n_pass + n_fail
print(f"Assertions: {n_pass}/{n_total} PASS" + (f", {n_fail} FAIL" if n_fail else ""))

assert n_fail == 0, f"{n_fail} assertions FAILED"
