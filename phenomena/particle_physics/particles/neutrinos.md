# Particle: Neutrinos

## One-Sentence Synthesis

> Neutrinos are the three lightest fermions in DFC — Jackiw-Rebbi zero modes that reach
> D6 (SU(2) winding, giving weak interaction) but do not fully penetrate the D4 inertia
> layer, acquiring tiny masses through a quadratic sub-threshold anchoring suppression
> (the DFC analog of a seesaw mechanism); their three mass eigenstates correspond to
> three distinct winding modes of the shallow SU(3) structure at the D3/D4 boundary,
> and their flavor oscillations are quantum interference between these eigenstates as the
> weak-interaction flavor eigenstates (ν_e, ν_μ, ν_τ) evolve in time — but the absolute
> mass scale and the winding mode depth spacings are not yet derived from first principles.

---

## Observed Properties

```
Generations:     3  (ν_e, ν_μ, ν_τ — one per lepton generation)
Charge:          0  (electrically neutral — no D5 U(1) coupling)
Weak isospin:    1/2  (SU(2) doublet partner of charged leptons)
Color charge:    0  (no D7 SU(3) coupling)
Spin:            1/2  (Jackiw-Rebbi zero mode)
Handedness:      left-handed only (right-handed sterile, if they exist)

Mass bounds (PDG 2024):
  Σm_ν < 0.12 eV          (Planck 2018 CMB cosmological bound)
  m_ν  < 0.45 eV          (KATRIN 2022 direct bound, electron neutrino)

Mass-squared differences from oscillation (NuFIT 2022, PDG):
  Δm²₂₁ = 7.42 × 10���⁵ eV²    (solar, KamLAND)
  |Δm²₃₁| = 2.517 × 10⁻³ eV²  (atmospheric, T2K, NOvA)

These imply (for normal hierarchy, m₁ ≈ 0):
  m₁ ~ O(few meV)
  m₂ ~ 9 meV
  m₃ ~ 50 meV
  Σm_ν ~ 59–60 meV   [well within the 120 meV bound]

Mass ordering: normal (m₁ < m₂ < m₃) or inverted (m₃ < m₁ < m₂) — not yet
determined experimentally. Normal hierarchy favored by T2K + NOvA (2σ).

PMNS mixing angles (PDG 2024):
  sin²θ₁₂ = 0.307 ± 0.013    (solar mixing)
  sin²θ₂₃ = 0.546 ± 0.021    (atmospheric mixing — near maximal)
  sin²θ₁₃ = 0.0220 ± 0.0007  (reactor mixing, small)
  δ_CP ≈ −π/2                 (CP-violating phase, T2K 2020)

Number of light neutrino species confirmed:
  N_ν = 2.984 ± 0.008   [from Z width at LEP — see w_z_bosons.md]
```

---

## DFC Account

### Origin: Sub-D4 Jackiw-Rebbi Zero Modes

Every fermion in DFC is a Jackiw-Rebbi zero mode at the compression field kink
(see `foundations/spin_emergence.md`). The zero mode couples to the D6 SU(2) closure
(giving weak isospin 1/2) and to the D5 U(1) closure (giving electric charge or lack
thereof). Neutrinos are zero modes that:

- **Reach D6**: carry weak isospin 1/2 — they couple to W and Z bosons
- **Do not reach D5 fully**: no electric charge — they do not excite the D5 U(1) loop
- **Do not fully penetrate D4**: near-zero mass — only fractional D4 anchoring

The third property is the key structural distinction. Charged leptons (electron, muon,
tau) have full D4 anchoring — their zero modes are tightly localized at the kink with
a large overlap with the inertia layer at D4. Neutrinos are structurally lighter: their
zero modes are more diffuse, reaching only a fraction f_ν of the D4 layer depth.

### The Sub-D4 Mass Formula

For particles with fractional D4 anchoring, the mass suppression is quadratic:

```
m_ν = m_e × f_ν²
```

where f_ν ∈ [0, 1] is the fractional D4 penetration depth of the neutrino zero mode.

**Why quadratic (not linear):** A particle that partially enters the D4 inertia layer
must traverse the D3/D4 boundary twice — in and back out. The mass matrix element
requires a double boundary crossing, giving a quadratic overlap. This is structurally
analogous to the seesaw mechanism in the Standard Model: a very small mass arises from
two suppressed processes rather than one.

For the cosmological bound Σm_ν < 0.12 eV:
```
f_ν < √(0.04 eV / 0.511 × 10⁶ eV) ~ 3 × 10⁻⁴
```

This extremely small fractional anchoring — the neutrino barely brushes the D4 layer
— is the DFC explanation for why neutrinos are so much lighter than electrons.

**Current status:** f_ν is a fit parameter, not derived from substrate dynamics. The
structural mechanism (quadratic suppression from double boundary crossing) is identified;
the specific value is not.

### Three Mass Eigenstates: Winding Modes at D3/D4 Boundary

The three neutrino mass eigenstates (ν₁, ν₂, ν₃) correspond to three distinct winding
modes of the shallow SU(3) structure at the D3/D4 boundary. This is the same threefold
structure that produces three quark colors and three lepton generations — but accessed
here at the sub-D4 depth rather than at D7.

Each winding mode has a slightly different depth anchoring:
```
d_ν₁ < d_ν₂ < d_ν₃    (normal hierarchy: mode 1 shallowest, mode 3 deepest)
```

The mass ratio between two winding modes at depths d_a, d_b:
```
m_b / m_a = exp(κ × (d_b − d_a))
```

where κ ≈ 5.3 is the depth-to-mass sensitivity (fit from the electron/muon mass ratio).

**Prediction from depth spacings:** The correct DFC prediction is the mass ratio m₃/m₂.
With equal-integer depth spacing (d₃ − d₂ = 1 unit), the DFC model predicts m₃/m₂ = κ¹
where κ ≈ 5.33 is the depth-to-mass sensitivity parameter. The observed value (for the
limit m₁ → 0) is m₃/m₂ = √(|Δm²₃₁|/Δm²₂₁) = √(2.517e-3/7.42e-5) = √(33.92) = 5.824.
The uncorrected discrepancy is −8.5% (Tier 2b).

**Structural color correction (Cycle 204, T3):** The third neutrino ν₃ sits nearest to the
D7/SU(3) closure threshold. A color phase correction of δd = N_c/(N_Hopf × 2π) = 1/(6π) ≈ 0.053
applies to ν₃'s effective depth, giving m₃/m₂ = κ^(1+1/(6π)) = 5.8248. This agrees with
the observed 5.824 at +0.010% — a 885× improvement with zero free parameters.

The formula uses only DFC T1/T2a/T2b quantities: κ [T2b], N_c = 3 [T1], N_Hopf = 9 [T1].
The physical derivation from the D4/D7 boundary value problem remains open (T3 → T2a path).
See `equations/neutrino_color_correction.py` for full numerical verification and sensitivity analysis.

**Note on metric confusion (Cycle 165 correction):** An earlier analysis claimed a "4.3×
discrepancy" by comparing the depth-difference ratio Δd₃₁/Δd₂₁ = 1.34 (a ratio of depth
intervals) to the mass-squared ratio Δm²₃₁/Δm²₂₁ = 33.92 (an entirely different quantity).
These are dimensionally incompatible. The correct comparison is the mass ratio m₃/m₂.

**Remaining open problem:** The structural formula achieves +0.010% at T3. The formal
derivation of δd = 1/(6π) from the D4/D7 BVP is the path to T2a.

### Flavor Oscillation: Quantum Interference in DFC

Neutrino oscillation — the conversion of ν_e → ν_μ → ν_τ as a neutrino propagates —
is a direct consequence of the flavor eigenstates (ν_e, ν_μ, ν_τ) not coinciding with
the mass eigenstates (ν₁, ν₂, ν₃).

**In DFC:** the flavor eigenstates are defined by the D6 SU(2) coupling (which W boson
emits which neutrino flavor). The mass eigenstates are defined by the D3/D4 winding
mode. The PMNS matrix is the rotation between these two bases — the D6 orientation
of each D3/D4 winding mode.

```
ν_α = Σᵢ U*_αi νᵢ    [PMNS matrix entry U_αi]
```

As the neutrino propagates, each mass eigenstate evolves with a phase exp(−im²L/2Eℏ).
The different phases produce quantum interference between flavors at the detector.

**The 2-flavor approximation:**
```
P(ν_α → ν_β) = sin²(2θ) × sin²(Δm² L / 4E)
```

The mixing angle θ controls the amplitude; the mass-squared difference controls the
oscillation length. Both are measurable.

**DFC interpretation:** oscillation is the beating between two compression field winding
modes at slightly different depths — the constructive and destructive interference of
the D3/D4 winding modes at the D6 readout. The PMNS mixing angles are the rotation
angles of the D6 orientation relative to the D3/D4 winding axes.

### Majorana or Dirac?

**Standard Model:** neutrinos are purely left-handed. If right-handed neutrinos do not
exist, neutrinos are Majorana particles (identical to their antiparticles). If they do
exist but are sterile (no gauge couplings), the seesaw mechanism gives tiny Majorana
masses.

**DFC account:** This is an open problem with a specific prediction path.

In DFC, a Dirac fermion has both a left-handed zero mode (coupling to D6 S³ chirality)
and a right-handed zero mode (with opposite S³ chirality coupling). The question is
whether the neutrino's zero mode has a right-handed component that is sterile at D6
(couples to neither W nor Z) but exists at D7 or above.

The DFC prediction is tentatively **Majorana**: the neutrino is a zero mode that only
exists on one side of the D3/D4 boundary (the left-handed side, defined by the D6 S³
chirality). There is no mirror image on the other side — the sub-D4 winding mode is
not duplicated. This would make the neutrino a Majorana fermion.

If confirmed experimentally (via neutrinoless double beta decay — no ν̄ emitted in
β⁻β⁻ → e⁻e⁻), this would be a genuine DFC prediction. The experimental search is
ongoing.

### Connection to Baryogenesis

The PMNS CP-violating phase δ_CP ≈ −π/2 (T2K 2020 measurement) contributes to
leptogenesis — CP-violating neutrino processes in the early universe could generate a
lepton asymmetry which converts to the baryon asymmetry via sphaleron processes. However,
as noted in `phenomena/particle_physics/baryogenesis.md`, the PMNS CP violation is
insufficient for the observed baryon asymmetry by ~12 orders of magnitude. The primary
DFC source of baryogenesis is the D7 closure chirality asymmetry, not the PMNS phase.

---

## Formal Equations

### Mass Formula

```
Sub-D4 anchoring:      m_ν = m_e × f_ν²
                       m_e = 0.511 MeV,  f_ν ~ few × 10⁻⁴

For normal hierarchy (m₁ lightest):
  m₁ ~ m_e × f_ν₁²
  m₂ = √(m₁² + Δm²₂₁)   ≈ 9 meV
  m₃ = √(m₁² + Δm²₃₁)   ≈ 50 meV
  Σm_ν ≈ 59 meV    [within Planck bound of 120 meV ✓]
```

### PMNS Mixing Matrix

```
U_PMNS = R₂₃ × R₁₃(δ_CP) × R₁₂

where Rᵢⱼ are rotation matrices in generations i,j:
  sin²θ₁₂ = 0.307   (solar mixing)
  sin²θ₂₃ = 0.546   (atmospheric mixing)
  sin²θ₁₃ = 0.022   (reactor mixing)
  δ_CP ≈ −π/2       (CP-violating phase)
```

### Oscillation Probability

```
P(ν_α → ν_β; L, E) = |Σᵢ U_αi* U_βi exp(−im²ᵢ L / 2E)|²

Two-flavor approximation:
  P(ν_α → ν_β) = sin²(2θ) sin²(Δm² L / 4ℏcE)

Oscillation length:  L_osc = 4πℏcE / Δm² = 2.48 m × (E/MeV) / (Δm²/eV²)
```

### Depth Spacing (winding modes)

```
Depth-spacing formula:
  Δd = (1/κ) × ln(m_high / m_low)

DFC equal-integer spacing predicts Δd₃₂ = Δd₂₁ = 1 unit, giving:
  m₃/m₂ (uncorrected) = κ^1 = 5.33  [Tier 2b, error −8.5%]
  m₃/m₂ (corrected)   = κ^(1+1/(6π)) = 5.8248  [T3, error +0.010%]
  m₃/m₂ (observed)    = √(2.517e-3/7.42e-5) = 5.824  [NuFIT 2022/PDG]

  Color correction: δd = N_c/(N_Hopf × 2π) = 3/(9×2π) = 1/(6π) ≈ 0.0531
  Physical: ν₃ at D7 threshold; SU(3) color topology adds fractional depth.

Note: the depth-difference ratio Δd₃₁/Δd₂₁ = 1.34 is a log-mass-ratio
compared at small m₁; it is NOT the same quantity as the mass ratio m₃/m₂.
Comparing 1.34 to 5.71 produced the spurious "4.3×" claim (Cycle 165 fix).
```

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| 3 neutrino flavors | 3 D6 depth anchoring levels (3 generations) | N_ν = 2.984 ± 0.008 ✓ | Structural ✓ |
| Electrically neutral | No D5 U(1) winding | Q = 0 ✓ | Structural ✓ |
| Only left-handed | D6 S³ single chirality | V−A coupling ✓ | Structural ✓ |
| Near-zero mass | Sub-D4 fractional anchoring | < 0.45 eV ✓ | Mechanism identified |
| Σm_ν ~ 59 meV | m_ν = m_e × f_ν² (fit f_ν) | < 120 meV ✓ | Consistency (f_ν fit) |
| Δm²₂₁, Δm²₃₁ | By construction from f_ν scan | Both matched by design | Input, not prediction |
| m₃/m₂ (uncorrected) | Equal-integer depth spacing κ^1 | 5.33 vs 5.824 observed | −8.5% Tier 2b — prior "4×" was metric error (C165) |
| m₃/m₂ (color-corrected) | κ^(1+1/(6π)) — ν₃ at D7 threshold correction | 5.8248 vs 5.824 observed | +0.010% Tier 3 (C204/C205) — 885× improvement |
| Normal vs inverted | Sign of SU(3) winding asymmetry at D3/D4 | Not determined | Open prediction |
| Majorana nature | Left-handed only; no D4 mirror mode | Not confirmed | DFC predicts Majorana |
| δ_CP ≈ −π/2 | D6 fold orientation CP phase (PMNS sector) | −π/2 (T2K 2020, 2σ) | Structural consistency |

---

## Open Questions

1. **Derive f_ν from substrate dynamics.** The anchoring fraction f_ν ~ few × 10⁻⁴ is
   the single free parameter controlling all neutrino masses. In DFC, f_ν should be
   determined by the D3/D4 boundary penetration probability of the neutrino zero mode —
   a function of (α, β, c, d_ν). The double-boundary-crossing mechanism is structurally
   identified; computing f_ν from first principles would be a genuine prediction.

2. **Derive the color phase correction from first principles.** The structural formula
   m₃/m₂ = κ^(1+N_c/(N_Hopf×2π)) = 5.8248 achieves +0.010% at T3 with zero free
   parameters (C204/C205). The remaining gap is a formal derivation of δd = 1/(6π)
   from the D4/D7 boundary value problem: compute the SU(3) holonomy phase acquired
   by a D4 winding mode traversing the D7 kink background, and show it produces exactly
   the depth correction N_c/(N_Hopf × 2π). Path: Jackiw-Rebbi zero mode analysis at
   the D4/D7 interface → winding-number-to-depth formula. File: `equations/neutrino_color_correction.py`.

3. **Derive the PMNS mixing angles from D6/D3-D4 geometry.** The three large mixing
   angles (θ₁₂ ≈ 34°, θ₂₃ ≈ 48°, θ₁₃ ≈ 8.5°) are strikingly different from the
   small CKM angles (θ_C ≈ 13°, θ₂₃ ≈ 2.4°, θ₁₃ ≈ 0.2°). In DFC, both mixing
   matrices are overlap integrals between D6 orientation states and mass eigenstates.
   Why are the neutrino mixing angles near-maximal while the quark mixing angles are
   small? This asymmetry may reflect the structural difference between sub-D4 winding
   modes (neutrinos, large mixing) and D7 quark states (smaller mixing).

4. **Confirm or refute the Majorana prediction.** DFC tentatively predicts neutrinos
   are Majorana — single-sided zero modes with no right-handed mirror state. This is
   testable via neutrinoless double beta decay: if ββ₀ν is observed, neutrinos are
   Majorana. Current bounds: T_half > 10²⁶ years (KamLAND-Zen 2022). Next generation
   (nEXO, LEGEND-1000) will probe to ~10²⁷ years.

---

## Connections

- **Three generations** — three D6 depth anchoring levels; same threefold structure;
  `foundations/three_generations.md`
- **Weak force** — neutrinos couple only to D6 SU(2) via W and Z;
  `phenomena/particle_physics/forces/weak_force.md`
- **W/Z bosons** — N_ν = 3 confirmed from Z width; Z decay to invisible;
  `phenomena/particle_physics/particles/w_z_bosons.md`
- **Spin emergence** — Jackiw-Rebbi zero mode as neutrino mechanism;
  `foundations/spin_emergence.md`
- **Mass hierarchy** — depth anchoring formula; sub-D4 suppression;
  `foundations/mass_hierarchy.md`
- **Baryogenesis** — PMNS CP phase contribution to leptogenesis (insufficient alone);
  `phenomena/particle_physics/baryogenesis.md`
- **CP violation** — δ_CP ≈ −π/2 in PMNS as testable prediction;
  `phenomena/particle_physics/cp_violation.md`
- **Neutrino masses module** — depth spacing computation, anchoring fraction scan;
  `equations/neutrino_masses.py`
- **Color phase correction** — κ^(1+1/(6π)) formula; selectivity/universality checks; sensitivity;
  `equations/neutrino_color_correction.py` (C205)
