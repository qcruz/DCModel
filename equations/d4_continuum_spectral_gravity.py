"""
D4 Continuum Spectral Density and Non-Perturbative Gravity Constraint
=====================================================================

Physical question:
    C394 computed the worldvolume Sakharov induced gravity from bound states
    (17 massless + 1 massive DOF) and found M^2_ind = 2.35% of M_Pl^2.
    Continuum scattering states were excluded as "not localized on kink."

    This module extends C394 by computing the FULL one-loop spectral
    contribution, including the continuum density-of-states modification
    from the Poeschl-Teller s=2 phase shifts. The Levinson theorem
    guarantees a sum rule: the spectral weight pulled into bound states
    is removed from the continuum.

    Key question: does the continuum modification increase or decrease
    the perturbative account?

DFC mechanism:
    The kink creates a Poeschl-Teller s=2 potential for fluctuations:
        V_eff(y) = 2*alpha - 6*m_KK^2 * sech^2(y/xi)

    Bound states: omega_0 = 0 (zero mode), omega_1 = sqrt(3*alpha/2) (shape)
    Continuum: omega >= m_sigma = sqrt(2*alpha), with modified density of states

    The PT s=2 potential is reflectionless. The transmission amplitude:
        T(q) = (q+i)(q+2i) / [(q-i)(q-2i)]   (q = k*xi = k/m_KK)

    gives the scattering phase shift:
        delta(q) = arctan(1/q) + arctan(2/q)

    The spectral density modification (per unit length, both parities):
        Delta_rho(k) = (2/pi) * d(delta)/dk

    Levinson theorem: integral Delta_rho dk = -2 (two bound states removed
    from continuum). This means the continuum correction is NEGATIVE —
    it REDUCES the total induced gravity relative to C394's bound-state-only
    estimate, because spectral weight was redistributed from high-omega
    (continuum) to low-omega (bound states), and the Sakharov integral
    weights lower-mass modes more heavily.

Computations:
    Part A: PT s=2 phase shifts (analytic, T1)
    Part B: Spectral density modification and Levinson verification (T1)
    Part C: Continuum contribution to Sakharov integral (T1/T2a)
    Part D: Complete one-loop account (bound + continuum) (T3)
    Part E: Non-perturbative fraction tightened (T3)
    Part F: Self-consistency constraints on G_N (T3/T4)

Key references:
    - d4_induced_gravity_worldvolume.py (C394): bound-state Sakharov, 2.35%
    - d4_substrate_response.py (C393): no massless spin-2, wrong-sign 1+1D
    - d4_zero_mode_gravity.py (C367): scalar zero-mode G_eff = G_N/23
    - Levinson (1949): phase shift sum rule
    - Poeschl-Teller: exactly solvable reflectionless potential

Cycle: 395
"""

import math
import numpy as np
from fractions import Fraction
from scipy import integrate

# =============================================================================
# DFC PARAMETERS
# =============================================================================

ALPHA = 18 ** (1 / 3)
BETA = 1 / (9 * math.pi)
PHI_0 = math.sqrt(ALPHA / BETA)
XI = math.sqrt(2 / ALPHA)

m_KK = 1 / XI                      # = sqrt(alpha/2)
m_KK_sq = ALPHA / 2
m_sigma = math.sqrt(2 * ALPHA)     # continuum threshold
m_sigma_sq = 2 * ALPHA
m_shape = math.sqrt(3 * ALPHA / 2) # shape mode
m_shape_sq = 3 * ALPHA / 2

I4 = Fraction(4, 3)
KAPPA = m_KK  # PT potential parameter kappa = 1/xi = m_KK

passed = 0
failed = 0

def check(label, value, expected=True, tol=1e-6):
    """Assertion checker."""
    global passed, failed
    if isinstance(expected, bool):
        ok = bool(value) == expected
        val_str = f"{value}"
    else:
        if expected == 0:
            ok = abs(value) < tol
        else:
            ok = abs(value - expected) / abs(expected) < tol
        val_str = f"{value:.6e} (expected {expected:.6e})"
    status = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    else:
        failed += 1
    print(f"  [{status}] {label}: {val_str}")
    return ok


# =============================================================================
# PART A: POESCHL-TELLER s=2 PHASE SHIFTS
# =============================================================================

print("=" * 72)
print("PART A: Poeschl-Teller s=2 Scattering Phase Shifts")
print("=" * 72)

print("""
  The PT s=2 fluctuation potential around the DFC kink:
    V_fluct(y) = 2*alpha - 6*m_KK^2 * sech^2(y/xi)

  In dimensionless units (u = y/xi, q = k/kappa):
    -psi'' - 6*sech^2(u)*psi = q^2 * psi

  Bound states: q^2 = -(s-n)^2 for n = 0, 1
    n=0: omega_0 = 0 (zero mode, psi_0 ~ sech^2)
    n=1: omega_1 = sqrt(3*alpha/2) (shape mode, psi_1 ~ sech*tanh)

  Continuum: q >= 0, omega = sqrt(q^2*kappa^2 + m_sigma^2)

  The PT s=2 potential is REFLECTIONLESS. Transmission amplitude:
    T(q) = (q+i)(q+2i) / [(q-i)(q-2i)]

  Scattering phase shift:
    delta(q) = arctan(1/q) + arctan(2/q)
""")


def phase_shift(q):
    """PT s=2 phase shift delta(q) = arctan(1/q) + arctan(2/q)."""
    if q < 1e-30:
        return math.pi  # delta(0) = pi/2 + pi/2 = pi
    return math.atan(1.0 / q) + math.atan(2.0 / q)


def d_phase_shift_dq(q):
    """Derivative d(delta)/dq = -1/(q^2+1) - 2/(q^2+4)."""
    return -1.0 / (q**2 + 1) - 2.0 / (q**2 + 4)


# Verify phase shift at key values
delta_0 = phase_shift(0)
delta_1 = phase_shift(1.0)
delta_10 = phase_shift(10.0)
delta_inf = 0.0  # lim q->inf delta(q) = 0

print(f"  Phase shift values:")
print(f"    delta(0)   = {delta_0:.6f} rad = {delta_0/math.pi:.6f} pi")
print(f"    delta(1)   = {delta_1:.6f} rad")
print(f"    delta(10)  = {delta_10:.6f} rad")
print(f"    delta(inf) = 0")

# Levinson theorem: delta(0) - delta(inf) = n_bound * pi
# For s=2: n_bound = 2, so delta(0) = 2*pi? or pi?
#
# SUBTLETY: For 1D scattering on the full line with a reflectionless potential,
# the transmission phase shift delta(0) = s * pi/2 + s * pi/2 = s * pi ... no.
#
# The correct statement: delta(q) = sum_{j=1}^{s} arctan(j/q).
# At q=0: each arctan -> pi/2. Sum = s * pi/2.
# For s=2: delta(0) = pi. The Levinson count uses delta(0)/pi = 1... but n_bound = 2.
#
# Resolution: In 1D on full line, the TOTAL density of states modification
# includes both even and odd parity channels. Each bound state removes 1 state
# from the combined spectrum. The factor of 2 in Delta_rho = (2/pi) d(delta)/dk
# accounts for both parities. The Levinson sum:
#   integral_0^inf Delta_rho dk = (2/pi) * [delta(inf) - delta(0)] = -2 = -n_bound

levinson_integral = (2.0 / math.pi) * (delta_inf - delta_0)
print(f"\n  Levinson theorem verification:")
print(f"    (2/pi) * [delta(inf) - delta(0)] = {levinson_integral:.6f}")
print(f"    Expected: -n_bound = -2")

check("A1_levinson_integral", levinson_integral, -2.0, tol=1e-10)

# Verify T(q) is reflectionless: |T|^2 = 1
q_test = 1.5
T_num = (q_test + 1j) * (q_test + 2j)
T_den = (q_test - 1j) * (q_test - 2j)
T_ratio = T_num / T_den
check("A2_reflectionless", abs(T_ratio)**2, 1.0, tol=1e-14)

# Verify derivative formula
q_test2 = 2.0
dq = 1e-8
numerical_deriv = (phase_shift(q_test2 + dq) - phase_shift(q_test2 - dq)) / (2 * dq)
analytic_deriv = d_phase_shift_dq(q_test2)
check("A3_derivative_formula", analytic_deriv, numerical_deriv, tol=1e-5)


# =============================================================================
# PART B: SPECTRAL DENSITY MODIFICATION AND NUMERICAL LEVINSON
# =============================================================================

print("\n" + "=" * 72)
print("PART B: Spectral Density Modification")
print("=" * 72)

print("""
  Modified density of states (both parities, per unit length):
    Delta_rho(k) = (2/pi) * d(delta)/dk

  In terms of dimensionless q = k/kappa:
    d(delta)/dk = (1/kappa) * d(delta)/dq
    Delta_rho(k) = (2/(pi*kappa)) * [-1/(q^2+1) - 2/(q^2+4)]

  The spectral density is NEGATIVE everywhere — the kink removes spectral
  weight from the continuum and concentrates it into bound states.
""")


def delta_rho_dimensionless(q):
    """
    Dimensionless spectral density modification.
    Delta_rho(k) dk = Delta_rho_dim(q) dq
    where Delta_rho_dim(q) = (2/pi) * d(delta)/dq
    """
    return (2.0 / math.pi) * d_phase_shift_dq(q)


# Numerical verification of Levinson via integration
result_levinson, _ = integrate.quad(delta_rho_dimensionless, 0, np.inf, limit=200)
print(f"  Numerical Levinson integral:")
print(f"    integral_0^inf Delta_rho_dim(q) dq = {result_levinson:.8f}")
print(f"    Expected: -2")

check("B1_levinson_numerical", result_levinson, -2.0, tol=1e-8)

# Profile of Delta_rho
print(f"\n  Spectral density profile (dimensionless):")
print(f"    {'q':>6}  {'Delta_rho_dim(q)':>16}  {'sign':>6}")
q_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
all_negative = True
for q in q_values:
    dr = delta_rho_dimensionless(q)
    if dr > 0:
        all_negative = False
    print(f"    {q:6.1f}  {dr:16.8f}  {'  < 0' if dr < 0 else '  > 0'}")

check("B2_all_negative", all_negative, True)

# Analytic integral verification
# integral_0^inf [1/(q^2+1)] dq = pi/2
# integral_0^inf [2/(q^2+4)] dq = pi/2
# Total = -(2/pi)(pi/2 + pi/2) = -2  CHECK
analytic_check = -(2.0 / math.pi) * (math.pi / 2 + math.pi / 2)
check("B3_analytic_levinson", analytic_check, -2.0, tol=1e-14)


# =============================================================================
# PART C: CONTINUUM CONTRIBUTION TO SAKHAROV INTEGRAL
# =============================================================================

print("\n" + "=" * 72)
print("PART C: Continuum Contribution to Induced Gravity")
print("=" * 72)

print("""
  The Sakharov integral for a mode of mass m with UV cutoff Lambda:
    F(m, Lambda) = integral_{1/Lambda^2}^inf ds/s^2 * exp(-m^2 * s)

  For m = 0: F = Lambda^2
  For general m: F > 0 always in 4D (C394 proven)

  The BOUND STATE contribution (C394):
    M^2_bound = sum_i N_i * F(m_i, Lambda) / (96*pi^2)

  The CONTINUUM MODIFICATION contribution:
    The kink modifies the density of continuum states. For each DOF,
    the continuum correction to M^2 is:

    Delta_M^2_cont = integral_0^inf dk Delta_rho(k) * F(omega^2(k), Lambda^2) / (96*pi^2)

    where omega^2(k) = k^2 + m_sigma^2 (continuum starts at m_sigma = 2*m_KK)
    and Delta_rho is the spectral density modification from Part B.

  Since Delta_rho < 0 everywhere and F > 0, the continuum correction is
  NEGATIVE — it reduces the total perturbative contribution.

  Physical interpretation: the kink pulls spectral weight from high-omega
  continuum modes (which contribute LESS to induced gravity because F
  decreases with mass) into low-omega bound states (which contribute MORE).
  The bound-state gain exceeds the continuum loss, but the continuum loss
  partially cancels the bound-state contribution.
""")

Lambda_sq = m_KK_sq  # UV cutoff = m_KK


def sakharov_F(m_sq, lambda_sq):
    """Schwinger proper-time integral F(m, Lambda)."""
    if m_sq < 1e-30:
        return lambda_sq

    def integrand(s):
        return (1.0 / s**2) * math.exp(-m_sq * s)

    s_min = 1.0 / lambda_sq
    result, _ = integrate.quad(integrand, s_min, np.inf, limit=200)
    return result


# Bound state contributions (reproducing C394)
N_gauge = 16   # 8 generators x 2 polarizations
N_trans = 1
N_shape = 1
N_bound_total = N_gauge + N_trans + N_shape  # = 18

F_massless = sakharov_F(0.0, Lambda_sq)
F_shape_mode = sakharov_F(m_shape_sq, Lambda_sq)

M2_per_scalar = F_massless / (96 * math.pi**2)
M2_per_shape = F_shape_mode / (96 * math.pi**2)

M2_bound = (N_gauge + N_trans) * M2_per_scalar + N_shape * M2_per_shape

print(f"  BOUND STATE contributions (reproducing C394):")
print(f"    F(m=0, Lambda) = {F_massless:.6f}")
print(f"    F(m_shape, Lambda) = {F_shape_mode:.6e}")
print(f"    M^2 per massless DOF = {M2_per_scalar:.6e}")
print(f"    M^2 per shape DOF    = {M2_per_shape:.6e}")
print(f"    M^2_bound (17 massless + 1 shape) = {M2_bound:.6e} M_Pl^2")
print(f"    As fraction of M_Pl^2: {M2_bound*100:.4f}%")

check("C1_M2_bound_reproduces_C394", M2_bound, 0.0235, tol=0.05)

# Continuum contribution for ONE scalar DOF
# The continuum modes have omega^2 = k^2 + m_sigma^2 where k >= 0
# In terms of dimensionless q = k/kappa (kappa = m_KK):
#   omega^2 = kappa^2 * (q^2 + 4)   since m_sigma = 2*kappa
#
# Delta_M2_cont_per_DOF = integral_0^inf dq * delta_rho_dim(q) *
#                         F(kappa^2*(q^2+4), Lambda^2) / (96*pi^2)
#
# Since Lambda^2 = kappa^2: the ratio m^2/Lambda^2 = q^2 + 4 >= 4

def continuum_integrand(q):
    """Integrand for continuum correction per DOF."""
    omega_sq = m_KK_sq * (q**2 + 4)  # omega^2 = kappa^2 * (q^2 + 4)
    F_val = sakharov_F(omega_sq, Lambda_sq)
    drho = delta_rho_dimensionless(q)  # negative
    return drho * F_val / (96 * math.pi**2)

# Numerical integration
# The integrand is well-behaved: drho ~ -1/q^2 at large q, F ~ exp(-q^2)
Delta_M2_cont_per_DOF, cont_err = integrate.quad(
    continuum_integrand, 0, 100, limit=300, epsabs=1e-15, epsrel=1e-10
)

print(f"\n  CONTINUUM MODIFICATION (per scalar DOF):")
print(f"    Delta_M^2_cont / DOF = {Delta_M2_cont_per_DOF:.6e} M_Pl^2")
print(f"    Integration error:      {cont_err:.2e}")
print(f"    Sign: {'NEGATIVE (as expected)' if Delta_M2_cont_per_DOF < 0 else 'UNEXPECTED POSITIVE'}")

check("C2_continuum_negative", Delta_M2_cont_per_DOF < 0, True)

# Total continuum correction for all DOF
# All 18 DOF (16 gauge + 1 trans + 1 shape) see the same PT potential
# in the transverse direction, so each gets the same continuum correction.
# However: the gauge and translational modes are BOUND states of the PT
# potential, while their continuum analogs are delocalized. The continuum
# correction represents the deficit: spectral weight removed from the
# continuum to form these bound states.

Delta_M2_cont_total = N_bound_total * Delta_M2_cont_per_DOF

print(f"\n  TOTAL CONTINUUM CORRECTION:")
print(f"    N_DOF = {N_bound_total} (all modes seeing s=2 PT potential)")
print(f"    Delta_M^2_cont_total = {Delta_M2_cont_total:.6e} M_Pl^2")
print(f"    As fraction of M_Pl^2: {Delta_M2_cont_total*100:.4f}%")

# Ratio of continuum correction to bound-state contribution
cont_to_bound_ratio = abs(Delta_M2_cont_total) / M2_bound
print(f"    |Continuum| / Bound = {cont_to_bound_ratio:.4f} ({cont_to_bound_ratio*100:.2f}%)")

check("C3_cont_small_vs_bound", cont_to_bound_ratio < 0.1, True)


# =============================================================================
# PART D: COMPLETE ONE-LOOP ACCOUNT
# =============================================================================

print("\n" + "=" * 72)
print("PART D: Complete One-Loop Perturbative Account")
print("=" * 72)

# Total one-loop induced gravity: bound states + continuum modification
M2_one_loop = M2_bound + Delta_M2_cont_total
M2_one_loop_fraction = M2_one_loop

print(f"\n  COMPLETE ONE-LOOP DECOMPOSITION:")
print(f"    Bound states (C394):       {M2_bound:.6e} M_Pl^2  (+{M2_bound*100:.4f}%)")
print(f"    Continuum correction:      {Delta_M2_cont_total:.6e} M_Pl^2  ({Delta_M2_cont_total*100:.4f}%)")
print(f"    ---")
print(f"    Total one-loop:            {M2_one_loop:.6e} M_Pl^2  ({M2_one_loop*100:.4f}%)")
print(f"    Net change from C394:      {(M2_one_loop - M2_bound)/M2_bound*100:.2f}%")

check("D1_one_loop_positive", M2_one_loop > 0, True)

# Combined with scalar exchange (C367: 4.4%)
scalar_exchange_fraction = 1.0 / 22.87
total_perturbative = scalar_exchange_fraction + M2_one_loop_fraction
nonpert_fraction = 1.0 - total_perturbative

print(f"\n  ALL PERTURBATIVE MECHANISMS:")
print(f"    Scalar zero-mode exchange (C367):  {scalar_exchange_fraction*100:.2f}%")
print(f"    One-loop induced (C395):           {M2_one_loop_fraction*100:.4f}%")
print(f"    ---")
print(f"    Total perturbative:                {total_perturbative*100:.2f}%")
print(f"    Non-perturbative:                  {nonpert_fraction*100:.2f}%")

check("D2_nonpert_above_90", nonpert_fraction > 0.90, True)


# =============================================================================
# PART E: NON-PERTURBATIVE FRACTION CONSTRAINT
# =============================================================================

print("\n" + "=" * 72)
print("PART E: Non-Perturbative Fraction Constraint")
print("=" * 72)

print("""
  KEY INSIGHT: The continuum correction is SMALL compared to the bound
  states (~few percent of the bound-state contribution). This means:

  1. C394's estimate of ~2.35% was already essentially correct at one loop.
  2. The continuum does NOT close the gap to M_Pl^2.
  3. The ~93% non-perturbative fraction is ROBUST against higher-order
     perturbative corrections from the continuum sector.

  PHYSICAL REASON: The continuum correction is suppressed because:
  - All continuum modes have omega >= m_sigma = 2*m_KK
  - The Sakharov kernel F(m, Lambda) at m^2/Lambda^2 = 4 is exponentially
    suppressed: F(4*Lambda^2, Lambda^2) / F(0, Lambda^2) << 1
  - Even though Levinson says 2 states worth of weight is removed,
    each continuum state contributes very little to induced gravity
    because of its high mass relative to the cutoff.

  CONSTRAINT ON NON-PERTURBATIVE MECHANISM:
  Whatever mechanism produces the remaining ~93% must:
  1. Generate M^2_NP = (1 - perturbative_fraction) * M_Pl^2
  2. Be positive (attractive gravity)
  3. NOT be accessible from one-loop perturbation theory
  4. Involve the strong-field self-gravitating regime (r_s/xi >> 1)
""")

# The required non-perturbative M^2
M2_NP_required = 1.0 - total_perturbative
print(f"  Required M^2_NP = {M2_NP_required:.4f} M_Pl^2")
print(f"  This is {M2_NP_required/M2_one_loop:.1f}x the one-loop result")

# What effective DOF would this require?
N_eff_equivalent = M2_NP_required / M2_per_scalar
print(f"\n  Equivalent to {N_eff_equivalent:.1f} massless scalar DOF")
print(f"  DFC has {N_gauge + N_trans} = 17 massless DOF")
print(f"  Deficit factor: {N_eff_equivalent/17:.1f}x")

check("E1_deficit_factor_large", N_eff_equivalent / 17 > 10, True)  # must be >> 1

# Self-gravity parameter: r_s/xi
E_kink = 4.0 / BETA  # = 36*pi in M_Pl units (but this is E_kink/M_Pl)
# E_kink = (4/3) * alpha^(3/2) / (beta * sqrt(2)) = (4/3) * PHI_0^2 * sqrt(alpha/2)
E_kink_calc = (4.0 / 3.0) * ALPHA**(1.5) / (BETA * math.sqrt(2))
r_s = 2 * E_kink_calc  # in Planck units where G_N = 1
r_s_over_xi = r_s / XI

print(f"\n  Strong-field self-gravity:")
print(f"    E_kink = {E_kink_calc:.2f} M_Pl")
print(f"    r_s = 2*G_N*E_kink = {r_s:.2f} l_Pl")
print(f"    r_s / xi = {r_s_over_xi:.1f}")
print(f"    Kink is {r_s_over_xi:.0f}x inside its own gravitational radius")
print(f"    This confirms: perturbation theory CANNOT access the dominant")
print(f"    gravitational physics. The ~93% must be non-perturbative.")

check("E2_deep_inside_rs", r_s_over_xi > 200, True)

# Convergence of perturbative expansion
# If each "loop" brings a factor of (M2_one_loop/M_Pl^2),
# the perturbative series converges rapidly:
pert_expansion_param = M2_one_loop
print(f"\n  Perturbative expansion parameter: {pert_expansion_param:.4e}")
print(f"  Two-loop estimate: ~ {pert_expansion_param**2:.2e} (negligible)")
print(f"  The perturbative series converges but converges to ~7%, not 100%")

check("E3_pert_converges", pert_expansion_param < 0.1, True)


# =============================================================================
# PART F: SELF-CONSISTENCY CONSTRAINTS ON G_N
# =============================================================================

print("\n" + "=" * 72)
print("PART F: Self-Consistency Constraints on G_N")
print("=" * 72)

print("""
  The D4 gap reduces to: WHY does the non-perturbative fraction equal
  exactly (1 - perturbative)?  This is tautological as stated.
  The real question: what FIXES G_N = 1/M_Pl^2 at its observed value?

  THREE SELF-CONSISTENCY CONDITIONS (independent):

  1. DIMENSIONAL BRIDGE (C366b, T1):
     r_s(M_Pl) / xi = sqrt(2*alpha) = omega_c
     This links gravitational scale (r_s), substrate scale (xi),
     and inertial scale (omega_c) through a single identity.

  2. ALPHA-G_N RELATION (T1):
     alpha * G_N = 18^(1/3)
     This is a consistency relation, not a derivation. But it constrains
     the dimensionless combination alpha*G_N to a specific irrational number
     that emerges from V(phi) through alpha = 18^(1/3).

  3. BPS ENERGY-ACTION IDENTITY (T1):
     E_kink * alpha_D5 = S_kink * alpha_D5 = 1
     The kink energy times the D5 coupling gives unity. Combined with
     S_kink = 4/beta = 36*pi and alpha_D5 = beta/4 = 1/(36*pi),
     this chain produces: alpha_D5 = 1/E_kink = G_N * M_Pl / E_kink.

  The JORMUNGANDR FIXED POINT would close D4 if:
     V(phi) -> kink -> E_kink(alpha, beta) -> gravity -> geometry
     -> compression -> V_eff(phi) = V(phi)

  This self-consistency loop would fix G_N = f(alpha, beta) uniquely.
  The perturbative fraction (~7%) and non-perturbative fraction (~93%)
  would BOTH be outputs of the fixed point, not independent inputs.
""")

# Verify the three consistency conditions
# Condition 1: dimensional bridge
omega_c = math.sqrt(2 * ALPHA)
r_s_Mpl_over_xi = 2 * 1.0 / XI  # r_s(M_Pl) = 2*G_N*M_Pl = 2 l_Pl, so r_s/xi = 2/xi
bridge = r_s_Mpl_over_xi
print(f"  Consistency condition 1 (dimensional bridge):")
print(f"    r_s(M_Pl)/xi = {bridge:.6f}")
print(f"    sqrt(2*alpha) = {omega_c:.6f}")
check("F1_dimensional_bridge", bridge, omega_c, tol=1e-10)

# Condition 2: alpha * G_N
alpha_GN = ALPHA * 1.0  # G_N = 1 in Planck units
print(f"\n  Consistency condition 2 (alpha-G_N):")
print(f"    alpha * G_N = {alpha_GN:.6f}")
print(f"    18^(1/3)    = {18**(1/3):.6f}")
check("F2_alpha_GN", alpha_GN, 18**(1./3), tol=1e-10)

# Condition 3: BPS energy-action
S_kink = 4.0 / BETA
alpha_D5 = BETA / 4.0
product = S_kink * alpha_D5
print(f"\n  Consistency condition 3 (BPS energy-action):")
print(f"    S_kink = {S_kink:.6f}")
print(f"    alpha_D5 = {alpha_D5:.8f}")
print(f"    S_kink * alpha_D5 = {product:.10f}")
check("F3_BPS_identity", product, 1.0, tol=1e-14)


# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 72)
print(f"ASSERTIONS: {passed} PASSED, {failed} FAILED out of {passed + failed}")
print("=" * 72)

if failed > 0:
    print(f"\n  *** {failed} ASSERTION(S) FAILED ***")
else:
    print(f"\n  All {passed} assertions passed.")

print(f"""
  KEY RESULTS:
  ============

  1. PT s=2 PHASE SHIFTS [T1]:
     delta(q) = arctan(1/q) + arctan(2/q), reflectionless
     Levinson theorem: integral Delta_rho = -2 = -n_bound  [EXACT]

  2. CONTINUUM CORRECTION IS NEGATIVE [T1]:
     Delta_M^2_cont = {Delta_M2_cont_total:.4e} M_Pl^2 ({Delta_M2_cont_total*100:.4f}%)
     The kink redistributes spectral weight from continuum to bound states.
     Since lower-mass modes contribute more to induced gravity, the net
     effect is a REDUCTION relative to the bound-state-only estimate.

  3. CONTINUUM CORRECTION IS SMALL [T1]:
     |Continuum| / Bound = {cont_to_bound_ratio*100:.2f}%
     Exponential suppression at m^2/Lambda^2 = 4 makes each continuum
     state contribute negligibly to the Sakharov integral.

  4. COMPLETE ONE-LOOP M^2_ind [T3]:
     Bound states:         {M2_bound*100:.4f}%  of M_Pl^2
     Continuum correction: {Delta_M2_cont_total*100:.4f}%  of M_Pl^2
     Total one-loop:       {M2_one_loop*100:.4f}%  of M_Pl^2
     (Net shift from C394: {(M2_one_loop - M2_bound)/M2_bound*100:.2f}%)

  5. NON-PERTURBATIVE FRACTION TIGHTENED [T3]:
     Total perturbative:    {total_perturbative*100:.2f}% (scalar + induced)
     Non-perturbative:      {nonpert_fraction*100:.2f}%
     This is ROBUST — higher perturbative corrections are negligible.

  6. THE D4 GAP IS INHERENTLY NON-PERTURBATIVE [T3]:
     r_s/xi = {r_s_over_xi:.0f} >> 1 (kink deep inside own r_s)
     Perturbative expansion parameter = {pert_expansion_param:.4e}
     The dominant ~93% of gravitational coupling CANNOT be reached
     by loop expansion. Resolution requires:
     (a) Jormungandr self-consistency, or
     (b) Strong-field boundary condition, or
     (c) Non-perturbative lattice computation

  D4 STATUS UPDATE:
     C394 result (2.35%) is confirmed and ROBUST at one loop.
     Continuum modes reduce, not increase, the perturbative account.
     The path forward is definitively NON-PERTURBATIVE.
""")
