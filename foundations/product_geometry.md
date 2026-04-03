# Product Geometry: The Most Consequential Structural Choice

## The Question

When you say "the three forces come from extra dimensions," you have to answer: *how are those
extra dimensions arranged?* Are they one combined space? Or separate spaces sitting next to each
other?

The answer completely changes the physics.

---

## Option A: Simple Group Unification (the standard approach)

Grand unified theories like SU(5) or SO(10) say: at high energies, there is *one* force with *one*
symmetry group. As the universe cools, that symmetry breaks into three pieces — the electromagnetic,
weak, and strong forces emerge as fragments of the original unified force.

In geometric language: the extra dimensions form a single, connected space. All three forces live
in the same room. At high energies they are indistinguishable; at low energies they separate.

**Mathematical signature:** A *simple* gauge group — one that cannot be written as a direct product
of smaller groups.

**Examples:** SU(5), SO(10), E₆, E₈×E₈

---

## Option B: Product Geometry (this model)

In this model, the three forces come from three *separate* geometric spaces, multiplied together:

```
Total internal space = U(1) × S³ × SU(3)
                        EM    Weak  Strong
```

These spaces coexist at every point but they do not interact through force carriers. There is no
common "room" — there are three separate rooms at every address in spacetime.

**Mathematical signature:** A *product* gauge group: U(1) × SU(2) × SU(3)

This is exactly the gauge group of the Standard Model — no unification required.

---

## Why This Choice Matters: Proton Stability

This is the most important physical consequence of the product structure.

In a simple unified group like SU(5), the large symmetry contains force carriers called **X and Y
bosons**. These bosons simultaneously couple to:
- The color (strong force) sector
- The electromagnetic sector

This means they can mediate a process where a quark turns into a lepton. And if quarks can turn
into leptons, a proton (made of three quarks) can decay.

The predicted proton lifetime in minimal SU(5):

```
τ_proton ~ 10^30 years      (minimal SU(5), already ruled out)
τ_proton ~ 10^34-36 years   (supersymmetric SU(5), under pressure from experiments)
```

The current experimental lower bound (Super-Kamiokande):

```
τ(p → π⁰ + e⁺) > 1.6 × 10^34 years
```

Every version of simple group unification is in tension with proton decay experiments, and the
tension gets worse with each new measurement.

**In the product geometry, there are no X or Y bosons.** There is no force carrier that
simultaneously lives in the color space AND the electromagnetic space. The two fibers are separate
rooms. A quark physically cannot turn into a lepton through any gauge interaction — period.

The proton is absolutely stable to all orders in perturbation theory.

The only decay channels are:
- Gravitational tunneling: τ > 10^44 years
- Exotic quantum gravity effects: τ > 10^44 years

Both are ten billion times longer than the experimental bound. The model is safe from all current
and foreseeable proton decay experiments.

---

## The Trade-Off

Simple group unification has an elegance the product structure lacks: one force, one coupling, one
dimensionless number at the unification scale. The product model gives up that elegance.

What does the product model gain?

1. **Proton stability** — absolute, not approximate
2. **A more rigid geometric foundation** — the geometry of U(1) × S³ × SU(3) is more tightly
   constrained than an arbitrary SU(5) potential, leaving fewer free parameters
3. **The observed gauge group as a theorem** — the Standard Model gauge group is not "chosen"; it
   is the product of the three simplest geometries that can carry U(1), SU(2), and SU(3) symmetry

---

## How Coupling Constants Unify Without a Simple Group

Objection: "In SU(5), the three coupling constants converge to one value at high energy. This is
beautifully confirmed (approximately) by experiment. If you don't have a simple group, how do you
explain the convergence?"

Answer: In this model, the three coupling constants are determined by the *sizes* of the three
force closure structures. As you go to higher energies (shorter distances), you probe the
underlying closure geometry more directly. The convergence is not towards a single coupling
constant but towards a single **squashing parameter** — a dimensionless ratio that describes how
much the internal structure is deformed from its maximally symmetric configuration.

At the closure scale (the energy at which the folding structure was stabilized), all three
effective couplings become functions of this single parameter. The observed convergence is real;
its interpretation is geometric rather than group-theoretic.

See `../equations/gauge_couplings.py` for the numerical implementation.

---

## Comparison Summary

| Feature | Simple Group (SU(5)) | Product Geometry (this model) |
|---|---|---|
| Gauge group at high E | Single, unified | Product of three |
| X, Y bosons | Yes | No |
| Proton decay | Predicted, constrained | Forbidden by structure |
| Coupling unification | At a single point | Via squashing parameter |
| Free parameters | 1 (unified coupling) | 1 (squashing ratio) |
| Elegance | One group | Three separate geometries |
| Experimental status | Pressured by proton decay limits | Consistent with all data |
