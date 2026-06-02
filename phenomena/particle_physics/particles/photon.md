# Particle: The Photon

## One-Sentence Synthesis

> The photon is the massless gauge boson of the D5 U(1) closure — a propagating
> phase excitation of the D5 vortex field whose masslessness follows from gauge
> invariance (no D4 inertial anchoring), whose two helicity states follow from the
> one-dimensional U(1) fold orientation, and whose coupling strength to charged matter
> is derived from the substrate quartic coupling β = 1/(9π) through g² = 8/27 → the
> 36π co-crystallization formula gives 1/α_em(M_c(EW)) = 36π exactly → 1/α_em(M_Z) =
> 128.09 (+0.15%); the Planck relation E = hν has the correct form from the massless
> dispersion ω = ck but requires the quantum of action ℏ, which is not yet derived
> from the DFC substrate.

---

## Observation

The photon is the quantum of the electromagnetic field. Established properties:

- **Zero rest mass**: photons travel at c in vacuum regardless of energy; m < 10⁻¹⁸ eV
- **Spin 1, helicity ±1**: two circular polarization states; no m=0 helicity (massless)
- **Electric charge 0**: photons do not self-interact at tree level
- **Energy E = hν**: emission and absorption in discrete quanta proportional to frequency
- **Momentum p = h/λ = E/c**: measurable as radiation pressure (Nichols 1901)
- **Compton wavelength**: λ_C = h/(m_e c) = 2.426 pm — relevant to photon-electron scattering
- **Gauge boson of U(1)_EM**: couples to all electrically charged particles with strength
  proportional to charge; coupling constant α_em = e²/(4πε₀ℏc) ≈ 1/137 at low energy
- **Thomson cross-section**: σ_T = (8π/3)(α_em/m_e)² = 6.652 × 10⁻²⁹ m² (electron)

Key measurements involving individual photons: photoelectric effect, Compton scattering,
Casimir force, Josephson junction, quantum optical coherence, Bell inequality violations
with polarization-entangled pairs.

---

## Standard Explanation

In the Standard Model, the photon is the massless gauge boson of the U(1)_EM gauge group,
arising from local invariance of the electromagnetic Lagrangian under ψ → e^{iθ(x)}ψ.
Its mass is exactly zero — protected by the gauge symmetry. The two photon helicities
are the two transverse modes of the massless vector field; the longitudinal mode is
absent because it would require mass (Goldstone boson eaten by a massive vector). The
coupling to matter is through the minimal coupling prescription p_μ → p_μ − eA_μ, with
e the elementary charge determined by α_em = e²/(4πε₀ℏc).

What the SM does not explain: why the gauge group is U(1) and not some other group, why
α_em has the value it does, why the photon is massless rather than acquiring a small mass.

---

## Dimensional Folding Explanation

### The photon as D5 U(1) gauge boson

In DFC, the photon is the phase excitation of the D5 vortex. The D5 closure is not a
real kink in the substrate field (as D6 and D7 closures are) — it is a vortex in the
complex extension of the substrate: the stable D5 topological defect has winding number
one in the U(1) phase and a core radius r_v ≈ 1.1 ξ (the substrate healing length).
This was established in `foundations/complex_substrate.md` (Cycle 75): the transverse
fluctuation operator around a real D5 kink has a tachyonic mode, showing that the real
kink is unstable; the vortex is the stable D5 defect.

The photon is the massless Nambu-Goldstone-like mode associated with the phase degree of
freedom of this D5 vortex — the phase can vary smoothly in space, and the restoring force
for uniform phase shifts is zero. This is the DFC statement of gauge invariance: the
phase of the D5 vortex at each point is an independent degree of freedom.

**Why the photon is massless:** The D5 vortex phase costs zero energy when shifted
uniformly. Spatially varying phase shifts cost gradient energy, which is the gauge field
kinetic term. There is no potential energy contribution from uniform phase rotations —
equivalently, no mass term for the photon field.

**Why exactly two polarization states:** The U(1) phase direction is one-dimensional
(a circle S¹). A propagating U(1) gauge field in 3+1D has exactly two transverse
polarization modes — the two transverse projections of the vector field. The longitudinal
mode is absent because the phase is a scalar, not a vector, and the gauge condition
eliminates it. This follows from the one complex degree of freedom (one U(1) circle)
at D5 depth, established in `foundations/d5_complex_structure.md` (Cycle 71) and
`foundations/complex_zero_mode_gap.md` (Cycle 70).

**Why the photon couples to matter:** The D6 kink (electron) is embedded in the D5
vortex background. Its zero mode acquires a complex phase from the D5 half-vortex
profile (established in `equations/complex_structure_derivation.py`, Cycle 67c):
the D6 zero mode dressed by the D5 phase background carries U(1) current
J_total = −2π/(5ξ). This non-zero current is the source of the photon-electron coupling.
The coupling strength is determined by the ratio of the D5 vortex effective radius
to the D6 kink width: r_U1/λ = 3/(4β) — giving g² = 8πβ/3.

### The coupling chain to α_em

The DFC derivation chain from substrate to the fine structure constant (Tier 2a, Cycles 117–142):

1. **β = 1/(9π)** (Tier 2a, Cycle 117): derived from V(φ) via D5 tachyonic instability +
   Hopf fiber dimension sum N_Hopf = 1+3+5 = 9. Zero free parameters.
2. **g_eff² = 8/27** (Tier 2a, Cycle 117): g_eff = 0.54433 (observed SM g_common = 0.5443,
   0.006% error). Full chain V(φ) → tachyon → O(2) → U(1) → J → d_n = 2n−1 → g² = 2I₄/N_Hopf.
3. **k_Y = √(5/3)** (Tier 2a, Cycle 30): hypercharge normalization from Dynkin index matching.
4. **ECCC co-crystallization at M_c(EW)**: α₁ = α₂ = α_common = 2/(27π) exactly.
5. **1/α_em(M_c(EW)) = 36π exactly** (Tier 2a, Cycle 141): at equal coupling,
   sin²θ_W = 1/(1 + k_Y²) = 3/8 → 1/α_em = (1 + k_Y²)/α_common = (8/3) × (27π/2) = 36π.
   Note: 36π = 4/β (algebraic identity: 4 × 9π = 36π, since β = 1/(9π)).
6. **1/α_em(M_Z) = 128.09** (+0.15%, Tier 2a, Cycle 142): EW running from M_c(EW) to M_Z.
7. **1/α_em(0) = 137.23** (+0.14%, Tier 2b, Cycle 142): additional QED running using
   observed SM fermion masses for hadronic vacuum polarization (Δ_QED = 9.136).

The key improvement over the old chain: the 36π formula bypasses the heuristic r_U1/λ = 3/(4β)
step (which gave 1.3% error) by using the algebraically exact ECCC co-crystallization condition.
Bottleneck 2 (the r_U1/λ derivation) is now CLOSED (Cycle 117): g² = 8/27 is derived, and
the holonomy derivation route was resolved to be consistent (not the formal bottleneck).

All numerical computations in `equations/alpha_em_prediction.py` and `equations/d5_complex_from_instability.py`.

---

## Formal Equations

### Massless dispersion (derived from DFC substrate)

The photon is the massless limit of the compression field where no buckling potential
applies. Setting the buckling potential to zero in the compression field equation gives
the massless wave equation; its plane wave solutions satisfy a dispersion relation where
the angular frequency equals the speed of light times the wavenumber:

```
□φ = 0    [massless compression field — no V(φ) term]

Plane waves: φ ∝ e^{i(k·x − ωt)}
Dispersion:  ω² = c²k²   →   ω = ck       [massless, linear ✓]
Group speed: v_g = dω/dk = c               [photon travels at c ✓]
```

### Photon energy (imported from QFT)

The minimum energy of the massless field mode at frequency ω equals the reduced Planck
constant times the angular frequency — this identification requires the quantum of action:

```
E = ℏω    [POSTULATE — quantum of action; imported from QFT; not derived from DFC substrate]
p = ℏk    [de Broglie relation; same status]

E = hν, p = h/λ follow immediately (h = 2πℏ, ω = 2πν).
```

### Photon coupling to matter (DFC chain)

The strength of the electromagnetic coupling emerges from the substrate quartic coupling
through the 36π co-crystallization formula. The gauge coupling squared equals eight divided
by twenty-seven (exactly, zero free parameters):

```
g² = 8/27 = 2I₄/N_Hopf            [Tier 2a, Cycle 117; I₄=4/3, N_Hopf=9]
β = 1/(9π)                         [Tier 2a; k_Y² = 5/3]

1/α_em(M_c(EW)) = (1+k_Y²)/α_common = 36π   [Tier 2a, Cycle 141; exactly 36π = 4/β]

EW running to M_Z (SM beta functions, Tier 2a):
  1/α_em(M_Z) = 128.09              [predicted; observed 127.9; error +0.15%]

QED running to q=0 (Δ_QED = 9.136 from SM fermion masses, Tier 2b):
  1/α_em(0) = 137.23               [predicted; observed 137.036; error +0.14%]
```

### Thomson cross-section (verified prediction)

The cross-section for low-energy photon scattering off an electron, where the photon
energy is much less than the electron rest mass energy, equals eight times pi divided
by three, times the square of the classical electron radius:

```
σ_T = (8π/3) × (α_em / m_e)²    [classical electron radius = α_em/m_e in natural units]
    = 6.633 × 10⁻²⁹ m²           [DFC prediction, α_em(0) = 1/137.23]
    = 6.652 × 10⁻²⁹ m²           [observed]
    error: −0.28%                  [10× improvement from 36π chain; Cycle 143]
```

Computed in `equations/scattering_cross_sections.py`. Tier 2a.

### Photon polarization

The two photon helicity states arise from the two transverse degrees of freedom of the
D5 U(1) phase. For propagation along z, the two circular polarization states are:

```
Right circular: A_μ ∝ (ε_x + i ε_y) e^{i(kz−ωt)},  helicity h = +1
Left circular:  A_μ ∝ (ε_x − i ε_y) e^{i(kz−ωt)},  helicity h = −1

Linear polarization = superposition: A_x = (R + L)/√2, A_y = i(R − L)/√2
```

The two helicities correspond to the two winding directions of the U(1) phase.

---

## Consistency Checks

| Property | DFC mechanism | Status |
|---|---|---|
| Masslessness (m_γ < 10⁻¹⁸ eV) | No D4 anchoring; gauge invariance of D5 phase | ✓ Structural |
| Speed c invariant | c is the substrate propagation constant | ✓ Derived (SR module, Cycle 78) |
| Exactly two helicity states | U(1) = S¹ gives one phase DOF; two transverse projections | ✓ Structural |
| Spin-1 angular momentum | U(1) fold orientation; h = ±ℏ per photon | ✓ Structural (ℏ imported) |
| Zero electric charge | D5 phase mode does not carry its own U(1) charge | ✓ Structural |
| E = hν (Planck relation) | Massless dispersion ω=ck + quantum of action ℏ | ✗ Partial (ℏ is postulate) |
| α_em(M_Z) = 1/127.9 | 36π co-crystallization → EW running (Cycle 141–142) | ✓ +0.15%, Tier 2a (1/128.09) |
| α_em(0) = 1/137.036 | 36π → EW run → Δ_QED=9.136 (observed HVP) | ✓ +0.14%, Tier 2b (1/137.23) |
| Thomson cross-section (6.65×10⁻²⁹ m²) | α_em(0) from 36π chain → σ_T | ✓ −0.28%, Tier 2a (Cycle 143) |
| Compton scattering angular distribution | Klein-Nishina formula from QED vertex | ✓ Structural (exact shape) |
| Photon does not self-interact (tree level) | U(1) is abelian — no three-photon vertex | ✓ Structural |
| No longitudinal photon | Gauge condition; one U(1) DOF → two transverse | ✓ Structural |

---

## Open Questions

1. **Bottleneck 2 CLOSED (Cycle 117).** g² = 8/27 is now Tier 2a from
   V(φ) → tachyonic instability → O(2) symmetry → U(1) → J → d_n = 2n−1 → N_Hopf = 9 →
   g² = 2I₄/N_Hopf. The heuristic r_U1/λ identification is superseded; the direct chain
   from V(φ) gives g² = 8/27 with zero free parameters. See `equations/d5_complex_from_instability.py`.
   Remaining open: prove the Hopf fiber series formula R_n = πd_n/I₄ from the DFC 5D KK overlap
   integral (last Tier 4 step; Cycle 107).

2. **Derive ℏ from the DFC substrate.** The Planck relation E = ℏω cannot be completed
   without identifying the substrate's natural action unit with ℏ. The ratio S_kink(D1)/ℏ =
   1.13×10⁴⁰ — about 13.4 bifurcation events away (model has 4 → residual ~10²⁸).
   See `foundations/planck_constant_derivation.md`.

3. **Photon mass bound.** The DFC account of photon masslessness (gauge invariance of the
   D5 phase) protects the mass exactly. But a residual mass m_γ > 0 would be generated if
   the D5 vortex phase acquired a potential term — for example, from the D5-D6 coupling.
   Whether the D5-D6 interaction generates a Proca-type mass for the photon is an open
   question. The experimental bound m_γ < 10⁻¹⁸ eV provides the constraint.

4. **Photon-photon scattering.** At one loop (the box diagram), photons do scatter off
   each other in QED with a tiny cross-section σ ∝ α² (ℏω)⁶/(m_e c²)⁶. In DFC, this
   requires a four-point function of the D5 phase field, which should emerge from the
   quartic interaction of the complex substrate Lagrangian. Whether the DFC prediction
   for light-by-light scattering (recently observed at LHC, ATLAS 2019) agrees with QED
   has not been computed.

---

## Connections

- `phenomena/light/light.md` — complete wave treatment (massless KG, dispersion, SR, GR)
- `foundations/d5_complex_structure.md` — D5=U(1) derivation chain; D6 modes carry
  U(1) charge (Cycle 71) — the mechanism of photon-matter coupling
- `foundations/complex_substrate.md` — D5 defect is vortex not kink (Cycle 75);
  vortex core radius r_v = 1.1 ξ; tachyonic L₂ mode rules out real D5 kink
- `foundations/phase_stiffness_derivation.md` — phase stiffness f²=(4/3)φ₀²/λ;
  Bottleneck 2 history; superseded by Cycle 117 Tier 2a derivation
- `equations/d5_complex_from_instability.py` — g²=8/27 Tier 2a derivation (Cycle 117); β=1/(9π)
- `equations/alpha_em_prediction.py` — 36π chain: 1/α_em(M_c(EW))=36π → 128.09 → 137.23 (Cycle 142)
- `equations/alpha_em_selfconsistency.py` — ECCC self-consistency; α_s+α_em joint prediction (Cycle 144)
- `equations/scattering_cross_sections.py` — Thomson σ_T = 6.633×10⁻²⁹ m² (−0.28%, Cycle 143)
- `equations/coupling_derivation.py` — old heuristic chain β→g²→α_em (superseded; 1.3% error)
- `equations/complex_structure_derivation.py` — D6 zero mode U(1) current J_total=−2π/(5ξ) (Cycle 67c)
- `foundations/coupling_emergence.md` — structural account of coupling emergence; V(φ)→β→36π chain
- `equations/atomic_structure.py` — QED running α_em from M_Z to m_e; hydrogen levels
- `equations/scattering_cross_sections.py` — Thomson σ_T = 6.37×10⁻²⁹ m² (Tier 2a)
- `phenomena/particle_physics/compton_scattering.md` — photon-electron collision;
  Klein-Nishina formula
- `phenomena/quantum/photoelectric_effect.md` — photon energy threshold; E = hν postulate
- `phenomena/quantum/anomalous_magnetic_moment.md` — a_e = α_em/(2π) from photon loop
- `phenomena/electromagnetism/electromagnetism.md` — photon as mediator of EM force
- `phenomena/condensed_matter/superconductivity.md` — photon acquires mass inside
  superconductor (Anderson-Higgs); DFC analog at D6 condensate scale
