"""
Neutrino masses from shallow dimensional anchoring.

In the Dimensional Folding Model, mass arises from anchoring into the D4 inertia layer.
Particles that barely reach D4 — neutrinos — have masses exponentially suppressed relative
to those with deeper anchoring (electrons, muons).

Conceptual basis:
    Photons:    ~D2   — no D4 anchoring → no rest mass
    Neutrinos:  ~D3.x — fractional D4 anchoring → tiny mass
    Electrons:  ~D5   — full D4 anchoring + dimple state → m_e = 0.511 MeV
    Muons:      ~D6   — deeper anchoring → m_μ = 105.7 MeV

Three neutrino mass eigenstates correspond to three winding modes of the SU(3) closure
at the shallow end of the dimensional stack — the same topological threefold structure
that produces three quark colors and three lepton generations, but accessed here at the
D3↔D4 boundary rather than deep in the confinement regime.

The neutrino mass scale is currently a fit parameter — f_ν (the D4 anchoring fraction)
is scanned to find values consistent with Planck + KATRIN bounds. A genuine first-principles
derivation would compute f_ν from the substrate dynamics at the D3↔D4 boundary without
using oscillation data as input. No such derivation exists yet.

Observable predictions:
  - Three distinct neutrino masses m₁ < m₂ < m₃ (or inverted hierarchy)
  - Mass-squared differences Δm²₂₁, Δm²₃₁ from depth differences between winding modes
  - Absolute mass scale constrained by f_ν, which is currently a fit parameter
  - Normal vs inverted hierarchy: determined by the sign of the SU(3) winding asymmetry

Experimental inputs used:
  - Δm²₂₁ = 7.53 × 10⁻⁵ eV²  (solar, KamLAND)
  - |Δm²₃₁| = 2.453 × 10⁻³ eV²  (atmospheric, T2K, NOvA)
  - Σmᵢ < 0.12 eV  (Planck 2018 cosmological bound)
  - Individual mass bounds: mᵢ < 0.45 eV (KATRIN 2022)

Usage:
    python equations/neutrino_masses.py

    Or import:
        from equations.neutrino_masses import predict_neutrino_masses, anchoring_mass
"""

import math

# ── Experimental constraints (PDG 2024) ──────────────────────────────────────

# Mass-squared differences from oscillation experiments (eV²)
# PDG 2024 values — consistent with equations/flavor_mixing.py (Cycle 69)
# and equations/neutrino_oscillations.py (Cycle 65)
DM2_SOLAR    = 7.42e-5    # Δm²₂₁ = m₂² - m₁²  (positive by convention)
DM2_ATM      = 2.517e-3   # |Δm²₃₁|  (sign = +: normal, -: inverted)
DM2_ATM_ERR  = 0.028e-3   # uncertainty (PDG 2024)

# Cosmological bound on sum of neutrino masses (Planck 2018)
SUM_MASS_BOUND_EV = 0.12  # eV

# KATRIN direct mass bound (90% CL, 2022)
KATRIN_BOUND_EV = 0.45    # eV

# Lepton anchor masses for calibration
M_ELECTRON_MEV = 0.51099895  # MeV
M_MUON_MEV     = 105.6583755 # MeV


# ── Depth-anchoring mass model ────────────────────────────────────────────────

def anchoring_mass(depth, depth_ref, mass_ref_mev, kappa):
    """
    Mass from dimensional anchoring depth using exponential suppression model.

    In this model, mass increases with anchoring depth into the D4 layer:

        m(d) = m_ref × exp(κ × (d - d_ref))

    where:
        d     = effective dimensional depth of the particle
        d_ref = reference depth (e.g., electron at D5)
        κ     = anchoring sensitivity (derived from lepton mass ratio)

    The exponential arises because D4 anchoring is a tunneling-like process:
    a particle with depth d < d_ref has exponentially suppressed overlap with
    the D4 inertia mode.

    Parameters
    ----------
    depth : float
        Effective dimensional depth of the particle (e.g., 3.5 for a neutrino).
    depth_ref : float
        Reference depth for the known particle (e.g., 5.0 for the electron).
    mass_ref_mev : float
        Mass of the reference particle in MeV.
    kappa : float
        Anchoring sensitivity — depth units per e-folding of mass.

    Returns
    -------
    float
        Predicted mass in MeV.
    """
    return mass_ref_mev * math.exp(kappa * (depth - depth_ref))


def fit_kappa_from_leptons(
    d_electron=5.0,
    d_muon=6.0,
    m_electron_mev=M_ELECTRON_MEV,
    m_muon_mev=M_MUON_MEV,
):
    """
    Extract the anchoring sensitivity κ from the electron/muon mass ratio.

    From:    m_μ / m_e = exp(κ × (d_μ - d_e))
    Solve:   κ = ln(m_μ / m_e) / (d_μ - d_e)

    This κ is the fundamental calibration of how steeply mass grows with depth.

    Returns
    -------
    dict with kappa and derived quantities.
    """
    ratio = m_muon_mev / m_electron_mev
    delta_d = d_muon - d_electron
    kappa = math.log(ratio) / delta_d

    return {
        'kappa':        kappa,
        'mass_ratio':   ratio,
        'delta_depth':  delta_d,
        'e_foldings':   math.log(ratio),
        'note':         (f'κ = {kappa:.4f}: each unit of depth increases mass '
                         f'by factor {math.exp(kappa):.1f}'),
    }


def sub_d4_mass(anchoring_fraction, m_electron_mev=M_ELECTRON_MEV, power=2.0):
    """
    Mass formula for particles that do not fully anchor into D4.

    The lepton mass formula (exp(κ × Δd)) applies to particles fully inside D4
    (d ≥ 4). For particles below D4 (neutrinos at d < 4), a different mechanism
    applies: the mass comes from the *overlap* of the particle's mode with the D4
    inertia layer.

    This overlap is quadratically suppressed for small anchoring fractions:

        m(f) = m_e × f^power

    where f ∈ [0, 1] is the fractional D4 penetration and power ≥ 2.

    Physical motivation: this is analogous to a seesaw mechanism in DFC language.
    A particle that only partially enters the D4 layer gets a mass that goes as the
    SQUARE of its anchoring (not linear) because it must tunnel in and back out:
    the mass matrix element requires two D3↔D4 boundary crossings.

    For power=2, m_ν < 0.1 eV requires f < 4.5 × 10⁻⁴.

    Parameters
    ----------
    anchoring_fraction : float
        f ∈ [0, 1], fractional D4 penetration.
    m_electron_mev : float
        Reference mass (electron) at f = 1.
    power : float
        Suppression power (default 2 — double boundary crossing).

    Returns
    -------
    float : mass in MeV.
    """
    return m_electron_mev * anchoring_fraction**power


def predict_neutrino_masses(
    d_electron=5.0,
    d_nu1=None,
    d_nu2=None,
    d_nu3=None,
    anchoring_fraction=1e-4,
    hierarchy='normal',
):
    """
    Predict three neutrino masses from their anchoring depths.

    Strategy:
      1. Calibrate κ from electron/muon mass ratio
      2. Parameterize neutrino depths relative to the D4 threshold (depth=4)
      3. The three winding modes of the SU(3) shallow closure give three slightly
         different depths → three slightly different masses
      4. Compare predicted mass-squared differences with oscillation data

    The anchoring fraction f_ν parametrizes how far into D4 neutrinos reach:
        d_ν ≈ 3 + f_ν    (D3 = 3.0, D4 full anchoring = 4.0)

    If d_ν values are not supplied, they are inferred from oscillation data:
    the mass-squared differences constrain the depth spacings between the three
    winding modes.

    Parameters
    ----------
    d_electron : float
        Effective depth of the electron (default 5.0).
    d_nu1, d_nu2, d_nu3 : float or None
        Depths of the three neutrino eigenstates. If None, inferred from
        oscillation constraints given anchoring_fraction.
    anchoring_fraction : float
        Fractional D4 penetration for the lightest neutrino (0 = no mass, 1 = full D4).
        Default 0.25.
    hierarchy : str
        'normal' (m₁ < m₂ < m₃) or 'inverted' (m₃ < m₁ < m₂).

    Returns
    -------
    dict with predicted masses, mass-squared differences, and consistency checks.
    """
    kappa_data = fit_kappa_from_leptons(d_electron=d_electron)
    kappa = kappa_data['kappa']

    # Sub-D4 mass via double-boundary-crossing suppression
    m1_mev = sub_d4_mass(anchoring_fraction)
    m1_ev  = m1_mev * 1e6  # convert MeV → eV

    # Infer m2 from solar mass-squared difference: m₂² = m₁² + Δm²₂₁
    m2_sq_ev2 = m1_ev**2 + DM2_SOLAR
    if m2_sq_ev2 < 0:
        m2_ev = None
    else:
        m2_ev = math.sqrt(m2_sq_ev2)

    # Infer m3 from atmospheric mass-squared difference
    if hierarchy == 'normal':
        # m₃² = m₁² + |Δm²₃₁|
        m3_sq_ev2 = m1_ev**2 + DM2_ATM
    else:
        # Inverted: m₁² = m₃² + |Δm²₃₁|  → m₃² = m₁² - |Δm²₃₁|
        m3_sq_ev2 = m1_ev**2 - DM2_ATM

    m3_ev = math.sqrt(abs(m3_sq_ev2)) if m3_sq_ev2 > 0 else None

    # Infer d_nu2 and d_nu3 from predicted masses
    d_nu2 = d_electron + math.log(m2_ev * 1e-6 / M_ELECTRON_MEV) / kappa if m2_ev else None
    d_nu3 = d_electron + math.log(m3_ev * 1e-6 / M_ELECTRON_MEV) / kappa if m3_ev else None

    # Sum of masses
    sum_ev = m1_ev + (m2_ev or 0) + (m3_ev or 0)

    # Mass-squared differences (predictions vs. data)
    dm2_21_pred = (m2_ev**2 - m1_ev**2) if m2_ev else None
    dm2_31_pred = (m3_ev**2 - m1_ev**2) if m3_ev else None

    return {
        'kappa':                kappa,
        'anchoring_fraction':   anchoring_fraction,
        'd_nu1':                d_nu1,
        'd_nu2':                d_nu2,
        'd_nu3':                d_nu3,

        'm1_ev':                m1_ev,
        'm2_ev':                m2_ev,
        'm3_ev':                m3_ev,
        'sum_masses_ev':        sum_ev,

        'dm2_21_pred_ev2':      dm2_21_pred,
        'dm2_21_data_ev2':      DM2_SOLAR,
        'dm2_31_pred_ev2':      dm2_31_pred,
        'dm2_31_data_ev2':      DM2_ATM,

        'sum_below_planck':     sum_ev < SUM_MASS_BOUND_EV,
        'below_katrin':         m1_ev < KATRIN_BOUND_EV,

        'hierarchy':            hierarchy,
        'note': ('m₁ from anchoring model; m₂, m₃ from oscillation mass-squared '
                 'differences. d_ν2, d_ν3 are back-derived depth values.'),
    }


def scan_anchoring_fractions(fractions=None, hierarchy='normal'):
    """
    Scan anchoring fractions to find the range consistent with all experimental bounds.

    Returns a list of (fraction, result) pairs that pass all constraints.
    """
    if fractions is None:
        # Sub-D4 anchoring fractions: logarithmically spaced from 1e-5 to 1e-3
        fractions = [10**(-5 + i * 0.1) for i in range(40)]

    consistent = []
    for f in fractions:
        result = predict_neutrino_masses(anchoring_fraction=f, hierarchy=hierarchy)
        m3 = result.get('m3_ev')
        if (result['sum_below_planck'] and result['below_katrin']
                and m3 is not None and m3 > 0):
            consistent.append((f, result))

    return consistent


def winding_mode_depth_spacing(kappa, dm2_target_ev2, m_base_ev):
    """
    Infer the depth spacing between two SU(3) winding modes from their
    mass-squared difference.

    If two neutrino winding modes have depths d₁ and d₂:
        m₂² - m₁² = Δm²
        m₁ × exp(κ × Δd) = m₂
        (m₁ exp(κΔd))² - m₁² = Δm²
        m₁²(exp(2κΔd) - 1) = Δm²

    Solve for Δd.

    Parameters
    ----------
    kappa : float
        Anchoring sensitivity from lepton calibration.
    dm2_target_ev2 : float
        Mass-squared difference to reproduce (eV²).
    m_base_ev : float
        Mass of the lighter state (eV).

    Returns
    -------
    float : depth spacing Δd between the two winding modes.
    """
    # m₁² (exp(2κΔd) - 1) = Δm²
    # exp(2κΔd) = 1 + Δm²/m₁²
    ratio = 1 + dm2_target_ev2 / m_base_ev**2
    if ratio <= 1:
        return 0.0
    return math.log(ratio) / (2 * kappa)


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("NEUTRINO MASSES — DIMENSIONAL ANCHORING MODEL")
    print("Dimensional Folding Model")
    print("=" * 65)

    kd = fit_kappa_from_leptons()
    print(f"\n--- Anchoring Calibration from Lepton Masses ---")
    print(f"  Electron depth:     D5 (d = 5.0)  [ASSUMPTION: D-label integer spacing = 1]")
    print(f"  Muon depth:         D6 (d = 6.0)  [ASSUMPTION: same integer spacing]")
    print(f"  WARNING: D-labels are provisional markers; spacing of 1.0 between")
    print(f"           adjacent D-levels is not derived from the substrate. Kappa")
    print(f"           and all depth-based quantities depend on this assumption.")
    print(f"  Mass ratio m_μ/m_e: {kd['mass_ratio']:.2f}")
    print(f"  Kappa κ:            {kd['kappa']:.4f}  ({kd['note']})")

    print(f"\n--- Neutrino Mass Predictions (Normal Hierarchy) ---")
    print(f"  (anchoring fraction scanned for consistency with Planck + KATRIN bounds)")
    print()
    print(f"  IMPORTANT: what is input vs. output in this model:")
    print(f"    INPUT  (from oscillation data): Δm²₂₁ = {DM2_SOLAR:.3e} eV²,  Δm²₃₁ = {DM2_ATM:.3e} eV²")
    print(f"    INPUT  (fit parameter):          anchoring fraction f_ν (not derived from substrate)")
    print(f"    OUTPUT (from model):             m₁ = m_e × f_ν² (this is the only genuine prediction)")
    print(f"    DERIVED (from m₁ + inputs):     m₂, m₃ from m₁² ± Δm² → circular for Δm² checks")
    print(f"    NOTE: the Δm² 'predictions' below are INPUTS used to derive m₂,m₃ — not free predictions")

    consistent = scan_anchoring_fractions(hierarchy='normal')
    if consistent:
        f_min = consistent[0][0]
        f_max = consistent[-1][0]
        print(f"\n  Consistent anchoring fractions (passes Planck + KATRIN): {f_min:.2e} – {f_max:.2e}")
        # Show mid-range example
        mid = consistent[len(consistent)//2]
        r = mid[1]
        print(f"\n  Example (f = {mid[0]:.2e}):")
        print(f"    m₁ = m_e × f²    = {r['m1_ev']*1000:.4f} meV  [OUTPUT: from anchoring model]")
        if r['m2_ev']:
            print(f"    m₂ = √(m₁²+Δm²₂₁) = {r['m2_ev']*1000:.4f} meV  [DERIVED from input Δm²₂₁]")
        if r['m3_ev']:
            print(f"    m₃ = √(m₁²+Δm²₃₁) = {r['m3_ev']*1000:.4f} meV  [DERIVED from input Δm²₃₁]")
        print(f"    Σmᵢ  = {r['sum_masses_ev']*1000:.3f} meV  "
              f"(Planck bound: < {SUM_MASS_BOUND_EV*1000:.0f} meV)  ✓ consistent")
        print(f"    Δm²₂₁ = {r['dm2_21_pred_ev2']:.3e} eV²  "
              f"(data: {DM2_SOLAR:.3e} eV²)  [CIRCULAR — input used to derive m₂]")
        print(f"    Δm²₃₁ = {r['dm2_31_pred_ev2']:.3e} eV²  "
              f"(data: {DM2_ATM:.3e} eV²)  [CIRCULAR — input used to derive m₃]")
    else:
        print("  No consistent range found — model parameters need refinement.")

    print(f"\n--- Winding Mode Depth Spacings ---")
    kappa = kd['kappa']
    # Use m₁ from first consistent result
    if consistent:
        m1_ev = consistent[0][1]['m1_ev']
        dd_solar = winding_mode_depth_spacing(kappa, DM2_SOLAR, m1_ev)
        dd_atm   = winding_mode_depth_spacing(kappa, DM2_ATM,   m1_ev)
        print(f"  Solar splitting  (Δd₂₁): {dd_solar:.5f} depth units")
        print(f"  Atmospheric split(Δd₃₁): {dd_atm:.5f} depth units")
        ratio_dfc = dd_atm / dd_solar
        # sqrt(DM2_ATM/DM2_SOLAR) = 5.71 is NOT the expected depth ratio.
        # The depth ratio is: ln(1+DM2_ATM/m₁²) / ln(1+DM2_SOLAR/m₁²)
        # which varies from ~1.34 (m₁→0) to ~5.7 (m₁→sqrt(Δm²₂₁)).
        # DFC equal-spacing prediction (Δd₃₁/Δd₂₁ = 2) requires m₁ ≈ 1.57 meV.
        # STATUS: the depth ratio is m₁-dependent; the 1.34 value at minimal m₁
        # is NOT a failure — it simply reflects that m₁ is unconstrained from below.
        print(f"  Ratio Δd₃₁/Δd₂₁:        {ratio_dfc:.2f}  "
              f"[at m₁={m1_ev*1000:.4f} meV; varies 1.34–5.7 across consistent m₁ range]"
              f"\n  DFC equal-winding prediction: ratio = 2 → m₁ ≈ 1.57 meV")

    print(f"\n--- Open Constraints ---")
    print(f"  Absolute mass scale:    requires first-principles derivation of f_ν")
    print(f"  Normal vs inverted:     sign of SU(3) winding asymmetry (open problem)")
    print(f"  Majorana vs Dirac:      depends on D3↔D4 boundary chirality (open problem)")
    print(f"  See foundations/dimensional_stack.md for depth-valence assignments.")
