# Phenomenon: Special Relativity

## One-Sentence Synthesis

> Special relativity is not an independent theory — it is the direct consequence of the
> compression field equation being Lorentz-covariant: c is the field's own propagation
> speed (not a speed limit imposed from outside), E = mc² is the KG dispersion at zero
> momentum, and time dilation is the slowing of irreversible compression-event bookkeeping
> for a moving structure whose internal clock is its Compton oscillation.

---

## Observation

The speed of light is the same in all inertial frames regardless of source or observer
motion. Clocks moving relative to an observer run slower (time dilation — confirmed by
muon lifetimes, GPS corrections, atomic clocks on aircraft). Moving objects are
length-contracted along their direction of motion. Mass and energy are equivalent
(E = mc²). No massive object can reach c; the energy required diverges as v → c.

These are not approximations — they are exact. Every prediction of SR has been confirmed.

---

## Standard Explanation

Einstein (1905): two postulates — (1) the laws of physics are the same in all inertial
frames, (2) c is the same in all inertial frames. From these, the Lorentz transformation
replaces the Galilean transformation. The invariant spacetime interval:

```
ds² = c²dt² − dx² − dy² − dz²
```

is the same for all observers. Time dilation: Δt' = γΔt. Length contraction:
L' = L/γ. Energy-momentum: E² = (pc)² + (mc²)². Rest energy: E = mc².

The Standard approach takes the two postulates as axioms. It does not explain why c is
universal or why the Lorentz transformation is the right one.

---

## Dimensional Folding Explanation

### The Core Mechanism

Special relativity is not a new theory in DFC. It is the symmetry of the compression
field equation.

The compression field equation:
```
∂²φ/∂t² = c²∇²φ − V'(φ)
```

can be written in manifestly covariant form as:
```
□φ = V'(φ)
```

where □ = (1/c²)∂²/∂t² − ∇² is the d'Alembertian, constructed from the Minkowski
metric with signature (+, −, −, −). This equation takes **exactly the same form** in
every inertial frame connected by a Lorentz transformation. There is no preferred frame,
no aether, no absolute rest state.

All of special relativity follows from this single structural fact.

### Why c Is Universal

c appears in the compression field equation as the ratio of the field's restoring force
to its inertia — a structural parameter of the field itself. It is not "the speed of
light." It is the speed at which any unanchored disturbance in the compression field
propagates. Light achieves this speed because it is the massless mode of the same field
(V'(φ) = 0, see `phenomena/light/light.md`).

A massive structure (kink, depth d ≥ 4) is anchored. Moving it requires pushing its
depth anchoring through the compression field — and the energy cost diverges as v → c
because the kink cannot propagate faster than the field it is made of.

**The "speed limit" c is not a law imposed on motion. It is the natural propagation
rate of the substrate from which all moving things are made.**

---

## Formal Derivations

### 1. Invariant Speed from Field Covariance

The wave equation □φ = 0 (massless limit) has plane-wave solutions:

```
φ = A exp(i(k·x − ωt))   with ω = c|k|
```

Under a Lorentz boost (v along x-axis), the wave 4-vector (ω/c, k) transforms as a
4-vector:
```
ω' = γ(ω − v k_x)
k'_x = γ(k_x − v ω/c²)
```

For a light wave: ω = c|k|. After the boost:
```
ω'/k'_x = c × γ(ω − v k_x) / γ(k_x − v ω/c²)
         = c × (ω − v k_x) / (k_x − v ω/c²)
         = c × (c k_x − v k_x) / (k_x − v c k_x/c²)     [using ω = c k_x for light along x]
         = c × k_x(c − v) / k_x(1 − v/c)
         = c     ✓
```

The speed of light is invariant under Lorentz boosts — derived, not postulated — because
the wave equation is Lorentz-covariant.

### 2. E² = (pc)² + (mc²)² from KG Dispersion

The massive compression field (kink) satisfies the Klein-Gordon equation (see
`equations/quantum_emergence.py`, `phenomena/quantum/quantum_mechanics.md`):

```
□φ + m_eff²c²/ℏ² φ = 0
```

Plane wave solutions φ = exp(i(k·x − ωt)) require:

```
ω²/c² − k² = m_eff²c²/ℏ²

→  (ℏω)² = (ℏck)² + (m_eff c²)²

→  E² = (pc)² + (mc²)²       ✓     [where E = ℏω, p = ℏk, m = m_eff]
```

This is the relativistic energy-momentum relation, derived directly from the compression
field equation without any additional assumption.

### 3. E = mc² at Rest

Setting p = 0 (k = 0) in the KG dispersion:
```
E² = (mc²)²    →    E = mc²      ✓
```

Rest energy is the Compton oscillation energy of a stationary kink. A particle at rest
carries energy purely as the oscillation of the compression field around its stable
minimum — not as kinetic energy, but as the field's intrinsic oscillation at rate
ω_C = mc²/ℏ.

### 4. Time Dilation from Compton Oscillation Rate

A stable kink is its own clock. Its natural oscillation rate at rest:
```
ω_C = m c²/ℏ     [Compton frequency]
```

When the kink moves at velocity v, its total energy is:
```
E = γmc²     [from KG dispersion with p = γmv]
```

Since energy and oscillation frequency are related by E = ℏω, the oscillation rate
of the moving kink as seen from the lab frame is:
```
ω_lab = E/ℏ = γmc²/ℏ = γ ω_C
```

The kink completes one internal oscillation every 2π/ω_lab seconds of lab time. But
one oscillation corresponds to one tick of the kink's proper clock (Compton cycle).
So:
```
Δτ (one proper tick) = 2π/ω_lab = 2π/(γ ω_C) = Δt/γ
```

Therefore:
```
Δτ = Δt/γ = Δt × √(1 − v²/c²)    [time dilation] ✓
```

**In DFC: time dilation is the slowing of a moving kink's internal Compton oscillation
as seen from the lab frame.** It is not a distortion of "time" as a dimension — it is
the relativistic energy increase of a moving kink increasing its oscillation rate,
so fewer proper cycles accumulate per unit lab time.

### 5. Length Contraction from Lorentz-Boosted Kink Profile

A stationary kink has spatial profile:
```
φ₀(x) = φ₀ tanh(x / λ_kink)     where λ_kink = √(2c²/α) = L_Pl
```

The kink is a solution of the Lorentz-covariant field equation. Under a boost to
velocity v, the spatial profile transforms as:
```
φ_v(x, t) = φ₀ tanh(γ(x − vt) / λ_kink)
```

The effective kink width in the lab frame:
```
λ_kink(v) = λ_kink / γ = λ_kink × √(1 − v²/c²)    [length contraction] ✓
```

A moving kink is compressed in its direction of motion by exactly the Lorentz factor.

### 6. Relativistic Mass Increase (as Energy, Not "Mass")

The total energy of a moving kink:
```
E = γmc²    →    E → ∞ as v → c
```

This is not a change in the kink's rest structure (mass m is fixed by α and β). It is
the increase in kinetic energy required to maintain the kink at speed v. The "speed
limit" is the divergence of this energy requirement: infinite energy would be needed
to push a kink to exactly c.

---

## The Non-Preferred-Frame Result

A common concern: does the compression field define a preferred rest frame (like an
aether)?

**No.** The compression field equation □φ = V'(φ) has no preferred frame built in.
The field is not "at rest" anywhere — it has no rest state, only propagating solutions
and stable kink solutions. All inertial frames see the same field equation with the same
c. The absence of a preferred frame is a property of the equation, not an additional
postulate.

This distinguishes DFC from classical aether theories. In those, the medium had a rest
frame (detectable via interferometry — Michelson-Morley). In DFC, the compression field
has no rest frame; it is Lorentz-invariant by construction.

---

## What This Explains

| SR phenomenon | DFC derivation |
|---|---|
| Invariance of c | Lorentz covariance of □φ = V'(φ) — same equation in all frames |
| E = mc² | KG dispersion at p = 0: E = m_eff c² |
| E² = (pc)² + (mc²)² | KG dispersion ω² = c²k² + m² — derived, not postulated |
| Time dilation Δτ = Δt/γ | Moving kink energy E = γmc² → fewer Compton cycles per lab second |
| Length contraction L' = L/γ | Lorentz-boosted kink profile compressed by γ |
| v → c requires E → ∞ | KG: E = γmc², γ → ∞ as v → c |
| No preferred frame | Field equation has no frame-dependent terms |
| Massless particles travel at c | V'(φ) = 0 → ω = ck, group velocity = c for all k |

---

## Connections to Other Phenomena

- **Light** — invariant c as massless KG mode; polarization unchanged under boosts;
  `phenomena/light/light.md`
- **Quantum mechanics** — KG → Schrödinger in NR limit; SR is the high-energy parent
  equation; `phenomena/quantum/quantum_mechanics.md`
- **General relativity** — SR is the flat-spacetime (weak gravity) limit of GR; the full
  compression gradient gives GR corrections; `phenomena/gravity/general_relativity.md`
- **Time dilation** — specific observational consequences; `phenomena/gravity/time_dilation.md`
- **Mass generation** — rest mass m_eff = ℏ√(2α)/c² from potential curvature; `foundations/substrate.md`
- **Quantum emergence** — KG derivation chain; `equations/quantum_emergence.py`

---

## Open Questions

1. **Lorentz invariance of V'(φ):** The free-field equation □φ = 0 is manifestly
   Lorentz-covariant. The full equation □φ = V'(φ) requires that V'(φ) also transform
   as a Lorentz scalar. Since V(φ) = −α/2 φ² + β/4 φ⁴ and φ is a scalar field, V'(φ)
   is automatically a scalar. This is consistent but should be formally verified that the
   kink solution (which breaks translational symmetry) does not introduce preferred-frame
   effects through its spatial profile.

2. **Spin and Lorentz group:** The Lorentz group has spinor representations (spin 1/2)
   as well as vector representations (spin 1). The scalar compression field φ gives spin-0
   and spin-1 particles. Spin-1/2 fermions require a spinor field — a Dirac-like extension
   of φ. Deriving spin-1/2 from DFC requires extending the scalar compression field to a
   spinor-valued field at D6. This is the open problem connecting SR to the spin structure
   of matter.

3. **Derive the Lorentz transformation from DFC first principles:** The derivation above
   uses the known Lorentz transformation and shows the field equation is invariant under
   it. The stronger result would be to derive the Lorentz transformation itself from the
   requirement that the compression field equation is invariant under all inertial frame
   changes — recovering SR from the field, rather than verifying the field is SR-consistent.

4. **Proper time as compression event count:** Time dilation is derived here from the
   Compton oscillation rate. A deeper version would show that the number of irreversible
   compression events accumulated by a moving kink equals its proper time — connecting the
   "time as bookkeeping" definition to the Lorentz-invariant proper time dτ = √(1 − v²/c²) dt.
