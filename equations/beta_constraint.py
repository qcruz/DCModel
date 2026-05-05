"""
β derivation candidates for V(φ) = −α/2 φ² + β/4 φ⁴.

The quartic coupling β is the single dimensionless shape parameter of the DFC
potential. The kink width λ = √(2c²/α) sets the length scale (via α); β controls
the ratio of barrier height to kink energy, the shape of the kink profile, and —
through g² = 8πβ/3 — all gauge couplings. This module systematically analyzes
all known candidates for fixing β from substrate dynamics.

Key result (Cycle 101): β = 1/(9π) from Hopf fiber dimension sum.
The three Hopf fibers at D5/D6/D7 are S¹, S³, S⁵ with dimensions 1, 3, 5.
Their sum is 9. The natural normalization β = 1/(9π) gives g² = 8/27 exactly,
with g = √(8/27) = 2√2/(3√3) matching g_common (SM) to 0.006%.

Summary of candidates:
  (a) kink width = Planck length  →  fixes α, NOT β.  BLOCKED.
  (b) S_kink/ℏ = integer          →  fixes α/β jointly; no natural integer.  BLOCKED.
  (c) ΔV/E_kink = topological     →  ΔV/E_kink = 3√(2α)/16, α-dependent.  BLOCKED.
  (d) β = 1/(dim_Hopf_total × π)  →  β = 1/(9π), g² = 8/27. NEW CANDIDATE.
      dim_Hopf_total = dim(S¹)+dim(S³)+dim(S⁵) = 1+3+5 = 9.
      Status: Tier 3 structural argument (derivation from V(φ) dynamics still open).

References:
  - foundations/coupling_derivation.md  (Bottleneck 2 status, 3-step chain)
  - equations/bottleneck2_beta_selfconsistency.py  (β_B2 self-consistency, Cycle 100)
  - equations/bottleneck2_2d_integral.py  (vortex integrals, Cycle 96)
  - foundations/hopf_fibration_geometry.md  (S¹/S³/S⁵ at D5/D6/D7)
  - equations/coupling_derivation.py  (g_common from SM running)

Usage:
    python3 equations/beta_constraint.py
"""

import math

PI = math.pi

# ── Constants ─────────────────────────────────────────────────────────────────

I4 = 4.0 / 3.0           # ∫sech⁴(u) du = 4/3  (Bogomolny identity, Cycle 47)
I6 = 16.0 / 15.0         # ∫sech⁶(u) du = 16/15
G_COMMON_SM = 0.5443     # SM equal-coupling at M_c(D5/D6) ≈ 9.44×10¹² GeV
BETA_REF = 0.035         # Reference β (empirical, kink width ~ Planck length)
BETA_ROUTE_F = 3 * G_COMMON_SM**2 / (8 * PI)   # Route F: invert g²=8πβ/3
BETA_1_9PI = 1.0 / (9.0 * PI)                   # New candidate: Hopf dimension
BETA_B2 = 27.0 / (256.0 * PI)                   # B2 self-consistent (Cycle 100)

# Hopf fiber dimensions at D5/D6/D7
DIM_S1 = 1   # S¹ at D5 → U(1)
DIM_S3 = 3   # S³ at D6 → SU(2)
DIM_S5 = 5   # S⁵ at D7 → SU(3)
DIM_HOPF_TOTAL = DIM_S1 + DIM_S3 + DIM_S5   # = 9


# ── Helper: g² and g from β ──────────────────────────────────────────────────

def g_from_beta(beta):
    """g² = 8πβ/3 (compact KK holonomy form, Cycle 85)."""
    g2 = 8.0 * PI * beta / 3.0
    return g2, math.sqrt(g2)


# ── Candidate (a): kink width = Planck length ─────────────────────────────────

def candidate_a():
    """
    Candidate (a): fix β by requiring kink width = Planck length at D1.

    The kink width is the spatial scale over which the field transitions
    between the two stable minima. Setting this width equal to the Planck
    length at the D1 compression depth gives a constraint on the quadratic
    coefficient α, not on the quartic coefficient β.

    The kink width equals the square root of two times the speed of light
    squared divided by the quadratic potential coefficient. Setting this
    equal to the Planck length determines α = 2M_Pl². The quartic coupling
    β remains unconstrained.

    Verdict: BLOCKED — fixes α, not β.
    """
    print("=== Candidate (a): kink width = Planck length ===")
    print("  ξ = √(2c²/α) = L_Pl  →  α = 2c²/L_Pl² = 2M_Pl²")
    print("  This fixes α_D1 = 2M_Pl² (quadratic coefficient at D1)")
    print("  β remains free — the width constraint is α-only")
    print("  Verdict: BLOCKED (fixes α, not β)")
    print()


# ── Candidate (b): S_kink/ℏ = integer ────────────────────────────────────────

def candidate_b(alpha=1.0, c=1.0):
    """
    Candidate (b): quantize the kink action as an integer multiple of ℏ.

    In 1+1D field theory, the kink action (Euclidean instanton action)
    equals the kink energy times a characteristic length. In units where
    the kink mass M_c = 1, the kink energy is 8/(3β). Requiring this to
    equal an integer n times ℏ (= 1 in natural units) gives β = 8/(3n).

    The problem: M_c is α-dependent (M_c = √(α/2)), so the constraint
    involves both α and β. No natural integer n produces β ≈ 0.035 without
    an additional assumption about n.

    For β = 1/(9π) ≈ 0.03537: E_kink/M_c = 8/(3β) = 24π ≈ 75.4.
    The integer nearest 75.4 is 75 or 76 — no obvious topological reason.

    Verdict: BLOCKED — α-dependent via M_c; no natural integer n.
    """
    M_c = math.sqrt(alpha / 2.0)
    print("=== Candidate (b): S_kink/ℏ = integer ===")
    print(f"  In α={alpha}, c={c} units: M_c = √(α/2) = {M_c:.4f}")
    print(f"  E_kink/M_c = 8/(3β):  ")
    for name, b in [("ref", BETA_REF), ("RouteF", BETA_ROUTE_F),
                    ("1/(9π)", BETA_1_9PI), ("B2", BETA_B2)]:
        Ek = 8.0 / (3.0 * b)
        print(f"    β={name:<10}: E_kink/M_c = {Ek:.4f}  "
              f"(nearest integer: {round(Ek)},  fractional part: {Ek % 1:.4f})")
    print("  No candidate gives E_kink/M_c = exact integer")
    print("  Note: ΔV/E_kink = 3√(2α)/16 is α-dependent → same problem")
    print("  Verdict: BLOCKED (requires additional α constraint)")
    print()


# ── Candidate (c): ΔV/E_kink = topological constant ─────────────────────────

def candidate_c():
    """
    Candidate (c): require the ratio of barrier height to kink energy to
    equal a pure topological constant.

    The barrier height equals the difference in potential energy between the
    unstable maximum at φ=0 and the stable minima at φ=±φ₀. This equals
    α²/(4β). The kink energy is (4/3)cα^{3/2}/(β√2). Their ratio is:

        ΔV/E_kink = [α²/(4β)] / [(4/3)α^{3/2}/(β√2)]
                  = 3√(2α) / 16

    This ratio depends on α alone, not on β. It cannot fix β.

    Verdict: BLOCKED — α-dependent; no β-fixing condition.
    """
    print("=== Candidate (c): ΔV/E_kink = topological constant ===")
    print("  ΔV/E_kink = 3√(2α)/16  [derived analytically]")
    print("  This is α-dependent and β-INDEPENDENT:")
    for a_test in [0.1, 0.5, 1.0, 2.0, 4.0]:
        ratio = 3.0 * math.sqrt(2.0 * a_test) / 16.0
        print(f"    α = {a_test:.1f}: ΔV/E_kink = {ratio:.6f}")
    print("  → ratio varies with α; β does not appear")
    print("  Verdict: BLOCKED (cannot fix β independently of α)")
    print()


# ── Candidate (d): β = 1/(dim_Hopf_total × π) ───────────────────────────────

def candidate_d():
    """
    Candidate (d) [NEW, Cycle 101]: β = 1/(dim_Hopf_total × π).

    The DFC substrate produces three gauge groups from Hopf fiber closures:
      - D5 depth: S¹ fiber → U(1),   dimension 1
      - D6 depth: S³ fiber → SU(2),  dimension 3
      - D7 depth: S⁵ fiber → SU(3),  dimension 5
    (See foundations/hopf_fibration_geometry.md, equations/hopf_dof_count.py)

    The total Hopf fiber dimension is the sum: 1 + 3 + 5 = 9.

    The natural normalization of the quartic coupling in the KK reduction
    over all three Hopf fibers involves their total dimensional measure,
    divided by the U(1) integration period π (half the circle circumference).
    This gives:

        β = 1 / (dim_total × π) = 1 / (9π)

    Consequences:
      - g² = 8πβ/3 = 8π/(3×9π) = 8/27 exactly
      - g = √(8/27) = 2√2/(3√3) = 2√6/9
      - 8/27 = (2/3)³  [cube of the ratio of first two Hopf fiber dimensions]
      - Matches SM g_common = 0.5443 to 0.006%

    Status: Tier 3 structural argument. The derivation of β = 1/(9π) from
    the V(φ) substrate dynamics — showing that the KK normalization over the
    three Hopf fibers produces this exact factor — is the remaining open step.
    Once proved, Bottleneck 2 closes: all three steps
    f² = I₄φ₀²/λ → r_U1 = λ/(βI₄) → g² = 2πβI₄ = 8/27
    follow with zero free parameters.

    Returns dict with key results.
    """
    beta = BETA_1_9PI
    g2, g = g_from_beta(beta)
    g2_exact = 8.0 / 27.0

    # Verify β = 1/(9π) ↔ g² = 8/27
    err_g2 = abs(g2 - g2_exact) / g2_exact
    err_g = abs(g - G_COMMON_SM) / G_COMMON_SM

    # Also verify: 8/27 = (2*dim_S1/dim_S3)^dim_S3
    hopf_ratio = (2.0 * DIM_S1 / DIM_S3) ** DIM_S3
    err_hopf = abs(g2_exact - hopf_ratio)

    # r_U1 at β = 1/(9π) [in units of λ]
    r_U1_over_lam = 3.0 / (4.0 * beta)  # = 3/(4β) = 27π/4

    print("=== Candidate (d) NEW: β = 1/(dim_Hopf_total × π) ===")
    print(f"  Hopf fiber dimensions at D5/D6/D7:")
    print(f"    dim(S¹) = {DIM_S1}  [D5 → U(1)]")
    print(f"    dim(S³) = {DIM_S3}  [D6 → SU(2)]")
    print(f"    dim(S⁵) = {DIM_S5}  [D7 → SU(3)]")
    print(f"    dim_total = {DIM_HOPF_TOTAL} = {DIM_S1}+{DIM_S3}+{DIM_S5}")
    print()
    print(f"  β = 1/(9π) = {beta:.6f}")
    print(f"  g² = 8πβ/3 = 8/27 = {g2:.6f}")
    print(f"  Error |g²(formula) − 8/27| / (8/27) = {err_g2:.2e}  ✓")
    print(f"  g = √(8/27) = 2√2/(3√3) = {g:.6f}")
    print(f"  Error vs SM g_common = 0.5443: {err_g*100:.4f}%")
    print()
    print(f"  Also: 8/27 = (2/3)³ = (2·dim(S¹)/dim(S³))^dim(S³)")
    print(f"  Check: (2×1/3)³ = {hopf_ratio:.6f}, diff from 8/27 = {err_hopf:.2e}  ✓")
    print()
    print(f"  r_U1/λ at β=1/(9π): 3/(4β) = 27π/4 = {r_U1_over_lam:.4f}")
    print(f"  (Compare: SM target r_U1/λ ≈ 21.4; 27π/4 ≈ 21.21, diff = {abs(r_U1_over_lam-21.4)/21.4*100:.2f}%)")
    print()
    print(f"  Gap: prove β = 1/(9π) from V(φ) → KK normalization over three Hopf fibers")
    print(f"  Once β fixed: g²=8/27 closes B2 with zero free parameters")
    print()

    return {
        'beta':          beta,
        'g2':            g2,
        'g':             g,
        'g2_exact':      g2_exact,
        'err_g2':        err_g2,
        'err_vs_SM_pct': err_g * 100,
        'r_U1_over_lam': r_U1_over_lam,
        'dim_hopf_total': DIM_HOPF_TOTAL,
    }


# ── β comparison table ────────────────────────────────────────────────────────

def beta_summary():
    """
    Summary table comparing all known β estimates and their predictions.
    """
    print("=== β comparison table ===")
    hdr = f"{'Name':<18} {'β':>10} {'g²':>10} {'g':>9} {'err vs SM g':>13}"
    print(hdr)
    print("-" * len(hdr))
    for name, b in [
        ("empirical ref",  BETA_REF),
        ("Route F",        BETA_ROUTE_F),
        ("B2 (Cycle 100)", BETA_B2),
        ("1/(9π) NEW",     BETA_1_9PI),
        ("SM (exact)",     None),
    ]:
        if b is None:
            g2 = G_COMMON_SM**2
            g = G_COMMON_SM
            print(f"{'SM (exact)':<18} {'—':>10} {g2:>10.6f} {g:>9.5f} {'0.000%':>13}")
            continue
        g2, g = g_from_beta(b)
        err = abs(g - G_COMMON_SM) / G_COMMON_SM * 100
        note = "← 8/27 exact" if abs(b - BETA_1_9PI) < 1e-10 else ""
        print(f"{name:<18} {b:>10.6f} {g2:>10.6f} {g:>9.5f} {f'{err:.4f}%':>13}  {note}")
    print()


# ── Alpha-independence check for g² = 8πβ/3 ─────────────────────────────────

def alpha_independence_check(beta=BETA_1_9PI):
    """
    Verify that g² = 8πβ/3 is α-independent, confirming the derivation
    chain does not require α as input.
    """
    g2_formula = 8.0 * PI * beta / 3.0
    print(f"=== α-independence of g² at β = 1/(9π) ===")
    max_err = 0.0
    for alpha in [0.01, 0.1, 1.0, 10.0, 100.0]:
        phi0 = math.sqrt(alpha / beta)
        lam = math.sqrt(2.0 / alpha)
        f2 = I4 * phi0**2 / lam           # Phase stiffness (Cycle 47, exact)
        r_U1 = phi0**2 / (beta * f2)      # r_U1 = φ₀²/(β f²) = 3λ/(4β)
        g2_chain = 2.0 * PI * lam / r_U1  # KK holonomy
        err = abs(g2_chain - g2_formula) / g2_formula
        max_err = max(max_err, err)
        print(f"  α={alpha:6.2f}: g²(chain)={g2_chain:.8f}, "
              f"g²(formula)={g2_formula:.8f}, err={err:.2e}")
    print(f"  Max error across all α: {max_err:.2e}  ✓  (α cancels identically)")
    print()


# ── Open derivation gap ───────────────────────────────────────────────────────

def open_gap():
    """
    State precisely what remains to be derived to close Bottleneck 2.
    """
    print("=== Open derivation gap (Bottleneck 2) ===")
    print()
    print("  CLOSED (proved exactly, 0 free parameters):")
    print("    P1: f² = I₄ × φ₀²/λ  [Cycle 47, Bogomolny identity ∫sech⁴=4/3]")
    print("    P2: r_U1 = λ/(βI₄) = 3λ/(4β)  [algebraic identity, α-independent]")
    print("    P3: g² = 2πλ/r_U1 = 2πβI₄ = 8πβ/3  [KK holonomy formula]")
    print()
    print("  CANDIDATE (Tier 3):")
    print("    C1: β = 1/(9π) from Hopf fiber dimension sum 1+3+5=9")
    print("        → g² = 8/27 exactly, 0.006% from SM g_common")
    print()
    print("  OPEN (required to close B2 at Tier 2):")
    print("    O1: Derive β = 1/(9π) from V(φ) substrate dynamics.")
    print("        Specific target: show the KK normalization integral over the")
    print("        product fiber S¹×S³×S⁵ (dim = 1×3×5, total 9 DOF) produces")
    print("        β = 1/(total_dim × π) = 1/(9π) from the field equation alone.")
    print("        Once O1 is proved: g² = 8/27, β = 1/(9π), Bottleneck 2 CLOSED.")
    print()
    print(f"  Current tier: g² = 8πβ/3 is Tier 3 (heuristic, 0.37% vs SM).")
    print(f"  If β = 1/(9π) is proved: Tier 2a (0.006% vs SM).")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 68)
    print("β DERIVATION CANDIDATES — DFC SUBSTRATE V(φ) = −α/2 φ² + β/4 φ⁴")
    print("Dimensional Folding Model")
    print("=" * 68)
    print()

    candidate_a()
    candidate_b()
    candidate_c()
    result = candidate_d()
    beta_summary()
    alpha_independence_check()
    open_gap()

    print()
    print("=" * 68)
    print("SUMMARY")
    print("=" * 68)
    print()
    print("  Candidates (a), (b), (c) all BLOCKED:")
    print("    (a) kink width = L_Pl → fixes α, not β")
    print("    (b) S_kink/ℏ = n     → α-dependent; no natural n")
    print("    (c) ΔV/E_kink = const → α-dependent; β-free")
    print()
    print(f"  NEW candidate (d): β = 1/(9π) from Hopf structure")
    print(f"    Hopf fiber dims: {DIM_S1}+{DIM_S3}+{DIM_S5} = {DIM_HOPF_TOTAL}")
    print(f"    β = 1/(9π) = {BETA_1_9PI:.6f}")
    print(f"    g² = 8/27 exactly   (= (2/3)³)")
    print(f"    g vs SM: {result['err_vs_SM_pct']:.4f}% error")
    print(f"    Status: Tier 3 — derive β = 1/(9π) from V(φ) to close B2")
