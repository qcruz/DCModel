# Foundation: Bifurcation Mode Count — Why D(4+n) Opens Exactly n Modes

## One-Sentence Summary

> At each compression threshold D(4+k), the substrate's bifurcation opens exactly one new
> complex degree of freedom; after n thresholds the accumulated configuration space is
> S^(2n-1) ⊂ ℂⁿ with SU(n) isometry — but the claim that each threshold adds exactly one
> complex (rather than one real) DOF is a structural argument, not yet a derivation from
> the substrate field equation.

---

## Status

This document maps the **first half of Bottleneck 1** — the open problem identified in
`foundations/depth_assignment.md`. The second half (n coincident degenerate zero modes →
SU(n)) was proved in `foundations/zero_mode_multiplet.md` (Cycle 59). The first half
remains open as of Cycle 62.

**What is proved:**
- The φ⁴ kink has exactly one zero mode (Pöschl-Teller uniqueness; Cycle 59)
- n coincident degenerate zero modes → configuration space S^(2n-1) → SU(n) (Cycle 59)
- The U(1), SU(2), SU(3) gauge groups require n = 1, 2, 3 coincident modes respectively

**What is not yet proved:**
- Why D(4+n) opens exactly n coincident modes from the substrate field equation
- Why each bifurcation adds one COMPLEX degree of freedom (2 real DOFs) rather than one real DOF (1 real DOF)
- Why the series terminates at n = 3 (the SU(3) confinement argument is stated but not derived)

---

## The Open Problem

The substrate undergoes a compression cascade: D1 → D2 → D3 → D4 → D5 → D6 → D7.
At each threshold D(4+k) for k = 1, 2, 3, a new gauge structure appears:

```
D5 threshold: 1 coincident zero mode → configuration space S¹ → U(1) gauge group
D6 threshold: 2 coincident zero modes → configuration space S³ → SU(2) gauge group
D7 threshold: 3 coincident zero modes → configuration space S⁵ → SU(3) gauge group
```

Given that the second half is proved — the n modes → SU(n) chain — the open question is:

**Why does the D(4+k) threshold open exactly k modes in total (not k−1 or k+1)?**

Equivalently: Why does each successive bifurcation add exactly one new zero mode?

---

## Candidate Mechanism: One-Codimension Bifurcation Theorem

A standard result in bifurcation theory is that a codimension-1 bifurcation — the crossing
of a single control parameter through a threshold — introduces exactly one new unstable
mode. For the DFC substrate, each depth threshold corresponds to a single bifurcation event:
the compression parameter α crosses a critical value at which V''(φ=0) passes through zero.

The substrate potential is the double-well form: the potential energy equals negative
one-half times the quadratic coupling times the field squared, plus one-quarter times the
quartic coupling times the field to the fourth power. At the bifurcation threshold, the
quadratic coefficient changes sign. The linearized fluctuation equation around the
transition point has exactly one mode with vanishing frequency squared — the incipient
zero mode.

```
Substrate potential:    V(φ) = −α/2 φ² + β/4 φ⁴
Threshold condition:    α = 0   (or α → 0⁺ from below)
Fluctuation operator:   L = −∂²_x + V''(φ) = −∂²_x − α
At threshold (α=0):     L = −∂²_x  (flat potential — one zero mode)
```

By codimension-1 bifurcation theory: a single threshold crossing introduces exactly one
new flat direction (zero eigenvalue of L). Each depth transition D(4+k-1) → D(4+k)
crosses one such threshold, adding one new unstable mode.

**Accumulated count:** After n threshold crossings (D4 → D(4+n)), the total number of
accumulated flat directions is n. If all n modes are coincident (same substrate depth,
same background), the configuration space is S^(2n-1) → SU(n).

**What this argument establishes:** That n consecutive codimension-1 bifurcations give n
soft modes total. This is the structural core of the mode count.

**What this argument does not establish:** Why n modes from n real codimension-1 thresholds
end up as n COMPLEX modes (S^(2n-1) ⊂ ℂⁿ rather than S^(n-1) ⊂ ℝⁿ). A sequence of n
real codimension-1 bifurcations gives an n-dimensional real configuration space (S^(n-1)),
not S^(2n-1). The complex structure requires additional input.

---

## The Complex Structure Gap

The S^(2n-1) configuration space requires that each mode direction is complex — that the
substrate's configuration space at each threshold has a natural U(1) fiber structure.
The candidate source of this complex structure is the D5 U(1) closure itself.

**Structural argument:**

The first threshold (D5) produces a U(1) gauge group. The U(1) gauge group has circle
symmetry — the configuration space at D5 is S¹, which is the unit circle in ℂ¹. This gives
the substrate a natural complex structure: the D5 mode's phase variable θ ∈ S¹ is a
complex unit, and all fields that couple to the D5 U(1) gauge group inherit this complex
structure.

The D6 and D7 modes appear at thresholds that occur after the D5 threshold. The D6
bifurcation opens in the presence of the existing D5 U(1) structure. If the D6 mode
couples to the D5 gauge field (as required by charge conservation — the D6 electron
kink carries U(1) charge), then the D6 mode's fluctuations are complex (the mode can have
any U(1) phase). This adds one complex dimension to the configuration space, bringing the
total from ℂ¹ (D5) to ℂ² (D5+D6), with configuration space S³ ⊂ ℂ².

Similarly, the D7 mode inherits the D5/D6 complex structure, adding one more complex
dimension to reach ℂ³ with configuration space S⁵.

```
D5: 1 complex DOF  → S¹ ⊂ ℂ¹  → U(1)
D6: 2 complex DOFs → S³ ⊂ ℂ²  → U(1)×SU(2)  → SU(2) gauge group
D7: 3 complex DOFs → S⁵ ⊂ ℂ³  → U(1)×SU(3)  → SU(3) gauge group
```

**Why complex rather than real:** The U(1) charge coupling forces each subsequent mode to
come with a phase (it can carry U(1) charge or not — giving a phase degree of freedom).
A purely real scalar coupled to a U(1) gauge field is not gauge-invariant under the full
U(1) symmetry unless it is neutral. The D6 and D7 modes carry U(1) charge (the electron
has charge −e; the quarks have fractional charge), so their configurations must be complex.

**Status:** This argument is structural. It does not follow from the field equation
V(φ) = −α/2 φ² + β/4 φ⁴ for the real scalar substrate. The identification "D6 mode
carries U(1) charge" is a consequence of the D5/D6 coupling, not a derived input. The
full derivation requires a DFC effective theory for the coupled D5/D6 system — currently
the main gap in Bottleneck 1.

---

## Termination at SU(3)

The series U(1), SU(2), SU(3) terminates at n=3. The candidate DFC argument is the SU(3)
confinement mechanism: the D7 closure produces SU(3) gluons whose self-interaction energy
diverges at long distances (confinement), preventing any further free DOFs from existing
outside the color-singlet bound states. No D8 threshold can open a new free gauge group
because any would-be D8 mode is confined in color-singlet combinations that reduce to the
existing D5/D6/D7 structure.

This termination argument is structural (stated in `foundations/depth_assignment.md` and
`foundations/hopf_fibration_geometry.md`). A derivation would require computing the D7
self-energy integral and showing its infrared divergence prevents D8 closure.

---

## Formal Equations

The linearized fluctuation spectrum of the φ⁴ kink background:

```
Pöschl-Teller operator (Cycle 59):
L η = −∂²_x η + [V''(φ_kink)] η = ω² η

V''(φ_kink) = −α + 3β φ₀² tanh²(x/ξ) = α(3 tanh²(x/ξ) − 1)

Pöschl-Teller bound states (n=2 PT potential):
  Bound state 0: ω₀² = 0              (zero mode — exactly one per kink)
  Bound state 1: ω₁² = (3/4)α = (3/4)(2/ξ²)    (shape mode)
  Continuum:     ω² = 2α + k²         (scattering states)
```

Count of unstable modes at threshold (α = 0):
```
  At α → 0⁺:  Spectrum has one mode with ω² → 0  (the zero mode)
               All others have ω² > 0 (shape mode → m_σ², continuum → k²)
  Conclusion: Exactly ONE new zero mode per threshold crossing  ✓ (structural)
```

Configuration space at D(4+n) (requires complex structure from D5):
```
  n real codimension-1 crossings:   configuration space = S^(n-1) ⊂ ℝⁿ  → O(n)
  n complex DOFs (with D5 U(1)):    configuration space = S^(2n-1) ⊂ ℂⁿ → U(n)
  Gauge group (quotient by overall phase): SU(n)

  Gap: why S^(2n-1) rather than S^(n-1)?
  → Requires deriving that D6, D7 modes inherit D5 complex structure
```

---

## What Needs to Be Computed

The following computations would complete Bottleneck 1:

**Computation 1 — Coupled D5/D6 spectrum:**
Write the linearized fluctuation equation for the substrate with both D5 and D6 modes
present. Count the number of zero modes (modes with ω²=0) at the D6 threshold. If the
D5 background imposes a complex structure on the D6 fluctuation, the count will be 2 (one
complex mode = 2 real modes). If not, it will be 1.

*Approach:* Consider a two-component field (φ_D5, φ_D6) coupled by a cross-term. At the
D6 threshold, count the zero eigenvalues of the 2×2 fluctuation operator.

**Computation 2 — D6/D7 mode count:**
Repeat Computation 1 for the D6→D7 threshold. If the D5/D6 background has SU(2) symmetry,
and the D7 mode carries SU(2) charge, then the D7 mode configuration is a doublet (2
complex components) under SU(2). But this should give 4 real DOFs, not 2. Something
must select 1 complex DOF from the 4.

*Constraint:* The D7 mode must be in the fundamental representation of SU(2). The
fundamental of SU(2) is 2-dimensional (doublet). But the result S⁵ ⊂ ℂ³ requires 3
complex DOFs total, not 2+2. This is the key unresolved tension in Bottleneck 1.

**Computation 3 — Index theorem approach:**
Use the Atiyah-Singer index theorem for the fluctuation operator L on the n-kink background.
The index gives the net count of zero modes (zero modes minus zero anti-modes). For the
φ⁴ kink, the index is 1 (one translation zero mode). For n coincident kinks, the index is n.
If the D6 mode carries U(1) charge e, the index of the coupled (D5+D6) fluctuation operator
may be 2 rather than 1.

---

## Consistency Checks

| Check | Status |
|---|---|
| Pöschl-Teller zero mode is unique (1 per kink) | ✓ proved Cycle 59 |
| n coincident zero modes → SU(n) | ✓ proved Cycle 59 |
| One codimension-1 bifurcation → one new soft mode | ✓ structural (codimension-1 theorem) |
| D5 U(1) imposes complex structure on D6/D7 modes | ✓ structural (charge coupling argument) |
| Formally derived: D6 has 2 complex DOFs (not 1 or 3) | ✗ OPEN — requires Computation 1 above |
| Termination at SU(3): no D8 free gauge group | ✓ structural (confinement argument) |

---

## Open Questions

1. **Coupled fluctuation spectrum (Computation 1):** Write the two-component substrate
   fluctuation equation (D5 + D6 fields) and count zero modes at the D6 threshold. Does
   the D5 background produce 2 zero modes (one complex) at the D6 threshold, or 1?

2. **Fundamental representation constraint:** The D7 mode should be in the fundamental of
   the existing D5/D6 gauge group. But this gives a constraint on the number of new DOFs that
   must be reconciled with S⁵ ⊂ ℂ³. How does the D6 SU(2) doublet structure combine with
   the D7 threshold to give 3 complex DOFs rather than 4?

3. **Alternative: Hopf fibration chain:** The Hopf fibrations are:
   ```
   S¹ → S³ → S²    (U(1) fiber over S²)
   S³ → S⁷ → S⁴   (SU(2) fiber over S⁴)
   S⁷ → S¹⁵ → S⁸  (G₂ fiber over S⁸)
   ```
   The DFC gauge groups use S¹, S³, S⁵ — which are NOT the Hopf tower. What constraint
   selects S^(2n-1) over the Hopf tower S^(2^n - 1)?

4. **Codimension-1 count from field equation:** At the D(4+k) threshold, solve V(φ) = 0
   with α → 0 for the full substrate field equation (including all existing D5,...,D(4+k-1)
   modes). How many zero eigenvalues does the full fluctuation operator L have?

---

## Connections

- `foundations/zero_mode_multiplet.md` — second half proved (n modes → SU(n); Cycle 59)
- `foundations/depth_assignment.md` — Bottleneck 1 five constraints; Route B formalism
- `foundations/hopf_fibration_geometry.md` — S^(2n-1) correspondence; Route B Hopf picture
- `equations/hopf_dof_count.py` — numerical verification of n modes → SU(n); gauge boson counts
- `foundations/kink_nucleation.md` — single-kink zero mode; Z₂ topology
- `foundations/kink_scattering.md` — shape mode spectrum; Pöschl-Teller exact results

Cycle 62 | Bottleneck 1 first half: structural argument mapped; derivation open
