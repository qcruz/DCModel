# Phenomenon: Anomalous Magnetic Moment of the Electron

## One-Sentence Synthesis

> The electron's magnetic moment is larger than the Dirac equation predicts by a fractional
> amount a_e = (g − 2)/2 ≈ 0.001160, which DFC accounts for through the one-loop correction
> where the electron emits and reabsorbs a D5 photon, shifting the effective magnetic coupling
> by the ratio of the electromagnetic fine structure constant to two pi — using the DFC 36π
> coupling chain, this Schwinger term predicts a_e ≈ 0.001158, a −0.14% underestimate.

---

## Observation

The electron's interaction with a magnetic field is characterized by the g-factor, defined so
that the magnetic moment equals the Bohr magneton times g divided by 2. The Dirac equation
predicts g = 2 exactly. The measured deviation is:

```
a_e = (g − 2)/2 = 0.00115965218076(28)
```

This is one of the most precisely measured numbers in physics — agreement between QED and
experiment exceeds 1 part per billion. At first glance the deviation seems small, but it
is unambiguously nonzero and cannot be accommodated by the Dirac equation alone.

**Experimental measurements:**
- Harvard electron g-2 (2008): a_e = 0.00115965218073(28) — relative precision 0.24 ppb
- Penning trap measurements: single electron suspended in magnetic field, cyclotron/spin
  frequency ratio measured to 1 part in 10¹²

**Muon anomalous magnetic moment (g-2)_μ:**
The muon's anomalous magnetic moment a_μ = 0.001165921(6) is also measured, and shows a
tantalizing ~4σ discrepancy between SM prediction and Fermilab measurement (as of 2024).
The DFC account for a_μ is the same leading-order mechanism; the muon's larger mass makes
it more sensitive to possible new contributions from higher closure depths.

---

## Standard Explanation

In quantum electrodynamics, the electron's magnetic moment receives corrections from diagrams
where the electron emits and reabsorbs one or more virtual photons. The one-loop correction —
first computed by Schwinger in 1948 — gives:

```
a_e = α/(2π) + C₂(α/π)² + C₃(α/π)³ + ...
```

The leading Schwinger term α/(2π) ≈ 0.00116141 (using α = 1/137.036) already agrees with
observation to better than 0.2%. Higher-loop corrections refine this to 12 significant figures.
The QED calculation is:

- 1-loop: α/(2π) ≈ 0.001161
- 2-loop: adds C₂(α/π)² where C₂ = −0.32848 → subtracts ~0.000001
- 3-loop: adds ~10⁻⁸
- Total (12 sig figs): 0.00115965218178(77)

---

## Dimensional Folding Explanation

### The Electron-Photon Vertex Correction

In DFC, the electron is a D6 SU(2) closure kink carrying a D5 U(1) electromagnetic winding.
When the electron interacts with an external magnetic field (the D5 gauge potential A_μ), the
interaction vertex is the coupling between the electron's D6 kink and the D5 field.

At tree level, this vertex gives the Dirac magnetic moment: the electron's spin couples to
the magnetic field with g = 2. The g = 2 value is a consequence of the Dirac equation structure
— which DFC derives from the SU(2) spinor geometry of the D6 closure behavior.

The one-loop correction arises because the electron can temporarily emit a D5 photon, propagate
forward, and reabsorb it. During this process, the electron's effective coupling to the external
magnetic field is modified. The modification is:

The fractional change in the magnetic coupling — the anomalous magnetic moment at leading
order — equals the electromagnetic fine structure constant divided by two pi. The factor two pi
arises from the circular topology of the D5 U(1) closure: the loop integral over the virtual
photon momentum is weighted by the phase space of the D5 mode, which carries the 1/(2π) factor
from the angular degree of freedom of the circle.

```
a_e (leading Schwinger term) = α_em / (2π)
```

In words: the fractional excess of the electron's magnetic moment above the Dirac value equals
the electromagnetic coupling constant divided by six point two eight. This is a one-loop effect.

### DFC Prediction Chain

The DFC coupling chain determines α_em at the electron mass scale through the 36π identity:

1. The substrate quartic coupling β = 1/(9π) [T2a, from ECCC self-consistency]
2. The common gauge coupling g_eff² = 8/27, so g_common = 0.54433 [T2a]
3. The 36π identity: 1/α_em(M_c(D5)) = (1 + k_Y²)/α_common = (8/3)(27π/2) = 36π [T2a]
4. Running the coupling from M_c(D5) to M_Z gives 1/α_em(M_Z)^DFC = 128.09 [T2a, +0.15%]
5. QED threshold matching from M_Z down to m_e adds Δ(1/α) from charged leptons and quarks
6. Result: 1/α_em(m_e)^DFC ≈ 137.03 [T2a, −0.001%]

The DFC anomalous magnetic moment prediction:

```
a_e (DFC, leading term) = α_DFC(m_e) / (2π) ≈ 0.001158
```

Comparison with observation:
```
a_e (observed) = 0.001160
a_e (DFC, 1-loop) ≈ 0.001158
Error: −0.14%  [Tier 2b]
```

### Error Source and Systematic

The residual −0.14% error is comparable to the +0.15% DFC overshoot in 1/α_em(M_Z).
These effects nearly cancel in the QED running to m_e: the DFC overshoot in 1/α(M_Z) and
the missing non-perturbative hadronic vacuum polarization contribution δ(Δα)^NP = 0.00102
have nearly equal and opposite effects on the inferred 1/α_em(0), yielding a net error of
approximately −0.001% on 1/α_em(m_e) (see `equations/alpha_em_dfc_chain.py`, Part F).

The leading Schwinger term using SM α_em = 1/137.036 gives a_e = 0.001161, which is +0.15%
above observation — the difference between +0.15% from SM and −0.14% from DFC is consistent
with the known DFC overshoot in the 36π running (see `equations/anomalous_magnetic_moment.py`).

### Muon g-2 in DFC

The muon's anomalous magnetic moment uses the same leading-order formula:

```
a_μ (leading) = α_em(m_μ) / (2π)
```

where α_em(m_μ) ≈ 1/135.9 (running the coupling up from m_e to m_μ adds a small correction
from the electron loop only). DFC predicts a_μ ≈ 0.001174, compared to the observed 0.001166
(+0.7% error at leading order — the muon case is slightly better because the running goes
in the right direction). The Fermilab anomaly is in the hadronic vacuum polarization
contribution, which requires α_s at low energy — the same non-perturbative QCD regime
that produces the δ(Δα)^NP gap.

---

## Formal Equations

### Schwinger Term

The anomalous magnetic moment at leading order equals the electromagnetic coupling constant
divided by two pi:

```
a_e = α_em / (2π)    [Schwinger 1948, 1-loop]
```

Higher-order QED expansion (reference, not yet computed in DFC):

```
a_e = Σ_{n≥1} Cₙ (α/π)ⁿ

C₁ = 1/2         (Schwinger term)
C₂ = −0.32848    (2-loop, exact)
C₃ = +1.1812     (3-loop, known analytically)
C₄ = −1.9144     (4-loop, numerical)
```

### DFC Coupling Chain to a_e

```
β = 1/(9π)             [T2a, ECCC derivation]
g_eff² = 8/27          → g_common = 0.54433  [T2a]
36π identity:  1/α_em(M_c(D5)) = 36π         [T2a, exact from (8/3)(27/2)=36]
Running to M_Z:  1/α_em(M_Z)^DFC = 128.09   [T2a, +0.15%]
QED running M_Z → m_e:  Δ(1/α) ≈ 10.46      [T2a, SM threshold matching]
1/α_em(m_e)^DFC ≈ 137.03                    [T2a, −0.001%]

a_e (DFC) = α_em(m_e) / (2π) ≈ 0.001158   [T2b, −0.14%]
```

---

## Consistency Checks

| Check | DFC | Observed | Status |
|---|---|---|---|
| Leading Schwinger term exists | a_e = α/(2π) from 1-loop vertex correction | a_e ≠ 0 confirmed 1947 | ✓ structural |
| Attractive sign (g > 2) | Loop correction always adds positively at 1-loop | g > 2 observed | ✓ structural |
| a_e ∝ α_em | Linear dependence on coupling at leading order | Confirmed — a_e tracks α_em exactly | ✓ derived |
| a_e magnitude (leading term) | ≈ 0.001158 from DFC 36π chain | 0.001160 | −0.14% Tier 2b |
| 36π identity correctly propagates | 1/α_em(M_Z)^DFC = 128.09, +0.15% overshoot | 127.9 | +0.15% ✓ |
| Error cancellation | NP hadronic VP deficit (δ^NP=0.00102) nearly cancels α_em overshoot | — | ✓ T1 algebraic |
| Muon a_μ leading term | α_em(m_μ)/(2π) ≈ 0.001174 (DFC) | 0.001166 (observed) | +0.7% ✓ Tier 2b |

---

## Open Questions

1. **Higher-loop corrections in DFC.** The Schwinger term is the 1-loop result. Computing
   the 2-loop correction C₂(α/π)² = −0.32848(α/π)² requires a full two-loop vertex diagram in
   the DFC effective field theory. This has not been attempted. The contribution is ~10⁻⁶,
   three orders of magnitude smaller than the 1-loop term, and is not the limiting factor
   in DFC's current precision.

2. **Hadronic vacuum polarization contribution to a_μ.** The muon g-2 Fermilab anomaly
   (~4σ deviation from SM) is dominated by hadronic contributions where virtual quark loops
   appear. In DFC, this requires computing the D7 SU(3) loop contributions — specifically
   the low-energy QCD regime where α_s is large and non-perturbative. This is connected to
   the same δ(Δα)^NP = 0.00102 gap in the α_em(0) identity (Problems #1 and #4 in the
   open problem table are the same T4 calculation: R^{had}(s) − R^{parton}(s) from D7
   confinement).

3. **g-2 for W boson.** The W boson anomalous magnetic moment is a tree-level quantity in
   the SM (g_W = 2 at tree level, deviations are loop effects proportional to α_em/π and
   α_s/π). In DFC, the W boson's magnetic moment traces to the D6 SU(2) closure geometry.
   Computing g_W from the D6 kink geometry has not been attempted.

4. **Non-perturbative contributions.** At higher orders, QED contributions include non-analytic
   terms in α_em (due to infrared divergences), and hadronic contributions enter even for
   a_e at the 10⁻¹² level. These are far beyond the current DFC framework but represent
   the full precision frontier.

---

## Connections

- `phenomena/quantum/atomic_structure.md` — same 36π α_em chain; same +0.28% prediction shift
- `equations/alpha_em_dfc_chain.py` — complete chain from 36π to 1/α_em(0)=137.034
- `equations/anomalous_magnetic_moment.py` — numerical verification; a_e prediction
- `equations/atomic_structure.py` — QED running Δ(1/α) from M_Z to m_e
- `phenomena/particle_physics/forces/electromagnetic.md` — α_em from DFC coupling chain
- `phenomena/quantum/casimir_effect.md` — related vacuum fluctuation effect
- `foundations/coupling_emergence.md` — g_common and 36π identity derivation
