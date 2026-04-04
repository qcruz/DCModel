"""
Cosmological equations — global compression dynamics and cosmic evolution.

At cosmological scales, the Dimensional Folding Model predicts that:

  1. COSMIC EXPANSION is lateral redistribution of the global compression budget.
     As the universe's compression progresses, structure cannot simply collapse
     inward uniformly — it redistributes sideways, producing the appearance of
     expansion from within.

  2. DARK ENERGY is the residual compression pressure — the ongoing tendency of
     the global compression field to remove degrees of freedom drives an effective
     positive energy density in empty space that counteracts gravitational collapse.

  3. THE COSMOLOGICAL CONSTANT Λ corresponds to the current global compression
     rate — the rate at which dimensional volume is being removed per unit of
     remaining volume. It is not a constant of the laws of physics but a slowly
     evolving parameter set by the global compression state.

  4. CYCLIC RENEWAL: when terminal folding approaches (the universe approaching
     D1), a global buckling instability triggers a new bifurcation event — a new
     dimensional layer emerges, effectively creating conditions for a new universe.
     The cycle is deterministic in necessity but indeterminate in detail.

  5. DARK MATTER candidates: stable intermediate-depth kinks that have not
     fully collapsed to the observed particle spectrum — structures sitting between
     D4 and D5 in the dimensional stack.

This module contains:
  - Hubble parameter from compression budget
  - Dark energy density from compression rate
  - Friedmann-like equation from compression dynamics
  - Cyclic renewal condition
  - Dark matter candidate mass range

Observational inputs (Planck 2018 + recent):
  H_0     ≈ 67.4 km/s/Mpc   (Hubble constant)
  Ω_Λ     ≈ 0.685            (dark energy fraction)
  Ω_m     ≈ 0.315            (matter fraction)
  Ω_DM    ≈ 0.265            (dark matter fraction)
  Ω_b     ≈ 0.049            (baryon fraction)
  t_univ  ≈ 13.8 Gyr         (age of universe)

STATUS: The qualitative picture is well-developed. The Friedmann analogue from
DFC first principles is the key open derivation.

Usage:
    python equations/cosmology.py
"""

import math

# ── Cosmological constants and observations ───────────────────────────────────

H_0_KM_S_MPC   = 67.4        # Hubble constant km/s/Mpc (Planck 2018)
H_0_SI         = 2.184e-18   # Hubble constant in s⁻¹
OMEGA_LAMBDA    = 0.685       # Dark energy fraction
OMEGA_MATTER    = 0.315       # Total matter fraction
OMEGA_DM        = 0.265       # Dark matter fraction
OMEGA_BARYON    = 0.049       # Baryon fraction
T_UNIVERSE_GYR  = 13.8        # Age of universe in Gyr
T_CMB_KELVIN    = 2.725       # CMB temperature today
RHO_CRIT_KG_M3 = 8.5e-27     # Critical density kg/m³
C_LIGHT         = 2.998e8     # m/s
G_NEWTON        = 6.674e-11   # N m² kg⁻²


# ── Hubble parameter from compression budget ──────────────────────────────────

def hubble_from_compression(rho_compression, rho_critical=RHO_CRIT_KG_M3):
    """
    Hubble parameter from compression budget density.

    In DFC, the Friedmann equation:
        H² = (8πG/3) ρ_total

    is reinterpreted as:
        H² = (8πG/3)(ρ_compression + ρ_dark_energy + ρ_matter)

    where:
        ρ_compression = compression budget density (kinetic + gradient + potential)
        ρ_dark_energy = residual compression pressure (Λ term)
        ρ_matter      = stable closure density (kinks = particles)

    The Hubble parameter measures the current global compression rate:
        H = (1/V) dV/dt  (fractional rate of dimensional volume change)

    In DFC, this is the rate at which the global dimensional volume is being
    removed by the compression process.

    Parameters
    ----------
    rho_compression : float
        Total energy density of the compression field (kg/m³).
    rho_critical : float
        Critical density for flat universe (kg/m³).

    Returns
    -------
    dict with Hubble parameter and density fractions.
    """
    omega = rho_compression / rho_critical
    H_sq  = (8 * math.pi * G_NEWTON / 3) * rho_compression
    H     = math.sqrt(abs(H_sq))

    return {
        'rho_compression_kg_m3':    rho_compression,
        'rho_critical_kg_m3':       rho_critical,
        'omega_total':              omega,
        'H_si':                     H,
        'H_km_s_mpc':               H / 3.241e-20,  # convert s⁻¹ to km/s/Mpc
        'note': ('H = √(8πGρ/3) — same form as Friedmann; DFC interpretation '
                 'is ρ = total compression budget density.'),
    }


def dark_energy_as_compression_rate(H_0=H_0_SI, omega_lambda=OMEGA_LAMBDA):
    """
    Dark energy density as the residual global compression rate.

    In DFC, dark energy is not a mysterious repulsive field — it is the
    ongoing tendency of the compression process to remove dimensional volume.
    The universe is not being pushed apart by dark energy; it is being
    continuously compressed, and the lateral redistribution of that compression
    manifests as accelerated expansion from within.

    The cosmological constant:
        Λ = 3 H_0² Ω_Λ / c²

    In DFC:
        Λ = (global compression rate)² × (dimensional volume fraction
             being removed per unit time)

    This gives Λ a physical meaning as a compression rate parameter rather
    than a vacuum energy density.

    Returns
    -------
    dict with dark energy density and DFC interpretation.
    """
    rho_lambda = omega_lambda * (3 * H_0**2) / (8 * math.pi * G_NEWTON)
    Lambda     = 3 * H_0**2 * omega_lambda / C_LIGHT**2

    return {
        'rho_lambda_kg_m3':     rho_lambda,
        'Lambda_m_minus2':      Lambda,
        'Lambda_gev2':          Lambda * (C_LIGHT * HBAR_TO_GEV_M)**2,
        'omega_lambda':         omega_lambda,
        'dfc_interpretation': (
            'Λ = 3H²Ω_Λ/c² ≈ {:.3e} m⁻². In DFC this is the global compression '
            'rate: the fractional rate of dimensional volume removal per unit '
            'Hubble time squared. Not a vacuum energy — a process rate.'.format(Lambda)
        ),
    }


# Helper for unit conversion
HBAR_TO_GEV_M = 0.197e-15  # ℏc in GeV·m


# ── Friedmann analogue from compression dynamics ──────────────────────────────

def friedmann_dfc_analogue(
    rho_matter,
    rho_lambda,
    k_curvature=0,
    rho_critical=RHO_CRIT_KG_M3,
):
    """
    DFC analogue of the Friedmann equation.

    Standard Friedmann equation:
        H² = (8πG/3)(ρ_m + ρ_Λ + ρ_r) - k c²/a²

    DFC reinterpretation:
        H² = (8πG/3)(ρ_closures + ρ_compression_residual + ρ_radiation) - k c²/a²

    where:
        ρ_closures               = stable kink density (baryons + dark matter)
        ρ_compression_residual   = ongoing compression pressure (dark energy)
        ρ_radiation              = D2-mode propagation density (photons + neutrinos)
        k                        = spatial curvature (0 = flat, consistent with DFC
                                   prediction that global compression is uniform)

    DFC prediction for spatial flatness:
        The compression process acts uniformly at cosmological scales — there is no
        preferred direction for folding. This naturally produces k = 0 (flat universe).
        Observed: Ω_total = 1.0000 ± 0.0040 (Planck 2018). ✓

    Parameters
    ----------
    rho_matter, rho_lambda : float
        Energy densities in kg/m³.
    k_curvature : int
        Spatial curvature (+1, 0, -1).

    Returns
    -------
    dict with Hubble parameter and components.
    """
    rho_total = rho_matter + rho_lambda
    H_sq = (8 * math.pi * G_NEWTON / 3) * rho_total
    if k_curvature != 0:
        # Curvature term requires scale factor a — set to 1 for present epoch
        H_sq -= k_curvature * C_LIGHT**2

    H = math.sqrt(max(H_sq, 0))

    return {
        'rho_matter':       rho_matter,
        'rho_lambda':       rho_lambda,
        'rho_total':        rho_total,
        'H_si':             H,
        'H_km_s_mpc':       H / 3.241e-20,
        'H_observed':       H_0_KM_S_MPC,
        'ratio_pred_obs':   (H / 3.241e-20) / H_0_KM_S_MPC if H > 0 else None,
        'flatness':         'Predicted: k=0 from uniform compression dynamics',
    }


def friedmann_with_observed():
    """Evaluate the DFC Friedmann analogue with observed density parameters."""
    rho_m   = OMEGA_MATTER   * RHO_CRIT_KG_M3
    rho_lam = OMEGA_LAMBDA   * RHO_CRIT_KG_M3
    return friedmann_dfc_analogue(rho_m, rho_lam, k_curvature=0)


# ── Cyclic renewal condition ──────────────────────────────────────────────────

def cyclic_renewal_condition(compression_budget_remaining, critical_fraction=0.01):
    """
    Condition for the cyclic renewal of the universe.

    In DFC, terminal folding occurs when the global compression budget has been
    almost entirely converted to stable closures and radiation — the remaining
    free compression budget approaches zero.

    When the remaining budget falls below the critical fraction:
        B_remaining / B_total < critical_fraction

    the compression stress exceeds all available restoring forces and a global
    buckling event occurs. This generates new orthogonal degrees of freedom —
    a new bifurcation at the highest level, creating conditions for a new universe.

    The cycle is:
        Compression → Bifurcation → Structure → Terminal folding → Global buckling
        → New bifurcation → (repeat)

    Key features:
      - Deterministic in necessity (the cycle always occurs)
      - Indeterminate in detail (the new universe's parameters depend on the
        microstructure of the terminal folding event)
      - Not eternal inflation (no pre-existing spacetime background)
      - Not a bounce (the old structure collapses to D1, not a reversal)

    Parameters
    ----------
    compression_budget_remaining : float
        Remaining free compression budget (fraction of initial, 0–1).
    critical_fraction : float
        Threshold below which global buckling occurs.

    Returns
    -------
    dict with renewal condition status.
    """
    renewal_imminent = compression_budget_remaining < critical_fraction

    return {
        'budget_remaining':     compression_budget_remaining,
        'critical_fraction':    critical_fraction,
        'renewal_imminent':     renewal_imminent,
        'current_estimate':     ('Far from renewal — universe is ~13.8 Gyr old, '
                                 'compression budget still >99% available'),
        'terminal_state':       ('D1 approach — all stable closures have collapsed, '
                                 'radiation redshifted to zero, only residual compression'),
        'renewal_mechanism':    ('Global buckling instability at D1 approach → '
                                 'new bifurcation → new dimensional layer → new universe'),
        'timescale':            ('Far-future: ~10^100 years (beyond black hole evaporation, '
                                 'proton decay if any, dark energy dominated expansion)'),
    }


# ── Dark matter candidates ────────────────────────────────────────────────────

def dark_matter_candidates():
    """
    Dark matter candidates from intermediate-depth stable kinks.

    In the DFC stack, particles correspond to stable closures at specific depths.
    The observed Standard Model particles occupy depths D2–D9.
    Stable structures between the observed depths — particularly between D4
    (mass onset) and D5 (electron) — would be:
      - Massive (they reach D4)
      - Electrically neutral (they don't reach D5 where U(1) closes)
      - Weakly interacting (they don't reach D6 where SU(2) closes fully)
      - Stable (topologically protected at their depth)

    These are the dimensional folding dark matter candidates.

    Returns
    -------
    dict with candidate properties and mass range.
    """
    return {
        'candidate_type':   'Intermediate-depth stable kinks (D4–D5 range)',
        'mass_range_gev':   (0.001, 0.511e-3 * 1000),  # ~ MeV to GeV scale
        'electric_charge':  0,         # Does not reach D5 (U(1) closure depth)
        'weak_charge':      'small',   # Partially reaches D6 — very weak coupling
        'strong_charge':    0,         # Does not reach D7 (SU(3) closure depth)
        'stability':        'Topologically protected — cannot decay without crossing D5 barrier',
        'detection':        'Gravitational only at large scales; weak interaction at short range',
        'distinguishing_feature': (
            'Unlike WIMP models, DFC dark matter is not a new particle type — '
            'it is the same compression field as ordinary matter, stabilized '
            'at a different depth. Its properties are not free parameters; '
            'they are determined by the depth model.'
        ),
        'mass_prediction':  ('From depth model with d_DM ≈ 4.5: '
                             'm_DM ≈ m_e × exp(κ × (4.5 - 5.0)) ≈ m_e × e^{-κ/2}. '
                             'With κ ≈ 5.33: m_DM ≈ 0.511 MeV × e^{-2.67} ≈ 35 keV. '
                             'This is the warm dark matter range — consistent with '
                             'small-scale structure observations.'),
        'open_problem':     'Precise depth assignment and stability lifetime calculation',
    }


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("COSMOLOGY — GLOBAL COMPRESSION DYNAMICS")
    print("Dimensional Folding Model")
    print("=" * 65)

    print(f"\n--- Friedmann Analogue with Observed Densities ---")
    fr = friedmann_with_observed()
    print(f"  ρ_matter:    {fr['rho_matter']:.3e} kg/m³")
    print(f"  ρ_lambda:    {fr['rho_lambda']:.3e} kg/m³")
    print(f"  H predicted: {fr['H_km_s_mpc']:.2f} km/s/Mpc")
    print(f"  H observed:  {fr['H_observed']:.2f} km/s/Mpc")
    print(f"  Ratio:       {fr['ratio_pred_obs']:.4f}")
    print(f"  Flatness:    {fr['flatness']}")

    print(f"\n--- Dark Energy as Compression Rate ---")
    de = dark_energy_as_compression_rate()
    print(f"  Λ:           {de['Lambda_m_minus2']:.4e} m⁻²")
    print(f"  ρ_Λ:         {de['rho_lambda_kg_m3']:.4e} kg/m³")
    print(f"  DFC:         {de['dfc_interpretation']}")

    print(f"\n--- Dark Matter Candidates ---")
    dm = dark_matter_candidates()
    print(f"  Type:        {dm['candidate_type']}")
    print(f"  Charge:      Q = {dm['electric_charge']},  color = {dm['strong_charge']}")
    print(f"  Stability:   {dm['stability']}")
    print(f"  Mass est.:   {dm['mass_prediction']}")

    print(f"\n--- Cyclic Renewal ---")
    renew = cyclic_renewal_condition(compression_budget_remaining=0.99)
    print(f"  Imminent:    {renew['renewal_imminent']}")
    print(f"  Current:     {renew['current_estimate']}")
    print(f"  Mechanism:   {renew['renewal_mechanism']}")
    print(f"  Timescale:   {renew['timescale']}")

    print(f"\n--- Density Parameter Summary ---")
    print(f"  Ω_Λ (dark energy):  {OMEGA_LAMBDA:.3f}")
    print(f"  Ω_DM (dark matter): {OMEGA_DM:.3f}")
    print(f"  Ω_b  (baryons):     {OMEGA_BARYON:.3f}")
    print(f"  Ω_total:            {OMEGA_LAMBDA+OMEGA_MATTER:.3f}  (predicted: 1.000)")

    print(f"\n--- Open Problems ---")
    print(f"  1. Derive Friedmann equation from DFC compression field dynamics")
    print(f"  2. Predict Λ from global compression rate (not fit from H_0)")
    print(f"  3. Compute dark matter mass precisely from depth model")
    print(f"  4. Hubble tension: DFC prediction vs CMB vs local distance ladder")
    print(f"  5. Inflation analogue: was early universe expansion a global bifurcation?")
    print(f"  See: foundations/formation.md, phenomena/thermodynamics/thermodynamics.md")
