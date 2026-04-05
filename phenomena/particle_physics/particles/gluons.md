# Particle: Gluons

## One-Sentence Synthesis

> Gluons are the eight massless connection fields of the D7 SU(3) closure — one per
> generator of SU(3) (3² − 1 = 8), each carrying a color-anticolor charge combination
> because the D7 connection transforms in the adjoint representation of SU(3), and
> their self-coupling (three-gluon and four-gluon vertices, absent in the photon)
> is the direct consequence of SU(3)'s non-Abelian structure, which causes confinement
> and asymptotic freedom — both structurally accounted for in DFC, neither yet derived
> from first principles of the substrate dynamics.

---

## Observed Properties

```
Mass:           0 (massless — no D6 squashing coupling, no Higgs interaction)
Spin:           1 (vector gauge field, connection 1-form)
Color charge:   yes — each gluon carries color-anticolor (octet representation)
Electric charge: 0
Weak charge:    0 (SU(2) singlet — no D6 winding)
Self-coupling:  yes — cubic and quartic vertices (non-Abelian)

Count:          8 (= dim adjoint of SU(3) = 3² − 1)
Color states:   8 independent color-anticolor combinations
Confinement:    yes — never observed as free particles
```

**Why massless:** Gluons are the gauge connection of an exact (unbroken) SU(3) color
symmetry. No Higgs mechanism operates on color charge — the D7 SU(3) closure is not
squashed. The 8 gluons remain massless.

**Why 8 (not 9):** SU(3) has 8 generators. The naive count of 3 colors × 3 anticolors
= 9 includes one color-singlet combination (rr̄ + gḡ + bb̄)/√3, which does not couple
to quarks and does not exist as an observable gluon. The 9th would be the generator
of U(1)_color, but U(1)_color is not a symmetry of QCD — the color group is SU(3), not
U(3). In DFC: the D7 closure has SU(3) topology (not U(3)), so there are exactly 8
connection fields.

---

## DFC Account

### Origin: D7 Connection Fields

The construction of gluons in DFC parallels the photon exactly, at a different depth:

**Photon (D5 U(1) closure):**
- At each point, the D5 fold orientation θ is independently defined
- Local U(1) symmetry → requires 1 connection field A_μ to compare orientations
- A_μ is the photon

**Gluons (D7 SU(3) closure):**
- At each point, the D7 color orientation is independently defined
- Local SU(3) symmetry → requires 8 connection fields G_μ^a (a = 1,...,8)
- G_μ^a are the 8 gluons

The argument is identical in structure. The difference is in the group:
- U(1) is Abelian → connection fields don't carry their own charge → photon is neutral
- SU(3) is non-Abelian → connection fields are in the adjoint representation → gluons
  carry color charge

### Why Gluons Carry Color (The Adjoint Representation)

The photon is the connection field of U(1). Under a gauge transformation U = e^{iα},
the photon transforms as:
```
A_μ → A_μ − ∂_μ α    [shifts, no color charge]
```

The gluons are the connection fields of SU(3). Under a local SU(3) transformation U(x):
```
G_μ → U G_μ U† + (i/g_s) (∂_μ U) U†
```

The first term (U G_μ U†) shows that gluons transform in the **adjoint representation**
of SU(3) — they rotate like color matrices, not like color vectors. This means gluons
carry color charge:

```
G_μ = G_μ^a T^a    [T^a are SU(3) generators, a = 1,...,8]
```

Each gluon G_μ^a is labeled by a generator T^a, which corresponds to a specific
color-anticolor combination. The eight generators of SU(3) in the adjoint representation
form the Gell-Mann matrices λ^a/2.

### The Non-Abelian Field Strength and Self-Coupling

The field strength tensor for gluons:
```
F_μν^a = ∂_μ G_ν^a − ∂_ν G_μ^a + g_s f^{abc} G_μ^b G_ν^c
```

The structure constants f^{abc} encode the non-commutativity of SU(3):
```
[T^a, T^b] = i f^{abc} T^c
```

The term g_s f^{abc} G_μ^b G_ν^c has no analogue in electromagnetism. It produces:
- **3-gluon vertex:** coupling ∝ g_s f^{abc}
- **4-gluon vertex:** coupling ∝ g_s² f^{abe} f^{cde}

These vertices make gluons interact with each other — unlike photons, which do not
couple to themselves at tree level.

**In DFC:** the f^{abc} structure constants are determined by the SU(3) algebra at D7.
The self-coupling is a consequence of the D7 closure topology having a non-commutative
structure. This is not introduced separately — it is the defining property of the
non-Abelian group structure that the D7 closure produces.

### Confinement: Why Gluons Are Never Free

The gluon self-attraction causes color field lines to collapse into flux tubes rather
than spreading outward:

```
D5 photon:    field lines spread → E ∝ 1/r² → V(r) = −α/r     [long range]
D7 gluon:     field lines collapse → σ = const. → V(r) = σr    [confinement]

σ ≈ 1 GeV/fm = 0.18 GeV²    [string tension from lattice QCD]
```

At separation r ~ 1/Λ_QCD ≈ 1 fm, the potential reaches ~1 GeV. At this point the field
energy is sufficient to create a new quark-antiquark pair from the vacuum — the string
breaks and two new hadrons form. Color is never observed outside a hadron.

**DFC structural account:** The D7 SU(3) closure topology does not support isolated
color charge in the D3 localization behavior. Any isolated D7 winding number must be
compensated by an equal and opposite winding within the localization range of the
D7 closure. This is why quarks and gluons are confined — not as a law imposed from
outside, but as a topological necessity of the D7 closure structure.

**What is not yet derived:** The precise calculation that shows isolated D7 winding
is topologically unstable — that it either must collapse (pulling the compensating
closure with it) or must produce a new closure pair (quark-antiquark creation). This
requires the full nonlinear D7 compression field theory, which is not yet formalized.
The string tension σ ≈ 1 GeV/fm is not predicted from DFC — it is observed.

### Asymptotic Freedom: Why Gluons Weaken at Short Distance

The running of the strong coupling constant:
```
α_s(μ) = α_s(M_Z) / (1 + (b₀/2π) α_s(M_Z) ln(μ/M_Z))

b₀ = 11 − 2n_f/3    [one-loop beta function coefficient]
   = 11 − 2(6)/3 = 7    [for n_f = 6 active quark flavors]
```

Since b₀ > 0 for n_f < 16.5: as μ increases (shorter distances), α_s decreases.
This is asymptotic freedom.

**DFC structural account:** At high energies (probing the substrate at short distances),
the color orientation comparison samples the D7 closure topology at shorter scales.
At shorter scales than the closure radius, the SU(3) structure is less fully formed —
the coupling is weaker. This is the DFC reinterpretation of asymptotic freedom:
high-energy probes see the D7 structure before it has fully closed.

**What is not yet derived:** The beta function coefficient b₀ = 7 from DFC geometry.
In the SM it is computed from the gauge field content (11 from gluon loops, −2n_f/3
from quark loops). In DFC, this requires computing the density of virtual D7 closure
fluctuations at a given energy scale from the substrate dynamics.

---

## Connection to the S-Matrix (Priority Bottleneck)

The primary path from DFC to verifiable S-matrix predictions runs through the gluon
sector:

**Nearest computable observable:** The ratio R in e⁺e⁻ → hadrons vs. e⁺e⁻ → μ⁺μ⁻:
```
R = σ(e⁺e⁻ → hadrons) / σ(e⁺e⁻ → μ⁺μ⁻) = 3 Σ_f Q_f²
```

where the factor 3 is the number of color states and Q_f is the quark electric charge.
This is currently a qualitative DFC prediction (product topology gives 3 color states),
but to make it a calculation rather than a consistency check requires computing the
e⁺e⁻ → qq̄ → hadrons cross-section from the D5 × D7 coupling structure.

**Path to a DFC S-matrix calculation:**
1. Express the quark-gluon vertex from the D7 overlap with the D5 field (already implicit
   in the gauge coupling structure)
2. Write the Feynman rules from the D7 field strength (F_μν^a above)
3. Compute a tree-level gluon exchange diagram from first principles
4. Verify that the result matches QCD (it should, if the D7 → SU(3) correspondence is correct)

This would be the first genuine S-matrix prediction from DFC substrate dynamics,
moving the completeness estimate from ~10% toward ~25%.

---

## Formal Equations

### QCD Lagrangian (D7 Connection Fields)

```
L_QCD = −(1/4) F_μν^a F^{μν a} + Σ_f q̄_f (iγ^μ D_μ − m_f) q_f

D_μ = ∂_μ − i g_s G_μ^a T^a    [covariant derivative]

F_μν^a = ∂_μ G_ν^a − ∂_ν G_μ^a + g_s f^{abc} G_μ^b G_ν^c

g_s² / (4π) = α_s(M_Z) = 0.1182    [observed]
```

### Color Algebra

```
SU(3) generators: T^a = λ^a / 2   (λ^a = Gell-Mann matrices)
Structure constants: [T^a, T^b] = i f^{abc} T^c
Quadratic Casimir: T^a T^a = (4/3) × I   [for quarks, fundamental rep]
Adjoint Casimir:   f^{acd} f^{bcd} = 3 δ^{ab}   [for gluons]
```

### Asymptotic Freedom Running

```
α_s(μ) = 2π / (b₀ ln(μ/Λ_QCD))    [one-loop, μ ≫ Λ_QCD]

b₀ = 11 − 2n_f/3 = 7    (n_f = 6)
Λ_QCD ≈ 200 MeV

α_s(M_Z = 91.2 GeV)  = 0.1182    ✓
α_s(1 GeV)           ≈ 0.5
α_s → 0 as μ → ∞     (asymptotic freedom)
α_s → ∞ as μ → Λ_QCD (confinement onset)
```

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| 8 gluons | dim(SU(3)) = 3²−1 = 8, D7 closure | 8 ✓ | Structural ✓ |
| Massless | Unbroken D7 SU(3), no S³ squashing | 0 ✓ | Structural ✓ |
| Spin 1 | D7 connection 1-form | 1 ✓ | Structural ✓ |
| Color-charged | Adjoint representation of D7 SU(3) | Yes ✓ | Structural ✓ |
| Self-coupling | Non-Abelian f^{abc} structure constants | 3-gluon, 4-gluon vertices ✓ | Structural ✓ |
| Confinement | No isolated D7 winding in D3 localization behavior | No free quarks/gluons ✓ | Structural (not derived) |
| Asymptotic freedom | High-energy probes see sub-closure scale | α_s(M_Z) = 0.1182 ✓ | Structural (not derived) |
| α_s not derived | g_s remains SM input | Input | OPEN |
| Λ_QCD not derived | Confinement scale from dynamics | 200 MeV | OPEN |

---

## Open Questions

1. **Derive the strong coupling constant g_s from DFC geometry.** The value α_s(M_Z) = 0.1182
   is currently an input. In DFC, it should be determined by the D7 closure geometry — the
   ratio of the closure radius to the kink width, or equivalently the overlap of the D7
   connection field with the quark zero mode wavefunction. This is the D7 analog of
   deriving the Weinberg angle from the D5/D6 geometry ratio.

2. **Derive Λ_QCD from the substrate dynamics.** The confinement scale Λ_QCD ≈ 200 MeV is
   where α_s diverges. In DFC, this is the scale at which the D7 closure topology becomes
   strongly coupled — where the non-Abelian self-interaction of the gluon fields starts
   dominating. Whether Λ_QCD can be derived from (α, β, c, d_7) is an open quantitative
   problem.

3. **First DFC S-matrix calculation.** The path to computing a gluon exchange diagram
   from DFC substrate dynamics is laid out above. Even a tree-level calculation of
   quark-quark scattering via gluon exchange — verifying it reproduces the QCD result
   — would be the first genuine S-matrix prediction from DFC. This should be a high-priority
   target. See the S-matrix section above.

4. **Derive confinement from topology.** The argument that isolated D7 winding is forbidden
   needs to be made precise. Specifically: show that the D7 compression field energy is
   minimized only for color-neutral configurations, and that the energy cost of separating
   color charge grows linearly with distance from the D7 closure dynamics. This is related
   to the Yang-Mills mass gap problem (Clay Millennium Prize).

---

## Connections

- **Strong force** — full account of D7 SU(3) gauge structure, confinement, asymptotic freedom;
  `phenomena/particle_physics/forces/strong_force.md`
- **Quarks** — gluons couple to quark color charge; color singlet formation;
  `phenomena/particle_physics/particles/quarks.md`
- **Nuclear binding** — residual D7 interaction between color-neutral nucleons;
  `phenomena/particle_physics/nuclear_binding.md`
- **Proton stability** — gluons confined to D7, cannot bridge to D5/D6;
  `phenomena/particle_physics/proton_stability.md`
