# Bell's Theorem and DFC

## The DFC Position

> DFC proposes that the fundamental substrate state of an entangled pair is
> irreducibly joint — it does not decompose into independent local states
> associated with each particle. The decomposition into spatially separated
> independent systems is an emergent approximation produced by D3 localization,
> and Bell's theorem reveals the limits of that approximation.
>
> DFC does not claim to have found a loophole in Bell's theorem. Bell's theorem
> is a valid mathematical result. DFC proposes a framework in which the
> factorizability assumption that Bell locality requires may not describe the
> fundamental ontology.

---

## What Bell Proves

Bell's theorem (1964) shows that no theory satisfying a particular locality
condition can reproduce quantum predictions for entangled pairs.

The locality condition (Bell factorizability): given a complete underlying
state λ, the joint probability of outcomes A and B factorizes:

```
P(A, B | a, b, λ) = P(A | a, λ) × P(B | b, λ)
```

where a and b are the measurement settings at each detector.

If this holds and measurement settings are independent of λ, then:

```
|E(a,b) - E(a,c)| ≤ 1 + E(b,c)    [CHSH Bell inequality]
```

Quantum mechanics predicts E(a,b) = −cos(θ) for the singlet state, which gives
CHSH = 2√2 ≈ 2.83. Experiments confirm the violation. The factorizability
condition fails in nature.

This is a theorem. It stands regardless of interpretation.

---

## Where DFC Locates the Issue

DFC proposes that Bell factorizability fails because the fundamental substrate
state of an entangled pair is **irreducibly joint**.

### The substrate state is not factorizable

In DFC, two entangled particles are two localized features of a single connected
substrate configuration. The complete state is:

```
Λ_AB = substrate configuration of the joint system
```

The key property: Λ_AB is not equivalent to a product Λ_A × Λ_B. The substrate
field connecting the two kinks is one continuous object. The decomposition into
"Alice's particle" and "Bob's particle" is an emergent description produced by
D3 localization — it is not the fundamental fact.

Because the fundamental state does not factorize into independent local pieces,
Bell's factorizability condition:

```
P(A, B | a, b, Λ_AB) = P(A | a, Λ_A) × P(B | b, Λ_B)
```

does not apply in the form Bell assumes. The right-hand side presupposes a
decomposition that the substrate does not possess.

### This is not about hidden variable location

An earlier version of this document framed the DFC position as "hidden variables
that are local at a deeper level." That framing was incorrect. Moving hidden
variables to a different depth does not automatically evade Bell. If the complete
state λ specifies all relevant information and measurement settings are independent,
Bell applies regardless of where λ lives.

The actual DFC claim is different: the notion of *spatially separated independent
systems* is an emergent approximation, and the fundamental state is irreducibly
joint. Bell's factorizability is a property of the emergent spatial description,
not the fundamental substrate.

### This is not superdeterminism

An earlier version argued that P(λ|a,b) ≠ P(λ) — that the hidden variable
correlates with measurement settings. That is the superdeterminism route, and DFC
does not take it. Measurement settings are freely chosen at the D3 level.

The DFC position is that Bell factorizability (Assumption 1 in Bell's framework)
fails — the joint outcome cannot be decomposed into independent local functions —
not that measurement independence (Assumption 2) fails.

---

## What DFC Must Derive

The structural picture is coherent, but turning it into a result requires three
derivations that have not been completed:

**1. Joint measurement statistics from substrate dynamics.**

Starting from V(φ) and an entangled kink pair, derive P(A,B|a,b). For the
singlet state, the target is E(a,b) = −cos(θ), giving CHSH = 2√2.

The SU(2) spinor geometry at the D6 closure provides the correct structure:
the correlation function is the inner product of Jackiw-Rebbi spinors projected
onto measurement axes. But this is currently a structural argument from the
D6 topology, not a derivation from the field equation.

**2. No-signaling from substrate dynamics.**

Show that P(A|a,b) = P(A|a) and P(B|a,b) = P(B|b). The randomness of the
buckling event (kink nucleation) is expected to enforce this, but it has not
been derived from V(φ).

**3. Emergent relativistic locality.**

Show that the emergent 3+1D description has no preferred signaling frame despite
the substrate connection. The connection is structural, not a propagating signal,
so no frame-dependent speed is involved — but this needs to be demonstrated.

---

## Quantitative Result: CHSH = 2√2

For the singlet state measured along axes at angle θ:

```
E(a,b) = -cos(θ)    [from SU(2) spinor inner product at D6 closure]
```

The CHSH value for optimal angles (a=0°, a'=90°, b=45°, b'=135°):

```
S = |E(0°,45°) - E(0°,135°)| + |E(90°,45°) + E(90°,135°)|
  = |-1/√2 - 1/√2| + |-1/√2 + (-1/√2)|
  = 2/√2 + 2/√2 = 2√2 ≈ 2.828
```

This matches the quantum prediction and the Tsirelson bound. See
`equations/bell_correlations.py` for numerical verification (error 4×10⁻¹⁶).

---

## The Tsirelson Bound as a D6 Constraint

The Tsirelson bound S ≤ 2√2 applies to all quantum correlations. In DFC, it
follows from the SU(2) topology of the D6 closure:

- Binary observables from kink nucleation (two outcomes: N = ±1)
- SU(2) spinor geometry constrains operator norms: ‖[A_i, A_j]‖ ≤ 2
- The algebraic identity C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂] combined with
  these operator bounds gives S ≤ 2√2

See `foundations/tsirelson_bound.md` for the full proof.

---

## Consistency Checks

| Claim | DFC mechanism | Status |
|---|---|---|
| Bell inequality violated | Irreducibly joint substrate state; non-factorizable | Structural ✓ |
| CHSH = 2√2 | SU(2) spinor geometry at D6 | Verified (bell_correlations.py) |
| E(a,b) = −cos(θ) | SU(2) spinor inner product | Verified numerically |
| Tsirelson bound S ≤ 2√2 | SU(2) operator algebra | Proved (tsirelson_bound.md) |
| No signaling | Random buckling + classical channel needed | Structural ✓; derivation OPEN |
| Measurement independence preserved | Settings freely chosen at D3 | By framework ✓ |
| P(A,B\|a,b) from substrate dynamics | Full V(φ) → kink → JR → singlet → Born rule chain | T2a (bell_joint_derivation.py) |

---

## Open Problems

1. **[T2a] P(A,B|a,b) derived from V(φ).** The derivation chain V(φ) → kink → JR
   zero mode → SU(2) spinor → singlet (from N₁+N₂=0) → Born rule → P(A,B|a,b) →
   E(a,b) = −cos(θ) → CHSH = 2√2 is assembled in `equations/bell_joint_derivation.py`
   (14/14 PASS). Steps 1–5 are T1, steps 6–7 are T2a/T3, steps 8–9 are T1. Overall T2a.
   Three remaining gaps: (a) measurement dynamics from V(φ) (T3), (b) emergent
   relativistic locality, (c) joint Born rule substrate justification.

2. **[T2a] No-signaling verified.** The reduced density matrix ρ_A = I/2 is verified
   numerically in `equations/bell_joint_derivation.py`. The substrate justification
   (randomness of kink nucleation enforces P(A|a,b) = P(A|a)) remains T3.

3. **Derive emergent relativistic locality.** Show that the substrate connection
   produces no preferred frame for the emergent 3+1D description.

4. **Entanglement over cosmological distances.** Does DFC predict any distance-
   dependent modification to Bell correlations from substrate expansion or
   decoherence effects?

---

## Connections

- `phenomena/quantum/entanglement.md` — phenomena-level entanglement description
- `foundations/measurement.md` — kink nucleation as the measurement event
- `foundations/spin_emergence.md` — Jackiw-Rebbi spinors at D6
- `foundations/tsirelson_bound.md` — Tsirelson bound from SU(2) algebra
- `equations/bell_correlations.py` — CHSH = 2√2 verified numerically
- `equations/bell_joint_derivation.py` — full derivation chain V(φ) → Bell violation (14/14 PASS)
- `educational/19_bell_inequalities.md` — educational treatment
