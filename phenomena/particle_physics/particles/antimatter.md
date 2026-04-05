# Phenomenon: Antimatter

## One-Sentence Synthesis

> In DFC, antiparticles are antikinks — compression field kinks with the opposite winding
> orientation at each closure depth (opposite D5 winding = opposite charge, opposite D7
> winding = anticolor) — and annihilation is the topologically inevitable kink-antikink
> collision that returns the field to vacuum, releasing the stored compression budget as
> radiation; the matter-antimatter asymmetry (η_B ≈ 6 × 10⁻¹⁰) is the DFC consequence
> of the D7 SU(3) buckling event being irreversible and chirally asymmetric — producing
> a small but nonzero net D7 winding number that persists as the baryon excess — though
> the precise value η_B remains an open quantitative problem.

---

## Observed Properties

```
Key facts:
  Every fermion has an antiparticle: e⁺, p̄, n̄, ν̄, q̄, ...
  Antiparticles have equal mass and opposite additive quantum numbers:
    charge: Q(e⁺) = +1 = −Q(e⁻)
    baryon number: B(p̄) = −1 = −B(p)
    lepton number: L(e⁺) = −1 = −L(e⁻)
    color: q̄ carries anticolor (conjugate SU(3) representation 3̄)

Annihilation:
  e⁺e⁻ → γγ  (at rest, two 0.511 MeV photons back-to-back)
  pp̄  → mesons → γγ + ν  (proton-antiproton annihilate into pions)
  Rate: σ_ann ∝ α²/s at high energy (EM annihilation); larger for hadronic

Baryon asymmetry (PDG 2024):
  η_B = (n_B − n_B̄) / n_γ ≈ 6.05 × 10⁻¹⁰     (CMB / BBN concordance)
  Ω_b h² = 0.02237 ± 0.00015   (Planck 2018)

CPT conservation (tested to high precision):
  m(e⁺) = m(e⁻) to 8 × 10⁻⁹  (ATRAP/BASE)
  q(p̄)/q(p) = −1 to 69 ppt    (BASE 2017)
  No CPT violation observed in any system
```

---

## DFC Account

### Antiparticles Are Antikinks

In the 1D compression field model, the kink:
```
φ_kink(x) = φ₀ tanh((x−x₀)/λ)
```
interpolates from −φ₀ (at −∞) to +φ₀ (at +∞). The antikink:
```
φ_antikink(x) = −φ₀ tanh((x−x₀)/λ)
```
interpolates in the opposite direction: from +φ₀ to −φ₀. Both have the same energy
(E_kink = E_antikink = (4/3)c√(2α³/β)), same mass, same width. The antikink is the
topological inverse of the kink — they carry opposite winding numbers.

**In the full multi-depth model:** An antiparticle is the field configuration with all
winding numbers reversed:

```
Electron (e⁻):         D5 winding = −1  [electric charge −1]
Positron (e⁺):         D5 winding = +1  [electric charge +1]

Proton (uud):          D7 winding (color) sum = 0  [color singlet, three quarks r+g+b]
                       D5 winding = +1              [electric charge +1]
Antiproton (ūūd̄):      D7 winding = 0  [anticolor singlet]
                       D5 winding = −1              [electric charge −1]

Quark (e.g., u):       D7 winding = red  [one unit, color r]
Antiquark (ū):         D7 winding = antired [color r̄]
```

All additive quantum numbers (charge, baryon number, lepton number, color) are DFC
winding numbers at specific closure depths — they reverse sign under the antikink
transformation.

### CPT Symmetry: Three Symmetries of the Field Equation

The compression field equation:
```
∂²φ/∂t² = c²∇²φ − V'(φ),    V(φ) = −α/2 φ² + β/4 φ⁴
```

has three discrete symmetries:

**C (charge conjugation):** φ → −φ. The potential V(φ) = V(−φ) is symmetric, so the
equation is unchanged. In DFC: reversing the sign of the compression field is equivalent
to exchanging kinks and antikinks. Physically: swapping all particles for their
antiparticles. The field equation is C-invariant.

**P (parity):** x → −x. The Laplacian c²∇²φ is parity-invariant. The equation is
unchanged. Kinks and antikinks are not mirror images of each other (a kink going left
is still a kink), so P is not the same as C.

**T (time reversal):** t → −t. Since the equation has only ∂²/∂t², it is
T-invariant — solutions run equally well forwards and backwards in time.

**CPT combined:** The product CPT is a symmetry of the equation, and by the CPT theorem
of QFT it is a symmetry of any Lorentz-invariant local field theory. In DFC: the
compression field equation is CPT-invariant by construction, which is why all
particle-antiparticle pairs have equal masses and equal lifetimes.

**P-violation:** The D6 SU(2) closure has a single intrinsic chirality (the S³ handedness
argument from `phenomena/particle_physics/forces/weak_force.md`). This breaks C and P
separately — the left-handed D6 connection couples to particles but not antiparticles
in the same way. But CP is approximately preserved (CP violation is small, ~10⁻³),
and CPT remains exact.

### Annihilation: Kink-Antikink Collision

When a particle and its antiparticle meet, the kink-antikink pair collides and
annihilates — the field returns to vacuum at both winding numbers. The stored compression
budget (mass energy) converts entirely to radiation (photons, or other massless modes).

**The kink-antikink collision in 1D:**
```
φ_total(x,t) ≈ φ_kink(x − vt) + φ_antikink(x + vt)

At collision center, the fields nearly cancel: φ → 0 (the unstable vacuum)
The configuration then relaxes to uniform vacuum, emitting radiation.
```

In 1+1D, the kink-antikink collision is exactly solvable. For two-body collision at
relative velocity 2v:
```
φ(x,t) = φ₀ × [tanh((x−x₀−vt)/λ) − tanh((x−x₀+vt)/λ) − 1]
```

This radiates at the collision moment, emitting energy as outgoing radiation with total
energy equal to the original pair mass (2E_kink). In the DFC model, this radiation
becomes photons (massless D2 modes).

**In the full model:**
- e⁺e⁻ annihilation: the D5 U(1) winding numbers (+1 and −1) cancel, releasing two
  photons (D5 connection field quanta, spin-1, back-to-back for momentum conservation)
- pp̄ annihilation: the D7 SU(3) windings cancel, releasing pions and ultimately photons

The two-photon minimum for e⁺e⁻ (not one photon) follows from momentum conservation:
a single photon cannot conserve both energy and momentum in the CM frame. The two-photon
final state is the D5 connection field radiating into two opposite-direction quanta.

### The Matter-Antimatter Asymmetry

The universe contains ~10¹⁰ photons for each surviving baryon. The baryon asymmetry:
```
η_B = (n_baryon − n_antibaryon) / n_photon ≈ 6 × 10⁻¹⁰
```

In DFC, this asymmetry arises from the D7 SU(3) buckling event in the early universe
(full account in `phenomena/cosmology/baryogenesis.md`). The key:

**Why baryons over antibaryons:** The D7 closure event is topologically irreversible. As
the early universe cools through the D7 symmetry-breaking scale (~Λ_QCD ~ 200 MeV),
the SU(3) field forms topological defects. The D7 closure topology has an intrinsic
chirality — the winding sense of the SU(3) knot has a preferred sign, set by the
cosmological initial conditions at the D7 buckling threshold.

The three Sakharov conditions are all satisfied in DFC at D7:
1. **Baryon number violation:** The D7 closure event can produce unequal numbers of
   quarks and antiquarks if the winding number of the SU(3) field is not exactly zero —
   sphaleron transitions (topological field rearrangements) at temperatures T ~ Λ_QCD
   can change the total baryon number by creating or destroying color-singlet combinations.

2. **CP violation:** The D7 closure chirality is asymmetric — the topology of the SU(3)
   closure favors one winding direction. Additionally, the CKM matrix provides CP
   violation in D6/D7 coupling (small: ~10⁻³), and the PMNS provides further CP
   violation in leptogenesis.

3. **Departure from equilibrium:** The D7 buckling event is a first-order phase
   transition — the universe passes through the QCD confinement transition out of
   thermal equilibrium. Spatial bubbles of the new phase nucleate and expand, creating
   the necessary departure from equilibrium at the bubble walls.

**What is not derived:** The precise value η_B ≈ 6 × 10⁻¹⁰ from DFC parameters. The
D7 chirality asymmetry produces η_B ≠ 0, but computing the numerical value requires
knowing the D7 winding asymmetry parameter — which depends on the substrate initial
conditions at the D7 buckling threshold, not yet derived.

### CPT and Mass Equality

The precise equality m(particle) = m(antiparticle) in DFC follows directly from the
CPT symmetry of the field equation. The kink and antikink have identical energies:

```
E_kink = E_antikink = (4/3)c√(2α³/β)
```

This is an exact result — the compression field potential V(φ) is symmetric in φ → −φ,
so the kink and antikink are exactly degenerate. Any asymmetry in mass between matter
and antimatter would signal CPT violation, which would in turn signal a violation of
Lorentz invariance (the CPT theorem requires both). Current experimental bounds on
CPT violation are among the most precise in physics.

---

## Formal Equations

### Kink-Antikink Fields

```
φ_kink(x)     = +φ₀ tanh((x−x₀)/λ)    [winding +1, particle]
φ_antikink(x) = −φ₀ tanh((x−x₀)/λ)    [winding −1, antiparticle]
E_kink = E_antikink = (4/3)c√(2α³/β)   [equal masses — CPT]
```

### Annihilation Cross-Section (EM)

```
e⁺e⁻ → γγ:    σ_ann = πr_e² (v_rel/c)⁻¹  [non-relativistic]
              σ_ann = πα²/s               [relativistic, s ≫ m_e²]
where r_e = classical electron radius = α ℏ/m_e c
```

### Baryon Asymmetry

```
η_B = (n_B − n_B̄) / n_γ = 6.05 × 10⁻¹⁰    [observed]

DFC:  η_B ∝ ε_CP × Γ_sphaleron / H(T_QCD)   [schematic]
      ε_CP = D7 closure chirality asymmetry
      Γ_sphaleron = topological transition rate at T ~ Λ_QCD
      H(T_QCD) = Hubble rate at QCD scale
Status: η_B ≠ 0 follows structurally; value not derived.
```

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| Equal particle/antiparticle masses | CPT: V(φ)=V(−φ) → E_kink = E_antikink | m(e⁺)=m(e⁻) to 10⁻⁹ ✓ | Derived ✓ |
| Opposite additive charges | Winding numbers reverse under φ → −φ | Q(e⁺) = −Q(e⁻) ✓ | Structural ✓ |
| Annihilation → photons | Kink+antikink → vacuum; budget → D5 radiation | e⁺e⁻ → γγ ✓ | Structural ✓ |
| Two-photon minimum | CM momentum conservation: one photon forbidden | ≥2 γ required ✓ | Structural ✓ |
| P-violation in weak sector | D6 S³ single chirality → C, P broken separately | V−A coupling ✓ | Structural ✓ |
| CPT exact | Lorentz-invariant field equation with CPT | No CPT violation observed ✓ | Structural ✓ |
| η_B ≠ 0 | D7 chirality + Sakharov at QCD transition | η_B ≈ 6×10⁻¹⁰ ✓ | Structural (not derived) |
| η_B = 6×10⁻¹⁰ | D7 winding asymmetry from initial conditions | 6.05×10⁻¹⁰ | OPEN |

---

## Open Questions

1. **Derive η_B = 6 × 10⁻¹⁰ from D7 closure parameters.** The baryon asymmetry is
   nonzero by D7 chirality — but the specific value requires computing the D7 winding
   asymmetry generated during the QCD phase transition, which depends on the initial
   conditions of the SU(3) field at the D7 buckling threshold. This is a cosmological
   initial-condition problem embedded in the D7 substrate dynamics.

2. **Does the DFC compression field equation satisfy the full CPT theorem?** The
   1D equation is CPT-invariant by the V(φ) = V(−φ) symmetry. In the full 3+1D multi-
   depth model, the CPT theorem requires Lorentz invariance of the field theory. The DFC
   field equation has Lorentz symmetry in the D3+D4 apparent geometry sector — but a
   rigorous proof that the full DFC substrate dynamics (including D5/D6/D7 sectors) is
   CPT-invariant requires the complete field theory formulation, which is not yet finished.

3. **Antimatter gravitational behavior.** General relativity predicts that antimatter
   falls in the same direction as matter under gravity (CPT requires it — a gravitational
   CPT violation would imply Lorentz violation). ALPHA-g experiment (CERN 2023) confirmed
   that antihydrogen falls downward (same as hydrogen). In DFC, this follows directly from
   CPT: the gravitational coupling of the antikink to the compression gradient field is the
   same as the kink's, because the potential V(φ) treats kinks and antikinks symmetrically.

4. **Why is there no antimatter in the observable universe?** The LIGO/Virgo/Fermi
   photon counterpart to GW170817 showed no gamma-ray burst asymmetry that would indicate
   large antimatter domains annihilating at domain walls. The universe appears to be matter-
   dominated all the way to the CMB scale. In DFC, if η_B was generated globally at the D7
   closure (not locally by domain walls), there should be no antimatter domains — the D7
   chirality selected one winding direction uniformly. This is testable by cosmic ray
   composition (no antihelium observed in AMS-02; limit on antimatter fraction < 10⁻⁷).

---

## Connections

- **Baryogenesis** — D7 closure chirality, Sakharov conditions, η_B derivation;
  `phenomena/cosmology/baryogenesis.md`
- **CP violation** — CKM and D7 chirality sources of CP violation;
  `phenomena/particle_physics/cp_violation.md`
- **Proton stability** — proton cannot decay to leptons (product topology);
  `phenomena/particle_physics/proton_stability.md`
- **Strong force** — D7 SU(3) topology is the source of the matter excess;
  `phenomena/particle_physics/forces/strong_force.md`
- **Weak force** — D6 chirality breaks C and P; W only couples left-handed;
  `phenomena/particle_physics/forces/weak_force.md`
- **Gluons / composite particles** — color-singlet hadrons as color+anticolor cancellation;
  `phenomena/particle_physics/particles/gluons.md`
