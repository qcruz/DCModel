# Phenomenon: Quantum Entanglement

## One-Sentence Synthesis

> Entanglement is the persistence of global field correlation between two sub-threshold
> regions of the compression field that share a common preparation history: because the
> substrate is one connected object, a buckling event (measurement) at one location
> changes the global field configuration and instantly reshapes the amplitude distribution
> at correlated locations — not as a signal propagating between separated objects, but
> as the response of a single internally connected medium.

---

## Observation

Two particles prepared in a joint quantum state are correlated in ways that exceed any
possible local hidden-variable explanation:

**Bell's theorem (1964):** No theory of pre-existing local hidden variables can reproduce
the quantum correlations for measurements on entangled spin-1/2 pairs. The inequality:

```
|E(a,b) − E(a,c)| ≤ 1 + E(b,c)    [CHSH Bell inequality]
```

is violated by quantum mechanics up to the Tsirelson bound 2√2 ≈ 2.83, vs. the classical
limit of 2.

**Experimental verification:**
- Aspect (1982): first loophole-free Bell test for photon pairs
- Zeilinger et al. (multiple, 2022 Nobel): space-like separated measurements, loophole-free
- Maximum observed CHSH violation: S ≈ 2.82 ± 0.01 (consistent with quantum prediction 2√2)

**Key properties:**
- Correlation exists regardless of separation (verified to >1000 km, satellite experiments)
- No information can be transmitted via entanglement (no-signaling theorem)
- Measuring one particle does not change that particle's local state probabilities
- The correlation is established at preparation; no signal passes between particles at measurement

---

## Standard Explanation

Two particles in a joint state |ψ⟩ = (|↑↓⟩ − |↓↑⟩)/√2 are described by a single
non-factorizable wavefunction. The wavefunction is a property of the pair, not of
either particle individually. Measurement on one collapses the joint state, instantaneously
defining the other particle's state.

Standard QM does not explain:
- Why the joint state is "real" (measurement problem / many-worlds / relational — each
  requires additional interpretive machinery)
- Why there is no signaling despite non-local correlation
- What physically instantiates the global correlation

The Bell inequality violation rules out pre-existing hidden variables (local realism) but
does not explain the mechanism.

---

## Dimensional Folding Explanation

### The Substrate Is One Object

In DFC, there is no ontological division between "particle 1 at location A" and "particle 2
at location B" as if they were truly independent objects that happen to be correlated.
There is the substrate — one connected compression field.

An entangled pair is a preparation event that creates a correlated compression field state
across an extended region. The two "particles" are two sub-threshold kink precursors — two
regions of the field that have been set into a correlated amplitude configuration by the
preparation process. They are not separate objects that communicate. They are two aspects
of one extended field state.

This is the fundamental resolution: entanglement is not a mysterious connection between
distant objects. It is the global property of a single connected field that has been
prepared in a non-factorizable state.

### The Singlet State as a Global Field Configuration

Consider two spin-1/2 particles prepared in the singlet state:

```
|ψ⟩ = (|↑↓⟩ − |↓↑⟩)/√2
```

In DFC, this is a compression field configuration φ_pair(x₁, x₂, t) with the following
properties:

1. **Two kink precursor regions:** At x₁ and x₂, the field has sub-threshold amplitude
   localized in the kink-like configurations that will become spin-up or spin-down when
   a measurement occurs.

2. **Anti-correlated topology:** The preparation event imposes a constraint — the total
   topological charge of the pair is zero. Specifically, the D6 SU(2) winding of the
   two kink precursors sums to zero:
   ```
   N_total = N₁ + N₂ = 0    [singlet: winding numbers cancel]
   ```

3. **Non-factorizable:** The field configuration is not φ₁(x₁) × φ₂(x₂). The amplitude
   of the kink precursor at x₁ depends on the boundary conditions set by x₂, and
   vice versa. The field is globally connected.

### Why Measurement Updates Both Instantaneously

When a measurement device at x₁ pushes the local field amplitude above the buckling
threshold (see `foundations/measurement.md`):

1. The field at x₁ nucleates into a definite kink state — say, spin-up (N₁ = +1)
2. The total winding constraint N_total = 0 requires N₂ = −1
3. This is not a signal propagating from x₁ to x₂. It is a re-configuration of the
   global field — the field at x₂ is now in a definite state because the global
   constraint is satisfied.

The speed of this "update" is not limited by the speed of light because no energy or
information travels from x₁ to x₂. The constraint was always a property of the field's
global configuration. The measurement at x₁ resolves a global degree of freedom.

**Analogy (imperfect):** If you tear a piece of paper in two and put the pieces in
sealed envelopes, opening one and finding the top reveals the other is the bottom.
No signal passed — the correlation was in the preparation. Entanglement is more subtle
than this (Bell's theorem rules out exactly this classical analogy for quantum correlations),
but the global-constraint structure is correct.

### Why Bell Inequalities Are Violated

Classical correlations (including pre-shared random variables) are limited by:
```
|E(a,b) − E(a,c)| ≤ 1 + E(b,c)    [Bell/CHSH inequality]
```

Quantum correlations violate this because the field configuration is non-factorizable:
the amplitude distribution at x₁ *depends on the measurement basis chosen at x₂* (and
vice versa) through the global constraint. This is not pre-existing information — the
correlation is a property of the field's response to the joint measurement configuration,
not a pre-assigned hidden variable.

In DFC terms: the two measurement devices jointly impose a new boundary condition on the
global field. The field's response (the correlation of outcomes) depends on the joint
boundary condition — both angles a and b matter simultaneously. A local hidden variable
theory cannot reproduce this because it assumes the field state at x₁ is independent of
the measurement setting at x₂.

**DFC reproduces the quantum prediction:** For the singlet state measured along axes
a and b separated by angle θ:
```
E(a,b) = −cos(θ)    [quantum prediction]
```

In DFC, this follows from the SU(2) geometry of the D6 kink's orientation: the
probability of finding opposite spins when measuring along axes at angle θ is determined
by the overlap of the two Jackiw-Rebbi spinors projected onto the measurement axes.
The cos(θ) factor is the inner product of SU(2) spinors. The violation of the Bell
inequality follows from the same SU(2) geometry.

### Why Entanglement Cannot Signal

The no-signaling property follows from the random character of the buckling event:

1. The field at x₁ nucleates at a specific location when the threshold is crossed. But
   which outcome (spin-up or spin-down) is determined by which kink precursor locally
   exceeds threshold first — a process determined by local field fluctuations that are,
   in principle, unpredictable.

2. The measurement at x₁ does not change the *marginal* probability of outcomes at x₂.
   Before measuring at x₁: P(↑₂) = P(↓₂) = 1/2. After measuring at x₁ (spin-up):
   the state at x₂ is definitely spin-down, but P(↓₂) = 1 is only accessible if you
   know the x₁ outcome — which requires a classical channel.

3. Without the classical channel, the observer at x₂ sees random outcomes with 50/50
   probability regardless of what was done at x₁. No information can be extracted from
   the marginal distribution alone.

In DFC: the global field reconfiguration is real, but it only creates usable information
when the two sets of random outcomes are compared using a classical channel. The randomness
of the buckling event enforces the no-signaling property.

---

## Formal Equations

### The Singlet State

```
|ψ_singlet⟩ = (|↑⟩₁|↓⟩₂ − |↓⟩₁|↑⟩₂) / √2

Joint density matrix:
    ρ = |ψ⟩⟨ψ|    [pure state]

Reduced density matrix at x₁ (tracing over x₂):
    ρ₁ = Tr₂[ρ] = I/2    [maximally mixed — no local information]
```

In DFC: the reduced density matrix being maximally mixed is the statement that the
kink precursor at x₁ has equal probability of nucleating in either orientation until
the global constraint is resolved.

### Bell Correlations

```
For measurement axes a⃗ at x₁ and b⃗ at x₂, with angle θ between them:

    E(a,b) = ⟨ψ|(σ⃗·â)(σ⃗·b̂)|ψ⟩ = −cos(θ)

CHSH inequality:
    S = |E(a,b) − E(a,b')| + |E(a',b) + E(a',b')| ≤ 2    [classical bound]
    S = 2√2 ≈ 2.83                                          [quantum maximum]

Optimal angles: a = 0°, a' = 90°, b = 45°, b' = 135°
    → S = 2√2 (Tsirelson bound)
```

### DFC Global Constraint

```
Total D6 SU(2) winding for a singlet pair:
    N_total = N₁ + N₂ = 0

After measurement at x₁ with outcome N₁ = +1:
    N₂ = −N₁ = −1    (instantaneous, by global constraint)
```

The global constraint is not enforced by a signal. It is a topological property of
the preparation event. It cannot be violated without disrupting the global field
configuration, which would require energy that the measurement device does not provide.

---

## Consistency Checks

| Property | DFC mechanism | Observed |
|---|---|---|
| Bell inequality violation | Non-factorizable global field constraint | S ≈ 2√2 ✓ |
| Correlation regardless of distance | Global connectivity of substrate | Verified to >1000 km ✓ |
| No signaling | Random buckling + classical channel required | Verified (no FTL signaling) ✓ |
| Maximal mixedness of reduced state | Global constraint not resolved locally | ρ₁ = I/2 ✓ |
| E(a,b) = −cos(θ) | SU(2) spinor inner product geometry | Quantum prediction ✓ |
| Correlation set at preparation | Global field configuration from preparation event | Loophole-free Bell tests ✓ |

---

## Open Questions

1. **Rigorous derivation of E(a,b) = −cos(θ) from DFC.** The argument above (SU(2)
   spinor inner product) gives the correct form but is a structural argument, not a
   derivation from the compression field dynamics. A complete derivation would compute
   the joint measurement probability from the D6 kink's response to two simultaneous
   boundary conditions and show the cos(θ) dependence follows from the substrate's SU(2)
   closure geometry.

2. **The Tsirelson bound from DFC.** Quantum mechanics has a maximum Bell violation of
   2√2 (Tsirelson bound). Why not larger? In DFC, the bound should follow from a
   property of the D6 SU(2) geometry — the maximum correlations achievable with SU(2)
   spinors. Whether the Tsirelson bound can be derived from the substrate's SU(2) closure
   topology is an open question with potential discriminating power.

3. **Entanglement over cosmological distances.** Satellite experiments (Micius, 2017)
   verified entanglement at 1200 km. The DFC global field connectivity extends in
   principle to the entire substrate. But gravitational redshift, expansion of the
   substrate's localization behavior, and photon decoherence along the propagation
   path all affect the entangled state. Whether DFC predicts a distance-dependent
   degradation of the Bell violation (from field propagation effects) that differs
   from standard QM is an open calculation.

4. **Entanglement entropy and the holographic principle.** The entanglement entropy
   of a region scales with its boundary area in many quantum gravity contexts (Bekenstein-
   Hawking, Ryu-Takayanagi). In DFC, entanglement entropy should be derivable from
   the number of correlated field degrees of freedom across a D3 boundary surface.
   Whether this reproduces the area scaling — and connects to the black hole entropy
   result — is an open structural question.

---

## Connections

- **Measurement** — kink nucleation as the measurement event that resolves the global
  constraint; `foundations/measurement.md`
- **Quantum mechanics** — superposition and global field states; `phenomena/quantum/quantum_mechanics.md`
- **Spin** — Jackiw-Rebbi spinor structure underlying the SU(2) correlations;
  `phenomena/quantum/spin.md`
- **Interference** — wave regime vs. kink regime; which-path detection as measurement;
  `phenomena/quantum/interference.md`
- **Wave-particle duality** — the buckling threshold that connects extended field to
  point-like detection; `phenomena/quantum/wave_particle_duality.md`
