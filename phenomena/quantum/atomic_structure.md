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

### The Coulomb Potential from D5 U(1) Closure

The proton carries D5 U(1) winding number plus one. The connection field of the D5 U(1)
closure — the photon field — mediates a force between D5 winding numbers proportional to
the product of winding numbers and inversely proportional to the distance between them.
This is the Coulomb potential. Its 1/r dependence follows from the massless D2 mode
spreading uniformly through the three apparent spatial degrees of freedom produced at D3
(see `phenomena/electromagnetism/electromagnetism.md`).

### Bound States from the Klein-Gordon Equation

The electron (a D5+D6 closure kink) satisfies the Klein-Gordon equation in the proton's
Coulomb potential. In the non-relativistic limit, this reduces to the Schrödinger equation.
The wavefunction must be normalizable — it must decay at large distances from the proton and
remain non-singular at the origin. These two boundary conditions together restrict the
allowed energies to a discrete set. The principal quantum number n counts the number of
radial nodes in the wavefunction and determines the energy level.

### The Energy Scale: Fine Structure Constant

The ground state energy — the energy required to ionize hydrogen from its lowest energy
state — is one-half times the electron rest mass energy times the square of the fine
structure constant:

```
E_1 = -m_e c² α²/2
```

where the fine structure constant alpha equals approximately one part in 137. The fine
structure constant is the dimensionless ratio characterizing the strength of the
electromagnetic coupling: the square of the gauge coupling constant g, divided by four
pi. In DFC, alpha at atomic energies is obtained by running the coupling constant alpha
at the Z boson mass scale down to atomic energies using the standard QED renormalization
group equation, then applying the formula above.

### The DFC Coupling Chain to Atomic Physics

The full chain, verified in `equations/atomic_structure.py`:

1. The substrate quartic coupling beta equals 0.0351, inferred from the bifurcation
   dynamics (see `equations/bifurcation_dynamics.py`)

2. The common gauge coupling squared equals eight pi times beta divided by three,
   giving g-common equal to 0.5423 — a 0.37% match to the Standard Model value of 0.5443
   (see `equations/coupling_derivation.py`)

3. The electromagnetic coupling at the Z mass scale follows from the Weinberg angle
   (Route 3B) giving alpha-em at M_Z of approximately 1/129.6 (observed 1/127.9, a 1.3%
   discrepancy)

4. One-loop QED running from M_Z down to the electron mass scale, summing contributions
   from all charged fermions lighter than M_Z, adds approximately 10.46 to the inverse
   coupling, giving alpha-em at atomic energies of approximately 1/140 (observed 1/137.036,
   a 2.1% discrepancy)

5. The ground state energy from the formula above: approximately minus 13.03 eV (observed
   minus 13.60 eV, a 4.2% discrepancy — the energy error is twice the fractional alpha
   error because energy is proportional to alpha squared)

### The 1/n² Spectrum: Derived

The scaling of energy levels with the inverse square of the principal quantum number
follows from the structure of the Coulomb-bound Schrödinger equation and requires no
additional DFC input beyond the existence of the 1/r Coulomb potential. This structural
prediction — that the ratio E_2/E_1 equals 1/4, the ratio E_3/E_1 equals 1/9, and so on
— is exact within the non-relativistic approximation and is confirmed by spectroscopy
to high precision.

### Error Budget

Every spectral line predicted by DFC is off by approximately 4.2%. This is not random
scatter but a systematic offset from a single source: the 1.27% error in alpha-em at
M_Z propagates through the QED running (where it roughly doubles to 2.1%), and then
doubles again because the energy is proportional to alpha squared. The ratio of any two
spectral lines (such as Lyman-alpha to H-alpha) is correct to the level of these
calculations, since the error cancels in the ratio.

Improving alpha-em at M_Z to below 0.5% accuracy would bring the hydrogen ground state
energy prediction to below 1% precision. The path to this improvement runs through the
rigorous derivation of the closure radius ratio from the substrate field equation (see
`foundations/coupling_derivation.md`), which is currently the principal open item in
the DFC coupling chain.

---

## Formal Equations

```
Bound state energy levels (non-relativistic):
    E_n = -m_e c² α²/(2n²)        n = 1, 2, 3, ...

Rydberg energy:
    E_Ry = m_e c² α²/2            [energy to ionize from n=1]

Photon energy in transition n_upper → n_lower:
    ΔE = E_Ry × (1/n_lower² − 1/n_upper²)   [positive — emitted photon energy]

Wavelength (requires hc as input — ℏ not derived from DFC):
    λ = hc / ΔE

DFC coupling chain (verified in equations/atomic_structure.py):
    β = 0.0351
    g² = 8πβ/3 → g_common = 0.5423
    α_em(M_Z) = α₂ × sin²θ_W = 0.007719   [obs: 0.007818, 1.3% off]
    Δ(1/α) from QED running (M_Z → m_e) = 10.46
    α_em(m_e) = 1/140.0                    [obs: 1/137.04, 2.1% off]
    E_1 = -m_e α²/2 = -13.03 eV           [obs: -13.60 eV, 4.2% off]
```

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Discrete energy spectrum | Normalizable KG solutions in Coulomb potential | Discrete spectral lines | ✓ DERIVED |
| 1/n² energy scaling | Coulomb potential in 3 apparent DOFs | E_n = −13.6/n² eV confirmed | ✓ DERIVED |
| α_em(M_Z) from DFC | 1/129.6 (from β via g²=8πβ/3) | 1/127.9 | ✗ 1.3% off |
| α_em(atomic) after QED running | 1/140.0 | 1/137.036 | ✗ 2.1% off |
| Ground state energy E_1 | −13.03 eV | −13.60 eV | ✗ 4.2% off |
| Ly-α wavelength | 126.84 nm | 121.567 nm | ✗ 4.3% off |
| H-α wavelength | 684.9 nm | 656.3 nm | ✗ 4.4% off |
| Ratio H-α/Ly-α | 5.40 | 5.40 | ✓ exact (errors cancel in ratios) |
| Fine structure splitting | order α² × E_1 — not yet computed | ~0.1 meV | not yet derived |

---

## Open Questions

1. **Improve α_em(M_Z) to < 0.5%.** The current 1.27% error in α_em(M_Z) produces a
   systematic 4.2% error in all hydrogen energy levels (E ∝ α²). The path to improvement
   runs through a rigorous derivation of r_U1/λ = 3/(4β) from the D5 phase boundary
   condition in the substrate field equation. This is the principal open item in
   `foundations/coupling_derivation.md`.

2. **Derive m_e from substrate parameters.** Currently the electron mass is an input
   taken from measurement. The dimple depth mechanism in `foundations/mass_hierarchy.md`
   provides a structural account but the precise value requires the dimple potential
   to be derived from substrate parameters. Until this is done, the DFC hydrogen
   prediction has one input (m_e) taken from experiment.

3. **Fine structure splitting from D5/D6 coupling.** The energy splitting between, for
   example, the 2s and 2p levels of hydrogen from spin-orbit coupling is of order alpha
   squared times the ground state energy (~0.1 meV). The Dirac equation for the D6
   Jackiw-Rebbi zero mode in a Coulomb potential should produce this splitting from the
   D5/D6 coupling without additional input.

4. **Lamb shift from DFC vacuum modes.** The 2s-2p Lamb shift (1058 MHz, measured to
   10⁻¹² precision in QED) arises from the electron's interaction with virtual photons —
   massless D2 mode fluctuations. This is the most stringent possible precision test of
   the DFC account of electromagnetism, and is a high-priority long-term target.

---

## Connections

- `phenomena/electromagnetism/electromagnetism.md` — Coulomb potential from D5 U(1) closure
- `phenomena/particle_physics/particles/electron.md` — electron as D5+D6 zero mode
- `phenomena/quantum/quantum_mechanics.md` — Schrödinger equation from KG
- `phenomena/quantum/casimir_effect.md` — vacuum fluctuations (needed for Lamb shift)
- `equations/coupling_derivation.py` — alpha-em from beta (needed for Rydberg constant)
- `foundations/mass_hierarchy.md` — electron mass from substrate parameters
