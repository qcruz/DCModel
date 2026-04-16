# Phenomenon: Superconductivity

## One-Sentence Synthesis

> Superconductivity is the regime in which pairs of D6 electron kinks form bound states
> through phonon-mediated D7 substrate interactions, acquiring a collective macroscopic
> phase coherence that eliminates the phase gradient (viscosity analog) required for
> electrical resistance; the superconducting gap Δ is the binding energy of the paired
> kink state, and the Meissner effect is the exclusion of D5 photon modes from the
> interior — the same S³ squashing geometry as the Higgs mechanism, but driven thermally
> at the condensed-matter scale.

---

## Observation

Below a critical temperature T_c (material-dependent, ranging from ~1 K for conventional
metals to ~135 K for high-T_c cuprates), certain materials exhibit:

1. **Zero electrical resistance:** Current flows without dissipation.
2. **Meissner effect:** Magnetic fields are expelled from the interior (not just excluded —
   existing fields are expelled as the material cools through T_c).
3. **Energy gap:** Electrons require a minimum energy 2Δ to break out of the paired state
   into normal quasiparticles.

Key data:
```
BCS gap equation:     Δ ≈ 1.764 k_B T_c     (for conventional superconductors)
London penetration depth:  λ_L = √(m / n_s μ₀ e²)
Flux quantization:    Φ_n = n × h/(2e)       (flux through a superconducting ring)
```

The gap equals approximately 1.764 times the Boltzmann constant times the critical
temperature. The penetration depth is the characteristic length over which an external
magnetic field decays inside the superconductor. Magnetic flux through a ring is
quantized in integer multiples of h divided by twice the electron charge.

The factor of 2e in flux quantization directly reflects Cooper pair formation (charge 2e).

---

## Standard Explanation

The BCS (Bardeen-Cooper-Schrieffer) theory explains conventional superconductivity:
electrons near the Fermi surface form Cooper pairs through phonon-mediated attraction.
One electron slightly polarizes the ionic lattice, creating a retarded positive charge
density that attracts a second electron. The pair has opposite momenta and spins
(k↑, −k↓) — a spin-singlet, S-wave bound state.

Below T_c, pairs condense into a macroscopic quantum state with a single coherent phase
angle θ. The order parameter Ψ = |Ψ|e^{iθ} is the Cooper pair condensate. The London
equations follow from the rigidity of θ. The Meissner effect arises because a photon
inside the superconductor acquires an effective mass from the condensate (the Anderson-Higgs
mechanism), exponentially suppressing the field over the penetration depth.

---

## Dimensional Folding Explanation

**Structural account (open for quantitative derivation):**

**Cooper pairs as kink-antikink bound states:**
In DFC, the electron is a D6 kink and the positron (its antiparticle) is the corresponding
antikink. However, Cooper pairs are not kink-antikink pairs — they are bound states of
two D6 kinks with opposite fold orientations (opposite spin). The binding is mediated by
D7 substrate phonons: collective oscillations of the D7 SU(3) substrate at the condensed-
matter scale (phonons in DFC are the acoustic modes of the D7 substrate at long wavelengths).

The phonon-mediated attraction between two D6 kinks with opposite momenta and orientations
produces a bound-state configuration whose binding energy is the superconducting gap Δ.
The bound state has charge 2e (two D6 kinks) and spin 0 (opposite fold orientations cancel).

**Phase coherence and zero resistance:**
In the normal metallic state, individual D6 electron kinks have independent phase angles θ_i.
Electrical resistance arises from momentum transfer between kinks — which requires a phase
gradient (∂θ/∂x ≠ 0) to sustain the current flow. Phase gradients generate energy dissipation.

Below T_c, the Cooper pairs condense into a state in which all pairs share a single
macroscopic phase angle θ. The DFC substrate's fold orientation locks globally across the
sample. A current flow corresponds to a phase gradient, but the rigidity of the condensate
resists local phase fluctuations — the gradient cannot decay locally without breaking pairs
globally. This is why the resistance is exactly zero: there is no local dissipation mechanism
compatible with the global phase constraint.

**Meissner effect as D5 mode exclusion:**
An external magnetic field is a D5 U(1) mode. Inside the superconductor, the condensate's
fixed phase θ and the photon's coupling produce an effective mass for the D5 mode (the
Anderson-Higgs mechanism). The D5 photon becomes massive inside the condensate, with a
mass proportional to the condensate density n_s. This mass causes the photon field to
decay exponentially over the London penetration depth λ_L — the D5 modes are excluded from
the interior.

This is geometrically the same S³ squashing mechanism as the electroweak Higgs
(see `foundations/higgs_geometry.md`) but operating at the condensed-matter scale. The
electroweak Higgs squashes S³ at the D6 closure scale (v = 246 GeV); the superconducting
condensate squashes the effective S³ of the D5 photon field at the material scale (T_c scale).

**Flux quantization from winding number:**
The quantization of magnetic flux in units h/(2e) follows from the single-valuedness of
the condensate order parameter θ as it winds around a superconducting ring. The phase must
return to itself modulo 2π after going around the ring, which constrains the enclosed flux
to integer multiples of h/(2e). This is the same winding-number mechanism as magnetic flux
quantization in the DFC account — see `equations/magnetic_monopoles.py`.

---

## Formal Equations

```
[STUB — phonon-mediated kink attraction not yet derived from DFC substrate]

BCS gap equation:
Δ = 2 ℏω_D exp(−1 / [N(0) V_phonon])    [BCS; inputs from experiment]

DFC structural statement:
Δ = binding energy of two D6 kinks via D7 phonon exchange
  ~ requires deriving V_phonon from D7 substrate acoustic modes

London penetration depth:
λ_L = √(m / n_s μ₀ e²)    [London; m = electron mass, n_s = superfluid density]

DFC statement: λ_L = scale over which D5 photon mode decays inside the condensate;
  set by condensate density n_s (number of paired D6 kinks per unit volume)

Flux quantization:
Φ_n = n × h/(2e)    where n ∈ Z     [direct from DFC winding number]
```

---

## Consistency Checks

| Check | Status |
|---|---|
| Cooper pairs carry charge 2e | ✓ (two D6 kinks with charge e each) |
| Meissner effect as D5 mode exclusion | ✓ (structural; same as Higgs geometry) |
| Flux quantization from winding number | ✓ (structural; same mechanism as magnetic flux) |
| BCS gap Δ ≈ 1.764 k_B T_c | ✗ (OPEN — phonon-mediated kink binding not derived) |
| London penetration depth from substrate | ✗ (OPEN — n_s not derived from DFC) |
| High-T_c superconductivity (cuprates) | ✗ (OPEN — d-wave pairing; different mechanism) |

---

## Open Questions

1. **Phonon-mediated kink attraction:** Derive the effective interaction V_phonon between
   two D6 kinks with opposite momenta, mediated by D7 acoustic modes (phonons) at long
   wavelengths. The DFC acoustic mode is the D7 substrate oscillation below the confinement
   scale (~155 MeV). At condensed-matter temperatures and scales, these modes should produce
   a retarded attractive potential analogous to the BCS phonon interaction.

2. **Critical temperature T_c from substrate parameters:** Given V_phonon from step 1,
   the BCS gap equation gives Δ as a function of N(0) (density of states at the Fermi level)
   and V_phonon. Deriving T_c requires connecting the Fermi energy to the DFC substrate at
   D6 depths — an open problem.

3. **High-T_c mechanism:** Cuprate superconductors have T_c up to 135 K and d-wave pairing
   symmetry. The DFC account must identify what aspect of the D7 substrate at higher
   temperatures produces d-wave rather than s-wave kink binding.

4. **Topological superconductors:** In topological superconductors, Majorana zero modes
   appear at the ends of 1D wires. In DFC, these should be Jackiw-Rebbi zero modes at
   the boundary between D6 kink and D6 antikink domains — the same topological mechanism
   as fermionic spin-1/2 (Cycle 33/41). This connection is worth formalizing.

---

## Connections

- `foundations/higgs_geometry.md` — S³ squashing as Higgs mechanism; same geometry as
  Meissner effect at different scale
- `foundations/compression_dynamics.md` — phase stiffness f²; resistance to phase gradients
- `phenomena/quantum/hawking_radiation.md` — Hawking radiation shares kink-antikink pair
  nucleation near a boundary; different context, same mechanism
- `phenomena/condensed_matter/superfluidity.md` — related: macroscopic phase coherence;
  different statistics (bosons vs. Cooper pairs)
- `phenomena/condensed_matter/quantum_hall_effect.md` — related topological phenomena
- `equations/magnetic_monopoles.py` — winding number quantization; flux quantization follows
- `foundations/depth_assignment.md` — D5/D6/D7 provisional assignments
