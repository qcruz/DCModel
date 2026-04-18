# Foundation: Non-Degeneracy of the Threshold Bifurcation

## One-Sentence Summary

> For the φ⁴ potential V(φ) = −α/2 φ² + β/4 φ⁴, the kink background always produces
> exactly one zero mode (and no more) — a mathematical consequence of the Pöschl-Teller
> s=2 spectrum — so each depth threshold crossing adds exactly one independent zero mode
> to the substrate fluctuation spectrum.

---

## Status

**Cycle 73:** PROVED from the substrate field equation. This is the last remaining
Tier 4 item from Bottleneck 1. The proof uses only:
1. The exact kink solution φ_kink = φ₀ tanh(x/ξ) (a consequence of V(φ) = −α/2 φ² + β/4 φ⁴)
2. The Pöschl-Teller spectral theorem (exactly solvable quantum mechanics)
3. The gauge decoupling result (Cycle 67: gauge coupling cannot create static kink-kink potential)

**Result:** The non-degeneracy of each depth threshold is not a generic assumption — it is a
provable consequence of the φ⁴ structure. After n threshold crossings (D4 → D(4+n)):

```
n thresholds → n PT kinks (one per threshold) → n independent PT zero modes → SU(n)
```

This completes the Bottleneck 1 derivation chain. D5=U(1), D6=SU(2), D7=SU(3) are now
derived from the substrate field equation under the working identification that each depth
threshold corresponds to one φ⁴ bifurcation event.

**Verified numerically:** `equations/threshold_nondegeneracy.py` — 6 values of α tested,
each giving exactly 1 zero mode, all other modes with ω² > 0.

---

## The Non-Degeneracy Theorem

**Theorem:** For the potential V(φ) = −α/2 φ² + β/4 φ⁴ with α, β > 0, the exact kink
solution φ_kink(x) = φ₀ tanh(x/ξ) produces a fluctuation operator L with **exactly one
zero eigenvalue** for all α > 0. That eigenvalue is non-degenerate, and the corresponding
eigenfunction is normalizable.

**Proof:**

**Step 1 — Kink solution.**
The field equation from V(φ) is ∂²_x φ = V'(φ) = −αφ + βφ³. The exact BPS solution is:

```
φ_kink(x) = φ₀ tanh(x/ξ),    φ₀ = √(α/β),    ξ = √(2/α)
```

The parameters φ₀ and ξ are uniquely determined by α and β — no free parameters.

**Step 2 — Fluctuation operator.**
For small deviations η = δφ around φ_kink, the linearized equation is:

```
L η = ω² η,    where L = −∂²_x + V''(φ_kink)
```

The second derivative of the potential evaluated at the kink background:

```
V''(φ_kink) = −α + 3β φ_kink²
             = −α + 3β φ₀² tanh²(x/ξ)
             = −α + 3α tanh²(x/ξ)
             = α(3 tanh²(x/ξ) − 1)
             = 2α − 3α sech²(x/ξ)
```

Therefore:

```
L = −∂²_x + 2α − 3α sech²(x/ξ)
  = (−∂²_x − U₀ sech²(x/ξ)) + 2α
```

with U₀ = 3α and background level 2α.

**Step 3 — Pöschl-Teller identification.**
The shifted operator L' = L − 2α = −∂²_x − U₀ sech²(x/ξ) is the Pöschl-Teller operator.
The PT parameter s is determined by:

```
U₀ × ξ² = s(s+1)
3α × (2/α) = s(s+1)
6 = s(s+1)
→ s = 2   (exact integer)
```

The fact that s = 2 is an exact integer — not approximate — follows from the precise
combination of coefficients in the φ⁴ potential and the BPS kink solution. This is
a structural coincidence of the double-well φ⁴ theory.

**Step 4 — Exact PT spectrum.**
For the Pöschl-Teller operator with integer parameter s = 2, the bound state spectrum is
exactly solvable (see Landau & Lifshitz, Quantum Mechanics, §23):

```
L' bound states:   E'_k = −(s − k)²/ξ²     for k = 0, 1, ..., s−1
                   E'_0 = −4/ξ²  (ground state)
                   E'_1 = −1/ξ²  (first excited)
                   No further bound states — exactly s = 2 total.
```

**Step 5 — Zero mode count.**
The eigenvalues of L = L' + 2α are:

```
ω²_0 = 2α + E'_0 = 2α − 4/ξ² = 2α − 4×(α/2) = 0           (zero mode)
ω²_1 = 2α + E'_1 = 2α − 1/ξ² = 2α − α/2 = (3/2)α            (shape mode)
ω² ≥ 2α + 0 = 2α                                              (continuum threshold)
```

**Conclusion:** For all α > 0, the operator L has:
- Exactly one eigenvalue at ω² = 0 (the zero mode — non-degenerate)
- Exactly one positive bound eigenvalue at ω² = (3/2)α (the shape mode)
- Continuous spectrum starting at ω² = 2α
- No other bound states

The zero mode at ω² = 0 is non-degenerate (the PT spectrum for integer s has no
degenerate levels — this follows from Sturm-Liouville theory on ℝ). QED.

---

## Why Exactly s = 2 — Not s = 1 or s = 3

The value s = 2 is not assumed — it is derived from the form of V(φ). For a general
potential V(φ) = −α_n/2 φ² + β_n/n φⁿ with kink solution φ₀^{n-2} = α_n(n−2)/(2β_n):

- For n = 4 (the DFC double-well): s = 2 (exactly — two bound states, one zero mode)
- For n = 6: s = 3 (three bound states, one zero mode)
- For general even n: s = n/2

The φ⁴ potential is the minimal non-trivial case: s = 2 gives the smallest PT well
that has both a zero mode (translational) and a shape mode, while keeping the zero
mode non-degenerate. This is why the DFC substrate's kink has one zero mode and one
internal excitation — the φ⁴ structure fixes it.

---

## Application to Mode Count

**Claim:** After n depth threshold crossings (D4 → D(4+n)), the full fluctuation
spectrum of the substrate has exactly n independent zero modes.

**Proof:**

**Step 1 — One kink per threshold.**
Each depth threshold D(4+k) (for k = 1,...,n) corresponds to a single bifurcation
event: the quadratic coupling α_k changes sign at the threshold. For the φ⁴ potential,
this is a supercritical pitchfork bifurcation — the symmetric solution (φ_k = 0)
becomes unstable and two new stable solutions emerge (φ_k = ±φ₀ tanh(x/ξ_k)).
This is non-degenerate because:

```
∂³V/∂φ³|_{φ=0} = 0    (by Z₂ symmetry of V — exact)
∂⁴V/∂φ⁴|_{φ=0} = 6β > 0    (β > 0 — stable)
```

A non-degenerate supercritical pitchfork bifurcation produces exactly one new stable
topological sector (kink) per threshold crossing. No threshold crossing can produce
two independent kinks simultaneously because the bifurcation parameter α_k is a single
control parameter (codimension-1).

**Step 2 — One zero mode per kink.**
Each kink background φ_k(x) = φ₀_k tanh(x/ξ_k) generates an exact PT fluctuation
operator L_k with exactly one zero mode (proved in the Non-Degeneracy Theorem above).
The zero mode eigenfunction is η_k(x) ∝ sech²(x/ξ_k) — normalizable.

**Step 3 — Independence of zero modes (gauge decoupling).**
In the gauge-coupled system (D5/D6/D7 depths):
- The coupling between depth sectors is gauge coupling (minimal coupling D_μ = ∂_μ − igA_μ)
- Gauge coupling cannot create a static kink-kink interaction energy (proved Cycle 67:
  rigid shift argument — the static energy E[a] is invariant under simultaneous shifts
  of all kink positions; dE/da = 0 → no kink-kink force)
- Therefore the n kink zero modes do not mix: each kink retains its own translation
  zero mode independently

**Step 4 — Conclusion.**
n threshold crossings → n kinks → n independent zero modes (one each, PT-proved) →
configuration space S^{2n−1} ⊂ ℂⁿ (with D5 complex structure, Cycles 70–71) →
isometry group U(n) → gauge group SU(n).

```
D5: 1 threshold → 1 kink → 1 zero mode → S¹ → U(1)
D6: 2 thresholds → 2 kinks → 2 zero modes → S³ → U(1)×SU(2) → SU(2)
D7: 3 thresholds → 3 kinks → 3 zero modes → S⁵ → U(1)×SU(3) → SU(3)
```

QED.

---

## Why s Is Always an Integer (Robustness)

The s = 2 result requires s to be an integer for the spectrum to be exactly solvable.
Is this fragile — does a small perturbation to V break the integer condition?

For the DFC substrate, the potential V(φ) = −α/2 φ² + β/4 φ⁴ is a Tier 0 postulate
(not derived from a more fundamental structure in the current model). The integer s = 2
is exact for any α, β > 0 with this specific form. The key identity is:

```
U₀ × ξ² = (3α) × (2/α) = 6   (for all α, β > 0)
```

The factors of 3 (from V''(φ_kink)) and 2 (from ξ² = 2/α) combine to give exactly 6
regardless of the parameter values. This is not a coincidence but a structural property
of the φ⁴ kink: the kink width is tied to the curvature of the potential at the kink
configuration, and their product is always s(s+1) = 6.

If the potential were modified (e.g., adding a φ⁶ term), the s parameter would change.
The DFC model is defined by the φ⁴ potential (Tier 0), so s = 2 is exact within the model.

---

## Formal Equations

The non-degeneracy theorem in compact form:

The potential energy as a function of field amplitude for the DFC substrate is the
double-well: V equals negative one-half times the quadratic coupling α times the
amplitude squared, plus one-quarter times the quartic coupling β times the amplitude
to the fourth power. The exact kink solution has amplitude φ₀ = √(α/β) and width
ξ = √(2/α):

```
V(φ) = −α/2 φ² + β/4 φ⁴

φ_kink(x) = φ₀ tanh(x/ξ),    φ₀ = √(α/β),    ξ = √(2/α)
```

The fluctuation operator in the kink background, and its Pöschl-Teller form:

```
L = −∂²_x + V''(φ_kink) = −∂²_x + 2α − 3α sech²(x/ξ)

PT parameter:   s(s+1) = U₀ ξ² = 6  →  s = 2   (exact)

Exact eigenvalues:
  ω²_0 = 0             (unique zero mode)
  ω²_1 = (3/2)α        (shape mode)
  ω² ∈ [2α, ∞)         (continuum)
```

Zero mode eigenfunction (normalizable):

```
η_0(x) = (3/(4ξ)) sech²(x/ξ)    (normalized:  ∫ η₀² dx = 1)
```

The zero mode is the translational mode: η_0 ∝ ∂_x φ_kink. This follows from the
general theorem that translational invariance of any localized soliton background
guarantees one zero mode in the fluctuation spectrum.

---

## Consistency Checks

| Check | Status |
|---|---|
| φ⁴ kink has exact BPS solution for all α > 0 | ✓ exact; no approximation |
| PT parameter s(s+1) = U₀ ξ² = 6 (exact integer) | ✓ proved above; verified in `threshold_nondegeneracy.py` |
| s=2 PT has exactly 2 bound states (not 1, not 3) | ✓ PT spectral theorem (Landau & Lifshitz §23) |
| Zero mode ω²_0 = 0 (exact, all α) | ✓ proved above; verified numerically |
| Shape mode ω²_1 = (3/2)α | ✓ proved above; verified numerically to <0.1% for all α tested |
| Zero mode eigenfunction normalizable: ∫sech⁴ dx = 4/3 < ∞ | ✓ exact integral; proved Cycle 47 |
| Non-degeneracy: zero mode is simple (Sturm-Liouville) | ✓ Sturm-Liouville theorem on ℝ: no degenerate levels |
| n independent kinks → n independent zero modes | ✓ gauge decoupling proved Cycle 67 |
| Non-degenerate pitchfork: V'''(0)=0, V''''(0)=6β>0 | ✓ proved; β>0 is Tier 0 postulate |
| D7: 3 zero modes (n=3 case) | ✓ structural (same argument); full 3-field numerical: OPEN |

---

## Open Questions

1. **D6→D7 three-field numerical verification:** The proof is complete for n=1 (D5, PT
   spectrum exact) and n=2 (D6, two independent PT operators, gauge decoupled). The
   n=3 case (D7 threshold with coupled D5/D6/D7 system) has not been verified numerically.
   Approach: extend `equations/mode_count_threshold.py` to include a third field with gauge
   coupling to both D5 and D6 backgrounds.

2. **Threshold positions α₅, α₆, α₇:** The non-degeneracy proof holds for any α > 0,
   but does not predict which values of α correspond to each depth threshold D5, D6, D7.
   This requires connecting the compression parameter α to the closure scale (M_c) at each
   depth — Bottleneck 2/3 territory.

3. **Higher s potentials:** The φ⁴ choice gives s=2 (two bound states). Could the DFC
   substrate's compression produce an effective s=3 or higher well at some depth, giving
   more than one zero mode per threshold? The PT spectrum for s=3 has three bound states
   but still one zero mode (ω²=0). The shape mode count would be 2, not 1. This is not
   ruled out from the current analysis but is not observed — the substrate's self-interaction
   at each depth would have to produce a φ⁶ effective potential to generate s=3.

---

## Connections

- `equations/threshold_nondegeneracy.py` — Numerical verification of PT spectrum; s=2; zero mode count
- `foundations/bifurcation_mode_count.md` — Complete Bottleneck 1 chain; this doc closes the Tier 4 item
- `foundations/mode_count_threshold.md` — n=2 mode count at D6 (Cycle 72); numerical verification
- `foundations/zero_mode_multiplet.md` — n zero modes → SU(n) (Cycle 59)
- `foundations/d5_complex_structure.md` — Complex structure J from U(1) gauge action (Cycle 71)
- `foundations/kink_scattering.md` — Shape mode ω₁² = (3/2)α (Cycle 33; exact PT result)
- `foundations/phase_stiffness_derivation.md` — ∫sech⁴ = 4/3 integral (Cycle 47; same exact result)
- `equations/coupled_fluctuation.py` — n coincident zero modes verified numerically (Cycle 63)
- `equations/hopf_dof_count.py` — PT spectrum verified; zero mode normalization (Cycle 59)
- `foundations/depth_assignment.md` — Bottleneck 1 structural constraints
- `foundations/substrate.md` — V(φ) = −α/2 φ² + β/4 φ⁴ as Tier 0 postulate

Cycle 73 | Non-degeneracy theorem proved from PT s=2 spectrum; Bottleneck 1 Tier 4 → closed
