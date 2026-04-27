# Phenomenon: Photoelectric Effect

## One-Sentence Synthesis

> The photoelectric effect — the emission of electrons from a metal surface by light —
> is the DFC account of D5 U(1) mode energy deposited into a D6 electron kink's binding
> configuration: emission occurs when the photon's energy exceeds the work function
> (the depth of the electron's closure binding below the vacuum), and the excess energy
> becomes the electron's kinetic energy after escape; the proportionality E = hν is
> imported from QFT as a postulate (labeled in `phenomena/electromagnetism/light.md`).

---

## Observation

When light of frequency ν strikes a metal surface, electrons are emitted if and only if
the frequency exceeds a threshold ν₀ that depends on the material (the work function W):

```
ν ≥ ν₀ = W / h
```

The threshold frequency equals the work function divided by Planck's constant. Below this
threshold, no electrons are emitted regardless of light intensity. Above it:

```
KE_max = h(ν − ν₀) = hν − W
```

The maximum kinetic energy of emitted electrons equals Planck's constant times the
difference between the photon frequency and the threshold frequency. This equals the
photon energy minus the work function.

Key observations:
- Emission is instantaneous (no time delay at threshold)
- Electron energy depends on frequency, not intensity
- Intensity controls the number of electrons, not their energy
- Einstein explained this with light quanta (1905); Nobel Prize 1921

Current precision: photoelectron spectroscopy resolves energy levels to < 1 meV, giving
detailed information about electronic structure.

---

## Standard Explanation

Einstein (1905) proposed that light consists of quanta, each carrying energy E = hν. An
electron in the metal is bound with energy W (the work function). Absorption of one quantum
provides energy hν. If hν > W, the electron is liberated with kinetic energy hν − W.
If hν ≤ W, the electron cannot escape regardless of how many quanta are present.

The Standard Model account: photons are excitations of the U(1) gauge field. Absorption
is a QED vertex where the incoming photon, the bound-state electron, and the outgoing
free-electron states are connected by the electromagnetic coupling e. The cross-section
for absorption is proportional to the square of the matrix element between initial (bound)
and final (free) electron states, weighted by the photon polarization vector.

---

## Dimensional Folding Explanation

**Structural account:**

In DFC, the photon is a massless D5 U(1) mode carrying energy proportional to its
frequency. The relation E = ℏω (the photon energy equals the reduced Planck constant times
the angular frequency) is a postulate imported from quantum field theory — not derived from
the DFC substrate (see `phenomena/electromagnetism/light.md`, where this is explicitly
labeled).

The electron is a D6 kink closure. In a metal, the electron's kink configuration is bound
within the metal's collective D7 substrate structure at a binding depth corresponding to
the work function W. The vacuum level (the D6 closure's free configuration outside the
metal) lies W above the bound configuration.

Photoelectric emission in DFC is the threshold process in which a D5 photon mode's
amplitude, deposited into the electron kink's local field, drives the kink over the
binding-energy barrier and into a free configuration:

- If the photon energy hν < W: the deposited amplitude is insufficient to drive the
  kink over the barrier. No emission occurs. The energy is dissipated as thermal agitation
  of the metal's D7 substrate.
- If hν ≥ W: the kink is driven over the binding barrier. The excess energy hν − W
  becomes the kinetic energy of the propagating kink (the free electron's kinetic energy).

The instantaneous nature of emission follows directly from the DFC buckling picture:
once the photon amplitude pushes the local field above the buckling threshold, kink
escape is immediate — there is no accumulation time required.

**What is needed for a quantitative prediction:**
- ℏ from substrate (Tier 4 open — see `foundations/planck_constant_derivation.md`)
- Work function W from the D7 substrate's collective closure binding energy at the
  metal's Fermi depth (requires condensed-matter DFC account of metallic bonding)

Without ℏ derived from the substrate, the relation E = hν remains a postulate and the
photoelectric threshold cannot be predicted in DFC units.

---

## Formal Equations

```
[STUB — ℏ from substrate required for quantitative prediction]

Threshold condition:
hν ≥ W         (photon energy ≥ binding energy of D6 kink in metal)

Emitted electron kinetic energy:
KE_max = hν − W = h(ν − ν₀)    where ν₀ = W/h

DFC structural statement:
The threshold W corresponds to the barrier height ΔV_binding for the D6 electron
kink to escape the metal's collective D7 closure potential — analogous to the DFC
nucleation barrier ΔV = α²/(4β), but at the condensed-matter scale.
```

---

## Consistency Checks

| Check | Status |
|---|---|
| Instantaneous emission from buckling threshold picture | ✓ (structural) |
| Energy-frequency proportionality (E = hν) | ✗ (postulate, not derived from substrate) |
| Intensity controls count, not energy | ✓ (one-photon absorption; structural) |
| Threshold frequency prediction for specific metals | ✗ (OPEN — requires ℏ and W from substrate) |
| Photon absorbed completely (vs. partially) | ✓ (kink nucleation is all-or-nothing) |

---

## Open Questions

1. **ℏ from substrate:** The primary blockage. The ratio of the photon energy to the
   photon frequency is Planck's constant. In DFC, this requires identifying the substrate's
   natural action unit with ℏ. See `foundations/planck_constant_derivation.md` — currently
   ~13.4 bifurcation events separate the D1 kink action from ℏ (S_kink(D1)/ℏ = 1.13×10⁴⁰;
   BPS-correct formula, Cycle 75), leaving a ~10²⁸ residual at D5 depth.

2. **Work function from D7 substrate:** Model the metallic binding as a collective D7
   closure configuration and derive the depth W of the D6 electron kink below the free-field
   vacuum. Candidate approach: effective kink-in-potential model where the potential is the
   metal's bulk D7 field.

3. **Above-threshold spectrum:** The photoelectron kinetic energy spectrum KE = hν − W
   is exact for the maximum energy (one-photon absorption). Multi-photon absorption
   (observed at high laser intensities) requires a DFC account of sequential D5 mode
   depositions, each driving the kink closer to the barrier until it escapes.

---

## Connections

- `phenomena/electromagnetism/light.md` — E = ℏω labeled as postulate; photon as D5 mode
- `foundations/planck_constant_derivation.md` — ℏ hierarchy; 13.2 bifurcations; open
- `foundations/compression_dynamics.md` — buckling threshold condition; barrier ΔV
- `foundations/kink_nucleation.md` — nucleation as threshold-crossing event
- `phenomena/condensed_matter/superconductivity.md` — related: electrons in collective
  D7 substrate potential
- `equations/atomic_structure.py` — electron energy levels in DFC framework
- `foundations/d5_complex_structure.md` — D5=U(1) derivation chain complete (Cycle 71);
  confirms photon as D5 mode with gauge group U(1)
