# Phenomenon: Decoherence

## One-Sentence Synthesis

> Decoherence is the irreversible entanglement of a quantum system's superposition with
> the compression field's environmental degrees of freedom — as the off-diagonal elements
> of the density matrix (the interference terms between superposed states) become
> distributed across an exponentially large number of environmental kink configurations,
> they become unmeasurable in practice, and the system behaves as if it is in a classical
> probability mixture; in DFC, this is the same process as measurement (a buckling threshold
> crossing), but extended to the case where the triggering interaction is with a large
> thermal environment rather than a single apparatus.

---

## Observation

Quantum superpositions are not observed at macroscopic scales. The transition from quantum
to classical behavior is real and occurs rapidly:

- **Electron in a double slit:** Interference fringes visible. Coherence length ~nanometers
  to micrometers depending on temperature and environment.
- **Buckyballs (C₆₀, 1999 Zeilinger group):** 60-atom molecules show interference fringes
  in a vacuum, demonstrating quantum coherence at that scale.
- **Schrödinger-cat states in superconductors:** SQUID circuits in superpositions of
  clockwise/counterclockwise current. Coherence times ~microseconds at mK temperatures,
  collapsing exponentially as temperature rises.
- **Decoherence time scale:** For a macroscopic object (mass m, separation delta-x, in
  thermal environment at temperature T), the decoherence time is approximately Planck's
  constant divided by (m times delta-x squared times k-B times T divided by Planck's constant),
  which for a 1 gram object with 1 nm separation at room temperature is ~10⁻²³ seconds —
  far faster than any measurement.
- **Pointer states:** Decoherence selects "preferred" basis states (pointer states) — those
  that are most robust against environmental entanglement. For position measurements, position
  eigenstates are pointer states. For spin in a magnetic field, the up/down eigenstates are
  pointer states.

---

## Standard Explanation

In standard quantum mechanics, decoherence occurs when a system becomes entangled with its
environment. The reduced density matrix of the system (obtained by tracing out the
environmental degrees of freedom) loses its off-diagonal elements — the coherences — on a
timescale set by the system-environment coupling strength. The system's state transitions
from a pure state (a superposition) to a mixed state (a classical probability distribution
over the pointer basis), effectively suppressing interference.

Decoherence does not solve the measurement problem: it explains why we don't observe
interference at macroscopic scales, but not why individual measurement outcomes are definite
(the Born rule). It eliminates the superposition from the accessible state without selecting
which outcome occurs.

---

## Dimensional Folding Explanation

1. **Decoherence as environmental entanglement:** In DFC, a quantum superposition is an
   amplitude distribution over field configurations that has not yet committed to a single
   topological sector. The compression field is a single connected object, so any local
   amplitude distribution is correlated with the field configuration elsewhere. When the
   local superposition couples to many environmental degrees of freedom (thermal vibrations,
   air molecules, photons), those correlations spread the amplitude across a large number
   of substrate configurations.

2. **Why interference terms vanish:** The off-diagonal terms in the density matrix represent
   coherence between two field configurations. As those configurations become entangled with
   exponentially many environmental configurations, the two branches of the superposition
   can no longer interfere — any interference would require all the environmental modes to
   also interfere coherently, which is exponentially unlikely. The off-diagonal terms do not
   disappear from the full system; they become inaccessible to any local measurement.

3. **Pointer states from stability:** The pointer states (classical-looking states) are those
   field configurations that are most stable under environmental coupling — the kink states,
   not the sub-threshold superpositions. A kink is a topologically protected configuration
   that does not spread when it interacts with the environment. A sub-threshold superposition
   does spread. This is why macroscopic objects are always observed in kink-like (classical)
   states: only kinks are stable against environmental entanglement.

4. **Decoherence vs. measurement:** In `foundations/measurement.md`, measurement is a
   threshold-crossing event that nucleates a kink — an irreversible commitment to one
   topological sector. Decoherence is the pre-threshold process that makes the superposition
   practically inaccessible without requiring a threshold-crossing event. The distinction:
   decoherence destroys coherence; measurement nucleates a kink. The two often occur together
   but are conceptually distinct in DFC.

5. **Timescale:** The decoherence time in DFC should follow from the rate at which the
   amplitude leaks into environmental kink configurations — related to the Kramers escape
   rate from `foundations/born_rule_derivation.md`. A quantitative estimate of the
   decoherence timescale from substrate parameters is an open derivation.

---

## Formal Equations

### Density matrix decoherence

A quantum superposition of two field configurations separated by Δx is described by
the reduced density matrix obtained by tracing out the environmental degrees of freedom.
The off-diagonal element — the interference term between the two configurations — decays
exponentially in time at a rate set by the decoherence rate Λ and the separation squared:

```
ρ(x, x', t) = ρ(x, x', 0) × exp(−Λ (x − x')² t)

where Λ = (2m k_B T γ) / ℏ²

  m   = mass of the system
  T   = temperature of the environment
  γ   = momentum relaxation rate (system-environment coupling strength)
  k_B = Boltzmann constant
  ℏ   = reduced Planck constant (POSTULATE — not yet derived from DFC substrate)
```

The interference terms that carry quantum coherence are suppressed by a factor
exp(−Λ Δx² t). When this factor falls below 1/e, coherence is effectively lost.

### Decoherence time

The decoherence time — the time for the coherence factor to fall to 1/e — is the
reciprocal of the decoherence rate times the squared separation:

```
τ_D = 1 / (Λ Δx²) = ℏ² / (2m k_B T γ Δx²)
    = τ_relax × (λ_th / Δx)²    [Zurek form]

where:
  τ_relax = m/γ      (momentum relaxation time — classical friction timescale)
  λ_th = ℏ / √(2mk_BT)  (thermal de Broglie length)
```

The thermal de Broglie length is the quantum length scale below which quantum effects
are important. For separations much larger than this length, decoherence is extremely
rapid.

### Numerical estimates

For a 1-gram macroscopic object at room temperature (T = 300 K), with separation
Δx = 1 nm and typical air-molecule scattering relaxation time τ_relax ≈ 10⁻¹³ s:

```
λ_th = ℏ / √(2mk_BT) = 1.055×10⁻³⁴ / √(2 × 10⁻³ × 4.14×10⁻²¹)
     ≈ 1.16×10⁻²³ m   [sub-nuclear — quantum effects completely irrelevant]

τ_D = τ_relax × (λ_th / Δx)²
    = 10⁻¹³ × (1.16×10⁻²³ / 10⁻⁹)²
    ≈ 10⁻¹³ × 1.35×10⁻²⁸
    ≈ 10⁻⁴¹ s   [far faster than any physical timescale]
```

For a C₆₀ molecule (m ≈ 720 u ≈ 1.2×10⁻²⁴ kg) in vacuum at T = 1 K,
with Δx = 10 nm and τ_relax = 10⁻³ s (isolated):

```
λ_th = ℏ / √(2 × 1.2×10⁻²⁴ × 1.38×10⁻²³ × 1)
     ≈ 5.7×10⁻¹² m  [5.7 pm]

τ_D = 10⁻³ × (5.7×10⁻¹² / 10⁻⁸)²
    ≈ 10⁻³ × 3.2×10⁻⁷ ≈ 3×10⁻¹⁰ s
```

Consistent with why C₆₀ interference is only observable in high vacuum at low temperature.

### Connection to DFC substrate

In DFC, the decoherence rate Λ follows from the rate at which sub-threshold amplitude
in the compression field leaks into environmental kink configurations. The Kramers escape
rate for a field fluctuation to reach the kink threshold φ₀ from amplitude φ < φ₀ sets
the environmental coupling γ in the formula above. This connection is not yet formally
derived. See `foundations/born_rule_derivation.md` Open Problem: position Born rule from
Kramers escape statistics.

The decoherence formula above requires ℏ, which is imported as a postulate
(not derived from DFC substrate). See `foundations/planck_constant_derivation.md`.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Decoherence occurs | Environmental entanglement spreads amplitude | Universally observed | ✓ structural |
| Pointer states exist | Kink configurations are stable; superpositions are not | Pointer states observed in SQUIDs, etc. | ✓ structural |
| Decoherence faster for larger objects | More environmental modes couple to heavier kinks | Macroscopic quantum states not observed | ✓ structural |
| Decoherence timescale | From Kramers escape rate and environmental coupling | ~10⁻²³ s for macroscopic objects | not yet derived ✗ |

---

## Open Questions

1. **Derive the decoherence timescale from substrate parameters:** Use the Kramers escape
   rate formula (from `foundations/born_rule_derivation.md`) to compute the rate at which
   a sub-threshold superposition becomes entangled with N environmental modes, and derive
   the decoherence time as a function of system mass, separation, and temperature.

2. **Pointer state selection from kink stability:** Show formally that kink configurations
   are stable under small environmental perturbations while sub-threshold superpositions
   are not. This would explain why pointer states are kink-like.

3. **Decoherence without measurement:** Distinguish decoherence (amplitude spreading without
   threshold crossing) from measurement (threshold crossing to a definite topological sector).
   Can decoherence be reversed? In DFC, it cannot be easily reversed once the amplitude has
   spread into many environmental modes, but it is not irreversible in the same strong sense
   as measurement.

---

## Connections

- `foundations/measurement.md` — threshold-crossing model of measurement
- `foundations/born_rule_derivation.md` — Kramers escape rate (position Born rule, open)
- `phenomena/quantum/quantum_mechanics.md` — wave functions and superposition
- `phenomena/quantum/entanglement.md` — substrate connectivity and entanglement
- `phenomena/quantum/wave_particle_duality.md` — kink regime vs. sub-threshold regime
