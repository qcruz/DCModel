# Phenomenon: Superfluidity

## One-Sentence Synthesis

> Superfluidity is the regime in which D3 substrate modes acquire long-range phase
> coherence — the fold orientation angle locks globally across the sample, eliminating
> the phase gradients required for viscosity; Bose-Einstein condensation is the
> macroscopic occupation of a single D2 propagation mode, and quantized vortices
> arise from the same winding-number topology that underlies DFC kink charge.

---

## Observation

Below a critical temperature (T_λ = 2.17 K for He-4), liquid helium-4 becomes superfluid:

1. **Zero viscosity:** The fluid flows through capillaries with no measurable pressure drop.
2. **Fountain effect:** Superfluid climbs container walls and siphons over the top.
3. **Critical velocity:** Superfluidity breaks down above a critical flow velocity v_c = Δ/p
   (Landau criterion), where Δ is the roton gap and p is the quasiparticle momentum.
4. **Quantized vortices:** Vortices in the superfluid carry circulation quantized in integer
   multiples of h/m, where m is the He-4 atomic mass.

Key data:
```
T_λ (He-4)     = 2.17 K
κ (circulation quantum) = h / m_He4 = 9.97 × 10⁻⁸ m²/s
Critical velocity v_c   ≈ 1 cm/s (for narrow capillaries, He-4)
```

Bose-Einstein condensation (BEC) in ultracold dilute gases was first observed in 1995
(Cornell, Wieman, Ketterle). In a BEC, a macroscopic fraction of atoms occupies the
single lowest-energy mode.

---

## Standard Explanation

He-4 atoms are bosons (integer spin: nuclear spin 0, electron spin 0). Below T_λ, a
macroscopic fraction condenses into the zero-momentum ground state — Bose-Einstein
condensation. The condensate has a single macroscopic wavefunction Ψ = √(n_s) e^{iθ}.
The superfluid velocity is proportional to the gradient of the phase: v_s = (ℏ/m) ∇θ.
Zero viscosity follows from the rigidity of θ: small perturbations cannot locally deplete
the phase without costing macroscopic energy.

The Landau criterion sets the critical velocity: an external flow cannot create
quasiparticle excitations (rotons or phonons) if its velocity is below v_c = min(E(p)/p),
where E(p) is the quasiparticle dispersion curve.

Quantized vortices: the single-valuedness of Ψ around a vortex core requires ∮ ∇θ · dl = 2πn,
giving circulation κ_n = n × h/m.

---

## Dimensional Folding Explanation

**Structural account (open for quantitative derivation):**

**Phase coherence and zero viscosity:**
In DFC, He-4 atoms are composite closures — bound configurations of D6 kinks forming a
bosonic bound state (integer total spin). The atom's internal fold orientation angle θ
(the quantum phase) can vary independently from atom to atom in the normal liquid phase.
Viscosity in a liquid arises from momentum transfer between atoms when they pass each other.
In DFC terms, this momentum transfer requires a phase gradient — a spatial variation of θ
between neighboring atoms — to mediate the force.

Below T_λ, the collective configuration of the bosonic closures locks into a state in which
all atoms share the same macroscopic θ. This global phase coherence is the superfluid state.
With no phase gradient available at the scale of atomic separations, there is no mechanism
for momentum transfer: the fluid flows past itself without exchanging momentum. Viscosity
is zero because the usual phase-gradient channel for momentum transfer is absent from the
coherent configuration.

**Bose-Einstein condensation as D2 mode occupation:**
In DFC, propagating modes are D2 behaviors — the substrate's first propagation depth.
A BEC is the macroscopic occupation of a single D2 mode (the zero-momentum mode). The
critical temperature is the temperature below which the thermal occupation of excited modes
is insufficient to prevent the ground mode from being overwhelmingly dominant. In DFC terms,
the D2 mode at k = 0 acquires a macroscopic field amplitude — the entire condensate's
compression budget is concentrated in a single propagation mode.

**Quantized vortices from winding number:**
A vortex in the superfluid is a topological defect: the phase θ winds by 2πn as one travels
around the vortex core. The winding number n is an integer, for the same reason DFC kink
charge is quantized — single-valuedness of the field configuration around a closed path.
The circulation quantum κ = h/m follows from the winding-number constraint on θ:

The velocity field of a vortex equals ℏ/m times the gradient of the phase angle. The
integral of the velocity around a closed loop encircling the vortex core equals n times
ℏ/m times 2π, which equals n times h/m — the circulation quantum.

```
∮ v_s · dl = n × (h/m)     [quantized circulation; exact from winding number]
```

This quantization is a Tier 1 structural result — it follows from the topology of the
superfluid order parameter, independent of the material parameters.

**Landau criterion from roton gap:**
The minimum energy for creating a quasiparticle excitation in DFC is the roton gap Δ_roton.
A flow with velocity v creates quasiparticles only if v × p ≥ E(p) for some momentum p
(the flow can supply sufficient energy). The critical velocity v_c = min(E(p)/p) follows
from minimizing over the quasiparticle spectrum. In DFC, the roton is a localized
fluctuation of the D3 substrate at the atomic scale — a structural identification, not
a derived result.

---

## Formal Equations

```
[STUB — BEC transition temperature not yet derived from DFC substrate]

Superfluid velocity:
v_s = (ℏ/m) ∇θ     [London-like; ℏ from substrate is open]

Quantized circulation:
κ_n = n × h/m    n ∈ Z    [EXACT structural result from winding number]

BEC critical temperature:
k_B T_c = (2π ℏ²/m) × (n / ζ(3/2))^(2/3)
where n = particle density, ζ(3/2) ≈ 2.612
[BCS-like; requires ℏ from substrate]

Landau critical velocity:
v_c = min_p [E(p) / p]    [structural; E(p) from substrate quasiparticle spectrum]
```

---

## Consistency Checks

| Check | Status |
|---|---|
| Zero viscosity from global phase coherence | ✓ (structural) |
| Quantized vortex circulation κ = nh/m | ✓ (structural; winding number exact) |
| Landau criterion from quasiparticle spectrum | ✓ (structural) |
| BEC transition temperature T_c from DFC | ✗ (OPEN — requires ℏ from substrate) |
| Roton dispersion curve from D3 substrate | ✗ (OPEN — quasiparticle spectrum not derived) |
| He-4 vs He-3 (fermionic → no BEC, requires pairing) | ✓ (structural; fermions need to pair first) |

---

## Open Questions

1. **ℏ from substrate:** BEC transition temperature requires ℏ. Same blockage as the
   photoelectric effect and Planck constant derivation. See
   `foundations/planck_constant_derivation.md`.

2. **Roton gap from D3 substrate:** The roton minimum in He-4 occurs at wavevector
   k ≈ 1.9 Å⁻¹ with gap Δ_roton/k_B ≈ 8.65 K. Deriving this from the D3 substrate's
   localization behavior at the atomic scale requires a DFC model of the He-4 atom
   and its quantum fluid structure.

3. **He-3 superfluidity:** Helium-3 atoms are fermions (spin 1/2). They become superfluid
   at T_c ≈ 2 mK through Cooper-pair formation (analogous to BCS superconductivity).
   The DFC account must connect He-3 superfluidity to the Cooper-pair mechanism in
   `phenomena/condensed_matter/superconductivity.md`.

---

## Connections

- `phenomena/condensed_matter/superconductivity.md` — same phase coherence mechanism;
  Cooper pairs are the fermionic analog of the BEC condensate
- `foundations/compression_dynamics.md` — phase stiffness; phase gradient as viscosity analog
- `foundations/kink_nucleation.md` — winding number topology; same as vortex quantization
- `equations/magnetic_monopoles.py` — winding number quantization (flux/circulation analog)
- `phenomena/quantum/quantum_mechanics.md` — Bose-Einstein statistics from fold orientation symmetry
