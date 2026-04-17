# Phenomenon: Lamb Shift

## One-Sentence Synthesis

> The Lamb shift — the splitting of the hydrogen 2s and 2p energy levels — arises in DFC
> from vacuum mode coupling between the D5 U(1) photon field and the D6 electron kink:
> the electron's self-energy under its own emitted-and-reabsorbed D5 modes shifts the
> 2s state upward relative to the 2p state by an amount requiring a loop integral in
> the DFC effective field theory (structural account; numerical derivation open).

---

## Observation

In hydrogen, the 2s and 2p orbitals are predicted by the Dirac equation to be exactly
degenerate (same energy) — both have principal quantum number n = 2 and total angular
momentum j = 1/2. Willis Lamb and Robert Retherford measured in 1947 that the 2s₁/₂
level lies above the 2p₁/₂ level by:

```
Δν_Lamb = 1057.845 MHz     (2s₁/₂ − 2p₁/₂ in hydrogen)
```

This splitting is approximately 4.4 μeV. It was the first experimental signal that
quantum electrodynamics must include vacuum fluctuations — the measurement contributed
directly to the development of renormalization.

Current experimental precision: better than 1 part in 10⁶ (leading to the proton radius
puzzle when combined with muonic hydrogen results).

---

## Standard Explanation

In QED, the Lamb shift arises from two sources:
1. **Electron self-energy:** The electron continuously emits and reabsorbs virtual photons.
   The self-energy loop integral diverges in the ultraviolet but the divergence is absorbed
   by mass renormalization. The finite remainder shifts the 2s level because the 2s
   wavefunction has nonzero probability at the proton's location (where the Coulomb field
   gradient is strongest), while 2p has a node there.
2. **Vacuum polarization:** The virtual electron-positron pair creation shifts the effective
   Coulomb potential, contributing a small additional correction.

The dominant term is the electron self-energy, which gives a shift proportional to the
electron's probability density at the origin (Bethe, 1947).

---

## Dimensional Folding Explanation

**Structural account (open for quantitative derivation):**

In DFC, the electron is a kink configuration at D6 depths. The photon is a massless D5
U(1) mode. The electron-photon interaction is the coupling of the D6 kink's phase
orientation to the D5 field's amplitude — parameterized by the gauge coupling g_em,
which is derived from β through the DFC chain (Cycle 42/44).

The Lamb shift in DFC corresponds to the same self-energy diagram as in QED, reinterpreted:
the electron kink continuously excites and reabsorbs D5 vacuum modes. The energy shift
equals the integral over all D5 mode wavevectors k of the mode energy times the square
of the electron-photon coupling at that wavevector.

The structural reason the 2s level is shifted more than 2p is the same in DFC as in QED:
the 2s kink configuration has higher overlap with the region of maximum D5 mode density
(near the proton closure), while the 2p configuration has a node at that location.

**What is needed for a quantitative prediction:**
- The DFC photon propagator: the Green's function of the massless D5 Klein-Gordon field
  in the presence of the D6 kink background
- The electron-photon vertex factor: derived from the DFC coupling chain (g_em from β)
- The loop integral: ∫d⁴k [vertex² × photon_propagator × electron_propagator] over all
  D5 wavevectors, regulated by the DFC closure scale M_c(D5) as ultraviolet cutoff
- The bound-state wavefunctions: the hydrogen 2s and 2p wavefunctions in the DFC account
  of atomic structure (already developed in `phenomena/quantum/atomic_structure.md`)

This is the same order in perturbation theory as the anomalous magnetic moment g-2, which
is also a one-loop self-energy diagram.

---

## Formal Equations

### DFC Self-Energy Diagram (schematic — loop integral open)

The electron self-energy under its emitted-and-reabsorbed D5 photon modes is represented
by the diagram in which the electron propagator emits and reabsorbs a single photon. The
energy shift equals the integral over all D5 photon wavevectors of the product of the
squared vertex factor, the photon propagator, and the electron propagator:

```
ΔE_self ≡ (g_em² / (2π)²) ∫ d⁴k D_μν(k) S_F(p − k)
          [integrated over D5 mode space; regulated at M_c(D5) = 9.44 × 10¹² GeV]

2s-2p splitting:
Δν_Lamb = (ΔE_self[2s] − ΔE_self[2p]) / h    [2p contribution ≈ 0: |ψ_2p(0)|² = 0]
```

The DFC photon propagator is the massless D5 Klein-Gordon Green's function: the negative
of the metric tensor divided by the squared wavevector, D_μν(k) = −η_μν/k². The DFC
vertex factor g_em is derived from β through the coupling chain.

**DFC inputs:**
```
g_em² = 4π α_em(m_e) = 4π/140.1      [from β chain; Cycle 42/44]
UV cutoff: M_c(D5) = 9.44 × 10¹² GeV  [from SM α₁=α₂ crossing]
```

**DFC status: loop integral not yet computed.** The full integral requires the bound-state
electron propagator in the hydrogen potential — this is the open step.

### Bethe Non-Relativistic Estimate (QED reference, not DFC)

The dominant Lamb shift contribution is the electron self-energy for the 2s state. The
energy shift of the n-th s-wave level equals four times the fifth power of the fine
structure constant times the electron rest energy, divided by three times pi times n cubed,
times the logarithm of the electron rest energy divided by twice the average excitation
energy:

```
ΔE(ns) = (4 α⁵ m_e c²) / (3π n³) × ln(m_e c² / (2 <E>_avg))

For n = 2 (2s state), <E>_avg ≈ 16.6 eV (Bethe 1947):
  Bethe log = ln(511000 / 33.2) ≈ 9.64
  Simple formula gives: 1308 MHz   [vs Bethe's actual 1040 MHz — discrepancy from
                                    simplified <E>_avg; exact calculation sums all states]
  Full QED (observed): 1057.845 MHz
```

The 2p contribution vanishes because the 2p wavefunction has a node at the nucleus:
|ψ_2p(0)|² = 0, so the 2p self-energy is zero at leading order. The 2s-2p splitting
equals approximately the 2s self-energy alone.

### DFC Systematic Prediction (Tier 2b)

Since the Lamb shift scales as α⁵ in leading order, and the DFC fine structure constant
at the electron mass scale (1/140.1) is 2.2% below the physical value (1/137.036), the
DFC Lamb shift prediction is below the observed value by approximately five times 2.2%,
which equals about 11%:

```
α_DFC(m_e) = 1/140.1  (observed: 1/137.036;  error: −2.2%)

DFC scaling prediction:
  Δν_DFC = Δν_obs × (α_DFC / α_obs)⁵
          = 1057.845 × (137.036/140.1)⁵
          = 1057.845 × 0.8953
          = 947 MHz

  Relative error: −10.5%   ✗ TIER 2b (exceeds 5% threshold)
```

The error budget across all DFC EM predictions (single source: α_em(m_e) = 1/140.1):

| Observable | α power | Predicted DFC error |
|---|---|---|
| H energy levels E_n | 2 | −4.4% (Tier 2a) |
| Thomson cross-section | 2 | −4.4% (Tier 2a) |
| Electron g-2 (leading) | 1 | −2.2% (Tier 2a) |
| **Lamb shift (leading)** | **5** | **−10.5% (Tier 2b)** |

Resolving the r_U1/λ derivation gap (Bottleneck 2) would correct α_em(m_e) and bring
the Lamb shift within the 5% threshold. Verified in `equations/lamb_shift.py` (Cycle 62).

---

## Consistency Checks

| Check | Status |
|---|---|
| Structural account consistent with DFC photon/electron picture | ✓ (structural) |
| Self-energy diagram topology same as QED | ✓ |
| g_em = √(4π α_em) from DFC chain available as input | ✓ (2.2% error in α_em at m_e) |
| Bethe formula includes correct 1/n³ factor for n=2 | ✓ (Cycle 62 fix) |
| DFC scaling prediction: 947 MHz vs observed 1057.845 MHz | ✗ −10.5% error — Tier 2b (Cycle 62) |
| Lamb shift from DFC self-energy loop integral (first principles) | ✗ OPEN — requires D5 photon propagator in hydrogen potential |
| Proton radius puzzle (muonic hydrogen discrepancy) addressed | ✗ OPEN |

---

## Open Questions

1. **DFC self-energy integral:** Compute ∫d⁴k D_μν(k) S_F(p−k) using the DFC D5 photon
   propagator (massless KG Green's function) and the DFC electron vertex factor (from
   g_em = e derived via β chain). Regulate with M_c(D5). Compare finite remainder to
   Bethe's 1947 result (1040 MHz for the dominant log term).

2. **UV structure of the DFC loop:** The Lamb shift integral in QED requires mass
   renormalization to separate the divergent and finite parts. In DFC, the closure scale
   M_c(D5) serves as a physical ultraviolet cutoff. Determine whether this cutoff changes
   the finite remainder relative to QED, or whether the two agree in the limit M_c → ∞.

3. **Proton radius puzzle:** Muonic hydrogen Lamb shift measurements give a proton charge
   radius that differs from electron hydrogen measurements by 4σ. DFC must account for
   whether the proton's D7 SU(3) closure structure differs in muonic vs. electronic context.

---

## Connections

- `equations/lamb_shift.py` — DFC scaling estimate (−10.5%); Bethe formula; error budget (Cycle 62)
- `phenomena/quantum/atomic_structure.md` — hydrogen energy levels from DFC coupling chain; same α_em
- `phenomena/quantum/anomalous_magnetic_moment.md` — g-2 (α¹ dependence; −2.2%); same root error
- `foundations/coupling_derivation.md` — g_em from β; DFC coupling chain; r_U1/λ gap source
- `foundations/bifurcation_mode_count.md` — Bottleneck 1; why DFC gauge structure gives this α
- `equations/atomic_structure.py` — QED running α_em from M_Z to m_e
- `equations/scattering_cross_sections.py` — Thomson σ_T (α² dependence; −4.4%); same root error
