# Phenomenon: Time Dilation

## One-Sentence Synthesis

> Time dilation is the modification of a kink's internal Compton oscillation rate by
> two mechanisms: velocity (the moving kink's energy increases as γmc², stretching its
> oscillation period in the lab frame by exactly γ) and gravity (the compression gradient
> near a mass modifies the local field propagation, shifting the Compton frequency by
> the gravitational potential depth Φ/c²) — both derivable from the Lorentz covariance
> and potential structure of the compression field equation, not from any independent
> postulate about the nature of time.

---

## Observation

Clocks run slower in two distinct circumstances, and the effects combine:

**Velocity time dilation (special relativistic):**
- Muons produced in cosmic ray showers at 15 km altitude arrive at Earth's surface —
  they should decay in ~0.6 μs, travelling only ~180 m, but at v ≈ 0.9997c the
  Lorentz factor γ ≈ 41 extends their lifetime to ~25 μs, sufficient to reach sea level ✓
- Atomic clocks on aircraft (Hafele-Keating 1971): clocks on eastbound flights lost ~59 ns,
  westbound gained ~273 ns — consistent with combined velocity and gravitational effects ✓
- GPS satellites: velocity effect gives −7.2 μs/day (clocks slow); gravity effect gives
  +45.9 μs/day (clocks fast); net +38.7 μs/day correction applied continuously ✓

**Gravitational time dilation (general relativistic):**
- Pound-Rebka experiment (1959): gamma rays climbing 22.5 m in Earth's gravity are
  redshifted by Δν/ν = gh/c² = 2.46 × 10⁻¹⁵ — confirmed to 1% ✓
- GPS altitude effect: clocks at 20,200 km run fast by +45.9 μs/day ✓
- Strong gravity: neutron star surface clocks run ~30% slower than distant clocks

**Combined formula:**
```
dτ/dt = √(1 − v²/c² − 2Φ/c²)
```
where Φ = −GM/r is the gravitational potential (negative, deeper in the well).

---

## Standard Explanation

**SR time dilation:** From the Lorentz transformation. A clock moving at v in the
lab frame ticks at rate dτ/dt = √(1 − v²/c²) = 1/γ.

**GR gravitational time dilation:** From the spacetime metric. Near a mass M:
```
g₀₀ = 1 − 2GM/(rc²) = 1 + 2Φ/c²
```
Proper time relates to coordinate time by dτ = √(g₀₀) dt ≈ (1 + Φ/c²) dt.

Both results are postulated as properties of spacetime. GR does not explain why
spacetime geometry has this form — it derives it from the Einstein field equations,
which are themselves postulated.

---

## Dimensional Folding Explanation

### Time in DFC

Time in DFC is not a dimension the substrate lives inside. It is the ordered bookkeeping
of irreversible events produced by the compression field. The compression process is
monotonically irreversible: dimensional volume is continuously removed and the substrate
cannot return to a previous configuration. This irreversibility defines the direction
and local rate of time.

A "clock" in DFC is any stable kink structure undergoing periodic internal motion. The
natural oscillation rate of a kink at rest — its Compton frequency — is:

```
ω_C = mc²/ℏ
```

This is the rate at which the kink cycles through its internal compression cycle. One
tick of the kink's proper clock = one Compton cycle. Time dilation is any modification
of this rate as observed from a given frame.

### Velocity Time Dilation: Full Derivation

When a kink moves at velocity v, its total energy in the lab frame is:

```
E = γmc²    [from KG dispersion: E² = (pc)² + (mc²)², with p = γmv]
```

The energy-frequency relation E = ℏω (the energy of a mode equals the reduced Planck
constant times its angular frequency) is a postulate imported from canonical quantum
field theory — it is not yet derived from the DFC substrate. See
`foundations/planck_constant_derivation.md` for the status of this derivation. Using it:

```
ω_lab = E/ℏ = γmc²/ℏ = γω_C    [requires E = ℏω — POSTULATE]
```

**Alternative derivation without ℏ (cleaner):** The same result follows directly from the
Lorentz boost of the KG solution. A stationary kink solution φ_K(t,x) oscillates at the
rest frequency ω_C. Applying the Lorentz boost x → γ(x − vt), t → γ(t − vx/c²), the
transformed solution oscillates at ω_lab = γω_C in the lab frame — purely from the
covariance of the field equation with no reference to ℏ. See `equations/special_relativity.py`
for the numerical verification of the boosted kink profile.

The kink oscillates faster (more energy), but one proper tick corresponds to one
complete oscillation regardless of frame. The lab time per proper tick:

```
Δt_lab = 2π / ω_lab = 2π / (γω_C) = (1/γ) × 2π/ω_C = Δτ/γ
```

Inverting:
```
Δτ = Δt_lab / γ = Δt_lab × √(1 − v²/c²)    [velocity time dilation] ✓
```

**DFC interpretation:** Moving clocks run slow because their internal Compton oscillation
energy is partially converted to kinetic energy — the field's inertia distributes the
total energy across both modes. The proper clock rate is the internal Compton rate, which
decreases (relative to lab time) as kinetic energy increases.

See `phenomena/gravity/special_relativity.md` Section 4 for the detailed derivation.

### Gravitational Time Dilation: Compression Gradient Mechanism

Near a mass M, the compression field has a modified propagation structure. The mass
represents a concentration of D4 inertial depth — a region where the compression field
is deeper anchored. This creates a local compression gradient that modifies the field's
effective potential.

In the weak-field limit, the compression field equation near mass M acquires an effective
potential correction:

```
∂²φ/∂t² = c²∇²φ − V'(φ) + (2Φ/c²) ∂²φ/∂t²     [Φ = −GM/r < 0]
```

The (2Φ/c²) term modifies the effective propagation speed locally. Rearranging:

```
(1 − 2Φ/c²) ∂²φ/∂t² = c²∇²φ − V'(φ)
```

The local field propagation is rescaled by the factor (1 − 2Φ/c²). For a clock at
potential Φ, the Compton frequency is:

```
ω_C(Φ) = mc²/ℏ × √(1 + 2Φ/c²) ≈ ω_C × (1 + Φ/c²)     [for |Φ/c²| ≪ 1]
```

In a gravitational potential well (Φ < 0), ω_C(Φ) < ω_C — the Compton rate is slower.
Compared to a clock at a higher potential (Φ = 0):

```
Δτ_low / Δτ_high = ω_C(Φ)/ω_C = √(1 + 2Φ/c²) ≈ 1 + Φ/c²    [gravitational time dilation] ✓
```

A clock deeper in the gravitational well runs slower — not because "spacetime is curved"
as an independent geometric fact, but because the local compression field potential is
deeper, reducing the Compton oscillation rate.

**DFC interpretation:** Gravitational time dilation is the modification of the local
field propagation by the compression gradient produced by a mass concentration. Time
runs slower near mass because the compression field is more deeply anchored there —
the kink's internal cycling rate is reduced by the same depth anchoring that produces
the gravitational force.

### The Combined Formula

Both effects act simultaneously on any kink:

```
dτ/dt = √(1 − v²/c²) × √(1 + 2Φ/c²)
      ≈ √(1 − v²/c² − 2GM/(rc²))          [for |v²/c²|, |2GM/rc²| ≪ 1]
```

**GPS quantitative check:**

Orbital parameters: r = 26,560 km (radius from Earth center), v = 3.87 km/s

Velocity effect:
```
dτ_v/dt = √(1 − v²/c²) ≈ 1 − v²/(2c²)
         = 1 − (3870)²/(2 × (3×10⁸)²)
         = 1 − 8.33 × 10⁻¹¹
→  −7.2 μs/day    ✓   [clocks slow]
```

Gravitational effect:
```
dτ_g/dt ≈ 1 + Φ/c² = 1 − GM/(rc²)
         = 1 − (6.674×10⁻¹¹ × 5.97×10²⁴) / (2.656×10⁷ × (3×10⁸)²)
         = 1 + 5.31 × 10⁻¹⁰
→  +45.9 μs/day    ✓   [clocks fast at altitude]
```

Net: +45.9 − 7.2 = +38.7 μs/day — GPS clocks would drift by 38.7 μs/day without
correction, causing ~11 km/day positional error. The correction is applied and
confirmed operational.

---

## Formal Equations

### Velocity Time Dilation

```
Proper time rate for a kink moving at velocity v:

    dτ/dt = √(1 − v²/c²) = 1/γ

Compton frequency in lab frame:
    ω_lab = γ ω_C = γ mc²/ℏ

One proper tick = 2π/ω_lab lab-time seconds
→  Δτ = Δt/γ
```

### Gravitational Time Dilation

```
For weak-field gravitational potential Φ = −GM/r:

    dτ/dt = √(1 + 2Φ/c²) ≈ 1 + Φ/c²    [|Φ/c²| ≪ 1]

Pound-Rebka (h = 22.5 m in Earth's gravity):
    Δν/ν = gh/c² = (9.81 × 22.5) / (3×10⁸)² = 2.46 × 10⁻¹⁵   ✓
```

### Combined

```
dτ/dt = √(g_μν v^μ v^ν / c²)    [GR form]

In weak-field, low-velocity limit:
    dτ/dt = √(1 − v²/c² − 2GM/(rc²))    ✓
```

---

## Consistency Checks

| Prediction | DFC mechanism | Observed |
|---|---|---|
| Muon lifetime at v ≈ 0.9997c | Compton rate slowed by γ ≈ 41 | Confirmed (sea-level muon flux) ✓ |
| Hafele-Keating aircraft clocks | Combined v and Φ corrections | ~59 ns / ~273 ns confirmed ✓ |
| GPS velocity correction | −7.2 μs/day from kinetic energy | Applied and verified ✓ |
| GPS gravitational correction | +45.9 μs/day from Φ at 20,200 km | Applied and verified ✓ |
| Pound-Rebka redshift | Δν/ν = gh/c² = 2.46 × 10⁻¹⁵ | Confirmed to 1% ✓ |
| Combined formula dτ/dt = √(1 − v²/c² − 2Φ/c²) | KG dispersion + field potential | Standard GR result ✓ |

---

## Open Questions

1. **Strong-field gravitational time dilation.** The derivation above is the weak-field
   limit |Φ/c²| ≪ 1. Near a neutron star or black hole, the compression gradient becomes
   extreme — the kink's Compton oscillation may interact nonlinearly with the deep potential.
   Whether DFC's nonlinear field equation reproduces the full Schwarzschild metric result
   (including the singularity at r = 2GM/c² and the infinite time dilation at the horizon)
   requires deriving the strong-field compression field solution.

2. **Time dilation and quantum coherence.** Entangled clocks at different gravitational
   potentials accumulate different proper times. This has been tested using atomic clocks
   at 1 cm height difference (2022 experiment: confirmed to within 1%). In DFC, the
   phase of a kink's Compton oscillation is the quantum phase of the wavefunction — so
   gravitational time dilation produces a gravitationally-induced quantum phase shift.
   Whether DFC predicts the exact gravitational phase shift measured in neutron
   interferometry (COW experiment) from first principles is an open derivation.

3. **The arrow of time.** Both velocity and gravitational time dilation slow the proper
   clock rate — they never reverse it. In DFC, this is the statement that the compression
   process is irreversible: the Compton oscillation rate can be slowed but the direction
   of the rate (positive, forward in time) cannot be reversed because dimensional volume
   removal is monotonic. A formal proof that DFC's irreversibility enforces the arrow of
   time — connecting to thermodynamics and baryogenesis — is an open question.

4. **Time dilation and the measurement problem.** If a clock is in superposition of two
   velocities, its Compton rate is also in superposition. The "tick" of a superposed clock
   is not definite. In DFC, a kink in a superposition of momenta is in the wave regime
   — no definite tick occurs until a measurement (buckling event) collapses the superposition.
   Whether DFC's treatment of the wave-kink transition resolves the quantum clock problem
   (Page-Wootters formalism) is an open question.

---

## Connections

- **Special relativity** — velocity time dilation as Section 4, KG dispersion derivation;
  `phenomena/gravity/special_relativity.md`
- **Special relativity equations** — boosted kink profile numerical verification (Cycle 79);
  `equations/special_relativity.py`
- **General relativity** — gravitational time dilation in the weak-field metric;
  `phenomena/gravity/general_relativity.md`
- **Light** — gravitational redshift as time dilation of photon frequency;
  `phenomena/light/light.md`
- **Entanglement** — gravitationally-induced quantum phase shifts in entangled clocks;
  `phenomena/quantum/entanglement.md`
- **Thermodynamics** — compression irreversibility as the arrow of time;
  `phenomena/thermodynamics/thermodynamics.md`
- **Arrow of time** — irreversibility of the compression process; Compton rate can slow
  but direction cannot reverse; `phenomena/thermodynamics/arrow_of_time.md`
- **Planck constant** — ℏ identification (used in Compton route); status as open problem;
  `foundations/planck_constant_derivation.md`
