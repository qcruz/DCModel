# Phenomenon: Baryogenesis

## One-Sentence Synthesis

> Baryogenesis in DFC is the net baryon winding number generated during the D7 SU(3)
> closure event — an irreversible first-order buckling that satisfies all three Sakharov
> conditions by construction (B violation during formation, CP asymmetry from the closure
> chirality, out-of-equilibrium dynamics from the buckling itself), with the asymmetry
> then frozen by B−L conservation after the closure stabilizes.

---

## Observation

The observable universe contains approximately η_B ≡ (n_B − n_B̄)/n_γ ≈ 6 × 10⁻¹⁰
baryons per photon. This ratio measures the fractional excess of matter over antimatter
that survived from the early universe. Consequences:

- Without baryogenesis, every baryon would have annihilated with an antibaryon, leaving
  only photons. No protons, no atoms, no stars.
- The asymmetry is tiny — one part in a billion — but sufficient to produce every
  baryon in the observable universe (including ~10⁸⁰ protons).
- The CMB spectrum is consistent with this ratio: η_B is extracted from the acoustic
  peak heights (Planck 2018: η_B = 6.10 ± 0.04 × 10⁻¹⁰).
- Big Bang nucleosynthesis (BBN) predicts light element abundances that depend on η_B.
  Observed D/H, ⁴He, and ⁷Li abundances are consistent with η_B ≈ 6 × 10⁻¹⁰.

---

## Sakharov's Three Conditions

Sakharov (1967) showed that any baryogenesis mechanism must satisfy:

**1. Baryon number violation (ΔB ≠ 0):** Without it, any initial B asymmetry would
be preserved but none could be generated from a symmetric initial state.

**2. C and CP violation:** Without them, any process generating baryons would generate
equal numbers of antibaryons — net B = 0.

**3. Departure from thermal equilibrium:** In thermal equilibrium, CPT symmetry guarantees
equal production of particles and antiparticles — net B = 0 in equilibrium.

The Standard Model has all three in principle (B violation via sphalerons, CP violation
via CKM phase, electroweak phase transition as non-equilibrium event), but the SM values
are insufficient: CKM phase gives too little CP violation, and the electroweak transition
is not strongly first-order for m_H ≈ 125 GeV.

---

## Dimensional Folding Explanation

### The D7 Closure as a Baryogenesis Event

The proton is stable in DFC because the SU(3) color topology at D7 is a product group
factor with no connection to the D5 lepton sector — quarks cannot turn into leptons through
any gauge interaction (see `phenomena/particle_physics/proton_stability.md`).

This absolute stability has a necessary consequence: **baryon number is not a symmetry
that can be violated by any low-energy process.** The baryon asymmetry of the universe
cannot have been generated after the D7 closure stabilized. It must have been generated
during the D7 closure itself — the one moment when the SU(3) topology was forming and
B could be imprinted as a structural initial condition.

The sphaleron analysis confirms this:
```
Sphalerons (D6 SU(2) topological transitions) violate B+L but preserve B−L.
→ Sphalerons can redistribute the asymmetry between baryons and leptons,
  but cannot change the total B−L.
→ If B−L is generated at D7 and then frozen, sphalerons cannot wash it out.
```

This is leptogenesis-compatible: whatever B−L asymmetry was generated at D7 closure
survives sphaleron washout and appears as the observed baryon excess.

### How the D7 Closure Satisfies the Sakharov Conditions

**Condition 1 — Baryon number violation during formation:**

The D7 closure is the formation of the SU(3) topology from the preceding unstructured
field. During this formation, the color winding numbers (which label quarks vs. antiquarks)
do not yet exist as a conserved quantity — they are being created. The formation can
produce a net winding number if the formation process is asymmetric. After the topology
stabilizes, the winding numbers (B and L) are conserved. The violation occurs only
during the formation — not before, not after.

This is analogous to monopole formation during a phase transition: magnetic charge is
not conserved in the disordered phase but is conserved in the ordered phase. The net
charge depends on the dynamics of the transition itself (Kibble-Zurek mechanism).

**Condition 2 — CP violation from D7 closure chirality:**

The D7 SU(3) closure, like the D6 S³ closure, has an intrinsic chirality that can
break CP symmetry. The SU(3) group is isomorphic to its complex conjugate under CPT,
but the dynamical process of closure — the buckling instability at D7 — selects a
specific orientation in the SU(3) manifold. If the closure process is not CP-symmetric
(i.e., if the buckling dynamics at D7 are not invariant under combined charge conjugation
and spatial reflection), then slightly more baryon windings than antibaryon windings
can be generated.

The existing CKM CP-violating phase (δ_CKM ≈ 1.2 rad) may be a residual imprint of
this closure chirality, frozen into the quark mixing structure as the D7 topology
stabilized. Whether δ_CKM is derivable from D7 closure geometry is an open derivation.

**Condition 3 — Out of equilibrium:**

The D7 closure is a first-order buckling instability: the compression field suddenly
breaks from the symmetric (unconfined) phase to the asymmetric (color-confined) phase.
A first-order phase transition is intrinsically out of thermal equilibrium — the
transition proceeds through bubble nucleation and propagation, with the bubble walls
separating the confined and unconfined phases. The matter and antimatter densities in
the wall region are not in equilibrium, satisfying Condition 3.

This is exactly the electroweak baryogenesis picture, but at the QCD scale:
the D7 SU(3) closure is the QCD confinement phase transition, which is first-order
(in some parameter regimes) and provides the non-equilibrium environment.

### The B−L Conservation Argument

After the D7 closure stabilizes:
- Baryon number B is conserved (proton is stable; no gauge-mediated B violation)
- Lepton number L is approximately conserved (neutrino masses are nonzero but small)
- Sphalerons can change B+L by multiples of 3 (one generation), but B−L is preserved

If the D7 closure generated a net (B−L) = (B_D7 − L_D7), sphalerons will redistribute
this asymmetry so that:

```
B_final = (B−L) × 12/(23+n_flavors) = η_B × s / T³

where s is entropy density.
```

The factor converts the initial B−L into the observed B through sphaleron equilibration.
This is the standard leptogenesis result applied to D7 baryogenesis.

### Why the Exact Value η_B ≈ 6 × 10⁻¹⁰ Is Not Yet Derived

The DFC mechanism explains *that* a baryon asymmetry is generated at D7 closure and
*why* it survives. It does not yet predict the magnitude.

The magnitude depends on:
1. The CP-asymmetric parameter in the D7 closure dynamics — analogous to ε in standard
   leptogenesis but from D7 closure geometry rather than heavy right-handed neutrino decays
2. The efficiency of the closure transition — what fraction of the generated asymmetry
   survives dilution and washout
3. The dilution factor from subsequent entropy production (primarily QCD confinement itself
   liberates significant entropy)

Computing these would require:
- The D7 closure rate (the bubble nucleation rate in the SU(3) confinement transition)
- The CP asymmetry ε_D7 in the closure dynamics
- The washout factor (suppressed for strong transitions)

This is the central unresolved quantitative problem in the DFC cosmology sector.

---

## Formal Equations

### Baryon-to-Photon Ratio (Observed)

```
η_B = (n_B − n_B̄) / n_γ = 6.10 ± 0.04 × 10⁻¹⁰   [Planck 2018]

Equivalently: Ω_b h² = 0.02237 ± 0.00015   [baryon density parameter]
```

### Sphaleron Conversion of B−L to B

After D7 closure, sphalerons equilibrate in thermal bath at T ≫ 100 GeV:

```
B_final = a × (B−L)_D7

where a = 28/(79+n_s) ≈ 28/79 ≈ 0.35   [for N_gen = 3, standard sphaleron result]
```

If the D7 closure generated (B−L)_D7 ≈ 10⁻⁸ × s_D7, sphaleron conversion gives
B_final ≈ 3.5 × 10⁻⁹ × s_D7, consistent with η_B when accounting for entropy
production. The initial (B−L) magnitude is the underived input.

### Kibble-Zurek Estimate of Defect Density

In a first-order phase transition, topological defects (monopoles, strings, domain walls)
form with density set by the correlation length at the transition:

```
n_defect ~ ξ⁻³     where ξ = coherence length at T_D7 (QCD transition, ~150 MeV)

ξ ≈ ℏc / (kT_D7) ≈ 1.3 fm    at T_D7 = 150 MeV

n_defect ~ (1.3 fm)⁻³ ≈ 0.47 fm⁻³ ≈ 3.5 × 10⁴¹ m⁻³
```

The baryon number density at that time:
```
n_B(T_D7) ≈ η_B × n_γ(T_D7) = η_B × (2ζ(3)/π²) T_D7³ ≈ 6×10⁻¹⁰ × 0.45 × (150 MeV/ℏc)³
```

This is not a derivation — it establishes the scale at which D7 closure defects form
relative to the baryon density. Whether these defects carry net baryon number is the
open question.

---

## Consistency Checks

| Requirement | DFC mechanism | Status |
|---|---|---|
| B violation during generation | D7 winding numbers not yet conserved during formation | ✓ structural |
| B−L conservation after formation | Product topology + no cross-closure carriers | ✓ (from proton_stability.md) |
| CP violation source | D7 closure chirality / CKM phase as frozen imprint | structural (undetermined) |
| Out-of-equilibrium | First-order D7 buckling instability | ✓ structural |
| Sphaleron washout avoided | B−L is conserved by sphalerons | ✓ (from proton_stability.md) |
| Magnitude η_B ≈ 6×10⁻¹⁰ | Requires D7 closure CP asymmetry calculation | **open** |
| BBN consistency | η_B is input, not output | ✓ (consistent by construction) |

---

## Open Questions

1. **Derive η_B from D7 closure dynamics.** The central unsolved problem. The CP
   asymmetry generated during D7 closure depends on the dynamics of the SU(3) phase
   transition. Whether DFC predicts η_B ≈ 6 × 10⁻¹⁰ or whether this number is an
   input is not yet determined.

2. **Is the D7 closure first-order?** QCD lattice simulations suggest the confinement
   transition at zero baryon density is actually a crossover (not first-order) for
   physical quark masses. If so, it does not strongly satisfy Condition 3. Whether the
   DFC D7 closure is first-order for the initial closure conditions (which differ from
   equilibrium QCD) requires analysis of the closure dynamics.

3. **CKM phase from D7 closure geometry.** The CP-violating phase δ_CKM ≈ 1.2 rad in
   the CKM matrix might be a residual imprint of the D7 closure chirality. Deriving
   δ_CKM from the SU(3) closure topology would both explain the CKM structure and
   provide a CP violation source for D7 baryogenesis.

4. **Leptogenesis vs. D7 baryogenesis.** Standard leptogenesis generates B−L through
   heavy right-handed neutrino decays at T ~ 10¹⁰ GeV. In DFC, right-handed neutrinos
   are not independently postulated (they would arise from the D6 closure structure).
   Whether DFC admits a standard leptogenesis mechanism in addition to D7 baryogenesis,
   or whether D7 baryogenesis replaces it, has not been analyzed.

5. **Baryon isocurvature perturbations.** If baryogenesis occurs at D7 closure via a
   local mechanism (bubble nucleation), there should be spatial fluctuations in η_B
   correlated with the QCD bubble wall structure. These would appear as baryon isocurvature
   perturbations in the CMB power spectrum. Current Planck constraints place tight limits
   on isocurvature — these constraints restrict the D7 closure mechanism's spatial
   coherence scale.

---

## Connections

- **Proton stability** — B−L conservation, sphaleron analysis, D7 product topology;
  `phenomena/particle_physics/proton_stability.md`
- **CP violation** — the source of the CP asymmetry in the D7 closure;
  `phenomena/particle_physics/cp_violation.md`
- **Three generations** — CKM mixing structure as potential D7 closure imprint;
  `foundations/three_generations.md`
- **Big Bang** — the broader cosmological context;
  `phenomena/cosmology/big_bang.md`
- **Strong force** — D7 SU(3) confinement transition;
  `phenomena/particle_physics/forces/strong_force.md`
- **Cosmic expansion** — dilution of the baryon asymmetry during expansion;
  `phenomena/cosmology/cosmic_expansion.md`
