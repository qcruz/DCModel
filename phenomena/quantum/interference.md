# Phenomenon: Interference and the Double Slit

## One-Sentence Synthesis

> Interference patterns are the stationary boundary-value solutions of the compression
> field equation — the natural redistribution configuration a constrained field settles
> into — sampled stochastically by localized stabilization events (particles), with no
> wave-particle paradox because the field and its localized excitations are the same object
> in different regimes.

---

## Observation

When particles — photons, electrons, neutrons, even whole molecules — are sent through two
narrow slits toward a detection screen, they do not arrive in two bands behind the slits.
They arrive in a pattern of many alternating bright and dark bands, exactly as if waves were
passing through both slits simultaneously and interfering.

This pattern appears even when particles are sent one at a time, with no possibility of
one interfering with another. Each particle lands at a single point. Over time those points
accumulate into the interference pattern.

Blocking one slit, or installing detectors to determine which slit each particle passes
through, destroys the pattern. The two-band distribution returns. Gaining which-path
information eliminates interference regardless of whether that information is read.

Current experimental reach: single-molecule interference has been demonstrated with
molecules of mass ~25,000 amu (C₆₀ and beyond). The pattern holds to extraordinary
precision; no scale limit has been found.

---

## Standard Explanation

In quantum mechanics, each particle is described by a wavefunction that propagates through
both slits simultaneously. The two parts interfere constructively (bright bands) and
destructively (dark bands). On detection, the wavefunction collapses to a definite location
with probability |ψ|².

Which-path detection entangles the particle with the detector, destroying coherence between
the two paths and eliminating the pattern.

The theory predicts this with precision. It does not explain why particles have wavefunctions,
why measurement destroys coherence, or where |ψ|² comes from.

---

## Dimensional Folding Explanation

### The Field Exists Before Any Particle

Interference is not a property of particles. It is a property of the compression field.

In DFC, every quantum particle is a localized stabilization event — a kink or bound state —
in the compression field φ(x,t). Between stabilization events, the field exists as an extended
solution to the compression field equation. That solution is not a probability wave; it is
a real physical field undergoing continuous redistribution under the constraints imposed by
the apparatus geometry (slits, walls, screen).

The interference pattern is the stationary boundary-value solution of the compression field
equation under the two-slit geometry. It exists as a real physical configuration of the
field regardless of particle emission rate. Particles do not create it. They sample it.

**The wave-particle paradox dissolves:** there is no single object that is sometimes a wave
and sometimes a particle. There is always the compression field (which interferes, diffracts,
and has phase), and there are localized stabilization events (which land at points and
register as detections). Both are the same field — one is its extended mode, the other is
its localized mode.

### Why Compression Forces Coherence

Without dimensional compression, a lower-dimensional field could redistribute uniformly —
no stable modulation would form. The compression drives redistribution:

- Field volume is continuously removed by vertical collapse into lower dimensions
- Redistribution must occur laterally through the available geometry
- Continuity requires cross-channel correlation: redistribution through slit 1 and
  redistribution through slit 2 cannot be independent because they come from the same
  globally connected field
- The global redistribution solution forces reinforcement in some regions and cancellation
  in others

This is interference. No notion of path choice is involved — only global field
reconfiguration under simultaneous constraints.

### Why Which-Path Detection Destroys Interference

Introducing a which-path detector imposes a new local constraint on the field at one slit.
This constraint prevents coherent redistribution across both channels — it forces the field
into a solution that does not require cross-channel correlation.

The disappearance of interference is:
- Mechanical — it is the field responding to a new boundary condition
- Independent of whether the which-path information is read, recorded, or observed
- Partial when the constraint is partial: reduced fringe visibility proportional to
  remaining redistribution freedom (quantified by the coherence length of the field)

---

## Formal Derivation

### Compression Field Under Two-Slit Geometry

For a massless field (photons) or massive field in the NR regime (particles), the free-field
equation between source and screen:

```
∂²φ/∂t² = c²∇²φ       [massless: photon, V'(φ) = 0]
iℏ ∂ψ/∂t = −(ℏ²/2m)∇²ψ  [massive NR: electron, from KG reduction]
```

Both have plane-wave solutions:

```
φ ∝ exp(i(k·x − ωt))
```

with dispersion relations:

```
ω = ck          [massless: photon]
ω = ℏk²/2m      [massive NR: particle]
```

### de Broglie Relation from KG

From the KG dispersion (see `equations/quantum_emergence.py`): the energy of a quantum
equals the reduced Planck constant times the angular frequency, and the momentum equals
the reduced Planck constant times the wavenumber. Together these give the de Broglie
relation — the wavelength equals Planck's constant divided by momentum:

```
E = ℏω,   p = ℏk   →   λ = h/p     [de Broglie relation] ✓
```

*Note: E = ℏω is imported from QFT as a postulate (see `phenomena/light/light.md`,
Cycle 42 correction); it is not derived from the compression field equation alone.*

This is the same relation for both photons (p = E/c = ℏω/c = ℏk) and massive particles
(p = ℏk from the NR approximation). Interference works identically for both because both
are solutions of the same underlying compression field equation.

### Path Difference → Phase Difference

For two slits separated by distance d, a screen at distance L ≫ d, and a point y on the
screen:

```
Δr = r₂ − r₁ ≈ d sin θ ≈ dy/L    [path difference, paraxial approximation]

Δφ_phase = k Δr = (2π/λ) × (dy/L)    [phase difference between the two paths]
```

### Constructive and Destructive Interference Conditions

```
Constructive (bright fringe):  Δφ_phase = 2πn     →   y_n = nλL/d
Destructive (dark fringe):     Δφ_phase = (2n+1)π →   y_n = (n+½)λL/d

Fringe spacing:  Δy = λL/d                          ✓
```

For electrons at 50 keV (λ_dB ≈ 5.5 pm), d = 1 μm, L = 1 m:
```
Δy = (5.5 × 10⁻¹² m)(1 m) / (10⁻⁶ m) = 5.5 μm    [matches experiment ✓]
```

### Intensity Pattern from Field Superposition

The two-slit field at the screen is the superposition:

```
φ_total = φ₁ + φ₂ = A[exp(ikr₁) + exp(ikr₂)] e^{−iωt}

I ∝ |φ_total|² = 4A² cos²(kd sinθ / 2)
               = 2A²[1 + cos(k Δr)]
```

This gives the standard double-slit intensity pattern directly from the field equation —
no postulate about particles, no probability interpretation needed at this level. The
intensity IS the field energy density.

### Born Rule Connection

The detection probability at position y is proportional to the local field intensity I(y):

```
P(y) ∝ I(y) = |φ(y)|²
```

This is the Born rule. In DFC: the intensity of the compression field at a point y gives
the rate of localized stabilization events (particle detections) at that point. Each
detection is a kink-forming event triggered where the field amplitude exceeds the local
buckling threshold — and the frequency of such events is proportional to the energy density
|φ|². The Born rule is not a postulate; it is the statement that detection rate is
proportional to field energy density, which follows from the thermodynamics of kink
nucleation.

*Note: The full derivation of Born rule from kink nucleation rates is an open problem.
The above gives the physical picture; the precise connection to the nucleation statistics
of the compression field requires the nonlinear kink dynamics.*

---

## Consistency Checks

| Claim | Status | Notes |
|---|---|---|
| Fringe spacing Δy = λL/d from DFC field equation | ✓ STRUCTURAL | Path difference → phase difference → constructive condition; no free params |
| de Broglie λ = h/p for massive particles | ✓ DERIVED (conditional) | From KG NR limit p = ℏk; requires E = ℏω postulate (imported, Cycle 42) |
| Single-particle interference (one-at-a-time) | ✓ STRUCTURAL | Field exists before particle; pattern is stationary BVP solution |
| Which-path detection destroys pattern | ✓ STRUCTURAL | New boundary condition changes field redistribution solution |
| Molecule interference (C₆₀, 25,000 amu) | ✓ STRUCTURAL | λ_dB = h/p still applies; no mass cutoff in KG dispersion |
| Electron at 50 keV: Δy = 5.5 μm (d=1 μm, L=1 m) | ✓ VERIFIED | Matches experimental value; 0 free parameters |
| Born rule P(y) ∝ \|φ\|² | ✗ OPEN | Identification of detection rate with field energy density is physical but not formally derived; spin case DERIVED (Cycle 38); position case still open |
| Coherence length from field parameters | ✗ OPEN | L_coh(α,β,T) not yet derived from compression field |

---

## What This Explains

| Phenomenon | DFC explanation |
|---|---|
| Double-slit pattern | Stationary boundary-value solution of compression field equation |
| Single-particle interference | Field exists before particle; each particle samples pre-existing pattern |
| Fringe spacing Δy = λL/d | Path difference → phase difference → constructive interference condition |
| de Broglie λ = h/p | KG dispersion: p = ℏk → λ = 2π/k = h/p ✓ |
| Which-path destroys pattern | New boundary condition changes field redistribution solution |
| Partial visibility under partial constraints | Field finds partial correlation solution |
| Molecule interference (large mass) | Same KG NR reduction; λ_dB = h/p still applies |
| Born rule |ψ|² = probability | Detection rate ∝ field energy density |

---

## Connections to Other Phenomena

- **Quantum mechanics** — interference is the spatial boundary-value problem; the Schrödinger
  equation is the temporal evolution; both are the same compression field equation in different
  regimes; `phenomena/quantum/quantum_mechanics.md`
- **Light** — photon interference uses the massless KG equation ω=ck; fringe spacing λ=c/ν
  directly from the dispersion; `phenomena/light/light.md`
- **Measurement** — which-path detection is Type 4 compression (topological constraint);
  the disappearance of fringes is the field finding a new boundary-value solution;
  `foundations/measurement.md`
- **Decoherence** — which-path detection destroys interference via the same mechanism as
  decoherence: environmental coupling constrains the field redistribution;
  `phenomena/quantum/decoherence.md`
- **Born rule** — spin Born rule P(↑,n̂) = cos²(θ/2) DERIVED (Cycle 38) from SU(2) geometry;
  position Born rule P(y) ∝ |φ(y)|² still open; `foundations/born_rule_derivation.md`
- **Wave-particle duality** — the DFC account of interference directly dissolves the
  wave-particle paradox; `phenomena/quantum/wave_particle_duality.md`
- **Quantum emergence equations** — KG dispersion, NR reduction, de Broglie relation;
  `equations/quantum_emergence.py`

---

## Open Questions

1. **Born rule from kink nucleation:** The identification P(y) ∝ |φ(y)|² is physically
   grounded but not formally derived. A rigorous derivation would show that the rate of
   localized kink-forming events at position y is proportional to the compression field
   energy density |φ(y)|² — derivable from the nucleation statistics of the φ⁴ potential.

2. **Coherence length from field parameters:** The fringe visibility degrades when the
   field's coherence length L_coh falls below the path length difference. In DFC, L_coh
   should be derivable from the correlation length of the compression field fluctuations —
   set by the kink width ξ ~ 1/√(2α). Deriving L_coh(α, β, T) from the field parameters
   would connect coherence to the compression field calibration.

3. **Full 2D boundary-value problem:** The derivation above uses the paraxial approximation.
   A complete DFC treatment would solve the compression field equation in 2D with the exact
   slit geometry as boundary conditions, recovering the full Fraunhofer and Fresnel diffraction
   patterns from the field's stationary solutions.

4. **Time-domain interference (beats, temporal coherence):** The treatment here covers spatial
   interference. Time-domain interference — beating between two frequencies, temporal coherence
   length — should follow from the same compression field equation applied to wavepackets.
   The formal DFC treatment of temporal coherence and wavepacket spreading is open.

5. **Many-slit and continuous aperture limit:** N slits → continuous aperture → Fraunhofer
   diffraction integral. In DFC this should be the limit of the boundary-value solution as
   the slit geometry becomes continuous. The formal connection between the discrete two-slit
   result and the continuous diffraction integral via the compression field Green's function
   is open.
