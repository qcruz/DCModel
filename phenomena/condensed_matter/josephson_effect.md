# Phenomenon: Josephson Effect

## One-Sentence Synthesis

> The Josephson effect is the macroscopic quantum tunneling of Cooper pairs across a
> barrier between two superconductors, where the tunneling current depends on the phase
> difference δ between the two condensates as I = I_c sin(δ) (DC Josephson), and where
> an applied voltage drives the phase at a rate proportional to the Cooper pair charge 2e,
> producing oscillations at the exact frequency f_J = 2eV/h (AC Josephson) — both results
> follow from the DFC topology of D5 U(1) winding and D6 Cooper pair charge 2e,
> with no free parameters beyond the critical current I_c.

---

## Observation

A **Josephson junction** consists of two superconductors separated by a thin barrier
(insulator, normal metal, or weak link). The barrier interrupts the macroscopic condensate
phase coherence. Two experimentally distinct effects are observed:

**DC Josephson effect:** A supercurrent flows across the junction with no applied voltage.
The current depends on the phase difference δ = θ₂ − θ₁ between the two condensates:

```
I = I_c sin(δ)    [DC Josephson current; no voltage required]
```

The current is the sine of the phase difference, multiplied by the critical current
I_c (maximum supercurrent the junction can carry, which depends on junction geometry).

**AC Josephson effect:** When a constant voltage V is applied across the junction, the
phase difference evolves in time, and the current oscillates at a frequency set by V:

```
f_J = 2eV/h = K_J × V

K_J = 2e/h = 483 597.848 416... GHz/V    [Josephson constant — exact since 2019 SI]
```

The Josephson constant equals twice the electron charge divided by Planck's constant.
At V = 1 mV, the oscillation frequency is approximately 483.6 GHz.

**Shapiro steps:** Under applied microwave irradiation at frequency f_rf, the junction
voltage locks to rational multiples of f_rf/K_J, producing quantized voltage steps:

```
V_n = n × h f_rf / (2e) = n × f_rf / K_J    [Shapiro steps; n = integer]
```

Each step voltage equals an integer times the ratio of the microwave frequency to the
Josephson constant.

**SQUID (superconducting quantum interference device):** Two Josephson junctions in a
superconducting loop show interference. The total critical current depends on the enclosed
magnetic flux Φ:

```
I_SQUID(Φ) = 2 I_c |cos(π Φ / Φ₀)|    [SQUID interference; Φ₀ = h/(2e)]
```

The critical current is twice I_c times the absolute value of the cosine of π times the
flux-to-flux-quantum ratio. The pattern is periodic in Φ₀ = h/(2e) and goes to zero
at half-integer multiples of Φ₀.

Key numerical values:
```
K_J = 483 597.848 GHz/V   (Josephson constant — used as SI voltage standard)
Φ₀  = h/(2e) = 2.068 × 10⁻¹⁵ Wb   (flux quantum — SQUID period)
V(1 GHz)  = 1/K_J × 1 GHz ≈ 2.068 µV   (Shapiro step at 1 GHz)
```

---

## Standard Explanation

In BCS theory, the Josephson effect arises from the quantum-mechanical amplitude for
a Cooper pair to tunnel from one superconductor to the other through the barrier. The
pair tunneling amplitude is proportional to exp(iδ), where δ = θ₂ − θ₁ is the phase
difference between the two condensates.

The DC Josephson current I = I_c sin(δ) follows from computing the net tunneling rate.
The AC effect follows from the second Josephson equation: the Cooper pair's energy in an
applied voltage V is 2eV (charge 2e in potential V), which drives the phase at the rate

```
dδ/dt = 2eV / ℏ
```

Integrating: δ(t) = δ₀ + (2eV/ℏ)t. The current then oscillates: I = I_c sin(δ₀ + 2πf_J t),
with f_J = 2eV/h. The Josephson constant K_J = 2e/h is a combination of fundamental
constants with no material dependence; its exact value made it useful as a voltage standard
since 1990, and it was fixed by definition in the 2019 SI revision.

The SQUID interference is a direct analog of optical double-slit interference: the two
junctions correspond to two paths for Cooper pair tunneling, and their phase difference
is controlled by the enclosed magnetic flux through the single-valuedness of the condensate
phase around the ring (the same flux quantization as in `superconductivity.md`).

---

## Dimensional Folding Explanation

**DC Josephson current from phase topology:**
In DFC, each superconductor is a region in which D6 electron kinks have condensed into
a state with a shared macroscopic phase angle θ — a global fold orientation of the D6
substrate. The Josephson junction is a spatial defect in the D6 substrate: the barrier
region interrupts the global phase, creating a phase discontinuity δ = θ₂ − θ₁.

The quantum amplitude for a Cooper pair to tunnel across the barrier is proportional to
the overlap integral of the two condensate wavefunctions across the barrier. This overlap
has the form exp(iδ). The physical current (the rate at which D6 kink pairs transit the
barrier) is the imaginary part of this amplitude, giving the current-phase relation:

```
I = I_c sin(δ)
```

The maximum current I_c depends on the barrier geometry and the condensate density on
each side — it is set by material parameters, not by the DFC topology alone. The
dependence on sin(δ) is topological: it is the only sinusoidal function that satisfies
time-reversal symmetry (I → −I under δ → −δ) and periodicity (I(δ + 2π) = I(δ)).

**AC Josephson effect from Cooper pair energy:**
When a potential difference V is applied across the junction, a Cooper pair crossing the
barrier gains energy 2eV (the pair has charge 2e from two D6 kinks, each carrying D5
winding number n = −1). By the quantum-mechanical principle that energy equals frequency
times Planck's constant, this energy drives the evolution of the phase difference at the rate:

```
dδ/dt = 2eV / ℏ
```

The phase difference therefore increases linearly in time: δ(t) = δ₀ + (2eV/ℏ)t. The
Josephson current I = I_c sin(δ(t)) then oscillates at the frequency at which the phase
completes each cycle:

```
f_J = (1/2π) × (dδ/dt) = eV/(πℏ) = 2eV/h
```

The Josephson constant K_J = 2e/h is therefore fixed entirely by two topological
quantities: the Cooper pair charge 2e (from the D6 kink-pair winding structure) and
Planck's constant ℏ (imported as a Tier 0 postulate — see `equations/planck_constant_derivation.py`).
No free parameters enter. This makes K_J an exact Tier 1 DFC prediction.

**Shapiro steps from phase locking:**
An applied microwave field at frequency f_rf adds an oscillating component to the
voltage: V = V_dc + V_rf cos(2πf_rf t). The Josephson equation becomes:

```
δ(t) = δ₀ + (2eV_dc/ℏ)t + (eV_rf/πℏf_rf) sin(2πf_rf t)
```

The resulting Josephson current contains terms at all harmonics nf_J ± mf_rf. When the
DC Josephson frequency f_J = 2eV_dc/h equals an integer multiple n of f_rf, a resonance
condition is satisfied — the current oscillation locks to the driving field. This locking
produces a finite DC current at a fixed voltage:

```
V_n = n × h f_rf / (2e) = n × f_rf / K_J
```

These are the Shapiro steps. Each step is at an exact multiple of f_rf/K_J — the same
topology that fixes K_J fixes the step positions.

**SQUID from loop topology:**
In a SQUID, two Josephson junctions connect the two sides of a superconducting ring.
The Cooper pair condensate must be single-valued around the ring: after traversing both
junctions and the two arms, the phase must return to its starting value modulo 2π.

The enclosed magnetic flux Φ contributes 2πΦ/Φ₀ to the total phase around the loop
(from the flux quantum Φ₀ = h/(2e)). This constraint forces the two junction phase
differences δ₁ and δ₂ to satisfy δ₂ − δ₁ = 2πΦ/Φ₀. The total critical current of
the two junctions is then:

```
I_SQUID = I_c sin(δ̄ + πΦ/Φ₀) + I_c sin(δ̄ − πΦ/Φ₀) = 2I_c cos(πΦ/Φ₀) × sin(δ̄)
```

where δ̄ = (δ₁ + δ₂)/2 is the average phase. The maximum supercurrent the SQUID can
carry is:

```
I_SQUID,max(Φ) = 2 I_c |cos(π Φ / Φ₀)|
```

The SQUID is therefore a flux-to-current transducer with sensitivity determined entirely
by the flux quantum Φ₀ = h/(2e). This is the same winding number that determines flux
quantization in a superconducting ring (see `phenomena/condensed_matter/superconductivity.md`).
The DFC origin of both is identical: single-valuedness of the condensate phase around a
closed loop, with each Cooper pair carrying D5 winding number contribution of 2e.

---

## Formal Equations

### DC Josephson Current-Phase Relation (Tier 1 — structural)

The current through the junction depends on the phase difference δ between the two
condensates as the sine of that difference, multiplied by the critical current:

```
I(δ) = I_c sin(δ)     [DC Josephson current]

0 ≤ I ≤ I_c (I_c is material-dependent — junction geometry; not from DFC topology alone)
Maximum current at δ = π/2 (quarter cycle); current = 0 at δ = 0 or π.
```

### AC Josephson Equation (Tier 1 — exact from DFC topology)

The voltage across the junction drives the phase difference at a rate proportional to
the Cooper pair energy. The rate of phase evolution equals the Cooper pair energy 2eV
divided by the reduced Planck constant:

```
dδ/dt = 2eV / ℏ

→ δ(t) = δ₀ + 2π f_J t     where f_J = 2eV/h

Josephson constant:  K_J ≡ 2e/h = 483 597.848 416 984 GHz/V  (exact — 2019 SI)
```

### Shapiro Steps (Tier 1 — exact from K_J)

Under microwave irradiation at frequency f_rf, quantized voltage steps appear at integer
multiples of the ratio of the microwave frequency to the Josephson constant:

```
V_n = n × h f_rf / (2e) = n × f_rf / K_J    n = 0, ±1, ±2, ...

Example: f_rf = 10 GHz → V_n = n × 20.678 µV
```

### SQUID Interference (Tier 1 — exact from Φ₀ = h/(2e))

The maximum supercurrent of a symmetric two-junction SQUID as a function of the enclosed
magnetic flux Φ equals twice the single-junction critical current, modulated by the
absolute value of the cosine of π times the ratio of flux to the flux quantum:

```
I_max(Φ) = 2 I_c |cos(π Φ / Φ₀)|     Φ₀ = h/(2e) = 2.068 × 10⁻¹⁵ Wb

Period: ΔΦ = Φ₀ = h/(2e)
Zeros: Φ = (n + 1/2) Φ₀ (half-integer flux quanta)
```

### Josephson Energy and Inductance (Tier 1 — structural)

The energy stored in the junction equals the critical current times the reduced Planck
constant divided by the Cooper pair charge 2e:

```
E_J = ℏ I_c / (2e) = I_c Φ₀ / (2π)    [Josephson energy]

L_J(δ) = ℏ / (2e I_c cos δ) = L_{J0} / cos(δ)    [Josephson inductance]
L_{J0} = ℏ/(2e I_c) at δ → 0
```

The Josephson inductance is the inductance the junction presents to small oscillations.
It diverges at δ = π/2, where the junction is carrying its maximum current.

---

## Consistency Checks

| Check | Status |
|---|---|
| K_J = 2e/h = 483 597.848 GHz/V (Josephson constant) | ✓ Tier 1 — exact (Cycle 60; error 2×10⁻¹² in superconductivity.py) |
| K_J = 2e/h follows from Cooper pair charge 2e + winding | ✓ Structural (D5 U(1) winding × two D6 kinks) |
| Φ₀ = h/(2e) sets SQUID periodicity | ✓ Tier 1 — same flux quantum as superconductivity (Cycle 60) |
| Shapiro steps at V_n = n f_rf/K_J | ✓ Tier 1 — exact consequence of K_J (Cycle 90) |
| DC current I = I_c sin(δ) (current-phase relation) | ✓ Structural (topological — only sin satisfying time-reversal + periodicity) |
| I_c (critical current) from DFC substrate | ✗ OPEN — depends on junction geometry and condensate density (not derived) |
| Josephson inductance L_J = ℏ/(2eI_c cos δ) | ✓ Structural (follows from DC CPR + Josephson equation) |
| RF-driven dynamics: Josephson oscillation at f_J = K_J V | ✓ Tier 1 — exact from dδ/dt = 2eV/ℏ |

---

## Open Questions

1. **Critical current I_c from DFC:** The critical current depends on the barrier transparency —
   the overlap integral of the two condensate kink configurations across the junction region.
   Deriving I_c from the DFC substrate requires modeling the D6 kink condensate profile near
   a spatial defect (the barrier). This is the junction analog of the vortex core problem
   (see `equations/complex_substrate.py`): the kink condensate must accommodate a phase
   discontinuity over a length set by the coherence length ξ.

2. **Current-phase relation beyond sinusoidal:** For high-transparency junctions (short junctions
   with ballistic transport), the current-phase relation deviates from sin(δ) and includes
   higher harmonics: I(δ) = I_c [sin(δ) + r₂ sin(2δ) + ...]. The DFC expansion in junction
   transparency would require computing the tunneling amplitude as a function of barrier height
   in the D6 substrate potential.

3. **Transient dynamics and chaos:** For a Josephson junction driven with both DC and AC bias,
   the phase dynamics is described by the resistively-shunted junction (RSJ) model. The system
   shows transitions between phase-locked (Shapiro) and running (Josephson oscillation) states.
   The DFC account would treat this as a driven kink oscillation in a periodic potential — the
   Josephson phase δ plays the role of the kink coordinate, and the junction washboard potential
   U(δ) = −E_J cos(δ) − ℏI/(2e) × δ is directly the DFC kink potential.

4. **Andreev reflection:** At a superconductor-normal metal interface, a normal electron is
   retroreflected as a hole (Andreev process). In DFC, this is the conversion between a
   free D6 kink (normal electron) and a D6 kink-antikink bound pair (Cooper pair) at the
   boundary where the phase coherence begins. This conversion process sets I_c for
   superconductor-normal metal-superconductor junctions.

---

## Connections

- `phenomena/condensed_matter/superconductivity.md` — Cooper pair topology; Anderson-Higgs;
  Meissner effect; flux quantization; K_J first mentioned
- `phenomena/condensed_matter/quantum_hall_effect.md` — related: topological conductance
  quantization R_K = h/e²; both from winding number
- `phenomena/condensed_matter/superfluidity.md` — quantized circulation κ₀ = h/m_{He4};
  same winding principle
- `foundations/higgs_geometry.md` — S³ squashing; same phase-locking mechanism as
  superconducting condensate
- `equations/superconductivity.py` — K_J verified (Cycle 60); Φ₀ verified; London depth
- `equations/josephson_effect.py` — DC CPR, Shapiro steps, SQUID, Josephson energy (Cycle 90)
- `equations/magnetic_monopoles.py` — winding number quantization; Φ₀ derivation
- `foundations/complex_substrate.md` — D5 vortex structure; phase winding (Cycle 75)
- `foundations/depth_assignment.md` — D5/D6 assignments; Cooper pair as two D6 kinks
