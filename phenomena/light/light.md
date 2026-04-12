# Phenomenon: Light

## One-Sentence Synthesis

> Light is the massless limit of the compression field — a D2 propagation mode that
> carries no D4 inertial anchor, travels at c because c is the natural propagation
> speed of the compression field itself; the Planck relation E = hν has the right form
> from the massless dispersion ω = ck combined with the quantum of action ℏ, but the
> value of ℏ and the identification E = ℏω require a derivation not yet completed in
> DFC (see Open Question 1 and `foundations/planck_constant_derivation.md`).

---

## Observation

Light propagates through empty space at a constant speed regardless of the motion of its
source or observer. It carries energy and information across cosmological distances. It
bends around massive objects. It redshifts as it climbs out of gravitational wells. It
is emitted and absorbed in discrete quanta whose energy is proportional to frequency.
Near extreme mass concentrations, it cannot escape. Nothing with mass can travel as fast.

---

## Standard Explanation

In the Standard Model, light consists of photons — massless spin-1 gauge bosons mediating
the electromagnetic force. Photons propagate at c through the electromagnetic field.
Their energy is E = hν (frequency times Planck's constant). Emission and absorption are
mediated by interactions between the electromagnetic field and charged matter. Photons
carry no rest mass, which is why they propagate at the universal speed limit.

GR adds that photons follow null geodesics through curved spacetime — their paths bent by
mass not because a force acts on them, but because the geometry of the effective metric
curves.

What standard physics does not explain: why c is the speed limit, why mass is zero, why
energy is proportional to frequency, or what the physical content of the photon's complex
wave function is.

---

## Dimensional Folding Explanation

### Abstract Level

**Light is the compression field in the regime before any closure topology forms.**

Every massive particle is a stable compression fold that has reached at least depth D4 —
the threshold of inertial anchoring. The fold oscillates at its Compton frequency
ω_C = m c²/ℏ, and at low energies its slow envelope satisfies the Schrödinger equation
(see `phenomena/quantum/quantum_mechanics.md`).

A photon is what happens when the mass goes to zero: m → 0, ω_C → 0, and the
distinction between "fast carrier" and "slow envelope" disappears entirely. What remains
is a pure compression wave with no stable minimum to oscillate around — the field simply
propagates. Its dispersion is linear: ω = ck. Its speed is c, the propagation speed of
the compression field itself.

**c is not a speed limit imposed on motion. It is the natural propagation rate of the
compression field substrate.** Massive structures are anchored into depth layers (D4+)
that resist the field's natural propagation rate. Getting matter to move fast requires
pushing its inertial anchoring — the deeper the anchoring, the more energy required.
The speed limit c is the speed at which the unanchored field moves, and nothing with
depth can match it.

**E = hν has the right form from the massless dispersion.** For a massless field,
ω = ck → E = pc (from the KG dispersion relation). Combined with the quantum of action
(E = ℏω, p = ℏk), this gives E = hν. The dispersion relation ω = ck is structural
(derived from the KG equation). The identification E = ℏω is the additional step —
it requires showing that the compression field's minimum excitation energy is ℏω.
This step is not yet derived from the DFC substrate; it is currently imported from
canonical quantum field theory (see Open Question 1).

**Polarization is fold orientation.** The compression wave propagating along z has two
transverse degrees of freedom — the fold can be oriented at any angle θ in the x-y plane.
This is exactly the fold orientation angle identified as the quantum phase (see
`equations/quantum_emergence.py`). Horizontal and vertical polarization are
θ = 0 and θ = π/2. Circular polarization is θ(t) rotating at the photon frequency —
the fold orientation precesses continuously, and the wave function is ψ = A e^{±iθ}.
The two helicity states (left- and right-circular) are the two signs of this precession.

---

### Perspective 1: From the Observer in D3

From within the D3 localization layer, light appears as a self-propagating electromagnetic
wave or a massless particle traveling at c in all inertial frames. It passes through
vacuum, bends around masses, and loses energy climbing out of gravitational wells.

The constancy of c appears as a fundamental postulate — built into Special Relativity.

### Perspective 2: From the Compression Field

Light is a near-D2 mode propagating along the boundary between the D2 propagation layer
and the D3 localization layer. It does not anchor into D3 the way massive structures do.
It rides the D2↔D3 interface.

The invariance of c is not a postulate. It is a structural fact: c is the fixed
propagation speed of the compression field equation ∂²φ/∂t² = c²∇²φ. Massive objects
move relative to light because matter is more deeply anchored in the dimensional stack
(D4 inertia, D3 localization) and therefore moves through the D2 propagation regime
at reduced effective speed. Light does not move through space at a speed — it defines
the rate at which the unanchored compression field propagates.

---

## Formal Derivation

### The Photon as the Massless Compression Wave

The compression field equation:
```
∂²φ/∂t² = c²∇²φ − V'(φ)
```

For a photon, V'(φ) = 0 — there is no buckling potential. The field has not reached
the depth threshold (D4+) where the double-well potential stabilizes. The equation
reduces to:
```
∂²φ/∂t² = c²∇²φ     [massless wave equation]
```

Plane wave solutions: φ(x,t) = A e^{i(kx − ωt)} require:
```
ω² = c²k²    →    ω = ck    [linear (massless) dispersion] ✓
```

For comparison, a massive particle satisfies ω² = c²k² + m_eff² (KG dispersion),
with m_eff = ℏ√(2α)/c² from the potential curvature.

### E = hν from Massless Dispersion

The massless KG dispersion relation gives:
```
ω = ck   →   E = pc       [massless: energy = momentum × c]
```

Combined with the de Broglie-Planck relations (currently imported from QFT, not
derived from DFC substrate):
```
E = ℏω    [POSTULATE — quantum of action; not yet derived from DFC; see Open Q.1]
p = ℏk    [POSTULATE — de Broglie relation; same status]
```

Then: E = ℏω = ℏck = hcλ⁻¹ = hν.

**What is derived from DFC:** The form ω = ck (massless linear dispersion, from
the substrate wave equation with no potential). The existence of exactly two
transverse polarization states (from the D2 closure topology). The speed c as a
structural constant.

**What is imported (not yet derived):** The identification E = ℏω — that the
minimum excitation energy of the massless mode is one quantum of action ℏ per
cycle. Deriving this from DFC substrate requires showing that the compression field
admits excitations only in units of ℏω, which is the core of the Planck constant
hierarchy problem (`foundations/planck_constant_derivation.md`).

Note: E = ℏω and E = hν (since h = 2πℏ, ω = 2πν) are the **same relation** —
the derivation of one from the other is trivially circular. Both require ℏ.

### c as the Compression Field Propagation Speed

The compression field equation ∂²φ/∂t² = c²∇²φ has c as a structural parameter —
it is the ratio of the field's restoring force (the ∇²φ term) to its inertia
(the ∂²/∂t² term). In the Planck-scale calibration (see `equations/folding_gradient.py`):
```
c² = α / (2/L_Pl²) = α L_Pl² / 2
```

where α = 2c²/L_Pl² is the Planck-scale compression parameter. c is self-consistently
defined as the propagation speed of the same field whose Planck-scale kink width sets
L_Pl. This is consistent, not circular: c is fixed by the field parameters, and L_Pl
is derived from c and G together.

**Why nothing massive can reach c:**

A massive structure has depth d ≥ 4, anchored via the buckling potential with m_eff > 0.
Its energy-momentum satisfies E² = (pc)² + (m_eff c²)². To reach speed v → c requires
E → ∞ (for any m_eff > 0). Physically: accelerating mass pushes more compression into
its depth anchoring, which requires more energy, which adds more effective mass — a
self-reinforcing resistance that asymptotes at c. Light avoids this entirely because
it has no depth anchoring to push against.

### Polarization from Fold Orientation

A photon propagating along z has a compression wave amplitude in the transverse (x,y)
plane. The fold orientation angle θ ∈ [0, 2π) in that plane gives the polarization state:

```
ψ_photon = A e^{iθ}     [complex amplitude = fold orientation]
```

| θ | Polarization state |
|---|---|
| θ = 0 | Linear horizontal (x-axis) |
| θ = π/2 | Linear vertical (y-axis) |
| θ = π/4 | Linear at 45° |
| θ(t) = +ωt | Left circular (fold precesses counterclockwise) |
| θ(t) = −ωt | Right circular (fold precesses clockwise) |

The two helicity states (±1) are the two directions of precession of the fold
orientation around the propagation axis. This is the DFC identification of photon
spin: a spin-1 massless particle has one unit of fold orientation angular momentum
along its propagation direction.

The orthogonality of polarization states:
```
⟨ψ_H | ψ_V⟩ = ∫ e^{iθ_H} (e^{iθ_V})* dθ = 0    (for θ_H ≠ θ_V ± nπ)
```

follows from the fold orientations being geometrically orthogonal.

### Gravitational Redshift as Compression Rate Change

When a photon travels from a region of stronger compression gradient (near a mass) to
weaker (far from it), it crosses regions with different rates of dimensional volume
removal. The photon frequency is set by the local propagation conditions:
```
ν_observed = ν_emitted × √(1 − 2GM/rc²)    [gravitational redshift, GR result]
```

In DFC: as the photon climbs out of the compression gradient, the local c² (the
effective propagation speed in the modified background) changes. The frequency drops
because the photon's ω = ck must adjust to the local field conditions — same k,
reduced effective c → reduced ω → redshift. The energy loss goes into work done
against the compression gradient. ✓

---

## What This Explains

| Phenomenon | DFC explanation |
|---|---|
| Constancy of c | c is the compression field propagation speed, not a velocity |
| Masslessness | No D4 anchor — no buckling potential, no stable minimum |
| E = hν | ω = ck from KG (✓ derived) + E = ℏω (POSTULATE — ℏ not yet derived from DFC) |
| Gravitational bending | D2 mode follows the local compression gradient geometry |
| Gravitational redshift | Effective propagation conditions change with gradient depth |
| Discrete emission/absorption | Reconfiguration is threshold-driven (buckling character) |
| Thermal radiation | Distributed low-frequency shedding under compression pressure |
| Photon capture by black holes | Compression rate exceeds c — D2 mode cannot propagate outward |
| Speed limit for massive objects | Depth anchoring (D4+) resists the unanchored propagation rate |
| Two polarization states | Two transverse fold orientation degrees of freedom |
| Helicity ±1 | Left/right precession of fold orientation around propagation axis |

---

## Analogy: Wave on a Membrane

The compression field is like a taut membrane. Massive particles are stable knots
(topological features) tied into the membrane — they have structure that resists being
moved. Light is a propagating ripple on the same membrane — no knot, just a wave.

The speed of the ripple is set by the tension and density of the membrane — these are
c and the Planck-scale parameters (α, β). The knots cannot move through the membrane
faster than the ripple speed, because they are made of the same material as the ripple;
getting them to move requires deforming the membrane around them, which takes energy
proportional to how tightly they are knotted.

**Where the analogy breaks down:** A real membrane exists in a pre-existing room and
has edges. The compression field does not exist in anything — it is the substrate.
Also, the membrane analogy suggests light and matter are different kinds of objects on
the same substrate, when the DFC model says they are the same object (the compression
field) in different regimes (massless propagation vs. stable fold with potential).

---

## Connections to Other Phenomena

- **Quantum mechanics** — the Schrödinger equation for photons follows the same NR
  reduction of KG, but the m→0 limit is the relativistic regime; photon polarization =
  fold orientation θ = quantum phase; `phenomena/quantum/quantum_mechanics.md`
- **Interference** — the double-slit pattern follows from the massless KG wave equation
  under boundary conditions; fringe spacing λ = h/p = hc/E; `phenomena/quantum/interference.md`
- **General relativity** — gravitational lensing and redshift are consequences of the
  compression gradient modifying the local effective c²; `phenomena/gravity/general_relativity.md`
- **Thermodynamics** — thermal radiation (blackbody spectrum) is the statistical
  distribution of massless compression wave excitations; Planck distribution from
  equipartition over massless modes; `phenomena/thermodynamics/thermodynamics.md`
- **Electromagnetism** — the photon is the gauge boson of the U(1) closure at D5;
  the fold orientation angle θ is the U(1) phase; `foundations/product_geometry.md`
- **Quantum emergence** — fold orientation as complex phase; massless dispersion;
  `equations/quantum_emergence.py`

---

## Open Questions

1. **Derive E = hν without complex amplitudes:** The derivation above uses ℏω from
   canonical quantization of the KG field. A fully DFC-native derivation would show
   that the compression wave's energy comes in units of ℏω directly from the fold
   action integral — without importing the quantum postulate E = ℏω from outside.

2. **Photon spin from D2 topology:** The two helicity states of the photon (spin ±1)
   are here identified with the two precession directions of the fold orientation. A
   rigorous derivation requires showing that the D2 closure mode has exactly two
   transverse degrees of freedom and that they transform as a spin-1 representation
   under rotations of the D3 localization layer.

3. **Null geodesic from compression gradient:** GR predicts that photons follow null
   geodesics in curved spacetime. In DFC, this should follow from the compression
   field equation for massless modes in a background compression gradient. The specific
   derivation — showing that the massless KG equation in a curved background reduces to
   the null geodesic equation — is a key open derivation connecting DFC to GR's photon
   sector.

4. **Blackbody spectrum from compression field statistics:** Planck's distribution
   n(ν) = 1/(e^{hν/kT} − 1) should follow from the Bose-Einstein statistics of
   massless compression wave quanta in thermal equilibrium. This requires identifying
   the statistical mechanics of the D2 mode spectrum — which is open but expected to
   reproduce the standard result since the massless KG quantization gives bosons.

5. **Why exactly two transverse polarization states:** Gauge invariance (in the U(1)
   closure interpretation) removes the longitudinal mode, leaving exactly two physical
   polarizations. In DFC, this should follow from the topology of the D2 closure mode —
   the U(1) circle has exactly one angular degree of freedom, giving one transverse
   phase, and the photon's two polarizations correspond to the real and imaginary parts
   of that complex phase.
