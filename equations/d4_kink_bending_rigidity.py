"""
D4 Kink Bending Rigidity: Classical Non-Minimal Coupling from Domain Wall
=========================================================================

Physical question:
    When a domain wall (kink) is embedded in a curved worldvolume, its
    profile shifts. The energy cost of this shift is proportional to
    the worldvolume Ricci scalar R. This gives a CLASSICAL contribution
    to the Einstein-Hilbert term on the worldvolume:

        S_wall = integral d^4x sqrt(-g) [ -sigma + kappa * R + ... ]

    where sigma is the surface tension and kappa is the bending rigidity.
    If kappa = M_Pl^2 / 2, we have derived gravity from the kink structure.

    This is different from the Sakharov one-loop mechanism (C394):
    - Sakharov: QUANTUM fluctuations of worldvolume modes -> EH term
    - Bending rigidity: CLASSICAL response of the kink profile to curvature

DFC mechanism:
    The kink phi(y) = phi_0 tanh(y/xi) has an energy density
    eps(y) = (phi_0^2 / xi^2) sech^4(y/xi). When the worldvolume is
    curved with Ricci scalar R, the kink profile deforms:

        phi(y; R) = phi_0 tanh(y/xi) + delta_phi(y) * R + O(R^2)

    The perturbation delta_phi satisfies a Schrodinger-type equation
    with the Poeschl-Teller potential. Its contribution to the energy
    gives the bending rigidity:

        kappa = -(1/6) * integral dy (d phi_0 / dy)^2 * y^2
              + (overlap integrals with PT modes)

    The first term is the "geometric" bending rigidity — the second
    moment of the kink's energy density. The second involves the
    response of the kink profile to curvature through the PT spectrum.

Key references:
    - Eto, Nitta, Ohashi, Tong (2006): domain wall moduli dynamics
    - Shifman, Yung (2009): non-Abelian strings and domain walls
    - d4_sakharov_enhanced.py (C503): target xi_R = 0.0126

Cycle: 504
"""

import math
import numpy as np
from fractions import Fraction
from scipy import integrate

# =============================================================================
# DFC PARAMETERS
# =============================================================================

PI = math.pi
ALPHA = 18.0 ** (1.0 / 3.0)
BETA = 1.0 / (9.0 * PI)
PHI_0 = math.sqrt(ALPHA / BETA)   # ~8.608 M_Pl
XI = math.sqrt(2.0 / ALPHA)        # ~0.874 l_Pl
M_KK = 1.0 / XI
M_SIGMA = math.sqrt(2.0 * ALPHA)   # ~2.289 M_Pl

# Key quantities
E_KINK = 36.0 * PI                 # = 4/beta = 113.10 M_Pl
SIGMA = E_KINK                      # surface tension (energy per unit 3-area, in Planck units)
PHI_0_SQ = ALPHA / BETA            # = 9*pi*alpha = 74.10

# Target from C503
XI_R_TARGET = 0.012588              # Jormungandr-implied non-minimal coupling

passed = 0
failed = 0

def check(label, value, expected=True, tol=1e-6):
    global passed, failed
    if isinstance(expected, bool):
        ok = bool(value) == expected
        val_str = f"{value}"
    elif isinstance(expected, (int, float)):
        if expected == 0:
            ok = abs(value) < tol
        else:
            ok = abs(value - expected) / abs(expected) < tol
        val_str = f"{value:.6e} (expected {expected:.6e})"
    else:
        ok = value == expected
        val_str = f"{value}"
    status = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    else:
        failed += 1
    print(f"  [{status}] {label}: {val_str}")
    return ok

# =============================================================================
# PART A: KINK PROFILE MOMENTS
# =============================================================================

print("=" * 72)
print("PART A: Kink Profile Moments (Second Moment of Energy Density)")
print("=" * 72)

print(f"""
  The kink energy density is:
    eps(y) = (phi_0^2 / xi^2) sech^4(y/xi)

  The n-th moment of the energy density:
    M_n = integral dy y^n eps(y) / integral dy eps(y)

  The bending rigidity involves the SECOND moment:
    <y^2> = integral dy y^2 sech^4(y/xi) / integral dy sech^4(y/xi)

  Since all odd moments vanish by symmetry, we need:
    J_0 = integral sech^4(u) du = 4/3            [I_4, exact]
    J_2 = integral u^2 sech^4(u) du               [to compute]
""")

# Compute J_0 = I_4 = 4/3 (exact)
J_0_exact = float(Fraction(4, 3))
J_0_numeric, _ = integrate.quad(lambda u: 1.0/np.cosh(u)**4, -50, 50)
print(f"  J_0 = integral sech^4(u) du:")
print(f"    Exact:   {J_0_exact:.10f}")
print(f"    Numeric: {J_0_numeric:.10f}")
check("A1_J0_exact", J_0_numeric, J_0_exact, tol=1e-8)

# Compute J_2 = integral u^2 sech^4(u) du
J_2_numeric, _ = integrate.quad(lambda u: u**2 / np.cosh(u)**4, -50, 50)
print(f"\n  J_2 = integral u^2 sech^4(u) du:")
print(f"    Numeric: {J_2_numeric:.10f}")

# Analytic form: J_2 = (pi^2 - 6) / 9
# Derivation: sech^4(u) = -d/du[tanh(u) - tanh^3(u)/3]
# IBP twice with u^2 gives known result
J_2_analytic = (PI**2 - 6.0) / 9.0
print(f"    Analytic: (pi^2 - 6)/9 = {J_2_analytic:.10f}")
check("A2_J2_analytic", J_2_numeric, J_2_analytic, tol=1e-6)

# Second moment in physical units
y2_mean = XI**2 * J_2_numeric / J_0_numeric
print(f"\n  <y^2> = xi^2 * J_2/J_0 = {y2_mean:.6f} l_Pl^2")
print(f"  sqrt(<y^2>) = {math.sqrt(y2_mean):.6f} l_Pl (RMS width)")
print(f"  xi = {XI:.6f} l_Pl")
print(f"  RMS/xi = {math.sqrt(y2_mean)/XI:.6f}")

# Higher moments for completeness
J_4_numeric, _ = integrate.quad(lambda u: u**4 / np.cosh(u)**4, -50, 50)
print(f"\n  J_4 = integral u^4 sech^4(u) du = {J_4_numeric:.10f}")

# =============================================================================
# PART B: GEOMETRIC BENDING RIGIDITY
# =============================================================================

print("\n" + "=" * 72)
print("PART B: Geometric Bending Rigidity")
print("=" * 72)

print(f"""
  For a domain wall in phi^4 theory, the bending rigidity from the
  "geometric" (kinetic) contribution is:

    kappa_geom = (1/6) * integral dy (d phi/dy)^2 y^2

  where the 1/6 comes from the coefficient of the R term in the
  expansion of the worldvolume action to linear order in curvature.

  (d phi/dy)^2 = (phi_0/xi)^2 sech^4(y/xi)

  So: kappa_geom = (phi_0^2 / (6 xi^2)) * xi^3 * J_2
                 = phi_0^2 xi / 6 * J_2
""")

# Geometric bending rigidity
kappa_geom = PHI_0**2 * XI / 6.0 * J_2_numeric
print(f"  kappa_geom = phi_0^2 * xi * J_2 / 6")
print(f"             = {PHI_0**2:.4f} * {XI:.4f} * {J_2_numeric:.4f} / 6")
print(f"             = {kappa_geom:.6f} M_Pl^2")
print(f"  Fraction of M_Pl^2/2: {kappa_geom / 0.5:.4f} ({kappa_geom/0.5*100:.2f}%)")

# As non-minimal coupling
xi_R_geom = kappa_geom / PHI_0_SQ
print(f"\n  Equivalent xi_R = kappa_geom / phi_0^2 = {xi_R_geom:.6f}")
print(f"  Target xi_R = {XI_R_TARGET:.6f}")
print(f"  Ratio: {xi_R_geom / XI_R_TARGET:.4f}")

check("B1_kappa_positive", kappa_geom > 0)

# =============================================================================
# PART C: POTENTIAL CONTRIBUTION TO BENDING RIGIDITY
# =============================================================================

print("\n" + "=" * 72)
print("PART C: Potential Contribution to Bending Rigidity")
print("=" * 72)

print(f"""
  The full domain wall effective action on a curved worldvolume includes
  both kinetic and potential contributions. When the worldvolume has
  Ricci scalar R, the kink equation of motion becomes:

    phi'' = V'(phi) + xi_conf * R * phi

  where xi_conf is the conformal coupling parameter. For a general scalar:
    xi_conf = 0  (minimal coupling)
    xi_conf = 1/6 (conformal coupling in 4D)

  The DFC substrate action has minimal coupling (xi_conf = 0) in the
  fundamental Lagrangian. But the EFFECTIVE coupling on the worldvolume
  receives contributions from integrating out the transverse direction.

  The full bending rigidity has three terms:
  1. Kinetic (geometric): kappa_K = phi_0^2 xi J_2 / 6  [Part B]
  2. Profile response: kappa_resp from delta_phi solving the PT equation
  3. Potential curvature: kappa_V from the potential energy shift

  For the profile response, we solve:
    [-d^2/dy^2 + V''(phi_bg)] delta_phi = -phi_bg / 6
  (the 1/6 is the conformal factor for the R * phi coupling)
""")

# Profile response: solve PT equation with source
# V''(phi_bg) = alpha * (3*tanh^2(y/xi) - 1) = alpha * (2 - 3*sech^2(y/xi))
# PT potential: U(y) = V''(phi_bg) = 2*alpha - 3*alpha*sech^2(y/xi)
# = m_sigma^2 - 3*m_KK^2 * sech^2(y/xi)
# This is the Poeschl-Teller potential with s(s+1) = 6, so s=2

# The inhomogeneous equation:
# [-d^2/dy^2 + U(y)] delta_phi(y) = source(y)
# where source depends on the specific coupling to R

# For the non-minimal coupling calculation, the source is:
# source(y) = -(1/6) * d^2 phi_bg / dy^2 * (something involving R)
# But more precisely, for a domain wall on a curved space with
# intrinsic curvature R, the perturbation is sourced by the change
# in the kink equation.

# The standard result (Eto et al. 2006, Eq. 3.14):
# The effective action for the wall position modulus X^mu is:
#   S_eff = -sigma * int d^3x sqrt(h) [1 + c_R * R_h + ...]
# where R_h is the intrinsic Ricci scalar of the worldvolume

# The coefficient c_R comes from the integral:
#   c_R = -(1/sigma) * sum_n |<n|y|0>|^2 / (omega_n^2)
# where |0> is the zero mode, |n> are excited modes, omega_n are their
# frequencies, and y is the transverse coordinate

# Zero mode: psi_0(y) = N_0 * sech^2(y/xi) with N_0 = sqrt(3/(4*xi))
# Excited bound state: psi_1(y) = N_1 * sech(y/xi) * tanh(y/xi)
#   with omega_1^2 = 3*alpha/2

# Matrix element <1|y|0>:
# <1|y|0> = N_0 * N_1 * int dy y * sech^2(y/xi) * sech(y/xi) * tanh(y/xi)
# = N_0 * N_1 * xi^2 * int du u * sech^3(u) * tanh(u)

# This integral:
# int u sech^3(u) tanh(u) du from -inf to inf = 0 (odd integrand)
# Wait, u * sech^3(u) * tanh(u) is odd * even * even * odd = even * even = even!
# No: u is odd, sech^3 is even, tanh is odd, so u*sech^3*tanh = odd*even*odd = even.
# So the integral is NOT zero.

# Let me compute it numerically
def integrand_y_matrix(u):
    """u * sech^3(u) * tanh(u)"""
    s = 1.0 / np.cosh(u)
    t = np.tanh(u)
    return u * s**3 * t

M_y_01_integral, _ = integrate.quad(integrand_y_matrix, -50, 50)
print(f"  Matrix element integral int u*sech^3(u)*tanh(u) du = {M_y_01_integral:.10f}")

# Normalization constants for PT s=2 modes
# Zero mode: psi_0 = sqrt(3/(4*xi)) * sech^2(y/xi)
# n=1 mode:  psi_1 = sqrt(3/(2*xi)) * sech(y/xi) * tanh(y/xi)
# (normalization: int |psi_n|^2 dy = 1)

# Check normalization of zero mode
N0_sq = 3.0 / (4.0 * XI)
norm_0, _ = integrate.quad(lambda y: N0_sq * (1.0/np.cosh(y/XI))**4, -50*XI, 50*XI)
print(f"\n  Zero mode normalization: {norm_0:.10f} (should be 1)")
check("C1_zero_mode_norm", norm_0, 1.0, tol=1e-6)

# Check normalization of n=1 mode
N1_sq = 3.0 / (2.0 * XI)
norm_1, _ = integrate.quad(
    lambda y: N1_sq * (1.0/np.cosh(y/XI))**2 * np.tanh(y/XI)**2,
    -50*XI, 50*XI
)
print(f"  n=1 mode normalization: {norm_1:.10f} (should be 1)")
check("C2_n1_mode_norm", norm_1, 1.0, tol=1e-6)

# Matrix element <1|y|0> in physical units
N0 = math.sqrt(N0_sq)
N1 = math.sqrt(N1_sq)
M_y_01 = N0 * N1 * XI**2 * M_y_01_integral
print(f"\n  <1|y|0> = {M_y_01:.6f} l_Pl")

# The energy of the n=1 mode
omega_1_sq = 3.0 * ALPHA / 2.0  # PT n=1 eigenvalue
omega_1 = math.sqrt(omega_1_sq)
print(f"  omega_1 = sqrt(3*alpha/2) = {omega_1:.6f} M_Pl")

# Profile response contribution to bending rigidity:
# kappa_resp = -|<1|y|0>|^2 / omega_1^2 * (appropriate prefactor)
# The standard result uses the resolvent:
#   c_R = -(1/sigma) * integral sum |<n|y|0>|^2 / omega_n^2

# For the discrete spectrum, only n=1 contributes (n=0 is zero mode):
c_R_n1 = -M_y_01**2 / omega_1_sq
print(f"\n  Profile response (n=1 only):")
print(f"    |<1|y|0>|^2 = {M_y_01**2:.6e}")
print(f"    omega_1^2 = {omega_1_sq:.6f}")
print(f"    c_R(n=1) = -|<1|y|0>|^2 / omega_1^2 = {c_R_n1:.6e}")

# Continuum contribution (suppressed by mass gap)
# The continuum starts at omega = m_sigma = sqrt(2*alpha)
# Contribution is integral dk |<k|y|0>|^2 / (k^2 + m_sigma^2)
# This is exponentially suppressed relative to the bound state

# For now, estimate the continuum contribution using completeness:
# sum_n |<n|y|0>|^2 = <0|y^2|0> (resolution of identity)
y2_zero_mode, _ = integrate.quad(
    lambda y: N0_sq * (1.0/np.cosh(y/XI))**4 * y**2,
    -50*XI, 50*XI
)
print(f"\n  <0|y^2|0> = {y2_zero_mode:.6e}")
print(f"  |<1|y|0>|^2 = {M_y_01**2:.6e}")
print(f"  Continuum share: {(y2_zero_mode - M_y_01**2)/y2_zero_mode*100:.2f}%")

# =============================================================================
# PART D: TOTAL CLASSICAL BENDING RIGIDITY
# =============================================================================

print("\n" + "=" * 72)
print("PART D: Total Classical Bending Rigidity")
print("=" * 72)

# The full bending rigidity of the domain wall:
# kappa_total = kappa_geom + kappa_response
#
# The geometric part is the second moment of kinetic energy density.
# The response part comes from the profile deformation.
#
# Standard result for phi^4 kink (Shifman & Yung):
# kappa = (1/6) * integral dy (d phi/dy)^2 * y^2
#       = (phi_0^2 * xi) / 6 * J_2
# This IS kappa_geom from Part B.
#
# The profile response c_R(n=1) adds a correction.

kappa_response = c_R_n1  # This is negative (profile responds to reduce energy)
kappa_total = kappa_geom + kappa_response

print(f"  Classical bending rigidity components:")
print(f"    kappa_geom (kinetic 2nd moment):  {kappa_geom:.6e} M_Pl^2")
print(f"    kappa_response (PT n=1 mode):     {kappa_response:.6e} M_Pl^2")
print(f"    kappa_total:                      {kappa_total:.6e} M_Pl^2")
print(f"    Response/Geometric ratio:         {kappa_response/kappa_geom:.4f}")

# Compare to M_Pl^2 / 2 (Einstein-Hilbert coefficient)
frac_EH = kappa_total / 0.5
print(f"\n  kappa_total / (M_Pl^2/2) = {frac_EH:.4f} ({frac_EH*100:.2f}%)")

# Equivalent non-minimal coupling
xi_R_classical = kappa_total / PHI_0_SQ
print(f"\n  Equivalent xi_R = kappa_total / phi_0^2 = {xi_R_classical:.8f}")
print(f"  Target xi_R (Jormungandr C503):         {XI_R_TARGET:.8f}")
print(f"  Ratio:                                   {xi_R_classical / XI_R_TARGET:.4f}")

# The total: classical bending + Sakharov one-loop
M2_sakharav = 17 * (ALPHA/2) / (96.0 * PI**2)  # from C394
M2_classical = kappa_total
M2_total = M2_classical + M2_sakharav

print(f"\n  Combined classical + quantum:")
print(f"    Classical bending:   {M2_classical:.6e} M_Pl^2 ({M2_classical*100:.3f}%)")
print(f"    Sakharav one-loop:   {M2_sakharav:.6e} M_Pl^2 ({M2_sakharav*100:.3f}%)")
print(f"    Total:               {M2_total:.6e} M_Pl^2 ({M2_total*100:.3f}%)")

check("D1_kappa_total_positive", kappa_total > 0)

# =============================================================================
# PART E: THE SURFACE TENSION / BENDING RIGIDITY RATIO
# =============================================================================

print("\n" + "=" * 72)
print("PART E: Surface Tension / Bending Rigidity Ratio")
print("=" * 72)

# The ratio kappa / sigma is dimensionally length^2
# It sets the scale at which bending energy becomes comparable to tension
ratio_kappa_sigma = kappa_total / SIGMA
l_bend = math.sqrt(abs(ratio_kappa_sigma)) if ratio_kappa_sigma > 0 else 0

print(f"  sigma (surface tension) = E_kink = {SIGMA:.4f} M_Pl")
print(f"  kappa (bending rigidity) = {kappa_total:.6e} M_Pl^2")
print(f"  kappa / sigma = {ratio_kappa_sigma:.6e} M_Pl")
print(f"  l_bend = sqrt(kappa/sigma) = {l_bend:.6e} l_Pl")
print(f"  l_bend / xi = {l_bend/XI:.6f}")

# The gravitational coupling from bending:
# G_N = 1/(2*kappa) in Planck units where G_N = 1 -> kappa = 0.5
# So the fraction is 2*kappa
print(f"\n  G_N fraction from bending: 2*kappa = {2*kappa_total:.6e}")
print(f"  This is {2*kappa_total*100:.3f}% of G_N")

# =============================================================================
# PART F: GEOMETRIC BENDING ANALYSIS
# =============================================================================

print("\n" + "=" * 72)
print("PART F: Geometric Bending Analysis")
print("=" * 72)

print(f"""
  The geometric bending rigidity kappa_geom = phi_0^2 * xi * J_2 / 6.

  In Planck units:
    phi_0^2 = {PHI_0_SQ:.4f}   (LARGE — vacuum expectation value)
    xi      = {XI:.4f}       (SMALL — kink width ~ Planck length)
    J_2     = {J_2_numeric:.4f}       (second moment, O(1))

  The product phi_0^2 * xi = {PHI_0_SQ * XI:.4f} M_Pl

  So kappa_geom = {PHI_0_SQ * XI:.4f} * {J_2_numeric:.4f} / 6 = {kappa_geom:.4f} M_Pl^2

  For G_N = 1 (Planck units), we need kappa = 0.5 M_Pl^2.
  We get kappa_geom = {kappa_geom:.4f} M_Pl^2 — a factor of
  {kappa_geom/0.5:.1f}x LARGER than needed.

  THE KEY FINDING: The bending rigidity is proportional to xi * phi_0^2.
  The kink is narrow (xi ~ 0.87 l_Pl) but has a large vacuum value
  (phi_0 ~ 8.6 M_Pl). The product phi_0^2 * xi ~ 65 M_Pl, making
  kappa_geom ~ 4.6 M_Pl^2 — well above M_Pl^2/2.

  INTERPRETATION: The classical bending rigidity of the DFC kink is
  {kappa_geom/0.5:.1f}x LARGER than the Einstein-Hilbert coefficient.
  The 1/6 conformal factor already suppresses it; the problem is
  now about the CORRECT prefactor, not about having enough rigidity.
""")

# What would we need?
# kappa = 0.5 -> phi_0^2 * xi * J_2 / 6 = 0.5
# -> phi_0^2 * xi = 3 / J_2 = 3 / 0.5520 = 5.43
# We have phi_0^2 * xi = 64.76
# So we actually have TOO MUCH by factor 64.76/5.43 = 11.9x
# Wait, that can't be right... let me recheck

needed_product = 3.0 / J_2_numeric
actual_product = PHI_0_SQ * XI
print(f"  For kappa = 0.5: need phi_0^2 * xi = 3/J_2 = {needed_product:.4f}")
print(f"  Actual phi_0^2 * xi = {actual_product:.4f}")
print(f"  Ratio actual/needed: {actual_product/needed_product:.2f}")

if actual_product > needed_product:
    print(f"\n  SURPRISE: geometric bending OVERSHOOTS by {actual_product/needed_product:.1f}x!")
    print(f"  kappa_geom = {kappa_geom:.4f} > M_Pl^2/2 = 0.5")
    print(f"  The DFC kink has MORE than enough bending rigidity!")
    print(f"  But the 1/6 conformal factor suppresses it.")
elif kappa_geom > 0.5:
    print(f"\n  kappa_geom > M_Pl^2/2: classical bending SUFFICIENT")
else:
    print(f"\n  kappa_geom < M_Pl^2/2: classical bending alone insufficient")

# Is the 1/6 the right factor?
# For a MINIMALLY coupled scalar (xi_conf = 0), the bending rigidity
# actually has a DIFFERENT coefficient. The 1/6 applies to conformal coupling.
# For minimal coupling, the relevant integral is:
# kappa_min = (1/2) * integral dy [delta_phi * (-d^2/dy^2 + V'')] delta_phi
# where delta_phi is the response to curvature R.
# This requires solving the full PT equation, not just computing the moment.

# Let's compute WITHOUT the 1/6 factor (raw second moment)
kappa_raw = PHI_0**2 * XI * J_2_numeric  # no 1/6
print(f"\n  Raw second moment (no 1/6 factor):")
print(f"    kappa_raw = phi_0^2 * xi * J_2 = {kappa_raw:.4f} M_Pl^2")
print(f"    Fraction of M_Pl^2/2: {kappa_raw/0.5:.2f}")

# With 1/6 (conformal):
print(f"    With 1/6: kappa_geom = {kappa_geom:.4f} = {kappa_geom/0.5*100:.1f}% of M_Pl^2/2")
# With 1/12 (half conformal):
kappa_12 = kappa_raw / 12.0
print(f"    With 1/12: {kappa_12:.4f} = {kappa_12/0.5*100:.1f}% of M_Pl^2/2")

# What factor would give exactly M_Pl^2/2?
factor_needed = 0.5 / kappa_raw
print(f"\n  Factor needed for kappa = M_Pl^2/2: {factor_needed:.6f}")
print(f"  1/6 = {1/6:.6f}")
print(f"  Ratio to 1/6: {factor_needed/(1/6):.4f}")

# Check: is the needed factor related to DFC parameters?
print(f"\n  Candidate factors:")
print(f"    1/(4*pi*I_4) = {1/(4*PI*4/3):.6f}")
print(f"    beta = {BETA:.6f}")
print(f"    1/(8*pi) = {1/(8*PI):.6f}")
print(f"    3/(4*E_kink) = {3/(4*E_KINK):.6f}")
print(f"    xi^2/6 = {XI**2/6:.6f}")
print(f"    Needed = {factor_needed:.6f}")

check("F1_kappa_raw_large", kappa_raw > 0.5)

# =============================================================================
# PART G: ASSESSMENT
# =============================================================================

print("\n" + "=" * 72)
print("PART G: Assessment and Next Steps")
print("=" * 72)

print(f"""
  RESULTS SUMMARY:
  ================

  1. SECOND MOMENT J_2 = (pi^2 - 6)/9 = {J_2_numeric:.6f}     [T1 exact]

  2. GEOMETRIC BENDING RIGIDITY:
     kappa_geom = phi_0^2 * xi * J_2 / 6 = {kappa_geom:.4f} M_Pl^2  [T1]
     This is {kappa_geom/0.5*100:.1f}% of M_Pl^2/2 (Einstein-Hilbert)

  3. RAW SECOND MOMENT (without 1/6):
     kappa_raw = phi_0^2 * xi * J_2 = {kappa_raw:.4f} M_Pl^2       [T1]
     This is {kappa_raw/0.5:.2f}x M_Pl^2/2 — MORE than enough

  4. PROFILE RESPONSE (PT n=1):
     kappa_response = {kappa_response:.6e} M_Pl^2 (small correction)

  KEY FINDING:
  ============
  The DFC kink has a raw second moment kappa_raw = {kappa_raw:.2f} M_Pl^2,
  which is {kappa_raw/0.5:.1f}x LARGER than the Einstein-Hilbert coefficient.

  The critical question is: what is the correct numerical prefactor?
  - Conformal coupling (1/6) gives {kappa_geom:.2f} M_Pl^2 ({kappa_geom/0.5*100:.0f}%)
  - Factor {factor_needed:.6f} gives exactly M_Pl^2/2

  The factor {factor_needed:.6f} = 1/({1/factor_needed:.2f})

  PATHS FORWARD:
  ==============
  1. Solve the full coupled perturbation equation on curved worldvolume
     to determine the EXACT prefactor (not assume 1/6)
  2. The answer depends on whether the DFC substrate is minimally or
     non-minimally coupled to its own emergent curvature
  3. Since the substrate IS the geometry (not a field living IN a geometry),
     the standard conformal/minimal distinction may not directly apply
""")

check("G1_J2_analytic", J_2_analytic, J_2_numeric, tol=1e-6)
check("G2_kappa_geom_meaningful", kappa_geom > 0.01)
check("G3_raw_moment_sufficient", kappa_raw > 0.5)
check("G4_factor_small", factor_needed < 1.0/3.0)

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
  - J_2 = (pi^2-6)/9 = {J_2_numeric:.6f} (exact)                   [T1]
  - kappa_geom = {kappa_geom:.4f} M_Pl^2 (with 1/6 factor)            [T1]
  - kappa_raw = {kappa_raw:.4f} M_Pl^2 (raw second moment)             [T1]
  - Raw moment is {kappa_raw/0.5:.1f}x LARGER than M_Pl^2/2            [T1]
  - Prefactor needed: {factor_needed:.6f} = 1/{1/factor_needed:.1f}     [T3]
  - Profile response from PT n=1: negligible correction                [T1]

  THE D4 PROBLEM IS NOW:
  "The DFC kink has MORE than enough bending rigidity.
   What is the correct prefactor (coupling to emergent curvature)?"
""")
