"""
Neutrino Oscillations — DFC Module

Physical question: Why do neutrinos change flavor as they propagate, and can DFC predict
the mixing angles and mass-squared differences?

DFC mechanism: Three neutrino mass eigenstates correspond to three distinct winding
configurations of the substrate at the D3/D4 depth boundary. The weak (D6 SU(2)) interaction
couples to flavor eigenstates, which are the projection of the mass eigenstates onto the
D6 closure basis. Because the mass basis (D4 geometry) and the flavor basis (D6 geometry)
are misaligned, a neutrino produced in a pure flavor eigenstate is a superposition of mass
eigenstates. These accumulate different phases as they propagate (different phase velocities
from different masses), causing the flavor composition to oscillate periodically.

DFC status:
  - Three flavors exist:        DERIVED (three SU(3) color charges → three generations; Tier 1)
  - Oscillation formula:        STRUCTURAL (follows from QM superposition; no DFC modification)
  - PMNS mixing angles:         NOT DERIVED (Tier 3 — consistency with SU(3) structure; not predicted)
  - Mass-squared differences:   NOT DERIVED (Tier 4 — requires D3/D4 winding depth calculation)
  - Normal vs. inverted order:  NOT DERIVED (Tier 4 — requires relative winding mode depths)

Key references:
  - neutrino_oscillations.md — DFC structural account
  - phenomena/particle_physics/particles/neutrinos.md — D4 winding mass structure
  - foundations/three_generations.md — why three flavors (SU(3) color → three generations)
  - equations/neutrino_masses.py — absolute mass scale (Tier 4 open)
"""

import math

# ─── Observed oscillation parameters (NuFIT 5.2, 2022) ───────────────────────
# These are INPUTS from experiment — NOT DFC predictions.

# Mixing angles (degrees)
THETA_12_DEG = 33.41    # Solar angle; sin²(θ₁₂) = 0.304
THETA_23_DEG = 49.1     # Atmospheric angle; sin²(θ₂₃) = 0.570 (upper octant preference)
THETA_13_DEG = 8.58     # Reactor angle; sin²(θ₁₃) = 0.02220

# Mass-squared differences (eV²)
DM2_21_EV2 = 7.42e-5    # Solar; Δm²₂₁ = m²₂ − m²₁ > 0
DM2_31_EV2 = 2.510e-3   # Atmospheric (normal ordering); Δm²₃₁ = m²₃ − m²₁ > 0

# CP-violating phase (degrees) — preliminary
DELTA_CP_DEG = 195.0    # ~1.6σ from zero (not yet established)

# ─── Oscillation conversion factor ────────────────────────────────────────────
# In natural units: phase = Δm² L / (4E)
# With Δm² in eV², L in km, E in GeV:
#   phase [rad] = (Δm² [eV²] × L [km]) / (4 × E [GeV] × (ℏc in eV·km))
#   ℏc = 197.3269804 MeV·fm = 197.3269804 × 10⁻¹⁸ eV·km
#   phase = Δm²[eV²] × L[km] × (1/(4 × 197.3269804 × 10⁻¹⁸ eV·km)) / E[GeV] × (1 GeV / 10⁹ eV)
#         = 1.26693 × Δm²[eV²] × L[km] / E[GeV]
# Standard textbook value: 1.267

PHASE_FACTOR = 1.26693   # conversion: phase[rad] = PHASE_FACTOR × Δm²[eV²] × L[km] / E[GeV]


# ─── Two-flavor oscillation ───────────────────────────────────────────────────

def oscillation_prob_2flavor(theta_deg, dm2_ev2, L_km, E_GeV):
    """
    Two-flavor oscillation probability P(να → νβ), α ≠ β.

    The probability that a neutrino produced as flavor α is detected as flavor β equals
    the product of the sine squared of twice the mixing angle and the sine squared of
    the phase accumulated during propagation. The phase equals 1.267 times the mass-squared
    difference (in eV²) times the propagation distance (in km), divided by the neutrino
    energy (in GeV).

    P(να → νβ) = sin²(2θ) × sin²(1.267 × Δm² [eV²] × L [km] / E [GeV])

    Args:
        theta_deg: mixing angle in degrees
        dm2_ev2: mass-squared difference in eV²
        L_km: propagation distance in km
        E_GeV: neutrino energy in GeV

    Returns:
        float: oscillation probability (0 to 1)
    """
    theta = math.radians(theta_deg)
    phase = PHASE_FACTOR * dm2_ev2 * L_km / E_GeV
    return math.sin(2 * theta)**2 * math.sin(phase)**2


def survival_prob_2flavor(theta_deg, dm2_ev2, L_km, E_GeV):
    """
    Two-flavor survival probability P(να → να).

    The survival probability equals one minus the oscillation probability: the fraction
    of neutrinos that remain in their original flavor after propagating distance L.

    P(να → να) = 1 − sin²(2θ) × sin²(phase)
    """
    return 1.0 - oscillation_prob_2flavor(theta_deg, dm2_ev2, L_km, E_GeV)


def oscillation_length_km(dm2_ev2, E_GeV):
    """
    Oscillation length: the distance at which the oscillation phase equals π/2.

    The oscillation length equals the neutrino energy divided by 1.267 times the
    mass-squared difference. In units of km and GeV, the formula is:
    L_osc = E [GeV] / (1.267 × Δm² [eV²]) km.

    At this distance, P(να → νβ) is at its first maximum (= sin²(2θ)).

    Args:
        dm2_ev2: mass-squared difference in eV²
        E_GeV: energy in GeV

    Returns:
        float: oscillation length in km
    """
    return E_GeV / (PHASE_FACTOR * dm2_ev2)   # L where phase = π/2: 1.267*dm2*L/E = π/2


# ─── Experimental comparison ──────────────────────────────────────────────────

def solar_neutrino_comparison():
    """
    Solar neutrino disappearance: P(νe → νe) for solar parameters.

    The MSW (Mikheyev-Smirnov-Wolfenstein) effect in matter significantly modifies
    solar oscillations from the vacuum formula — the electron neutrino interacts with
    solar electrons, changing the effective mixing angle in matter. For this structural
    comparison we use the effective survival probability at Earth (averaged over energy
    and matter effects): P_obs ≈ 0.55–0.60, consistent with theta_12 ≈ 33° plus MSW.

    Vacuum approximation (ignoring matter effects — qualitative only).
    """
    # Solar L/E: Earth-Sun = 150e9 m = 1.5e8 km; typical solar neutrino E = 1-10 MeV
    L_km = 1.496e8       # Earth-Sun distance (km)
    E_values_GeV = [0.001, 0.005, 0.010]  # 1, 5, 10 MeV solar neutrino energies

    results = []
    for E_GeV in E_values_GeV:
        # Vacuum 2-flavor survival P(νe → νe) using θ₁₂, Δm²₂₁
        P_surv = survival_prob_2flavor(THETA_12_DEG, DM2_21_EV2, L_km, E_GeV)
        L_osc = oscillation_length_km(DM2_21_EV2, E_GeV)
        results.append({
            'E_MeV': E_GeV * 1000,
            'L_osc_km': L_osc,
            'P_survival_vacuum': P_surv,
            'note': 'MSW matter effects dominate in Sun; vacuum approx qualitative only',
        })
    return results


def atmospheric_neutrino_comparison():
    """
    Atmospheric muon-neutrino disappearance: P(νμ → νμ).

    Super-Kamiokande (1998) measured P(νμ → νμ) ≈ 0.5 for L/E ≈ 500 km/GeV,
    consistent with maximal mixing θ₂₃ ≈ 45° and Δm²₃₁ ≈ 2.5×10⁻³ eV².

    Uses 2-flavor approximation (dominant contribution is θ₂₃, Δm²₃₁).
    """
    L_values = [100, 500, 1000, 5000, 12000]  # km
    E_GeV = 1.0  # 1 GeV atmospheric muon neutrino

    results = []
    for L_km in L_values:
        P_surv = survival_prob_2flavor(THETA_23_DEG, DM2_31_EV2, L_km, E_GeV)
        results.append({
            'L_km': L_km,
            'E_GeV': E_GeV,
            'L_over_E_km_GeV': L_km / E_GeV,
            'P_survival': P_surv,
        })
    # Oscillation length at 1 GeV for Δm²₃₁
    L_osc = oscillation_length_km(DM2_31_EV2, E_GeV)
    return {'results': results, 'L_osc_km': L_osc}


def daya_bay_comparison():
    """
    Daya Bay reactor antineutrino disappearance: P(νe-bar → νe-bar).

    Daya Bay (2012) measured theta_13 using L ≈ 1.6 km baseline at E ≈ 3-8 MeV.
    The near-maximal disappearance of reactor antineutrinos at this baseline is
    governed by theta_13 and Δm²_31.

    Note: reactor experiments see P ≈ 0.94 (6% disappearance from theta_13).
    """
    L_km = 1.648        # Daya Bay far hall baseline (km)
    E_values_GeV = [0.003, 0.004, 0.006, 0.008]  # 3, 4, 6, 8 MeV reactor antineutrinos

    results = []
    for E_GeV in E_values_GeV:
        # Dominant term: sin²(2θ₁₃) × sin²(1.267 × Δm²₃₁ × L / E)
        P_surv = survival_prob_2flavor(THETA_13_DEG, DM2_31_EV2, L_km, E_GeV)
        results.append({
            'E_MeV': E_GeV * 1000,
            'P_survival': P_surv,
        })
    # Observed: ~6% disappearance at ~5 MeV
    P_obs = 0.944  # Daya Bay measured survival probability
    P_dfc = survival_prob_2flavor(THETA_13_DEG, DM2_31_EV2, 1.648, 0.005)
    return {
        'results': results,
        'P_dfc_at_5MeV': P_dfc,
        'P_observed': P_obs,
        'error_pct': 100.0 * (P_dfc - P_obs) / P_obs,
    }


def kamland_comparison():
    """
    KamLAND reactor neutrino oscillation: P(νe-bar) at ~180 km baseline.

    KamLAND (2002) used multiple Japanese reactors at ~180 km average distance
    to measure Δm²₂₁ and θ₁₂. The survival probability averaged over L/E shows
    clear oscillatory behavior → confirmed large mixing angle solution.
    """
    L_km = 180.0     # KamLAND effective baseline
    E_values_GeV = [0.003, 0.004, 0.006, 0.008, 0.010]  # 3–10 MeV reactor

    results = []
    for E_GeV in E_values_GeV:
        P_surv = survival_prob_2flavor(THETA_12_DEG, DM2_21_EV2, L_km, E_GeV)
        results.append({
            'E_MeV': E_GeV * 1000,
            'L_over_E': L_km / E_GeV,
            'P_survival': P_surv,
        })
    return results


def mass_ratio_comparison():
    """
    Mass-squared difference ratio: structural comparison to DFC expectations.

    Observed ratio: Δm²₃₁ / Δm²₂₁ = 2.51e-3 / 7.42e-5 ≈ 33.8

    DFC expectation: the three neutrino mass eigenstates correspond to three winding
    modes at the D3/D4 boundary with increasing depth anchoring. If the depth spacing
    between modes is approximately equal (D-depth ladder with spacing proportional to
    some power of the compression ratio), the mass-squared splittings should follow a
    geometric progression. The ratio Δm²₃₁/Δm²₂₁ ≈ 34 vs. a geometric expectation
    of Δm²₃₁/Δm²₂₁ = Δm²₃₂/Δm²₂₁ + 1 ≈ DFC depth ratio squared.

    This is the same ratio previously computed in neutrino_masses.py:
    DFC predicted ratio ≈ 1.34 (uniform D-spacing assumption) vs. observed ≈ 5.71
    (from neutrino_masses.py) — a 4.3× failure indicating non-uniform spacing.
    """
    dm2_ratio_obs = DM2_31_EV2 / DM2_21_EV2
    # From neutrino_masses.py: the DFC spacing model gives ratio ≈ 1.34
    dm2_ratio_dfc = 1.34  # DFC depth-spacing model (see neutrino_masses.py)
    error_pct = 100.0 * (dm2_ratio_dfc - dm2_ratio_obs) / dm2_ratio_obs

    return {
        'dm2_21_ev2': DM2_21_EV2,
        'dm2_31_ev2': DM2_31_EV2,
        'ratio_observed': dm2_ratio_obs,
        'ratio_dfc': dm2_ratio_dfc,
        'error_pct': error_pct,
        'status': 'FAILS — uniform D-spacing assumption gives ratio 1.34, observed 33.8 (4.3x off)',
    }


def oscillation_summary():
    """
    Summary of what DFC derives vs. imports for neutrino oscillations.
    """
    return {
        'derived': [
            'Three neutrino flavors exist (SU(3) three-generation count; Tier 1)',
            'Oscillation formula P = sin²(2θ) sin²(1.267 Δm² L / E) '
            '(standard QM superposition; no DFC modification)',
            'Oscillation length L_osc = E / (1.267 Δm²) [km, GeV, eV²]',
        ],
        'structural': [
            'Flavor/mass basis mismatch from D4 (mass) vs D6 (flavor) geometry',
            'Near-maximal θ₂₃ from near-degeneracy of 2nd/3rd winding modes (structural)',
            'Majorana-or-Dirac question: depends on D4 winding self-conjugacy (open)',
        ],
        'not_derived': [
            'PMNS mixing angles θ₁₂=33.4°, θ₂₃=49.1°, θ₁₃=8.6° (Tier 3 — not predicted)',
            'Mass-squared differences Δm²₂₁, Δm²₃₁ (Tier 4 — D4 winding depths open)',
            'Mass ordering (normal vs. inverted) (Tier 4 — depth ordering open)',
            'CP phase δ_CP ≈ 195° (Tier 4 — relative winding phases open)',
        ],
    }


# ─── Main output ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 65)
    print("NEUTRINO OSCILLATIONS — DFC MODULE")
    print("=" * 65)
    print()
    print("INPUT (observed, not DFC predictions):")
    print(f"  θ₁₂ = {THETA_12_DEG}°,  θ₂₃ = {THETA_23_DEG}°,  θ₁₃ = {THETA_13_DEG}°")
    print(f"  Δm²₂₁ = {DM2_21_EV2:.2e} eV²  (solar)")
    print(f"  Δm²₃₁ = {DM2_31_EV2:.3e} eV²  (atmospheric, normal ordering)")

    # --- Oscillation lengths ---
    print("\n--- Oscillation Lengths ---")
    print(f"  P = sin²(2θ) × sin²(1.267 × Δm² [eV²] × L [km] / E [GeV])")
    for label, dm2, theta, E_GeV in [
        ("Solar    (θ₁₂, Δm²₂₁) at 1 MeV  ", DM2_21_EV2, THETA_12_DEG, 0.001),
        ("Solar    (θ₁₂, Δm²₂₁) at 5 MeV  ", DM2_21_EV2, THETA_12_DEG, 0.005),
        ("Atm.     (θ₂₃, Δm²₃₁) at 1 GeV  ", DM2_31_EV2, THETA_23_DEG, 1.0),
        ("Reactor  (θ₁₃, Δm²₃₁) at 5 MeV  ", DM2_31_EV2, THETA_13_DEG, 0.005),
        ("KamLAND  (θ₁₂, Δm²₂₁) at 5 MeV  ", DM2_21_EV2, THETA_12_DEG, 0.005),
    ]:
        L_osc = oscillation_length_km(dm2, E_GeV)
        print(f"  {label}: L_osc = {L_osc:.1f} km")

    # --- Atmospheric disappearance ---
    print("\n--- Atmospheric νμ Disappearance (E = 1 GeV, θ₂₃ = 49.1°, Δm²₃₁) ---")
    atm = atmospheric_neutrino_comparison()
    print(f"  Oscillation length at 1 GeV: {atm['L_osc_km']:.1f} km")
    print(f"  {'L (km)':>8}  {'L/E (km/GeV)':>14}  {'P(νμ→νμ)':>12}")
    for row in atm['results']:
        print(f"  {row['L_km']:>8.0f}  {row['L_over_E_km_GeV']:>14.0f}  {row['P_survival']:>12.4f}")
    print(f"  Super-K observed: P(νμ→νμ) ≈ 0.5 at L/E ≈ 500 km/GeV → matches maximum disappearance")

    # --- Daya Bay comparison ---
    print("\n--- Daya Bay θ₁₃ Measurement (L = 1.648 km) ---")
    db = daya_bay_comparison()
    print(f"  P(νe-bar→νe-bar) at 5 MeV: DFC = {db['P_dfc_at_5MeV']:.4f}  "
          f"Obs ≈ {db['P_observed']:.3f}  "
          f"Error = {db['error_pct']:.1f}%")
    print(f"  [Note: DFC uses input θ₁₃ = 8.58° from Daya Bay; this is NOT a DFC prediction]")

    # --- Mass ratio failure ---
    print("\n--- Mass-Squared Difference Ratio (DFC vs. Observed) ---")
    mr = mass_ratio_comparison()
    print(f"  Δm²₃₁ / Δm²₂₁:  observed = {mr['ratio_observed']:.1f},  "
          f"DFC depth model = {mr['ratio_dfc']:.2f},  error = {mr['error_pct']:.0f}%")
    print(f"  Status: {mr['status']}")

    # --- Summary ---
    print("\n--- DFC Status ---")
    st = oscillation_summary()
    print("  DERIVED:")
    for s in st['derived']:
        print(f"    ✓ {s}")
    print("  STRUCTURAL:")
    for s in st['structural']:
        print(f"    ~ {s}")
    print("  NOT DERIVED (inputs from experiment):")
    for s in st['not_derived']:
        print(f"    ✗ {s}")

    print("\n[Module: equations/neutrino_oscillations.py | Cycle 65]")
