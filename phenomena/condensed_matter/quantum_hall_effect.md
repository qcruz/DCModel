# Phenomenon: Quantum Hall Effect

## One-Sentence Synthesis

> The integer quantum Hall effect arises from D5 U(1) Landau level states carrying
> topological winding numbers that are integers, giving a Hall conductance topologically
> protected to the value ν × e²/h — the same winding-number quantization that protects
> DFC kink charge; the fractional QHE (ν = 1/3, 2/5, ...) requires composite fermion
> formation — kink-flux-tube bound states where D5 and D6 depth behaviors mix.

---

## Observation

A two-dimensional electron system (GaAs/AlGaAs heterostructure or graphene) in a strong
perpendicular magnetic field at low temperature exhibits:

1. **Integer QHE:** Hall conductance σ_xy quantized in integer multiples of e²/h:
   ```
   σ_xy = ν × e²/h     ν ∈ {1, 2, 3, ...}
   ```
   The Hall conductance equals the filling factor ν times the ratio of the square of
   the electron charge to Planck's constant. Longitudinal conductance σ_xx = 0 at
   the plateaus (zero dissipation).

2. **Fractional QHE:** σ_xy quantized at fractional multiples of e²/h:
   ```
   σ_xy = ν × e²/h     ν ∈ {1/3, 2/5, 3/7, 2/3, ...}
   ```
   Discovered by Störmer, Tsui, Laughlin (1982); Nobel Prize 1998.

Key data:
```
e²/h = 3.874 × 10⁻⁵ S    (von Klitzing constant R_K = h/e² = 25812.807 Ω — exact since 2019 SI redefinition)
Plateau width: determined by disorder (localization of bulk states)
Temperature: QHE requires T ≪ ℏω_c/k_B (cyclotron gap)
```

---

## Standard Explanation

**Integer QHE:** In a magnetic field, electrons form Landau levels at energies (n + 1/2)ℏω_c
where ω_c = eB/m is the cyclotron frequency. At filling factor ν, exactly ν Landau levels
are filled. The Hall conductance is computed via the TKNN (Thouless-Kohmoto-Nightingale-den
Nijs) formula as the integral of the Berry curvature over the filled Brillouin zone — a
Chern number, which is always an integer:

```
σ_xy = (e²/h) × C₁     C₁ ∈ Z    (first Chern number)
```

The Chern number is topologically protected — it cannot change under continuous deformations
of the Hamiltonian that preserve the gap.

**Fractional QHE:** At ν = 1/3, electrons form a strongly correlated Laughlin state. The
Laughlin wavefunction describes a liquid of electrons with fractional quasiparticle
excitations (charge e/3). Jain's composite fermion theory: each electron binds to two
flux quanta of the external magnetic field, forming a composite object that experiences a
reduced effective field and fills an integer Landau level.

---

## Dimensional Folding Explanation

**Structural account (integer QHE — closer to derivable):**

In DFC, the 2D electron system is a collection of D6 kink closures confined to a 2D region
(the D3 localization depth restricts apparent motion to the plane). The perpendicular
magnetic field is a D5 U(1) mode configuration with nonzero field-strength tensor component
B_z = ∂_x A_y − ∂_y A_x.

The Landau levels are quantized D5 mode energies in the presence of this background field.
Each Landau level is labeled by an integer n. The filling factor ν counts how many Landau
levels are fully occupied below the Fermi energy.

The TKNN Chern number C₁ is a topological winding number of the occupied D5 Landau level
states over the magnetic Brillouin zone. In DFC terms, this is the same type of winding
number that:
- Protects the DFC kink charge (Z₂ winding in 1D)
- Quantizes vortex circulation in superfluids (Z winding in 2D)
- Protects the proton from decay (product topology argument)

The Hall conductance σ_xy = C₁ × e²/h is topologically quantized because the Chern number
C₁ is an integer and cannot change under smooth deformations of the occupied-band geometry.
The topological protection is the DFC statement that the winding number of the D5 Landau
level states is quantized in the same way as the DFC kink winding number.

**Fractional QHE — composite kink-flux-tube bound states:**

The fractional QHE requires a DFC account of composite fermions. Each composite fermion
is a D6 electron kink bound to two D5 magnetic flux tubes. This bound state is a mixed
D5/D6 depth configuration — a case where the substrate at D5 and D6 depths wraps together
into a new effective object. The composite fermion's effective charge and statistics differ
from the bare electron kink because the flux attachment modifies the D5 mode coupling.

The Jain sequence ν = p/(2p±1) (filling factors 1/3, 2/5, 3/7, ...) follows from
composite fermions (each with two attached flux quanta) filling p integer Landau levels
in a reduced effective field. In DFC, this is p-level occupation of composite kink-flux
states in a residual D5 background after two flux quanta per kink are absorbed.

This account is structural. A quantitative DFC derivation of the Laughlin state or the
Jain sequence requires developing the DFC effective theory for D5/D6 composite objects.

---

## Formal Equations

```
[STUB — Chern number from DFC D5 band structure not yet computed]

Integer QHE:
σ_xy = ν × e²/h     ν = C₁ ∈ Z    (Chern number of filled Landau levels)

TKNN formula:
C₁ = (1/2π) ∫_BZ F_xy dk_x dk_y     [Berry curvature F_xy over Brillouin zone]

DFC statement: C₁ = winding number of D5 Landau level state bundle over BZ
  — same topology as DFC kink winding number

Composite fermion filling:
ν = p / (2p ± 1)     p ∈ Z⁺    [Jain sequence]
DFC: composite = D6 kink + 2 × D5 flux quanta
```

---

## Consistency Checks

| Check | Status |
|---|---|
| Hall conductance σ_xy topologically quantized | ✓ (structural; same winding topology as DFC kinks) |
| von Klitzing constant R_K = h/e² | ✓ (structural; requires ℏ from substrate — open) |
| Integer filling factor as Landau level count | ✓ (structural) |
| Chern number C₁ from DFC D5 band structure | ✗ (OPEN — Chern number not computed in DFC) |
| Fractional QHE from composite kink-flux states | ✗ (OPEN — D5/D6 composite theory not developed) |
| Edge states from bulk-boundary correspondence | ✗ (OPEN — requires DFC bulk-boundary argument) |

---

## Open Questions

1. **Chern number from DFC D5 Landau levels:** Compute the Berry curvature F_xy of the
   lowest DFC D5 Landau level state over the magnetic Brillouin zone and verify that
   C₁ = 1. This requires the DFC analog of the Bloch state formalism for D5 modes in
   a uniform background field.

2. **Composite kink-flux theory:** Develop the DFC effective theory for a D6 electron
   kink bound to two D5 magnetic flux tubes. What is the effective statistics and charge
   of this composite object? How does flux attachment modify the D5 holonomy?

3. **Edge states (bulk-boundary correspondence):** Integer QHE has chiral edge modes —
   gapless states that propagate around the boundary of the 2D sample. In DFC, these
   should be Jackiw-Rebbi-type zero modes at the boundary between the topologically
   nontrivial (QHE) bulk and the trivial vacuum. Formalizing this connection would
   link IQHE edge physics to the DFC account of chiral fermions (see `foundations/spin_emergence.md`).

4. **Von Klitzing constant from substrate:** R_K = h/e² = 25812.807 Ω exactly. Both h
   and e are open in DFC as fundamental predictions. Deriving R_K from the substrate
   would be a major Tier 2a result.

---

## Connections

- `foundations/depth_assignment.md` — D5/D6 depth behavior; U(1) and SU(2) provisional assignments
- `foundations/kink_nucleation.md` — winding number topology; Z₂ and Z quantizations
- `phenomena/condensed_matter/superconductivity.md` — related topological phase; Meissner as photon mass
- `phenomena/condensed_matter/superfluidity.md` — quantized vortex circulation; same winding number
- `foundations/spin_emergence.md` — Jackiw-Rebbi zero modes; chiral fermions
- `phenomena/electromagnetism` — D5 U(1) photon modes; magnetic field as field-strength tensor
- `equations/magnetic_monopoles.py` — winding number quantization in DFC context
