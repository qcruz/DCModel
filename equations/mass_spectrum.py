"""
Lepton and quark mass predictions from geometric defect model.

In the Dimensional Folding Model, the three lepton generations arise from the
quantum mechanical modes of a fermion confined in a compact extra dimension with
a "dimple" — a small, sharp local depression in the effective potential.

  - Electron (ground state):  wavefunction concentrated at the dimple center
                               mass ∝ dimple depth  (local scale)
  - Muon (first excited):     wavefunction has a NODE at the dimple center
                               mass ∝ 1/dimension_size  (global scale)
  - Tau (second excited):     samples outer curvature
                               mass ∝ combination of both

Usage:
    python equations/mass_spectrum.py

    Or:
        from equations.mass_spectrum import predict_lepton_masses, fit_dimple_params
"""

import math
from typing import Optional

# ─── Observed Masses (PDG 2024) ───────────────────────────────────────────────

M_OBS = {
    'electron': 0.51099895,     # MeV
    'muon':     105.6583755,    # MeV
    'tau':      1776.86,        # MeV
    'up':       2.16,           # MeV
    'down':     4.67,           # MeV
    'charm':    1270.0,         # MeV
    'strange':  93.4,           # MeV
    'top':      172760.0,       # MeV
    'bottom':   4180.0,         # MeV
}

# Observed ratios
MUON_ELECTRON_RATIO = M_OBS['muon'] / M_OBS['electron']    # 206.77
TAU_MUON_RATIO      = M_OBS['tau'] / M_OBS['muon']         # 16.82
TAU_ELECTRON_RATIO  = M_OBS['tau'] / M_OBS['electron']     # 3477.2


# ─── Dimple Potential Model ───────────────────────────────────────────────────

def dimple_potential(x, depth, width, box_size):
    """
    Effective 1D potential for a fermion in a compact extra dimension with a dimple.

    V(x) = V_box(x) + V_dimple(x)

    V_box:   infinite square well from 0 to L (confining dimension)
    V_dimple: Gaussian depression centered at x=L/2

        V_dimple(x) = -depth × exp(-(x - L/2)² / (2 width²))

    Parameters
    ----------
    x : float
        Position (0 < x < box_size)
    depth : float
        Depth of the dimple in MeV (sets electron mass scale)
    width : float
        Width of the dimple (fraction of box_size, typically << 1)
    box_size : float
        Size of the extra dimension (sets muon mass scale)

    Returns
    -------
    float : potential energy in MeV
    """
    center = box_size / 2.0
    v_dimple = -depth * math.exp(-((x - center)**2) / (2 * (width * box_size)**2))
    return v_dimple


def perturbation_energies(depth, width, box_size, n_modes=3):
    """
    Compute first-order energy corrections for the lowest modes of an infinite
    square well due to the dimple perturbation.

    Unperturbed basis: ψ_n(x) = √(2/L) sin(nπx/L)

    First-order correction: E_n^(1) = ⟨n|V_dimple|n⟩

    For a narrow Gaussian dimple (width << L):
        E_n^(1) ≈ -depth × (2/L) × sin²(nπ/2) × σ√(2π)
                 = -depth × (2σ√(2π)/L) × sin²(nπ/2)

    where σ = width × L is the dimple width in absolute units.

    Key result:
        n=1 (electron): sin²(π/2) = 1.0   → full dimple correction
        n=2 (muon):     sin²(π)   = 0.0   → zero dimple correction (node at center)
        n=3 (tau):      sin²(3π/2)= 1.0   → full dimple correction again

    Parameters
    ----------
    depth : float
        Dimple depth in MeV
    width : float
        Dimple width as fraction of box_size (e.g., 0.01 = 1% of dimension)
    box_size : float
        Size of extra dimension (arbitrary length units, cancels in ratios)
    n_modes : int
        Number of modes to compute

    Returns
    -------
    list of dicts: [{mode, E_unperturbed, E_dimple_correction, E_total}, ...]
    """
    sigma = width * box_size
    # Perturbation integral: ⟨n|V|n⟩ for narrow Gaussian at center
    # ≈ -depth × (2/L) × sin²(nπ/2) × σ√(2π)
    dimple_factor = depth * (2 / box_size) * sigma * math.sqrt(2 * math.pi)

    results = []
    for n in range(1, n_modes + 1):
        # Unperturbed energy: E_n = n² π² ℏ²c² / (2 m L²)
        # For now, working in units where E_n is in terms of (πℏc/L)²
        # We'll parameterize the actual mass scale separately.
        E_unperturbed_units = n**2  # in units of π²ℏ²c²/(2mL²)

        # Node factor: sin²(nπ/2)
        node_factor = math.sin(n * math.pi / 2)**2

        E_correction_units = -dimple_factor / (depth) * node_factor * depth
        # Simplify: correction = -dimple_factor × sin²(nπ/2)
        E_correction = -dimple_factor * node_factor

        results.append({
            'mode': n,
            'name': {1: 'electron', 2: 'muon', 3: 'tau'}.get(n, f'mode_{n}'),
            'E_unperturbed_units': E_unperturbed_units,
            'E_dimple_correction': E_correction,
            'node_factor': node_factor,
        })

    return results


def predict_lepton_masses(dimple_depth_mev: float, box_mass_mev: float,
                          dimple_width_frac: float = 0.02):
    """
    Predict electron, muon, and tau masses from two geometric parameters.

    The electron mass comes primarily from the dimple correction.
    The muon mass comes primarily from the box energy (no dimple).
    The tau mass includes both contributions.

    This is a first-order perturbation theory estimate. The two free parameters
    (dimple_depth_mev, box_mass_mev) should be fixed by fitting to the electron
    and muon masses, then the tau is a prediction.

    Parameters
    ----------
    dimple_depth_mev : float
        Sets the electron mass scale. Roughly m_electron ~ f × dimple_depth_mev
        where f depends on dimple_width_frac.
    box_mass_mev : float
        The energy scale of the lowest mode of the box (without dimple).
        Roughly m_muon ~ 4 × box_mass_mev  (n=2 mode, no dimple)
    dimple_width_frac : float
        Width of the dimple as fraction of box size. Default 0.02 (2%).

    Returns
    -------
    dict with predicted masses and comparison to observations.
    """
    # Using box_size = 1.0 (normalized); energy scale set by box_mass_mev
    box_size = 1.0

    # Perturbation corrections
    modes = perturbation_energies(dimple_depth_mev, dimple_width_frac, box_size, n_modes=3)

    # Mode energies in physical units:
    # E_n(physical) = n² × box_mass_mev  +  E_dimple_correction(n)
    # The dimple correction is already in MeV (dimple_depth_mev sets its scale)
    #
    # Box contribution: E_n,box = n² × box_mass_mev
    # (lowest mode = box_mass_mev, second mode = 4 × box_mass_mev, etc.)

    E_box = [n**2 * box_mass_mev for n in [1, 2, 3]]
    E_corr = [m['E_dimple_correction'] for m in modes]

    m_electron_pred = abs(E_box[0] + E_corr[0])
    m_muon_pred     = abs(E_box[1] + E_corr[1])  # E_corr[1] = 0 (node at dimple)
    m_tau_pred      = abs(E_box[2] + E_corr[2])

    return {
        'dimple_depth_mev':    dimple_depth_mev,
        'box_mass_mev':        box_mass_mev,
        'dimple_width_frac':   dimple_width_frac,

        'electron': {
            'predicted_mev': m_electron_pred,
            'observed_mev':  M_OBS['electron'],
            'ratio':         m_electron_pred / M_OBS['electron'],
        },
        'muon': {
            'predicted_mev': m_muon_pred,
            'observed_mev':  M_OBS['muon'],
            'ratio':         m_muon_pred / M_OBS['muon'],
        },
        'tau': {
            'predicted_mev': m_tau_pred,
            'observed_mev':  M_OBS['tau'],
            'ratio':         m_tau_pred / M_OBS['tau'],
        },

        'muon_electron_ratio_pred': m_muon_pred / m_electron_pred,
        'muon_electron_ratio_obs':  MUON_ELECTRON_RATIO,
        'tau_muon_ratio_pred':      m_tau_pred / m_muon_pred,
        'tau_muon_ratio_obs':       TAU_MUON_RATIO,
    }


def fit_dimple_params():
    """
    Find the dimple parameters that reproduce the observed electron and muon masses,
    then predict the tau mass.

    Two constraints:
        m_electron ≈ dimple_depth × (2/L × σ√2π)       (dimple sets electron mass)
        m_muon     ≈ 4 × box_mass_mev                    (box mode, no dimple)

    From these:
        box_mass_mev = m_muon / 4
        dimple_depth = m_electron / (normalization factor)

    Then tau is a prediction.

    Returns
    -------
    dict with fitted parameters and tau prediction.
    """
    # From muon mass: n=2 box mode = 4 × E_1,box → E_1,box = m_muon/4
    # (at zeroth order with no dimple)
    box_mass_from_muon = M_OBS['muon'] / 4.0  # ~26.4 MeV

    # From electron mass: need dimple to shift down by (box_mass_from_muon - m_electron)
    delta_needed = box_mass_from_muon - M_OBS['electron']   # ~25.9 MeV

    # For dimple_width_frac = 0.02:
    #   E_correction(n=1) = -depth × (2/1.0) × (0.02×1.0)×√(2π) × sin²(π/2)
    #                      = -depth × 2 × 0.02 × 2.507 × 1.0
    #                      = -depth × 0.1003
    width = 0.02
    sigma = width * 1.0
    norm = 2.0 * sigma * math.sqrt(2 * math.pi) * 1.0  # sin²(π/2) = 1
    dimple_depth_fitted = delta_needed / norm

    result = predict_lepton_masses(dimple_depth_fitted, box_mass_from_muon, width)

    result['fit_notes'] = [
        f"box_mass_mev fitted from m_muon/4 = {box_mass_from_muon:.3f} MeV",
        f"dimple_depth fitted to match m_electron = {dimple_depth_fitted:.3f} MeV",
        f"tau mass is a PREDICTION — no free parameters used",
    ]

    return result


# ─── Main Output ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("LEPTON MASS SPECTRUM — GEOMETRIC DEFECT MODEL")
    print("Dimensional Folding Model")
    print("=" * 60)

    print("\n--- Observed Mass Ratios (target) ---")
    print(f"  m_muon / m_electron = {MUON_ELECTRON_RATIO:.2f}")
    print(f"  m_tau  / m_muon     = {TAU_MUON_RATIO:.2f}")
    print(f"  m_tau  / m_electron = {TAU_ELECTRON_RATIO:.1f}")

    print("\n--- Fitted Parameters ---")
    fit = fit_dimple_params()
    for note in fit['fit_notes']:
        print(f"  {note}")

    print("\n--- Mass Predictions ---")
    for particle in ['electron', 'muon', 'tau']:
        d = fit[particle]
        status = "INPUT" if particle in ['electron', 'muon'] else "PREDICTION"
        print(f"  {particle:10s}:  predicted {d['predicted_mev']:10.3f} MeV   "
              f"observed {d['observed_mev']:10.3f} MeV   "
              f"ratio {d['ratio']:.3f}   [{status}]")

    print("\n--- Key Ratios ---")
    print(f"  muon/electron  predicted: {fit['muon_electron_ratio_pred']:.2f}  "
          f"observed: {fit['muon_electron_ratio_obs']:.2f}")
    print(f"  tau/muon       predicted: {fit['tau_muon_ratio_pred']:.2f}  "
          f"observed: {fit['tau_muon_ratio_obs']:.2f}")

    print("\n--- Physical Interpretation ---")
    print("  Electron mass scale: LOCAL (dimple depth)")
    print("  Muon mass scale:     GLOBAL (box/dimension size)")
    print("  Tau mass scale:      BOTH (second excited mode)")
    print("\n  The 207× ratio between muon and electron is natural because")
    print("  dimple depth and dimension size are geometrically independent.")

    print("\n--- Sensitivity Analysis ---")
    print("  Effect of varying dimple depth ±10%:")
    base = fit_dimple_params()
    depth_base = base['dimple_depth_mev']
    box_base   = base['box_mass_mev']
    for factor in [0.9, 1.0, 1.1]:
        r = predict_lepton_masses(depth_base * factor, box_base)
        print(f"    depth × {factor:.1f}: e={r['electron']['predicted_mev']:.3f}  "
              f"μ={r['muon']['predicted_mev']:.1f}  "
              f"τ={r['tau']['predicted_mev']:.1f} MeV")
