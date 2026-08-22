# Module 28 — Gravity in DFC: Current Status

**Series:** DFC Educational Modules
**Prerequisite reading:** Module 01 (substrate and kinks), Module 04 (forces),
Module 14 (spacetime emergence)

**Last updated:** August 2026

---

## 1. The Central Challenge

DFC claims all physics emerges from a single potential:

V(phi) = -alpha/2 phi^2 + beta/4 phi^4

The strong, weak, and electromagnetic forces are connected to V(phi) through
closure topologies at D5, D6, and D7, with quantitative predictions and
equation modules. Gravity is different. Newton's gravitational constant G_N
currently enters DFC through Planck units, not as a derived output.

The D4 gravity gap is the deepest structural gap in DFC. It is not one
problem but **four sub-problems**, each partially addressed:

| Sub-gap | Question | Status |
|---|---|---|
| D4-A: Scale | What sets the absolute gravitational scale? | T3 (three independent routes give alpha^3 = 18) |
| D4-B: Metric | How does spacetime geometry emerge from V(phi)? | T3/T4 (weak-field chain established, strong-field open) |
| D4-C: Graviton | Does the substrate have a massless spin-2 mode? | T3 (viable mechanism identified, coupling-dependent) |
| D4-D: Coupling | What is G_N in terms of alpha and beta? | T3 (perturbative 7% computed exactly, 93% non-perturbative) |

---

## 2. What Has Been Derived

### 2a. The 1/r Potential — Derived, Not Assumed

The kink profile phi(y) = phi_0 tanh(y/xi) falls off exponentially in the
transverse direction. This cannot produce 1/r gravity directly. But kinks
(particles) are localized sources ON the three-dimensional worldvolume of
the domain wall. The Green's function of the 3D Laplacian is 1/(4 pi r) —
so any localized source interacting through the wall produces a 1/r potential
automatically.

The full Poeschl-Teller mode sum confirms this: the zero mode gives exact
1/r at all distances. The n=1 bound state contributes nothing (odd parity,
vanishes at y=0). The continuum contributes less than 6% at the kink center
and is exponentially suppressed beyond two kink widths. The result is
verified across 11 orders of magnitude with logarithmic derivative
d(ln G)/d(ln r) = -1.000 to 10^-9 precision.

Newton's law V(r) = -G_eff M_1 M_2 / r is confirmed for the DFC system.
**Tier: T1 exact.**

### 2b. The Perturbative Sector — Complete

Three perturbative channels contribute to the gravitational coupling:

| Channel | Source | Fraction of G_N |
|---|---|---|
| Scalar zero-mode exchange | Tree-level kink-kink | 4.37% |
| Sakharav induced metric | One-loop worldvolume modes | 2.36% |
| V''' analog metric | Potential-sector coupling | 0.01% |
| **Total perturbative** | | **~6.7%** |

The enhancement factor F = G_N / G_eff = (25/12) times 4 pi xi = 22.87 is
computed exactly using Fraction arithmetic. The rational prefactor 25/12 =
I_4^3 / I_6^2 is a sech-integral identity. The continuum spectral correction
is negative and negligible (0.22% of the bound state contribution).

The remaining approximately 93% is non-perturbative — this is the primary
gravitational mechanism in DFC.

**Tier: T1 for scalar fraction and mode sum; T3 for non-perturbative interpretation.**

### 2c. Gravitational Wave Polarizations — Resolved Structurally

General relativity predicts two transverse-traceless tensor polarizations.
DFC's compression field phi is a scalar. Two candidate mechanisms were tested:

**Candidate A (composite tensor from scalar gradients):** FAILS. The tensor
d_mu(dphi) d_v(dphi) is purely longitudinal for any plane wave — zero spin-2
content. This is a theorem, not a numerical result. A scalar field cannot
produce spin-2 modes through its derivatives alone.

**Candidate B (worldvolume gauge fields):** VIABLE. The kink's moduli space
is SU(3), giving 16 gauge degrees of freedom on the worldvolume. The tensor
product 1 x 1 = 0 + 1 + 2 produces spin-2 content. The Sakharav induced
gravity mechanism generates a standard Einstein-Hilbert action whose
linearized fluctuations have exactly two TT polarizations at speed c.

The scalar breathing mode is Planck-mass-gapped (m_sigma = 2.29 M_Pl) —
invisible at LIGO frequencies.

**Tier: T3 (structurally viable, coupling-dependent).**

### 2d. The Jormungandr Fixed-Point — Three Routes Converge

The dimensionless product alpha^3 is determined by three independent arguments
that all give the same answer: alpha^3 = 18.

1. **Topological:** alpha^3 = Q_top times N_Hopf = 2 times 9 = 18 [T1]
2. **BPS/coupling:** S_kink times alpha_D5 = 1 gives alpha^3 = 18 [T1]
3. **Gravitational self-consistency:** The Jormungandr fixed-point equation
   F_mode_sum(alpha) = F_self_consistency(alpha) has a unique real positive
   solution at alpha^3 = 18 [T3, C400]

The third route is especially significant: it says the double-well potential
V(phi) is an **attractor** of its own gravitational dynamics. The kink's
self-gravitational back-reaction reproduces the same V(phi) that produced
the kink, if and only if alpha = cuberoot(18).

**Tier: T1 for the algebraic result; T3 for the gravitational interpretation.**

### 2e. The Weak-Field Metric Chain

A mass M sources a zero-mode perturbation of the substrate:

```
Mass -> delta_phi(r) -> delta_V''(r) -> delta_c_eff(r) -> g_00(r)
```

The perturbation delta_phi(r) = N_0 times g_source times M / (4 pi r times
E_kink) shifts the effective mass-squared V''(phi) at the vacuum, changing
the local propagation speed. A key identity makes this a genuine metric: the
relation V''(phi_0) = 2 alpha = omega_c^2 ensures the metric perturbation
is **frequency-independent** — slow probes and fast probes see the same
geometry. This is required for a metric rather than a dispersive medium.

**Tier: T1 for the frequency-independence identity; T3 for the full metric chain.**

### 2f. Einstein Equation Structure

The Jormungandr self-consistency, reformulated in metric language, recovers
the Einstein equation structure:

- **Sakharav Einstein-Hilbert action:** The worldvolume modes generate an
  effective R term via the induced gravity mechanism [T1]
- **Noether conservation:** The substrate's translational symmetry produces
  d_mu T^muv = 0 [T1]
- **Coupling:** alpha^3 = 18 determines the Einstein-Hilbert coefficient [T1]

These three elements together give the structure of Einstein's field equations.
However, the strong-field behavior breaks down: at the kink core (r ~ xi),
the linearized metric has g_00(xi) = +258 (wrong sign), indicating that
perturbation theory fails catastrophically at the substrate scale.

**Tier: T3 for Einstein structure; T1 for individual components.**

---

## 3. What Remains Open

### 3a. The Strong-Field Problem (D4-B, PRIMARY)

The kink has energy E_kink = 36 pi M_Pl and width xi = 0.874 l_Pl. Its
Schwarzschild radius r_s = 226 l_Pl is 259 times larger than its width.
The ratio r_s/xi = 259 >> 1 means the kink sits deep inside its own
gravitational radius.

An attempt to construct the strong-field metric using TOV equations with
scale-dependent G_eff(r) (transitioning from G_N/23 at the core to G_N
asymptotically) reduces GR compactness from 151 to 6.6 — a 23-fold
improvement — but 6.6 is still greater than 1. The TOV-with-G_eff ansatz
is insufficient. The GR metric framework breaks down at the kink core.

The substrate itself IS smooth — the sech^4 energy density has no singularity.
The problem is that GR's metric language cannot describe this regime.
Deriving the actual effective metric requires the full substrate compression
dynamics, not just a modified Newton's constant in Schwarzschild/TOV.

This is the PRIMARY open problem in DFC gravity.

**Tier: T4 open.**

### 3b. The 93% Non-Perturbative Coupling (D4-D)

The perturbative sector captures only 6.7% of G_N. The remaining 93% IS
the gravity — operating through the substrate's compression geometry rather
than through particle exchange.

DFC's interpretation: gravity is not a force mediated by spin-2 exchange.
Gravity is what differential compression of the substrate looks like from
within. Where there are more closures (particles), the substrate compresses
differently. That differential compression IS gravity. The 93% is not
missing physics — it is the dominant mechanism.

Quantifying this requires the D4-B strong-field metric construction.

**Tier: T4 (requires D4-B).**

### 3c. The Perturbative Equivalence Principle (D4-B/D4-D)

The perturbative force-to-metric ratio is 1.84 — the scalar force and the
Sakharav metric are not proportional. This means the equivalence principle
is violated at the perturbative level by a factor of 1.84. However, the
perturbative sector is only 7% of gravity. The non-perturbative force-metric
mismatch is only 2.1%, making EP restoration a mild constraint on whatever
compression geometry mechanism provides the 93%.

**Tier: T3 (constraint identified, resolution requires D4-B).**

---

## 4. DFC's Distinctive Claims About Gravity

Unlike string theory, loop quantum gravity, or other approaches, DFC makes
specific structural claims about gravity:

1. **Gravity is not a fundamental force.** It is emergent compression behavior
   of the substrate. There is no fundamental graviton in the substrate
   spectrum — this was proven (C393) and is considered expected rather than
   problematic.

2. **1/r is derived from worldvolume dimensionality.** The spatial dependence
   of gravity follows from the 3D Green's function on the domain wall, not
   from any input.

3. **The gravitational scale is self-consistent.** alpha^3 = 18 is determined
   by three independent routes, one of which is gravitational self-consistency
   (Jormungandr). The potential V(phi) is an attractor of its own gravity.

4. **Scale-dependent coupling.** G_eff transitions from G_N/23 at the kink
   core to G_N asymptotically. This has no effect at cosmological or
   astrophysical scales (the transition occurs at the Planck scale), so all
   standard gravitational tests are unaffected.

5. **No modifications to GR at observable scales.** DFC predicts standard
   Einstein gravity at all scales above the Planck length. The scale-dependent
   G_eff is exponentially suppressed above ~10 kink widths (~10 Planck lengths).
   BBN, CMB, solar system tests, and gravitational wave observations are all
   consistent.

---

## 5. Cosmological Implications

DFC's gravity account, combined with standard cosmological parameters,
produces quantitative cosmological predictions (C409-C414):

| Observable | DFC | Observed | Error |
|---|---|---|---|
| Y_p (BBN helium-4) | 0.2475 | 0.2449 | +1.05% |
| CMB first peak ell_1 | 222 | 220 | +0.9% |
| Sound horizon r_s | 143.87 Mpc | 144.43 Mpc | -0.39% |
| BAO scale r_drag | 146.70 Mpc | 147.09 Mpc | -0.27% |
| Age of universe | 13.780 Gyr | 13.797 Gyr | -0.12% |
| Spatial flatness | Omega_k = 0 | < 0.0007 | consistent |

The scale-dependent G_eff has no effect on any of these — it is Planck-scale
only. DFC's cosmological predictions use standard GR with DFC-specific
inputs (g_A = 4/pi from D6 topology, tau_n = 878.0 s, 3 generations from
S^3 topology).

---

## 6. The Path Forward

The most promising path to closing the D4 gap:

1. **Derive the full substrate effective metric** — not through TOV with
   modified G_N, but through the substrate's own compression dynamics. The
   sech^4 energy density is smooth. The effective metric must be derivable
   from V(phi) directly.

2. **Close the Jormungandr circularity** — the current fixed-point equation
   uses G_N as input. If the analog metric construction independently
   produces G_N from compression, the loop becomes self-contained.

3. **Quantify the non-perturbative 93%** — once the full metric is known,
   the coupling coefficient emerges as a derived quantity rather than a fit.

If DFC can close this loop, it will be the first framework to derive all
four forces from a single starting point without pre-existing spatial
dimensions or gauge groups. If the 93% cannot be accounted for, gravity
may require structure beyond the double-well potential.

Either result is scientifically valuable.

---

## 7. Equation Modules

| Module | Cycle | Tests | Result |
|---|---|---|---|
| d4_gravity_dimensional.py | C366b | — | xi ~ l_Pl, omega_c bridge |
| d4_zero_mode_gravity.py | C367 | — | G_eff = G_N/23 scalar exchange |
| d4_gravity_spin2_enhancement.py | C392 | 17/17 | Profile narrowing reduces coupling |
| d4_substrate_response.py | C393 | 14/14 | No massless spin-2 in scalar spectrum |
| d4_induced_gravity_worldvolume.py | C394 | 14/14 | Sakharav 2.35% M_Pl^2, wrong-sign resolved |
| d4_continuum_spectral_gravity.py | C395 | 17/17 | Continuum correction negligible |
| d4_analog_metric.py | C396 | 17/17 | 1/r from worldvolume, transverse confinement |
| d4_worldvolume_green.py | C397 | 15/15 | Full mode sum, G_eff = G_N/22.9 |
| d4_gw_polarization_test.py | C398 | 15/15 | Candidate A FAILS, Candidate B viable |
| d4_1r_intermediate_test.py | C399 | 23/23 | 1/r across 11 orders of magnitude |
| d4_jormungandr_fixed_point.py | C400 | 24/24 | alpha^3 = 18 unique solution |
| d4_metric_from_compression.py | C403 | 18/18 | Weak-field metric chain, V'' = omega_c^2 |
| d4_metric_force_equivalence.py | C405 | 24/24 | Three channels, EP ratio 1.84 |
| d4_einstein_from_jormungandr.py | C407 | 22/22 | Einstein structure, strong-field breakdown |
| d4_strong_field_metric.py | C408 | 20/20 | TOV with G_eff, compactness still > 1 |

**Total: 15 modules, 258/258 PASS, 0 FAIL.**

---

**See also:** `foundations/d4_gravity_gap.md` (full technical analysis),
`foundations/jormungandr_double_well.md` (cyclical compression hypothesis),
Module 14 (spacetime emergence), Module 16 (cosmology).
