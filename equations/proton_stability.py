"""
Proton stability analysis for the Dimensional Folding Model.

In the product geometry U(1) × SU(2) × SU(3), the proton is absolutely stable
to all gauge interactions. This module:

1. Demonstrates WHY there are no proton decay operators in the model
2. Computes the lower bound on proton lifetime from allowed (non-gauge) channels
3. Compares predictions to current experimental limits

Key result: The product geometry forbids gauge-mediated proton decay by construction.
The only allowed channels involve gravitational processes or exotic quantum tunneling,
both predicting τ_proton > 10^44 years — well beyond experimental reach.

Usage:
    python equations/proton_stability.py
"""

import math

# ─── Physical Constants ───────────────────────────────────────────────────────

M_PROTON_GEV   = 0.938272     # GeV
M_PLANCK_GEV   = 1.22e19      # GeV
HBAR_S         = 6.582e-25    # GeV·s (ℏ in natural units)
AGE_UNIVERSE   = 4.35e17      # seconds  (~13.8 billion years)
AGE_UNIVERSE_Y = 1.38e10      # years

# ─── Experimental Limits (Super-Kamiokande, 2020) ────────────────────────────

EXP_LIMITS = {
    'p_to_pi0_e+':       1.6e34,   # years  (dominant SU(5) mode)
    'p_to_pi+_nubar':    3.9e32,   # years
    'p_to_K+_nubar':     5.9e33,   # years  (dominant SUSY mode)
    'p_to_eta_e+':       1.0e34,   # years
    'p_to_rho0_e+':      1.0e34,   # years
}

# ─── Why Gauge-Mediated Decay is Forbidden ────────────────────────────────────

def explain_proton_stability():
    """
    Explain structurally why the product geometry forbids proton decay.

    In SU(5): There exist X and Y bosons (leptoquarks) with quantum numbers
    that allow quark → lepton transitions. These live in the coset SU(5) / (SU(3)×SU(2)×U(1)).

    In the product geometry: There IS no coset. The three fibers are separate.
    No gauge boson can have legs in both the SU(3) and SU(2) or U(1) fibers simultaneously.

    Returns a dictionary of the reasoning.
    """
    return {
        'product_gauge_group': 'U(1) × SU(2) × SU(3)',
        'x_y_bosons_exist': False,
        'reason': (
            "In a product gauge group, all gauge bosons are associated with "
            "one specific factor. A U(1) boson couples only to U(1) charges. "
            "An SU(3) gluon couples only to color charges. There is no boson "
            "that simultaneously couples to both color and lepton number, because "
            "such a boson would require a non-trivial representation of the product "
            "that mixes the two factors — which does not exist in a product group."
        ),
        'dimension_5_operators': (
            "Baryon-number-violating dimension-5 operators (QQQL, UUDE) require "
            "integrating out heavy leptoquarks. In the product geometry, the only "
            "heavy particles are KK modes, which are color singlets, SU(2) singlets, "
            "or U(1) singlets separately — never combinations. So even at dimension-5, "
            "the effective operators are absent to all perturbative orders."
        ),
        'conclusion': (
            "Proton decay through any gauge interaction is forbidden by the product "
            "group structure. This is not an approximate suppression — it is an exact "
            "structural zero at every order in perturbation theory."
        ),
    }


# ─── Gravitational Proton Decay ───────────────────────────────────────────────

def gravitational_decay_lifetime(m_proton_gev=M_PROTON_GEV, m_planck_gev=M_PLANCK_GEV):
    """
    Estimate proton lifetime from gravitational / Planck-suppressed operators.

    Even without X/Y bosons, gravity can mediate baryon-number violation through
    dimension-6 operators suppressed by M_Planck^-2:

        Γ ~ (m_proton^5) / (M_Planck^4)

    The proton lifetime:
        τ ~ M_Planck^4 / m_proton^5

    Parameters
    ----------
    m_proton_gev : float
        Proton mass in GeV.
    m_planck_gev : float
        Planck mass in GeV.

    Returns
    -------
    dict with lifetime estimate.
    """
    # Rate in natural units (GeV)
    gamma_natural = m_proton_gev**5 / m_planck_gev**4

    # Convert to seconds: τ[s] = ℏ / Γ[GeV]
    tau_seconds = HBAR_S / gamma_natural

    # Convert to years
    tau_years = tau_seconds / (3.156e7)   # seconds per year

    return {
        'm_proton_gev':     m_proton_gev,
        'm_planck_gev':     m_planck_gev,
        'decay_rate_gev':   gamma_natural,
        'lifetime_seconds': tau_seconds,
        'lifetime_years':   tau_years,
        'lifetime_log10_y': math.log10(tau_years),
        'comparison':       f"{tau_years:.1e} years  (exp limit: ~10^34 years)",
    }


# ─── Sphaleron-Mediated B Violation ──────────────────────────────────────────

def sphaleron_rate(temperature_gev, higgs_vev_gev=0.24622):
    """
    Sphaleron processes violate baryon + lepton number (B+L), but preserve B-L.
    They cannot cause proton decay (which requires ΔB = -1, ΔL = -1, so ΔB-ΔL = 0).
    But they are relevant at high temperatures.

    Sphaleron rate:
        Γ_sph / V ≈ (α_W T)^4 × exp(-E_sph / T)

    At T >> v (electroweak scale), E_sph / T → small and rate is unsuppressed.
    At T << v, rate is exponentially suppressed.

    Parameters
    ----------
    temperature_gev : float
        Temperature in GeV.
    higgs_vev_gev : float
        Higgs vev in GeV.

    Returns
    -------
    dict with sphaleron rate characteristics.
    """
    alpha_w = 0.0337    # SU(2) fine structure constant at m_Z

    # Sphaleron energy (electroweak scale)
    E_sph_gev = (8 * math.pi / math.sqrt(alpha_w)) * higgs_vev_gev / 2  # approximate

    if temperature_gev > higgs_vev_gev:
        # High T: rate is unsuppressed, B+L violation active
        suppression = 1.0
        status = "ACTIVE (B+L violation cosmologically relevant)"
    else:
        # Low T: exponentially suppressed
        suppression = math.exp(-E_sph_gev / temperature_gev)
        status = "FROZEN (exponentially suppressed)"

    return {
        'temperature_gev': temperature_gev,
        'sphaleron_energy_gev': E_sph_gev,
        'suppression_factor': suppression,
        'status': status,
        'note': "Sphalerons cannot cause proton decay (preserve B-L). "
                "Relevant only for baryogenesis.",
    }


# ─── Comparison to Experimental Bounds ───────────────────────────────────────

def compare_to_experiment():
    """
    Compare model predictions for proton stability to experimental bounds.

    Returns summary table.
    """
    grav_result = gravitational_decay_lifetime()

    print("=" * 70)
    print("PROTON STABILITY ANALYSIS")
    print("Dimensional Folding Model (Product Geometry)")
    print("=" * 70)

    print("\n--- Structural Argument: No Gauge-Mediated Decay ---")
    stability = explain_proton_stability()
    print(f"  Gauge group: {stability['product_gauge_group']}")
    print(f"  X,Y bosons exist: {stability['x_y_bosons_exist']}")
    print(f"  Conclusion: {stability['conclusion']}")

    print("\n--- Allowed Channel: Gravitational Operators ---")
    print(f"  Estimated τ_proton = {grav_result['lifetime_years']:.2e} years")
    print(f"  log10(τ) = {grav_result['lifetime_log10_y']:.1f}")

    print("\n--- Experimental Lower Bounds (Super-Kamiokande) ---")
    for channel, limit in EXP_LIMITS.items():
        arrow = channel.replace('_to_', ' → ').replace('_', ' ')
        print(f"  {arrow:25s}  τ > {limit:.1e} years")

    print("\n--- Summary ---")
    print(f"  Model prediction:         τ > 10^{grav_result['lifetime_log10_y']:.0f} years (gravitational)")
    print(f"  Best experimental limit:  τ > 10^34 years (Super-K, p → π⁰ e⁺)")
    print(f"  Safety margin:            10^{grav_result['lifetime_log10_y']:.0f - 34:.0f} × experimental reach")
    margin = grav_result['lifetime_log10_y'] - 34
    print(f"  Safety margin:            10^{margin:.0f} × above current limits")
    print()
    print("  NOTE: The model's prediction is not 'consistent with' the bound —")
    print("  the mechanism is STRUCTURALLY ABSENT. It's like asking whether a")
    print("  circle has corners: the question doesn't apply.")


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    compare_to_experiment()

    print("\n--- Sphaleron Activity at Various Temperatures ---")
    for T in [1000.0, 100.0, 10.0, 1.0, 0.1, 0.01]:
        s = sphaleron_rate(T)
        print(f"  T = {T:8.3f} GeV:  {s['status'][:40]}")
