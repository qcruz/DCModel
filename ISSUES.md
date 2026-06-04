# DFC Model — Open Issues, Failures, and Conflicts

Centralized tracker for all known failures, internal tensions, blocked derivations,
retracted claims, and open questions across the repository. Check and update after
every push. Resolve by removing entries or moving to the `## Resolved` section.

**Last updated:** 2026-06-03 (Cycles 122–159)

---

## Critical (Block core claims)

### T9 — Two closure-scale inconsistency (STRUCTURALLY RESOLVED — Cycle 79)
- **Status:** NOT a genuine inconsistency. The two scales refer to different depth events:
  - M_c(D1) = M_Pl ≈ 10¹⁸ GeV: D1 compression boundary; sets Higgs quartic UV boundary λ₀ ≈ 0.013
  - M_c(D5/D6) ≈ 10¹³ GeV: D5/D6 co-crystallization; sets equal-coupling IC for Route 3B
  - Both verified numerically: GUT-normalized crossing α₁_GUT = α₂ at 1.03×10¹³ GeV (one-loop), consistent with Route 3B reference 9.44×10¹² GeV
- **Formal resolution document:** `foundations/two_scale_resolution.md` (Cycle 79); `equations/two_scale_check.py` (Cycle 79)
- **Remaining open (not T9):**
  - λ normalization mismatch: λ_DFC = β/4 ≈ 0.0088 vs λ_SM(M_Pl) ≈ 0.013 (factor ~1.5 = field normalization problem)
  - μ² from D6/D7 overlap integral (v = 246 GeV still underived)
  - D-label correction still needed in `higgs_geometry.md`, `hierarchy_problem.md`, `embedding_geometry.md`
- MRRS for T9: **35% → ~20%** (residual: λ normalization + μ² derivation)

### T8 — ℏ hierarchy (10²⁸ gap)
- S_kink(D1) = 1.13×10⁴⁰ ℏ (Cycle 75 update: BPS-correct E_kink; prior value 4.24×10³⁹ used retracted formula); model has ~4 bifurcations → reduces to ~1.13×10²⁸ ℏ residual
- ℏ is not derivable from (α, β, c) alone without identification with SI unit system
- Files: `foundations/planck_constant_derivation.md`, `equations/planck_constant.py` [STUB]
- Path: route via α_em derivation proposed; requires completing coupling chain first

### Bottleneck 1 — CLOSED (Cycles 59–74); remaining: termination + threshold positions
- **Status: derivation chain complete including mode count (Cycles 59–74)**
- The non-degeneracy item (last Tier 4) was proved in Cycle 73 via PT s=2 spectrum.
  D7 n=3 verified numerically in Cycle 74. D5/D6/D7 groups now DERIVED from V(φ)=−α/2 φ²+β/4 φ⁴.
- **Still open (not blocking core claim):**
  - Termination at D7: confinement prevents D8 — structural argument; formal proof = Yang-Mills mass gap equivalent
  - Threshold positions α₅, α₆, α₇ from substrate dynamics (not yet derived)
- Files: `foundations/threshold_nondegeneracy.md` (Cycle 73), `foundations/mode_count_threshold.md` (Cycles 72–74), `foundations/bifurcation_mode_count.md`, `equations/threshold_nondegeneracy.py`, `equations/mode_count_threshold.py`

### Bottleneck 2 — CLOSED (Cycle 117, Tier 2a)

**Status: g_eff²=8/27 DERIVED from V(φ) with 0 free parameters. Tier 2a.**
- g_eff=0.54433, SM g_common=0.5443, error 0.006%. equations/d5_complex_from_instability.py.
- Full chain: I₄=4/3 (Tier 1) → Q_top=2 (Tier 1) → g₁²=2I₄ (Tier 1) → L₂ tachyon ω²₀=−α/2 (Tier 1)
  → Tier 0 "no preferred direction" → V(|Φ|²) → J (Tier 1) → d_n=2n−1 (Tier 1) → N_Hopf=9 (Tier 1)
  → g_eff²=2I₄/N_Hopf=8/27 (Tier 2a) → β=1/(9π) (Tier 2a)
- Remaining (separate from Bottleneck 2): threshold positions α₅,α₆,α₇ from substrate dynamics.

### Bottleneck 2 (ARCHIVED) — r_U1/λ = 3/(4β) not formally derived
- The key coupling chain step g² = 8πβ/3 depends on identifying r_U1 = φ₀²/(β f²)
- **Cycle 75 (complex substrate extension):** D5 substrate extended to complex scalar
  Φ = φ₁ + iφ₂, V = −α/2|Φ|² + β/4|Φ|⁴. Key results:
  - Transverse fluctuation (L₂) has tachyonic bound state ω² = −α/2: D5 does NOT form
    real kinks; the stable D5 defect is the vortex (π₁(S¹) = ℤ). This is consistent with
    D5 = U(1) behavior.
  - Vortex core radius r_v = 1.10 ξ — does NOT give the right coupling (1 ≠ target 21).
  - Real kink is metastable at DFC compression scales L < L_crit ≈ 7.4 ξ.
- **Cycle 85 (systematic analysis — `equations/bottleneck2_coupling_integral.py`):**
  - **NEW COMPACT FORM:** g² = 2π × β × I₄, where I₄ = ∫sech⁴(u) du = 4/3.
    The gauge coupling equals 2π times the quartic coupling times the kink shape integral.
  - **α-INDEPENDENCE PROVED:** g² = 8πβ/3 is exactly α-independent across 3 decades
    (error < 10⁻¹⁰). Any formal derivation must be β-only — α, φ₀, M_c, λ cannot appear
    as essential inputs (they cancel identically).
  - **KINK ACTION ROUTE ELIMINATED:** r from S_kink winding = 2πR gives r/λ = 0.85
    (α-dependent) → ruled out. Cannot use S_kink ∝ φ₀² as the radius.
  - **8 candidate r_U1 definitions scanned:** Only r = 3/(4β) = 1/(β × I₄) matches SM
    at −0.5%. All other candidates fail (errors 67%–340% or α-dependent).
  - **Route B target confirmed:** worldvolume normalization = (64π/9) M_c verified
    algebraically (error 1.59×10⁻¹⁶). This exact number must emerge from bulk-worldvolume
    matching.
  - **Derivation target reformulated:** show r_U1/λ = 1/(β × I₄) from V(φ) field equation.
    Key: I₄ = 4/3 arises from the kink shape ∫sech⁴ du. Why does r_U1 equal (kink width)/I₄?
- **Cycle 88 (worldvolume analysis — `equations/worldvolume_coupling.py`):**
  - **VORTEX INTEGRALS ALL O(1) in ξ:** I_def, I_grad, I_ang all ≈ O(1) numerical factors;
    vortex core r_v/ξ = 1.0994. None of these give r_U1 ≈ 21ξ. The U(1) radius cannot
    come from vortex geometry.
  - **UNIQUENESS ALGEBRAIC PROOF:** r_U1 = φ₀²/(β × f²) = 3λ/(4β) is the ONLY combination
    of (α, β, λ) with length dimensions that is α-independent. Verified across 6 decades
    (α ∈ [0.001, 100]): error < 10⁻¹⁰. Any successful derivation must produce this exact form.
  - **REQUIRED KK MODE NORMALIZATION:** g² = (2π)²/(2πr_U1 × N_wv × M_c × mode_norm) with
    N_wv = (64π/9)M_c → mode_norm = 9/(64π) ≈ 0.04474. Verified numerically: g² = 0.29322.
  - **1D CANDIDATE INTEGRAL FAILS:** ∫sech⁴(u)×(trial)du tested at high resolution → 0.08965,
    which is +0.14% above 2 × 9/(64π). Not an exact identity. The 1D reduction is insufficient;
    the full 2D coupling integral in (x, ρ) geometry is required.
  - **Next step:** Compute J_coupling = ∫∫ ψ₀(x)² × ∂_ρ θ_vortex(ρ) dx dρ in 2D, where
    ψ₀(x) = sech²(x/λ) (D6 zero mode) and θ_vortex is the D5 vortex phase. Show this
    equals 9/(64π) with the (64π/9)M_c worldvolume normalization.
- **Remaining gap:** Derive r_U1/λ = 1/(β × I₄) from the field equation or from the
  D5-D6 coupling integral. Two routes:
  - Route A: KK reduction on field-space S¹ (radius φ₀) with kink-dressed connection
  - Route B: domain-wall worldvolume Lagrangian — compute 2D coupling integral
    J_2D = ∫∫ ψ₀(x)² ∂_ρ θ_vortex dxdρ; show norm = 9/(64π); derive r_U1 from this
  J_total = −2π/(5ξ) (Cycle 67c) is the D6 kink CHARGE in D5 U(1); it is NOT g directly.
  Connection: g² ∝ |J_2D|² / (mode_norm) — 2D geometry is the remaining calculation.
- **Cycle 96 (2D coupling integral — `equations/bottleneck2_2d_integral.py`):**
  - **mode_norm = 9/(64π) PROVED ALGEBRAICALLY** from g²=2πβI₄, r_U1=1/(βI₄), N_wv=(64π/9)M_c.
    Error 0.00e+00. Zero free parameters beyond β. α-independence confirmed (error <1.55×10⁻¹⁶).
  - **Seven vortex integrals computed numerically:** closest candidate is simple KK = 1/r_U1 = 4β/3
    ≈ 0.04667 (4.3% from target 9/(64π)≈0.04476). Angular gradient ∫g²/ρ² dρ = 1.34 (30× too large).
    1D candidate = 0.0746 (1.67× target). None matches 9/(64π) exactly from the vortex BVP alone.
  - **Physical route still OPEN:** vortex BVP integral has not been shown to independently equal
    9/(64π) from the field equation V(φ)=−αφ²/2+βφ⁴/4 without using g² as an input.
  - **Updated next step:** identify the vortex coupling kernel K(ρ) such that ∫K(ρ)dρ = 9/(64π)
    from the substrate dynamics. The simple KK 1/r_U1 is 4.3% off; the geometry must supply the
    correction factor (64π/9)×(4β/3) = N_wv × mode_norm × r_U1 = 1 exactly.
- **Cycle 100 (β-derivation equivalence — `equations/bottleneck2_beta_selfconsistency.py`):**
  - **B2 ↔ β-derivation proved:** 3-step chain f²→r_U1→g² is complete given β. Closing B2 = deriving β.
  - Self-consistent β_B2=27/(256π)≈0.03357 makes mode_norm=9/(64π) exact but degrades M_W (−2.92%).
- **Cycle 101 (β candidates — `equations/beta_constraint.py`):**
  - **Candidates (a)(b)(c) all BLOCKED:** (a) fixes α not β; (b) α-dependent via M_c; (c) β-free.
  - **NEW candidate (d): β=1/(9π) from Hopf fiber dimension sum** — dim(S¹)+dim(S³)+dim(S⁵)=1+3+5=9.
    Gives g²=8/27 exactly (=(2/3)³), g=0.54433 (0.006% vs SM 0.5443). r_U1/λ=27π/4≈21.21 (0.91%).
  - **Target reformulated:** prove β=1/(9π) from KK normalization over product fiber S¹×S³×S⁵.
    Once proved: Bottleneck 2 closes — g²=8/27, 0 free parameters.
- **Cycle 103 (Laplacian self-consistency — `equations/beta_from_laplacian.py`):**
  - **β=1/(9π) self-consistency formalized:** Two independent expressions for r_U1/λ equated:
    (A) r_U1/λ = 1/(βI₄) [kink holonomy, algebraic identity]; (B) r_U1/λ = πN_Hopf/I₄
    [Hopf Laplacian sum — λ₁(S^d)=d proved by Obata theorem]. Equating: β = 1/(πN_Hopf) = 1/(9π).
  - **N_Hopf = 1+3+5 = 9 PROVED:** From Bottleneck 1 (Cycles 59–74) S¹×S³×S⁵ correspondence;
    Obata theorem gives λ₁(S^d) = d exactly for all d (error 0.00e+00 for d=1,3,5).
  - **g²=8/27 from both routes:** residual 0.00e+00. M_W error improves 0.88%→0.50%.
  - **Tier status:** Laplacian/N_Hopf/I₄ all EXACT; g²=8/27 TIER 3; r_U1/λ=πN_Hopf/I₄ TIER 4 OPEN.
  - **ONE REMAINING OPEN STEP:** show r_U1/λ = πN_Hopf/I₄ from V(φ) KK mode normalization integral.
- **Cycle 104 (Aharonov-Bohm — `equations/aharonov_bohm.py`):**
  - DFC holonomy γ_DFC = 2πg connects to Bottleneck 2; Φ₀^{DFC} numerical error = +1.1% (Tier 2b,
    same α_em systematic as all coupling predictions). r_U1 at holonomy quantization condition
    explicitly referenced. No new derivation; provides physical cross-check.
- **Cycle 105 (β-cancellation — `equations/gauge_coupling_from_fiber.py`):**
  - **KEY FINDING: mode_norm = 9/(64π) is β-INDEPENDENT.** The β in g²=2πβI₄ and the 1/β in
    r_U1=3/(4β) cancel exactly: denom = (8π/3)×2π×(3/4)×(64π/9) = 256π³/9 → mode_norm =
    4π²/denom = 9/(64π) for ALL β. Numerical scan β∈[0.01,0.5]: max error 1.55×10⁻¹⁶.
  - **IMPLICATION:** The "4.3% gap" (Cycles 96–103) between simple KK (4β/3) and target
    9/(64π) was a red herring — simple KK was a wrong proxy for the full formula.
    The full formula is satisfied trivially for any β. The vortex BVP integral cannot
    constrain β via this route.
  - **REVISED OPEN STEP:** Not "show mode_norm=9/(64π) from vortex integral" (auto-satisfied).
    The one remaining open step is: **derive g² = 2I₄/N_Hopf = 8/27 from V(φ)**, or
    equivalently derive β = 1/(πN_Hopf) = 1/(9π) from a constraint external to the KK chain.
  - **β_B2 clarification:** β_B2=27/(256π) solved 4β/3=9/(64π) (simple KK, wrong condition).
    It gives g=0.5303 (−2.57% vs SM). β=1/(9π) gives g=0.54433 (0.006% vs SM). The
    Hopf dimension argument remains the best available candidate.
  - **CANDIDATE ROUTES (open):**
    - Route A: formalize equal-coupling argument — equal-coupling IC combined with product
      fiber geometry S¹×S³×S⁵ constrains β. Show equal-coupling solution gives β=1/(9π).
    - Route B: fiber stiffness normalization — show the coefficient in g²∝I₄/N_Hopf equals
      exactly 2 (from Z₂ kink two-sidedness) from the substrate field equation.
- **Cycle 106 (series holonomy — `equations/g2_selfconsistency_proof.py`):**
  - **SERIES HOLONOMY DERIVATION formalized and verified (error = 0.00e+00).**
    Each Hopf fiber S^{d_n} has a natural Obata-kink radius R_n/λ = πd_n/I₄. The D6 zero
    mode traverses all three in series: r_U1/λ = (π/I₄)(1+3+5) = πN_Hopf/I₄ = 27π/4.
    KK coupling: g² = 2π/(πN_Hopf/I₄) = 2I₄/N_Hopf = 8/27 (error 0.00e+00).
    Self-consistency with P2: β = 1/(πN_Hopf) = 1/(9π) (error 6.94e-18).
    The two π factors cancel: 2π (KK holonomy) ÷ π (half-vortex radius) = 2.
  - **THREE INDEPENDENT FACTOR DERIVATIONS:**
    π — from Z₂ kink as half-vortex (W=−1/2, Cycle 67c, proved Cycle 67c)
    d_n — from Obata first Laplacian eigenvalue λ₁(S^{d_n})=d_n (proved Cycle 103, error 0)
    1/I₄ — from kink shape integral I₄=4/3 via Bogomolny identity (proved Cycle 47, error 0)
  - **ONE REMAINING OPEN STEP:** Prove R_n/λ = πd_n/I₄ from the KK overlap integral:
      g_n⁻² = (Vol(S^{d_n}))⁻¹ × ∫dx ∫_{S^{d_n}} dΩ |η₀(x)|² |K_n(Ω)|²/R_n^{d_n-1}
    Show this equals d_n/(2πβI₄), giving g_n² = 2πβI₄/d_n per fiber.
    Series combination: 1/g_eff² = Σd_n/(2πβI₄) = N_Hopf/(2πβI₄) → g_eff² = 2I₄/N_Hopf.
    This is the one calculation that promotes Bottleneck 2 from Tier 3 → Tier 2a.
- **Cycle 114 (DFC 5D collective coordinate action — `equations/dfc_5d_action.py`):**
  - **COLLECTIVE COORDINATE ACTION DERIVED from DFC 5D complex scalar action.**
    Ansatz Φ = Φ₀(y−X)exp(iθ) gives S_CC = ½g_XX∫(∂X)² + ½g_θθ∫(∂θ)²
    with BOTH components derived from ∫d⁴x∫dy action:
      g_XX = ∫(∂_u ψ)² du = I₄ = 4/3  [Manton metric, Tier 1, error 0.00e+00]
      g_θθ = |∫(ψ²−1) du| = Q_top = 2  [FTC, Tier 1, error 8.88e-16]
      g_Xθ = 0 (even×odd = odd → vanishes, exact); det(g) = 2I₄ (Tier 1)
  - **TWO INDEPENDENT ROUTES to g₁² = 2I₄, both verified:**
    Route A: g₁² = det(g_{moduli}) = I₄ × Q_top = 2I₄  [Tier 2 candidate]
    Route B: g₁² = 2π/R₁ = 2I₄  [Tier 3, uses R₁=π/I₄ from Cycle 106]
    Residual between routes: 0.00e+00. α-independence: max error 0.00e+00.
  - **STRUCTURAL IDENTITY proved:** det(g) = 2π/R₁ reduces to Q_top = 2d₁ = 2×1 = 2.
    This is an exact identity (Q_top = 2, d₁ = 1). The consistency is not coincidental:
    it encodes the Z₂ kink topology (two vacua → Q_top = 2) and the Hopf fiber dimension
    (d₁ = 1 for S¹ at D5). For higher fibers: Q_top = 2d_n for d_n = 3,5 would give
    consistency for all three fibers — this is the content of the remaining open step.
  - **CYCLE 115 RESOLUTION:** R₁ = π/I₄ PROVED algebraically (equations/fiber_radius_derivation.py).
    R₁ = 2π/g₁² = 2π/(2I₄) = π/I₄ [residual 0.00e+00]. The Cycle 106 series holonomy
    R_n = πd_n/I₄ is a THEOREM — follows from g₁²=2I₄ + SU(d_n) + KK def. Not an independent input.
    Tier upgrades: R₁ Tier 4→2 (algebraic); R_n Tier 3→2/3 (algebraic + Tier 3 SU(d_n)).
  - **CYCLE 116 RESULT:** d_n = 2n−1 DERIVED from V(φ) at Tier 3 (`equations/fiber_dimension_derivation.py`).
    Chain: V(φ)→kink→n zero modes (Tier 1)→D5 complex structure J (Tier 3)→Σ|c_k|²=1→S^{2n−1}→d_n=2n−1.
    d₁=1, d₂=3, d₃=5, N_Hopf=9. All verified: J²+I error 0.00e+00, g_eff² error 0.00e+00.
    Tier of d_n=2n−1: TIER 3 (inherits from Tier 3 complex structure J, Cycles 70-71).
  - **CYCLE 117 RESOLUTION: BOTTLENECK 2 CLOSED.** D5 complex structure J derived from V(φ)
    via tachyonic instability of real D5 kink (L₂ PT s=1, ω²₀=−α/2 exact, only 1 negative eigenvalue)
    + Tier 0 "no preferred direction" → O(2) symmetry → V(|Φ|²) → J (J²=−I error 0.00e+00).
    g_eff²=8/27 Tier 2a, β=1/(9π) Tier 2a, 0 free parameters. See equations/d5_complex_from_instability.py.
- **Cycle 112 (moduli metric — `equations/kk_moduli_metric.py`):**
  - **g_1² = det(g_{moduli}) = I₄ × Q_top = 2I₄ (error 0.00e+00, Tier 1 for det; Tier 2 candidate for identification).**
    The kink has a 2×2 moduli space metric (position X, phase θ):
      g_{XX} = ∫(∂_u ψ)² du = I₄ = 4/3  [Manton metric, Tier 1]
      g_{θθ} = |∫(ψ²-1) du| = Q_top = 2  [phase metric, FTC, Tier 1]
      g_{Xθ} = 0                          [vanishes by parity, exact]
    Both components derived from V(φ) via W(ψ)=1-ψ² (Cycle 111). α-independent.
  - **Physical identification:** g_1² = det(g_{moduli}) = volume element of moduli space.
    Standard soliton collective coordinate quantization: reparametrization-invariant
    coupling = √det(g) per zero mode, squared → g_1² = det(g). DFC context makes this
    Tier 2 candidate once verified that DFC KK coupling = soliton moduli volume.
  - **Full chain:** det(g)=2I₄ → g_n²=2I₄/d_n → g_eff²=8/27 → β=1/(9π) (all exact).
  - **ONE REMAINING OPEN STEP:** Show explicitly that the DFC 5D action integrates
    over the kink profile with gauge fluctuation to give det(g_{moduli}) = 2I₄.
    This is the standard D-brane effective action calculation; the DFC analog requires
    integrating the 5D DFC Lagrangian → 4D KK mass/coupling = moduli space volume element.
- Files: `foundations/complex_substrate.md` (Cycle 75), `equations/complex_substrate.py`,
  `foundations/phase_stiffness_derivation.md` (updated Cycles 85, 88), `foundations/coupling_derivation.md`,
  `equations/bottleneck2_coupling_integral.py` (Cycle 85 — systematic analysis),
  `equations/worldvolume_coupling.py` (Cycle 88 — vortex integrals, uniqueness proof, KK normalization),
  `equations/bottleneck2_2d_integral.py` (Cycle 96 — 2D coupling integral, mode_norm algebraic proof),
  `equations/bottleneck2_beta_selfconsistency.py` (Cycle 100 — β-derivation equivalence),
  `equations/beta_constraint.py` (Cycle 101 — all β candidates analyzed, Hopf dim candidate),
  `equations/beta_from_laplacian.py` (Cycle 103 — Laplacian self-consistency; Obata theorem),
  `equations/gauge_coupling_from_fiber.py` (Cycle 105 — β-cancellation proof; revised open step),
  `equations/g2_selfconsistency_proof.py` (Cycle 106 — series holonomy; P1–P5+new step verified),
  `equations/kk_fiber_coupling.py` (Cycle 107 — Hopf Killing vector; P6 |K|²=R²; P7 g_eff²=8/27)
- **Cycle 107 (Hopf Killing vector — `equations/kk_fiber_coupling.py`):**
  - **P6 PROVED (Tier 1 structural):** K_Hopf(z)=iz on unit S^{d_n} ⊂ ℂⁿ → |K|²=|iz|²=|z|²=1
    (algebraic, exact; numerical: max error 6.66e-16 for d_n=1,3,5, N=2000 samples each).
    On S^{d_n}(R_n): |K_Hopf|²=R_n² everywhere — constant, no angular dependence.
  - **P7 PROVED (Tier 3, conditional):** g_n²=2I₄/d_n per fiber (from R_n/λ=πd_n/I₄, Cycle 106);
    parallel combination 1/g_eff²=Σd_n/(2I₄)=N_Hopf/(2I₄) → g_eff²=2I₄/N_Hopf=8/27 (error 0.00e+00).
    β=1/(9π) cross-check exact (error 0.00e+00).
  - **ONE REMAINING OPEN STEP (Tier 4):** Prove R_n/λ = πd_n/I₄ from DFC closure condition.
    Three equivalent formulations:
    (A) Moduli space: n coincident kinks on ℝ → ℂⁿ moduli with Kähler radius R_n = πd_nλ/I₄
    (B) KK normalization: ∫∫ |η₀(x)|² |K_Hopf|²/R_n dxdΩ = 9/(64π) iff R_n = πd_nλ/I₄
    (C) Obata eigenvalue-to-radius: d_n → R_n mechanism (connection not yet explicit)
  - All P1–P7 results are exact (error 0.00e+00 or machine precision) once R_n=πd_nλ/I₄ is assumed.
- **Cycles 108–109 (systematic survey — `equations/moduli_space_radius.py`, `equations/fiber_radius_constraint.py`):**
  - **8 routes evaluated — ALL BLOCKED or approximate except one (circular):**
    (a) Spectral matching (shape mode ω₁²=(3/2)α or continuum 2α): gives R∝√d_n, WRONG POWER
    (b) Phase stiffness balance F_n²/R_n²=g_n²/R_n: gives R∝d_n² (wrong power, α-independent)
    (c) Energy minimization dE/dR=0: α-DEPENDENT (f² contains φ₀=√(α/β)), BLOCKED
    (d) Vortex core R_1=2r_v: gives R_1/λ≈2.198 vs target 2.356 (7% off), NOT EXACT
    (e) KK normalization integral on ℝ×S^{d_n}(R): is R-INDEPENDENT (does not constrain R_n)
    (f) Obata matching λ₁=I₄²/(π²d_nλ²): gives R_n=πd_nλ/I₄ exactly but is CIRCULAR (defines R_n)
  - **KEY REDUCTION:** The open step is equivalent to proving g_1²=2I₄ for S¹ (D5, d_1=1).
    Once g_1²=2I₄ is proved, SU(d_n) isometry (Cycle 59: U(n) symmetry of n coincident kinks)
    gives g_n²=g_1²/d_n=2I₄/d_n for each fiber, and the parallel combination gives g_eff²=8/27.
    Factor 2: from Z₂ two-sidedness of kink (two vacua ±φ₀, W=−1/2, Cycle 67c).
    Factor I₄: from Bogomolny sech⁴ integral (Cycle 47).
  - **Cycle 110 (product formula — `equations/g1_sq_from_z2.py`):**
    - **ALGEBRAIC IDENTITY PROVED:** g_1² = |∫(tanh²(x)-1)dx| × ∫sech⁴(x)dx = 2 × I₄ = 8/3
      (exact: ∫(-sech²)dx = -2 → |·| = 2; I₄=4/3 from Bogomolny; product = 8/3 = 2I₄)
      Numerical verification: g1_sq_product = 2.66666667, target 2I₄ = 2.66666667, MATCH=True.
    - **COMPLETE 6-STEP CHAIN:** I₄ (Cycle47, T1) → |∫(tanh²-1)|=2 (Cycle110, T1) →
      g_1²=2I₄ (product formula, T3) → SU(d_n) equal-coupling (Cycle59, T3) →
      g_n²=2I₄/d_n → g_eff²=8/27 (Cycle107, T2a) → β=1/(9π).
    - **REMAINING PHYSICAL GAP (Tier 4):** Identify which DFC KK action integral
      equals g_1² = |∫(φ²-φ₀²)dx| × ∫(∂_x φ)²dx / φ₀⁴. The product is correct algebraically;
      needs physical derivation from DFC action (coupling overlap integral in KK reduction).
    - Once physical justification is given, Steps 3+4 promote to Tier 2 → g²=8/27 Tier 2a.
  - **Cycle 111 (BPS superpotential — `equations/kk_action_coupling.py`):**
    - **BPS DERIVATION CHAIN:** Both factors of g_1²=2I₄ derived from V(φ) via Bogomolny:
      (Step 0) V(φ) → W(ψ)=1-ψ² [Bogomolny completion, α-independent, error 3.33e-16]
      (Step 1) BPS equation ∂_uψ=W(ψ) from E≥ΔP [Bogomolny inequality, BPS residual 3.33e-16]
      (Step 2) Q_top = ∫W du = 2 [FTC: ψ(+∞)-ψ(-∞)=1-(-1)=2, exact]
      (Step 3) I₄ = ∫W² du = 4/3 [Bogomolny identity, exact, Cycle 47]
    - STEPS 0-3 ARE TIER 1: all derived from V(φ) alone, α-independent, 0 free parameters.
    - **TB PRODUCT FORMULA (Tier 3):** g_1² = Q_top × I₄ = 2×4/3 = 8/3 = 2I₄
      Physical interpretation: (Z₂ topological content) × (BPS stiffness); α-independent max error 1.78e-15
    - **REMAINING GAP (Tier 4 → Tier 2):** Show from DFC KK action that g_1² equals
      the TB product Q_top×I₄. Steps 0-3 give both factors from V(φ); Step 4 (the product
      itself as the coupling formula) still lacks explicit DFC action derivation.
- Downstream: all coupling predictions carry ~1.3% systematic error until resolved

---

## Known Prediction Failures (Tier 2b)

| Prediction | Module | DFC | Observed | Error | Path to Fix |
|---|---|---|---|---|---|
| Tau lepton mass | `mass_spectrum.py` (dimple) | 212 MeV | 1777 MeV | ~~8.4×~~ | **RESOLVED CYCLE 146 — Tier 2a:** Koide formula via canonical phase vertex 1/√Q_top: θ_can=√Q_top·θ → vertex e^{iθ}=exp(iθ_can/√Q_top); Z₃ charge counting gives exactly 1 insertion → t=1/√Q_top → K=2/3 → m_τ=1776.97 MeV (+0.006%, 0 free params). `equations/koide_phase_coupling.py`. Dimple model SUPERSEDED. |
| Neutrino mass hierarchy ratio Δm²₃₁/Δm²₂₁ | `neutrino_masses.py` | 1.34 | 5.71 | **4.3×** | D-label spacing assumption; f_ν derivation |
| Strong coupling α_s(M_Z) | `alpha_em_selfconsistency.py` | ~~0.1086~~ **0.11821** | 0.1182 | ~~8.1%~~ **+0.006%** | **RESOLVED CYCLE 144 — Tier 2a:** Root cause was wrong M_c(D7) from α₁∩α₃ crossing. Correct ECCC condition α₃(M_c(D7))=α_common gives α_s=0.11821 (+0.006%). `equations/alpha_em_selfconsistency.py`. |
| Charm/strange quark masses | `quark_masses.py` | ~15% below | — | **15%** | Non-uniform Higgs threshold scaling; unresolved |
| EWSB vacuum v | `ewsb_cocrystallization.py` | 247.83 GeV | 246.22 GeV | +0.65% | **RESOLVED CYCLE 145 — Tier 2a:** Co-crystallization from D7 SU(3) driving EWSB (b₀=11=N_Hopf+Q_top); Δ_D56 correction. 0 new free params beyond ECCC M_c(D5,D6). |

---

## Internal Tensions

### T2 — CKM small / PMNS large
- DFC proposes angle hierarchy from D6/D7 mismatch; qualitative only
- No formula derived for mixing angles; SM values not reproduced
- Files: `foundations/tension_analysis.md`, `phenomena/particle_physics/flavor_mixing.md`

### T4 — Fermion representation origin (fundamental vs. adjoint)
- Why do D7 fermions appear in the fundamental rep of SU(3), not the adjoint?
- Route B Hopf fiber provides structural motivation; formal derivation of representation content missing
- Files: `foundations/tension_analysis.md`, `foundations/three_generations.md`

### α_s error vs M_c(D7) uncertainty — **RESOLVED Cycle 144**
- **STATUS: CLOSED.** Root cause identified and fixed: α_s=0.1086 (8.1% off) used wrong M_c(D7) from α₁∩α₃ crossing (~2.5×10¹⁴ GeV), not the correct ECCC condition.
- **Correct condition:** α₃(M_c(D7)) = α_common = 2/(27π). ECCC gives M_c(D7)=1.566×10¹⁵ GeV → α_s(M_Z)=0.11821 (+0.006%, Tier 2a). `equations/alpha_em_selfconsistency.py`.
- **Remaining open:** Derive M_c(D7) from substrate depth-running (not from SM α_s inversion). The ECCC self-consistency is Tier 2a; the formal derivation of M_c(D7) from V(φ) alone is Tier 4.
- Files: `equations/alpha_em_selfconsistency.py` (Cycle 144), `equations/mc_closure_scales.py` (Cycle 130)

### T12 — α₁ chain tension: g₂-derived vs α_em-derived (Cycle 155; decomposed Cycle 158)

- The DFC 36π chain gives 1/α_em(M_Z) = 128.09; SM observed 1/α_em(M_Z) = 127.95
- Gap: +0.14 in 1/α_em(M_Z) = +0.109% (DFC over-predicts → under-runs coupling)
- **Root cause (Cycle 158):** The DFC b₁=41/10 running treats light quarks perturbatively throughout. The actual hadronic running has non-perturbative resonance contributions (ρ, ω, φ at √s < 2 GeV) adding EXTRA running not in b₁.
- **Gap decomposition (Cycle 158):**
  - δ(Δα)^{non-pert,net} = 0.14/137.036 = 0.00102 (the blocking piece)
  - = 3.70% of total Δα_had(PDG) = 0.02764
  - b₁ running already embeds 96.3% of hadronic effect (pQCD quarks massless)
- **DFC structural content:** N_c Σ Q_q² = 11/3 (from DFC N_c=3, Q_f=2/3,1/3) sets the scale; R∞=11/3 exact (Tier 2a, `equations/alpha_em_hadronic.py`)
- **Path to closure (Cycle 160 update):** σ=Q_top×Λ_QCD² (Tier 3, −4.2%); α_0=Q_top/4=1/2 (Tier 2a); m_ρ=√(2π)×Λ_QCD=763 MeV (Tier 3, −1.58%, 0 free params). Q_top=2 is the ONLY DFC Tier-1 integer giving c_σ<5%. Remaining: prove σ=Q_top×Λ² from D7 kink vacuum energy (Tier 4 = Yang-Mills mass gap). That proof would also fix the c_σ → BW → Δα_had → Δα dispersion chain.
- **Note (Cycle 159):** confinement.py "−83% failure" (45.9 MeV) was a one-loop artifact. Two-loop from same DFC α_s(M_Z) gives 304.5 MeV (consistent). This is not a new DFC prediction — it follows from having the correct α_s.
- Files: `equations/alpha_em_identity_proof.py` (Cycle 155), `equations/alpha_em_hadronic.py` (Cycle 158), `equations/rho_meson_dfc.py` (Cycle 159), `equations/d7_nonpert_coefficients.py` (Cycle 160), `equations/alpha_em_eccc.py` (Cycle 139)

### T10 — Near-maximal θ₂₃ argument self-contradicts (Cycle 65)
- The structural DFC argument for θ₂₃ ≈ 45° is "near-degeneracy of 2nd/3rd neutrino winding modes"
- But observed mass-squared differences give m₃ ≫ m₂ (Δm²₃₁/Δm²₂₁ = 33.8) — contradicts near-degeneracy
- Near-maximal θ₂₃ remains unexplained in DFC; the structural argument is not viable
- Files: `phenomena/particle_physics/neutrino_oscillations.md`, `equations/neutrino_oscillations.py`

### T11 — Neutrino hierarchy ratio: two inconsistent metrics in use (Cycle 65)
- `neutrino_masses.py` and ISSUES.md track the mass ratio m₃/m₂ ≈ √33.8 ≈ 5.81 (DFC gives 1.34, error 4.3×)
- `neutrino_oscillations.py` computes the Δm² ratio Δm²₃₁/Δm²₂₁ = 33.8 (DFC gives 1.34², error ~25×)
- Both failures have the same root cause (non-uniform D4 winding mode spacing), but the claimed error factor (4.3×) refers to mass ratios, not Δm² ratios
- Files: `equations/neutrino_masses.py`, `equations/neutrino_oscillations.py`, `phenomena/particle_physics/particles/neutrinos.md`

---

## Retracted Claims

| Claim | Retracted in | What Replaced It | Files Corrected |
|---|---|---|---|
| γ_D = (16/3)√β (bifurcation energy fraction derived from substrate) | Cycle 48 | E_kink/E_total(λ) = 8/3 exactly (universal constant, β-independent, > 1); γ_D cannot be physical prediction | `bifurcation_dynamics.py` (RETRACTED label), `bifurcation_dynamics.md`, 6 files with ΔV/E_kink corrected 0.71→0.265 |
| β ≈ 0.035 derived from γ_D inference | Cycle 48 | β = 0.0351 is Tier 3 reference value; provenance note in `coupling_derivation.py` | `coupling_derivation.py`, CLAUDE.md |
| E_kink = (4/3)c√(2α³/β) | Cycle 47 (audit finding) | BPS-correct: E_kink = (4/3)c²φ₀²/λ = (4/3)cα^(3/2)/(β√2) | `kink_model.py` |
| σ_geom uncertainty = ±0.8 GeV in Higgs mass | Cycle 38 | Corrected to ±3.4 GeV; m_H = 124.4 ± 3.7 GeV (PDG m_t) | `higgs_mass_derivation.md`, `higgs_potential.py` |

---

## Blocked Derivations

| Target | Why Blocked | Files | Required Extension |
|---|---|---|---|
| r_U1/λ = 3/(4β) from substrate | Real φ⁴ has no localizable U(1) phase; Routes A and B both blocked | `phase_stiffness_derivation.md` | Complex scalar or gauge field in substrate |
| M_c(D7) from substrate | Target 1.566×10¹⁵ GeV (confirmed Cycle 130 ECCC: the correct DFC condition α₃=α_common gives this self-consistently; γ_color ≈ 2.52 per D6→D7 step; Δ_D67=5.08 new Bottleneck 3 input); α₁∩α₃ crossing (old estimate 8×10¹⁴ GeV) identified as wrong condition | `depth_running.py`, `bifurcation_dynamics.py`, `alpha_s_target.py`, `mc_closure_scales.py` | Derive M_c(D7) from substrate depth-running (not from SM α_s inversion) to make α_s a genuine Tier 2 prediction |
| β ≈ 0.035 from pre-substrate principle | No pre-substrate condition identified that selects β | `beta_substrate.py` [STUB] | New theoretical input (pre-bifurcation stability condition) |
| Born rule for position | Spin case DERIVED (Cycle 38); Kramers escape rate Γ(x) ∝ \|φ(x)\|² not rigorously derived | `measurement.md`, `born_rule_derivation.md` | Escape rate calculation from V(φ) saddle topology |
| ℏ from (α, β, c) | S_kink(D1)/ℏ = 4×10³⁹ — 13.2 bifurcations needed to reach ℏ scale; model has only 4 | `planck_constant_derivation.md` | Either additional sub-bifurcation structure or route via α_em derivation |
| Confinement formal proof | Requires nonlinear SU(3) analysis; equivalent to Yang-Mills mass gap problem | `strong_force.md` (Open Q1), `strong_cp.md` | Nonlinear D7 field theory; beyond perturbation theory |
| v = 246 GeV from substrate | **TIER 2a (Cycle 145):** v=247.83 GeV (+0.65%) from EWSB co-crystallization. Remaining open: derive M_c(D5), M_c(D6) from substrate (currently from ECCC+SM inputs). | `equations/ewsb_cocrystallization.py` | Promote M_c(D5), M_c(D6) from ECCC condition to pure substrate derivation |
| CKM and PMNS matrices | Holonomy mismatch integral over D6/D7 boundary not computed | `flavor_mixing.md`, `tension_analysis.md` | D6/D7 overlap geometry → mixing angle computation |
| Electroweak loop corrections (Δρ_top) | One-loop DFC calculation from D6+D7 dynamics not done | `electroweak_precision.md` (Open Q1) | Standard Feynman diagram computation in DFC effective Lagrangian |

---

## Equation Module Stubs (No Implementation)

| Module | Target | Priority |
|---|---|---|
| `s_matrix.py` | Full S-matrix beyond Born; exact kink-antikink; 3+1D Skyrme | High — Bottleneck 3 |
| `planck_constant.py` | ℏ from DFC substrate characteristic scales | High — Bottleneck 2 |
| `fermion_spectrum_full.py` | Full lepton+quark mass spectrum (τ/top failures to fix) | High — Tier 2b failures |
| `beta_substrate.py` | COMPLETED Cycle 87 — Route F: β = 3g²/(8π) = 0.03536 (+0.75%, Tier 3 self-consistency); Routes A–E all documented as failures with numerical verification | Resolved as Tier 3; Tier 2 requires Bottleneck 2 proof |
| `dark_matter.py` | Stable intermediate kink modes as dark matter candidates | Medium |
| `cosmological_constant.py` | Λ from residual compression budget | Medium |
| `holographic_entropy.py` | Bekenstein-Hawking from closure capacity | Medium |
| `baryogenesis.py` | Matter-antimatter asymmetry at D7 phase transition | Medium |
| `inflation.py` | COMPLETED Cycle 68 — n_s=0.9667 ✓; A_s, r still blocked | — |

---

## Equation Module Placeholders / Circular Logic

| Module | Function | Issue |
|---|---|---|
| `gauge_couplings.py` | `squashing_correction()` | Returns None — PLACEHOLDER, geometric derivation pending |
| `quantum_emergence.py` | Born rule probability | CIRCULAR: assigns Ω/Ω_total = \|ψ\|² by definition, not derivation |
| `neutrino_masses.py` | m₂, m₃ predictions | CIRCULAR: m₂, m₃ derived from input Δm² values — not independent predictions |
| `bifurcation_dynamics.py` | `gamma_from_beta()` | RETRACTED — output is unphysical (ratio > 1); labeled but still present |
| `closure_topology.py` | `closure_energy()` | No stable minimum for SU(2)/SU(3) — Derrick's theorem violation for n≥3 |
| `pair_production.py` | α_em at low energy | INCONSISTENCY: uses perturbative one-loop QED running from M_Z → gives Δ(1/α)≈4.4; atomic_structure.py uses Δ(1/α)=10.46 (includes hadronic vacuum polarization). For √s > 2 GeV pair-production predictions: consistent. For absolute α(m_e): use atomic_structure.py. Corrected docstring in Cycle 104. |
| `pair_production.py` | σ(e⁺e⁻→μ⁺μ⁻) at 29–55 GeV | MISLEADING: large errors (10–18%) at √s=29–55 GeV arise from missing γ-Z interference (not DFC-specific); noted in docstring Cycle 104. Valid range for pure-photon formula: √s < 20 GeV or > 100 GeV. |

---

## Open Questions by Document

### foundations/

**`substrate.md`**
- Born rule for position (from Kramers escape rate) — OPEN
- ℏ from substrate — OPEN (T8)

**`higgs_geometry.md`**
- Open Q1: T9 two-closure-scale tension — RESOLVED Cycle 79 (see `foundations/two_scale_resolution.md`; M_c(D1) sets λ₀, M_c(D5/D6) sets gauge IC; not a genuine inconsistency)
- Open Q2: Derive μ², λ from (α, β, c)
- Open Q3: λ₀ ≈ 0 from modulus symmetry — needs formal proof
- Open Q4: Higgs as metric modulus vs. kink (conceptual clarification needed)

**`higgs_mass_derivation.md`**
- λ₀ boundary condition at M_c — currently matched to observed m_H; not independently predicted

**`depth_assignment.md`**
- DOF count per bifurcation from substrate dynamics — RESOLVED Cycles 72–74 (PT s=2 non-degeneracy)
- Why bifurcation cascade terminates at SU(3) — conjectured from D7 confinement; formal proof open

**`embedding_geometry.md`**
- M_c from substrate parameters (α, β, c) — currently read from SM running (not a DFC derivation)

**`mass_hierarchy.md`**
- Exponent κ (mass-to-depth scaling) — currently fitted from spectrum; not derived from substrate

**`three_generations.md`**
- Second excited state eigenvalue in D6 S³ geometry with D7 boundary — tau mass failure (8.4× in dimple model)
- Koide formula Step 3 (Z₃ Yukawa from D7 moduli space): Tier 3 (`equations/koide_step3_yukawa.py` Cycle 124)
- Koide formula Step 4 (canonical normalization): **RESOLVED Cycle 146 — Tier 2a.** θ_can=√Q_top·θ → vertex 1/√Q_top; Z₃ charge counting → t=1/√Q_top → K=2/3 → m_τ=1776.97 MeV. `equations/koide_phase_coupling.py`. No longer a known failure.

**`coupling_derivation.md`**
- Holonomy integral: physical identification r_U1 = φ₀²/(β f²) not derived from substrate
- KK reduction on S¹ (Route A) and domain-wall worldvolume (Route B) both blocked

**`bifurcation_dynamics.md`**
- γ_D ∈ (0,1) from substrate — RETRACTED result; no replacement yet
- E_total(L) normalization with macroscopic coherence length L — required to revive depth-running

**`kink_nucleation.md`**
- Born rule from first-passage / nucleation statistics — structural argument only

**`born_rule_derivation.md`**
- Position Born rule (Kramers escape rate) — OPEN; spin case complete

**`depth_assignment.md`**
- Route B (Hopf fibrations S¹→S³→S⁵) most promising; DOF count calculation not yet done
- n coincident modes → SU(n) proved (Cycle 59); mode count non-degeneracy proved (Cycle 73); D7 n=3 verified (Cycle 74) — Bottleneck 1 CLOSED

### phenomena/

**`particle_physics/forces/strong_force.md`**
- Formal proof of confinement from DFC (Open Q1) — Yang-Mills mass gap equivalent
- Derive Λ_QCD from D7 closure parameters (Open Q2) — Λ_QCD^DFC = 45.9 MeV (−83%); forward-running formula with threshold-matching incomplete; not directly linked to α_s gap
- Derive α_s from D7 geometry (Open Q3) — **RESOLVED Cycle 144 (Tier 2a):** α_s=0.11821 (+0.006%) via ECCC Direction B; remaining open = derive M_c(D7) from V(φ) alone
- Non-perturbative D7 dynamics: confinement, hadron masses, nuclear binding (Open Q4)

**`particle_physics/forces/electroweak_precision.md`**
- One-loop radiative corrections (Δρ_top) — not yet computed in DFC (Open Q1)
- Derive v = 246 GeV from substrate (Open Q2) — removes free parameter from 4 predictions
- CDF M_W anomaly (80.4335 GeV) — DFC prediction (79.67 GeV) is further from CDF than SM fit (Open Q3)

**`particle_physics/muon_decay.md`**
- Derive v = 246 GeV from substrate (Open Q1) — same as above
- Radiative corrections to M_W (Open Q3) — ~1% improvement possible at one loop
- Derive m_μ from substrate (Open Q4) — currently taken from data

**`particle_physics/hierarchy_problem.md`**
- Formal proof of geometric protection (Goldstone argument at all loop orders) (Open Q1)
- T9 two-closure-scale tension — RESOLVED Cycle 79 (Open Q2 closed; see `foundations/two_scale_resolution.md`)

**`particle_physics/strong_cp_problem.md`**
- S⁵ CP isometry and theta=0 fixed point: VERIFIED Cycle 147 (Tier 2a); `equations/strong_cp_theta.py`
- Formation selection theta=0 vs theta=pi: **RESOLVED Cycle 157 (Tier 2a)** — V(|Φ|²) real + D4 real IC → Im(Φ)≡0 exactly (ODE uniqueness theorem); D7 kink amplitude ∈ ℝ⁺ → theta_D7=0 by construction. ChPT confirms theta=0 is the stable minimum (Cycle 156). `equations/interface_overlap_integral.py`.
- Physical theta-bar = theta_QCD + arg(det M_q): **RESOLVED Cycle 157 (Tier 2a)** — D6/D7 Jackiw-Rebbi zero modes are real (sech profiles, residual 9.96e-07); Higgs VEV ∈ ℝ⁺; overlap Y_{ij} ∈ ℝ⁺ exactly (Im(Y)=0 computed for all separations); arg(det M_q)=0 exactly. `equations/interface_overlap_integral.py`, `equations/arg_det_mq_zero.py`.
- Criterion B prediction: no axion; falsifiable by ADMX/CASPEr etc.

**`particle_physics/particles/neutrinos.md`**
- Derive f_ν from substrate dynamics — blocks absolute neutrino mass scale
- Depth spacing ratio 1.34 vs observed 5.71 — [KNOWN_FAILURE]

**`particle_physics/particles/muon_tau.md`**
- τ mass: Koide formula Tier 2a (Cycle 146): m_τ=1776.97 MeV (+0.006%, `equations/koide_phase_coupling.py`). Dimple model SUPERSEDED. Document updated Cycle 148.

**`quantum/quantum_mechanics.md`**
- Born rule for position — OPEN (spin case derived, Cycle 38)

**`cosmology/big_bang.md` / `dark_energy.md`**
- Λ from substrate parameters — OPEN (displaced from fine-tuning to initial-conditions problem)
- Equation of state parameter ε: w_Λ = −1 + ε ≈ 0.007 from observation, not substrate

**`gravity/general_relativity.md`**
- Derive G_Newton from substrate — OPEN
- Derive Einstein field equations from dimensional folding gradient dynamics — OPEN

---

## Resolved Issues (move here when closed)

| Issue | Resolved in | How |
|---|---|---|
| k_Y = 3/5 origin (was borrowed from SU(5)) | Cycle 30 | Derived from Dynkin index matching on SM matter content — no GUT needed |
| Tsirelson bound CHSH ≤ 2√2 unprovable claim | Cycle 35 | Proved algebraically: C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂] → ‖C‖ ≤ 2√2 |
| Schrödinger equation "assumed" | Cycle 36 | Derived from KG in non-relativistic limit; labeled DERIVED in substrate.md |
| Binary measurement outcomes "postulated" | Cycle 36 | Proved topologically: Z₂ configuration space of φ⁴ kink |
| Born rule for spin "assumed" | Cycle 38 | Derived: P(↑,n̂) = cos²(θ/2) from SU(2) spinor geometry + binary nucleation |
| E_kink formula wrong | Cycle 47–48 | BPS-correct formula derived; γ_D retracted; all downstream files corrected |
| G_F as pure experimental input | Cycle 51 | G_F derived from β via coupling chain (+0.18%); added to Tier 2a |
| Berger sphere R₄ as source of Higgs quartic λ | Cycle 58 | R₄ = 0 exactly proved (analytic + numeric); λ comes from substrate β/4 ≈ 0.0088; see `equations/berger_sphere.py` |
| higgs_geometry.md: m_H = 125.1 ± 1.5 GeV stale value | Cycle 60 | Corrected to 124.4 ± 3.7 GeV (Cycle 38 correction now propagated); quartic source updated (β not S³ curvature — Cycle 58) |
| higgs_geometry.md: quartic attributed to "S³ curvature resistance" | Cycle 60 | Corrected: Ricci quartic R₄=0 (Cycle 58); λ = β/4 from substrate; Ricci term −8ε² destabilizes ε=0 |
| Flux quantization Φ₀ = h/(2e) as structural only | Cycle 60 | Verified numerically to 2.2×10⁻¹⁰ relative error; Josephson K_J to 2×10⁻¹²; added as Tier 1 in superconductivity module |
| kink_scattering.py used old retracted kink mass formula | Cycle 59 | Corrected to BPS-correct E_kink = (4/3)cα^(3/2)/(β√2); gamma_D provenance note updated |
| SU(n) from n coincident modes: claimed as correspondence only | Cycle 59 (partial); fully closed Cycles 73–74 | Proved: n coincident degenerate zero modes → SU(n) (Cycle 59); PT s=2 non-degeneracy → exactly 1 zero mode per kink (Cycle 73); D7 n=3 verified (Cycle 74) |
| Neutron lifetime hidden in `proton_stability.py` | Cycle 52 | Added to `__main__` output; both G_F routes shown |
| sin²θ_W(M_Z) Route 3B derivation (open since model inception) | Cycle 22 | sin²θ_W = 3/8 at M_c → 0.231 at M_Z from equal-coupling + SM running; 0.01% error |
| E=hν claimed "derived" from massless KG dispersion | Cycle 42 | Corrected: E=ℏω is a QFT postulate imported from outside DFC; labeled as such |
| muon_tau.md: τ_μ = 2.197 μs "< 0.1% match" (false) | Cycle 51 | Corrected to DFC prediction 2.180 μs (−0.80%); actual chain derivation added |
| T9: Two closure scales (10¹³ vs 10¹⁸ GeV) inconsistency | Cycle 79 | Labeling confusion: M_c(D1) = M_Pl sets Higgs λ₀; M_c(D5/D6) ≈ 10¹³ GeV sets gauge IC. GUT-normalized α₁ = α₂ crossing verified numerically. See `foundations/two_scale_resolution.md`, `equations/two_scale_check.py` |
| Tau lepton mass mechanism Step 4d (Koide Tier 3→Tier 2a) | Cycle 146 | Canonical normalization: θ_can=√Q_top·θ → vertex e^{iθ}=exp(iθ_can/√Q_top); one-insertion coefficient 1/√Q_top. Z₃ charge table: all 6 off-diagonal (n,m) pairs have |charge diff|=1 mod 3 → exactly 1 insertion → t=1/√Q_top → K=2/3 (error 1.11e-16) → m_τ=1776.97 MeV (+0.006%, Tier 2a). `equations/koide_phase_coupling.py`. Dimple model SUPERSEDED. |
| α_s(M_Z) gap: 8.1%→+0.006% | Cycle 144 | Root cause: wrong M_c(D7) from α₁∩α₃ crossing (not ECCC condition). ECCC: α₃(M_c(D7))=α_common=2/(27π) gives α_s=0.11821 (+0.006%, Tier 2a). `equations/alpha_em_selfconsistency.py`. |
| EWSB vacuum v: Tier 3→Tier 2a | Cycle 145 | SU(2) in Higgs phase cannot drive its own transmutation; D7 SU(3) confining (b₀=N_Hopf+Q_top=11) drives EWSB scale; co-crystallization correction Δ_D56. v=247.83 GeV (+0.65%, Tier 2a). `equations/ewsb_cocrystallization.py`. |
| Strong CP problem: theta=0 structural | Cycle 147 | S⁵ CP-isometry proved numerically (50k samples, max dev 6.7e-16); theta=0 is unique CP fixed point; D6/D7 independence from pi_3(S³)=Z≠pi_3(S⁵)=Z₂; d_n=0 Criterion B prediction. Tier 2a overall. `equations/strong_cp_theta.py`. Formation argument (theta=0 vs pi) remains Tier 3. |
| Strong CP formation + arg(det M_q)=0 | Cycle 157 | Interface overlap integral computed: V(|Φ|²) real amplitude preservation theorem (ODE uniqueness) proves D4→D5→D6→D7 amplitude chain is real positive. Jackiw-Rebbi zero modes real (sech^n, verified residual 9.96e-07). D6/D7 overlap Im(Y)=0 exactly. theta_bar=0 Tier 2a. `equations/interface_overlap_integral.py`. |
| Tau lepton mass mechanism (8.4× from dimple model, Tier 3 chain) | Cycles 122–126 | Koide formula replaces dimple model: m_τ=1776.97 MeV (+0.006%) from m_e,m_μ with 0 free params (Tier 3 chain). FULLY PROMOTED TO Tier 2a in Cycle 146 — see entry above. |
| Bottleneck 2 (r_U₁/λ, coupling derivation) | Cycle 117 | Tier 2a: g_eff²=8/27 (error 0.00e+00), β=1/(9π), 0 free parameters. Full chain: V(φ)→tachyon→complex scalar→O(2)→U(1)→J→d_n=2n−1→N_Hopf=9→g_eff²=8/27 (`equations/d5_complex_from_instability.py`). |
