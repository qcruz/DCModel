# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

**Last updated:** Cycle 488 (2026-09-01)

---

## How This Document Works

- **This is a living roadmap and todo list.** Add items as they come up. Remove items when done.
- **Task selection:** Cycle through tiers in order (P1→P2→P3→P4→P5→P6→P7→P1→...). Check the `Last tier worked:` marker below to determine the next tier. **Within each tier, always work the FIRST bullet point.** After working an item, move it to the BOTTOM of that tier's list. This ensures systematic coverage. If a tier has no actionable items, spend the cycle researching and adding new items to that tier. Update the marker after each cycle.
- **Item ordering:** Items within each tier are ordered by impact × tractability. UNBLOCKED items go to the top; BLOCKED/STUCK items go to the bottom. When new progress unblocks an item, move it up accordingly.
- **P5 = Exploratory, P6 = Documentation, P7 = Critical Review.** P7 exists to prevent the project from becoming locked into assumptions. It is a standing invitation to question, compare, reframe, and adapt.
- **Last tier worked: P2** (C488)
- **Never skip items because they are hard.** Always attempt incremental progress. Ruling out wrong approaches, documenting blockers, and outlining next steps are all valid progress.
- **Keep items short.** Detailed notes belong in equation modules, `ISSUES.md`, or `push_history.md` — not here.

---

## Priority 1 — High-Impact Predictions

- **Top quark mass from Koide** — UNBLOCKED. Koide formula with t=1/√Q_top gives m_t. Test against m_t = 172.69 GeV. Quick computation, high-impact if within 1%
- **DFC prediction for W mass** — UNBLOCKED. M_W = 79.67 GeV (−0.88%). CDF anomaly at 80.4335 GeV, CMS at 80.360 GeV. Timely — active experimental tension. See `equations/ew_radiative_corrections.py`
- **Muon anomalous magnetic moment (g−2)_μ** — major experimental target. C488: a_e upgraded to T2a. Compute a_μ through higher loops + hadronic LbL. High visibility. Partially blocked on hadronic VP
- **Derive pion mass from GMOR** — m_pi = 136.9 MeV (−1.9%, T2a with lattice condensate + isospin). Pure DFC −38% (NJL-limited). See `equations/pion_mass_gmor.py`
- **Derive light quark masses (D6 Yukawa)** — M0 = exp(-(b₀+1/α))×v/√2 run to 2 GeV: +2.68% T2a (C459). Mechanism needs T1 proof. See `equations/light_quark_mass_derivation.py`
- **Derive proton-neutron mass difference from DFC** — C467: Δm=1.289 MeV (−0.4%, T2b). C487: σ_πN=50.9 MeV (−2.2%, T2b). BLOCKED: derive C_QCD from DFC isovector matrix element. See `equations/proton_neutron_mass_difference.py`, `equations/pion_nucleon_sigma_term.py`
- **Beyond-mean-field Walecka EOS** — BLOCKED: C479 kink-background g₂ correct sign but 14× too weak. Need loop/resonance enhancement or NJL gap equation. See `equations/nuclear_kink_nonlinear_eos.py`
- **Derive V(phi) contact terms for deuteron binding** — BLOCKED: C473 central B_d=1.15 MeV (−48%). Need kink-kink overlap potential at r<1/Λ_QCD. See `equations/deuteron_tensor_ope.py`

---

## Priority 2 — Tier Upgrades

- **Upgrade Lamb shift to T2a** — UNBLOCKED. Existing module gives leading-order result. Add VP + self-energy corrections using DFC α_em chain (same technique as C488 a_e upgrade). See `equations/lamb_shift.py`
- **Close f_pi 1.6% gap** — traces to m_rho undershoot. Has equation module. See `equations/fpi_gap_closure.py`
- **Upgrade cosmological predictions to T2a** — broad impact. Λ_cosm (−3.5%), CMB ℓ₁ (+0.89%), BAO r_drag (−0.27%) all T3. Identify which tier bottleneck to close first
- **Upgrade proton charge radius to T2a** — C476: corrected to +1.5% (emp κ_p) or +2.5% (SU(6)). Needs: derive κ_p from DFC, regularize pion cloud. See `equations/proton_charge_radius_dfc.py`
- **Upgrade Delta-N splitting to T2b** — currently −7.4%, inherited from m_rho undershoot. See `equations/delta_n_splitting.py`
- **Derive hadronic VP δ(Δα)^NP = 0.00102** — PARTIALLY BLOCKED. C474: BW integral works for ρ. Parton subtraction negative. Need dispersive approach. Unblocks α_em(0) identity + muon g-2. See `equations/hadronic_vp_dfc.py`
- **Upgrade baryon Regge intercept to T2a** — BLOCKED on Y-junction penalty Δ=−1 (P3 item). See `equations/regge_intercept_derivation.py`
- **Prove alpha_em(0) identity A−B = ln(1/α_em(0))** — BLOCKED on hadronic VP (T4). Oldest open bottleneck. See `equations/alpha_em_dfc_chain.py`
- **Upgrade cosmological constant combination rule** — STUCK. Gap (iii) Casimir=α: 16 mechanisms tested, 7 ruled out. No derivation of exp(-α) found. See `equations/substrate_casimir_alpha.py`

---

## Priority 3 — Structural Gaps

- **Heavy quarkonium spectrum** — UNBLOCKED. Charmonium (J/ψ, ψ') and bottomonium (Υ) from Regge + Coulomb. Tests DFC string tension and α_s at different energy scales. Multiple testable predictions
- **Derive neutrino θ₂₃ from V(φ)** — NEARLY UNBLOCKED. C475: reduced to one unknown Δ_V/(2B)=0.0995 (D7 kink-vortex overlap integral). Same BVP as CKM. See `equations/neutrino_theta23_z3_mechanism.py`
- **Derive CKM/PMNS from D6/D7 overlap** — same overlap integral as θ₂₃. High impact: flavor mixing is a major SM gap
- **Derive Y-junction penalty = −1** — critical blocker for baryon Regge, Δ-N splitting. C463: NG Casimir gives Δ=1/8 (12.5%). 3 paths: quark-diquark, junction mode removal, WKB. See `equations/regge_intercept_derivation.py`
- **Baryon asymmetry magnitude** — Sakharov conditions met (T2a, C414). η_B magnitude T4. Compute CP violation strength from D6/D7 topology → predict η_B ~ 6×10⁻¹⁰
- **Dark matter mass and relic abundance** — m_DM=35.6 keV (T4, depth model). Relic abundance OPEN. High visibility. See `equations/cosmological_predictions_2.py`
- **Upgrade Koide phase t = 1/√Q_top to T1** — needs 5D Yukawa vortex integral
- **D4 gravity gap** — derive G_N from compression geometry. C469: perturbative approach misconceived (95.6% non-perturbative). BLOCKED on new approach. See `foundations/d4_gravity_gap.md`
- **Derive depth attenuation law exp(−S·d)** — gap (ii) CLOSED (C457). Action density argument gives WKB exp(-S*d). See `equations/depth_attenuation_law.py`
- **Prove substrate Casimir self-energy = α** — STUCK. 16 mechanisms tested, 7 ruled out. Best: I₄×Q_top=8/3 (+1.8%). See `equations/substrate_casimir_alpha.py`
- **Derive nuclear saturation from DFC couplings** — BLOCKED. C481: composite qq̄ nature of nuclear σ is root cause. Next: NJL gap equation. See `equations/nuclear_kink_nonlinear_eos.py`
- **Derive Bekenstein-Hawking entropy from V(φ)** — can S_BH = A/(4G) be derived from kink thermodynamics?
- **Derive ℏ from (α, β, c)** — BLOCKED on α_em(0) identity. See `ISSUES.md` T8
- **Bell: measurement dynamics from V(φ)** — how does kink nucleation implement spinor projection? T3 structural. See `equations/bell_joint_derivation.py` Part F step 6
- **Bell: joint Born rule substrate justification** — extend Born rule to tensor-product measurements. See `equations/bell_joint_derivation.py` Part F step 7
- **Bell: emergent relativistic locality** — show substrate connection produces no preferred frame. See `foundations/bell_hidden_variables.md`

---

## Priority 4 — Known Failures

- **Nuclear symmetry energy J** — NEARLY RESOLVED: was −36%, now +9.2% (T3). Reclassify? See `equations/nuclear_symmetry_energy.py`
- **M_W = 79.67 GeV (−0.88%)** — close to threshold. Traces to sin²θ_W running or EW corrections. See `equations/ew_radiative_corrections.py`
- **Charm/strange quark mass residual** — κ_q=πN_c/2: charm +0.29%, strange +2.09%. Small gap, may be closable
- **Neutrino mass ratio m₃/m₂** — κ=5.33 vs observed 5.81 (−8.3%). Depth ratio needs refinement. See `equations/neutrino_masses.py`
- **Nucleon magnetic moment ratio** — +2.75%. C470: dominated by isoscalar κ_S=−0.060 (sea quarks). −3/2+1/(8π) matches to 0.022%. BLOCKED on DFC sea quark content. See `equations/nucleon_magnetic_moments.py`
- **Nuclear surface diffuseness** — −20%, DFC m_sigma too heavy
- **Lithium problem** — BBN Li-7/H +194% vs obs. Same as standard BBN — DFC does not resolve. See `equations/bbn_predictions.py`
- **Triple-alpha Q value** — BLOCKED by SEMF failure for A < 12

---

## Priority 5 — Exploratory

- **Proton spin puzzle — direct I₀/I₁ from DFC kink BVP** — UNBLOCKED. C484: Σ=0.320 (−3.2%). Next: compute I₀/I₁ directly from DFC kink profile (numerical BVP) → T2b. See `equations/proton_spin_dfc.py`
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

---

## Priority 6 — Documentation

- **Update prediction scorecard** — `educational/06_predictions.md`. Pending: refined Σ (C484), J resolution (C483), Bell chain (C482), a_e T2a upgrade (C488), σ_πN (C487)
- **Update current_state.md** — major findings since last review (C419): proton charge radius fixed, light quark masses T2a, deuteron tensor, hadronic VP, θ₂₃, σ_πN, a_e upgrade
- **Create new educational modules** — continual check. Remaining:
  - **Born rule from V(φ) module** — full derivation chain V(φ)→Schrödinger→⟨ε⟩∝|ψ|²→rate∝|ψ|²
  - **Electroweak precision tests module** — collect M_W, M_Z, G_F, sin²θ_W, Γ_Z results
  - **Proton charge radius module** — C476 sign bug discovery + corrected prediction
- **Document audits (continuous)** — pick 2-4 random docs, check for stale tiers/refs/language
- **Practical applications** — add entries to `practical_applications/`
- **Archive/organize project docs** — consolidate, merge redundant docs
- **Update open questions** — `educational/07_open_questions.md`. C485: updated recently

---

## Priority 7 — Critical Review

This tier exists to keep the project honest and adaptive. The goal is not to defend
DFC but to stress-test it — compare against existing theories, identify where standard
approaches do better, question foundational assumptions, and adapt the model when
evidence warrants it. Mathematical verifiability is the standard; attachment to any
particular concept is not.

- **Identify unfalsifiable claims** — review all T3/T4 items. Which ones make no testable prediction? Which are structured so that any outcome can be accommodated? Flag these and either sharpen them into falsifiable predictions or demote them to speculative
- **Compare D-depth assignments against alternatives** — the D5=U(1), D6=SU(2), D7=SU(3) mapping is a working hypothesis. Are there alternative assignments or reframings that fit the data equally well or better? What would break the current assignment?
- **Evaluate practical relevance** — does DFC produce any result that is *useful* beyond matching existing measurements? Identify areas where DFC could inform experiment design, material science, engineering limits, or computational methods. If the answer is "not yet," document what would need to change
- **Review mathematical rigor of key claims** — select 2-3 core derivations and examine them for hidden assumptions, circular reasoning, or unjustified steps. Are the tier assignments honest? Could a skeptical mathematician follow each T1 proof?
- **Explore alternative frameworks** — are there other starting points (different potentials, different field content, different compression mechanisms) that could produce the same or better results? What is special about V(φ) = −α/2 φ² + β/4 φ⁴ vs. other double-well potentials?
- **Catalog what DFC cannot do** — maintain an honest list of phenomena that DFC has no account for, even in principle. This is different from P4 (known failures with partial results). This is about blind spots — things the framework does not even attempt
- **External literature comparison** — when a DFC result matches observation, check whether the same result has been derived elsewhere from different premises. If so, what does that tell us about the uniqueness (or non-uniqueness) of the DFC derivation?
- **Audit prediction quality vs. standard approaches** — C486: DONE. See `foundations/critical_review_predictions.md`. Four categories: SM-replicated (atomic, cosmo, EW), genuine value (couplings, N_c, strong CP, generations), SM-superior (loops, flavor), unfalsifiable (D1/D2, D4 gravity). Key finding: ~10 genuine predictions of SM free parameters from 2 inputs; rest is replication
