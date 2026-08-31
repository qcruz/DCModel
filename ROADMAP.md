# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

**Last updated:** Cycle 480 (2026-08-30)

---

## How This Document Works

- **This is a living roadmap and todo list.** Add items as they come up. Remove items when done.
- **Task selection:** Cycle through tiers in order (P1→P2→P3→P4→P5→P6→P1→...). Check the `Last tier worked:` marker below to determine the next tier. **Within each tier, always work the FIRST bullet point.** After working an item, move it to the BOTTOM of that tier's list. This ensures systematic coverage. If a tier has no actionable items, spend the cycle researching and adding new items to that tier. Update the marker after each cycle.
- **P5 = Exploratory, P6 = Documentation.** Documentation is last so that new derivations and discoveries accumulate before the documentation pass, giving more material to document.
- **Last tier worked: P2** (C480)
- **Never skip items because they are hard.** Always attempt incremental progress. Ruling out wrong approaches, documenting blockers, and outlining next steps are all valid progress.
- **Keep items short.** Detailed notes belong in equation modules, `ISSUES.md`, or `push_history.md` — not here.

---

## Priority 1 — High-Impact Predictions

- **Derive proton-neutron mass difference** — 1.289 MeV (−0.4%, T2b with GL coeff C=0.50). Blocked on: derive C from DFC confinement. See `equations/proton_neutron_mass_difference.py`
- **Muon anomalous magnetic moment (g−2)_μ** — major experimental target. DFC has α_em chain + leading-order a_e. Compute a_μ from 36π chain + hadronic LbL. Compare to Fermilab/J-PARC measurement. High visibility
- **Derive pion mass from GMOR** — m_pi = 136.9 MeV (−1.9%, T2a with lattice condensate + isospin). Pure DFC −38% (NJL-limited). See `equations/pion_mass_gmor.py`
- **Derive pion-nucleon sigma term** — UNBLOCKED by C459 M0 derivation. Target: σ_πN ≈ 52 MeV
- **Top quark mass from Koide** — Koide formula with t=1/√Q_top gives m_t. Test against m_t = 172.69 GeV. High-impact if within 1%
- **Derive light quark masses (D6 Yukawa)** — M0 = exp(-(b₀+1/α))×v/√2 run to 2 GeV: +2.68% T2a (C459). Mechanism needs T1 proof. See `equations/light_quark_mass_derivation.py`
- **Derive V(phi) contact terms for deuteron binding** — C473: central B_d=1.15 MeV (−48%), bare tensor OPE overbinds ~30-60 MeV. Blocker: derive kink-kink overlap potential at r<1/Λ_QCD to determine NN form factor. See `equations/deuteron_tensor_ope.py`
- **DFC prediction for W mass** — M_W = 79.67 GeV (−0.88%). CDF anomaly at 80.4335 GeV, CMS at 80.360 GeV. What does DFC predict for the current tension? See `equations/ew_radiative_corrections.py`
- **Beyond-mean-field Walecka EOS** — C479: kink-background g₂<0 (correct sign!) but 14× too weak. Need loop/resonance enhancement. See `equations/nuclear_kink_nonlinear_eos.py`

---

## Priority 2 — Tier Upgrades

- **Upgrade electron a_e to T2a** — currently T2b (−0.14%, leading term only). Add Schwinger α/2π term using DFC α_em. See `equations/anomalous_magnetic_moment.py`
- **Close f_pi 1.6% gap** — traces to m_rho undershoot. See `equations/fpi_gap_closure.py`
- **Upgrade baryon Regge intercept to T2a** — Y-junction penalty Δ=−1 is T3 bottleneck. See `equations/regge_intercept_derivation.py`
- **Upgrade cosmological predictions to T2a** — Λ_cosm (−3.5%), CMB ℓ₁ (+0.89%), BAO r_drag (−0.27%) all T3. Identify which tier bottleneck to close first
- **Upgrade Delta-N splitting to T2b** — currently −7.4%, inherited from m_rho undershoot. See `equations/delta_n_splitting.py`
- **Prove alpha_em(0) identity A−B = ln(1/α_em(0))** — oldest open bottleneck (T4→T1). Blocked on hadronic VP (same T4 gap). See `equations/alpha_em_dfc_chain.py`
- **Upgrade Lamb shift to T2a** — existing module gives leading-order result. Need VP + self-energy corrections using DFC α_em chain. See `equations/lamb_shift.py`
- **Derive hadronic VP δ(Δα)^NP = 0.00102** — C474: Fixed π-factor NW bug. BW integral implemented (BW/NW=1.01 for ρ). ρ VP=0.00377 matches Davier 2π data. Parton subtraction framework gives NEGATIVE result — target requires R(s)−R_pQCD(s) difference, not BW−parton. Need dispersive approach. See `equations/hadronic_vp_dfc.py`
- **Upgrade proton charge radius to T2a** — C476: Foldy sign bug found (−17.6% was WRONG). Corrected: r_p=0.854 fm (+1.5%, emp κ_p) or 0.862 fm (+2.5%, SU(6) κ_p). Needs: derive κ_p from DFC, regularize pion cloud. See `equations/proton_charge_radius_dfc.py`
- **Upgrade cosmological constant combination rule** — gaps (i) CLOSED, (ii) CLOSED. Gap (iii) Casimir=α: C480 tested 4 more mechanisms (16 total, 7 ruled out). New T1: √(S_kink/(2π))=α^(3/2). No derivation of exp(-α) found. See `equations/substrate_casimir_alpha.py`

---

## Priority 3 — Structural Gaps

- **Derive nuclear saturation from DFC couplings** — overlaps with P1 Walecka work
- **Derive Y-junction penalty = −1** — Y-graph Casimir computed (C463): gives Δ=1/8 (12.5% of required). NG Casimir insufficient; non-Casimir mechanism needed. 3 paths: quark-diquark, junction mode removal, semiclassical WKB. See `equations/regge_intercept_derivation.py` Part I
- **Dark matter mass and relic abundance** — m_DM=35.6 keV (T4, depth model). Relic abundance OPEN. What DFC topology gives a stable DM candidate? See `equations/cosmological_predictions_2.py`
- **Upgrade Koide phase t = 1/√Q_top to T1** — needs 5D Yukawa vortex integral
- **Derive CKM/PMNS from D6/D7 overlap** — light quark part promoted to P1. NOTE: same D6/D7 overlap integral needed for θ₂₃ (see below)
- **Derive Bekenstein-Hawking entropy from V(φ)** — DFC has D4 gravity framework. Can S_BH = A/(4G) be derived from kink thermodynamics? Connects to holographic principle
- **Derive ℏ from (α, β, c)** — blocked on α_em(0) identity. See `ISSUES.md` T8
- **Derive depth attenuation law exp(−S·d)** — gap (ii) CLOSED (C457, 9/10). Action density argument: instanton confined to kink core → dS/dd = S_inst/ξ → WKB gives exp(-S*d). See `equations/depth_attenuation_law.py`
- **Prove substrate Casimir self-energy = α** — 12 mechanisms tested (C462), 5 ruled out, none exact. Best: I₄×Q_top=8/3 (+1.8%). New identity: α×√(2α)/2=N_c [T1]. Most promising path: show V''/2 enters as effective action (non-perturbative), or BPS saturation. See `equations/substrate_casimir_alpha.py`
- **D4 gravity gap** — derive effective metric, spin-2 mode, G_N from V(φ). C469: G_eff(r) transition question MISCONCEIVED — perturbative coupling flat at G_N/F=G_N/22.87 at all r>>ξ. No gradual transition exists. 95.6% non-perturbative at ALL scales. Path: derive G_N from compression geometry directly (not from perturbative enhancement). See `equations/d4_geff_transition.py`, `foundations/d4_gravity_gap.md`
- **Baryon asymmetry magnitude** — Sakharov conditions met (T2a, C414). η_B magnitude T4. Compute CP violation strength from D6/D7 topology → predict η_B ~ 6×10⁻¹⁰
- **Heavy quarkonium spectrum** — charmonium (J/ψ, ψ') and bottomonium (Υ) from Regge + Coulomb. Test DFC string tension and α_s at different scales
- **Derive neutrino θ₂₃ from V(φ)** — C475: mass matrix formalized. tan(2θ₂₃)=−2B/(F(2)×Δ_V) [T1]. Reduced to one unknown: Δ_V/(2B)=0.0995 (D7 kink-vortex overlap integral). Same BVP as CKM. See `equations/neutrino_theta23_z3_mechanism.py`

---

## Priority 4 — Known Failures

- **Nuclear symmetry energy J** — −36%, needs larger g_rho
- **Nuclear surface diffuseness** — −20%, DFC m_sigma too heavy
- **M_W = 79.67 GeV (−0.88%)** — traces to sin²θ_W running or higher-order EW corrections. Investigate whether DFC Δr parameter differs from SM. See `equations/ew_radiative_corrections.py`
- **Neutrino mass ratio m₃/m₂** — κ=5.33 vs observed 5.81 (−8.3%). Depth ratio needs refinement. See `equations/neutrino_masses.py`
- **Triple-alpha Q value** — blocked by SEMF failure for A < 12
- **Nucleon magnetic moment ratio** — +2.75% off. C470: ratio deviation dominated by isoscalar κ_S=−0.060 (sea quarks), not κ_V (pion cloud). Algebraic form −3/2+1/(8π) matches to 0.022% but origin unclear. Blocked on: predict κ_S from DFC sea quark content. See `equations/nucleon_magnetic_moments.py`
- **Lithium problem** — BBN Li-7/H = 4.7×10⁻¹⁰ (+194% vs obs). Same as standard BBN — DFC does not resolve this. Does DFC offer any new mechanism? See `equations/bbn_predictions.py`
- **Charm/strange quark mass residual** — κ_q=πN_c/2 gives charm +0.29% but strange +2.09%. Can the strange mass gap be closed?

---

## Priority 5 — Exploratory

- **Proton spin puzzle** — C477: VIABLE. Σ=g_A/N_c=4/(3π)=0.424 (+29%, 2.4σ). Spin crisis natural from 1/N_c suppression. Next: compute I₀/I₁ from DFC Y-junction profile → refined Σ [T2b target]. See `equations/proton_spin_dfc.py`
- **Investigate κ_q ≈ N_c·b₀/(2N_c+1) identity** — 0.03% match, coincidence or structural?
- **DFC predictions for LHC Run 4** — what does DFC predict differently from SM for upcoming collider experiments? Any distinctive signatures?
- **Investigate N_c·ln(2α)/2 ≈ α identity** — −5.2% match. See `equations/substrate_casimir_alpha.py`
- **Prove y(v) = exp(-(b₀+1/α)) from kink overlap** — T2a numerics confirmed (C459), needs structural derivation. See `equations/light_quark_mass_derivation.py`
- **Gravitational wave spectrum from D4** — DFC has spin-2 composite tensor mode. What are the propagation properties? Any deviation from GR waveform?
- **Investigate mu_p/mu_n ≈ −3/2 + 1/(8π)** — 0.022% match on ratio. Is 1/(8π) derivable from kink binding? See `equations/freeform_math_exploration.py` E54
- **Investigate π+√N_c ≈ ln(1/α_em)** — −0.95% match. See E57
- **DFC implications for quantum computing** — does substrate structure place limits on qubit coherence, entanglement rates, or quantum error correction? Connects to practical applications
- **Neutron star max mass** — naive flux-tube approach failed (−77%). Connects to P1 Walecka
- **CMB-S4 predictions** — what does DFC predict for CMB-S4 sensitivity targets? n_s refinement, r upper bound, N_eff precision
- **Condensed matter from V(φ)** — superconductivity, superfluidity modules exist. Can DFC predict BCS gap Δ or T_c for specific materials?
- **Freeform math exploration** — workspace: `equations/freeform_math_exploration.py`. Feed blocked items here. C471: E59-E63 explored queued items. Key finding: F*C = 300π² (T1 identity). F irreducible (factor 5 from I_6=16/15). kS has no DFC algebraic form. VMD gap traces to g_rho 19% too large. BW integral needed for δ(Δα)^NP.
- **Evaluate new open problems for DFC** — Navier-Stokes, baryon asymmetry, quantum gravity (proton spin DONE C477)

---

## Priority 6 — Documentation

- **Update open questions** — `educational/07_open_questions.md`
- **Document audits (continuous)** — pick 2-4 random docs, check for stale tiers/refs/language
- **Practical applications** — add entries to `practical_applications/`. Candidates: nuclear energy density limits, particle accelerator predictions, astrophysical observables
- **Update current_state.md** — major findings since last review (C419): proton charge radius fixed, light quark masses T2a, deuteron tensor analysis, hadronic VP corrections, θ₂₃ mass matrix
- **Archive/organize project docs** — consolidate, merge redundant docs, clean up structure
- **Create new educational modules** — continual check: review recent results for topics deserving new `educational/` docs. Hadron spectroscopy DONE (C472, module 30). Remaining:
  - **Born rule from V(φ) module** — full derivation chain V(φ)→Schrödinger→⟨ε⟩∝|ψ|²→rate∝|ψ|². Only mentioned in passing in modules 17/19 despite being a major result
  - **Proton charge radius module** — C476 sign bug discovery + corrected prediction. Good educational example of how careful derivation catches errors
  - **Electroweak precision tests module** — collect M_W, M_Z, G_F, sin²θ_W, Γ_Z results into one educational narrative
- **Update prediction scorecard** — `educational/06_predictions.md`. C478: added r_p correction, m_π, Δm(n−p), proton spin Σ, g_A. Next: add proton spin module 31 link
