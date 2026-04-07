# Gauge Coupling Constants from DFC Substrate

## Status

> **Cycle 40:** This document formally maps the coupling constant derivation problem
> (Bottleneck 2). It identifies what has been derived, what has been established via
> consistency (Route 3B), and what remains genuinely open.
>
> **What is derived:** sin²θ_W = 0.231 from equal-coupling initial condition + SM RG
> running + k_Y = 3/5 from Dynkin normalization (Route 3B, Cycles 22 and 30).
>
> **What is open:** The value of the common coupling g_common at M_c from DFC substrate
> parameters (α, β, c). Until this is derived, α_em, g_W, and α_s are consistency
> checks, not predictions.

---

## The Three Coupling Constants

The Standard Model has three gauge coupling constants:

| Coupling | Group | Value at M_Z | Meaning |
|---|---|---|---|
| α₁ = g₁²/(4π) | U(1)_Y | 0.01696 | Hypercharge coupling |
| α₂ = g₂²/(4π) | SU(2)_L | 0.03375 | Weak isospin coupling |
| α₃ = g₃²/(4π) | SU(3)_c | 0.1182 | Strong coupling |

Plus the fine structure constant α_em = e²/(4πε₀ℏc) = α₁ α₂/(α₁ + α₂) × (evaluated
at the relevant scale). All three are inputs in the Standard Model. DFC aims to derive them.

---

## What Route 3B Has Established

### The Equal-Coupling Initial Condition (DERIVED, Cycle 22)

The DFC substrate produces all three gauge closures (D5=U(1), D6=SU(2), D7=SU(3))
from the same compression field with the same kinetic term:

```
L_kinetic = (c²/2) (∂φ/∂t)² − (c²/2) (∂φ/∂x)²
```

The same kinetic coefficient c applies at all three closure depths. This produces an
equal-coupling initial condition: at the co-crystallization scale M_c, the three
effective gauge couplings are equal:

```
g₁(M_c) = g₂(M_c) = g₃(M_c) = g_common    [STRUCTURAL — from common kinetic term]
```

In practice DFC uses the weaker condition g₁(M_c) = g₂(M_c) for the Weinberg angle,
since D5 and D6 share a co-crystallization stage while D7 closes independently.

### The Hypercharge Normalization (DERIVED, Cycle 30)

The k_Y = √(5/3) normalization factor (needed to put U(1)_Y on the same footing as
SU(2) and SU(3)) is derived from the Dynkin index matching condition on the SM matter
content, without invoking a GUT group:

```
k_Y² = Σ_fermions Y² / (N_fund/2)    [Dynkin trace normalization]
     = 5/3    [verified in equations/hypercharge_normalization.py]
```

This means g₁_normalized = k_Y × g₁_unnormalized = √(5/3) × g₁.

### Weinberg Angle (DERIVED FROM ABOVE, Cycle 22)

Starting from g₁(M_c) = g₂(M_c) with the k_Y = √(5/3) normalization:

```
sin²θ_W(M_c) = g₁²/(g₁² + g₂²) = 1/(1 + k_Y²) = 1/(1 + 5/3) = 3/8
```

Running from M_c ≈ 10¹³ GeV to M_Z using the SM one-loop beta functions:

```
sin²θ_W(M_Z) = 0.2312 ± 0.0002    [observed: 0.23122 ± 0.00003]
```

**This is the DFC's best current numerical prediction — derived, not fitted.**

### The Strong Coupling (CONSISTENT, not derived)

The α₃ ∩ α₁ crossing in SM running occurs at μ ≈ 2.4 × 10¹⁴ GeV (one-loop),
consistent with a separate D7 closure scale. The two-scale depth-running model
predicts M_c(D7) ≈ 10¹⁵ GeV from the α_s running. These are consistent but not
a derivation of α_s(M_Z) from substrate parameters.

---

## The Missing Step: g_common from (α, β, c)

All of the above uses SM RG running to connect M_c to M_Z — the SM does the heavy
lifting. The genuinely DFC piece is the equal-coupling initial condition and k_Y = 3/5.
But the VALUE of g_common at M_c is not derived — it is taken from SM running backwards.

**What is g_common at M_c?**

From `equations/gauge_couplings.py`, the SM couplings at M_c(12) ≈ 10¹³ GeV are:

```
1/α₁(10¹³) ≈ 43.9
1/α₂(10¹³) ≈ 41.3    ← nearly equal (5% off)
1/α₃(10¹³) ≈ 34.2

At exact crossing: 1/α_common ≈ 42.6  →  α_common ≈ 0.0235  →  g_common ≈ 0.543
```

So the common coupling at M_c is approximately g_common ≈ 0.54. This is a specific
dimensionless number that a complete DFC derivation must reproduce from (α, β, c).

---

## The Derivation Structure

### What a first-principles coupling derivation requires

In Kaluza-Klein-type theories, the gauge coupling is the overlap between the matter
field profile and the gauge field mode profile, integrated over the internal geometry.
In DFC, the analogous calculation is:

```
g_DFC = ∫ φ_kink(x) × A_gauge(x) × dV    [schematic]
```

where:
- φ_kink(x) = φ₀ tanh(x/λ) is the kink background at D6 (matter source)
- A_gauge(x) is the gauge field mode arising from D5 closure moduli

For the U(1) gauge mode in DFC, the natural candidate is:
```
A_μ ~ ∂_μ θ    [gradient of the Goldstone phase of the U(1) closure]
```

The coupling is then the Wilson phase accumulated by the kink as it moves through the
gauge field:
```
g_U1 = (kink momentum) × (U(1) holonomy per unit length) × (kink size)
```

### Dimensional analysis estimate

The natural dimensionless combination from the substrate parameters at the closure scale:

```
g_DFC ~ α_Dc / M_c²    [where α_Dc is the substrate α at depth Dc]
```

Using M_c = √(α_D5/2):

```
g_DFC ~ α_D5 / (α_D5/2) = 2    [dimension analysis alone gives O(1)]
```

Dimensional analysis gives g ~ 2, α_gauge ~ 4/(4π) ≈ 0.32. This is too large by a
factor of ~14 compared to the observed α_common ≈ 0.0235.

The missing suppression: geometric factors from the specific Hopf fibration topology
(S¹ → S³ → S² for U(1), S³ → S⁷ → S⁴ for SU(2), S⁵ ↪ ℂ³ for SU(3)). The actual
coupling computation requires integrating over the fiber, not just the base.

### The holonomy integral (open calculation)

For the U(1) closure at D5, the S¹ fiber has circumference 2π × r_U1. The coupling
is the ratio of the kink's U(1) charge to the gauge field normalization. In DFC terms:

```
g_U1 = 2π × (winding number of kink around S¹) / √(S¹ volume in substrate units)
      = 2π / √(2π × r_U1 / λ_D5)
```

where r_U1 is the U(1) closure radius and λ_D5 is the D5 kink width. The ratio
r_U1/λ_D5 is the key unknown — it sets the geometric suppression.

For g_U1 = 0.54 (= g_common):

```
r_U1/λ_D5 = (2π / g_U1)² / (2π) = 2π / g_U1² = 2π / 0.29 ≈ 21.6
```

The U(1) closure radius is ~22 kink widths at D5. This is a concrete numerical target
for the Route B Hopf fibration calculation.

---

## The Path to α_em

Once g_common is derived, the rest follows:

### Step 1: From g_common to sin²θ_W

Already done (Route 3B): sin²θ_W = 3/8 at M_c → 0.231 at M_Z. ✓

### Step 2: From g₁, g₂ to g_em

The electromagnetic coupling at M_Z:

```
1/α_em = 1/α₁ × cos²θ_W + 1/α₂ × sin²θ_W    [tree-level mixing]

More precisely: e = g₁ g₂ / √(g₁² + g₂²) = g₂ sin θ_W = g₁ cos θ_W

α_em(M_Z) = e²/(4π) = α₂(M_Z) × sin²θ_W(M_Z) = 0.03375 × 0.231 ≈ 0.0078
           = 1/128    [consistent with observed 1/(127.9) ✓]
```

At low energy, QED running gives α_em(0) = 1/137. ✓

**If** g_common is derived from DFC, then g₂(M_c) = g_common and all subsequent
values follow from RG running — a complete chain from substrate to α_em.

### Step 3: From g₃ to α_s

The strong coupling at the D7 closure scale M_c(D7) would equal g_common (from the
same equal-coupling initial condition). Running from M_c(D7) ≈ 10¹⁵ GeV to M_Z:

```
1/α₃(M_Z) = 1/α_common + (7/(2π)) × ln(M_c(D7)/M_Z)
           ≈ 42.6 + 7/(2π) × ln(10¹⁵/91) ≈ 42.6 − 29.3 ≈ 8.5  [using SM running]
```

Wait — the SM beta function for SU(3) has b₃ = +7 (coupling weakens at high energy),
so running DOWN from M_c(D7) to M_Z means the coupling gets stronger:

```
1/α₃(M_Z) = 1/α₃(M_c) − (7/(2π)) × ln(M_c/M_Z)
           = 42.6 − (7/6.28) × 29.8 = 42.6 − 33.2 = 9.4
```

α₃(M_Z) ≈ 1/9.4 ≈ 0.106 vs observed 0.118 — 10% off with M_c(D7) ≈ 10¹⁵ GeV.
The M_c(D7) value is not yet precisely determined from substrate dynamics.

---

## Open Problems and Priorities

| Problem | Status | Priority |
|---|---|---|
| g_common from holonomy integral over D5 S¹ | OPEN | Critical (Bottleneck 2) |
| r_U1/λ_D5 from Route B Hopf structure | OPEN | Connects to Bottleneck 1 |
| M_c(D7) from substrate (gives α_s) | OPEN | High |
| sin²θ_W = 0.231 | DERIVED ✓ | Done |
| k_Y = 3/5 | DERIVED ✓ | Done |
| α_em(M_Z) = 1/128 | CONSISTENT ✓ | Follows from Route 3B |
| α_s(M_Z) = 0.118 | CONSISTENT ~10% | Needs M_c(D7) |

**The single most valuable calculation:** Compute the holonomy integral of the D5 U(1)
closure to get g_U1 in terms of (α_D5, β, c). This gives g_common without SM running,
and from g_common all three coupling constants follow.

The ratio r_U1/λ_D5 ≈ 21.6 is the key dimensionless target that the Hopf fibration
geometry at D5 must produce. See `foundations/depth_assignment.md` Route B for the
geometric candidate.

---

## Connections

- `foundations/embedding_geometry.md` — Route 3B: sin²θ_W = 3/8 at closure scale
- `foundations/hypercharge_normalization.md` — k_Y = 3/5 from Dynkin index matching
- `foundations/depth_assignment.md` — Route B: S¹ at D5, S³ at D6, S⁵ at D7
- `foundations/depth_running.md` — two-scale model; M_c(D5) from substrate
- `foundations/bifurcation_dynamics.md` — γ_D = (16/3)√β; β ≈ 0.035; M_c(D5) exact
- `equations/gauge_couplings.py` — numerical running; pairwise crossings
- `equations/weinberg_angle_rg.py` — full Route 3B derivation; g_common at M_c
- `equations/hypercharge_normalization.py` — k_Y = 3/5 numerical verification
- `equations/coupling_derivation.py` — STUB: holonomy integral, first-principles g
