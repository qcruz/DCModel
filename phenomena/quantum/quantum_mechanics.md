# Phenomenon: Quantum Mechanics — Wave Functions and the Uncertainty Principle

## One-Sentence Synthesis

> Quantum mechanics is not a separate layer of reality imposed on top of classical
> physics — it is what the dynamics of a stable compression fold looks like from the
> outside when the observer is slow compared to the fold's internal Compton oscillation
> frequency.

---

## Observation

Quantum mechanics requires several structures that have no obvious origin in classical
physics:

- **Complex wave functions** — particles are described by complex-valued amplitudes ψ(x,t),
  not positions
- **The Schrödinger equation** — iℏ ∂ψ/∂t = [−ℏ²/2m ∇² + V] ψ, with the imaginary
  unit i built into time evolution
- **The Born rule** — measurement outcomes have probability P = |ψ|², not P = ψ
- **The uncertainty principle** — Δx·Δp ≥ ℏ/2, irreducible by any measurement improvement
- **Commutation relations** — [x̂, p̂] = iℏ, meaning position and momentum are
  fundamentally incompatible observables
- **Quantization** — energies come in discrete packets, ΔE = ℏω

Standard quantum mechanics treats all of these as postulates. No derivation from more
fundamental principles is offered. Where does the complex number i come from? Why is
probability quadratic in the amplitude? Why is there an ℏ at all?

---

## Standard Explanation

The Copenhagen interpretation accepts the wave function as the fundamental object and
the Schrödinger equation as a given. The Born rule is postulated. The uncertainty
principle follows from the commutation relations, which follow from the operator
definitions, which are postulated. The imaginary unit i is inserted by hand.

Attempts to derive quantum mechanics have not produced a complete derivation from a
classical substrate:
- **de Broglie–Bohm:** must postulate the guiding wave equation separately
- **Many worlds:** takes Schrödinger as given
- **Stochastic mechanics (Nelson):** must postulate the background stochastic field
- **Emergent QM (t'Hooft):** promising but incomplete

None derives the Schrödinger equation from a classical field with a mechanical origin.

---

## Dimensional Folding Explanation

### Abstract Level

**Quantum mechanics is the non-relativistic envelope dynamics of a stable compression fold.**

A stable fold in the compression field — a kink sitting at the minimum of the buckling
potential — is not static. It oscillates internally at its natural frequency, set by
the potential curvature at the minimum:

```
ω_Compton = m_eff c² / ℏ
```

This is the Compton frequency. It is very fast: for an electron, ω_C ≈ 7.8 × 10²⁰ rad/s.
Every physical process we observe occurs at energies far below this threshold.

An external observer watching a process at energies E ≪ m_eff c² cannot follow the fast
internal oscillation directly. The observable quantity is the slowly-varying envelope of
that oscillation — how the fold's amplitude and orientation drift over time.

**The quantum wave function is this envelope.**

This is not a new idea in mathematics: any real oscillating quantity A(t)cos(ωt + θ(t))
can be written as Re[ψ(t) e^{−iωt}] where ψ = A e^{iθ} is complex. The complex structure
of quantum mechanics emerges automatically when you describe the slow part of any fast
real oscillation. The imaginary unit i appears because time differentiation of the carrier
e^{−iωt} brings down a factor of −iω, and that factor propagates into the equation of
motion for the envelope.

**Why quantum mechanics looks the way it does:**

| QM feature | DFC origin |
|---|---|
| Complex wave function ψ | Envelope of a real oscillation: ψ = A exp(iθ) |
| Imaginary unit i in ∂/∂t | Stripping the Compton carrier e^{−iωt} |
| ℏ | Quantum of action = E_kink × λ_kink |
| m_eff | Curvature of compression potential at stable minimum: m_eff = ℏ√(2α)/c² |
| Quantum phase θ | Fold orientation angle ∈ [0, 2π) |
| Uncertainty principle | Kink width and energy set by same parameters (α, β) |
| Potential V(x) | Local compression gradient from nearby stable structures |

**The uncertainty principle is structural, not epistemological.**

A compression kink has a spatial width λ and an energy E, both determined by the same
compression field parameters α and β. Making the kink narrower requires steeper gradients
— which requires more energy. The Heisenberg relation Δx·Δp ≥ ℏ/2 is not a statement
about measurement disturbance. It is the statement that a kink cannot simultaneously have
sharp position (small λ) and small momentum (low E), because both are determined by the
same underlying α and β.

---

### Perspective 1: From Inside the Stable Fold

From the reference frame of a particle (a stable compression kink), the external world
consists of slowly varying compression gradients. The particle's own fast internal
oscillation at ω_Compton defines its rest energy and the unit of action ℏ — these are
fixed, not observable from within.

What is observable is the slow variation of the envelope: how the particle drifts through
the compression gradient field, how its orientation changes as it interacts with other
folds. The Schrödinger equation describes exactly this: the evolution of the slow envelope
ψ(x,t) under external compression gradients.

From this perspective, "quantum mechanics" is just classical compression field dynamics
seen through a low-pass filter. The filter cuts off everything above ω_Compton. What
passes through is ψ and the Schrödinger equation.

### Perspective 2: From the Compression Field

From outside — from the perspective of the full compression field φ(x,t) — there is no
wave function and no quantum mechanics. There is a real field satisfying:

```
∂²φ/∂t² = c²∇²φ − V'(φ)
```

The "quantum" behavior is the behavior of small perturbations around stable folds at
low energies. The quantum-classical transition is not a measurement-induced collapse — it
is the boundary between the regime where the slow-envelope description holds (low energy,
quantum) and the regime where the full nonlinear field dynamics must be tracked
(high energy, classical chaos or particle creation).

---

## Formal Derivation

### Step 1: Compression Field Equation

The compression field satisfies (see `equations/compression_field.py`):
```
∂²φ/∂t² = c²∇²φ − V'(φ)
V(φ) = −α/2 φ² + β/4 φ⁴    [buckling potential]
V'(φ) = −αφ + βφ³
```

Stable minima at φ₀ = ±√(α/β). At these minima:
```
V'(φ₀) = 0,   V''(φ₀) = −α + 3βφ₀² = 2α > 0   ✓ (stable)
```

### Step 2: Linearization → Klein-Gordon

Write φ = φ₀ + δφ, expand V' to first order in δφ:
```
∂²δφ/∂t² = c²∇²δφ − 2α δφ
```

Comparing to the Klein-Gordon equation (∂²/∂t² − c²∇² + m²c⁴/ℏ²)φ = 0:

```
m_eff²c⁴/ℏ² = 2α   →   m_eff = ℏ√(2α) / c²   [SI units]
```

The effective mass of the quantum particle is set by the curvature of the
compression potential at the stable fold minimum. Deeper, steeper folds → heavier
particles.

### Step 3: Non-Relativistic Decomposition → Complex Envelope

Any real field satisfying the Klein-Gordon equation can be decomposed as:
```
δφ(x,t) = 1/√(2m_eff) [ψ(x,t) e^{−im_eff c²t/ℏ} + ψ*(x,t) e^{+im_eff c²t/ℏ}]
```

where ψ(x,t) varies slowly: |∂ψ/∂t| ≪ (m_eff c²/ℏ)|ψ|.

**Identification of the quantum phase — closing the derivation:**

The fold oscillates as:
```
δφ = A(x,t) cos(θ(x,t) − m_eff c²t/ℏ)
```

where A(x,t) is the fold amplitude and θ(x,t) is the fold orientation angle.
Writing this in complex exponential form:
```
δφ = Re[A(x,t) e^{iθ(x,t)} × e^{−im_eff c²t/ℏ}]
```

The quantum amplitude is:
```
ψ(x,t) = A(x,t) e^{iθ(x,t)}
```

**The quantum phase is the fold orientation angle.** This identification is not
imposed — it follows directly from writing a real oscillation in its complex envelope
form. The complex structure of quantum mechanics is the complex exponential form of
a real oscillation at the Compton frequency.

### Step 4: Non-Relativistic Limit → Schrödinger Equation

Substitute the NR decomposition into the KG equation, collect positive-frequency
terms (multiply through by e^{+im_eff c²t/ℏ} and keep terms not oscillating at ±2ω_C):

```
∂²ψ/∂t² − (2im_eff c²/ℏ) ∂ψ/∂t = c²∇²ψ
```

The m_eff²c⁴/ℏ² terms cancel exactly (this cancellation is the heart of the
NR reduction — the fast oscillation subtracts out).

In the non-relativistic limit (|∂²ψ/∂t²| ≪ (2m_eff c²/ℏ)|∂ψ/∂t|, valid when
E_kinetic ≪ m_eff c²), drop ∂²ψ/∂t²:

```
−(2im_eff c²/ℏ) ∂ψ/∂t = c²∇²ψ
```

Multiply both sides by −ℏ²/(2m_eff c²):

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   iℏ ∂ψ/∂t = − (ℏ²/2m_eff) ∇²ψ                          │
│                                                            │
│   Free-particle Schrödinger equation   ✓                  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

This is exact in the limit E ≪ m_eff c². For an electron in hydrogen:
E_kinetic ≈ 13.6 eV, m_e c² ≈ 511,000 eV → ratio ≈ 2.7 × 10⁻⁵. The
NR approximation is excellent for all atomic, molecular, and low-energy physics.

### Step 5: Compression Gradient → Potential Term

When there is a slowly varying spatial modulation W(x) of the compression curvature
(arising from a nearby stable kink acting as a compression source), the KG equation
becomes:
```
∂²δφ/∂t² = c²∇²δφ − [2α + W(x)] δφ
```

After NR reduction, W(x) appears as a potential in the Schrödinger equation:

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   iℏ ∂ψ/∂t = [− (ℏ²/2m_eff) ∇² + V(x)] ψ               │
│                                                            │
│   Full Schrödinger equation with arbitrary potential  ✓   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

where V(x) = ℏ W(x) / (2m_eff).

**Force identification in the Schrödinger equation:**

| Force | W(x) | Schrödinger potential |
|---|---|---|
| Gravity | Folding gradient Φ_fold(x) = −GM/r | V(x) = −GmM/r ✓ |
| Electromagnetism | U(1) closure mode field A_μ | Minimal coupling p̂ → p̂ − qA/c |
| Strong confinement | SU(3) closure depth modulation | Color potential V_QCD(r) |

All forces enter quantum mechanics through the same mechanism: a local modulation
W(x) of the compression field curvature that becomes a potential after NR reduction.
There is no separate "quantization" procedure — it is the NR limit of a classical field.

### Step 6: Momentum Operator and Commutation Relation

The Schrödinger equation defines the momentum operator:
```
p̂ = −iℏ∇
```

The position operator is multiplication by x:
```
x̂ = x ×
```

Their commutator on any test function f(x):
```
[x̂, p̂] f = x(−iℏ ∂f/∂x) − (−iℏ) ∂(xf)/∂x
           = −iℏ x ∂f/∂x + iℏ (f + x ∂f/∂x)
           = iℏ f
```

Therefore:
```
┌─────────────────────────┐
│   [x̂, p̂] = iℏ   ✓    │
└─────────────────────────┘
```

This is a mathematical identity — not an independent postulate. From Robertson's
theorem, any two observables Â, B̂ with [Â, B̂] = iC satisfy ΔA·ΔB ≥ |⟨C⟩|/2.
For [x̂, p̂] = iℏ:
```
Δx·Δp ≥ ℏ/2   ✓   (Heisenberg uncertainty principle)
```

### Summary: Postulates Replaced by Derivations

| Standard QM postulate | DFC status |
|---|---|
| Wave function ψ is complex | Derived: envelope of real compression oscillation |
| iℏ ∂ψ/∂t = Ĥψ (free particle) | Derived: NR limit of KG from compression field |
| iℏ ∂ψ/∂t = Ĥψ with V(x) | Derived: compression gradient W(x) → V(x) |
| p̂ = −iℏ∇ | Derived: from Schrödinger equation |
| [x̂, p̂] = iℏ | Derived: mathematical identity from operator definitions |
| Δx·Δp ≥ ℏ/2 | Derived: from [x̂, p̂] = iℏ via Robertson |
| Born rule P = \|ψ\|² | Proposed mechanism — not yet rigorously derived |

---

## Analogy: The Radio Carrier Wave

A radio broadcast encodes information as the slowly-varying amplitude and phase
of a fast carrier wave at frequency ω_carrier:
```
signal(t) = A(t) cos(ω_carrier t + θ(t))
           = Re[ψ(t) e^{−iω_carrier t}]   where ψ(t) = A(t) e^{iθ(t)}
```

The receiver strips out the carrier and works with the complex envelope ψ(t), which
carries all the information. The equation governing ψ is much simpler than the equation
governing the raw oscillation.

For the compression field:
- **Carrier** = Compton oscillation at ω = m_eff c²/ℏ (the particle's rest energy)
- **Envelope** = quantum wave function ψ(x,t)
- **Stripping the carrier** = NR decomposition: δφ = Re[ψ e^{−iωt}]
- **Equation for the envelope** = Schrödinger equation
- **Complex amplitude ψ = A e^{iθ}** = fold amplitude × fold orientation phase

The quantum wave function is the information-carrying envelope of the compression
fold's Compton oscillation.

**Where the analogy breaks down:** A radio carrier is an imposed oscillation on an
external field. The Compton oscillation is the intrinsic oscillation of the fold
itself — it is not externally driven but set by the shape of the compression potential.
And the fold is a nonlinear, topologically stable structure, not a linear perturbation.
The Schrödinger equation holds only in the linearized regime |δφ| ≪ φ₀.

---

## Connections to Other Phenomena

- **Compression field** — the substrate; `equations/compression_field.py`
- **Particle masses** — m_eff = ℏ√(2α)/c² connects compression curvature to mass;
  `equations/neutrino_masses.py`, `equations/quark_masses.py`
- **Gravity in QM** — folding gradient Φ_fold → potential V(x); `equations/folding_gradient.py`
- **Thermodynamics** — the Born rule connects to entropy via accessible pathway counting;
  `equations/entropy_production.py`
- **Quantum emergence equations** — all four mechanisms and the full derivation chain;
  `equations/quantum_emergence.py`
- **Cosmic expansion** — the same compression field governs both QM and cosmology;
  `phenomena/cosmology/cosmic_expansion.md`
- **Measurement** — measurement as compression: projective, weak, Zeno, decoherence, and
  QND each correspond to specific compression modes; the measurement problem resolved via
  buckling threshold; `foundations/measurement.md`

---

## Open Questions

1. **Born rule:** Can P = |ψ|² be derived rigorously from folding pathway counting
   (Ω_outcome/Ω_total)? The candidate mechanism is clear (born_rule_folding() in
   quantum_emergence.py), but the quantitative bridge between |ψ|² and pathway
   fractions is not yet complete.

2. **Second quantization:** The Schrödinger equation describes a single stable kink.
   A many-kink system requires the field operator ψ̂(x) with [ψ̂(x), ψ̂†(x')] = δ(x−x').
   This should emerge from the multi-kink sector of the compression field — the formal
   derivation is open.

3. **Spin:** Spinors transform under SU(2) with a 4π periodicity (a 2π rotation gives
   a sign flip). In DFC, this should emerge from the SU(2) closure topology at D6: a
   particle winds once around the SU(2) fiber under a 2π physical rotation. The formal
   connection between D6 winding number and spinor transformation is open.

4. **Relativistic QM:** The derivation stops at the NR limit. The full relativistic
   theory — the Dirac equation for spin-1/2, QED — requires keeping the full Klein-Gordon
   equation and coupling it to the U(1) closure mode field. The DFC path from KG → Dirac
   requires the spinor structure from question 3.

5. **Decoherence and measurement:** The NR decomposition is clean for an isolated kink.
   With environmental coupling, the fold orientation θ becomes entangled with environmental
   folds, and the pure state |ψ| e^{iθ} decoheres into a mixed state. How decoherence
   arises from DFC compression field interactions — and why it selects a preferred
   pointer basis — is the open problem of the quantum-classical boundary.
