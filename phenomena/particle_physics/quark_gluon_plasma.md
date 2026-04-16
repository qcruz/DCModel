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

**Key open derivation:** Derive T_c from DFC parameters directly — compute the D7 string
tension from the SU(3) closure geometry and substrate field equation, then set T_c via the
thermal disruption condition. Primary blockage: α_s at the QCD scale requires M_c(D7)
from substrate (Bottleneck 2). See `equations/quark_gluon_plasma.py` for the current
numerical estimate and its error.

---

## Formal Equations

### QCD Deconfinement Temperature

The deconfinement temperature marks the crossover where the D7 SU(3) closure configurations
become thermally disrupted. A rough estimate follows from balancing the string tension
(the energy cost per unit length of separating a quark-antiquark pair) against the thermal
energy scale. The string tension σ has dimensions of energy per length (or equivalently
energy squared in natural units):

```
T_c ~ √σ / (2π)    [rough dimensional estimate]
σ ≈ 0.18 GeV²      [empirical string tension from Regge trajectories]
T_c ~ √0.18 / (2π) ≈ 68 MeV    [underestimates observed T_c by factor ~2]
```

The deconfinement temperature is approximately proportional to the square root of the
string tension divided by two pi. The observed T_c ≈ 155 MeV is higher than this
dimensional estimate because the crossover involves collective effects not captured by
the one-parameter string tension.

### Color Debye Screening

Above T_c, color charge is Debye-screened: the gluon propagator acquires an effective
thermal mass proportional to the strong coupling times the temperature. The Debye screening
length — the scale over which color fields are suppressed — equals one divided by the product
of the strong coupling constant g_s and the temperature:

```
λ_D ~ 1 / (g_s T)    [Debye screening length]
g_s = √(4π α_s)

At T = 2T_c ≈ 310 MeV,  α_s ≈ 0.25:
    g_s ≈ 1.77
    λ_D ~ 1/(1.77 × 310 MeV) ≈ 0.36 fm
```

This is shorter than the hadronic radius (~1 fm), confirming that color forces are
effectively screened at twice the crossover temperature.

### DFC Prediction for T_c (current status)

The DFC coupling chain gives α_s(M_Z) = 0.105 (11% below observed). Running α_s down
to the QCD scale using one-loop perturbation theory is unreliable at low energies —
the one-loop formula diverges at Λ_QCD. The DFC prediction from `equations/quark_gluon_plasma.py`:

```
DFC α_s(M_Z) = 0.105  (11% below observed 0.1182)
DFC Λ_QCD (one-loop) ≈ 1841 MeV    (vs empirical 217 MeV — one-loop divergence)
DFC T_c estimate ≈ 1160 MeV        (vs observed 154 MeV — 653% error)
```

The 653% error traces directly to:
1. The 11% error in α_s(M_Z) from M_c(D7) not derived from substrate
2. The one-loop running formula is uncontrolled at hadronic scales (non-perturbative regime)

The proper path to T_c requires either lattice calculation of the D7 closure partition
function, or a non-perturbative DFC computation beyond the current one-loop framework.

### KSS Viscosity Bound

The ratio of shear viscosity to entropy density (η/s) has a conjectured lower bound from
the AdS/CFT correspondence. This lower bound equals one divided by four pi:

```
η/s ≥ 1/(4π) ≈ 0.0796    [KSS bound, Kovtun-Son-Starinets 2005]
```

The RHIC QGP measurement gives η/s ≈ 1-4 times this bound — the closest approach to
the bound of any known fluid. In DFC, this bound may follow from the SU(3) commutator
structure of the D7 closure (analogous to how the Tsirelson bound CHSH ≤ 2√2 was proved
from SU(2) commutator norms in Cycle 35). This connection is suggestive and not yet derived.

### Order Parameter: Polyakov Loop

The Polyakov loop L is the thermal Wilson loop in the imaginary time direction — its
expectation value is zero in the confined phase (global center symmetry preserved) and
nonzero in the deconfined phase (symmetry broken):

```
⟨L⟩ = 0    (T < T_c, confined — global Z₃ center symmetry of SU(3) unbroken)
⟨L⟩ ≠ 0    (T > T_c, deconfined — Z₃ symmetry spontaneously broken)
```

In DFC, the Polyakov loop is the thermal holonomy of the D7 SU(3) connection around
the compactified time direction. The center symmetry Z₃ ⊂ SU(3) is the DFC analog of
the discrete residual symmetry that distinguishes confined and deconfined phases.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Deconfinement exists | D7 flux tubes thermally disrupted above T_c | QGP at RHIC/LHC confirmed | ✓ structural |
| Near-perfect fluid (η/s near bound) | Near-critical D7 dynamics → maximal correlations | η/s ≈ 1–4 × 1/(4π) at RHIC | ✓ structural (qualitative) |
| QGP as early-universe phase | D7 SU(3) closure not yet stabilized above T_c | Universe in QGP state t < 10 μs | ✓ structural |
| T_c ≈ 155 MeV | DFC estimates 1160 MeV (one-loop, blocked by α_s error) | 154 ± 9 MeV (lattice QCD) | ✗ 653% off — α_s blockage |
| Z₃ center symmetry breaking | Polyakov loop ⟨L⟩ from D7 holonomy | ⟨L⟩ = 0 → ≠ 0 across crossover | ✓ structural (topology) |
| Crossover, not first order at μ_B=0 | D7 crossover character depends on quark masses | Crossover confirmed by lattice | structural account open ✗ |

---

## Open Questions

1. **Derive T_c from D7 closure geometry.** The deconfinement temperature should follow
   from the string tension σ and the D7 closure parameters. The blocking step is deriving
   α_s at the QCD scale from the DFC substrate — specifically M_c(D7) from substrate
   dynamics (Bottleneck 2). Once M_c(D7) is derived, α_s(M_c) = g²/(4π) is fixed and
   the running to hadronic scales becomes a calculation rather than an estimate.

2. **KSS bound from D7 SU(3) commutator structure.** The Tsirelson bound CHSH ≤ 2√2
   was derived from SU(2) commutator norms (Cycle 35). An analogous argument may derive
   η/s ≥ 1/(4π) from the SU(3) commutator algebra of the D7 closure — the viscosity
   bound as a structural consequence of the D7 topology rather than an import from
   AdS/CFT. This would be a genuine DFC prediction.

3. **QCD critical endpoint at finite baryon density.** The QCD phase diagram at nonzero
   baryon chemical potential μ_B may have a critical endpoint where the crossover becomes
   a first-order transition. In DFC, this corresponds to the D7 closure under combined
   thermal and baryon density compression — a two-parameter deformation of the V(φ)
   effective potential. The search for this endpoint is an active experimental program
   (RHIC BES, CBM at FAIR).

4. **Jet quenching coefficient q̂ from D7 medium.** The jet quenching parameter q̂
   measures the rate of transverse momentum broadening of a high-energy parton traversing
   the QGP. DFC should predict q̂ from the D7 gluon density and the substrate coupling
   g_s. The current α_s error propagates into this prediction.

---

## Connections

- `phenomena/particle_physics/forces/strong_force.md` — confinement from D7 SU(3) closure
- `phenomena/particle_physics/particles/quarks.md` — D7 kinks as quarks
- `phenomena/particle_physics/particles/gluons.md` — D7 connection fields as gluons
- `phenomena/cosmology/baryogenesis.md` — pre-QCD-crossover baryon generation
- `phenomena/thermodynamics/phase_transitions.md` — phase transitions from V_eff bifurcations
- `equations/quark_gluon_plasma.py` — numerical estimates; T_c 653% error; α_s blockage confirmed
- `equations/coupling_derivation.py` — α_s(M_Z) = 0.105 (11% below observed)
