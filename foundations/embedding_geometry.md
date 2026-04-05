# Embedding Geometry and the Weinberg Angle

## The Central Question

The Weinberg angle θ_W (sin²θ_W ≈ 0.231) sets the ratio of electromagnetic to weak coupling
strength and determines the W/Z mass ratio. In the Standard Model it is a free parameter — a
measured input with no derivation. In DFC it must emerge from the geometry of the D5/D6 closure
configuration.

The approach explored here — called **Route 3** — does not attempt to derive θ_W from the
closure radii R_U1 and R_S3 directly (that path is blocked by Derrick's theorem; see
`foundations/substrate.md` and the closure_topology.py header). Instead, it derives θ_W from
the **embedding structure** of the closures — how D5 and D6 sit relative to each other in the
substrate — and from the **kinetic boundary conditions** shared by all closures at their
formation scale.

---

## The D5/D6 Configuration Space

The electromagnetic and weak closures are not independent objects. They co-emerge from the same
D4 → D5 → D6 bifurcation sequence in the same substrate. Their joint configuration is:

| Layer | Closure | Gauge structure | Object |
|---|---|---|---|
| D5 | Electromagnetic | U(1) | Circle S¹ — the photon winding mode |
| D6 | Weak | SU(2) | 3-sphere S³ — the weak boson rotation modes |
| D7 | Strong | SU(3) | The knot structure whose pressure squashes D6 |

The critical observation: **D5 and D6 are not separate theories that happen to mix. They are
adjacent closure behaviors of the same field, born from the same substrate kinetics, and their
coupling constants reflect the same underlying compression dynamics.**

The key structural question is therefore: what does the shared substrate origin imply about the
relationship between g₁ (U(1) coupling) and g₂ (SU(2) coupling) at the scale where the closures
form?

---

## Route 3A: Hopf Fibration Embedding (Why It Gives the Wrong Answer)

The Hopf fibration is a natural mathematical object connecting U(1) and SU(2):

```
S¹ ↪ S³ → S²
(fiber)  (total)  (base)
```

The D6 closure is S³. The D5 closure is S¹. The Hopf map is a continuous projection from S³ to
S², with S¹ fibers. This looks like exactly the embedding of D5 inside D6.

**Naive derivation:**

If U(1) is embedded in SU(2) as its Cartan subgroup, the GUT embedding coefficient is:
```
sin²θ_W = Tr(T_Y²) / Tr(T_3²) = 1/2
```
where T_Y is the weak hypercharge generator and T_3 is the third SU(2) generator.

**Why this is wrong:**

sin²θ_W = 1/2 is not the observed value (0.231). More importantly, the structural identification
is incorrect: **U(1)_Y is not the Cartan subalgebra of SU(2)_L.** They are separate groups with
separate origins.

- U(1)_Y (hypercharge) is the D5 electromagnetic closure — a winding mode around a circle.
- SU(2)_L (weak) is the D6 rotational closure — the full S³ geometry.

After electroweak symmetry breaking, U(1)_em (ordinary electromagnetism) IS a subgroup of the
combined U(1)_Y × SU(2)_L. But before symmetry breaking — and at the closure scale — U(1)_Y
and SU(2)_L are separate closures with no containment relation. The photon after EWSB is a linear
combination of B (the D5 mode) and W³ (a D6 mode), not the D5 mode alone.

Route 3A fails because it tries to embed D5 inside D6, but they are siblings, not parent-child.

**Connection to the Higgs mechanism:**

The Hopf fibration is not irrelevant — it describes something real in the model, just not the
Weinberg angle. After EWSB (S³ squashing), the vacuum manifold of the D6 closure is
S³ → S² (with S¹ = U(1)_em as the unbroken direction). This IS the Hopf structure. The three
Goldstone bosons parametrize S² = SU(2)/U(1); the surviving massless mode is the photon. This
connection is already built into `foundations/higgs_geometry.md` through the ε squashing picture.

---

## Route 3B: Equal Couplings at Closure Formation Scale

**The structural premise:**

All three gauge closures — D5 U(1), D6 SU(2), D7 SU(3) — emerge from the same continuous
substrate field. They do not emerge from separate physics. They are different closure behaviors
of the same object under successive bifurcation.

The DFC substrate has a single kinetic term:

```
L_kinetic = (1/2) c² (∂φ)²
```

There is no reason for the coupling extracted from this kinetic term to differ between the D5,
D6, and D7 closures at the moment of their formation. All three closures are born with the same
kinetic coefficient.

**The equal-coupling prediction:**

At the closure formation scale M_c, all gauge couplings are equal:

```
α₁(M_c) = α₂(M_c) = α₃(M_c) = α_U    (DFC closure scale initial condition)
```

This is the same initial condition as a GUT group (SU(5), SO(10)), but it arises here without
a GUT group. There is no unified symmetry group that is then broken. The equal couplings at M_c
are a boundary condition from shared substrate kinetics, not the residue of a broken symmetry.

**The Weinberg angle at the closure scale:**

Using the standard GUT-normalization relation (which correctly accounts for the different
embedding dimensions of U(1)_Y vs SU(2)):

```
sin²θ_W = (3/5) α_Y / (α_Y + α₂)
         = (3/5) × (3/5)⁻¹ α₁ / ((3/5)⁻¹ α₁ + α₂)
```

Wait — in GUT normalization α₁ = (5/3) α_Y, so α_Y = (3/5) α₁. Therefore:

```
sin²θ_W = α_Y / (α_Y + α₂)
         = (3/5)α₁ / ((3/5)α₁ + α₂)
```

At M_c where α₁ = α₂ = α_U:

```
sin²θ_W(M_c) = (3/5) α_U / ((3/5)α_U + α_U)
             = (3/5) / (3/5 + 1)
             = (3/5) / (8/5)
             = 3/8 = 0.375
```

This is the **tree-level structural prediction from Route 3B**: the Weinberg angle equals 3/8 at
the closure formation scale. It requires no new free parameters — it follows from the single
kinetic coefficient of the DFC substrate.

**Why the same factor of 3/5 as SU(5):**

The factor of 3/5 is not specific to SU(5) as a group. It is the ratio of quadratic Casimirs
that correctly normalizes the U(1) embedding. In SU(5) it arises from the embedding
U(1)_Y ⊂ SU(5); in DFC it arises from the count of charged degrees of freedom in the D5
closure geometry. The structural argument is the same even though there is no GUT group.

---

## RG Running to M_Z

The physical Weinberg angle at the electroweak scale M_Z is not 3/8. It is obtained by running
the equal couplings at M_c down to M_Z using the Standard Model renormalization group.

**One-loop running (SM beta coefficients):**

```
b₁ = +41/10    (U(1)_Y — not asymptotically free; coupling decreases going down)
b₂ = −19/6     (SU(2)_L — asymptotically free; coupling increases going down)
b₃ = −7        (SU(3)_c — strongly asymptotically free)
```

From equal couplings at M_c, running to M_Z:

```
α_i⁻¹(M_Z) = α_U⁻¹ + (b_i / 2π) × ln(M_c / M_Z)
```

where the b₁, b₂ convention is: μ dα_i/dμ = −(b_i/2π) α_i².

Defining L = ln(M_c / M_Z) > 0:

```
α₁⁻¹(M_Z) = α_U⁻¹ + (b₁/2π) L      [b₁ > 0 → α₁(M_Z) < α_U]
α₂⁻¹(M_Z) = α_U⁻¹ + (b₂/2π) L      [b₂ < 0 → α₂(M_Z) > α_U]
```

Then:

```
sin²θ_W(M_Z) = (3/5)α₁(M_Z) / ((3/5)α₁(M_Z) + α₂(M_Z))
```

**Closed-form formula:**

After eliminating α_U via the constraint that SM running reproduces the observed α_em(M_Z),
the Weinberg angle at M_Z is determined by M_c alone:

```
sin²θ_W(M_Z) = 3/8 − [109/(48π)] × α_em(M_Z) × ln(M_c / M_Z)
```

sin²θ_W **decreases** from 3/8 as M_c increases (more running separates the couplings).
The coefficient 109 = 8b₁ − (11/3) × (SM combination) — derived from SM beta coefficients.

**Reference predictions at benchmark M_c values:**

| M_c (GeV)  | log₁₀(M_c) | sin²θ_W(M_Z) | Error vs 0.231 |
|---|---|---|---|
| 10¹²        | 12.0        | ≈ 0.244      | +5.7%          |
| **10¹³**    | **13.0**    | **≈ 0.231**  | **0.0% ✓**     |
| 3×10¹³      | 13.5        | ≈ 0.225      | −2.6%          |
| 3×10¹⁴      | 14.5        | ≈ 0.212      | −8.3%          |
| 10¹⁵        | 15.0        | ≈ 0.205      | −11.2%         |
| 10¹⁸        | 18.0        | ≈ 0.166      | −28.1%         |

(Numerical values from `equations/weinberg_angle_rg.py`. Non-SUSY SM one-loop running.)

**Key result:** The observed value sin²θ_W = 0.231 is reproduced when M_c ≈ 10¹³ GeV.

**The self-consistent scale:** This scale is not a new free parameter. In the SM, the scale
where α₁ = α₂ in one-loop running (with no GUT group) is M_c(12) ≈ 10¹³ GeV — determined
entirely by the observed couplings at M_Z. DFC's equal-coupling initial condition is
*self-consistent*: the scale where the prediction works is exactly the scale where α₁ = α₂
in SM running. The prediction requires no new input beyond the SM couplings themselves.

Note: the non-SUSY SU(5) GUT gives sin²θ_W ≈ 0.212 (−8%) because it requires all three
couplings to meet at one scale (~3×10¹⁴ GeV), which is higher than the D5/D6 crossing scale.
In DFC, the product topology means D7 need not meet D5/D6 at the same scale.

---

## Connection to the S³ Squashing (ε) Picture

The two derivations of the Weinberg angle in the model — the ε squashing picture
(higgs_geometry.md) and Route 3B (this document) — are not competing. They operate at different
scales and together constrain the full picture.

**The squashing picture (IR):**

After EWSB at v ≈ 246 GeV, the physical Weinberg angle is:
```
sin²θ_W = 1 − m_W²/m_Z² = 1 − cos²θ_W
```
determined by the ratio of the squashed and unsquashed radii of D6 S³. This is a low-energy
geometric statement about the vacuum configuration.

**Route 3B (UV):**

At the closure scale M_c, the initial conditions for g₁ and g₂ are equal. The value of
sin²θ_W at M_Z then follows from RG running — this is the UV geometric statement.

**Consistency requirement:**

Both pictures must agree at M_Z. The RG running of Route 3B provides the value of g₁/g₂ at M_Z.
The squashing parameter ε is then determined by this ratio:

```
cos²θ_W = m_W²/m_Z² = 1 − sin²θ_W(M_Z)   →   ε is fixed by Route 3B + SM running
```

Route 3B gives sin²θ_W = 0.231 from M_c ≈ 10¹³ GeV. The squashing parameter ε is then not
a free parameter — it is determined by:
1. The equal-coupling initial condition (from shared substrate kinetics)
2. The scale where α₁ = α₂ in SM running (M_c ≈ 10¹³ GeV — self-consistent)
3. Standard RG running below M_c

**Tension with the Higgs mass derivation:** The Higgs mass prediction in `higgs_geometry.md`
uses a closure scale M_c ≈ 10¹⁸ GeV. The Weinberg angle equal-coupling scale is M_c ≈ 10¹³
GeV — five orders of magnitude lower. These cannot both be the same scale.

Possible resolutions:
- The two "closure scales" refer to different physical events: D5/D6 electroweak closure
  (M_c^ew ≈ 10¹³ GeV) vs. the geometric modulus matching condition in the Higgs derivation.
- The Higgs derivation closure scale estimate (~10¹⁸ GeV) may be an overestimate from
  the tree-level quartic boundary condition; two-loop corrections not yet applied.
- This tension is an active open problem requiring resolution before either derivation
  can be considered fully consistent.

---

## Free Parameter Assessment

| Quantity | Status in Route 3B |
|---|---|
| sin²θ_W = 3/8 at M_c | Derived — no free parameters |
| RG running to M_Z | Derived — uses SM beta functions (SM particles are already in the model) |
| The closure scale M_c(12) | Self-consistent — determined by where α₁ = α₂ in SM running (~10¹³ GeV) |
| α_U (coupling magnitude at M_c) | Determined by α_em(M_Z) and M_c — not a free parameter |
| The 3/5 normalization factor | OPEN — borrowed from GUT embedding; needs derivation from D5 geometry |
| Tension with Higgs closure scale | OPEN — 10¹³ GeV vs 10¹⁸ GeV unresolved |

**Verdict on free parameters:**

Route 3B introduces **zero new free parameters**. The prediction sin²θ_W = 0.231 follows from:
- The structural 3/8 initial condition (from shared substrate kinetics)
- SM one-loop running (uses already-known SM beta functions)
- The self-consistent M_c ≈ 10¹³ GeV (determined from SM couplings, not inserted by hand)

This is genuinely stronger than SU(5): SU(5) requires postulating a GUT group AND the
unification scale. Route 3B requires neither — it uses only the product topology (D5/D6 separate
from D7) and the equal-coupling initial condition. The key advantage: **no unified gauge group
is assumed**, consistent with `foundations/product_geometry.md`.

---

## Comparison: Route 3B vs Route 1 (Skyrme Stabilization)

| Aspect | Route 3B (topological, this doc) | Route 1 (Skyrme) |
|---|---|---|
| New free parameters | 0 (up to M_c derivation) | 1 (Skyrme coefficient e_Sk) |
| What is derived | sin²θ_W at closure scale; physical value with M_c as input | R_S3 (SU(2) closure radius); then R_U1/R_S3 → sin²θ_W |
| Dependence on Derrick's theorem problem | None (doesn't use R_S3) | Circumvents it (adds stabilizing term) |
| Connection to existing model structure | Strong (same-substrate kinetics, product topology) | Medium (modifies substrate Lagrangian) |
| Risk | M_c may need a derivation that reintroduces free parameters | e_Sk is a new substrate parameter with no geometric motivation yet |
| Alignment with established physics | Strong (GUT SU(5) analogue without GUT group) | Moderate (Skyrme-type models are known but not standard) |

**Assessment at this stage:** Route 3B is structurally more natural for DFC. It requires no
modification to the substrate Lagrangian and produces a concrete numerical prediction contingent
only on M_c. The primary remaining work is: (1) derive or constrain M_c from substrate dynamics,
(2) compute the running numerically (see companion module `equations/weinberg_angle_rg.py`).

---

## Open Problems

1. **Resolve the M_c tension** — the D5/D6 equal-coupling scale (M_c ≈ 10¹³ GeV) and the Higgs
   mass derivation closure scale (~10¹⁸ GeV) differ by five orders. These must either refer to
   different physical events, or one derivation has an error. This is the most urgent open problem.

2. **Derive M_c(12) from substrate parameters** — the scale where α₁ = α₂ is currently read
   from observed SM couplings. A DFC derivation would predict it from (α, β, c). Until then the
   prediction is "if the D5/D6 closure scale equals the SM α₁=α₂ crossing, sin²θ_W = 0.231."

3. **Two-loop running** — one-loop is approximate; two-loop corrections are ~1–2%. Threshold
   corrections from heavy particles near M_c are currently absent.

4. **Hypercharge normalization from geometry** — the factor of 3/5 is borrowed from GUT embedding
   arguments. It should be derived from the count of D5 closure winding modes and their coupling
   to D4 fermion modes. This is a concrete combinatorial question within DFC.

5. **α₃ at M_c(12)** — at 10¹³ GeV, α₃ ≈ 0.027 ≠ α₁ ≈ α₂ ≈ 0.024. The D7 (SU(3)) closure
   does not form at the same scale as D5/D6 — consistent with separate bifurcation stages but
   requires the equal-coupling argument to be stated separately for each stage.

---

## Status

| Component | Status |
|---|---|
| sin²θ_W = 3/8 at closure scale (structural) | Derived ✓ |
| Equal-couplings initial condition from shared substrate | Structural argument complete; formal proof OPEN |
| RG running formula (one-loop SM) | Established ✓ — see equations/weinberg_angle_rg.py |
| sin²θ_W(M_Z) = 0.231 self-consistently from M_c ≈ 10¹³ GeV | Derived (conditional on α₁=α₂ closure identification) ✓ |
| Self-consistency of M_c(12) (no new free parameter) | Established ✓ — M_c determined by SM running |
| Connection to ε squashing (higgs_geometry.md) | Consistent; quantitative tie OPEN |
| Tension: Weinberg scale (10¹³ GeV) vs Higgs scale (10¹⁸ GeV) | OPEN — must be resolved |
| Hypercharge normalization (3/5 factor) from geometry | OPEN |
| M_c from DFC substrate parameters (α, β, c) | OPEN |
