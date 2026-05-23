"""
D6/D7 overlap integral — Bottleneck 3 quantitative analysis (Cycle 131).

PHYSICAL QUESTION:
  The Higgs mass parameter μ² requires a coupling between the D7 SU(3) closure
  and the D6 SU(2) squashing mode. How large must this coupling be, and what
  overlap integral form provides it?

DFC MECHANISM:
  The D7 kink (SU(3) closure at scale M_c(D7)) exerts a pressure on the D6
  S³ squashing mode (SU(2) closure at M_c(D6)). This coupling generates the
  negative mass-squared term in the Higgs potential: μ²_DFC = α_D7 × I_D67.

NEW IN CYCLE 131 (using ECCC scales from mc_closure_scales.py):
  M_c(D6) = 9.698×10¹² GeV  [ECCC: α₂(M_c(D6)) = g_eff²/(4π)]
  M_c(D7) = 1.566×10¹⁵ GeV  [ECCC: α₃(M_c(D7)) = g_eff²/(4π)]
  Δ_D67   = 5.085  [= log(M_c(D7)/M_c(D6)), Tier 3, ECCC Cycle 130]
  ξ_D7/ξ_D6 = exp(-5.085) ≈ 0.00619

REQUIRED I_D67 (from Bottleneck 3 consistency condition):
  μ²_DFC [GeV²] = α_D7 [GeV²] × I_D67  →  I_D67 = μ²_required / α_D7
  μ²_required = β × v²/2  [from V(ε) = -α/2 ε² + β/4 ε⁴ minimum condition]
  α_D7 = 2 × M_c(D7)²     [substrate coupling at D7 depth]
  → I_D67_required = β v² / (4 M_c(D7)²) ≈ 2.17×10⁻²⁸

PROFILE OVERLAP ANALYSIS:
  For kink profiles sech²(x/ξ_Di), the narrow-kink overlap in the limit ξ_D7 ≪ ξ_D6:
    ∫ sech²(x/ξ_D6) sech²(x/ξ_D7) dx ≈ 2ξ_D7

  Normalized to make dimensionless: divide by 2ξ_D6 (the D6 kink width):
    I_sech ≈ ξ_D7/ξ_D6 = M_c(D6)/M_c(D7) = exp(-Δ_D67) ≈ 0.00619

  GAP: I_sech/I_required ≈ 2.9×10²⁵ — profile overlap alone is 25 orders too large.

GAP ANALYSIS — THREE ROUTES:
  Route 1 (multi-step cascade): product of N identical overlaps
    I_D67 = exp(-N × Δ_D67)  →  N = ln(1/I_required) / Δ_D67 ≈ 12.7 steps
    Interpretation: 13 intermediate depth transitions each contributing exp(-5.08)
    Assessment: DFC has only 4 active depth transitions (D1-D7); N=13 is not available.

  Route 2 (power law: (v/M_c(D7))^p):
    I_D67 = (v/M_c(D7))^p
    p needed: 28 / log₁₀(M_c(D7)/v) ≈ 28 / 13.0 ≈ 2.15
    For p=2: I_D67 = (246/1.566e15)² = 2.47×10⁻²⁶  [ratio = 114× too large]
    For p=2.15: I_D67 ≈ 2.17×10⁻²⁸  [matches, but p must be derived]

  Route 3 (re-examine μ² formula):
    The formula μ²_DFC = α_D7 × I_D67 places the full D7 scale in the numerator.
    Alternative: μ²_DFC = M_c(D6)² × f(β, Δ_D67) where f is an O(1) function.
    This gives μ² in D6 units directly, without the enormous α_D7 factor.
    Assessment: If f(β, Δ_D67) ~ β/4 × exp(-2Δ_D67), then:
      μ²_DFC = M_c(D6)² × β/4 × exp(-2Δ_D67)
              = (9.70×10¹²)² × (1/(9π))/4 × exp(-10.17)
              = 9.41×10²⁵ × 0.00877 × 3.83×10⁻⁵
              = 3.16×10¹⁸ GeV² [still 15 orders too large for 1063 GeV²]

STRUCTURAL FINDING:
  The ~10⁻²⁸ suppression required for I_D67 is NOT naturally produced by:
    (a) A single kink profile overlap (gives ~10⁻³)
    (b) A simple power law in v/M_c(D7) (gives ~10⁻²⁶ for p=2)
    (c) A product of Δ_D67 overlaps with DFC depth count (gives ~10⁻¹⁰ for N=4)

  The suppression is fundamentally the hierarchy problem: μ² ~ 1000 GeV² while
  α_D7 ~ 10³⁰ GeV². In the SM this fine-tuning has no explanation. In DFC, the
  question becomes: does the substrate dynamics naturally produce a coupling
  I_D67 = 2×10⁻²⁸ without fine-tuning?

  REVISED FORMULA CANDIDATE (Cycle 131):
    Instead of I_D67 = μ²/α_D7, consider the formula:
      μ²_DFC = M_c(D6)² × (v/M_c(D7))^n × g(β)
    where n is derived from D6/D7 coupling structure.
    This makes the suppression explicit as a power of the scale ratio.
    With n=2: μ²_DFC = M_c(D6)² × (v/M_c(D7))² × g(β)
              = M_c(D6)² × exp(-2Δ_total) × g(β)
              where Δ_total = log(M_c(D7)/v) ≈ 30.0

    TARGET: μ²_DFC = 1063 GeV² = β v²/2
    CHECK: M_c(D6)² × (v/M_c(D7))² × g(β) = 1063 GeV²
      → g(β) = 1063 / [M_c(D6)² × (v/M_c(D7))²]
             = β v²/2 / [M_c(D6)² × v²/M_c(D7)²]
             = β/2 × (M_c(D7)/M_c(D6))²
             = β/2 × exp(2Δ_D67)
             = (1/9π)/2 × exp(10.17)
             = 0.01768 × 2607
             = 46.1   [this is an O(1)? → NO, it's O(50)]

    So this route gives g(β) ≈ 46, not O(1). Still not natural.

CONCLUSION (Cycle 131):
  The Bottleneck 3 gap for μ² requires physics beyond the simple kink overlap.
  Three possible resolutions:
  (a) The correct formula for μ² in DFC is NOT μ² = α_D7 × I_D67 but involves
      a different coupling mechanism between D6 and D7 depth modes.
  (b) There is additional logarithmic running of μ² from M_c(D7) down to v
      (radiative generation of μ² at the electroweak scale from D7 corrections).
  (c) The suppression is topological — only certain winding configurations couple
      D7 to D6, giving additional selection rules that suppress I_D67.

  The most promising route: (b) radiative generation — analogous to the CW
  potential derivation, where μ² is generated at one loop with log(M_c(D7)/v)
  enhancing the D7 contribution. This gives:
    μ²_rad ≈ (g_eff²/16π²) × M_c(D7)² × log(M_c(D7)/v)

  Check: (8/27)/(16π²) × (1.566e15)² × log(1.566e15/246)
       = 0.01883 × 2.45×10³⁰ × 30.0
       ≈ 1.38×10³⁰ GeV² [still 27 orders too large!]

  Radiative generation at one loop doesn't help — α_D7 ≫ μ² still.

  Verdict: The Bottleneck 3 gap is the hierarchy problem recast in DFC language.
  The model must explain WHY μ² ≪ M_c(D7)² without fine-tuning. This is an
  open problem at Tier 4. The structural account (D1-D6 depth separation
  providing exponential decoupling) gives a qualitative argument but not
  a quantitative one.

KEY REFERENCES:
  - equations/mc_closure_scales.py   (ECCC scales, Δ_D67=5.085, Cycle 130)
  - equations/vev_derivation.py      (μ² formula, λ from β, target μ=23 GeV, Cycle 86)
  - foundations/vev_derivation.md    (Bottleneck 3 mapping, Cycles 53,58,79,86)
  - foundations/hierarchy_problem.md (DFC hierarchy dissolution argument)
  - foundations/alpha_s_derivation.md (ECCC, M_c(D7)=1.566e15 GeV, Cycle 130)

Usage:
    python3 equations/d6_d7_overlap.py
"""

import math

# ─── ECCC Closure Scales (Cycle 130, mc_closure_scales.py) ───────────────────

G_EFF_SQ     = 8.0 / 27.0                    # g_eff² = 2I₄/N_Hopf [Tier 2a]
ALPHA_COMMON = G_EFF_SQ / (4.0 * math.pi)    # = 2/(27π) ≈ 0.02358
BETA         = 1.0 / (9.0 * math.pi)         # β = 1/(9π) [Tier 2a, Cycle 117]

# ECCC closure scales
M_Z   = 91.1876     # GeV
MC_D6 = 9.6978e12   # GeV  [ECCC: α₂(M_c(D6)) = α_common]
MC_D7 = 1.5663e15   # GeV  [ECCC: α₃(M_c(D7)) = α_common]
DELTA_D67 = math.log(MC_D7 / MC_D6)          # = 5.085

# Kink widths
XI_D6 = 1.0 / MC_D6    # GeV⁻¹
XI_D7 = 1.0 / MC_D7    # GeV⁻¹

# Electroweak VEV
V_EW = 246.0  # GeV

# ─── Consistency Target ───────────────────────────────────────────────────────

def mu_required_gev():
    """
    Target μ for Higgs potential minimum: μ = v × √λ_DFC = v × √(β/4).

    From V(ε) = −α_D6/2 ε² + β/4 ε⁴, minimum at ε₀ = √(α_D6/β),
    v = √2 × ε₀ → α_D6 = β v²/2 → μ² = α_D6 = β v²/2.
    """
    lam_dfc = BETA / 4.0
    return V_EW * math.sqrt(lam_dfc)

def mu_sq_required_gev2():
    """μ² required to produce v = 246 GeV in the DFC Higgs potential."""
    return BETA * V_EW**2 / 2.0

def alpha_D7_gev2():
    """D7 compression parameter: α_D7 = 2 M_c(D7)²."""
    return 2.0 * MC_D7**2

def i_d67_required():
    """
    Required dimensionless overlap integral I_D67 from μ² = α_D7 × I_D67.

    I_D67 = μ²_required / α_D7 = (β v² / 2) / (2 M_c(D7)²)
           = β v² / (4 M_c(D7)²)
    """
    return mu_sq_required_gev2() / alpha_D7_gev2()


# ─── Profile Overlap Integrals ────────────────────────────────────────────────

def sech2_overlap_narrow(xi_narrow, xi_wide):
    """
    Sech² kink profile overlap in the narrow-kink limit (xi_narrow ≪ xi_wide).

    ∫ sech²(x/xi_wide) sech²(x/xi_narrow) dx ≈ 2 × xi_narrow

    This is the leading-order result when the D7 kink width ξ_D7 is much
    smaller than the D6 kink width ξ_D6: the D7 kink appears as a delta
    function from the D6 profile's perspective.

    Returns the integral in units of GeV⁻¹.
    """
    return 2.0 * xi_narrow

def sech2_overlap_exact(xi_d6, xi_d7, n_points=10000):
    """
    Numerically exact sech² overlap integral.

    ∫_{-∞}^{∞} sech²(x/ξ_D6) × sech²(x/ξ_D7) dx

    Integrate over range ±8 × max(ξ_D6, ξ_D7).

    Returns the integral in units of GeV⁻¹.
    """
    xi_max = max(xi_d6, xi_d7)
    x_max  = 8.0 * xi_max
    dx     = 2.0 * x_max / n_points
    total  = 0.0
    for i in range(n_points):
        x = -x_max + (i + 0.5) * dx
        u6 = x / xi_d6
        u7 = x / xi_d7
        # Avoid overflow: cosh(u)² overflows for |u| > ~355; sech²→0 for large |u|
        s6 = 1.0 / (math.cosh(u6))**2 if abs(u6) < 354 else 0.0
        s7 = 1.0 / (math.cosh(u7))**2 if abs(u7) < 354 else 0.0
        total += s6 * s7 * dx
    return total

def i_sech_normalized(xi_d6, xi_d7):
    """
    Dimensionless version of the sech² overlap: divide by 2ξ_D6 (D6 kink norm).

    I_sech = [∫ sech²(x/ξ_D6) sech²(x/ξ_D7) dx] / (2 ξ_D6)

    In the narrow-kink limit: I_sech ≈ ξ_D7/ξ_D6 = M_c(D6)/M_c(D7).
    """
    integral = sech2_overlap_narrow(xi_d7, xi_d6)
    return integral / (2.0 * xi_d6)


# ─── Gap Analysis ─────────────────────────────────────────────────────────────

def gap_factor():
    """
    Ratio I_sech / I_required — how many orders of magnitude the simple
    kink profile overlap overestimates the required I_D67.
    """
    i_sech = i_sech_normalized(XI_D6, XI_D7)
    i_req  = i_d67_required()
    return i_sech / i_req

def cascade_n_steps(i_req, delta, base=None):
    """
    How many identical overlap steps of size exp(-delta) would be needed
    to reach I_D67 = i_req?

    I = exp(-N × delta) → N = -log(i_req) / delta
    """
    if base is None:
        # exp(-delta) per step
        n = -math.log(i_req) / delta
    else:
        n = -math.log(i_req) / math.log(1.0 / base)
    return n

def power_law_p(i_req, ratio):
    """
    What power p satisfies (ratio)^p = i_req?
    p = log(i_req) / log(ratio)
    """
    return math.log(i_req) / math.log(ratio)


# ─── Alternative μ² Formulas ──────────────────────────────────────────────────

def mu_sq_radiative(g_eff_sq, mc_d7, v):
    """
    Radiative generation of μ² at one loop.

    Schematic one-loop Coleman-Weinberg contribution from D7 sector:
      μ²_rad ≈ (g_eff² / 16π²) × M_c(D7)² × log(M_c(D7)/v)

    This is the type of formula that appears in radiative symmetry breaking.
    Returns μ²_rad in GeV².
    """
    log_ratio = math.log(mc_d7 / v)
    return (g_eff_sq / (16.0 * math.pi**2)) * mc_d7**2 * log_ratio

def mu_sq_d6_scale(mc_d6, beta, delta_d67, n_overlap=1):
    """
    Alternative formula: μ² from D6 scale with overlap suppression.

    μ²_DFC = M_c(D6)² × (β/4) × exp(-n × Δ_D67)

    This anchors μ² to the D6 scale and adds the D6/D7 overlap suppression
    as a power. For n=2: exp(-2×5.08) ≈ 4×10⁻⁵.

    Returns μ²_alt in GeV².
    """
    lam_dfc = beta / 4.0
    return mc_d6**2 * lam_dfc * math.exp(-n_overlap * delta_d67)


# ─── Main Output ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("D6/D7 OVERLAP INTEGRAL — BOTTLENECK 3 ANALYSIS")
    print("Using ECCC closure scales (Cycle 130 + Cycle 131)")
    print("=" * 70)

    print("\n[ECCC CLOSURE SCALES — Tier 3, mc_closure_scales.py]")
    print(f"  g_eff²     = 8/27 = {G_EFF_SQ:.6f}  [Tier 2a, Cycle 117]")
    print(f"  α_common   = 2/(27π) = {ALPHA_COMMON:.6f}")
    print(f"  β          = 1/(9π) = {BETA:.6f}  [Tier 2a, Cycle 117]")
    print(f"  M_c(D6)    = {MC_D6:.4e} GeV  [ECCC: α₂ = α_common]")
    print(f"  M_c(D7)    = {MC_D7:.4e} GeV  [ECCC: α₃ = α_common, self-consistent]")
    print(f"  Δ_D67      = ln(M_c(D7)/M_c(D6)) = {DELTA_D67:.4f}")
    print(f"  ξ_D7/ξ_D6  = M_c(D6)/M_c(D7) = exp(-Δ_D67) = {math.exp(-DELTA_D67):.5f}")

    print("\n[BOTTLENECK 3 CONSISTENCY TARGET]")
    mu_req    = mu_required_gev()
    mu_sq_req = mu_sq_required_gev2()
    a_D7      = alpha_D7_gev2()
    i_req     = i_d67_required()
    lam_dfc   = BETA / 4.0
    print(f"  λ_DFC      = β/4 = {lam_dfc:.6f}  [substrate quartic at D6 depth, Cycle 58]")
    print(f"  μ_required = v × √λ_DFC = {mu_req:.2f} GeV  [to give v=246 GeV]")
    print(f"  μ²_required = β v²/2    = {mu_sq_req:.2f} GeV²")
    print(f"  α_D7        = 2M_c(D7)² = {a_D7:.3e} GeV²  [D7 compression parameter]")
    print(f"  I_D67_required = μ²/α_D7 = {i_req:.3e}  [dimensionless — from μ²=α_D7×I_D67]")
    print(f"  = β v² / (4 M_c(D7)²) = {BETA:.5f} × {V_EW}² / (4 × {MC_D7:.3e}²)")
    print(f"  = (v/M_c(D7))² × β/4 = ({V_EW/MC_D7:.3e})² × {lam_dfc:.5f}")
    print(f"  = {(V_EW/MC_D7)**2:.3e} × {lam_dfc:.5f} = {i_req:.3e}")

    print("\n[PROFILE OVERLAP — NARROW-KINK LIMIT]")
    integral_dim = sech2_overlap_narrow(XI_D7, XI_D6)
    i_sech = i_sech_normalized(XI_D6, XI_D7)
    gap = gap_factor()
    print(f"  ∫ sech²(x/ξ_D6) sech²(x/ξ_D7) dx ≈ 2ξ_D7 = {integral_dim:.3e} GeV⁻¹")
    print(f"  Normalized: I_sech = (2ξ_D7)/(2ξ_D6) = ξ_D7/ξ_D6 = {i_sech:.5f}")
    print(f"  = M_c(D6)/M_c(D7) = exp(-Δ_D67) = exp(-{DELTA_D67:.3f}) = {math.exp(-DELTA_D67):.5f}")
    print(f"  Required:   I_D67  = {i_req:.3e}")
    print(f"  Gap factor: I_sech / I_required = {gap:.3e}  ({math.log10(gap):.1f} orders of magnitude)")
    print(f"  → Kink profile overlap is {math.log10(gap):.0f} orders too large!")

    # Also show the exact numerical integral (with high precision)
    print(f"\n[NUMERICAL VERIFICATION — exact sech² integral]")
    i_exact = sech2_overlap_exact(XI_D6, XI_D7, n_points=5000)
    i_narrow = sech2_overlap_narrow(XI_D7, XI_D6)
    print(f"  Exact numerical: {i_exact:.6e} GeV⁻¹")
    print(f"  Narrow-kink:     {i_narrow:.6e} GeV⁻¹")
    print(f"  Relative error:  {abs(i_exact/i_narrow - 1):.2e}  (narrow-kink is excellent for ξ_D7≪ξ_D6)")

    print("\n[GAP ANALYSIS — THREE ROUTES]")

    # Route 1: cascade
    n_steps = cascade_n_steps(i_req, DELTA_D67)
    print(f"\n  Route 1 — multi-step cascade (product of N overlaps):")
    print(f"    I_D67 = exp(-N × Δ_D67)  →  N = {n_steps:.1f} steps needed")
    print(f"    DFC has N_max = 4 active depth transitions (D1→D7)")
    print(f"    With N=4: I = exp(-4×{DELTA_D67:.3f}) = {math.exp(-4*DELTA_D67):.3e}")
    print(f"    With N=2 (D6→D7 only): I = exp(-2×{DELTA_D67:.3f}) = {math.exp(-2*DELTA_D67):.3e}")
    print(f"    Assessment: N=12.7 required but DFC has only 4 depth steps → INSUFFICIENT")

    # Route 2: power law
    scale_ratio = V_EW / MC_D7
    p_needed = power_law_p(i_req, scale_ratio)
    print(f"\n  Route 2 — power law in v/M_c(D7):")
    print(f"    I_D67 = (v/M_c(D7))^p = ({scale_ratio:.3e})^p")
    print(f"    log₁₀(v/M_c(D7)) = {math.log10(scale_ratio):.3f}")
    print(f"    p needed = log(I_req)/log(v/M_c(D7)) = {p_needed:.3f}")
    for p in [1, 2, p_needed, 3]:
        i_p = scale_ratio**p
        print(f"    p={p:.2f}: I = (v/M_c(D7))^{p:.2f} = {i_p:.3e}  [ratio to req: {i_p/i_req:.3e}]")
    print(f"    Assessment: p≈2.15 gives exact match; must derive p from DFC dynamics.")

    # Route 3: radiative
    print(f"\n  Route 3 — one-loop radiative generation:")
    mu_sq_rad = mu_sq_radiative(G_EFF_SQ, MC_D7, V_EW)
    print(f"    μ²_rad = (g_eff²/16π²) × M_c(D7)² × log(M_c(D7)/v)")
    print(f"           = ({G_EFF_SQ:.4f}/16π²) × ({MC_D7:.3e})² × {math.log(MC_D7/V_EW):.2f}")
    print(f"           = {mu_sq_rad:.3e} GeV²")
    print(f"    Required: {mu_sq_req:.2f} GeV²")
    print(f"    Ratio: {mu_sq_rad/mu_sq_req:.3e}  (one-loop correction is {math.log10(mu_sq_rad/mu_sq_req):.0f} orders too large)")
    print(f"    Assessment: One-loop radiative from D7 scale still gives μ²~M_c(D7)² → NOT helpful")

    # Route 4: D6-scale formula
    print(f"\n  Route 4 — μ² anchored to D6 scale with n-overlap suppression:")
    print(f"    μ²_alt = M_c(D6)² × (β/4) × exp(-n × Δ_D67)")
    for n in [0, 1, 2, 3, 4]:
        mu_sq_alt = mu_sq_d6_scale(MC_D6, BETA, DELTA_D67, n)
        ratio = mu_sq_alt / mu_sq_req
        print(f"    n={n}: μ²_alt = {mu_sq_alt:.3e} GeV²  [ratio to req: {ratio:.3e}]")
    # Find n that gives the right answer
    # mu_sq_req = MC_D6² × (β/4) × exp(-n × Δ_D67)
    # exp(-n × Δ_D67) = mu_sq_req / (MC_D6² × β/4)
    target_exp = mu_sq_req / (MC_D6**2 * lam_dfc)
    n_exact = -math.log(target_exp) / DELTA_D67
    print(f"    Exact n: {n_exact:.3f}  (to reproduce μ²=β v²/2)")
    print(f"    exp(-n_exact × Δ_D67) = {target_exp:.3e}")
    print(f"    Assessment: n≈{n_exact:.1f} overlaps required — must derive from D6/D7 coupling.")

    print("\n[STRUCTURAL SUMMARY]")
    print(f"  The Bottleneck 3 gap for μ² is the hierarchy problem in DFC language.")
    print(f"  Required: I_D67 = β v² / (4 M_c(D7)²) = {i_req:.3e}")
    print(f"  This is (v/M_c(D7))² × β/4, naturally small because v ≪ M_c(D7).")
    print()
    print(f"  The DFC structural argument (hierarchy_problem.md) claims that the")
    print(f"  D1-to-D6 depth separation exponentially decouples Planck corrections.")
    print(f"  The QUANTITATIVE version requires deriving a power p≈2 or an overlap")
    print(f"  count n≈{n_exact:.1f} from the D6/D7 coupling dynamics.")
    print()
    print(f"  TIER ASSIGNMENTS:")
    print(f"    μ²_required = β v²/2 = {mu_sq_req:.2f} GeV²: Tier 3 [β Tier 2a; v experimental]")
    print(f"    I_D67_required = {i_req:.3e}: Tier 3 [from consistency condition]")
    print(f"    Narrow-kink sech² overlap gives {i_sech:.5f} (≠ {i_req:.2e}): gap unresolved")
    print(f"    Power law p≈2.15 route: Tier 4 [p not yet derived from substrate]")
    print()
    print(f"  BOTTLENECK 3 OPEN PROBLEM (Tier 4):")
    print(f"    Derive μ² in GeV² from the DFC D6/D7 coupling mechanism.")
    print(f"    Options: (a) derive power p from D6/D7 mode structure;")
    print(f"             (b) show the sech² overlap formula is wrong and find the")
    print(f"                 correct coupling operator;")
    print(f"             (c) compute the Coleman-Weinberg potential at D7 scale.")
    print()
    print(f"  KEY INPUT FROM ECCC (Cycle 130, non-circular):")
    print(f"    Δ_D67 = {DELTA_D67:.4f}  [= log(M_c(D7)/M_c(D6)) — input to overlap analysis]")
    print(f"    This constrains the kink width ratio ξ_D7/ξ_D6 = {math.exp(-DELTA_D67):.5f}")
    print(f"    and sets the natural suppression scale exp(-Δ_D67) = {math.exp(-DELTA_D67):.5f}.")

    print("\n[VERIFICATION]")
    # Check: required I_D67 consistency
    mu_sq_check = a_D7 * i_req
    print(f"  μ²_DFC = α_D7 × I_D67 = {a_D7:.3e} × {i_req:.3e} = {mu_sq_check:.3f} GeV²")
    print(f"  Target μ²_required = {mu_sq_req:.3f} GeV²")
    print(f"  Consistency: {abs(mu_sq_check/mu_sq_req - 1):.2e}  (machine precision ✓)")
    print(f"  v from these: v = √(2μ²/β) = {math.sqrt(2*mu_sq_check/BETA):.2f} GeV  (target 246 GeV ✓)")
