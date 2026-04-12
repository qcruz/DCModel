# Phenomenon: Atomic Structure and the Hydrogen Spectrum

## One-Sentence Synthesis

> Atomic structure is the bound-state spectrum of the compression field equation for a
> D5 U(1) kink (the electron) in the Coulomb field of a D5 U(1) source (the proton) —
> the hydrogen energy levels E-n equal negative 13.6 electron volts divided by the
> square of the principal quantum number, following from the same Klein-Gordon equation
> that produces the free electron, evaluated in the 1/r attractive potential produced by
> the proton's D5 winding number; the fine structure constant alpha equals approximately
> 1/137 and sets the energy scale of atomic physics through the ratio of the electron's
> electromagnetic interaction energy to its rest mass energy — but alpha is not yet
> derived from DFC substrate parameters.

---

## Observation

The hydrogen atom emits and absorbs light only at specific discrete wavelengths, organized
into series:

- **Lyman series** (ultraviolet): transitions to the ground state (n=1); first line at
  121.6 nm (Lyman-alpha)
- **Balmer series** (visible): transitions to n=2; first line at 656.3 nm (H-alpha, red)
- **Paschen series** (infrared): transitions to n=3

The Rydberg formula gives the wavenumber of each transition as the Rydberg constant times
the difference of inverse squares of the two principal quantum numbers.

- **Ground state energy:** −13.606 eV (ionization energy of hydrogen)
- **Energy levels:** E-n = −13.606/n² eV (n = 1, 2, 3, ...)
- **Fine structure:** Transitions have small splittings from spin-orbit coupling and
  relativistic corrections, of order alpha squared times the ground state energy (~0.1 meV)
- **Lamb shift:** A further splitting of order alpha cubed from quantum electrodynamic
  corrections (vacuum polarization, electron self-energy); first measured by Lamb and
  Retherford (1947), 1058 MHz for the 2s-2p splitting in hydrogen
- **Hyperfine structure:** Interaction between electron and proton magnetic moments;
  the famous 21 cm line (1.420 GHz), used in radio astronomy

---

## Standard Explanation

The hydrogen atom is solved by the Schrödinger equation (or Dirac equation for relativistic
corrections) for an electron in a Coulomb potential proportional to the inverse of the
electron-proton separation. Quantization of angular momentum gives discrete energy levels.
The energy depends only on the principal quantum number n at leading order; fine structure
depends on the orbital angular momentum and spin quantum numbers through spin-orbit coupling.

The Lamb shift requires quantum field theory: the electron interacts with the quantized
electromagnetic field (virtual photon emission and reabsorption), shifting the 2s level
up relative to the 2p level by an amount calculable in QED to extraordinary precision
(agreement with experiment at the 10⁻¹² level — the most precisely tested prediction
in all of science).

---

## Dimensional Folding Explanation

**STUB — full derivation not yet written.**

**DFC mechanism direction:**

Atomic structure is the first place DFC's QM sector and EM sector meet in a quantitative
calculation. It is therefore a critical Tier 2 target.

1. **The Coulomb potential from D5 closure:** The proton carries D5 U(1) winding number
   +1. The connection field of the D5 U(1) closure (the photon field) mediates an
   inverse-square force between D5 winding numbers. This is the Coulomb potential,
   already accounted for in `phenomena/electromagnetism/electromagnetism.md`. In DFC,
   the 1/r dependence follows from the massless D2 mode's spreading in three apparent
   spatial dimensions.

2. **The bound state from the KG equation:** The electron (a D5+D6 closure kink) satisfies
   the Klein-Gordon equation (non-relativistic limit: the Schrödinger equation) in the
   proton's Coulomb potential. The discrete energy spectrum of bound states follows
   directly from the boundary condition that the wavefunction must be normalizable —
   the electron's amplitude must fall off at large distances and must be non-singular
   at the origin.

3. **Energy scale set by the fine structure constant:** The ground state energy equals
   one-half times the electron mass times the square of the fine structure constant,
   where alpha equals approximately 1/137. The fine structure constant is the dimensionless
   ratio of the electromagnetic coupling strength (the square of the D5 winding number's
   coupling constant) to the quantum of action. In DFC, alpha equals the common gauge
   coupling squared divided by 4 pi at the atomic scale — but running from the closure
   scale down to atomic energies must be computed. This is a Tier 2 target dependent
   on the coupling derivation in `equations/coupling_derivation.py`.

4. **Fine structure from spin-orbit coupling:** The electron's spin (D6 SU(2) Jackiw-Rebbi
   zero mode) couples to the magnetic field it sees in its own rest frame (the proton's
   electric field Lorentz-boosted). This coupling is already present in the Dirac equation
   that the D6 zero mode satisfies. The fine structure splitting is of order alpha squared
   times the ground state energy — a structural prediction that follows from the D5/D6
   coupling hierarchy.

5. **Lamb shift from vacuum fluctuations:** Requires the DFC account of quantum vacuum
   fluctuations (massless D2 mode zero-point oscillations). This connects to
   `phenomena/quantum/casimir_effect.md`. The Lamb shift calculation is a high-precision
   Tier 2 target for the future.

**Key open derivation:** The ground state energy E-1 = −alpha squared times m-e times c
squared divided by 2. This requires knowing alpha from `equations/coupling_derivation.py`.
With the current heuristic value alpha-em ≈ 1/129.6 at the Z scale, running to atomic
energies (~1 eV) gives alpha ≈ 1/137.4 (very close to 1/137.036). Computing the hydrogen
ground state energy from DFC parameters would be a first Tier 2 atomic physics result.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Discrete spectrum exists | Bound states from normalizable KG solutions | Confirmed — discrete spectral lines | ✓ structural |
| 1/n² energy scaling | Coulomb potential in 3 apparent spatial dimensions | E-n = −13.6/n² eV | ✓ structural (from KG) |
| Ground state energy | E-1 = −alpha²/2 × m-e × c² | −13.606 eV | not yet derived (requires alpha) ✗ |
| Balmer series wavelengths | From Rydberg formula with DFC alpha | H-alpha = 656.3 nm | not yet derived ✗ |
| Fine structure splitting | Order alpha squared | ~0.1 meV for H | not yet derived ✗ |

---

## Open Questions

1. **Compute the Rydberg constant from DFC parameters:** R-infinity equals the electron mass
   times c times alpha squared divided by 2 times Planck's constant. This requires both alpha
   and the electron mass from substrate parameters. It is the most basic quantitative atomic
   physics prediction.

2. **Run alpha from closure scale to atomic scale:** Use the QED beta function to run alpha
   from the Z mass scale (where coupling_derivation.py gives 1/129.6) down to atomic energies
   (where alpha = 1/137.036). Verify that DFC alpha at the atomic scale matches.

3. **Hydrogen fine structure from spin-orbit:** Derive the fine structure splitting from the
   D5/D6 coupling in the Dirac equation for the D6 Jackiw-Rebbi zero mode.

4. **Lamb shift from DFC vacuum modes:** Compute the Lamb shift from the DFC account of
   vacuum fluctuations. This would be the most stringent precision test of the model.

---

## Connections

- `phenomena/electromagnetism/electromagnetism.md` — Coulomb potential from D5 U(1) closure
- `phenomena/particle_physics/particles/electron.md` — electron as D5+D6 zero mode
- `phenomena/quantum/quantum_mechanics.md` — Schrödinger equation from KG
- `phenomena/quantum/casimir_effect.md` — vacuum fluctuations (needed for Lamb shift)
- `equations/coupling_derivation.py` — alpha-em from beta (needed for Rydberg constant)
- `foundations/mass_hierarchy.md` — electron mass from substrate parameters
