"""
Quark masses from SU(3) confinement depth and isospin asymmetry.

In the Dimensional Folding Model, quarks are confined structures at ~D8–9, where
three-body SU(3) confinement locks in. Six quarks = three generations × two isospin
states. Their masses span five orders of magnitude, which this model attributes to
two separate geometric effects:

  GENERATION HIERARCHY  (why charm >> up, top >> charm):
    Three generations correspond to progressively deeper anchoring into the SU(3)
    confinement closure. Each generation sits at a higher effective depth index,
    experiencing stronger confinement = higher mass.

    The three SU(3) winding modes are not equally spaced — the mass ratio between
    successive generations is roughly geometric (each generation ~10–100× heavier
    than the previous, with the top quark as a special case near the Higgs coupling
    threshold).

  ISOSPIN ASYMMETRY  (why down > up at light scale, but top >> bottom):
    Up-type and down-type quarks within a generation arise from the two orientations
    of the SU(2) squashing. The mass ratio within a generation reflects the SU(2)
    squashing parameter ε — the same parameter that determines the W/Z mass ratio.
    At light generations the asymmetry is small; at heavy generations the Yukawa
    coupling to the Higgs dominates.

Mass hierarchy (PDG 2024, GeV):
    Generation 1:  up    ~0.00216  down   ~0.00467
    Generation 2:  charm ~1.27     strange ~0.093
    Generation 3:  top   ~172.76   bottom  ~4.18

Depth assignments (provisional):
    Quark confinement begins at the QCD transition depth (~D7-8)
    Generation 1 sits at d₁ ≈ 7.5
    Generation 2 sits at d₂ ≈ 8.5
    Generation 3 sits at d₃ ≈ 9.5

Key open question: the top quark mass (~173 GeV) is anomalously close to the Higgs
vev (246 GeV) — its Yukawa coupling y_t ≈ 1. In this model, this is interpreted as
the top quark being the deepest quark, with anchoring depth approaching the closure
scale. The Higgs mass generation is therefore linked to the top quark depth.

Usage:
    python equations/quark_masses.py

    Or import:
        from equations.quark_masses import predict_quark_masses, fit_generation_model
"""

import math

# ── Observed quark masses (PDG 2024, MS-bar at 2 GeV for light quarks) ───────

QUARK_MASSES_GEV = {
    'up':      2.16e-3,    # u  (MS-bar 2 GeV)
    'down':    4.67e-3,    # d  (MS-bar 2 GeV)
    'strange': 0.0934,     # s  (MS-bar 2 GeV)
    'charm':   1.275,      # c  (MS-bar m_c)
    'bottom':  4.180,      # b  (MS-bar m_b)
    'top':     172.76,     # t  (pole mass)
}

# Generation grouping
GENERATIONS = {
    1: ('up',      'down'),
    2: ('charm',   'strange'),
    3: ('top',     'bottom'),
}

# Up-type and down-type
UP_TYPE   = ('up',   'charm',   'top')
DOWN_TYPE = ('down', 'strange', 'bottom')

# Higgs vev
HIGGS_VEV_GEV = 246.22


# ── Generation mass scale model ───────────────────────────────────────────────

def generation_mass_scale(gen, M0, kappa_q):
    """
    Mass scale for quark generation n from the confinement depth model.

    Each generation sits at a deeper point in the SU(3) confinement closure:
        M_gen(n) = M0 × exp(κ_q × (n - 1))

    where:
        M0    = mass scale of generation 1 (up/down average ∝ GeV)
        κ_q   = confinement depth sensitivity
        n     = generation index (1, 2, 3)

    The exponential arises because confinement depth enters the mass
    through the same anchoring mechanism as the lepton hierarchy.

    Parameters
    ----------
    gen : int
        Generation index (1, 2, or 3).
    M0 : float
        Reference mass scale for generation 1 in GeV.
    kappa_q : float
        Confinement depth sensitivity parameter.

    Returns
    -------
    float : mass scale for that generation in GeV.
    """
    return M0 * math.exp(kappa_q * (gen - 1))


def isospin_split(mass_scale_gev, r_ud):
    """
    Split a generation mass scale into up-type and down-type masses.

    Within a generation, the up-type and down-type quark masses differ due to
    the SU(2) squashing asymmetry. The ratio r_ud = m_up / m_down is a geometric
    parameter set by the squashing angle.

    For light quarks (gen 1, 2): r_ud < 1 (down slightly heavier)
    For heavy quarks (gen 3):    r_ud >> 1 (top much heavier — Higgs Yukawa dominates)

    The top quark's anomalously high mass reflects its proximity to the Higgs
    coupling threshold: y_t ≈ 1 means the top Yukawa coupling is O(1), which
    in this model signals the top quark sitting at the depth where the S³ squashing
    is maximally sensitive.

    Parameters
    ----------
    mass_scale_gev : float
        Geometric mean mass scale for the generation in GeV.
    r_ud : float
        Mass ratio m_up_type / m_down_type for this generation.

    Returns
    -------
    (m_up_gev, m_down_gev)
    """
    # mass_scale = sqrt(m_up × m_down)  (geometric mean)
    # r_ud = m_up / m_down
    # → m_up = mass_scale × sqrt(r_ud)
    # → m_down = mass_scale / sqrt(r_ud)
    m_up   = mass_scale_gev * math.sqrt(r_ud)
    m_down = mass_scale_gev / math.sqrt(r_ud)
    return m_up, m_down


def fit_generation_model():
    """
    Fit the generation mass scale model to observed quark masses.

    Strategy:
      1. Compute the geometric mean mass scale for each generation
      2. Fit M0 and κ_q to the three generation scales
      3. Extract the isospin ratio r_ud for each generation
      4. Assess consistency with the SU(2) squashing interpretation

    Returns
    -------
    dict with fit parameters and residuals.
    """
    # Geometric mean mass scale per generation
    scales_gev = {}
    ratios_ud = {}
    for gen, (up, down) in GENERATIONS.items():
        m_up   = QUARK_MASSES_GEV[up]
        m_down = QUARK_MASSES_GEV[down]
        scales_gev[gen] = math.sqrt(m_up * m_down)
        ratios_ud[gen]  = m_up / m_down

    # Fit κ_q from generations 1→2 and 2→3
    kappa_12 = math.log(scales_gev[2] / scales_gev[1])  # (n=2-1=1 step)
    kappa_23 = math.log(scales_gev[3] / scales_gev[2])

    # M0 from generation 1
    M0 = scales_gev[1]

    # Average κ_q (should be ~constant for geometric depth model)
    kappa_q_avg = (kappa_12 + kappa_23) / 2

    # Predicted scales with average kappa
    pred_scales = {gen: generation_mass_scale(gen, M0, kappa_q_avg) for gen in [1, 2, 3]}

    return {
        'M0_gev':           M0,
        'kappa_12':         kappa_12,
        'kappa_23':         kappa_23,
        'kappa_q_avg':      kappa_q_avg,

        'scales_observed':  scales_gev,
        'scales_predicted': pred_scales,
        'residuals': {
            gen: pred_scales[gen] / scales_gev[gen]
            for gen in [1, 2, 3]
        },

        'isospin_ratios':   ratios_ud,
        'r_ud_gen1':        ratios_ud[1],
        'r_ud_gen2':        ratios_ud[2],
        'r_ud_gen3':        ratios_ud[3],

        'top_yukawa':       math.sqrt(2) * QUARK_MASSES_GEV['top'] / HIGGS_VEV_GEV,
        'note': ('κ_12 ≠ κ_23 signals non-uniform depth spacing — top quark is '
                 'anomalous due to proximity to Higgs coupling threshold.'),
    }


def predict_quark_masses(M0=None, kappa_q=None, r_ud=None):
    """
    Predict all six quark masses from three parameters:
        M0    = generation-1 mass scale (GeV)
        kappa_q = confinement depth sensitivity
        r_ud  = list of three isospin ratios [r1, r2, r3]

    If parameters are None, uses values from fit_generation_model().

    Returns
    -------
    dict with predicted and observed masses for all six quarks.
    """
    if M0 is None or kappa_q is None or r_ud is None:
        fit = fit_generation_model()
        M0     = fit['M0_gev']
        kappa_q = fit['kappa_q_avg']
        r_ud   = [fit['r_ud_gen1'], fit['r_ud_gen2'], fit['r_ud_gen3']]

    predictions = {}
    for i, gen in enumerate([1, 2, 3]):
        scale = generation_mass_scale(gen, M0, kappa_q)
        m_up_pred, m_down_pred = isospin_split(scale, r_ud[i])
        up_name, down_name = GENERATIONS[gen]

        predictions[up_name] = {
            'predicted_gev':  m_up_pred,
            'observed_gev':   QUARK_MASSES_GEV[up_name],
            'ratio':          m_up_pred / QUARK_MASSES_GEV[up_name],
        }
        predictions[down_name] = {
            'predicted_gev':  m_down_pred,
            'observed_gev':   QUARK_MASSES_GEV[down_name],
            'ratio':          m_down_pred / QUARK_MASSES_GEV[down_name],
        }

    return predictions


def top_quark_yukawa_interpretation():
    """
    Interpret the top quark Yukawa coupling in the dimensional folding model.

    The top quark Yukawa y_t ≈ 1 means:
        m_top = y_t × v / √2 ≈ v / √2

    In this model, y_t ≈ 1 signals the top quark sitting at the depth where
    the S³ squashing is maximally sensitive — the Higgs vev and the top mass
    are set by the same geometric parameter.

    This is why:
      1. The Higgs mass is radiatively generated primarily by the top loop
      2. The top quark is both the heaviest quark and the closest to the Higgs scale
      3. The electroweak vacuum stability depends on m_top (see higgs_mass_derivation.md)

    Returns
    -------
    dict with interpretation quantities.
    """
    m_top = QUARK_MASSES_GEV['top']
    y_t   = math.sqrt(2) * m_top / HIGGS_VEV_GEV
    ratio = m_top / HIGGS_VEV_GEV

    return {
        'top_mass_gev':       m_top,
        'higgs_vev_gev':      HIGGS_VEV_GEV,
        'yukawa_y_t':         y_t,
        'm_top_over_vev':     ratio,
        'depth_interpretation': (
            'y_t ≈ 1 means the top quark depth sits at the S³ squashing threshold. '
            'The top is not just the heaviest quark — it is the quark closest to the '
            'Higgs closure geometry. All lighter quarks have y < 1 because they sit '
            'below the squashing threshold in depth.'
        ),
    }


def generation_mass_ratios():
    """
    Compute the up-type and down-type mass ratios between successive generations.

    These ratios encode the underlying geometric depth spacing.
    A uniform geometric depth model predicts constant ratios.
    Deviations reveal non-uniform depth spacing (especially for generation 3).

    Returns
    -------
    dict with observed and model-expected ratios.
    """
    m = QUARK_MASSES_GEV
    return {
        # Up-type ratios
        'charm_over_up':    m['charm'] / m['up'],
        'top_over_charm':   m['top']   / m['charm'],
        'top_over_up':      m['top']   / m['up'],

        # Down-type ratios
        'strange_over_down':  m['strange'] / m['down'],
        'bottom_over_strange': m['bottom']  / m['strange'],
        'bottom_over_down':   m['bottom']  / m['down'],

        # Log ratios (should be constant for uniform depth spacing)
        'log_charm_up':     math.log(m['charm'] / m['up']),
        'log_top_charm':    math.log(m['top']   / m['charm']),
        'log_strange_down': math.log(m['strange'] / m['down']),
        'log_bottom_strange': math.log(m['bottom'] / m['strange']),

        'note': ('Non-constant log ratios reveal non-uniform SU(3) winding depth '
                 'spacing. The top quark is the clearest outlier — it sits '
                 'near the Higgs coupling threshold.'),
    }


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("QUARK MASSES — CONFINEMENT DEPTH MODEL")
    print("Dimensional Folding Model")
    print("=" * 65)

    fit = fit_generation_model()
    print(f"\n--- Generation Mass Scale Fit ---")
    print(f"  M0 (gen-1 scale):    {fit['M0_gev']*1000:.3f} MeV")
    print(f"  κ_q (gen 1→2):       {fit['kappa_12']:.4f}")
    print(f"  κ_q (gen 2→3):       {fit['kappa_23']:.4f}")
    print(f"  κ_q (average):       {fit['kappa_q_avg']:.4f}")
    print(f"  {fit['note']}")

    print(f"\n--- Isospin Ratios per Generation (m_up / m_down) ---")
    for gen in [1, 2, 3]:
        names = GENERATIONS[gen]
        r = fit['isospin_ratios'][gen]
        print(f"  Gen {gen} ({names[0]:8s} / {names[1]:8s}): {r:.4f}")

    print(f"\n--- Predicted vs Observed Quark Masses ---")
    pred = predict_quark_masses()
    print(f"  {'Quark':10s}  {'Predicted':>12s}  {'Observed':>12s}  {'Ratio':>8s}")
    print(f"  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*8}")
    for name, vals in pred.items():
        p = vals['predicted_gev']
        o = vals['observed_gev']
        r = vals['ratio']
        unit = 'GeV' if o > 0.1 else 'MeV'
        scale = 1.0 if unit == 'GeV' else 1000.0
        print(f"  {name:10s}  {p*scale:>10.4f} {unit}  {o*scale:>10.4f} {unit}  {r:>8.4f}")

    print(f"\n--- Log Mass Ratios Between Generations ---")
    ratios = generation_mass_ratios()
    print(f"  ln(charm/up):      {ratios['log_charm_up']:.3f}")
    print(f"  ln(top/charm):     {ratios['log_top_charm']:.3f}")
    print(f"  ln(strange/down):  {ratios['log_strange_down']:.3f}")
    print(f"  ln(bottom/strange):{ratios['log_bottom_strange']:.3f}")

    print(f"\n--- Top Quark Interpretation ---")
    top = top_quark_yukawa_interpretation()
    print(f"  m_top:              {top['top_mass_gev']:.2f} GeV")
    print(f"  Higgs vev:          {top['higgs_vev_gev']:.2f} GeV")
    print(f"  Yukawa y_t:         {top['yukawa_y_t']:.4f}")
    print(f"  m_top/v:            {top['m_top_over_vev']:.4f}")
    print(f"  {top['depth_interpretation']}")

    print(f"\n--- Open Problems ---")
    print(f"  1. Non-uniform κ_q between generations needs geometric explanation")
    print(f"  2. Isospin ratios need derivation from SU(2) squashing parameter")
    print(f"  3. Top quark anomaly: y_t ≈ 1 needs first-principles depth assignment")
    print(f"  4. QCD confinement scale ΛQCD from compression threshold (open)")
    print(f"  See foundations/three_generations.md and foundations/higgs_geometry.md")
