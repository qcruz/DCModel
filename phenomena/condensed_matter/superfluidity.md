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

### Quantized Vortex Circulation (Tier 1 — exact)

The circulation of the superfluid velocity field around a closed loop encircling n vortex
cores equals n times Planck's constant divided by the atomic mass. The integer n is the
winding number — the number of times the condensate phase angle θ completes a full 2π
rotation as one travels around the loop:

```
κ_n = n × h / m_He4     n ∈ {1, 2, 3, ...}

κ₀ = h / m_He4 = 9.9693 × 10⁻⁸ m²/s    [circulation quantum; exact from topology]
Observed: 9.97 × 10⁻⁸ m²/s
Relative error: 7.1 × 10⁻⁵   (CODATA-limited, not topologically limited)

m_He4 = 4.002602 u = 6.64647 × 10⁻²⁷ kg
```

The quantization argument is identical to the DFC kink charge quantization and the
superconducting flux quantum: single-valuedness of the macroscopic order parameter
Ψ = √(n_s) e^{iθ} around a closed path requires the phase to return to itself modulo
2π per vortex, imposing integer winding. No material parameters appear; the result is
exact. Numerical verification in `equations/superfluidity.py`, with zero free parameters.

Circulation quanta for winding numbers 1 through 5:

| n | κ_n (m²/s) |
|---|---|
| 1 | 9.969 × 10⁻⁸ |
| 2 | 1.994 × 10⁻⁷ |
| 3 | 2.991 × 10⁻⁷ |
| 4 | 3.988 × 10⁻⁷ |
| 5 | 4.985 × 10⁻⁷ |

### Topological Quantization: Unified DFC Picture

All fundamental quantization constants in condensed matter arise from the same DFC U(1)
winding number mechanism — single-valuedness of a macroscopic order parameter. The relevant
particle's charge or mass appears in the denominator:

```
Φ₀_SC  = h / (2e) = 2.0678 × 10⁻¹⁵ Wb    [superconductor; Cooper pair charge 2e]
Φ₀_e   = h / e    = 4.1357 × 10⁻¹⁵ Wb    [normal metal; electron charge e]
κ₀     = h / m    = 9.969  × 10⁻⁸  m²/s  [superfluid; He-4 atomic mass m]
G₀     = e² / h   = 3.874  × 10⁻⁵  S     [QHE; conductance quantum]
K_J    = 2e / h   = 4.836  × 10¹⁴  Hz/V  [Josephson; Cooper pair frequency]
```

The ratio κ₀ / Φ₀_e = e / m_He4 = e/m, the specific charge of the electron — a consistency
relation connecting the superfluid and electromagnetic sectors with no free parameters.

### Superfluid Velocity Field (structural)

The velocity of the superfluid component equals the reduced Planck constant divided by the
atomic mass, times the spatial gradient of the condensate phase angle:

```
v_s = (ℏ/m) ∇θ
```

This London-like relation identifies the superfluid velocity as a phase gradient. In DFC,
ℏ appears here but is not yet derived from the substrate (see `foundations/planck_constant_derivation.md`).
The formula is imported from quantum mechanics, not from the DFC field equation.

### BEC Critical Temperature (IMPORTED — requires ℏ; BLOCKED)

The critical temperature for Bose-Einstein condensation in an ideal Bose gas equals a
numerical prefactor times the square of the reduced Planck constant divided by the mass,
times the particle number density raised to the two-thirds power. The prefactor involves
Riemann's zeta function evaluated at three-halves (ζ(3/2) ≈ 2.612):

```
k_B T_c = (2πℏ²/m) × (n / ζ(3/2))^(2/3)

At He-4 liquid density n = 2.18 × 10²⁸ m⁻³:
  T_c (ideal Bose gas) = 3.13 K
  T_λ (He-4 observed)  = 2.17 K
  Ratio: 1.44×

Note: ideal Bose gas overestimates T_λ by 44% because He-4 atoms
interact strongly via hard-core repulsion (not included in ideal gas formula).
```

**DFC status: BLOCKED.** The formula requires ℏ, which is not derived from the substrate.
Even once ℏ is derived, the ideal gas formula itself is imported from statistical mechanics
(not from DFC dynamics). See `foundations/planck_constant_derivation.md`.

### Landau Critical Velocity (structural)

A superfluid flow at velocity v can create a quasiparticle excitation of momentum p only
if the kinetic energy of the relative motion exceeds the excitation energy — that is, if
v times p is greater than or equal to the excitation energy E(p). The critical velocity
below which no quasiparticle creation is possible is the minimum of the excitation energy
divided by momentum over all momenta:

```
v_c = min_p [ E(p) / p ]

For He-4: minimum at the roton gap Δ_roton/k_B ≈ 8.65 K
  v_c ≈ 1 cm/s for narrow capillaries
```

**DFC status:** Structural identification only. The quasiparticle dispersion curve E(p)
for He-4 (phonon + roton spectrum) is not derived from the D3 substrate behavior.

---

## Consistency Checks

| Check | Status |
|---|---|
| Circulation quantum κ₀ = h/m_He4 = 9.9693 × 10⁻⁸ m²/s | ✓ Tier 1 — verified to 7.1×10⁻⁵ (CODATA-limited, Cycle 61) |
| Quantized circulation κ_n = n × h/m for all integer n | ✓ Tier 1 — exact from winding number; 0 free parameters (Cycle 61) |
| Zero viscosity from global phase coherence | ✓ (structural) |
| Landau criterion from quasiparticle spectrum | ✓ (structural) |
| He-4 vs He-3 (fermionic → no BEC, requires pairing) | ✓ (structural; fermions need to pair first) |
| BEC transition temperature T_c from DFC | ✗ BLOCKED — requires ℏ from substrate; ideal gas formula gives 3.13 K vs 2.17 K (44% off due to interactions) |
| Roton dispersion curve from D3 substrate | ✗ OPEN — quasiparticle spectrum not derived |

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

- `equations/superfluidity.py` — numerical verification: κ₀, BEC T_c, topological comparison (Cycle 61)
- `phenomena/condensed_matter/superconductivity.md` — same phase coherence mechanism;
  Cooper pairs are the fermionic analog of the BEC condensate; Φ₀=h/(2e) vs κ₀=h/m
- `phenomena/condensed_matter/quantum_hall_effect.md` — same DFC U(1) winding topology;
  conductance quantum G₀=e²/h
- `equations/superconductivity.py` — Josephson effect K_J=2e/h; same topological class
- `equations/quantum_hall.py` — von Klitzing constant R_K=h/e²; same winding mechanism
- `foundations/kink_nucleation.md` — winding number topology; same as vortex quantization
- `foundations/planck_constant_derivation.md` — ℏ hierarchy; blocks BEC T_c derivation
- `equations/magnetic_monopoles.py` — winding number quantization (flux/circulation analog)
