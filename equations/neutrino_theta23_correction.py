"""
T10: Neutrino mixing angle theta_23 — depth-correction analysis.

Physical question:
  Does the DFC color-topology correction delta_d = 1/(6*pi) [C205, T11] also
  shift theta_23 away from the Z2-symmetric 45 degrees?
  And what D6-level asymmetry would be needed to explain the observed 4 degree
  deviation (theta_23 = 49 degrees vs. 45 degrees)?

DFC mechanism:
  At leading order, the Z2 exchange symmetry of S^3 at D6 depth (mu <-> tau)
  forces equal entries |U_mu2| = |U_tau2| and |U_mu3| = |U_tau3|, giving
  theta_23 = 45 degrees exactly [T3, C206].

  The C205 color correction delta_d = N_c/(N_Hopf * 2*pi) = 1/(6*pi) shifts
  the MASS EIGENSTATE depth of nu_3 (not the flavor eigenstate depth).

  Key question: does a depth shift on a MASS eigenstate break theta_23 symmetry?

Key result (this module):
  If d_mu = d_tau (Z2 symmetric flavor depths at D6), then ANY correction to the
  depth d_3 of the mass eigenstate nu_3 shifts |U_mu3| and |U_tau3| by the SAME
  factor -- leaving their ratio at 1 and theta_23 = 45 degrees unchanged.

  Conclusion: delta_d = 1/(6*pi) solves T11 (mass ratio) but CANNOT shift theta_23.
  The 4-degree deviation requires a D6-level mechanism that explicitly breaks mu <-> tau.

References:
  - C205: equations/neutrino_color_correction.py (T11 solved)
  - C206: phenomena/particle_physics/neutrino_oscillations.md (T10 Z2 argument)
  - ISSUES.md T10, T11

Part A: Verify depth-shift symmetry argument algebraically
Part B: Compute required D6 asymmetry for 4-degree shift
Part C: Candidate DFC sources for D6 mu/tau asymmetry
Part D: Updated T10 status
"""

import numpy as np

print("="*65)
print("T10: Neutrino theta_23 — depth correction analysis")
print("="*65)

# ============================================================
# Constants
# ============================================================
N_c = 3
N_Hopf = 9
delta_d = N_c / (N_Hopf * 2 * np.pi)           # 1/(6*pi), C205 color correction
kappa = 5.33                                      # depth-mass ratio [T2b, C165]

theta_23_obs_deg = 49.1                           # observed; NuFIT 5.2 NH best fit
theta_23_LO_deg = 45.0                            # DFC leading order (Z2 symmetry)
delta_theta_obs_deg = theta_23_obs_deg - theta_23_LO_deg

print(f"\n--- Observed values ---")
print(f"  theta_23 (observed, NH best fit): {theta_23_obs_deg:.1f} deg")
print(f"  theta_23 (DFC leading order, Z2): {theta_23_LO_deg:.1f} deg")
print(f"  Deviation to explain:  {delta_theta_obs_deg:.1f} deg")
print(f"  delta_d = 1/(6*pi) = {delta_d:.6f}")

# ============================================================
# Part A: Depth-shift symmetry argument
# ============================================================
print("\n--- Part A: Does delta_d shift theta_23? ---")
print("[T1 algebraic]")

# At leading order: d_mu = d_tau = d_D6 (Z2 symmetric)
# Mass eigenstates at depths d_2 (nu_2) and d_3 (nu_3)
# Exponential overlap model: U_alpha_i propto exp(-c * |d_alpha - d_i|)
#
# At 45 degrees: d_3 - d_D6 = d_D6 - d_2 = Delta (equal distance)
#
# After color correction: d_3 -> d_3 + delta_d
# New distances from D6:
#   nu_3: d_3 + delta_d - d_D6 = Delta + delta_d
#   nu_2: d_D6 - d_2 = Delta (unchanged)
#
# For BOTH tau and mu (since d_mu = d_tau = d_D6):
#   |U_mu3| propto exp(-c*(Delta + delta_d))
#   |U_tau3| propto exp(-c*(Delta + delta_d))
# -> ratio |U_mu3|/|U_tau3| = 1 EXACTLY, regardless of c and delta_d

# Numerical verification with exponential overlap model
c = 1.0           # arbitrary depth-overlap width (result independent of this)
Delta = 1.0       # leading-order symmetric depth distance (arbitrary)

# Leading order (Z2 exact)
d_mu = 0.0        # D6 flavor depth of nu_mu
d_tau = 0.0       # D6 flavor depth of nu_tau (equals d_mu by Z2)
d2 = -Delta       # nu_2 depth (below D6)
d3 = +Delta       # nu_3 depth (above D6)

U_mu2_LO = np.exp(-c * abs(d_mu - d2))
U_tau2_LO = np.exp(-c * abs(d_tau - d2))
U_mu3_LO = np.exp(-c * abs(d_mu - d3))
U_tau3_LO = np.exp(-c * abs(d_tau - d3))

# Normalize columns
norm2 = np.sqrt(U_mu2_LO**2 + U_tau2_LO**2)
norm3 = np.sqrt(U_mu3_LO**2 + U_tau3_LO**2)
U_mu2_LO /= norm2;  U_tau2_LO /= norm2
U_mu3_LO /= norm3;  U_tau3_LO /= norm3

theta_23_LO = np.degrees(np.arctan2(abs(U_mu3_LO), abs(U_tau3_LO)))
print(f"\n  Leading order (Z2 exact, d_mu = d_tau):")
print(f"    |U_mu3| = {abs(U_mu3_LO):.6f}, |U_tau3| = {abs(U_tau3_LO):.6f}")
print(f"    ratio |U_mu3|/|U_tau3| = {abs(U_mu3_LO)/abs(U_tau3_LO):.8f}  (expect 1.0)")
print(f"    theta_23 = {theta_23_LO:.4f} deg  (expect 45.0)")

# After color correction: d_3 -> d_3 + delta_d
d3_corrected = d3 + delta_d

U_mu3_corr = np.exp(-c * abs(d_mu - d3_corrected))
U_tau3_corr = np.exp(-c * abs(d_tau - d3_corrected))
U_mu2_corr = np.exp(-c * abs(d_mu - d2))
U_tau2_corr = np.exp(-c * abs(d_tau - d2))

norm3c = np.sqrt(U_mu3_corr**2 + U_tau3_corr**2)
norm2c = np.sqrt(U_mu2_corr**2 + U_tau2_corr**2)
U_mu3_corr /= norm3c;  U_tau3_corr /= norm3c
U_mu2_corr /= norm2c;  U_tau2_corr /= norm2c

theta_23_corr = np.degrees(np.arctan2(abs(U_mu3_corr), abs(U_tau3_corr)))
ratio_corr = abs(U_mu3_corr)/abs(U_tau3_corr)

print(f"\n  After color correction delta_d = 1/(6*pi) = {delta_d:.6f}:")
print(f"    d_3 + delta_d = {d3_corrected:.6f}")
print(f"    |U_mu3| = {abs(U_mu3_corr):.6f}, |U_tau3| = {abs(U_tau3_corr):.6f}")
print(f"    ratio |U_mu3|/|U_tau3| = {ratio_corr:.8f}  (expect 1.0)")
print(f"    theta_23 = {theta_23_corr:.4f} deg  (expect 45.0 unchanged)")

shift_from_delta_d = theta_23_corr - theta_23_LO
print(f"\n  Shift in theta_23 from delta_d: {shift_from_delta_d:.6f} deg")
print(f"  [T1] Symmetry argument: d_mu = d_tau => ratio is 1 exactly for any delta_d")

# Verify over range of c values
print(f"\n  Robustness check (vary c, Delta):")
max_shift = 0.0
for c_test in [0.1, 0.5, 1.0, 2.0, 5.0]:
    for Delta_test in [0.5, 1.0, 2.0]:
        U_m3 = np.exp(-c_test * abs(d_mu - (Delta_test + delta_d)))
        U_t3 = np.exp(-c_test * abs(d_tau - (Delta_test + delta_d)))
        ratio_test = U_m3 / U_t3
        shift = abs(ratio_test - 1.0)
        max_shift = max(max_shift, shift)
print(f"  Max deviation from |U_mu3|/|U_tau3| = 1 over parameter scan: {max_shift:.2e}")
print(f"  [T1] Confirmed: delta_d = 1/(6*pi) does NOT shift theta_23")
print(f"  Conclusion: C205 color correction solves T11 (mass ratio) but NOT T10 (theta_23)")

# ============================================================
# Part B: Required D6 asymmetry for 4-degree shift
# ============================================================
print("\n--- Part B: Required D6 asymmetry to explain 4-degree deviation ---")
print("[T2a numerical]")

theta_target_rad = np.radians(theta_23_obs_deg)

# In 2x2 atmospheric sector:
# tan(2 theta_23) = 2 * epsilon / delta
# where epsilon = off-diagonal M_mutau, delta = M_tautau - M_mumu
# For the observed theta:
# tan(2 * 49.1 deg) = tan(98.2 deg)

tan_2theta = np.tan(2 * theta_target_rad)
print(f"\n  tan(2 * theta_23_obs) = tan(2 * {theta_23_obs_deg}°) = {tan_2theta:.4f}")

# For small deviations from 45 deg, delta_theta = delta/(2*epsilon)
# We need to find delta/epsilon
delta_theta_rad = np.radians(delta_theta_obs_deg)

# At theta_23 = 45+x with small x: tan(90+2x) = -cot(2x) ~ -1/(2x) for small x
# More carefully: tan(2*theta_23) = 2*epsilon/delta
# At theta = 45 + x (in deg), x=4.1 deg:
x_rad = np.radians(delta_theta_obs_deg)
# tan(90 + 2x) = -cot(2x)
ratio_delta_eps = abs(1.0 / tan_2theta)
print(f"  |delta/epsilon| = |1/tan(2*theta_23)| = {ratio_delta_eps:.4f}")
print(f"  (small => theta_23 close to 45, but NOT exactly 45)")

# The DFC flavor depth asymmetry needed:
# If d_tau differs from d_mu by epsilon_d (small flavor asymmetry),
# then in the 2x2 sector the mixing angle shifts from 45 deg.
# For an exponential model with Z2 breaking d_tau - d_mu = eps_d:
#   U_mu3 ~ exp(-c*(d_3 - d_D6))    [same as before]
#   U_tau3 ~ exp(-c*(d_3 - (d_D6 + eps_d)))  [tau closer to nu_3]
#   ratio = exp(-c * eps_d)  [if nu_3 is above d_D6]
# The mixing angle: tan(theta_23) = |U_mu3|/|U_tau3| [in the 2-col form]
# At 45 + 4.1 deg: tan(49.1 deg) = 1.1554
# So exp(-c * eps_d) = tan(theta_23_obs) / 1 = 1.1554... wait

# Let me be more careful. In the standard form:
# |U_tau3|/|U_mu3| = tan(theta_23) for the (2,3) sector
# (the larger entry in tau gives the >45 deg mixing)
# tan(49.1 deg) = 1.1554
tau_mu_ratio_needed = np.tan(theta_target_rad)
print(f"\n  tan(theta_23_obs) = |U_tau3|/|U_mu3| = {tau_mu_ratio_needed:.4f}")
print(f"  (need ~15.5% asymmetry in tau vs mu mixing amplitudes)")

# In exponential model: ratio = exp(c * eps_d)  [tau is closer to nu_3 by eps_d]
# For c = 1 (depth unit):
c_std = 1.0
eps_d_needed = np.log(tau_mu_ratio_needed) / c_std
print(f"\n  Required D6 flavor depth asymmetry eps_d (for c=1):")
print(f"  eps_d = ln({tau_mu_ratio_needed:.4f}) / 1 = {eps_d_needed:.4f} depth units")
print(f"  Compare to: delta_d (mass eigenstate correction) = {delta_d:.4f} depth units")
print(f"  Ratio: eps_d / delta_d = {eps_d_needed/delta_d:.3f}")

print(f"\n  Interpretation: The required D6 asymmetry is {eps_d_needed/delta_d:.1f}x")
print(f"  larger than the C205 mass-eigenstate correction delta_d = 1/(6*pi).")
print(f"  These are at different depth levels (D6 flavor vs D4 mass) -- independent effects.")

# ============================================================
# Part C: Candidate DFC sources for D6 mu/tau asymmetry
# ============================================================
print("\n--- Part C: Candidate DFC sources for D6 mu/tau asymmetry ---")
print("[T4 structural — open]")

print("""
  The theta_23 = 45 deg leading order result follows from the Z2 (mu<->tau)
  exchange symmetry of S3 at D6 depth. The 4.1-degree deviation from 45 deg
  requires this Z2 symmetry to be EXPLICITLY broken at D6.

  Candidate mechanisms in DFC (all T4 — no formula yet):

  1. CKM-like D6/D7 interface mixing:
     The same D6/D7 interface that produces the color correction delta_d = 1/(6*pi)
     could also mix the D6 flavor states non-uniformly. If the D7 closure
     couples more strongly to the tau-like winding mode than the mu-like mode,
     it would break Z2. This is the DFC analog of CKM mixing.
     Required: D6 Dirac operator in D7 SU(3) kink background with flavor labeling.

  2. D4/D6 boundary condition asymmetry:
     The D4 inertia depth sets the mass scale for all generations.
     If the D4/D6 boundary conditions differ slightly for mu and tau (due to
     the winding-number difference: mu is the 2nd winding, tau is the 3rd),
     this would break Z2.
     Required: Formal D4/D6 BVP with winding-number-dependent BC.

  3. CP-violating phase from D6 topology:
     The S3 at D6 carries a discrete CP violation possibility from the
     non-trivial pi_3(S3) = Z topology. A CP phase delta would shift
     theta_23 from 45 deg (this is the Dirac CP phase in PMNS).
     The Dirac CP phase delta_CP is measured at ~ -90 deg (T2K/NOvA), which
     would contribute to the apparent theta_23 deviation in marginalizations.
     Required: DFC account of CP violation at D6 (pi_3(S3) = Z).
  """)

# ============================================================
# Part D: Updated T10 status
# ============================================================
print("--- Part D: T10 updated status ---")
print()
print(f"  Leading order: theta_23 = 45.0 deg  [T3, Z2 symmetry of S3 at D6, C206]")
print(f"  C205 color correction: NO shift in theta_23  [T1, this module C209]")
print(f"  Observed: theta_23 = {theta_23_obs_deg} deg  (NuFIT 5.2 NH best fit)")
print(f"  Unexplained deviation: {delta_theta_obs_deg:.1f} deg")
print(f"  Required asymmetry: ~14% in |U_tau3|/|U_mu3| = tan({theta_23_obs_deg} deg) = {tau_mu_ratio_needed:.4f}")
print(f"  Mechanism: D6-level Z2 breaking needed (three T4 candidates listed above)")
print(f"  Path to T3: identify which DFC mechanism produces the ~14% asymmetry")
print(f"  Path to T2a: derive D6 Dirac operator result (JR-type BVP at D6/D7 interface)")
print()
print(f"  NOTE: delta_d = 1/(6*pi) and theta_23 deviation are INDEPENDENT problems.")
print(f"  The mass-eigenstate correction (T11) does not affect theta_23 (T10).")
print(f"  Both require D4/D7 BVP work, but at different levels: D4 mass for T11,")
print(f"  D6 flavor for T10.")
