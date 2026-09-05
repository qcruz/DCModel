# Gravity Theory Integration — Running Inventory

**Status:** Active reference document
**Purpose:** Track exactly which concepts from each gravity framework are used in the
current DFC standard, what they contribute, and where they appear in the codebase.
This is the authoritative list of borrowed gravity machinery.

---

## Why This Document Exists

DFC borrows mathematical results from at least five distinct gravity frameworks:
Randall-Sundrum, DFGH thick domain walls, Sakharov induced gravity, analog gravity
(Gordon-Unruh), and AdS/CFT. Each framework contributes specific, non-overlapping
pieces of the gravity derivation chain. Some pieces are well-integrated; others remain
exploratory. This document maintains the inventory so that:

1. Every gravity-sector calculation can trace its parentage
2. Conflicts between frameworks are visible (not buried in separate files)
3. The analog gravity import — which has zero ontological conflicts with DFC — gets
   the systematic treatment it deserves
4. Redundancies are identified (two frameworks giving the same result by different routes)

---

## The Gravity Derivation Chain

DFC needs seven pieces to derive gravity (see `foundations/d4_gravity_gap.md`):

| # | Requirement | Current source framework | Status |
|---|---|---|---|
| 1 | Effective metric exists | Analog gravity (Gordon-Unruh) | T3 |
| 2 | Metric is dynamical | Sakharov induced gravity | T3 |
| 3 | Energy sources geometry | DFGH self-consistency | T2a |
| 4 | Response propagates (1/r) | Randall-Sundrum localization | T1 |
| 5 | Correct tensor structure (spin-2) | Sakharov (worldvolume gauge products) | T3 |
| 6 | Correct spatial profile | RS + 3D Laplacian Green's function | T1 |
| 7 | Correct coefficient G_N | RS thin-wall: kappa = 0.4972 (−0.57%) | T1 |

No single framework covers all seven. The integration is the DFC contribution.

---

## Framework 1: Randall-Sundrum (RS)

### What DFC uses

| Concept | Mathematical content | Where it appears | Tier |
|---|---|---|---|
| Warp-factor gravity localization | Sturm-Liouville zero mode on exponential profile: psi_0 proportional to e^{2A(y)} is normalizable | `equations/d4_coupled_kink_warp.py` | T1 |
| Effective 4D Planck mass | M_4^2 = M_5^3 / k, where k is the AdS curvature | `equations/d4_coupled_kink_warp.py` | T1 |
| 1/r gravitational profile | Localized source on domain wall produces 3D Green's function | `foundations/d4_gravity_gap.md` Blocker 2 | T1 |
| Z_2 reflection symmetry | Kink profile phi(-y) = -phi(y) automatically provides the orbifold symmetry | Structural (automatic from V(phi)) | T1 |
| KK tower spacing | m_n = n / r_compactification; first mode at Planck scale | `equations/d4_coupled_kink_warp.py` | T2a |

### What DFC does NOT use from RS

- The RS1 two-brane setup (hierarchy via inter-brane distance) — DFC has one kink, not two
- The fine-tuning condition between brane tension and bulk cosmological constant — in DFC,
  both are determined by V(phi), so the "tuning" is automatic
- The assumption that the 3-brane is a fundamental object — the kink is a dynamical
  feature of V(phi)

### Cohesion assessment

RS is the single most productive gravity framework for DFC. Every concept used is
mathematically clean and transfers without modification. The only translation needed
is linguistic: "5D spacetime" becomes "compression coordinate," "brane" becomes "kink."
No mathematical content changes.

**Key quantitative result:** kappa = 1/k = 0.4972 (−0.57% from target 0.5). This is
the DFC value of Newton's constant in Planck units.

---

## Framework 2: DFGH (DeWolfe-Freedman-Gubser-Horowitz)

### What DFC uses

| Concept | Mathematical content | Where it appears | Tier |
|---|---|---|---|
| Coupled scalar-gravity ODE system | A'' = -(1/6)(phi')^2; phi'' + 4A'phi' = V'(phi); constraint | `equations/d4_coupled_kink_warp.py` | T1 |
| Self-consistent field + warp profile | Given V(phi), both phi(y) and A(y) are determined simultaneously | `equations/d4_thick_wall_bvp.py` | T2a |
| Thick domain wall corrections | Backreaction of the wall's finite width on the warp factor | `equations/d4_thick_wall_bvp.py` | T3 |
| AdS curvature from vacuum energy | k^2 = -V(phi_0) / (6 M_5^3) | `equations/d4_coupled_kink_warp.py` | T1 |

### What DFC does NOT use from DFGH

- The 5D Planck mass M_5 as a free parameter — DFC must derive it from (alpha, beta)
- Multi-scalar generalizations (supergravity potentials) — DFC has one scalar
- Solutions with multiple domain walls — DFC currently considers only the single-kink sector

### Cohesion assessment

DFGH is the mathematical engine that connects V(phi) to the warp factor. It is
indispensable: without DFGH, DFC cannot compute k and therefore cannot compute G_N.
The one substantive gap is M_5: DFGH treats it as input, DFC needs it as output.
The convention M_5^3 = 2 is used in current calculations.

**Key result:** The DFGH system with DFC's V(phi) is self-consistent — the constraint
equation is satisfied by the kink + warp solution (verified numerically).

---

## Framework 3: Sakharov Induced Gravity

### What DFC uses

| Concept | Mathematical content | Where it appears | Tier |
|---|---|---|---|
| One-loop Einstein-Hilbert action | Integrating out worldvolume fields produces (M_ind^2 / 2) integral of R sqrt(g) | `equations/d4_induced_gravity_worldvolume.py` | T3 |
| Species counting | N_s = 17 massless DOF (8 SU(3) gluons x 2 + 1 translational Goldstone) | `equations/d4_induced_gravity_worldvolume.py` | T2a |
| Sign of induced gravity | Positive in 4D (quadratic divergence dominates logarithmic) | `equations/d4_induced_gravity_worldvolume.py` | T1 |
| Non-minimal coupling enhancement | xi_R phi^2 R term fills 93% of the gravity gap | `equations/d4_sakharov_enhanced.py` | T3 |
| Spin-2 from gauge field products | 1 x 1 = 0 + 1 + 2 representation decomposition gives spin-2 sector | `foundations/d4_gravity_gap.md` Blocker 4 | T3 |

### What DFC does NOT use from Sakharov

- The assumption that the background geometry is given a priori — DFC determines it
  self-consistently via DFGH
- The treatment of matter fields as fundamental (Sakharov assumed standard QFT matter) —
  DFC's worldvolume fields are closure modes of the substrate

### Cohesion assessment

Sakharov provides the mechanism for HOW the effective metric becomes dynamical (Requirement
2 in the chain). The one-loop calculation is mathematically sound but quantitatively
insufficient: it gives only 2.36% of G_N. The non-minimal coupling route (xi_R) fills
most of the gap but introduces a new parameter. The Helfrich membrane approach (see
analog gravity section below) offers a potentially parameter-free non-perturbative
alternative.

**Key result:** M_ind^2 = 0.0236 M_Pl^2 (one-loop); xi_R = 0.0126 fills to ~95% (T3).

---

## Framework 4: Analog Gravity (Gordon-Unruh)

### What DFC currently uses

| Concept | Mathematical content | Where it appears | Tier |
|---|---|---|---|
| Position-dependent propagation speed | c_eff(y) varies across kink profile via V''(phi_bg(y)) | `equations/d4_analog_metric.py` Part B | T1 |
| Effective metric construction | g_muv^eff from Visser (1998) acoustic metric formalism | `equations/d4_analog_metric.py` Part C | T3 |
| Frequency-independent metric | V''(phi_0) = 2 alpha = const in vacuum: all probes see the same geometry | `foundations/d4_gravity_gap.md` Blocker 3 | T1 |
| Poschl-Teller reflectionless scattering | s = 2 PT potential; phase shift delta(q) = arctan(1/q) + arctan(2/q) | `equations/d4_analog_metric.py` Part D | T1 |

### What DFC has NOT yet imported (high priority)

This is the core of the analog gravity exploration. The following results from the analog
gravity literature are mathematically available and have zero ontological conflicts with DFC:

**4a. Hawking temperature from V(phi)**

In any system with an effective metric possessing a horizon, the Hawking temperature is
determined by the surface gravity kappa_H:

```
T_H = kappa_H / (2 pi)
```

where kappa_H = |d(c_eff)/dy| evaluated at the horizon (where c_eff = v_flow in the
fluid analogy). For a DFC black hole analog — a substrate configuration where the
compression profile creates a trapping region — the Hawking temperature would be:

```
T_H = |V'''(phi_bg) * phi_bg'| / (2 pi * sqrt(V''(phi_bg)))
```

evaluated at the effective horizon.

**Current status:** Not computed. The formula is straightforward given the kink profile.
The question is whether localized closures (particles) create horizons in the effective
metric. For weak-field sources (ordinary matter), no horizon forms. For Planck-density
concentrations (black holes), the substrate profile must be solved self-consistently
via DFGH. The strong-field module `equations/d4_strong_field_metric.py` shows that
the GR metric framework breaks down at the kink core (compactness still greater than
one even with scale-dependent G_eff), which is exactly where analog gravity predicts
the metric description should fail.

**Priority:** High. A DFC-native Hawking temperature derivable from alpha and beta
alone would be a Tier 2a prediction.

---

**4b. Trans-Planckian dispersion relation**

The analog gravity literature (Jacobson-Corley 1999, Unruh 1995) shows that at
wavelengths comparable to the "atomic spacing" of the medium, the acoustic
approximation breaks down and the dispersion relation acquires corrections:

```
omega^2 = c^2 k^2 + eta * k^4 / M_Pl^2 + ...
```

The sign of eta (subluminal vs. superluminal at high energy) determines whether
Hawking radiation is robust or UV-sensitive.

For DFC, the "atomic spacing" is the kink width xi. The dispersion relation for
substrate perturbations near the kink is determined by V(phi):

```
omega^2 = k^2 + V''(phi_bg(y))      [exact, no approximation]
```

The Poschl-Teller structure gives discrete bound states plus a continuum.
The bound state spectrum IS the "dispersion correction" — the deviation from
omega^2 = k^2 that occurs when wavelength approaches xi.

**Current status:** The bound state spectrum is known exactly (PT with s = 2:
one zero mode at omega = 0, one bound state at omega^2 = 3 alpha / 2). The
continuum has no gap above omega^2 = 2 alpha. The dispersion is SUBLUMINAL
(V''(phi_0) = 2 alpha greater than zero adds a positive mass-squared to the
asymptotic dispersion). This means Hawking radiation IS robust against trans-
Planckian modifications — a concrete prediction.

**Priority:** Medium. The mathematical content is already computed in
`equations/d4_analog_metric.py` Part A. What remains is packaging it as a
prediction about quantum gravity phenomenology.

---

**4c. Superradiance from rotating closures**

Rotating acoustic horizons amplify certain wave modes (superradiance). For a
rotating DFC closure (a particle with angular momentum), the substrate analog
metric would have a Kerr-like structure. Superradiance would cause the closure
to spin down by emitting substrate perturbations — this IS what electromagnetic
and gravitational radiation from rotating objects look like at the substrate level.

**Current status:** Not explored. Requires understanding angular momentum in
the substrate picture, which connects to the D6 SU(2) closure structure.

**Priority:** Low (conceptually interesting but computationally difficult).

---

**4d. Acoustic horizon thermodynamics**

The full thermodynamic structure of acoustic horizons (entropy, temperature,
specific heat, evaporation time) has been worked out in the analog gravity
literature (Barcelo, Liberati, Visser 2005). All of these transfer directly
to DFC if the substrate configuration produces an effective horizon.

Relevant connections:
- Bekenstein-Hawking entropy S = A / (4 G_N) — already computed in DFC
  (`equations/d4_bekenstein_hawking_from_varphi.py`), inherits kappa gap (−0.57%)
- Specific heat C = dE/dT — negative for Schwarzschild, determines evaporation
  instability
- Information paradox — in analog gravity, there is no paradox because the
  "trans-Planckian" physics (atomic structure of the medium) is known. DFC
  similarly has explicit UV structure (the kink profile), suggesting the
  information paradox dissolves.

**Current status:** Bekenstein-Hawking entropy derived; other thermodynamic
quantities not computed.

**Priority:** Medium-high. The information paradox dissolution is conceptually
important and could be a distinctive DFC claim.

---

**4e. Analog cosmology — expanding substrate as expanding acoustic medium**

Analog gravity has been extended to cosmology (Barcelo, Liberati, Visser 2003):
an expanding medium produces an expanding effective metric. For DFC, the
substrate's cosmological behavior (compression/expansion) directly produces
the Friedmann equations via the analog metric.

The existing DFC cosmology module (`equations/cosmology.py`) derives H_0 from
substrate parameters. The analog gravity connection would provide a SECOND
independent route to the same result — a consistency check.

**Current status:** Not explored as analog gravity; the cosmological
predictions exist but are derived via different methods.

**Priority:** Medium. A consistency check between two independent derivation
routes is valuable.

---

**4f. Lorentz invariance as emergent low-energy symmetry**

The analog gravity literature has extensively studied how Lorentz invariance
emerges at low energies in systems where the fundamental dynamics is NOT
Lorentz-invariant (the medium has a preferred frame). The key result: for any
non-dispersive medium (omega proportional to k at low k), the low-energy
effective theory is exactly Lorentz-invariant (Barcelo et al. 2001).

DFC's substrate has a natural "preferred frame" (the rest frame of the vacuum
configuration). But perturbations in the vacuum see V''(phi_0) = 2 alpha,
which is constant — no dispersion. Therefore, Lorentz invariance emerges
exactly at energies well below the sigma mass.

**Current status:** Structural argument exists (T3). The analog gravity
framework provides the precise theorem guaranteeing Lorentz emergence.

**Priority:** High. Upgrading the Lorentz invariance argument from T3 to T1
(by citing the analog gravity theorem) would strengthen the entire framework.

---

### Why analog gravity is uniquely well-suited to DFC

The cohesion/conflict audit found ZERO conflicts — not even cosmetic ones.
This is because DFC and analog gravity share the same foundational claim:
geometry is the acoustic structure of a medium. In laboratory analog gravity
(BEC sonic black holes, water wave analogs), the medium is explicitly known
and nobody mistakes the emergent geometry for fundamental spacetime. DFC makes
the same claim about actual spacetime: it IS the acoustic geometry of the
substrate, and the substrate IS the fundamental reality.

This means every mathematical result from the analog gravity literature
transfers to DFC without any ontological translation, reinterpretation, or
modification. The mathematics is identical; only the identity of the medium
changes (from a laboratory fluid to the substrate).

---

## Framework 5: AdS/CFT Correspondence

### What DFC uses

| Concept | Mathematical content | Where it appears | Tier |
|---|---|---|---|
| Compression coordinate = RG scale | Depth y maps to energy scale mu; deeper = higher energy | `equations/adscft_topo_insulator_dfc.py` Part A | T1 |
| Bulk-boundary operator dictionary | PT bound states map to worldvolume operators via mass-dimension relation | `equations/adscft_topo_insulator_dfc.py` Part A | T2a |
| Central charge from AdS radius | c = pi L^3 / (8 G_5) ~ 19.4 (predicts O(10) worldvolume DOF) | `equations/adscft_topo_insulator_dfc.py` Part A | T2a |
| Operator dimensions from PT spectrum | Zero mode gives Delta = 4 (stress tensor); bound state gives Delta ~ 5.6 | `equations/adscft_topo_insulator_dfc.py` Part A | T2a |
| KSS viscosity bound | eta/s >= 1/(4 pi); DFC predicts eta/s ~ 0.085 for QGP | `equations/adscft_topo_insulator_dfc.py` Part C | T3 |
| Ryu-Takayanagi entropy | S_A = Area(gamma_A) / (4 G_N); inherits kappa gap | `equations/adscft_topo_insulator_dfc.py` Part A | T3 |
| Confinement from IR wall | Substrate reaching vacuum at finite effective depth corresponds to confinement | `foundations/literature_reframing.md` A5 | T3 |

### What DFC uses with caveats

| Concept | Caveat | Impact |
|---|---|---|
| Full duality (bulk = boundary) | DFC has no large-N parameter; N_c = 3 is small | Quantitative corrections expected |
| Exact conformal invariance on boundary | Worldvolume theory is massive (PT bound states) | Full CFT toolkit not applicable |
| Classical gravity in bulk | Without large N, quantum substrate corrections are O(1) | Holographic calculations are approximate |

### Altland-Zirnbauer topological classification (via AdS/CFT module)

| Concept | Mathematical content | Where it appears | Tier |
|---|---|---|---|
| D5 = class AI (time-reversal, T^2 = +1) | Trivial topological invariant in d = 1 — no protected zero mode | `equations/adscft_topo_insulator_dfc.py` Part B | T1 |
| D6 = class BDI (T, C, S all present) | Z invariant in d = 1 — one protected zero mode = Jackiw-Rebbi fermion | `equations/adscft_topo_insulator_dfc.py` Part B | T1 |
| D7 = class AIII (chiral symmetry only) | Z invariant — index theorem protects quark zero modes | `equations/adscft_topo_insulator_dfc.py` Part B | T1 |
| Depth sequence traces AZ path | AI -> BDI -> AIII is a specific trajectory through the periodic table | `equations/adscft_topo_insulator_dfc.py` Part B | T2a |

### Cohesion assessment

AdS/CFT is the most content-rich framework DFC borrows from, but also the one with the
most substantive conflicts (3, per the Cluster A audit). The structural mapping
(compression = radial, kink = boundary, RG = depth) is natural and productive. The
quantitative toolkit (conformal bootstrap, large-N expansion, exact correlation
functions) is NOT directly applicable because DFC violates the prerequisites (large N,
exact conformal invariance).

DFC should use AdS/CFT for:
- Structural guidance (what maps to what)
- Qualitative predictions (confinement from IR wall, operator counting)
- The AZ topological classification (which is rigorous and independent of large N)

DFC should NOT rely on AdS/CFT for:
- Exact correlation functions
- Precise transport coefficients (KSS bound is suggestive, not rigorous at N_c = 3)
- The assumption that substrate dynamics is well-described by classical gravity in the bulk

---

## Cross-Framework Consistency Map

Where two frameworks give the same result independently:

| Result | Framework A | Framework B | Agreement |
|---|---|---|---|
| 1/r gravitational profile | RS (zero-mode localization) | Analog gravity (3D Green's function on worldvolume) | Exact |
| G_N from V(phi) | RS (M_4^2 = M_5^3/k) | Sakharov (one-loop + non-minimal) | RS gives 99.4%; Sakharov gives ~95% (different route) |
| Effective metric exists | DFGH (warp factor) | Analog gravity (position-dependent c_eff) | Same metric, different derivation |
| Worldvolume DOF count | Sakharov (N_s = 17) | AdS/CFT (central charge ~ 19) | Consistent (O(10) DOF) |
| Subluminal dispersion | Analog gravity (V'' > 0 in vacuum) | PT bound state spectrum (mass gap) | Same physics, different language |

No contradictions found between any pair of frameworks. This is a non-trivial consistency
check: five independently developed theories of gravity emergence, applied to the same
substrate, produce mutually compatible results.

---

## Open Questions and Next Steps

### Highest priority

1. **Sakharov + Helfrich non-perturbative M_Pl** — if membrane fluctuation methods
   close the 97.6% Sakharov gap without introducing new parameters, G_N becomes a
   derived quantity. This would resolve DFGH's M_5 gap simultaneously.

2. **Analog gravity Hawking temperature** — derive T_H from V(phi) for a substrate
   configuration with an effective horizon. This is a concrete, computable prediction.

3. **Lorentz invariance as analog gravity theorem** — cite the Barcelo et al. (2001)
   result to upgrade the Lorentz emergence argument from T3 to T1.

### Medium priority

4. **Trans-Planckian prediction packaging** — the subluminal dispersion result is already
   computed but not packaged as a quantum gravity prediction. This is a testable claim.

5. **Consistency check: cosmology via analog gravity** — derive Friedmann equations from
   the expanding substrate analog metric and compare with existing DFC cosmology results.

6. **Information paradox dissolution** — DFC has explicit UV structure (kink profile);
   analog gravity shows this resolves the information paradox. Write up the argument.

### Lower priority

7. **Superradiance from rotating closures** — conceptually interesting but requires
   angular momentum formalism not yet developed.

8. **Full AdS/CFT correlation function test** — compute a worldvolume two-point function
   both directly and via substrate bulk propagator; check agreement. Limited by N_c = 3
   (corrections expected to be large).
