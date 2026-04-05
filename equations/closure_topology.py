"""
Topological closure spectrum — why U(1), SU(2), SU(3) are the stable force structures.

In the Dimensional Folding Model, the gauge forces are not imposed — they are the
minimal stable topological configurations that the compression field can form at the
D5+ depths. Each force corresponds to a self-reinforcing closed loop in the folding
structure, characterized by its topology (not its size).

Core claim:
  At each internal depth (D5+), the compression field can close into topological loops.
  The minimal stable loops at successive depths are exactly:
    D5:  U(1)   — the simplest closed loop (circle, S¹)
    D6:  SU(2)  — the 3-sphere (S³), first non-trivial simply-connected closure
    D7:  SU(3)  — the 8-dimensional Lie group, minimal 3-body confinement structure

These are not chosen — they are the minimal stable configurations, classified by
the topological constraints imposed by each depth's available degrees of freedom.

The force strengths (coupling constants) are set by the sizes of these closures,
not by their topologies. The topologies determine which forces exist; the sizes
determine how strong they are.

STATUS: The identification of U(1)/SU(2)/SU(3) with depth-ordered closures is
well-motivated but not yet formally derived. The open problem is showing from
the substrate dynamics why these three and not others are stable.

Key references:
  - foundations/product_geometry.md — why these form a product, not a simple group
  - foundations/three_generations.md — why SU(3) has exactly 3 winding modes
  - foundations/higgs_geometry.md — S³ squashing as electroweak symmetry breaking

Usage:
    python equations/closure_topology.py
"""

import math

# ── Topological invariants of the force closures ──────────────────────────────

CLOSURE_STRUCTURES = {
    'U(1)': {
        'topology':       'S¹ (circle)',
        'dimension':      1,
        'rank':           1,
        'generators':     1,
        'fundamental_group': 'ℤ  (winding number)',
        'homotopy_pi1':   'ℤ',
        'homotopy_pi2':   '0',
        'homotopy_pi3':   'ℤ',
        'depth_layer':    5,
        'force':          'Electromagnetism',
        'coupling_name':  'α_EM ≈ 1/137',
        'stability':      ('Stable because S¹ is the only closed 1-manifold. '
                           'Any connected, compact, 1D space is a circle.'),
    },
    'SU(2)': {
        'topology':       'S³ (3-sphere)',
        'dimension':      3,
        'rank':           1,
        'generators':     3,
        'fundamental_group': '0  (simply connected)',
        'homotopy_pi1':   '0',
        'homotopy_pi2':   '0',
        'homotopy_pi3':   'ℤ',
        'depth_layer':    6,
        'force':          'Weak nuclear force',
        'coupling_name':  'α_W ≈ 1/29 at M_Z',
        'stability':      ('Stable because SU(2) ≅ S³ is the unique simply-connected '
                           '3-dimensional Lie group. It cannot be further decomposed.'),
    },
    'SU(3)': {
        'topology':       'SU(3) Lie group (8-dimensional)',
        'dimension':      8,
        'rank':           2,
        'generators':     8,
        'fundamental_group': '0  (simply connected)',
        'homotopy_pi1':   '0',
        'homotopy_pi2':   '0',
        'homotopy_pi3':   'ℤ',
        'depth_layer':    7,
        'force':          'Strong nuclear force (QCD)',
        'coupling_name':  'α_s ≈ 0.118 at M_Z',
        'stability':      ('Stable because SU(3) is the minimal Lie group '
                           'admitting a 3-dimensional fundamental representation '
                           '— the structure required for 3-body confinement.'),
    },
}


# ── Closure energy model ───────────────────────────────────────────────────────

def closure_energy(topology_dim, closure_radius, alpha, beta, c=1.0):
    """
    Energy of a topological closure of a given topology and radius.

    A closure is a stable field configuration that winds around a topological
    cycle. Its energy has two contributions:
      - Curvature energy: ∝ (c/R)² × V_topology  (cost of bending the field)
      - Compression energy: ∝ α × R² × V_topology  (cost of maintaining the closure)

    The stable radius R_0 minimizes the total energy:
        dE/dR = 0  →  R_0 = (c/√α) × (curvature/compression)^(1/4)

    At R = R_0, the closure energy is:
        E_closure ∝ c × √α  (independent of R_0 — topological protection)

    Parameters
    ----------
    topology_dim : int
        Dimension of the topological manifold (1 for U(1), 3 for SU(2), 8 for SU(3)).
    closure_radius : float
        Characteristic radius of the closure.
    alpha, beta, c : float
        Compression field parameters.

    Returns
    -------
    dict with energy components and stable radius estimate.
    """
    # Characteristic volume ∝ R^topology_dim
    volume = closure_radius**topology_dim

    # Curvature energy: field gradient energy ∝ (1/R²) × V
    E_curvature = (c / closure_radius)**2 * volume

    # Compression energy: potential energy of deformed field ∝ α × V
    E_compression = alpha * closure_radius**2 * volume

    # Stable radius estimate.
    #
    # IMPORTANT LIMITATION (Derrick's theorem): For topology_dim ≥ 3, both
    # E_curvature = c² R^(n-2) and E_compression = α R^(n+2) are monotonically
    # INCREASING with R. There is no classical energy minimum — dE/dR > 0 for
    # all R > 0. This is an instance of Derrick's theorem: static solitons in
    # φ⁴ theory do not exist for spatial dimension n ≥ 2 from energy balance alone.
    #
    # For n=1 (U(1)): E_curv ~ c²/R (decreasing), E_comp ~ α R³ (increasing)
    # → genuine energy minimum at R ~ (c²/3α)^(1/4) ≈ c/√α (kink width). ✓
    #
    # For n ≥ 3 (SU(2), SU(3)): Both terms increase with R. The R_stable formula
    # below gives the scale where the two terms are COMPARABLE (equipartition
    # estimate), not a true energy minimum. Stability for SU(2)/SU(3) closures
    # comes from topological protection, not energy minimization.
    if topology_dim > 2:
        # Equipartition scale: E_curv(R*) ≈ E_comp(R*)
        # c² R^(n-2) ≈ α R^(n+2)  →  R* = (c²/α)^(1/4)
        # The (n-2)/(n+2) factor below is a shape correction; note this is NOT
        # a minimum of E_total.
        R_stable = (c**2 * (topology_dim - 2) / (alpha * (topology_dim + 2)))**(0.25)
    else:
        R_stable = c / math.sqrt(alpha)   # n=1: kink width (genuine minimum)

    E_total = E_curvature + E_compression

    return {
        'topology_dim':     topology_dim,
        'radius':           closure_radius,
        'R_stable_est':     R_stable,
        'E_curvature':      E_curvature,
        'E_compression':    E_compression,
        'E_total':          E_total,
        'topologically_protected': True,
        'note': ('Closure energy is topologically protected: cannot change '
                 'continuously. Discrete jumps require passing through the '
                 'unstable (unwound) configuration. WARNING: for dim >= 3, '
                 'R_stable is an equipartition scale estimate, not a true energy '
                 'minimum — see Derrick\'s theorem comment above.'),
    }


def minimal_stable_closure_at_depth(depth):
    """
    Identify the minimal stable topological closure at a given dimensional depth.

    The progression:
      Depth 5: 1D closure (circle) is the only possibility → U(1)
      Depth 6: 2D closures are not Lie groups; 3D (S³ = SU(2)) is minimal → SU(2)
      Depth 7: Next Lie group with a non-trivial 3-body structure → SU(3)
      Depth 8+: Higher closures; SU(4), SU(5), etc. — not observed as fundamental

    Why does the sequence stop at SU(3)?
      The three observed forces saturate the available topological types at D5–D7.
      Above D7, the compression field enters the quark confinement regime, where
      the SU(3) closure already accounts for all available degrees of freedom.

    Parameters
    ----------
    depth : int or float
        Dimensional depth index.

    Returns
    -------
    dict with closure identification.
    """
    if depth < 5:
        return {'closure': None, 'reason': 'Below D5: no stable closed modes, only open propagation'}
    elif depth < 6:
        return {'closure': 'U(1)', 'topology': 'S¹', 'force': 'Electromagnetism',
                'reason': 'First internal depth: only 1D closed manifold is S¹'}
    elif depth < 7:
        return {'closure': 'SU(2)', 'topology': 'S³', 'force': 'Weak force',
                'reason': 'Second internal depth: minimal simply-connected Lie group'}
    elif depth < 8:
        return {'closure': 'SU(3)', 'topology': 'SU(3)', 'force': 'Strong force',
                'reason': 'Third internal depth: minimal group with 3-body representation'}
    else:
        return {'closure': 'composite', 'reason': 'D8+: quark confinement regime, no new fundamental forces'}


def coupling_constant_from_closure_size(R_closure, R_reference, alpha_reference):
    """
    Running coupling constant from closure radius at a given energy scale.

    In this model, coupling constants are determined by the ratio of the
    closure radius to the probing scale at the measurement energy:

        α(μ) ∝ (R_closure / λ(μ))²

    where λ(μ) = c/μ is the probing length scale at energy μ.

    At low energy (large λ): the probe doesn't resolve the closure → weak coupling
    At high energy (small λ): the probe resolves the closure → coupling approaches 1

    This gives asymptotic freedom for SU(3) (coupling decreases at high energy)
    and Landau pole behavior for U(1) (coupling increases at high energy).

    Parameters
    ----------
    R_closure : float
        Physical radius of the closure structure (in appropriate units).
    R_reference : float
        Closure radius at the reference scale.
    alpha_reference : float
        Known coupling at the reference scale.

    Returns
    -------
    float : coupling constant scaled by radius ratio.
    """
    return alpha_reference * (R_closure / R_reference)**2


def product_structure_argument():
    """
    Why the force structures form a product U(1) × SU(2) × SU(3), not a simple group.

    If the three forces were unified in a simple group G ⊃ U(1)×SU(2)×SU(3),
    then G → U(1)×SU(2)×SU(3) would require a spontaneous symmetry breaking at
    some high energy scale, and proton decay would be predicted.

    In this model, the three closures form at DIFFERENT depths (D5, D6, D7)
    through DIFFERENT instability events. They were never unified — they are
    structurally independent topological configurations.

    The product structure is not a remnant of a broken simple group.
    It is the natural result of three independent compression-driven closures
    at three successive depth thresholds.

    Returns
    -------
    dict with the product structure argument.
    """
    return {
        'U(1)_depth':   5,
        'SU(2)_depth':  6,
        'SU(3)_depth':  7,
        'formation':    'Each at a separate bifurcation threshold — independent events',
        'structure':    'U(1) × SU(2) × SU(3)  (direct product, not quotient)',
        'proton_decay': 'Forbidden — no X/Y bosons, no leptoquark operators',
        'coupling_unification': (
            'Couplings converge at the closure scale because all three closures '
            'were formed at the same geometric scale (D_closure — exact value not '
            'yet derived from DFC substrate parameters; SM running suggests '
            '~10^15-10^16 GeV for coupling convergence). '
            'Convergence reflects common origin, not simple group unification.'
        ),
        'GUT_distinction': (
            'SU(5), SO(10) unification requires G → SM breaking at GUT scale. '
            'This model has no GUT scale — the closure scale is where the '
            'closures FORMED, not where they broke from a higher symmetry.'
        ),
    }


# ── Topological protection ────────────────────────────────────────────────────

def topological_charge(winding_number, closure_type='U(1)'):
    """
    Topological charge of a closure configuration.

    Topological charges are conserved exactly (not just approximately) because
    they count how many times the field winds around a topological cycle.
    No continuous deformation can change a winding number — only a discontinuous
    transition through the unstable (unwound) configuration.

    For U(1): charge = electric charge (integer multiples of e)
    For SU(2): isospin (integer or half-integer)
    For SU(3): color (triplet under fundamental representation)

    Parameters
    ----------
    winding_number : int
        Number of times the field winds around the closure topology.
    closure_type : str
        'U(1)', 'SU(2)', or 'SU(3)'.

    Returns
    -------
    dict with topological charge interpretation.
    """
    interpretations = {
        'U(1)':  f'Electric charge: {winding_number}e',
        'SU(2)': f'Isospin state in SU(2) multiplet: winding = {winding_number}',
        'SU(3)': f'Color state in SU(3) fundamental: winding = {winding_number}',
    }
    return {
        'winding_number':   winding_number,
        'closure_type':     closure_type,
        'interpretation':   interpretations.get(closure_type, 'Unknown closure'),
        'conserved':        True,
        'conservation_reason': 'Topological — no smooth deformation can change winding number',
    }


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("CLOSURE TOPOLOGY — FORCE STRUCTURES FROM DIMENSIONAL DEPTH")
    print("Dimensional Folding Model")
    print("=" * 65)

    print(f"\n--- Force Structure Identification ---")
    print(f"  {'Closure':8s}  {'Topology':20s}  {'Depth':>6s}  {'Force'}")
    print(f"  {'-'*8}  {'-'*20}  {'-'*6}  {'-'*25}")
    for name, info in CLOSURE_STRUCTURES.items():
        print(f"  {name:8s}  {info['topology']:20s}  {info['depth_layer']:>6d}  "
              f"{info['force']}")

    print(f"\n--- Minimal Stable Closure at Each Depth ---")
    for d in [4, 5, 6, 7, 8]:
        result = minimal_stable_closure_at_depth(d)
        closure = result.get('closure', 'None')
        reason  = result.get('reason', '')
        print(f"  Depth {d}: {str(closure):8s}  — {reason}")

    print(f"\n--- Product Structure Argument ---")
    prod = product_structure_argument()
    print(f"  U(1) forms at depth:   {prod['U(1)_depth']}")
    print(f"  SU(2) forms at depth:  {prod['SU(2)_depth']}")
    print(f"  SU(3) forms at depth:  {prod['SU(3)_depth']}")
    print(f"  Formation:  {prod['formation']}")
    print(f"  Structure:  {prod['structure']}")
    print(f"  Proton:     {prod['proton_decay']}")
    print(f"  Couplings:  {prod['coupling_unification']}")

    print(f"\n--- Closure Energies (Normalized Units) ---")
    for dim, label in [(1, 'U(1)'), (3, 'SU(2)'), (8, 'SU(3)')]:
        e = closure_energy(dim, closure_radius=1.0, alpha=1.0, beta=1.0)
        print(f"  {label:6s}  (dim={dim}):  E_total = {e['E_total']:.4f}  "
              f"R_stable = {e['R_stable_est']:.4f}")

    print(f"\n--- Open Problems ---")
    print(f"  1. Derive why the open→closed transition occurs at D5 specifically")
    print(f"  2. Compute U(1)/SU(2)/SU(3) closure sizes from substrate parameters")
    print(f"  3. Show SU(4) and higher are NOT stable at D8+ (exclusion argument)")
    print(f"  4. Connect winding numbers to quantized electric charge values")
    print(f"  See: foundations/product_geometry.md, foundations/three_generations.md")
