# Phenomenon: Dark Matter

## One-Sentence Synthesis

> In DFC, dark matter is the population of stable intermediate-depth closures that anchor
> deeply enough to acquire inertia (reach D4) but not deeply enough to complete the U(1)
> winding at D5 — structurally massive but electromagnetically invisible, gravitationally
> active because they compress the same substrate that produces the gravitational field,
> with a DFC mass estimate of ~35 keV placing them in the warm dark matter regime; the
> cosmological abundance Ω_DM ≈ 0.265 is not yet derived from DFC parameters.

---

## Observed Properties

```
Cosmological abundance (Planck 2018):
  Ω_DM h² = 0.1200 ± 0.0012
  Ω_DM    = 0.265
  Ω_b     = 0.049  (baryons)
  Ω_DM / Ω_b ≈ 5.4  (dark matter outweighs ordinary matter ~5:1)

Galaxy rotation curves (Rubin & Ford 1970; van Albada et al. 1985):
  Observed: v(r) = const beyond optical disk (~flat)
  Newtonian expectation: v(r) ∝ r^{−1/2} (Keplerian)
  Implication: enclosed mass grows ∝ r beyond luminous disk → extended mass halo

Gravitational lensing:
  Weak lensing maps (SDSS, DES, KiDS) → DM halos trace galaxy overdensities
  Bullet Cluster (1E 0657-56, 2006): DM and gas decouple during cluster merger
    X-ray gas (baryons): slows and heats → displaced from DM
    DM halos: pass through each other nearly collisionlessly
    Constraint: DM self-interaction σ/m < 1 cm²/g

CMB power spectrum (Planck 2018):
  DM suppresses odd acoustic peaks relative to even (no photon pressure)
  First peak (l ≈ 220) height ratio encodes Ω_DM/Ω_b
  DM drives structure formation: seeds gravitational wells into which baryons fall

Large-scale structure:
  CDM predicts hierarchical structure (small → large) — well-confirmed at scales > 1 Mpc
  Tension at small scales:
    Missing satellites: fewer dwarf galaxies observed than CDM simulates (~10-50×)
    Core-cusp: CDM predicts cuspy DM halo centers; observations suggest cores
    Too-big-to-fail: CDM predicts dense massive satellites that are not observed
    All three partly resolved by warm DM (keV-scale mass → free-streaming erases small structures)

Non-detection (direct + collider):
  XENON1T / LUX / PandaX: no DM-nucleus scattering signal
  LHC: no missing energy signal consistent with WIMP pair production
  AMS-02: no antihelium (no DM annihilation signal in cosmic rays)
  Fermion mass range excluded: WIMP thermal relics below ~few GeV (from relic density + direct)
```

---

## DFC Account

### Dark Matter as Incomplete-Depth Closures

In DFC, every massive particle is a stable compression field kink that has anchored to
sufficient depth. The depth determines which properties the closure acquires:

```
D2: propagation mode — massless (photon-like)
D3: localization — exists at a position
D4: inertia onset — acquires rest mass
D5: U(1) closure — acquires electric charge
D6: SU(2) closure — acquires weak interaction, spin-1/2 statistics
D7: SU(3) closure — acquires color charge
```

**Dark matter is a closure that stops between D4 and D5.** It acquires inertia (mass)
by completing D4, but the U(1) winding at D5 does not close — there is no stable
electromagnetic winding number. Without a D5 winding, the closure:

- Has no electric charge → does not emit or absorb photons
- Has no color → does not interact via gluon exchange
- Has mass → gravitational interaction through the compression gradient field
- May partially reach D6 → very weak interaction from incomplete SU(2) coupling

The "darkness" of dark matter is not a mysterious absence — it is the natural
consequence of a closure that stabilizes before reaching the electromagnetic closure
depth. The substrate that produces dark matter is the same substrate as ordinary matter;
the difference is depth of anchoring.

### Mass Estimate from the Depth Model

From the depth-to-mass relation (see `foundations/mass_hierarchy.md` and
`equations/quark_masses.py`):

```
m(d) = m_e × exp(κ × (d − d_e))

where:
  m_e  = 0.511 MeV (electron mass — anchor point at d_e = 5)
  κ    ≈ 5.33     (depth-to-mass scaling exponent)
  d_e  = 5         (electron depth)
```

For a dark matter closure at depth d_DM ≈ 4.5 (between D4 and D5):

```
m_DM ≈ 0.511 MeV × exp(5.33 × (4.5 − 5.0))
      = 0.511 MeV × exp(−2.665)
      ≈ 0.511 MeV × 0.069
      ≈ 35 keV
```

This is warm dark matter territory. For comparison:
- Cold DM (WIMP): ~GeV–TeV
- Sterile neutrino DM: ~keV–few keV (Dodelson-Widrow: ~1–10 keV)
- DFC prediction: ~35 keV

**Consistency with small-scale structure:** Warm dark matter has free-streaming
length λ_fs ∝ 1/m_DM. At m_DM ~ 35 keV, structures below ~100 kpc are washed out —
qualitatively resolving the missing satellites, core-cusp, and too-big-to-fail problems
without additional fine-tuning.

**Lyman-alpha forest constraint:** Thermal WDM requires m > 3.5 keV (Viel et al. 2013)
to preserve observed small-scale structure in the Lyman-alpha forest. DFC at ~35 keV
comfortably satisfies this. ✓

### Collisionless Behavior (Bullet Cluster)

The Bullet Cluster shows that DM halos pass through each other with minimal
self-interaction. In DFC, the self-interaction of intermediate-depth kinks is through
compression field exchange at D4 depth. Since the kinks carry no D5 (EM) or D7 (color)
winding, the dominant self-interaction is gravitational — the same compression gradient
coupling that produces gravity for all structures.

The kink-kink interaction via direct D4 compression exchange would be short-range
(Yukawa-type, range ~ kink width λ = ℏ/(m_DM c) ≈ 6 nm for m_DM = 35 keV). At
galactic scales, this is negligibly short — consistent with the Bullet Cluster bound
σ/m < 1 cm²/g. A formal calculation of this cross-section from the φ⁴ kink-kink
scattering formula is an open problem.

### The Thermal Relic Overclosure Problem

**Important caveat:** A fully thermalized species with m = 35 keV that decoupled
while relativistic (like a standard warm dark matter fermion) would contribute:

```
Ω h² ≈ m / (93 eV) × (g_s(T_dec)/10.75)^{−1}
```

For m = 35 keV, this gives Ω h² ≫ 1 — the universe would be vastly overclosed.
This is the standard overclosure problem for warm dark matter candidates.

Resolution paths in DFC:
1. **Non-thermal production:** DFC DM candidates may not thermalize with the SM bath.
   They have no EM or color coupling. If produced via D4-depth compression dynamics
   during the QCD phase transition (or another non-equilibrium event), the relic
   density is set by the production rate rather than thermal equilibrium. This is
   analogous to the Dodelson-Widrow mechanism for sterile neutrinos (produced via
   oscillation mixing, not thermalization).

2. **Dilution by entropy production:** If the SM plasma undergoes entropy injection
   (e.g., from QCD transition, or D7 buckling event) after DM production, the DM/photon
   ratio is diluted. This lowers Ω_DM relative to the naive thermal estimate.

3. **Different depth assignment:** If d_DM is not exactly 4.5 but is adjusted by a
   small amount, or if multiple intermediate-depth species contribute with a spectrum
   of masses, the effective abundance could match observations.

**Status:** The thermal relic problem is a real constraint on the DFC DM candidate.
The DFC framework motivates the mass range but does not yet predict the production
mechanism or resulting abundance. Ω_DM = 0.265 is not derived.

### Why Gravitational Coupling

In DFC, gravity is the compression gradient field — the tendency of compressed structures
to relieve their compression by redistributing into neighboring field configurations.
All structures that have acquired D3 localization and D4 inertia couple to this gradient,
regardless of their electromagnetic or color properties. The DFC DM kink, sitting at
d_DM ≈ 4.5, has completed D3 (it is localized) and D4 (it has inertia). It therefore
participates in the compression gradient field — it has gravitational mass.

This is why dark matter clusters like ordinary matter on large scales but is dark:
the gravitational and electromagnetic couplings are at different depths. A closure can
complete D4 without completing D5.

### Structure Formation

The DFC DM halos seed structure formation in the same way as ΛCDM: DM is initially
the dominant non-relativistic component, collapses into halos first, and baryons fall
into the resulting compression wells (gravitational wells in standard language). The
DFC account of this process is qualitatively identical to ΛCDM — the DM halos are
compressed regions of higher-depth kink density that attract further baryonic closures
through the common D3–D4 gradient field.

No new DFC mechanism is needed for structure formation — the existing gravitational
account carries over directly. The open problem is whether the DFC warm dark matter
mass (~35 keV) correctly reproduces the observed power spectrum, which requires a full
Boltzmann code with DFC-specific free-streaming length.

---

## Formal Equations

### Depth-to-Mass Relation (DFC Dark Matter)

```
m_DM(d) = m_e × exp[κ(d − d_e)]       [depth-to-mass scaling]

  d_DM ≈ 4.5  (between D4 inertia onset and D5 U(1) closure)
  κ    ≈ 5.33 (from quark mass ladder fits)
  d_e  = 5.0  (electron anchor depth)
  m_e  = 0.511 MeV

→  m_DM ≈ 35 keV
```

### Free-Streaming Length

```
λ_fs ≈ 0.12 Mpc × (m_DM / 1 keV)^{−4/3} × (g*/10.75)^{1/3}   [thermal WDM]

For m_DM = 35 keV:
  λ_fs ≈ 0.12 × 35^{−4/3} ≈ 0.12 / 121 ≈ 1 × 10^{−3} Mpc ≈ 1 kpc

Structures below ~1 kpc are suppressed by free-streaming.
This reduces the number of sub-kpc halos (small satellite galaxies).
```

*(Note: free-streaming formula assumes thermal production — which has overclosure
problem as described above. Non-thermal production changes this calculation.)*

### Kink-Width and Self-Interaction Scale

```
λ_kink = ℏ / (m_DM c) ≈ (197 MeV·fm) / (0.035 MeV) ≈ 5600 fm ≈ 5.6 nm

DM self-interaction cross-section from kink-kink scattering [OPEN]:
  σ ~ λ_kink²  ≈ (5.6 nm)² ≈ 3 × 10^{−16} m² = 3 × 10^{−12} barn

σ/m_DM ≈ 3×10^{−16} m² / (35 keV / c²) ≈ ... [calculation requires kink-kink
   S-matrix from φ⁴ field theory — not yet done]

Bullet Cluster constraint: σ/m < 1 cm²/g ≈ 1.8 × 10^{−28} m²/eV
Status: OPEN (self-interaction cross-section not yet computed from DFC dynamics)
```

### Relic Density (Not Yet Reproduced)

```
Observed: Ω_DM h² = 0.1200

Thermal WDM estimate:
  Ω_WDM h² ≈ (m_DM / 93 eV)  [for fully thermalized light fermion]
  For m = 35 keV: Ω h² ≈ 376  →  overclosure factor ~3000×

Status: DFC does not yet have a production mechanism that gives Ω_DM = 0.265.
The thermal relic estimate is inapplicable without a specific production channel.
```

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| No electric charge | Closure stops before D5 U(1) winding | Q = 0 confirmed | Structural ✓ |
| No color charge | Closure stops before D7 SU(3) winding | No hadronic signal | Structural ✓ |
| Has mass (gravitational) | D4 inertia acquired | Gravitational lensing ✓ | Structural ✓ |
| Mass estimate ~35 keV | Depth model d_DM ≈ 4.5, κ ≈ 5.33 | m_DM not independently measured | Prediction (warm DM range) |
| Lyman-alpha constraint m > 3.5 keV | 35 keV >> 3.5 keV threshold | m > 3.5 keV ✓ | Consistent ✓ |
| Collisionless (Bullet Cluster) | Self-interaction range ~ nm, negligible at kpc+ | σ/m < 1 cm²/g ✓ | Qualitative ✓ |
| Small-scale structure suppression | Free-streaming at ~1 kpc (warm DM) | Missing satellites, core-cusp | Qualitative match |
| Ω_DM = 0.265 | Not derived from DFC parameters | 0.265 ± 0.007 | OPEN ✗ |
| Thermal relic density | Overclosed by ×3000 if thermalized | Ω h² = 0.120 | Problem (production mechanism unknown) |
| No DM signal in XENON/LUX | No EM or strong coupling → no nucleus recoil | No direct detection signal ✓ | Structural ✓ |

---

## Open Questions

1. **Derive the DM abundance Ω_DM = 0.265 from DFC parameters.** The thermal relic
   estimate gives gross overclosure at m = 35 keV. The correct production mechanism
   for DFC DM candidates — non-thermal production via D4-depth compression dynamics
   during phase transitions, Dodelson-Widrow-type oscillation mixing, or another channel
   — must be identified and the resulting relic density computed. This is the most
   critical open problem for the DFC dark matter account.

2. **Compute the DM–nucleus scattering cross-section from DFC dynamics.** The DFC DM
   candidate has no EM or color coupling, so direct detection requires a different
   channel — possibly through D4-depth gradient field exchange (a gravitational
   scattering analog). Estimating this cross-section would predict the direct detection
   rate for experiments like XENON, LUX, and PandaX and identify why no signal has
   been seen.

3. **Compute the kink-kink self-interaction cross-section.** The φ⁴ kink-kink scattering
   in 1+1D is known analytically. The full 3+1D equivalent for DFC intermediate-depth
   kinks requires the S-matrix at D4 depth. This is connected to the broader S-matrix
   bottleneck but is a concrete and tractable sub-problem.

4. **Is d_DM precisely 4.5, or does it have a spread?** The depth model gives a single
   value d_DM ≈ 4.5 by analogy with the electron depth d_e = 5. But the same D4–D5
   depth range might support a continuum or a discrete spectrum of stable intermediate
   closures — analogous to how D7 supports a spectrum of quark masses. A spectrum would
   predict multiple DM species with a mass distribution, changing both the clustering
   properties and the direct detection predictions.

5. **Why does dark matter not reach D5?** The electron reaches D5 and acquires charge.
   What prevents some kinks from reaching D5? The answer requires understanding the
   specific compression field conditions at the D4→D5 transition — whether there is a
   potential barrier, a topological obstruction, or an energetic requirement that some
   kinks do not meet. This connects to the D-depth assignment mechanism bottleneck.

---

## Connections

- **Cosmic expansion / dark energy** — DM drives structure formation; dark energy
  drives late-time acceleration; both are components of the same cosmological budget;
  `phenomena/cosmology/cosmic_expansion.md`
- **Baryogenesis** — why baryons outnumber antibaryons; DM abundance is a separate
  problem from baryon asymmetry; `phenomena/cosmology/baryogenesis.md`
- **General relativity** — gravitational lensing and rotation curves are GR effects;
  `phenomena/gravity/general_relativity.md`
- **Electric charge** — DM has none precisely because it doesn't complete D5 U(1);
  `phenomena/electromagnetism/electric_charge.md`
- **Dimensional stack** — D4 inertia / D5 U(1) boundary is the key depth threshold;
  `foundations/dimensional_stack.md`
- **Mass hierarchy** — depth-to-mass scaling that predicts m_DM ~ 35 keV;
  `foundations/mass_hierarchy.md`
- **Neutrinos** — also sub-D5 structures but with specific winding modes at the D3/D4
  boundary; DM and neutrinos are both "light" closures in different depth regimes;
  `phenomena/particle_physics/particles/neutrinos.md`
- **CMB** — dark matter acoustic oscillation signature; `phenomena/cosmology/cosmic_microwave_background.md`
- **DM equation module** — closure scale vs. rest mass; `equations/dark_matter.py`
  *(Note: the module gives M_c(D4) ~ 3.4×10¹⁴ GeV and M_c(D5) ~ 10¹³ GeV as closure
  energy scales — not rest masses. The rest-mass estimate ~35 keV in this document comes
  from a depth-to-mass exponential extrapolation; the ratio M_c/m_particle is ~10¹⁹ for
  the electron and appears consistent with the DM estimate, but this connection is not yet
  formally derived.)*
