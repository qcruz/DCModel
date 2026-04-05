# Phenomenon: Electromagnetism

## One-Sentence Synthesis

> Electromagnetism is the physics of the connection field that arises from the D5 U(1)
> closure: when the fold orientation angle θ is a local symmetry (independently defined
> at each point in space), a vector potential A_μ exists as the mathematical object
> required for comparing phases at neighboring points, and Maxwell's equations are the
> minimal self-consistent dynamics for that connection.

---

## Observation

Electric charges attract or repel with force F = kq₁q₂/r². Moving charges create
magnetic fields. Changing magnetic fields induce electric fields. Together, E and B fields
propagate as electromagnetic waves at speed c. The force is infinite-range. Maxwell's
four equations describe all classical electromagnetic phenomena with complete precision.
The photon mediates the force quantum mechanically.

---

## Standard Explanation

U(1) gauge theory. Gauge invariance of the electron field ψ → e^{iα(x)} ψ requires
introducing a vector potential A_μ with transformation A_μ → A_μ + ∂_μ α. The field
strength F_μν = ∂_μ A_ν − ∂_ν A_μ is gauge-invariant. The Maxwell Lagrangian
L = −¼ F_μν F^μν gives Maxwell's equations. The photon is massless because a mass
term m² A_μ A^μ would break gauge invariance.

This derivation is correct and predictively complete. What it does not explain is why
the electron has a local phase symmetry in the first place.

---

## Dimensional Folding Explanation

### Why There Is a Local Phase Symmetry

In DFC, the fold orientation angle θ(x,t) is the quantum phase — the direction the
compression fold points in its transverse plane at each spacetime point. It is physically
identified as the U(1) winding angle of the D5 closure (see `phenomena/light/light.md`,
`foundations/product_geometry.md`).

A key property of the D5 closure: the fold orientation θ is **defined independently at
each point in space**. The D5 closure topology at point x has no rigid connection to the
D5 closure topology at point y. They are separate closure events at each location.

This means the absolute value of θ(x) is unobservable — there is no physical meaning to
"the fold orientation here is 30° more than over there" unless we have a way to transport
and compare phases. Only **phase differences** (relative orientations between nearby
points) have physical content.

This is gauge symmetry — not as a postulate, but as a physical consequence of the D5
closure being independently defined at each spatial location.

### Why A_μ Must Exist

Once θ(x) is a local symmetry, a problem arises: how does the compression field equation
know how to compare field values at neighboring points?

The ordinary derivative ∂_μ ψ of a matter field ψ = |ψ| e^{iθ(x)} is not gauge-invariant
— it mixes the physical amplitude |ψ| with the unphysical phase variation ∂_μ θ. To
write a physically meaningful field equation, we need a **covariant derivative** that
subtracts off the local phase variation:

```
D_μ ψ = (∂_μ − ie A_μ) ψ
```

The field A_μ is the **connection** — the object that tells you how to parallel-transport
the phase θ from one point to another. It is defined as the locally-varying phase
reference against which ∂_μ θ is measured.

A_μ is not an independent variable introduced by hand. It is the **necessary mathematical
consequence** of θ being a local symmetry. You cannot write a consistent field equation
for a locally-phased field without it.

Under a local phase transformation θ(x) → θ(x) + α(x), consistency requires:
```
A_μ → A_μ + (1/e) ∂_μ α     [gauge transformation]
```

This is the electromagnetic gauge transformation — derived from the local nature of θ,
not postulated.

### The Field Strength and Maxwell's Equations

The **curvature** of the connection A_μ — how much the phase rotates when you
parallel-transport around a closed loop — is the physically observable quantity:

```
F_μν = ∂_μ A_ν − ∂_ν A_μ     [field strength tensor]
```

F_μν is gauge-invariant (the ∂_μ α terms cancel). Its components are:
```
F_{0i} = E_i / c     [electric field components]
F_{ij} = −ε_{ijk} B_k    [magnetic field components]
```

The **dynamics** of A_μ — how it propagates through space — is fixed by asking: what
is the simplest gauge-invariant action for A_μ? The answer is the Maxwell Lagrangian:

```
L_EM = − (1/4) F_μν F^μν
```

This is the unique lowest-order gauge-invariant kinetic term. No additional variables
are introduced. The Euler-Lagrange equations of L_EM give Maxwell's equations directly.

---

## Formal Derivation of Maxwell's Equations

### Setup

The full Lagrangian (matter field + EM field):
```
L = |D_μ ψ|² − V(|ψ|²) − (1/4μ₀) F_μν F^μν
```

where D_μ = ∂_μ − ie A_μ, V is the matter potential, and μ₀ is the permeability of
free space.

### Equations of Motion for A_μ

Varying L with respect to A_ν gives the Euler-Lagrange equation:
```
∂_μ F^μν = μ₀ J^ν
```

where J^ν = (cρ, J) is the 4-current (charge density ρ and current density J).

In component form, this gives two of Maxwell's four equations:

```
∇·E = ρ/ε₀               [Gauss's law]
∇×B − (1/c²)∂E/∂t = μ₀J  [Ampere-Maxwell law]
```

### Bianchi Identity

The other two Maxwell equations follow automatically from the antisymmetry of F_μν —
they are geometric identities, not equations of motion:

```
∂_[μ F_νρ] = 0

→  ∇·B = 0                [no magnetic monopoles]
→  ∇×E + ∂B/∂t = 0       [Faraday's law]
```

**All four Maxwell equations follow from one gauge-invariant Lagrangian.** ✓

### Why the Photon Is Massless

A mass term for A_μ would take the form:
```
L_mass = (1/2) m² A_μ A^μ
```

Under a gauge transformation A_μ → A_μ + (1/e)∂_μ α:
```
A_μ A^μ → A_μ A^μ + (2/e) A^μ ∂_μ α + (1/e²)(∂_μ α)²  ≠  A_μ A^μ
```

The mass term is not gauge-invariant. It would destroy the local phase symmetry — the
very structure that requires A_μ to exist.

In DFC: A_μ is massless because the fold orientation θ has no geometrically distinguished
value — no stable minimum like the Higgs field at D6. There is no "mass" for the phase
connection because the phase itself is arbitrary. The masslessness is topological: U(1)
is a circle — homogeneous, with no geometrically distinguished point.

### Why the Force Falls as 1/r²

The potential between two charges at separation r is determined by the propagator of the
massless A_μ field. For a massless field propagating through the substrate's three apparent spatial degrees of freedom:

```
G(r) = 1/(4πr)     [Green's function of ∇² in 3D]

V(r) = q₁ q₂ / (4πε₀ r) = k q₁ q₂ / r     [Coulomb's law] ✓
```

The 1/r dependence and 1/r² force is a direct consequence of the photon being massless
propagating through three apparent spatial degrees of freedom. If the photon had mass m, the potential would
become the Yukawa form V(r) ∝ exp(−mr/ℏc)/r — exponentially suppressed beyond the
Compton wavelength ℏc/m. The weak force (massive W/Z) behaves this way.

### Magnetic Fields as Relativistic Electricity

Magnetism has no independent existence in DFC. A magnetic field observed in one inertial
frame is a purely electric field in a relatively-moving frame. From the Lorentz
transformation of the F_μν tensor:

```
E'_⊥ = γ(E_⊥ + v × B)
B'_⊥ = γ(B_⊥ − v/c² × E)
```

A wire carrying current (moving charges) creates a magnetic field for a stationary
observer. For an observer moving with the current, those same charges are at rest — the
force is purely electric. The two descriptions are related by a Lorentz boost.

In DFC: this follows directly from the Lorentz covariance of the compression field
equation and the identification of E and B as components of the gauge-invariant F_μν
tensor (see `phenomena/gravity/special_relativity.md`).

---

## The Full Derivation Chain — What Introduces What

| Object | Origin | What it describes |
|---|---|---|
| φ (scalar field) | Compression field | Matter — kinks, closures |
| θ(x) | Fold orientation angle at each point | Local U(1) phase |
| Local θ symmetry | D5 closure independently defined at each point | Gauge symmetry |
| A_μ | Required by local θ symmetry | Connection — how to compare phases |
| F_μν = ∂_μA_ν − ∂_νA_μ | Curvature of A_μ | Observable EM field strength |
| E, B | Components of F_μν | Electric and magnetic fields |
| Maxwell's equations | Euler-Lagrange of L = −¼F_μνF^μν | Dynamics of A_μ |
| Photon | Massless excitation of A_μ | Gauge boson — carries EM interaction |
| Charge e | U(1) winding number at D5 | Coupling strength between φ and A_μ |
| Coulomb 1/r² | Massless propagator in 3D | Range of EM force |

No variable introduced without a reason. Each entry follows from the one above it.

---

## Connections to Other Phenomena

- **Light** — photon as massless A_μ excitation; polarization = fold orientation θ;
  E = hν from massless dispersion; `phenomena/light/light.md`
- **Electric charge** — U(1) winding number at D5; quantization from topology;
  `phenomena/electromagnetism/electric_charge.md`
- **Special relativity** — F_μν is a Lorentz tensor; magnetism is relativistic electricity;
  `phenomena/gravity/special_relativity.md`
- **Electroweak unification** — D5 U(1) and D6 SU(2) as adjacent independent closures;
  the same logic gives W_μ^a at D6;
  `phenomena/particle_physics/forces/electroweak.md`
- **Quantum mechanics** — covariant derivative D_μ = ∂_μ − ieA_μ enters Schrödinger
  equation as minimal coupling; `phenomena/quantum/quantum_mechanics.md`
- **Product geometry** — U(1) independence from SU(2) and SU(3); `foundations/product_geometry.md`

---

## Open Questions

1. **Derive the fine structure constant α ≈ 1/137:** The electromagnetic coupling
   strength e (equivalently α = e²/4πε₀ℏc ≈ 1/137) should be determined by the
   geometry of the U(1) closure at D5 — the winding density of the D5 topology per
   unit compression volume. This is the most important open quantitative prediction in
   the EM sector; the Standard Model takes α as a measured input.

2. **Derive the Maxwell Lagrangian as uniquely minimal:** The argument above identifies
   L = −¼F_μνF^μν as the lowest-order gauge-invariant kinetic term. A rigorous DFC
   derivation would show it is the unique operator constructible from the D5 connection
   at the relevant energy scale, ruling out higher-dimension operators (F⁴, etc.) as
   subleading — connecting the Lagrangian to the compression field's expansion in powers
   of the field amplitude.

3. **Non-Abelian extension to D6 and D7:** The same local-symmetry structure that produces
   A_μ at D5 produces W_μ^a (a=1,2,3) at D6 and G_μ^a (a=1,...,8) at D7. Non-Abelian connections
   self-interact (gluons attract gluons; W bosons attract W bosons) because the
   non-Abelian field strength F_μν^a = ∂_μA_ν^a − ∂_νA_μ^a + f^{abc}A_μ^bA_ν^c
   contains cubic and quartic terms in A. Deriving the self-coupling structure from the
   DFC D6/D7 local symmetry would complete the full gauge sector.

4. **Magnetic monopoles:** The Bianchi identity ∇·B = 0 follows from F = dA being
   exact. In DFC, this would correspond to the U(1) closure having no topological
   defects. However, the global topology of U(1) does admit Dirac monopoles as solitonic
   solutions. Whether the D5 closure topology in DFC permits or excludes these — and
   what the predicted monopole mass would be — is an open question with direct
   experimental consequences.
