# DFC Scientific Merit Criteria

This document defines the objective standards by which this project evaluates its own
scientific status. Referenced from CLAUDE.md. These criteria are permanent and apply at
every stage of development. They exist to distinguish genuine progress from apparent
progress, and to keep the project anchored to physics rather than to internal narrative
consistency.

---

## Tier System for Claims

Every claim in this project is assigned to one of five tiers. The tier determines what
is required to consider the claim substantiated. **Tier assignment is not permanent** —
a claim moves up when additional derivation is completed.

---

**Tier 0 — Core Postulates** *(inputs; not derived; define the model)*

Tier 0 items are the starting assumptions of the model. They cannot be evaluated as
right or wrong in isolation — only their consequences can be tested. They must be stated
explicitly and kept minimal. Any postulate that can be derived from another within the
model should be demoted to a lower tier.

Current Tier 0 postulates:
1. There is one continuous self-compressing field. No pre-existing space, gauge group,
   or dimensional structure is assumed.
2. The field's self-interaction potential has the double-well form V(φ) = −α/2 φ² + β/4 φ⁴.
   The quadratic coupling alpha and quartic coupling beta are free parameters of the model.
3. Bifurcation events — points at which the compressed field opens a new degree of
   freedom rather than compressing further — produce all structure observed as particles,
   forces, and spacetime.

---

**Tier 1 — Structural Predictions** *(logical consequences of Tier 0; no quantitative free parameters)*

Tier 1 claims are qualitative or topological. Substantiated when: (a) the logical
argument from Tier 0 is written out completely with no missing steps, and (b) the claim
matches the observed qualitative feature.

Current Tier 1 claims:

| Claim | Logical basis | Status |
|---|---|---|
| Proton absolutely stable | Product topology U(1)×SU(2)×SU(3) has no baryon→lepton path | Argument written ✓ |
| Exactly three fermion generations | SU(3) fundamental rep has dimension 3 | Argument written; Cycle 35 ✓ |
| Photon is massless, propagates at c | Massless KG dispersion: ω∝k | Derived from field equation ✓ |
| Exactly two photon polarizations | One angular DOF (S¹) has two transverse projections | Structural argument ✓ |
| Parity violation in weak force | JR zero mode at positively wound D6 kink is left-handed | Cycle 41 ✓ |
| Spin-1/2 is minimum spin | FR winding N=1 + JR zero mode | Cycle 33 ✓ |
| Space appears three-dimensional | Three DOFs emerge at D3 localization depth | Structural; not derived ✗ |
| Binary measurement outcomes | Z₂ configuration space of substrate | Cycle 36 ✓ |

---

**Tier 2 — Quantitative Predictions** *(computed from substrate parameters; compared to measurement)*

Substantiated when all four conditions are met:
1. Runnable equation module takes substrate parameters as input and produces the number.
2. No circular steps — the target quantity does not appear as an input anywhere.
3. Predicted value matches observed value within 5% (or stated theoretical uncertainty).
4. Number of free parameters is explicitly stated.

Tier 2a — **Verified** (see CLAUDE.md for current table)

Tier 2b — **Failing** (equation exists, >5% error; see CLAUDE.md)

---

**Tier 3 — Correspondences** *(consistent with observation; not yet derived from Tier 0)*

Tier 3 items must be labeled as "working hypothesis" in all documents. The goal is to
promote to Tier 2 (complete the derivation) or discard (derivation path closes).

Current Tier 3 items:

| Item | Why it is Tier 3 | Path to Tier 2 |
|---|---|---|
| D5 depth produces U(1) behavior | Consistent with Hopf S¹ correspondence | Derive DOF count per bifurcation from substrate field equation |
| D6 depth produces SU(2) behavior | Same as above for S³ | Same path |
| D7 depth produces SU(3) behavior | Same as above for S⁵; confinement supports termination | Same path plus formal confinement argument |
| V = −α/2 φ² + β/4 φ⁴ form | Postulated; consistent with known symmetry-breaking physics | Derive from self-interaction dynamics of a compressing 1D field |

---

**Tier 4 — Claims Awaiting Resolution** *(stated but neither derived nor falsified)*

Tier 4 items have no supporting derivation and no equation module. They are placeholders
for future work, not results. Must be labeled "open" in all documents.

Examples: derivation of Planck's constant from substrate; derivation of the cosmological
constant; derivation of matter-antimatter asymmetry; quark mass spectrum beyond e/μ;
neutrino masses beyond qualitative correspondence.

---

## Criteria for Novel Scientific Contribution

The project makes a genuine novel scientific contribution if and only if it satisfies at
least one of the following four criteria.

**Criterion A — Derives a SM postulate without circular import:**
The model produces a quantity the Standard Model takes as an unexplained input parameter,
without importing that quantity at any step.

Current candidates: gauge coupling from beta (heuristic; not yet rigorous); three
generations from SU(3) topology (structural; complete); proton stability from product
topology (structural; complete).

**Criterion B — Makes a prediction the SM cannot make:**
The model predicts a specific numerical value for a quantity the Standard Model does not
predict, and the prediction is testable in principle.

Current candidates: absolute proton stability (SM predicts only suppressed decay; DFC
predicts strictly zero from topology); β-g coupling relationship (if holonomy derivation
is made rigorous).

**Criterion C — Provides a structural explanation for a SM pattern:**
The model explains why a feature of the SM has the form it does. Must be specific enough
to rule out alternatives.

Current candidates: parity violation in weak force (JR zero mode chirality); three
generations (SU(3) rep dimension 3); product gauge group (independent closure thresholds).

**Criterion D — Passes an independent consistency check:**
A quantity computed by two different paths gives the same answer, and the agreement is
not guaranteed by construction.

Current candidate: common gauge coupling from SM running (0.5443) vs. substrate formula
using only β (0.5423, 0.4% agreement).

---

## Completeness Milestones

**Phase 1 — Structural coherence (~30%):** All Tier 1 claims have complete logical
arguments. The qualitative structure is internally consistent.

**Phase 2 — Quantitative contact (~50%):** At least five Tier 2a predictions match
within 5%. EM coupling, Weinberg angle, and Higgs mass all in Tier 2a.

**Phase 3 — Coupling sector complete (~70%):** All three force couplings derived to
within 5% with no free parameters beyond (α, β). D-depth assignments promoted to Tier 2.

**Phase 4 — Parameter-free (~85%):** β derived from a pre-substrate condition.
V(φ) form derived from compression dynamics. Free parameters reach zero.

**Phase 5 — Scientifically rigorous (~95%):** All Tier 4 failures resolved or formally
shown to require extension. At least one prediction satisfies Criterion A or B.

---

## Evaluation Checklist for New Derivations

When promoting a claim up the tier ladder, apply this checklist:

- [ ] Can the derivation be stated in natural language without any symbol not definable in words?
- [ ] Does the derivation chain start only from Tier 0 postulates and previously substantiated results?
- [ ] Is the target quantity absent from the right-hand side of every step?
- [ ] Is there a runnable equation module that produces the predicted number?
- [ ] Is the percent discrepancy from observation computed and printed by the module?
- [ ] Is the number of free parameters explicitly counted and printed?
- [ ] Is there at least one Consistency Check table row testing against an independent check?

If any item is unchecked, the claim remains at its current tier until satisfied.
