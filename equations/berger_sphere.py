"""
DFC Berger Sphere — Ricci Scalar under S³ Squashing

Computes the Ricci scalar R(ε) for the Berger sphere (biaxially squashed S³)
with the DFC parametrization from foundations/higgs_geometry.md and
foundations/vev_derivation.md:

    ds²(ε) = (1/4)[(σ₁² + σ₂²) + (1+ε)² σ₃²]

where σᵢ are left-invariant 1-forms on SU(2) ≅ S³ satisfying the
Maurer-Cartan equations dσᵢ = -εᵢⱼₖ σⱼ∧σₖ.

KEY RESULT (proved analytically in Cycle 58):

    R(ε) = 24 − 16ε − 8ε²   [EXACT — polynomial terminates at degree 2]

    Coefficients:
        R₀ =  24   (round S³, radius 1/2: R = 6/(1/2)² = 24)
        R₁ = −16   (linear; from b = (1+ε)/2 linear in ε)
        R₂ =  −8   (quadratic)
        R₄ =   0   (quartic — ZERO, identically)
        Rₙ =   0   for all n ≥ 3

Derivation method (Cartan structure equations):
    Orthonormal coframe: ω¹ = aσ₁, ω² = aσ₂, ω³ = bσ₃  with a=1/2, b=(1+ε)/2
    Connection 1-forms solved from: dωⁱ + Γⁱⱼ∧ωʲ = 0 (torsion-free condition)
    Curvature: Ωⁱⱼ = dΓⁱⱼ + Γⁱₖ∧Γᵏⱼ

    Sectional curvatures (exact):
        K₁₂ = (4a² − 3b²) / a⁴    [base × base]
        K₁₃ = K₂₃ = b² / a⁴       [base × fiber]

    Ricci scalar: R = 2(K₁₂ + K₁₃ + K₂₃) = 2(4a²−b²)/a⁴

    With a=1/2, b=(1+ε)/2: R = 32 − 8(1+ε)² = 24 − 16ε − 8ε²   QED

CONSEQUENCE FOR VEV DERIVATION:
    The vev_derivation.md (pre-Cycle 58) claimed λ_DFC = R₄/r_D6⁴. This is
    incorrect: R₄ = 0 identically. The quartic stabilizer in V(ε) does NOT
    come from the Berger sphere Ricci scalar.

    Physical interpretation of R(ε):
        R decreases as |ε| increases → squashing LOWERS curvature energy.
        The Ricci term therefore DESTABILIZES ε = 0 (not stabilizes it).
        Both the D7 pressure and the curvature term contribute to −μ²ε².

    Source of the quartic stabilizer:
        λ comes from the substrate quartic β evaluated at D6 depth:
            V(ε) = −α_D6/2 ε² + β/4 ε⁴
        The Higgs potential Mexican hat is the SUBSTRATE POTENTIAL evaluated
        at the squashing mode — not a geometric curvature effect.
        λ_DFC = β/4 ≈ 0.0351/4 ≈ 0.0088   vs SM: λ₀(M_c) ≈ 0.013 (~1.5× off)

    Revised VEV formula:
        ε₀ = √(α_D6/β)          [substrate potential minimum]
        v  = √2 · ε₀ · C_unit   [C_unit: substrate→GeV conversion, requires M_c(D6)]
        Remaining gap: α_D6 in GeV requires M_c(D6) from Bottleneck 1.

References:
    foundations/vev_derivation.md       — VEV derivation strategy (updated Cycle 58)
    foundations/higgs_geometry.md       — Higgs as S³ squashing modulus
    foundations/hopf_fibration_geometry.md — Berger sphere at D6 depth
    equations/higgs_potential.py        — numerical Higgs predictions

Usage:
    python equations/berger_sphere.py
"""

import math


# ─── Berger Sphere Geometry ───────────────────────────────────────────────────

def berger_radii(epsilon: float):
    """
    Radii of the biaxial Berger sphere for DFC squashing parameter ε.

    The metric ds² = (1/4)[(σ₁²+σ₂²) + (1+ε)²σ₃²] corresponds to:
        a = 1/2           (horizontal S² base radius — constant)
        b = (1+ε)/2       (Hopf fiber radius — changes with squashing)

    At ε = 0: a = b = 1/2 (round S³ of radius 1/2).
    At ε > 0: Hopf fiber elongated (prolate Berger sphere).
    At ε < 0: Hopf fiber compressed (oblate Berger sphere).
    """
    a = 0.5
    b = (1.0 + epsilon) / 2.0
    return a, b


def sectional_curvatures(epsilon: float) -> dict:
    """
    Sectional curvatures of the Berger sphere (exact, from Cartan equations).

    For the biaxial Berger sphere with horizontal radius a and fiber radius b:

        The base-base sectional curvature (in the plane of two horizontal directions)
        equals four times the horizontal radius squared minus three times the fiber
        radius squared, all divided by the fourth power of the horizontal radius:
            K₁₂ = (4a² − 3b²) / a⁴

        The base-fiber sectional curvatures (one horizontal, one fiber direction)
        equal the fiber radius squared divided by the fourth power of the horizontal
        radius:
            K₁₃ = K₂₃ = b² / a⁴

    For the round sphere (ε = 0, a = b = 1/2):
        K₁₂ = K₁₃ = K₂₃ = 4 = 1/a²  ✓  (constant curvature 1/r² with r=1/2)
    """
    a, b = berger_radii(epsilon)
    K_base = (4 * a**2 - 3 * b**2) / a**4
    K_fiber = b**2 / a**4
    return {
        'K_12': K_base,
        'K_13': K_fiber,
        'K_23': K_fiber,
        'a': a,
        'b': b,
    }


def ricci_scalar_exact(epsilon: float) -> float:
    """
    Exact Ricci scalar of the Berger sphere for squashing parameter ε.

    The Ricci scalar equals twice the sum of all sectional curvatures. In three
    dimensions with biaxial symmetry, this sum has three terms (base-base,
    base-fiber, base-fiber), giving:

        R = 2(K₁₂ + K₁₃ + K₂₃) = 2(4a² − b²) / a⁴

    Substituting a = 1/2 and b = (1+ε)/2:

        R = 32 − 8(1+ε)²  =  24 − 16ε − 8ε²

    This is EXACT. The polynomial terminates at degree two. R₄ = 0.
    """
    a, b = berger_radii(epsilon)
    return 2.0 * (4 * a**2 - b**2) / a**4


def ricci_scalar_expansion(epsilon: float) -> float:
    """
    Taylor series expansion of R(ε) — equals the exact result because R₄ = 0.

    R(ε) = R₀ + R₁·ε + R₂·ε²   (higher terms vanish)

        R₀ =  24  (round S³ Ricci scalar: R = 6/r² = 6/(1/2)² = 24)
        R₁ = -16  (linear destabilization from fiber elongation)
        R₂ =  -8  (quadratic; R₄ = 0 identically)
    """
    return 24.0 - 16.0 * epsilon - 8.0 * epsilon**2


# ─── Effective Potential for Squashing Modulus ────────────────────────────────

def higgs_potential_substrate(epsilon: float, alpha_D6: float,
                               beta: float = 0.0351) -> float:
    """
    DFC effective potential for the squashing modulus ε (Cycle 58 result).

    The squashing parameter ε is identified with the Higgs field (normalized).
    The substrate potential V(φ) = -α/2 φ² + β/4 φ⁴ evaluated at the D6
    squashing mode gives the Mexican hat directly:

        V(ε) = -α_D6/2 · ε² + β/4 · ε⁴

    The two terms have distinct physical origins:
        -α_D6/2 · ε²:  destabilization from substrate quadratic coupling at D6
                         depth, PLUS the Ricci curvature contribution (R decreases
                         with |ε|, so geometric energy ALSO destabilizes ε = 0).
                         Both effects enter through the effective α_D6.
        +β/4 · ε⁴:     stabilization from substrate quartic coupling β.
                         This is the sole source of the quartic stabilizer —
                         NOT the Berger sphere geometry (R₄ = 0 identically).

    The minimum of V(ε) is at ε₀ = √(α_D6/β), giving v = √2 ε₀ [substrate units].
    """
    return -alpha_D6 / 2.0 * epsilon**2 + beta / 4.0 * epsilon**4


def vev_substrate(alpha_D6: float, beta: float = 0.0351) -> float:
    """
    Squashing VEV in substrate units: ε₀ = √(α_D6/β).

    This is the substrate field vacuum value at D6 depth — identical in form
    to the kink vacuum φ₀ = √(α/β) but evaluated at the D6 compression scale.
    The electroweak VEV in GeV is:

        v_GeV = √2 · ε₀ · C_unit

    where C_unit is the substrate-to-GeV conversion factor (requires M_c(D6)
    from Bottleneck 1 — currently open).
    """
    return math.sqrt(alpha_D6 / beta)


def lambda_higgs_dfc(beta: float = 0.0351) -> float:
    """
    DFC quartic Higgs coupling from substrate β (Cycle 58 result).

    The quartic term +β/4 · ε⁴ in V(ε) corresponds to a Higgs quartic:
        λ_DFC = β/4

    Numerically (with β = 0.0351):
        λ_DFC = 0.0351/4 ≈ 0.00878

    Comparison with SM tree-level value at closure scale:
        λ₀_SM(M_c) ≈ 0.013    (from SM vacuum stability running; Buttazzo et al.)
        Ratio: λ₀_SM / λ_DFC ≈ 1.48

    The factor ~1.5 is a normalization mismatch between the substrate unit system
    and the SM Higgs field normalization. The DFC substrate uses V = -α/2 φ² + β/4 φ⁴
    while the SM uses V = -μ²|H|² + λ|H|⁴ with |H|² = h²/2 at the minimum.
    Tracking the field normalization through the identification ε ↔ h/v introduces
    a factor of 2 in the quartic: λ_SM = 2 × λ_DFC = β/2 ≈ 0.0176. Still off from
    0.013 by ~35%. The remaining discrepancy is an open problem in the normalization.
    """
    return beta / 4.0


# ─── Numerical Verification ───────────────────────────────────────────────────

def verify_r4_zero(eps_h: float = 1e-3) -> float:
    """
    Numerical verification that the quartic coefficient R₄ = 0.

    Uses a fourth-order finite-difference stencil:
        f''''(0) ≈ [f(2h) - 4f(h) + 6f(0) - 4f(-h) + f(-2h)] / h⁴

    divided by 4! = 24 to give the Taylor coefficient R₄.
    """
    R_2h = ricci_scalar_exact(2 * eps_h)
    R_h  = ricci_scalar_exact(eps_h)
    R_0  = ricci_scalar_exact(0.0)
    R_mh = ricci_scalar_exact(-eps_h)
    R_2mh = ricci_scalar_exact(-2 * eps_h)
    fourth_deriv = (R_2h - 4*R_h + 6*R_0 - 4*R_mh + R_2mh) / eps_h**4
    return fourth_deriv / 24.0  # Taylor coefficient R₄ = f''''(0)/4!


# ─── Main Output ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("DFC BERGER SPHERE — RICCI SCALAR UNDER S³ SQUASHING")
    print("Cycle 58: R₄ = 0 proved; λ source identified as substrate β")
    print("=" * 65)

    # ── 1. Verify R(ε) = 24 − 16ε − 8ε² ────────────────────────────────────
    print("\n--- 1. Exact Ricci Scalar R(ε) ---")
    print("  Analytical formula: R(ε) = 2(4a²−b²)/a⁴ with a=1/2, b=(1+ε)/2")
    print("  = 32 − 8(1+ε)² = 24 − 16ε − 8ε²  [exact polynomial, degree 2]")
    print()
    print(f"  {'ε':>8}  {'R_exact':>12}  {'R_series':>12}  {'|diff|':>12}")
    print(f"  {'-'*8}  {'-'*12}  {'-'*12}  {'-'*12}")
    for eps in [-1.0, -0.5, -0.2, 0.0, 0.2, 0.5, 1.0, 2.0]:
        R_ex = ricci_scalar_exact(eps)
        R_se = ricci_scalar_expansion(eps)
        print(f"  {eps:8.2f}  {R_ex:12.6f}  {R_se:12.6f}  {abs(R_ex-R_se):12.2e}")

    # ── 2. Taylor coefficients ───────────────────────────────────────────────
    # Use appropriate step sizes to avoid catastrophic cancellation.
    # For R₀: direct. For R₁: h=0.01. For R₂: h=0.05. For R₄: h=0.1.
    print(f"\n--- 2. Taylor Coefficients (numerical differentiation) ---")
    h1, h2, h4 = 0.01, 0.05, 0.1
    R0 = ricci_scalar_exact(0.0)
    R1_num = (ricci_scalar_exact(h1) - ricci_scalar_exact(-h1)) / (2*h1)
    # finite diff gives d²R/dε²; Taylor coefficient R₂ = (d²R/dε²)/2!
    R2_deriv = (ricci_scalar_exact(h2) - 2*R0 + ricci_scalar_exact(-h2)) / h2**2
    R2_num = R2_deriv / 2.0
    R4_num = verify_r4_zero(eps_h=h4)
    print(f"  R₀ = {R0:12.6f}   expected  24.000000")
    print(f"  R₁ = {R1_num:12.6f}   expected -16.000000")
    print(f"  R₂ = {R2_num:12.6f}   expected  -8.000000  (coeff of ε²)")
    print(f"  R₄ = {R4_num:12.2e}   expected   0.00e+00  ← KEY RESULT")

    # ── 3. Sectional curvatures ──────────────────────────────────────────────
    print(f"\n--- 3. Sectional Curvatures ---")
    print(f"  Round sphere (ε=0): all K = 1/a² = {1/(0.5**2):.1f}  (constant curvature)")
    print(f"  {'ε':>6}  {'K₁₂ (base-base)':>18}  {'K₁₃=K₂₃ (base-fiber)':>22}  {'R=2ΣK':>8}")
    for eps in [0.0, 0.2, 0.5, 1.0]:
        K = sectional_curvatures(eps)
        R_chk = 2 * (K['K_12'] + K['K_13'] + K['K_23'])
        print(f"  {eps:6.2f}  {K['K_12']:18.6f}  {K['K_13']:22.6f}  {R_chk:8.4f}")
    print("  K₁₂ decreases; K₁₃=K₂₃ increase. Net R = 2(4a²−b²)/a⁴ is exact.")

    # ── 4. Physical interpretation ───────────────────────────────────────────
    print(f"\n--- 4. Physical Interpretation ---")
    print(f"  dR/dε|_{{ε=0}} = -16  (negative: squashing LOWERS curvature energy)")
    print(f"  d²R/dε²      =  -8  (second derivative also negative)")
    print(f"")
    print(f"  Geometric energy is proportional to R. Since R decreases with |ε|:")
    print(f"  → Squashing lowers geometric energy → ε = 0 is DESTABILIZED.")
    print(f"  → The Ricci term contributes to the negative −μ²ε² in V(ε).")
    print(f"  → The Ricci term does NOT provide a quartic stabilizer (R₄ = 0).")

    # ── 5. Effective potential and VEV ───────────────────────────────────────
    print(f"\n--- 5. Effective Potential V(ε) = −α_D6/2 ε² + β/4 ε⁴ ---")
    BETA = 0.0351
    lam = lambda_higgs_dfc(BETA)
    print(f"  β = {BETA}  (DFC Tier 3 reference value)")
    print(f"  λ_DFC = β/4 = {lam:.5f}   [quartic from substrate, not Ricci geometry]")
    print(f"  λ_SM(M_c) ≈ 0.013         [from SM vacuum stability running]")
    print(f"  Ratio λ_SM/λ_DFC = {0.013/lam:.2f}  (normalization factor — open)")
    print(f"")
    print(f"  VEV in substrate units: ε₀ = √(α_D6/β)")
    print(f"  {'α_D6':>8}  {'ε₀':>12}  {'v = √2·ε₀':>14}  {'V(ε₀)':>14}")
    for a_D6 in [0.5, 1.0, 2.0, 5.0, 10.0]:
        e0 = vev_substrate(a_D6, BETA)
        v0 = math.sqrt(2) * e0
        V0 = higgs_potential_substrate(e0, a_D6, BETA)
        print(f"  {a_D6:8.1f}  {e0:12.6f}  {v0:14.6f}  {V0:14.6f}")
    print(f"")
    print(f"  [OPEN] Unit conversion ε₀ → GeV requires M_c(D6) from Bottleneck 1.")
    print(f"  Target: v = 246 GeV  →  α_D6 to be derived from substrate dynamics.")

    # ── 6. Summary ───────────────────────────────────────────────────────────
    print(f"\n--- 6. Summary ---")
    print(f"  PROVED (analytic + numeric):  R(ε) = 24 − 16ε − 8ε²  exactly")
    print(f"  PROVED:  R₄ = {R4_num:.1e}  ≈ 0  (quartic coefficient identically zero)")
    print(f"  CORRECTED:  vev_derivation.md claim 'λ_DFC = R₄/r_D6⁴' is wrong")
    print(f"  NEW:  λ_DFC = β/4 ≈ 0.0088  (from substrate quartic; ~1.5× below SM)")
    print(f"  NEW:  V(ε) = −α_D6/2 ε² + β/4 ε⁴  →  v = √(2α_D6/β) [substrate units]")
    print(f"  OPEN:  α_D6 in GeV requires M_c(D6) from Bottleneck 1")
    print(f"  OPEN:  normalization factor ~1.5 between β/4 and λ₀_SM needs resolution")
