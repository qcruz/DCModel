# Kink Fluctuation Spectrum and Kink-Antikink Scattering

## Status

> **New in Cycle 33:** First derivation of an S-matrix element from DFC substrate
> dynamics. Two results:
>
> 1. **Shape mode: ω₁ = (√3/2) m_σ** — parameter-free prediction from the
>    Pöschl-Teller fluctuation spectrum. No free parameters: the ratio ω₁/m_σ = √3/2
>    follows from the double-well potential structure alone.
>
> 2. **Kink-antikink Born phase shift: δ(k) = 4 m_σ / (β k)** at k << m_σ —
>    the first scattering amplitude derived from the DFC substrate.
>
> Both results are computed in the 1+1D kink model (toy model for DFC closures).
> The 3+1D extension to pointlike particles requires the Skyrme/higher-dimensional
> substrate treatment. Verified in `equations/kink_scattering.py`.
>
> **New in Cycle 89:** Exact T-matrix T(q) = (q+iM_c)(q+i2M_c)/[(q−iM_c)(q−i2M_c)]
> derived from the reflectionless Pöschl-Teller n=2 potential. |T|²=1 exactly.
> Levinson theorem verified: δ(0⁺) = 2π, δ(∞) = 0. See `equations/s_matrix.py`.
>
> **New in Cycle 91:** Effective range theory derived from the exact T-matrix.
> Scattering length a_s = 3/M_c = 3λ and effective range r₀ = 11/(6M_c) ≈ 1.833λ —
> both exact, parameter-free. Wigner time delay τ_W(0) = −3/M_c = −a_s (exact
> identity). The PT n=2 potential is time-advancing (always negative τ_W).
> See `equations/scattering_length.py`.

---

## Setup: Fluctuations Around the Kink

The DFC substrate field equation is:

```
∂²φ/∂t² = c² ∂²φ/∂x² − dV/dφ

V(φ) = −α/2 φ² + β/4 φ⁴
```

The kink solution φ_K(x) = φ₀ tanh(x/λ) with φ₀ = √(α/β), λ = c√(2/α).

Write φ = φ_K(x) + η(x,t) and linearize in η:

```
∂²η/∂t² = c² ∂²η/∂x² − V''(φ_K(x)) η
```

The fluctuation potential is:

```
V''(φ_K(x)) = −α + 3β φ_K²(x)
             = −α + 3α tanh²(x/λ)
             = α[2 − 3 sech²(x/λ)]
             = m_σ²[1 − (3/2) sech²(x/λ)]
```

where m_σ = √(2α) is the meson mass (asymptotic frequency of small oscillations).

For time-dependence e^{−iωt}, the spatial eigenvalue equation is:

```
[−c² d²/dx² + V''(φ_K(x))] η = ω² η
```

---

## Exact Solution: Pöschl-Teller Potential

Setting y = x/λ and using (m_σ λ)² = 2α × (2c²/α) / c² = 4 (exactly, independent of α,β):

```
[−d²/dy² + 4 − 6 sech²(y)] η = ω² λ² η
```

Substituting E = ω²λ² − 4:

```
[−d²/dy² − 6 sech²(y)] η = E η
```

This is the **Pöschl-Teller potential** with n(n+1) = 6, **n = 2**. It is exactly solvable.
The bound state energies for integer n are:

```
E_j = −(n−j)²,   j = 0, 1, ..., n−1
```

For n = 2:

```
j = 0:  E₀ = −4  →  ω²λ² = 0   →  ω₀ = 0          (zero mode)
j = 1:  E₁ = −1  →  ω²λ² = 3   →  ω₁ = √3/λ = (√3/2) m_σ  (shape mode)
```

The continuum begins at E = 0, ω = m_σ.

### The Key Identity

```
(m_σ λ)² = √(2α) × √(2/α) × c/c = 2 × √(2α) × √(2/α) = ...
          = 2α × (2/α) = 4   (exactly, for any α, β, c)
```

This ensures the Pöschl-Teller form is **always n = 2** for the φ⁴ kink, regardless of
the specific values of α and β. The spectrum is universal.

---

## The Shape Mode: First Parameter-Free DFC Prediction

### Result

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ω₁ / m_σ = √3 / 2 ≈ 0.8660                               │
│                                                             │
│  The shape mode of any φ⁴ kink is at 86.6% of the          │
│  meson mass, independent of α, β, or c.                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Physical content

The kink fluctuation spectrum has:

| Mode | ω / m_σ | Type | Physical interpretation |
|---|---|---|---|
| Zero mode | 0 | Bound state | Translational degree of freedom |
| Shape mode | √3/2 ≈ 0.8660 | Bound state | Internal excitation |
| Continuum | ≥ 1 | Scattering states | Meson emission |

The shape mode is **below the continuum** (ω₁ < m_σ). A kink excited into its shape mode
cannot decay by emitting a single meson — it is a stable internal degree of freedom.
It can only decay by emitting two mesons (threshold at 2ω₁ = √3 m_σ < 2m_σ, so this is
kinematically possible but suppressed).

### DFC interpretation

In the DFC model, each topological closure (kink at depth D) has this internal structure:
- A translational mode (position is a degree of freedom)
- A shape mode at 86.6% of the substrate meson mass

The shape mode is a candidate for the first excitation of particles that share the same
closure topology. An analogy: in the Skyrme model, the nucleon (I=1/2) and Delta (I=3/2)
are both described by the same Skyrme field — the Delta is the rotationally excited
nucleon. In the DFC φ⁴ substrate, the shape mode is the kinetically excited kink.

Whether ω₁ corresponds to a specific observed particle splitting requires computing
the shape mode at each closure depth (D5, D6, D7) and comparing to the observed
particle mass spectrum. This is an open computational problem.

### Why this is parameter-free

The ratio ω₁/m_σ does not depend on α, β, or c because:
- Both ω₁ and m_σ scale as √α (so the ratio is α-independent)
- β appears only in the kink width λ, not in the normalized frequency ratio
- c cancels between ω₁ and m_σ

The result ω₁ = (√3/2) m_σ is a **structural invariant** of any double-well φ⁴ potential.

---

## Kink-Antikink Scattering

### Long-range potential (Manton approximation)

The kink tail at large x approaches:
```
φ_K(x) → φ₀ (1 − 2e^{−x/λ})   as x → +∞
```

When a kink (at −R/2) and antikink (at +R/2) are separated by R >> λ, their tails
overlap and produce an attractive potential:

```
V_KK̄(R) = −8(α/β) exp(−m_σ R) = −8φ₀² exp(−m_σ R)
```

The coupling strength:
```
A ≡ 8(α/β) = 8φ₀²    [in GeV, same units as α/β]
```

The interaction is Yukawa-type: exponential decay at range 1/m_σ, mediated by the
substrate field's lightest excitation (the σ meson at mass m_σ).

### Born-approximation phase shift

For the 1+1D Yukawa potential V(x) = −A e^{−m_σ|x|}, the Born-approximation S-matrix
phase shift is:

```
δ_Born(k) = A m_σ / [k (4k² + m_σ²)]

Low-k limit (k << m_σ):   δ(k) ≈ A / (k m_σ) = 8(α/β) / (k √(2α)) = 4m_σ / (βk)

High-k limit (k >> m_σ):  δ(k) ≈ A m_σ / (4k³) → 0
```

The reflection coefficient (probability of backward scattering):
```
R(k) = sin²(δ(k))
```

### Levinson's theorem check

Levinson's theorem in 1+1D states:
```
δ(0⁺) − δ(∞) = n_bound × π
```

where n_bound counts the number of bound states of the **single-kink** fluctuation potential.
The PT n=2 potential has 2 bound states (zero mode + shape mode), giving:

```
δ_exact(0⁺) = 2π,  δ_exact(∞) = 0   [from s_matrix.py — exact PT result, Cycle 89]
```

For the **kink-antikink Born approximation** (Yukawa potential), the Born phase shift
δ_Born(k) ~ A/(k m_σ) diverges as k → 0. This Born divergence is consistent with the
infinite scattering length for an attractive Yukawa potential (no additional bound states
of the two-particle system accounted for here).

---

## Numerical Results at D5 Closure Scale

With α = 2 M_c(D5)², β = 0.035, m_σ = 2.04 × 10^13 GeV:

| Quantity | Value | Notes |
|---|---|---|
| m_σ | 2.04 × 10^13 GeV | Meson mass = √(2α) |
| m_σ λ | 2.000 (exactly) | Parameter-free identity |
| ω₁/m_σ | 0.8660 = √3/2 | Shape mode (parameter-free ✓) |
| ω₁ | 1.77 × 10^13 GeV | Shape mode frequency at D5 |
| A (coupling) | 4.74 × 10^28 GeV | = 8α/β |
| δ(k=m_σ) | 22.8 rad | Phase shift at threshold |
| R(k=m_σ) | 0.52 | Reflection at threshold |
| R(k=10 m_σ) | 0.0008 | Near-transparent at high energy |
| a_s / λ | 3.000 (exactly) | Scattering length = 3 kink widths (Cycle 91) |
| a_s (D5) | 5.80 × 10^−29 m | Physical scattering length at D5 scale |
| r₀ / λ | 1.833 = 11/6 (exactly) | Effective range (Cycle 91) |
| τ_W(0) | −3/M_c = −a_s | Zero-energy time advance (Cycle 91) |

---

## Effective Range Theory from the Exact T-Matrix (Cycle 91)

The exact single-kink T-matrix (Cycle 89) allows the full effective range expansion to be
derived analytically. This section states the physical relationships in words before giving
the formal expressions.

### Scattering Length

The scattering length measures the zero-energy limit of the phase shift: it equals the
negative of the phase shift divided by the wavenumber, taken as the wavenumber approaches
zero. A positive scattering length corresponds to an effectively repulsive potential at
zero energy; a negative scattering length to an effectively attractive one.

For the Levinson-shifted phase shift δ_s(q) = δ(q) − 2π (which goes to zero as q → 0),
a Taylor expansion of the two arctan contributions gives:

```
arctan(M_c/q) → π/2 − q/M_c + O(q³)   as q → 0
arctan(2M_c/q) → π/2 − q/(2M_c) + O(q³)

δ_s(q) = δ(q) − 2π → −(1/M_c + 1/(2M_c)) × 2q + O(q³) = −3q/M_c + O(q³)
```

The scattering length is defined as minus the coefficient of q in this expansion:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  a_s = 3/M_c = 3λ       (exact, 0 free parameters)          │
│                                                              │
│  The scattering length is exactly three times the kink       │
│  width λ = 1/M_c = c/√(2α), for any α, β, c.                │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

The scattering length is positive (equal to +3λ), consistent with the reflectionless
character of the potential: there is no zero-energy bound state (a bound state at threshold
would require a_s → +∞).

### Effective Range

The effective range parameterizes the leading correction to the zero-energy approximation.
The quantity q × cot(δ_s(q)) has a Taylor expansion in even powers of q; its constant term
equals minus the inverse scattering length, and the coefficient of q² gives the effective
range divided by two.

Expanding q × cot(δ_s(q)) to order q²:

```
q cot δ_s(q) = −M_c/3 + (11/12M_c) q² + O(q⁴)
```

The coefficient of q² on the right gives r₀/2 = 11/(12M_c), so:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  r₀ = 11/(6M_c) ≈ 1.833λ   (exact, 0 free parameters)       │
│                                                              │
│  The effective range is eleven-sixths of the kink width.     │
│  The coefficient 11/12 comes from the sum of the two pole    │
│  contributions: 1/(2κ₀) × f(κ₀) + 1/(2κ₁) × f(κ₁), where  │
│  κ₀ = 2M_c (zero mode) and κ₁ = M_c (shape mode).           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Wigner Time Delay

The Wigner time delay measures how much longer a wave packet takes to traverse the
scattering region compared to free propagation. It equals the derivative of the phase
shift with respect to the wavenumber.

Taking the derivative of δ(q) = 2 arctan(M_c/q) + 2 arctan(2M_c/q):

```
τ_W(q) = dδ/dq = −2M_c/(q² + M_c²) − 4M_c/(q² + 4M_c²)
```

Both terms are negative for all real q. The time delay is **always negative** — the
reflectionless PT n=2 potential is time-advancing: a wave packet transits the scattering
region in less time than it would take to traverse the same distance freely.

At zero wavenumber, the time delay equals minus the scattering length (divided by the
wave speed, set to 1 here):

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  τ_W(0) = −3/M_c = −a_s    (exact identity)                 │
│                                                              │
│  The zero-energy time advance equals the scattering length.  │
│  Both measure the same effective range of the kink's         │
│  influence on the scattering state.                          │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Connection to Bottleneck 2

The scattering length a_s = 3λ and the holonomy radius r_U1 = 3λ/(4β) (the candidate for
the U(1) coupling radius in Bottleneck 2) differ by a factor of 1/(4β) ≈ 7.1 at β ≈ 0.035.
The scattering length sets the physical size of the kink's influence on a passing wave;
the holonomy radius is the effective orbit radius for the gauge coupling. Both share the
scale 3λ but differ by the quartic coupling suppression.

---

## Limitations of the 1+1D Model

**The 1+1D kink model is a toy model for DFC closures.** Several features require caution:

1. **Kink mass M_K vs. meson mass m_σ ratio:** In 1+1D, the BPS-correct kink energy
   E_kink = (8/3)M_c³/β (Cycle 48 retraction; see `equations/kink_model.py`), while
   m_σ = 2M_c. The ratio E_kink/m_σ = (4/3)M_c²/β ~ 10^26 at M_c = 10^13 GeV.
   In 1+1D φ⁴ theory, the kink is an extremely heavy extended object (domain wall),
   not a pointlike particle. The DFC closures that correspond to particles are 3+1D
   objects — the 1+1D kink is the simplest toy model for their topological character.

2. **Shape mode physical correspondence:** The shape mode in 1+1D is an
   internal oscillation of the domain wall. In the DFC model, the physical correspondence
   for a particle would be to the Skyrme soliton's excitation spectrum (see
   `foundations/route1_skyrme.md`) — the 3+1D generalization of the kink.

3. **Scattering in 3+1D:** The Born phase shift computed here applies to 1+1D kink-antikink
   scattering. Physical cross-sections in 3+1D would require the partial wave expansion
   of the Yukawa potential, giving σ_total ∝ A²/k² (standard result).

These limitations do not invalidate the shape mode prediction (it is a property of the
fluctuation potential, universal for φ⁴ kinks in any dimension) but do mean that the
specific numbers for M_K and the scattering phase shift require the full 3+1D treatment.

---

## Summary

| Claim | Status |
|---|---|
| Fluctuation equation maps to Pöschl-Teller n=2 | Derived ✓ |
| (m_σ λ)² = 4 exactly (parameter-free) | Derived ✓ |
| ω₀ = 0 (zero mode) | Derived ✓ |
| ω₁/m_σ = √3/2 ≈ 0.8660 (shape mode, parameter-free) | **Derived ✓ (new prediction)** |
| Shape mode is stable (below decay threshold) | Established ✓ |
| Kink-antikink long-range potential: V = −8(α/β) e^{−m_σ R} | Established ✓ |
| Born-approximation phase shift δ(k) = 4m_σ/(βk) | **First S-matrix from DFC (Born approx.)** |
| Levinson consistency δ(0⁺)=2π, δ(∞)=0 (n=2 bound states) | Verified exact ✓ (Cycle 89) |
| Exact single-kink T-matrix: T(q) = (q+iM_c)(q+i2M_c)/[(q−iM_c)(q−i2M_c)] | **Derived exact ✓ (Cycle 89)** |
| Reflectionless property \|T(q)\|² = 1 for all q | Proved ✓ (Cycle 89, machine precision) |
| Born agrees with exact at q >> M_c (leading term 6M_c/q) | Verified ✓ (Cycle 89) |
| Scattering length a_s = 3/M_c = 3λ (0 free params) | **Derived exact ✓ (Cycle 91)** |
| Effective range r₀ = 11/(6M_c) ≈ 1.833λ (0 free params) | **Derived exact ✓ (Cycle 91)** |
| Wigner time delay τ_W(q) always negative (time-advancing) | **Proved ✓ (Cycle 91)** |
| τ_W(0) = −3/M_c = −a_s (exact identity) | **Proved ✓ (Cycle 91)** |
| 3+1D extension to physical particles | OPEN |
| Shape mode physical correspondence (which splitting?) | OPEN |
| Exact kink-antikink scattering (DHN two-soliton) | OPEN |

---

## Connections

- `foundations/substrate.md` — DFC kink model; V(φ) postulates
- `foundations/route1_skyrme.md` — 3+1D generalization (Skyrme soliton)
- `foundations/bifurcation_dynamics.md` — β ≈ 0.035; γ_D = (16/3)√β RETRACTED (Cycle 48; E_kink/E_total(λ) = 8/3 exactly, β-independent)
- `equations/kink_scattering.py` — shape mode and kink-antikink Born phase shift
- `equations/kink_model.py` — static kink solution
- `equations/s_matrix.py` — exact single-kink T-matrix (Cycle 89): T(q), phase shift,
  Levinson verification, Wigner time delay, Born vs exact comparison
- `equations/scattering_length.py` — effective range theory (Cycle 91): a_s = 3/M_c,
  r₀ = 11/(6M_c), τ_W(q) always negative, τ_W(0) = −a_s; Born vs exact comparison
