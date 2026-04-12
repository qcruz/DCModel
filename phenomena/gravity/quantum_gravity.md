# Phenomenon: Quantum Gravity

## One-Sentence Synthesis

> Quantum gravity — the regime where both quantum mechanics and gravity are simultaneously
> important, near the Planck scale of approximately 10¹⁹ GeV — is not a separate problem
> in DFC because the compression field is already a quantum field (its kink solutions are
> the particles) and gravity is already the gradient of that field (not a separate
> geometric structure imposed on spacetime); the divergences that plague quantum gravity
> in the standard approach arise because that approach attempts to quantize spacetime
> geometry as if it were an independent object, while in DFC the geometry is a downstream
> appearance of the substrate and the substrate field equation is already well-defined at
> the Planck scale (the kink width at D1 equals the Planck length).

---

## Observation

Quantum gravity effects are expected near the Planck scale:
- **Planck length:** L-Pl = sqrt(hbar times G / c³) ≈ 1.6 × 10⁻³⁵ meters
- **Planck mass:** M-Pl = sqrt(hbar times c / G) ≈ 2.2 × 10⁻⁸ kg ≈ 1.22 × 10¹⁹ GeV/c²
- **Planck time:** t-Pl = L-Pl / c ≈ 5.4 × 10⁻⁴⁴ seconds

No experiment directly probes the Planck scale. Evidence that quantum gravity is needed:

- **Black hole evaporation (Hawking radiation):** Black holes emit thermal radiation at
  temperature T-H = hbar times c³ / (8 pi G M k-B). As a black hole evaporates, it shrinks
  to Planck size, at which point classical GR breaks down and quantum gravity is required.
  What happens at M ~ M-Pl? GR predicts a singularity; QM predicts information must be
  preserved. The resolution is unknown.
- **Big Bang singularity:** GR predicts infinite density and curvature at t = 0. Quantum
  effects should prevent a true singularity. The structure of the universe before the Planck
  epoch requires quantum gravity.
- **Black hole information paradox:** Hawking's calculation suggests information is lost in
  black hole evaporation (pure states evolve to mixed states). This violates quantum
  mechanics. The resolution requires understanding Planck-scale physics.
- **Ultraviolet divergences in quantum GR:** Attempts to quantize GR produce non-renormalizable
  ultraviolet divergences — infinitely many independent counterterms are needed. GR as a
  quantum field theory is only an effective description valid far below the Planck scale.

---

## Standard Explanation

The standard approaches to quantum gravity are:

**String theory:** Replaces point particles with extended strings. The graviton appears as
a spin-2 mode of the closed string. UV divergences are regulated by the string length. Predicts
supersymmetry and extra dimensions; neither confirmed experimentally.

**Loop quantum gravity (LQG):** Quantizes spacetime geometry directly. Space consists of
a spin network of discrete quanta of area and volume. Time evolution is discrete. Does not
reproduce smooth spacetime in an obvious limit; does not easily accommodate the matter
content of the SM.

**Supergravity:** SUSY extension of GR. Improved UV behavior but still not finite at all
loop orders without string theory completion.

**Asymptotic safety:** GR may have a non-trivial UV fixed point under renormalization group
flow, making it a well-defined quantum theory. Evidence from truncated flow equations but
not proven.

None of these approaches is experimentally confirmed, and they are mutually inconsistent
in their fundamental starting assumptions.

---

## Dimensional Folding Explanation

**STUB — full derivation not yet written.**

**DFC mechanism direction:**

1. **The problem is dissolved, not solved:** DFC does not "quantize gravity" because gravity
   is not an independent classical structure to be quantized. Gravity is the gradient of the
   compression field (see `phenomena/gravity/general_relativity.md`). The compression field
   is already quantum-mechanical: its kink solutions are the particles, its fluctuations are
   the quantum fields. There is no second step of quantization needed.

2. **The Planck scale as D1 kink width:** In DFC, the Planck length is the width of the
   D1 kink — the scale at which the substrate field's compression structure is defined
   (see `foundations/bifurcation_dynamics.md`). This is not a breakdown point but a
   characteristic length built into the substrate. The field equation is well-defined at
   this scale; there is no singularity.

3. **Black hole singularities replaced by D1 compression:** As matter falls into a black
   hole and density increases without bound, DFC predicts that the compression field
   approaches the D1 regime — maximum compression — rather than reaching infinite density.
   The "singularity" in GR is the artifact of treating the metric as a smooth manifold even
   when compression rates have exceeded the propagation speed. In DFC, this regime is
   described by the D1 field equation with no singular behavior.

4. **Information paradox:** In DFC, information is encoded in the topological configuration
   of the substrate — the winding numbers of the various closure depths. Winding numbers
   are conserved (topological conservation laws). Information about what fell into the black
   hole is stored in the substrate's topological configuration and must be conserved
   throughout Hawking evaporation. The apparent information loss in GR is the consequence
   of treating the black hole as a smooth geometric object rather than as a concentrated
   substrate configuration.

5. **Graviton as massless D2 mode:** The graviton — the quantized particle of the
   gravitational field — should be the spin-2 massless D2 mode. Its DFC identification
   is not fully worked out. In `phenomena/gravity/gravitational_waves.md`, gravitational
   waves propagate at c with the same dispersion as massless modes. The graviton would
   be the single-quantum excitation of the same field. Spin-2 requires the D2 mode to
   carry two units of fold orientation — this is more complex than the spin-1 photon
   (one unit of D2 orientation) and is an open derivation.

6. **Why gravity is weak:** The gravitational coupling constant G is approximately 10⁴⁰
   times weaker than the electromagnetic coupling. In DFC, this hierarchy should follow
   from the depth separation between D2 (gravity as background field curvature) and D5
   (electromagnetism as U(1) closure). The derivation of this ratio is a Criterion A target.

**Key open derivation:** Show that the DFC substrate field equation at D1 depth is
non-singular and well-defined at the Planck scale. Identify the graviton as a specific
D2 mode and derive its spin-2 character. Derive the ratio G/alpha-em ≈ 10⁻⁴⁰ from
substrate parameters.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| No true singularity | D1 compression regime replaces divergent density | Not observable (but GR predicts singularity) | ✓ structural (argument written) |
| Gravitational waves travel at c | Massless D2 mode dispersion | v-gw = c confirmed to 10⁻¹⁵ | ✓ (in gravitational_waves.md) |
| Black hole information conserved | Topological winding numbers conserved | Hawking unitary evolution — active research | ✓ structural |
| Graviton spin-2 | D2 mode carries two fold orientation units | — | not yet derived ✗ |
| Gravity/EM strength ratio | G/alpha-em from depth separation D2/D5 | ~10⁻⁴⁰ | not yet derived ✗ |

---

## Open Questions

1. **Derive the graviton as a spin-2 D2 mode:** Show that the massless D2 mode carries
   two units of fold orientation angular momentum (helicity ±2), reproducing the spin-2
   character of the graviton. Compare with the spin-1 photon (one unit at D5).

2. **Derive G from substrate parameters:** The gravitational constant G determines the
   strength of gravity. Its DFC expression should involve the ratio of the D2 propagation
   depth scale to the D5 closure scale. A successful derivation would be one of the most
   significant results in the project.

3. **Black hole evaporation endpoint:** What happens when a black hole shrinks to Planck
   size in DFC? Does it leave a stable remnant (a D1 kink), evaporate completely with
   information released in the final Hawking quanta, or transition to a new phase?

4. **Einstein field equations from substrate:** Derive the full Einstein field equations
   from the DFC compression gradient dynamics. Partial progress in general_relativity.md;
   full derivation open.

---

## Connections

- `phenomena/gravity/general_relativity.md` — gravity as compression gradient
- `phenomena/gravity/black_holes.md` — D1 compression as black hole interior
- `phenomena/gravity/gravitational_waves.md` — graviton as massless D2 mode
- `foundations/bifurcation_dynamics.md` — Planck length as D1 kink width
- `foundations/planck_constant_derivation.md` — Planck scale and hbar
- `foundations/substrate.md` — substrate field equation at D1
