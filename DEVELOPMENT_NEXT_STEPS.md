# Development Next Steps: Prediction Accuracy & Mathematical Testing

**Status:** Active development roadmap
**Last updated:** August 2026

---

## Current Scorecard State

The astrophysical scorecard (`equations/astrophysical_scorecard.py`) tests DFC-derived
parameters against 15+ astrophysical observables across 9 categories (Parts A-I).

### Results Summary

| Part | Prediction | Error | Tier | Status |
|------|-----------|-------|------|--------|
| A | Chandrasekhar limit | <5% | T2a | PASS |
| B | NS max mass (QHD-I) | ~20% high | T3 | PASS (within 50%) |
| C1 | pp Gamow energy | <5% | T2a | PASS |
| C2 | CNO Gamow energy | <5% | T2a | PASS |
| C3 | Triple-alpha Q value | FAIL | -- | Known limitation |
| D | NS radius | +16.5% | T3 | PASS (within 30%) |
| E | SN bounce density | ~42% high | T3 | PASS (within factor 3) |
| F1 | Thomson cross section | <5% | T2a | PASS |
| F2 | Eddington luminosity | <1% | T2a | PASS |
| G | Jeans mass (recombination) | ~OOM | T3 | PASS (within factor 10) |
| H | Nuclear drip lines | Mixed | T3 | Partial PASS |
| I | Stellar lifetime | ~factor 2 | T3 | PASS (within factor 3) |

### Strengths

Strong predictions all trace to two T2a parameters: alpha_em = 1/136.98 and
M_N = 934.8 MeV. Any classical formula depending primarily on these (Chandrasekhar
limit, Gamow energies, Thomson cross section, Eddington luminosity) inherits their
accuracy. This is genuine predictive reach — DFC derives alpha_em from embedding
geometry, then that value correctly propagates through astrophysics without adjustment.

### Weaknesses and Root Causes

**Root cause 1 — QHD-I is too stiff:** The Walecka linear sigma-omega model produces
a systematically stiff EOS at high density. Inflates NS max mass (~2.5 vs ~2.1 M_sun)
and NS radius (~14.5 vs ~12.5 km). Fix: add nonlinear sigma self-interaction (sigma^3,
sigma^4) from V(phi). `equations/nonlinear_walecka_eos.py` exists but mean-field
treatment alone is insufficient — beyond-MF corrections needed.

**Root cause 2 — SEMF for light nuclei:** The semi-empirical mass formula is a smooth
liquid-drop model. Fails for A < 12 because shell effects, clustering, and tensor forces
dominate. Triple-alpha Q value requires binding energies of He-4, Be-8, C-12 — all
where SEMF error is amplified by differences.

**Root cause 3 — Coupling universality blocks nuclear binding:** DFC bare couplings
g_sigma = g_omega = M_N/f_pi from KSRF produce sigma-omega cancellation too strong
for nuclear binding (net central potential only −0.58 MeV at 1 fm). Tensor OPE
improves slightly but remains insufficient. Resolution requires deriving effective
coupling asymmetry from V(φ) nonlinear sigma terms.

### Caution on Overclaiming

Parts G (Jeans mass) and I (stellar lifetime) pass only at order-of-magnitude level.
These use rough approximations where almost any reasonable M_N and alpha_em would pass.
Should be tightened or flagged as "consistency checks" rather than "predictions."

---

## Completed Items

Items that were previously on the roadmap and have been delivered:

| Item | Deliverable | Result | Cycle |
|------|------------|--------|-------|
| BBN helium fraction | `bbn_predictions.py` | Y_p=0.2475 (+1.05%, 0.64σ) | C409 |
| CMB first peak + sound horizon | `cosmological_predictions.py` | ℓ₁=222 (+0.89%), r_s (−0.39%) | C410 |
| BAO drag scale | `cosmological_predictions_2.py` | r_drag=146.70 Mpc (−0.27%) | C412 |
| Inflation + baryon asymmetry | `cosmological_predictions_3.py` | n_s=0.9667, Sakharov conditions met | C414 |
| Stellar lifetime (pp-chain) | `stellar_lifetime_pp_chain.py` | Improved from factor-3 to factor-2 | C417 |
| Light nuclei binding | `light_nuclei_binding.py` | NEGATIVE RESULT: bare couplings don't bind | C418 |
| Nuclear magic numbers | `nuclear_shell_kappa.py` | All 7 standard magic numbers reproduced | C361 |
| Cosmological constant | `cosmological_constant_prediction.py` | ρ_Λ^{1/4}=2.16 meV (−3.5%, 0 free params) | C362 |
| Dark energy EOS | `cosmological_predictions_2.py` | w_Λ=−0.992 (within 1.3σ Planck) | C412 |

---

## Open Items: High Priority

### 1. Nonlinear Walecka EOS — Beyond Mean Field

The deliverable `equations/nonlinear_walecka_eos.py` exists, but mean-field treatment
alone is insufficient. g₂ from V(φ) kink-fluctuation expansion gives +1.2% vs NL3,
but g₃ from V(φ) quartic is too small, causing overbinding and K=2947 MeV.

**What's needed:** Beyond-mean-field corrections or a different mapping from V(φ) to
the nuclear sigma field that respects the asymmetry between g_sigma and g_omega at
nuclear density. This would fix NS radius, NS max mass, and saturation density
(scorecard Parts B, D, E) simultaneously.

**Expected impact:** NS radius ~14.5→~12-13 km, NS max mass ~2.5→~2.1 M_sun.

### 2. Nuclear Binding — Correlated Two-Pion Exchange

**C419 UPDATE:** The coupling asymmetry path was investigated in
`equations/nuclear_coupling_asymmetry.py`. V(φ) nonlinear sigma terms DO create a
structural asymmetry (+5.5% at deuteron density, +48% at saturation), but this is
INSUFFICIENT for deuteron binding. The dominant bottleneck is not coupling universality
but the bare sigma coupling strength: g_sigma = 9.645 is too weak for single-Yukawa
binding regardless of sigma mass or coupling ratio (threshold: g_sig/g_ome ~ 6.0).

**C420 2PE RESULT:** `equations/nuclear_2pi_exchange.py` computes the 2PE spectral
function from DFC g_A = 4/π and f_pi = Λ/π. The 2PE is 19x deeper than bare sigma
at r = 1 fm (−14.1 vs −0.73 MeV). S-wave binding with observed params: B = 4.3 MeV.
S-wave binding with DFC params: NOT BOUND. The 5.3% f_pi overshoot weakens 2PE by
19% (1/f_pi⁴ scaling), pushing the potential just below the binding threshold.

**C423 running mass result:** Pagels-Stokar with running quark mass M(k²) = M_q ×
[Λ²/(k²+Λ²)]^(6/11) gives f_pi = 72.49 MeV (−21.3%) — WORSE than constant-mass PS
(89.63 MeV, −2.7%). Running mass falls off too fast, dominating over bracket enhancement.
Constant-mass PS is the correct low-energy approximation and the best DFC f_pi prediction.

**KEY UPDATE:** Using PS f_pi = 89.63 MeV (below 96.5 MeV threshold), deuteron DOES bind
with 2PE. Remaining gap: quantitative B_d match requires contact terms from V(φ).

**Connection:** Item 1 (nonlinear Walecka EOS) benefits from the +48% coupling
enhancement at saturation density, even though Item 2 requires a different mechanism.

### 3. Triple-Alpha Q Value

Requires binding energies of He-4, Be-8, C-12 — all light nuclei where SEMF fails.
Blocked by Item 2 (need binding for light nuclei first). Low priority until coupling
asymmetry is resolved.

---

## Open Items: Medium Priority

### 4. Atomic Physics Predictions

- Hydrogen ground state energy: E_1 = -alpha^2 m_e/2
- Rydberg constant: R_inf = alpha^2 m_e/(2h)
- Fine structure splitting: Delta_E = alpha^4 m_e/n^3 terms
- Lamb shift: tests QED loop corrections

**Gap:** DFC does not yet derive m_e independently (T3/T4 in mass hierarchy).

### 5. Stellar Structure Relations

- Main sequence mass-luminosity relation: L proportional to M^3.5
- White dwarf mass-radius relation: R proportional to M^{-1/3}
- Minimum hydrogen-burning mass: ~0.08 M_sun from pp threshold

### 6. Proton-Neutron Mass Difference

Delta_m = m_n - m_p = 1.293 MeV. Requires electromagnetic self-energy difference
(from alpha_em) plus quark mass difference contribution. Extremely demanding.

### 7. Pion Mass from Lambda_QCD

m_pi ~ 135 MeV. As pseudo-Goldstone boson, m_pi^2 proportional to m_q Lambda_QCD.
DFC gives Lambda_QCD = 304.5 MeV. Needs DFC quark masses.

---

## Priority Order

1. Derive contact terms from V(φ) — PS f_pi = 89.63 MeV resolves the binding
   threshold issue (C423), but quantitative B_d match needs short-range contacts.
   DFC V(φ) kink core should provide principled C_S, C_T values.
2. Beyond-mean-field Walecka EOS with V(φ) asymmetry — +48% coupling enhancement at
   ρ₀ (C419); fixes NS radius, NS max mass, saturation density simultaneously
3. Atomic physics predictions — straightforward if/when m_e is derived
4. Stellar structure relations — extends astrophysical reach
5. Proton-neutron mass splitting — demanding but high-impact

---

## Connections

- `equations/astrophysical_scorecard.py` — current scorecard implementation
- `equations/nonlinear_walecka_eos.py` — current nonlinear EOS (MF insufficient)
- `equations/light_nuclei_binding.py` — deuteron/He-4 binding (negative result)
- `equations/nuclear_kink_fluctuation.py` — g₂ from V(φ) (+1.2% vs NL3)
- `equations/nuclear_kink_g3_vphi.py` — g₃ from V(φ) quartic
- `equations/bbn_predictions.py` — BBN predictions (completed)
- `equations/cosmological_predictions.py` — CMB/BAO predictions (completed)
- `equations/nuclear_shell_kappa.py` — magic numbers from DFC (completed)
- `foundations/mass_hierarchy.md` — lepton/quark mass derivations needed for Items 4-7
