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
