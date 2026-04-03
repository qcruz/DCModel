# The 16-Dimensional Setup and Compactification

## The Full Space

The complete space of this model is:

```
M^16 = M^4 × U(1) × S³ × SU(3)
```

Where:
- **M^4** = 4-dimensional Minkowski spacetime (what we observe directly)
- **U(1)** = a circle, 1 real dimension, carries electromagnetism
- **S³** = a 3-sphere, 3 real dimensions, carries the weak force
- **SU(3)** = the group manifold of SU(3), 8 real dimensions, carries the strong force

Dimension count: 4 + 1 + 3 + 8 = **16 total**

---

## What "Compactified" Means

The extra twelve dimensions are not missing — they are present at every point in spacetime. They
are simply very, very small.

**Analogy:** A tightrope viewed from 100 meters away looks like a 1-dimensional line. From 1
centimeter away, you can see it is a 3D cylinder. The extra "circular" dimension exists everywhere
along the rope but is invisible at long distances.

In this model, there are 12 extra shapes attached to every point in spacetime. They are invisible
not because they don't exist but because they are ~10^-35 meters across — far below any probe.

---

## The Three Fibers in Detail

### Fiber 1: U(1) — The Electromagnetic Circle

- **Shape:** A circle, S¹
- **Dimension:** 1
- **Radius:** R_EM ~ 10^-35 m (order of magnitude)
- **Symmetry group it generates:** U(1) — the symmetry of electromagnetism
- **Force carried:** Electromagnetism, mediated by photons
- **Charge:** The winding number around the circle. Integer winding = integer electric charge.

**Intuition:** Imagine a particle traveling around the circle. If it must return to exactly where
it started (periodic boundary conditions), only certain wavelengths fit — these are the quantized
values of electric charge. Charge quantization is a geometric fact about circles.

### Fiber 2: S³ — The Weak Force Sphere

- **Shape:** A 3-sphere (the surface of a 4-dimensional ball)
- **Dimension:** 3
- **Radius:** R_weak ~ 10^-35 m (roughly similar to R_EM; ratio determines mixing angle)
- **Symmetry group it generates:** SU(2) — the symmetry group of the weak force
- **Force carried:** Weak interactions, mediated by W⁺, W⁻, Z⁰
- **Higgs mechanism:** The *squashing* of this sphere from perfectly round to ellipsoidal

**Key fact:** S³ is isomorphic as a manifold to the group SU(2). This means the group of rotations
of the 3-sphere IS the weak force symmetry group. The geometry and the physics are the same object.

**Intuition:** A perfectly round S³ has full SU(2) symmetry — all three weak bosons are massless.
When the sphere gets "squashed" in one direction (compressed into an ellipsoid), one axis is
preferred, one symmetry is broken, and the W and Z bosons acquire mass. This is the Higgs mechanism
without a Higgs field — just a shape change. See `04_higgs_geometry.md`.

### Fiber 3: SU(3) — The Strong Force Manifold

- **Shape:** The group manifold of SU(3) itself
- **Dimension:** 8
- **Symmetry groups it generates:** TWO copies of SU(3) — left multiplication and right multiplication
  - Left copy → color symmetry (the strong force, gluons)
  - Right copy → flavor symmetry (the three generations)
- **Force carried:** Strong interaction, mediated by 8 gluons
- **Generation number:** The fundamental representation of SU(3) is 3-dimensional → exactly 3 generations

**This is the crucial fiber.** By using SU(3) as its own fiber, the model gets double duty:
the same geometric object generates both the strong force AND the reason there are three matter
families. See `03_three_generations.md`.

---

## The Scale Hierarchy

Why are the extra dimensions so much smaller than observable scales?

The relevant scales:

```
Observable universe:    ~10^26 m
Human scale:            ~1 m
Atomic scale:           ~10^-10 m
Nuclear scale:          ~10^-15 m
Electroweak scale:      ~10^-19 m     (probed at the LHC)
Compactification scale: ~10^-34 m     (the extra dimensions live here)
Planck scale:           ~1.6×10^-35 m (quantum gravity regime)
```

The gap between the electroweak scale (~10^-19 m) and the compactification scale (~10^-34 m) is
a factor of ~10^15. This is related to the hierarchy problem — why is the Higgs mass (electroweak
scale) so much lighter than the Planck scale? In this model, the Higgs mass is a radiative
correction to a geometric modulus, which partially addresses the hierarchy problem.

---

## Kaluza-Klein Towers

In any compactified extra dimension, fields propagating in that dimension have a tower of heavier
"echoes" — the Kaluza-Klein (KK) modes. For a circle of radius R, the KK masses are:

```
m_n = n × ℏc / R,    n = 0, 1, 2, 3, ...
```

For R ~ 10^-35 m:
```
m_KK ~ ℏc / (10^-35 m) ~ 10^19 GeV  ≈  M_Planck
```

The first KK excitations are at Planck-scale energies — completely inaccessible to any foreseeable
collider experiment. This explains why the extra dimensions have not been directly detected: their
signatures only appear at energies ~10^15 times higher than the LHC.

---

## Notation Reference

| Symbol | Meaning | Value |
|---|---|---|
| R_EM | Radius of U(1) fiber | ~10^-35 m (order) |
| R_W | Radius of S³ fiber | ~10^-35 m (order) |
| R_S | Size scale of SU(3) fiber | ~10^-35 m (order) |
| ε | Squashing parameter of S³ | ~0.23 (electroweak mixing angle related) |
| η | Squashing parameter of SU(3) | sets flavor breaking scale |
| M_c | Compactification scale | R^-1 × ℏc ~ 10^16-19 GeV |
| M_Pl | Planck mass | 1.22 × 10^19 GeV |

The precise values of R_EM, R_W, R_S are not free parameters to be measured independently —
they are related to the observed coupling constants g₁, g₂, g₃ of the Standard Model.
