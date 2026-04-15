# The Electroweak VEV from DFC Substrate Parameters

## Status

> **Cycle 53:** This document formally maps the v = 246 GeV derivation problem.
> v is currently an experimental input to four Tier 2a predictions (M_W, M_Z, G_F, τ_μ).
> Completing this derivation would promote those four predictions to fully first-principles
> results, removing the last experimental input from the weak-sector coupling chain.
>
> **Epistemic status: OPEN.** The structural argument for why μ² and λ have the right
> signs is complete; the numerical computation of their magnitudes from (α, β, c)
> is the missing step.

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

The term that stabilizes the potential at large squashing — the brim of the Mexican hat
— comes from the intrinsic curvature resistance of the S³ geometry. A round three-sphere
is a rigid object: deforming it from round to ellipsoidal costs energy proportional to
the square of the eccentricity. At large squashing (ε → ∞), this cost dominates.

For small squashing, the curvature energy scales as ε⁴ rather than ε² because: the
leading (ε²) correction to the Ricci scalar under uniform S³ squashing vanishes by
symmetry (the squashing is a conformal mode, not a Ricci-changing mode, at leading
order). The first non-trivial curvature cost is at quartic order:

```
V_curvature(ε) ≈ +λ_DFC ε⁴    where λ_DFC ~ (S³ curvature resistance) / (closure radius)⁴
```

This is the same suppression that makes the tree-level Higgs quartic small:
λ_tree(M_c) ≈ 0.013 (see `foundations/higgs_mass_derivation.md`). The gauge-Higgs
unification structure of the S³ modulus protects the quartic from being O(1).

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

### 3.3 Connection to the T9 tension

The T9 tension (see `ISSUES.md` Critical section) is directly relevant here: the Higgs
mass derivation uses M_c(Higgs) ≈ 10¹⁸ GeV, while the Weinberg angle derivation uses
M_c(D5/D6) ≈ 10¹³ GeV. The VEV derivation requires knowing which M_c is the physical
cutoff for the squashing potential. Resolution options:

**(a) Two distinct closure events:** D5/D6 co-crystallization (≈ 10¹³ GeV) is the scale
at which the gauge structure freezes and the equal-coupling condition applies. The Higgs
mass derivation closure (≈ 10¹⁸ GeV) is the scale at which the geometric description of
the S³ modulus becomes dynamical — a different event, the D6 geometric mode being
promoted to a propagating degree of freedom. If this interpretation is correct, then:

- v is set by dynamics below the D6 activation scale (≈ 10¹⁸ GeV)
- The gauge coupling running uses the D5/D6 co-crystallization scale (≈ 10¹³ GeV)
- The two scales are physically distinct closure processes

**(b) Single closure scale with derivation error:** If both processes occur at the same
scale, one of the two numbers (10¹³ vs 10¹⁸) contains a systematic error. This would
require retracing the Route 3B running and/or the Higgs RG analysis.

Resolution of T9 is a prerequisite for the VEV derivation, because v enters as
v = μ/√λ, and the scale at which μ and λ are defined depends on which M_c is correct.

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

### 4.2 Step 2 — Compute S³ curvature resistance

The quartic coefficient λ from the S³ geometry requires computing the fourth-order term
in the expansion of the S³ Ricci scalar under uniform squashing:

```
R(ε) = R₀ + R₂ ε² + R₄ ε⁴ + ...
```

For a round S³ with radius r, R₀ = 6/r². The first non-trivial squashing-induced
correction R₄ is the curvature resistance λ_DFC. This is a geometric calculation in
differential geometry — the expansion of the Ricci scalar for the Berger sphere
(one-parameter family of squashed S³ metrics).

**This calculation is tractable.** The Berger sphere metric squashing is a known
object in differential geometry. The fourth-order term in the Ricci scalar expansion
is computable. This is the most tractable step in the VEV derivation.

The Berger sphere family: the metric on S³ with squashing parameter ε along the Hopf
fiber direction is:

```
ds²(ε) = (1/4) [(σ₁² + σ₂²) + (1 + ε)² σ₃²]
```

where σ₁, σ₂, σ₃ are the left-invariant 1-forms on SU(2). The Ricci scalar for this
metric has the expansion:

```
R(ε) = 6/r² × [1 − (ε²/4) + (higher order)]     [schematic — signs need verification]
```

The precise fourth-order coefficient — which is λ_DFC in DFC units — requires evaluating
the quartic term in this expansion with the DFC closure radius r = r_D6.

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
potential — equals the fourth-order coefficient in the expansion of the S³ Ricci scalar
under Berger squashing, divided by the fourth power of the D6 closure radius:

```
λ_DFC = R₄_Berger / r_D6⁴
```

The consistency condition that both numbers must satisfy is:

```
μ_DFC / √λ_DFC = 246 GeV    →    μ_DFC = 246 × √λ_DFC ≈ 28 GeV  (for λ ≈ 0.013)
```

---

## 7. Open Problems

1. **Berger sphere quartic coefficient.** Compute R₄ in the expansion of R(ε) for
   the Berger sphere metric, expressed in DFC substrate units. This is tractable
   via the Ricci tensor formula for the squashed S³: R_ij = diag(2/r², 2/r², 2/(r²(1+ε)²))
   at leading squashing. The fourth-order term requires evaluating the curvature-squared
   corrections. Target: λ_DFC ≈ 0.013 (consistent with SM vacuum stability running).

2. **D6/D7 overlap integral.** Compute ∫|∂_z φ_kink(D7)| × δV_D6(z) dz to give μ²
   in substrate units. Requires knowing the relative depth separation between D6 and D7
   closures (Bottleneck 1) and the cross-depth coupling in V(φ). Target: μ ≈ 28 GeV.

3. **Resolve T9 before computing v.** The scale at which V(ε) is evaluated determines
   whether μ and λ are computed at 10¹³ GeV or 10¹⁸ GeV. The two-scale interpretation
   (gauge scale ≠ modulus activation scale) needs formal justification from the DFC
   field dynamics.

4. **RG matching at closure scale.** Once μ_DFC and λ_DFC are computed at M_c, they
   must be run down to the electroweak scale using the SM RGE before the VEV is extracted.
   This running is standard SM calculation (already done for λ in higgs_mass_derivation.md)
   but requires the correct M_c as the starting point.

---

## Connections

- `foundations/higgs_geometry.md` — S³ squashing potential; Open Question 2 (derive μ, λ)
- `foundations/higgs_mass_derivation.md` — λ₀ ≈ 0.013 at closure scale; RG running
- `foundations/depth_assignment.md` — Route B: S³ at D6 (source of the curvature geometry)
- `foundations/coupling_derivation.md` — coupling chain from β to M_W, M_Z, G_F, τ_μ
- `foundations/hopf_fibration_geometry.md` — Berger sphere structure at D6 depth
- `foundations/tension_analysis.md` — T9: two-closure-scale tension
- `phenomena/particle_physics/muon_decay.md` — M_W, M_Z, G_F, τ_μ predictions (v input)
- `phenomena/particle_physics/forces/electroweak_precision.md` — five precision tests
- `ISSUES.md` — T9 (Critical), Bottleneck 1 (D-depth assignment), Blocked: v = 246 GeV
