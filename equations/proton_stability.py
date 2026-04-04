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


# ─── Neutron lifetime consistency check ──────────────────────────────────────

def dfc_decay_classification():
    """
    Classify neutron vs. proton decay in DFC closure-topology terms.

    The key distinction between allowed and forbidden decays in the product
    geometry U(1) × SU(2) × SU(3):

        FORBIDDEN (cross-closure):
            Requires a carrier that couples across independent closure depths.
            Example: p → π⁰ + e⁺ requires d → e⁺ (color → lepton number),
            i.e., a carrier bridging D7 (SU(3)) to D5 (U(1)). No such carrier
            exists in a product group.

        ALLOWED (intra-closure):
            The carrier belongs entirely to one closure factor and the initial
            and final states are both charged under that same factor.
            Example: n → p + e⁻ + ν̄_e proceeds via W⁻ emission from the SU(2)
            closure at D6. All participants carry SU(2) quantum numbers.

    The neutron decay chain:
        d → u + W⁻        (SU(2) isospin transition — intra-D6)
        W⁻ → e⁻ + ν̄_e   (SU(2) lepton doublet — intra-D6)

    Every leg of this diagram couples only through the D6 SU(2) closure.
    No cross-closure transition is involved. DFC allows this decay exactly
    as the Standard Model does, with no correction.

    Returns
    -------
    dict with closure assignments and allowed/forbidden classification.
    """
    return {
        'reaction':             'n → p + e⁻ + ν̄_e',
        'quark_transition':     'd → u + W⁻',
        'w_boson_decay':        'W⁻ → e⁻ + ν̄_e',
        'closure_involved':     'SU(2) at D6 only',
        'cross_closure':        False,
        'classification':       'ALLOWED — intra-D6 SU(2) transition',
        'dfc_correction':       'None — DFC adds no modification to SM W-boson coupling at low energy',
        'contrast_with_proton': {
            'reaction':         'p → π⁰ + e⁺  (hypothetical)',
            'quark_transition': 'd → e⁺  (requires color → lepton number)',
            'closures_needed':  'D7 (SU(3)) → D5 (U(1)): cross-closure',
            'cross_closure':    True,
            'classification':   'FORBIDDEN — no carrier bridges independent closure depths',
        },
        'consistency_requirement': (
            'τ_neutron (DFC) = τ_neutron (SM). '
            'The DFC product group structure must reproduce the SM neutron lifetime '
            'exactly, with zero additional correction. Any discrepancy would indicate '
            'an error in the closure-depth assignment of SU(2).'
        ),
    }


def neutron_lifetime_treelevel(
    G_F=1.16638e-5,     # Fermi constant in GeV^-2
    V_ud=0.97373,       # CKM element
    g_A=1.2756,         # axial coupling
    m_n=0.93957,        # neutron mass in GeV
    m_p=0.93827,        # proton mass in GeV
    m_e=5.1100e-4,      # electron mass in GeV
    hbar_gev_s=6.5821e-25,  # ℏ in GeV·s
    n_steps=10000,
):
    """
    Tree-level neutron lifetime from β decay kinematics.

    The neutron decays via n → p + e⁻ + ν̄_e mediated by W-boson exchange.
    In the Fermi effective theory (W integrated out):

        Γ = G_F² |V_ud|² (1 + 3g_A²) / (2π³) × I_PS

    where I_PS is the phase-space integral over allowed electron energies:

        I_PS = ∫_{m_e}^{E_max} p_e × E_e × (E_max − E_e)² dE_e

        E_max = m_n − m_p        [endpoint energy, neglecting nucleon recoil]
        p_e   = √(E_e² − m_e²)  [electron momentum]
        (E_max − E_e) = neutrino energy (massless neutrino approximation)

    DFC prediction: τ_n (DFC) = τ_n (SM tree level). No DFC correction.

    Observed: τ_n = 879.4 ± 0.6 s (PDG 2022, beam method average).
    Tree-level SM prediction (no radiative corrections): τ_n ≈ 920–940 s.
    With radiative corrections (+RC ≈ 3.9%): τ_n ≈ 880 s  ✓

    Parameters
    ----------
    G_F : float
        Fermi constant (GeV⁻²).
    V_ud : float
        CKM element |V_ud|.
    g_A : float
        Neutron axial coupling g_A = G_A/G_V.
    m_n, m_p, m_e : float
        Neutron, proton, electron masses (GeV).
    hbar_gev_s : float
        ℏ in GeV·s (for converting Γ[GeV] → τ[s]).
    n_steps : int
        Integration steps for phase-space integral.

    Returns
    -------
    dict with lifetime prediction and DFC consistency check.
    """
    E_max = m_n - m_p   # endpoint energy (GeV); ≈ 1.293 MeV

    # Numerical integration: ∫ p_e E_e (E_max − E_e)² dE_e
    # from E_e = m_e to E_e = E_max
    dE = (E_max - m_e) / n_steps
    I_PS = 0.0
    for i in range(n_steps):
        E_e = m_e + (i + 0.5) * dE
        if E_e >= E_max:
            break
        p_e = math.sqrt(max(E_e**2 - m_e**2, 0.0))
        E_nu = E_max - E_e
        I_PS += p_e * E_e * E_nu**2 * dE

    # Decay rate (GeV, natural units)
    prefactor = G_F**2 * V_ud**2 * (1.0 + 3.0 * g_A**2) / (2.0 * math.pi**3)
    Gamma_gev = prefactor * I_PS

    # Lifetime
    tau_s_tree = hbar_gev_s / Gamma_gev

    # Radiative correction factor (from SM QED, ≈ +3.9%)
    # Including this brings tree-level into agreement with observation
    RC_factor  = 1.039
    tau_s_rc   = tau_s_tree / RC_factor   # RC increases rate, reduces lifetime

    tau_observed = 879.4   # seconds (PDG 2022)

    return {
        'E_max_mev':            E_max * 1000,
        'phase_space_integral': I_PS,
        'Gamma_gev':            Gamma_gev,
        'tau_tree_s':           tau_s_tree,
        'tau_tree_min':         tau_s_tree / 60,
        'tau_with_RC_s':        tau_s_rc,
        'tau_observed_s':       tau_observed,
        'tree_vs_obs_ratio':    tau_s_tree / tau_observed,
        'RC_corrected_ratio':   tau_s_rc / tau_observed,
        'dfc_correction':       0.0,
        'dfc_prediction_s':     tau_s_rc,  # DFC = SM (no extra correction)
        'within_5pct':          abs(tau_s_rc / tau_observed - 1.0) < 0.05,
        'closure_check': (
            'n → p + e⁻ + ν̄_e is a D6 SU(2) intra-closure decay. '
            'DFC product group adds zero correction to the SM W-boson coupling. '
            f'Predicted τ = {tau_s_rc:.1f} s  vs  observed τ = {tau_observed} s  '
            f'(ratio = {tau_s_rc/tau_observed:.4f})'
        ),
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
    print(f"  Safety margin:            10^{grav_result['lifetime_log10_y'] - 34:.0f} × experimental reach")
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

    print("\n" + "="*60)
    print("NEUTRON LIFETIME CONSISTENCY CHECK")
    print("="*60)
    cls = dfc_decay_classification()
    print(f"\nReaction: {cls['reaction']}")
    print(f"  Quark transition: {cls['quark_transition']}")
    print(f"  W-boson decay:    {cls['w_boson_decay']}")
    print(f"  Closure involved: {cls['closure_involved']}")
    print(f"  Cross-closure:    {cls['cross_closure']}")
    print(f"  Classification:   {cls['classification']}")
    cp = cls['contrast_with_proton']
    print(f"\nContrast — {cp['reaction']}")
    print(f"  Quark transition: {cp['quark_transition']}")
    print(f"  Closures needed:  {cp['closures_needed']}")
    print(f"  Classification:   {cp['classification']}")

    print()
    result = neutron_lifetime_treelevel()
    print(f"Tree-level lifetime:          τ_tree = {result['tau_tree_s']:.1f} s")
    print(f"After radiative correction:   τ_RC   = {result['tau_with_RC_s']:.1f} s")
    print(f"Observed:                     τ_obs  = {result['tau_observed_s']} s")
    print(f"Ratio τ_RC / τ_obs:           {result['RC_corrected_ratio']:.4f}")
    print(f"Within 5%:                    {result['within_5pct']}")
    print(f"DFC correction:               {result['dfc_correction']}")
    print(f"\n{result['closure_check']}")
    status = "✓ CONSISTENT" if result['within_5pct'] else "✗ DISCREPANCY"
    print(f"DFC prediction = SM prediction = {result['dfc_prediction_s']:.1f} s  [{status}]")
