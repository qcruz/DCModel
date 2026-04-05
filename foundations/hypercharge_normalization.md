# Hypercharge Normalization: k_Y = 3/5 Derived from DFC

## Status

> **Previously:** k_Y = 3/5 borrowed from SU(5) GUT embedding — listed as an open
> problem in `foundations/embedding_geometry.md`.
>
> **Now:** k_Y = 3/5 derived from DFC's own equal-coupling condition and SM matter
> content. No unified gauge group assumed or needed.
> Verified numerically in `equations/hypercharge_normalization.py`.

---

## The Problem

Route 3B (see `foundations/embedding_geometry.md`) derives sin²θ_W = 3/8 at the
closure scale M_c from the equal-coupling initial condition. The derivation requires
a normalization factor k_Y relating the canonical U(1) coupling g₁ to the physical
hypercharge coupling g_Y:

```
α₁ = (1/k_Y) × α_Y    →    sin²θ_W = (k_Y α_Y) / (k_Y α_Y + α₂)
```

At M_c with equal couplings α₁ = α₂ = α_U:

```
sin²θ_W(M_c) = k_Y / (k_Y + 1)
```

For k_Y = 3/5: sin²θ_W(M_c) = (3/5)/(8/5) = 3/8 exactly.

The same factor k_Y = 3/5 appears in SU(5) grand unification, where it comes from
embedding U(1)_Y inside SU(5). Previously this embedding was the only known source of
the factor, making Route 3B appear to borrow silently from GUT assumptions. This
document gives a derivation that requires no GUT group.

---

## The Derivation

### Step 1: What "equal coupling" requires

The DFC substrate has one kinetic term: L_kinetic = (c²/2)(∂φ)². At M_c, the D5
closure produces the U(1) gauge field and the D6 closure produces the SU(2) gauge
field, both from the same kinetic term. Equal coupling means both couplings are
extracted with the **same normalization convention**.

The standard SU(2) convention normalizes generators in the fundamental representation
so that:

```
Tr(T^a T^b) = (1/2) δ^{ab}    [SU(2) fundamental, standard convention]
```

This gives the Dynkin index T(doublet) = 1/2 for the SU(2) fundamental representation.

For the equal-coupling condition to be meaningful — for α₁(M_c) = α₂(M_c) to make
sense — the U(1)_Y generator must be normalized with the **same Dynkin index convention**.
That is: the normalization k_Y must be chosen so that the U(1) Dynkin index matches
the SU(2) Dynkin index over one complete generation of matter.

### Step 2: Compute T(SU2) per generation

The SU(2)_L Dynkin index from one generation of SM matter:

| Representation | N_color | Dynkin index | Contribution |
|---|---|---|---|
| Q_L = (u_L, d_L) doublet | 3 | T = 1/2 | 3 × 1/2 = 3/2 |
| L_L = (ν_L, e_L) doublet | 1 | T = 1/2 | 1 × 1/2 = 1/2 |
| u_R, d_R, e_R singlets | — | T = 0 | 0 |

```
T(SU2) per generation = 3/2 + 1/2 = 2
```

### Step 3: Compute Σ Y² per generation

The U(1)_Y Dynkin index sums Y² over every left-handed Weyl fermion:

| Fermion | N_color | Y | N_color × Y² |
|---|---|---|---|
| u_L (in Q_L) | 3 | +1/6 | 3 × 1/36 = 1/12 |
| d_L (in Q_L) | 3 | +1/6 | 3 × 1/36 = 1/12 |
| ν_L (in L_L) | 1 | −1/2 | 1 × 1/4  = 1/4  |
| e_L (in L_L) | 1 | −1/2 | 1 × 1/4  = 1/4  |
| u_R          | 3 | +2/3 | 3 × 4/9  = 4/3  |
| d_R          | 3 | −1/3 | 3 × 1/9  = 1/3  |
| e_R          | 1 | −1   | 1 × 1    = 1    |

Summing:

```
Σ Y² = 1/12 + 1/12 + 1/4 + 1/4 + 4/3 + 1/3 + 1
     = 2/12 + 6/12 + 16/12 + 4/12 + 12/12
     = 40/12 = 10/3
```

### Step 4: Solve for k_Y

The equal-coupling normalization condition:

```
k_Y × Σ Y² = T(SU2)
k_Y × (10/3) = 2
k_Y = 2 × (3/10) = 6/10 = 3/5
```

This is the **unique normalization** that makes U(1)_Y and SU(2)_L Dynkin indices
consistent with each other — the one required for "equal coupling" to be a
well-defined statement.

### Step 5: Verify the Weinberg angle

With k_Y = 3/5 and equal couplings at M_c:

```
sin²θ_W(M_c) = k_Y / (k_Y + 1) = (3/5) / (3/5 + 1) = (3/5) / (8/5) = 3/8 = 0.375
```

Running to M_Z via SM one-loop beta functions (from `equations/weinberg_angle_rg.py`
and `equations/hypercharge_normalization.py`):

```
sin²θ_W(M_Z) = 3/8 − [109/(48π)] × α_em(M_Z) × ln(M_c/M_Z)
             = 0.231335     [with M_c = 1.02 × 10^13 GeV]

Observed:    sin²θ_W(M_Z) = 0.23122
Error:       +0.050%   ✓
```

---

## Why the Same Factor Appears in SU(5)

SU(5) grand unification gives k_Y = 3/5 from a different starting point: the
embedding U(1)_Y ⊂ SU(5) requires the hypercharge generator to sit inside the
SU(5) Lie algebra with the correct normalization for the 5-dimensional fundamental
representation. The calculation in SU(5):

```
T(SU(5) fundamental, T_Y generator) = Tr(T_Y²) = 3/5 × Tr(T_3²)  →  k_Y = 3/5
```

The two derivations agree because **they are computing the same thing from different
angles**: the unique normalization of Y consistent with the SM matter content. SU(5)
arrives at this through group theory (a complete 5 representation); DFC arrives at it
through the equal-coupling physical condition. Both use the SM matter content; neither
has a free choice.

The key difference is that DFC's derivation requires **no unified gauge group**. SU(5)
exists and predicts proton decay; DFC uses product topology U(1) × SU(2) × SU(3)
and forbids proton decay (see `foundations/product_geometry.md`). Both give k_Y = 3/5.

---

## What This Means for Route 3B

The Route 3B derivation chain is now complete at each step:

| Step | Claim | Source | Status |
|---|---|---|---|
| Equal couplings at M_c | All closures from same substrate kinetics | DFC structural | ✓ Derived |
| k_Y = 3/5 | Dynkin normalization condition on SM matter | **This document** | ✓ **Derived** |
| sin²θ_W(M_c) = 3/8 | k_Y / (k_Y + 1) | Algebra | ✓ Derived |
| RG running to M_Z | SM one-loop beta functions | SM (already in model) | ✓ Verified |
| sin²θ_W(M_Z) = 0.231 | Result at M_c(12) = 10^13 GeV | `weinberg_angle_rg.py` | ✓ Verified |
| M_c(12) = 10^13 GeV | Self-consistent with SM running | Self-consistent | OPEN |

One open item remains: deriving M_c(12) from substrate parameters (α, β, c) rather
than identifying it as the SM α₁ = α₂ crossing scale. This is the key bottleneck
identified in `foundations/d_depth_lagrangians.md`.

---

## Anomaly Cancellation as Independent Check

The hypercharge assignments used in the k_Y derivation (Y from Q = T₃ + Y) must
also satisfy the gauge anomaly cancellation conditions. All four conditions check out
for one generation:

| Anomaly condition | Value | Verified |
|---|---|---|
| U(1)³ = Σ_L Y³ − Σ_R Y³ | 0 | ✓ |
| SU(2)² × U(1) = Σ_{doublets} Y × N_c | 0 | ✓ |
| SU(3)² × U(1) = Σ_{quarks} (L−R) × Y × n_weyl | 0 | ✓ |
| Gravitational × U(1) = Σ_L Y − Σ_R Y | 0 | ✓ |

All four conditions canceling simultaneously is a non-trivial constraint on Y. The SM
hypercharge assignments satisfy all four — this is why the SM is anomaly-free. The
same assignments produce k_Y = 3/5.

---

## Connections

- `foundations/embedding_geometry.md` — Route 3B; Open Problem 4 (3/5 factor) resolved here
- `foundations/d_depth_lagrangians.md` — general framework; Open Problem on k_Y factor
- `equations/hypercharge_normalization.py` — numerical verification; k_Y = 3/5 exactly ✓
- `equations/weinberg_angle_rg.py` — RG running to M_Z; +0.050% error ✓
- `foundations/product_geometry.md` — why DFC uses product topology (no GUT group)
- `foundations/three_generations.md` — SM matter content from DFC closure topology
