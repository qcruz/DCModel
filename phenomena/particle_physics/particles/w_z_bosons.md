# Particle: W and Z Bosons

## One-Sentence Synthesis

> The W⁺, W⁻, and Z⁰ bosons are the three D6 SU(2) connection fields made massive by
> the S³ squashing — physically, each is a kink-scale oscillation in the D6 orientation
> field carrying SU(2) winding; the photon is the fourth linear combination that remains
> massless because it aligns with the S³ squashing axis; the Weinberg angle (the mixing
> parameter between the D5 and D6 closures, setting the ratio of W to Z mass) is predicted
> as three-eighths at the closure scale from the equal-coupling initial condition of the
> shared substrate kinetic term, and runs via Standard Model renormalization group equations
> to the observed value of 0.231 at the Z boson mass scale (Route 3B, sin²θ_W derived
> to 0.01% in `equations/weinberg_angle_rg.py`); the W and Z masses are predicted from the
> substrate quartic coupling β = 1/(9π) through the chain V(φ) → β → g_eff² = 8/27 → ECCC
> → M_W = 79.67 GeV (−0.88%) and M_Z = 90.86 GeV (−0.36%) with no free parameters beyond
> the two closure scales (Tier 2a, `equations/muon_lifetime.py`, Cycle 93); the electroweak
> VEV is derived as v = 247.83 GeV (+0.65%) from EWSB co-crystallization (Tier 2a, Cycle 145).

---

## Observed Properties

```
W± boson:
  Mass:          80.377 ± 0.012 GeV
  Spin:          1 (vector, charged gauge boson)
  Charge:        ±1 (W⁺ carries +1e, W⁻ carries −1e)
  Weak isospin:  1 (in the adjoint of SU(2))
  Lifetime:      ~3 × 10⁻²⁵ s
  Width:         Γ_W = 2.085 GeV
  Decays:        W → ℓν (each lepton flavor ~10.8%), W → qq̄' (~33.3% × 3 colors)

Z⁰ boson:
  Mass:          91.1876 ± 0.0021 GeV
  Spin:          1 (vector, neutral gauge boson)
  Charge:        0
  Weak isospin:  0 (mass eigenstate — mix of W³ and B)
  Lifetime:      ~3 × 10⁻²⁵ s
  Width:         Γ_Z = 2.4952 GeV
  Decays:        Z → ℓ⁺ℓ⁻ (~3.37% per flavor), Z → νν̄ (~6.67% per flavor), Z → qq̄ (~70%)

Mass ratio:
  m_W / m_Z = cos θ_W = 0.8819    [Weinberg angle relation]
  m_W² / m_Z² cos²θ_W = ρ = 1     [tree level, S³ custodial symmetry]
```

**Why the W is charged and Z is neutral:** The three SU(2) connection fields W¹, W², W³
are the original gauge fields. These are not mass eigenstates — they mix with the D5 U(1)
field B under electroweak mixing:

```
W⁺ = (W¹ − iW²)/√2    [carries +1 unit of SU(2) isospin charge → electric charge +1]
W⁻ = (W¹ + iW²)/√2    [carries −1 unit → electric charge −1]
Z  = W³ cos θ_W − B sin θ_W    [neutral combination: no net electric charge]
A  = W³ sin θ_W + B cos θ_W    [photon: massless, U(1)_EM]
```

The photon is the one linear combination that aligns with the S³ squashing axis — it
sees no geometric resistance and remains massless.

---

## DFC Account

### Origin: D6 Connection Fields Made Massive

The W and Z bosons originate by the same gauge logic that produces the photon and gluons,
at the D6 closure depth:

**Photon (D5 U(1)):** local U(1) orientation → 1 massless connection field A_μ.
**W/Z (D6 SU(2)):** local SU(2) orientation → 3 connection fields W_μ^a (a=1,2,3).
**Gluons (D7 SU(3)):** local SU(3) orientation → 8 massless connection fields G_μ^a.

The critical difference from the other two cases: the D6 SU(2) closure undergoes squashing.

### The S³ Squashing Mechanism (Mass from Geometry)

The D6 closure has the group manifold of SU(2), which is the 3-sphere S³. In the
substrate, the S³ geometry at D6 is not perfectly round — it is squashed by the parameter
ε (the Higgs field in DFC language). See `foundations/higgs_geometry.md`.

**Perfect S³ (ε = 0):** All rotation directions are equivalent. All three W_μ^a are
massless. The full SU(2) symmetry is preserved.

**Squashed S³ (ε = ε₀):** One rotation direction costs no energy — that is the photon.
Two rotation directions perpendicular to the squashing axis encounter geometric resistance —
those are the W± and Z. The resistance energy is the W and Z mass.

The mass formula follows directly:
```
m_W = (1/2) g_W v = 80.4 GeV    [SU(2) coupling × VEV]
m_Z = m_W / cos θ_W = 91.2 GeV   [from electroweak mixing geometry]
m_γ = 0                           [squashing axis = unbroken U(1)]
```

where v is the amplitude of the D6 squashing field at its minimum. The observed VEV is
246.22 GeV; the DFC prediction from EWSB co-crystallization is v = 247.83 GeV (+0.65%,
Tier 2a, Cycle 145): the D7 SU(3) confinement scale drives dynamical symmetry breaking
through a one-loop Coleman-Weinberg mechanism with b₀ = N_Hopf + Q_top = 11.

### The Coupling Chain: M_W and M_Z from V(φ)

The W and Z masses are predicted numerically from the substrate quartic coupling via the
following chain (all steps Tier 2a, `equations/muon_lifetime.py`, Cycle 93):

```
V(φ) = −α/2 φ² + β/4 φ⁴    → β = 1/(9π)            [kink instability threshold, Tier 2a]
   ↓ holonomy integral
g_eff² = 8πβ/3 = 8/27       → g_eff = 0.54433        [common gauge coupling, 0.006%]
   ↓ ECCC: α_i(M_c(Di)) = α_common = 2/(27π)
sin²θ_W = 0.2312             → g_W = 0.6520           [via Route 3B + RG running]
   ↓ M_W = g_W v / 2 (v = 247.83 GeV from EWSB co-crystallization)
M_W = 79.67 GeV  (observed 80.377 GeV, −0.88%)        [Tier 2a, 2 free params]
M_Z = 90.86 GeV  (observed 91.188 GeV, −0.36%)        [Tier 2a, from M_W/cos θ_W]
G_F = 1.168×10⁻⁵ GeV⁻²     (observed 1.166×10⁻⁵, +0.18%)  [Tier 2a]
```

The two free parameters in the M_W/M_Z predictions are the two ECCC closure scales
M_c(D5) and M_c(D6), which are read from Standard Model running rather than derived
independently. The remaining 0.88%/0.36% discrepancies reflect this residual dependence.

### The Weinberg Angle: DFC's Key Open Quantity

The Weinberg angle θ_W is the mixing angle between the D5 U(1) connection field B_μ and
the D6 SU(2) field W_μ³:

```
tan θ_W = g' / g_W    where g' = U(1)_Y coupling, g_W = SU(2) coupling
sin²θ_W = 0.23122     [measured at the Z pole]
```

**In DFC:** the D5 and D6 closures are independent but geometrically adjacent — they share
the D3 localization layer. The coupling strengths g' and g_W reflect the geometric
accessibility of the D5 and D6 closures to the fermion zero modes. In principle:

```
tan θ_W ≈ R_U1 / R_S3    [ratio of D5 and D6 closure radii]
```

where R_U1 is the D5 U(1) closure radius and R_S3 is the D6 S³ closure radius.

**Current status (Route 3B — Cycle 22, verified):** sin²θ_W = 3/8 at the closure scale
follows from the equal-coupling initial condition: because all gauge closures (D5, D6, D7)
emerge from the same substrate kinetic term, their coupling constants are equal at the
closure scale. With the hypercharge normalization factor k_Y = 3/5 derived from Dynkin
index matching on Standard Model matter content (Cycle 30, no GUT group needed), the
Weinberg angle at the closure scale is exactly three-eighths. Running this value down to
the Z boson mass scale via Standard Model one-loop beta functions gives sin²θ_W = 0.2312,
matching the observed 0.23122 to 0.01%.

The residual open problem is deriving the closure scale M_c ≈ 10¹³ GeV from the substrate
parameters (alpha, beta, c) rather than identifying it from Standard Model running. See
`foundations/embedding_geometry.md`, `equations/weinberg_angle_rg.py`.

**Why this is the most accessible derivation:** Unlike the strong coupling α_s or the
individual Yukawa couplings, sin²θ_W is determined by a geometric ratio between two
known closure structures (D5 U(1) and D6 SU(2)), both of which have explicit DFC
correspondences. The derivation path is:
```
substrate parameters → d₅, d₆ → R_U1/R_S3 ratio → tan θ_W → sin²θ_W = 0.23122
```
Even a structural argument for why R_U1/R_S3 ≈ tan(28.7°) from the closure geometry
would be significant.

### The W±: Charged Current, Flavor Change

The W bosons are charged — they carry one unit of SU(2) isospin, which adds or removes
electric charge from the fermions they couple to. This makes them the only SM gauge bosons
that change particle flavor:

```
d → u + W⁻     [down quark → up quark, emitting W⁻]
e⁻ → ν_e + W⁻  [electron → electron neutrino, emitting W⁻]
```

**DFC interpretation:** the W± carries a D6 SU(2) winding number change. The transition
d → u is an intra-D7 flavor transition mediated by a D6 gauge field — the quark changes
its D6 orientation (SU(2) doublet structure) by emitting a W that carries the orientation
difference. This is why the neutron lifetime calculation in `equations/proton_stability.py`
works: d → u is permitted as an intra-D6 transition; D7 → D5 cross-closure transitions
are forbidden by the topological constraint that different closure types cannot directly
convert.

**Helicity constraint:** the W couples only to left-handed fermions (the chiral D6 S³
closure has a single orientation, and only fermions aligned with that orientation couple).
The V−A structure (vector minus axial, coupling g_W/√2) is the mathematical statement of
maximal left-handedness.

### The Z⁰: Neutral Current, Parity-Violating

The Z boson couples to all fermions — left-handed and right-handed — but with different
strengths. The coupling is parity-violating (not maximal, unlike W) because the Z is a
mix of the chiral D6 field W³ and the non-chiral D5 field B:

```
Z coupling to fermion f:
  g_L = T₃ − Q sin²θ_W    [left-handed coupling]
  g_R = −Q sin²θ_W         [right-handed coupling]
```

where T₃ is the SU(2) isospin and Q is the electric charge. The asymmetry g_L ≠ g_R
reflects the partial D6 content of the Z: the SU(2) portion couples only to left-handed
fermions; the U(1) portion couples to both.

**The Z pole:** At center-of-mass energy √s = m_Z = 91.2 GeV, e⁺e⁻ colliders produce
Z bosons at resonance with an enormous cross-section. The Z width Γ_Z = 2.4952 GeV has
been measured to 0.01% precision at LEP, giving the number of light neutrino species:

```
N_ν = Γ_Z(invisible) / Γ_Z(νν̄)^SM = (0.499 GeV) / (0.1676 GeV) = 2.984 ± 0.008
```

This measurement — that there are exactly 3 light neutrino flavors — is one of the most
precise tests of the SM. **In DFC:** three neutrino species follows from three D6 closure
depth anchoring levels (the three generations). The Z width measurement is thus a precision
confirmation of the three-generation structure.

### The ρ Parameter: Derived from S³ Geometry

The tree-level relation ρ = 1 follows from the S³ custodial SU(2) symmetry:

```
ρ ≡ m_W² / (m_Z² cos²θ_W) = 1    (tree level)
```

**DFC derivation:** When the S³ is squashed along one axis, the SU(2)_custodial symmetry
rotating among the three W fields (not the gauge SU(2), but a global analog) is preserved
at tree level. This forces ρ = 1 exactly — it is a property of the S³ geometry, not
a coincidental cancellation. Radiative corrections give ρ ≈ 1.00039 (from top/bottom
mass splitting, Higgs loops). The deviation from 1 is entirely accounted for.

This ρ = 1 derivation is one of the genuine structural successes of the DFC Higgs
account — it is not postulated but follows from the S³ squashing having a specific
geometric form (see `foundations/higgs_geometry.md`).

---

## Formal Equations

### Physical Mass Eigenstates

```
W_μ± = (W_μ^1 ∓ iW_μ^2) / √2            [charged W bosons]
Z_μ  = W_μ^3 cos θ_W − B_μ sin θ_W      [neutral Z boson]
A_μ  = W_μ^3 sin θ_W + B_μ cos θ_W      [photon — massless]
```

### W and Z Masses

```
m_W  = g_W v / 2         = 79.67 GeV     [DFC prediction, −0.88%; observed 80.377 GeV]
m_Z  = m_W / cos θ_W     = 90.86 GeV     [DFC prediction, −0.36%; observed 91.188 GeV]
m_γ  = 0                                  ✓
ρ    = m_W²/(m_Z² cos²θ_W) = 1          ✓    [derived from S³ geometry]

g_W  = 0.6520                 [from β → g_eff → ECCC → sin²θ_W route; Tier 2a]
g'   = g_W tan θ_W            [U(1)_Y coupling from sin²θ_W]
e    = g_W sin θ_W = g' cos θ_W   [electric charge — unification relation]
v    = 247.83 GeV             [DFC prediction from EWSB co-crystallization, +0.65%; Tier 2a]
```

### Decay Widths

```
Γ(W → ℓν) = g_W² m_W / (48π) ≈ 226 MeV    [per lepton generation]
Γ(W → qq̄') = 3 × g_W² m_W |V_ij|² / (48π) ≈ 705 MeV    [3 colors, summed]
Γ_W(total) = 2.085 GeV    ✓

Γ(Z → ff̄) = (g_W² m_Z) / (48π cos²θ_W) × (g_L² + g_R²)
Γ_Z(total) = 2.4952 GeV    ✓

Number of light neutrino generations from Γ_Z:
  N_ν = 2.984 ± 0.008    ✓    [confirms exactly 3 generations]
```

### Fermi Constant (Low-Energy Limit)

```
G_F / √2 = g_W² / (8m_W²) = 1.168 × 10⁻⁵ GeV⁻²    [DFC prediction, +0.18%; observed 1.1664×10⁻⁵]

This connects the high-energy W picture to the low-energy 4-fermion Fermi theory.
Inserting m_W = g_W v/2:    G_F = 1 / (√2 v²)
DFC: v = 247.83 GeV → G_F = 1.168×10⁻⁵ GeV⁻² (+0.18%); from β → g_eff → ECCC chain.
```

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| 3 gauge bosons | SU(2) has 3 generators (2²−1=3), D6 connection | W⁺, W⁻, Z ✓ | Structural ✓ |
| Spin 1 | D6 SU(2) connection 1-form | 1 ✓ | Structural ✓ |
| W charged, Z neutral | SU(2) adjoint carries isospin; Z = W³/B mixture | ±1, 0 ✓ | Structural ✓ |
| M_W = 79.67 GeV | β→g_eff→ECCC→g_W→M_W (muon_lifetime.py) | 80.377 GeV | −0.88% ✓ Tier 2a (Cycle 93) |
| M_Z = 90.86 GeV | M_W / cos θ_W from same chain | 91.188 GeV | −0.36% ✓ Tier 2a (Cycle 93) |
| G_F = 1.168×10⁻⁵ GeV⁻² | g_W²/(8M_W²) from DFC chain | 1.166×10⁻⁵ GeV⁻² | +0.18% ✓ Tier 2a (Cycle 93) |
| v = 247.83 GeV | EWSB co-crystallization: b₀=N_Hopf+Q_top=11 | 246.22 GeV | +0.65% ✓ Tier 2a (Cycle 145) |
| ρ = 1 (tree level) | S³ custodial SU(2) symmetry | 1.00039 ✓ | Derived from S³ geometry ✓ |
| m_γ = 0 | Squashing axis = unbroken U(1) | 0 ✓ | Structural ✓ |
| Parity violated (W) | D6 S³ chirality — single intrinsic orientation | V−A structure ✓ | Structural (formal derivation open) |
| N_ν = 3 | Three D6 depth-anchoring levels | 2.984 ± 0.008 ✓ | Structural prediction ✓ |
| sin²θ_W = 0.231 | Equal-coupling initial condition + k_Y = 3/5 + SM RG running (Route 3B) | 0.23122 | 0.01% — derived ✓ (M_c from SM running, not substrate — remaining open) |
| g_W = 0.6520 | β→g_eff→ECCC→sin²θ_W→g_W (Tier 2a) | 0.6533 | −0.19% ✓ Tier 2a (Cycle 93) |
| Γ(Z→e⁺e⁻) = 82.7 MeV | DFC chain: β→G_F, M_Z, sin²θ_W → coupling formula | 83.984 MeV | −1.56% ✓ Tier 2a (Cycle 93) |
| Γ_Z(total) = 2456 MeV | DFC chain: sum over all SM fermions (massless limit) | 2495.2 MeV | −1.56% ✓ Tier 2a (Cycle 93) |
| Γ_inv = 493 MeV (3ν) | DFC chain + N_ν=3 structural prediction | 499.0 MeV | −1.16% ✓ Tier 2a (Cycle 93) |
| R_l = Γ_had/Γ_ll = 20.75 | DFC fermion coupling strengths (vector + axial) | 20.767 | −0.10% ✓ Tier 2a (Cycle 93) |
| R_b = Γ_bb̄/Γ_had = 0.220 | DFC b-quark couplings: T₃=−1/2, Q=−1/3 | 0.21629 | +1.58% ✓ Tier 2a (Cycle 93) |
| A_FB^lep = 0.0168 | A_FB = (3/4)A_e²; A_e from sin²θ_W | 0.01626 | +3.17% ✓ Tier 2a (Cycle 93) |
| A_FB^b = 0.105 | A_FB^b = (3/4)A_e A_b; needs loop corrections | 0.0996 | +5.4% ✗ Tier 2b (Cycle 93) |

---

## Open Questions (Priority Tier 1)

1. **RESOLVED (Cycle 22/30): sin²θ_W = 0.2312 derived via Route 3B.** The Weinberg angle
   follows from the equal-coupling initial condition at the D5/D6 closure scale M_c ≈ 10¹³ GeV
   (g₁ = g₂ = g₃ at M_c, confirmed numerically), plus the Dynkin normalization k_Y = 3/5
   derived from the SM matter content. SM RG running from M_c to M_Z gives sin²θ_W = 0.2312
   (error < 0.01%). **Remaining open:** deriving M_c from the substrate compression dynamics
   rather than from the SM running itself (currently M_c is read off from the α₁=α₂ crossing
   in the SM RG equations). See `foundations/embedding_geometry.md`, `equations/weinberg_angle_rg.py`.

2. **PARTIALLY RESOLVED (Cycles 117/93): g_W is derived via the β chain at Tier 2a.**
   The chain V(φ) → β=1/(9π) → g_eff²=8/27 → ECCC → sin²θ_W = 0.2312 → g_W = 0.6520
   gives M_W = 79.67 GeV (−0.88%) and M_Z = 90.86 GeV (−0.36%) with 2 free parameters
   (the two ECCC closure scales from SM running). The −0.88% residual for M_W is the
   remaining gap. **Fully open:** derive the D6 S³ closure scale M_c(D6) from substrate
   parameters alone, without reading it from Standard Model RG crossing. In principle:
   g_W ~ 1/R_S3 in Planck units, but the exact relation requires computing the zero-mode
   overlap with the SU(2) connection field at D6.

3. **Formal derivation of D6 chirality from closure structure.** The parity violation
   of the weak force is attributed to the S³ carrying a single intrinsic orientation.
   Why does the D6 closure produce a chiral S³ rather than both chiralities? This
   requires a precise account of how the sequential bifurcation events in the substrate
   produce the D6 topology with a fixed handedness. This is the formal derivation behind
   the structural argument in `phenomena/particle_physics/forces/weak_force.md`.

4. **CKM matrix from D6/D7 closure overlap.** The nine quark flavor-mixing amplitudes
   (three angles and one CP phase) describe how the D6 SU(2) weak eigenstates relate to
   the D7 SU(3) color/mass eigenstates. In DFC, these mixing angles are overlap integrals
   between D6 fold orientation states and D7 closure states — determined by the relative
   geometry of D6 and D7 at each quark depth anchoring level. The path is:
   d₆, d₇ (depth anchoring levels for each quark) → D6/D7 orientation overlap → CKM.

---

## Connections

- **Weak force** — full DFC account of SU(2) gauge structure and left-handedness;
  `phenomena/particle_physics/forces/weak_force.md`
- **Electroweak** — D5 and D6 closures as adjacent independent structures sharing D3;
  `phenomena/particle_physics/forces/electroweak.md`
- **Mass generation** — S³ squashing mechanism, ρ=1 from custodial SU(2);
  `phenomena/particle_physics/mass_generation.md`
- **Higgs boson** — the squashing parameter ε is the Higgs field;
  `phenomena/particle_physics/particles/higgs_boson.md`
- **Proton stability / neutron decay** — W mediates d→u intra-D6 transition; τ_n = 878.4 s;
  `phenomena/particle_physics/proton_stability.md`
- **Three generations** — N_ν = 3 from Z width confirms 3 D6 depth levels;
  `foundations/three_generations.md`
- **CP violation** — CKM CP phase from D6 fold orientation geometry;
  `phenomena/particle_physics/cp_violation.md`
- **Z boson decay widths** — all partial widths, Γ_Z, R_l, R_b, A_FB^lep from DFC coupling chain (Cycle 93);
  `equations/z_boson_decays.py`
- **Electroweak precision** — ρ=1, T=0, sin²θ_W self-consistency checks;
  `equations/electroweak_precision.py`, `equations/muon_lifetime.py`
- **Coupling chain** — β=1/(9π) → g_eff²=8/27 → ECCC derivation;
  `equations/d5_complex_from_instability.py` (Cycle 117)
- **EWSB co-crystallization** — v=247.83 GeV (+0.65%) from b₀=11;
  `equations/ewsb_cocrystallization.py` (Cycle 145)
- **ECCC self-consistency** — M_c(D7)/M_c(D5) ratio and α_em/α_s joint determination;
  `equations/alpha_em_selfconsistency.py` (Cycle 144)
