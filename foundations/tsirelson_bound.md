# Tsirelson Bound from DFC SU(2) Closure Algebra

## Status

> **Cycle 35:** Formal proof of CHSH ≤ 2√2 from SU(2) closure algebra.
> Closes the OPEN item from `foundations/bell_hidden_variables.md`.
>
> **Result:** The Tsirelson bound is a theorem of operator algebra for any system
> with binary (±1) observables. DFC's D6 SU(2) closure produces exactly this
> structure. The bound is tight: CHSH = 2√2 is achieved at optimal angles.
>
> Verified numerically in `equations/bell_correlations.py`.

---

## The Theorem

**Tsirelson's Theorem (1980):** For any quantum state ρ and any observables
A₁, A₂ (on system A) and B₁, B₂ (on system B) with eigenvalues ±1:

```
CHSH = |⟨A₁B₁⟩ + ⟨A₁B₂⟩ + ⟨A₂B₁⟩ − ⟨A₂B₂⟩| ≤ 2√2
```

The bound 2√2 ≈ 2.828 is tight — it is achieved by the quantum singlet state at
optimal angles.

---

## Proof from Operator Algebra

### Step 1: Write the CHSH operator

Define:
```
C = A₁ ⊗ (B₁ + B₂) + A₂ ⊗ (B₁ − B₂)

Let M = B₁ + B₂  and  N = B₁ − B₂
```

The CHSH value is an expectation value: CHSH = ⟨C⟩ ≤ ‖C‖_op (operator norm).
So we need to bound ‖C‖_op.

### Step 2: Compute C²

```
C² = (A₁ ⊗ M + A₂ ⊗ N)(A₁ ⊗ M + A₂ ⊗ N)
   = A₁² ⊗ M² + A₁A₂ ⊗ MN + A₂A₁ ⊗ NM + A₂² ⊗ N²
```

Since A_i² = I (eigenvalues ±1 → A_i² = I):
```
C² = I ⊗ M² + A₁A₂ ⊗ MN + A₂A₁ ⊗ NM + I ⊗ N²
   = I ⊗ (M² + N²) + A₁A₂ ⊗ MN + A₂A₁ ⊗ NM
```

### Step 3: Simplify M² + N² and MN + NM

Expand:
```
M² + N² = (B₁ + B₂)² + (B₁ − B₂)²
        = B₁² + 2B₁B₂ + B₂² + B₁² − 2B₁B₂ + B₂²
        = 2B₁² + 2B₂² = 2I + 2I = 4I    [since B_j² = I]
```

```
MN + NM = (B₁+B₂)(B₁−B₂) + (B₁−B₂)(B₁+B₂)
        = (B₁²−B₂²) + [B₂,B₁] + (B₁²−B₂²) + [B₁,B₂]
        = 2(I − I) + [B₁,B₂] − [B₁,B₂] = 0
```

```
MN − NM = (B₁+B₂)(B₁−B₂) − (B₁−B₂)(B₁+B₂)
        = −2[B₁,B₂]
```

Therefore, using {A₁,A₂} = A₁A₂ + A₂A₁ and [A₁,A₂] = A₁A₂ − A₂A₁:
```
A₁A₂ ⊗ MN + A₂A₁ ⊗ NM
= (1/2){A₁,A₂} ⊗ (MN+NM) + (1/2)[A₁,A₂] ⊗ (MN−NM)
= 0 + (1/2)[A₁,A₂] ⊗ (−2[B₁,B₂])
= −[A₁,A₂] ⊗ [B₁,B₂]
```

### Step 4: The key identity

```
C² = 4(I ⊗ I) − [A₁,A₂] ⊗ [B₁,B₂]
```

### Step 5: Bound the commutator norm

For SU(2) spin operators A_i = â_i · σ and B_j = b̂_j · σ:
```
[A₁, A₂] = [â₁·σ, â₂·σ] = 2i(â₁ × â₂) · σ
‖[A₁,A₂]‖_op = 2|â₁ × â₂| ≤ 2     [equality when â₁ ⊥ â₂]
‖[B₁,B₂]‖_op = 2|b̂₁ × b̂₂| ≤ 2     [equality when b̂₁ ⊥ b̂₂]
```

### Step 6: Bound the eigenvalue of C²

The maximum eigenvalue of C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂]:

The operator −[A₁,A₂]⊗[B₁,B₂] has maximum eigenvalue
+‖[A₁,A₂]‖_op × ‖[B₁,B₂]‖_op ≤ 2 × 2 = 4.

Therefore:
```
λ_max(C²) ≤ 4 + 4 = 8

‖C‖_op = √λ_max(C²) ≤ √8 = 2√2
```

### Step 7: Conclude

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   CHSH = ⟨C⟩ ≤ ‖C‖_op ≤ 2√2 ≈ 2.828                         │
│                                                                 │
│   The Tsirelson bound follows from:                             │
│     1. Binary observables: A_i² = B_j² = I                     │
│     2. Commutator norm: ‖[A_i, A_j]‖_op ≤ 2 for SU(2)        │
│     3. The algebraic identity C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂]   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## When the Bound Is Achieved (Tightness)

The bound is achieved when:
1. â₁ ⊥ â₂ and b̂₁ ⊥ b̂₂ (maximally non-commuting pairs)
2. The state ρ is such that ⟨−[A₁,A₂]⊗[B₁,B₂]⟩ = 4

For condition 2 with the singlet state and optimal angles (a=0°, a'=90°, b=45°, b'=135°):
```
[A₁,A₂] = [σ_z, σ_x] = 2iσ_y     (eigenvalues ±2i, operator norm 2)
[B₁,B₂] = [n̂₁·σ, n̂₂·σ]           (perpendicular axes, operator norm 2)

⟨singlet | [A₁,A₂]⊗[B₁,B₂] | singlet⟩ = −4
→ ⟨C²⟩ = 4 + 4 = 8 → ‖C‖ = 2√2   ✓
```

Verified: `equations/bell_correlations.py` gives CHSH = 2.828427 = 2√2 (error 4×10^-16).

---

## DFC-Specific Content: Why D6 SU(2) Saturation Matters

The proof uses two properties that DFC must supply:

**Property 1 (Binary outcomes):** Measurements on the D6 kink return binary outcomes ±1.

In DFC, this follows from the fact that the D6 SU(2) kink has two topological sectors
(winding ±1). A measurement pushes the kink precursor into one sector, giving a definite
binary outcome.

**Property 2 (SU(2) commutation relations):** The measurement operators satisfy
[A₁, A₂] = 2i(â₁ × â₂)·σ, with operator norm ≤ 2.

In DFC, this follows from the SU(2) Lie algebra of the D6 closure. The generators of
D6 SU(2) rotations satisfy [σ_i, σ_j] = 2iε_{ijk}σ_k, giving the norm bound ≤ 2.

Both properties are structural consequences of the D6 SU(2) closure topology. The
Tsirelson bound therefore follows from the **SU(2) structure of the D6 closure alone**.

### What Would Violate the Tsirelson Bound

A violation of CHSH > 2√2 would require either:
- Observables with more than 2 distinct eigenvalues (not binary) — inconsistent with
  the D6 kink's two topological sectors
- A commutator norm > 2 — inconsistent with SU(2) algebra
- A Hilbert space structure that differs from the standard quantum one

No DFC configuration produces CHSH > 2√2 as long as the D6 closure is SU(2) and
measurements are binary. This is why the Tsirelson bound is a prediction of DFC,
not merely a consistency check.

### Discriminating Prediction

If the D6 closure had a different topology — e.g., SU(2) × U(1) or a higher group —
the measurement operators could in principle have larger commutators, potentially
allowing CHSH > 2√2. The fact that DFC predicts CHSH ≤ 2√2 (exactly the quantum
mechanical bound) is therefore a non-trivial structural consequence of the D6 = SU(2)
assignment.

*If experiments ever observe CHSH > 2√2 (which is currently technically impossible
but not theoretically ruled out by all extensions of QM), it would falsify both
standard QM and the D6 = SU(2) assignment in DFC.*

---

## Remaining Open Problem

The proof above is complete as an algebraic theorem given Properties 1 and 2. What
remains open in DFC:

**Deriving Properties 1 and 2 from the substrate field equations.** Specifically:
- Why are measurement outcomes binary? (Why does the kink nucleate into exactly two
  sectors rather than a continuous distribution?)
- Why does the D6 SU(2) closure produce the standard quantum Hilbert space (complex
  amplitudes, Born rule) rather than some other probability structure?

These are part of the general open problem of deriving the quantum formalism from the
DFC substrate — `equations/quantum_emergence.py`. The Tsirelson bound is established
*conditional* on these properties. The unconditional derivation awaits the quantum
formalism.

---

## Summary

| Claim | Status |
|---|---|
| C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂] (algebraic identity) | **Proved ✓** |
| ‖[A_i,A_j]‖_op ≤ 2 for SU(2) (commutator bound) | **Proved ✓** |
| CHSH ≤ 2√2 (Tsirelson) | **Proved ✓** (given binary observables + SU(2)) |
| CHSH = 2√2 achieved at optimal angles | Verified numerically ✓ |
| Binary outcome property from D6 kink topology | Argued; formal derivation OPEN |
| Hilbert space from substrate | OPEN (quantum formalism) |

---

## Connections

- `foundations/bell_hidden_variables.md` — DFC Bell resolution; Assumption 2 violation
- `equations/bell_correlations.py` — CHSH = 2√2 verified (error 4×10^-16)
- `foundations/spin_emergence.md` — D6 SU(2) closure; Jackiw-Rebbi spinors
- `equations/quantum_emergence.py` — deriving quantum formalism from substrate (stub)
