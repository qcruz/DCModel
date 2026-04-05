"""
Physical constants and model parameters for the Dimensional Folding Model.

All values in SI units unless otherwise noted.
Particle Data Group (PDG) 2024 values used where applicable.
"""

import math

# ─── Fundamental Constants ────────────────────────────────────────────────────

HBAR = 1.054571817e-34          # J·s  (reduced Planck constant)
C    = 2.99792458e8             # m/s  (speed of light)
G    = 6.67430e-11              # m³/(kg·s²)  (gravitational constant)
KB   = 1.380649e-23             # J/K  (Boltzmann constant)
ALPHA_EM = 1 / 137.035999084   # dimensionless (fine structure constant at q=0)
E_CHARGE = 1.602176634e-19      # C  (elementary charge)

# ─── Planck Units ─────────────────────────────────────────────────────────────

M_PLANCK_KG = math.sqrt(HBAR * C / G)          # kg
M_PLANCK_GEV = M_PLANCK_KG * C**2 / 1.602e-10  # GeV
L_PLANCK = math.sqrt(HBAR * G / C**3)           # m
T_PLANCK = math.sqrt(HBAR * G / C**5)           # s

# ─── Particle Masses (PDG 2024) ───────────────────────────────────────────────
# In MeV/c²

# Leptons
M_ELECTRON = 0.51099895        # MeV
M_MUON     = 105.6583755       # MeV
M_TAU      = 1776.86           # MeV

M_NU_1 = 0.0                   # MeV  (lightest neutrino, normal ordering)
M_NU_2 = None                  # MeV  (to be constrained)
M_NU_3 = None                  # MeV  (to be constrained)

# Quarks (running masses at their own scale, approximate)
M_UP      = 2.16               # MeV
M_DOWN    = 4.67               # MeV
M_CHARM   = 1270.0             # MeV
M_STRANGE = 93.4               # MeV
M_TOP     = 172760.0           # MeV  (pole mass)
M_BOTTOM  = 4180.0             # MeV

# Gauge bosons
M_W    = 80377.0               # MeV
M_Z    = 91187.6               # MeV
M_H    = 125200.0              # MeV  (Higgs)
M_GLUON = 0.0                  # MeV  (massless)
M_PHOTON = 0.0                 # MeV  (massless)

# ─── Standard Model Coupling Constants ───────────────────────────────────────
# At the Z pole (q = M_Z)

G1_MZ = 0.3573                 # U(1)_Y coupling
G2_MZ = 0.6514                 # SU(2)_L coupling
G3_MZ = 1.2179                 # SU(3)_c coupling (strong)

WEINBERG_ANGLE_SIN2 = 0.23122  # sin²(θ_W) at M_Z (on-shell scheme)
WEINBERG_ANGLE = math.asin(math.sqrt(WEINBERG_ANGLE_SIN2))  # radians

# Higgs vacuum expectation value
HIGGS_VEV = 246220.0           # MeV  (v = 246.22 GeV)

# ─── Model-Specific Parameters ────────────────────────────────────────────────
# These are the geometric parameters of the Dimensional Folding Model.
# Values marked ESTIMATE are order-of-magnitude; not yet precisely derived.

# Closure scale — energy at which D5/D6/D7 closure behaviors formed (ESTIMATE)
M_CLOSURE_SCALE = 1.0e16       # MeV  (10^16 GeV, ESTIMATE — between GUT and Planck scale)
M_COMPACTIFICATION = M_CLOSURE_SCALE  # deprecated alias — use M_CLOSURE_SCALE

# D5/D6/D7 closure geometry sizes (in meters, all order Planck length, ESTIMATES)
R_U1  = 1.0e-34                # m    characteristic radius of D5 U(1) closure (ESTIMATE)
R_S3  = 1.0e-34                # m    characteristic radius of D6 S³ closure (ESTIMATE)
R_SU3 = 1.0e-34                # m    characteristic size of D7 SU(3) closure (ESTIMATE)

# Squashing parameters (dimensionless, 0 = round, 1 = maximally deformed)
# ε_W: D6 S³ squashing → sets electroweak symmetry breaking
EPSILON_W = math.sqrt(WEINBERG_ANGLE_SIN2)     # ~0.481 (related to Weinberg angle)

# η_F: D7 SU(3) closure squashing → sets flavor symmetry breaking scale
ETA_FLAVOR = 0.1               # ESTIMATE — to be constrained from quark masses

# Dimple parameters for mass hierarchy
# d: dimple depth (sets electron mass scale)
# R_dim: dimension size (sets muon mass scale)
DIMPLE_DEPTH = None            # to be derived from M_ELECTRON
DIMENSION_SIZE = None          # to be derived from M_MUON / M_ELECTRON ratio

# Top quark Yukawa coupling (dominant Higgs mass correction)
YUKAWA_TOP = math.sqrt(2) * M_TOP / HIGGS_VEV  # ≈ 0.995


def print_summary():
    """Print a summary of key constants and derived quantities."""
    print("=== Dimensional Folding Model — Constants Summary ===\n")

    print("Fundamental:")
    print(f"  Planck mass:          {M_PLANCK_GEV:.3e} GeV")
    print(f"  Planck length:        {L_PLANCK:.3e} m")
    print()

    print("Observed particle masses (MeV):")
    print(f"  Electron:             {M_ELECTRON}")
    print(f"  Muon:                 {M_MUON}")
    print(f"  Tau:                  {M_TAU}")
    print(f"  Top quark:            {M_TOP:.1f}")
    print(f"  Higgs:                {M_H:.1f}")
    print(f"  W boson:              {M_W:.1f}")
    print(f"  Z boson:              {M_Z:.1f}")
    print()

    print("Key ratios:")
    print(f"  m_muon / m_electron:  {M_MUON / M_ELECTRON:.2f}  (207 expected)")
    print(f"  m_tau / m_muon:       {M_TAU / M_MUON:.2f}")
    print(f"  m_top / m_bottom:     {M_TOP / M_BOTTOM:.2f}")
    print(f"  m_Z / m_W:            {M_Z / M_W:.6f}  (= 1/cos θ_W expected)")
    print()

    print("Model parameters:")
    print(f"  Closure scale:          {M_CLOSURE_SCALE:.1e} MeV = {M_CLOSURE_SCALE/1e3:.1e} GeV")
    print(f"  Weinberg angle sin²:    {WEINBERG_ANGLE_SIN2}")
    print(f"  S³ squashing ε_W:       {EPSILON_W:.4f}")
    print(f"  Top Yukawa:             {YUKAWA_TOP:.4f}")


if __name__ == "__main__":
    print_summary()
