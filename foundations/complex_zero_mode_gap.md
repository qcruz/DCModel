# Foundation: Complex Zero Mode Gap — Why the Real Substrate Produces U(1), SU(2), SU(3)

## Status

> **Cycle 70:** Formalizes the Bottleneck 1 Tier 3 remaining gap.
>
> **Result:** The second-order substrate field equation gives each zero mode TWO real
> degrees of freedom — initial position and initial velocity along the zero mode direction.
> For n coincident kinks at the same depth, this gives 2n real DOFs and configuration
> space S^(2n-1), whose real isometry group is SO(2n). The SO(2) = U(1) coincidence at
> D5 (n=1) means the real substrate alone produces U(1) without needing complex structure.
> For D6 (n=2) and D7 (n=3), the real isometry is SO(4) ≅ SU(2)×SU(2) and SO(6) ≅ SU(4)
> — both larger than SU(2) and SU(3). The D5 background provides the complex structure
> that reduces SO(2n) → U(n) → SU(n) at D6/D7.
>
> **Tier 3 gap remaining:** Formally derive that the D5 U(1) background provides a complex
> structure J satisfying J² = −I on the D6/D7 zero mode spaces. This is the final step to
> promote D5=U(1) and D6=SU(2) from Tier 3 to Tier 2.
>
> **Relationship to prior results:** The zero_mode_multiplet.md proof (Cycle 59) assumed
> n complex modes giving S^(2n-1) ⊂ ℂⁿ. This document explains where those complex modes
> come from: pairing of position and velocity DOFs at each threshold, organized by the D5
> complex structure at D6/D7.

---

## The Gap Stated Precisely

The substrate potential is the double-well form: the potential energy as a function of
field amplitude equals negative one-half times the quadratic coupling times the amplitude
squared, plus one-quarter times the quartic coupling times the amplitude to the fourth
power. This is a real scalar field theory. Its kink solution and zero mode are both
real-valued functions.

```
V(φ) = −α/2 φ² + β/4 φ⁴
φ₀(x) = √(α/β) tanh(x/ξ),     ξ = c√(2/α)
η₀(x) = ∂φ₀/∂x ∝ sech²(x/ξ)  [real, normalizable]
```

The zero_mode_multiplet.md proof (Cycle 59) establishes: n coincident complex zero modes
→ configuration space S^(2n-1) ⊂ ℂⁿ → SU(n) gauge group.

**The gap:** The substrate is real. Real zero modes span a real vector space. n real
zero modes give configuration space S^(n-1) ⊂ ℝⁿ with SO(n) isometry — not SU(n).

For n = 1, 2, 3 this gives:

| n | Real config space | Real isometry | Wanted | Match? |
|---|---|---|---|---|
| 1 (D5) | S⁰ ⊂ ℝ¹ | SO(1) = trivial | U(1) | ✗ |
| 2 (D6) | S¹ ⊂ ℝ² | SO(2) = U(1) | SU(2) | ✗ |
| 3 (D7) | S² ⊂ ℝ³ | SO(3) ≅ SU(2)/Z₂ | SU(3) | ✗ |

**Resolution:** The substrate equation is second-order in time. A zero-frequency mode has
two independent initial data — initial displacement and initial velocity along the zero
mode direction. This pairs each single spatial zero mode with a time-evolution DOF,
doubling the mode count. Accounting for this pairing:

| n kinks | Total real DOFs | Config space | Real isometry |
|---|---|---|---|
| 1 (D5) | 2 | S¹ ⊂ ℝ² | SO(2) = U(1) ✓ |
| 2 (D6) | 4 | S³ ⊂ ℝ⁴ | SO(4) ≅ SU(2)×SU(2) ✗ |
| 3 (D7) | 6 | S⁵ ⊂ ℝ⁶ | SO(6) ≅ SU(4) ✗ |

**At D5 (n=1): SO(2) = U(1) exactly.** The real and complex pictures coincide. The real
substrate alone gives U(1) at D5.

**At D6/D7:** The real isometry is too large. The D5 complex structure reduces it.

---

## The Two-DOF Mechanism: Second-Order Time Evolution

The substrate field equation is second-order in time:

```
∂²φ/∂t² = c² ∂²φ/∂x² − V'(φ)
```

A field fluctuation around the kink background takes the form δφ(x,t) = A(t) η₀(x),
where η₀(x) is the zero mode profile. Substituting into the linearized equation and using
Lη₀ = 0 (zero mode condition), the amplitude A(t) satisfies:

```
Ä(t) = 0    →    A(t) = v₀ t + q₀
```

Here q₀ is the initial displacement along the zero mode direction (the kink's position
offset) and v₀ is the initial velocity along the zero mode (the kink's initial speed).
Both are continuous free parameters — both are zero-frequency (zero-energy-cost) motions.

The initial data space for the zero mode subsystem is the two-dimensional real vector space
with coordinates (q₀, v₀). Restricting to states of fixed norm (fixed total excitation
amplitude) gives the unit circle in this plane. The unit circle is the one-dimensional
sphere S¹, and its symmetry group — the group of rigid rotations that preserve the
circle — is SO(2).

Since SO(2) is the same Lie group as U(1) (both are the group of rotations of a circle,
with one real angular parameter), the D5 gauge group U(1) is precisely the symmetry of the
zero mode's initial data space. No complex structure is required for this identification.

**Summary of D5 derivation:**
1. Substrate field equation is second-order → zero mode has 2 real DOFs: (position, velocity)
2. Unit-norm constraint on these 2 DOFs → S¹
3. Symmetry group of S¹ as a real manifold → SO(2)
4. SO(2) = U(1) as Lie groups (both have one-dimensional abelian Lie algebra)
5. Therefore D5 gauge group = U(1) ✓ — derived from the substrate without complex structure

---

## Why D6 Cannot Use the Same Logic: SO(4) ≠ SU(2)

At D6, two coincident kinks share the same background. The total zero mode initial data
space is four-dimensional: two independent zero modes, each with position and velocity.
The space is ℝ⁴ with coordinates (q₁, v₁, q₂, v₂). Restricting to unit norm gives S³ ⊂ ℝ⁴.

The symmetry group of S³ as a real oriented Riemannian manifold is SO(4). The Lie algebra
so(4) has dimension six (four-dimensional anti-symmetric matrices: 4×3/2 = 6 generators).
The Lie algebra su(2) has dimension three.

Since the symmetry groups have different dimensions, SO(4) and SU(2) are distinct:

```
dim(SO(4)) = 6  ≠  dim(SU(2)) = 3
```

The full isometry group SO(4) decomposes as a direct product of two SU(2) groups:

```
so(4) ≅ su(2)_L ⊕ su(2)_R    [as Lie algebras]
```

This decomposition — which has a left-handed and a right-handed factor — is verified
numerically in `equations/u1_from_paired_modes.py` (error < 10⁻¹⁵).

Without additional structure, neither su(2)_L nor su(2)_R is preferred. To obtain exactly
SU(2) as the gauge group, the substrate must select one of the two three-dimensional
subgroups from the six-dimensional SO(4) isometry. The mechanism that does this is the
complex structure inherited from the D5 U(1) gauge field.

---

## Complex Structure from the D5 Background

The D5 U(1) gauge group acts on all charged fields as multiplication by a phase e^(iθ).
A field coupled to the D5 U(1) gauge field must be described by a complex number (or
complex vector), because the phase rotation mixes real and imaginary components.

The D6 zero modes carry U(1) charge (the D6 electron has charge −e, established by the
Jackiw-Rebbi construction and the SU(2) doublet structure). Because they carry U(1) charge,
their configuration space must support U(1) phase rotation. This means the four real DOFs
(q₁, v₁, q₂, v₂) must be organized into two complex DOFs:

```
z₁ = q₁ + i v₁     (first zero mode: position + i × velocity)
z₂ = q₂ + i v₂     (second zero mode: position + i × velocity)
```

The pairing (q_k, v_k) → z_k = q_k + i v_k is precisely the complex structure J on ℝ⁴:

```
J: ℝ⁴ → ℝ⁴,    J(q₁, v₁, q₂, v₂) = (−v₁, q₁, −v₂, q₂),    J² = −I
```

With this complex structure, the symmetry group is reduced from SO(4) to the subgroup of
SO(4) that commutes with J — the complex-linear isometries. This subgroup is U(2):

```
SO(4) ∩ Aut(J) = U(2) ≅ U(1) × SU(2)
```

The U(1) factor in U(2) is the overall phase rotation (acting identically on both modes).
This U(1) is the same as the D5 gauge U(1) — it is already accounted for. The remaining
symmetry acting on the D6 modes alone is SU(2). This is the D6 gauge group.

The pairing q_k + i v_k is natural: position and velocity along the zero mode are
conjugate variables (they are the zero-mode sector of the canonical phase space).
In the Hamiltonian formulation with canonical momentum π₀ = v₀, the zero mode
coordinate and its conjugate momentum pair to form the complex variable of the
symplectic structure. The D5 U(1) gauge symmetry selects this symplectic pairing
as the relevant complex structure.

---

## The Complete Cascade Picture

Applying this mechanism at each depth:

```
D5 (n=1 kink):
  2 real DOFs (q, v) → S¹ ⊂ ℝ² → SO(2) = U(1)
  No complex structure needed.
  D5 gauge group = U(1)  ✓

D6 (n=2 kinks):
  4 real DOFs (q₁,v₁,q₂,v₂) → S³ ⊂ ℝ⁴ → SO(4) ≅ SU(2)×SU(2) [real]
  + D5 complex structure J → SO(4) ∩ Aut(J) = U(2) ≅ U(1)×SU(2)
  D5 U(1) factor already gauged → residual D6 gauge group = SU(2)  ✓

D7 (n=3 kinks):
  6 real DOFs (q₁,v₁,q₂,v₂,q₃,v₃) → S⁵ ⊂ ℝ⁶ → SO(6) ≅ SU(4) [real]
  + D5 complex structure J → SO(6) ∩ Aut(J) = U(3) ≅ U(1)×SU(3)
  D5 U(1) factor already gauged → residual D7 gauge group = SU(3)  ✓
```

The gauge boson counts follow immediately:

```
D5: dim(U(1)) = 1 → 1 photon  ✓
D6: dim(SU(2)) = 3 → 3 weak bosons (W⁺, W⁻, Z⁰ before EWSB)  ✓
D7: dim(SU(3)) = 8 → 8 gluons  ✓
```

---

## Consistency with Prior Results

This picture is consistent with and extends the prior Bottleneck 1 work:

**Cycles 66–67c (bifurcation_mode_count.md, complex_structure_derivation.py):** Proved
that scalar coupling between D5 and D6 lifts zero modes (reduces n), while gauge coupling
preserves n independent zero modes. The current document explains why gauge coupling
is the appropriate inter-depth coupling: the D5 U(1) gauge field acts on the D6 modes
as a U(1) phase rotation, which is the source of the complex structure J.

**Cycle 59 (zero_mode_multiplet.md):** Proved that n complex zero modes sharing a
background give SU(n). The current document provides the physical origin of the complex
structure that makes those n real mode pairs behave as n complex modes.

**Cycles 62–63 (bifurcation_mode_count.md, coupled_fluctuation.py):** Proved that n
independent kinks at the same depth have n coincident degenerate zero modes. The
current document adds that each zero mode carries 2 real DOFs from the second-order PDE,
giving 2n real DOFs total — matching the S^(2n-1) geometry of zero_mode_multiplet.md.

---

## Formal Equations

### Zero mode initial data space

The zero mode amplitude A(t) satisfies Ä = 0 with general solution:

```
A(t) = q₀ + v₀ t

where:
  q₀ = A(0) = initial position displacement along zero mode
  v₀ = dA/dt|_{t=0} = initial velocity along zero mode
```

The zero mode initial data forms the real plane ℝ². After restricting to unit total
action (∫ dτ [½v₀² + ½ω₀²q₀²] = const at ω₀→0), the normalized data lies on:

```
S¹ = {(q₀, v₀) ∈ ℝ² : q₀² + v₀² = 1}
```

### SO(2n) ∩ Aut(J) = U(n)

Given the real space ℝ^(2n) with orthonormal basis (q₁, v₁, q₂, v₂, ..., qₙ, vₙ),
the standard complex structure is the linear map:

```
J(qₖ) = vₖ,    J(vₖ) = −qₖ,    for k = 1, ..., n
J² = −I
```

The subgroup of SO(2n) that commutes with J consists of all real orthogonal
transformations that also preserve the complex structure — the unitary group U(n):

```
SO(2n) ∩ {M : MJ = JM} = U(n) ≅ U(1) × SU(n)
```

**Dimension count:**
```
dim(SO(2n)) = n(2n−1)
dim(U(n))   = n²
dim(SU(n))  = n² − 1
```

Verified for n = 1, 2, 3 in `equations/u1_from_paired_modes.py`.

### Lie algebra decompositions

```
n=1: so(2) ≅ u(1)          [both 1-dimensional, abelian]
n=2: so(4) ≅ su(2) ⊕ su(2) [6-dimensional; complex structure selects one su(2) ⊕ u(1) = u(2)]
n=3: so(6) ≅ su(4)          [15-dimensional; complex structure selects su(3) ⊕ u(1) = u(3)]
```

---

## Consistency Checks

| Check | Statement | Status |
|---|---|---|
| SO(2) = U(1) as Lie groups | dim(so(2)) = dim(u(1)) = 1; both abelian; isomorphic | ✓ verified (u1_from_paired_modes.py) |
| SO(4) ≠ SU(2): dimension mismatch | dim(so(4)) = 6, dim(su(2)) = 3 | ✓ verified |
| so(4) ≅ su(2)_L ⊕ su(2)_R | Explicit generator decomposition; commutation table checked | ✓ verified (error < 10⁻¹⁵) |
| SO(4) ∩ Aut(J) = U(2): dim 4 | u(2) = u(1) ⊕ su(2); complex-linear subgroup of SO(4) | ✓ verified |
| SO(6) ∩ Aut(J) = U(3): dim 9 | u(3) = u(1) ⊕ su(3); dim 9 ✓ | ✓ verified |
| Gauge boson counts from SU(n) | 1, 3, 8 for n=1,2,3 matching photon/W-Z/gluon | ✓ structural (Cycle 59) |
| D5 U(1) provides J: formal proof | That the D5 gauge field defines J on D6/D7 zero mode space | ✗ OPEN — Tier 3 gap |

---

## Open Questions

1. **Formal proof that D5 U(1) defines J on D6 zero mode space:** The structural argument
   is: D6 modes carry U(1) charge → their configuration must be complex → J is defined by
   the phase rotation. Making this rigorous requires computing the D5 gauge field coupling
   to the D6 zero mode fluctuations and showing it is exactly the complex structure J.
   Approach: Write the coupled D5+D6 field equations; compute the zero mode wavefunction
   in the D5 gauge background (as started in complex_structure_derivation.py, Cycle 67c);
   show the U(1) phase acts as J on the D6 mode space.

2. **Why does the second-order PDE pair (q, v) rather than producing independent modes?**
   In the Hamiltonian formulation, q and v = π (canonical momentum) are conjugate. The
   symplectic form Ω(q,v) = dq∧dv is preserved by time evolution. The connection between
   the symplectic pairing and the complex structure J is: Ω(·, J·) = ⟨·,·⟩ (the inner
   product). This identifies the complex structure with the symplectic structure on the
   zero mode phase space. A derivation would connect the Darboux theorem for the zero
   mode subsystem to the U(1) complex structure.

3. **Termination at n=3:** After SU(3) forms at D7, why is there no D8? The confinement
   argument (isolated D7 winding is topologically forbidden) prevents free DOFs from
   forming at D8. A quantitative version requires computing the D7 self-energy integral
   and showing it diverges faster than any finite-action D8 mode.

---

## Connections

- `foundations/zero_mode_multiplet.md` — proves n complex modes → SU(n) (Cycle 59)
- `foundations/bifurcation_mode_count.md` — maps the full Bottleneck 1 gap (Cycles 62–67c)
- `equations/complex_structure_derivation.py` — D5 half-vortex makes D6 kink complex (Cycle 67c)
- `equations/u1_from_paired_modes.py` — numerical verification of SO(2n)/U(n) results (Cycle 70)
- `equations/coupled_fluctuation.py` — n independent kinks → n degenerate zero modes (Cycle 63)
- `equations/gauge_coupling_zero_modes.py` — gauge coupling preserves n zero modes (Cycle 67)
- `foundations/hopf_fibration_geometry.md` — S¹/S³/S⁵ Hopf correspondence (Cycle 42)
- `foundations/depth_assignment.md` — Bottleneck 1 full map
