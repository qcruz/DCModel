# Phenomenon: Quarks

## One-Sentence Synthesis

> Quarks are compression-field kinks that reach D7 (the SU(3) color closure) in addition
> to D5 and D6 — their color charge is the D7 winding orientation in the 3-dimensional
> fundamental representation of SU(3), their fractional electric charges follow from the
> D7 color triplet distributing the D5 hypercharge across three states (giving Y = 1/3
> rather than the lepton value Y = −1), their spin-1/2 comes from the Jackiw-Rebbi zero
> mode at D7, and their confinement reflects that isolated D7 winding configurations
> have no stable D3 realization — only color-neutral combinations close.

---

## Observation

Six quark flavors, arranged in three generations of two isospin partners:

| Flavor | Mass | Q | T₃ | Color | Generation |
|---|---|---|---|---|---|
| up (u) | 2.2 MeV | +2/3 | +1/2 | r/g/b | 1 |
| down (d) | 4.7 MeV | −1/3 | −1/2 | r/g/b | 1 |
| charm (c) | 1.27 GeV | +2/3 | +1/2 | r/g/b | 2 |
| strange (s) | 96 MeV | −1/3 | −1/2 | r/g/b | 2 |
| top (t) | 173 GeV | +2/3 | +1/2 | r/g/b | 3 |
| bottom (b) | 4.18 GeV | −1/3 | −1/2 | r/g/b | 3 |

Defining features:
- Never observed in isolation — only in color-neutral bound states (hadrons)
- Fractional electric charges: +2/3 or −1/3 (no other elementary particle has these)
- Carry color charge (red, green, or blue) — the only particles to do so
- Couple to all three gauge forces (D5, D6, D7)
- Mass range spans ~80,000× from up quark to top quark

---

## Standard Explanation

Quarks are fundamental spin-1/2 fermions in the SM charged under SU(3)_c × SU(2)_L × U(1)_Y.
Color confinement is a consequence of the non-Abelian SU(3) running coupling growing at low
energies; the QCD string tension σ ≈ 0.18 GeV² produces a linear potential that makes
quark isolation energetically impossible. Masses from Yukawa couplings to the Higgs; the
SM offers no explanation for why they span five orders of magnitude.

---

## Dimensional Folding Explanation

### Structural Identity: Reaching D7

A quark is a compression-field kink whose closure structure extends through all three
internal depths:

```
D5 — U(1)_Y closure   → hypercharge  (all quarks)
D6 — SU(2)_L closure  → weak isospin (left-handed quarks in doublets)
D7 — SU(3)_c closure  → color charge (quarks only — leptons stop at D6)
```

The defining property of quarks — what separates them from leptons — is that they reach
D7. The D7 SU(3) closure is the compression field's deepest stable bifurcation; quarks
are the kinks that penetrate to this depth.

### Color Charge: D7 Winding Orientation

At D7, the compression field closes into the SU(3) group manifold. Just as the D5
closure carries a U(1) winding number (quantized charge) and the D6 closure carries
an SU(2) winding (weak isospin doublet), the D7 closure carries an SU(3) orientation.

The fundamental representation of SU(3) is 3-dimensional. A quark's color state is
its orientation in this 3-dimensional color space — one of three basis directions
(red, green, blue). These three color states correspond to the three independent
directions in the SU(3) fundamental representation:

```
|r⟩, |g⟩, |b⟩  ←→  three basis vectors of the fundamental 3 of SU(3)
```

An antiquark carries anticolor — the conjugate representation 3̄. A gluon carries
color-anticolor (adjoint representation, 8-dimensional — the 8 generators of SU(3)).

The three colors are not three independent structures — they are three orientations of
the same D7 closure in color space, related to each other by SU(3) color rotations
(gluon exchange). This is why the strong force treats all colors identically
(color independence of QCD).

### Fractional Charge: D7 Color Triplet Distributes Hypercharge

Quarks have fractional electric charges (+2/3 and −1/3) while all other elementary
particles have integer charges. This follows from the Gell-Mann–Nishijima formula
Q = T₃ + Y/2 with the quark hypercharge Y = 1/3 (not an integer):

```
u_L: Q = +1/2 + (1/3)/2 = +2/3
d_L: Q = −1/2 + (1/3)/2 = −1/3
```

Why Y = 1/3 for quarks when leptons have Y = −1?

In DFC, the D7 color closure is a 3-dimensional representation. The D5 hypercharge
is distributed across the three color states of the D7 fundamental:

```
Y_quark = Y_lepton / N_c    [N_c = 3 color states in the D7 fundamental]
|Y_quark / Y_lepton| = 1/3
```

The D7 closure "divides" the D5 winding across 3 states. Each individual quark carries
1/3 of the hypercharge unit that a lepton carries. This is why all quark hypercharges
are multiples of 1/3, and why fractional electric charges arise only for particles
that reach D7.

The constraint that quark and lepton hypercharges are related by 1/N_c is also the
statement required by gauge anomaly cancellation in the Standard Model — the
requirement that quantum corrections do not break gauge invariance. In DFC, anomaly
cancellation is not imposed separately; it is a consequence of the D5/D6/D7 closure
topology producing consistent winding number assignments.

**Note:** The precise DFC derivation of why Y_quark = +1/3 (positive, not negative as
this ratio argument with Y_lepton = −1 might suggest) requires working through the
full hypercharge assignments including both left-handed and right-handed components
with their D7 winding. This is currently a correspondence, not a derivation.

### Spin-1/2: Jackiw-Rebbi at D7

The quark spin-1/2 follows by the same mechanism as the electron — the Jackiw-Rebbi
zero mode of the compression kink background, now at D7 (see `foundations/spin_emergence.md`):

```
ψ_0(x) = A × cosh^{−Mλ}(x/λ) × |spinor, color⟩

where M = g_Y^{(D7)} φ₀   [D7 Yukawa coupling, different from the D6 lepton coupling]
```

The zero mode is a direct product of a Lorentz spinor and a color state. A quark is a
spin-1/2 particle in each of its three color states — three copies of the spin-1/2
zero mode, one per color.

The D7 Yukawa coupling g_Y^{(D7)} is larger than the D6 lepton coupling because D7 is
a deeper closure with a larger coupling constant (α_s > α_W > α_EM at low energies).
This is consistent with quarks being more tightly bound to their kink background than
leptons.

### Confinement: D7 Topology Forbids Isolated Color

The D7 SU(3) closure does not support isolated color-charged configurations in D3
localization space. More precisely:

A single quark carries D7 winding in the fundamental representation (color triplet).
For this D7 winding to exist as a stable D3 configuration, it must close — the
winding must return to its starting value as we move around the kink in the substrate's D3 localization behavior.

For an SU(3) color singlet (color-neutral combination), the D7 winding closes:
```
3 ⊗ 3̄ → 1           [meson: quark + antiquark → color singlet]
3 ⊗ 3 ⊗ 3 → 1       [baryon: three quarks → color singlet via ε tensor]
```

For an isolated quark (color triplet, not neutral), the D7 winding cannot close in
D3 — there is no configuration in the substrate's D3 localization behavior along which the SU(3) orientation returns to
its starting value. The compression field at D3 does not support such an open
boundary condition.

The energy cost of separating quarks grows with distance because the D7 color flux
does not disperse (unlike the D5 electric flux which spreads out as 1/r²). The D7
flux collapses into a tube — the QCD string — because the D7 topology forces it to
remain attached to another D7 winding. The tube energy per unit length is the string
tension σ ≈ 0.18 GeV².

When enough energy is input to break the string, the compression field nucleates a
new quark-antiquark pair from the vacuum — the string breaks and two new hadrons
form. Color charge is never isolated; it is transferred to the new pair.

**Open problem:** The precise DFC mechanism — showing from the nonlinear compression
field equations that isolated D7 winding is unstable in D3 — requires the full
nonlinear field theory at D7. The statement is structurally consistent with the model
but the formal derivation is not yet complete.

### Six Flavors: Three D7 Sectors × Two SU(2)_L Isospin States

The six quark flavors arise from two independent structures:

1. **Three generations**: The D7 SU(3) topology has three independent winding sectors
   (same mechanism as the three lepton generations, see `foundations/three_generations.md`).
   Each D7 sector contributes one up-type and one down-type quark.

2. **Two isospin states per generation**: At D6, each generation of quarks forms an
   SU(2)_L doublet — the left-handed up-type (T₃ = +1/2) and down-type (T₃ = −1/2)
   components. These are the two columns of each generation block.

```
Generation 1: (u_L, d_L) doublet  +  u_R, d_R singlets   [D7 sector 1]
Generation 2: (c_L, s_L) doublet  +  c_R, s_R singlets   [D7 sector 2]
Generation 3: (t_L, b_L) doublet  +  t_R, b_R singlets   [D7 sector 3]
```

The 6 = 3 × 2 count follows from the D7 topology (three sectors) combined with the
D6 doublet structure (two isospin states).

### Mass Hierarchy

Quark masses span ~80,000× from up (2.2 MeV) to top (173,000 MeV). The same
three-sector structure that gives three generations applies here — each sector has a
ground-state zero mode with a different effective D7 Yukawa coupling.

The depth-scaling exponent for quarks is κ_q ≈ 4.5–4.7 per generation step
(vs κ_lepton ≈ 5.33 for charged leptons). The smaller κ_q reflects that quarks'
mass scale is set by D7 coupling rather than D6.

```
quark_masses.py (fitted to u, d, t, b; predicts c, s):
  Predicted charm:   1079 MeV   Observed: 1275 MeV   (−15%)
  Predicted strange:   79 MeV   Observed:   93 MeV   (−15%)
```

The 15% systematic underestimate of c and s is consistent across both predictions —
a common correction factor, possibly from the quark mass renormalization scheme
(MS-bar masses vs. physical pole masses) or a uniform offset in the D7 coupling scale.

**Top quark anomaly:** The top quark Yukawa coupling y_t = m_t/v ≈ 173/246 ≈ 0.99 ≈ 1.
Every other quark has y ≪ 1. In DFC, this means the top quark's D7 zero-mode sits
at the D6 S³ squashing threshold — the top is the deepest quark state, and its mass
scale is set not by the D7 Yukawa alone but by its proximity to the Higgs (D6 squashing)
scale. The near-unity Yukawa is a geometric coincidence between the D7 depth scale and
the D6 squashing scale for the third-generation D7 sector.

---

## Formal Equations

### Color Charge

```
SU(3)_c fundamental representation: dimension 3
Color states: |r⟩, |g⟩, |b⟩   [basis of the 3-rep]
Gluon fields: G_μ^a,  a = 1,...,8   [connection on the color bundle]

Quark covariant derivative:
D_μ q = (∂_μ − ig_s T^a G_μ^a) q    [T^a = SU(3) generators, 3×3 matrices]
```

### Electric Charge from Winding Numbers

```
Q = T₃ + Y/2           [Gell-Mann–Nishijima]

Quark doublet hypercharge Y = +1/3:
  u_L: Q = +1/2 + 1/6 = +2/3   ✓
  d_L: Q = −1/2 + 1/6 = −1/3   ✓

Relation to lepton hypercharge:
  |Y_quark| = |Y_lepton| / N_c = 1 / 3
```

### Color-Neutral Combinations (Confinement)

```
Color singlets (stable D3 configurations):
  Meson:  3 ⊗ 3̄ ∋ 1     q q̄ with matching color-anticolor
  Baryon: 3 ⊗ 3 ⊗ 3 ∋ 1  ε_{abc} q^a q^b q^c

Color non-singlets (no stable D3 configuration):
  Single quark: 3 — no closed D7 winding in D3 → confined
  Diquark:      3 ⊗ 3 = 6 ⊕ 3̄ — no singlet → confined
```

### Confinement Potential

```
V(r) = −4α_s/3r + σ r     [Cornell potential]

σ ≈ 0.18 GeV²   [string tension — energy per unit length of QCD flux tube]
V → ∞ as r → ∞ → quarks cannot be separated
```

### Running Coupling

```
α_s(μ) = 2π / (β_0 ln(μ/Λ_QCD))

β_0 = 11 − 2N_f/3    [N_f = 6 active flavors]
Λ_QCD ≈ 200–300 MeV  [confinement scale]

α_s → ∞  as  μ → Λ_QCD   (confinement)
α_s → 0   as  μ → ∞       (asymptotic freedom)
```

---

## Consistency Checks

| Property | DFC | Observed |
|---|---|---|
| Spin | Jackiw-Rebbi zero mode with D7 coupling | 1/2 ✓ |
| Color states | 3 = dimension of SU(3) fundamental rep at D7 | 3 ✓ |
| Charges +2/3, −1/3 | Q = T₃ + Y/2, Y = 1/3 from D7 triplet distribution | ✓ |
| Six flavors | 3 D7 sectors × 2 SU(2)_L isospin states | 6 ✓ |
| Confinement | Isolated D7 winding has no stable D3 realization | ✓ (qualitative) |
| Asymptotic freedom | SU(3) non-Abelian: gluon loops anti-screen | ✓ |
| y_t ≈ 1 | Top sits at D6 squashing threshold | consistent ✓ |
| Charm/strange mass | ~15% below observed | ✗ (systematic offset) |
| Confinement mechanism | Nonlinear D7 field theory not yet computed | open |
| Y_quark sign/value | Consistency argument; not formally derived from D7 | open |

---

## Open Questions

1. **Formally derive quark hypercharges from D7 topology.** The argument that
   Y_quark = Y_lepton/N_c distributes hypercharge across color states is structurally
   sound but not derived from the D7 field equations. The precise sign and value of
   Y requires working through the D5/D6/D7 coupling structure with both left- and
   right-handed components.

2. **Derive confinement from the nonlinear compression field at D7.** Show explicitly
   that the DFC compression field equations at D7 depth do not admit isolated color-
   charged stable solutions in D3. The qualitative argument (D7 winding cannot close
   alone in D3) is consistent; the formal proof requires the full nonlinear theory.

3. **Resolve the 15% systematic offset in charm/strange masses.** The quark mass
   model predicts both c and s at 85% of their observed values. A common scale
   correction (scheme conversion from MS-bar to physical masses, or a uniform D7
   coupling offset) would remove this. The correction needs a physical justification.

4. **Derive the top quark mass from the D6/D7 proximity.** The near-unity Yukawa
   coupling y_t ≈ 1 is interpreted as the top quark D7 sector sitting at the Higgs
   (D6 squashing) threshold. Computing m_t from the geometry of the D7–D6 boundary
   interaction would connect the quark and Higgs sectors.

5. **CKM mixing matrix from D6/D7 coupling.** The weak interactions do not connect
   pure mass eigenstates — quark flavor mixing is encoded in the CKM matrix. In DFC,
   this mixing arises from the misalignment between the D6 (weak isospin) and D7
   (mass) eigenstates across the three D7 sectors. The CKM matrix is the rotation
   between D6 and D7 eigenstate bases. Deriving its values from the sector geometry
   is the quark mixing open problem.

---

## Connections

- **Strong force** — D7 SU(3) gluon fields, confinement mechanism;
  `phenomena/particle_physics/forces/strong_force.md`
- **Electroweak** — Q = T₃ + Y/2, quark doublet structure;
  `phenomena/particle_physics/forces/electroweak.md`
- **Spin-1/2 emergence** — Jackiw-Rebbi zero mode at D7;
  `foundations/spin_emergence.md`
- **Three generations** — D7 winding sectors; `foundations/three_generations.md`
- **Composite particles** — quarks bound into hadrons; `phenomena/particle_physics/particles/composite_particles.md`
- **Proton stability** — D7→D5 transition forbidden; `phenomena/particle_physics/proton_stability.md`
- **CP violation** — CKM mixing between D7 sectors; `phenomena/particle_physics/cp_violation.md`
- **Mass hierarchy** — depth-anchoring κ_q; `foundations/mass_hierarchy.md`
- **Electron** — lepton analog (stops at D6, no D7); `phenomena/particle_physics/particles/electron.md`
