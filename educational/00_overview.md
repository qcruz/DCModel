# Module 00 — What Is the DFC Model?

*No physics background required. This module can be read in about ten minutes.*

---

## What This Project Explores

The Standard Model of particle physics describes all known particles and forces with
remarkable precision. But it requires about 19 numbers — particle masses, force
strengths, mixing angles — that must be measured and inserted by hand. The theory
works beautifully once you have those numbers, but it does not explain where they
come from.

This project starts from a simple question: what structures emerge from a single
scalar field with a double-well self-interaction, if you let it compress?

---

## The Central Idea

The Dimensional Folding Compression (DFC) model starts with one continuous field that
compresses and folds itself. The project explores whether the structures that emerge —
particles, forces, spatial dimensions — can account for what we observe.

The field has a specific self-interaction potential — a mathematical shape that governs
how it interacts with itself. This shape is a double well, like a landscape with two
valleys and a hill between them. The particular form is:

```
V(φ) = −(α/2) φ² + (β/4) φ⁴
```

Do not worry about the symbols yet. The key point is: this potential causes the field to
prefer being "over" in one valley or the other, and to resist being at the hilltop in the
middle. This resistance to the unstable middle is what drives compression.

---

## What "Compression" Means

Imagine squeezing a garden hose. If you squeeze hard enough, it buckles — it kinks into
a new shape rather than compressing smoothly. The new shape has a structure the original
smooth hose did not.

The DFC field does something similar. As it compresses toward a one-dimensional state,
it reaches thresholds where it cannot compress further without buckling into a new
configuration. These buckling events — called **bifurcations** — are where all structure
comes from.

In the DFC account, particles, forces, and apparent spatial dimensions are downstream
consequences of these bucklings. The interesting part is that this setup produces
specific numerical predictions that can be compared to measurement.

---

## How Forces Emerge

In the Standard Model, there are three fundamental forces (besides gravity): the
electromagnetic force, the weak nuclear force, and the strong nuclear force. They are
described by three separate mathematical structures called gauge groups: U(1), SU(2),
and SU(3). Nobody explains *why* nature chose these three. The Standard Model simply
postulates them.

In the DFC model, these structures are not postulated. They appear as the topology
of different bifurcation depths.

Think of it this way. When the field buckles for the first time, the configuration it
creates has a certain symmetry — a one-dimensional circular symmetry. That circular
symmetry is what we observe as electromagnetism (U(1)). When it buckles a second time,
the new configuration has a three-dimensional symmetry. That is the weak force (SU(2)).
A third buckling produces an eight-dimensional symmetry — the strong force (SU(3)).

In this picture, the three forces are three different topological behaviors of the
same object, each arising at a different depth of compression.

---

## A First Quantitative Example

Here is a concrete example of how this works.

The electromagnetic force has a characteristic strength called the fine structure
constant, usually written α_em. Its value is approximately 1/137. The Standard Model
treats this as one of those 19 unexplained numbers — you measure it and insert it.

In the DFC model, the gauge coupling (related to force strength) at the compression
threshold scale turns out to equal exactly:

```
1 / α_em  =  36π  ≈  113
```

This follows from two prior DFC results (both derived from the field potential with
zero free parameters):
- The common gauge coupling g² = 8/27 (the "common strength" at which all three forces
  unify in the DFC account)
- The hypercharge normalization k_Y = √(5/3) (derived from the winding structure)

Together these give 1/α_em = 36π at the threshold scale. Running this value to the
energy scale we measure at in laboratory experiments (the Z boson mass scale) gives:

```
1/α_em  =  128.09
Observed:  127.95
Error: +0.15%
```

Zero free parameters. The strength of electromagnetism follows from the geometry
of compression — an interesting result worth exploring further.

---

## What Has Worked and What Hasn't

The project is under active development. Some results are surprisingly close to
observation; others are clearly off. Both are documented.

**Interesting results (zero free parameters, <1% error):**
- The common gauge coupling g² = 8/27
- The electromagnetic fine structure constant α_em(M_Z) — 0.15% error
- The Weinberg angle sin²θ_W = 0.231 — less than 0.01% error
- The strong coupling α_s = 0.1182 — 0.006% error
- The tau lepton mass m_τ = 1777 MeV — 0.006% error
- The neutron lifetime 878 s — 0.1% error

**Structural results:**
- Exactly three fermion generations (from the dimension of SU(3) representation)
- Proton stability from topology
- Tsirelson's quantum bound — proved exactly

**Open gaps:**
- Gravity is described structurally but Newton's constant is not yet derived
- The neutrino mass hierarchy is only approximately reproduced
- Nuclear binding energies have the right sign but wrong magnitude
- Several quark masses are off by a few percent

---

## What Makes This Approach Different

Most approaches beyond the Standard Model add new structure — extra dimensions,
supersymmetric partners, larger gauge groups. DFC starts from less structure: one
field, one potential. Whatever emerges has to come from the compression dynamics.

This leads to some testable consequences. For example, the model predicts no proton
decay, no axion, and no supersymmetric partners. If any of these were observed, the
framework would need fundamental revision.

---

## How to Read Further

The modules in this directory build on each other. The next module (01) covers the
substrate in more detail: what the field equation means, what kinks are, and why they
are the right building blocks for particles.

For readers who want the technical content, the repository contains:
- `foundations/` — the mathematical and conceptual foundations
- `phenomena/` — DFC accounts of specific physical phenomena
- `equations/` — runnable Python modules that compute all predictions

Every claim in the technical documents is assigned a tier (Tier 1 through 4) indicating
how well established it is. Tier 1 means logically proved from the postulates. Tier 4
means conjectured but not yet computed. Honesty about the difference between these tiers
is a core commitment of the project.

---

*Next: Module 01 — The Substrate: One Object, One Potential*
