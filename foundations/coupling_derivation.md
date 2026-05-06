# Gauge Coupling Constants from DFC Substrate

## Status

> **Cycle 40 (original mapping):** Formally mapped the coupling constant derivation
> problem (Bottleneck 2). Identified what is derived vs open.
>
> **Cycle 42:** g² = 8πβ/3 heuristically derived from kink phase stiffness f²=(4/3)φ₀²/λ
> → holonomy formula. g_common = 0.5423 vs SM 0.5443 (0.37%). α_em(M_Z) = 1/129.6 (1.3%
> off). Tier 3 heuristic — physical derivation of r_U1/λ remains open.
>
> **Cycle 47:** f² = (4/3)φ₀²/λ proved exactly via ∫sech⁴(u)du = 4/3 (Bogomolny
> identity, Cycle 47). This is the rigorous foundation of the phase stiffness.
>
> **Cycle 85:** Compact form g² = 2π×β×I₄ proved equivalent to g²=8πβ/3. α-independence
> proved across 3 decades (error <10⁻¹⁰). Eight candidate r_U1 definitions scanned;
> only 3/(4β) = 1/(β×I₄) matches SM at −0.5%. Route B worldvolume normalization
> (64π/9)M_c verified algebraically (error 1.6×10⁻¹⁶).
>
> **Cycle 87:** β = 3g_common²/(8π) = 0.03536 (+0.75% from reference 0.0351) —
> Route F self-consistency. If Bottleneck 2 closes, β is NOT a free parameter.
>
> **Cycle 96:** mode_norm = 9/(64π) ≈ 0.04476 PROVED algebraically from KK matching
> with zero free parameters (error 0.00e+00). Seven vortex BVP candidates tested;
> closest is simple KK 1/r_U1 = 4β/3 = 0.04667 (4.3% from target). Physical route
> (deriving mode_norm from V(φ) field equation alone) still open.
>
> **Cycle 100:** B2 ↔ β-derivation structural equivalence PROVED. The 3-step chain
> (P1) f²=I₄φ₀²/λ [Cycle 47, exact] → (P2) r_U1=λ/(βI₄)=3λ/(4β) [algebraic identity,
> α-independent] → (P3) g²=2πλ/r_U1=2πβI₄=8πβ/3 [KK holonomy] is complete given β.
> Self-consistent β_B2=27/(256π)≈0.03357 makes mode_norm=9/(64π) exactly (error
> 0.00e+00) and gives g²=9/32 (exact), g=3/(4√2)≈0.5303 (−2.57% vs SM 0.5443), but
> degrades M_W from −0.88% to −2.92%. The 4.25% gap between simple KK (4β/3=0.04667)
> and target (9/(64π)=0.04476) equals the 4.3% difference between β_ref=0.035 and
> β_B2=27/(256π). Closing B2 = deriving β from V(φ); once β is fixed, g² follows
> automatically with zero additional free parameters. See
> equations/bottleneck2_beta_selfconsistency.py.
>
> **Cycle 101:** Candidates (a) kink-width=L_Pl, (b) S_kink/ℏ=n, (c) ΔV/E_kink=const
> all shown BLOCKED: (a) fixes α not β; (b) gives E_kink/M_c=8/(3β), α-dependent;
> (c) ΔV/E_kink=3√(2α)/16, β-free. NEW candidate (d): β=1/(9π) from Hopf fiber
> dimension sum — dim(S¹)+dim(S³)+dim(S⁵) = 1+3+5 = 9 at D5/D6/D7. This gives
> g²=8/27 exactly (=(2/3)³, error <2×10⁻¹⁶) and g=√(8/27)=2√2/(3√3)=0.54433,
> matching SM g_common=0.5443 to 0.006%. Also: r_U1/λ=27π/4≈21.21 (0.91% from
> target 21.4). Status: Tier 3 structural argument; formal derivation from V(φ)
> KK normalization over S¹×S³×S⁵ product fiber is the remaining open step.
> See equations/beta_constraint.py.
>
> **Cycle 103:** β=1/(9π) self-consistency formalized. Two routes for r_U1/λ:
> (A) 1/(βI₄) [kink holonomy]; (B) πN_Hopf/I₄ [Hopf Laplacian sum, Obata theorem].
> Equating → β=1/(9π), g²=8/27. λ₁(S^d)=d proved (error 0.00e+00). N_Hopf=9 exact.
> M_W error improves 0.88%→0.50%. TIER 4 OPEN: show r_U1/λ=πN_Hopf/I₄ from V(φ).
> See `equations/beta_from_laplacian.py`.
>
> **Cycle 105:** KEY FINDING — mode_norm = 9/(64π) is β-INDEPENDENT (β cancels
> exactly in the full KK formula). The "4.3% gap" (Cycles 96–103) between simple KK
> (4β/3) and target 9/(64π) was a red herring: simple KK ≠ full formula. Full formula
> is trivially satisfied for any β. Vortex BVP cannot constrain β via this route.
> REVISED OPEN STEP: derive g² = 2I₄/N_Hopf = 8/27 from V(φ), or equivalently
> derive β = 1/(9π) from a constraint external to the KK chain.
> β_B2=27/(256π) solved the wrong condition (simple KK); gives g=0.5303 (−2.57%).
> β=1/(9π) [Hopf dim sum] gives g=0.54433 (0.006% vs SM) — best available candidate.
> Candidate routes: (A) equal-coupling IC + product fiber S¹×S³×S⁵ → β=1/(9π);
> (B) Z₂ kink two-sidedness → coefficient 2 in g²=2I₄/N_Hopf.
> See `equations/gauge_coupling_from_fiber.py`.
>
> **Current status:** g² = 8πβ/3 is Tier 3 (heuristic, 0.006% at β=1/(9π)).
> Proved: f² exact (P1); r_U1=1/(βI₄) algebraic identity (P2); g²=2πβI₄ compact
> form (P3); mode_norm=9/(64π) β-independent identity (P4, Cycle 105).
> Candidate: β=1/(9π) from Hopf dim sum 1+3+5=9 → g²=8/27 (0.006% vs SM).
> Open: derive g²=2I₄/N_Hopf=8/27 directly from V(φ) without β as input.

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
| g_common from holonomy integral over D5 S¹ | OPEN (physical route) | Critical (Bottleneck 2) |
| r_U1/λ_D5 = 1/(β×I₄) from V(φ) alone | OPEN — algebraic identity proved, physical derivation open | Critical |
| f² = (4/3)φ₀²/λ from Bogomolny identity | PROVED ✓ (Cycle 47) | Done |
| g² = 2π×β×I₄ compact form, α-independence | PROVED ✓ (Cycle 85) | Done |
| mode_norm = 9/(64π) algebraic proof | PROVED ✓ (Cycle 96, error 0.00e+00) | Done |
| β self-consistent from Route F | Tier 3 (Cycle 87, 0.75% off) | Done when B2 closes |
| M_c(D7) from substrate (gives α_s) | OPEN — target 2.094×10¹⁵ GeV | High |
| sin²θ_W = 0.231 | DERIVED ✓ (Route 3B) | Done |
| k_Y = 3/5 | DERIVED ✓ (Cycle 30) | Done |
| α_em(M_Z) = 1/129.6 | Tier 2a, 1.3% off ✓ | Improves when B2 closes |
| α_s(M_Z) = 0.118 | 11% off — needs M_c(D7) | High |

**The critical next calculation:** Identify the vortex coupling kernel K(ρ) such that
∫K(ρ)dρ = 9/(64π) directly from the D5 vortex BVP field equation and V(φ), without
using g² as input. The closest known candidate is the simple KK normalization
1/r_U1 = 4β/3 (4.3% off). The 4.3% correction arises from non-trivial vortex geometry
and has not yet been identified analytically.

The ratio r_U1/λ_D5 ≈ 21.4 (= 3/(4β) at β = 0.035) is the key dimensionless target.
See `equations/bottleneck2_2d_integral.py` for the systematic candidate scan (Cycle 96).

---

## Connections

- `foundations/embedding_geometry.md` — Route 3B: sin²θ_W = 3/8 at closure scale
- `foundations/hypercharge_normalization.md` — k_Y = 3/5 from Dynkin index matching
- `foundations/depth_assignment.md` — Route B: S¹ at D5, S³ at D6, S⁵ at D7
- `foundations/depth_running.md` — two-scale model; M_c(D5) from substrate
- `foundations/bifurcation_dynamics.md` — β ≈ 0.035; M_c(D5) exact; NOTE: γ_D = (16/3)√β
  was RETRACTED Cycle 48 (BPS-correct E_kink gives 8/3 universal, β-independent)
- `foundations/phase_stiffness_derivation.md` — f² = (4/3)φ₀²/λ proved (Cycle 47);
  holonomy gap precisely located; Route A and Route B identified
- `equations/gauge_couplings.py` — numerical running; pairwise crossings
- `equations/weinberg_angle_rg.py` — full Route 3B derivation; g_common at M_c
- `equations/hypercharge_normalization.py` — k_Y = 3/5 numerical verification
- `equations/coupling_derivation.py` — g²=8πβ/3 chain; α_em(M_Z)=1/129.6; Tier 2a
- `equations/bottleneck2_coupling_integral.py` — compact form g²=2πβI₄; α-independence;
  8 candidate r_U1 definitions; Route B normalization verified (Cycle 85)
- `equations/worldvolume_coupling.py` — Bottleneck 2 gap precisely mapped; r_U1=3λ/(4β)
  algebraic identity; Route B matching formula; vortex candidates (Cycle 88)
- `equations/bottleneck2_2d_integral.py` — mode_norm=9/(64π) proved algebraically;
  seven vortex BVP candidates; simple KK 4.3% from target (Cycle 96)
- `equations/beta_substrate.py` — Route F: β=0.03536, 0.75% (Cycle 87)
