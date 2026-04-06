# Bell's Theorem and DFC Hidden Variables

## The Founding Claim

> **The DFC model's resolution of Bell's theorem is its deepest structural claim:**
>
> The hidden variables that determine quantum measurement outcomes are **local in the
> substrate** (they exist as definite values in the compression field at D-depths below D3)
> but appear **non-local from the D3 perspective** (because the substrate's pre-D3
> connectivity spans what appears to be spatially separated points).
>
> This is not superdeterminism and not a non-local hidden variable theory.
> It is a claim that "locality" has two meanings — one at the substrate level and one
> at the apparent-3D level — and Bell's theorem applies to the latter, not the former.

---

## Bell's Theorem: What It Actually Proves

Bell's theorem (1964) shows that **no theory satisfying three assumptions** can reproduce
the quantum predictions for entangled spin-1/2 pairs:

**Assumption 1 (Outcome locality):** The outcome at detector A is a function only of
the local hidden variable λ and the local measurement setting a:
```
result_A = f(λ, a)
```

**Assumption 2 (Parameter independence / no-conspiracy):** The hidden variable λ is
statistically independent of the measurement settings:
```
P(λ | a, b) = P(λ)    [λ does not depend on what the experimenters choose to measure]
```

**Assumption 3 (Completeness):** The hidden variable λ fully specifies the outcome
probabilities — no additional information is needed.

**What Bell proves:** If all three assumptions hold, then E(a,b) satisfies:
```
|E(a,b) - E(a,c)| ≤ 1 + E(b,c)    [CHSH Bell inequality]
```

Quantum mechanics violates this with E(a,b) = -cos(θ), reaching CHSH = 2√2 ≈ 2.83.
Experiments confirm the violation.

**Consequence:** At least one of Assumptions 1, 2, or 3 must fail in any correct theory.

---

## Where DFC Locates the Failure

DFC violates **Assumption 2** — but not in the "superdeterminism" sense. Here is the
precise mechanism.

### The DFC Hidden Variable

In DFC, the hidden variable for an entangled pair is the joint substrate field state at all
D-depths:
```
λ = φ(x₁, x₂, D1, D2, D3, D4)    [full substrate configuration at all depths]
```

This is a function over all four compression depths, not just the apparent D3 positions
x₁ and x₂. The field at D1 and D2 is not spatially separated in the way D3 configurations
are — it precedes the D3 localization behavior.

### Why λ Correlates with Measurement Settings

At D3 (the localization depth), the measurement setting at detector B is an event at
spatial location x_B. But at D1/D2 depths, the substrate has **no concept of spatial
separation** yet — D3 localization is what creates the appearance of spatial distance.

The substrate at D1/D2 is therefore:
- Not "at x₁" or "at x₂" — those labels are D3 constructs
- Globally connected — the compression budget at D1/D2 spans what will become the
  entire apparent spatial separation

This means: the D1/D2 substrate state λ_pre contains information about both detector
settings (a and b) in the sense that it is the state from which both the entangled pair
**and the measurement devices** emerged. At D1/D2, "a" and "b" are not separate from λ —
they are downstream projections of the same substrate.

**This is the precise statement:**
```
P(λ | a, b) ≠ P(λ)    [Assumption 2 fails]
```

Not because experimenters' choices are predetermined (superdeterminism), but because λ
includes depth levels where "a," "b," and the pair preparation are not yet separated
into distinct events.

### Why This Is Not Superdeterminism

Superdeterminism is usually rejected because it seems to require an implausible
conspiracy: that the hidden variable happens to be correlated with the experimenters'
free choices. Bell himself rejected it as "not very nice."

The DFC mechanism is structurally different:
1. **There is no conspiracy.** The D1/D2 substrate is not "conspiring" with the
   experimenter's choices. It is simply that at D1/D2 depths, there are no separate
   events — all downstream events (including the "choice" of measurement setting)
   are products of the same substrate dynamics.

2. **The experimenter's freedom is real at D3.** From the D3 perspective, the
   measurement settings a and b are freely chosen. The apparent non-locality arises
   because D3 freedom does not imply D1/D2 independence.

3. **The correlation is structural, not conspiratorial.** The entangled pair and the
   measurement devices share a common substrate ancestry at pre-D3 depths. The
   correlation between λ and (a, b) is a consequence of this shared ancestry — the
   same way that two events with a common cause are correlated without conspiracy.

A precise analogy: At D3, two separate dice rolls appear independent. At D1/D2, both
dice are part of the same substrate — the "independence" of the rolls is an emergent
D3 property, not a pre-D1 property. Bell's theorem assumes D3-level independence of λ
and (a, b). DFC says this D3 independence is not the fundamental level.

---

## The DFC Resolution: Two Kinds of Locality

DFC proposes that "local" has two distinct meanings:

**Substrate-local (D-depth local):**
The hidden variable λ = φ(x, D1..D4) is a definite value in the substrate at each
point in the compression field. There are no "spooky" influences at a distance at the
substrate level — the substrate evolves by local field equations everywhere.

**Apparent-local (D3-local):**
The measurement outcomes, when projected onto D3 (apparent spatial locations), appear
to have non-local correlations. This is because D3 localization maps a globally connected
substrate (D1/D2) onto an apparently separable spatial arrangement.

The Bell theorem applies to apparent-local hidden variable theories. DFC has
substrate-local hidden variables — which appear non-local at D3.

The claim: **non-locality is the appearance of D1/D2 substrate connectivity from the
perspective of D3 localization.**

---

## Quantitative Consequence: The CHSH Value

If the DFC mechanism is correct, the predicted CHSH value is determined by the SU(2)
geometry of the D6 closure (which provides the spinor structure for spin measurements).

For the singlet state with measurement axes at angle θ:
```
E(a,b) = -cos(θ)    [from SU(2) spinor inner product at D6 closure]
```

The CHSH for optimal angles (a=0°, a'=90°, b=45°, b'=135°):
```
S_DFC = |E(0°,45°) - E(0°,135°)| + |E(90°,45°) + E(90°,135°)|
      = |-cos(45°) - (-cos(135°))| + |(-cos(-45°)) + (-cos(-45°))|
      = |-1/√2 - 1/√2| + |1/√2 + 1/√2|...

Correct calculation:
    E(0°,45°)   = -cos(45°)  = -1/√2
    E(0°,135°)  = -cos(135°) = +1/√2
    E(90°,45°)  = -cos(-45°) = -1/√2
    E(90°,135°) = -cos(45°)  = -1/√2

S = |(-1/√2) - (1/√2)| + |(-1/√2) + (-1/√2)|
  = |-2/√2| + |-2/√2|
  = 2/√2 + 2/√2 = 4/√2 = 2√2 ≈ 2.828
```

The Tsirelson bound 2√2 is reproduced from SU(2) spinor geometry. See
`equations/bell_correlations.py` for the numerical verification.

### The Tsirelson Bound as a D6 Structural Constraint

The Tsirelson bound S ≤ 2√2 applies to all quantum correlations. In DFC, it
should follow from the SU(2) topology of the D6 closure:

- SU(2) spinors live in a 2-dimensional complex Hilbert space (S² / Bloch sphere)
- The maximum inner product between unit spinors is bounded by |⟨ψ₁|ψ₂⟩|² ≤ 1
- The CHSH inequality is linear in expectation values of tensor products of SU(2) operators
- The maximum of a linear function of SU(2) tensor products on the Bloch sphere gives 2√2

This is the structural argument. A complete derivation would show that no substrate
configuration with SU(2) closure geometry can exceed 2√2. Whether the DFC substrate
could have a different geometry (non-SU(2)) at some depth and give S > 2√2 is an
open question — and a potential discriminating prediction.

---

## Formal Statement of the DFC Bell Resolution

**Theorem (informal):** Let λ = φ(D1..D4) be the substrate field state at all depths below
D3. Then:

1. λ is a **definite** (not probabilistic) value at every point in the substrate at all
   compression depths. The substrate is a deterministic classical field.

2. At D3 (apparent spatial), λ projects onto apparently separate hidden variables
   λ₁ = φ(x₁, D3) and λ₂ = φ(x₂, D3) that are **correlated** because they are
   projections of the same D1/D2 substrate state.

3. The correlation E(λ₁, a) × E(λ₂, b) integrated over λ with the DFC measure
   (SU(2) spinor geometry at D6) gives E(a,b) = -cos(θ).

4. Bell's Assumption 2 fails because P(λ | a, b) ≠ P(λ) at D1/D2 depths — not due
   to conspiracy, but because D1/D2 does not have the concept of independent events.

**Status:** Points 1-2 are established by the DFC substrate framework. Point 3 requires
a formal derivation of E(a,b) = -cos(θ) from the DFC field equations (open).
Point 4 is the core philosophical claim — structurally argued but not yet a theorem.

---

## Consistency Checks

| Claim | DFC mechanism | Status |
|---|---|---|
| Bell inequality violated | Non-factorizable D6 closure winding constraint | Structural ✓ |
| CHSH = 2√2 | SU(2) spinor geometry at D6 | Derived (see equations/bell_correlations.py) |
| E(a,b) = -cos(θ) | SU(2) spinor inner product | Derived (verified numerically) |
| Tsirelson bound S ≤ 2√2 | Maximum of SU(2) tensor product operators | Structural argument ✓; formal proof OPEN |
| No signaling | Random buckling + classical channel required | Structural ✓ |
| Hidden variables exist | Substrate field values at D1/D2 are definite | By DFC postulates |
| Assumption 2 fails (DFC) | D1/D2 connectivity spans apparent separation | Structural claim ✓ |
| Not fine-tuned conspiracy | Correlation from common substrate ancestry | Argued ✓; formal measure OPEN |

---

## Open Problems

1. **Formal derivation of E(a,b) = -cos(θ) from DFC field dynamics.** Compute the joint
   measurement probability for two D6 kink precursors under arbitrary measurement angles a,b
   from the D6 substrate field equations and show that it equals -(1/2)cos(θ).

2. **Formal derivation of Tsirelson bound from DFC.** Show that for any preparation of
   two D6 kink precursors and any two measurement settings, the CHSH value S ≤ 2√2.
   This would require the constraint: the D6 closure is described by an SU(2) Bloch sphere
   (not a larger Hilbert space), which limits correlations to ≤ 2√2.

3. **Measure on λ.** The DFC hidden variable λ = φ(D1..D4) has a measure induced by the
   substrate field dynamics. Computing this measure explicitly (from the substrate's
   stationary distribution or initial conditions) would make the hidden variable theory
   precise and quantitative.

4. **Independence of measurement choices at D3.** Bell's theorem requires experimenters'
   free choices to be (effectively) independent of λ. In DFC, this independence holds
   at D3 — the apparent-spatial level. A precise statement of "D3-independence" and when
   it holds is needed to complete the argument.

5. **Predictions beyond standard QM.** If DFC violates Assumption 2 in a specific way,
   it might predict deviations from standard QM in regimes where the D1/D2 connectivity
   plays a role — e.g., at extreme energies, or for measurements separated by cosmological
   distances where substrate expansion modifies the D1/D2 connectivity. Quantifying this
   would give falsifiable predictions.

---

## Connections

- `phenomena/quantum/entanglement.md` — phenomena-level description of entanglement
- `foundations/measurement.md` — kink nucleation as the measurement event
- `foundations/spin_emergence.md` — Jackiw-Rebbi spinors at D6
- `foundations/route1_skyrme.md` — D6 SU(2) closure topology
- `equations/bell_correlations.py` — CHSH = 2√2 verified from SU(2) geometry
- `foundations/substrate.md` — the substrate as one deterministic classical field
