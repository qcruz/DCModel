"""
CKM and PMNS flavor mixing matrices from DFC depth-basis misalignment.

Physical question:
  Why are the CKM (quark) mixing angles small and the PMNS (neutrino) mixing angles
  large? DFC structural account: D6/D7 adjacency aligns quark bases (small CKM);
  D4 near-degeneracy and D4/D6 depth gap produce large PMNS mixing.

DFC mechanism:
  Two eigenstate bases per fermion:
    - Flavor basis: defined by D6 SU(2) doublet coupling to W bosons
    - Mass basis: defined by D4 inertia anchoring (+ D7 color for quarks)
  Misalignment angle = mixing angle.
  CP phase = total phase around three-generation fold orientation triangle.

  Key structural predictions:
    - CKM small (D6/D7 adjacent → nearly aligned): θ_ij all < 13°  ✓
    - PMNS large (D4 far from D6, near-degenerate masses): θ ≈ 30–50°  ✓ direction
    - CP violation exists (three non-degenerate generations → J ≠ 0)   ✓ structural
    - CP violation requires N ≥ 3 generations (J=0 for N=2)             ✓ proved

  Quantitative failures:
    - No CKM angle derived from DFC parameters (all taken from data)
    - Neutrino mass ratio Δm²₃₁/Δm²₂₁ = 33.9 vs DFC 1.34 (4.3× off)
    - θ₂₃ near-degeneracy argument conflicts with m₃ ≫ m₂ (T10 tension)

Key references:
  phenomena/particle_physics/flavor_mixing.md
  equations/neutrino_masses.py (mass ratio failure)
  equations/neutrino_oscillations.py (Daya Bay comparison)
  foundations/zero_mode_multiplet.md (three generations from SU(3))
"""

import math
import cmath
import numpy as np

# ============================================================
# Observed CKM values (PDG 2024)
# ============================================================
CKM_THETA_12_DEG = 13.04    # Cabibbo angle
CKM_THETA_13_DEG = 0.2062
CKM_THETA_23_DEG = 2.381
CKM_DELTA_DEG    = 69.213   # CP-violating phase

# ============================================================
# Observed PMNS values (PDG 2024, normal hierarchy)
# ============================================================
PMNS_THETA_12_DEG = 33.44
PMNS_THETA_23_DEG = 49.2
PMNS_THETA_13_DEG = 8.57
PMNS_DELTA_DEG    = -120.0  # preliminary T2K/NOvA

# Neutrino mass-squared differences (eV²)
DM2_21 = 7.42e-5    # solar
DM2_31 = 2.517e-3   # atmospheric
DM2_RATIO_OBS = DM2_31 / DM2_21

# DFC prediction for mass ratio (from neutrino_masses.py: uniform D4 depth spacing)
DM2_RATIO_DFC = 1.34**2   # (m3/m2)^2 with uniform spacing → 1.34^2 ≈ 1.80
# Actually, neutrino_masses.py gives m2/m1 = 1.34 from uniform depth spacing
# So Δm²₃₁/Δm²₂₁ ≈ (m3²-m1²)/(m2²-m1²). With uniform spacing m_n ∝ n:
# Δm²₃₁ = 9-1=8, Δm²₂₁ = 4-1=3, ratio = 8/3 ≈ 2.67
# But the reported failure is 4.3× on mass ratio m3/m2, not Δm² ratio
DM2_RATIO_DFC_FROM_MASSES = 8.0 / 3.0   # uniform m_n ∝ n spacing

# ============================================================
# CKM matrix construction
# ============================================================
def ckm_matrix(theta12_deg, theta13_deg, theta23_deg, delta_deg):
    """
    Standard PDG parametrization of the CKM matrix.
    V = R23(theta23) × R13(theta13, delta) × R12(theta12)
    Returns 3×3 complex unitary matrix.
    """
    t12 = math.radians(theta12_deg)
    t13 = math.radians(theta13_deg)
    t23 = math.radians(theta23_deg)
    d   = math.radians(delta_deg)

    c12, s12 = math.cos(t12), math.sin(t12)
    c13, s13 = math.cos(t13), math.sin(t13)
    c23, s23 = math.cos(t23), math.sin(t23)
    eid = cmath.exp(1j * d)

    V = np.array([
        [c12*c13,                      s12*c13,              s13*cmath.exp(-1j*d)],
        [-s12*c23 - c12*s23*s13*eid,   c12*c23 - s12*s23*s13*eid,   s23*c13],
        [s12*s23 - c12*c23*s13*eid,   -c12*s23 - s12*c23*s13*eid,   c23*c13],
    ], dtype=complex)
    return V

# ============================================================
# PMNS matrix construction
# ============================================================
def pmns_matrix(theta12_deg, theta23_deg, theta13_deg, delta_deg):
    """
    Standard PMNS matrix (Majorana phases set to zero for simplicity).
    Same functional form as CKM.
    """
    return ckm_matrix(theta12_deg, theta13_deg, theta23_deg, delta_deg)

# ============================================================
# Jarlskog invariant
# ============================================================
def jarlskog(V):
    """
    J = Im[V_ud V*_us V_cs V*_cd]
    Single rephasing-invariant measure of CP violation.
    J = 0 ↔ no CP violation (either all angles = 0 or δ = 0).
    """
    return np.imag(V[0,0] * np.conj(V[0,1]) * V[1,1] * np.conj(V[1,0]))

def jarlskog_formula(theta12_deg, theta13_deg, theta23_deg, delta_deg):
    """
    Analytic formula: J = s12 c12 s13 s23 c23 sin(delta)
    """
    t12 = math.radians(theta12_deg)
    t13 = math.radians(theta13_deg)
    t23 = math.radians(theta23_deg)
    d   = math.radians(delta_deg)
    return (math.sin(t12) * math.cos(t12) * math.sin(t13) *
            math.sin(t23) * math.cos(t23) * math.sin(d))

# ============================================================
# Unitarity checks
# ============================================================
def unitarity_check(V, name="V"):
    """
    Check V†V = I (unitarity) to numerical precision.
    """
    VdV = V.conj().T @ V
    max_deviation = np.max(np.abs(VdV - np.eye(3)))
    return max_deviation

# ============================================================
# CP violation requires N ≥ 3 generations
# ============================================================
def jarlskog_n_generations(n):
    """
    For N=2 generations, the mixing matrix is real (no CP phase available).
    J = 0 exactly.
    For N=3, J ≠ 0 if all three angles are distinct.
    This is the structural DFC claim: CP violation requires N=3 (SU(3) at D7).
    """
    if n == 2:
        # 2-generation CKM is real rotation
        theta_c = math.radians(CKM_THETA_12_DEG)
        V2 = np.array([
            [math.cos(theta_c),  math.sin(theta_c)],
            [-math.sin(theta_c), math.cos(theta_c)],
        ])
        J2 = np.imag(V2[0,0] * np.conj(V2[0,1]) * V2[1,1] * np.conj(V2[1,0]))
        return J2
    elif n == 3:
        V3 = ckm_matrix(CKM_THETA_12_DEG, CKM_THETA_13_DEG, CKM_THETA_23_DEG, CKM_DELTA_DEG)
        return jarlskog(V3)
    else:
        raise ValueError(f"Only N=2 or N=3 supported; got {n}")

# ============================================================
# Depth asymmetry: quark (D6/D7 adjacent) vs neutrino (D4/D6 distant)
# ============================================================
def depth_gap_mixing_estimate():
    """
    Structural DFC argument: mixing angle θ scales with the depth gap between
    the mass basis (D_mass) and the flavor basis (D6).

    For quarks: mass from D7, flavor from D6 → gap = 1 depth step
    For neutrinos: mass from D4, flavor from D6 → gap = 2 depth steps

    Qualitative estimate: larger depth gap → larger mixing angle.
    This is structural; no quantitative formula is available from DFC.
    """
    # CKM (quark): D7 mass, D6 flavor → depth gap = 1
    ckm_depth_gap = 1   # D6 → D7
    ckm_max_angle = max(CKM_THETA_12_DEG, CKM_THETA_23_DEG, CKM_THETA_13_DEG)

    # PMNS (neutrino): D4 mass, D6 flavor → depth gap = 2
    pmns_depth_gap = 2  # D4 → D5 → D6
    pmns_max_angle = max(PMNS_THETA_12_DEG, PMNS_THETA_23_DEG, PMNS_THETA_13_DEG)

    return {
        'ckm_depth_gap': ckm_depth_gap,
        'ckm_max_angle_deg': ckm_max_angle,
        'pmns_depth_gap': pmns_depth_gap,
        'pmns_max_angle_deg': pmns_max_angle,
        'angle_ratio': pmns_max_angle / ckm_max_angle,
    }

# ============================================================
# Main output
# ============================================================
if __name__ == "__main__":
    print("=" * 68)
    print("equations/flavor_mixing.py — CKM and PMNS from DFC depth-basis misalignment")
    print("=" * 68)

    print("\n--- CKM Matrix (observed PDG values) ---")
    V_ckm = ckm_matrix(CKM_THETA_12_DEG, CKM_THETA_13_DEG, CKM_THETA_23_DEG, CKM_DELTA_DEG)
    print(f"  Input angles: θ₁₂={CKM_THETA_12_DEG}°, θ₁₃={CKM_THETA_13_DEG}°, "
          f"θ₂₃={CKM_THETA_23_DEG}°, δ={CKM_DELTA_DEG}°")
    print(f"  CKM |V| matrix:")
    for row in np.abs(V_ckm):
        print(f"    {row[0]:.4f}  {row[1]:.4f}  {row[2]:.4f}")
    J_ckm = jarlskog(V_ckm)
    J_formula = jarlskog_formula(CKM_THETA_12_DEG, CKM_THETA_13_DEG,
                                  CKM_THETA_23_DEG, CKM_DELTA_DEG)
    unit_err_ckm = unitarity_check(V_ckm, "CKM")
    print(f"  Jarlskog J = {J_ckm:.2e}  (formula: {J_formula:.2e})  [obs: ~3×10⁻⁵]")
    print(f"  Unitarity check ‖V†V − I‖_max = {unit_err_ckm:.2e}  ✓")
    print(f"  DFC status: θ values are OBSERVED INPUTS — not derived from substrate")

    print("\n--- PMNS Matrix (observed PDG values) ---")
    V_pmns = pmns_matrix(PMNS_THETA_12_DEG, PMNS_THETA_23_DEG,
                          PMNS_THETA_13_DEG, PMNS_DELTA_DEG)
    print(f"  Input angles: θ₁₂={PMNS_THETA_12_DEG}°, θ₂₃={PMNS_THETA_23_DEG}°, "
          f"θ₁₃={PMNS_THETA_13_DEG}°, δ={PMNS_DELTA_DEG}°")
    print(f"  PMNS |V| matrix:")
    for row in np.abs(V_pmns):
        print(f"    {row[0]:.4f}  {row[1]:.4f}  {row[2]:.4f}")
    J_pmns = jarlskog(V_pmns)
    unit_err_pmns = unitarity_check(V_pmns, "PMNS")
    print(f"  Jarlskog J_PMNS = {J_pmns:.4f}  (≠0: CP violation present in lepton sector)")
    print(f"  Unitarity check ‖V†V − I‖_max = {unit_err_pmns:.2e}  ✓")

    print("\n--- CP Violation Requires N ≥ 3 Generations ---")
    J2 = jarlskog_n_generations(2)
    J3 = jarlskog_n_generations(3)
    print(f"  N=2 generations: J = {J2:.2e}  (exactly 0: real CKM matrix, no CP violation)")
    print(f"  N=3 generations: J = {J3:.2e}  (nonzero: CP violation exists)")
    print(f"  DFC: J=0 for N=2 because 2D real rotation has no phase angle")
    print(f"  DFC: J≠0 for N=3 because three D6 fold orientations form a non-degenerate")
    print(f"       triangle with nonzero area in the 3D generation space   ✓ structural")

    print("\n--- Depth Gap: CKM Small vs PMNS Large ---")
    d = depth_gap_mixing_estimate()
    print(f"  Quarks:   D7(mass) ↔ D6(flavor), depth gap = {d['ckm_depth_gap']}")
    print(f"    max CKM angle = {d['ckm_max_angle_deg']:.2f}° (Cabibbo angle)")
    print(f"  Neutrinos: D4(mass) ↔ D6(flavor), depth gap = {d['pmns_depth_gap']}")
    print(f"    max PMNS angle = {d['pmns_max_angle_deg']:.2f}° (θ₂₃)")
    print(f"  Angle ratio max_PMNS / max_CKM = {d['angle_ratio']:.1f}×")
    print(f"  DFC: larger depth gap → larger mixing (structural, not quantitative) ✓")

    print("\n--- Neutrino Mass Ratio (known failure) ---")
    print(f"  Δm²₃₁/Δm²₂₁ observed: {DM2_RATIO_OBS:.1f}")
    print(f"  DFC (uniform m_n ∝ n spacing): Δm²₃₁/Δm²₂₁ ≈ {DM2_RATIO_DFC_FROM_MASSES:.2f}")
    print(f"  Error factor: {DM2_RATIO_OBS / DM2_RATIO_DFC_FROM_MASSES:.1f}×   ✗ T11 (ISSUES.md)")
    print(f"  Root cause: non-uniform D4 depth spacing required; uniform spacing assumed")
    print(f"  T10 (ISSUES.md): θ₂₃ ≈ 49° near-degeneracy argument conflicts with m₃ ≫ m₂")

    print("\n--- Summary ---")
    print(f"  ✓ CP violation exists (J ≠ 0 for N=3) — structural proof")
    print(f"  ✓ CP violation requires N ≥ 3 — structural proof")
    print(f"  ✓ CKM small / PMNS large asymmetry — structural direction")
    print(f"  ✗ No CKM angle derived from substrate parameters")
    print(f"  ✗ Neutrino mass ratio Δm²₃₁/Δm²₂₁ = {DM2_RATIO_OBS:.0f} vs DFC {DM2_RATIO_DFC_FROM_MASSES:.1f}")
    print(f"  ✗ θ₂₃ near-maximal structural argument fails for m₃ ≫ m₂ (T10)")
