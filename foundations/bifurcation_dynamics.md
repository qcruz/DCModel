# Bifurcation Dynamics: Deriving γ_space from Substrate Parameters

## Status

> **Cycle 32 claim RETRACTED in Cycle 48.** The central result γ_D = (16/3)√β was
> derived using an incorrect kink energy formula:
>
> **Wrong:** `E_kink = (4/3) c √(2α³/β)` — overstates E_kink by a factor of 2√β
> **Correct (BPS):** `E_kink = (4/3) c² φ₀²/λ = (4/3) c α^(3/2)/(β√2)`
>
> With the correct formula, the ratio E_kink / E_total(λ) = **8/3** exactly —
> a universal constant independent of α, β, and c. Since 8/3 > 1, the interpretation
> of this ratio as a "compression fraction" γ_D ∈ (0, 1) fails. The γ_D = (16/3)√β
> result is retracted. The β ≈ 0.035 inference that followed from it is also retracted
> as a derivation (β remains at Tier 3 — a reference value, not derived).
>
> What remains valid: the depth-running integration, the M_c(D5) reproduction,
> the Planck-length self-consistency check, and the D-label disambiguation.
> See `equations/bifurcation_dynamics.py` for the corrected numerical verification.

---

## The Bifurcation Mechanism

The DFC substrate obeys:

```
V(φ) = −(α/2) φ² + (β/4) φ⁴
```

The vacuum sits at φ₀ = √(α/β), and the kink solution interpolates between ±φ₀:

```
φ_kink(x) = φ₀ tanh(x / λ)

where:
  λ = √(2c²/α)     [kink width / coherence length]
  φ₀ = √(α/β)      [vacuum field value]
```

The kink energy (mass of one topological closure) is (BPS-correct formula,
derived from the Bogomolny identity and verified by direct numerical integration):

```
E_kink = (4/3) c² φ₀²/λ = (4/3) c α^(3/2)/(β√2)

NOTE: A previous formula (4/3) c √(2α³/β) was incorrect — it overstates
E_kink by a factor of 2√β. See foundations/phase_stiffness_derivation.md.
```

A **bifurcation event** occurs when the substrate reaches a compression threshold where
it cannot continue compressing in the current mode without opening a new degree of freedom.
This is a buckling instability: the kink cannot compress further along its current axis,
so it sheds energy by creating a new orthogonal mode. That new mode is a higher D-depth
layer.

The fraction of the compression budget consumed by this bifurcation event is γ_D — the
key parameter in the depth-running equation α_{D+1} = α_D × (1 − γ_D).

---

## γ_D Derivation Attempt and Retraction (Cycle 32 → Cycle 48)

### Step 1: Energy budget within one coherence volume

The natural spatial scale for the bifurcation event is one kink coherence length λ. Within
this region, the total compression energy available to the substrate is the potential energy
density integrated over the coherence volume:

```
E_total(λ) = |V_min| × λ = (α²/4β) × λ
```

where V_min = −α²/(4β) is the depth of the double-well potential minimum.

Substituting λ = √(2c²/α) = c√(2/α):

```
E_total(λ) = (α²/4β) × c√(2/α) = (c√2 / 4β) × α^(3/2)
```

### Step 2: Ratio with BPS-correct E_kink

Using the correct kink energy E_kink = (4/3) c α^(3/2)/(β√2):

```
γ_D = E_kink / E_total(λ)
    = [(4/3) c α^(3/2)/(β√2)] / [(c√2/4β) × α^(3/2)]
    = (4/3) × (4β)/(β × √2 × √2)
    = (4/3) × 4/2
    = 8/3  ≈ 2.667
```

All α, β, c dependence cancels. The ratio is the universal constant 8/3 — independent
of every substrate parameter.

### Why this is not γ_D

Since 8/3 > 1, this ratio cannot be a "compression fraction" γ_D ∈ (0, 1). The
E_total(λ) = |V_min| × λ measure is smaller than E_kink: a single kink contains more
energy than the potential-energy-density × width product. This means E_total(λ) is not
the right normalization for the compression budget.

The Cycle 32 result γ_D = (16/3)√β arose from substituting the wrong E_kink formula
(which was smaller by a factor of 2√β). With the wrong formula, the ratio was
(16/3)√β ≈ 0.999 at β = 0.035 — numerically close to 1 and physically plausible as
a compression fraction, but built on an error. The derivation is **retracted**.

### What would be needed for a valid γ_D derivation

To derive a physical compression fraction from the kink model, the right framework is:

```
γ_D = E_kink / E_total(L)
```

where L is a macroscopic length scale much larger than λ. If L is the coherence length
of the full substrate field (rather than one kink width), then E_total(L) ≫ E_kink and
γ_D ≪ 1 naturally. But L must be derived from the substrate dynamics — it cannot be
postulated without undermining the derivation. This remains an open problem.

---

## Connection to the Two-Scale Depth-Running Model

The depth-running model requires a compression fraction γ_space such that:

```
M_c(D5) = M_Pl × (1 − γ_space)^2   →   γ_space ≈ 0.9991
```

The Cycle 32 claim was that β could be inferred from γ_space via γ = (16/3)√β. This
inference is **retracted**. The depth-running integration remains valid with γ_space
treated as an independent fitted parameter. The M_c(D5) reproduction is self-consistent
but does not derive β from first principles.

### What the depth-running model does correctly

With γ_space as input (not derived from β), the depth-running equation:

```
α_{D+1} = α_D × (1 − γ_space)
```

correctly reproduces the closure scale hierarchy from D1 to D5:

```
M_c(D5) ≈ 1.02 × 10^13 GeV  (matches Route 3B target, error < 0.001%)
```

The D1 anchor M_c(D1) = M_Pl with α_D1 = 2M_Pl² is self-consistent, and the kink width
at D1 equals the Planck length (see below). These structural results are unaffected by
the γ_D retraction.

### Status of β ≈ 0.035

The value β ≈ 0.035 is retained as a **Tier 3 reference value** — not derived from first
principles. It was previously inferred from the (wrong) γ_D formula; it now stands only
as a value consistent with: (a) the kink width at D1 = Planck length, and (b) the
heuristic coupling derivation g² = 8πβ/3 (Cycle 42, also heuristic). Deriving β from
a pre-substrate condition is the highest-priority open problem in the model.

---

## Why γ → 0 at the D5/D6 Gauge Co-Emergence

Even without a derived γ_D, the structural argument for co-crystallization remains:

The γ → 0 behavior at D5/D6 can be understood by considering L >> λ:

```
γ = E_kink / E_total(L) = E_kink / [(α²/4β) × L]
```

As L → ∞, γ → 0 regardless of α, β, or c. The D5/D6 gauge closures involve a coherence
length L_macro >> λ_D5, so their γ is genuinely close to zero. This argument is structural
and survives the retraction of the γ_D = (16/3)√β formula (which was specifically for L = λ).

1. **Different length scale:** By D5/D6, the substrate has organized into a structure whose
   coherence length is not λ_D5 but L_macro >> λ_D5. The total compression energy in the
   denominator is E_total(L_macro) >> E_kink, driving γ → 0.

2. **Co-emergence from the same event:** The D5 (U(1)) and D6 (SU(2)) closures emerge as
   two aspects of a single bifurcation event. The energy budget for this bifurcation is
   shared between both closures; neither individually consumes a large fraction.

3. **Physical consequence:** Because γ_{D5→D6} ≈ 0, the D6 closure forms at the same
   energy scale as D5. This is the DFC account of electroweak structure: U(1) and SU(2)
   do not unify by merging into a simple group — they co-crystallize because they emerge
   from the same substrate event with the same compression budget.

---

## The D-Label Ambiguity: Two Schemes in the Repository

**Important note for readers of the codebase.**

Two different D-label schemes appear in the repository and must not be confused:

**Scheme A** (`equations/bifurcation.py`, `foundations/dimensional_stack.md`):
- D-labels index particle mass scales as observed
- D5 = electron (0.511 MeV), D6 = muon (105.7 MeV), D7 = ΛQCD (0.2 GeV)
- D10 = electroweak (246 GeV)
- This scheme describes the phenomenological mass hierarchy

**Scheme B** (`equations/depth_running.py`, `foundations/depth_running.md`,
`foundations/embedding_geometry.md`, Route 3B):
- D-labels index gauge closure thresholds
- D5 = U(1) gauge closure at M_c ≈ 10^13 GeV
- D6 = SU(2) gauge closure (co-crystallizes with D5)
- D7 = SU(3) gauge closure at ≈ 8 × 10^14 GeV
- This scheme derives from the depth-running model and Route 3B

These are **different mappings** of the same continuous substrate. The unification of both
schemes — showing how the gauge closure thresholds (Scheme B) determine the particle mass
spectrum (Scheme A) through the folding dynamics — is an open problem.

The Route 3B derivations (Weinberg angle, hypercharge normalization, depth-running) all
use Scheme B. When reading `bifurcation.py` or `dimensional_stack.md`, mentally append
"(Scheme A)" to any D-label.

---

## What Remains Open

Three open problems survive the Cycle 48 retraction:

### 1. γ_D from a valid energy normalization

The ratio E_kink / E_total(λ) = 8/3 > 1, so E_total(λ) = |V_min|×λ is not a valid
compression budget. A valid derivation must identify an energy normalization E_norm > E_kink
that depends on β (so γ_D = E_kink/E_norm is β-dependent and < 1). The macroscopic
coherence length argument (γ → 0 for L >> λ) shows the direction: E_norm = |V_min|×L for
some substrate-derived L. Identifying L from the kink dynamics is the key step.

### 2. β from a pre-substrate principle

The quartic coupling β is currently a Tier 3 reference value (β ≈ 0.035) without a
derivation. A complete account would compute β from a fundamental starting point — perhaps
from the topology of the D1 state itself, or from the self-consistency condition that the
kink solution be stable at the Planck scale.

### 3. α from β and c

The substrate has three parameters: α, β, c. The closure scale formula M_c = √(α/2)
fixes the combination α_D1 ≈ 2 M_Pl² in GeV². The kink width λ = c√(2/α_D1) then fixes
the coherence length. With β ≈ 0.035 derived above, the remaining free parameter is c
(the substrate propagation speed, normalized to 1 in natural units but potentially
carrying information about the pre-geometric substrate).

### Self-consistency check: kink width at D1 = Planck length

With α_D1 = 2 M_Pl² and c = 1 (natural units):

```
λ_D1 = √(2/α_D1) = √(2 / (2 M_Pl²)) = 1/M_Pl = l_Planck
```

The kink coherence length at D1 is the Planck length to 0.1%. This is not put in by
hand — it follows from the D1 anchor M_c(D1) = M_Pl together with the formula
M_c = √(α/2). The DFC substrate is internally self-consistent: the smallest stable
excitation at D1 has a size equal to the Planck length.

---

### 3. Why exactly 4 macroscopic bifurcations (D1→D4)

Without a valid γ_D derivation, the number-of-bifurcations question is even more open.
The model does not yet explain why the sequence terminates at D4 and transitions to
closed gauge modes at D5.

The open/closed transition (why D5+ forms compact topological loops rather than open
propagating modes) must come from a different argument — one related to the topology of
the available closed manifolds at each compression depth.

---

## Summary

| Claim | Status |
|---|---|
| Bifurcation mechanism is buckling instability of kink potential | Established ✓ |
| E_kink = (4/3) c² φ₀²/λ (BPS-correct, Bogomolny identity) | Proved ✓ (Cycle 48) |
| γ_D = (16/3)√β derived from E_kink / E_total(λ) | **RETRACTED** (Cycle 48) — used wrong E_kink |
| E_kink(BPS) / E_total(λ) = 8/3 exactly (universal constant) | Proved ✓ (Cycle 48) |
| β ≈ 0.035 from γ_space ≈ 0.9991 requirement | RETRACTED as derivation — β is Tier 3 reference |
| M_c(D5) ≈ 10^13 GeV from depth-running (γ_space as input) | Verified ✓ |
| Kink width at D1 = Planck length (self-consistency) | Verified ✓ |
| γ_{D5→D6} → 0 from macroscopic coherence length argument | Physical argument ✓; formal derivation OPEN |
| D-label ambiguity (Scheme A vs B) documented | Documented ✓ |
| γ_D ∈ (0,1) derivation from substrate with correct E_kink | OPEN — requires deriving L from dynamics |
| β from pre-substrate principle | OPEN |
| Why open/closed transition at D4→D5 | OPEN |

---

## Connections

- `foundations/depth_running.md` — two-scale model; γ_space as input
- `foundations/substrate.md` — DFC kink model; V(φ) = −α/2 φ² + β/4 φ⁴
- `equations/bifurcation.py` — Scheme A D-label assignments (particle mass spectrum)
- `equations/depth_running.py` — Scheme B D-label assignments (gauge closure thresholds)
- `equations/bifurcation_dynamics.py` — E_kink/E_total = 8/3 verified; gamma_from_beta() RETRACTED (label present)
- `foundations/embedding_geometry.md` — Route 3B; M_c(D5) = 10^13 GeV
