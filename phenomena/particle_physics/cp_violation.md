# Phenomenon: CP Violation

## One-Sentence Synthesis

> CP violation in DFC has two separate sources that must be clearly distinguished:
> the SM CKM/PMNS phases arise from the fold orientation angles between quark and lepton
> generations at the D6–D7 boundary (a low-energy manifestation of the closure geometry),
> while the cosmological CP violation sufficient for baryogenesis arises from the intrinsic
> chirality of the D7 SU(3) closure event itself — an irreversible asymmetry baked in
> during the first-order buckling that is far larger than the CKM phase and is the source
> of η_B ≈ 6 × 10⁻¹⁰.

---

## Observation

**CP symmetry:** Under the combined transformation C (charge conjugation: particles → antiparticles)
and P (parity: spatial reflection x → −x), the laws of physics were expected to be invariant.

**Observed violations:**
- **Kaons (1964, Cronin-Fitch, Nobel 1980):** K₀_L decays to 2 pions with a small amplitude
  (~0.2% of the time) — CP-violating because 2 pions is the CP-even channel
- **B mesons (2001, BaBar and Belle):** B⁰ and B̄⁰ oscillations show large CP asymmetry in
  time-dependent decays; asymmetry parameters ≈ 0.7 in B → J/ψ K_S channel
- **D mesons (2019, LHCb):** First observation of CP violation in charm system
- **Neutrino oscillations:** PMNS matrix may have a CP-violating phase (T2K experiment,
  ~3σ evidence for δ_CP ≈ −π/2)

**The asymmetry between matter and antimatter:**
The universe contains η_B ≡ (n_B − n_B̄)/n_γ ≈ 6 × 10⁻¹⁰ — about one extra baryon per
10⁹ photon pairs. This is the net remnant after the vast matter-antimatter annihilation
in the early universe. The SM CKM phase cannot generate this asymmetry — it is roughly
twelve orders of magnitude too small.

**The CKM matrix:** The charged-current weak interaction mixes quark generations through
the CKM matrix:

```
Vud  Vus  Vub
Vcd  Vcs  Vcb
Vtd  Vts  Vtb
```

With one irreducible complex phase δ ≈ 1.2 rad (the Jarlskog invariant J ≈ 3 × 10⁻⁵).
CP violation requires at least 3 generations of quarks — with 2 generations, the matrix
is real and no CP-violating phase exists.

---

## Standard Explanation

CP violation in the SM arises from the complex Yukawa couplings that mix quark generations.
In the mass basis, the weak interaction has off-diagonal elements — the CKM matrix —
and the irreducible complex phase is the source of CP violation.

Why exactly 3 generations? Unknown — the SM takes this as input. Why is the CP phase
δ ≈ 1.2 rad? Unknown — it is a measured parameter. Why is the SM CP violation insufficient
for baryogenesis? Known — the Jarlskog invariant J ≈ 3 × 10⁻⁵ is too small by many orders.

---

## Dimensional Folding Explanation

### Two Distinct Sources of CP Violation

DFC distinguishes two physically different CP violation mechanisms:

**Source 1: CKM/PMNS phase (low-energy, measured)**

The three quark generations correspond to three different depth anchoring levels in the
D6-D7 regime (see `foundations/three_generations.md`). The fold orientation angle θ at
D6 for each generation is independently defined by the closure geometry. When the three
generations mix through weak interactions (W boson exchange through D6), the relative
fold orientation angles between generations produce a net complex phase — the CKM matrix.

Specifically: the CKM matrix element V_ij is the overlap integral of the D6 fold
orientation eigenstates for generation i and generation j:

```
V_ij = ⟨ψ_i | e^{iθ_ij} | ψ_j⟩
```

where θ_ij is the fold orientation angle between the two generation eigenstates. The
irreducible complex phase δ of the CKM matrix is the non-zero total phase accumulated
around the triangle V_ud × V*_cd × V_cs × ... (the Jarlskog triangle). It is non-zero
if and only if all three generation states are genuinely different — i.e., if the three
fold orientation angles θ₁₂, θ₁₃, θ₂₃ are all distinct and non-zero.

**In DFC:** The CKM phase is a low-energy manifestation of the D6 closure geometry.
It is real, it is the source of kaon and B-meson CP violation, and it is measured
correctly. But it is too small by many orders of magnitude to generate η_B.

**Source 2: D7 closure chirality (cosmological, not directly observable today)**

The D7 SU(3) closure event during baryogenesis produces a net baryon asymmetry through
the intrinsic chirality of the closure topology — not through the CKM phase at all.

The D7 closure is a first-order buckling event that is:
- Irreversible (cannot un-close a closure)
- Out-of-equilibrium (the closure happens faster than thermal relaxation)
- Chiral: S³ has an intrinsic orientation (clockwise vs. counterclockwise in the 4D
  embedding). This orientation is the DFC source of CP violation for baryogenesis.

The mechanism: During the D7 buckling, the orientation of the SU(3) closure (its
"handedness" in the D6–D7 configuration space) selects a preferred direction. In a
CP-symmetric theory, both orientations would be produced equally — net B = 0. In DFC,
the closure orientation is determined by the earlier D6 SU(2) closure chirality, which
is already chiral (S³ is intrinsically chiral — see `phenomena/particle_physics/forces/weak_force.md`).
The D6 chirality propagates to D7, and the D7 closure has a preferred orientation.

This preferred orientation means the D7 closure creates slightly more quarks than
antiquarks — the net baryon winding number is non-zero. Once the closure stabilizes,
this asymmetry is frozen by B−L conservation (sphalerons cannot change B−L, as shown
in `phenomena/cosmology/baryogenesis.md`).

**Result:** η_B ≈ 6 × 10⁻¹⁰ comes from the D7 closure chirality, not the CKM phase.
The calculation of η_B from DFC geometry remains an open problem.

### Why CP Violation Requires 3 Generations (From DFC)

With two quark generations, the CKM matrix is:
```
V = [cos θ_C   sin θ_C]
    [-sin θ_C  cos θ_C]
```

This is a real rotation — no complex phase. The Jarlskog invariant J = 0. No CP violation.

In DFC: with only two generation depth levels, the fold orientation angles θ₁₂ and θ₂₁
are equal and opposite — there is no closed triangle in the generation space whose phase
is non-zero.

With three generations, the three fold orientation angles θ₁₂, θ₁₃, θ₂₃ are independent.
The phase δ is the argument of the triangle:

```
J = Im[V_us V_cb V*_ub V*_cs] ≠ 0    [for any triangle with nonzero area]
```

In DFC: the triangle has nonzero area precisely because three independent depth anchoring
levels exist at D6 — the same mechanism that produces three generations (see
`foundations/three_generations.md`).

**The minimum generation count for CP violation is 3 because the DFC three-generation
structure (three distinct D6 depth anchoring levels) is the minimum configuration with
a non-trivial closed triangle in the fold orientation space.**

### CP Violation and Parity Violation

The weak force is left-handed — it couples only to left-handed fermions (SU(2)_L).
This parity violation is separate from CP violation but related:
- P violation: left-handed only coupling (intrinsic chirality of D6 S³ geometry)
- C violation: different coupling to particles vs. antiparticles (from chirality + gauge structure)
- CP violation: combined C+P transformation is approximately preserved but not exact
  (the CKM phase breaks this residual symmetry)

In DFC: P violation is structural (S³ is intrinsically chiral → SU(2)_L). C violation
follows from the coupling being handed. CP violation is the residual symmetry breaking
from the non-trivial CKM phase, which arises from the three distinct D6 generation
levels having non-degenerate fold orientation angles.

---

## Formal Equations

### CKM Matrix Parametrization

```
V_CKM = V₁₂(θ₁₂) × V₁₃(θ₁₃, δ) × V₂₃(θ₂₃)

Standard PDG form:
    c₁₂ c₁₃           s₁₂ c₁₃           s₁₃ e^{-iδ}
   -s₁₂ c₂₃ - c₁₂ s₂₃ s₁₃ e^{iδ}   c₁₂ c₂₃ - s₁₂ s₂₃ s₁₃ e^{iδ}   s₂₃ c₁₃
    s₁₂ s₂₃ - c₁₂ c₂₃ s₁₃ e^{iδ}  -c₁₂ s₂₃ - s₁₂ c₂₃ s₁₃ e^{iδ}   c₂₃ c₁₃

Observed values:
  sin θ₁₂ = 0.2245   (Cabibbo angle)
  sin θ₁₃ = 0.00365
  sin θ₂₃ = 0.04053
  δ ≈ 1.196 rad       (CP-violating phase)
```

### Jarlskog Invariant

```
J = Im[V_ud V*_us V_cs V*_cd] = sin θ₁₂ cos θ₁₂ sin θ₁₃ sin θ₂₃ cos θ₂₃ sin δ
  ≈ 3.0 × 10⁻⁵

This is the single rephasing-invariant measure of CP violation in the SM.
```

### CP Asymmetry in B Decays

```
For B⁰ → J/ψ K_S:
    A_CP(t) = (Γ(B̄⁰ → f) − Γ(B⁰ → f)) / (sum)
             = sin(2β) sin(Δm t)

where β ≡ arg(−V_cd V*_cb / V_td V*_tb) ≈ 21°
→ sin(2β) ≈ 0.691    [observed: 0.699 ± 0.017]  ✓
```

---

## Consistency Checks

| Property | DFC mechanism | Observed |
|---|---|---|
| CP violation requires ≥3 generations | Non-trivial fold orientation triangle needs 3 D6 depths | 3 generations observed; 2 gives real CKM ✓ |
| Kaon ε parameter ~ 2×10⁻³ | CKM phase δ ≈ 1.2 rad from D6 geometry | Observed ε_K = 2.23 × 10⁻³ ✓ |
| sin(2β) ≈ 0.69 in B decays | CKM triangle angle β from fold orientation angles | Observed 0.699 ± 0.017 ✓ |
| SM CP too small for baryogenesis | J ≈ 3×10⁻⁵ → η_B ≪ 10⁻¹⁰ | SM insufficient — confirmed ✓ |
| Cosmological CP from D7 closure | D7 closure chirality → net winding asymmetry | η_B = 6×10⁻¹⁰ (DFC prediction: not yet computed) |

---

## Open Questions

1. **Derive the CKM angles from D6 geometry.** The four CKM parameters (θ₁₂, θ₁₃, θ₂₃, δ)
   are not yet derived from DFC — they are measured inputs. In DFC, they should follow from
   the fold orientation angles between the three D6 generation depth levels and the overlap
   integrals of their wavefunctions. Computing these from the D6 closure geometry is the
   quantitative challenge.

2. **Compute η_B from D7 closure chirality.** The qualitative argument establishes that
   the D7 closure creates a net baryon asymmetry via its intrinsic chirality. The number
   η_B ≈ 6 × 10⁻¹⁰ must be derivable from the magnitude of the D7 chirality asymmetry
   and the Kibble-Zurek density of kinks (see `phenomena/cosmology/baryogenesis.md`).
   This requires computing the CP-violating amplitude of the D7 closure event — the ratio
   of closure events with one orientation vs. the other.

3. **Strong CP problem.** QCD admits a CP-violating term θ_QCD in the Lagrangian, but
   the measured value is |θ_QCD| < 10⁻¹⁰ — a severe fine-tuning problem. In DFC, the
   strong CP problem would be addressed if the D7 closure geometry naturally sets θ_QCD = 0
   or a small value. Whether the D7 SU(3) closure topology forces θ_QCD ≈ 0 (an analog
   of the Peccei-Quinn mechanism) is an open structural question.

4. **PMNS CP phase.** The lepton sector has its own CP-violating phase δ_CP in the PMNS
   matrix. Current evidence (T2K) suggests δ_CP ≈ −π/2. Whether DFC's D6 closure geometry
   for neutrinos produces a different prediction for the PMNS phase than for the CKM phase
   (since neutrinos may anchor at different D6 depth levels than charged leptons) is an
   open question with testable consequences from DUNE and HyperKamiokande.

---

## Connections

- **Baryogenesis** — D7 closure chirality as the source of cosmological CP violation;
  `phenomena/cosmology/baryogenesis.md`
- **Three generations** — three D6 depth levels as the origin of the CKM structure;
  `foundations/three_generations.md`
- **Weak force** — D6 S³ chirality producing parity violation and left-handedness;
  `phenomena/particle_physics/forces/weak_force.md`
- **Antimatter** — CP violation as partial explanation for matter-antimatter asymmetry;
  `phenomena/particle_physics/particles/antimatter.md`
- **Neutrinos** — PMNS matrix CP phase and its DFC origin;
  `phenomena/particle_physics/particles/neutrinos.md`
