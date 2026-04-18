# Foundation: Complex Scalar Extension at D5 — Opening the Gauge Coupling Derivation

## Status

> **Cycle 75:** Proposes and analyses the extension of the D5 substrate sector from a
> real scalar φ to a complex scalar Φ = φ₁ + iφ₂ with potential
> V = −α/2|Φ|² + β/4|Φ|⁴. This extension is exploratory — it is not yet a Tier 0 revision
> but a candidate modification whose consequences are being mapped.
>
> **Motivation:** The gauge coupling g² = 8πβ/3 is computed heuristically with 0.37% match
> (Cycle 42), but the step from phase stiffness f² to the closure fiber radius r_U1/λ = 3/(4β)
> lacks a derivation from the field equation. Both candidate derivation routes (KK reduction,
> domain-wall worldvolume) are blocked for a real scalar because real φ⁴ has no circle in
> field space. The complex extension provides that circle.
>
> **Key structural result (new in Cycle 75):** The fluctuation operator for the transverse
> (φ₂) direction around a real kink in the complex scalar is a Pöschl-Teller operator with
> s = 1, giving one bound state at ω² = −α/2 < 0. This tachyonic mode is NOT a physical
> instability of D6/D7 particles — it is the signature that D5 does not form real kinks at
> all. The stable D5 defect is the vortex (classified by π₁(S¹) = ℤ), not the Z₂ kink.
> This is structurally consistent with D5 = U(1): a U(1) closure behavior produces vortices,
> not Z₂ walls.
>
> **What the extension opens:** KK reduction on the field-space S¹ of radius φ₀ and the
> Abelian Higgs vortex holonomy both become geometrically well-defined. The vortex core
> radius r_v ~ ξ is a new length scale, but is of order 1 in units of ξ — much smaller than
> the target r_U1/λ = 3/(4β) ≈ 21. The identification of r_U1 in terms of vortex geometry
> remains the gap.

---

## Motivation: Why the Real Scalar Is Blocked

The derivation chain for the U(1) gauge coupling g² runs:

```
β → f² [kink phase stiffness, PROVED] → r_U1/λ [closure radius, GAP] → g² [holonomy]
```

The phase stiffness of the kink is proved exactly (Cycle 47): the stiffness — the energy
cost per unit squared phase gradient — equals four-thirds times the vacuum field amplitude
squared, divided by the kink half-width.

```
f² = (4/3) φ₀² / ξ    [exact; ∫sech⁴(u) du = 4/3 proved]
```

The holonomy formula then gives: the gauge coupling squared equals two times pi divided
by the dimensionless ratio of the closure fiber radius to the kink width.

```
g² = 2π / (r_U1 / λ)
```

With r_U1/λ = 3/(4β), this gives g² = 8πβ/3, matching the SM to 0.37%.

**The gap:** The identification r_U1/λ = 3/(4β) is motivated dimensionally but not derived
from the field equation. The "closure fiber radius" r_U1 is the radius of the U(1) circle
that the Goldstone phase winds around. For a real scalar φ:
- The field space is ℝ — there is no circle
- The vacuum manifold is {+φ₀, −φ₀} — a two-point set, with no circle
- The holonomy formula has no geometric object to compute it from

The real scalar is structurally blocked from giving a derivable r_U1.

---

## The Extension

The D5 substrate field is extended to a complex scalar:

```
Φ = φ₁ + i φ₂    [complex scalar at D5 depth]
V(|Φ|) = −α/2 |Φ|² + β/4 |Φ|⁴    [V depends only on magnitude; O(2) symmetric]
```

In natural language: the potential energy of the D5 field depends only on the amplitude
of Φ — the distance from zero in the complex plane — through the same double-well form
used for the real substrate. The quadratic coupling α and quartic coupling β are the same
free parameters as before.

The stable vacuum states are all field configurations with amplitude equal to the
equilibrium value: the set of all field values at distance φ₀ = √(α/β) from zero in the
complex plane forms a circle of radius φ₀. This circle is the S¹ vacuum manifold.

```
|Φ₀|² = α/β    →    |Φ₀| = φ₀ = √(α/β)    [vacuum circle, radius φ₀]
```

The symmetry of the vacuum manifold is the group of rotations of a circle — the U(1)
group — which acts on Φ by uniform phase rotation: Φ → e^{iθ}Φ. This is the D5 gauge
symmetry.

---

## What Is Preserved

All structure from the real scalar sector is preserved intact:

**Kink solutions:** The real kink Φ = φ₀ tanh(x/ξ) (with φ₂ = 0) satisfies the complex
scalar field equation exactly. Its energy, width ξ = √(2/α), vacuum amplitude φ₀, and
the BPS-correct energy E_kink = (4/3)c²φ₀²/ξ are all unchanged.

**Longitudinal fluctuation spectrum:** The fluctuation operator L₁ in the φ₁ direction
around the real kink is the PT operator with s = 2 — the same as for the real scalar.
Exactly two bound states: a zero mode at ω² = 0 and a shape mode at ω² = (3/2)α.
The zero mode non-degeneracy theorem (Cycle 73) holds unchanged.

**SU(n) gauge group derivation:** The entire Bottleneck 1 derivation chain
(Cycles 59–74) is preserved. The n zero modes at depth D(4+n), the 2n real DOFs from the
second-order PDE, the complex structure J from the D5 U(1) gauge action, and the
SO(2n) ∩ Aut(J) = U(n) → SU(n) result are all independent of whether the D5 field is
real or complex. The D6 and D7 kinks remain real scalar kinks in their respective
depth sectors.

**Phase stiffness:** f² = (4/3)φ₀²/ξ is unchanged — it is derived from the kink profile
in the longitudinal direction and is unaffected by extending to complex field space.

---

## What Is New

### Field-Space S¹ Vacuum Manifold

The vacuum manifold |Φ| = φ₀ is geometrically a circle in the complex plane, with
circumference 2πφ₀. Every phase value θ ∈ [0, 2π) corresponds to a distinct but
energetically equivalent vacuum configuration Φ₀ = φ₀e^{iθ}. This is the object that
was absent in the real scalar (whose vacuum manifold was just two points) and is
required for a geometrically well-defined holonomy integral.

### D5 Does Not Form Real Kinks

The transverse fluctuation operator L₂ around the real kink Φ = φ₀ tanh(x/ξ) is:

```
L₂ = −∂²/∂x² − α sech²(x/ξ)
```

In natural language: the operator controlling fluctuations in the φ₂ direction around
the real kink is the sum of minus the second spatial derivative and a negative-valued
Pöschl-Teller potential proportional to the squared hyperbolic secant of position divided
by the kink width.

This is a Pöschl-Teller attractive potential with parameter s = 1, since the product
of the well depth and the squared kink width equals two: α × (2/α) = 2 = 1 × (1+1).

The single bound state of this s = 1 PT operator has eigenvalue:

```
ω²₀(L₂) = −α/2    [negative eigenvalue — tachyonic mode]
```

A negative eigenvalue means the real kink is an unstable extremum of the action in the
φ₂ direction: perturbing the real kink slightly in the imaginary-field direction releases
energy. The real kink is a saddle point in the complex scalar field space, not a minimum.

**Structural consequence:** The D5 substrate does not form stable real kinks. The
stable D5 topological defect is the vortex — the configuration Φ_D5 = f(r)e^{inθ} that
winds the phase of the field around a core in the transverse plane. Vortices are
classified by the first homotopy group of the vacuum manifold π₁(S¹) = ℤ, confirming
that D5 admits topological winding-number defects. This is consistent with D5 = U(1)
behavior: a U(1) structure produces vortex defects, not domain walls.

The D6 and D7 kinks are NOT affected: they are kinks of separate depth-sector fields
(φ₆, φ₇) which couple to the D5 condensate as a background. The D6 and D7 kinks do
not experience the tachyonic L₂ mode of the D5 sector.

### Vortex Solution at D5

In the transverse plane to the D5 vortex string, the profile satisfies: the sum of the
second radial derivative, the first radial derivative divided by radius, minus the
winding number squared times the profile divided by the radius squared, plus two times
the profile times one minus the profile squared, equals zero.

```
g''(ρ) + g'(ρ)/ρ − n²g(ρ)/ρ² + 2g(ρ)(1 − g(ρ)²) = 0
```

where ρ = r/ξ is the dimensionless radial coordinate and g(ρ) = f(r)/φ₀ is the
dimensionless vortex amplitude. The boundary conditions are: the profile vanishes at
the vortex core (g(0) = 0) and equals unity in the vacuum (g(∞) = 1).

The numerical solution gives the vortex core radius — the radial distance where the
amplitude reaches 1/√2 — of approximately r_v ≈ 1.1 ξ. This is of order one in
units of the kink width. See `equations/complex_substrate.py` for the full numerical
solution and tabulated profile values.

### Goldstone Photon on the Vortex World-Sheet

When the D5 condensate breaks U(1) → 1, the Goldstone theorem produces a massless
scalar excitation (the Goldstone boson). In the presence of the vortex string, this
Goldstone mode propagates along the vortex world-sheet as a massless spin-1 field —
the photon. The effective action for the phase field θ on the world-sheet is:

```
S_θ = (f²/2) ∫ dt dx (∂_μ θ)²    [massless Goldstone action, phase speed = c]
```

In natural language: the action governing phase fluctuations θ on the D5 vortex
world-sheet equals one-half times the phase stiffness times the integral of the squared
gradient of θ over world-sheet coordinates. The stiffness f² = (4/3)φ₀²/ξ sets the
speed and normalization of phase excitations.

This Goldstone mode is the DFC photon: a massless spin-1 excitation propagating along
the D5 vortex string. Its coupling to D6 kinks (fermions) is the electromagnetic gauge
coupling.

---

## Gap: Identifying r_U1 from the Vortex Geometry

The vortex provides a circle — but which circle is r_U1, and why does its ratio to the
kink width equal 3/(4β)?

From the holonomy formula g² = 2π/(r_U1/λ) and the target g² = 8πβ/3:
```
r_U1/λ = 3/(4β) ≈ 21.4   [for β = 0.035]
```

The vortex core radius r_v ≈ 1.1 ξ = 1.1 λ is of order 1, not 21. So r_U1 ≠ r_v.

The field-space radius φ₀ has r_U1/λ = φ₀/ξ = α/√(2β) — this depends on α, not just β,
and is not equal to 3/(4β) in general. So r_U1 ≠ φ₀ (field-space radius).

The phase stiffness identification: r_U1 = φ₀²/(β × f²) = φ₀² × ξ × 3/(4βφ₀²) = 3ξ/(4β)
gives r_U1/ξ = 3/(4β) — a pure function of β, as required. This is the heuristic step
(Cycle 42) that is motivated but not derived.

**What must be computed to close the gap:** The effective coupling of the D5 Goldstone
phase to a D6 kink, computed from the biquadratic inter-depth coupling V_56. The coupling
integral ∫j_x dx = −2π/(5ξ) (Cycle 67c) gives the charge of the D6 kink in the D5 phase
background. Converting this charge integral to a dimensionless coupling g² requires:

1. Normalizing the photon propagator using the phase stiffness f²
2. Identifying the effective "fiber radius" as the inverse of the charge density
   at the kink center

The computation is: g² = (charge integral)² / (photon normalization × kink normalization).
This is the specific integral that must be evaluated to close Bottleneck 2.

---

## Formal Equations

### Complex scalar field equation

The Euler-Lagrange equation for the D5 complex scalar:

```
∂²Φ/∂t² = c² ∂²Φ/∂x² + αΦ − β|Φ|²Φ
```

In natural language: the second time derivative of the D5 field equals the speed of light
squared times the second spatial derivative, plus the quadratic coupling times the field,
minus the quartic coupling times the squared amplitude times the field.

### Vacuum manifold

The set of stable uniform solutions satisfies |Φ₀|² = α/β. In the complex plane, these
form the circle:

```
S¹ = { Φ ∈ ℂ : |Φ| = φ₀ = √(α/β) }    [U(1) vacuum manifold, radius φ₀]
```

### Transverse fluctuation operator

Around the real kink Φ_kink = φ₀ tanh(x/ξ):

```
L₂ = −∂²/∂x² + V''_⊥    where  V''_⊥ = ∂²V/∂φ₂² |_{φ₂=0} = −α sech²(x/ξ)
```

PT parameter: s(s+1) = α ξ² = α × (2/α) = 2  →  s = 1.
Bound state energy: ω²₀ = −(s/ξ)² = −α/2.

### Vortex profile (dimensionless)

```
g''(ρ) + g'(ρ)/ρ − n²g(ρ)/ρ² + 2g(ρ)(1 − g²(ρ)) = 0
g(0) = 0,  g(∞) = 1,  [g(ρ) ~ ρⁿ near ρ = 0]
ρ = r / ξ,  g = f / φ₀
```

### Phase stiffness and coupling chain

```
f² = (4/3) φ₀² / ξ    [DERIVED, Cycle 47; ∫sech⁴ = 4/3]
g² = 2π / (r_U1/λ)    [holonomy formula; r_U1 from vortex geometry — GAP]
g² = 8πβ/3            [heuristic result, 0.37% match with SM; labeled RIGOROUSLY OPEN]
```

---

## Consistency Checks

| Check | Statement | Status |
|---|---|---|
| Real kink is solution | Φ = φ₀ tanh(x/ξ) satisfies complex scalar EOM | ✓ algebraic |
| Longitudinal PT spectrum | L₁ has s=2, ω²₀=0 (zero mode), ω²₁=(3/2)α | ✓ Cycle 73 numerical |
| Transverse PT parameter | s(s+1) = αξ² = 2 → s=1 | ✓ algebraic |
| Transverse bound state tachyonic | ω²₀(L₂) = −α/2 < 0 | ✓ numerical (complex_substrate.py) |
| Vortex profile solves ODE | g(ρ) from BVP: g(0)=0, g(∞)=1 | ✓ numerical |
| Vortex core radius | r_v ≈ 1.1 ξ (Cycle 75 BVP solution) | ✓ numerical |
| r_v ≠ r_U1 | r_v/ξ ≈ 1.1 ≪ 3/(4β) ≈ 21.4 | ✗ Gap confirmed — r_U1 not from vortex core |
| g² = 8πβ/3 from field equation | Requires derivation of r_U1/λ = 3/(4β) from D5-D6 coupling | ✗ OPEN |

---

## Open Questions

1. **Derive r_U1 from the D5-D6 coupling integral:** The charge of the D6 kink in the D5
   background is ∫j_x dx = −2π/(5ξ) (Cycle 67c). The photon propagator normalization
   involves f². Compute g² = (∫j_x dx)² × (photon normalization)⁻¹ × (kink normalization)⁻¹
   and check whether this equals 8πβ/3. This is the primary Bottleneck 2 computation.

2. **KK reduction on the field-space S¹:** The field-space S¹ at radius φ₀ now exists
   geometrically. Treat the phase θ of the D5 condensate as a compact Kaluza-Klein
   coordinate and reduce the D5 action on this circle. Identify the effective 1D gauge
   coupling e² from the 2D action S ~ f²∫(∂θ)². Compute e²  in terms of φ₀ and β.

3. **Kink stability in the compressed D5 sector:** The real kink (if it forms during
   compression) is a saddle point, not a minimum. Verify that at compression scales
   L ~ ξ, the energy of the "soft" (around-the-circle) escape path exceeds E_kink,
   so that the compression-stabilized kink is metastable during the cascade.

4. **Extend to D6/D7:** If D5 is complex (V_D5 = −α/2|Φ|² + β/4|Φ|⁴), D6 and D7
   may also benefit from complex field descriptions with higher-winding vortices
   (n=2 at D6 for SU(2), n=3 at D7 for SU(3)). Examine whether the Bottleneck 1
   results (Cycles 59–74) are reproduced by this picture or require modification.

---

## Connections

- `foundations/phase_stiffness_derivation.md` — f² = (4/3)φ₀²/ξ proved; gap precisely located (Cycle 47)
- `foundations/coupling_derivation.md` — g² = 8πβ/3 heuristic derivation chain (Cycle 42)
- `equations/complex_structure_derivation.py` — D6 kink charge in D5 background (Cycle 67c)
- `equations/complex_substrate.py` — vortex profile, tachyonic L₂ mode, coupling candidates (Cycle 75)
- `foundations/d5_complex_structure.md` — D5 U(1) complex structure from gauge action (Cycle 71)
- `foundations/complex_zero_mode_gap.md` — SO(2n)∩Aut(J)=U(n) derivation (Cycle 70)
- `foundations/hopf_fibration_geometry.md` — Hopf S¹/S³/S⁵ correspondence at D5/D6/D7 (Cycle 42)
- `foundations/threshold_nondegeneracy.md` — PT s=2 unique zero mode (Cycle 73)
- `foundations/zero_mode_multiplet.md` — n complex modes → SU(n) (Cycle 59)
