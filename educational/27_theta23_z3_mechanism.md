# Module 27 — The Atmospheric Mixing Angle: Why Neutrinos Break a Symmetry by Exactly the Right Amount

**Series:** DFC Educational Modules — each module is self-contained and can be read
independently. For background on neutrino masses, see Module 21 (Neutrino Masses).
For the center vortex mechanism, see Module 09 (I₄ Identity) and Module 10 (Cascade
Uniqueness).

**Context:** This module documents the identification of the Z₃ holonomy mechanism
for the θ₂₃ neutrino mixing angle deviation in Cycle 364. It is written in a
journaling style — capturing the reasoning, discovery process, and physical
interpretation at the moment the result was found.

---

## The Problem: A Mixing Angle That Should Be 45° But Isn't

Neutrinos come in three flavors: electron, muon, and tau. When a neutrino propagates
through space, the flavor states mix — a neutrino born as a muon neutrino has a
probability of being detected as a tau neutrino. This mixing is described by three
angles, and the one that governs muon-to-tau mixing is called θ₂₃, the "atmospheric
mixing angle" (because it was first measured in atmospheric neutrino experiments).

The observed value is θ₂₃ ≈ 49.26° ± 0.79°. This is close to 45° — the value that
would mean muon and tau neutrinos mix with perfect symmetry — but not exactly 45°.
The deviation is about 4°, and it is statistically significant.

In DFC, the three neutrino generations correspond to three winding numbers (n = 1, 2, 3)
on the S³ sphere at D6 depth. The muon (n = 2) and tau (n = 3) are related by a Z₂
exchange symmetry of S³ — swapping the two hemispheres. This symmetry predicts
θ₂₃ = 45° exactly. A previous analysis (Cycle 209) proved rigorously that the
neutrino depth correction δd = 1/(6π), which governs mass splittings, cannot shift
θ₂₃ at all — it acts identically on both muon and tau because their D6 depths are
equal. The mixing angle problem and the mass ratio problem are independent.

So where does the 4° come from?

---

## The Clue: What Lies Below D6

The D6 depth is where SU(2) closure behavior produces the three generations. But
below D6 lies D7, where SU(3) closure produces the strong force. The D7 structure
has a feature that D6 does not: a Z₃ center symmetry.

The center of SU(3) is the group Z₃ = {1, z₃, z₃²}, where z₃ = exp(2πi/3). Every
SU(3) representation carries a Z₃ charge — its "triality" — determined by how it
transforms under the center. The fundamental representation has triality 1, the
anti-fundamental has triality 2, and the adjoint has triality 0.

The key insight is that the three generation winding numbers n = 1, 2, 3 at D6
acquire Z₃ charges q = n mod 3 when they cross the D7 threshold:

| Generation | Winding n | Z₃ charge q = n mod 3 | Z₃ phase | Status |
|---|---|---|---|---|
| Electron | 1 | 1 | z₃ = exp(2πi/3) | Z₃ charged |
| Muon | 2 | 2 | z₃² = exp(4πi/3) | Z₃ charged |
| Tau | 3 | 0 | 1 | Z₃ neutral |

The tau, with winding number 3, has q = 3 mod 3 = 0. It is a Z₃ singlet — completely
transparent to the D7 confinement mechanism. The muon, with q = 2, carries Z₃ charge
and interacts with the D7 center vortex background.

This is a structural, parameter-free result. It follows from the definition of
modular arithmetic and the fact that the D7 gauge group is SU(3), which has a
Z₃ center. No fitting is involved.

---

## The Asymmetry: Center Vortex Factors

The center vortex mechanism provides a concrete measure of how much the D7
confinement affects each generation. The vortex factor for Z₃ charge q is:

F(q) = 1 − cos(2πq/3)

This is the same factor that governs string tension in the center vortex picture
of confinement (Module 09). Computing it for each generation:

- F(1) = 1 − cos(2π/3) = 3/2 (electron)
- F(2) = 1 − cos(4π/3) = 3/2 (muon)
- F(0) = 1 − cos(0) = 0 (tau)

The tau experiences zero D7 confinement correction. The muon experiences a correction
of 3/2. The asymmetry between muon and tau is F(μ) − F(τ) = 3/2 − 0 = 3/2. This
is the structural origin of the μ↔τ symmetry breaking.

Note that the electron and muon have identical vortex factors (both 3/2). The
asymmetry is specifically between the Z₃-charged modes (q = 1, 2) and the
Z₃-neutral mode (q = 0). Only the tau is neutral.

---

## Candidate Formulas: How Close Can We Get?

The Z₃ mechanism tells us the source of the asymmetry, but not the exact formula
relating the vortex factor to the depth shift ε_d that produces θ₂₃ ≠ 45°. The
relationship between the mixing angle and the depth asymmetry is:

θ₂₃ = arctan(exp(ε_d))

where ε_d is a depth shift in units of the compression scale. The observed value
requires ε_d ≈ 0.149 depth units.

We explored seven candidate formulas built from DFC structural quantities. Two
fall within the 1σ experimental window:

| Formula | ε_d | θ₂₃ predicted | Error from observed |
|---|---|---|---|
| N_c/(2N_Hopf) = 1/6 | 0.167 | 49.75° | +0.49° (within 1σ) |
| 1/(2π) | 0.159 | 49.54° | +0.28° (within 1σ) |
| F(2)/(2πI₄) = 9/(16π) | 0.179 | 50.10° | +0.84° |
| F(2)×δd = (3/2)/(6π) | 0.080 | 47.28° | −1.98° |

The formula ε_d = 1/(2π) gives the closest match (+0.28°). The formula
ε_d = N_c/(2N_Hopf) = 1/6 has a cleaner structural interpretation (the ratio
of color degrees of freedom to Hopf modes). The formula ε_d = F(2)/(2πI₄) = 9/(16π)
has the most transparent physical content — the vortex factor divided by the
winding phase and the Casimir — but overshoots by 0.84°.

None of these formulas has been derived from V(φ). They are structural candidates,
not predictions.

---

## What This Result Does and Does Not Achieve

**What it achieves:**
1. Identifies a concrete, parameter-free structural mechanism (Z₃ center holonomy)
   that breaks the μ↔τ Z₂ symmetry. This was previously unknown.
2. Predicts the correct sign: θ₂₃ > 45° (muon neutrino mixes more than the
   symmetric value). The Z₃ correction acts on the muon, not the tau.
3. Provides multiple candidate formulas that match the observed value within or
   near the 1σ experimental uncertainty.
4. Establishes that the same Z₃ center that governs quark confinement also governs
   neutrino mixing angle deviations — a connection not present in the Standard Model.

**What it does not achieve:**
1. No formula is derived from V(φ). The mechanism is identified, but the quantitative
   depth shift is not computed from the substrate field equation.
2. The discrimination between candidate formulas requires solving the D6/D7 Dirac
   boundary value problem — showing how a muon-type kink (n = 2) propagating through
   the D7 SU(3) background acquires a depth shift proportional to its Z₃ charge.
3. The overall tier remains T4 for the quantitative prediction (T1 for the mechanism).

---

## What Remains Open

- **Formal V(φ) derivation:** Solve the D6/D7 BVP for a Dirac fermion with winding
  number n crossing the SU(3) kink background. The Z₃ holonomy matrix z₃^n should
  produce a depth-dependent phase shift that, when projected onto the mass eigenstate
  basis, gives ε_d as a function of F(q) and the kink profile. This would upgrade
  from T4 to T2a.

- **Connection to CKM:** The same Z₃ mechanism should produce the quark mixing angles
  (CKM matrix). The CKM angles are small because quarks interact directly with D7
  confinement (fundamental representation), while neutrino mixing is large because
  neutrinos are D7-neutral at leading order — the Z₃ effect is a correction to an
  otherwise maximal mixing. This connection is structural but not yet quantitative.

- **Octant determination:** Current experiments are consistent with θ₂₃ in either the
  upper octant (> 45°) or the lower octant (< 45°), with a preference for upper.
  DFC predicts the upper octant definitively. This is a falsifiable prediction that
  upcoming experiments (DUNE, Hyper-Kamiokande) will test.

---

## Summary

| Quantity | Value | Tier | Note |
|----------|-------|------|------|
| Z₃ charge table | e(1), μ(2), τ(0) | T1 | n mod 3 |
| Z₃ breaks μ↔τ | q_μ=2 ≠ q_τ=0 | T1 | Structural |
| Vortex asymmetry | F(μ)−F(τ) = 3/2 | T1 | Parameter-free |
| Sign prediction | θ₂₃ > 45° | T1 | Correct |
| Best formula match | 49.54° (1/(2π)) | T4 | +0.28° from observed |
| Structural candidate | 50.1° (9/(16π)) | T4 | +0.84° from observed |
| Overall T10 status | Mechanism T1, formula T4 | T4 | BVP derivation needed |

---

**See also:** Module 21 (Neutrino Masses) for the depth correction δd = 1/(6π).
Module 09 (I₄ Identity) for the kink shape integral. Module 10 (Cascade Uniqueness)
for the cascade mechanism. `equations/neutrino_theta23_z3_mechanism.py` for the full
calculation (14/15 assertions passed). `equations/neutrino_theta23_correction.py` for
the proof that δd cannot shift θ₂₃.
