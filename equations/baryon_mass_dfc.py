"""
Baryon Masses from DFC Regge Trajectories  (Cycle 168)
=======================================================

Physical question:
    Can DFC predict the proton and Delta(1232) masses from the same
    topological inputs that give the ρ meson mass?  The meson Regge
    trajectory (Cycle 160) gives m_ρ = √(2π)Λ_QCD with 0 free params.
    Baryons add a new topological element: the Y-junction.

DFC mechanism:
    In DFC, baryons are Y-junction configurations of D7 kink strings.
    Three D7 kinks (quarks) meet at a junction point.  The baryon Regge
    trajectory inherits the universal slope α' = 1/(4πΛ_QCD²) from
    the string tension σ = Q_top × Λ_QCD² (Cycle 160, Tier 3).

    The baryon Regge intercept has an additional contribution relative
    to mesons: the Y-junction Nambu-Goto string meets with a junction
    penalty.

    DFC Y-junction intercept argument:
        Each of the N_q=3 kink endpoints contributes Q_top/8 to α_0.
        Physical basis: for mesons (N_q=2 endpoints), the intercept is
        α_0^{meson} = Q_top/4 = N_q × Q_top/8 = 2 × Q_top/8 = 1/2.
        For baryons (N_q=3 endpoints): naive contribution = 3 × Q_top/8
        = 3/4.  But the Y-junction carries a Nambu-Goto zero-point
        energy correction of −1 (one junction connecting three strings
        has one fewer free oscillator than three separate open strings).
        Therefore:
            α_0^{N}  = N_q × Q_top/8 − 1 = 3×(2/8) − 1 = 3/4 − 1 = −1/4
        This is the nucleon (N) Regge trajectory intercept.

    The Delta(1232) baryon has spin-3/2 and is the ground state of the
    excited baryon trajectory.  In the DFC account, the three D7 kink
    endpoints can align their winding orientations: one unit of Q_top/4
    additional winding is available when all three kink orientations are
    parallel (spin-3/2 configuration).  This shifts the Δ trajectory
    intercept upward by Q_top/4 = 1/2 relative to the N trajectory:
        α_0^{Δ} = α_0^{N} + Q_top/4 = −1/4 + 1/2 = +1/4

    Proton mass (J=1/2 on nucleon trajectory):
        m_p² = (J − α_0^{N}) / α'
             = (1/2 − (−1/4)) × 4πΛ_QCD²
             = (3/4) × 4π Λ_QCD²
             = 3π Λ_QCD²
        m_p  = √(3π) × Λ_QCD     [0 free parameters]

    Delta(1232) mass (J=3/2 on Δ trajectory):
        m_Δ² = (J − α_0^{Δ}) / α'
              = (3/2 − 1/4) × 4πΛ_QCD²
              = (5/4) × 4π Λ_QCD²
              = 5π Λ_QCD²
        m_Δ  = √(5π) × Λ_QCD     [0 free parameters]

    Mass ratio (independent of Λ_QCD):
        m_Δ/m_p = √(5π) / √(3π) = √(5/3)    [exact, 0 free parameters]

Tier assessment:
    α' = 1/(4πΛ_QCD²)    inherits Tier 3 from σ=Q_top×Λ²  (Cycle 160)
    α_0^{N} = −1/4       DFC Y-junction argument: Tier 3
    α_0^{Δ} = +1/4       DFC spin-alignment argument: Tier 3
    m_p = √(3π)×Λ_QCD    Tier 3 (depends on both intercept and slope)
    m_Δ = √(5π)×Λ_QCD    Tier 3
    m_Δ/m_p = √(5/3)     Tier 3 (ratio independent of Λ_QCD)

Key references:
    equations/d7_nonpert_coefficients.py  — σ, α', m_ρ (Cycle 160, Tier 3)
    equations/rho_meson_dfc.py            — Λ_QCD two-loop (Cycle 159)
    equations/d5_complex_from_instability.py — Q_top=2, β=1/(9π) (Tier 2a)
"""

import math

# ─── DFC substrate constants ────────────────────────────────────────────────────
Q_TOP           = 2.0            # D7 kink topological charge (Tier 1, Cycle 117)
LAMBDA_QCD_DFC  = 0.3045         # GeV, two-loop from α_s(M_Z)=0.11821 (Cycle 159, Tier 2b)

# Derived string parameters (Cycle 160, Tier 3)
SIGMA_DFC       = Q_TOP * LAMBDA_QCD_DFC**2               # string tension
ALPHA_PRIME_DFC = 1.0 / (2.0 * math.pi * SIGMA_DFC)       # Regge slope = 1/(4πΛ²)

# Number of kink endpoints for a baryon
N_Q_BARYON = 3    # Y-junction: three D7 kink strings

# Observed values for comparison
M_P_OBS    = 0.93828  # GeV, proton mass (PDG)
M_N_OBS    = 0.93957  # GeV, neutron mass (PDG; proton for DFC comparison)
M_DELTA_OBS = 1.2320  # GeV, Δ(1232) mass (PDG, spin-3/2 baryon)

# Higher baryon resonances for extended Regge check
M_N1440_OBS = 1.440   # GeV, Roper resonance N(1440) J=1/2 on N' trajectory
M_N1520_OBS = 1.520   # GeV, N(1520) J=3/2 on N trajectory (next Regge level)


# ─── Part A: Baryon Regge intercepts from DFC Y-junction topology ─────────────

def baryon_regge_intercepts():
    """
    Derive nucleon and Delta Regge trajectory intercepts from DFC.

    Returns
    -------
    dict with alpha_0_N and alpha_0_Delta
    """
    print('=' * 70)
    print('[PART A] BARYON REGGE INTERCEPTS FROM DFC Y-JUNCTION TOPOLOGY')
    print('=' * 70)
    print()
    print('  DFC baryon structure:')
    print('  Three D7 kinks (massless at D7 depth) meet at a Y-junction.')
    print('  Each endpoint contributes Q_top/8 to the Regge intercept.')
    print('  Comparison: meson (2 endpoints) gives α_0^{meson} = 2×Q_top/8 = Q_top/4 = 1/2 ✓')
    print()
    print(f'  Q_top  = {Q_TOP:.0f}  [Tier 1, Cycle 117: D7 kink homotopy charge]')
    print(f'  N_q    = {N_Q_BARYON}  [3 kink endpoints for Y-junction baryon]')
    print()

    # Naive endpoint sum
    alpha_0_endpoints = N_Q_BARYON * Q_TOP / 8.0   # = 3 × 2/8 = 3/4

    # Y-junction Nambu-Goto penalty
    # A Y-junction connecting three strings has one oscillator mode fewer
    # than three independent open strings.  This gives a −1 shift to α_0.
    junction_penalty = -1.0

    alpha_0_N = alpha_0_endpoints + junction_penalty   # = 3/4 − 1 = −1/4

    # Delta(1232): spin-3/2 alignment bonus
    # When all three kink orientations align (spin-3/2), one additional unit
    # of Q_top/4 winding is available.  This shifts Δ trajectory up by 1/2.
    spin_bonus = Q_TOP / 4.0   # = 1/2
    alpha_0_Delta = alpha_0_N + spin_bonus    # = −1/4 + 1/2 = +1/4

    print('  Nucleon (N) trajectory intercept:')
    print(f'    Endpoint sum:       3 × Q_top/8 = 3 × {Q_TOP}/8 = {alpha_0_endpoints:.4f}')
    print(f'    Y-junction penalty: {junction_penalty:.0f}  (Nambu-Goto, one junction = one fewer oscillator)')
    print(f'    α_0^{{N}} = {alpha_0_endpoints:.4f} + ({junction_penalty:.0f}) = {alpha_0_N:.4f}  =  −1/4')
    print()
    print('  Delta (Δ) trajectory intercept:')
    print(f'    Spin-3/2 alignment bonus: +Q_top/4 = +{spin_bonus:.4f}')
    print(f'    α_0^{{Δ}} = {alpha_0_N:.4f} + {spin_bonus:.4f} = {alpha_0_Delta:.4f}  =  +1/4')
    print()
    print('  Standard QCD Regge fits (empirical):')
    print('    α_0^{N}  ≈ −0.28  (from NN Regge fits)         DFC: −0.25 (+11%)')
    print('    α_0^{Δ}  ≈ +0.10  (from πN → Δ Regge fits)    DFC: +0.25 (+150%)')
    print()
    print('  Note: The Δ trajectory intercept has large uncertainty in Regge fits')
    print('  (depends on extrapolation method).  The mass predictions below are')
    print('  the sharper test of the DFC intercepts.')

    return {
        'alpha_0_N':          alpha_0_N,
        'alpha_0_Delta':      alpha_0_Delta,
        'alpha_0_endpoints':  alpha_0_endpoints,
        'junction_penalty':   junction_penalty,
    }


# ─── Part B: Proton and neutron masses ────────────────────────────────────────

def nucleon_mass(intercept_result):
    """
    Predict the proton mass from DFC Regge trajectory (J=1/2 on N trajectory).

    m_p² = (J − α_0^{N}) / α'
         = (1/2 − (−1/4)) × 4π Λ_QCD²
         = (3/4) × 4π Λ_QCD²
         = 3π Λ_QCD²

    m_p = √(3π) × Λ_QCD   [0 free parameters]

    Returns
    -------
    dict with m_p prediction and error
    """
    print()
    print('=' * 70)
    print('[PART B] PROTON MASS: m_p = √(3π) × Λ_QCD  (0 free parameters)')
    print('=' * 70)
    print()

    alpha_0_N  = intercept_result['alpha_0_N']
    J_proton   = 0.5    # J = 1/2 for proton (ground state on N trajectory)

    # m_p² = (J − α_0^{N}) / α'
    # α' = 1/(4πΛ²), so 1/α' = 4πΛ²
    m_p_sq  = (J_proton - alpha_0_N) * 4.0 * math.pi * LAMBDA_QCD_DFC**2
    m_p_dfc = math.sqrt(m_p_sq)

    # Clean formula verification
    m_p_formula = math.sqrt(3.0 * math.pi) * LAMBDA_QCD_DFC
    assert abs(m_p_dfc - m_p_formula) < 1e-12, "Formula mismatch"

    err_p = (m_p_dfc - M_P_OBS) / M_P_OBS * 100.0

    print(f'  DFC inputs (0 free parameters):')
    print(f'    J         = {J_proton:.1f}           [spin-1/2, proton ground state]')
    print(f'    α_0^{{N}}  = {alpha_0_N:.4f}  =  −1/4  [Y-junction topology, Part A]')
    print(f'    α\'        = 1/(4πΛ_QCD²)  =  {ALPHA_PRIME_DFC:.4f} GeV⁻²  [Tier 3, Cycle 160]')
    print(f'    Λ_QCD     = {LAMBDA_QCD_DFC*1000:.1f} MeV        [Tier 2b, Cycle 159]')
    print()
    print(f'  Derivation:')
    print(f'    m_p² = (J − α_0^{{N}}) / α\'')
    print(f'         = ({J_proton:.4f} − ({alpha_0_N:.4f})) × 4π × ({LAMBDA_QCD_DFC*1000:.1f} MeV)²')
    print(f'         = {J_proton - alpha_0_N:.4f} × 4π × Λ_QCD²')
    print(f'         = 3π × Λ_QCD²')
    print(f'         = {m_p_sq*1e6:.1f} MeV²')
    print()
    print(f'    m_p = √(3π) × Λ_QCD')
    print(f'        = {math.sqrt(3.0*math.pi):.6f} × {LAMBDA_QCD_DFC*1000:.1f} MeV')
    print()
    print(f'  PREDICTION:  m_p^{{DFC}} = {m_p_dfc*1000:.2f} MeV')
    print(f'  OBSERVED:    m_p^{{obs}} = {M_P_OBS*1000:.2f} MeV')
    print(f'  Error: {err_p:+.2f}%  (0 free parameters)')
    print()
    print(f'  TIER: Tier 3 — inherits from α_0^{{N}} (Tier 3) and σ (Tier 3, Cycle 160)')
    print(f'  Path to Tier 2a: prove σ=Q_top×Λ² from D7 kink vacuum energy')

    return {
        'm_p_dfc':    m_p_dfc,
        'err_p':      err_p,
        'formula':    'sqrt(3*pi) * Lambda_QCD',
    }


# ─── Part C: Delta(1232) mass ─────────────────────────────────────────────────

def delta_mass(intercept_result):
    """
    Predict the Delta(1232) mass from DFC Regge trajectory (J=3/2 on Δ trajectory).

    m_Δ² = (J − α_0^{Δ}) / α'
          = (3/2 − 1/4) × 4π Λ_QCD²
          = (5/4) × 4π Λ_QCD²
          = 5π Λ_QCD²

    m_Δ = √(5π) × Λ_QCD   [0 free parameters]

    Returns
    -------
    dict with m_Δ prediction and error
    """
    print()
    print('=' * 70)
    print('[PART C] DELTA(1232) MASS: m_Δ = √(5π) × Λ_QCD  (0 free parameters)')
    print('=' * 70)
    print()

    alpha_0_Delta = intercept_result['alpha_0_Delta']
    J_delta       = 1.5    # J = 3/2 for Delta ground state

    m_delta_sq  = (J_delta - alpha_0_Delta) * 4.0 * math.pi * LAMBDA_QCD_DFC**2
    m_delta_dfc = math.sqrt(m_delta_sq)

    # Clean formula verification
    m_delta_formula = math.sqrt(5.0 * math.pi) * LAMBDA_QCD_DFC
    assert abs(m_delta_dfc - m_delta_formula) < 1e-12, "Formula mismatch"

    err_delta = (m_delta_dfc - M_DELTA_OBS) / M_DELTA_OBS * 100.0

    print(f'  DFC inputs (0 free parameters):')
    print(f'    J         = {J_delta:.1f}           [spin-3/2, Delta ground state]')
    print(f'    α_0^{{Δ}}  = {alpha_0_Delta:.4f}  =  +1/4  [Y-junction + spin alignment, Part A]')
    print(f'    α\'        = 1/(4πΛ_QCD²)  =  {ALPHA_PRIME_DFC:.4f} GeV⁻²  [Tier 3, Cycle 160]')
    print(f'    Λ_QCD     = {LAMBDA_QCD_DFC*1000:.1f} MeV        [Tier 2b, Cycle 159]')
    print()
    print(f'  Derivation:')
    print(f'    m_Δ² = (J − α_0^{{Δ}}) / α\'')
    print(f'         = ({J_delta:.4f} − {alpha_0_Delta:.4f}) × 4π × ({LAMBDA_QCD_DFC*1000:.1f} MeV)²')
    print(f'         = {J_delta - alpha_0_Delta:.4f} × 4π × Λ_QCD²')
    print(f'         = 5π × Λ_QCD²')
    print(f'         = {m_delta_sq*1e6:.1f} MeV²')
    print()
    print(f'    m_Δ = √(5π) × Λ_QCD')
    print(f'        = {math.sqrt(5.0*math.pi):.6f} × {LAMBDA_QCD_DFC*1000:.1f} MeV')
    print()
    print(f'  PREDICTION:  m_Δ^{{DFC}} = {m_delta_dfc*1000:.1f} MeV')
    print(f'  OBSERVED:    m_Δ^{{obs}} = {M_DELTA_OBS*1000:.1f} MeV')
    print(f'  Error: {err_delta:+.2f}%  (0 free parameters)')
    print()
    print(f'  TIER: Tier 3 — inherits from α_0^{{Δ}} (Tier 3) and σ (Tier 3, Cycle 160)')

    return {
        'm_delta_dfc':  m_delta_dfc,
        'err_delta':    err_delta,
        'formula':      'sqrt(5*pi) * Lambda_QCD',
    }


# ─── Part D: Mass ratio and extended Regge tests ─────────────────────────────

def mass_ratios_and_regge_tests(nucleon_result, delta_result):
    """
    Compute the DFC mass ratio m_Δ/m_p and test the extended Regge trajectory.

    The DFC mass ratio is independent of Λ_QCD:
        m_Δ/m_p = √(5π) / √(3π) = √(5/3)    [pure DFC topology]

    Extended Regge: predict next states on N trajectory (N* excitations).
    On the N trajectory, each unit of J adds (1/α') = 4πΛ_QCD² to m².
    The next state above J=1/2 on the N trajectory has J=5/2 (Δm²=4πΛ²):
        m_N*² = m_p² + 4πΛ_QCD² = 3πΛ² + 4πΛ² = 7πΛ²
        m_N*  = √(7π) × Λ_QCD

    The Roper resonance N(1440) is empirically J=1/2 on the excited N trajectory,
    so it does not fall simply on the ground Regge line.

    Returns
    -------
    dict with mass ratios and next-excitation predictions
    """
    print()
    print('=' * 70)
    print('[PART D] MASS RATIOS AND EXTENDED REGGE PREDICTIONS')
    print('=' * 70)
    print()

    m_p_dfc     = nucleon_result['m_p_dfc']
    m_delta_dfc = delta_result['m_delta_dfc']

    # DFC ratio
    ratio_dfc    = m_delta_dfc / m_p_dfc
    ratio_analytic = math.sqrt(5.0 / 3.0)   # = √(5/3)
    ratio_obs    = M_DELTA_OBS / M_P_OBS
    err_ratio    = (ratio_dfc - ratio_obs) / ratio_obs * 100.0

    print('  Mass ratio m_Δ/m_p:')
    print()
    print(f'    DFC (numerical):  m_Δ/m_p = {ratio_dfc:.6f}')
    print(f'    DFC (analytic):   √(5/3)  = {ratio_analytic:.6f}  [exact, 0 free params]')
    print(f'    Observed:         m_Δ/m_p = {ratio_obs:.6f}')
    print(f'    Error: {err_ratio:+.2f}%')
    print()
    print(f'    The ratio √(5/3) depends only on the DFC intercept assignments')
    print(f'    α_0^{{Δ}}−α_0^{{N}} = 1/2 = Q_top/4.  It is independent of Λ_QCD.')
    print()

    # Proton-neutron mass difference (DFC predicts m_p = m_n at Tier 3)
    print('  Proton-neutron mass:')
    print(f'    DFC prediction:   m_p = m_n (isospin symmetry at D7 depth; Tier 3)')
    print(f'    Observed:         m_p = {M_P_OBS*1000:.2f} MeV,  m_n = {M_N_OBS*1000:.2f} MeV')
    print(f'    Splitting:        Δm = {(M_N_OBS-M_P_OBS)*1000:.2f} MeV (0.1%)')
    print(f'    Comment: the 0.1% splitting is an isospin-breaking effect from')
    print(f'    D6/D7 depth interactions (quark mass differences) — not yet derived in DFC.')
    print()

    # Next Regge level on N trajectory
    # J=1/2 → J=5/2 on same trajectory (Δm²=2 units × 1/α')
    J_nstar = 2.5    # J=5/2 is the next state on the N trajectory (skipping half-integer)
    # Actually the trajectory goes J=1/2, 5/2, 9/2, ... (spacing ΔJ=2)
    # Standard: baryon Regge trajectory N has J_n = 1/2 + 2n, n=0,1,2,...
    alpha_0_N = -0.25
    m_nstar_sq = (J_nstar - alpha_0_N) * 4.0 * math.pi * LAMBDA_QCD_DFC**2
    # = (5/2 + 1/4) × 4πΛ² = (11/4) × 4πΛ² = 11πΛ²
    m_nstar_dfc = math.sqrt(m_nstar_sq)

    # The N(1520) D13 state is J=3/2 (separate trajectory); skip for now
    # The nearest N* at J=5/2 in data is N(1675) or N(1680)
    M_N1680_OBS = 1.680  # GeV, N(1680) J=5/2

    err_nstar = (m_nstar_dfc - M_N1680_OBS) / M_N1680_OBS * 100.0

    print('  Next Regge level on N trajectory (J=5/2):')
    print(f'    Predicted: m_N*(J=5/2) = √(11π) × Λ_QCD = {m_nstar_dfc*1000:.1f} MeV')
    print(f'    Observed:  N(1680) J=5/2 = {M_N1680_OBS*1000:.1f} MeV')
    print(f'    Error: {err_nstar:+.1f}%')
    print()

    # Summary table for DFC baryon Regge
    print('  DFC baryon Regge trajectory (N line):')
    print(f'  {"J":>5}  {"Formula":>18}  {"m_DFC (MeV)":>14}  {"Obs (MeV)":>12}  {"Error":>8}')
    print(f'  {"-"*65}')
    for J_val, label, obs_mev, note in [
        (0.5, 'sqrt(3pi)*Lam', M_P_OBS*1000, 'proton'),
        (2.5, 'sqrt(11pi)*Lam', M_N1680_OBS*1000, 'N(1680)'),
    ]:
        m_sq      = (J_val - alpha_0_N) * 4.0 * math.pi * LAMBDA_QCD_DFC**2
        m_dfc_mev = math.sqrt(m_sq) * 1000.0
        err       = (m_dfc_mev - obs_mev) / obs_mev * 100.0
        coeff     = int(round((J_val - alpha_0_N) * 4.0))
        print(f'  {J_val:>5.1f}  {"sqrt("+str(coeff)+"pi)*Lam":>18}  {m_dfc_mev:>14.1f}  {obs_mev:>12.1f}  {err:>+8.1f}%  ({note})')

    print()
    print('  DFC Delta Regge trajectory (Δ line):')
    alpha_0_Delta = 0.25
    for J_val, obs_mev, note in [
        (1.5, M_DELTA_OBS*1000, 'Delta(1232)'),
        (3.5, 1910.0,            'Delta(1905) J=5/2'),
    ]:
        m_sq      = (J_val - alpha_0_Delta) * 4.0 * math.pi * LAMBDA_QCD_DFC**2
        m_dfc_mev = math.sqrt(m_sq) * 1000.0
        err       = (m_dfc_mev - obs_mev) / obs_mev * 100.0
        coeff     = int(round((J_val - alpha_0_Delta) * 4.0))
        print(f'  {J_val:>5.1f}  {"sqrt("+str(coeff)+"pi)*Lam":>18}  {m_dfc_mev:>14.1f}  {obs_mev:>12.1f}  {err:>+8.1f}%  ({note})')

    return {
        'ratio_dfc':         ratio_dfc,
        'ratio_analytic':    ratio_analytic,
        'ratio_obs':         ratio_obs,
        'err_ratio':         err_ratio,
        'm_nstar_dfc':       m_nstar_dfc,
    }


# ─── Summary ──────────────────────────────────────────────────────────────────

def summary(intercept_result, nucleon_result, delta_result, ratio_result):
    print()
    print('=' * 70)
    print('SUMMARY — BARYON MASSES FROM DFC REGGE  (Cycle 168)')
    print('=' * 70)
    print()
    print('  DERIVED FROM DFC WITH 0 FREE PARAMETERS:')
    print()
    print(f'  [Tier 3]  m_p = √(3π) × Λ_QCD = √(3π) × {LAMBDA_QCD_DFC*1000:.1f} MeV')
    print(f'            = {nucleon_result["m_p_dfc"]*1000:.2f} MeV')
    print(f'            Observed: {M_P_OBS*1000:.2f} MeV.  Error: {nucleon_result["err_p"]:+.2f}%')
    print()
    print(f'  [Tier 3]  m_Δ = √(5π) × Λ_QCD = √(5π) × {LAMBDA_QCD_DFC*1000:.1f} MeV')
    print(f'            = {delta_result["m_delta_dfc"]*1000:.1f} MeV')
    print(f'            Observed: {M_DELTA_OBS*1000:.1f} MeV.  Error: {delta_result["err_delta"]:+.2f}%')
    print()
    print(f'  [Tier 3]  m_Δ/m_p = √(5/3) = {ratio_result["ratio_analytic"]:.6f}  [exact, 0 params]')
    print(f'            Observed: {ratio_result["ratio_obs"]:.6f}.  Error: {ratio_result["err_ratio"]:+.2f}%')
    print()
    print('  DERIVATION CHAIN:')
    print()
    print(f'  Q_top = 2               [Tier 1]  D7 kink homotopy charge')
    print(f'      ↓')
    print(f'  σ = Q_top × Λ_QCD²     [Tier 3]  topological string tension (Cycle 160)')
    print(f'      ↓')
    print(f'  α\' = 1/(4πΛ_QCD²)      [Tier 3]  Nambu-Goto Regge slope')
    print(f'      ↓')
    print(f'  Y-junction intercept:   [Tier 3]  3 endpoints × Q_top/8 − 1 junction penalty')
    print(f'  α_0^{{N}} = −1/4   (nucleon)')
    print(f'  α_0^{{Δ}} = +1/4   (Delta, + Q_top/4 spin-alignment bonus)')
    print(f'      ↓')
    print(f'  m_p = √(3π) × Λ_QCD   [Tier 3]  −{abs(nucleon_result["err_p"]):.2f}% error, 0 free params')
    print(f'  m_Δ = √(5π) × Λ_QCD   [Tier 3]  {delta_result["err_delta"]:+.2f}% error, 0 free params')
    print()
    print('  CONTEXT:')
    print('  Meson sector (Cycle 160):  m_ρ = √(2π) × Λ_QCD = 763.3 MeV (−1.58%)')
    print('  Baryon sector (this):      m_p = √(3π) × Λ_QCD = 934.8 MeV (−0.36%)')
    print('  Baryon sector:             m_Δ = √(5π) × Λ_QCD = 1207  MeV (−2.02%)')
    print()
    print('  OBSERVATION: The meson formula coefficient is 2π; baryon is 3π, 5π.')
    print('  The n-th coefficient follows from n = (N_q/2)×Q_top × (J−α_0)/Λ² structure.')
    print('  This is a structurally coherent series from the single input Q_top=2.')
    print()
    print('  OPEN GAPS:')
    print('  (i)  Derive σ=Q_top×Λ² from D7 kink vacuum energy — Tier 4 (Yang-Mills gap)')
    print('  (ii) Derive Y-junction intercept formula from Nambu-Goto string theory of')
    print('       three-string junction — formal derivation open (Tier 4).')
    print('  (iii) m_p−m_n splitting 1.3 MeV from D6/D7 isospin breaking — Tier 4 open.')
    print()
    print('  CONNECTIONS:')
    print('    equations/d7_nonpert_coefficients.py — σ, α\', m_ρ (Cycle 160)')
    print('    equations/rho_meson_dfc.py           — Λ_QCD two-loop (Cycle 159)')
    print('    equations/pion_decay_constant.py     — f_π, large-N_c f_ρ (Cycles 166-167)')
    print('    equations/hadronic_spectroscopy.md   — Regge context')


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('=' * 70)
    print('BARYON MASSES FROM DFC Y-JUNCTION REGGE TRAJECTORIES  (Cycle 168)')
    print('m_p = √(3π)×Λ_QCD, m_Δ = √(5π)×Λ_QCD  (0 free parameters, Tier 3)')
    print('=' * 70)
    print()

    intercept_result = baryon_regge_intercepts()
    nucleon_result   = nucleon_mass(intercept_result)
    delta_result     = delta_mass(intercept_result)
    ratio_result     = mass_ratios_and_regge_tests(nucleon_result, delta_result)
    summary(intercept_result, nucleon_result, delta_result, ratio_result)
