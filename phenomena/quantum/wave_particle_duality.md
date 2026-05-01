# Phenomenon: Wave-Particle Duality

## One-Sentence Synthesis

> Wave-particle duality is dissolved in DFC: the compression field always has wave
> properties (phase, superposition, interference, diffraction), and localized kinks in
> that field always have particle properties (definite position, discrete energy, momentum);
> the apparent paradox disappears because these are not two aspects of one object but two
> regimes of the same field — the wave regime (sub-threshold amplitude) and the kink regime
> (amplitude past the buckling threshold).

---

## Observation

Every quantum object exhibits both wave and particle behavior, depending on how it is
interrogated:

**Wave behavior observed:**
- Electrons, photons, neutrons, and even C₆₀ molecules produce interference fringes in
  double-slit experiments
- Diffraction from crystal lattices (Davisson-Germer 1927 for electrons, Bragg for X-rays)
- Phase shifts in neutron interferometers sensitive to Earth's rotation
- The de Broglie relation λ = h/p connects a wave property (wavelength) to a particle
  property (momentum) for every object ever tested

**Particle behavior observed:**
- Each detection event is a point on the screen — not a smeared arrival
- Photon counters click once per photon — energy arrives in discrete lumps E = hν
- Compton scattering: photon imparts definite momentum to a single electron
- The interference pattern builds up one dot at a time

**The paradox:** How can the same object be both extended (to produce interference) and
localized (to land at a point)?

---

## Standard Explanation

In quantum mechanics, each particle is described by a wavefunction ψ(x,t) — a complex-valued
field that propagates and interferes. The probability of detecting the particle at x is |ψ(x)|².
Detection causes "wavefunction collapse": the extended field instantaneously localizes.

The de Broglie relation λ = h/p is a postulate connecting wave and particle properties.
The Born rule |ψ|² → probability is a separate postulate.

What standard QM does not explain:
- Why quantum objects have wavefunctions (it is assumed)
- What physical process constitutes "collapse"
- Where |ψ|² comes from (the Born rule is postulated, not derived)
- Why there is one object with two seemingly contradictory descriptions

---

## Dimensional Folding Explanation

### The Dissolution of the Paradox

There is no paradox in DFC because there are not two contradictory aspects of one object.
There are two distinct regimes of one field:

**Regime 1 — Extended wave:** The compression field φ(x,t) below the buckling threshold
amplitude φ₀ = √(α/β). In this regime the field satisfies the linear wave equation
(KG equation):

```
□φ = 0       [massless: photon]
□φ = m²c²φ/ℏ²   [massive: particle]
```

The field has phase, superposition, and interference. It propagates as an extended entity
through all available paths simultaneously. This is what is often called "the wave."

**Regime 2 — Localized kink:** When the field amplitude reaches φ₀ at some point in the
substrate, the potential V(φ) = −α/2 φ² + β/4 φ⁴ causes buckling — the field locks into
a topological kink solution:

```
φ_kink(x) = φ₀ tanh((x − x₀)/λ)     λ = √(2c²/α) ≈ L_Planck
```

This kink is localized, carries definite energy E = (4/3)φ₀² √(αc⁴/2), and can only
exist at one position. This is what is often called "the particle."

**The resolution:** The "wave" and the "particle" are not two descriptions of one object.
They are two phases of the same field. The transition between them — the buckling event —
is what standard QM calls "measurement" or "collapse." It is a real physical threshold
crossing, not a mysterious discontinuity.

### The Photon

A photon is a massless excitation of the D5 gauge field. Between emission and absorption,
the field propagates as a solution of the massless wave equation. It has frequency ν,
wavelength λ = c/ν, and phase. It interferes with itself through both slits.

When the photon reaches an absorbing atom — a stable kink configuration — the field
amplitude at that location rises above the local buckling threshold. The energy is
absorbed in a single interaction: one photon → one excited atom. The "click" is the
buckling event.

The energy of a photon mode with angular frequency ω is proportional to ω, with the
constant of proportionality being the quantum of action ℏ (Planck's constant divided
by 2π). This identification E = ℏω is a postulate imported from quantum field theory,
not derivable from the dispersion relation ω = ck alone — the dispersion relation
only determines the speed of propagation. Since ω = 2πν, this is the same statement
as E = hν (h = 2πℏ, ν = ω/2π). See `phenomena/light/light.md` for the full audit
(Cycle 42 correction).

The photon does not "choose" to be a wave or a particle at any point. It is always
the field. What changes is whether the field amplitude locally exceeds the kink threshold.

### The Electron (and All Massive Particles)

A massive particle (electron, neutron, molecule) is a stable kink in the compression
field. But the kink itself has an associated field — the Compton wavelength oscillation
of the kink's phase. This phase field propagates as a wave:

```
φ_phase(x,t) ∝ exp(i(p·x/ℏ − Et/ℏ))
```

with wavelength λ = h/p (de Broglie relation — derived from KG, not postulated).

When the electron passes through a double slit, it is the phase field of the kink that
propagates through both slits. The kink itself must travel through one slit. But which
slit is determined by the outcome of the kink-field interaction at the screen. In the
absence of which-path detection, the phase field through both slits is coherent and
interferes constructively/destructively, biasing where the kink re-localizes.

The interference pattern is the probability distribution for re-localization events —
but it is set by the physical field, not by abstract probability waves.

### The de Broglie Relation as a Derived Result

The de Broglie relation λ = h/p follows from the KG dispersion relation:

```
Klein-Gordon dispersion:
    −ω² + c²k² = −(mc²/ℏ)²
    E = ℏω,   p = ℏk

→  λ = 2π/k = h/p                  [de Broglie relation] ✓
→  E² = p²c² + (mc²)²              [energy-momentum relation] ✓
```

No additional postulate is needed. The wave property (wavelength λ) is built into the
compression field's KG equation, and the particle property (momentum p) emerges from
the kink's motion. The de Broglie relation is the statement that both descriptions are
limits of the same underlying field equation.

### The Buckling Threshold and the Born Rule

**Why detections are point-like:** The kink is spatially localized to width λ_kink ≈ L_Planck.
When the field localizes, it does so at a single substrate location — the buckling event
is a phase transition at one point, not a smeared process. This produces the point-like
detection.

**The Born rule (partial account):** The probability of detecting at location x is
proportional to the local field intensity |φ(x)|². This is because:
1. The buckling probability at x is proportional to how close the local field amplitude
   is to the threshold φ₀
2. For a linear field, the amplitude envelope is |φ(x)|
3. The probability of threshold-crossing goes as the square of the amplitude: P ∝ |φ|²

This is the physical origin of the Born rule — it is the threshold-crossing probability
for a real field, not a separate axiom. A full derivation remains an open question (see
`phenomena/quantum/quantum_mechanics.md`), but the physical mechanism is clear.

---

## Formal Equations

### The Two Regimes of the Compression Field

```
Wave regime (|φ| ≪ φ₀):
    □φ + m²c²φ/ℏ² = 0    [Klein-Gordon, linearized]

    Solutions: φ = A exp(i(k·x − ωt)) + c.c.
    Dispersion: ω² = c²k² + (mc/ℏ)²

Kink regime (|φ| → φ₀):
    φ_kink(x) = φ₀ tanh((x − x₀)/λ)    λ = √(2c²/α)

    Energy: E_kink = (4/3)c²φ₀²/λ = (4c²/3)√(α/2) (α/β)   [BPS-correct, Cycle 48]
```

### de Broglie from KG

```
p = ℏk    →    λ = h/(ℏk) = h/p    ✓
E = ℏω    →    E = hν               ✓

Both photons and massive particles satisfy the same relation because
both are solutions of the same compression field equation.
```

### Fringe Visibility and Coherence

For a double-slit experiment with slit separation d, screen distance L:

```
Fringe spacing:     Δy = λL/d = hL/(pd)
Visibility:         V = (I_max − I_min)/(I_max + I_min)
                    V = 1  (full coherence, no which-path)
                    V → 0  (which-path detector coupled)
```

In DFC: V = 1 when no boundary condition distinguishes the two slits. V → 0 when
a local constraint at one slit prevents coherent cross-channel redistribution.

---

## Consistency Checks

| Property | DFC mechanism | Verified |
|---|---|---|
| de Broglie λ = h/p | KG dispersion: p = ℏk (given E=ℏω postulate) | Structurally consistent ✓ |
| E = hν for photons | E = ℏω is a postulate (quantum of action); E=hν is the same relation | Consistent — not independently derived ✓ |
| Interference pattern shape | Stationary BVP of wave equation | λL/d fringe spacing ✓ |
| Point-like detection | Kink localization width λ_kink ~ L_Planck | Structural ✓ |
| Which-path destroys fringes | New boundary condition prevents cross-channel | Mechanical ✓ |
| Born rule |φ|² → probability | Threshold-crossing probability of real field | Partial ✓ |
| Large-molecule interference | KG equation holds for all mass scales | Qualitative ✓ |

---

## Open Questions

1. **Rigorous derivation of the Born rule.** The argument above (buckling probability ∝ |φ|²)
   gives the correct scaling but is not a proof. **Partial result (Cycle 38):** The spin Born
   rule P(↑, n̂) = cos²(θ/2) has been derived from SU(2) spinor geometry + binary nucleation
   (zero free parameters) — see `foundations/born_rule_derivation.md`. The position Born rule
   (buckling event rate Γ(x) ∝ |φ(x)|² from Kramers escape dynamics) remains open. A rigorous
   derivation would compute the threshold-crossing rate from the nonlinear field dynamics and
   show it equals |φ|² exactly, including normalization.

2. **Kink re-localization dynamics.** When an electron passes through a double slit, the
   kink's phase field propagates coherently through both slits. The re-localization at the
   screen requires the kink to form at one specific location. The dynamics of how the phase
   field's interference pattern biases the kink formation location — the "measurement"
   process in DFC terms — is not yet formally derived.

3. **Many-particle coherence.** The C₆₀ interference experiments show coherence for objects
   with ~720 atoms. In DFC, a C₆₀ molecule is a composite kink structure. The coherence
   of its center-of-mass motion follows from the KG equation applied to the composite.
   At what scale does internal decoherence of the composite's kink degrees of freedom
   suppress the external coherence? This is the DFC version of the quantum-to-classical
   transition.

4. **Weak measurement and which-path partial information.** Partial which-path information
   reduces fringe visibility by a factor related to the distinguishability of the slit
   states. In DFC, this corresponds to a partial boundary condition at one slit — the
   field is partially, not fully, constrained. Deriving the visibility reduction from
   the degree of constraint is an open formal problem.

---

## Connections

- **Interference** — double-slit geometry, de Broglie derivation, fringe spacing;
  `phenomena/quantum/interference.md`
- **Quantum mechanics** — kink/wave relationship, the wave equation as the compression
  field equation; `phenomena/quantum/quantum_mechanics.md`
- **Quantum tunneling** — the wave regime allows penetration of classically forbidden
  regions as evanescent modes; `phenomena/quantum/quantum_tunneling.md`
- **Measurement** — kink nucleation as the measurement event; `foundations/measurement.md`
- **Light** — photon as massless compression wave with E = hν; `phenomena/light/light.md`
- **Spin** — Jackiw-Rebbi zero mode — the localized kink that is the electron;
  `phenomena/quantum/spin.md`
- **Born rule (spin)** — P(↑,n̂)=cos²(θ/2) DERIVED from SU(2) geometry + binary nucleation
  (Cycle 38); `foundations/born_rule_derivation.md`
- **Decoherence** — large-molecule coherence suppression; `phenomena/quantum/decoherence.md`
- **Special relativity** — de Broglie verified via KG dispersion; `equations/special_relativity.py` (Cycle 78)
