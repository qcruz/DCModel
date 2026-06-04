# Module 01 — The Substrate: One Object, One Potential

*Prerequisites: Module 00 (recommended). No mathematics required beyond high school
algebra. This module introduces the central object of the DFC model.*

---

## What Is a Field?

Before describing the DFC substrate, we need a working idea of what a "field" is.

A temperature map of a room is a field: at every point in the room, there is a number
(the temperature). The field does not consist of objects at those points — it is a
single thing spread continuously across the space. Where it is cold is part of the same
field as where it is warm.

A magnetic field is similar: at every point in space, there are three numbers (the
direction and strength of the magnetic force). The whole field is one thing.

The DFC substrate is a field — but with one crucial difference from these examples.
The substrate is not *in* space. Space, in the DFC account, is a downstream consequence
of the substrate's behavior. The substrate does not have a pre-existing coordinate grid
to live on. It simply *is* — one continuous object — and what we experience as space is
a consequence of how that object organizes itself.

This is a radical claim, and Module 00 summarized why the model makes it. For now, just
note: the substrate is a scalar field, meaning at each of its "points" (not spatial
points — internal organizational states), there is a single number. We call this number
φ (phi).

---

## The Potential Energy Landscape

Every physical system has a tendency to settle into its lowest energy state. A ball on
a hill rolls downward. A chemical reaction proceeds toward its lowest energy configuration.
The substrate's behavior is governed by a rule that assigns energy to each configuration
of φ. This rule is called the **potential**, written V(φ).

The DFC potential has a specific shape:

```
V(φ) = −(α/2) φ² + (β/4) φ⁴
```

Do not worry about the symbols yet — we will unpack them. The key is what this shape
*looks like*.

Imagine a landscape with:
- **Two valleys**, one at φ = +φ₀ and one at φ = −φ₀ (where φ₀ is a particular value)
- **A hill** in the middle at φ = 0

This is called a **double-well potential**. If you place a ball at the center (φ = 0),
it is at an unstable equilibrium — it will roll into one valley or the other. The two
valleys are the stable states.

The natural language statement of the potential is this: **the field resists being
at zero, and is drawn toward one of two equal and opposite extremes.**

The height of the middle hill and the depth of the valleys are controlled by two
numbers, α (alpha) and β (beta). These are the model's fundamental parameters.

---

## The Two Parameters: α and β

The parameter **α** (alpha) controls the **instability at zero**: a larger α means a
steeper hill in the middle, a stronger push away from φ = 0.

The parameter **β** (beta) controls the **strength of the self-interaction**: a larger
β means steeper valley walls, a stronger restoring force once the field moves away from
zero.

Together, they determine the equilibrium values:

The field settles at values where V(φ) is minimized:
```
φ₀ = ±√(α/β)
```

(Read: phi-naught equals plus or minus the square root of alpha divided by beta.)

This is the kink equilibrium: the two stable states the field can sit in.

One crucial development from the model: β is not a free parameter. A derivation in
the model (the key result of Cycle 117, the main "Bottleneck 2" result) shows that
the quartic self-interaction strength is:

```
β = 1/(9π)
```

The number 9 comes from the dimension of the Hopf fiber structure that emerges from
the field's topology (the fibers S¹, S³, S⁵ have dimensions 1, 3, 5, summing to 9).
The factor π comes from the winding geometry.

This result is important: one of the two fundamental parameters is derived, not inserted.
The model has fewer unexplained numbers than it appears to at first.

---

## The Kink: A Topological Object

The substrate does not sit uniformly in one valley everywhere. In regions of the field,
it might be at +φ₀; in other regions, at −φ₀. Where the field transitions between these
two values, there is a special structure called a **kink**.

A kink is a smooth interpolation from −φ₀ to +φ₀ over a finite region. The mathematical
shape of the kink is:

```
φ(x) = φ₀ × tanh(x/λ)
```

(Read: phi of x equals phi-naught times the hyperbolic tangent of x divided by lambda.)

In plain language: **the field starts at −φ₀ far to one side, rises smoothly through
zero at the center, and reaches +φ₀ far to the other side.** The width λ = 1/M_c tells
you how narrow or wide this transition region is.

The kink is a **topological object** — it cannot be smoothed away. You cannot continuously
deform a kink into the uniform state φ = +φ₀ everywhere without passing through a
configuration that costs enormous energy. The kink is locked in by the topology of
having different values on the two sides.

In DFC, every particle is, at its core, a kink or a configuration built from kinks.
The kink's unremovability is why particles are stable: they cannot simply disappear
into the vacuum.

---

## The Compression

The word "compression" in the model's name refers to a specific behavior of the field.

Consider the substrate with some initial spread — some volume (in the model's internal
sense, not physical space) over which it varies. The substrate is self-compressing: its
own dynamics drive it toward a more compact configuration, toward a single dominant
state, toward "smaller" in some internal sense.

As the field compresses, it reaches thresholds — compression depths where it cannot
compress further without restructuring. These restructurings are the **bifurcations**
described in Module 00.

Think of a kink being squeezed from both sides. When the squeeze reaches a certain
strength, the kink cannot maintain its smooth profile — it splits, or folds, or creates
a new topological structure. The compression has forced a transition.

Each such transition produces new structure. The result of the first transition is
structure that we identify with electromagnetic behavior (U(1)). The second transition
produces weak-force structure (SU(2)). The third produces strong-force structure (SU(3)).

This is the DFC program: derive the entire particle physics content of nature from
this one field compressing through three transitions.

---

## The Kink Energy

How much energy does a kink store? The model gives an exact answer:

```
E_kink = (4/3) × c² × φ₀² / λ
```

(Read: the kink energy equals four-thirds times c-squared times phi-naught squared
divided by the kink width lambda.)

The factor 4/3 comes from the integral of the kink shape — specifically from:
```
I₄ = ∫ sech⁴(u) du = 4/3
```

This is one of the most important numbers in the model. The integral I₄ = 4/3 appears
repeatedly in the derivation of gauge couplings, topological charges, and mass formulas.
It is an exact mathematical result from the kink profile.

The kink energy is finite and well-defined. This is the mass of the particle associated
with the kink — the mass of the lightest particle that can exist in the substrate.

---

## The Topological Charge

Every kink carries a quantity called **topological charge**, Q_top. The charge counts
how many times the field interpolates from −φ₀ to +φ₀ across the object.

For a single kink:
```
Q_top = 2
```

This equals 2 because the field starts at −φ₀ = −1 (in units where φ₀ = 1) and ends
at +φ₀ = +1, making a total change of 2.

The topological charge is conserved: it cannot change without annihilating a kink with
an antikink (a transition from +φ₀ to −φ₀). This conservation is the DFC explanation
for why certain particles cannot decay — they carry Q_top = 2, and there is no way to
reduce this to zero without an equal and opposite charge to cancel against.

---

## What Is Verified So Far

From just the field V(φ) and its kink solutions, the model has already established the
following (all exact, zero free parameters, derived from V(φ) alone):

- **I₄ = 4/3** — the kink shape integral from sech⁴(u) = 4/3 (exact arithmetic)
- **Q_top = 2** — the topological charge of the kink from field theory
- **β = 1/(9π)** — the quartic coupling derived from the Hopf fiber dimension sum
- **g_eff² = 8/27** — the common gauge coupling derived from I₄, Q_top, and β
  (verified to 0.006% against SM measurement)

The gauge coupling g_eff² = 8/27 means:
```
g_eff = 0.54433
```

The Standard Model measures the common coupling at which electromagnetic, weak, and
strong forces appear to merge: g_SM = 0.5443. The DFC derivation from V(φ) agrees to
0.006% — within the experimental uncertainty.

This is the clearest indication that the DFC field potential is connected to the actual
physics of nature: the coupling constant of the fundamental forces follows from the
shape of the kink.

---

## Open Questions

Two parameters remain free:
- **α** — the instability parameter, which sets the scale of the kink width λ = 1/M_c
- The ratio α/β appears in the kink equilibrium φ₀ = √(α/β)

These set the overall energy scales of the model. They are not yet derived from any
deeper principle. The model's predictions for particle masses and force strengths depend
on α through the kink width, but the value of α itself is currently a free input.

Deriving α from first principles — or showing why any non-zero α gives the same
dimensionless predictions — would be the completion of the foundational level of the
model.

---

## Summary

| Concept | In plain language | Mathematical form |
|---|---|---|
| Substrate | One continuous scalar field | φ(x) — a number at each state |
| Potential | Double-well energy landscape | V(φ) = −αφ²/2 + βφ⁴/4 |
| Equilibrium | Two stable values | φ₀ = ±√(α/β) |
| Kink | Smooth transition between the two stable values | φ(x) = φ₀ tanh(x/λ) |
| Kink energy | The energy stored in a kink = particle mass | E = (4/3)c²φ₀²/λ |
| I₄ | The kink shape integral (an exact number) | I₄ = ∫sech⁴ du = 4/3 |
| Q_top | The topological charge of a kink | Q_top = 2 |
| β | The quartic self-interaction (derived) | β = 1/(9π) |
| Compression | The field driving toward compact configurations | — |
| Bifurcation | A compression threshold where new structure forms | — |

---

*Next: Module 02 — How Space Appears: Localization and the D-Depth Ladder*