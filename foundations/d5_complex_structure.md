# Foundation: The D5 U(1) Charge Defines the Complex Structure — Closing Bottleneck 1

## Status

> **Cycle 71:** Closes the Tier 3 gap identified in `foundations/complex_zero_mode_gap.md`
> (Cycle 70) and `foundations/bifurcation_mode_count.md` (Cycles 62–67c).
>
> **Result:** The D5 U(1) gauge action on charged fields IS the complex structure J on the
> zero mode space. Any field carrying D5 U(1) charge q ≠ 0 transforms as φ → e^(iqθ) φ
> under D5 gauge transformations; the infinitesimal generator (dθ → 0) of this action
> is a rotation J in the (Re φ, Im φ) plane satisfying J² = −I. This is the definition of
> a complex structure. Since D6 zero modes carry D5 U(1) charge (proved in Cycle 67c), J
> is defined on the D6 zero mode space. Combined with the Cycle 70 result
> SO(4)∩Aut(J)=U(2)→SU(2), the derivation chain for D6=SU(2) is complete.
>
> **Bottleneck 1 chain — now complete:**
> 1. D5 = U(1): two real zero mode DOFs → S¹ → SO(2)=U(1) (Cycle 70)
> 2. D6 zero modes carry D5 U(1) charge: ∫j_x = −2π/(5ξ) ≠ 0 (Cycle 67c)
> 3. U(1) charge action = complex structure J: φ → e^(iqθ)φ → J² = −I **(Cycle 71)**
> 4. SO(4)∩Aut(J) = U(2) → SU(2) after factoring U(1) (Cycle 70)
> 5. Three D6 zero modes similarly give SO(6)∩Aut(J) = U(3) → SU(3) (Cycle 70)
>
> **Remaining open items:** (a) Why D(4+n) opens exactly n zero modes from substrate
> dynamics (codimension-1 argument is structural, not derived from field equation);
> (b) termination at SU(3): why does the substrate not continue to D8=SU(4)?
> These are Tier 4 items — the gauge group assignments U(1), SU(2), SU(3) are now
> derivable assuming the mode count.

---

## The Argument

### Step 1: U(1) Charge Action on a Complex Field

The D5 U(1) gauge symmetry transforms any field carrying charge q as:

```
φ → e^(iqθ) φ    [for any gauge parameter θ]
```

Writing φ = A + iB in terms of its real part A and imaginary part B, the gauge
transformation maps:

```
A + iB  →  e^(iqθ)(A + iB) = (cos qθ + i sin qθ)(A + iB)
         = (A cos qθ − B sin qθ) + i(A sin qθ + B cos qθ)
```

In real coordinates (A, B), this is a rotation by angle qθ in the (A,B) plane:

```
(A, B)  →  (A cos qθ − B sin qθ,  A sin qθ + B cos qθ)
```

The infinitesimal generator of this rotation — the rate of change at θ = 0 — maps:

```
d/dθ|_{θ=0} (A cos qθ − B sin qθ,  A sin qθ + B cos qθ) = (−qB, qA)
```

In matrix form, this generator is the linear map J_q on ℝ²:

```
J_q : (A, B) → (−qB, qA)

As a 2×2 matrix (acting on column vector [A, B]ᵀ):

J_q = q × [[0, −1], [1, 0]]
```

### Step 2: J_q Satisfies J² = −I (the complex structure condition)

The matrix [[0,−1],[1,0]] squared equals [[−1,0],[0,−1]] = −I. Therefore:

```
J_q² = q² × (−I) = −q²I
```

For the charge normalized so that q² = 1 (i.e., |q| = 1), this gives:

```
J_q² = −I    ✓
```

A linear map J satisfying J² = −I is the definition of a **complex structure** on a
real vector space. It allows the space to be interpreted as a complex vector space by
declaring "multiplication by i" to mean "apply J."

**Consequence:** Any real vector space carrying a U(1) action with charge q = ±1
automatically has a complex structure. There is no additional ingredient required —
the complex structure is the U(1) action itself.

For q ≠ ±1 (fractional or higher charges): J_q² = −q²I. This is still a rotation
(non-degenerate), but not a complex structure in the strict sense unless we rescale
J → J/|q|. The normalized generator J_{norm} = J_q/|q| satisfies J_{norm}² = −I.
In all cases, as long as q ≠ 0, the U(1) action induces a complex structure on the space.

### Step 3: Application to D6 Zero Modes

The D6 zero modes in the D5 background carry D5 U(1) charge (Cycle 67c). The dressed
zero mode is the real zero mode profile multiplied by the D5 phase:

```
η₀^dressed(x) = η₀^real(x) × e^{iθ₅(x)}
```

where θ₅(x) = (π/2)(1 − tanh(x/ξ)) is the D5 half-vortex phase profile. The dressed
mode has:
- Real part: A(x) = η₀^real(x) cos θ₅(x)
- Imaginary part: B(x) = η₀^real(x) sin θ₅(x)

The U(1) current density of this dressed mode is j_x = η₀^{real,2} × ∂_x θ₅, and its
integral gives the total charge:

```
∫ j_x dx = −2π/(5ξ) ≠ 0    [proved exactly in Cycle 67c; ∫sech⁶ = 16/15]
```

Since the D6 dressed zero mode carries nonzero D5 U(1) charge, it lives in a complex
representation of D5 U(1). The D5 gauge action rotates this mode in its (Re, Im) plane
with generator J (as derived in Steps 1–2). This J is the complex structure on the D6
zero mode space.

### Step 4: Generalization to n Zero Modes

For n coincident D6 kinks, each kink has one dressed zero mode η₀^(k) carrying D5
U(1) charge. The collective zero mode space is ℝ^(2n) with coordinates:

```
(A₁, B₁, A₂, B₂, ..., Aₙ, Bₙ)    where A_k = Re(η₀^(k)), B_k = Im(η₀^(k))
```

The D5 U(1) gauge transformation with global parameter θ acts identically on each mode:

```
(A_k, B_k)  →  (A_k cos θ − B_k sin θ,  A_k sin θ + B_k cos θ)    for each k
```

(using |q|=1 normalized charge). The infinitesimal generator is the block-diagonal
complex structure J:

```
J = block_diag([[0,−1],[1,0]], [[0,−1],[1,0]], ...) ∈ SO(2n)
```

This J satisfies J² = −I on ℝ^(2n). It is the complex structure on the n-dimensional
complex vector space ℂⁿ = ℝ^(2n) with J = "multiplication by i".

### Step 5: The Gauge Group is SU(n)

From Cycle 70 (`foundations/complex_zero_mode_gap.md`, `equations/u1_from_paired_modes.py`):

```
The subgroup of SO(2n) commuting with J is U(n) = U(1) × SU(n).
dim({a ∈ so(2n) : [a,J]=0}) = n²    [verified for n=1,2,3]
```

The global U(1) factor in U(n) corresponds to the overall D5 U(1) phase acting
identically on all n modes — this is the D5 gauge group itself, already accounted for.
The residual symmetry acting *between* the n modes is SU(n).

**At D6 (n=2):** The two dressed D6 zero modes form ℂ² with SU(2) as the gauge group.
This is the D6 gauge group.

**At D7 (n=3):** Three dressed D7 zero modes (inheriting complex structure from D5/D6
backgrounds) form ℂ³ with SU(3) as the gauge group. This is the D7 gauge group.

---

## The Complete Bottleneck 1 Derivation Chain

```
SUBSTRATE (V(φ) = −α/2 φ² + β/4 φ⁴, second-order PDE)
    │
    ▼ [Codimension-1 bifurcation, Cycle 62]
One new zero mode per depth threshold: total n modes at D(4+n)
    │
    ▼ [Cycle 70: second-order PDE → 2 DOFs/mode]
2n real DOFs at D(4+n) → S^(2n−1) ⊂ ℝ^(2n)
    │
    ┌────────────────────┬──────────────────────────┐
    │ n=1 (D5)           │ n=2 (D6), n=3 (D7)        │
    ▼                    ▼                            │
SO(2) = U(1) ✓          SO(4) or SO(6) — too large   │
[Cycle 70: real          [need complex structure J]   │
 substrate gives                                      │
 U(1) directly]         ▼ [Cycle 67c: D6 modes       │
                        carry D5 U(1) charge;         │
                        ∫j_x = −2π/(5ξ) ≠ 0]         │
                                                      │
                        ▼ [Cycle 71: THIS DOCUMENT]   │
                        U(1) charge → J: φ→e^{iθ}φ,  │
                        J² = −I; J ∈ so(2n)           │
                                                      │
                        ▼ [Cycle 70: commutant]        │
                        SO(2n) ∩ Aut(J) = U(n)         │
                        dim verified: n=2→4, n=3→9     │
                                                      │
                        ▼                             │
                        Factor out D5 U(1) (global)   │
                                                      │
                        ▼                             │
              SU(2) (D6)  and  SU(3) (D7)  ✓          │
```

**What is proved in this chain:**
- D5 = U(1): algebraic derivation (Cycle 70) ✓
- D6 = SU(2): complete chain (Cycles 59, 63, 67c, 70, 71) ✓ (assuming n=2 modes at D6)
- D7 = SU(3): complete chain (same, assuming n=3 modes at D7) ✓ (assuming n=3 modes at D7)

**What remains open (Tier 4):**
- Why D(4+n) opens exactly n zero modes: codimension-1 argument is structural; substrate
  field equation derivation not yet complete
- Termination at D7: confinement argument is structural; formal derivation open

---

## Formal Equations

### U(1) phase action and complex structure

The D5 U(1) gauge action on a field with charge q:

```
Φ_θ(A, B) = (A cos qθ − B sin qθ,  A sin qθ + B cos qθ)
```

Its infinitesimal generator (Lie algebra element, or "velocity at θ=0"):

```
J_q = dΦ_θ/dθ |_{θ=0}: (A,B) → (−qB, qA)

Matrix form:  J_q = q [[0, −1], [1, 0]]
```

Complex structure condition (for |q|=1):

```
J_q² = q² [[0,−1],[1,0]]² = q²(−I) = −I    ✓
```

Generalization to n modes (block diagonal):

```
J = diag(J_q, J_q, ..., J_q) ∈ so(2n)     [n copies]
```

### Commutant result (Cycle 70, reproduced here)

The dimension of the subgroup of SO(2n) commuting with J:

```
dim({a ∈ so(2n) : [a, J] = 0}) = n²    [= dim(U(n))]
```

After factoring out the D5 U(1) global phase (1 generator), the residual gauge
symmetry between the n modes has dimension:

```
n² − 1 = dim(SU(n))
```

For n = 1, 2, 3: gauge boson counts are 0, 3, 8 — matching (no new bosons from D5 phase),
three W/Z bosons, eight gluons.

---

## Consistency Checks

| Check | Statement | Status |
|---|---|---|
| J² = −I from U(1) action | q² × (−I) = −I for |q|=1 | ✓ algebraic proof |
| J ∈ so(2n) | J is antisymmetric: Jᵀ = −J | ✓ block [[0,−1],[1,0]]ᵀ = [[0,1],[-1,0]] = −J |
| D6 modes carry U(1) charge | ∫j_x = −2π/(5ξ) ≠ 0 | ✓ Cycle 67c (exact) |
| Commutant dim U(2)=4 (D6) | dim({a∈so(4):[a,J]=0})=4 | ✓ Cycle 70 (numerical SVD) |
| Commutant dim U(3)=9 (D7) | dim({a∈so(6):[a,J]=0})=9 | ✓ Cycle 70 (numerical SVD) |
| J_gauge = J_Cycle70: identical matrix | Both are [[0,−1],[1,0]] per block | ✓ verified (d5_j_connection.py) |
| n=1 (D5): J = U(1) generator | The D5 U(1) group generator IS the complex structure | ✓ SO(2)=U(1) (Cycle 70) |
| Fractional charge normalizes to J | J_{norm} = J_q/|q| → J_{norm}² = −I for any q≠0 | ✓ algebraic |
| Why J is global (not local) | Gauge parameter θ is global → J acts uniformly on all modes | ✓ structural |
| Mode count n=2,3 at D6,D7 | One new mode per threshold crossing (codimension-1) | ✗ structural only |

---

## Tier Assessment Update

With the Cycle 71 result, the D-depth assignments upgrade as follows:

| Depth | Prior tier | New tier | Justification |
|---|---|---|---|
| D5 = U(1) | Tier 3 | **Tier 2 candidate** | Cycle 70: SO(2)=U(1) from real substrate |
| D6 = SU(2) | Tier 3 | **Tier 2 candidate** | Cycles 67c+70+71: full chain (assuming n=2 modes) |
| D7 = SU(3) | Tier 3 | **Tier 2 candidate** | Same chain (assuming n=3 modes at D7) |

"Tier 2 candidate" means: the derivation chain is logically complete, but one step
(the mode count n per threshold from substrate dynamics) remains structural rather than
derived. Tier 2 requires all four conditions including a runnable equation module; the
partial chain is now in `equations/d5_j_connection.py`.

A full Tier 2 promotion requires: (a) deriving the mode count from the substrate
field equation; (b) packaging the complete chain in a single runnable module.

---

## Connections

- `foundations/complex_zero_mode_gap.md` — 2 DOFs/mode from PDE; SO(2n)∩Aut(J)=U(n) (Cycle 70)
- `foundations/zero_mode_multiplet.md` — n complex modes → SU(n) (Cycle 59)
- `foundations/bifurcation_mode_count.md` — full Bottleneck 1 structural chain (Cycles 62–67c)
- `equations/complex_structure_derivation.py` — D6 modes charged in D5 background (Cycle 67c)
- `equations/u1_from_paired_modes.py` — commutant dim verified for n=1,2,3 (Cycle 70)
- `equations/d5_j_connection.py` — J from U(1) gauge action; verified J²=−I, same commutant (Cycle 71)
- `equations/gauge_coupling_zero_modes.py` — gauge coupling preserves n zero modes (Cycle 67)
- `foundations/depth_assignment.md` — Bottleneck 1 overview and context
