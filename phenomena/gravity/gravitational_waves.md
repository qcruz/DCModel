# Phenomenon: Gravitational Waves

## One-Sentence Synthesis

> Gravitational waves are propagating perturbations of the compression gradient field —
> ripples in the rate at which the D3 localization layer is being re-tiled — that travel
> at c in the short-wavelength limit because the compression field equation gives the same
> dispersion relation as massless D2 modes.

---

## Observation

Gravitational waves are transverse disturbances that stretch and compress space
perpendicularly to their direction of travel. Key observations:

- GW150914 (LIGO, 2015): first direct detection — two ~30 M_☉ black holes merging at
  ~400 Mpc, strain h ~ 10⁻²¹ at Earth
- GW170817 (LIGO/Virgo + Fermi GBM, 2017): binary neutron star merger; simultaneous
  gamma-ray burst constrains v_gw = c to within 10⁻¹⁵
- Binary pulsars (Hulse-Taylor, PSR B1913+16): orbital energy loss matches GR quadrupole
  formula to 0.3% over 30+ years (Nobel 1993)
- GW polarizations: LIGO/Virgo analyses are consistent with tensor (spin-2) modes (+
  and ×); scalar and vector modes are disfavored
- Gravitational wave background: stochastic signal detected by NANOGrav/PTA in 2023

---

## Standard Explanation

General Relativity: linearized around flat spacetime, the metric perturbation h_μν
satisfies the wave equation in the transverse-traceless (TT) gauge:

```
□h_μν = −(16πG / c⁴) T_μν
```

The two independent tensor polarizations are labeled + and ×. For a system of
accelerating masses, the radiated power is given by the quadrupole formula:

```
P = −(G / 5c⁵) d³Q_ij/dt³ d³Q_ij/dt³
```

where Q_ij is the reduced mass quadrupole moment. The waves travel at c and carry
energy away from the source, causing orbital inspiral.

The spin-2 nature of the graviton — consistent with + and × polarizations — follows
from the fact that the gravitational field in GR is a rank-2 symmetric tensor.

---

## Dimensional Folding Explanation

### Perspective 1: From the observer in spacetime

What the observer measures as a gravitational wave — a slowly varying strain pattern
alternately stretching and compressing perpendicular directions at strain h ~ 10⁻²¹ —
is the large-distance tail of a propagating compression gradient perturbation. When
two massive objects spiral together, the local compression gradient structure — the
folding-rate distribution that spacetime observers interpret as the gravitational field
— reorganizes rapidly. That reorganization propagates outward as a wave in the
compression field.

The strain h encodes how much the effective D3 re-tiling has been locally deformed
by the passing perturbation: space appears stretched along one transverse axis and
compressed along the other because the compression gradient has temporarily modified
the rate at which the D3 layer is being tiled in each direction.

### Perspective 2: From the substrate

The compression field φ oscillates around its stable minimum φ₀ = ±√(α/β).
A gravitational wave is a propagating small oscillation δφ around this minimum.
The linearized field equation gives:

```
∂²(δφ)/∂t² − c² ∇²(δφ) + 2α (δφ) = 0
```

which is the Klein-Gordon equation with mass term √(2α). This produces the dispersion
relation:

```
ω² = c²k² + 2α
```

In the short-wavelength (high-k) limit where k ≫ √(2α)/c:

```
v_group = c²k / ω = c²k / √(c²k² + 2α)  →  c    as k → ∞
```

This is why gravitational waves travel at c: in the long-baseline, high-frequency
regime accessible to LIGO, the mass term is negligible (√(2α) ≪ observed GW
frequencies ~10–1000 Hz requires α ≪ 10⁶ s⁻²), and the propagation speed
asymptotes to c.

The constraint that v_gw = c to 10⁻¹⁵ (GW170817) requires that the effective
graviton mass in the DFC dispersion relation satisfies:

```
m_graviton c² = ℏ √(2α) ≪ H₀ ≈ 10⁻³³ eV
```

This means α at cosmological scales satisfies α ≪ H₀²/c² ≈ 10⁻⁷² s⁻². This
is the same constraint derived from the cosmological expansion sector.

### The Polarization Problem (honest gap)

The DFC compression field φ is a **scalar** field. Small oscillations of a scalar
field produce **scalar (spin-0) waves** — perturbations in the amplitude of φ that
are spherically symmetric around the propagation direction. They do not produce the
transverse-traceless tensor modes (+ and ×) that LIGO observes.

GR's tensor polarizations arise because the metric perturbation h_μν is a rank-2
symmetric tensor — it has spin-2 degrees of freedom that a scalar field φ simply
does not have.

There are two candidate resolutions within DFC:

**Candidate A — Composite tensor structure from D3 geometry:**
The metric g_μν of the D3 localization layer is itself a composite object, built from
the compression gradient ∂_μ φ. A perturbation δφ propagating through the D3 layer
induces a correlated perturbation in the metric:

```
δg_μν ~ ∂_μ(δφ) ∂_ν(δφ) / φ₀²
```

This composite object *is* a rank-2 tensor and *could* carry the + and × modes.
Whether this coupling correctly reproduces the full TT-gauge result is not yet derived.

**Candidate B — The spin-2 structure is inherited from the D3 layer itself:**
The D3 localization behavior — which produces apparent 3D space — may have an
intrinsic orientation structure that carries spin-2 modes independently of the scalar φ.
In this picture, the scalar φ drives the energy redistribution and sets the wave speed,
but the polarization pattern is determined by the D3 geometric structure.

Both candidates require formal derivation. Until resolved, the DFC dispersion relation
(ω² = c²k² + 2α) should be read as giving the propagation speed of the compression
perturbation, not as a complete derivation of gravitational wave polarizations.

---

## Analogy: Sound Waves in a Vibrating Sheet

Imagine a tightly stretched elastic sheet (the D3 localization layer) sitting on a
fluid substrate (the compression field). When two heavy objects placed on the sheet
spiral together and merge, the local distortion of the sheet propagates outward as a
wave — it moves across the sheet at the sheet's tension-governed wave speed. Observers
on the sheet measure this as a pattern that alternately stretches north-south and
east-west as it passes.

- The elastic tension → the compression gradient field's restoring force
- Propagation speed of sheet waves → c (in the high-frequency limit)
- Stretching/compressing the sheet surface → the + and × strain pattern

**Where it breaks down:** The sheet waves are transverse disturbances in a pre-existing
2D manifold. In DFC, the D3 layer is not pre-existing — it is the re-tiling of the
compression field itself. There is no background sheet; the wave *is* the perturbation
of the tiling. The analogy captures the propagation and strain character but not the
emergent nature of the geometry being disturbed.

---

## Formal Equations

### Dispersion Relation (DFC — derived)

```
ω² = c²k² + 2α

v_group = c²k / √(c²k² + 2α)
v_group → c   as k → ∞   [massless limit, consistent with LIGO ✓]
```

### Graviton Mass Bound (from GW170817 — derived constraint)

```
v_gw = c (1 + δ),   |δ| < 10⁻¹⁵
→  m_graviton = ℏ√(2α)/c²  ≪  H₀/c ≈ 10⁻³³ eV
→  α ≪ H₀²/c² ≈ 10⁻⁷² s⁻²   [cosmological constraint on α]
```

### Binary Pulsar Energy Loss (standard — not yet derived from DFC)

```
dE/dt = −(32/5) G⁴/c⁵ × m₁²m₂²(m₁+m₂) / r⁵

Hulse-Taylor observed: 0.997 × GR prediction (0.3% match over 30 years)
```

The quadrupole formula requires the full nonlinear coupling between compression
budget density T₀₀ and the compression gradient field. It is not yet derived from
DFC field dynamics.

### Strain at Earth (standard — not yet derived from DFC)

```
h ~ (4G / c⁴ r) × d²Q/dt²

h ~ 10⁻²¹   for GW150914 at r ≈ 400 Mpc
```

This follows from the quadrupole formula combined with detector geometry.
The DFC derivation of this expression requires the full G_Newton(α, β, c) derivation
as a prerequisite.

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| v_gw = c | KG dispersion: v_group → c as k ≫ √(2α)/c | v_gw = c to 10⁻¹⁵ (GW170817) | Derived (high-k limit) ✓ |
| Graviton mass bound | α ≪ H₀²/c² required by v = c constraint | m_graviton < 10⁻²³ eV (PDG) | Consistent ✓ |
| Hulse-Taylor orbital decay | Quadrupole energy loss — structural description only | 0.997 × GR prediction | OPEN (not derived) |
| + and × tensor polarizations | Scalar φ → scalar modes; tensor modes not shown | Tensor polarizations confirmed by LIGO | OPEN ✗ |
| h ~ 10⁻²¹ at Earth | Requires G_Newton(α, β, c) — not yet derived | h ≈ 10⁻²¹ (GW150914) | OPEN (requires G_Newton) |
| Stochastic GW background | Large-scale compression perturbation background — structural description | NANOGrav 2023 signal detected | OPEN (not computed) |

---

## Connections to Other Phenomena

- `phenomena/gravity/general_relativity.md` — the dispersion relation ω² = c²k² + 2α
  is derived there; the tensor polarization gap is first identified there
- `phenomena/gravity/black_holes.md` — binary black hole mergers are the loudest
  observed GW sources; each merger is an extreme compression-rate reorganization event
- `equations/folding_gradient.py` — implements the GW dispersion relation numerically,
  including the graviton mass constraint and the Planck-scale α value
- `phenomena/cosmology/cosmic_expansion.md` — the same α constraint (α ≪ H₀²/c²)
  that limits the graviton mass also governs the dark energy equation of state prediction
- `phenomena/quantum/spin.md` — the tensor vs scalar polarization question connects
  to how the substrate produces spin-2 excitations; the same FR/Jackiw-Rebbi
  framework that gives spin-1/2 would need to be extended to give spin-2 gravitons

---

## Open Questions

1. **Tensor polarizations from scalar φ:** How do the + and × polarizations emerge
   from a scalar compression field? The leading candidate is the composite metric
   perturbation δg_μν ~ ∂_μ(δφ)∂_ν(δφ)/φ₀². Evaluate whether this composite tensor
   carries the correct spin-2 degrees of freedom by computing its decomposition under
   SO(3) rotations transverse to the propagation direction.

2. **Quadrupole radiation formula from DFC:** The power radiated P = −(G/5c⁵)(d³Q/dt³)²
   requires deriving G_Newton from (α, β, c) first, then showing that the DFC field
   equation produces the same quadrupole coupling. This is a two-step derivation
   following directly from the G_Newton open problem in `general_relativity.md`.

3. **Stochastic gravitational wave background:** NANOGrav's 2023 detection of a stochastic
   GW background at nHz frequencies raises the question: what does DFC predict for the
   background compression perturbation spectrum? This may connect to the primordial
   perturbation spectrum gap identified in `big_bang.md` — both require deriving the
   Harrison-Zel'dovich-equivalent spectrum from compression dynamics.

4. **Extreme mass-ratio inspirals and Planck-scale dynamics:** Near the innermost stable
   orbit of a massive black hole, the compression gradient perturbation enters the
   nonlinear regime. The linearized (KG) dispersion relation breaks down. Whether DFC
   predicts observable deviations from GR waveforms in this regime — detectable by LISA —
   requires the full nonlinear compression field dynamics.
