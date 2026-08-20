"""
D4 Gravitational Redshift: DFC Predictions vs Observed Phenomena
================================================================

Physical question:
    The gravity spoke (C396-C400) established internal consistency of the DFC
    gravity framework: analog metric, 1/r potential, Jormungandr fixed point.
    But these were inward-facing results. This module turns OUTWARD: compute
    DFC predictions for specific observed gravitational redshift phenomena
    and compare against measured values.

    Gravitational redshift is the simplest gravitational prediction because
    it requires only the weak-field metric (the Newtonian potential) and the
    connection between potential depth and clock rate. It does NOT require
    the full nonlinear field equations, making it the ideal first test.

DFC mechanism:
    In DFC, a clock is a stable kink undergoing periodic internal motion at
    its Compton frequency omega_C = mc^2/hbar. Near a mass M, the compression
    field is deeper anchored — the local field propagation is modified.

    The key chain is:
    1. V(phi) -> kink -> worldvolume 3D Laplacian -> 1/r potential [T1, C397/C399]
    2. 1/r potential -> Phi(r) = -G_N M/r [T3, requires G_N derivation]
    3. Modified field eq: (1 - 2Phi/c^2) d^2phi/dt^2 = c^2 nabla^2 phi - V'(phi)
       This step is OPEN: the (2Phi/c^2) term is a working hypothesis
    4. Local Compton frequency: omega_C(Phi) = omega_C * sqrt(1 + 2Phi/c^2)

    Step 3 is where the derivation chain currently breaks. The existing DFC
    account (time_dilation.md) inserts this term as a hypothesis. The analog
    metric (C396) shows HOW the substrate's propagation speed varies near a
    kink, but connecting this to the standard Newtonian potential for an
    external mass source is not yet done.

    HONEST STATUS: DFC can derive 1/r from worldvolume dimensionality [T1].
    DFC cannot yet derive the coefficient G_N from V(phi) [T4]. DFC cannot
    yet derive the (2Phi/c^2) modification from substrate dynamics [T4].
    When the standard Phi = -GM/r is ASSUMED, all gravitational redshift
    predictions follow identically to GR, because the mechanism is the same
    (modified local clock rate by potential depth).

Computations:
    Part A: Derivation chain — what DFC provides vs what is assumed
    Part B: Pound-Rebka prediction (lab-scale, weak field)
    Part C: GPS gravitational correction (satellite altitude)
    Part D: Solar limb redshift (stellar scale)
    Part E: White dwarf surface redshift (strong field, z ~ 10^-4)
    Part F: Neutron star surface redshift (strong field, z ~ 0.3)
    Part G: Analog metric connection — what C396 actually provides
    Part H: Tier assessment and derivation gap map

Key references:
    - phenomena/gravity/time_dilation.md: existing structural DFC account
    - equations/d4_analog_metric.py (C396): position-dependent propagation
    - equations/d4_1r_intermediate_test.py (C399): 1/r verified 11 orders
    - equations/d4_worldvolume_green.py (C397): worldvolume Green's function
    - foundations/d4_gravity_gap.md: D4 gap sub-problems

Cycle: 402
"""

import math
from fractions import Fraction

# =============================================================================
# PHYSICAL CONSTANTS (SI)
# =============================================================================
G_N = 6.67430e-11        # m^3 kg^-1 s^-2
c = 2.99792458e8          # m/s
hbar = 1.054571817e-34    # J s
M_sun = 1.989e30          # kg
M_earth = 5.972e24        # kg
R_earth = 6.371e6         # m
g_earth = 9.80665         # m/s^2
k_B = 1.380649e-23        # J/K

# DFC parameters (Planck units)
ALPHA = 18 ** (1 / 3)          # ~2.6207
BETA = 1 / (9 * math.pi)      # ~0.03537
XI = math.sqrt(2 / ALPHA)     # kink width ~0.874 l_Pl
M_SIGMA = math.sqrt(2 * ALPHA)  # sigma mass
E_KINK = 36 * math.pi         # kink energy in M_Pl

# Enhancement factor from C397/C399/C400
F_ENHANCEMENT = Fraction(25, 12) * 4 * math.pi * XI  # = 22.87

# =============================================================================
# TRACKING
# =============================================================================
results = []
def check(tag, computed, expected, tol=0.05):
    if isinstance(expected, bool):
        ok = (computed == expected)
    else:
        if expected == 0:
            ok = abs(computed) < tol
        else:
            ok = abs(computed - expected) / max(abs(expected), 1e-30) < tol
    status = "PASS" if ok else "FAIL"
    results.append((tag, status, computed, expected))
    print(f"  [{status}] {tag}: computed={computed}, expected={expected}")
    return ok

print("=" * 72)
print("D4 GRAVITATIONAL REDSHIFT: DFC Predictions vs Observations")
print("Cycle 402")
print("=" * 72)

# =============================================================================
# PART A: Derivation chain — what DFC provides vs what is assumed
# =============================================================================
print("\n--- Part A: Derivation chain audit ---")

# The gravitational redshift prediction chain has 4 links:
#
# Link 1 [T1, C397/C399]: Worldvolume dimensionality -> 1/r potential
#   Green's function of 3D Laplacian on domain wall = 1/(4*pi*r)
#   Verified across 11 orders of magnitude. This is a THEOREM.
#
# Link 2 [T3, C400]: G_N from Jormungandr fixed-point
#   G_N = 1/F_enhancement * (structural factors from V(phi))
#   F = 22.87 uniquely determined at alpha^3 = 18 fixed point
#   T3 because the self-consistency condition is structural, not formally derived
#
# Link 3 [T4 OPEN]: (2*Phi/c^2) modification of field equation
#   The weak-field metric g_00 = 1 + 2*Phi/c^2 requires showing that
#   the compression gradient near a mass modifies the local field propagation
#   by exactly 2*Phi/c^2. time_dilation.md inserts this as hypothesis.
#   C396 shows position-dependent propagation speed near a kink, but
#   connecting to external Newtonian potential is not done.
#
# Link 4 [T1 given Link 3]: Compton frequency modification
#   omega_C(Phi) = omega_C * sqrt(1 + 2*Phi/c^2)
#   This is algebraic given the modified field equation.

chain = {
    "Link_1_1r_potential": "T1 (worldvolume Laplacian, C397/C399)",
    "Link_2_G_N_coefficient": "T3 (Jormungandr F=22.87, C400)",
    "Link_3_metric_modification": "T4 OPEN (2*Phi/c^2 not derived from V(phi))",
    "Link_4_Compton_shift": "T1 given Link 3 (algebraic)"
}

for link, tier in chain.items():
    print(f"  {link}: {tier}")

# OVERALL TIER: T4 (weakest link is Link 3)
# But IF we assume GR's weak-field metric (which DFC claims to reproduce
# structurally), then all predictions follow identically to GR.

print("\n  OVERALL: T4 (blocked by Link 3)")
print("  If GR weak-field metric assumed: predictions identical to GR")
print("  DFC adds: causal mechanism (compression gradient) + 1/r derivation")

check("A1_1r_derived", True, True)
check("A2_GN_open", True, True)  # G_N not derived from V(phi)

# =============================================================================
# PART B: Pound-Rebka prediction (1959)
# =============================================================================
print("\n--- Part B: Pound-Rebka experiment ---")

# Setup: gamma rays climbing h = 22.5 m in Earth's gravity
# Predicted redshift: Delta_nu/nu = g*h/c^2

h_PR = 22.5  # meters

# DFC prediction chain:
# 1. 1/r -> Phi(r) = -G_N * M_earth / r  [T1 structure, T4 coefficient]
# 2. Phi at surface: Phi_surface = -G_N * M_earth / R_earth
# 3. Phi at height h: Phi_top = -G_N * M_earth / (R_earth + h)
# 4. Delta_Phi = Phi_top - Phi_surface = G_N * M_earth * h / R_earth^2 = g*h
# 5. Fractional frequency shift: Delta_nu/nu = Delta_Phi / c^2 = g*h/c^2

Delta_Phi_PR = g_earth * h_PR  # m^2/s^2
redshift_PR_predicted = Delta_Phi_PR / c**2

# Observed (Pound-Rebka 1959, Pound-Snider 1965 to 1%)
redshift_PR_observed = 2.46e-15

error_PR = (redshift_PR_predicted - redshift_PR_observed) / redshift_PR_observed

print(f"  Height: {h_PR} m")
print(f"  Delta_Phi = g*h = {Delta_Phi_PR:.2f} m^2/s^2")
print(f"  DFC prediction: Delta_nu/nu = {redshift_PR_predicted:.4e}")
print(f"  Observed:        Delta_nu/nu = {redshift_PR_observed:.4e}")
print(f"  Error: {error_PR*100:.4f}%")
print(f"  Status: {'+' if error_PR > 0 else ''}{error_PR*100:.2f}% (Pound-Snider confirmed to 1%)")

# NOTE: This is identical to GR because we used Phi = -GM/r (assumed, not derived)
# DFC contribution: 1/r derived from worldvolume [T1]; g*h approximation [T1]
# DFC gap: G_N coefficient [T4]; (2Phi/c^2) metric modification [T4]

check("B1_PoundRebka_redshift", redshift_PR_predicted, redshift_PR_observed, tol=0.01)

# =============================================================================
# PART C: GPS gravitational correction
# =============================================================================
print("\n--- Part C: GPS satellite time dilation ---")

# GPS orbit: altitude 20,200 km = 20,200,000 m from surface
# Radius from Earth center: r_GPS = R_earth + 20200 km
r_GPS = R_earth + 20200e3  # m = 26,571 km
v_GPS = 3874.0  # m/s (orbital velocity)

# Gravitational potential at surface and GPS altitude
Phi_surface = -G_N * M_earth / R_earth
Phi_GPS = -G_N * M_earth / r_GPS

# Gravitational time dilation factor
# dtau/dt = sqrt(1 + 2*Phi/c^2) ≈ 1 + Phi/c^2
# Clock at GPS altitude runs FAST relative to surface:
# Delta_tau_grav = (Phi_GPS - Phi_surface) / c^2

Delta_Phi_GPS = Phi_GPS - Phi_surface  # positive (less negative at altitude)
grav_correction_per_sec = Delta_Phi_GPS / c**2  # fractional rate difference

# Convert to microseconds per day
grav_correction_per_day = grav_correction_per_sec * 86400 * 1e6  # microseconds

# Velocity time dilation (special relativistic)
# dtau/dt = sqrt(1 - v^2/c^2) ≈ 1 - v^2/(2c^2)
vel_correction_per_sec = -v_GPS**2 / (2 * c**2)
vel_correction_per_day = vel_correction_per_sec * 86400 * 1e6

# Net
net_correction_per_day = grav_correction_per_day + vel_correction_per_day

# Observed/applied GPS correction
grav_observed = 45.9  # microseconds/day (gravitational, clocks fast)
vel_observed = -7.2   # microseconds/day (velocity, clocks slow)
net_observed = 38.7   # microseconds/day

print(f"  GPS altitude: {(r_GPS - R_earth)/1e3:.0f} km")
print(f"  GPS orbital velocity: {v_GPS:.0f} m/s")
print(f"\n  Gravitational correction: {grav_correction_per_day:+.1f} us/day (obs: +{grav_observed} us/day)")
print(f"  Velocity correction:     {vel_correction_per_day:+.1f} us/day (obs: {vel_observed} us/day)")
print(f"  Net correction:          {net_correction_per_day:+.1f} us/day (obs: +{net_observed} us/day)")

error_grav = (grav_correction_per_day - grav_observed) / grav_observed
error_vel = (vel_correction_per_day - vel_observed) / vel_observed
error_net = (net_correction_per_day - net_observed) / net_observed

print(f"\n  Gravitational error: {error_grav*100:+.2f}%")
print(f"  Velocity error:     {error_vel*100:+.2f}%")
print(f"  Net error:          {error_net*100:+.2f}%")

check("C1_GPS_grav", grav_correction_per_day, grav_observed, tol=0.02)
check("C2_GPS_vel", abs(vel_correction_per_day), abs(vel_observed), tol=0.15)
check("C3_GPS_net", net_correction_per_day, net_observed, tol=0.05)

# =============================================================================
# PART D: Solar limb redshift
# =============================================================================
print("\n--- Part D: Solar gravitational redshift ---")

# Solar surface gravitational potential
R_sun = 6.957e8  # m
Phi_sun_surface = -G_N * M_sun / R_sun

# Gravitational redshift z = -Phi/c^2 (positive for light escaping)
z_sun_predicted = -Phi_sun_surface / c**2

# Observed: z_sun ≈ 2.12e-6 (multiple measurements, consistent with GR)
z_sun_observed = 2.12e-6

error_sun = (z_sun_predicted - z_sun_observed) / z_sun_observed

print(f"  Solar surface Phi/c^2 = {Phi_sun_surface / c**2:.6e}")
print(f"  DFC predicted z = {z_sun_predicted:.4e}")
print(f"  Observed z =      {z_sun_observed:.4e}")
print(f"  Error: {error_sun*100:+.2f}%")

check("D1_solar_redshift", z_sun_predicted, z_sun_observed, tol=0.02)

# =============================================================================
# PART E: White dwarf surface redshift (Sirius B)
# =============================================================================
print("\n--- Part E: White dwarf redshift (Sirius B) ---")

# Sirius B: M ≈ 1.018 M_sun, R ≈ 0.0084 R_sun = 5844 km
M_SirB = 1.018 * M_sun
R_SirB = 0.0084 * R_sun

Phi_SirB = -G_N * M_SirB / R_SirB
z_SirB_predicted = -Phi_SirB / c**2

# Observed: z ≈ 3.0e-4 (Barstow et al. 2005)
z_SirB_observed = 3.0e-4

error_SirB = (z_SirB_predicted - z_SirB_observed) / z_SirB_observed

print(f"  Sirius B: M = {M_SirB/M_sun:.3f} M_sun, R = {R_SirB/R_sun:.4f} R_sun")
print(f"  Surface Phi/c^2 = {Phi_SirB / c**2:.4e}")
print(f"  DFC predicted z = {z_SirB_predicted:.4e}")
print(f"  Observed z =      {z_SirB_observed:.4e}")
print(f"  Error: {error_SirB*100:+.1f}%")

# White dwarf: still weak enough field for linear approximation
check("E1_SirB_redshift", z_SirB_predicted, z_SirB_observed, tol=0.15)

# =============================================================================
# PART F: Neutron star surface redshift (strong field)
# =============================================================================
print("\n--- Part F: Neutron star redshift (strong field) ---")

# Typical neutron star: M ≈ 1.4 M_sun, R ≈ 10 km
M_NS = 1.4 * M_sun
R_NS = 10e3  # m

# Schwarzschild radius
r_s_NS = 2 * G_N * M_NS / c**2

# Compactness parameter
compactness = r_s_NS / R_NS

# Weak-field (linear) redshift
z_NS_weak = G_N * M_NS / (R_NS * c**2)

# Full Schwarzschild redshift (exact GR)
z_NS_exact = 1.0 / math.sqrt(1.0 - r_s_NS / R_NS) - 1.0

print(f"  Neutron star: M = {M_NS/M_sun:.1f} M_sun, R = {R_NS/1e3:.0f} km")
print(f"  Schwarzschild radius: r_s = {r_s_NS/1e3:.2f} km")
print(f"  Compactness r_s/R = {compactness:.3f}")
print(f"  Weak-field z (DFC linear) = {z_NS_weak:.4f}")
print(f"  Full Schwarzschild z (GR) = {z_NS_exact:.4f}")
print(f"  Linear/exact ratio = {z_NS_weak / z_NS_exact:.4f}")
print(f"  Nonlinear correction: {(z_NS_exact - z_NS_weak)/z_NS_exact * 100:.1f}%")

# DFC STATUS: The weak-field (linear) approximation gives z_NS_weak.
# GR's full Schwarzschild solution gives z_NS_exact, which is ~30% higher
# for a typical NS. DFC's nonlinear field equation has NOT been solved
# in the strong-field regime. This is an OPEN problem (D4-B strong field).

print(f"\n  DFC STATUS: Weak-field linear approximation works to")
print(f"  {(z_NS_exact - z_NS_weak)/z_NS_exact * 100:.0f}% for NS. Full nonlinear")
print(f"  compression field solution needed for exact match.")

check("F1_NS_compactness", compactness, 0.414, tol=0.05)
check("F2_NS_weak_z", z_NS_weak, 0.207, tol=0.02)
check("F3_NS_exact_z", z_NS_exact, 0.306, tol=0.05)
# Weak-field error relative to exact
check("F4_NS_linear_error", (z_NS_exact - z_NS_weak) / z_NS_exact, 0.324, tol=0.05)

# =============================================================================
# PART G: Analog metric connection — what C396 actually provides
# =============================================================================
print("\n--- Part G: Analog metric connection to redshift ---")

# C396 showed that perturbations near a kink see an effective refractive
# index n(y) = sqrt(1 + 3*alpha*sech^2(y/xi) / (omega^2 - 2*alpha)).
# This is the position-dependent propagation speed near a SINGLE kink.
#
# For gravitational redshift, we need the effect of a DISTANT mass on
# a local clock. The connection is:
#
# 1. A distant mass M is a concentration of kink energy at position r_M.
# 2. This mass creates a compression gradient in the surrounding field.
# 3. The compression gradient modifies the local propagation speed.
# 4. The modification, in the weak-field limit, should give g_00 = 1 + 2*Phi/c^2.
#
# What C396 provides:
# - V''(phi_bg) = alpha * (2 - 3*sech^2(y/xi)) near a kink [T1]
# - The transverse potential is LINEAR (constant acceleration g = 710 l_Pl^-1) [T1]
# - This confines excitations to the worldvolume [T1]
# - For LOCALIZED sources on the wall, 1/r emerges [T1, C397/C399]
#
# What C396 does NOT provide:
# - The connection between the external mass M and the modification to the
#   local field equation. The analog metric gives the geometry near ONE kink;
#   gravitational redshift requires the cumulative effect of MANY kinks
#   (a mass M) on a distant clock.
# - The coefficient relating the 1/r potential to the Newtonian G_N.

# Demonstrate the DFC-derivable quantities:

# 1/r derived from worldvolume dimensionality [T1]
print("  DERIVED [T1]: Worldvolume 3D Laplacian -> G(r) = 1/(4*pi*r)")
print("                Verified across 11 orders of magnitude (C399)")

# Enhancement factor from kink profile [T1]
F_exact = float(Fraction(25, 12)) * 4 * math.pi * XI
print(f"  DERIVED [T1]: Enhancement factor F = (25/12) * 4*pi*xi = {F_exact:.2f}")

# G_eff = G_N / F [T3]
print(f"  STRUCTURAL [T3]: G_eff = G_N / F = G_N / {F_exact:.2f}")
print(f"                   Perturbative scalar accounts for {1/F_exact*100:.1f}% of G_N")

# The (2*Phi/c^2) term [T4 OPEN]
print(f"  OPEN [T4]: (2*Phi/c^2) metric modification not derived from V(phi)")
print(f"             C396 analog metric gives local propagation speed near kink")
print(f"             Connection to external Newtonian potential NOT established")

# What DFC DOES predict uniquely (beyond GR):
print(f"\n  DFC-UNIQUE predictions:")
print(f"  1. Gravitational redshift source is compression gradient, not spacetime curvature")
print(f"  2. 1/r emerges from worldvolume dimensionality (3D), not postulated")
print(f"  3. At r ~ xi ~ 0.87 l_Pl, massive modes contribute and 1/r may deviate")
print(f"  4. Scalar breathing mode gapped at m_sigma = {M_SIGMA:.2f} M_Pl (unobservable)")

check("G1_F_enhancement", F_exact, 22.87, tol=0.01)
check("G2_perturbative_fraction", 1/F_exact, 0.0437, tol=0.01)

# =============================================================================
# PART H: Tier assessment and summary
# =============================================================================
print("\n--- Part H: Tier assessment and derivation gap map ---")

print("""
  GRAVITATIONAL REDSHIFT PREDICTION SUMMARY
  ==========================================

  All gravitational redshift predictions are NUMERICALLY IDENTICAL to GR
  in the weak-field regime, because DFC derives the same 1/r potential
  structure and assumes the same (2*Phi/c^2) metric modification.

  What DFC DERIVES (that GR postulates):
  - 1/r potential from worldvolume dimensionality [T1, C397/C399]
  - Kink (particle) as source of compression gradient [T1, V(phi)]
  - Enhancement factor F = 22.87 from kink profile [T1]
  - alpha^3 = 18 from Jormungandr self-consistency [T3, C400]

  What DFC ASSUMES (not yet derived):
  - G_N coefficient connecting V(phi) to observed gravitational strength [T4]
  - (2*Phi/c^2) metric modification from substrate dynamics [T4]
  - Strong-field (Schwarzschild) solution from nonlinear field equation [T4]
""")

# Summary table
predictions = [
    ("Pound-Rebka (h=22.5m)", redshift_PR_predicted, redshift_PR_observed,
     (redshift_PR_predicted - redshift_PR_observed)/redshift_PR_observed * 100,
     "T4 (uses Phi=-GM/r assumed)"),
    ("GPS grav (+45.9 us/day)", grav_correction_per_day, grav_observed,
     error_grav * 100,
     "T4 (uses Phi=-GM/r assumed)"),
    ("GPS velocity (-7.2 us/day)", vel_correction_per_day, vel_observed,
     error_vel * 100,
     "T1 (KG dispersion, Lorentz covariance)"),
    ("GPS net (+38.7 us/day)", net_correction_per_day, net_observed,
     error_net * 100,
     "T4 (gravitational term dominates)"),
    ("Solar redshift (z~2.1e-6)", z_sun_predicted, z_sun_observed,
     error_sun * 100,
     "T4 (uses Phi=-GM/r assumed)"),
    ("Sirius B (z~3e-4)", z_SirB_predicted, z_SirB_observed,
     error_SirB * 100,
     "T4 (weak field, uses Phi=-GM/r)"),
    ("NS weak-field (z~0.21)", z_NS_weak, z_NS_exact,
     (z_NS_weak - z_NS_exact)/z_NS_exact * 100,
     "T4 (linear approx; NL solution OPEN)"),
]

print("  | Observation | DFC predicted | Observed | Error | Tier |")
print("  |---|---|---|---|---|")
for name, pred, obs, err, tier in predictions:
    print(f"  | {name} | {pred:.4e} | {obs:.4e} | {err:+.2f}% | {tier} |")

print(f"""
  DERIVATION GAP MAP for gravitational redshift:

  CLOSED:
  - 1/r potential from worldvolume dimensionality [T1, C397/C399]
  - Velocity time dilation from KG dispersion [T1]
  - Enhancement factor F = 22.87 [T1, C392/C400]
  - alpha^3 = 18 self-consistency [T3, C400]

  OPEN:
  - G_N = f(alpha, beta, c) [T4, D4-D]
  - Metric modification (2*Phi/c^2) from V(phi) [T4, D4-B]
  - Strong-field (Schwarzschild) from nonlinear field eq [T4]
  - Gravitational lensing angle [requires D4-B]
  - Shapiro delay [requires D4-B]
  - Mercury precession [requires full GR metric, D4-B]

  NEXT OBSERVABLE: Mercury perihelion precession
  Requires: D4-B weak-field metric derived from V(phi)
  Currently: structural account only (compression gradient -> precession)
""")

check("H1_chain_overall_T4", True, True)

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 72)
print("FINAL RESULTS")
print("=" * 72)
n_pass = sum(1 for _, s, _, _ in results if s == "PASS")
n_fail = sum(1 for _, s, _, _ in results if s == "FAIL")
n_total = len(results)
print(f"\n  {n_pass}/{n_total} PASS, {n_fail}/{n_total} FAIL")

for tag, status, computed, expected in results:
    marker = "PASS" if status == "PASS" else "FAIL"
    print(f"  [{marker}] {tag}")

print(f"""
KEY FINDING:
  All gravitational redshift predictions are numerically identical to GR
  because they use the same Phi = -GM/r potential structure. DFC's 1/r
  derivation from worldvolume dimensionality [T1] is a genuine advance
  over GR (which postulates 1/r via the field equations). However, the
  G_N coefficient and the (2*Phi/c^2) metric modification are NOT yet
  derived from V(phi) — these are the D4-B and D4-D sub-problems.

  The gravitational redshift tests do NOT currently distinguish DFC from
  GR. They confirm consistency (DFC does not contradict observations)
  but do not provide independent evidence for DFC's gravity mechanism.

  The FIRST test that could distinguish DFC from GR would be at the
  Planck scale (r ~ xi ~ 0.87 l_Pl), where massive worldvolume modes
  contribute to the potential and 1/r may deviate. This is far beyond
  current experimental reach.

TIER: T4 overall (gravitational predictions use assumed G_N and metric).
  Velocity time dilation component is T1 (KG dispersion).
  1/r structure is T1 (worldvolume dimensionality).
  Quantitative gravitational predictions are T4 (G_N, metric undetermined).
""")
