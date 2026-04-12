# Phenomenon: Flavor Mixing (CKM and PMNS Matrices)

## One-Sentence Synthesis

> Flavor mixing — the fact that quarks and leptons produced in weak interactions are
> superpositions of mass eigenstates, quantified by the CKM matrix for quarks and the
> PMNS matrix for neutrinos — arises in DFC from the misalignment between the D6 SU(2)
> flavor basis (defined by which states couple to the W bosons at D6) and the D4/D7 mass
> basis (defined by the depth anchoring that gives each fermion its mass), with the
> mixing angles measuring the projection angles between these two bases and the CP-violating
> phases encoding the relative orientation of the three-generation structure between the
> two bases.

---

## Observation

Quarks and leptons mix between generations when they participate in weak interactions.

**CKM matrix (quark sector):** The Cabibbo-Kobayashi-Maskawa matrix parametrizes the
mismatch between quark mass eigenstates (up, charm, top; down, strange, bottom) and the
weak interaction eigenstates. It is approximately:
- V-ud ≈ 0.974, V-us ≈ 0.225 (Cabibbo angle theta-C ≈ 13°)
- V-cb ≈ 0.041 (small second-third generation mixing)
- V-ub ≈ 0.004 (very small first-third generation mixing)
- One CP-violating phase delta-CKM ≈ 1.2 radians

The near-diagonal structure (most mixing is between first and second generations) is
unexplained in the SM — it is a free parameter.

**PMNS matrix (neutrino sector):** Completely different structure from CKM:
- theta-12 ≈ 33° (large)
- theta-23 ≈ 49° (near-maximal)
- theta-13 ≈ 8.6°
- CP phase delta-CP ≈ 195° (preliminary)

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

**STUB — full derivation not yet written.**

**DFC mechanism direction:**

1. **Two bases for fermion states:** Each fermion exists in two distinct eigenstate bases
   in DFC:
   - The **flavor basis:** defined by which D6 SU(2) closure state the fermion is paired
     with. The electron flavor is defined by pairing with the W-boson closure at D6.
   - The **mass basis:** defined by the D4 inertia anchoring depth. A fermion's mass is
     set by how deeply its zero mode penetrates into D4 (see `foundations/mass_hierarchy.md`).

   These two bases are generically misaligned. The mixing angles measure this misalignment.

2. **CKM from D6-D7 boundary geometry:** For quarks, the mass basis is set by both D6
   (electroweak) and D7 (color) closure depths. The CKM matrix represents the misalignment
   between the D6 flavor basis and the D7 mass basis for quarks. The near-diagonal CKM
   structure (small off-diagonal elements) corresponds to a small misalignment — the two
   bases are nearly aligned for quarks, which may follow from the D6-D7 closure proximity
   in the depth sequence.

3. **PMNS from D4-D6 boundary geometry:** For leptons, the mass basis is set by D4/D5/D6
   only (no D7 anchoring). The PMNS matrix represents the misalignment between the D6
   lepton flavor basis and the D4 mass basis for neutrinos. The large PMNS mixing angles
   (near-maximal for theta-23) may follow from a near-degeneracy in the D4 depth anchoring
   of the second and third generation neutrinos.

4. **Why CKM small and PMNS large:** The CKM matrix is nearly diagonal; the PMNS matrix
   has large off-diagonal elements. In DFC, this asymmetry would follow from the different
   depth structures:
   - Quarks reach D7 and receive large masses from color confinement. The D7 anchoring
     provides a strong mass hierarchy that tends to align the mass and flavor bases.
   - Neutrinos do not reach D5 (no electric charge) and barely penetrate D4. Their masses
     are tiny and nearly degenerate. Near-degeneracy produces large mixing (two nearly
     equal wells have maximally mixed eigenstates).

5. **CP violation from phase structure:** The CP-violating phases in CKM and PMNS encode
   the relative orientation of the three-generation structure between the flavor and mass
   bases. In DFC, the three generations come from the three-dimensional fundamental
   representation of SU(3). The CP phase is the relative phase angle between the SU(3)
   color structure at D7 and the SU(2) weak structure at D6 across the three generations.

**Key open derivation:** Compute the CKM and PMNS matrix elements from the depth anchoring
geometry. The target values are the nine CKM matrix elements and the three PMNS mixing
angles. A successful derivation would be a major Criterion A result.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Mixing exists | Mass/flavor basis mismatch at D6/D4 boundary | CKM and PMNS both measured | ✓ structural |
| CKM near-diagonal | D6-D7 proximity aligns bases for quarks | V-ud ≈ 0.974, V-us ≈ 0.225 | argument direction only ✗ |
| PMNS large angles | D4 near-degeneracy for neutrinos produces large mixing | theta-23 ≈ 49° | argument direction only ✗ |
| CKM small vs PMNS large | D7 anchoring breaks mass degeneracy for quarks | Confirmed pattern | argument direction only ✗ |
| CP phase nonzero | Relative phase between D7 and D6 orientation | delta-CKM ≈ 1.2 rad | not yet derived ✗ |

---

## Open Questions

1. **Derive the Cabibbo angle:** The Cabibbo angle (theta-C ≈ 13°) is the dominant CKM
   mixing angle between the first and second quark generations. Computing it from DFC depth
   geometry would be a significant Tier 2 result.

2. **Explain the CKM/PMNS asymmetry:** Derive from first principles why quark mixing is
   small (CKM near-diagonal) while lepton mixing is large (PMNS has large angles). The
   argument that D7 anchoring aligns the quark bases while D4 near-degeneracy misaligns
   the neutrino bases needs quantitative development.

3. **GIM mechanism from DFC:** The GIM mechanism (Glashow-Iliopoulos-Maiani) explains why
   flavor-changing neutral currents are suppressed. In the SM it follows from the unitary
   CKM matrix. What is the DFC account of the GIM mechanism?

---

## Connections

- `phenomena/particle_physics/neutrino_oscillations.md` — PMNS matrix observables
- `phenomena/particle_physics/cp_violation.md` — CP phases in CKM and PMNS
- `phenomena/particle_physics/particles/quarks.md` — D7 anchoring and quark masses
- `phenomena/particle_physics/particles/neutrinos.md` — D4 anchoring and neutrino masses
- `foundations/three_generations.md` — why three generations exist
- `foundations/mass_hierarchy.md` — depth anchoring and mass scales
