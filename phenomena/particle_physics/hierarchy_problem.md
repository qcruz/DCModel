# Phenomenon: The Hierarchy Problem

## One-Sentence Synthesis

> The hierarchy problem — why the Higgs boson mass of 125 GeV is stable against quantum
> corrections that should push it to the Planck scale of 10¹⁹ GeV — is dissolved in DFC
> because the Higgs is not a fundamental scalar field with a postulated mass but the
> breathing mode of a geometric modulus (the squashing parameter of the D6 S³ closure),
> whose mass is radiatively generated at the closure scale and protected below that scale
> by the geometric symmetry of the S³ — the same symmetry that prevents the squashing
> parameter from acquiring a large vacuum expectation value at sub-closure energies.

---

## Observation

The Standard Model contains a fundamental scalar field (the Higgs field) with a tree-level
mass parameter of 125 GeV. Quantum corrections from virtual particles running in loops
contribute to the Higgs mass squared at every order of perturbation theory:

- **Top quark loop:** Contributes delta-m-H-squared ≈ −(3/8 pi squared) times the top
  Yukawa coupling squared times the UV cutoff squared. With a cutoff at the Planck scale
  (~10¹⁹ GeV), this gives delta-m-H-squared ≈ −(10³⁶ GeV²), roughly 10³⁰ times the
  observed Higgs mass squared.
- **Fine-tuning:** To get a Higgs mass of 125 GeV with a Planck-scale cutoff, the bare
  mass parameter and the radiative correction must cancel to 1 part in 10³⁰. This
  extraordinary cancellation has no structural explanation in the SM.
- **The naturalness criterion:** A physical quantity is "natural" if its value is stable
  against small changes in the theory's parameters. The Higgs mass is unnatural: changing
  the bare mass by one part in 10³⁰ changes the physical mass by 100%.
- **Proposed solutions:** Supersymmetry (cancels loop corrections with superpartners),
  Randall-Sundrum extra dimensions (Planck scale is an illusion), composite Higgs
  (Higgs is not fundamental), little Higgs, twin Higgs. None confirmed experimentally.

---

## Standard Explanation

The hierarchy problem exists because the Standard Model has no mechanism to protect scalar
field masses from large radiative corrections. Every other SM particle's mass is either
forbidden by gauge symmetry (photon, gluon) or protected by chiral symmetry (fermions:
setting mass to zero restores a symmetry). But scalar fields have no such protection:
the mass-squared term is gauge-invariant and there is no symmetry that forces it to zero.
So quantum corrections drive scalar masses to the highest scale in the theory.

SUSY solves this by pairing every scalar with a fermion whose loop diagram has the opposite
sign, canceling the divergence exactly when SUSY is unbroken. The absence of SUSY partners
at the LHC up to ~2 TeV has pushed fine-tuning concerns back into the SUSY parameter space.

---

## Dimensional Folding Explanation

**STUB — full derivation not yet written.**

**DFC mechanism direction:**

In DFC, the hierarchy problem dissolves structurally. The key insight is that the Higgs
is not a fundamental scalar field but a geometric modulus. The argument:

1. **The Higgs is a geometric modulus, not a fundamental scalar:** The Higgs field is the
   squashing parameter epsilon of the D6 S³ closure (see `foundations/higgs_geometry.md`).
   It is not an independent field postulated to break electroweak symmetry; it is the
   breathing mode of the D6 closure geometry. Its potential is determined by the geometry
   of S³ squashing, not by an arbitrary scalar potential.

2. **The mass is radiatively generated at the closure scale:** The Higgs mass is generated
   by top quark loops evaluated with a UV cutoff at the closure scale (approximately 10¹³
   GeV for D5/D6), not at the Planck scale. The top quark loop gives a mass of order the
   top quark mass times the top Yukawa coupling over 4 pi, evaluated with a closure-scale
   cutoff. This is why m-H ≈ 125 GeV is in the right ballpark. The calculation is done
   in `foundations/higgs_mass_derivation.md`.

3. **Protection by geometric symmetry below the closure scale:** Below the closure scale,
   the S³ squashing parameter is protected by the geometric symmetry of the S³. The S³
   cannot be continuously deformed to zero squashing without passing through an energy
   barrier set by the closure scale. This is the DFC analog of the symmetry protection
   that protects fermion masses: just as chiral symmetry prevents fermion mass corrections
   from growing without bound, the S³ geometric symmetry prevents the squashing parameter
   from receiving large corrections below the closure scale.

4. **No large corrections from Planck-scale physics:** In DFC, the Planck scale is not a
   fundamental UV cutoff for Higgs physics. It is the scale of D1 compression — the kink
   width at D1 equals the Planck length, but this does not introduce Planck-scale corrections
   to the D6 closure geometry because D1 and D6 are separated by multiple bifurcation events.
   The hierarchy of scales (Planck >> D6 closure >> Higgs mass) is not a fine-tuning but
   the natural output of the bifurcation cascade.

5. **Why no SUSY partners:** DFC does not predict supersymmetry. The hierarchy problem
   does not require SUSY in DFC because the alternative protection mechanism (geometric
   symmetry of the closure modulus) is already present. SUSY would require a separate
   closure structure not produced by the D1→D7 bifurcation sequence.

**Key open derivation:** Formalize the protection argument. Show that radiative corrections
to epsilon receive contributions only from scales between the D6 closure scale and the
Higgs mass — not from Planck-scale physics. This requires computing the effective potential
for epsilon as a function of the renormalization scale, with the closure scale as the
UV boundary condition.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Higgs mass in right range | Generated radiatively at closure scale by top loop | 125.25 GeV | ✓ (124.4 ± 3.7 GeV from higgs_mass_derivation.md) |
| No Planck-scale fine-tuning | Geometric protection below closure scale | Hierarchy is stable experimentally | ✓ structural (argument written) |
| No SUSY partners | DFC does not produce SUSY | No SUSY below ~2 TeV at LHC | ✓ (correct absence prediction) |
| Closure-scale UV cutoff | Radiative corrections cut off at D6 scale, not Planck | — | not yet formally derived ✗ |

---

## Open Questions

1. **Formal proof of geometric protection:** Show that the S³ squashing parameter epsilon
   does not receive corrections larger than the closure scale from any loop diagram in the
   DFC effective theory below that scale. This is the DFC analog of the chiral symmetry
   argument for fermion masses.

2. **Why the closure scale is 10¹³ GeV, not Planck:** Explain structurally why D6 closes
   at 10¹³ GeV rather than 10¹⁹ GeV (Planck) or 10¹⁵ GeV (GUT). This is connected to
   Bottleneck 1 (D-depth assignment mechanism).

3. **Little hierarchy problem:** The LHC has found no new particles below ~2 TeV. In most
   SUSY/composite Higgs models, this creates a "little hierarchy problem" (residual
   fine-tuning). In DFC, what is the prediction for new physics between 100 GeV and 10 TeV?
   If the closure scale is 10¹³ GeV, there should be no new DFC particles below that scale
   except the SM spectrum.

---

## Connections

- `foundations/higgs_geometry.md` — Higgs as S³ squashing parameter
- `foundations/higgs_mass_derivation.md` — radiative mass generation at closure scale
- `phenomena/particle_physics/mass_generation.md` — mass generation mechanism
- `phenomena/particle_physics/particles/higgs_boson.md` — Higgs boson as modulus mode
- `foundations/planck_constant_derivation.md` — Planck scale vs. closure scale hierarchy
