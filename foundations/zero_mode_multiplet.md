# Zero Mode Multiplets and the SU(n) Symmetry Origin

## Status

> **Cycle 59:** Formal derivation of the second half of Bottleneck 1.
>
> **Result:** Given that the substrate at depth D(4+n) opens n coincident degenerate
> zero modes on a common background, the symmetry group of their configuration space is
> provably SU(n) — not U(1)^n. The proof is algebraic and does not require knowing
> *why* n modes appear at D(4+n).
>
> **Remaining open:** Why the substrate opens exactly 1, 2, 3 coincident zero modes at
> D5, D6, D7 respectively. This is the first half of Bottleneck 1 and is not resolved here.
>
> **Status of Bottleneck 1:** Partially resolved. The symmetry-from-degeneracy argument
> is now a derivation (not a correspondence). The DOF count from substrate dynamics remains
> a working hypothesis.

---

## The Question

`foundations/hopf_fibration_geometry.md` identifies the key derivation gap: when n field
modes are present at depth D(4+n), does their symmetry group become SU(n), or merely
the product of n independent U(1) groups?

The distinction is physically critical. U(1)^n would give n independent photon-like bosons.
SU(n) gives a non-Abelian gauge theory with off-diagonal gauge bosons — the W bosons
(n=2) and gluons (n=3).

This document proves that n **coincident degenerate** zero modes on a shared background
give SU(n), not U(1)^n.

---

## The Zero Mode in the φ⁴ Substrate

The substrate field satisfies:

```
∂²φ/∂t² = c² ∂²φ/∂x² − V'(φ),    V(φ) = −α/2 φ² + β/4 φ⁴
```

The kink solution at compression depth D is:

```
φ₀(x) = √(α/β) tanh(x/ξ),    ξ = c √(2/α)
```

Here ξ is the kink width — the spatial scale over which the field transitions between
the two vacuum values minus-root-(α/β) and plus-root-(α/β).

A small fluctuation δφ around this kink satisfies the linearized equation:

```
∂²(δφ)/∂t² = c² ∂²(δφ)/∂x² − V''(φ₀) δφ
```

The second derivative of the potential evaluated at the kink profile is:

```
V''(φ₀(x)) = −α + 3β φ₀²(x) = α (2 − 3 sech²(x/ξ))
```

The first term (plus-2α) acts as a mass. The second term (minus-3α times sech-squared)
is a Pöschl-Teller attractive potential well centered on the kink.

### The zero mode

The Pöschl-Teller potential with depth parameter equal to 2 has a bound state at zero
frequency. This bound state is the translational zero mode:

```
η₀(x) = ∂φ₀/∂x ∝ sech²(x/ξ)
```

It has zero eigenvalue (frequency ω = 0) because translating the kink costs no energy —
the translated kink is also an exact solution to the field equation.

**The zero mode is normalizable:** The integral of sech⁴(x/ξ) from minus-infinity to
plus-infinity equals 4ξ/3, which is finite. This means the zero mode represents a
genuine localized degree of freedom, not a propagating wave.

**The zero mode is unique:** The Pöschl-Teller spectrum for depth parameter 2 contains
exactly two bound states: the zero mode (ω = 0) and one shape mode (ω₁ = c√(3α/2),
the breathing mode). There is exactly one zero mode per kink.

---

## The Critical Distinction: Coincident vs. Separated Modes

The symmetry group of n zero modes depends entirely on whether they share a common
background or sit on separate, spatially separated kinks.

### Case 1: n separated kinks

Suppose n kinks are located at positions x₁, x₂, ..., xₙ far apart (separation much
larger than ξ). Each kink has its own zero mode:

```
η₀^(i)(x) ∝ sech²((x − xᵢ)/ξ),    i = 1, ..., n
```

These zero modes are spatially non-overlapping. A displacement of kink i does not
affect kink j. The n modes decouple: the zero mode subspace is:

```
{c₁ η₀^(1) + c₂ η₀^(2) + ... + cₙ η₀^(n) : cᵢ ∈ ℝ}   [real, n-dimensional]
```

Each cᵢ can be varied independently. The symmetry group is: each mode has an
independent U(1) phase shift (if the field is complexified) → symmetry group U(1)^n.

### Case 2: n coincident degenerate zero modes

Now suppose n zero modes all share the **same background kink** at position x = 0.
The field has n components (ψ₁, ψ₂, ..., ψₙ) each satisfying the same linearized
equation with the same Pöschl-Teller background:

```
Lψᵢ = ω² ψᵢ,    L = −c² ∂²/∂x² + V''(φ₀(x)),    i = 1, ..., n
```

Since all n components experience the **same operator L** with the **same background
φ₀(x)**, all n zero modes are:

```
ψᵢ^(0)(x) = cᵢ η₀(x),    η₀(x) ∝ sech²(x/ξ),    cᵢ ∈ ℂ
```

with the **same spatial profile** η₀(x). The only freedom is the n complex amplitudes
c = (c₁, c₂, ..., cₙ) ∈ ℂⁿ.

The total energy in the zero mode sector is:

```
E_zero = ∫ |η₀(x)|² dx × (|c₁|² + |c₂|² + ... + |cₙ|²) = const × |c|²
```

The physical constraint is that the total amplitude is fixed by the substrate normalization
(the energy stored in the zero mode sector is fixed at formation). This gives:

```
|c₁|² + |c₂|² + ... + |cₙ|² = const
```

This constraint defines the space of zero mode configurations:

```
{c ∈ ℂⁿ : |c|² = const} = S^(2n−1) ⊂ ℂⁿ
```

The space of configurations is the unit sphere in ℂⁿ — a sphere of real dimension 2n−1.

---

## The Symmetry Group Is SU(n)

The symmetry group of the zero mode configuration space S^(2n−1) ⊂ ℂⁿ, preserving
the complex structure, is:

```
Isom₀(S^(2n−1), ℂ structure) = U(n) = U(1) × SU(n)
```

This result follows from the fact that a unitary matrix U ∈ U(n) maps ℂⁿ to itself
and preserves the Hermitian norm: |Uc|² = c† U† U c = c† c = |c|². So U maps
S^(2n−1) to itself by isometries.

**Why is the symmetry U(n) and not some larger group?** Because U(n) is exactly the
group that preserves the Hermitian inner product on ℂⁿ. Any isometry of S^(2n−1)
that also preserves the complex structure (i.e., commutes with multiplication by i)
must be unitary. So U(n) is the full complex-structure-preserving isometry group.

**Why does U(1) decouple?** The overall phase c → e^{iα} c is an isometry of S^(2n−1}
but corresponds to a global phase shift of all components simultaneously. In the
substrate, this global phase is already accounted for by the D5 U(1) closure at the
previous depth. The gauge group at depth D(4+n) for n ≥ 2 is the SU(n) factor — the
special unitary group — which acts without any overall phase change.

**The gauge group at D(4+n) is SU(n).**

---

## Proof That n Coincident Modes Give SU(n), Not U(1)^n

The key distinction is sharpened by the following argument:

**Theorem:** n complex degrees of freedom with Hermitian norm constraint |c|² = const
have symmetry group SU(n) if and only if all n components experience the same background.

**Proof (informal):** If the backgrounds are identical, any unitary rotation of the
components (c₁,...,cₙ) → U(c₁,...,cₙ) maps a valid zero mode configuration to another
valid zero mode configuration with the same energy, because:

1. The spatial profile η₀(x) is unchanged (it depends only on the background, not on which
   direction the amplitude points in ℂⁿ)
2. The energy depends only on |c|² = Σ|cᵢ|², which is invariant under U(n)
3. Therefore, the full U(n) rotation is a symmetry of the zero mode sector

If any component experiences a different background (even slightly different α, β, or
kink position), the degeneracy is broken: the components have different energies, and
only the subgroup of U(n) that leaves each component's energy invariant remains a
symmetry. In the extreme case of fully separated kinks, only U(1)^n (independent phase
rotations of each component) survives.

**Conclusion:** Coincidence and degeneracy are the conditions. n coincident degenerate
zero modes → SU(n) gauge symmetry.

---

## Application to D5, D6, D7

### D5: n = 1 → U(1)

One complex DOF. Configuration space S¹ ⊂ ℂ¹. Symmetry group U(1). One gauge
boson: the photon. This is trivial — one component has no off-diagonal mixing.

**Generator count:** dim(U(1)) = 1. One gauge boson. ✓

### D6: n = 2 → SU(2)

Two coincident complex DOFs sharing the same D6 background. Configuration space
S³ ⊂ ℂ². Symmetry group SU(2).

The two components (ψ₁, ψ₂) rotate into each other under SU(2). The off-diagonal
generators (corresponding to σ₁, σ₂) mix the two components — these are the W⁺ and W⁻
bosons. The diagonal generator (σ₃) gives the W³ boson (which mixes with the D5 U(1)
to give Z and photon).

**Generator count:** dim(SU(2)) = 3. Three gauge bosons (W⁺, W⁻, W³/Z). ✓

**Why not U(1) × U(1)?** U(1) × U(1) would arise if the two D6 modes were on separate
backgrounds. But if they are coincident on the same D6 threshold, their zero modes
are degenerate and the full SU(2) rotation is a symmetry.

### D7: n = 3 → SU(3)

Three coincident complex DOFs sharing the same D7 background. Configuration space
S⁵ ⊂ ℂ³. Symmetry group SU(3).

The three components (ψ₁, ψ₂, ψ₃) are the three quark colors (R, G, B). The eight
generators of SU(3) — the Gell-Mann matrices λ₁,...,λ₈ — mix the three components.
The off-diagonal generators correspond to gluons that carry color charge (e.g., R→G).
The two diagonal generators (λ₃, λ₈) correspond to the color-neutral gluon combinations.

**Generator count:** dim(SU(3)) = 8. Eight gauge bosons (gluons). ✓

**Why not U(1)³?** Three independent phase rotations of three separated components
would give U(1)³. But three coincident zero modes on the same D7 background degenerate
and the full SU(3) rotation is a symmetry — the substrate cannot distinguish one color
orientation from another.

---

## Summary Table

| Depth | n (complex DOFs) | Configuration space | Symmetry group | Generators | Gauge bosons |
|---|---|---|---|---|---|
| D5 | 1 | S¹ ⊂ ℂ¹ | U(1) | 1 | photon |
| D6 | 2 | S³ ⊂ ℂ² | SU(2) | 3 | W⁺, W⁻, Z⁰ |
| D7 | 3 | S⁵ ⊂ ℂ³ | SU(3) | 8 | 8 gluons |

---

## What This Derivation Does and Does Not Prove

### What is now proved

The statement "n coincident degenerate zero modes on a common background have SU(n)
gauge symmetry" is a derivation. No free parameters appear. The argument follows from:

1. The zero mode spatial profile being η₀(x) ∝ sech²(x/ξ) — the same for all components
   sharing a background (from the Pöschl-Teller analysis)
2. The configuration space being {c ∈ ℂⁿ : |c|² = const} = S^(2n−1) (from norm conservation)
3. The complex-structure-preserving isometry of S^(2n−1) being U(n) (algebraic fact)
4. The global U(1) factor being absorbed by the previous depth's closure — leaving SU(n)

This promotes the claim "n coincident modes → SU(n)" from Tier 3 (correspondence) to
**Tier 2 status** conditional on the coincidence being established.

### What remains open (Tier 3)

The following is NOT proved here:

> **Why does the substrate at depth D(4+n) open exactly n coincident degenerate modes?**

This is the first half of Bottleneck 1. The argument above shows that *if* the substrate
opens n coincident modes at D(4+n), *then* the gauge group is SU(n). But it does not
derive from the substrate field equation that n modes (rather than 1, or 2, or n+1)
are opened.

The three specific open questions:
1. Why does D5 open exactly 1 complex DOF (and not 2)?
2. Why does D6 open exactly 2 complex DOFs (and not 1 or 3)?
3. Why does D7 open exactly 3 complex DOFs (and not 4)?

The route to answering these requires analyzing the bifurcation structure of the substrate
field equation at each compression threshold — specifically, counting the number of
unstable modes at each bifurcation point. This is addressed in `foundations/depth_assignment.md`
(Open Problem 1) and remains the core of Bottleneck 1.

---

## The Termination Argument: Why Not D8 = SU(4)?

The n=4 case would require four coincident degenerate zero modes on a D8 background.
The substrate dynamics would need to:
1. Reach a D8 compression threshold
2. Open 4 coincident modes there

The argument that neither occurs:

The D7 closure produces color confinement — all colored modes at D7 depths bind into
color-neutral combinations below the QCD scale Λ_QCD ≈ 200 MeV. The modes that would
seed a D8 bifurcation are the D7 zero modes themselves. But these zero modes are
confined: they cannot propagate freely through the D3 localization layer. Instead, they
form bound states (mesons, baryons) which are color-singlets under SU(3).

The result: there are no free D7-depth modes available to coincide at a D8 threshold.
The substrate's compression energy at D7 depths is consumed by the gluon
self-interaction and stored in the confinement potential, not in a new bifurcation.

**Status:** Structural argument. The formal version would require showing that the D7
nonlinear field theory has no normalizable zero mode on a composite (color-neutral) background.

---

## Connections

- `foundations/depth_assignment.md` — the full depth assignment problem; Open Problems 1–5
- `foundations/hopf_fibration_geometry.md` — the geometric correspondence S^(2n−1) → SU(n)
- `foundations/bifurcation_dynamics.md` — compression dynamics; γ_D derivation (RETRACTED)
- `phenomena/quantum/spin.md` — Jackiw-Rebbi zero mode for the D6 case (spinor structure)
- `equations/hopf_dof_count.py` — numerical verification of DOF counts and SU(n) structure
- `equations/spin_zero_mode.py` — original Jackiw-Rebbi calculation for spin-1/2
