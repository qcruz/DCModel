# Depth-Running of the Substrate Compression Parameter

## The Central Problem

The DFC substrate's compression parameter α sets the mass scale of closures at each
depth: M_c(D) = √(α_D / 2). Two scales are known:

```
M_c(D1) ≈ M_Pl = 1.22 × 10^19 GeV    (Planck-scale compression — D1 anchor)
M_c(D5) ≈ M_c(D6) ≈ 10^13 GeV         (Route 3B — D5/D6 co-crystallization)
```

These constrain α across the depth sequence. But the *mechanism* governing how α
evolves from D1 to D5/D6/D7 — the depth-running equation — is not yet derived from
the substrate mechanics.

The depth-running equation takes the schematic form:

```
α_{D+1} = α_D × (1 − γ_D)

where γ_D = fraction of compression budget consumed at the D-th bifurcation
```

This document explores what forms of γ_D are consistent with known constraints and
what new predictions they produce.

See `equations/depth_running.py` for all numerical results.

---

## What the Data Require

Three constraints fully characterize the depth-running across D1→D7:

**Constraint 1: Planck anchor**
```
α_D1 = 2 × M_Pl² ≈ 2 × (1.22 × 10^19 GeV)²
```

**Constraint 2: D5/D6 co-crystallization**
```
M_c(D5) ≈ M_c(D6)   (within factor ~2)
→ γ_{D5→D6} ≈ 0     (negligible compression consumed at the D5→D6 transition)
```

**Constraint 3: D5 at Route 3B scale**
```
M_c(D5) = 1.02 × 10^13 GeV
→ total suppression from D1 to D5: α_D5/α_D1 = (M_c(D5)/M_Pl)² ≈ 10^{−12.2}
```

These three constraints rule out two simple models and select a two-scale structure.

---

## Models Explored

### Model 1: Uniform γ (falsified by co-crystallization)

If γ is the same at every depth step:

```
M_c(D) = M_Pl × (1−γ)^{(D−1)/2}
```

Fitting to M_c(D5) = 10^13 GeV gives γ_uniform ≈ 0.9906. The prediction at D6:

```
M_c(D6) = M_c(D5) × (1−γ) ≈ 10^13 × 0.009 ≈ 9 × 10^{10} GeV
```

D5/D6 ratio ≈ 110. This contradicts the co-crystallization requirement
M_c(D5) ≈ M_c(D6).

**Result: Uniform depth-running is falsified by the equal-coupling Route 3B result.
The co-crystallization of D5 and D6 at the same scale demands that γ_{D5→D6} ≈ 0.**

### Model 2: DOF-weighted γ (falsified)

If γ is proportional to the number of new degrees of freedom opened at each depth:

```
γ_D ∝ n_DOF(D+1)    (where U(1)→1 DOF, SU(2)→3 DOF, SU(3)→8 DOF)
```

This correctly places D5 at 10^13 GeV but gives D5/D6 ratio ≈ 100 (SU(2) opens 3×
more DOF than U(1), causing 3× more suppression at D5→D6). Falsified for the same
reason as Model 1.

### Model 3: Two-scale (established — co-crystallization satisfied)

**Key insight from co-crystallization:** The near-zero suppression at D5→D6 means
the D5 (U(1)) and D6 (SU(2)) closures form from the same substrate configuration —
they co-emerge as adjacent behaviors of the same D4→D5/D6 bifurcation.

The two-scale model partitions depth transitions into two regimes:

```
Spacetime depths (D1→D5):  γ_space ≈ 0.9991  (large suppression per step)
Gauge co-emergence (D5→D6): γ_weak  ≈ 0        (co-crystallization)
```

With 4 uniform spacetime steps from M_Pl to M_c(D5):

```
(1 − γ_space)^4 = (M_c(D5)/M_Pl)^2 = (10^{13}/1.22×10^{19})^2 ≈ 10^{−12.2}
γ_space ≈ 1 − 10^{−3.05} ≈ 0.9991
```

Results (γ_weak = 0.001):
```
D1: 1.22 × 10^19 GeV  (M_Pl — input)
D2: 3.69 × 10^17 GeV
D3: 1.12 × 10^16 GeV
D4: 3.37 × 10^14 GeV
D5: 1.02 × 10^13 GeV  (Route 3B target — input)
D6: 1.02 × 10^13 GeV  (co-crystallization ✓ — D5/D6 ratio = 1.001)
D7: depends on γ_color [open]
```

**This model is self-consistent and requires only one free parameter (γ_space) fixed by
the M_Pl → M_c(D5) ratio. Co-crystallization is satisfied by construction.**

---

## The D7 Scale: A New Prediction Target

With D5/D6 co-crystallization established, the D7 closure (SU(3)) is the remaining
unknown. Two approaches:

### Approach A: γ_color as free parameter

M_c(D7) = M_c(D6) × √(1 − γ_color)

γ_color can range from ≈ 0 (D7 co-crystallizes with D6) to ≈ 1 (D7 forms at very
low energy). Any value is geometrically possible from the depth-running alone.

### Approach B: Equal-coupling initial condition at D7

Route 3B uses equal coupling at D5/D6: α₁(M_c(D5)) = α₂(M_c(D6)) ≈ 0.024.
If the same initial condition applies at D7 — the SU(3) closure also starts with
α_U ≈ 0.024 — then M_c(D7) is determined by SM running of α_s:

```
1/α_s(M_c(D7)) = 1/α_s(M_Z) + (7/2π) × ln(M_c(D7)/M_Z)

Setting α_s(M_c(D7)) = α_U ≈ 0.024:
1/0.024 = 1/0.118 + (7/2π) × ln(M_c(D7)/91.2 GeV)
→ M_c(D7) ≈ 7.9 × 10^14 GeV  (log10 ≈ 14.9)
```

**Prediction: M_c(D7) ≈ 8 × 10^14 GeV from the equal-coupling condition on SU(3).**

This is numerically close to — but distinct from — the GUT scale (~3 × 10^15 GeV for
non-SUSY SU(5)). It's above M_c(D5/D6) by a factor of ~80.

---

## A Structural Surprise: Depth-Order vs. Energy-Order

The equal-coupling prediction M_c(D7) ≈ 8 × 10^14 GeV > M_c(D5/D6) ≈ 10^13 GeV
has a significant implication: **the SU(3) closure formed at higher compression
(higher energy) than the electroweak closures.**

In the current D-depth labeling convention, D7 > D6 > D5 means "deeper compression."
But if the SU(3) closure forms at higher energy, it formed *earlier* in the
compression sequence — at a *lower* depth number by the current convention.

Two resolutions:

**Resolution A: Invert the gauge depth ordering.**
Assign SU(3) to D5 (first gauge closure, highest compression), SU(2) to D6, U(1) to
D7. The "depth" label then corresponds consistently to decreasing energy:
```
D5: SU(3) at 8 × 10^14 GeV  [first to close]
D6: SU(2) at ~10^13 GeV      [second]
D7: U(1)  at ~10^13 GeV      [co-crystallizes with D6]
```
This requires renaming the depth assignments across all documents — a significant
change but self-consistent.

**Resolution B: D-depth labels are not energy-ordered.**
D-depth labels the *bifurcation sequence from D1*, not the energy scale. The
compression field can bifurcate at D6 (U(1)) before D5 (SU(3)) if the SU(2)/U(1)
co-crystallization threshold is reached after a different compression pathway than
the SU(3) threshold. In this view, "deeper" means "more bifurcations from D1,"
not "higher energy."

**The model as described (D5=U(1), D6=SU(2), D7=SU(3)) is consistent with
Resolution B** — depth labels bifurcation sequence, and the SU(3) closure forms
at a higher *energy* even though it requires *more* bifurcations from D1.

This needs further derivation but is not an immediate inconsistency. The D-depth
assignments are provisional working hypotheses (see CLAUDE.md).

---

## Physical Picture of the Two-Scale Depth-Running

Why would γ_space >> γ_weak? The physical argument:

**Spacetime bifurcations (D1→D4) open macroscopic structure.** The bifurcations that
produce apparent spatial localization (D3) and inertia (D4) redistribute large amounts
of compression budget into the degrees of freedom that define 3+1 dimensional behavior.
These are the "expensive" bifurcations — each one opens structure that the entire
subsequent universe organizes around. Large γ is natural: most of the Planck-scale
compression is consumed creating the apparent spacetime structure.

**Gauge co-emergence (D5→D6) is cheap.** Once the electroweak threshold is reached,
the substrate explores U(1) and SU(2) closure configurations quasi-simultaneously.
They co-emerge because they are two aspects of the same D4→gauge bifurcation event —
the splitting of the gauge-capable compression into its winding modes. The energy
difference between U(1) and SU(2) closure formation is small compared to the
compression budget spent reaching that threshold.

This physical picture is consistent with the SM: the electroweak symmetry group
SU(2)_L × U(1)_Y describes two independent closures that happen to form at the same
compression threshold — they emerge together but are topologically distinct from the
moment of their formation. The product topology of DFC means they are forever
independent — not a single force that later separates, but two separate closures
that co-emerge simultaneously at the same threshold energy.

---

## What Would Complete the Derivation

The two-scale model identifies γ_space as the key parameter. It is currently fitted
to reproduce M_c(D5). A derivation from substrate mechanics would compute:

```
γ_space = f(α, β, c)
```

The physical content: when the substrate undergoes a bifurcation at depth D, what
fraction of the compression budget (parameterized by α) is irreversibly committed
to the new degree of freedom?

A natural candidate: the kink energy at depth D as a fraction of the total
compression energy available:

```
γ_D ≈ E_kink(D) / E_total(D) = (4/3)c√(2α_D³/β) / (α_D²/(4β) × L)
```

where L is the coherence length of the substrate. This ratio depends on L — the
size of the substrate patch undergoing bifurcation — which connects to the
cosmological horizon problem (why does the substrate bifurcate coherently?).

The horizon problem's DFC counterpart: coherent bifurcation requires the substrate
at D1 to have sub-D3 connectivity (see `phenomena/cosmology/big_bang.md`). The
coherence length L that enters γ_D may be determined by this pre-D3 connectivity.

If L ~ λ_D1 = √(2c²/α_D1) (Planck length at D1), then:
```
γ_space = (4/3)c√(2α³/β) × (4β) / (α² × λ_D1 × c) = (16/3) × √(2α/β) / λ_D1
         = (16/3) × √(2α/β) × √(α/2)/c = (16/3) × α / (c√β)
```

This connects γ_space to the substrate parameters (α, β, c) and the Planck length.
Whether this produces γ_space ≈ 0.999 is a computation that remains open.

---

## Summary

| Claim | Status |
|---|---|
| Uniform depth-running is inconsistent with D5/D6 co-crystallization | Established ✓ |
| Two-scale model: γ_space >> γ_weak ≈ 0 satisfies all D1–D6 constraints | Established ✓ |
| M_c(D5) = M_c(D6) ≈ 10^13 GeV from two-scale model | Satisfied by construction ✓ |
| M_c(D7) ≈ 8 × 10^14 GeV from equal-coupling initial condition on SU(3) | Predicted (conditional) |
| Depth-ordering ≠ energy-ordering for gauge closures | Structural finding — open |
| Deriving γ_space from (α, β, c) | OPEN — the key remaining derivation |
| Co-crystallization mechanism (why γ_D5→D6 ≈ 0) | Physical argument given; formal derivation OPEN |

---

## Connections

- `foundations/d_depth_lagrangians.md` — M_c(D) = √(α_D/2) relationship
- `foundations/embedding_geometry.md` — Route 3B; M_c(D5) = 10^13 GeV from SM running
- `equations/depth_running.py` — all numerical models and constraint tables
- `equations/weinberg_angle_rg.py` — confirms M_c(12) = 1.02 × 10^13 GeV
- `phenomena/cosmology/big_bang.md` — pre-D3 substrate connectivity (coherence length L)
