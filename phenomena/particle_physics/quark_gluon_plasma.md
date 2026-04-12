# Phenomenon: Quark-Gluon Plasma

## One-Sentence Synthesis

> Quark-gluon plasma is the deconfined phase of the D7 SU(3) closure: at temperatures
> above approximately 150 MeV (the QCD crossover temperature), thermal energy is sufficient
> to disrupt the color-flux-tube binding that confines quarks into hadrons, and the
> individual D7 kinks (quarks) and D7 connection fields (gluons) propagate quasi-freely
> within the plasma volume — not as a gas of free particles but as a strongly coupled
> fluid whose transport properties reflect the near-transition dynamics of the D7 closure
> geometry.

---

## Observation

At sufficiently high temperature or density, nuclear matter transitions to a state in
which quarks and gluons are no longer confined inside hadrons:

- **QCD phase transition:** Lattice QCD calculations predict a crossover (not a sharp
  first-order transition) at temperature T-c ≈ 155 MeV at zero baryon density.
- **RHIC (Relativistic Heavy Ion Collider, 2000–present):** Gold-gold collisions at 200 GeV
  per nucleon pair produce a hot, dense medium. Elliptic flow measurements show the medium
  behaves as a nearly perfect fluid (very low shear viscosity to entropy density ratio,
  eta/s ≈ 1/(4 pi) in natural units — close to the conjectured quantum lower bound from
  AdS/CFT).
- **LHC heavy ion program (ALICE detector):** Lead-lead collisions at 5.5 TeV reach higher
  temperatures. Jet quenching (suppression of high-momentum particle production) confirms
  the dense medium. Temperature estimates ~500 MeV at formation.
- **Early universe QGP:** The universe was in a quark-gluon plasma state for the first
  ~10 microseconds after the Big Bang, before the QCD crossover at t ≈ 10 μs.
- **Neutron star cores:** At sufficiently high baryon density (several times nuclear
  saturation density), quark matter may exist in neutron star cores. The equation of state
  at these densities is highly uncertain.

---

## Standard Explanation

In QCD, the running coupling constant alpha-s decreases at high energies (asymptotic
freedom). At temperatures above T-c, the thermal scale sets the effective momentum,
making alpha-s small enough that quarks and gluons are only weakly bound. Color screening
(Debye screening of the color charge) disrupts the long-range confining force, freeing
quarks and gluons to propagate over distances larger than a single hadron.

The transition is actually a crossover at zero baryon density (not a true phase transition
in the thermodynamic sense), though it may become a first-order transition at high baryon
density with a critical endpoint. The order of the transition depends on the number of
quark flavors and their masses.

---

## Dimensional Folding Explanation

**STUB — full derivation not yet written.**

**DFC mechanism direction:**

1. **Confinement as D7 flux tube:** In DFC, confinement of color charge follows from the
   non-Abelian SU(3) structure of the D7 closure: isolated D7 winding has no stable D3
   localization (no stable particle). Color flux concentrates into tubes between quarks
   (see `phenomena/particle_physics/forces/strong_force.md`). The string tension (~1 GeV/fm)
   sets the energy cost of separating quarks.

2. **Deconfinement as D7 thermal disruption:** At high temperature, thermal fluctuations
   of the compression field provide enough energy to disrupt the flux tube formation. The
   deconfinement transition in DFC corresponds to the temperature at which the thermal
   energy density equals the D7 string tension times the flux tube length (roughly the
   hadron size). Above this temperature, the D7 kinks (quarks) can propagate without
   forming stable color-neutral clusters.

3. **Strongly coupled fluid from near-critical dynamics:** The QGP observed at RHIC is
   not a weakly coupled gas but a strongly coupled fluid with very low viscosity. In DFC,
   this near-perfect-fluid behavior reflects the near-critical dynamics of the D7 closure:
   near the deconfinement temperature, the substrate's D7 field is at the edge of the
   closure threshold, and fluctuations are maximally correlated, minimizing the viscosity.

4. **AdS/CFT viscosity bound:** The ratio of shear viscosity to entropy density for the
   QGP (eta/s ≈ 1/4 pi) matches the AdS/CFT lower bound for strongly coupled gauge
   theories. In DFC, this may follow from the D7 closure being the strongest-coupled
   sector — the one whose closure threshold is deepest — and the D7 dynamics near
   deconfinement being holographically dual to a string theory in an AdS space. This
   connection is suggestive but not yet derived.

5. **Early universe QGP and baryogenesis:** The QCD crossover at T ~ 155 MeV in the
   early universe is when the D7 SU(3) closure stabilizes cosmologically. Before this
   moment, quarks propagate freely. The baryogenesis scenario in
   `phenomena/cosmology/baryogenesis.md` operates before this crossover.

**Key open derivation:** Compute the QCD deconfinement temperature T-c from DFC parameters.
The target is T-c ≈ 155 MeV. This requires computing the D7 string tension from the
substrate field equation and relating it to the deconfinement thermal energy.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Deconfinement exists | D7 flux tubes disrupted above T-c | QGP observed at RHIC, LHC | ✓ structural |
| Near-perfect fluid | Near-critical D7 dynamics | eta/s ≈ 1/4 pi at RHIC | ✓ structural (qualitative) |
| T-c ≈ 155 MeV | D7 string tension / hadron size thermal threshold | 155 MeV from lattice QCD | not yet derived ✗ |
| Crossover not first order | At zero baryon density | Crossover confirmed by lattice | not yet accounted for ✗ |

---

## Open Questions

1. **Derive T-c from DFC substrate:** Compute the critical temperature for D7 deconfinement
   from the string tension and hadron scale, both of which should follow from the D7 closure
   geometry and the substrate coupling.

2. **First-order transition at finite density:** The QCD phase diagram may have a critical
   endpoint at finite baryon density where the crossover becomes first-order. In DFC,
   this would correspond to a specific condition on the D7 closure under compression.

3. **Viscosity bound from D7 closure:** Derive the eta/s bound of 1/(4 pi) from the D7
   SU(3) closure dynamics. If this follows from the product topology and the strength of
   the D7 coupling, it would be a structural derivation of a significant QGP property.

---

## Connections

- `phenomena/particle_physics/forces/strong_force.md` — confinement from D7 SU(3) closure
- `phenomena/particle_physics/particles/quarks.md` — D7 kinks as quarks
- `phenomena/particle_physics/particles/gluons.md` — D7 connection fields as gluons
- `phenomena/cosmology/baryogenesis.md` — pre-QCD-crossover baryon generation
- `phenomena/thermodynamics/phase_transitions.md` — phase transitions from V_eff bifurcations
