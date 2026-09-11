# Electroweak Precision Tests

## What This Module Covers

The electroweak sector of particle physics is one of the most precisely measured
areas of all science. The W and Z boson masses, their decay widths, the Fermi
constant, and the Weinberg angle are known to parts per million or better. Any
framework claiming to describe particle physics must reproduce these numbers.

This module collects DFC's electroweak predictions in one place, explains where
each number comes from in the substrate framework, and honestly reports what
works, what is approximate, and what remains open.

---

## The DFC Electroweak Chain

Every electroweak prediction in DFC traces back to the substrate potential
V(φ) through a specific chain of derivations:

1. **V(φ) → gauge coupling.** The substrate quartic self-coupling β = 1/(9π)
   determines the gauge coupling squared: the square of the effective gauge
   coupling equals eight divided by twenty-seven. This comes from the moduli
   space metric of the kink solution.

2. **Gauge coupling → Weinberg angle.** The ratio of hypercharge to weak
   isospin couplings, combined with renormalization group running from
   the co-crystallization scale to the Z mass, gives the sine squared of
   the Weinberg angle: 0.2312 (observed: 0.2312, error: 0.01%).

3. **Weinberg angle → boson masses.** The W mass equals the Z mass times the
   cosine of the Weinberg angle. The Z mass comes from the electroweak
   vacuum expectation value divided by two times the cosine.

4. **Boson masses → decay widths.** Each partial width is computed from the
   coupling strength and phase space, following standard electroweak theory
   but with DFC-derived input parameters.

---

## Prediction Scorecard

### Tier 2a Predictions (all verified, less than 5% error)

**Weinberg angle** — The sine squared of the weak mixing angle equals 0.2312
at the Z mass scale. DFC derives this from the co-crystallization formula with
renormalization group running. The hypercharge embedding coefficient (three-fifths)
is derived from the D5 closure topology. The co-crystallization scale is the
single external input.
- Predicted: 0.2312
- Observed: 0.23121
- Error: 0.01%
- Module: `weinberg_angle_rg.py`

**W boson mass** — The W mass at tree level is 80.10 GeV (−0.34% from observation).
Including standard one-loop radiative corrections (the Sirlin formula, which
accounts for top quark loops breaking custodial symmetry), the prediction
improves to 80.38 GeV.
- Predicted: 80.38 GeV
- Observed: 80.377 GeV
- Error: +0.009%
- Inputs: m_t, m_H (SM masses entering loop corrections)
- Module: `ew_radiative_corrections.py`

**Z boson mass** — The Z mass comes from the muon lifetime formula inverted
to extract the electroweak VEV, combined with the Weinberg angle.
- Predicted: 90.86 GeV
- Observed: 91.1876 GeV
- Error: −0.36%
- Module: `muon_lifetime.py`

**Fermi constant** — The Fermi constant is the low-energy effective coupling
for weak interactions, determined by the W mass and the gauge coupling.
- Predicted: 1.168 × 10⁻⁵ GeV⁻²
- Observed: 1.166 × 10⁻⁵ GeV⁻²
- Error: +0.18%
- Module: `muon_lifetime.py`

**Muon lifetime** — The muon decays through W exchange. The lifetime depends
on the Fermi constant and the muon mass.
- Predicted: 2.180 μs
- Observed: 2.197 μs
- Error: −0.80%
- Inputs: m_μ (from DFC mass spectrum), M_W, sin²θ_W
- Module: `muon_lifetime.py`

**Z total width** — The Z decays to all kinematically allowed fermion pairs.
The total width sums all partial widths.
- Predicted: 2456 MeV
- Observed: 2495 MeV
- Error: −1.56%
- Module: `z_boson_decays.py`

**Z invisible width** — The Z decays to three neutrino species. The invisible
width directly counts the number of light neutrino generations.
- Predicted: 493 MeV
- Observed: 499.0 MeV
- Error: −1.16%
- Module: `z_boson_decays.py`

**Hadronic-to-leptonic ratio R_l** — The ratio of hadronic to leptonic Z
partial widths tests the color factor and quark couplings.
- Predicted: 20.746
- Observed: 20.767
- Error: −0.10%
- Module: `z_boson_decays.py`

**Bottom quark fraction R_b** — The fraction of Z hadronic decays going to
bottom quarks tests the b quark's electroweak couplings.
- Predicted: 0.2197
- Observed: 0.21629
- Error: +1.58%
- Module: `z_boson_decays.py`

**Leptonic forward-backward asymmetry** — The asymmetry in the angular
distribution of leptons from Z decay measures the vector-to-axial coupling ratio.
- Predicted: 0.01677
- Observed: 0.01626
- Error: +3.17%
- Module: `z_boson_decays.py`

---

## Error Budget

Nearly all electroweak errors trace to a single source: the M_Z prediction
is 0.36% low, and this propagates multiplicatively into every quantity that
depends on M_Z. The Z total width, for instance, scales roughly as the cube
of M_Z, so a −0.36% error in M_Z becomes approximately −1.1% in the width.

The M_Z error itself comes from the β chain: the electroweak VEV is derived
from the co-crystallization formula, which inherits a +0.65% offset. This
partially cancels against the Weinberg angle, leaving −0.36% in M_Z.

The W mass is more precise (+0.009%) because the one-loop Sirlin correction
absorbs the leading M_Z sensitivity through the ρ parameter.

---

## What DFC Adds Beyond Standard Model

The Standard Model treats the Weinberg angle, gauge couplings, and Higgs VEV
as independent measured parameters. DFC derives relationships between them:

1. The gauge coupling squared equals eight divided by twenty-seven — this is
   not an input but a consequence of the kink moduli space metric.

2. The Weinberg angle at the co-crystallization scale follows from the
   hypercharge embedding, which is derived from the D5 closure topology.

3. The electroweak VEV is connected to the co-crystallization scales at
   D5 and D6 depths through the co-crystallization formula.

These connections reduce the number of independent electroweak parameters.
The remaining inputs (m_t, m_H for loop corrections; the co-crystallization
scale for running) are not yet derived from V(φ).

---

## Open Questions

- Can the co-crystallization scale M_c be derived from (α, β), removing the
  last external input from the Weinberg angle prediction?
- Can the top quark mass be derived from DFC, making the W mass prediction
  fully self-contained?
- The leptonic forward-backward asymmetry error (+3.17%) is the largest in
  the electroweak sector — does this reflect a genuine DFC deviation or just
  missing higher-order corrections?
- The Z mass error (−0.36%) propagates into most other predictions. Closing
  the VEV gap (+0.65%) would improve the entire electroweak sector simultaneously.

---

## Consistency Check

| Prediction | DFC | Observed | Error | Tier |
|---|---|---|---|---|
| sin²θ_W(M_Z) | 0.2312 | 0.23121 | 0.01% | T2a |
| M_W | 80.38 GeV | 80.377 GeV | +0.009% | T2a |
| M_Z | 90.86 GeV | 91.188 GeV | −0.36% | T2a |
| G_F | 1.168×10⁻⁵ | 1.166×10⁻⁵ | +0.18% | T2a |
| τ_μ | 2.180 μs | 2.197 μs | −0.80% | T2a |
| Γ_Z | 2456 MeV | 2495 MeV | −1.56% | T2a |
| Γ_inv | 493 MeV | 499 MeV | −1.16% | T2a |
| R_l | 20.746 | 20.767 | −0.10% | T2a |
| R_b | 0.2197 | 0.2163 | +1.58% | T2a |
| A_FB^lep | 0.01677 | 0.01626 | +3.17% | T2a |

All ten electroweak predictions fall within T2a range (less than 5% error).
The systematic pattern — most errors negative and scaling with M_Z — confirms
a single-source error propagation rather than independent failures.
