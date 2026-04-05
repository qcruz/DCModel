# Phenomenon: Quantum Tunneling

## One-Sentence Synthesis

> Quantum tunneling is the compression field's evanescent mode — when the local kinetic
> energy in the KG equation changes sign inside a potential barrier, the field solution
> transitions from oscillatory to exponentially decaying rather than vanishing; the nonzero
> amplitude at the far side of the barrier is the transmission amplitude, and the Gamow
> exponent G = ∫√(2m[V−E]) dx/ℏ follows from the analytic continuation k → iκ.

---

## Observation

Quantum particles pass through potential barriers that are energetically inaccessible to
classical particles. The tunneling probability decreases exponentially with barrier width
and height. Key examples:

**Alpha decay:** Uranium-238 emits alpha particles at 4.27 MeV, but the Coulomb barrier
peak is ~30 MeV. The alpha particle has less than 1/7 of the energy needed to classically
escape. Yet alpha decay occurs with a half-life of 4.5 × 10⁹ years — finite, not infinite.

**Stellar fusion:** In the solar core (T ≈ 1.5 × 10⁷ K, kT ≈ 1.3 keV), the typical proton
kinetic energy is ~1 keV. The Coulomb barrier between two protons peaks at ~550 keV — 400
times higher. Without tunneling, stars cannot burn. All stellar energy production in the universe
depends on tunneling through the Coulomb barrier.

**Tunnel diodes / scanning tunneling microscopy:** Electrons tunnel through nanometer-scale
vacuum gaps. The current falls off as e^{−2κd} where d is the gap width, reaching ~1 order
of magnitude per Å — so precise that STM can resolve individual atoms by measuring current as
the tip scans at fixed height.

**Proton transfer in chemistry:** Enzymatic reactions involving proton transfer are significantly
accelerated by proton tunneling at room temperature, affecting enzyme catalysis rates by
factors of 10–100.

In all cases: the tunneling probability is T ∝ exp(−2G), where G = ∫√(2m[V(x)−E])/ℏ dx
integrated over the classically forbidden region.

---

## Standard Explanation

The Schrödinger equation (in the time-independent form) for a particle with total energy E
moving in potential V(x):

```
−(ℏ²/2m) d²ψ/dx² + V(x)ψ = Eψ

→   d²ψ/dx² = −k²(x) ψ    where  k²(x) = 2m(E − V(x))/ℏ²
```

**Classically allowed region** (E > V): k²(x) > 0, k real → oscillatory solutions ψ ∝ e^{±ikx}.

**Classically forbidden region** (E < V): k²(x) < 0, k → iκ where κ = √(2m(V−E))/ℏ > 0
→ evanescent solutions ψ ∝ e^{±κx}.

The wavefunction does not vanish inside the barrier — it decays exponentially. For a
rectangular barrier of height V₀ > E and width L:

```
T ≈ 16k²κ²/(k²+κ²)² × e^{−2κL}    [exact, rectangular barrier]
T ≈ e^{−2κL}                         [dominant exponential, κL >> 1]

κ = √(2m(V₀−E))/ℏ
```

For a general barrier shape, the WKB approximation generalizes this to:

```
T ≈ exp(−2G)    where G = (1/ℏ) ∫ₓ₁ˣ² √(2m[V(x)−E]) dx
```

The integral runs from the classical turning points x₁ (entry to barrier) to x₂ (exit).

---

## Dimensional Folding Explanation

### The KG Equation Does Not Know About Barriers

In DFC, every particle is a configuration of the compression field ψ. The field dynamics
(massless KG for photons, massive KG for scalar particles, Dirac equation for fermions)
all have the same structure in a potential:

```
∂²ψ/∂t² = c² ∂²ψ/∂x² − ω₀²ψ − (2m V(x)/ℏ²) ψ
```

where ω₀ = mc²/ℏ is the rest frequency and V(x) represents the local potential energy
landscape.

For a stationary state at energy E = ℏω, the spatial equation is:

```
d²ψ/dx² = −[k₀² − 2mV(x)/ℏ²] ψ   where k₀² = (E² − m²c⁴)/(ℏc)²
```

This is a linear ODE. It does not know about classical forbidden regions. It has no mechanism
to enforce ψ = 0 beyond a certain point. The field simply continues — its spatial behavior
changes depending on the sign of the coefficient, but the field does not terminate.

**When the coefficient is negative** (E > V, classically allowed):
the coefficient is negative → oscillatory solution → the compression field oscillates.

**When the coefficient is positive** (E < V, classically forbidden):
the coefficient is positive → real exponential solution → the compression field decays.

The transition between these two behaviors is continuous and smooth — no wall, no collapse,
just the field following its own equation of motion through a changing potential landscape.

The tunneling transmission amplitude is the compression field amplitude at x₂ (the far side
of the barrier) relative to the amplitude at x₁ (the near side). It is not the particle
"going through" a barrier — it is the field having nonzero amplitude everywhere, with the
amplitude reduced by the evanescent factor across the barrier.

### What the Particle "Is" During Tunneling

In the DFC picture, the particle is a kink configuration of the field — a topologically stable
structure in the field. The kink's spatial extent is of order the kink width λ = √(2c²/α).
When the kink encounters a barrier:

- The kink's leading edge enters the evanescent region
- The field amplitude in the barrier region falls as e^{−κx}
- There is a nonzero probability amplitude for the kink to emerge at the far side

This is not a trajectory — the kink does not travel through the barrier. It is a collective
field reconfiguration in which the probability of the kink being located on the far side is
nonzero. The field is connected across the barrier; the evanescent mode is the continuous
thread.

The measurement question — does the particle "exist" inside the barrier? — has a natural DFC
answer: the field is nonzero there, so in principle a sufficiently precise measurement of the
field configuration inside the barrier would register a nonzero value. But that measurement
would itself perturb the field and collapse the evanescent amplitude. The barrier traversal
time (the time for which the particle is "inside") is therefore an ill-defined quantity, which
is consistent with the experimental difficulty of measuring it (the attosecond tunneling time
debate remains open in standard QM).

### The WKB Exponent from the KG Equation

For a slowly varying potential V(x), the WKB approximation to the evanescent solution is:

```
ψ(x) ≈ C × [κ(x)]^{−1/2} × exp(−∫ κ(x') dx')

κ(x) = √(2m[V(x)−E]) / ℏ
```

The Gamow exponent G = ∫κ(x)dx is the integral of the evanescent decay rate over the
classically forbidden region. The factor [κ(x)]^{−1/2} is the WKB prefactor from current
conservation.

This is a standard result of the Schrödinger/KG equation. In DFC, it follows directly from
the field equation with no additional assumptions. The exponential dominates:

```
T ≈ exp(−2G)    [WKB transmission, exact in slowly-varying limit]
```

---

## Formal Equations

### Rectangular Barrier

```
Transmission coefficient T:

  T = [1 + (k² + κ²)² sinh²(κL) / (4k²κ²)]^{−1}

  k = √(2mE)/ℏ          (wavenumber in free region)
  κ = √(2m(V₀−E))/ℏ     (decay rate in barrier)
  L = barrier width

Opaque barrier limit (κL >> 1):

  T ≈ (16k²κ²/(k²+κ²)²) × e^{−2κL}
```

### WKB Tunneling Factor (General Barrier)

```
G = (1/ℏ) ∫_{x₁}^{x₂} √(2m[V(x)−E]) dx

T ≈ A × exp(−2G)     [A = prefactor of order 1]
```

### Alpha Decay Gamow Factor

```
G = (π Z_d Z_α α_EM / v_α) − correction terms

v_α = √(2 E_α / m_α)       [alpha velocity at infinity]
Z_d = daughter nucleus charge
Z_α = 2 (alpha charge)
α_EM = e²/ℏc ≈ 1/137

Half-life:  T½ = (ln 2) × (πR/v_α) × exp(+2G)
```

Identical to the Gamow factor in `phenomena/particle_physics/radioactive_decay.md`. The
DFC account gives the same result as the standard QM calculation — confirming that the
compression field equation reproduces WKB tunneling without modification.

### Gamow Peak for Stellar Fusion

The rate of a nuclear reaction in a stellar plasma depends on the product of:
- The Maxwell-Boltzmann velocity distribution: ∝ exp(−E/kT)
- The tunneling factor: ∝ exp(−bE^{−1/2}) where b = π Z₁Z₂ α_EM √(2m) / ℏ

The product peaks at the Gamow peak energy:

```
E_0 = (b kT / 2)^{2/3}

For p + p fusion in the solar core (T = 1.5 × 10⁷ K, kT = 1.29 keV):
  b ≈ 0.97 MeV^{1/2}
  E_0 ≈ 5.9 keV   (vs classical barrier peak ~550 keV)

Fusion rate ∝ exp(−3E_0/kT) ≈ exp(−13.7) ≈ 10^{−6}  [strongly suppressed but nonzero]
```

The sun burns slowly precisely because this suppression factor is ~10⁻⁶ — the sun is not
a bomb. The solar luminosity is set by the depth of this tunneling suppression.

---

## Consistency Checks

| Process | DFC mechanism | Status |
|---|---|---|
| Alpha decay Gamow factor | WKB tunneling through D5 Coulomb barrier | ✓ (verified in radioactive_decay.md) |
| T ∝ exp(−2κL) scaling | Evanescent KG solution in forbidden region | ✓ (standard result, no modification) |
| STM exponential distance dependence | Same evanescent mode, vacuum barrier | ✓ |
| Gamow peak for stellar fusion | Maxwell-Boltzmann × tunneling factor product | ✓ (derived from KG equation) |
| No modification to standard results | DFC field equation = Schrödinger in NR limit | ✓ |

DFC adds no new content to the tunneling calculation beyond identifying the particle as the
compression field configuration. The WKB result is exact in the slowly-varying limit, and the
KG equation in the non-relativistic limit is the Schrödinger equation.

---

## Open Questions

1. **Tunneling time.** Measured tunneling times in attosecond experiments appear to be
   consistent with near-instantaneous traversal, but the interpretation is controversial
   (Hartman effect, Büttiker-Landauer time). In DFC: the kink configuration is never
   localized inside the barrier — there is no well-defined "traversal trajectory." The
   tunneling time should be computed from the compression field correlation function across
   the barrier, not from a particle trajectory. Whether DFC predicts a specific tunneling
   time is open.

2. **Barrier penetration in the nonlinear regime.** The WKB result applies to the linearized
   KG equation. The full DFC compression field has a nonlinear potential V(φ) = −α/2 φ² +
   β/4 φ⁴. For barriers comparable to the kink energy scale, the nonlinear terms affect the
   evanescent solution. Whether the nonlinear tunneling rate differs measurably from the
   linearized WKB result has not been computed.

3. **Resonant tunneling.** Quantum wells between two barriers support resonant transmission
   (T = 1) at specific energies. In DFC, this corresponds to the evanescent mode picking up
   a resonant constructive interference between the two barriers. The condition is the same
   as in standard QM (bound state energy of the well matches transmission resonance). No new
   DFC content is expected, but explicit verification from the field equation has not been done.

4. **Macroscopic quantum tunneling.** Josephson junctions and SQUIDs exhibit macroscopic
   quantum tunneling of a macroscopic variable (the superconducting phase). In DFC, this
   would be collective tunneling of a D6 SU(2) condensate configuration. Whether DFC can
   account for macroscopic quantum coherence is connected to the unresolved Born rule problem.

---

## Connections

- **Radioactive decay** — alpha decay as the primary application of the Gamow formula;
  `phenomena/particle_physics/radioactive_decay.md`
- **Nuclear binding** — stellar fusion requires tunneling through the Coulomb barrier;
  `phenomena/particle_physics/nuclear_binding.md`
- **Quantum mechanics** — KG/Schrödinger equation in classically forbidden regions;
  `phenomena/quantum/quantum_mechanics.md`
- **Strong force** — the D7 nuclear potential that forms the inner part of the alpha decay
  barrier; `phenomena/particle_physics/forces/strong_force.md`
- **Electromagnetism** — the D5 Coulomb barrier that must be tunneled through;
  `phenomena/electromagnetism/electromagnetism.md`
- **Measurement** — whether the compression field has a definite value inside the barrier;
  `foundations/measurement.md`
