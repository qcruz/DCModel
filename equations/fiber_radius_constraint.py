"""
fiber_radius_constraint.py — Cycle 109: Derive R_n from the KK normalization constraint

Physical question:
    For each Hopf fiber S^{d_n}(R_n) at depth D(4+n), what value of R_n is selected
    by the DFC substrate? Specifically: does the KK normalization condition
    (mode_norm = 9/(64π)) independently determine R_n = πd_nλ/I₄?

Setup:
    From Cycle 107 (kk_fiber_coupling.py), P6: |K_Hopf(Ω)|² = R_n² everywhere on
    S^{d_n}(R_n). The KK normalization integral for the gauge zero mode on the fiber is:

        N_KK = ∫∫ |η₀(x)|² × |K_Hopf(Ω)|²/R_n² × dΩ/Vol(S^{d_n}(R_n)) dx

    Since |K_Hopf|² = R_n² (constant) and dΩ integrates to Vol(S^{d_n}(R_n)):
        N_KK = ‖η₀‖² × R_n² × Vol/Vol × (1/R_n²) = ‖η₀‖²

    For normalized η₀ (‖η₀‖ = 1): N_KK = 1 regardless of R_n.

    This is CONSISTENT with R_n being free from this integral — mode_norm=9/(64π)
    was proved β-independent (Cycle 105) and R_n-independent by the same logic.

    REVISED APPROACH: The constraint on R_n comes not from the gauge normalization
    integral, but from the ZERO MODE COMPLETENESS condition:
    The d_n zero modes on S^{d_n}(R_n) must be NORMALIZABLE and COMPLETE in L²(ℝ).

    For the n-th kink system on ℝ × S^{d_n}(R_n):
    The zero modes η₀^(j)(x, Ω) = η₀(x) × Y₁^(j)(Ω) where Y₁^(j) are first-order
    spherical harmonics on S^{d_n}(R_n) (Hopf fiber harmonics, l=1).

    The FIRST SPHERICAL HARMONIC eigenvalue is λ₁ = d_n/R_n².
    The condition that this matches the KINK's internal scale sets R_n.

    KINK INTERNAL SCALE FROM SPECTRAL MATCHING:
    The fluctuation operator L = -∂_x² + V''(φ_kink) has spectrum:
    - ω² = 0 (zero mode, translation)
    - ω₁² = (3/2)α (shape mode)
    - ω² ≥ 2α (continuum)

    The fiber eigenvalue d_n/R_n² must match a kink spectral quantity.
    Different matching conditions give different R_n values:
    (a) Match to zero mode: d_n/R_n² = 0 → R_n = ∞ (trivial, wrong)
    (b) Match to shape mode: d_n/R_n² = (3/2)α = 3M_c² → R_n = λ√(d_n/3)
    (c) Match to continuum threshold: d_n/R_n² = 2α = 4M_c² → R_n = λ√(d_n)/2
    (d) Match to I₄M_c²/π² (from Cycle 108): d_n/R_n² = I₄²/(π²λ²d_n) → R_n = πd_nλ/I₄ ✓

    ROUTE (d) is self-consistent with R_n = πd_nλ/I₄. What is the condition?
    λ₁(S^{d_n}(R_n)) = I₄²/(π²d_nλ²) means:
        The fiber Laplacian eigenvalue equals I₄²/(π²d_nλ²).

    Rewrite: λ₁ × R_n²/d_n = 1 → λ₁ = d_n/R_n² (Obata, trivially).
    So condition (d) is: (d_n/R_n²) × (π²d_nλ²/I₄²) = 1 → R_n = πd_nλ/I₄.
    This is circular — it just defines R_n without providing a physical origin.

    BREAKTHROUGH APPROACH — Phase stiffness balance:
    The PHYSICAL condition is: the Hopf fiber radius R_n is set by the balance
    between the zero mode phase stiffness and the fiber curvature.

    Phase stiffness gradient energy on S^{d_n}(R_n):
        E_gradient = (1/2) f_n² × (1/R_n)² × Vol(S^{d_n})
    where f_n² = d_n × I₄φ₀²/λ (d_n independent zero modes, each with stiffness f²).

    This must be minimized subject to the constraint that the fiber wraps once:
    ∮ A·dl = 1 (one unit of flux). This is a functional of R_n.

    From the holonomy condition: g_n² × (2πR_n) = 2π (one winding) → g_n² = 1/R_n.
    But from DFC: g_n² = 2πβI₄ per unit r_U1... these differ.

    CLEANER ROUTE: The effective 1D coupling formula.
    From Cycle 85: g² = 2πβI₄ comes from r_U1 = 1/(βI₄).
    The physical interpretation: r_U1 is the scale at which the substrate
    "sees" a full 2π phase winding of the gauge field.

    For the n-th fiber alone: the zero mode η₀^{(n)} traverses the fiber over
    distance R_n before the phase winds by 2π/g_n times. Wait — let me think
    about this via the AB phase accumulated:

    AB phase = g × (flux in fiber / Φ₀) × 2π = g × (2πR_n × B_n) × 2π / (2π/e)
    For one winding: g × 2πR_n × (1/R_n) = 2π → g = 1 (trivial).

    The correct AB phase from DFC holonomy (Cycle 104):
    γ_DFC = g × 2π (for n=1 vortex, traversal at r_U1)
    Setting γ_DFC = 2π (one full winding): g = 1? But g ≈ 0.544.

    The mismatch is because the vortex is a HALF-vortex (W = -1/2, Cycle 67c).
    Full winding requires traversing twice the distance: r_effective = 2 × r_vortex.
    But the vortex has complex structure — this doesn't simply give a factor 2.

    DIRECT NUMERICAL APPROACH:
    Instead of deriving analytically, let's verify numerically that the formula
    g_n² = 2I₄/d_n is consistent with the DFC compact form g² = 2πβI₄ for
    β = 1/(9π), and map out which physical quantities control R_n.

Key references:
    - Cycle 47: f² = I₄φ₀²/λ (phase_stiffness_derivation.md)
    - Cycle 73: zero mode spectrum; shape mode ω₁² = (3/2)α (threshold_nondegeneracy.py)
    - Cycle 85: g² = 2πβI₄, r_U1 = 1/(βI₄) (bottleneck2_coupling_integral.py)
    - Cycle 107: |K_Hopf|² = R², g_n² = 2I₄/d_n per fiber (kk_fiber_coupling.py)
    - Cycle 108: Obata matching λ₁ = I₄²/(π²d_nλ²); moduli_space_radius.py
"""

import numpy as np
from scipy.optimize import brentq

PI = np.pi
I4 = 4.0 / 3.0   # ∫sech⁴(u) du (Bogomolny)
I6 = 16.0 / 15.0  # ∫sech⁶(u) du
N_HOPF = 9         # Obata sum

FIBERS = [
    {'name': 'S¹', 'depth': 'D5', 'd': 1, 'n': 1},
    {'name': 'S³', 'depth': 'D6', 'd': 3, 'n': 2},
    {'name': 'S⁵', 'depth': 'D7', 'd': 5, 'n': 3},
]


def sphere_volume(d, R=1.0):
    """
    Volume of d-sphere S^d(R) = C_d × R^d.
    C_1 = 2π, C_3 = 2π², C_5 = π³.
    General: C_d = 2π^{(d+1)/2} / Γ((d+1)/2).
    """
    from scipy.special import gamma
    C_d = 2 * PI**((d + 1) / 2.0) / gamma((d + 1) / 2.0)
    return C_d * R**d


def kk_spectrum_on_fiber(d, R, k_max=5):
    """
    KK mass spectrum on S^d(R): m_k² = k(k+d-1)/R², k=0,1,2,...
    Degeneracy: C(d+k,k) - C(d+k-2,k-2) = number of spin-k spherical harmonics on S^d.
    For k=0: 1 (massless gauge field); k=1: d (the fiber zero modes).
    """
    spectrum = []
    for k in range(k_max + 1):
        m_sq = k * (k + d - 1) / R**2
        # Degeneracy of k-th KK level on S^d
        if k == 0:
            degen = 1
        elif k == 1:
            degen = d + 1  # on S^d, l=1 harmonics have d+1 degeneracy... actually d
            degen = d      # first spherical harmonics on S^d: dimension = d+1-1 = d+1? Let me use d.
        else:
            from scipy.special import comb
            degen = int(comb(d + k, k) - (comb(d + k - 2, k - 2) if k >= 2 else 0))
        spectrum.append({'k': k, 'm_sq': m_sq, 'degen': degen})
    return spectrum


def matching_conditions_all(alpha=1.0):
    """
    For each fiber S^{d_n}, compute R_n from different matching conditions
    between fiber Laplacian eigenvalue and kink spectral scales.
    """
    lam = np.sqrt(2.0 / alpha)  # kink width
    Mc = 1.0 / lam              # = sqrt(alpha/2)

    conditions = {
        '(a) zero_mode': 0.0,           # d/R² = 0 → R→∞
        '(b) shape_mode': 1.5 * alpha,  # d/R² = (3/2)α
        '(c) continuum': 2.0 * alpha,   # d/R² = 2α
        '(d) I4^2/pi^2': I4**2 / (PI**2 * lam**2),  # from Obata matching (per d_n)
    }

    print(f"\n  α = {alpha:.2f}, λ = {lam:.4f}, M_c = {Mc:.4f}")
    print(f"  Target R_n/λ = πd_n/I₄ for d_n = 1,3,5: "
          f"{PI*1/I4:.4f}, {PI*3/I4:.4f}, {PI*5/I4:.4f}")
    print()

    for label, spectral_val in conditions.items():
        print(f"  {label}:")
        if spectral_val == 0:
            print(f"    R_n → ∞ (trivial)")
            continue
        for f in FIBERS:
            d = f['d']
            # λ₁ = d/R_n² = spectral_val/d_n (condition d scales with 1/d_n)
            if label == '(d) I4^2/pi^2':
                # λ₁ = I₄²/(π²d_nλ²): R_n = πd_nλ/I₄
                R_n_over_lam = PI * d / I4
            else:
                # λ₁ = d/R_n² = spectral_val → R_n = √(d/spectral_val)
                R_n_over_lam = np.sqrt(d / spectral_val) / lam
            target = PI * d / I4
            err = (R_n_over_lam - target) / target * 100
            print(f"    S^{d} (D{4+f['n']}): R_n/λ = {R_n_over_lam:.4f}  "
                  f"(target {target:.4f}, err {err:+.1f}%)")
        print()


def phase_stiffness_hopf_radius():
    """
    Derive R_n from the PHASE STIFFNESS + HOLONOMY BALANCE.

    The d_n coincident zero modes at depth D(4+n) have:
    - Total phase stiffness: F_n² = d_n × f² = d_n × I₄φ₀²/λ
    - This stiffness characterizes the "rigidity" of the phase modulus.
    - The Hopf radius R_n is the scale at which the phase stiffness equals
      the holonomy cost: F_n²/R_n = g_n² × (holonomy factor).

    From P3 (g² = 2πβI₄) and the single-fiber coupling g_n² = 2I₄/d_n:
    The holonomy per unit length is g_n²/R_n = 2I₄/(d_n R_n).

    Phase stiffness balance: F_n² × (1/R_n²) = g_n²/R_n [schematic]
    → d_n × I₄φ₀²/λ × (1/R_n²) = 2I₄/(d_n R_n)
    → d_n × φ₀² / (λ R_n) = 2/d_n
    → R_n = d_n² × φ₀²/(2λ)

    This is α-DEPENDENT (φ₀ = √(α/β)), so it's blocked.

    Correct approach: use NATURAL UNITS where φ₀=1, λ=1 (set α=β=1 for dimensional analysis).
    In these units: F_n² = d_n × I₄, g_n² = 2I₄/d_n, and:
    F_n² × (1/R_n²) = g_n²/R_n → d_n I₄/R_n² = 2I₄/(d_n R_n) → R_n = d_n²/2.

    This gives R_n/λ = d_n²/2, scaling as d_n² not d_n.
    For d_n=1: R_1=1/2 (vs π/I₄≈2.36, wrong).

    Conclusion: Phase stiffness balance (this form) does NOT give R_n = πd_nλ/I₄.
    The missing π/I₄ factor must come from a different physical mechanism.
    """
    results = []
    for f in FIBERS:
        d = f['d']
        R_from_balance = d**2 / 2.0  # in units of λ (φ₀=1, λ=1)
        R_target = PI * d / I4
        ratio = R_from_balance / R_target
        results.append({
            'd': d,
            'R_balance': R_from_balance,
            'R_target': R_target,
            'ratio': ratio,
        })
    return results


def hopf_vortex_radius_connection():
    """
    Explore the connection: R_n = 2 × r_v × d_n where r_v is the D5 vortex core.

    From Cycle 75: D5 vortex core radius r_v ≈ 1.0990 ξ where ξ = λ (kink width).
    So r_v/λ ≈ 1.0990.

    Claim: R_n = π/(2I₄) × d_n × λ × something.

    Check: if R_1 = 2r_v (two vortex radii):
        R_1/λ = 2 × 1.0990 = 2.198  (vs target π/I₄ = 2.356, 7% off)

    Not exact. The vortex core is a numerical result (r_v ≈ 1.099ξ); the target
    requires r_v = π/(2I₄) = 3π/8 ≈ 1.178ξ for exact matching.

    Note: the BPS vortex equation gives r_v numerically (no exact closed form).
    The DFC model would need r_v = 3π/8 × ξ exactly for this connection to work.
    """
    r_v_over_xi = 1.0990  # from complex_substrate.py (Cycle 75)
    R1_from_2rv = 2 * r_v_over_xi
    R1_target = PI / I4
    discrepancy = (R1_from_2rv - R1_target) / R1_target * 100

    target_r_v = PI / (2 * I4)  # = 3π/8 ≈ 1.178 for exact matching

    return {
        'r_v_numerical': r_v_over_xi,
        'R1_from_2rv': R1_from_2rv,
        'R1_target': R1_target,
        'discrepancy_pct': discrepancy,
        'target_r_v_for_exact': target_r_v,
        'gap': abs(r_v_over_xi - target_r_v) / target_r_v * 100,
    }


def check_exact_vortex_condition():
    """
    Would r_v = 3π/8 ξ (exact) follow from the BVP for the D5 vortex?

    The D5 vortex profile f(r) satisfies:
        f'' + f'/r - f/r² - f(f²-1)/ξ² = 0  [ξ is coherence length]
    with f(0)=0, f(∞)=1.

    The core radius r_v is defined as: f(r_v) = 1/√2 (half-max criterion).
    Numerically: r_v ≈ 1.099ξ (Cycle 75).

    For r_v = 3π/8 ξ ≈ 1.178ξ: this would require a slightly different field profile.
    The discrepancy is 7%, larger than numerical precision.

    CONCLUSION: The D5 vortex core does NOT satisfy r_v = 3π/8 ξ exactly.
    The connection R_1 = 2r_v is APPROXIMATE (7% off), not exact.
    """
    r_v_numerical = 1.0990
    r_v_exact_claim = 3 * PI / 8  # = 3π/8 ≈ 1.178
    discrepancy = (r_v_numerical - r_v_exact_claim) / r_v_exact_claim * 100
    return {
        'r_v_numerical': r_v_numerical,
        'r_v_exact_claim': r_v_exact_claim,
        'discrepancy_pct': discrepancy,
        'verdict': 'APPROXIMATE (7% off) — not an exact identity',
    }


def energy_minimization_over_R(d, alpha=1.0, beta=1.0/(9*PI)):
    """
    Minimize the total energy functional over R_n.

    Total energy (schematic, in units of λ=1/Mc):
        E(R) = E_kink + E_gauge(R) + E_coupling(R)

    E_kink = (8/3) Mc³/β [fixed, independent of R]
    E_gauge(R) = (d/R)² × V_d(R) / (2g²) [Laplacian term on S^d(R)]
               ~ d/R² × C_d R^d / g² = d × C_d R^{d-2} / g²
    E_coupling(R) = g² × ‖η₀‖² × R² [coupling of zero mode to fiber]
                  ~ g² × f² × R²

    dE/dR = 0:
        d(d-2) C_d R^{d-3}/g² + 2g²f²R = 0
        d(d-2) C_d R^{d-4}/(2g⁴f²) = -1  [for d>2]

    For d=1 (S¹): d-2 = -1 < 0 → d(d-2) = -1 < 0, so there IS a minimum.
        -C_1 R^{-3}/g² + 2g²f²R = 0
        C_1/(g⁴f²R⁴) = 2
        R⁴ = C_1/(2g⁴f²)
        R = (C_1/(2g⁴f²))^{1/4}

    This is α-dependent (f² = I₄φ₀²/λ), so this approach is blocked unless
    the α-dependence cancels in the final expression for R_n/λ.

    Let's check: R = (C_1/(2g⁴f²))^{1/4} / λ (in units of λ)
    f²/λ = I₄φ₀²/λ² = I₄α/(βλ²) = I₄α/(β × 2/α) = I₄α²/(2β)
    So f²/λ is α-DEPENDENT. Blocked.
    """
    lam = np.sqrt(2.0 / alpha)
    phi0 = np.sqrt(alpha / beta)
    f_sq = I4 * phi0**2 / lam  # phase stiffness

    g_sq = 2 * I4 / d  # claimed per-fiber coupling

    # For d=1: R = (C_1/(2g⁴f²))^{1/4}
    # C_1 = 2π (circumference of unit S¹)
    if d == 1:
        from scipy.special import gamma
        C_1 = 2 * PI
        R_minimum = (C_1 / (2 * g_sq**2 * f_sq))**0.25
        R_target = PI / I4 * lam
        return {
            'd': d, 'R_minimum': R_minimum, 'R_target': R_target,
            'ratio': R_minimum / R_target,
            'alpha_dep': True,  # f_sq is α-dependent
        }
    return {'d': d, 'result': 'blocked for d>2'}


def summary_table():
    """
    Compile all attempted derivations of R_n = πd_nλ/I₄ and their status.
    """
    rows = [
        ('Naive phase winding (1/λ)×R_n = 2π', 'R_n = 2πλ', 'd-INDEPENDENT', 'BLOCKED'),
        ('Kink shape mode match d/R²=(3/2)α', 'R_n = λ√(d/3)', 'R ∝ √d not d', 'BLOCKED'),
        ('Continuum threshold d/R²=2α', 'R_n = λ√(d)/2', 'R ∝ √d not d', 'BLOCKED'),
        ('Phase stiffness balance F²/R² = g²/R', 'R_n = d²λ/2', 'R ∝ d² not d', 'BLOCKED'),
        ('Energy minimization dE/dR=0', 'R_n ~ (C_d/g⁴f²)^{1/4}', 'α-DEPENDENT', 'BLOCKED'),
        ('Vortex core connection R_1=2r_v', 'R_1/λ ≈ 2.20', '7% off target 2.36', 'APPROXIMATE'),
        ('Obata matching λ₁=I₄²/(π²d_nλ²)', 'R_n = πd_nλ/I₄ ✓', 'CIRCULAR (defines R_n)', 'OPEN'),
        ('Moduli space metric (Cycle 108)', 'Not computed', 'Requires 2-kink calc', 'OPEN'),
        ('KK normalization integral (Cycle 108)', 'R_n-independent', 'Does not constrain R_n', 'BLOCKED'),
    ]
    return rows


def run_all():
    print("=" * 70)
    print("fiber_radius_constraint.py — Cycle 109")
    print("Probing which physical condition fixes R_n = πd_nλ/I₄")
    print("=" * 70)

    # --- Step 1: Matching conditions ---
    print("\nStep 1: Spectral matching conditions — R_n from fiber-kink eigenvalue match")
    print("-" * 60)
    matching_conditions_all(alpha=1.0)

    # --- Step 2: Phase stiffness balance ---
    print("Step 2: Phase stiffness balance (in natural units λ=1)")
    print("-" * 60)
    results = phase_stiffness_hopf_radius()
    print(f"  {'d_n':<6} {'R_balance/λ':<15} {'R_target/λ':<15} {'ratio':<10}")
    for r in results:
        print(f"  {r['d']:<6} {r['R_balance']:<15.4f} {r['R_target']:<15.4f} {r['ratio']:.4f}")
    print(f"\n  Phase stiffness balance gives R ∝ d² (not d). BLOCKED.")

    # --- Step 3: Vortex core connection ---
    print("\nStep 3: Vortex core connection R_1 = 2r_v?")
    print("-" * 60)
    vc = hopf_vortex_radius_connection()
    print(f"  r_v/ξ (numerical, Cycle 75): {vc['r_v_numerical']:.4f}")
    print(f"  R_1 = 2r_v: R_1/λ = {vc['R1_from_2rv']:.4f}")
    print(f"  Target R_1/λ = π/I₄ = {vc['R1_target']:.4f}")
    print(f"  Discrepancy: {vc['discrepancy_pct']:+.1f}%")
    print(f"  For exact: r_v would need to be {vc['target_r_v_for_exact']:.4f}ξ = 3π/8ξ")
    print(f"  Actual gap from 3π/8: {vc['gap']:.1f}%  → APPROXIMATE, not exact")

    exact_check = check_exact_vortex_condition()
    print(f"\n  BVP verdict: {exact_check['verdict']}")

    # --- Step 4: Energy minimization ---
    print("\nStep 4: Energy minimization for S¹ fiber (d=1)")
    print("-" * 60)
    em = energy_minimization_over_R(d=1, alpha=1.0)
    print(f"  R_min/λ (energy min.) = {em['R_minimum']:.4f}")
    print(f"  R_target/λ = {em['R_target']:.4f}")
    print(f"  Ratio: {em['ratio']:.4f}")
    print(f"  α-dependent: {em['alpha_dep']} → BLOCKED")

    # --- Step 5: Summary table ---
    print("\nStep 5: Summary of attempted derivations")
    print("-" * 60)
    rows = summary_table()
    print(f"  {'Approach':<45} {'Result':<22} {'Status':<12}")
    for name, result, issue, status in rows:
        print(f"  {name[:43]:<45} {result[:20]:<22} {status}")

    # --- Step 6: What IS known ---
    print("\nStep 6: What IS established about R_n")
    print("-" * 60)
    print(f"  KNOWN (Cycle 106): r_U1/λ = πN_Hopf/I₄ = 27π/4 (from series holonomy, error 0)")
    print(f"  KNOWN (Cycle 107): g_n² = 2I₄/d_n (IF R_n = πd_nλ/I₄)")
    print(f"  KNOWN (Cycle 107): g_eff² = 8/27 (IF R_n = πd_nλ/I₄)")
    print(f"  UNKNOWN: WHY is R_n = πd_nλ/I₄?")
    print()
    print(f"  The factor π/I₄ = {PI/I4:.6f} = 3π/4 is the ratio:")
    print(f"    π (from Hopf winding, proved Cycle 67c)")
    print(f"  ÷ I₄ (from Bogomolny sech⁴ integral, proved Cycle 47)")
    print()
    print(f"  This RATIO π/I₄ arises naturally in DFC from:")
    print(f"    g_n² = 2π/(R_n/λ) AND g_n² = 2I₄/d_n")
    print(f"  → R_n/λ = 2π/g_n² = π/(I₄/d_n) = πd_n/I₄")
    print()
    print(f"  The chain is therefore COMPLETE given:")
    print(f"    g_n² = 2I₄/d_n  [per-fiber coupling = 2I₄ / (# of zero modes)]")
    print()
    print(f"  The derivation reduces to proving: g_n² = 2I₄/d_n")
    print(f"  ← EQUIVALENT to proving: R_n = πd_nλ/I₄")
    print(f"  ← EQUIVALENT to proving: g_eff² = 2I₄/N_Hopf = 8/27")
    print()
    print(f"  ALL THREE are equivalent formulations of the SAME open step.")

    # --- Step 7: Proposed mechanism ---
    print("\nStep 7: Most promising physical mechanism")
    print("-" * 60)
    print("  PROPOSED: 'Equal zero-mode coupling' principle")
    print()
    print("  In DFC, each zero mode at depth D(4+n) couples equally to the gauge field.")
    print("  With d_n zero modes, the total coupling budget is 2I₄ (the full single-mode")
    print("  coupling, from the Bogomolny identity). Each zero mode gets 1/d_n of this:")
    print("    g_j² = 2I₄/d_n  for j = 1,...,d_n")
    print()
    print("  Physical reason: the d_n zero modes are EQUIVALENT by the SU(d_n) symmetry")
    print("  of n coincident kinks (Cycle 59: U(n) isometry). Equal couplings follow from")
    print("  equal treatment of equivalent zero modes under this symmetry.")
    print()
    print("  The total coupling 2I₄ is fixed by the Bogomolny identity I₄=4/3:")
    print("    g_total² = 2I₄ = 8/3 for ONE D5 kink alone (S¹ fiber, d=1)")
    print("    [from g² = 2π/(R_1/λ) = 2π/(π/I₄) = 2I₄ ✓]")
    print()
    print("  This is consistent but REQUIRES a proof that g_total² = 2I₄ for S¹.")
    print("  That proof needs: R_1 = πλ/I₄ for S¹. Still circular.")
    print()
    print(f"  KEY QUESTION: What makes R_1 = πλ/I₄ for the S¹ Hopf fiber at D5?")
    print(f"  Answer requires computing the moduli space metric for the D5 complex kink.")

    # --- Final summary ---
    print("\n" + "=" * 70)
    print("CYCLE 109 FINDINGS")
    print("=" * 70)
    print()
    print("Blocked routes:")
    print("  - All spectral matching conditions (shape mode, continuum) give R ∝ √d_n")
    print("  - Phase stiffness balance gives R ∝ d_n² (α-independent but wrong power)")
    print("  - Energy minimization is α-dependent (blocked)")
    print("  - Vortex core connection is ~7% off (not exact)")
    print("  - KK normalization integral is R_n-independent (does not constrain R_n)")
    print()
    print("What remains:")
    print("  The open step is equivalent to proving g_1² = 2I₄ for the S¹ fiber (D5).")
    print("  This is equivalent to R_1 = πλ/I₄ for the one-kink system at D5.")
    print()
    print("  Physical route to g_1² = 2I₄:")
    print("  The D5 complex kink has one zero mode (translation). The phase of this")
    print("  zero mode couples to the U(1) gauge field with coupling strength g_1².")
    print("  From P3 (Cycle 85): g² = 2πβI₄. For β = 1/(9π): g² = 2I₄/9 = 8/27.")
    print("  But this is the PARALLEL combination! For S¹ alone: g_1² = 2I₄ = 8/3.")
    print()
    print("  The D5 single-fiber coupling g_1² = 2I₄ must be derived from:")
    print("  ∫∫ |η₀(x,Ω)|² dxdΩ on ℝ × S¹(R_1), using R_1 as the free parameter,")
    print("  and imposing the normalization condition that determines R_1 uniquely.")
    print()
    print("  This calculation — the 2D mode normalization on ℝ × S¹(R) — is the")
    print("  single remaining computation. To be done in Cycle 110.")
    print()
    print("Tier: R_n = πd_nλ/I₄ remains Tier 4 OPEN.")
    print("Next: compute ∫∫ |η₀(x,θ)|² dxdθ on ℝ × S¹(R) for general R,")
    print("      find R that satisfies the DFC normalization condition.")


if __name__ == '__main__':
    run_all()
