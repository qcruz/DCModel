# The D4 Gap: Deriving Gravity from the Substrate

**Status:** Active exploration (T4 open — deepest structural gap in DFC)
**Purpose:** Map precisely what is known, what is assumed, and what paths exist
toward deriving G_N from V(φ) parameters (α, β, c).

---

## 1. The Problem

DFC claims that all physics emerges from V(φ) = −α/2 φ² + β/4 φ⁴. This includes
gravity. Yet Newton's gravitational constant G_N currently enters DFC as an input
(through the use of Planck units), not as an output.

Specifically:
- DFC works in Planck units where G_N = ℏ = c = 1
- The kink width ξ = √(2/α) = 0.874 l_Pl ≈ l_Pl "by construction"
- The identification ξ ~ l_Pl sets the energy scale but does not derive G_N

**What "closing the D4 gap" means:** Express G_N as a function of α and β (and
possibly c), with no external input. Equivalently, derive the Planck mass M_Pl
from V(φ) parameters alone: M_Pl = f(α, β, c).

---

## 2. What V(φ) Already Provides

### 2a. A natural length scale

The kink width ξ = √(2/α) = √(2/∛18) = 0.874 in whatever units α carries.
If α has dimensions [mass²], then ξ has dimensions [1/mass] — it is a length.

Currently α = ∛18 M_Pl² — but this includes M_Pl as an input. The dimensionless
content is: α = ∛18 × (some mass scale)². The D4 gap is: what determines that
mass scale?

### 2b. A natural energy scale

The kink energy E_kink = (4/3) c α^(3/2) / (β√2) = 36π M_Pl in Planck units.
This is a large number — the kink is 113 Planck masses. The fact that this
number comes out as 36π (= S_kink = 1/α_em(M_c)) is a highly non-trivial
structural result.

### 2c. A self-interaction structure

V(φ) contains both attraction (−α/2 φ²) and repulsion (+β/4 φ⁴). At small φ,
attraction dominates; at large φ, repulsion wins. This is structurally identical
to gravity at small scales (attraction) being arrested by some mechanism at the
Planck scale (quantum pressure / substrate rigidity).

### 2d. Inertia from fold resistance

The D4 interpretive role: "mass is the degree to which a structure is anchored
against dimensional reconfiguration." In V(φ) language:

- A kink at φ₀ sits in a potential well with curvature V''(φ₀) = 2α
- Displacing the kink from equilibrium requires energy proportional to 2α × (δφ)²
- This resistance to displacement IS inertia
- The oscillation frequency ω_c = √(2α) = √(V''(φ₀)) IS the Compton frequency

The Compton frequency of a kink is determined by V''(φ₀). This is established
(T1). What is NOT established: the connection between this oscillation frequency
(inertia) and the long-range 1/r gravitational field that the kink produces.

---

## 3. What Is Missing

### 3a. The 1/r potential

Gravity produces a 1/r potential at long distances. DFC kinks produce a localized
profile φ_kink(x) = φ₀ tanh(x/ξ) that falls off exponentially, not as 1/r.

The missing step: how does a localized kink produce a long-range 1/r field?

In standard physics, the 1/r potential arises from a massless spin-2 field
(graviton) mediating the interaction. In DFC, the massless spin-2 mode should
be a D2 propagating excitation of the substrate. The zero-mode ω₀ = 0 of the
Pöschl-Teller spectrum (the translational mode of the kink) is massless — but
it is a scalar mode, not spin-2.

### 3b. Spin-2 from substrate

Where does the spin-2 character of gravity come from? In DFC:
- The substrate field φ is a scalar
- Gravity requires a rank-2 tensor (metric perturbation h_μν)
- The bridge: the energy-momentum tensor T_μν of the kink IS a rank-2 object
- T_μν couples to the metric g_μν, which is the substrate's geometric structure

But this assumes a pre-existing metric, which contradicts DFC's claim that
geometry is downstream. The correct DFC picture: the metric IS the substrate's
configuration at D3/D4 depths, and gravity is the response of this configuration
to the presence of a kink (closure).

### 3c. G_N as a coupling constant

In standard GR, G_N is the coupling constant between matter and geometry:
G_μν = 8πG_N T_μν. In DFC, both sides of this equation are substrate behavior.
The "coupling constant" G_N should be a derived quantity measuring how strongly
one part of the substrate (a closure) affects another part (the background
configuration).

**Dimensional analysis argument:** G_N has dimensions [length³ / (mass × time²)]
or equivalently [1/mass²] in natural units. The only mass² scale in V(φ) is α.
So G_N ~ 1/α up to dimensionless factors of β. Since α = ∛18 M_Pl² and
G_N = 1/M_Pl², we need:

```
G_N = c_G / α
```

where c_G is a dimensionless constant. In current Planck units:
G_N = 1/M_Pl² and α = ∛18 M_Pl², so c_G = α × G_N = ∛18 ≈ 2.62.

This is tantalizingly simple: **G_N = ∛18 / α = 1/M_Pl²**, which is just the
definition. But if we can derive WHY c_G = ∛18 (= α itself in Planck units),
we would have a closed formula: G_N = α/α² = 1/α.

Wait — let's be more careful. In DFC natural units where c = 1 but M_Pl is NOT
set to 1, the relationship is:

```
α = ∛18 × M_Pl²
G_N = 1/M_Pl²
Therefore: α × G_N = ∛18 (dimensionless)
```

So the content of the D4 gap is: **why does α × G_N equal a specific
dimensionless number (∛18)?** Or equivalently: why is α = ∛18 in units where
G_N = 1?

---

## 4. Paths Forward

### Path A: Self-gravity of the kink

A kink of energy E_kink = 113 M_Pl and width ξ = 0.874 l_Pl has an enormous
energy density concentrated at the Planck scale. Its own gravitational field
(in the Newtonian limit) would be:

```
Φ_grav ~ G_N × E_kink / ξ ~ (1/M_Pl²) × (113 M_Pl) / (0.874 l_Pl)
       ~ 113 / (0.874 M_Pl) ~ 129 / M_Pl
```

In natural units this is ~129, which is large — the kink is a strongly
self-gravitating object. This suggests that the kink IS in the nonlinear
gravity regime, consistent with the Jormungandr picture.

**Key question:** Does the self-gravitational energy of the kink equal some
known DFC quantity? If E_grav ~ G_N E_kink² / ξ = (113)² / 0.874 ≈ 14600
M_Pl, this is much larger than E_kink itself — indicating that the simple
Newtonian estimate breaks down and the full nonlinear regime is relevant.

### Path B: Kink-kink interaction

Two kinks separated by distance R interact through the substrate. At large
R >> ξ, the interaction should reduce to the gravitational potential
V(R) = −G_N m₁ m₂ / R if gravity is substrate-mediated.

The DFC kink-kink interaction at large separation comes from the overlap of
exponential tails: V_int(R) ~ exp(−R/ξ) for R >> ξ. This is a YUKAWA
interaction (massive mediator), not a 1/r interaction (massless mediator).

The resolution: at distances R >> ξ but still in the "substrate interior"
(D1-D4 depths), the interaction is Yukawa. The 1/r behavior emerges at D3
localization scales where the substrate's geometry becomes effectively flat
and a massless spin-2 mode propagates. The crossover scale is somewhere
between ξ ~ l_Pl and l_D3 ~ (particle Compton wavelength).

### Path C: Compression → curvature feedback

The DFC interpretive dictionary identifies:
- Spacetime curvature = irreducible misalignment of folding orientation after transport
- Gravity = coherent re-tiling induced by closure density

If a closure (kink) locally compresses the substrate, the surrounding substrate
must accommodate this compression. The accommodation propagates outward as a
coherent distortion of the D3 localization structure — this IS curvature.

The strength of this propagation (how much curvature per unit compression) is
G_N. Deriving it requires computing the substrate's response function:
how much does the D3 localization geometry distort in response to a localized
compression of magnitude E_kink at width ξ?

### Path D: Jormungandr endpoint (see jormungandr_double_well.md)

The Jormungandr picture reverses the problem: instead of deriving G_N from V(φ)
forward (substrate → gravity), it derives V(φ) from G_N backward (gravity at
maximal compression → double-well). If the endpoint of gravitational collapse
naturally produces a double-well effective potential, then G_N and α are related
by the self-consistency condition that the collapse endpoint reproduces V(φ).

---

## 5. Connections to Other Open Problems

| Problem | Connection to D4 |
|---|---|
| T8 (ℏ derivation) | G_N and ℏ are linked via M_Pl = √(ℏc/G). Deriving G_N may require or enable deriving ℏ. |
| T16 (Λ_cosm) | The cosmological constant prediction ρ_Λ ~ M_Pl⁴ exp(−283) uses M_Pl as input. Deriving M_Pl makes this a pure DFC prediction. |
| Jormungandr | D4 gap and Jormungandr are the same problem from different directions. |
| D3 localization | Gravity requires D3 (apparent space) to propagate through. D4 may depend on D3 being established first. |

---

## 6. Status

- **What is established:** ξ ~ l_Pl (structural identification, T1); ω_c = √(2α) as
  Compton frequency (T1); inertia as fold resistance (conceptual, T3); kink is
  strongly self-gravitating (dimensional analysis)
- **What is missing:** 1/r potential from substrate dynamics; spin-2 mode identification;
  G_N = f(α, β) explicit formula; kink-kink long-range interaction
- **Most promising path:** Path C (compression → curvature response function) combined
  with Path D (Jormungandr self-consistency)

---

**See also:** `foundations/jormungandr_double_well.md` for the cyclical compression
hypothesis. `equations/quantum_gravity.py` for current Planck-scale computations.
`foundations/dimensional_stack.md` for D4 interpretive framework.
