# Phenomenon: Hawking Radiation

## One-Sentence Synthesis

> The event horizon of a black hole is the boundary at which D3 localization pressure
> from the closure density gradient cannot be compensated by substrate alignment
> propagation; virtual kink-antikink pairs nucleate near the horizon by the same
> mechanism as particle-antiparticle pair production, with one member crossing into
> the closure and one escaping — producing a thermal flux at temperature T_H = ℏc³/(8πGMk_B)
> that requires both G_Newton and ℏ from the substrate (both open).

---

## Observation

Stephen Hawking (1974) predicted that black holes are not perfectly black — they emit
thermal radiation from their horizons at a temperature inversely proportional to their
mass. The Hawking temperature for a black hole of mass M is:

```
T_H = ℏ c³ / (8π G M k_B)
```

The Hawking temperature equals the reduced Planck constant times the cube of the speed
of light, divided by the product of eight times pi, Newton's gravitational constant,
the black hole mass, and the Boltzmann constant.

Key data:
```
T_H (solar mass, M_☉)   ≈ 6 × 10⁻⁸ K     (undetectably small)
T_H (primordial, M~10¹⁵ g) ≈ 10¹² K      (would be evaporating now → detectable if observed)
Evaporation time:   t_evap ∝ M³           (large black holes evaporate extremely slowly)
```

Hawking radiation has not been directly observed (T_H is far too small for astrophysical
black holes). Analog models (acoustic black holes in BEC systems) have demonstrated the
effect in the laboratory.

---

## Standard Explanation

Hawking's original derivation uses quantum field theory in curved spacetime. Near the
event horizon, the extreme spacetime curvature mixes positive and negative frequency
modes of the quantum field — modes that appear as positive frequency to a freely-falling
observer appear as mixed positive/negative to a distant observer (Bogoliubov transformation).
This mixing produces a thermal spectrum of particles at infinity.

Equivalently (Unruh effect picture): a uniformly accelerating observer near the horizon
perceives the Minkowski vacuum as a thermal bath. The surface gravity κ = c⁴/(4GM) sets
the acceleration, giving T_H = ℏκ/(2πck_B).

The information paradox: if black holes radiate thermally and eventually evaporate
completely, the information about the infalling matter appears to be lost. This remains
one of the deepest unresolved questions in theoretical physics.

---

## Dimensional Folding Explanation

**Structural account (open for quantitative derivation):**

**Event horizon as substrate alignment boundary:**
In DFC, the black hole is a massive closure configuration — a high-density D3 localization
region where the substrate's fold orientation cannot be transported outward (the alignment
propagation speed equals c, but the closure density gradient requires faster-than-c
alignment to compensate). The horizon is the surface at which this compensation fails.

Inside the horizon: substrate alignment propagates inward faster than the closure density
forces outward alignment. Any substrate mode configuration is drawn toward the central
closure.

Outside the horizon: substrate alignment propagates outward; field configurations can escape
to infinity. The horizon is the DFC boundary between these regimes.

**Pair nucleation at the horizon:**
Virtual kink-antikink pairs continuously nucleate and annihilate from the vacuum by the
same mechanism as particle-antiparticle pair production (see
`phenomena/particle_physics/pair_production.md`). These virtual pairs have lifetimes set
by the energy-time relation: Δt ~ ℏ/(2 E_kink).

Near the horizon, the substrate gradient is steep — the pair's two members experience
different alignment pressures. For pairs nucleating sufficiently close to the horizon,
one member's trajectory curves into the closure (it crosses the horizon inward) while
the partner's trajectory curves outward (it can propagate to infinity). Once separated
by the horizon, the pair can no longer annihilate: the two members are topologically
disconnected by the horizon boundary.

The escaping member carries positive energy; the infalling member carries negative energy
(in the exterior coordinate frame), reducing the closure's mass. The net effect: the
closure loses mass steadily while emitting a flux of real kink configurations — Hawking
radiation.

**Thermal spectrum:**
The thermal character of the emission arises from the same quantum-mechanical averaging
that produces the Unruh effect: the external observer's inability to access the interior
state makes the observed radiation appear thermal. In DFC, this is the loss of phase
coherence between the escaping and infalling kink members — because one is behind the
horizon, its fold orientation angle is inaccessible to the external observer, and the
external state is a mixed (thermal) state.

**Temperature from surface gravity:**
The Hawking temperature T_H = ℏc³/(8πGMk_B) requires both ℏ and G_Newton from the
substrate. Neither is currently derived (both are Tier 4 open). Structurally, T_H is
proportional to the surface gravity κ = c⁴/(4GM) — the gradient of the alignment
propagation speed at the horizon. Higher surface gravity → steeper gradient → harder
separation of the virtual pair → higher effective temperature.

**Information paradox in DFC:**
In DFC, the substrate is one object. The information "lost" to the interior is not
destroyed — it is encoded in the D1 substrate configuration of the closure. Whether
this encoding is accessible to the external observer depends on whether the substrate
at D1 depth is globally connected (which DFC's premise requires: there is one continuous
object, not two disconnected pieces). The DFC resolution of the information paradox is
that the substrate's global connectivity at D1 depth means the information is never
truly lost — but recovering it requires correlations across the horizon that are
exponentially suppressed for macroscopic black holes. This is a structural resolution,
not a derived result.

---

## Formal Equations

```
[STUB — quantitative prediction blocked by G_Newton and ℏ derivation gaps]

Hawking temperature:
T_H = ℏ c³ / (8π G M k_B)     [requires G_Newton and ℏ from substrate]

Surface gravity:
κ = c⁴ / (4 G M)              [Schwarzschild black hole]

Evaporation timescale:
t_evap = (5120 π G² M³) / (ℏ c⁴)    [requires G_Newton and ℏ]

DFC pair nucleation rate at horizon:
Γ_pair ∝ exp(−2 E_kink / T_H)    [Boltzmann factor; structural analog of Schwinger rate]
```

---

## Consistency Checks

| Check | Status |
|---|---|
| Horizon as substrate alignment boundary | ✓ (structural) |
| Pair nucleation mechanism same as pair production | ✓ (structural; see pair_production.md) |
| Thermal spectrum from phase decoherence | ✓ (structural) |
| T_H ∝ 1/M (inverse mass scaling) | ✓ (structural; from surface gravity argument) |
| Quantitative T_H from DFC substrate | ✗ (OPEN — requires G_Newton and ℏ from substrate) |
| Information paradox resolution | ✗ (OPEN — structural argument present; not derived) |

---

## Open Questions

1. **G_Newton from substrate:** The gravitational constant G_Newton does not yet appear
   as a derived parameter in DFC. The DFC account of gravity is that curvature is
   the misalignment of fold orientation under transport (see the DFC interpretive dictionary
   in `foundations/substrate.md`), but translating this to G_Newton as a numerical value
   requires identifying the substrate's alignment stiffness with the Planck scale.

2. **ℏ from substrate:** Same blockage as the photoelectric effect. See
   `foundations/planck_constant_derivation.md`. T_H would be the first prediction requiring
   both G_Newton and ℏ simultaneously — making it the last prediction to be computable.

3. **Analog Hawking radiation in BEC systems:** BEC analogs of black holes (sonic horizons)
   have observed thermal phonon emission. In DFC, the BEC is a macroscopic D2 mode
   occupation; the sonic horizon is a D2/D3 alignment boundary. Comparing DFC predictions
   for the analog spectrum to BEC experiments could provide a test before astrophysical
   Hawking radiation is accessible.

4. **Black hole information in DFC:** Formalize whether the D1 substrate connectivity
   is sufficient to resolve the information paradox — specifically, whether the infalling
   member's fold orientation is encoded in the substrate's global state in a way that
   correlates with the outgoing Hawking radiation.

---

## Connections

- `phenomena/particle_physics/pair_production.md` — same kink-antikink nucleation mechanism
- `phenomena/gravity/black_holes.md` — closure density, horizon geometry in DFC
- `foundations/planck_constant_derivation.md` — ℏ hierarchy (Tier 4 open)
- `foundations/substrate.md` — one continuous object; D1 global connectivity
- `foundations/compression_dynamics.md` — buckling threshold; pair nucleation condition
- `phenomena/condensed_matter/superfluidity.md` — BEC analog black holes; sonic horizons
