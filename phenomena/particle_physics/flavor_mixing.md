# Phenomenon: Flavor Mixing (CKM and PMNS Matrices)

## One-Sentence Synthesis

> Flavor mixing — the fact that quarks and leptons produced in weak interactions are
> superpositions of mass eigenstates, quantified by the CKM matrix for quarks and the
> PMNS matrix for neutrinos — arises in DFC from the misalignment between the D6 SU(2)
> flavor basis (defined by which states couple to the W bosons) and the D4/D7 mass basis
> (defined by the depth anchoring that gives each fermion its mass); for quarks, the small
> CKM mixing follows from D6/D7 adjacency nearly aligning the two bases, while for
> neutrinos, the large PMNS mixing follows from D4-anchored mass eigenvalues being nearly
> degenerate (near-degeneracy produces large mixing), with CP-violating phases encoding
> the relative fold orientation of the three-generation SU(3) structure between the two
> bases.

---

## Observation

Quarks and leptons mix between generations when they participate in weak interactions.

**CKM matrix (quark sector):** The Cabibbo-Kobayashi-Maskawa matrix parametrizes the
mismatch between quark mass eigenstates (up, charm, top; down, strange, bottom) and the
weak interaction eigenstates. It is approximately:
- V_ud ≈ 0.974, V_us ≈ 0.225 (Cabibbo angle θ_C ≈ 13°)
- V_cb ≈ 0.041 (small second-third generation mixing)
- V_ub ≈ 0.004 (very small first-third generation mixing)
- One CP-violating phase δ_CKM ≈ 1.2 radians

The near-diagonal structure (most mixing is between first and second generations) is
unexplained in the SM — it is a free parameter.

**PMNS matrix (neutrino sector):** Completely different structure from CKM:
- θ_12 ≈ 33° (large)
- θ_23 ≈ 49° (near-maximal — but see T10 in ISSUES.md: DFC structural argument for
  near-degeneracy conflicts with m₃ ≫ m₂)
- θ_13 ≈ 8.6°
- CP phase δ_CP ≈ 195° (preliminary)

The large neutrino mixing angles contrasting with small quark mixing angles is a major
unexplained pattern in the SM.

**Observable consequences:**
- Strangeness-changing decays (K-meson oscillations, B-meson oscillations)
- B-meson CP violation (measured at BaBar, Belle, LHCb)
- Neutrino oscillations (see `phenomena/particle_physics/neutrino_oscillations.md`)

---

## Standard Explanation

In the SM, quark and lepton masses arise from Yukawa couplings to the Higgs field. The
Yukawa coupling matrices for up-type quarks, down-type quarks, and charged leptons are
generally independent 3×3 complex matrices. In the mass eigenstate basis (diagonalizing
the Yukawa matrices), the weak interaction picks out a specific linear combination of the
left-handed fields. The mismatch between the mass eigenstate basis and the weak eigenstate
basis is the CKM matrix (for quarks) and the PMNS matrix (for leptons).

The SM provides no explanation for why the Yukawa coupling matrices have the values they
do. They are 18 independent real parameters (for three generations with complex phases)
taken from experiment. The near-diagonality of the CKM matrix and the near-maximality
of the PMNS neutrino mixing are unexplained patterns.

---

## Dimensional Folding Explanation

### Two Eigenstate Bases for Every Fermion

In DFC, each fermion type participates in two distinct physical processes that define two
generally distinct bases:

**The flavor basis** is defined by coupling to the W bosons at D6 SU(2) depth. The
electron-neutrino pair, the muon-muon-neutrino pair, and the tau-tau-neutrino pair are
the three SU(2) doublets — the three flavor pairs through which weak charge is conserved.
The flavor basis is determined by the D6 SU(2) closure topology.

**The mass basis** is defined by the depth at which the fermion's zero mode anchors into
the D4 inertia behavior. The electron mass, muon mass, and tau mass correspond to three
different D4 anchoring depths for the three generations (see `foundations/mass_hierarchy.md`).
For quarks, the mass basis also involves D7 SU(3) closure, which gives quarks their
constituent mass contribution from confinement.

These two bases — flavor and mass — are **generically misaligned**. There is no symmetry
principle forcing them to coincide. The mixing angles measure the projection angle between
the flavor eigenstates and the mass eigenstates.

### Why CKM Mixing Is Small: D6/D7 Adjacency

For quarks, both the flavor basis (D6 SU(2)) and the mass basis (D7 SU(3) + D4 inertia)
involve closure events at adjacent depths D6 and D7. The topological structures at D6
and D7 are tightly coupled: the D7 SU(3) closure forms in the presence of the already-
established D6 SU(2) background.

This coupling means the three quark mass eigenstates formed at D7 are constrained by the
D6 structure — the two bases are nearly aligned by construction. The CKM matrix is
nearly diagonal because the D6/D7 proximity forces the quark flavor and mass eigenstate
directions to be nearly parallel, with small off-diagonal elements corresponding to small
angular misalignments at the D6/D7 boundary.

The Cabibbo angle (θ_C ≈ 13°) — the dominant first-second generation mixing — measures
the misalignment between the D6 SU(2) doublet direction and the D7 mass eigenstate axis
for the strange quark. This small angle corresponds to a small fold orientation difference
between the D6 and D7 closures.

**Structural prediction direction:** CKM mixing angles are small because D6 and D7 are
adjacent depths, forcing their respective closure geometries to be nearly aligned.
Quantitative derivation of the Cabibbo angle from the D6/D7 boundary geometry is an
open problem.

### Why PMNS Mixing Is Large: D4 Near-Degeneracy

For neutrinos, the situation is entirely different. Neutrinos do not close at D5 (they
have no electric charge — no D5 U(1) closure) and do not close at D7 (they carry no
color). Their masses are anchored at D4 inertia depth, but at a very small scale compared
to charged leptons.

The three neutrino mass eigenstates correspond to three D4 depth anchoring levels. Because
neutrino masses are tiny (sub-eV), the three mass eigenstates are nearly degenerate —
the three D4 anchoring depths are very close together. Near-degeneracy has a universal
consequence for quantum mixing: when the mass differences between eigenstates are small,
the eigenstates mix strongly.

The physical reason: if two states have masses m₁ and m₂ with m₁ ≈ m₂, then any small
perturbation (such as the D6 coupling that defines flavor eigenstates) can produce a
large rotation between the mass basis and the perturbation's eigenbasis. The mixing angle
approaches 45° (maximal mixing) in the limit of exact degeneracy (m₁ = m₂).

For neutrinos, the D4 depth anchoring levels are nearly but not exactly degenerate. The
observed θ_23 ≈ 49° (near-maximal) and θ_12 ≈ 33° (large) are consistent with near-
degenerate neutrino mass eigenstates mixing strongly with the D6 flavor basis.

**Note (ISSUES.md T10):** The structural argument "near-degeneracy → large mixing" is
directionally correct for θ_12 and the general large-mixing observation. However, it is
in tension with the measured mass hierarchy: Δm²₃₁/Δm²₂₁ ≈ 34, meaning m₃ is substantially
heavier than m₁ and m₂. This is not "near-degeneracy" between all three states. The
argument that near-degeneracy explains θ_23 ≈ 49° specifically requires m₂ ≈ m₃, but
the data shows m₃ ≫ m₂. This structural argument applies only to the {m₁, m₂} pair,
not the full three-generation picture. This tension is tracked in ISSUES.md as T10.

### CP Violation from Three-Generation Phase Structure

The CKM and PMNS matrices each have one irreducible CP-violating phase. In the SM, this
phase requires at least three generations — with only two, the matrix is real and no CP
violation is possible.

In DFC, this follows directly from the three-generation structure. The three quark
generations correspond to three distinct D6 zero-mode orientations — the three dimensions
of the SU(3) fundamental representation at D7 (proved in `foundations/zero_mode_multiplet.md`
and `foundations/three_generations.md`). The CKM phase is the total phase accumulated
when one generation's D6 fold orientation is transported around the triangle connecting
all three generation fold orientations.

Specifically: the Jarlskog invariant J = Im[V_ud V*_us V_cs V*_cd] is nonzero if and
only if the three fold orientation angles θ₁₂, θ₁₃, θ₂₃ are all distinct and nonzero —
i.e., if the three generations are genuinely distinguishable. With only two generations,
the triangle in fold orientation space degenerates to a line, and J = 0. With three
non-degenerate generations, J ≠ 0 automatically.

In DFC: CP violation in the quark sector requires exactly three generations because the
SU(3) D7 zero-mode structure provides exactly three distinguishable fold orientation
states, and the triangle formed by three orientations in a three-dimensional space has
a nonzero area (complex phase) when the three orientations are distinct.

### Asymmetry Between CKM and PMNS: A Structural Argument

The fundamental asymmetry — CKM small, PMNS large — is a direct consequence of the
different depth structures of quarks and leptons:

**Quarks (D6/D7 coupling):** Mass eigenstates form near the flavor eigenstates → small
mixing. The depth separation between the mass and flavor bases is one bifurcation event
(D6 → D7).

**Neutrinos (D4/D6 coupling):** Mass eigenstates form far from the flavor eigenstates
→ large mixing. The depth separation between the mass and flavor bases is two bifurcation
events (D4 → D5 → D6). The larger the depth separation, the more the two bases can
rotate relative to each other.

This structural difference — fewer depth steps between mass and flavor basis for quarks,
more steps for neutrinos — is the DFC explanation for why CKM is nearly diagonal while
PMNS has large off-diagonal elements.

---

## Formal Equations

### CKM Matrix Parametrization

The CKM matrix mixes the d-type quark flavor eigenstates (d', s', b') with the mass
eigenstates (d, s, b). It is a 3×3 unitary matrix parametrized by three angles and one
CP-violating phase:

```
V_CKM = R₁₂(θ₁₂) × R₁₃(θ₁₃, δ) × R₂₃(θ₂₃)

Standard PDG form (c_ij = cos θ_ij, s_ij = sin θ_ij):

    c₁₂c₁₃           s₁₂c₁₃           s₁₃e^{−iδ}
  −s₁₂c₂₃ − c₁₂s₂₃s₁₃e^{iδ}   c₁₂c₂₃ − s₁₂s₂₃s₁₃e^{iδ}   s₂₃c₁₃
   s₁₂s₂₃ − c₁₂c₂₃s₁₃e^{iδ}  −c₁₂s₂₃ − s₁₂c₂₃s₁₃e^{iδ}   c₂₃c₁₃

Observed values (PDG):
  θ₁₂ ≈ 13.04°  (Cabibbo angle — D6/D7 u-d sector misalignment)
  θ₁₃ ≈  0.21°  (very small — first/third generation coupling)
  θ₂₃ ≈  2.38°  (small — second/third generation coupling)
  δ   ≈ 69.2°   (CP-violating phase)

DFC structural statement: These four angles are not derived from DFC parameters —
they are measured inputs. DFC predicts they should be small (for quarks), nonzero
(three distinct D6 orientation angles), and the CP phase should be nonzero (three
non-degenerate generations give nonzero triangle area). The specific values require
the D6/D7 boundary overlap integral.
```

### Jarlskog Invariant

The single rephasing-invariant measure of CP violation equals the imaginary part of a
specific product of CKM matrix elements. Its magnitude equals the product of sines of
all three mixing angles times the sine of the CP phase:

```
J = Im[V_ud V*_us V_cs V*_cd]
  = s₁₂ c₁₂ s₁₃ s₂₃ c₂₃ sin δ
  ≈ 3.0 × 10⁻⁵

DFC: J = 0 requires either all mixing angles zero (bases aligned) or δ = 0
(no CP violation). The substrate structure produces J ≠ 0 automatically when:
  (a) three distinct D6 fold orientation angles exist, AND
  (b) their total accumulated phase around the generation triangle is nonzero.
```

### PMNS Matrix Parametrization

The PMNS matrix mixes the charged-lepton flavor eigenstates (ν_e, ν_μ, ν_τ) with the
neutrino mass eigenstates (ν₁, ν₂, ν₃). Same form as CKM but with completely different
numerical values:

```
V_PMNS = R₁₂(θ₁₂) × R₁₃(θ₁₃, δ_CP) × R₂₃(θ₂₃) × diag(e^{iα₁/2}, e^{iα₂/2}, 1)

Observed values (PDG):
  θ₁₂ ≈ 33.44°  (large — solar neutrino mixing)
  θ₂₃ ≈ 49.2°   (near-maximal — atmospheric neutrino mixing)
  θ₁₃ ≈  8.57°  (nonzero — reactor neutrino mixing)
  δ_CP ≈ −120°  (preliminary — T2K/NOvA)

DFC structural statement: Large PMNS angles are expected from near-degenerate
neutrino mass eigenstates at D4 depth. The specific values require the D4 mode
structure and the D4/D6 coupling geometry — not yet derived.
```

### Mass-Squared Differences (from neutrino oscillations)

Neutrino oscillations measure differences of squared masses, not masses directly. The
measured values (normal hierarchy assumed):

```
Δm²₂₁ = m₂² − m₁² ≈ 7.42 × 10⁻⁵ eV²  (solar)
Δm²₃₁ = m₃² − m₁² ≈ 2.517 × 10⁻³ eV²  (atmospheric)
Ratio: Δm²₃₁/Δm²₂₁ ≈ 33.9

DFC prediction (neutrino_masses.py): ratio ≈ 1.34   ✗ 4.3× off
Root cause: uniform D4 depth spacing assumed (m_n ∝ n); actual spacing non-uniform
```

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| Mixing exists | Flavor/mass basis misalignment at D6/D4 boundary | CKM and PMNS both measured | ✓ structural |
| CP violation requires ≥3 generations | Three generation triangle in D6 fold space has nonzero area only for N≥3 | 2-generation CKM is real; CP violation requires 3 | ✓ structural |
| CKM near-diagonal | D6/D7 adjacency aligns quark bases | All CKM angles < 13° | ✓ direction only |
| PMNS large angles | D4 near-degeneracy → large mixing; D4/D6 depth gap | θ₁₂ = 33°, θ₂₃ = 49° | ✓ direction only |
| Near-maximal θ₂₃ from near-degeneracy | Requires m₂ ≈ m₃ | m₃ ≫ m₂ (Δm²₃₁/Δm²₂₁ = 34) | ✗ T10 tension — structural argument fails for θ₂₃ |
| Neutrino mass ratio | Δm²₃₁/Δm²₂₁ = (m₃/m₂)² ≈ 34 | 33.9 | ✗ DFC gives 1.34 (4.3× off) |
| Cabibbo angle θ_C ≈ 13° from DFC | D6/D7 boundary overlap integral | 13.04° | ✗ OPEN — not derived |
| CKM CP phase δ ≈ 69° | Accumulated D6 fold orientation phase | 69.2° | ✗ OPEN — not derived |

---

## Open Questions

1. **Derive the Cabibbo angle from D6/D7 boundary:** The Cabibbo angle θ_C ≈ 13°
   (the first-second generation quark mixing angle) is the dominant CKM parameter. In
   DFC, it measures the misalignment between the D6 SU(2) doublet direction and the D7
   mass eigenstate axis for the strange quark. Compute this from the overlap integral of
   D6/D7 zero-mode wavefunctions — this would be a significant Criterion A result.

2. **Explain why θ₂₃ ≈ 49° without m₂ ≈ m₃:** The T10 tension (ISSUES.md) shows
   that the near-degeneracy argument for near-maximal θ₂₃ conflicts with Δm²₃₁/Δm²₂₁ ≈
   34. An alternative structural account is needed that produces large θ₂₃ without
   requiring m₂ ≈ m₃. One candidate: the D4/D6 coupling geometry produces inherently
   large mixing for the second-third generation even without mass degeneracy.

3. **GIM mechanism in DFC:** The GIM mechanism explains why flavor-changing neutral
   currents (FCNC) are suppressed in the SM. It follows from the unitarity of the CKM
   matrix. In DFC, unitarity is guaranteed by the topology of the D6 closure basis —
   any unitary transformation of the three D6 zero modes gives another valid basis. The
   GIM cancellation should follow automatically from this topological unitarity, but the
   explicit computation has not been done.

4. **Lepton flavor universality breaking:** The muon anomalous magnetic moment and
   B → K ℓ⁺ ℓ⁻ decays show hints of lepton flavor universality violation (LFU). In DFC,
   LFU holds at tree level (equal D6 coupling to all three generations) but could be
   broken by loop corrections involving the different D4 mass anchoring depths of the
   three generations. This is a testable prediction direction.

---

## Connections

- `foundations/zero_mode_multiplet.md` — n zero modes → SU(n): the mechanism that
  produces exactly three gauge-coupled generation states at D6/D7 depths
- `foundations/three_generations.md` — why exactly three generations exist
- `phenomena/particle_physics/neutrino_oscillations.md` — PMNS matrix; oscillation
  probabilities; Daya Bay comparison
- `phenomena/particle_physics/cp_violation.md` — CKM CP phase as D6 fold orientation
  phase; baryogenesis as separate D7 source
- `phenomena/particle_physics/particles/quarks.md` — D7 SU(3) mass contribution;
  constituent vs. current mass
- `phenomena/particle_physics/particles/neutrinos.md` — D4 anchoring and neutrino masses
- `foundations/mass_hierarchy.md` — depth anchoring and mass scale for each generation
- `equations/flavor_mixing.py` — CKM/PMNS matrix values; structural consistency checks;
  Jarlskog invariant; T10 tension documented
- `equations/neutrino_masses.py` — mass ratio failure (4.3×); Δm² predictions
