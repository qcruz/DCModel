# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

**Last updated:** Cycle 434 (2026-08-27)

---

## How This Document Works

- **This is a living roadmap and todo list.** Add items as they come up. Remove items when done.
- **Task selection:** Pick randomly from ANY item across ALL priority tiers, unless the user gives more specific instructions.
- Completed items are removed from the active lists and recorded in the Completed Items table at the bottom.
- Each item should be readable at a glance: what will it add to project completeness?
- Priority tiers are for reference, not strict ordering.

---

## Priority 1 — High-Impact Predictions

These extend DFC's quantitative prediction count or close significant gaps.

- **Derive V(phi) contact terms for deuteron binding** — principled C_S, C_T from kink core to fix overbinding (currently +187%). Would give a quantitative B_d prediction.
- **Beyond-mean-field Walecka EOS** — fix NS radius (14.5 -> 12-13 km), max mass (2.5 -> 2.1 M_sun), and nuclear saturation density. Needs RPA or beyond-MF corrections.
- **Derive proton-neutron mass difference** — predict Delta_m = 1.293 MeV from DFC alpha_em + quark mass splitting. Blocked on light quark mass derivation.
- **Derive pion mass from Lambda_QCD** — predict m_pi ~ 135 MeV via GMOR relation with DFC Lambda_QCD = 304.5 MeV. Blocked on chiral symmetry breaking mechanism.

---

## Priority 2 — Tier Upgrades

Upgrade existing T3/T4 results toward T2a/T1.

- **Prove alpha_em(0) identity A-B = ln(1/alpha_em(0))** — oldest open bottleneck. T4 -> T1 would make all atomic/EM predictions fully derived.
- **Derive hadronic vacuum polarization delta(Delta_alpha)^NP = 0.00102** — close the 1.5% gap in the 36pi alpha_em chain. Needs D7 confinement spectral density.
- **Upgrade Regge intercept alpha_0 = 1/2 from T3 to T2a** — string tension is already T2a (C243), but the intercept remains T3 structural. Would upgrade all meson mass predictions.
- **Derive cosmological constant combination rule** — prove why rho_Lambda = M_Pl^4 x exp(-(T1+T2+T3)). Each term is T2a; combination is T3.
- **Close f_pi 2.7% gap** — investigate finite m_pi corrections and higher-order PS corrections. f_pi propagates into nuclear predictions via 1/f_pi^4.

---

## Priority 3 — Structural Gaps

Deep theory work on foundational questions.

- **D4 gravity gap: derive effective metric from substrate** — deepest structural gap in DFC. Derive g_mu_nu, massless spin-2 mode, and G_N from V(phi).
- **Derive neutrino theta_23 formula from V(phi)** — mechanism identified (Z_3 holonomy) but quantitative formula not derived. 4-degree deviation from 45 degrees.
- **Derive nuclear saturation from DFC couplings** — connect V(phi) to bulk nuclear matter (rho_0, E/A, K). Overlaps with P1 Walecka work.
- **Upgrade Koide phase t = 1/sqrt(Q_top) from T2a to T1** — current T2a derivation uses canonical vertex factor argument (C146). T1 upgrade requires computing the 5D Yukawa vortex integral directly from the D5/D6 kink overlap, bypassing the perturbative vertex expansion.
- **Derive CKM/PMNS matrices from D6/D7 overlap** — 4 CKM + 3 PMNS parameters currently not derived. Needs D6/D7 interface computation.
- **Derive Planck constant from (alpha, beta, c)** — close the gap to a fully self-contained unit system. Blocked on alpha_em(0) identity (P2).

---

## Priority 4 — Known Failures

Predictions that are clearly wrong. Fix when an approach becomes available.

- **Nucleon magnetic moment ratio** — mu_p/mu_n = -1.500 vs obs -1.460 (+2.7%). Needs isospin violation.
- **Proton charge radius** — -17.6% off. Missing intrinsic quark charge radius. Needs nucleon wavefunction.
- **Delta-N mass splitting** — +92% -> -40% range. Needs frozen infrared alpha_s ~ 0.72.
- **Nuclear symmetry energy J** — -36%. Needs larger g_rho (8.59 vs predicted 5.57).
- **Nuclear surface diffuseness** — -20%. DFC bare m_sigma = 456.8 MeV too heavy.
- **Nolen-Schiffer residual** — ~7% CSB sources identified but not computed from DFC.
- **Triple-alpha Q value** — blocked by SEMF failure for A < 12.

---

## Priority 5 — Documentation

- **Update prediction scorecard** — add new predictions to `educational/06_predictions.md` as they land
- **Update open questions** — revise `educational/07_open_questions.md` when issues close
- **Clean cycle numbers from 07_open_questions.md** — has dozens of (C###) references that violate the no-cycle-numbers-in-educational-docs rule. Needs full rewrite to remove cycle tracking and present current state cleanly.
- **Document audits (continuous)** — every few cycles, pick 2-4 random docs and review for: stale tier labels, outdated references (e.g. ISSUES.md), cycle numbers in public docs, language rule violations, factual inconsistencies with current model state. This is a permanent item — never remove it.
- **Practical applications** — add entries to `practical_applications/` from verified T1/T2a results

---

## Priority 6 — Exploratory

- **Freeform mathematical exploration** — continued fractions, modular arithmetic, algebraic identities on DFC constants. Workspace: `equations/freeform_math_exploration.py`
- **Evaluate new open problems for DFC** — candidates: Navier-Stokes, baryon asymmetry, dark matter identity, proton spin crisis, quantum gravity. One cycle per candidate.

---

## Completed Items

| Item | Result | Cycle |
|------|--------|-------|
| String tension tier fix | sigma = Q_top x Lambda^2 already T2a (C243), not T3; meson module updated | C433 |
| Atomic physics predictions | R_inf -0.28%, a_0 +0.14%, fine struct -0.73%, hyperfine -0.50%, 11/11 PASS | C430 |
| Stellar structure predictions | sigma_T +0.08%, WD R +0.62%, M_HBMM +0.40%, 12/12 PASS | C429 |
| M_W one-loop correction | 80.38 GeV (+0.009%), T24 CLOSED | C427 |
| Meson Regge spectrum | m_rho -1.5%, m_a2 +0.3%, 4/4 within 2%, 0 free params | C425 |
| Calibrated deuteron binding | B_cal = 6.39 MeV, DFC produces binding from derived params | C424 |
| f_pi running mass test | Running mass WORSE (-21.3%); constant-mass PS (-2.7%) is best | C423 |
| Nuclear coupling asymmetry | V(phi) creates +5.5% at deuteron, +48% at saturation; insufficient alone | C419 |
| 2PE binding mechanism | 2PE 19x deeper than bare sigma; f_pi is the bottleneck | C420 |
| Inflation + baryon asymmetry | n_s = 0.9667, Sakharov conditions met, 6 absence predictions | C414 |
| BAO drag scale | r_drag = 146.70 Mpc (-0.27%) | C412 |
| Dark energy EOS | w_Lambda = -0.992 (within 1.3 sigma Planck) | C412 |
| CMB first peak | ell_1 = 222 (+0.89%), r_s (-0.39%) | C410 |
| BBN helium fraction | Y_p = 0.2475 (+1.05%, 0.64 sigma) | C409 |
| Cosmological constant | rho_Lambda^{1/4} = 2.16 meV (-3.5%, 0 free params) | C362 |
| Nuclear magic numbers | All 7 standard magic numbers reproduced | C361 |
| Neutrino depth shift | delta_d = 1/(6pi) T2a via JR-BPS | C354 |
| Quark masses (kappa_q) | kappa_q = pi*N_c/2 from center vortex; charm +0.29% | C274 |
| Stellar lifetime (pp-chain) | Improved from factor-3 to factor-2 | C417 |
| Light nuclei binding | NEGATIVE RESULT: bare couplings don't bind | C418 |
| Yang-Mills Clay proof | Internally complete, 12 citations, 0 T2a on critical path | C322 |
| Born rule | T2a, two independent derivation routes | C339/C359 |
| Strong CP theta=0 | T2a, S^5 CP isometry | C147/C157 |
| Tau lepton mass (Koide) | 1776.97 MeV (+0.006%) | C146 |
| EWSB vacuum v | 247.83 GeV (+0.65%) | C145 |
| alpha_s(M_Z) ECCC | 0.11821 (+0.006%) | C144 |
| alpha_em(M_Z) 36pi | 1/128.09 (+0.15%) | C141 |
| Bottleneck 2 (coupling) | g_eff^2 = 8/27 from V(phi) | C117 |
| Bottleneck 1 (D7=SU(3)) | n coincident modes -> SU(n) | C59-74 |

---

## Retracted Claims

| Claim | Retracted | Replacement |
|---|---|---|
| gamma_D = (16/3)sqrt(beta) | C48 | E_kink/E_total = 8/3 exactly |
| beta ~ 0.035 from gamma_D | C48 | beta = 1/(9pi) derived T2a (C117) |
| E_kink formula (pre-BPS) | C47 | BPS-correct: E_kink = (4/3)c*alpha^(3/2)/(beta*sqrt(2)) |
| sigma_geom +/- 0.8 GeV (Higgs) | C38 | Corrected to +/- 3.4 GeV; m_H = 124.4 +/- 3.7 GeV |

---

## Reference: Known Module Issues

| Module | Issue |
|---|---|
| `gauge_couplings.py` | `squashing_correction()` returns None -- placeholder |
| `quantum_emergence.py` | Born rule assigned by definition (use `born_rule_*.py`) |
| `neutrino_masses.py` | m_2, m_3 from input Delta_m^2 -- not independent |
| `bifurcation_dynamics.py` | `gamma_from_beta()` RETRACTED |
| `closure_topology.py` | No stable minimum for n>=3 (Derrick's theorem) |
| `pair_production.py` | Large errors at sqrt(s)=29-55 GeV from missing gamma-Z interference |

---

## Reference: Quantities Not Yet Derived

| Quantity | Observed | Blocking Issue |
|---|---|---|
| m_pi | 139.57 MeV | Chiral SB mechanism from DFC |
| m_u, m_d | 2.2, 4.7 MeV | Chiral SB + Yukawa from substrate |
| r_p | 0.8409 fm | Pion cloud integral |
| m_n - m_p | 1.293 MeV | Needs m_d - m_u + EM |
| Delta(1232)-N | 293 MeV | Frozen IR alpha_s |
| N=184 magic | Predicted by some | SO strength / deformation |
| CKM elements | 4 params | D6/D7 overlap |
| PMNS (theta_12, theta_13) | Known | D6 holonomy |
| Absolute neutrino masses | Constrained | f_nu from substrate |
| sigma_piN | 52 MeV | Needs m_hat = (m_u+m_d)/2 |

---

## Reference: Open Blocked Derivations

| Target | Status | Key file |
|---|---|---|
| M_c(D7) from substrate | T2b; needs 2-loop C_match | `ym_sp5_mcdz_derivation.py` |
| hbar from (alpha, beta, c) | T4; blocked by alpha_em identity | -- |
| CKM/PMNS matrices | T4 | -- |
| SU(3) vs SO(6) | Largely resolved; J propagation proof open | `d5_complex_from_instability.py` |
| Koide t derivation | T4 | `koide_phase_coupling.py` |
| Series holonomy (Step 9c) | T3; KK reduction formal | -- |
| Collapse mechanism | T2a (C360) | `collapse_trigger_condition.py` |
