# Phenomenon: The Weak Nuclear Force

## One-Sentence Synthesis

> The weak force is the gauge interaction of the D6 SU(2) closure — by the same
> local-symmetry structure that produces A_μ at D5 and G_μ^a at D7, the independently-defined
> SU(2) orientation at each spatial point produces three gauge fields W_μ^a; unlike the
> other forces, D6 SU(2) is a chiral closure (S³ carries an intrinsic orientation defined
> by the dimensional structure that creates it), so only left-handed fermions couple to it,
> and the S³'s squashing away from perfect symmetry gives the W and Z bosons their mass
> while leaving the photon massless.

---

## Observation

The weak force mediates all flavor-changing transitions — most familiarly neutron beta
decay n → p + e⁻ + ν̄_e. It is carried by three massive gauge bosons: W⁺, W⁻ (m_W ≈ 80.4 GeV),
and Z⁰ (m_Z ≈ 91.2 GeV). It is short-range (~10⁻¹⁸ m) because of these masses.

Two properties distinguish it from electromagnetism and the strong force:

**Parity violation (P-violation):** The weak force is left-handed. Only left-handed fermions
(chirality L) couple to the W bosons. Right-handed fermions are completely unaffected by
W exchange. This was discovered by Wu (1956) in Co-60 beta decay — the electron emission
is not symmetric under mirror reflection. The weak force violates parity maximally.

**Massive gauge bosons:** The W and Z bosons have mass. For EM and the strong force, the
gauge bosons are massless (photon, gluons). The weak force gauge bosons are as heavy as
nuclei of gold (~80–91 atomic mass units). Their mass comes from the Higgs mechanism and
is the source of the force's short range.

---

## Standard Explanation

Glashow-Salam-Weinberg electroweak theory (1968, Nobel 1979): SU(2)_L × U(1)_Y is the
gauge group. The _L subscript means only left-handed fermions transform under SU(2). A
Higgs doublet acquires a vacuum expectation value (VEV), breaking the symmetry to U(1)_EM
and giving masses m_W = g_W v/2 and m_Z = m_W/cos θ_W (where v ≈ 246 GeV and θ_W is the
Weinberg angle sin²θ_W ≈ 0.231). At low energies (q² ≪ m_W²), the W exchange reduces to
the Fermi 4-fermion contact interaction with coupling G_F/√2 = g_W²/8m_W².

The SM takes the left-handedness as a postulate: left and right chiralities are assigned
to different SU(2) representations by hand. It does not explain why.

---

## Dimensional Folding Explanation

### The Same Gauge Logic, at D6

The weak force arises by the exact mechanism as EM (D5) and the strong force (D7):

- At D5: local U(1) orientation → 1 gauge field A_μ → electromagnetism
- At D6: local SU(2) orientation → 3 gauge fields W_μ^a (a=1,2,3) → weak force
- At D7: local SU(3) orientation → 8 gauge fields G_μ^a → strong force

SU(2) has 3 generators (2² − 1 = 3), so three gauge fields are required — one connection
field per generator. The D6 closure gives each fermion an **SU(2) orientation** in a
2-dimensional complex space (a spinor direction). Because this orientation is independently
defined at each point in space, a connection W_μ^a exists — it is the mathematical object
required for comparing SU(2) orientations at neighboring points.

### Why D6 Is Chiral: S³ Carries an Intrinsic Orientation

This is the key structural difference of the weak force from all others.

The group manifold of SU(2) is S³ — the 3-sphere. Compare:
- U(1) group manifold is S¹ (a circle). S¹ is orientation-symmetric: clockwise and
  counterclockwise are related by a simple reflection. No intrinsic chirality.
- SU(2) group manifold is S³ (a 3-sphere). S³ is **chiral**: the two orientations of S³
  (right-handed and left-handed) are not continuously related. S³ has a definite handedness
  that cannot be removed by a continuous transformation.

When the D6 closure creates an SU(2) topology at each spatial point, it does so with a
single definite chirality — the orientation inherent to the dimensional structure that
generates the D6 closure. This chirality is preserved throughout the closure geometry.

**The physical consequence:** only fermions whose intrinsic spin is aligned with the S³
orientation couple to the W_μ^a connection fields. These are the left-handed fermions
(spin antiparallel to momentum for particles, spin parallel for antiparticles). Right-handed
fermions are aligned with the opposite S³ orientation — they see no W_μ^a connection.

**In DFC terms:** parity violation is not a postulate — it is the structural consequence of
the D6 closure having a single intrinsic orientation. The chirality of S³ is why the weak
force violates parity maximally.

*The precise DFC derivation of why the D6 S³ closure has exactly one intrinsic chirality
(rather than both, or neither) is an open problem — see Open Questions below.*

### Why the W and Z Bosons Are Massive

In electromagnetism, the photon is massless because the U(1) circle is homogeneous — no
point is geometrically distinguished, so no stable minimum exists and no mass term is
consistent with A_μ. The photon's masslessness reflects this topological uniformity of S¹.

The S³ (SU(2) group manifold) at D6 is also homogeneous in its undistorted form — but it
can be **squashed**: deformed from a perfectly round S³ to an ellipsoidal shape. When the
S³ is squashed (ε ≠ 0, where ε is the squashing parameter), the full SU(2) symmetry is
broken. The rotations along the squashing axis require no energy (that direction becomes
the massless photon — the surviving U(1)_EM). The rotations perpendicular to the squashing
axis encounter resistance — those are the massive W±, Z⁰.

The squashing parameter ε is the Higgs field — not a new independent field added by hand,
but the geometric deformation of the D6 S³ closure. (See `foundations/higgs_geometry.md`
for the full DFC derivation of the Higgs potential from S³ geometry.)

The vacuum sits at ε₀ = v/√2 where v ≈ 246 GeV (the electroweak scale). This gives:
```
m_W = (1/2) g_W v ≈ 80.4 GeV
m_Z = m_W / cos θ_W ≈ 91.2 GeV
```

The photon remains massless because the squashing preserves one U(1) rotation axis — the
electromagnetic U(1) of D5 and D6 combined.

### Why the Force Is Short-Range

A massive gauge boson W (mass m_W) mediates a Yukawa potential:
```
V(r) = g² exp(−m_W r/ℏc) / r
```

The exponential suppression sets in at the Compton wavelength of the W:
```
λ_W = ℏc/m_W ≈ (197 MeV·fm) / 80,400 MeV ≈ 2.5 × 10⁻³ fm ≈ 10⁻¹⁸ m
```

The weak force is effectively zero beyond 10⁻¹⁸ m — 1000 times shorter than a proton's
radius. By contrast, EM (massless photon) is infinite range and the strong force (massless
gluons, but confined) is effective to ~1 fm.

**In DFC:** the short range is the direct consequence of the S³ squashing — the mass gap
of the W boson is the energy scale set by the D6 closure geometry (ε₀ v). A perfectly
symmetric S³ (ε = 0) would give massless W bosons and an infinite-range weak force.

---

## Formal Equations

### SU(2) Gauge Lagrangian

The weak force Lagrangian (gauge kinetic + left-handed fermion coupling):
```
L_W = −(1/4) F_μν^a F^{aμν} + Σ_f L̄_f (iγ^μ D_μ) L_f
```

where L_f are the left-handed fermion doublets and:
```
F_μν^a = ∂_μ W_ν^a − ∂_ν W_μ^a + g_W ε^{abc} W_μ^b W_ν^c   [SU(2) field strength]
D_μ = ∂_μ − ig_W (τ^a/2) W_μ^a                               [covariant derivative]
τ^a = Pauli matrices                                           [SU(2) generators]
ε^{abc}                                                        [SU(2) structure constants: [τ^a/2,τ^b/2] = iε^{abc}τ^c/2]
```

The self-coupling term ε^{abc}W_μ^bW_ν^c makes the weak force non-Abelian — W bosons
carry weak isospin and self-interact, like gluons carry color. However, unlike gluons,
the W bosons are massive and do not produce confinement.

### Physical W and Z Bosons

The three SU(2) gauge fields W_μ^{1,2,3} mix with the U(1)_Y field B_μ to give the
physical mass eigenstates:
```
W_μ± = (W_μ^1 ∓ iW_μ^2) / √2      [charged W bosons: m_W = g_W v/2]
Z_μ  = W_μ^3 cos θ_W − B_μ sin θ_W [neutral Z boson: m_Z = m_W/cos θ_W]
A_μ  = W_μ^3 sin θ_W + B_μ cos θ_W [photon: massless]
```

where the Weinberg angle θ_W relates the SU(2) and U(1)_Y couplings:
```
tan θ_W = g'/g_W     where g' = U(1)_Y coupling, g_W = SU(2) coupling
sin²θ_W ≈ 0.231      [measured at Z pole]
```

The photon is the linear combination of W³ and B that remains massless after squashing.
Electromagnetism is preserved: the broken SU(2)×U(1)_Y preserves exactly one U(1) — the
U(1)_EM of D5 combined with the unsquashed rotation axis of D6.

### Mass Relations

From the Higgs VEV v ≈ 246.22 GeV and measured couplings:
```
m_W = g_W v / 2 = (0.653 × 246.22) / 2 ≈ 80.4 GeV   ✓  [observed: 80.377 GeV]
m_Z = m_W / cos θ_W ≈ 80.4 / cos(28.7°) ≈ 91.2 GeV  ✓  [observed: 91.188 GeV]
```

The ρ parameter measures the ratio m_W/m_Z against the prediction:
```
ρ = m_W² / (m_Z² cos²θ_W) = 1     [tree level — confirmed at 10⁻³ precision]
```

### Low-Energy Fermi Theory

At energies q² ≪ m_W², the W propagator 1/(q² − m_W²) → −1/m_W². The full weak amplitude
reduces to a 4-fermion contact interaction:
```
H_eff = (G_F/√2) J_μ^† J^μ

G_F/√2 = g_W² / (8m_W²) = 1.1664 × 10⁻⁵ GeV⁻²   [Fermi constant]
```

This is Fermi's original theory (1934) — now understood as the low-energy effective
theory of W exchange, valid at nuclear and atomic energies (q ≪ 80 GeV).

### Neutron Decay Rate

The amplitude for n → p + e⁻ + ν̄_e proceeds via d → u + W⁻(virtual) → u + e⁻ + ν̄_e.
Since (m_n − m_p)² ≈ (1.29 MeV)² ≪ m_W² ≈ 6450 GeV², the Fermi approximation is exact.

At tree level (with radiative corrections from `equations/proton_stability.py`):
```
Γ_n = (G_F² |V_ud|²  m_e⁵) / (2π³) × f(E_max/m_e) × (1 + 3λ²)

where:
  V_ud ≈ 0.974    [CKM matrix element: d→u coupling strength]
  f ≈ 1.635       [phase space integral]
  λ = g_A/g_V ≈ −1.270  [axial/vector coupling ratio]

→ τ_n(tree) ≈ 912.7 s
→ τ_n(tree × RC) ≈ 878.4 s   [with radiative corrections factor 1/1.039]
Observed: τ_n = 879.4 ± 0.6 s   ✓
```

The neutron lifetime is the cleanest quantitative test of the D6 weak sector: the intra-D6
transition d → u is permitted (same D-depth, same closure type), the V−A coupling
structure follows from the left-handed D6 chirality, and the rate matches to 0.1%.

---

## What This Explains

| Observation | DFC mechanism |
|---|---|
| W, Z bosons carry the force | D6 SU(2) local symmetry → 3 connection fields W_μ^a |
| Only 3 weak gauge bosons | SU(2) has 3 generators (2²−1=3) |
| Parity violated maximally | S³ group manifold of D6 is chiral — single intrinsic orientation |
| Right-handed fermions don't couple | Aligned with opposite S³ orientation |
| W, Z are massive (80–91 GeV) | S³ squashing (Higgs mechanism): ε ≠ 0 breaks SU(2)×U(1) |
| Photon remains massless | Squashing preserves one U(1) rotation axis |
| Force range ~10⁻¹⁸ m | Yukawa suppression from W mass: λ_W = ℏc/m_W |
| Neutron decay τ_n = 879.4 s | Fermi theory from W exchange: computed 878.4 s (0.1% error) |
| m_W/m_Z = cos θ_W | Ratio of D5/D6 coupling geometry = Weinberg angle |

---

## Comparison: EM vs Strong vs Weak

| Property | EM (D5) | Strong (D7) | Weak (D6) |
|---|---|---|---|
| Gauge group | U(1) | SU(3) | SU(2)_L |
| Generators | 1 | 8 | 3 |
| Gauge bosons | 1 photon | 8 gluons | W±, Z⁰ |
| Boson mass | 0 | 0 | 80–91 GeV |
| Self-coupling | None | 3- and 4-gluon | 3- and 4-W |
| Chiral? | No | No | Yes (left only) |
| Range | ∞ | ~1 fm (confined) | ~10⁻¹⁸ m |
| Force falls as | 1/r² | Constant (flux tube) | exp(−m_W r)/r |
| Broken? | No | No | Yes (SU(2)×U(1)→U(1)) |

---

## Connections to Other Phenomena

- **Electroweak unification** — D5 U(1) and D6 SU(2) as adjacent independent closures;
  `phenomena/particle_physics/forces/electroweak.md`
- **W/Z bosons** — the three D6 gauge bosons; `phenomena/particle_physics/particles/w_z_bosons.md`
- **Higgs geometry** — D6 S³ squashing gives mass; `foundations/higgs_geometry.md`
- **Proton stability / neutron lifetime** — weak decay is intra-D6; τ_n computed;
  `phenomena/particle_physics/proton_stability.md`
- **Electromagnetism** — D5 U(1) closure, same gauge logic; `phenomena/electromagnetism/electromagnetism.md`
- **Strong force** — D7 SU(3) closure, also non-Abelian; `phenomena/particle_physics/forces/strong_force.md`
- **CP violation** — weak force violates CP in quark sector; `phenomena/particle_physics/cp_violation.md`
- **Radioactive decay** — beta decay is the canonical weak process; `phenomena/particle_physics/radioactive_decay.md`

---

## Open Questions

1. **Formal derivation of D6 chirality:** The physical argument is that S³ is chiral (has
   an intrinsic orientation defined by the D6 closure structure), producing the left-handed
   coupling. A formal DFC derivation requires showing that the D6 S³ closure topology has
   exactly one intrinsic chirality — and explaining why the dimensional structure generating
   D6 results in the observed left handedness. This would derive parity violation from first
   principles rather than postulating SU(2)_L.

2. **Weinberg angle (Route 3B — partially derived):** sin²θ_W = 0.231 is reproduced by
   the equal-coupling initial condition (Route 3B, see `foundations/embedding_geometry.md`
   and `equations/weinberg_angle_rg.py`). All gauge closures emerge from the same substrate
   with the same kinetic coefficient → α₁ = α₂ at the D5/D6 formation scale M_c(12) ≈ 10^13 GeV
   → sin²θ_W = 3/8 at M_c → SM running → 0.231 at M_Z (0.00% discrepancy). Remaining open
   items: (a) derive M_c(12) from substrate parameters (α, β, c) rather than reading it from
   SM running; (b) derive the 3/5 hypercharge normalization from D5 closure geometry rather
   than borrowing it from SU(5) GUT embedding.

3. **Derive the CKM matrix from DFC closure structure:** The CKM matrix parametrizes quark
   flavor mixing under weak transitions (d→u, s→c, b→t with off-diagonal amplitudes V_us,
   V_cb, etc.). Three mixing angles and one CP-violating phase. In DFC, these should follow
   from the overlap geometry of D6 (SU(2) closure) with D7 (SU(3) closure) — how the color
   eigenstates and weak eigenstates relate given the independent D6 and D7 topologies.

4. **Non-perturbative weak regime:** At energies above m_W, the weak coupling g_W is
   not small. Sphaleron processes (topological transitions in the SU(2) field) can violate
   baryon and lepton number. In DFC, these correspond to transitions in the D6 topology —
   the S³ winding number changing. The rate of such transitions (relevant for baryogenesis)
   requires non-perturbative D6 analysis analogous to the non-perturbative D7 problem
   for QCD confinement.
