# Phenomenon: Cosmic Microwave Background

## One-Sentence Synthesis

> The CMB is the relic thermal distribution of massless D2 compression modes from the
> epoch of recombination — a near-perfect blackbody at T_rec ≈ 3000 K, now redshifted
> to 2.725 K by cosmic expansion, whose extraordinary uniformity (10⁻⁵) is structurally
> explained by the substrate's pre-D3 connectivity, while the small anisotropies that
> seeded all large-scale structure remain an open derivation.

---

## Observation

The CMB is thermal radiation filling all of space, discovered in 1965 by Penzias and
Wilson. Key measured properties:

- **Temperature:** T₀ = 2.7255 ± 0.0006 K (FIRAS/COBE 2009)
- **Spectrum:** Near-perfect blackbody; deviations from Planck spectrum < 50 ppm
- **Uniformity:** Temperature uniform to ΔT/T ~ 10⁻⁵ across the sky (after removing
  the dipole from our peculiar velocity)
- **Polarization:** E-mode polarization at ~5 μK RMS; B-mode upper limits constrain
  inflationary gravitational waves
- **Acoustic peaks:** Power spectrum shows peaks at ℓ ≈ 220, 540, 810... (angular
  multipoles corresponding to sound horizon multiples)
- **Recombination redshift:** The CMB surface of last scattering is at z ≈ 1100,
  corresponding to T_rec ≈ 3000 K and t_rec ≈ 380,000 years after the Big Bang
- **Baryon acoustic oscillations:** The same acoustic scale imprinted in the CMB is
  also visible in the large-scale distribution of galaxies

---

## Standard Explanation

Before recombination (z > 1100), photons and baryons formed a tightly coupled fluid.
Acoustic oscillations in this baryon-photon plasma produced compressions and rarefactions
at specific length scales set by the sound horizon r_s:

```
r_s = ∫₀^{t_rec} c_s dt / a(t)   [sound horizon at recombination]
c_s = c/√3(1 + R)               [sound speed; R = 3ρ_b/(4ρ_γ)]
```

At recombination, when T dropped below ~3000 K, electrons and protons combined into
neutral hydrogen. Photons decoupled from matter and have free-streamed since.

The CMB blackbody spectrum follows from the Planck distribution at T_rec, then
redshifted: T(z) = T₀(1+z). The acoustic peaks in the angular power spectrum
C_ℓ reflect modes that were in specific phases (maximum compression or rarefaction)
at recombination.

The anisotropies ΔT/T ~ 10⁻⁵ originate from primordial density perturbations — small
fluctuations in the baryon-photon fluid that were amplified by gravity and frozen at
recombination. Their amplitude A_s ≈ 2×10⁻⁹ and nearly scale-invariant spectral
index n_s ≈ 0.965 are predicted by inflation.

---

## Dimensional Folding Explanation

### Perspective 1: From the observer in spacetime

At z ≈ 1100, the universe became transparent. Photons that had been scattered by free
electrons now free-streamed without interaction. The observer sees a snapshot of the
universe at that epoch — a sphere of photons emitted from a surface 42 billion
light-years away (comoving), carrying the temperature map of the baryon-photon plasma
at T_rec ≈ 3000 K.

The DFC observer-frame account: the CMB photons are D2 modes (massless compression
field propagation modes) that have been free-streaming through the D3 localization
layer since recombination. Their spectrum is that of a blackbody because the baryon-
photon plasma before recombination was in thermal equilibrium at each epoch —
the D2 mode distribution was the Bose-Einstein distribution at T(t).

### Perspective 2: From the substrate

The substrate at the recombination epoch was in a state where D2 modes were thermally
excited at temperature T_rec ≈ 3000 K, with D3+D4 structure (baryons) forming a
coupled fluid. The thermal equilibrium was maintained by Compton scattering — D5
photon-electron scattering, which coupled the D2 radiation modes to the D3+D4 matter
kinks.

When the temperature dropped below the hydrogen ionization threshold (~13.6 eV at
some critical density), the rate of Compton scattering fell below the expansion rate
and the coupling broke. The D2 modes decoupled from D3+D4 matter and propagated freely
thereafter.

From the substrate's perspective, this is a decoherence event: the D2 modes ceased
to be coupled to the D3+D4 compression field configuration and became free-propagating
modes. Their distribution at decoupling was frozen — a snapshot of the thermal D2 mode
distribution at T_rec.

The redshifting of the CMB temperature T(z) = T₀(1+z) is the consequence of cosmic
expansion: as the D3 localization layer is globally re-tiled (cosmic expansion), the
wavelengths of D2 modes stretch proportionally. This is a direct consequence of the
DFC lateral redistribution account of expansion.

### The Uniformity: Pre-D3 Connectivity

The most striking feature of the CMB is its uniformity: T uniform to 10⁻⁵ across
regions that were separated by more than the causal horizon at recombination. In
standard cosmology, this requires inflation to explain.

In DFC, the uniformity is structurally explained (see `phenomena/cosmology/big_bang.md`):

The substrate is one continuous object. Before D3 localization produced apparent spatial
separation, there was no spatial distance — the substrate was connected by construction.
Correlations across what appear as large spatial separations in D3 are correlations
within a single object that predate the emergence of spatial separation.

The CMB uniformity reflects the uniformity of the substrate at the pre-D3 epoch:
at maximum compression (near-D1), the substrate has no spatial structure and therefore
no spatial variation. The uniformity is not a coincidence requiring exponential
inflation to set up — it is the expected state of a substrate that was connected
before D3 separation.

**Quantitative test:** The CMB is uniform to ΔT/T ~ 10⁻⁵. The DFC structural account
predicts exact uniformity from the pre-D3 connectivity; the 10⁻⁵ residual is the
amplitude of the primordial perturbations, which is an open derivation (see below).

### The Blackbody Spectrum: D2 Mode Bose-Einstein Distribution

The CMB blackbody spectrum follows directly from the account developed in
`phenomena/thermodynamics/blackbody_radiation.md`:

D2 modes (massless compression waves, photons) are bosons. In thermal equilibrium at
temperature T, the mean occupation number of each mode at frequency ν is:

```
n(ν) = 1/(e^{hν/kT} − 1)    [Bose-Einstein distribution for massless modes]
```

The mode density of D2 modes in D3 space (two polarizations, volume V):

```
dN/dν = (8πν²V/c³)    [density of states — from KG dispersion in 3D, two modes]
```

The energy spectral density:

```
u(ν, T) = (8πhν³/c³) × 1/(e^{hν/kT} − 1)    [Planck spectrum — derived ✓]
```

This is the CMB spectrum. The observed T₀ = 2.7255 K fits this formula to < 50 ppm.

The current CMB temperature follows from the recombination temperature and redshift:

```
T₀ = T_rec / (1 + z_rec) = 3000 K / 1100 ≈ 2.73 K    [consistent ✓]
```

---

## Anisotropies: The Open Problem

The CMB anisotropies ΔT/T ~ 10⁻⁵ encode two distinct things:

**1. The primordial perturbation spectrum:**
Small fluctuations in the substrate density before recombination. These trace back to
whatever produced density perturbations in the early universe — in standard cosmology,
quantum fluctuations stretched to cosmological scales during inflation.

In DFC, the origin of the primordial perturbation spectrum is an open derivation:
- The Big Bang is a buckling instability (first compression threshold crossing)
- The buckling cascade may naturally generate density perturbations with a
  Harrison-Zel'dovich-like (scale-invariant) spectrum — but this has not been derived
- The amplitude A_s ≈ 2×10⁻⁹ is not predicted from DFC parameters

**2. Acoustic oscillations before recombination:**
Given a primordial perturbation spectrum, the baryon-photon fluid's acoustic evolution
until recombination is well-understood (and reproduced identically by DFC via the
SM fluid equations, which the DFC does not modify). The acoustic peak structure in
the angular power spectrum (ℓ_peak ≈ 220, 540, 810...) is inherited from SM.

**DFC status for anisotropies:**
- Large-scale power (ℓ < 10): connected to horizon problem (explained structurally) ✓
- Acoustic peaks: inherited from SM baryon-photon fluid physics ✓ (not DFC-derived)
- Primordial amplitude A_s: not derived — OPEN
- Spectral index n_s ≈ 0.965 (slight red tilt): not derived — OPEN

---

## Analogy: Ringing Bell in a Dark Room

Imagine a massive bell struck at the center of a very large dark room. Sound waves
propagate outward in all directions. After some time, the bell cools and stops
vibrating. An observer far away later hears the residual sound — a fading wave
pattern whose spectrum depends on the bell's temperature at the moment it stopped
ringing, and whose angular distribution reflects the initial distribution of
the striking.

- The bell = the hot plasma at recombination
- The room = D3 space
- Sound waves = D2 compression modes (photons)
- The observed sound after the bell cools = CMB photons free-streaming today
- The specific ring pattern = acoustic oscillations before recombination

**Where it breaks down:** Sound in a room decays exponentially (energy dissipates into
the room's walls). CMB photons travel without dissipation through the transparent
universe since recombination. The analogy captures the "snapshot of thermal
equilibrium" character but not the lossless propagation since decoupling.

---

## Formal Equations

### CMB Planck Spectrum (derived from D2 mode Bose-Einstein statistics)

```
u(ν, T₀) = (8πhν³/c³) / (e^{hν/kT₀} − 1)    T₀ = 2.7255 K

Observed CMB peak:
ν_peak = 2.82 kT₀/h = 160 GHz   (from Wien's law: λ_peak = 1.06 mm) ✓

Total CMB energy density:
ρ_CMB = (π²/15)(kT₀)⁴/(ℏc)³ ≈ 4.2×10⁻¹⁴ J/m³ ✓
```

### Temperature Redshift

```
T(z) = T₀ × (1 + z)

At recombination: T(z=1100) = 2.7255 × 1101 ≈ 3002 K   (ionization threshold ✓)
At matter-radiation equality: T(z=3400) ≈ 9262 K
```

### Angular Power Spectrum (from SM, not yet derived from DFC)

```
C_ℓ = (2/π) ∫ k² P(k) |Δ_ℓ(k)|² dk

P(k) ∝ k^{n_s}     primordial power spectrum   [n_s ≈ 0.965, DFC: OPEN]
A_s ≈ 2×10⁻⁹      amplitude                   [DFC: OPEN]

Acoustic peaks at ℓ_n ≈ nπ/(r_s/d_A)  where d_A is the angular diameter distance
First peak: ℓ_1 ≈ 220   [observed ✓, inherited from SM fluid physics]
```

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| Planck spectrum shape | D2 Bose-Einstein statistics at T_rec | T₀ = 2.7255 K; deviations < 50 ppm | Derived ✓ |
| T₀ = T_rec/(1+z_rec) | Cosmic expansion redshifts D2 wavelengths | 3000/1100 ≈ 2.73 K ✓ | Derived ✓ |
| CMB uniformity (ΔT/T ~ 10⁻⁵) | Pre-D3 substrate connectivity (no horizon problem) | Uniform to 10⁻⁵ | Structural ✓ |
| Flatness (Ω_k ≈ 0) | Near-D1 has no spatial geometry by construction | Ω_total = 1.000 ± 0.004 | Structural ✓ |
| Acoustic peak positions | Inherited from SM baryon-photon fluid equations | Peaks at ℓ ≈ 220, 540, 810 | Inherited ✓ |
| Primordial amplitude A_s | Not derived from DFC compression dynamics | A_s ≈ 2×10⁻⁹ | OPEN ✗ |
| Spectral index n_s | Not derived — no DFC inflation analog | n_s ≈ 0.965 | OPEN ✗ |
| CMB B-mode polarization | Compression waves → scalar perturbations; tensor modes OPEN | r < 0.06 (Planck/BICEP) | OPEN ✗ |
| Baryon-photon coupling before recombination | Compton scattering = D5 photon-electron kink interaction | Thomson optical depth τ ≈ 0.054 | Inherited from SM |

---

## Connections to Other Phenomena

- `phenomena/cosmology/big_bang.md` — the Big Bang as first buckling instability;
  the pre-D3 connectivity that explains CMB uniformity is established there
- `phenomena/cosmology/cosmic_expansion.md` — expansion redshifts T(z) = T₀(1+z);
  the D2 mode wavelengths stretch with lateral redistribution
- `phenomena/thermodynamics/blackbody_radiation.md` — the Planck spectrum derivation
  from D2 mode Bose-Einstein statistics; CMB inherits this account directly
- `phenomena/light/light.md` — CMB photons are D2 modes; same structural description
- `phenomena/cosmology/dark_matter.md` — dark matter's gravitational effects on CMB
  power spectrum are a key observable; DFC dark matter candidate (~35 keV kinks)
  must reproduce the observed acoustic peak ratios
- `phenomena/gravity/gravitational_waves.md` — primordial GW background would
  generate CMB B-mode polarization; the same open problem (tensor from scalar φ)
  appears here

---

## Open Questions

1. **Derive the primordial perturbation amplitude A_s from DFC compression dynamics.**
   The CMB anisotropy amplitude ΔT/T ~ 10⁻⁵ traces to A_s ≈ 2×10⁻⁹. In DFC, the
   first buckling instability at the Big Bang generates compression perturbations.
   Whether these perturbations have the right amplitude and scale-invariant spectrum
   requires computing the quantum fluctuations of the compression field near the first
   bifurcation threshold — the DFC analog of slow-roll inflation's power spectrum formula.

2. **Account for the slight red tilt n_s ≈ 0.965.** A perfectly scale-invariant
   spectrum has n_s = 1. The observed slight red tilt (suppression of small-scale
   power) is predicted by slow-roll inflation to ~1%. In DFC, a deviation from
   n_s = 1 would arise from the compression field's dynamics not being perfectly
   scale-free near the first bifurcation — the running of α, β, c with compression
   scale. Whether this produces a consistent 3.5% red tilt is open.

3. **CMB B-mode polarization and tensor modes.** Primordial gravitational waves
   produce a distinct B-mode polarization pattern in the CMB. The tensor-to-scalar
   ratio r measures the amplitude of these GW relative to scalar perturbations.
   Current limits: r < 0.06. DFC's scalar φ field does not naturally produce tensor
   perturbations (the same gap as in gravitational_waves.md). Whether DFC predicts
   r = 0 (no primordial GW) or some small r (from composite tensor metric structure)
   is open.

4. **CMB as test of DFC dark matter (~35 keV warm DM candidate).** Warm dark matter
   suppresses structure formation below the free-streaming length. The CMB acoustic
   peak ratios and the matter power spectrum constrain the dark matter mass. Whether
   the DFC ~35 keV candidate is consistent with CMB constraints (Lyman-alpha forest
   limits, structure suppression at small scales) requires comparing the DFC thermal
   relic abundance and free-streaming length to Planck CMB posterior.
