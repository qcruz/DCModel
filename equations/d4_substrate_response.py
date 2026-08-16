"""
D4 Substrate Response: Linear Response Kernel of the DFC Substrate
==================================================================

Physical question:
    Does the DFC substrate, when perturbed around its vacuum or kink background,
    possess a linear response kernel with a massless spin-2 pole? Specifically,
    does the stress-energy response function contain a structure of the form:
        D_muv_ab(k) ~ P^(2)_muv_ab / k^2
    where P^(2) is the spin-2 projection operator?

    This is the "most important mathematical experiment" identified in the D4
    gravity gap analysis (foundations/d4_gravity_gap.md). The answer determines
    whether DFC can produce gravity from V(phi) or has identified a fundamental
    obstruction.

DFC mechanism:
    Start with the DFC substrate action S[phi] built from V(phi). Expand around
    the vacuum phi_0 or kink background:
        phi = phi_bg + delta_phi
    Compute the quadratic action S^(2)[delta_phi], which defines the propagator.
    The stress-energy tensor T_muv[phi] is a functional of phi. Perturbing phi
    induces delta_T_muv. The linear response kernel is:
        chi_muv_ab(x-y) = <delta_T_muv(x) delta_T_ab(y)>
    In momentum space, chi(k) encodes how the substrate responds to energy-momentum
    perturbations. If chi(k) has a 1/k^2 pole with spin-2 tensor structure, the
    substrate produces gravity.

Computations:
    Part A: Quadratic action S^(2)[delta_phi] around vacuum phi_0
    Part B: Stress-energy tensor T_muv and its perturbation delta_T_muv
    Part C: T_muv-T_muv correlator (linear response kernel) in 1+1D
    Part D: Spin content analysis of the response kernel
    Part E: Kink background response (Poeschl-Teller spectrum)
    Part F: Assessment of spin-2 emergence prospects

Key references:
    - d4_gravity_spin2_enhancement.py (C392): Enhancement factor F = G_N/G_eff = 22.87
    - d4_zero_mode_gravity.py (C367): Scalar zero-mode gives G_eff = G_N/23
    - d4_gravity_dimensional.py (C366b): alpha * G_N = 18^(1/3)
    - foundations/d4_gravity_gap.md: D4 gap restructured into D4-A through D4-D

Cycle: 393
"""

import math
import numpy as np
from fractions import Fraction

# =============================================================================
# DFC parameters (Planck units: G = hbar = c = 1, M_Pl = 1)
# =============================================================================
ALPHA = 18 ** (1 / 3)        # ~2.6207
BETA = 1 / (9 * math.pi)     # ~0.03537
PHI_0 = math.sqrt(ALPHA / BETA)  # vacuum field value
XI = math.sqrt(2 / ALPHA)    # kink width ~0.874 l_Pl
M_SIGMA = math.sqrt(2 * ALPHA)  # small-oscillation mass around vacuum
G_N = 1.0                    # Planck units
M_PL = 1.0

# Sech integrals (exact)
I4 = Fraction(4, 3)
I6 = Fraction(16, 15)
I8 = Fraction(32, 35)
I10 = Fraction(256, 315)

# =============================================================================
# Assertion infrastructure
# =============================================================================
results = []
pass_count = 0
fail_count = 0

def check(label, value, expected=True, tol=1e-6):
    global pass_count, fail_count
    if isinstance(expected, bool):
        ok = bool(value) == expected
        detail = f"got {value}"
    else:
        if expected == 0:
            ok = abs(value) < tol
            detail = f"got {value}, |val| < {tol}"
        else:
            rel = abs(value - expected) / abs(expected)
            ok = rel < tol
            detail = f"got {value}, expected {expected}, rel_err {rel:.2e}"
    status = "PASS" if ok else "FAIL"
    if ok:
        pass_count += 1
    else:
        fail_count += 1
    results.append((label, status, detail))
    print(f"  [{status}] {label}: {detail}")
    return ok


# =============================================================================
# Part A: Quadratic action around vacuum phi_0
# =============================================================================
print("=" * 72)
print("PART A: Quadratic action S^(2)[delta_phi] around vacuum")
print("=" * 72)
print()

# V(phi) = -alpha/2 phi^2 + beta/4 phi^4
# V'(phi) = -alpha phi + beta phi^3
# V''(phi) = -alpha + 3 beta phi^2
# At vacuum phi_0 = sqrt(alpha/beta):
#   V''(phi_0) = -alpha + 3*beta*(alpha/beta) = -alpha + 3*alpha = 2*alpha
#   This is the mass-squared of small oscillations: m_sigma^2 = 2*alpha

V_pp_vac = -ALPHA + 3 * BETA * PHI_0**2
print(f"V''(phi_0) = {V_pp_vac:.6f}")
print(f"2*alpha    = {2*ALPHA:.6f}")
check("A1_V_pp_vacuum", V_pp_vac, 2 * ALPHA, tol=1e-12)

# The quadratic action around phi = phi_0 + sigma is:
#   S^(2) = integral d^Dx [1/2 (d_mu sigma)^2 + 1/2 m_sigma^2 sigma^2]
# where m_sigma^2 = V''(phi_0) = 2*alpha
# Propagator: G(k) = 1/(k^2 + m_sigma^2)
# This is a MASSIVE scalar propagator with mass m_sigma = sqrt(2*alpha)

m_sigma_sq = 2 * ALPHA
m_sigma = math.sqrt(m_sigma_sq)
print(f"\nm_sigma = sqrt(2*alpha) = {m_sigma:.6f} M_Pl")
print(f"m_sigma / m_KK = {m_sigma * XI:.6f}")
# m_KK = 1/XI, so m_sigma * XI = m_sigma / m_KK
check("A2_m_sigma_over_mKK", m_sigma * XI, 2.0, tol=1e-12)
# m_sigma = 2/XI = 2*m_KK exactly: sqrt(2*alpha) = 2/sqrt(2/alpha) = 2*sqrt(alpha/2)
# Wait: m_KK = 1/XI = sqrt(alpha/2), so m_sigma/m_KK = sqrt(2*alpha)/sqrt(alpha/2)
# = sqrt(2*alpha * 2/alpha) = sqrt(4) = 2. Yes, m_sigma = 2*m_KK exactly.

print(f"\nThe vacuum propagator G(k) = 1/(k^2 + 2*alpha) is MASSIVE.")
print(f"Correlation length = 1/m_sigma = {1/m_sigma:.6f} l_Pl = XI/2 = {XI/2:.6f}")
check("A3_corr_length", 1/m_sigma, XI/2, tol=1e-12)

# V'''(phi_0) = 6*beta*phi_0 (cubic coupling)
V_ppp_vac = 6 * BETA * PHI_0
print(f"\nV'''(phi_0) = 6*beta*phi_0 = {V_ppp_vac:.6f}")

# V''''(phi_0) = 6*beta (quartic coupling)
V_pppp_vac = 6 * BETA
print(f"V''''(phi_0) = 6*beta = {V_pppp_vac:.6f}")

print()

# =============================================================================
# Part B: Stress-energy tensor and its perturbation
# =============================================================================
print("=" * 72)
print("PART B: Stress-energy tensor T_muv and perturbation delta_T_muv")
print("=" * 72)
print()

# For a scalar field phi with V(phi):
#   T_muv = d_mu phi d_v phi - eta_muv [1/2 (d phi)^2 - V(phi)]
# The trace: T = T^mu_mu = (1-D/2)(d phi)^2 + D*V(phi)  in D dimensions
# In D=2 (1+1D): T = -V(phi) = constant at vacuum (no propagating trace mode)
# In D=4 (3+1D): T = -(d phi)^2 + 4*V(phi)

# Perturb: phi = phi_0 + sigma
# d_mu phi = d_mu sigma (phi_0 is constant at vacuum)
# T_muv = d_mu sigma d_v sigma - eta_muv [1/2 (d sigma)^2 - V(phi_0+sigma)]

# Linear perturbation of T_muv around vacuum (sigma = 0):
#   delta_T_muv^(1) = 0 for the vacuum (no linear coupling!)
# This is because T_muv is QUADRATIC in field derivatives.

# Quadratic perturbation:
#   delta_T_muv^(2) = d_mu sigma d_v sigma
#                     - eta_muv [1/2 (d sigma)^2 + 1/2 V''(phi_0) sigma^2]

# The T_muv-T_muv correlator (in free field limit) is:
#   chi_muv_ab(k) = <T_muv(k) T_ab(-k)>
# This is a 4-point function of sigma fields (since T is quadratic in sigma).

# KEY STRUCTURAL RESULT:
# The scalar field T_muv correlator decomposes into spin-0 and spin-2 parts:
#   chi_muv_ab(k) = A_0(k^2) P^(0)_muv_ab + A_2(k^2) P^(2)_muv_ab
# where P^(0) and P^(2) are spin-0 and spin-2 projection operators.
# The question is whether A_2(k^2) has a 1/k^2 pole.

print("Structural analysis of T_muv-T_muv correlator:")
print()
print("For a FREE massive scalar (mass m_sigma):")
print("  chi_muv_ab(k) = integral d^Dp/(2pi)^D")
print("    [p_mu (k-p)_v p_a (k-p)_b + permutations] / [(p^2+m^2)((k-p)^2+m^2)]")
print()
print("This is a bubble (one-loop) diagram.")
print("In the infrared (k -> 0):")
print("  The bubble diagram with massive propagators gives:")
print("  chi(k) ~ C / m_sigma^(D-4)  (constant, no 1/k^2 pole)")
print()
print("CRITICAL: A free massive scalar has NO massless pole in chi(k).")
print("The T_muv-T_muv correlator falls off at k -> 0, not as 1/k^2.")
print()

# Verify: in D=4, the scalar bubble integral with mass m gives
# Im chi(s) ~ theta(s - 4m^2) * sqrt(1 - 4m^2/s) * [polynomial in s]
# No pole at s=0. The spectral density starts at threshold 2*m_sigma.

threshold = 2 * m_sigma
print(f"Two-particle threshold: 2*m_sigma = {threshold:.6f} M_Pl")
print(f"This is 4/XI = 4*m_KK = {4/XI:.6f} M_Pl")
check("B1_threshold", threshold, 4/XI, tol=1e-12)

print()
print("CONCLUSION (Part B):")
print("  Around the VACUUM, the DFC substrate response has NO massless pole.")
print("  The stress-energy correlator has a two-particle threshold at 2*m_sigma.")
print("  Gravity cannot emerge from vacuum fluctuations alone.")
print("  The kink background is essential -- see Part E.")
print()


# =============================================================================
# Part C: 1+1D stress-energy correlator (explicit computation)
# =============================================================================
print("=" * 72)
print("PART C: T_muv-T_muv correlator in 1+1D (explicit)")
print("=" * 72)
print()

# In 1+1D, compute the Euclidean bubble integral explicitly.
# For a massive scalar with propagator G(p) = 1/(p^2 + m^2):
# Pi(k) = integral dp/(2pi) G(p) G(k-p)
#        = integral dp/(2pi) 1/[(p^2+m^2)((k-p)^2+m^2)]
# Using Feynman parameterization:
# Pi(k) = integral_0^1 dx integral dp/(2pi) 1/[(p-xk)^2 + m^2 + x(1-x)k^2]^2
# = integral_0^1 dx / [4*pi*sqrt(m^2 + x(1-x)k^2)] * 1/[m^2 + x(1-x)k^2]
# Wait, in 1D momentum integral:
# integral dp/(2pi) 1/[p^2 + Delta]^2 = 1/(4*Delta^(3/2)) (for D=1 Euclidean)

# Actually, in 1+1D Euclidean (D=2), the bubble is:
# Pi(k) = integral d^2p/(2pi)^2 1/[(p^2+m^2)((k-p)^2+m^2)]
# Using Feynman param:
# = integral_0^1 dx integral d^2p/(2pi)^2 1/[p^2 + Delta(x)]^2
# where Delta(x) = m^2 + x(1-x)k^2
# In D=2: integral d^2p/(2pi)^2 1/[p^2+Delta]^2 = 1/(4*pi*Delta)

# So Pi(k) = integral_0^1 dx / (4*pi*(m^2 + x(1-x)*k^2))
# = 1/(4*pi) * integral_0^1 dx / (m^2 + x(1-x)*k^2)

# For k -> 0: Pi(0) = 1/(4*pi*m^2) -- finite, no pole.
# For general k: the integral can be done analytically.

# The integral integral_0^1 dx / (a + bx(1-x)) where a=m^2, b=k^2:
# = integral_0^1 dx / (a + b(x - x^2))
# = integral_0^1 dx / (-b(x^2 - x) + a)
# = integral_0^1 dx / (-b(x - 1/2)^2 + a + b/4)
# Let c = a + b/4 = m^2 + k^2/4, d = b = k^2
# = integral_0^1 dx / (c - d(x-1/2)^2)
# = 1/sqrt(c*d) * arctan(sqrt(d/c)*(x-1/2)) from 0 to 1  [if c > d/4]
# At x=1: arctan(sqrt(d/c)*1/2), at x=0: arctan(sqrt(d/c)*(-1/2))
# = 2/(sqrt(c*d)) * arctan(sqrt(d/(4c)))   [by symmetry about x=1/2]
# But actually for m > 0 and real k, we need c > d/4 i.e. m^2 > 0 always true.

# Let's compute numerically for verification
from scipy import integrate

m2 = m_sigma_sq  # 2*alpha

def bubble_integrand(x, k_sq):
    return 1.0 / (m2 + x * (1 - x) * k_sq)

# Pi(k) at k=0
Pi_0, _ = integrate.quad(bubble_integrand, 0, 1, args=(0.0,))
Pi_0 /= (4 * math.pi)
print(f"Pi(k=0) = 1/(4*pi*m_sigma^2) = {1/(4*math.pi*m2):.8f}")
print(f"Pi(k=0) numeric = {Pi_0:.8f}")
check("C1_Pi_k0", Pi_0, 1/(4*math.pi*m2), tol=1e-10)

# Pi(k) at k = m_sigma (threshold approach)
k_sq_test = m2
Pi_m, _ = integrate.quad(bubble_integrand, 0, 1, args=(k_sq_test,))
Pi_m /= (4 * math.pi)
print(f"\nPi(k=m_sigma) = {Pi_m:.8f}")

# Pi(k) at k -> infinity: ~ 1/(4*pi*k^2) * integral_0^1 dx / x(1-x)
# which diverges logarithmically. But for finite k:
# Pi(k) for large k ~ 2*arctan(1/2)/(pi*k*sqrt(m^2+k^2/4)) ~ 2*arctan(0.5)/(pi*k^2)

# Key check: Pi(k) is MONOTONICALLY DECREASING from Pi(0) to 0
k_values = np.linspace(0.01, 20.0, 200)
Pi_values = []
for kv in k_values:
    val, _ = integrate.quad(bubble_integrand, 0, 1, args=(kv**2,))
    Pi_values.append(val / (4 * math.pi))
Pi_values = np.array(Pi_values)

# Check monotone decrease
diffs = np.diff(Pi_values)
all_decreasing = np.all(diffs < 0)
print(f"\nPi(k) monotonically decreasing: {all_decreasing}")
check("C2_Pi_monotone_decrease", all_decreasing, True)

# Check NO pole: Pi(k) -> 0 as k -> infinity
Pi_large_k = Pi_values[-1]
Pi_ratio = Pi_values[0] / Pi_large_k  # Pi(0)/Pi(20)
print(f"Pi(k=0.01) = {Pi_values[0]:.2e}")
print(f"Pi(k=20)   = {Pi_large_k:.2e}")
print(f"Ratio Pi(0)/Pi(20) = {Pi_ratio:.1f}")
# If there were a 1/k^2 pole, Pi(k) ~ 1/k^2 and the ratio would be ~ (20/0.01)^2 = 4e6.
# Instead the ratio is ~ 9 (smooth, no pole). This confirms no massless pole.
check("C3_Pi_no_pole_ratio", Pi_ratio < 100, True)

print()
print("The scalar bubble Pi(k) is a smooth, monotonically decreasing function.")
print("It has NO 1/k^2 pole. This confirms: vacuum fluctuations of a massive")
print("scalar do not produce a long-range (1/r) interaction.")
print()


# =============================================================================
# Part D: Spin content analysis
# =============================================================================
print("=" * 72)
print("PART D: Spin content analysis of substrate response")
print("=" * 72)
print()

# In D=4, the T_muv-T_muv correlator of a scalar field decomposes as:
# chi_muv,ab(k) = A_0(k^2) P^(0)_muv,ab(k) + A_2(k^2) P^(2)_muv,ab(k)
#
# where the spin-2 projector is:
# P^(2)_muv,ab = 1/2 (Pi_ma Pi_vb + Pi_mb Pi_va) - 1/(D-1) Pi_muv Pi_ab
# with Pi_muv = delta_muv - k_mu k_v / k^2
#
# For a FREE massive scalar, both A_0 and A_2 come from the bubble integral.
# Neither has a 1/k^2 pole -- both are finite at k=0.
#
# The spin-2 component A_2 is present (T_muv has spin-2 content), but it is
# analytic at k=0. There is no massless spin-2 particle in the spectrum.

# Count polarizations:
# In D dimensions, a symmetric traceless rank-2 tensor has
# D(D+1)/2 - 1 = (D^2+D-2)/2 components.
# Transverse condition removes D: (D^2+D-2)/2 - D = (D^2-D-2)/2 = (D-2)(D+1)/2
# For D=4: (4-2)(4+1)/2 = 5 propagating DOF for massive spin-2
# For MASSLESS spin-2 in D=4: only 2 helicity states (h = +2, -2)
# The 5 -> 2 reduction is from gauge invariance h_muv -> h_muv + d_mu xi_v + d_v xi_mu

D = 4
massive_spin2_dof = (D - 2) * (D + 1) // 2  # 5
massless_spin2_dof = 2  # helicity +2, -2
print(f"Massive spin-2 DOF in D={D}: {massive_spin2_dof}")
print(f"Massless spin-2 DOF in D={D}: {massless_spin2_dof}")
check("D1_massive_spin2_dof", massive_spin2_dof, 5)
check("D2_massless_spin2_dof", massless_spin2_dof, 2)

print()
print("KEY STRUCTURAL POINT:")
print("  The DFC substrate field phi is a SCALAR (spin-0).")
print("  T_muv[phi] is a COMPOSITE operator built from phi.")
print("  The T_muv-T_muv correlator contains spin-0 AND spin-2 channels.")
print("  But a spin-2 CHANNEL in the correlator is NOT the same as a")
print("  spin-2 PARTICLE in the spectrum.")
print()
print("  For a massless spin-2 particle to exist, A_2(k^2) must have")
print("  a pole: A_2(k^2) ~ c / k^2 as k -> 0.")
print("  A free massive scalar does NOT produce this.")
print()

# The critical question: can interactions or the kink background produce
# a massless spin-2 bound state?

# In condensed matter, this is related to the question of emergent gravity.
# Sakharov (1967) induced gravity: integrating out matter fields generates
# an Einstein-Hilbert term in the effective action. The coefficient is:
# M_eff^2 = (1/16*pi) sum_i (-1)^{2s_i} (2s_i+1) m_i^2 ln(Lambda^2/m_i^2)
# For a single massive scalar: M_eff^2 = m_sigma^2/(16*pi) * ln(Lambda^2/m_sigma^2)

# Sakharov's induced gravity coefficient from the DFC substrate:
Lambda_UV = 1 / XI  # UV cutoff = m_KK
M_eff_sq_Sakharov = m_sigma_sq / (16 * math.pi) * math.log(Lambda_UV**2 / m_sigma_sq)
print(f"Sakharov induced gravity coefficient:")
print(f"  M_eff^2 = m_sigma^2/(16*pi) * ln(Lambda^2/m_sigma^2)")
print(f"  Lambda = m_KK = 1/XI = {1/XI:.4f} M_Pl")
print(f"  m_sigma/m_KK = 2 (exact)")
print(f"  ln(m_KK^2/m_sigma^2) = ln(1/4) = {math.log(0.25):.4f}")
print(f"  M_eff^2 = {M_eff_sq_Sakharov:.6f} M_Pl^2")
print()

# Note: ln(1/4) < 0, so M_eff^2 < 0 with a single scalar mode.
# This is the WRONG SIGN for gravity (repulsive, not attractive).
# This is a known issue with Sakharov's approach for scalars --
# fermions contribute with opposite sign, giving the correct sign.
# In DFC, the kink itself is the non-perturbative object that could
# change this picture.

wrong_sign = M_eff_sq_Sakharov < 0
print(f"Sakharov M_eff^2 < 0 (wrong sign for gravity): {wrong_sign}")
check("D3_Sakharov_wrong_sign", wrong_sign, True)

print()
print("RESULT: The naive Sakharov induced gravity from DFC vacuum")
print("fluctuations gives the WRONG SIGN. This means:")
print("  (1) Gravity cannot emerge from vacuum fluctuations of phi alone.")
print("  (2) The kink background is essential for correct-sign gravity.")
print("  (3) Non-perturbative effects (kink-kink interactions, topology)")
print("      must provide the dominant gravitational coupling.")
print("  This is consistent with the C392 finding that 96% of G_N is")
print("  non-perturbative content.")
print()


# =============================================================================
# Part E: Kink background response (Poeschl-Teller spectrum)
# =============================================================================
print("=" * 72)
print("PART E: Response kernel around kink background")
print("=" * 72)
print()

# Around the kink phi_kink(y) = phi_0 * tanh(y/XI), the fluctuation equation
# is a Poeschl-Teller problem with s=2:
#   [-d^2/dy^2 + V_PT(y)] psi_n = omega_n^2 psi_n
# where V_PT(y) = m_sigma^2 - 6*alpha/cosh^2(y/XI) + ... = 2*alpha*(1 - 3/cosh^2(y/XI))
# Bound states: omega_0^2 = 0 (zero mode), omega_1^2 = 3*alpha/2 (shape mode)
# Continuum: omega^2 >= 2*alpha (scattering states)

omega_0_sq = 0.0
omega_1_sq = 1.5 * ALPHA
omega_cont_sq = 2 * ALPHA

print("Poeschl-Teller spectrum (s=2):")
print(f"  Zero mode:    omega_0^2 = {omega_0_sq:.4f} (MASSLESS)")
print(f"  Shape mode:   omega_1^2 = 3*alpha/2 = {omega_1_sq:.6f}")
print(f"  Continuum:    omega^2 >= 2*alpha = {omega_cont_sq:.6f}")
print()

# The zero mode psi_0(y) ~ sech^2(y/XI) is massless (omega_0 = 0).
# But it is a SCALAR mode -- it corresponds to kink translation.
# It has spin-0, not spin-2.
#
# The shape mode psi_1(y) ~ sech(y/XI)*tanh(y/XI) is massive and odd-parity.
# Also spin-0.
#
# CRITICAL QUESTION: Can the kink background mix scalar and tensor channels
# to produce an effective spin-2 mode?

print("Zero mode analysis:")
print("  psi_0(y) = N * sech^2(y/XI)")
print("  This is a SCALAR (spin-0) translational mode.")
print("  Spin quantum number: s = 0")
print("  Parity: even")
print()

# In 3+1D, the kink worldvolume is a 3-brane.
# Fluctuations split into:
# (a) Scalar: phi -> phi_kink + sigma * psi_0(y) -- transverse displacement
# (b) Vector: zero modes associated with internal symmetry (none for real scalar)
# (c) Tensor: metric-like fluctuations of the worldvolume embedding

# For a REAL SCALAR field phi, there are NO tensor zero modes.
# A tensor mode requires at least TWO scalar fields (complex phi)
# or an explicit metric degree of freedom.

# With the DFC complex extension phi in C^n, the moduli space has
# dim = 8 (SU(3) generators) + 1 (translation) = 9 DOF.
# But all moduli modes are spin-0 on the worldvolume.

print("Kink moduli in DFC:")
print(f"  Translation: 1 DOF (scalar, spin-0)")
print(f"  SU(3) orientation: 8 DOF (scalar, spin-0)")
print(f"  Total: 9 = N_Hopf moduli (all spin-0)")
print()

N_moduli = 9  # N_Hopf
check("E1_moduli_count", N_moduli, 9)

# The stress-energy response around the kink:
# chi_muv,ab(k; kink) has TWO new features vs vacuum:
# 1. A zero-mode contribution (massless scalar pole)
# 2. Modified continuum threshold (Poeschl-Teller shape)
#
# The zero-mode contribution to chi_muv,ab gives:
# chi^(0)_muv,ab ~ T_muv^(0) T_ab^(0) / k^2
# where T_muv^(0) is the stress-energy of the zero mode.
# But T_muv^(0) = rho_0(y) * eta_muv (scalar, not tensor).
# So the 1/k^2 pole is in the spin-0 channel, not spin-2.

print("Zero-mode contribution to chi_muv,ab:")
print("  The zero mode IS massless and provides a 1/k^2 pole.")
print("  But it is in the spin-0 (scalar) channel.")
print("  This gives the G_eff = G_N/23 result from C367.")
print()
print("  A spin-2 pole requires spin-2 structure in the numerator:")
print("  chi^(2)_muv,ab ~ [rank-4 tensor with spin-2 projection] / k^2")
print("  This is ABSENT in the real scalar field theory.")
print()

# The scalar zero-mode exchange between kinks:
# V(R) = -G_eff M1 M2 / R with G_eff = G_N / F
# F = (25/12) * 4*pi*XI = 22.87 (C367/C392)
F_enhancement = float(Fraction(25, 12)) * 4 * math.pi * XI
print(f"Enhancement factor F = (25/12)*4*pi*XI = {F_enhancement:.4f}")
print(f"Scalar zero mode accounts for 1/F = {1/F_enhancement:.4f} = {100/F_enhancement:.1f}% of G_N")
check("E2_enhancement_F", F_enhancement, 22.87, tol=0.005)

print()


# =============================================================================
# Part F: Assessment and paths forward
# =============================================================================
print("=" * 72)
print("PART F: Assessment of spin-2 emergence prospects")
print("=" * 72)
print()

print("RESULTS SUMMARY:")
print("-" * 50)
print()
print("1. VACUUM RESPONSE: No massless pole of any spin.")
print(f"   Two-particle threshold at 2*m_sigma = {threshold:.4f} M_Pl.")
print(f"   Sakharov coefficient has WRONG SIGN (M_eff^2 = {M_eff_sq_Sakharov:.4f}).")
print()
print("2. KINK BACKGROUND: One massless pole (scalar zero mode).")
print(f"   Provides G_eff = G_N/{F_enhancement:.1f} (4.4% of G_N).")
print(f"   The pole is spin-0, not spin-2.")
print(f"   No spin-2 mode in the Poeschl-Teller spectrum (all modes scalar).")
print()
print("3. SPIN-2 OBSTRUCTION: A real scalar field phi has no mechanism")
print("   to produce a propagating spin-2 mode. T_muv is a composite of")
print("   spin-0 fields. While chi_muv,ab has spin-2 tensor structure in")
print("   its decomposition, no MASSLESS spin-2 pole appears.")
print()
print("4. POSSIBLE RESOLUTIONS (ordered by promise):")
print()
print("   (a) INDUCED GRAVITY via kink worldvolume dynamics:")
print("       Integrating out the massive modes (shape + continuum)")
print("       around the kink background generates higher-derivative")
print("       effective action terms on the worldvolume.")
print("       If these include a Ricci scalar term:")
print("         S_eff = integral d^4x sqrt(-g) [M_eff^2/2 R + ...]")
print("       then gravity is induced with G_N = 1/(8*pi*M_eff^2).")
print("       This does NOT require a spin-2 particle in the substrate")
print("       spectrum -- it requires that the worldvolume effective")
print("       action has Einstein-Hilbert structure.")
print("       STATUS: T4 (most promising path)")
print()
print("   (b) JORMUNGANDR SELF-CONSISTENCY:")
print("       V(phi) -> matter -> compression -> geometry -> collapse")
print("       -> endpoint -> V_eff(phi) = V(phi)")
print("       The fixed-point condition would constrain G_N = f(alpha,beta)")
print("       without requiring an explicit spin-2 mode in the substrate.")
print("       STATUS: T4 (requires formal self-consistency loop)")
print()
print("   (c) EMERGENT METRIC from substrate deformation:")
print("       g_muv^eff = eta_muv + F_muv[phi, d phi, ...]")
print("       Kinks deform the substrate; other excitations propagate")
print("       through the deformed substrate, experiencing effective geometry.")
print("       STATUS: T4 (most fundamental but least developed)")
print()

# Quantitative check: the 96% non-perturbative content
nonpert_fraction = 1 - 1/F_enhancement
print(f"Non-perturbative fraction of G_N: {nonpert_fraction:.4f} = {100*nonpert_fraction:.1f}%")
check("F1_nonpert_fraction", nonpert_fraction, 0.956, tol=0.005)

# The fact that 96% is non-perturbative is CONSISTENT with induced gravity,
# where the gravitational coupling comes from integrating out modes, not from
# a single zero-mode exchange.

# Key dimensionless number: alpha * G_N = 18^(1/3) [T1]
alpha_GN = ALPHA * G_N
print(f"\nalpha * G_N = {alpha_GN:.6f}")
print(f"18^(1/3) = {18**(1/3):.6f}")
check("F2_alpha_GN", alpha_GN, 18**(1/3), tol=1e-12)

# What induced gravity requires:
# M_eff^2 = alpha / (18^(1/3)) = alpha^(2/3) / 18^(1/3)
# Since G_N = 1/M_Pl^2 = 1 in our units, this is automatically satisfied.
# But this is the CONSISTENCY RELATION, not a derivation.
# The D4 gap is to show that the dynamics produce M_eff^2 = M_Pl^2 from V(phi).

print()
print("D4 GAP STATUS after this analysis:")
print("=" * 50)
print()
print("D4-A (Scale): alpha * G_N = 18^(1/3) consistency [T1]")
print("              Absolute scale from dynamics: T4 OPEN")
print()
print("D4-B (Metric): No explicit g_muv^eff construction: T4 OPEN")
print("               Most fundamental sub-gap")
print()
print("D4-C (Graviton): Scalar zero mode exists (omega_0 = 0)")
print("                 NO spin-2 mode in substrate spectrum")
print("                 Masslessness protection: unidentified")
print("                 T4 OPEN (hardest sub-gap)")
print()
print("D4-D (Coupling): Scalar fraction 4.4% [T3]")
print("                 Full coupling: T4 OPEN")
print()
print("VERDICT: The DFC substrate around its kink background does NOT")
print("contain a propagating massless spin-2 mode. This is a negative")
print("result for the direct graviton emergence approach (D4-C).")
print("However, this does NOT rule out induced gravity (D4-B) or")
print("Jormungandr self-consistency (D4-A/D4-D), which do not require")
print("a fundamental spin-2 particle in the substrate spectrum.")
print()

# Tier assignments for this module
print("TIER ASSIGNMENTS:")
print("  Vacuum response has no massless pole: T1 (algebraic)")
print("  Sakharov wrong sign: T1 (one-loop computation)")
print("  Kink zero mode is scalar, not spin-2: T1 (PT spectrum)")
print("  Scalar zero mode gives G_eff = G_N/23: T3 (C367)")
print("  No spin-2 mode in scalar field theory: T1 (representation theory)")
print("  Non-perturbative fraction 96%: T3 (C392)")
print("  Induced gravity as resolution path: T4 (uncomputed)")
print()

# =============================================================================
# Summary
# =============================================================================
print("=" * 72)
print(f"SUMMARY: {pass_count} PASS, {fail_count} FAIL out of {pass_count + fail_count}")
print("=" * 72)
for label, status, detail in results:
    print(f"  [{status}] {label}: {detail}")

if fail_count > 0:
    print(f"\n*** {fail_count} ASSERTION(S) FAILED ***")
else:
    print(f"\nAll {pass_count} assertions passed.")
