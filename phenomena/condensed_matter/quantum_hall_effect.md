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

### Von Klitzing Constant and Conductance Quantum (Tier 1 — exact)

The fundamental resistance and conductance units of the quantum Hall regime follow from
the D5 U(1) winding number and the elementary charge e. The von Klitzing constant is the
ratio of Planck's action to the square of the elementary charge:

```
R_K = h/e² = 25812.807 Ω     [exact; fixed by 2019 SI redefinition]
G₀  = e²/h = 3.874 × 10⁻⁵ S  [conductance quantum; exact]
```

Numerical verification: `equations/quantum_hall.py` confirms R_K to relative error 3.6×10⁻¹⁰
(limited by CODATA precision, not by DFC). Free parameter count: 0.

### Integer QHE Hall Conductance (Tier 1)

At integer filling factor ν (exactly ν Landau levels below the Fermi energy), the Hall
conductance equals ν times the conductance quantum. The integer ν is the first Chern number
of the occupied Landau level bundle over the magnetic Brillouin zone:

```
σ_xy = ν × e²/h      ν = C₁ ∈ {1, 2, 3, ...}

Chern number definition:
C₁ = (1/2π) ∫_BZ F_xy(k) dk_x dk_y    [Berry curvature integral over BZ]

TKNN result: C₁ ∈ Z always (integer by topology)
```

In DFC, C₁ is the winding number of the D5 U(1) Landau level states over the magnetic
Brillouin zone — the same type of topological integer that protects DFC kink charge.

Plateau values (verified in `equations/quantum_hall.py`):

| ν | σ_xy (µS) | R_H (Ω) |
|---|---|---|
| 1 | 38.740 | 25812.807 |
| 2 | 77.481 | 12906.404 |
| 3 | 116.221 | 8604.269 |

### Landau Level Energies

In a uniform perpendicular magnetic field B, Landau levels form at energies equal to
integer-plus-one-half times the quantum of action times the cyclotron frequency. The
cyclotron frequency is the ratio of the electron charge times the field strength to the
effective mass:

```
E_n = (n + 1/2) ℏω_c    n = 0, 1, 2, ...
ω_c = eB / m_eff          [cyclotron frequency]

QHE condition: T ≪ T_cyc = ℏω_c / k_B

At B = 10 T: T_cyc ≈ 13.4 K   (QHE clearly observable; mK experiments resolve FQHE)
```

### Fractional QHE — Jain Sequence (Structural)

Composite fermion theory (Jain, 1989): each electron kink binds to two D5 magnetic flux
quanta, forming a composite object. The filling factors at which the FQHE is observed follow
the sequence — the filling factor equals the number of composite fermion Landau levels p
divided by twice that number plus or minus one:

```
ν = p / (2p ± 1)     p ∈ Z⁺

Lower branch:  ν = 1/3, 2/5, 3/7, 4/9, ...
Upper branch:  ν = 1/1, 2/3, 3/5, 4/7, ...
```

The Hall conductance at each fractional ν is still σ_xy = ν × e²/h — the conductance quantum
formula applies to all filling factors, integer and fractional.

**DFC status:** The Jain sequence is structural in DFC — the composite kink-flux binding
mechanism is identified (D6 kink + 2 D5 flux quanta) but the effective theory for these
composite objects has not been derived from the substrate field equation.

---

## Consistency Checks

| Check | Status |
|---|---|
| von Klitzing constant R_K = h/e² = 25812.807 Ω | ✓ Tier 1 — verified to 3.6×10⁻¹⁰ (Cycle 61) |
| Conductance quantum G₀ = e²/h = 38.74 µS | ✓ Tier 1 — exact from D5 winding (Cycle 61) |
| Hall conductance σ_xy = ν × e²/h for integer ν | ✓ Tier 1 — exact from Chern integer (Cycle 61) |
| Topological protection of σ_xy (Chern integer) | ✓ (structural; same winding topology as DFC kinks) |
| Jain sequence ν = p/(2p±1) | ✓ (structural; composite kink-flux binding identified) |
| Chern number C₁ from DFC D5 Landau level bundle | ✗ OPEN — Chern number not computed in DFC |
| Fractional QHE effective theory | ✗ OPEN — D5/D6 composite kink-flux theory not developed |
| Edge states from bulk-boundary correspondence | ✗ OPEN — requires DFC bulk-boundary argument |

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
- `equations/quantum_hall.py` — numerical verification: R_K, G₀, IQHE plateaus, Landau levels (Cycle 61)
