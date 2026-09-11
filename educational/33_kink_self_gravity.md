# Module 33 — How Kinks Attract Each Other: Gravity from V(φ)

**Series:** DFC Educational Modules
**Prerequisite reading:** Module 01 (substrate and kinks), Module 13 (mass from
compression), Module 28 (gravity gap)

**Last updated:** September 2026

---

## 1. The Question

If gravity is not a fundamental force but an emergent behavior of the substrate,
then we need to answer a concrete question: what makes one kink fall toward another?

In standard physics, two masses attract because they both curve spacetime, and
each one follows the curvature created by the other. In DFC, there is no
pre-existing spacetime to curve. There is only the substrate and its potential
V(φ) = −α/2 φ² + β/4 φ⁴. The challenge is to show that two kinks in this
potential attract each other, and that the attraction looks like Newton's law
F = G M₁ M₂ / r².

This module walks through the answer in three steps: what a single kink does to
the substrate around it, how a second kink responds, and why the result is
gravity.

---

## 2. A Kink Curves the Substrate

A kink — the localized transition from φ = −φ₀ to φ = +φ₀ — carries energy.
Its rest energy is concentrated near the center, falling off over a width
ξ = √(2/α) ≈ 0.87 in Planck units. Outside this narrow region, the field
sits in its vacuum state.

That localized energy has consequences. The kink's energy density acts as a
source in the coupled equations that relate the field profile to the substrate's
curvature. These are the DFGH equations (named after DeWolfe, Freedman, Gubser,
and Horowitz, who derived the mathematical structure):

> The curvature of the substrate's energy profile at any point equals minus
> one-sixth of the square of the field gradient at that point.

In symbols: A″ = −(1/6)(φ′)². The function A(y) describes how the substrate's
energy density varies along the compression coordinate y. At the kink center,
where the field gradient (φ′)² is largest, A″ is most negative — the substrate
curves most sharply. Far from the kink, the field reaches its vacuum value,
φ′ → 0, and A(y) settles into a steady linear decay: A(y) → −k·y, where
k ≈ 2.01 is determined entirely by α and β.

The result: the kink creates a gravitational well. The substrate's energy
density falls off exponentially away from the kink, as e^{2A(y)}. This
exponential decay is not put in by hand — it is a mathematical consequence
of the negative vacuum energy V(φ₀) = −α²/(4β) of the double-well potential.
A substrate with negative vacuum energy automatically produces an exponentially
decaying energy profile. This is the same structure as anti-de Sitter geometry,
but here it arises from V(φ), not from assuming a spacetime.

---

## 3. Confinement: The Kink Stays on the Wall

Before asking how kinks attract each other, we should notice something the warp
factor A(y) already explains: why particles are confined to three apparent
spatial degrees of freedom in the first place.

A numerical simulation (Module C575) placed a single kink in a substrate where
the compression parameter α varies gently from place to place. The kink
accelerated — not toward deeper compression, as one might naively expect, but
toward the region where its rest mass is lighter. The formula for this
acceleration is:

> The acceleration of a kink in a compression gradient equals negative
> three-halves times the gradient of the compression parameter, divided by
> the compression parameter itself.

This was confirmed numerically to 0.6% precision, with perfect linear scaling
(doubling the gradient doubles the acceleration) and a parabolic trajectory
(constant acceleration, just like a ball in a uniform gravitational field).

In the self-gravitating picture, this force acts along the compression
coordinate y — the direction "into" the substrate. It pushes kinks back
toward the center of the domain wall whenever they try to drift away. This
is confinement: the substrate's own curvature traps its excitations near the
wall. Particles do not escape into the bulk because the bulk has exponentially
suppressed energy density — there is nothing there to support dynamics.

---

## 4. Attraction: Kinks Fall Toward Each Other

Now consider two kinks, each sitting on the domain wall but separated by some
distance r along the wall's surface (the worldvolume — what we experience as
three apparent spatial degrees of freedom).

Each kink creates an A(y) profile in its neighborhood. The question is: does
kink 1's gravitational well affect kink 2?

The answer comes from a different mechanism than the confinement force. The
confinement force (Section 3) acts along the extra dimension y. The attraction
between kinks acts along the worldvolume — it is a force in the directions we
call "space."

The key is the **graviton zero mode**. The warp factor e^{2A(y)} created by
the kink traps a massless spin-2 excitation — a graviton — localized near the
wall. This is a mathematical theorem about exponentially decaying profiles
(the Randall-Sundrum result, used here as a theorem about zero modes, not as
a claim about extra dimensions). The graviton zero-mode wavefunction is
ψ₀(y) ∝ e^{A(y)}, concentrated near y = 0 where A is largest.

This trapped graviton mediates a force between kinks on the worldvolume. The
force follows the standard inverse-square law:

> The gravitational force between two kinks equals Newton's constant times
> the product of their masses, divided by the square of their separation.

Newton's constant itself is determined by how tightly the graviton is
localized. The tighter the localization (the deeper the gravitational well
A(y)), the weaker gravity is in 4D, because the graviton's probability is
more spread out in the y-direction. Specifically:

> Newton's constant equals one divided by sixteen pi times the square of
> the Planck mass, where the Planck mass squared equals twice the fifth
> power of the fundamental mass scale times the integral of the fourth
> power of e^A over the compression coordinate.

The integral ∫ e^{4A} dy is computed numerically from the DFGH solution. With
the current (conventional) value of the 5D mass scale, this gives a gravitational
coupling κ = 1.29 — about 2.6 times the target value of 0.50.

---

## 5. The Force Hierarchy

The analysis reveals a striking hierarchy of forces acting on a kink at a
distance of ten kink-widths from another kink:

| Force | Magnitude | Direction |
|---|---|---|
| Bulk confinement | 341 | Along y (keeps kinks on the wall) |
| Worldvolume gravity | 1.29 | Along x (attracts kinks to each other) |
| Sigma exchange | 10⁻⁸ | Along x (exponentially suppressed at this range) |

Gravity is the weakest of the three. The sigma meson exchange — the direct
kink-kink interaction mediated by the massive scalar mode — is exponentially
suppressed beyond a few kink widths. The bulk confinement force is by far the
strongest, which is why particles are so tightly confined to the worldvolume
that the extra dimension is undetectable.

This hierarchy is not tuned. It follows from the mathematics of V(φ): the
confinement force scales with the AdS curvature k ≈ 2, the gravitational
coupling involves an integral over the exponentially decaying warp factor,
and the sigma exchange decays as e^{−m_σ r} with m_σ ≈ 2.3. The weakness
of gravity relative to other forces — one of the great puzzles of physics —
is a structural consequence of the kink profile.

---

## 6. The Complete Chain

The full derivation from V(φ) to Newton's law proceeds in seven steps:

1. **V(φ) → kink** (Tier 1, exact): The double-well potential has a kink
   solution φ₀ tanh(y/ξ) with mass M_kink = (2√2/3) α^{3/2}/β.

2. **Kink → DFGH** (Tier 2a, verified): The kink's energy density enters the
   coupled DFGH equations. The numerical boundary-value solution matches all
   boundary conditions and constraints.

3. **DFGH → warp factor A(y)** (Tier 2a, numerical): The solution gives
   A(y) with asymptotic decay rate k = α/√(48β) ≈ 2.01.

4. **A(y) → graviton zero mode** (Tier 2a, theorem): The exponentially
   decaying warp factor traps a normalizable massless spin-2 mode ψ₀ ∝ e^{A(y)}.

5. **Graviton → Planck mass** (Tier 3, convention-dependent): The Planck
   mass squared equals twice the 5D mass scale cubed times the graviton
   normalization integral ∫ e^{4A} dy. The 5D mass scale M₅³ is currently
   set by convention (= 2), not derived from V(φ).

6. **Planck mass → Newton's constant** (Tier 1, definition): G_N = 1/(16π M_Pl²).

7. **Newton's constant → force law** (Tier 1, theorem): F = G_N M₁ M₂ / r².

Every step is Tier 1 or 2a **except Step 5**, where M₅³ remains underived.
This is the sole bottleneck in the gravity chain. The needed value is
M₅³ ≈ 0.77; the best DFC candidate (β × 4π = 4/9 ≈ 0.44) is 43% low.
Closing this gap would make gravity a zero-free-parameter prediction of V(φ).

---

## 7. What This Means

The two simulations (C575 and C576) together paint a complete picture of
how gravity works in DFC:

- A kink's energy density curves the substrate (A″ = −(1/6)(φ′)²)
- The curved substrate confines all excitations to the domain wall
- The same curvature traps a massless graviton on the wall
- The graviton mediates inverse-square attraction between kinks
- The gravitational constant is determined by the kink profile

Gravity is not a separate force bolted on to the model. It is the substrate
responding to its own energy content — the same V(φ) that produces the strong,
weak, and electromagnetic forces through closure topologies at D5–D7 also
produces gravity through the warp factor at D4. The chain has one open link
(M₅³), but the mechanism is complete.

The deeper lesson: confinement and attraction are two projections of the same
deformation. The warp factor A(y) simultaneously keeps particles on the wall
(confinement along y) and pulls them toward each other (attraction along the
worldvolume). A ball sitting in a bowl is held down by gravity and rolls toward
other balls — same bowl, two effects. In DFC, the kink's gravitational well
is that bowl.

---

## 8. Current Status and Open Questions

| Quantity | Value | Error | Tier |
|---|---|---|---|
| κ (thin-wall, algebraic) | 0.497 | −0.6% | T1 |
| κ (thick-wall + graviton) | 1.29 | +158% | T3 |
| Force hierarchy (gravity weakest) | confirmed | — | T1 structural |
| C575 bulk force law | a = −(3/(2α))dα/dx | 0.6% match | T1 structural |
| Linearity (a ∝ ε) | confirmed | 1.1% | T1 structural |

**What is established:**
- The mechanism (kink → warp factor → graviton → Newton's law)
- The confinement force (confirmed numerically)
- The force hierarchy (gravity is weakest, by structural necessity)
- The thin-wall algebraic result (κ = 0.497, −0.6%)

**What remains open:**
- Derive M₅³ from α and β (sole blocker for zero-parameter G_N)
- Understand why thin-wall (−0.6%) works better than thick-wall (+158%)
- Verify the graviton equation of motion on the thick-wall background
- Determine whether ψ₀ = e^A receives thick-wall corrections

---

## Equation Modules

- `equations/kink_gravity_gradient.py` — kink in α(x) gradient, 10/10 PASS
- `equations/kink_self_gravity.py` — complete self-gravitating chain, 11/11 PASS
- `equations/d4_thick_wall_bvp.py` — DFGH BVP solution, graviton correction
- `equations/d4_coupled_kink_warp.py` — thin-wall algebraic result

---

*Module 33 — Kink Self-Gravity. See Module 28 for the broader D4 gravity gap
analysis, and Module 14 for spacetime emergence.*
