# Phenomenon: Phase Transitions

## One-Sentence Synthesis

> Phase transitions are bifurcations in the effective potential V_eff(φ, T) of the
> compression field — the pressure of thermal agitation deforms the double-well potential
> until a stable minimum appears, disappears, or merges with another, producing the
> macroscopic symmetry changes observed as melting, magnetization, and the electroweak
> transition.

---

## Observation

Matter transitions sharply between phases at specific conditions. Three distinct behaviors:

**First-order transitions** (e.g., solid ↔ liquid, liquid ↔ gas):
- Discontinuous order parameter at the transition point
- Coexistence of both phases at the transition
- Latent heat: energy absorbed or released at constant temperature
- Nucleation dynamics: transition proceeds via bubble or crystal nucleation

**Continuous (second-order) transitions** (e.g., ferromagnetism below T_C, superconductivity):
- Order parameter grows continuously from zero at the critical point
- Diverging correlation length: ξ ∝ |T − T_c|^{−ν}
- Diverging susceptibility: χ ∝ |T − T_c|^{−γ}
- Universality: different materials share the same critical exponents if they share the
  same symmetry breaking pattern and spatial dimensionality (Wilson-Fisher fixed points)

**Crossovers** (e.g., the Standard Model electroweak transition for m_H > 73 GeV):
- No true non-analyticity in the free energy; the system changes character gradually
- The SM Higgs transition for the observed m_H = 125 GeV is a crossover, not a
  true phase transition (the order parameter varies rapidly but continuously)

Specific cosmic phase transitions:
- QCD confinement at T ~ 155 MeV (also a crossover for physical quark masses)
- Electroweak symmetry breaking at T_EW ~ 159 GeV (crossover in SM)
- Potential first-order transitions in extensions of the SM (SUSY, 2HDM) — relevant
  for baryogenesis Sakharov conditions

---

## Standard Explanation

**Landau theory:** Near a second-order transition, expand the free energy in powers of
an order parameter m:

```
F(m, T) = a(T)m² + b m⁴ + ...    [b > 0 for stability]
```

For T > T_c: a > 0, minimum at m = 0 (disordered phase).
For T < T_c: a < 0, two degenerate minima at m = ±√(−a/2b) (ordered phase).
The transition is second-order when the sign of a changes continuously at T_c.

For a first-order transition, a cubic term (or a fluctuation-induced cubic) causes the
ordered minimum to appear at non-zero m while the disordered minimum is still stable.
The two minima coexist at the transition temperature.

**Universality classes:** Critical exponents (ν, γ, β, δ...) depend only on the symmetry
of the order parameter and the spatial dimensionality d — not on the microscopic details.
The 3D Ising model, liquid-gas transition, and binary alloy demixing all share the same
exponents because they all break Z₂ symmetry in d = 3.

---

## Dimensional Folding Explanation

### Perspective 1: From the observer in spacetime

Phase transitions are observed as macroscopic changes in material properties at critical
temperatures or pressures. The DFC account identifies the microscopic substrate of these
transitions with bifurcations in the compression field's effective potential.

### Perspective 2: From the substrate

**All phase transitions are bifurcations of V_eff(φ, T).**

The DFC field equation describes a scalar field φ with buckling potential:

```
V(φ) = −α/2 φ² + β/4 φ⁴
```

At finite temperature T, thermal fluctuations modify the effective potential. To one
loop in the φ⁴ theory:

```
V_eff(φ, T) ≈ −α/2 φ² + β/4 φ⁴ + (thermal correction terms ∝ T²φ²)
```

The thermal correction adds a positive T²φ² term that can overwhelm the negative −α/2 φ²
at high temperature, turning the double-well into a single-well potential centered at φ = 0:

```
V_eff(φ, T) ≈ (−α/2 + cT²)φ² + β/4 φ⁴

T < T_c = √(α/(2c)):  double-well → ordered phase (φ ≠ 0)
T > T_c:              single-well → disordered phase (φ = 0)
```

This is a **second-order (continuous) transition** at T_c, with the order parameter
(the stable field value φ₀) growing as φ₀ ∝ √(T_c − T) below the transition — the
mean-field exponent β = 1/2.

**First-order transitions** arise when the effective potential has three extrema — a
local maximum and two local minima — and the system must quantum/thermally tunnel from
one minimum to the other across a potential barrier. The latent heat is the energy
difference between the two minima:

```
ΔQ = V_eff(φ_metastable) − V_eff(φ_stable) > 0     [barrier between minima]
```

In the DFC double-well, the barrier height is α²/(4β) in zero-temperature units.
Thermal fluctuations that exceed this barrier drive the transition.

### The Bifurcation Sequence as Phase Transitions

The DFC substrate's own history — the D1 → D2 → D3 → D4 → D5 → D6 → D7 sequence — is a
sequence of phase transitions in the compression field's effective potential at cosmic
cooling scales:

```
D1 → D2:  First buckling instability (Big Bang) — the compression field's near-D1
           potential acquires a first stable minimum → propagation modes exist

D5 closure: The substrate reaches the compression threshold at which a U(1)-topology
            minimum appears in the internal gauge sector of V_eff

D6 closure: S³-topology minimum appears → SU(2) closure stable; couplings "crystallize"
            at M_c(12) ≈ 10^13 GeV (the Route 3B equal-coupling scale)

D6 squashing: As the universe cools to T_EW ≈ 159 GeV, the S³ minimum deforms —
              the squashing parameter ε = φ_H/v grows from 0 to 1 → EWSB
              W and Z become massive; this is the Higgs "transition" (crossover in SM)

D7 closure: SU(3)-topology minimum appears; color confinement sets in at T_QCD ≈ 155 MeV
```

**Two-scale distinction:** The D6 closure (formation of the S³ topology as a stable
minimum) occurs at ~10^13 GeV. This is the "crystallization" of the D6 closure, not EWSB.
EWSB is the subsequent deformation of that already-formed S³ geometry — its squashing.
These are distinct events separated by ~10 orders of magnitude in energy scale.

### The Higgs Transition: S³ Squashing

The electroweak transition is the concrete DFC example of a phase transition. From
`foundations/higgs_geometry.md`, the effective potential for the S³ squashing parameter ε:

```
V_eff(ε) = −A ε² + B ε⁴     [A, B > 0 from competing geometric pressures]
```

At T > T_EW: thermal fluctuations maintain ε = 0 (round S³, full SU(2) symmetry,
massless W and Z)

At T < T_EW: the double-well minimum at ε = ε₀ = √(A/2B) ≈ 1 becomes stable
→ S³ is squashed → W, Z masses m_W = gε₀v/2, m_Z = gε₀v/(2cos θ_W)

The order parameter is ε (or equivalently the Higgs field φ_H = ε × v):
- Above T_EW: ⟨φ_H⟩ = 0 (unbroken phase)
- Below T_EW: ⟨φ_H⟩ = v = 246 GeV (broken phase)

**Crossover vs. first-order:** The SM analysis (using perturbative expansion and lattice
QCD techniques) shows that for m_H = 125 GeV, the EWSB transition is a crossover — the
free energy is analytic at T_EW and the order parameter changes rapidly but continuously.
The DFC squashing picture is consistent with a crossover: as T decreases through T_EW,
the S³ squashes smoothly from round to ellipsoidal, with no latent heat and no coexisting
phases. The DFC model does not change the SM's crossover character.

**Baryogenesis implication:** The Sakharov conditions require a first-order EWSB
transition to produce a baryon asymmetry at the electroweak scale. The SM does not
provide this (crossover). DFC does not automatically change this — if the D6 squashing
is a crossover, the electroweak baryogenesis route is unavailable. The DFC baryogenesis
account (`phenomena/cosmology/baryogenesis.md`) relies on the D7 QCD transition
satisfying Sakharov conditions at ~155 MeV — not on EWSB.

### QCD Confinement: D7 Closure Condensation

At T_QCD ≈ 155 MeV, the D7 SU(3) color field undergoes a deconfinement transition (in
reverse from high T to low T: confinement sets in as the universe cools). The order
parameter is the Polyakov loop ⟨L⟩, which measures the free energy of an isolated quark:

```
T > T_QCD: ⟨L⟩ ≠ 0 → quarks free (quark-gluon plasma)
T < T_QCD: ⟨L⟩ = 0 → quarks confined inside hadrons
```

In DFC terms: at T > T_QCD, the D7 closure field is in a deconfined phase where color
charge can propagate freely. Below T_QCD, the D7 topology fully confines — the D7
SU(3) closure structure becomes energetically unstable in isolation; only color-neutral
(D7-topology-neutral) combinations can be stable free objects in D3 space.

For physical quark masses, the QCD transition is also a crossover (determined by lattice
QCD). The DFC account does not modify this.

---

## Analogy: Cooling Ferromagnet

Iron above the Curie temperature (T_C = 1043 K) is paramagnetic — atomic magnetic
dipoles point in random directions; no net magnetization. Below T_C, the exchange
interaction is strong enough to align neighboring dipoles; the system spontaneously
magnetizes in some direction.

This is a second-order transition:
- Order parameter (magnetization M) grows continuously from 0 below T_C
- At T_C, fluctuations are correlated on all length scales — the correlation length
  diverges, and the system has fractal-like spatial structure

In DFC terms: the spin field is the DFC closure orientation; the exchange interaction
is the D3 nearest-neighbor coupling of adjacent closure orientations; the Curie
temperature is the thermal energy at which the double-well minimum in the orientation
potential becomes accessible.

**Where it breaks down:** Ferromagnetic domains are macroscopic; the DFC transitions
are in the compression field's internal gauge sector. The domain structure of a
ferromagnet has no direct analog in the cosmic phase transitions. But the
order-parameter/double-well structure and the universality of critical exponents are
exact parallels.

---

## Formal Equations

### Thermal Effective Potential (one-loop, schematic)

```
V_eff(φ, T) = −α/2 φ² + β/4 φ⁴ + (λ/24) T² φ²    [where λ is the quartic coupling]

Critical temperature (second-order):
T_c = √(12α / λ)

Order parameter below T_c:
φ₀(T) = √[(α − λT²/12) / β]  =  √(α/β) × √(1 − T²/T_c²)
```

### Latent Heat (first-order transition)

```
L = T_c × (S_broken − S_symmetric) = T_c × dV_eff/dT|_coexistence × Δφ²
```

For the φ⁴ potential with both minima at coexistence:
```
L ≈ T_c × (λ/12) × φ₀²(T_c)   [schematic — exact computation requires V_eff(φ, T_c)]
```

### DFC Barrier Height ↔ Latent Heat

```
V_barrier(T=0) = α²/(4β)   [zero-temperature barrier between vacua]
L ∝ V_barrier(T_c)          [latent heat ∝ barrier height at transition temperature]
```

This connection — latent heat proportional to barrier height — can in principle be
derived from the DFC potential parameters without reference to SM inputs. The value
of α at the D6 squashing scale is not yet derived from substrate dynamics.

---

## Consistency Checks

| Transition | DFC mechanism | Observed | Status |
|---|---|---|---|
| Second-order: order parameter continuous | Double-well acquires minimum continuously | ✓ ferromagnetism, BEC, superconductivity | Structural ✓ |
| Latent heat ∝ potential barrier | First-order: tunneling between minima → ΔQ = V_barrier | ✓ (structural) | Structural ✓ |
| EWSB as S³ squashing | ε parameter deforms round S³; φ_H = εv | ⟨φ_H⟩ = 246 GeV ✓ | Structural ✓ |
| EWSB is a crossover (SM) | Smooth deformation, no latent heat | SM lattice: crossover for m_H = 125 GeV | Consistent ✓ |
| QCD confinement at ~155 MeV | D7 topology fully confines; color-neutral combinations only | T_QCD = 155 ± 1 MeV (lattice) | Structural ✓ |
| Critical exponents from universality | Exponents from DFC scalar φ⁴ field symmetry | 3D Ising: ν=0.630, β=0.326 (well-measured) | OPEN (not derived) |
| Latent heat values quantitatively | Barrier height α²/(4β) at closure scale — α not derived | E.g., L_water = 6 kJ/mol | OPEN (α not derived from substrate) |
| EWSB temperature T_EW from DFC | S³ squashing parameter A, B from substrate — not derived | T_EW ≈ 159 GeV | OPEN |

---

## Connections to Other Phenomena

- `foundations/higgs_geometry.md` — the S³ squashing potential V_eff(ε) is the
  specific realization of DFC phase transition mechanics for EWSB
- `phenomena/particle_physics/particles/higgs_boson.md` — the Higgs boson is the
  excitation above the squashed minimum; its mass from the second derivative of V_eff(ε)
- `phenomena/cosmology/big_bang.md` — the D-depth bifurcation sequence IS the cosmic
  phase transition history; each threshold crossing is a DFC phase transition
- `phenomena/cosmology/baryogenesis.md` — Sakharov conditions require a first-order
  phase transition; DFC uses the D7 QCD transition (not EWSB) for baryogenesis
- `phenomena/thermodynamics/thermodynamics.md` — phase transitions are the most
  dramatic manifestations of the second law (latent heat = irreversible entropy increase)
- `equations/compression_field.py` — implements the buckling potential and its
  critical parameter values

---

## Open Questions

1. **Derive critical exponents for the DFC φ⁴ universality class.** The DFC potential
   V(φ) = −α/2 φ² + β/4 φ⁴ in d spatial dimensions is in the Ising (Z₂) universality
   class for a real scalar. The Wilson-Fisher fixed point gives ν, β, γ as functions
   of d and the number of order parameter components n. For n=1, d=3: ν = 0.630,
   β = 0.326. These should be derivable from DFC without additional inputs — but
   the renormalization group flow of the DFC potential has not been computed.

2. **Derive the EWSB temperature T_EW ≈ 159 GeV from D6 squashing parameters.**
   The squashing potential V_eff(ε) has parameters A and B from competing geometric
   pressures (D7 SU(3) pressure vs. D6 S³ restoration force). The temperature at which
   the squashing minimum appears is T_EW = √(A/(2c_thermal)). A and B are not yet
   derived from the substrate parameters (α, β, c) at D6 depth.

3. **Characterize the D5/D6 crystallization at 10^13 GeV as a phase transition.**
   The Route 3B derivation uses M_c(12) ≈ 10^13 GeV as the scale where D5/D6 couplings
   "freeze in" to equal values. What is the order parameter for this transition? Is it
   first-order (with latent heat = energy released into the thermal bath) or second-order?
   What observable signature would it leave in the spectrum of primordial perturbations?

4. **Latent heat of first-order DFC transitions from barrier height α²/(4β).**
   The zero-temperature barrier height α²/(4β) is the DFC proxy for latent heat.
   For the D6 EWSB transition (if it were first-order), this would be related to
   the observed EW sphaleron energy E_sph ≈ 10 TeV. Deriving the relationship
   between V_barrier and E_sph from the DFC squashing potential geometry is open.
