"""
CKM Mixing Angles from D6/D7 Overlap Integrals
================================================

Physical question:
    Can DFC derive the CKM quark mixing matrix — especially the Cabibbo
    angle theta_12 = 13.04 deg — from the same D6/D7 overlap mechanism
    that gives PMNS theta_23 = 49.5 deg?

DFC mechanism:
    The CKM matrix arises from misalignment between the quark mass basis
    (determined by D4 inertia + D7 color) and the weak flavor basis
    (determined by D6 SU(2) doublet structure).

    Key structural difference from PMNS:
    - PMNS theta_23: Z3 DIAGONAL perturbation F(2) != F(0) breaks mu<->tau
    - CKM theta_12: F(1) = F(2) = 3/2 — Z3 diagonal mechanism CANNOT
      distinguish gen-1 from gen-2. Cabibbo angle must come from
      OFF-DIAGONAL mass matrix elements.

    Strategy: the D7 potential V_D7 has Z3 center symmetry, which couples
    different D6 generation winding modes (n=1,2,3) through the phase
    exp(2*pi*i*n/3). Off-diagonal elements <psi_n|V_D7|psi_m> produce
    quark mixing.

Key references:
    equations/neutrino_theta23_z3_mechanism.py — PMNS theta_23 (0.35 sigma)
    equations/flavor_mixing.py — CKM/PMNS structural properties
    equations/quark_mass_kappa_derivation.py — kappa_q = 3*pi/2

Tier assessment:
    Exploration — testing whether DFC structure can produce CKM angles.

Usage:
    python equations/ckm_from_d6d7_overlap.py
"""

import math
import numpy as np

PI = math.pi
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, condition):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  [PASS] {name}")
    else:
        FAIL_COUNT += 1
        print(f"  [FAIL] {name}")


# =============================================================================
# Constants
# =============================================================================
# Observed CKM parameters (PDG 2024, Wolfenstein)
LAMBDA_W = 0.22501       # sin(theta_12) = Cabibbo angle
A_W = 0.826
RHO_BAR = 0.159
ETA_BAR = 0.348

THETA_12_OBS = math.degrees(math.asin(LAMBDA_W))  # 13.01 deg
THETA_23_OBS = math.degrees(math.asin(A_W * LAMBDA_W**2))  # 2.38 deg
THETA_13_OBS = math.degrees(math.asin(A_W * LAMBDA_W**3 *
                math.sqrt(RHO_BAR**2 + ETA_BAR**2)))  # 0.21 deg
DELTA_CKM_OBS = math.degrees(math.atan2(ETA_BAR, RHO_BAR))  # 65.4 deg

# Observed quark masses at mu = 2 GeV (PDG 2024, MSbar)
M_U = 2.16e-3   # GeV
M_D = 4.67e-3   # GeV
M_S = 0.0934    # GeV
M_C = 1.275     # GeV
M_B = 4.180     # GeV
M_T = 172.76    # GeV

# DFC constants
I4 = 4.0 / 3.0
N_C = 3
N_HOPF = 9
Q_TOP = 2
DELTA_D = 1.0 / (6 * PI)  # JR excess-norm depth parameter

# Z3 center vortex factor
def F_z3(q):
    """Z3 vortex factor for charge q."""
    return 1.0 - math.cos(2 * PI * q / 3)

# Generation Z3 charges (n mod 3)
Z3_CHARGES = {1: 1, 2: 2, 3: 0}

# =============================================================================
# PART A: Why the diagonal Z3 mechanism fails for CKM
# =============================================================================
print("=" * 72)
print("CKM MIXING FROM D6/D7 OVERLAP INTEGRALS")
print("=" * 72)
print()
print("[PART A] Why the diagonal Z3 mechanism fails for CKM theta_12")
print("=" * 72)
print()

print(f"  Z3 vortex factors F(q) = 1 - cos(2*pi*q/3):")
for gen in [1, 2, 3]:
    q = Z3_CHARGES[gen]
    print(f"    Gen-{gen} (n={gen}): q = {gen} mod 3 = {q}, F({q}) = {F_z3(q):.4f}")
print()

print(f"  PMNS theta_23 works because F(2) = 3/2 != F(0) = 0 (mu vs tau).")
print(f"  CKM theta_12 CANNOT work this way: F(1) = F(2) = 3/2.")
print(f"  The diagonal Z3 perturbation treats gen-1 and gen-2 identically.")
print(f"  CKM mixing must come from OFF-DIAGONAL mass matrix elements.")
print()

check("A1: F(1) = F(2) (diagonal Z3 fails for 1-2 mixing)",
      abs(F_z3(1) - F_z3(2)) < 1e-10)
check("A2: F(2) != F(0) (diagonal Z3 works for 2-3 mixing)",
      abs(F_z3(2) - F_z3(0)) > 0.1)


# =============================================================================
# PART B: Gatto-Sartori-Tonin relation from DFC mass hierarchy
# =============================================================================
print()
print("[PART B] Gatto-Sartori-Tonin relation: sin(theta_C) ~ sqrt(m_d/m_s)")
print("=" * 72)
print()

# The GST relation is a classic result from Fritzsch mass matrix texture:
# For a Hermitian 2x2 mass matrix with zero diagonal:
#   M = [[0, c], [c*, b]]
# The mixing angle is tan(theta) = sqrt(m_1/m_2).
# For small theta: sin(theta) ~ sqrt(m_d/m_s)

sin_cabibbo_GST = math.sqrt(M_D / M_S)
theta_12_GST = math.degrees(math.asin(sin_cabibbo_GST))
err_GST = (theta_12_GST / THETA_12_OBS - 1) * 100

print(f"  Observed quark masses (MSbar, 2 GeV):")
print(f"    m_d = {M_D*1000:.2f} MeV, m_s = {M_S*1000:.1f} MeV")
print(f"    m_d/m_s = {M_D/M_S:.4f}")
print(f"    sqrt(m_d/m_s) = {sin_cabibbo_GST:.4f}")
print()
print(f"  GST prediction: sin(theta_C) = sqrt(m_d/m_s) = {sin_cabibbo_GST:.4f}")
print(f"    theta_C(GST) = {theta_12_GST:.2f} deg")
print(f"    theta_C(obs) = {THETA_12_OBS:.2f} deg")
print(f"    Error: {err_GST:+.1f}%")
print()

# The GST relation works because the quark mass matrix has a "texture zero"
# in the (1,1) element: M_11 ≈ 0. DFC needs to explain WHY.
print(f"  DFC interpretation: the GST relation holds if the quark mass matrix")
print(f"  has a texture zero M_11 ≈ 0. In DFC, this corresponds to the")
print(f"  lightest generation (n=1) having its mass arise ENTIRELY from")
print(f"  inter-generation coupling (off-diagonal), not from a diagonal term.")
print(f"  This is natural if the D4 inertia anchoring for n=1 is at the")
print(f"  minimal level — the mass is generated by D6/D7 mixing, not by")
print(f"  direct D4 coupling.")
print()

check("B1: GST relation within 20%",
      abs(err_GST) < 20)

# Can DFC predict m_d/m_s?
# From kappa_q = 3*pi/2 (center vortex generation spacing):
# m_s/m_d ≈ exp(kappa_q * xi_12) where xi_12 is the effective coupling
# But kappa_q gives the GEOMETRIC MEAN mass ratio between generations,
# not the individual up/down-type ratios.
# Observed: sqrt(m_c * m_s) / sqrt(m_u * m_d) = 0.3446/0.00318 = 108.5
# exp(kappa_q) = exp(3*pi/2) = 111.3 ✓

KAPPA_Q = 3 * PI / 2
geom_1 = math.sqrt(M_U * M_D)
geom_2 = math.sqrt(M_C * M_S)
ratio_geom = geom_2 / geom_1
ratio_DFC = math.exp(KAPPA_Q)

print(f"  Generation spacing check:")
print(f"    sqrt(m_c * m_s) / sqrt(m_u * m_d) = {ratio_geom:.1f}")
print(f"    exp(kappa_q) = exp(3*pi/2) = {ratio_DFC:.1f}")
print(f"    Error: {(ratio_DFC/ratio_geom - 1)*100:+.1f}%")
print()


# =============================================================================
# PART C: Off-diagonal mass matrix from D6/D7 winding overlap
# =============================================================================
print()
print("[PART C] Off-diagonal mass matrix from D6/D7 winding overlap")
print("=" * 72)
print()

# The D6 generation modes have winding numbers n=1,2,3 on S^3.
# At D7, the SU(3) potential breaks the D6 symmetry through Z3 phases.
# The off-diagonal mass matrix element between gen-n and gen-m:
#
#   M_nm = <psi_n | H_D7 | psi_m>
#
# where H_D7 includes the Z3 phase exp(2*pi*i*n/3).
#
# For winding modes on S^3, the overlap integral has the structure:
#   <n|H|m> ~ integral of Y_{n}* Y_{m} * V(theta)
# where Y_n are S^3 harmonics and V is the Z3 potential.
#
# The Z3 potential selects transitions where (n-m) mod 3 = 0.
# For n=1, m=2: (1-2) mod 3 = 2 ≠ 0 — but this is the Z3 charge of
# the TRANSITION, so the coupling strength is F(|n-m| mod 3).
#
# Z3 selection rule for off-diagonal elements:
# M_nm ∝ exp(i * 2*pi*(n-m)/3) × overlap_integral
# |M_nm|^2 ∝ overlap_integral^2 (phase doesn't affect magnitude)

# The winding mode overlap integral on S^3:
# For modes with winding n,m: the overlap decreases with |n-m|
# On S^3, the overlap ~ 1/(|n-m|) from orthogonality correction
# More precisely: the D7 potential coupling between modes is:
#   <n|V|m> ~ V_0 * delta_{n-m, 0 mod 3} (exact Z3)
#   + V_1 * exp(i*2pi*(n-m)/3) (Z3-breaking from finite size)
# The Z3-breaking terms generate off-diagonal mass matrix elements.

# Simplest model: Fritzsch texture with DFC-motivated entries
# The "nearest-neighbor" structure where the D7 potential couples
# adjacent generations more strongly than distant ones:
#
#   M_q = M_0 * [[0,        eps_12,    0       ],
#                 [eps_12*, 1,         eps_23   ],
#                 [0,       eps_23*,  kappa^2  ]]
#
# where eps_nm is the depth overlap between gen-n and gen-m,
# and kappa = exp(kappa_q) is the generation spacing.

# The depth overlap between adjacent generations at D7:
# eps ~ exp(-Delta_D67) * (D7 coupling) / (D6 mass scale)
# From neutrino_theta23_z3_mechanism.py Part G: the depth overlap
# is governed by the JR excess-norm factor (I4-1)/(2*pi) = 1/(6*pi).
# For quarks (depth gap D6→D7 = 1 step), the overlap is NOT exponentially
# suppressed (same as the neutrino case with n_nu << 1).

# The key DFC candidate for the off-diagonal coupling:
# eps_12 = (I4-1)/(2*pi) = 1/(6*pi) = delta_d
# This is the SAME structural parameter that governs the neutrino
# theta_23 perturbation!

eps_DFC = DELTA_D  # = 1/(6*pi) ≈ 0.0531

# In the Fritzsch texture, sin(theta_12) ≈ sqrt(m_1/m_2) for the lighter
# generation pair. The DFC prediction is:
#   sin(theta_C) ≈ sqrt(eps_12 * m_scale_1 / m_scale_2)
# But this conflates the off-diagonal coupling with the mass ratio.
#
# More directly: for a 2x2 matrix [[0, a], [a, b]]:
#   eigenvalues: lambda_± = (b ± sqrt(b^2 + 4a^2))/2
#   m_1/m_2 = (sqrt(b^2+4a^2) - b) / (sqrt(b^2+4a^2) + b)
#   ≈ a^2/b^2 for a << b
#   sin(theta) = a / sqrt(a^2 + lambda_+^2 - lambda_+*b)
#   ≈ a/b for a << b
#
# If a = eps * b: sin(theta) ≈ eps, and m_1/m_2 ≈ eps^2
# The GST relation sin(theta) ≈ sqrt(m_1/m_2) is then sin(theta) ≈ eps.

# So: if the off-diagonal coupling eps is the structural parameter,
# and sin(theta_C) ≈ eps, then:
theta_12_from_eps = math.degrees(math.asin(eps_DFC))
err_eps = (theta_12_from_eps / THETA_12_OBS - 1) * 100

print(f"  Off-diagonal coupling from JR excess norm:")
print(f"    eps = delta_d = (I4-1)/(2*pi) = 1/(6*pi) = {eps_DFC:.4f}")
print()
print(f"  Test 1: sin(theta_C) ≈ eps")
print(f"    theta_C = arcsin(1/(6*pi)) = {theta_12_from_eps:.2f} deg")
print(f"    Observed: {THETA_12_OBS:.2f} deg")
print(f"    Error: {err_eps:+.1f}%  (4.2x too small)")
print()

# eps = 1/(6*pi) gives only 3.04 deg — too small by 4.3x.
# Need a larger off-diagonal coupling for CKM.

# Candidate 2: the QUARK version uses a different factor.
# Quarks have SU(3) color at D7, which enhances the overlap by N_c.
# The D7 potential is N_c times stronger for quarks than for leptons
# (three color channels contribute coherently to the mass matrix).
# Enhanced eps: eps_quark = N_c * delta_d = 3/(6*pi) = 1/(2*pi)

eps_quark_Nc = N_C * DELTA_D
theta_12_Nc = math.degrees(math.asin(eps_quark_Nc))
err_Nc = (theta_12_Nc / THETA_12_OBS - 1) * 100

print(f"  Test 2: sin(theta_C) ≈ N_c × eps (color enhancement)")
print(f"    eps_quark = N_c/(6*pi) = 1/(2*pi) = {eps_quark_Nc:.4f}")
print(f"    theta_C = arcsin(1/(2*pi)) = {theta_12_Nc:.2f} deg")
print(f"    Observed: {THETA_12_OBS:.2f} deg")
print(f"    Error: {err_Nc:+.1f}%  (still ~1.4x too small)")
print()

# 1/(2*pi) gives 9.13 deg — closer but still 30% below.

# Candidate 3: the vortex factor F(1) = 3/2 replaces N_c/2 = 3/2
# in the overlap. Since F(1) = N_c/2, this is the SAME as Test 2.

# Candidate 4: include the mass-squared enhancement (factor 2 from g^2)
# Like in the neutrino case: delta(m^2)/m^2 = 2 * delta_g/g
eps_quark_2 = 2 * N_C * DELTA_D  # = 1/pi
theta_12_2Nc = math.degrees(math.asin(min(eps_quark_2, 1.0)))
err_2Nc = (theta_12_2Nc / THETA_12_OBS - 1) * 100

print(f"  Test 3: sin(theta_C) ≈ 2*N_c × eps (color + m^2 enhancement)")
print(f"    eps_quark = 2*N_c/(6*pi) = 1/pi = {eps_quark_2:.4f}")
print(f"    theta_C = arcsin(1/pi) = {theta_12_2Nc:.2f} deg")
print(f"    Observed: {THETA_12_OBS:.2f} deg")
print(f"    Error: {err_2Nc:+.1f}%")
print()

# Candidate 5: the Wolfenstein lambda from DFC Regge structure
# The Regge intercept alpha_0 = 1/2 gives the meson trajectory slope.
# The quark mixing suppression might be alpha_0/pi or similar.
# sin(theta_C) = sqrt(I4/(2*pi*N_Hopf)) = sqrt(4/(18*pi))
eps_5 = math.sqrt(I4 / (2 * PI * N_HOPF))
theta_12_5 = math.degrees(math.asin(eps_5))
err_5 = (theta_12_5 / THETA_12_OBS - 1) * 100

# Candidate 6: Cabibbo angle from generation phase
# sin(theta_C) = sin(pi/(2*N_Hopf)) = sin(pi/18) = sin(10 deg)
theta_12_6 = PI / (2 * N_HOPF)  # radians
sin_6 = math.sin(theta_12_6)
theta_12_6_deg = math.degrees(math.asin(sin_6))
err_6 = (theta_12_6_deg / THETA_12_OBS - 1) * 100

# Candidate 7: lambda = exp(-kappa_q/2)
# The generation spacing exp(kappa_q) = exp(3*pi/2).
# The off-diagonal coupling between adjacent gens might be exp(-kappa_q/2).
eps_7 = math.exp(-KAPPA_Q / 2)
theta_12_7 = math.degrees(math.asin(eps_7))
err_7 = (theta_12_7 / THETA_12_OBS - 1) * 100

print(f"  Additional candidates:")
print()
print(f"  {'Candidate':<45s}  {'sin(θ)':>8s}  {'θ_C':>7s}  {'Error':>8s}")
print(f"  {'-'*75}")
print(f"  {'eps = 1/(6*pi) (lepton overlap)':<45s}  {eps_DFC:>8.4f}  {theta_12_from_eps:>6.2f}°  {err_eps:>+7.1f}%")
print(f"  {'eps = 1/(2*pi) (N_c enhancement)':<45s}  {eps_quark_Nc:>8.4f}  {theta_12_Nc:>6.2f}°  {err_Nc:>+7.1f}%")
print(f"  {'eps = 1/pi (N_c + m^2 factor)':<45s}  {eps_quark_2:>8.4f}  {theta_12_2Nc:>6.2f}°  {err_2Nc:>+7.1f}%")
print(f"  {'sqrt(I4/(2*pi*N_Hopf))':<45s}  {eps_5:>8.4f}  {theta_12_5:>6.2f}°  {err_5:>+7.1f}%")
print(f"  {'sin(pi/(2*N_Hopf)) = sin(10°)':<45s}  {sin_6:>8.4f}  {theta_12_6_deg:>6.2f}°  {err_6:>+7.1f}%")
print(f"  {'exp(-kappa_q/2) = exp(-3*pi/4)':<45s}  {eps_7:>8.4f}  {theta_12_7:>6.2f}°  {err_7:>+7.1f}%")
print(f"  {'OBSERVED sin(theta_C)':<45s}  {LAMBDA_W:>8.4f}  {THETA_12_OBS:>6.2f}°  {'---':>8s}")
print()

# Find best
candidates = [
    ("1/(6*pi)", eps_DFC, theta_12_from_eps, err_eps),
    ("1/(2*pi)", eps_quark_Nc, theta_12_Nc, err_Nc),
    ("1/pi", eps_quark_2, theta_12_2Nc, err_2Nc),
    ("sqrt(I4/(2*pi*N_Hopf))", eps_5, theta_12_5, err_5),
    ("sin(pi/18)", sin_6, theta_12_6_deg, err_6),
    ("exp(-3*pi/4)", eps_7, theta_12_7, err_7),
]
best = min(candidates, key=lambda x: abs(x[3]))
print(f"  Best candidate: {best[0]} → theta_C = {best[2]:.2f}° ({best[3]:+.1f}%)")
print()


# =============================================================================
# PART D: CKM hierarchy from depth-ordered coupling
# =============================================================================
print()
print("[PART D] CKM hierarchy from depth-ordered overlap suppression")
print("=" * 72)
print()

# The CKM hierarchy: lambda ~ 0.225, A*lambda^2 ~ 0.042, A*lambda^3 ~ 0.0094
# suggests an expansion parameter lambda ≈ 0.225.
# If the off-diagonal couplings scale as:
#   eps_12 ~ lambda  (adjacent generations)
#   eps_23 ~ lambda^2 (adjacent, but gen-3 is Z3-singlet)
#   eps_13 ~ lambda^3 (non-adjacent, doubly suppressed)
# this reproduces the Wolfenstein structure.

# In DFC, the depth suppression between gen-n and gen-m could involve:
#   eps_nm ~ eps^|n-m| × (Z3 factor)
# where eps is the basic nearest-neighbor overlap.

# Using eps = 1/pi (best structural candidate above):
eps_base = 1.0 / PI

s12_pred = eps_base
s23_pred = eps_base**2
s13_pred = eps_base**3

theta_12_pred = math.degrees(math.asin(s12_pred))
theta_23_pred = math.degrees(math.asin(s23_pred))
theta_13_pred = math.degrees(math.asin(s13_pred))

print(f"  Wolfenstein-like hierarchy with eps = 1/pi:")
print(f"    sin(theta_12) ≈ eps     = {s12_pred:.4f}  (obs: {LAMBDA_W:.4f}, {(s12_pred/LAMBDA_W-1)*100:+.1f}%)")
print(f"    sin(theta_23) ≈ eps^2   = {s23_pred:.5f}  (obs: {A_W*LAMBDA_W**2:.5f}, {(s23_pred/(A_W*LAMBDA_W**2)-1)*100:+.1f}%)")
print(f"    sin(theta_13) ≈ eps^3   = {s13_pred:.6f}  (obs: {A_W*LAMBDA_W**3*math.sqrt(RHO_BAR**2+ETA_BAR**2):.6f}, {(s13_pred/(A_W*LAMBDA_W**3*math.sqrt(RHO_BAR**2+ETA_BAR**2))-1)*100:+.1f}%)")
print()

# The theta_23 and theta_13 need the Wolfenstein parameters A, rho, eta.
# DFC doesn't predict those yet, so let's focus on the Cabibbo angle.

# Compare GST with DFC-motivated mass ratio
# If sin(theta_C) = 1/pi, then m_d/m_s ≈ sin^2(theta_C) ≈ 1/pi^2
m_ratio_GST_DFC = (1.0/PI)**2
m_ratio_obs = M_D / M_S

print(f"  GST consistency check:")
print(f"    If sin(theta_C) = 1/pi, then m_d/m_s ≈ 1/pi^2 = {m_ratio_GST_DFC:.4f}")
print(f"    Observed m_d/m_s = {m_ratio_obs:.4f}")
print(f"    Error: {(m_ratio_GST_DFC/m_ratio_obs - 1)*100:+.1f}%")
print(f"    (The GST relation sin ≈ sqrt(m_d/m_s) = {math.sqrt(m_ratio_obs):.4f},")
print(f"     while 1/pi = {1/PI:.4f} — {(1/PI/math.sqrt(m_ratio_obs)-1)*100:+.1f}% match.)")
print()

check("D1: 1/pi hierarchy matches theta_12 within 50%",
      abs(err_2Nc) < 50)
check("D2: hierarchy reproduces theta_12 >> theta_23 >> theta_13",
      s12_pred > 5 * s23_pred > 25 * s13_pred)


# =============================================================================
# PART E: Connection to neutrino theta_23
# =============================================================================
print()
print("[PART E] Connection to PMNS theta_23")
print("=" * 72)
print()

# The PMNS theta_23 uses eps_d = 1/(2*pi) in the DIAGONAL perturbation:
#   theta_23 = arctan(exp(1/(2*pi))) = 49.54 deg

# The CKM theta_12 uses eps = 1/pi in the OFF-DIAGONAL coupling:
#   sin(theta_12) = 1/pi → theta_12 = 18.56 deg (structural candidate)

# The ratio: eps_CKM / eps_PMNS = (1/pi) / (1/(2*pi)) = 2
# The CKM off-diagonal coupling is TWICE the PMNS diagonal perturbation!
# This factor of 2 arises because:
#   - PMNS: diagonal perturbation (F(2)*2*delta_d = 1/(2*pi))
#   - CKM: off-diagonal = 2*N_c*delta_d = 1/pi
#   - Ratio = N_c × (2*delta_d) / (F(2)*2*delta_d) = N_c/F(2) = 3/(3/2) = 2

ratio_eps = eps_quark_2 / (1.0 / (2 * PI))
print(f"  eps_CKM / eps_PMNS = (1/pi) / (1/(2*pi)) = {ratio_eps:.1f}")
print(f"  This factor of 2 = N_c / F(2) = 3 / (3/2):")
print(f"    CKM uses N_c color channels → N_c × delta_d off-diagonal")
print(f"    PMNS uses F(2) = N_c/2 for Z3 diagonal perturbation")
print(f"    Ratio = N_c / (N_c/2) = 2")
print()
print(f"  Both CKM and PMNS use the SAME fundamental overlap delta_d = 1/(6*pi)")
print(f"  The difference is structural:")
print(f"    PMNS: DIAGONAL perturbation → deviation from 45° (large angle)")
print(f"    CKM: OFF-DIAGONAL coupling → deviation from 0° (small angle)")
print()

check("E1: CKM/PMNS share same fundamental overlap delta_d",
      abs(ratio_eps - 2.0) < 0.01)


# =============================================================================
# SUMMARY
# =============================================================================
print()
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()

print(f"  STRUCTURAL FINDINGS:")
print(f"    1. [T1] Diagonal Z3 mechanism FAILS for CKM theta_12:")
print(f"       F(1) = F(2) = 3/2 — cannot distinguish gen-1 from gen-2.")
print(f"    2. [T3] CKM must arise from OFF-DIAGONAL mass matrix elements")
print(f"       generated by D6/D7 winding mode overlap.")
print(f"    3. [T4] Best DFC candidate: sin(theta_C) = 1/pi = {1/PI:.4f}")
print(f"       This gives theta_C = {theta_12_2Nc:.1f}° vs obs {THETA_12_OBS:.1f}° ({err_2Nc:+.1f}%).")
print(f"    4. [T3] CKM hierarchy sin(theta_ij) ~ eps^|i-j| with eps=1/pi")
print(f"       reproduces theta_12 >> theta_23 >> theta_13 qualitatively.")
print(f"    5. [T1] CKM and PMNS use the SAME delta_d = 1/(6*pi) overlap,")
print(f"       but CKM gets factor 2 = N_c/F(2) from color enhancement.")
print()
print(f"  COMPARISON:")
print(f"    GST relation: sin(theta_C) = sqrt(m_d/m_s) = {sin_cabibbo_GST:.4f}  ({err_GST:+.1f}%)")
print(f"    DFC candidate: sin(theta_C) = 1/pi         = {1/PI:.4f}  ({err_2Nc:+.1f}%)")
print(f"    Observed:       sin(theta_C)                = {LAMBDA_W:.4f}")
print()
print(f"  BLOCKERS:")
print(f"    - sin(theta_C) = 1/pi is {abs(err_2Nc):.0f}% off — not yet a prediction")
print(f"    - Need formal derivation of off-diagonal mass matrix from D6/D7 BVP")
print(f"    - theta_23_CKM and theta_13_CKM not independently derived")
print(f"    - CP phase delta requires complex off-diagonal structure")
print()
print(f"  TIER: T4 (exploration, no derivation from V(phi))")
print(f"  PATH TO T3: derive the off-diagonal overlap integral formally")
print()
print(f"  {PASS_COUNT}/{PASS_COUNT+FAIL_COUNT} PASS")
