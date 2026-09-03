# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

**Last updated:** Cycle 504 (2026-09-02)

---

## How This Document Works

- **This is a living roadmap and todo list.** Add items as they come up. Remove items when done.
- **Task selection:** Cycle through tiers in order (P1→P2→P3→P4→P5→P6→P7→P1→...). Check the `Last tier worked:` marker below to determine the next tier. **Within each tier, always work the FIRST bullet point.** After working an item, move it to the BOTTOM of that tier's list. This ensures systematic coverage. If a tier has no actionable items, spend the cycle researching and adding new items to that tier. Update the marker after each cycle.
- **Item ordering:** Items within each tier are ordered by impact × tractability. UNBLOCKED items go to the top; BLOCKED/STUCK items go to the bottom. When new progress unblocks an item, move it up accordingly.
- **P5 = Exploratory, P6 = Documentation, P7 = Critical Review.** P7 exists to prevent the project from becoming locked into assumptions. It is a standing invitation to question, compare, reframe, and adapt.
- **Last tier worked: P3** (C504)
- **Never skip items because they are hard.** Always attempt incremental progress. Ruling out wrong approaches, documenting blockers, and outlining next steps are all valid progress.
- **Keep items short.** Detailed notes belong in equation modules, `ISSUES.md`, or `push_history.md` — not here.
- **Spoke Dashboard:** Updated when a spoke's best tier, key gap, or last-touched cycle changes. Spokes not touched in 50+ cycles deserve priority attention during tier rotation.
- **Critical Blockers:** Updated when a blocker is resolved or a new multi-item blocker is discovered. When a blocker clears, promote newly-unblocked items upward in their tiers.
- **Pending Propagation:** Each P6 cycle picks one item from this queue. New results that need doc updates get added here immediately. Checked-off items are removed after 2 cycles.

---

## Priority 1 — High-Impact Predictions

- **DFC prediction for W mass** — RESOLVED. Tree-level M_W = 80.10 GeV (−0.34%), one-loop corrected M_W = 80.38 GeV (+0.009%, T2a). 10/10 PASS. CDF anomaly at 80.4335 GeV, CMS at 80.360 GeV — DFC matches CMS. See `equations/ew_radiative_corrections.py`
- **Muon anomalous magnetic moment (g−2)_μ** — major experimental target. C488: a_e upgraded to T2a. Compute a_μ through higher loops + hadronic LbL. High visibility. Partially blocked on hadronic VP
- **Derive pion mass from GMOR** — m_pi = 136.9 MeV (−1.9%, T2a with lattice condensate + isospin). Pure DFC −38% (NJL-limited). See `equations/pion_mass_gmor.py`
- **Derive light quark masses (D6 Yukawa)** — M0 = exp(-(b₀+1/α))×v/√2 run to 2 GeV: +2.68% T2a (C459). Mechanism needs T1 proof. See `equations/light_quark_mass_derivation.py`
- **Derive proton-neutron mass difference from DFC** — C467: Δm=1.289 MeV (−0.4%, T2b). C487: σ_πN=50.9 MeV (−2.2%, T2b). BLOCKED: derive C_QCD from DFC isovector matrix element. See `equations/proton_neutron_mass_difference.py`, `equations/pion_nucleon_sigma_term.py`
- **Beyond-mean-field Walecka EOS** — BLOCKED: C479 kink-background g₂ correct sign but 14× too weak. Need loop/resonance enhancement or NJL gap equation. See `equations/nuclear_kink_nonlinear_eos.py`
- **Derive V(phi) contact terms for deuteron binding** — BLOCKED: C473 central B_d=1.15 MeV (−48%). Need kink-kink overlap potential at r<1/Λ_QCD. See `equations/deuteron_tensor_ope.py`
- **Top quark mass from Koide** — C494: INVESTIGATED, NOT VIABLE. K=2/3 fails for all quark triplets. Best: (c,b,t) pole masses gives +17.7%. Quarks have QCD corrections + CKM mixing that leptons lack. t_actual=0.688 is 2.8% below lepton value — possible QCD correction but not derived. See `equations/top_quark_koide.py`

---

## Priority 2 — Tier Upgrades

- **Close f_pi 1.6% gap** — traces to m_rho undershoot. Has equation module. See `equations/fpi_gap_closure.py`
- **Upgrade cosmological predictions to T2a** — broad impact. Λ_cosm (−3.5%), CMB ℓ₁ (+0.89%), BAO r_drag (−0.27%) all T3. Identify which tier bottleneck to close first
- **Upgrade proton charge radius to T2a** — C476: corrected to +1.5% (emp κ_p) or +2.5% (SU(6)). Needs: derive κ_p from DFC, regularize pion cloud. See `equations/proton_charge_radius_dfc.py`
- **Upgrade Delta-N splitting to T2b** — currently −7.4%, inherited from m_rho undershoot. See `equations/delta_n_splitting.py`
- **Derive hadronic VP δ(Δα)^NP = 0.00102** — PARTIALLY BLOCKED. C474: BW integral works for ρ. Parton subtraction negative. Need dispersive approach. Unblocks α_em(0) identity + muon g-2. See `equations/hadronic_vp_dfc.py`
- **Upgrade baryon Regge intercept to T2a** — BLOCKED on Y-junction penalty Δ=−1 (P3 item). See `equations/regge_intercept_derivation.py`
- **Prove alpha_em(0) identity A−B = ln(1/α_em(0))** — BLOCKED on hadronic VP (T4). Oldest open bottleneck. See `equations/alpha_em_dfc_chain.py`
- **Upgrade cosmological constant combination rule** — STUCK. Gap (iii) Casimir=α: 16 mechanisms tested, 7 ruled out. No derivation of exp(-α) found. See `equations/substrate_casimir_alpha.py`
- **Upgrade nuclear symmetry energy J to T2a** — C490: RECLASSIFIED from P4 (was −36% failure, now +9.2% T3). Path: self-consistent m* from DFC Walecka + explicit Fock integral with DFC g_ρ. See `equations/nuclear_symmetry_energy.py`

---

## Priority 3 — Structural Gaps

- **Derive CKM/PMNS from D6/D7 overlap** — same overlap integral as θ₂₃. High impact: flavor mixing is a major SM gap
- **Derive Y-junction penalty = −1** — critical blocker for baryon Regge, Δ-N splitting. C463: NG Casimir gives Δ=1/8 (12.5%). 3 paths: quark-diquark, junction mode removal, WKB. See `equations/regge_intercept_derivation.py`
- **Baryon asymmetry magnitude** — Sakharov conditions met (T2a, C414). η_B magnitude T4. Compute CP violation strength from D6/D7 topology → predict η_B ~ 6×10⁻¹⁰
- **Dark matter mass and relic abundance** — m_DM=35.6 keV (T4, depth model). Relic abundance OPEN. High visibility. See `equations/cosmological_predictions_2.py`
- **Upgrade Koide phase t = 1/√Q_top to T1** — needs 5D Yukawa vortex integral
- **D4 gravity gap — derive correct bending prefactor** — C504: classical kink bending rigidity κ_raw=27.83 M_Pl² (55.7× M_Pl²/2). With 1/6 conformal factor: κ_geom=4.64 M_Pl² (9.3× overshoot). Problem is now: what is the correct prefactor? Factor needed=0.01797≈β/2. J₂=(π²−6)/9 exact [T1]. Three paths: (1) derive coupling prefactor from substrate self-gravity, (2) check if β=1/(9π) appears naturally, (3) numerical kink-on-curved-background. See `equations/d4_kink_bending_rigidity.py`, `equations/d4_sakharov_enhanced.py`
- **D4 gravity gap — non-perturbative enhancement** — derive G_eff(r) transition from G_N/23 to G_N. Coupled field+metric BVP (numerical). Priority B. See `foundations/d4_gravity_gap.md` §9
- **D4 gravity gap — emergent diffeomorphism** — identify symmetry protecting graviton mass. Priority C. See `foundations/d4_gravity_gap.md` §9
- **D4 gravity gap — numerical kink-kink simulation** — simulate V(φ) with two kinks, measure mutual attraction profile and coefficient. Bypasses analytical blockers. Priority D. See `foundations/d4_gravity_gap.md` §9
- **Derive depth attenuation law exp(−S·d)** — gap (ii) CLOSED (C457). Action density argument gives WKB exp(-S*d). See `equations/depth_attenuation_law.py`
- **Prove substrate Casimir self-energy = α** — STUCK. 16 mechanisms tested, 7 ruled out. Best: I₄×Q_top=8/3 (+1.8%). See `equations/substrate_casimir_alpha.py`
- **Derive nuclear saturation from DFC couplings** — BLOCKED. C481: composite qq̄ nature of nuclear σ is root cause. Next: NJL gap equation. See `equations/nuclear_kink_nonlinear_eos.py`
- **Derive Bekenstein-Hawking entropy from V(φ)** — can S_BH = A/(4G) be derived from kink thermodynamics?
- **Derive ℏ from (α, β, c)** — BLOCKED on α_em(0) identity. See `ISSUES.md` T8
- **Bell: measurement dynamics from V(φ)** — how does kink nucleation implement spinor projection? T3 structural. See `equations/bell_joint_derivation.py` Part F step 6
- **Bell: joint Born rule substrate justification** — extend Born rule to tensor-product measurements. See `equations/bell_joint_derivation.py` Part F step 7
- **Bell: emergent relativistic locality** — show substrate connection produces no preferred frame. See `foundations/bell_hidden_variables.md`
- **Heavy quarkonium spectrum** — C489: 5/7 PASS. Bottomonium M(1S) +3.3%, Δ(3S-1S) −18%. Charmonium splittings −7% to −16% but absolute mass +22% (α_s 25% low at m_c from 1-loop running). Path: 2-loop α_s. See `equations/quarkonium_spectrum.py`
- **Upgrade neutrino θ₂₃ to T2a** — C496: θ₂₃ = arctan(exp(1/(2π))) = 49.54° (+0.28°, 0.35σ, T3). For T2a: prove JR excess-norm governs Yukawa perturbation formally. See `equations/neutrino_theta23_z3_mechanism.py`

---

## Priority 4 — Known Failures

- **Nucleon magnetic moment ratio** — +2.75%. C470: dominated by isoscalar κ_S=−0.060 (sea quarks). −3/2+1/(8π) matches to 0.022%. BLOCKED on DFC sea quark content (NJL blocker). See `equations/nucleon_magnetic_moments.py`
- **Nuclear surface diffuseness** — −20%, DFC m_sigma too heavy
- **Lithium problem** — BBN Li-7/H +194% vs obs. Same as standard BBN — DFC does not resolve. See `equations/bbn_predictions.py`
- **Triple-alpha Q value** — BLOCKED by SEMF failure for A < 12

**Resolved (removed from P4):**
- ~~M_W = 79.67 GeV (−0.88%)~~ — RESOLVED C497: tree-level gap closed to +0.009% by standard one-loop Sirlin Δr corrections. See `equations/ew_radiative_corrections.py` (10/10 PASS, T2a)
- ~~Charm/strange quark mass residual~~ — RESOLVED C274: κ_q=πN_c/2 gives charm +0.29%, strange +2.09% (both T2a). See `equations/quark_mass_kappa_derivation.py`
- ~~Neutrino mass ratio m₃/m₂~~ — RESOLVED C204: color phase correction κ^(1+1/(6π)) = 5.8248 matches observed 5.8242 to +0.010% (T3, 0 free params). See `equations/neutrino_color_correction.py`

---

## Priority 5 — Exploratory

- **Prove y(v) = exp(-(b₀+1/α)) from kink overlap** — T2a numerics confirmed (C459), needs structural derivation for T1. See `equations/light_quark_mass_derivation.py`
- **DFC predictions for LHC Run 4** — high visibility. What does DFC predict differently from SM? Any distinctive signatures?
- **CMB-S4 predictions** — timely. n_s refinement, r upper bound, N_eff precision from DFC
- **Freeform math exploration** — workspace: `equations/freeform_math_exploration.py`. Feed blocked items here. C471: F*C = 300π² (T1 identity). Always available
- **Investigate κ_q ≈ N_c·b₀/(2N_c+1) identity** — 0.03% match, coincidence or structural?
- **Investigate mu_p/mu_n ≈ −3/2 + 1/(8π)** — 0.022% match. Is 1/(8π) derivable from kink binding? See E54
- **Investigate π+√N_c ≈ ln(1/α_em)** — −0.95% match. See E57
- **Investigate N_c·ln(2α)/2 ≈ α identity** — −5.2% match. See `equations/substrate_casimir_alpha.py`
- **Gravitational wave spectrum from D4** — spin-2 composite tensor mode propagation. Any GR deviation?
- **DFC implications for quantum computing** — qubit coherence limits from substrate structure
- **Neutron star max mass** — naive flux-tube failed (−77%). Connects to P1 Walecka
- **Condensed matter from V(φ)** — BCS gap, T_c predictions from existing modules
- **Evaluate new open problems for DFC** — Navier-Stokes, quantum gravity (proton spin DONE C477)
- **Proton spin puzzle — vector meson / 1/N_c corrections** — C498: e-scan shows I₀/I₁ saturates at ~0.186 for all e > 3. Pure ANW Skyrme gives Σ ≈ 0.23 regardless of e (systematic −28%). Next: include ρ/ω vector mesons (HLS) or compute 1/N_c corrections. See `equations/proton_spin_dfc.py`
- **Internal consistency web audit** — C501: PHASE 1 DONE. 7/7 core checks PASS. 35 stale BETA/g_eff values across 31 files found. Λ_QCD spread 124.6% (scheme differences). Phase 2: fix stale values, add cross-module derived-quantity checks. See `equations/consistency_web_audit.py`
- **Adversarial prediction hunting** — deliberately search for quantities where DFC *must* disagree with observation or SM. Not tracking known failures but proactively seeking new ones. A model that can't be wrong can't be right
- **Parameter sensitivity / fragility analysis** — perturb α=∛18, β=1/(9π), g_eff²=8/27 by ±0.1% and measure cascade of prediction errors. Distinguish robust structural predictions from numerologically fragile ones
- **Numerical substrate simulation** — simulate 1D field with V(φ) = −α/2 φ² + β/4 φ⁴ computationally. Do kink-antikink pairs form and bifurcate under compression? Do closure configurations emerge spontaneously?
- **Independent derivation paths** — for key results (α_s, sin²θ_W, m_p), find completely different derivation routes within DFC. Agreement = strong. Disagreement = hidden assumption exposed
- **Rigorous free-parameter accounting** — count every place a value is taken from observation (even implicitly). Compare total free inputs vs total independent predictions. This is the model's actual information-theoretic score
- **Phase diagram & extreme regime predictions** — QCD deconfinement T_c, quark-gluon plasma properties, neutron star max mass, EW phase transition order. Hard targets from lattice QCD and astrophysics
- **Analog system comparison** — identify condensed matter systems with double-well potentials and kink solutions (polyacetylene, ferroelectrics, superfluid ³He). Do they exhibit emergent gauge-like behaviors at domain boundaries?

---

## Priority 6 — Documentation

- **Update prediction scorecard** — `educational/06_predictions.md`. C492: added a_e, σ_πN, quarkonium, charm/strange updates. Remaining: quarkonium to hadron spectroscopy module
- **Create new educational modules** — continual check. Remaining:
  - **Born rule from V(φ) module** — full derivation chain V(φ)→Schrödinger→⟨ε⟩∝|ψ|²→rate∝|ψ|²
  - **Electroweak precision tests module** — collect M_W, M_Z, G_F, sin²θ_W, Γ_Z results
  - **Proton charge radius module** — C476 sign bug discovery + corrected prediction
- **Document audits (continuous)** — pick 2-4 random docs, check for stale tiers/refs/language
- **Practical applications** — add entries to `practical_applications/`
- **Archive/organize project docs** — consolidate, merge redundant docs
- **Update open questions** — `educational/07_open_questions.md`. C485: updated recently
- **Update current_state.md** — DONE C499: updated with C482–C498 results (θ₂₃, a_e, Lamb shift, M_W, σ_πN, Bell chain, e-scan, J reclassification)

---

## Priority 7 — Critical Review

This tier exists to keep the project honest and adaptive. The goal is not to defend
DFC but to stress-test it — compare against existing theories, identify where standard
approaches do better, question foundational assumptions, and adapt the model when
evidence warrants it. Mathematical verifiability is the standard; attachment to any
particular concept is not.

- **Evaluate practical relevance** — does DFC produce any result that is *useful* beyond matching existing measurements? Identify areas where DFC could inform experiment design, material science, engineering limits, or computational methods. If the answer is "not yet," document what would need to change
- **Review mathematical rigor of key claims** — select 2-3 core derivations and examine them for hidden assumptions, circular reasoning, or unjustified steps. Are the tier assignments honest? Could a skeptical mathematician follow each T1 proof?
- **Explore alternative frameworks** — are there other starting points (different potentials, different field content, different compression mechanisms) that could produce the same or better results? What is special about V(φ) = −α/2 φ² + β/4 φ⁴ vs. other double-well potentials?
- **Catalog what DFC cannot do** — maintain an honest list of phenomena that DFC has no account for, even in principle. This is different from P4 (known failures with partial results). This is about blind spots — things the framework does not even attempt
- **External literature comparison** — when a DFC result matches observation, check whether the same result has been derived elsewhere from different premises. If so, what does that tell us about the uniqueness (or non-uniqueness) of the DFC derivation?
- **Audit prediction quality vs. standard approaches** — C486: DONE. See `foundations/critical_review_predictions.md`. Four categories: SM-replicated (atomic, cosmo, EW), genuine value (couplings, N_c, strong CP, generations), SM-superior (loops, flavor), unfalsifiable (D1/D2, D4 gravity). Key finding: ~10 genuine predictions of SM free parameters from 2 inputs; rest is replication
- **Identify unfalsifiable claims** — C493: DONE. See `foundations/critical_review_predictions.md` Category 4 (expanded). 4 genuinely unfalsifiable (ontological framing), 5 currently unfalsifiable but sharpenable, 3 "danger zone" claims that could accommodate any outcome. Key action items: fix D-depth assignments, set T4 stagnation deadlines, attempt NJL gap equation
- **Rigorous free-parameter audit** — count every observational input across all equation modules. Compute true prediction-to-parameter ratio. Document where "0 free params" claims rely on implicit inputs
- **Compare D-depth assignments against alternatives** — C500: DONE. Exhaustive 6-permutation analysis added to `foundations/depth_assignment.md`. C1 (complexity ordering) + C4 (3 generations) uniquely select current assignment. Weakest link: C1 not derived from V(φ). See depth_assignment.md §Exhaustive Permutation Analysis

---

## Spoke Coverage Dashboard

The hub is V(φ). Each spoke is a physics domain radiating outward. This table tracks
development breadth — which spokes are strong, which are neglected, and where the
highest-leverage upgrades lie. Update this table whenever a spoke's best tier, gap
status, or last-touched cycle changes.

| # | Spoke | Best tier | Key modules | Key gaps | Last cycle |
|---|---|---|---|---|---|
| 1 | Coupling constants | T2a | alpha_em_prediction, alpha_em_selfconsistency, alpha_s_pure_dfc, d5_complex_from_instability | α_em(0) identity T4 (hadronic VP); Casimir=α T3 | C488 |
| 2 | Electroweak | T2a | muon_lifetime, weinberg_angle_rg, z_boson_decays, ew_radiative_corrections, ewsb_cocrystallization, higgs_potential | Muon g−2 hadronic T4; ~~M_W~~ resolved +0.009% | C497 |
| 3 | Hadron spectroscopy | T2a | meson_regge_spectrum, baryon_mass_dfc, quarkonium_spectrum, pion_mass_gmor, rho_meson_dfc | Y-junction Δ=−1 T3; hadronic VP T4; quarkonium α_s T3 | C489 |
| 4 | Nuclear physics | T3 | nuclear_symmetry_energy, nuclear_saturation_dfc, nuclear_dfc_periodic_table, deuteron_tensor_ope, nuclear_kink_nonlinear_eos | Deuteron B_d −48% T4; Walecka g₂ 14× weak T4; NJL gap eq. | C490 |
| 5 | Cosmology | T2a | cosmological_predictions, cosmological_predictions_2, cosmological_predictions_3, bbn_predictions, cosmology | Λ combination rule T3; η_B magnitude T4; DM relic T4 | C414 |
| 6 | Bell / QM foundations | T2a | bell_joint_derivation, born_rule_derivation, born_rule_schrodinger, collapse_mechanism | Measurement dynamics T3; joint Born rule T3; emergent locality T3 | C482 |
| 7 | Neutrino physics | T3 | neutrino_masses, neutrino_theta23_z3_mechanism, neutrino_casimir_depth | θ₂₃ = 49.54° (+0.35σ, T3); m₃/m₂ −8.3% T3; absolute mass scale T4 | C496 |
| 8 | Atomic physics | T2a | atomic_structure, atomic_physics_predictions, lamb_shift, fine_structure | Lamb shift T2a (−0.69%); remaining atomic predictions inherit α_em(0) offset | C495 |
| 9 | Gravity (D4) | T3 | d4_strong_field_metric, d4_einstein_from_jormungandr, d4_zero_mode_gravity, d4_gravity_spin2_enhancement + 13 more | 7 blockers mapped (C501); Sakharav EH = 2.4% M_Pl²; non-pert 93% open; spin-2 Candidate B viable T3 | C501 |
| 10 | Flavor / masses | T2a | koide_phase_coupling, light_quark_mass_derivation, quark_mass_kappa_derivation, generation_count_proof | CKM angles T4; top quark mass T4; τ dimple route 8.4× off | C459 |
| 11 | Proton structure | T2a | proton_spin_dfc, proton_charge_radius_dfc, nucleon_magnetic_moments, pion_nucleon_sigma_term | μ_p/μ_n sea quarks T4; charge radius pion cloud T3; pure Skyrme Σ −28% (needs HLS/1/N_c) | C498 |

**Reading this table:** Spokes at T2a are well-developed; T3 means structural account exists
but quantitative precision is limited; T4 means major derivation gaps remain. Spokes not
touched in 50+ cycles deserve priority attention. The "Key gaps" column shows what would
upgrade the spoke's best tier.

---

## Critical Blockers

Items that block 2 or more downstream tasks. Resolving these has outsized impact.
When a blocker is resolved, update this table and promote unblocked items in P1-P3.

| Blocker | Status | Unblocks |
|---|---|---|
| **Hadronic VP** δ(Δα)^NP = 0.00102 | T4 — dispersive approach needed | α_em(0) identity; muon g−2; all atomic physics T2b→T2a |
| **D6/D7 overlap integral** (kink-vortex BVP) | T4 — θ₂₃ resolved without BVP (C496); still needed for CKM | CKM/PMNS; baryon asymmetry magnitude |
| **Y-junction penalty Δ = −1** | T3 — Casimir gives 12.5% | Baryon Regge intercept T2a; Δ-N splitting T2b |
| **NJL gap equation** with DFC condensate | T4 — composite σ dynamics | Walecka EOS; nuclear saturation; pion mass (pure DFC); μ_p/μ_n sea quarks |
| **2-loop α_s running** | T3 — 1-loop implemented | Quarkonium absolute masses; charmonium M(1S) +22% gap |
| **D4 spin-2 enhancement** (factor ~23) | T4 — non-perturbative | G_N derivation; gravitational predictions; Planck scale |

---

## Pending Propagation

Results that have landed but need to be propagated to documentation, scorecards,
or other tracking. Each P6 cycle should pick one item from this queue. Check off
items when done; remove checked items after 2 cycles.

- [ ] C482: Bell chain T2a → update `educational/19_bell_inequalities.md` with full derivation chain
- [ ] C484: proton spin Σ refined to −3.2% → update `educational/31_proton_spin_puzzle.md`
- [ ] C496: θ₂₃ = arctan(exp(1/(2π))) = 49.54° (T4→T3) → update `educational/06_predictions.md` neutrino section
- [ ] C495: Lamb shift T2a upgrade (−0.69%) → update `educational/06_predictions.md` atomic section
- [x] C414–C417: cosmological predictions (inflation, baryogenesis, absence) → update `current_state.md` (DONE C499)
- [ ] Stellar census module (`equations/stellar_census_dark_energy.py`) 15/17 PASS → add to prediction scorecard
