# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

When I say "continue," start here. Pick the highest-priority unchecked item,
do it in one focused cycle, commit, push, then check it off.

**Last updated:** Cycle 427 (2026-08-26)

---

## How This Document Works

- Items are ordered by priority within each tier (P1 highest).
- Each item has a checkbox: `[ ]` = open, `[x]` = done, `[-]` = blocked.
- Sub-steps under each item are the concrete actions to take.
- When an item is completed, check it off and add the cycle number + result.
- When a new task is identified during work, add it to the appropriate priority tier.
- This file replaces both `ISSUES.md` and `DEVELOPMENT_NEXT_STEPS.md`.

---

## Priority 1 — High-Impact Predictions (do these first)

These extend DFC's quantitative prediction count or close significant gaps.

### P1.1 — Derive contact terms from V(phi) for deuteron binding
- **Goal:** Principled C_S, C_T values from V(phi) kink core to get quantitative B_d
- **Why:** PS f_pi = 89.63 MeV produces binding (B_cal = 6.39 MeV, +187%) but overbinds 3x.
  Contact terms would correct the short-range physics. Best calibrated match at f_pi ~ 92 MeV.
- **Current:** T3 partial (DFC produces binding, mechanism correct, quantitative match needs work)
- **Sub-steps:**
  - [ ] Compute V(phi) kink core contribution to short-range NN potential
  - [ ] Extract C_S, C_T contact parameters from kink profile
  - [ ] Re-run 2PE + contacts binding calculation
  - [ ] Compare B_d prediction to observed 2.2246 MeV
- **Files:** `equations/nuclear_2pi_exchange.py`, `equations/nuclear_coupling_asymmetry.py`
- **Blocking:** None — tractable with current tools

### P1.2 — Beyond-mean-field Walecka EOS
- **Goal:** Fix NS radius (~14.5 -> ~12-13 km), NS max mass (~2.5 -> ~2.1 M_sun), saturation density
- **Why:** Fixes astrophysical scorecard Parts B, D, E simultaneously. +48% coupling enhancement
  at saturation density (C419) is available but MF treatment is insufficient.
- **Current:** T4 (g_2 from V(phi) +1.2% vs NL3, but g_3 too small; K=2947 MeV)
- **Sub-steps:**
  - [ ] Implement RPA correlations or beyond-MF corrections to nonlinear Walecka EOS
  - [ ] Map V(phi) asymmetry to effective g_sigma/g_omega splitting at nuclear density
  - [ ] Compute corrected saturation properties (rho_0, E/A, K)
  - [ ] Recompute NS mass-radius relation with improved EOS
- **Files:** `equations/nonlinear_walecka_eos.py`, `equations/nuclear_kink_fluctuation.py`
- **Blocking:** May need new theoretical insight for V(phi) -> nuclear sigma mapping

### P1.3 — Stellar structure relations (new predictions)
- **Goal:** Derive mass-luminosity relation, WD mass-radius, minimum H-burning mass from DFC
- **Why:** New testable predictions using already-derived DFC parameters (alpha_em, M_N)
- **Current:** Not started
- **Sub-steps:**
  - [ ] Main sequence mass-luminosity relation: L proportional to M^3.5
  - [ ] White dwarf mass-radius relation: R proportional to M^{-1/3}
  - [ ] Minimum hydrogen-burning mass: ~0.08 M_sun from pp threshold
  - [ ] Create `equations/stellar_structure_predictions.py`
- **Files:** None yet
- **Blocking:** None — straightforward from existing DFC parameters

### P1.4 — Atomic physics predictions
- **Goal:** Hydrogen E_1, Rydberg constant, fine structure, Lamb shift from DFC alpha_em
- **Why:** Clean T2a predictions using the 36pi chain alpha_em
- **Current:** Not started
- **Sub-steps:**
  - [ ] Compute E_1 = -alpha^2 m_e/2 using DFC alpha_em (m_e as input)
  - [ ] Compute Rydberg constant R_inf
  - [ ] Compute fine structure splitting
  - [ ] Assess Lamb shift (tests QED loops — may need DFC-specific QED)
  - [ ] Create `equations/atomic_physics_predictions.py`
- **Files:** None yet
- **Blocking:** m_e not independently derived (T3/T4) — use as input for now

### P1.5 — Proton-neutron mass difference
- **Goal:** Derive Delta_m = m_n - m_p = 1.293 MeV
- **Why:** High-impact fundamental prediction; requires alpha_em + quark mass difference
- **Current:** Not started (T4)
- **Sub-steps:**
  - [ ] Compute EM self-energy difference from DFC alpha_em
  - [ ] Estimate quark mass contribution (m_d - m_u) from DFC quark mass derivation
  - [ ] Compare to observed 1.293 MeV
- **Files:** None yet
- **Blocking:** Needs m_u, m_d from DFC (currently not derived for light quarks)

### P1.6 — Pion mass from Lambda_QCD
- **Goal:** Derive m_pi ~ 135 MeV from DFC parameters
- **Why:** Fundamental prediction; m_pi^2 proportional to m_q Lambda_QCD
- **Current:** Not started (T4)
- **Sub-steps:**
  - [ ] Derive chiral symmetry breaking condensate from DFC
  - [ ] Compute m_pi via GMOR relation with DFC Lambda_QCD = 304.5 MeV
  - [ ] Compare to observed 139.57 MeV
- **Files:** None yet
- **Blocking:** Needs m_q (light quark masses) from DFC

---

## Priority 2 — Tier Upgrades (improve existing predictions)

These upgrade existing T3/T4 results toward T2a/T1.

### P2.1 — alpha_em(0) identity: A-B = ln(1/alpha_em(0))
- **Goal:** Prove algebraically (T4 -> T1)
- **Why:** Closes the oldest open bottleneck in the coupling chain
- **Current:** T4 structural identity
- **Sub-steps:**
  - [ ] Identify algebraic form of A and B from DFC parameters
  - [ ] Attempt proof from V(phi) structure
- **Files:** `equations/alpha_em_dfc_chain.py`

### P2.2 — Hadronic vacuum polarization: delta(Delta_alpha)^NP = 0.00102
- **Goal:** Close the 1.5% gap in the 36pi alpha_em chain
- **Why:** Would make alpha_em(0) fully derived; currently accounts for 98.5% of VP
- **Current:** T3 (two models bracket target: global +4.08x, local -0.35x)
- **Sub-steps:**
  - [ ] Develop D7 confinement spectral density model
  - [ ] Compute dispersive integral with improved spectral function
  - [ ] Close the 0.00102 gap
- **Files:** `equations/hadronic_vp_dispersive.py`, `equations/alpha_em_hadronic.py`

### P2.3 — String tension sigma = Q_top x Lambda^2 (T3 -> T2a)
- **Goal:** Derive string tension from D7 kink vacuum energy
- **Why:** Would upgrade all meson Regge predictions from T3 to T2a
- **Current:** T3 structural (-4.2% vs lattice)
- **Sub-steps:**
  - [ ] Derive sigma from Yang-Mills mass gap / D7 dynamics
  - [ ] Verify against lattice value
- **Files:** `equations/ym_string_tension.py`, `equations/meson_regge_spectrum.py`

### P2.4 — Cosmological constant combination rule (T3 -> T2a)
- **Goal:** Derive why rho_Lambda = M_Pl^4 x exp(-(T1+T2+T3))
- **Why:** Exponent is +0.05% accurate; the T3 gap is just the combination rule
- **Current:** T3 (each term individually T2a; combination T3)
- **Sub-steps:**
  - [ ] Derive the exponential suppression from substrate compression dynamics
  - [ ] Prove the additive exponent structure
- **Files:** `equations/cosmological_constant_prediction.py`

### P2.5 — f_pi: close remaining 2.7% gap
- **Goal:** Improve from -2.7% (PS) toward <1%
- **Why:** f_pi propagates into nuclear force predictions via 1/f_pi^4
- **Current:** T3 (PS gives 89.63 MeV, -2.7%; running mass worse at -21.3%)
- **Sub-steps:**
  - [ ] Investigate finite m_pi corrections (~1-2%)
  - [ ] Account for M_N(DFC) vs M_N(obs) (-0.45%)
  - [ ] Check higher-order PS corrections
- **Files:** `equations/fpi_correction_t18.py`, `equations/fpi_running_mass.py`

---

## Priority 3 — Structural Gaps (deep theory work)

### P3.1 — D4 gravity gap: metric emergence
- **Goal:** Derive g_mu_nu^eff from substrate dynamics
- **Why:** Deepest structural gap in DFC; resolves how gravity emerges
- **Current:** T4 (15 modules, many partial results, but no full metric)
- **Sub-steps:**
  - [ ] D4-B: Derive effective metric from substrate compression
  - [ ] D4-C: Show massless spin-2 mode emerges (hardest sub-gap)
  - [ ] D4-A: Connect M_Pl to V(phi) parameters (T3 via Jormungandr)
  - [ ] D4-D: Derive G_N coefficient (T3 via fixed-point)
- **Files:** `foundations/d4_gravity_gap.md`, 15 modules `equations/d4_*.py`

### P3.2 — Neutrino mixing angle theta_23: derive formula from V(phi)
- **Goal:** Close the 4-degree deviation from 45 degrees
- **Why:** Mechanism identified (Z_3 holonomy, T1 structural) but formula not derived
- **Current:** T4 (best candidates within 1 sigma of observed 49.26 degrees)
- **Sub-steps:**
  - [ ] Derive epsilon_d from D6/D7 interface dynamics
  - [ ] Select between candidate formulas using V(phi) arguments
- **Files:** `equations/neutrino_theta23_z3_mechanism.py`

### P3.3 — Nuclear saturation from DFC
- **Goal:** Derive saturation properties (rho_0, E/A, K) from V(phi) couplings
- **Why:** Connects DFC to bulk nuclear matter; validates coupling predictions
- **Current:** T4 (linear Walecka fails: rho_0 +42%, E/A +40%, K +600%)
- **Sub-steps:**
  - [ ] Beyond-MF corrections with V(phi) nonlinear sigma
  - [ ] RPA correlation energy
  - [ ] Compute improved K, E/A, rho_0
- **Files:** `equations/nuclear_walecka_prediction.py`
- **Connection:** Overlaps with P1.2

### P3.4 — Koide phase t = 1/sqrt(Q_top) derivation
- **Goal:** Derive the Koide formula phase from substrate topology
- **Why:** Would make tau mass prediction fully derived (currently uses Koide as structural input)
- **Current:** T4 (5D Yukawa vortex integral open)
- **Files:** `equations/koide_phase_coupling.py`

### P3.5 — CKM/PMNS matrices from D6/D7 overlap
- **Goal:** Derive mixing matrix elements from substrate geometry
- **Why:** 4 CKM + 3 PMNS parameters currently not derived
- **Current:** T4 (D6/D7 overlap integral not computed)
- **Sub-steps:**
  - [ ] Compute D6/D7 overlap integral
  - [ ] Extract mixing angles
- **Blocking:** Requires better understanding of D6/D7 interface

### P3.6 — Planck constant from (alpha, beta, c)
- **Goal:** Derive hbar from substrate parameters
- **Why:** Would close the gap to fully self-contained unit system
- **Current:** T4 (blocked by T12 / alpha_em chain)
- **Blocking:** P2.1 must close first

---

## Priority 4 — Known Limitations (acknowledge, fix when tractable)

These are predictions that are clearly wrong. Fix when an approach becomes available.

### P4.1 — Nucleon magnetic moment ratio (mu_p/mu_n = -1.500 vs obs -1.460, +2.7%)
- **Current:** T4. SU(6) ratio preserved because both scale as 1/m_q. Breaking requires
  isospin violation (strange sea, m_u != m_d, or pion cloud asymmetry).
- **Files:** `equations/prediction_tests_phase2.py`

### P4.2 — Proton charge radius (-17.6%)
- **Current:** T4. Missing ~0.13 fm^2 from intrinsic quark charge radius.
  MODEL LIMITATION — needs nucleon wavefunction.
- **Files:** `equations/prediction_tests_phase3.py`

### P4.3 — Delta-N mass splitting (+92% -> -40%)
- **Current:** T4. Need frozen infrared alpha_s ~ 0.72 (vs 0.43 from perturbative).
- **Files:** `equations/prediction_tests_phase3.py`

### P4.4 — Symmetry energy J (-36%)
- **Current:** T4. g_rho = g_omega/sqrt(N_c) = 5.57 gives J = 20.6 MeV vs obs 32 MeV.
  Needs g_rho = 8.59 for exact match.
- **Files:** `equations/phase3_corrections.py`

### P4.5 — Nuclear surface diffuseness (-20%)
- **Current:** T3. DFC bare m_sigma = 456.8 MeV gives surface too sharp.
  May resolve if m_sigma(effective) < m_sigma(bare) at nuclear density.
- **Files:** `equations/nuclear_msigma_resolution.py`

### P4.6 — Nolen-Schiffer residual (~7%)
- **Current:** T3. Three CSB sources identified (rho-omega mixing, pion mass splitting,
  neutron-proton mass difference) but not computed from DFC.
- **Files:** `equations/nuclear_nolen_schiffer.py`

### P4.7 — Triple-alpha Q value (FAIL)
- **Current:** Blocked by SEMF failure for A < 12. Needs light nuclei binding (P1.1).
- **Blocking:** P1.1

---

## Priority 5 — Documentation and Communication

### P5.1 — Educational modules (ongoing)
- Modules 00-28 exist. Continue adding new topics as predictions are made.
- [ ] Update `educational/06_predictions.md` when new predictions land
- [ ] Update `educational/07_open_questions.md` when issues close
- [ ] Create new modules for major breakthroughs (journaling format)

### P5.2 — Document audits (periodic)
- Every document should be reviewed periodically for accuracy, language compliance,
  stale references, and tier consistency.
- Pick a random document each cycle and audit it.

### P5.3 — Practical applications (every ~5-10 cycles)
- Entries in `practical_applications/` following `OVERVIEW.md` format.
- Derive engineering-relevant limits from verified (T1/T2a) DFC results.

---

## Priority 6 — Exploratory (when other priorities are blocked)

### P6.1 — Freeform mathematical exploration
- Workspace: `equations/freeform_math_exploration.py`
- Techniques: continued fractions, modular arithmetic, algebraic identities,
  number theory, exponential/log transforms, mass ratio analysis
- Promote significant findings to proper equation modules

### P6.2 — New open problem evaluation
- Candidates: Navier-Stokes, baryon asymmetry, dark matter identity,
  proton spin crisis, quantum gravity
- One cycle per candidate: write structural argument, identify DFC angle,
  record honestly where DFC adds nothing new

---

## Completed Items

| Item | Result | Cycle |
|------|--------|-------|
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

## Known Equation Module Issues

| Module | Issue |
|---|---|
| `gauge_couplings.py` | `squashing_correction()` returns None -- placeholder |
| `quantum_emergence.py` | Born rule assigned by definition (use `born_rule_*.py`) |
| `neutrino_masses.py` | m_2, m_3 from input Delta_m^2 -- not independent |
| `bifurcation_dynamics.py` | `gamma_from_beta()` RETRACTED |
| `closure_topology.py` | No stable minimum for n>=3 (Derrick's theorem) |
| `pair_production.py` | Large errors at sqrt(s)=29-55 GeV from missing gamma-Z interference |

---

## Quantities Not Yet Derived

| Quantity | Observed | Blocking Issue |
|---|---|---|
| m_pi | 139.57 MeV | Chiral SB mechanism from DFC (see P1.6) |
| m_u, m_d | 2.2, 4.7 MeV | Chiral SB + Yukawa from substrate |
| r_p | 0.8409 fm | Pion cloud integral (see P4.2) |
| m_n - m_p | 1.293 MeV | Needs m_d - m_u + EM (see P1.5) |
| Delta(1232)-N | 293 MeV | Frozen IR alpha_s (see P4.3) |
| N=184 magic | Predicted by some | SO strength / deformation |
| CKM elements | 4 params | D6/D7 overlap (see P3.5) |
| PMNS (theta_12, theta_13) | Known | D6 holonomy (see P3.5) |
| Absolute neutrino masses | Constrained | f_nu from substrate |
| sigma_piN | 52 MeV | Needs m_hat = (m_u+m_d)/2 |

---

## Open Blocked Derivations

| Target | Status | Key file |
|---|---|---|
| M_c(D7) from substrate | T2b; needs 2-loop C_match | `ym_sp5_mcdz_derivation.py` |
| hbar from (alpha, beta, c) | T4; blocked by P2.1 | -- |
| CKM/PMNS matrices | T4; see P3.5 | -- |
| SU(3) vs SO(6) | Largely resolved; J propagation proof open | `d5_complex_from_instability.py` |
| Koide t derivation | T4; see P3.4 | `koide_phase_coupling.py` |
| Series holonomy (Step 9c) | T3; KK reduction formal | -- |
| Collapse mechanism | T2a (C360) | `collapse_trigger_condition.py` |
