"""
Hydrogen Spectrum from DFC Substrate Parameters
================================================

Physical question:
    What is the ground state energy of hydrogen? What are the spectral line
    energies for the Balmer and Lyman series? These are the most basic predictions
    of the DFC EM sector combined with the quantum (bound state) sector.

DFC mechanism:
    The electron is a D5+D6 kink whose free propagation follows the Klein-Gordon
    equation. In the Coulomb field of the proton (the 1/r field produced by the
    proton's D5 U(1) winding number), the electron has bound states with energies
    that depend only on the principal quantum number n. The energy scale is set by
    the fine structure constant alpha_em — the dimensionless ratio of the
    electromagnetic coupling strength to the quantum of action.

    Chain:
        β → g² = 8πβ/3 → g_common at M_c(12)
        → SU(2) coupling at M_Z → α_em(M_Z) = α₂ × sin²θ_W
        → QED running (one-loop) → α_em(m_e) ≈ 1/137
        → E_n = -m_e c² α²/(2n²)

    The one-loop QED running from M_Z to m_e is standard (not DFC-specific).
    The α_em(M_Z) value is the DFC prediction; the running to α_em(0) is
    the same QED beta function used in the SM.

Key result:
    DFC predicts α_em(0) ≈ 1/140 (observed: 1/137.036, 2.2% off).
    DFC predicts E_1 = -13.04 eV (observed: -13.606 eV, 4.5% off).
    Lyman-alpha wavelength: DFC 126.8 nm (observed 121.6 nm, 4.3% off).

Status:
    Tier 2b (quantitative prediction — currently failing at 4.5%).
    The error propagates from the 1.3% error in α_em(M_Z) through α².
    Improving α_em(M_Z) to < 0.5% would bring E_1 to < 1% precision.

References:
    - phenomena/quantum/atomic_structure.md
    - equations/coupling_derivation.py     (α_em(M_Z) ← β)
    - phenomena/electromagnetism/electromagnetism.md
    - foundations/mass_hierarchy.md        (m_e as substrate input)
"""

import math
import sys
import os

# Allow import of coupling_derivation from this directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coupling_derivation import coupling_chain_from_beta, BETA


# ─────────────────────────────────────────────────────────────────────────────
# Physical constants (inputs, not DFC predictions)
# ─────────────────────────────────────────────────────────────────────────────

M_E_MEV     = 0.51099895       # electron mass in MeV (PDG 2024; input from mass_spectrum.py)
M_E_EV      = M_E_MEV * 1e6   # electron rest mass energy in eV
HC_EV_NM    = 1239.84193       # hc in eV·nm (input — requires ℏ)
M_Z_MEV     = 91187.6          # Z boson mass in MeV
ALPHA_OBS_0 = 1.0 / 137.035999084  # observed fine structure constant at q²→0

# Observed hydrogen energy levels (PDG / NIST)
E_GROUND_OBS_EV = -13.5984     # ground state energy in eV (ionization energy)


# ─────────────────────────────────────────────────────────────────────────────
# Section 1: QED running from M_Z to m_e
# ─────────────────────────────────────────────────────────────────────────────

def qed_running(alpha_mz, mu_high_mev=M_Z_MEV, mu_low_mev=M_E_MEV):
    """
    Run alpha_em from mu_high down to mu_low using one-loop QED.

    The one-loop QED beta function is:
        d(1/α) / d(ln μ) = -(2/3π) × Σ_f N_c Q_f²   [sum over fermions with m_f < μ]

    As the scale decreases, 1/α increases (alpha decreases).

    Integrating in steps from M_Z down to m_e, with threshold matching
    at each fermion mass:

        1/α(m_e) = 1/α(M_Z) + (2/3π) × Σ_f N_c Q_f² × ln(M_Z / m_f)

    The sum runs over all charged fermions lighter than M_Z:
        Leptons:  e (0.511 MeV), μ (105.7 MeV), τ (1776.9 MeV)
        Quarks:   u (2.16 MeV), d (4.67 MeV), s (93.4 MeV), c (1270 MeV),
                  b (4180 MeV), [t excluded: m_t = 172760 MeV > M_Z]

    Parameters
    ----------
    alpha_mz : float   Fine structure constant at M_Z (DFC input).
    mu_high_mev : float  Upper scale in MeV (default: M_Z).
    mu_low_mev  : float  Lower scale in MeV (default: m_e).

    Returns
    -------
    dict with α at low scale and running details.
    """

    # Fermion content: (name, N_c, Q², mass_MeV)
    fermions = [
        ("e",    1, 1.0,     0.51099895),
        ("mu",   1, 1.0,     105.6583755),
        ("tau",  1, 1.0,     1776.86),
        ("u",    3, 4.0/9,   2.16),
        ("d",    3, 1.0/9,   4.67),
        ("s",    3, 1.0/9,   93.4),
        ("c",    3, 4.0/9,   1270.0),
        ("b",    3, 1.0/9,   4180.0),
        # top (m_t = 172760 MeV > M_Z = 91188 MeV): not included
    ]

    delta_inv_alpha = 0.0
    contributions = []

    for (name, nc, q2, m_mev) in fermions:
        if m_mev >= mu_high_mev:
            contributions.append((name, nc, q2, m_mev, 0.0))
            continue

        # The contribution to Δ(1/α) from this fermion running from μ=m_f to μ=M_Z:
        #   (2/3π) × N_c × Q² × ln(M_Z / m_f)
        ln_factor = math.log(mu_high_mev / m_mev)
        contrib = (2.0 / (3.0 * math.pi)) * nc * q2 * ln_factor
        delta_inv_alpha += contrib
        contributions.append((name, nc, q2, m_mev, contrib))

    inv_alpha_high = 1.0 / alpha_mz
    inv_alpha_low  = inv_alpha_high + delta_inv_alpha
    alpha_low      = 1.0 / inv_alpha_low

    return {
        'alpha_at_mz':        alpha_mz,
        'inv_alpha_at_mz':    inv_alpha_high,
        'delta_inv_alpha':    delta_inv_alpha,
        'inv_alpha_at_me':    inv_alpha_low,
        'alpha_at_me':        alpha_low,
        'contributions':      contributions,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Section 2: Hydrogen energy levels
# ─────────────────────────────────────────────────────────────────────────────

def hydrogen_energy_levels(alpha_em, m_e_ev=M_E_EV, n_max=6):
    """
    Compute hydrogen energy levels E_n = -m_e c² α²/(2n²).

    This is the non-relativistic Schrödinger (or leading-order Dirac) result.
    The formula follows from quantization of the Coulomb bound state — the
    condition that the wavefunction be normalizable restricts n to positive
    integers. The energy depends only on n at leading order.

    Parameters
    ----------
    alpha_em : float   Fine structure constant.
    m_e_ev   : float   Electron rest mass energy in eV.
    n_max    : int     Maximum principal quantum number to compute.

    Returns
    -------
    dict with energy levels and Rydberg energy.
    """
    # Rydberg energy: E_Ry = m_e c² α² / 2
    E_Ry = m_e_ev * alpha_em**2 / 2.0

    levels = {}
    for n in range(1, n_max + 1):
        levels[n] = -E_Ry / n**2

    return {
        'alpha_em':  alpha_em,
        'E_Ry_ev':   E_Ry,
        'E_Ry_formula': 'E_Ry = m_e c² α²/2',
        'levels_ev': levels,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Section 3: Spectral series
# ─────────────────────────────────────────────────────────────────────────────

def spectral_series(levels_ev, hc_ev_nm=HC_EV_NM):
    """
    Compute transition energies and wavelengths for the main hydrogen series.

    Each spectral line corresponds to a transition n_upper → n_lower.
    The photon energy is the difference in energy levels.
    The wavelength uses hc = 1239.84 eV·nm (input — requires ℏ).

    Series:
        Lyman  (n_lower = 1): UV transitions to ground state
        Balmer (n_lower = 2): visible/near-UV transitions
        Paschen (n_lower = 3): infrared transitions

    Parameters
    ----------
    levels_ev : dict   Energy levels {n: E_n} in eV.
    hc_ev_nm  : float  Planck constant × speed of light in eV·nm (input).

    Returns
    -------
    dict with series of transitions.
    """
    series_def = {
        'Lyman':   {'n_low': 1, 'n_high_range': range(2, 7)},
        'Balmer':  {'n_low': 2, 'n_high_range': range(3, 8)},
        'Paschen': {'n_low': 3, 'n_high_range': range(4, 8)},
    }

    series_out = {}
    for (series_name, params) in series_def.items():
        n_low = params['n_low']
        transitions = []
        for n_high in params['n_high_range']:
            if n_high not in levels_ev or n_low not in levels_ev:
                continue
            delta_E = levels_ev[n_high] - levels_ev[n_low]   # positive (emission)
            wavelength_nm = hc_ev_nm / delta_E
            transitions.append({
                'n_upper':      n_high,
                'n_lower':      n_low,
                'delta_E_ev':   delta_E,
                'wavelength_nm': wavelength_nm,
            })
        series_out[series_name] = transitions

    return series_out


# ─────────────────────────────────────────────────────────────────────────────
# Reference values for comparison
# ─────────────────────────────────────────────────────────────────────────────

# Observed wavelengths (NIST, vacuum), nm
OBS_WAVELENGTHS = {
    # Lyman series (n → 1)
    ('Lyman',   2, 1): 121.567,
    ('Lyman',   3, 1): 102.572,
    ('Lyman',   4, 1): 97.254,
    # Balmer series (n → 2)
    ('Balmer',  3, 2): 656.279,   # H-alpha (red)
    ('Balmer',  4, 2): 486.133,   # H-beta (blue-green)
    ('Balmer',  5, 2): 434.047,   # H-gamma (violet)
    ('Balmer',  6, 2): 410.174,   # H-delta
    # Paschen series (n → 3)
    ('Paschen', 4, 3): 1875.10,
    ('Paschen', 5, 3): 1281.81,
}


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print()
    print("=" * 70)
    print("  HYDROGEN SPECTRUM FROM DFC SUBSTRATE PARAMETERS")
    print("=" * 70)
    print()

    # Step 1: Get α_em(M_Z) from DFC coupling chain
    print("Step 1: α_em(M_Z) from DFC coupling derivation")
    print("-" * 50)
    chain = coupling_chain_from_beta(BETA)
    alpha_mz_dfc = chain['alpha_em_mz']
    print(f"  β (substrate quartic coupling)  = {BETA:.4f}")
    print(f"  g² = 8πβ/3                      = {chain['g_common']**2:.6f}")
    print(f"  α_em(M_Z) from DFC              = {alpha_mz_dfc:.6f}  (1/{1/alpha_mz_dfc:.2f})")
    print(f"  α_em(M_Z) observed              = 0.007818  (1/127.9)")
    print(f"  Error:                            {100*abs(alpha_mz_dfc - 0.007818)/0.007818:.2f}%")
    print()

    # Step 2: QED running from M_Z to m_e
    print("Step 2: QED running from M_Z → m_e (one-loop threshold matching)")
    print("-" * 50)
    running = qed_running(alpha_mz_dfc)

    print(f"  {'Fermion':<8}  {'N_c':>4}  {'Q²':>6}  {'m (MeV)':>12}  {'Δ(1/α)':>9}")
    print(f"  {'-'*8}  {'-'*4}  {'-'*6}  {'-'*12}  {'-'*9}")
    for (name, nc, q2, m_mev, contrib) in running['contributions']:
        print(f"  {name:<8}  {nc:>4}  {q2:>6.4f}  {m_mev:>12.4f}  {contrib:>9.4f}")
    print(f"  {'':8}  {'':4}  {'':6}  {'Total Δ(1/α):':>12}  {running['delta_inv_alpha']:>9.4f}")
    print()
    print(f"  1/α at M_Z (DFC)    = {running['inv_alpha_at_mz']:.4f}")
    print(f"  + Δ(1/α) from QED   = {running['delta_inv_alpha']:.4f}")
    print(f"  1/α at m_e (DFC)    = {running['inv_alpha_at_me']:.4f}")
    print(f"  1/α at m_e observed = {1/ALPHA_OBS_0:.4f}")
    print(f"  Error:               {100*abs(running['alpha_at_me'] - ALPHA_OBS_0)/ALPHA_OBS_0:.2f}%")
    print()

    # Step 3: Hydrogen energy levels
    print("Step 3: Hydrogen energy levels E_n = -m_e c² α²/(2n²)")
    print("-" * 50)
    alpha_me_dfc = running['alpha_at_me']
    alpha_me_obs = ALPHA_OBS_0

    hl_dfc = hydrogen_energy_levels(alpha_me_dfc)
    hl_obs = hydrogen_energy_levels(alpha_me_obs)

    print(f"  Rydberg energy (DFC):  E_Ry = {hl_dfc['E_Ry_ev']:.4f} eV")
    print(f"  Rydberg energy (obs):  E_Ry = {hl_obs['E_Ry_ev']:.4f} eV")
    print(f"  Error:                 {100*abs(hl_dfc['E_Ry_ev'] - hl_obs['E_Ry_ev'])/hl_obs['E_Ry_ev']:.2f}%")
    print()
    print(f"  {'n':>3}  {'E_n (DFC, eV)':>16}  {'E_n (obs, eV)':>15}  {'Error':>8}")
    print(f"  {'-'*3}  {'-'*16}  {'-'*15}  {'-'*8}")
    for n in range(1, 7):
        e_dfc = hl_dfc['levels_ev'][n]
        e_obs = hl_obs['levels_ev'][n]
        err = 100 * abs(e_dfc - e_obs) / abs(e_obs)
        print(f"  {n:>3}  {e_dfc:>16.4f}  {e_obs:>15.4f}  {err:>7.2f}%")
    print()

    # Step 4: Spectral series
    print("Step 4: Spectral series wavelengths")
    print("-" * 70)
    series_dfc = spectral_series(hl_dfc['levels_ev'])
    series_obs = spectral_series(hl_obs['levels_ev'])

    # Named lines for prominent series
    line_names = {
        ('Lyman',  2, 1): 'Ly-α',
        ('Lyman',  3, 1): 'Ly-β',
        ('Balmer', 3, 2): 'H-α (red)',
        ('Balmer', 4, 2): 'H-β (blue)',
        ('Balmer', 5, 2): 'H-γ (violet)',
        ('Balmer', 6, 2): 'H-δ',
        ('Paschen',4, 3): 'Pa-α',
    }

    print(f"  {'Series':<8} {'n':>4}→{'n':>2}  {'Name':<14}  {'DFC (nm)':>10}  {'Obs (nm)':>10}  {'Error':>8}")
    print(f"  {'-'*8} {'-'*4} {'-'*2}  {'-'*14}  {'-'*10}  {'-'*10}  {'-'*8}")

    for series_name in ['Lyman', 'Balmer', 'Paschen']:
        for t_dfc in series_dfc[series_name]:
            n_up = t_dfc['n_upper']
            n_lo = t_dfc['n_lower']

            key = (series_name, n_up, n_lo)
            obs_wl = OBS_WAVELENGTHS.get(key)
            if obs_wl is None:
                continue

            dfc_wl = t_dfc['wavelength_nm']
            err = 100 * abs(dfc_wl - obs_wl) / obs_wl
            name = line_names.get(key, '')
            print(f"  {series_name:<8} {n_up:>4}→{n_lo:<2}  {name:<14}  {dfc_wl:>10.3f}  {obs_wl:>10.3f}  {err:>7.2f}%")

    print()

    # Step 5: Error budget
    print("Step 5: Error budget")
    print("-" * 50)
    err_alpha_mz = 100 * abs(alpha_mz_dfc - 0.007818) / 0.007818
    err_alpha_me = 100 * abs(alpha_me_dfc - ALPHA_OBS_0) / ALPHA_OBS_0
    err_e1 = 100 * abs(hl_dfc['levels_ev'][1] - E_GROUND_OBS_EV) / abs(E_GROUND_OBS_EV)
    print(f"  α_em(M_Z) error:   {err_alpha_mz:.2f}%")
    print(f"  α_em(m_e) error:   {err_alpha_me:.2f}%  [after QED running]")
    print(f"  E_1 error:         {err_e1:.2f}%  [E_1 ∝ α², so ~2× the α error]")
    print()
    print("  Source of error: α_em(M_Z) from DFC is 1.3% below observed.")
    print("  QED running adds ~10.5 to 1/α → DFC 1/α(m_e) ≈ 140 vs obs 137.")
    print("  The α² dependence doubles the relative error in energy levels.")
    print()
    print("  Improving α_em(M_Z) to < 0.5% would bring E_1 to < 1% precision.")
    print("  Required: rigorous derivation of r_U1/λ = 3/(4β) from substrate.")
    print()

    print("=" * 70)
    print("SUMMARY TABLE (Tier 2b predictions — quantitative, currently failing)")
    print("=" * 70)
    print()
    print(f"  {'Quantity':<28}  {'DFC':>12}  {'Observed':>12}  {'Error':>8}  {'Status'}")
    print(f"  {'-'*28}  {'-'*12}  {'-'*12}  {'-'*8}  {'-'*10}")
    rows = [
        ("α_em(M_Z)",       f"1/{1/alpha_mz_dfc:.1f}",  "1/127.9",  f"{err_alpha_mz:.1f}%", "✗ 1.3% off"),
        ("α_em(0) = 1/137", f"1/{1/alpha_me_dfc:.1f}",  "1/137.0",  f"{err_alpha_me:.1f}%", "✗ 2.2% off"),
        ("E_1 (ground state)", f"{hl_dfc['levels_ev'][1]:.3f} eV",
                              f"{E_GROUND_OBS_EV:.3f} eV", f"{err_e1:.1f}%", "✗ 4.5% off"),
        ("Rydberg energy",  f"{hl_dfc['E_Ry_ev']:.4f} eV",
                              "13.5984 eV",         f"{100*abs(hl_dfc['E_Ry_ev']-13.5984)/13.5984:.1f}%", "✗ 4.5% off"),
        ("Ly-α wavelength", f"{series_dfc['Lyman'][0]['wavelength_nm']:.2f} nm",
                              "121.567 nm",         f"{100*abs(series_dfc['Lyman'][0]['wavelength_nm']-121.567)/121.567:.1f}%", "✗ 4.3% off"),
        ("H-α wavelength",  f"{series_dfc['Balmer'][0]['wavelength_nm']:.2f} nm",
                              "656.279 nm",         f"{100*abs(series_dfc['Balmer'][0]['wavelength_nm']-656.279)/656.279:.1f}%", "✗ 4.3% off"),
        ("1/n² spacing", "structural", "confirmed", "0%", "✓ DERIVED"),
    ]
    for row in rows:
        print(f"  {row[0]:<28}  {row[1]:>12}  {row[2]:>12}  {row[3]:>8}  {row[4]}")
    print()
    print("  Note: all errors inherit from the 1.3% error in α_em(M_Z).")
    print("  When r_U1/λ = 3/(4β) is rigorously derived, this chain improves end-to-end.")


if __name__ == "__main__":
    main()
