"""
Entropy production from folding pathway multiplication.

In the Dimensional Folding Model, entropy is not an abstract bookkeeping quantity —
it is the count of accessible folding configurations compatible with macroscopic
constraints. Entropy increases because compression events irreversibly multiply the
number of available folding pathways.

Core identification:
    S = k_B × ln(Ω_fold)

where Ω_fold = number of distinct folding configurations accessible to the system
given its macroscopic state (energy, volume, compression budget).

The second law is not assumed here — it is derived:
    dΩ_fold/dt ≥ 0  always

because each compression event either:
  (a) eliminates some closures (reducing local Ω) but disperses compression
      into more distributed pathways (increasing global Ω by more), or
  (b) creates new folding pathways directly through buckling events.

The arrow of time is the direction in which Ω_fold increases.
Time's past is the configuration with fewer accessible folding paths.
Time's future is the configuration with more.

This module contains:
  - Folding entropy formula
  - Entropy production rate from compression field dynamics
  - Connection to thermodynamic quantities (temperature, heat, work)
  - The arrow of time as a derived quantity
  - Fluctuation theorem analogues (Jarzynski, Crooks) in folding language

STATUS: The qualitative derivation is complete (see phenomena/thermodynamics/thermodynamics.md).
The quantitative connection between Ω_fold and the compression field parameters
is an open problem — specifically, how to count folding configurations from φ(x,t).

Usage:
    python equations/entropy_production.py
"""

import math

# ── Physical constants ────────────────────────────────────────────────────────

K_BOLTZMANN = 1.380649e-23   # J/K
K_BOLTZMANN_EV = 8.617333e-5  # eV/K


# ── Folding entropy ───────────────────────────────────────────────────────────

def folding_entropy(omega_fold, k_b=K_BOLTZMANN):
    """
    Boltzmann entropy from folding configuration count.

        S = k_B × ln(Ω_fold)

    In this model, Ω_fold counts the number of distinct compression field
    configurations φ(x) that are macroscopically indistinguishable (same
    total energy, same volume, same coarse-grained structure).

    This is identical in form to Boltzmann entropy, but the microstate count
    has a specific physical interpretation: it is the number of ways the
    compression field can be arranged at the microscopic (sub-kink-width) scale
    while producing the same macroscopic folding pattern.

    Parameters
    ----------
    omega_fold : float
        Number of accessible folding configurations (dimensionless, ≥ 1).
    k_b : float
        Boltzmann constant.

    Returns
    -------
    float : entropy in J/K.
    """
    if omega_fold <= 0:
        return 0.0
    return k_b * math.log(omega_fold)


def configuration_count_from_field(
    n_sites,
    phi_values_per_site,
    constraint_fraction=1.0,
):
    """
    Estimate the number of accessible folding configurations for a lattice of
    compression field sites.

    For a system of N sites, each with M available field values (discretized),
    the unconstrained count is M^N. Macroscopic constraints reduce this:

        Ω_fold = (φ_values_per_site)^N × constraint_fraction

    In a more refined model, constraint_fraction is determined by the conservation
    laws (compression budget, total kink number) and the folding pathway topology.

    Parameters
    ----------
    n_sites : int
        Number of independent degrees of freedom (lattice sites, modes, etc.).
    phi_values_per_site : int
        Number of distinct compression field values per site (discretization of φ).
    constraint_fraction : float
        Fraction of configurations compatible with macroscopic constraints (0–1].

    Returns
    -------
    dict with entropy estimate.
    """
    omega_unconstrained = phi_values_per_site ** n_sites
    omega_constrained   = omega_unconstrained * constraint_fraction

    # Use Stirling-style approximation for log
    S_unconstrained = K_BOLTZMANN * n_sites * math.log(phi_values_per_site)
    S_constrained   = S_unconstrained + K_BOLTZMANN * math.log(constraint_fraction) if constraint_fraction > 0 else 0.0

    return {
        'n_sites':              n_sites,
        'phi_values_per_site':  phi_values_per_site,
        'omega_unconstrained':  omega_unconstrained,
        'omega_constrained':    omega_constrained,
        'S_unconstrained_j_k':  S_unconstrained,
        'S_constrained_j_k':    S_constrained,
        'S_per_site':           K_BOLTZMANN * math.log(phi_values_per_site),
    }


# ── Temperature from compression agitation ───────────────────────────────────

def temperature_from_compression_rate(dphi_dt_rms, m_eff, k_b=K_BOLTZMANN):
    """
    Temperature as compression agitation density.

    In the DFC model, temperature measures the local rate and density of
    accelerated dimensional compression — how vigorously the field is
    attempting to align downward without successfully closing.

    The connection to standard thermodynamics:
        ½ m_eff <(∂φ/∂t)²> = ½ k_B T   (equipartition theorem)
        → T = m_eff × <(∂φ/∂t)²> / k_B

    This identifies temperature with the mean kinetic energy of compression
    field fluctuations around the stable minimum.

    Parameters
    ----------
    dphi_dt_rms : float
        RMS value of ∂φ/∂t (compression agitation rate).
    m_eff : float
        Effective mass of the compression mode (from V''(φ_stable)).

    Returns
    -------
    float : temperature in Kelvin.
    """
    return m_eff * dphi_dt_rms**2 / k_b


def compression_rate_from_temperature(T_kelvin, m_eff, k_b=K_BOLTZMANN):
    """
    Inverse of temperature_from_compression_rate.
    RMS compression rate from temperature.
    """
    return math.sqrt(k_b * T_kelvin / m_eff)


# ── Entropy production rate ───────────────────────────────────────────────────

def entropy_production_rate(
    compression_inflow,
    temperature_local,
    temperature_environment,
    k_b=K_BOLTZMANN,
):
    """
    Rate of entropy production from compression flow.

    When compression flows from a high-agitation region (hot) to a low-agitation
    region (cold), entropy is produced at a rate:

        dS/dt = P_compression × (1/T_cold - 1/T_hot) ≥ 0

    where P_compression is the power (rate of compression energy transfer).

    This is the DFC interpretation of the Clausius inequality, derived from the
    fact that compression flowing into a lower-density region creates more
    accessible folding pathways than it removes from the higher-density region.

    Parameters
    ----------
    compression_inflow : float
        Rate of compression energy flowing into the cold region (J/s or natural units).
    temperature_local : float
        Temperature of the receiving region (K).
    temperature_environment : float
        Temperature of the source region (K).

    Returns
    -------
    dict with entropy production rate and second-law check.
    """
    if temperature_local <= 0 or temperature_environment <= 0:
        return {'error': 'Temperatures must be positive'}

    dS_dt = compression_inflow * (1.0/temperature_local - 1.0/temperature_environment)
    second_law_satisfied = dS_dt >= 0

    return {
        'dS_dt':                dS_dt,
        'second_law_satisfied': second_law_satisfied,
        'sign_interpretation': (
            'Positive: entropy produced (compression flows hot→cold). '
            'Negative: would require compression to flow cold→hot — forbidden.'
        ),
    }


# ── Arrow of time ─────────────────────────────────────────────────────────────

def arrow_of_time_metric(omega_initial, omega_final):
    """
    The arrow of time as the direction of increasing folding configuration count.

    'Past' is defined as the state with fewer accessible folding configurations.
    'Future' is defined as the state with more accessible folding configurations.

    This gives time a physical, derived direction without requiring time to be
    fundamental. The arrow of time is not a property of the time coordinate —
    it is a property of the compression process.

    Parameters
    ----------
    omega_initial : float
        Configuration count at the earlier state.
    omega_final : float
        Configuration count at the later state.

    Returns
    -------
    dict with arrow of time determination.
    """
    delta_S = K_BOLTZMANN * math.log(omega_final / omega_initial)
    forward = omega_final >= omega_initial

    return {
        'omega_initial':        omega_initial,
        'omega_final':          omega_final,
        'delta_S_j_k':          delta_S,
        'time_direction':       'forward' if forward else 'backward (forbidden)',
        'second_law_satisfied': forward,
        'interpretation': (
            'The second law is not a postulate. It is the statement that the '
            'compression process has no global mechanism to re-align escaped '
            'compression without producing more distributed compression. '
            'Ω_fold is monotonically non-decreasing.'
        ),
    }


# ── Carnot efficiency in folding language ─────────────────────────────────────

def carnot_efficiency_folding(T_hot, T_cold):
    """
    Carnot efficiency as a statement about compression density ratio.

    In DFC: temperature measures compression agitation density.
    The Carnot efficiency is the maximum fraction of incoherent compression
    that can be forced into coherent output (work) given two compression
    reservoirs at different agitation densities.

        η = 1 - T_cold/T_hot = 1 - (agitation density, cold) / (agitation density, hot)

    This is not a statement about idealized reversible engines. It is a statement
    about the maximum coherence recoverable from two compression densities —
    a geometric property of the folding pathway landscape.

    The Carnot limit is sharp because:
      - Extracting work requires imposing alignment constraints on compression
      - Constraints inevitably reject some compression as heat
      - The fraction that must be rejected equals T_cold/T_hot (pathway geometry)

    Parameters
    ----------
    T_hot : float
        Temperature of hot reservoir (K) — high compression agitation density.
    T_cold : float
        Temperature of cold reservoir (K) — low compression agitation density.

    Returns
    -------
    dict with efficiency and folding interpretation.
    """
    eta = 1.0 - T_cold / T_hot
    rejected_fraction = T_cold / T_hot

    return {
        'T_hot':                T_hot,
        'T_cold':               T_cold,
        'carnot_efficiency':    eta,
        'rejected_fraction':    rejected_fraction,
        'interpretation': (
            f'{eta*100:.1f}% of compression can be forced into coherent output. '
            f'{rejected_fraction*100:.1f}% must be rejected as incoherent heat — '
            f'this is the pathway geometry minimum, not an engineering limitation.'
        ),
    }


# ── Fluctuation theorem analogue ──────────────────────────────────────────────

def jarzynski_folding_analogue(work_values, T_kelvin, k_b=K_BOLTZMANN):
    """
    Jarzynski equality analogue in folding language.

    The Jarzynski equality:
        <exp(-W/k_BT)> = exp(-ΔF/k_BT)

    connects the average of exp(-W/k_BT) over non-equilibrium work measurements
    to the equilibrium free energy difference ΔF.

    In DFC: W is the work done against compression gradients during a
    reconfiguration; ΔF is the difference in free compression budget between
    initial and final folding states.

    The equality holds because the folding process is microscopically reversible
    (the field equation is time-reversible) even though macroscopic compression
    produces irreversible entropy. The Jarzynski equality is the precise statement
    of how microscopic reversibility and macroscopic irreversibility coexist.

    Parameters
    ----------
    work_values : list of float
        Sample of work measurements W_i (in Joules or natural units).
    T_kelvin : float
        Temperature of the system (K).

    Returns
    -------
    dict with Jarzynski estimate of free energy difference.
    """
    beta = 1.0 / (k_b * T_kelvin)
    exp_terms = [math.exp(-beta * w) for w in work_values]
    mean_exp  = sum(exp_terms) / len(exp_terms)

    delta_F = -math.log(mean_exp) / beta

    return {
        'n_samples':    len(work_values),
        'mean_work':    sum(work_values) / len(work_values),
        'mean_exp_neg_betaW': mean_exp,
        'delta_F_estimate':  delta_F,
        'note': ('Jarzynski estimate of free compression budget difference ΔF. '
                 'Valid for any protocol connecting initial to final folding state.'),
    }


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("ENTROPY PRODUCTION — FOLDING PATHWAY MULTIPLICATION")
    print("Dimensional Folding Model")
    print("=" * 65)

    print(f"\n--- Entropy from Configuration Count ---")
    cfg = configuration_count_from_field(n_sites=100, phi_values_per_site=10,
                                          constraint_fraction=0.1)
    print(f"  N sites:          {cfg['n_sites']}")
    print(f"  φ values/site:    {cfg['phi_values_per_site']}")
    print(f"  Ω (constrained):  {cfg['omega_constrained']:.3e}")
    print(f"  S (constrained):  {cfg['S_constrained_j_k']:.4e} J/K")
    print(f"  S per site:       {cfg['S_per_site']:.4e} J/K")

    print(f"\n--- Carnot Efficiency in Folding Language ---")
    for T_hot, T_cold in [(600, 300), (1000, 300), (500, 450)]:
        carnot = carnot_efficiency_folding(T_hot, T_cold)
        print(f"  T_hot={T_hot}K, T_cold={T_cold}K:  "
              f"η = {carnot['carnot_efficiency']:.3f}  ({carnot['carnot_efficiency']*100:.1f}%)")

    print(f"\n--- Arrow of Time ---")
    aot = arrow_of_time_metric(omega_initial=1e10, omega_final=1e12)
    print(f"  Ω_initial:  {aot['omega_initial']:.2e}")
    print(f"  Ω_final:    {aot['omega_final']:.2e}")
    print(f"  ΔS:         {aot['delta_S_j_k']:.4e} J/K")
    print(f"  Direction:  {aot['time_direction']}")

    print(f"\n--- Entropy Production Rate ---")
    rate = entropy_production_rate(compression_inflow=100.0,
                                    temperature_local=300.0,
                                    temperature_environment=600.0)
    print(f"  dS/dt: {rate['dS_dt']:.4e} J/(K·s)")
    print(f"  Second law satisfied: {rate['second_law_satisfied']}")

    print(f"\n--- Open Problems ---")
    print(f"  1. Count folding configurations directly from φ(x,t) field")
    print(f"  2. Derive Ω_fold(E, V, N) from compression field theory")
    print(f"  3. Derive Carnot limit from folding geometry without assuming T")
    print(f"  4. Formalize Jarzynski analogue for compression field reconfigurations")
    print(f"  5. Connect to Bekenstein bound: S ≤ 2πRE/ℏc")
    print(f"  See: phenomena/thermodynamics/thermodynamics.md")
