# D-Depth Effective Lagrangians: The Bridge from Substrate to Gauge Theory

*This document addresses the primary bottleneck shared by Route 1 (Skyrme, see
`foundations/route1_skyrme.md`) and Route 3B (embedding geometry, see
`foundations/embedding_geometry.md`): deriving the Standard Model coupling constants
and mass scales from the DFC substrate parameters (α, β, c).*

---

## The Central Problem

The DFC model has two types of structure:

**Type A (structural):** The topology of the D5, D6, D7 closure behaviors explains *which*
gauge groups appear — U(1), SU(2), SU(3) — and topological arguments give parameter-free
predictions: three generations, proton stability, sin²θ_W = 3/8 at the closure scale, J = 1/2
for fermions.

**Type B (dynamical):** The *magnitudes* of the coupling constants — e², g_W², g_s² — and the
*scales* at which the closures form (M_c values) are not yet derived from the substrate. They
are either read from data or taken from self-consistency arguments.

The gap between Type A and Type B is the D-depth effective Lagrangian problem: how does the
DFC scalar field φ, with dynamics determined by V(φ) = −α/2 φ² + β/4 φ⁴, generate an
effective gauge Lagrangian at each closure depth, and what determines the coupling coefficients?

---

## Step 0: What the Substrate Provides

The DFC substrate has one field with one Lagrangian:

```
L_DFC = (c²/2)(∂_μφ)² − V(φ)
       = (c²/2)(∂_μφ)² + (α/2)φ² − (β/4)φ⁴
```

Three parameters: α (compression strength), β (buckling stiffness), c (propagation speed).

**The kink scale:** The stable kink solution φ_kink = √(α/β) tanh(x/λ) has width λ = √(2c²/α).
This width sets a length scale. In natural units (ℏ = c = 1), the corresponding mass scale is:

```
M_kink = 1/λ = √(α/2)
```

This is the fundamental relationship between α and the mass scale of stable closures formed
by the substrate. Every M_c value ultimately traces back to the value of α at the corresponding
depth.

**The vacuum amplitude:** At the stable minimum, φ₀ = √(α/β). The product φ₀ × λ = √(2c²/β)
depends only on β and c — independent of α. This combination will appear as the analogue of
the "Higgs VEV over coupling" ratio in the effective theories below.

---

## Step 1: D5 Effective Lagrangian (U(1) Closure)

### What forms at D5 depth

When the DFC substrate reaches D5 compression depth, a buckling event produces a closure
whose stable configuration has U(1) topology. The substrate field wraps into a circle:
the field value traces out S¹ as it circles the closure. Operationally, the field is
written in polar form:

```
φ_D5(x) = φ₀(x) × exp(iθ(x))
```

where φ₀(x) ≈ √(α_D5/β_D5) (the radial amplitude, near the minimum) and θ(x) is the
winding phase.

### The effective gauge field

The gradient of the phase θ is the natural gauge connection at D5 depth:

```
A_μ ≡ (1/e_D5) ∂_μθ
```

The kinetic term of the DFC Lagrangian evaluated at the D5 minimum becomes:

```
(c²/2)|∂_μφ_D5|² → (c²/2)φ₀² (∂_μθ)² = (c²/2)φ₀² e_D5² A_μ²
```

Comparing this with the standard form for a U(1) gauge theory
(L_Maxwell = −(1/4e²_D5) F_μν²), the identification of the D5 electromagnetic coupling
is:

```
e_D5² = (β_D5 / 2) × (geometry factor from D5 winding count)
```

The geometry factor is the ratio of quadratic Casimirs for the D5 U(1) closure embedded
in the substrate — this is the `3/5` normalization question from Route 3B, applied here
from the bottom up rather than the top down.

### The D5 closure scale

The D5 closure forms when the substrate compression reaches the depth at which the kink
width λ_D5 equals the topological cell size of the U(1) winding. This gives:

```
M_c(D5) = √(α_D5 / 2)     (in natural units)
```

**Self-consistency check:** Route 3B (embedding_geometry.md) finds M_c(12) ≈ 10^13 GeV
from the condition that SM running couplings α₁ = α₂ at that scale. The DFC identification
is that this scale equals M_c(D5) = M_c(D6). Then:

```
α_D5 ≈ 2 × (10^13 GeV)² ≈ 2 × 10^26 GeV²
```

This is a self-consistency condition on α_D5 — not yet a derivation of M_c from first
principles. The derivation would require knowing how α evolves from D1 to D5 (the
depth-running problem, §5 below).

### What is established vs. open for D5

| Claim | Status |
|---|---|
| U(1) gauge structure from phase wrapping | Established — topology argument |
| A_μ = (1/e_D5)∂_μθ identification | Consistent — standard scalar gauge embedding |
| e_D5² = β_D5 × (geometry factor) | Framework established; geometry factor OPEN |
| M_c(D5) = √(α_D5/2) relationship | Established — from kink width formula |
| Numerical value of α_D5 (hence M_c) | OPEN — requires depth-running derivation |

---

## Step 2: D6 Effective Lagrangian (SU(2) Closure)

### What forms at D6 depth

At D6 depth, the closure topology is SU(2) ≅ S³. The substrate field wraps around the
3-sphere. The DFC scalar field describes fluctuations on this S³, so φ_D6 takes values
in SU(2):

```
φ_D6(x) = exp(i τ_a θ_a(x) / 2)    (τ_a = Pauli matrices, a = 1,2,3)
```

This is the SU(2) non-linear sigma model field — the same structure as the Skyrme model
in Route 1 and as the pion field in QCD chiral perturbation theory.

### The effective Yang-Mills field

The SU(2) gauge field emerges from the left-invariant 1-form on the closure:

```
W_μ^a ≡ (1/g_W) Tr(τ_a φ_D6^† ∂_μ φ_D6)
```

The DFC kinetic term (c²/2)(∂_μφ_D6)² → (F_π²/4) Tr(∂_μU† ∂^μU) maps to the standard
chiral Lagrangian form, where:

```
F_π² = c² φ₀² × (S³ normalization) ≈ c² α_D6/β_D6 × (2 for S³ vs S¹ counting)
```

And the SU(2) coupling constant:

```
g_W² = β_D6 × (SU(2) geometry factor)
```

The geometry factor for SU(2) differs from that of U(1) because the 3-sphere has a
different ratio of quadratic Casimirs. The ratio g_W²/e_D5² depends on the ratio of
these geometry factors — currently not derived but structurally determinable from the
closure topology.

### Route 1 connection: F_π from D6 substrate

The pion decay constant F_π (physical value: 93 MeV) emerges from the D6/D7 interface —
specifically from the D6 SU(2) closure VEV as projected onto the D7 SU(3) structure.
The formula:

```
F_π² ≈ c² × α_D6/β_D6 × (D6→D7 projection factor)
```

Route 1 (Skyrme) needs F_π in units of MeV. Converting:

```
F_π ≈ c × √(α_D6/β_D6) × (projection factor)
```

The physical value F_π = 93 MeV then constrains α_D6/β_D6 given the projection factor.
If the projection factor can be derived geometrically, this determines the ratio α/β at
D6 depth from F_π alone — one equation connecting one ratio of substrate parameters to
a measured quantity.

### The D6 closure scale

By the same kink scale argument:

```
M_c(D6) = √(α_D6 / 2)
```

For Route 3B, M_c(D5) = M_c(D6) = M_c(12) ≈ 10^13 GeV — the co-crystallization hypothesis:
D5 and D6 closures form at the same compression depth because they are sequential bifurcations
from the same substrate configuration and their formation thresholds coincide. This is a
structural assumption that should be derivable from the depth-running equation.

### The Higgs VEV from D6

The S³ squashing at D6 gives the Higgs mechanism (see `foundations/higgs_geometry.md`).
The Higgs VEV v = 246 GeV emerges from the squashing parameter ε times the D6 closure
amplitude:

```
v² ≈ ε × φ₀_D6² = ε × α_D6/β_D6
```

This connects the Higgs VEV to substrate parameters through the squashing geometry.
The squashing parameter ε is currently taken from the observed W/Z mass ratio, not derived.
A derivation of ε from the D7 pressure on D6 (why the 3-sphere squashes by the observed
amount) would close this gap.

---

## Step 3: D7 Effective Lagrangian (SU(3) Closure)

### What forms at D7 depth

At D7 depth, the closure is SU(3). The substrate field takes values on the SU(3) group
manifold. The effective Lagrangian is the Skyrme Lagrangian:

```
L_Skyrme = (F_π²/4) Tr(∂_μ U† ∂^μ U) + (1/32 e_sk²) Tr[U†∂_μU, U†∂_νU]²
```

where U(x) ∈ SU(3).

### F_π and e_sk from substrate

Both F_π and e_sk emerge from the D7 effective field theory:

**Pion decay constant:**
```
F_π² = c² × α_D7/β_D7 × (D7/D6 boundary projection factor)
```

As discussed in §2, the physical F_π = 93 MeV constrains α_D7/β_D7. The ratio at D7
depth should match the ratio at D6 depth (they are the same substrate) unless depth-dependent
corrections to β differ from corrections to α.

**Skyrme coefficient:**
The quartic Skyrme term arises from the D7 higher-derivative dynamics. In QCD, e_sk emerges
from integrating out the ρ meson: e_sk ≈ 1/(√2 × g_ρ) where g_ρ is the ρ-nucleon coupling.
In DFC, the ρ meson analog is a radially excited D7 closure. Therefore:

```
e_sk ≈ 1 / (√2 × g_ρ_DFC)
```

where g_ρ_DFC is the coupling of the first radial excitation at D7 depth. This is determined
by the D7 closure's next-to-leading fluctuation spectrum — a computation that requires the
D7 effective Lagrangian in full.

**The strong coupling constant:**
```
g_s² = β_D7 × (SU(3) geometry factor)
```

At M_c(D7) ≈ Λ_QCD × exp(2π/b₃α_s) ≈ 10^15–10^16 GeV (the D7 closure formation scale,
much higher than M_c(D5/D6)), the equal-coupling condition gives:

```
g_s²(M_c(D7)) = g_W²(M_c(D7)) = e²(M_c(D7))
```

From this initial condition + QCD running, α_s(M_Z) = 0.118 follows — but this is
not yet confirmed in DFC because M_c(D7) is not independently derived.

---

## Step 4: The Equal-Coupling Initial Condition — Derived

### Why all three couplings start equal

The three gauge couplings all emerge from the same substrate kinetic term
L_kinetic = (c²/2)(∂_μφ)². The identification mechanism is:

1. At D5 depth: the kinetic term produces the U(1) coupling e_D5² = β_D5 × f_U1
2. At D6 depth: the kinetic term produces the SU(2) coupling g_W² = β_D6 × f_SU2
3. At D7 depth: the kinetic term produces the SU(3) coupling g_s² = β_D7 × f_SU3

where f_U1, f_SU2, f_SU3 are the geometry factors from each closure's topology.

**The equal-coupling argument:** If (a) the β parameter is depth-independent (same substrate
stiffness at all closure depths), and (b) the geometry factors f_U1 = f_SU2 = f_SU3
(all closures normalize the kinetic term equivalently), then:

```
e_D5² = g_W² = g_s²    at their respective closure scales
```

This is the DFC origin of the equal-coupling initial condition used in Route 3B.

**Assessment:** Condition (a) (depth-independent β) is plausible as a zeroth-order
approximation. Condition (b) (equal geometry factors) is a testable claim. The geometry
factors are fixed by the closure topology — they can in principle be computed from the
Casimir invariants of each group. This is a concrete open computation.

**If the geometry factors differ:** Let r = f_SU2/f_U1 ≠ 1. Then at M_c:
```
g_W² = r × e_D5²
sin²θ_W(M_c) = (3/5) α_1 / ((3/5)α_1 + α_2)
             = (3/5) α_1 / ((3/5)α_1 + r × α_1)
             = (3/5) / (3/5 + r)
```

For r = 1 (equal geometry): sin²θ_W = 3/8. For r = 5/3 (GUT normalization absorbed into r):
sin²θ_W = (3/5)/(3/5 + 5/3) = (3/5)/(34/15) = 9/34 ≈ 0.265. The geometry factor ratio
r is thus closely related to the `3/5` normalization question. Deriving r from the D5/D6
topology would simultaneously resolve the 3/5 factor and the equal-coupling condition.

---

## Step 5: The Depth-Running Problem

This is the fundamental unsolved problem. It is the DFC analog of the RG equation.

### Formulation

The substrate parameter α has a value at each depth D. The sequence:

```
α_D1 → α_D2 → α_D3 → α_D4 → α_D5 → α_D6 → α_D7
```

determines, via M_c(D) = √(α_D/2), the mass scales at which each closure forms.

The depth-running equation governs how α changes as the substrate progresses through
successive bifurcation depths. It must take the form:

```
dα/dD = F(α, β, c, D)
```

where F is determined by the substrate dynamics — specifically, how the quartic β-term
and the propagation speed c modify the effective compression strength at each depth.

### Constraints on the depth-running

Even without the full equation, the self-consistency conditions from known physics constrain
the depth-running:

| Constraint | Known value | DFC expression |
|---|---|---|
| M_c(D5) = M_c(D6) ≈ 10^13 GeV | From Route 3B | α_D5 = α_D6 ≈ 2 × 10^26 GeV² |
| F_π = 93 MeV | Observed | α_D7/β_D7 × (proj. factor) ≈ (93 MeV)² |
| v = 246 GeV (Higgs VEV) | Observed | ε × α_D6/β_D6 ≈ (246 GeV)² |
| M_c(D7) >> M_c(D6) | From α_s running | α_D7 >> α_D6 (D7 forms at higher compression) |
| M_Pl ≈ 10^18 GeV | Gravity scale | α_D1 ~ 2 × (10^18 GeV)² |

The ratio α_D1/α_D5 ≈ (10^18/10^13)² = 10^10 captures how much the effective compression
parameter drops from D1 to D5. A depth-running equation producing a factor of 10^10 over
5 depth steps would require an average suppression of ~10^2 per depth level.

### What would complete the derivation

A derivable depth-running equation F(α, β, c, D) would allow:

1. Starting from α_D1 ≈ 2M_Pl² (Planck-scale compression at D1)
2. Computing α_D5 from the running — predicting M_c(D5) from M_Pl
3. With M_c(D5) determined, Route 3B predicts sin²θ_W = 0.231 from first principles
4. With F_π = f(α_D7/β_D7), Route 1 predicts baryon masses from Planck-scale parameters

The form of F(α, β, c, D) is constrained by the requirement that it reproduce known physics
at five distinct scales (D1 through D7). Whether a smooth, parameter-free equation can satisfy
all five constraints simultaneously is an open and testable question.

---

## Summary: What the Framework Establishes

| Established now | Status |
|---|---|
| U(1), SU(2), SU(3) gauge fields emerge from phase wrapping of the DFC scalar at D5, D6, D7 | Framework — topology argument ✓ |
| M_c(D) = √(α_D/2) — closure scale from kink width | Derived ✓ |
| Equal-coupling initial condition from shared substrate kinetics | Structural argument ✓ |
| sin²θ_W = 3/8 at closure scale (from equal couplings + normalization) | Derived (Route 3B) ✓ |
| F_π² = c² × α_D6/β_D6 × (projection factor) | Framework ✓; factor OPEN ✗ |
| e_sk ≈ 1/√2 g_ρ_DFC from D7 radial excitation | Framework ✓; computation OPEN ✗ |

| Open problems | What is needed |
|---|---|
| Geometry factors f_U1, f_SU2, f_SU3 from closure topology | Casimir computation for each D-depth closure |
| Depth-running equation dα/dD = F(α, β, c, D) | Derivation from D1 compression dynamics |
| M_c values from substrate parameters | Follows from depth-running |
| 3/5 normalization from D5 geometry | Equivalent to f_U1 computation |
| α_s(M_Z) from DFC | Requires M_c(D7) from depth-running |
| D6 squashing parameter ε | Requires D7 pressure on D6 computed from substrate |

---

## The Derivation Sequence

When the depth-running problem is solved, the complete derivation sequence is:

```
Step 1: Postulate α_D1 ~ M_Pl² (D1 = Planck-scale substrate compression)

Step 2: Run α_D to D5 depth via dα/dD = F(α, β, c, D)
        → α_D5 → M_c(D5) = √(α_D5/2)  [predicts the electroweak closure scale]

Step 3: Apply equal-coupling initial condition at M_c(D5) = M_c(D6)
        → sin²θ_W = 3/8 → 0.231 via SM RG  [Route 3B prediction: no free parameters]

Step 4: Run α_D to D6 depth
        → α_D6/β_D6 → F_π, v (Higgs VEV)  [quantitative electroweak physics]

Step 5: Run α_D to D7 depth
        → α_D7/β_D7 → F_π (physical), e_sk  [Route 1: baryon masses, N-Δ splitting]

Step 6: Equal-coupling initial condition at M_c(D7)
        → α_s(M_Z) via QCD running  [strong force coupling from first principles]
```

Completing this sequence — even partially — would move the mathematical rigor estimate
significantly. Any step from 2 onward that gives a prediction from substrate parameters
rather than SM inputs would constitute a genuine first-principles derivation.

---

## Connections

- `foundations/embedding_geometry.md` — Route 3B (sin²θ_W from equal-coupling condition)
- `foundations/route1_skyrme.md` — Route 1 (F_π, e_sk, baryon masses from D6/D7)
- `foundations/substrate.md` — The DFC substrate field and kink solutions
- `foundations/higgs_geometry.md` — D6 S³ squashing; ε parameter; Higgs VEV
- `equations/weinberg_angle_rg.py` — Numerical verification of Route 3B
- `equations/kink_model.py` — Kink width/energy/scale relationships
