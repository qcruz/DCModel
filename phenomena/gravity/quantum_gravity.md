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

**DFC account:**

1. **The problem is dissolved, not solved:** DFC does not "quantize gravity" because gravity
   is not an independent classical structure to be quantized. Gravity is the gradient of the
   compression field (see `phenomena/gravity/general_relativity.md`). The compression field
   is already quantum-mechanical: its kink solutions are the particles, its fluctuations are
   the quantum fields. There is no second step of quantization needed.

2. **The Planck scale as D1 kink width:** In DFC, the Planck length is the width of the
   D1 kink — the scale at which the substrate field's compression structure is defined
   (see `foundations/bifurcation_dynamics.md`). This is not a breakdown point but a
   characteristic length built into the substrate. The field equation is well-defined at
   this scale; there is no singularity. This identification fixes the D1 substrate coupling:
   the quadratic coupling at D1 depth is twice the square of the Planck mass (in natural
   units), giving α_D1 = 2M_Pl².

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
   (one unit of D2 orientation) and is an open derivation (Tier 4).

6. **Why gravity is weak:** The gravitational coupling constant G is approximately 10⁴⁰
   times weaker than the electromagnetic coupling at the proton mass scale. In DFC, this
   hierarchy follows from the depth separation between D2 (gravity as background field
   curvature) and D5 (electromagnetism as U(1) closure). The quantitative derivation of
   this ratio — α_grav/α_em ≈ (m_p/M_Pl)² / α_em ≈ 10⁻³⁶ — is a Criterion A target
   not yet completed.

---

## Formal Equations

### Planck Scale (imported — requires ℏ and G as independent inputs)

The Planck length is the geometric mean of the reduced Planck constant and Newton's
gravitational constant divided by the 3/2 power of the speed of light. It is the unique
length scale at which quantum and gravitational effects are simultaneously of order unity:

```
L_Pl = √(ℏ G / c³) ≈ 1.616 × 10⁻³⁵ m
```

The Planck mass is the mass at which the Schwarzschild radius and the Compton wavelength
coincide. It equals the square root of the ratio of the reduced Planck constant times the
speed of light to Newton's gravitational constant:

```
M_Pl = √(ℏ c / G) ≈ 1.22 × 10¹⁹ GeV/c²
```

The Planck time is the Planck length divided by the speed of light:

```
t_Pl = L_Pl / c ≈ 5.39 × 10⁻⁴⁴ s
```

### D1 Substrate Parameters (structural — Cycles 32, 48, 75)

The identification of the D1 kink width with the Planck length determines the D1 quadratic
coupling. The kink width equals the speed of light times the square root of two divided by
the quadratic coupling, so setting this equal to the Planck length gives: the D1 quadratic
coupling equals two times the square of the Planck mass (in natural units):

```
ξ_D1 = c √(2/α_D1) = L_Pl   →   α_D1 = 2M_Pl²  (in natural units ℏ=c=1)
α_D1 ≈ 2.98 × 10³⁸ GeV²
```

### D1 Kink Action Hierarchy (BPS-correct, Cycles 48 and 75)

The kink action at D1 depth equals the kink energy times the kink formation timescale.
Using the BPS-correct kink energy (Cycle 48 retraction), the kink action is four-thirds
times the quadratic coupling divided by the quartic coupling:

```
S_kink(D1) = (4/3) α_D1 / β = (8/3) M_Pl² / β
```

For β ≈ 0.0351, the D1 kink action exceeds the quantum of action by a factor of
approximately 10⁴⁰:

```
S_kink(D1) ≈ 1.13 × 10⁴⁰ ℏ                    [BPS-correct; Cycle 75 update]
```

This hierarchy factor represents the gap between the Planck-scale kink action and the
observed quantum of action. Bridging it is the T8 open problem (Tier 4). Approximately
13.4 bifurcation events at an effective reduction factor of 10³ per step would be needed
to reach ℏ from S_kink(D1); the DFC model has 4 events (D1→D5), leaving a residual of
~10²⁸ ℏ at D5 depth. See `foundations/planck_constant_derivation.md`.

### Hawking Temperature (structural — imported from QFT; consistent with DFC)

A black hole of mass M radiates thermally at the Hawking temperature. The Hawking
temperature equals the reduced Planck constant times the cube of the speed of light,
divided by the product of eight times pi, Newton's gravitational constant, the black hole
mass, and the Boltzmann constant:

```
T_H = ℏ c³ / (8π G M k_B)
```

Representative values:

```
M = M_Sun = 2×10³⁰ kg:   T_H ≈ 6.2 × 10⁻⁸ K   (unobservably cold)
M = M_Pl  ≈ 2.2×10⁻⁸ kg: T_H ≈ 1.4 × 10³² K   (Planck temperature)
```

The Planck mass black hole evaporates at the Planck temperature — the D1 regime where
the substrate topology is fully exposed.

### Bekenstein-Hawking Entropy (structural — imported; consistent with DFC)

The entropy of a black hole is proportional to the area of its event horizon. The
Bekenstein-Hawking formula states that the entropy equals the Boltzmann constant times
the ratio of the horizon area to four times the square of the Planck length:

```
S_BH = k_B A / (4 L_Pl²)
```

where A = 16π G² M² / c⁴ is the area of the event horizon.

For a solar mass black hole: S_BH/k_B ≈ 1.05 × 10⁷⁷. For a Planck mass black hole:
S_BH/k_B = 4π ≈ 12.6, consistent with a single topological configuration quantum.

### Gravitational vs. Electromagnetic Coupling Ratio (Tier 4 — not yet derived)

The ratio of the gravitational coupling at the proton mass scale to the electromagnetic
fine structure constant equals the square of the proton-to-Planck mass ratio divided by
the fine structure constant:

```
α_grav(m_p) / α_em = (m_p / M_Pl)² / α_em ≈ 8 × 10⁻³⁷
```

This ~10³⁶ hierarchy between gravity and electromagnetism at the proton scale is not yet
derived from the DFC substrate. The qualitative argument attributes it to the D2/D5 depth
separation, but no quantitative chain from (α, β) to G exists.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| No true singularity at Planck scale | D1 compression replaces GR divergence; field equation well-defined | Not directly measurable; GR predicts singularity | ✓ structural |
| Gravitational waves travel at c | Massless D2 mode dispersion: ω = ck | v_gw = c to 10⁻¹⁵ (GW170817) | ✓ structural (gravitational_waves.md) |
| Black hole information conserved | Topological winding numbers conserved under Hawking evaporation | Unitary evolution — active research question | ✓ structural |
| Hawking temperature formula | T_H = ℏc³/(8πGMk_B) — structural consequence of D1 kink temperature | No direct observation; consistent with GR+QFT | ✓ imported, consistent |
| Bekenstein-Hawking entropy | S_BH = k_B A/(4L_Pl²) — Planck mass limit: S/k_B = 4π ≈ 12.6 | No direct observation; consistent with GR+QFT | ✓ verified (equations/quantum_gravity.py) |
| D1 kink action hierarchy | S_kink(D1)/ℏ = 1.13×10⁴⁰ (BPS-correct, Cycle 75) | ℏ from substrate not derived (T8) | ✓ computed; hierarchy unresolved |
| Graviton spin-2 | D2 mode carries two fold-orientation units | spin-2 from GW observations | not yet derived ✗ |
| Gravity/EM coupling ratio | α_grav/α_em from D2/D5 depth separation | ~10⁻³⁶ at proton scale | not yet derived ✗ |

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
- `foundations/bifurcation_dynamics.md` — Planck length as D1 kink width; α_D1 = 2M_Pl²
- `foundations/planck_constant_derivation.md` — ℏ hierarchy; S_kink(D1)/ℏ = 1.13×10⁴⁰; T8 open
- `foundations/substrate.md` — substrate field equation at D1
- `foundations/complex_substrate.md` — D5 complex scalar extension (Cycle 75); vortex geometry
- `equations/quantum_gravity.py` — Planck scale computations; Hawking temperature; entropy table
- `equations/planck_constant.py` — S_kink(D1)/ℏ = 1.13×10⁴⁰ numerical verification
