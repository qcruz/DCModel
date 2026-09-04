# Module 28 — Gravity from V(phi): The D4 Story

**Series:** DFC Educational Modules
**Prerequisite reading:** Module 01 (substrate and kinks), Module 04 (forces),
Module 14 (spacetime emergence)

**Last updated:** September 2026

---

## 1. The Question

DFC derives the strong, weak, and electromagnetic forces from closure topologies
of a single substrate with potential V(phi) = -alpha/2 phi^2 + beta/4 phi^4.
Can gravity emerge from the same potential?

This is the hardest question in the model. The other three forces arise from
topological structures at D5, D6, and D7 depths, with quantitative predictions
verified to sub-percent accuracy. Gravity — the D4 depth behavior — requires
showing that Newton's constant G_N is a consequence of alpha and beta, not an
independent input.

The current answer: **yes, to -0.57% accuracy, with zero free parameters.**

---

## 2. Why Gravity Is Different

The strong force binds quarks. The weak force mediates beta decay. Electromagnetism
propagates light. Each of these operates between specific types of substrate
closures at specific depth ranges.

Gravity is not like this. Gravity couples to everything that carries energy.
It does not select particles by type, charge, or closure topology. It responds
to the total energy-momentum content of the substrate configuration.

In DFC, this universality has a natural origin: every substrate excitation
carries energy, every energy concentration deforms the substrate, and that
deformation IS what gravity looks like from the perspective of objects living
on the substrate. But turning this intuition into a derived gravitational
coupling requires several concrete steps.

---

## 3. The Kink as a Domain Wall

The DFC kink — the localized solution phi(y) = phi_0 tanh(y/xi) — is not just
a one-dimensional soliton. It is a domain wall: a localized region of the
substrate separating two vacuum states (phi = +phi_0 and phi = -phi_0). What
appears as three apparent spatial degrees of freedom is the D3 localization
behavior on this wall. Particles and forces are closure behaviors concentrated
on the wall.

The wall has:

- **Width:** xi = sqrt(2/alpha) = 0.874 Planck lengths
- **Surface energy:** E_kink = 36 pi in Planck units
- **Vacuum field value:** phi_0 = sqrt(alpha/beta) = 8.608

These are all determined by alpha = cuberoot(18) and beta = 1/(9 pi), the
two parameters of V(phi).

---

## 4. The 1/r Potential — Derived, Not Assumed

The kink profile falls off exponentially in the transverse direction. This
cannot produce 1/r gravity directly. But sources (particles) are localized
ON the three-dimensional worldvolume. The Green's function of the
three-dimensional Laplacian is 1/(4 pi r) — so any localized source
interacting through the worldvolume automatically produces a 1/r potential.

The full Poeschl-Teller mode sum confirms this: the translational zero mode
gives exact 1/r at all distances. The continuum modes contribute less than
6% at the kink center and are exponentially suppressed beyond two kink
widths. The result is verified across 11 orders of magnitude.

**This is a T1 result — mathematically exact.**

---

## 5. The Key Discovery: Emergent Anti-de Sitter Geometry

Here is the central insight that resolves the gravitational coupling problem.

The DFC vacuum energy is:

V(phi_0) = -alpha^2 / (4 beta) = -48.55 (in Planck units)

This is **negative**. The substrate's equilibrium state has negative energy
density. The substrate's compression coordinate — the transverse direction
away from the kink — acquires an exponentially decaying energy profile.
This is mathematically identical to anti-de Sitter (AdS) geometry, but it
emerges from V(phi), not from a pre-existing ambient space.

The coupled equations for the kink and its transverse compression profile
(the DFGH formalism, after DeWolfe, Freedman, Gubser, and Horowitz) are:

```
A'' = -(1/6)(phi')^2
phi'' + 4A' phi' = V'(phi)
6(A')^2 = (1/4)(phi')^2 - (1/2)V(phi)     [constraint]
```

where A(y) is the warp factor describing how the substrate's energy density
varies along the compression coordinate y. The exponential e^{2A} controls
how strongly gravitational perturbations are concentrated near the kink.

At the vacuum (large y, where phi approaches phi_0 and phi' approaches zero),
the constraint equation reduces to:

6k^2 = -(1/2) V(phi_0) = alpha^2 / (8 beta)

The AdS curvature is therefore:

k = alpha sqrt(3 pi) / 4 = 2.011

This is entirely determined by V(phi). No additional parameters are needed.

---

## 6. Gravity Localization

In 1999, Randall and Sundrum demonstrated a mathematical result: when a
localized structure (domain wall) exists in a geometry with exponentially
decaying energy density, gravitational perturbations are automatically
confined to the wall's vicinity. The warp factor e^{2A} falls off
exponentially in the transverse direction, so the gravitational zero mode
has finite norm even though the compression coordinate extends without bound.

In DFC, this is not postulated — it is a consequence of V(phi). The
negative vacuum energy produces the exponential decay profile. The kink
produces the localized structure. The confinement of gravity follows
automatically. The Randall-Sundrum result is used here as a mathematical
theorem about exponential profiles and zero modes — not as a claim that
the substrate lives inside a pre-existing higher-dimensional space.

The effective Planck mass from this localization is:

M_4^2 = M_5^3 / k

where M_5^3 = 2 (fixed by the DFGH normalization) and k = 2.011.

Therefore:

M_4^2 = 2 / 2.011 = 0.994

The bending rigidity — the coefficient of the Ricci scalar in the
four-dimensional Einstein-Hilbert action — is:

kappa = M_4^2 / 2 = 1/k = 4 / (alpha sqrt(3 pi)) = 0.4972

The target value is 0.5000 (in Planck units).

**The error is -0.57%. Zero free parameters. T1 algebraic.**

---

## 7. Where the -0.57% Comes From

The entire gap traces to a single ratio:

alpha_DFC / alpha_exact = 18^(1/3) / (8/sqrt(3 pi)) = 1.0057

The DFC value alpha = cuberoot(18) = 2.6207 is 0.57% larger than the value
alpha = 8/sqrt(3 pi) = 2.6059 that would give kappa = 0.5000 exactly.

This gap has three possible interpretations:

1. **Thick-wall correction.** The thin-wall (Randall-Sundrum) formula
   assumes the domain wall is infinitely thin compared to the AdS radius.
   The DFC wall has k times xi = 1.76, meaning the wall thickness is
   comparable to the AdS radius. The thick-wall correction is expected
   to push kappa upward (toward 0.5), because the smooth transition
   region adds weight to the warp integral. The magnitude and sign are
   correct to close the gap, but the exact value requires solving the
   full coupled boundary value problem.

2. **A genuine prediction.** If the thick-wall correction turns out to be
   smaller than 0.57%, the remaining gap is a prediction: DFC says the
   gravitational coupling is slightly different from the thin-wall value.

3. **An identity waiting to be found.** The closeness of
   18^(1/3) to 8/sqrt(3 pi) may reflect a deeper algebraic relationship
   not yet identified.

---

## 8. Resolving the "Missing 93%"

Earlier analysis found that perturbative channels (scalar exchange, Sakharov
induced gravity, potential-sector coupling) account for only about 7% of the
observed gravitational coupling. The remaining 93% appeared to require
non-perturbative substrate compression dynamics.

The warp-factor analysis resolves this puzzle. The raw bending rigidity of
the kink profile is kappa_raw = 27.83 — about 56 times LARGER than the
target. The effective coupling is not built up from perturbative channels;
it is the result of the enormous raw rigidity being suppressed by the
AdS warp factor.

The suppression factor:

kappa_eff / kappa_raw = 0.4972 / 27.83 = 0.0179

This is approximately beta/2 = 1/(18 pi) = 0.0177 — another near-integer
relationship between the gravitational suppression and the substrate
quartic coupling.

The perturbative 7% and the warp-factor result are not contradictory.
They are different frameworks for the same physics: the perturbative
approach expands around flat space and finds the enhancement needed
(factor F = 22.87); the warp-factor approach works in the full
self-gravitating geometry and finds the suppression of the raw rigidity.
Both give gravitational couplings consistent with M_Pl^2 = 1.

---

## 9. What Remains Open

Despite the -0.57% result for the coupling coefficient, significant
structural questions remain:

### 9a. The Effective Metric

DFC does not yet have an explicit expression g_muv^eff[phi] — a metric as
a functional of the substrate field. The weak-field chain (mass produces
phi perturbation, which shifts local propagation speed, which defines an
effective metric) works and is frequency-independent (a key requirement).
But the strong-field behavior breaks down at the kink core.

### 9b. Spin-2 Structure

General relativity requires massless spin-2 gravitational waves with two
polarizations. A scalar field cannot produce spin-2 modes through its
derivatives alone (this is a proven theorem). The viable route is through
gauge fields on the worldvolume: SU(3) gauge degrees of freedom can form
spin-2 composites via the Sakharov induced gravity mechanism. This is
structurally viable but not yet computed in detail.

### 9c. The Thick-Wall Boundary Value Problem

The thin-wall formula gives kappa = 0.4972. The actual thick-wall value
requires solving the coupled kink-plus-warp-factor system self-consistently.
The shooting method fails (the kink solution sits on an unstable separatrix),
so a relaxation or collocation method is needed. This is a well-defined
numerical problem with no conceptual obstacles.

### 9d. Universal Coupling

Gravity must couple to ALL forms of energy-momentum equally (the equivalence
principle). DFC has the conceptual argument (every excitation carries energy,
energy deforms the substrate, deformation is the effective metric), but the
perturbative equivalence-principle mismatch is 2.1%. Whether the full
non-perturbative coupling eliminates this mismatch is not yet shown.

---

## 10. DFC's Claims About Gravity

1. **Gravity is emergent.** There is no fundamental graviton in the substrate
   spectrum. Gravity is what differential compression of the substrate looks
   like from within.

2. **The 1/r profile is derived** from the three-dimensional Green's function
   on the domain wall worldvolume.

3. **The gravitational scale is determined by V(phi).** The same potential
   that sets particle masses and coupling constants also determines
   kappa = 1/k = 0.4972, with zero additional inputs.

4. **The mechanism is Randall-Sundrum localization,** but it is not
   postulated — it emerges because V(phi_0) < 0.

5. **No modifications to GR at observable scales.** All corrections are
   at the Planck scale. BBN, CMB, solar system tests, and gravitational
   wave observations are unaffected.

---

## 11. The Derivation Chain

```
V(phi) = -alpha/2 phi^2 + beta/4 phi^4
  |
  v
V(phi_0) = -alpha^2/(4*beta) < 0    [negative vacuum energy]
  |
  v
Emergent AdS profile, k = alpha*sqrt(3*pi)/4    [from DFGH constraint]
  |
  v
Kink in exponentially decaying substrate    [V(phi) provides both]
  |
  v
Gravity localization on kink    [automatic from AdS profile + kink]
  |
  v
M_Pl^2 = M_5^3/k = 2/k = 0.994    [zero free parameters]
  |
  v
kappa = 1/k = 0.4972    [target: 0.5000, error: -0.57%]
```

Every arrow in this chain is either a mathematical identity or a
well-established mathematical result (DFGH coupled equations, gravity
localization on exponential profiles). The only DFC-specific inputs
are alpha = cuberoot(18) and beta = 1/(9 pi).

---

## 12. Equation Modules

| Module | Tests | Key result | Tier |
|---|---|---|---|
| d4_coupled_kink_warp.py | 13/13 | kappa = 1/k = 0.4972 (-0.57%) | T1 |
| d4_kink_bending_rigidity.py | 11/11 | kappa_raw = 27.83 M_Pl^2 | T1 |
| d4_bending_prefactor.py | 10/10 | Warp factor is the suppression mechanism | T3 |
| d4_worldvolume_green.py | 15/15 | 1/r verified 11 orders | T1 |
| d4_1r_intermediate_test.py | 23/23 | Power index = -1.000 | T1 |
| d4_jormungandr_fixed_point.py | 24/24 | alpha^3 = 18, F = 22.87 | T1 |
| d4_zero_mode_gravity.py | -- | G_eff = G_N/22.9 scalar exchange | T3 |
| d4_gw_polarization_test.py | 15/15 | Candidate A fails, B viable | T3 |
| d4_metric_from_compression.py | 18/18 | Frequency-independent g_00 | T3 |
| d4_einstein_from_jormungandr.py | 22/22 | Einstein structure at weak field | T3 |
| d4_strong_field_metric.py | 20/20 | TOV with G_eff, compactness > 1 | T3 |
| + 10 more modules | 90/90 | Various structural results | T1-T3 |

**Total: 21 modules, 271+ assertions, 0 failures.**

---

**See also:** `foundations/d4_gravity_gap.md` (full technical analysis),
Module 14 (spacetime emergence), Module 16 (cosmology).
