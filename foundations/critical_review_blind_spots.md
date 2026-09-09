# What DFC Cannot Do — Honest Blind Spot Catalog

**Purpose:** This document catalogs phenomena and questions that DFC has no
account for, even in principle at the current level of development. This is
distinct from P4 Known Failures (where partial results exist but are wrong)
and from ROADMAP items (where work is planned). These are genuine blind spots
— areas where the framework is silent, structurally limited, or where its
answers would be circular.

**Standard:** Each entry states what the phenomenon is, why DFC cannot address
it, and whether the limitation is fundamental (inherent to the framework) or
contingent (could be resolved with further development).

---

## Category 1: Fundamental Structural Limitations

These are things DFC cannot do because of its basic architecture — one scalar
field with a double-well potential. Resolving them would require changing the
framework, not extending it.

### 1.1 Flavor physics from first principles

DFC has no mechanism to derive the specific values of quark and lepton masses
from V(phi) alone. The Koide formula reproduces the tau mass from electron and
muon inputs, and the center-vortex mechanism gives charm and strange from a
single kappa parameter — but the *origin* of the mass hierarchy (why m_t/m_e
~ 3.4 x 10^5) is not derived. The Yukawa couplings arise from D6/D7 overlap
integrals that have not been computed. DFC can parametrize the hierarchy
(exponential depth suppression) but cannot predict individual masses without
additional structure.

**Type:** Contingent — overlap integrals are in principle computable but
require solving the coupled kink BVP at multiple depths simultaneously.

### 1.2 CKM and PMNS mixing matrices

The 4 CKM parameters and 6 PMNS parameters (10 total mixing parameters) are
not derived from DFC. The Z3 holonomy mechanism gives theta_23 to 0.35 sigma,
and the Gatto-Sartori-Tonin relation sin(theta_C) = sqrt(m_d/m_s) works at
-0.6% using DFC quark masses — but these are partial results, not a complete
mixing matrix derivation. The full CKM/PMNS requires the off-diagonal D6/D7
overlap integrals that are currently blocked.

**Type:** Contingent — same overlap integral problem as 1.1.

### 1.3 Why V(phi) = -alpha/2 phi^2 + beta/4 phi^4

The potential is a Tier 0 postulate. DFC does not explain why the universe
has this specific potential rather than phi^6, sine-Gordon, or any other
double-well. The alternative_potentials.py analysis (C536) shows that phi^4
is unique in several respects (simplest renormalizable, PT exactly solvable,
self-consistency closes to cubic), and RG universality suggests all symmetric
double-wells flow to phi^4 at long distances — but this is not a derivation.

**Type:** Fundamental — this is an axiom of the framework. Any explanation
would require a deeper theory that generates V(phi).

### 1.4 Why one spatial substrate dimension initially

DFC assumes the substrate starts near 1D (maximum compression) and that
apparent 3D space emerges at D3 depth. But the framework does not explain
why the initial state is 1D rather than 0D or 2D. The D1 precursor state
is postulated, not derived.

**Type:** Fundamental — initial conditions are outside the scope.

---

## Category 2: Calculational Gaps (Not Structural)

These are things DFC should be able to address but where the calculations
have not been done or are too difficult with current methods.

### 2.1 QCD phase diagram

DFC has not computed the QCD phase transition temperature T_c, the location
of the critical endpoint in the mu_B-T plane, or the order of the transition
for physical quark masses. The D7 deconfinement transition is proved weakly
first-order (via Svetitsky-Yaffe, T2a), but this is for pure gauge theory.
Including dynamical quarks changes the picture and DFC has no account of this.

**Type:** Contingent — lattice QCD does this numerically; DFC would need
an equivalent framework at finite temperature and density.

### 2.2 Specific material properties

DFC predicts universal constants (alpha_em, g_eff, masses) but cannot predict
properties of specific materials — melting points, conductivities, crystal
structures, chemical reaction rates. These require solving the many-body
Schrodinger equation with DFC's constants as inputs, which is standard
condensed matter physics, not a DFC calculation.

**Type:** Fundamental scope boundary — DFC provides constants and principles,
not material-specific solutions. This is analogous to how the Standard Model
does not predict the melting point of iron.

### 2.3 Quantum gravity regime

DFC has a structural account of gravity (D4 inertia, RS2 localization, kappa
= 0.497) but cannot compute quantum gravity observables — graviton scattering
amplitudes, black hole information loss resolution, or the fate of spacetime
at the Planck scale. The D4 gravity gap (4-9x overshoot in the thick-wall
regime) shows that the gravitational sector is not yet under control.

**Type:** Contingent — the substrate *is* the Planck-scale object, so DFC
should have something to say. But the calculations are beyond current reach.

### 2.4 Non-equilibrium QFT processes

DFC has no framework for computing non-equilibrium processes: thermalization
rates, transport coefficients in the quark-gluon plasma, jet quenching
parameters, or heavy-ion collision dynamics. These require real-time QFT
methods that DFC has not developed.

**Type:** Contingent — nothing prevents extending DFC to non-equilibrium,
but the framework does not currently exist.

### 2.5 Multi-loop precision calculations

DFC reproduces tree-level and some one-loop results (M_W with Sirlin
corrections, a_e to 4-loop QED). But DFC does not provide a systematic
loop expansion — it uses standard QFT perturbation theory with DFC-derived
couplings plugged in. There is no DFC-specific loop technology. If the
standard loop expansion fails (as it does for alpha_s at low scales, C544),
DFC has no alternative.

**Type:** Contingent — DFC could develop its own perturbative or
non-perturbative expansion, but currently borrows from standard QFT.

---

## Category 3: Questions DFC Does Not Even Ask

These are legitimate physics questions where DFC has nothing to say — not
because it fails, but because the questions are outside its scope.

### 3.1 Why is there something rather than nothing?

DFC assumes the substrate exists. It does not explain why.

### 3.2 Initial conditions of the universe

DFC derives inflationary observables (n_s) given N_e = 60 e-folds, but does
not derive N_e itself. The initial state of the substrate (pre-inflation)
is not specified.

### 3.3 The measurement problem (fully)

DFC has structural accounts of Born rule emergence and Bell correlations,
but does not resolve the measurement problem in the sense of explaining
why individual measurement outcomes occur. The substrate dynamics are
deterministic; the appearance of probabilistic outcomes requires a
decoherence-like argument that has not been fully developed.

### 3.4 Consciousness and observers

DFC has no account of consciousness, observers, or why physical systems
give rise to subjective experience. This is not a failing specific to DFC —
no physical theory addresses this.

### 3.5 Mathematical existence of the substrate

DFC uses the field equation derived from V(phi) but does not prove that
solutions exist in a mathematically rigorous sense (Sobolev regularity,
global existence, etc.). The Yang-Mills mass gap proof addresses this for
the gauge sector, but the full substrate field theory has not been placed
on rigorous mathematical footing.

---

## Category 4: Areas Where Standard Approaches Are Superior

Honest accounting of where existing theories do better than DFC.

### 4.1 Lattice QCD for hadron masses

Lattice QCD computes hadron masses to sub-percent accuracy from first
principles (given quark masses and alpha_s as inputs). DFC's hadron mass
predictions (proton -0.4%, rho -1.5%) are comparable but use different
inputs and are less systematic. For excited states and exotic hadrons,
lattice QCD is far superior.

### 4.2 Standard Model EFT for precision observables

The Standard Model effective field theory (SMEFT) framework provides
systematic higher-order corrections to electroweak observables. DFC
currently uses standard one-loop Sirlin corrections but has no equivalent
systematic expansion. For precision EW observables, SMEFT is the
established tool.

### 4.3 Cosmological perturbation theory

Standard LCDM with 6 parameters fits the CMB power spectrum to cosmic
variance limits. DFC reproduces some of these (H_0, theta_*, r_s) but
has not computed the full C_l spectrum. For detailed CMB analysis, standard
cosmological perturbation theory is far more developed.

### 4.4 Nuclear structure calculations

Ab initio nuclear structure (chiral EFT + many-body methods) computes
nuclear binding energies, spectra, and transitions with controlled
uncertainties. DFC's nuclear predictions (Walecka model with DFC couplings)
are mean-field level — competitive for bulk properties but inferior for
detailed spectroscopy.

---

## Summary Statistics

| Category | Count | Fundamental | Contingent |
|---|---|---|---|
| Structural limitations | 4 | 2 | 2 |
| Calculational gaps | 5 | 1 | 4 |
| Outside scope | 5 | 5 | 0 |
| Standard approaches superior | 4 | — | — |
| **Total** | **18** | **8** | **6** |

Of the 18 blind spots, 8 are fundamental (inherent to any single-field
framework) and 6 are contingent (could be resolved with further work).
The remaining 4 are areas where existing approaches are simply more
developed — not DFC failures but honest comparisons.

The most important contingent gaps are 1.1 (flavor physics) and 2.3
(quantum gravity) — these are areas where DFC *should* have something
unique to say but has not yet delivered quantitative results.
