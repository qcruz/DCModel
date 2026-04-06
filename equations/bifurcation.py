"""
Bifurcation sequence — dimensional emergence from compression instabilities.

This module formalizes the process by which successive bifurcation events create
new dimensional layers (D1 → D2 → D3 → D4 → ...). Each bifurcation occurs when
the compression field exceeds a critical threshold and a new orthogonal mode becomes
stable.

Core claim being formalized:
  Each dimensional layer is a stable eigenmode of the compression field that
  emerges when compression exceeds a critical value at the previous layer's
  threshold. The dimensional stack is the sequence of these eigenmodes, ordered
  by the compression level at which they become stable.

Key quantities:
  C_n    = critical compression for the n-th bifurcation (creates D(n+1))
  Λ_n    = energy/length scale of the n-th layer
  ω_n    = characteristic frequency of the n-th mode
  Γ_n    = folding rate at the n-th threshold

The sequence of thresholds determines:
  - Why exactly 4 macroscopic dimensions emerge (D1→D4)
  - What the energy scale of each layer is
  - Why higher layers (D5+) are internal rather than macroscopic

STATUS: The existence and ordering of bifurcations is well-motivated.
The precise threshold values C_n and their derivation from the substrate
parameters (α, β, c) is an open problem.

Usage:
    python equations/bifurcation.py
"""

import math

# ── Provisional dimensional layer assignments ─────────────────────────────────

# Effective depth index and characteristic energy scale of each layer
# These are provisional fits to the observed particle spectrum
# (see foundations/dimensional_stack.md)
#
# NOTE ON D-LABEL AMBIGUITY (TWO INCOMPATIBLE SCHEMES):
#
# Scheme A (THIS FILE): D-labels index particle mass scales.
#   D5 = electron (0.511 MeV), D6 = muon (105.7 MeV), D7 = LAMBDA_QCD (0.2 GeV)
#   D10 = electroweak scale (246 GeV)
#
# Scheme B (equations/depth_running.py, Route 3B, all Weinberg angle work):
#   D5 = U(1) gauge closure at M_c ~ 10^13 GeV
#   D6 = SU(2) closure (co-crystallizes with D5)
#   D7 = SU(3) closure at ~ 8 x 10^14 GeV
#
# These are DIFFERENT MAPPINGS of the same continuous substrate. Do NOT mix
# D-labels from the two schemes. All quantitative predictions (Weinberg angle,
# hypercharge normalization, depth-running) use Scheme B.
#
# The unification of both schemes — showing how Scheme B gauge closure thresholds
# determine the Scheme A particle mass spectrum — is an open problem.
# See foundations/bifurcation_dynamics.md for full discussion.
#
# The assignments below (Scheme A) are phenomenological working hypotheses.

DIMENSIONAL_LAYERS = {
    1: {'name': 'Unity/Compression',    'energy_scale_gev': None,       'description': 'D1 — maximal compression, no separable structure'},
    2: {'name': 'Propagation',          'energy_scale_gev': 0.0,        'description': 'D2 — light, massless modes, EM radiation'},
    3: {'name': 'Localization',         'energy_scale_gev': 1e-9,       'description': 'D3 — position, interaction, neutrino anchoring begins'},
    4: {'name': 'Inertia/Mass',         'energy_scale_gev': 1e-3,       'description': 'D4 — mass threshold, electron mass scale'},
    5: {'name': 'Electron/Charge',      'energy_scale_gev': 5.11e-4,    'description': 'D5 — electron fully anchored, EM charge stabilized'},
    6: {'name': 'Muon',                 'energy_scale_gev': 0.1057,     'description': 'D6 — muon depth, first excited lepton state'},
    7: {'name': 'QCD Transition',       'energy_scale_gev': 0.2,        'description': 'D7 — ΛQCD, color confinement locks in'},
    8: {'name': 'Light Quarks',         'energy_scale_gev': 1.0,        'description': 'D8 — up/down/strange confinement depth'},
    9: {'name': 'Heavy Quarks',         'energy_scale_gev': 100.0,      'description': 'D9 — charm/bottom/top depths'},
   10: {'name': 'Electroweak',          'energy_scale_gev': 246.0,      'description': 'D10 — Higgs vev, EW symmetry breaking scale'},
   18: {'name': 'Closure Scale',        'energy_scale_gev': 1e18,       'description': 'D18 — force structure closure, DFC geometric scale'},
}


# ── Bifurcation threshold model ───────────────────────────────────────────────

def bifurcation_threshold(n, C0, gamma):
    """
    Critical compression level for the n-th bifurcation event.

    Provisional model: thresholds grow geometrically with layer index.

        C_n = C0 × exp(γ × n)

    where:
        C0    = compression level at first bifurcation (D1 → D2)
        γ     = growth rate of threshold between layers
        n     = layer index (1 = D1→D2, 2 = D2→D3, etc.)

    The exponential growth of thresholds means:
      - Lower layers are macroscopic (easily reached)
      - Higher layers require extreme compression (particle physics scale)
      - The sequence naturally produces a hierarchy of energy scales

    Parameters
    ----------
    n : int
        Bifurcation index (n=1 produces D2, n=2 produces D3, etc.)
    C0 : float
        Reference compression threshold (arbitrary units).
    gamma : float
        Logarithmic growth rate per layer.

    Returns
    -------
    float : compression threshold C_n.
    """
    return C0 * math.exp(gamma * n)


def energy_scale_from_threshold(C_n, C_planck, E_planck_gev=1.22e19):
    """
    Map a compression threshold to an energy scale.

    If C_Planck corresponds to the Planck energy (1.22 × 10¹⁹ GeV),
    then intermediate thresholds map to intermediate energy scales.

    E_n = E_Planck × (C_n / C_Planck)^(1/2)

    The square root reflects that energy scales as the square root of
    compression density in the buckling potential picture.

    Parameters
    ----------
    C_n : float
        Compression threshold for layer n.
    C_planck : float
        Compression threshold at the Planck scale.
    E_planck_gev : float
        Planck energy in GeV.

    Returns
    -------
    float : energy scale in GeV.
    """
    return E_planck_gev * math.sqrt(C_n / C_planck)


def fit_gamma_from_spectrum():
    """
    Fit the bifurcation growth rate γ from the observed particle energy spectrum.

    Uses two anchor points (SCHEME A — particle mass scale D-labels):
      - D5 layer: electron mass ~ 5.11 × 10⁻⁴ GeV
      - Closure scale: M_c ~ 10¹⁸ GeV (Planck-scale anchor; D18 in Scheme A)

    WARNING: This function uses SCHEME A D-labels (particle mass scales), which
    are inconsistent with SCHEME B D-labels (gauge closure thresholds) used in
    equations/depth_running.py and all Route 3B work. The "closure scale" here
    at 10^18 GeV at D18 ≠ the Route 3B closure scale 10^13 GeV at D5 (Scheme B).
    Do not use this function's gamma as input to the two-scale depth-running model.

    For the physically derived gamma connecting to the substrate parameters, see:
    equations/bifurcation_dynamics.py  (gamma = (16/3) * sqrt(beta))

    The ratio of thresholds over 13 bifurcation steps gives γ.

    Returns
    -------
    dict with fitted parameters.
    """
    n_electron = 4         # D5 = 4 bifurcations from D1 (Scheme A)
    n_closure  = 17        # closure scale = ~17 bifurcations from D1 (Scheme A)
    E_electron = 5.11e-4   # GeV
    E_closure  = 1e18      # GeV  [Scheme A closure scale; NOT Route 3B M_c = 10^13 GeV]

    delta_n = n_closure - n_electron
    gamma = math.log(E_closure / E_electron) / delta_n

    # C0 from electron scale (anchor)
    # E_n = E_Planck × √(C_n / C_Planck) is one model;
    # simpler: just use the energy ratio directly
    scale_ratio_per_layer = math.exp(gamma)

    return {
        'gamma':                    gamma,
        'scale_ratio_per_layer':    scale_ratio_per_layer,
        'n_electron':               n_electron,
        'n_closure':                n_closure,
        'E_electron_gev':           E_electron,
        'E_closure_gev':            E_closure,
        'total_e_foldings':         math.log(E_closure / E_electron),
        'note': (f'Each bifurcation increases the energy scale by factor '
                 f'{scale_ratio_per_layer:.2f} (= e^γ = e^{gamma:.3f})'),
    }


def dimensional_stability_window(n, C_n, delta_C):
    """
    Stability window for the n-th dimensional layer.

    A layer is stable when the compression level is in the range:
        [C_n - δC/2, C_{n+1} - δC/2]

    Below C_n: the mode has not formed yet
    Above C_{n+1}: the next bifurcation occurs, creating a higher layer

    The width δC of each stability window sets how robust a given layer is
    against perturbations. Wide windows → more stable, more macroscopic.

    Parameters
    ----------
    n : int
        Layer index.
    C_n : float
        Lower threshold for this layer.
    delta_C : float
        Width of the stability window.

    Returns
    -------
    dict with stability range.
    """
    return {
        'layer': n,
        'C_lower': C_n,
        'C_upper': C_n + delta_C,
        'stability_width': delta_C,
        'stable': True,
        'note': f'D{n+1} layer stable for compression C ∈ [{C_n:.3f}, {C_n + delta_C:.3f}]',
    }


def why_four_macroscopic_dimensions():
    """
    Argument for why exactly D1–D4 produce macroscopic observed structure.

    The argument (provisional):
      1. D1: maximal compression — approached asymptotically, never a stable layer
      2. D2: first stable mode — massless propagation. Stable because the D2↔D3
             boundary has no intrinsic instability; light propagates without decay.
      3. D3: second stable mode — localization. Stable because position is
             self-consistent: a localized structure can persist without external support.
      4. D4: third stable mode — inertia. Stable because resistance to reconfiguration
             is self-reinforcing: once a structure anchors deeply, it resists further change.

    D5 and above are *internal* modes — they are stable (we observe them as particle
    properties: charge, flavor, color) but they do not produce additional macroscopic
    spatial dimensions. The transition from macroscopic to internal occurs because:
      - D1–D4 produce unbounded modes (propagation, localization, inertia extend to
        arbitrary scale)
      - D5+ modes are self-closing: they fold back on themselves into compact topologies
        (the gauge group closures U(1), SU(2), SU(3))

    This is the distinction between 'large' dimensions (D2–D4) and 'internal' dimensions
    (D5+) — not in the size of the dimension, but in whether the stable mode is
    open (extends without limit) or closed (forms a topological loop).

    Returns
    -------
    dict with dimensional classification.
    """
    return {
        'D1': {'type': 'sink',     'macroscopic': False, 'reason': 'Asymptotic limit, not a stable layer'},
        'D2': {'type': 'open',     'macroscopic': True,  'reason': 'Massless propagation — extends without limit'},
        'D3': {'type': 'open',     'macroscopic': True,  'reason': 'Localization — position extends without limit'},
        'D4': {'type': 'open',     'macroscopic': True,  'reason': 'Inertia — resistance extends without limit'},
        'D5': {'type': 'closed',   'macroscopic': False, 'reason': 'U(1) closure — forms compact electromagnetic loop'},
        'D6': {'type': 'closed',   'macroscopic': False, 'reason': 'Part of SU(2) closure — weak force topology'},
        'D7+':{'type': 'closed',   'macroscopic': False, 'reason': 'SU(3) closure — strong force topology'},
        'key_transition': (
            'D4→D5 is where open modes end and closed loops begin. '
            'This is why we observe three apparent spatial degrees of freedom + time '
            '(from D2, D3, D4 behaviors) and not additional macroscopic directions.'
        ),
        'open_question': (
            'Why does the closed/open transition occur precisely at D5? '
            'What is special about the 4th bifurcation that makes U(1) the minimal '
            'stable closed mode? This needs to be derived from the substrate dynamics.'
        ),
    }


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("BIFURCATION SEQUENCE — DIMENSIONAL EMERGENCE")
    print("Dimensional Folding Model")
    print("=" * 65)

    print(f"\n--- Bifurcation Growth Rate Fit ---")
    fit = fit_gamma_from_spectrum()
    print(f"  γ (log growth per layer):     {fit['gamma']:.4f}")
    print(f"  Energy scale ratio per layer: {fit['scale_ratio_per_layer']:.2f}×")
    print(f"  {fit['note']}")

    print(f"\n--- Provisional Dimensional Layer Energy Scales ---")
    print(f"  {'Layer':>6}  {'Name':20s}  {'Energy scale':>15s}")
    print(f"  {'-'*6}  {'-'*20}  {'-'*15}")
    for d, info in DIMENSIONAL_LAYERS.items():
        e = info['energy_scale_gev']
        if e is None:
            e_str = '      (asymptotic)'
        elif e == 0.0:
            e_str = '     0  (massless)'
        elif e < 1e-3:
            e_str = f'{e*1e6:>10.2f} eV'
        elif e < 1.0:
            e_str = f'{e*1e3:>10.2f} MeV'
        elif e < 1e6:
            e_str = f'{e:>10.2f} GeV'
        else:
            e_str = f'{e:.2e} GeV'
        print(f"  {d:>6}  {info['name']:20s}  {e_str:>15s}")

    print(f"\n--- Why 4 Macroscopic Dimensions ---")
    dims = why_four_macroscopic_dimensions()
    for key in ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7+']:
        d = dims[key]
        macro = '✓ macroscopic' if d['macroscopic'] else '  internal'
        print(f"  {key:5s}  [{d['type']:6s}]  {macro}  — {d['reason']}")
    print(f"\n  Key transition: {dims['key_transition']}")
    print(f"  Open question:  {dims['open_question']}")

    print(f"\n--- Open Problems ---")
    print(f"  1. First-principles derivation of threshold values C_n from (α, β, c)")
    print(f"  2. Why closed modes form at D5 specifically (not D4 or D6)")
    print(f"  3. Non-uniform γ between layers (energy spacing is not uniform)")
    print(f"  4. Connection between stability window width and layer observability")
    print(f"  See: foundations/formation.md, foundations/dimensional_emergence.md")
