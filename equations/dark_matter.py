"""
Dark matter candidates from stable intermediate kink modes in DFC.

STUB — Target for future development.

What this module will compute:
  - Mass spectrum of stable intermediate closure modes between D4 and D5
  - Stability conditions: which kink configurations are absolutely stable
    (topologically protected) vs. metastable (can decay)
  - Interaction cross-sections of DFC dark matter candidates with SM matter
  - Relic abundance from DFC compression budget dynamics

Physical argument:
  In DFC, the observed particles correspond to closures at D5 (U(1)), D6 (SU(2)),
  D7 (SU(3)). The compression depth sequence D1->D7 passes through intermediate
  depths D4.x, D4.5, etc. where partial closures could form.

  If a partial closure at depth D4+epsilon is topologically stable (its winding
  number prevents decay to D4 or ascent to D5), it would be:
  - Neutral (below D5 U(1) closure threshold -> no electromagnetic charge)
  - Stable (topological protection)
  - Massive (closure energy at D4+epsilon scale)
  - Weakly interacting (only gravitational + possible sub-D5 interactions)

  These are the defining properties of dark matter.

Candidate CLOSURE SCALES (M_c, not rest masses):
  From the two-scale depth model: M_c(D4) ~ 3.37e14 GeV (Cycle 32/depth_running.py)
  If dark matter corresponds to D4.5 (halfway between D4 inertia and D5 gauge):
    M_c(D4.5) = intermediate between M_c(D4) and M_c(D5) ≈ 10^13–10^14 GeV (closure SCALE)

  NOTE: M_c is the UV closure scale, NOT the particle rest mass. The electron has
  M_c(D5) ~ 10^13 GeV but rest mass = 0.511 MeV (ratio M_c/m ~ 10^19).
  Estimated DM rest mass ~ 35 keV from depth-to-mass exponential
  (see phenomena/cosmology/dark_matter.md).

  The M_c(D4.x) closure scales are above LHC reach — consistent with the DM
  candidates not being produced at colliders. Rest-mass derivation from M_c is
  the same unsolved problem as for quarks and leptons.

  Alternative: D3/D4 transition modes (at ~1 TeV scale) — accessible to colliders.

Key references:
  - foundations/dimensional_stack.md (D-depth ordering)
  - foundations/depth_running.md (D4 scale M_c ~ 3.37e14 GeV, two-scale model)
  - foundations/product_geometry.md (why DM cannot be a SM particle)
  - equations/depth_running.py (numerical depth scales)
  - phenomena/cosmology/dark_matter.md (DM rest mass ~35 keV estimate, M_c/m ratio)

Open problems:
  1. What topological condition stabilizes an intermediate closure?
  2. Is the D4->D5 transition a sharp threshold or a band?
  3. What is the DFC dark matter interaction cross-section with nucleons?
  4. Does the relic abundance match Omega_DM ~ 0.27 from the substrate budget?

PRIORITY: Medium (connects to cosmological observations)
"""

import math

# From two-scale depth model (equations/depth_running.py)
M_C_D4_GEV = 3.37e14   # GeV (D4 scale)
M_C_D5_GEV = 1.02e13   # GeV (D5 = electroweak closure)

# Ratio D5/D4 ~ 0.030 -- dark matter at intermediate depths would be heavier than SM
ratio_D5_D4 = M_C_D5_GEV / M_C_D4_GEV

if __name__ == "__main__":
    print("equations/dark_matter.py — STUB")
    print(f"  M_c(D4) = {M_C_D4_GEV:.3e} GeV  [D4 bifurcation/closure SCALE — not particle mass]")
    print(f"  M_c(D5) = {M_C_D5_GEV:.3e} GeV  [D5 = U(1) closure SCALE — not electron mass]")
    print(f"  M_c(D5) / M_c(D4) = {ratio_D5_D4:.4f}")
    print()
    print(f"  IMPORTANT: M_c values are the CLOSURE ENERGY SCALES (UV bifurcation scales),")
    print(f"  NOT the rest masses of DM particles. The electron has M_c(D5) ~ 10^13 GeV")
    print(f"  but rest mass = 0.511 MeV — ratio M_c/m_e ~ 2×10^19.")
    print(f"  Dark matter rest mass estimate: ~35 keV from depth-to-mass exponential")
    print(f"  (see phenomena/cosmology/dark_matter.md). The M_c → rest-mass connection")
    print(f"  is not yet formally derived in this module.")
    print()
    print("  Status: stability conditions, interaction cross-sections, relic abundance OPEN.")
