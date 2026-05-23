# The Electroweak VEV from DFC Substrate Parameters

## Status

> **Cycle 53:** This document formally maps the v = 246 GeV derivation problem.
> v is currently an experimental input to four Tier 2a predictions (M_W, M_Z, G_F, τ_μ).
> Completing this derivation would promote those four predictions to fully first-principles
> results, removing the last experimental input from the weak-sector coupling chain.
>
> **Cycle 58 — MAJOR CORRECTION:** The claim that λ_DFC = R₄/r_D6⁴ (the quartic
> coefficient of the Berger sphere Ricci scalar) is **wrong**. R₄ = 0 identically
> for the biaxial Berger sphere with DFC parametrization a=1/2, b=(1+ε)/2. The exact
> result is R(ε) = 24 − 16ε − 8ε² — a polynomial of degree 2. The quartic stabilizer
> λ comes from the substrate quartic β, not from the Ricci geometry. See
> `equations/berger_sphere.py` for the analytic derivation and numerical verification.
>
> **Cycle 79 update:** T9 is resolved — no longer a blocker for this derivation.
> M_c(D1) = M_Pl sets the Higgs quartic UV boundary; M_c(D5/D6) ≈ 10¹³ GeV sets gauge
> couplings. The VEV derivation uses M_c(D5/D6) as the relevant scale (D6 is part of the
> D5/D6 co-crystallization). Remaining gaps: (1) μ² from the D6/D7 overlap integral;
> (2) λ field normalization factor ~1.5 between β/4 ≈ 0.0088 and λ_SM(M_c) ≈ 0.013.
>
> **Epistemic status: OPEN.** T9 blocker cleared. Two genuine open problems remain
> before v can be predicted from substrate parameters.
>
> **Cycle 86 update:** `equations/vev_derivation.py` (new) provides quantitative
> Bottleneck 3 analysis. New findings: (1) The SM quartic runs **negative** at
> M_c(D5/D6) ≈ 9.70×10¹² GeV (SM vacuum metastable there), confirming that DFC must
> provide a POSITIVE UV boundary condition λ_BC = β/4 ≈ 0.0088 at M_c. This is a
> Tier 1 structural result. (2) DFC BC + 2-loop SM running gives m_H = 122.9 GeV
> (−1.9% error), consistent with higgs_potential.py (124.4 ± 3.7 GeV). (3) Target
> for D6/D7 overlap integral: μ = v × √λ_DFC = **23 GeV** (concrete numerical target).
> (4) The required D6/D7 overlap I_D67 ≈ 10⁻²⁸ — exponential suppression from the
> D6/D7 depth gap explains its smallness. Blockers: threshold positions (Bottleneck 1)
> and M_c(D7) (depth-running).
>
> **Cycle 130–131 update (ECCC + gap analysis):** ECCC closure scales now available
> from `equations/mc_closure_scales.py`: M_c(D5)=1.14×10¹³ GeV, M_c(D6)=9.70×10¹² GeV,
> M_c(D7)=1.57×10¹⁵ GeV, Δ_D67=5.085 (= log(M_c(D7)/M_c(D6))). **Gap analysis**
> (`equations/d6_d7_overlap.py`, Cycle 131): the narrow-kink sech² profile overlap
> gives I_sech ≈ ξ_D7/ξ_D6 = exp(−Δ_D67) ≈ 0.006, while the required I_D67 =
> β v²/(4 M_c(D7)²) ≈ 2.18×10⁻²⁸. **Gap factor: 2.8×10²⁵ (25 orders of magnitude).**
> All four candidate routes analyzed (cascade, power law, radiative, D6-anchored): none
> resolves the gap with current DFC depth count. The gap IS the hierarchy problem recast
> in DFC language. The power-law route (I = (v/M_c(D7))^p with p≈2.16) is the most
> promising but requires deriving p from the D6/D7 coupling structure. Bottleneck 3
> remains Tier 4 open.

---

## 1. The Problem

The electroweak coupling chain in DFC runs:

```
β → g² = 8πβ/3 → g_common = 0.5423
  → Route 3B equal-coupling + SM RG running
  → g₂(M_Z) = 0.6477,   sin²θ_W = 0.2312
  → M_W = g₂ v / 2
  → M_Z = M_W / cos θ_W
  → G_F = 1/(√2 v²)
  → τ_μ = 192π³ℏ / (G_F² m_μ⁵)
```

Every step in this chain except one is computed from DFC substrate parameters. The
exception is v = 246 GeV — the electroweak vacuum expectation value. This is the value
of the Higgs field at the minimum of the Mexican hat potential, the scale that sets the
W and Z boson masses. It is taken from experiment.

**What needs to be derived:** The squashing potential V(ε) = −μ²ε² + λε⁴ has a minimum
at the VEV — the value of the squashing parameter at which the potential energy is
smallest — equal to:

```
ε₀ = v/√2 = μ / √(2λ)
```

This means deriving v = 246 GeV requires computing μ and λ from the DFC substrate
parameters (α, β, c). Currently both are structural arguments, not numbers.

---

## 2. Structural Origin of μ² and λ

### 2.1 The negative mass-squared term μ²

The term that makes the symmetric point ε = 0 unstable — driving the spontaneous
symmetry breaking — has a geometric origin in DFC: it is the pressure exerted on the
D6 S³ closure geometry by the D7 SU(3) closure.

The D7 SU(3) closure is slightly asymmetric — it must be, in order to break the right-copy
flavor symmetry that would otherwise give degenerate quark flavors. This asymmetry in
the D7 geometry exerts a stress on the shared D6/D7 boundary. The D6 S³ responds to
this stress by deforming away from ε = 0, because a round sphere under asymmetric
external pressure minimizes energy at an ellipsoidal configuration, not at the symmetric
one.

In the effective potential for the squashing parameter ε, this external pressure appears
as a term proportional to −ε². The sign is negative because the pressure drives
deformation, which destabilizes the symmetric point. The coefficient μ² is proportional
to the magnitude of the D7 asymmetry, which in DFC is set by the SU(3) flavor symmetry
breaking scale.

In the substrate parametrization: the D7 closure creates an asymmetric distribution of
the compression field φ across the D6 boundary. The leading contribution to the D6
squashing potential from this asymmetric pressure is:

```
V_pressure(ε) ≈ −μ²_DFC ε²    where μ²_DFC ~ α_D7 × f(β, depth geometry)
```

The function f(β, depth geometry) encodes how the D7 compression amplitude couples into
the D6 shape mode. This coupling is not yet computed numerically.

### 2.2 The quartic restoring term λ

**Cycle 58 correction:** The pre-Cycle 58 account claimed that λ comes from the quartic
term in the Berger sphere Ricci scalar expansion. This is incorrect. The exact Ricci
scalar for the biaxial Berger sphere is:

```
R(ε) = 24 − 16ε − 8ε²   [exact; see equations/berger_sphere.py]
```

The quartic coefficient R₄ = 0 identically. There is no quartic term in R(ε). The
Ricci term actually DESTABILIZES ε = 0 (R decreases with |ε|, so geometric curvature
energy decreases as squashing increases — this is a negative-mass-squared contribution,
not a quartic stabilizer).

**Correct source of λ:** The quartic stabilizer comes from the substrate quartic
coupling β, evaluated at D6 depth. The DFC substrate potential V(φ) = −α/2 φ² + β/4 φ⁴
evaluated at the squashing mode gives the full Higgs potential directly:

```
V(ε) = −α_D6/2 ε² + β/4 ε⁴
```

The quartic term β/4 ε⁴ is the stabilizer. In terms of standard Higgs potential
notation V_H = −μ² h² + λ h⁴:

```
λ_DFC = β/4 ≈ 0.0351/4 ≈ 0.0088
```

Comparison with the SM tree-level value λ₀(M_c) ≈ 0.013 from vacuum stability running:
the DFC value is approximately 1.5× below. This factor reflects a normalization
mismatch between the substrate field ε and the SM Higgs field h — a remaining open
problem in the field identification. The structural identification λ ↔ β is correct;
the precise normalization requires care in mapping ε ↔ h.

### 2.3 The Minimum

The competition between destabilization (μ²) and stabilization (λ) produces the
spontaneous symmetry breaking minimum at:

```
ε₀² = μ²_DFC / (2 λ_DFC)    →    v = √2 ε₀ = μ_DFC / √λ_DFC
```

The electroweak VEV v = 246 GeV is the ratio μ/√λ evaluated at the D6 closure scale.

---

## 3. The Numerical Target

### 3.1 What needs to be computed

To derive v from first principles, two numbers are needed:

**μ² (units: GeV²):** The D7-to-D6 squashing pressure coefficient. In substrate units,
this involves:
- The D7 compression amplitude φ₀(D7) = √(α_D7/β)
- The coupling between D7 asymmetry and D6 shape modes (a D6/D7 overlap integral)
- The normalization that converts substrate energy to GeV²

The structural estimate is μ ≈ M_W ≈ 80 GeV, since the W boson mass sets the natural
electroweak scale. The more precise value depends on the overlap integral.

**λ (dimensionless):** The S³ curvature resistance coefficient. The physical quartic
coupling at the electroweak scale is λ(v) ≈ 0.129 (from the Higgs mass: m_H² = 2λv²
→ λ = m_H²/(2v²) = (125 GeV)²/(2 × 246²) = 0.129). At the closure scale, the tree-level
value is suppressed to λ₀ ≈ 0.013 (from SM vacuum stability running; see
`foundations/higgs_mass_derivation.md`). So the target at the closure scale is:

```
λ_DFC(M_c) ≈ 0.013 ± 0.007    [from SM running — not yet computed from DFC]
```

### 3.2 The consistency condition

If both μ and λ are computed from substrate parameters, the VEV is:

```
v = μ/√λ = √(μ²/λ)
```

For v = 246 GeV, with λ ≈ 0.013:

```
μ = v × √λ = 246 × √0.013 ≈ 246 × 0.114 ≈ 28 GeV
```

This is a concrete numerical target: the D7-to-D6 pressure must give an effective
mass parameter μ ≈ 28 GeV at the closure scale, which then runs (as part of the
electroweak sector) to the observed VEV at low energy.

### 3.3 T9 resolved — scale identification for the VEV derivation

**T9 is resolved (Cycle 79).** The two scales are physically distinct depth events and
can both be correct simultaneously (see `foundations/two_scale_resolution.md`):

- **M_c(D1) = M_Pl ≈ 10¹⁸ GeV:** D1 maximum-compression boundary. Sets the Higgs quartic
  UV boundary condition λ₀ ≈ 0.013. Used by `foundations/higgs_mass_derivation.md`.
- **M_c(D5/D6) ≈ 10¹³ GeV:** D5/D6 co-crystallization scale. Sets the equal-coupling
  gauge IC. Used by Route 3B. This is the relevant scale for the VEV derivation because
  the Higgs is a D6 object — its mass and VEV are set at the D6 closure scale, not at D1.

**Consequence for the VEV derivation:** The squashing potential V(ε) = −μ²ε² + β/4 ε⁴
is evaluated at M_c(D5/D6) ≈ 10¹³ GeV. The VEV v = μ/√λ at this scale then runs down
to the observed electroweak VEV v ≈ 246 GeV. The correct target for μ at M_c(D5/D6) is:

```
μ(M_c) = v_EW × √λ₀ = 246 × √0.013 ≈ 28 GeV
```

where λ₀ ≈ 0.013 is the tree-level quartic at the D6 closure scale (from SM running).
This remains the numerical target for the D6/D7 overlap integral computation.

---

## 4. The Derivation Path

### 4.1 Step 1 — Compute the D6/D7 overlap integral

The D7 closure amplitude φ₀(D7) couples to the D6 squashing mode through the gradient
of the compression field across the D6/D7 boundary. In the kink picture, this is:

```
μ² ∝ ∫ |∂_z φ_kink(D7)| × δV_D6(z) dz
```

where z is the depth coordinate, φ_kink(D7) is the D7 kink profile, and δV_D6(z) is the
perturbation to the D6 squashing potential induced by the D7 configuration.

This integral requires knowing the spatial overlap between the D7 kink tail and the D6
squashing region. In the substrate, both are centered at different compression thresholds
(D6 at M_c(D6), D7 at M_c(D7)), with an exponentially decaying overlap proportional to
exp(−Δ_depth × L), where Δ_depth = depth separation and L = kink characteristic length.

**Blocking factor:** The depth separation Δ_depth = M_c(D6) − M_c(D7) (in log energy
units) is not known from substrate dynamics — it requires completing Bottleneck 1
(D-depth assignment mechanism).

### 4.2 Step 2 — Establish λ from substrate β (Cycle 58 result)

**This step is now resolved.** The Berger sphere Ricci scalar has been computed exactly
(Cycle 58, `equations/berger_sphere.py`):

The Ricci scalar equals twice the sum of sectional curvatures. For the biaxial Berger
sphere with horizontal radius one-half and fiber radius one-half times one plus
the squashing parameter:

```
R(ε) = 2(4a² − b²)/a⁴   with a = 1/2, b = (1+ε)/2
     = 32 − 8(1+ε)²
     = 24 − 16ε − 8ε²   [EXACT — polynomial terminates at degree 2]
```

The quartic coefficient R₄ = 0 exactly (verified numerically to 1.5×10⁻¹² by
fourth-order finite difference). The Ricci scalar provides:
- A linear destabilization term (−16ε, first order in squashing)
- A quadratic destabilization term (−8ε², contributing to −μ²_eff ε²)
- **No quartic term**

The quartic stabilizer therefore comes from the substrate potential directly:

```
V(ε) = −α_D6/2 ε²  +  β/4 ε⁴       [substrate potential at D6 depth]
        ↑                  ↑
    destabilization    stabilization
  (D7 pressure + R)   (substrate β)

λ_DFC = β/4 ≈ 0.00877
```

The ~1.5× factor between λ_DFC and λ_SM(M_c) ≈ 0.013 is an open normalization
problem in the ε ↔ h field identification. The structural source of λ is now identified.

### 4.3 Step 3 — Convert to GeV

Both μ² and λ are initially computed in substrate units (dimensionless ratios of α, β, c).
Converting to GeV requires identifying the mass scale of the D6 closure, which in DFC
is set by the closure scale M_c(D6).

If M_c(D6) ≈ 10¹³ GeV (from Route 3B), then substrate-to-GeV conversion factors can be
computed from the kink mass formula at D6: m_kink(D6) ∝ c × φ₀(D6)²/λ_D6 ∝ c × α_D6^(3/2)/β_D6.

---

## 5. What Completing This Derivation Would Achieve

### 5.1 Upgrade four Tier 2a predictions to zero-free-parameter

Currently, four Tier 2a predictions (M_W, M_Z, G_F, τ_μ) use three inputs:
- β = 0.0351 (Tier 3 reference value — only partially derived)
- v = 246 GeV (experimental input)
- m_μ = 105.66 MeV (experimental input — needed for τ_μ)

If v is derived from (α, β, c), the second input disappears. The predictions become:

```
β, c, α, m_μ  →  M_W, M_Z, G_F, τ_μ
```

with m_μ the only remaining experimental input for the muon lifetime, and β still needing
derivation from a pre-substrate condition (Bottleneck 3).

### 5.2 Criterion A progress

This derivation would partially satisfy Criterion A (derives an SM postulate without
circular import): v = 246 GeV is a free parameter of the Standard Model's Higgs sector.
Deriving it from DFC substrate geometry would be the first case where the DFC derives
an SM input that cannot be derived within the SM itself.

### 5.3 Resolve or sharpen T9

The derivation requires resolving which closure scale applies to the squashing potential.
This resolution would either confirm the two-scale picture (D5/D6 gauge vs. D6 geometric)
or reveal a derivation error in either Route 3B or the Higgs mass derivation.

---

## 6. Formal Equations

The electroweak VEV, the value of the squashing parameter at the minimum of the effective
potential, equals the ratio of the mass parameter to the square root of twice the quartic
coupling:

```
v = μ / √λ ≈ 246 GeV
```

In DFC, the mass parameter squared — the negative coefficient of the quadratic term in
the squashing potential — is proportional to the D7 closure amplitude times the D6/D7
overlap integral, where the overlap integral measures how strongly the D7 asymmetric
compression state couples into the D6 shape mode:

```
μ²_DFC ∝ α_D7 × I_overlap(D6, D7)
```

The quartic coupling — the positive coefficient of the fourth-order term in the squashing
potential — comes directly from the substrate quartic coupling β (the Berger sphere Ricci
scalar contributes only a quadratic destabilizing term; its quartic coefficient R₄ = 0
exactly, proved in Cycle 58):

```
λ_DFC = β / 4 ≈ 0.0088
```

This is ~1.5× below λ_SM(M_c) ≈ 0.013, reflecting a field normalization factor between
the substrate squashing parameter ε and the canonically normalized SM Higgs field h.

The consistency condition that both numbers must satisfy is:

```
μ_DFC / √λ_DFC = 246 GeV    →    μ_DFC = 246 × √λ_DFC ≈ 28 GeV  (for λ ≈ 0.013)
```

---

## 7. Open Problems

1. **~~Berger sphere quartic coefficient~~** — **RESOLVED (Cycle 58):** R₄ = 0 exactly.
   The quartic stabilizer does NOT come from the Ricci scalar geometry. λ is identified
   as β/4 from the substrate potential. See `equations/berger_sphere.py`.

2. **Field normalization: ε ↔ h.** The substrate squashing parameter ε and the SM
   Higgs field h are related by a normalization factor. With λ_DFC = β/4 ≈ 0.0088
   and λ_SM(M_c) ≈ 0.013, the ratio is ~1.5. Identifying the precise DFC-to-SM
   field normalization (likely a factor involving the closure radius r_D6) would
   close this gap without requiring new physics.

3. **D6/D7 overlap integral for μ².** Compute ∫|∂_z φ_kink(D7)| × δV_D6(z) dz to
   give μ² in substrate units, then convert to GeV. This requires knowing the relative
   depth separation between D6 and D7 closures (Bottleneck 1). Target: μ ≈ 28 GeV
   (from consistency condition μ = v√λ with v = 246 GeV, λ ≈ 0.013).

4. **α_D6 in GeV units.** The VEV is v = √(2α_D6/β) in substrate units. Converting
   to GeV requires identifying M_c(D6) from Bottleneck 1. This is the last step
   once μ² and the normalization are resolved.

5. ~~**Resolve T9.**~~ **RESOLVED (Cycle 79).** The VEV is evaluated at M_c(D5/D6) ≈
   10¹³ GeV; M_c(D1) = M_Pl sets the Higgs λ₀ UV boundary only. See
   `foundations/two_scale_resolution.md`. The remaining issues are Items 2–4 above.

---

## Connections

- `foundations/higgs_geometry.md` — S³ squashing potential; Open Question 2 (derive μ, λ)
- `foundations/higgs_mass_derivation.md` — λ₀ ≈ 0.013 at closure scale; RG running
- `foundations/depth_assignment.md` — Route B: S³ at D6 (source of the curvature geometry)
- `foundations/coupling_derivation.md` — coupling chain from β to M_W, M_Z, G_F, τ_μ
- `foundations/hopf_fibration_geometry.md` — Berger sphere structure at D6 depth
- `foundations/two_scale_resolution.md` — T9 RESOLVED (Cycle 79): M_c(D1) vs M_c(D5/D6)
- `foundations/tension_analysis.md` — T9 entry updated: Structurally Resolved
- `phenomena/particle_physics/muon_decay.md` — M_W, M_Z, G_F, τ_μ predictions (v input)
- `phenomena/particle_physics/forces/electroweak_precision.md` — five precision tests
- `equations/vev_derivation.py` — Cycle 86: Bottleneck 3 quantitative analysis; SM running,
  DFC BC → m_H = 122.9 GeV, target μ = 23 GeV, D6/D7 overlap framework
- `equations/mc_closure_scales.py` — Cycle 130: ECCC closure scales; M_c(D6)=9.70e12, M_c(D7)=1.57e15, Δ_D67=5.085
- `equations/d6_d7_overlap.py` — Cycle 131: gap factor 2.8×10²⁵; power-law p≈2.16 route; hierarchy problem characterization
- `ISSUES.md` — T9 (Critical), Bottleneck 1 (D-depth assignment), Blocked: v = 246 GeV
