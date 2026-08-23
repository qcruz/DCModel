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
accuracy. This is genuine predictive reach -- DFC derives alpha_em from embedding
geometry, then that value correctly propagates through astrophysics without adjustment.

### Weaknesses and Root Causes

**Root cause 1 -- QHD-I is too stiff:** The Walecka linear sigma-omega model produces
a systematically stiff EOS at high density. Inflates NS max mass (~2.5 vs ~2.1 M_sun)
and NS radius (~14.5 vs ~12.5 km). Fix: add nonlinear sigma self-interaction (sigma^3,
sigma^4) from V(phi).

**Root cause 2 -- SEMF for light nuclei:** The semi-empirical mass formula is a smooth
liquid-drop model. Fails for A < 12 because shell effects, clustering, and tensor forces
dominate. Triple-alpha Q value requires binding energies of He-4, Be-8, C-12 -- all
where SEMF error is amplified by differences. Requires a different approach for light nuclei.

**Root cause 3 -- Nuclear saturation density:** The 42% overshoot in n_0 connects to
root cause 1. Linear QHD-I lacks scalar self-coupling that softens the EOS. Same fix.

### Caution on Overclaiming

Parts G (Jeans mass) and I (stellar lifetime) pass only at order-of-magnitude level.
These use rough approximations where almost any reasonable M_N and alpha_em would pass.
Should be tightened or flagged as "consistency checks" rather than "predictions."

---

## Tier 1: High-Impact, Feasible Now

### 1.1 Nonlinear Walecka EOS from V(phi)

Map the DFC substrate potential V(phi) = -alpha/2 phi^2 + beta/4 phi^4 onto the nuclear
sigma field self-interaction. The beta/4 phi^4 term directly provides the nonlinear sigma
coupling that softens the EOS.

**Expected impact:** NS radius drops from ~14.5 to ~12-13 km, NS max mass drops from
~2.5 to ~2.1 M_sun, saturation density improves. Fixes Parts B, D, and E simultaneously.

**Honest test:** The nonlinear coupling constants must come from beta, not be fitted.

**Deliverable:** `equations/nonlinear_walecka_eos.py`

### 1.2 Nuclear Binding for Light Nuclei (A <= 12) — COMPLETED (C418, NEGATIVE RESULT)

Coupled-channel deuteron (³S₁-³D₁ with tensor OPE) and He-4 variational Gaussian
calculations implemented. **Neither binds with DFC bare couplings.** Root cause: coupling
universality g_sigma = g_omega = M_N/f_pi from KSRF causes sigma-omega cancellation too
strong for nuclear binding. Net central potential only −0.58 MeV at 1 fm. Tensor OPE
improves slightly (E_min = −0.35 MeV) but insufficient.

**Resolution path:** Derive effective coupling asymmetry from V(φ) nonlinear sigma terms.
g₂ from C373 shifts effective g_sigma at nuclear density. If g_sigma/g_omega increases
by ~5-10% in medium, binding is restored.

**Deliverable:** `equations/light_nuclei_binding.py` (completed)

### 1.3 Deuteron Binding Energy — SUBSUMED BY 1.2

The deuteron coupled-channel calculation is now part of `light_nuclei_binding.py` (C418).
Same negative result: DFC bare couplings insufficient for binding. The path forward is
the effective coupling asymmetry from V(φ) nonlinear terms, not a separate deuteron module.

---

## Tier 2: Extend to New Domains

### 2.1 Atomic Physics Predictions

- Hydrogen ground state energy: E_1 = -alpha^2 m_e/2
- Rydberg constant: R_inf = alpha^2 m_e/(2h)
- Fine structure splitting: Delta_E = alpha^4 m_e/n^3 terms
- Lamb shift: tests QED loop corrections

**Gap:** DFC does not yet derive m_e independently (T3/T4 in mass hierarchy).

### 2.2 Cosmological Predictions

- **BBN helium fraction:** eta + tau_n (DFC T2a) -> Y_p ~ 0.245. Low-hanging fruit.
- **CMB acoustic peak positions:** First peak at l ~ 220 from sound horizon.
- **BAO scale:** r_s ~ 147 Mpc from DFC parameters.
- **Primordial helium fraction Y_p:** Y_p ~ 2n_n/(n_p + n_n) at freeze-out, directly
  from DFC tau_n = 878.0 s.

### 2.3 Stellar Structure

- Main sequence mass-luminosity relation: L proportional to M^3.5
- White dwarf mass-radius relation: R proportional to M^{-1/3}
- Minimum hydrogen-burning mass: ~0.08 M_sun from pp threshold

---

## Tier 3: Ambitious Stress Tests

### 3.1 Proton-Neutron Mass Difference

Delta_m = m_n - m_p = 1.293 MeV. Requires electromagnetic self-energy difference (from
alpha_em) plus quark mass difference contribution. Extremely demanding.

### 3.2 Pion Mass from Lambda_QCD

m_pi ~ 135 MeV. As pseudo-Goldstone boson, m_pi^2 proportional to m_q Lambda_QCD. DFC
gives Lambda_QCD = 304.5 MeV. Needs DFC quark masses.

### 3.3 Nuclear Magic Numbers from DFC

Shell closures at N,Z = 2, 8, 20, 28, 50, 82, 126. Arise from spin-orbit coupling in
nuclear potential. DFC's spin emergence (D6 Jackiw-Rebbi) should connect to nuclear
spin-orbit force. Extremely ambitious but would be a showpiece result.

---

## Priority Order

1. BBN helium fraction from DFC tau_n -- quick win, genuine prediction, new scorecard Part J
2. Nonlinear Walecka EOS from V(phi) -- fixes 3 existing predictions simultaneously
3. Deuteron binding energy -- clean nuclear test, no fitting
4. Tighten stellar lifetime -- replace factor-3 estimate with proper pp-chain luminosity
5. CMB/BAO predictions -- extends reach to cosmological observables

---

## Connections

- `equations/astrophysical_scorecard.py` -- current scorecard implementation
- `foundations/kink_nucleation.md` -- nuclear binding from kink structure
- `foundations/cosmological_constant_dfc.md` -- cosmological sector
- `foundations/mass_hierarchy.md` -- lepton/quark mass derivations needed for Tier 2-3
- `equations/neutron_lifetime.py` -- tau_n derivation (input to BBN)
- `equations/walecka_eos.py` -- current linear QHD-I (to be extended)
