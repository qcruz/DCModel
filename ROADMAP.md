# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

**Last updated:** Cycle 469 (2026-08-29)

---

## How This Document Works

- **This is a living roadmap and todo list.** Add items as they come up. Remove items when done.
- **Task selection:** Cycle through tiers in order (P1→P2→P3→P4→P5→P6→P1→...). Check the `Last tier worked:` marker below to determine the next tier. **Within each tier, always work the FIRST bullet point.** After working an item, move it to the BOTTOM of that tier's list. This ensures systematic coverage. If a tier has no actionable items, spend the cycle researching and adding new items to that tier. Update the marker after each cycle.
- **P5 = Exploratory, P6 = Documentation.** Documentation is last so that new derivations and discoveries accumulate before the documentation pass, giving more material to document.
- **Last tier worked: P3** (C469)
- **Never skip items because they are hard.** Always attempt incremental progress. Ruling out wrong approaches, documenting blockers, and outlining next steps are all valid progress.
- **Keep items short.** Detailed notes belong in equation modules, `ISSUES.md`, or `push_history.md` — not here.

---

## Priority 1 — High-Impact Predictions

- **Derive V(phi) contact terms for deuteron binding** — fix +187% overbinding. See `equations/deuteron_*.py`
- **Beyond-mean-field Walecka EOS** — fix NS radius, max mass, saturation density. See `equations/nuclear_saturation_dfc.py`
- **Derive proton-neutron mass difference** — 1.289 MeV (−0.4%, T2b with GL coeff C=0.50). Blocked on: derive C from DFC confinement. See `equations/proton_neutron_mass_difference.py`
- **Derive pion mass from GMOR** — m_pi = 136.9 MeV (−1.9%, T2a with lattice condensate + isospin). Pure DFC −38% (NJL-limited). See `equations/pion_mass_gmor.py`
- **Derive pion-nucleon sigma term** — UNBLOCKED by C459 M0 derivation. Target: σ_πN ≈ 52 MeV
- **Derive light quark masses (D6 Yukawa)** — M0 = exp(-(b₀+1/α))×v/√2 run to 2 GeV: +2.68% T2a (C459). Mechanism needs T1 proof. See `equations/light_quark_mass_derivation.py`

---

## Priority 2 — Tier Upgrades

- **Derive hadronic VP δ(Δα)^NP = 0.00102** — close 1.5% gap in 36π chain. C468: NW approximation overshoots 4-7x (ρ too broad for NW). Need full BW integral. See `equations/hadronic_vp_dfc.py`
- **Upgrade cosmological constant combination rule** — gaps (i) PI factorization CLOSED (C456), (ii) depth attenuation CLOSED (C457). One gap remains: (iii) Casimir=α. See `equations/lambda_pi_factorization.py`, `equations/depth_attenuation_law.py`
- **Close f_pi 1.6% gap** — traces to m_rho undershoot. See `equations/fpi_gap_closure.py`
- **Upgrade baryon Regge intercept to T2a** — Y-junction penalty Δ=−1 is T3 bottleneck. See `equations/regge_intercept_derivation.py`
- **Upgrade Delta-N splitting to T2b** — currently −7.4%, inherited from m_rho undershoot. See `equations/delta_n_splitting.py`
- **Prove alpha_em(0) identity A−B = ln(1/α_em(0))** — oldest open bottleneck (T4→T1). Blocked on hadronic VP (same T4 gap). See `equations/alpha_em_dfc_chain.py`

---

## Priority 3 — Structural Gaps

- **Derive neutrino θ₂₃ from V(φ)** — Z₃ holonomy mechanism identified. See `ISSUES.md` T10
- **Derive nuclear saturation from DFC couplings** — overlaps with P1 Walecka work
- **Derive Y-junction penalty = −1** — Y-graph Casimir computed (C463): gives Δ=1/8 (12.5% of required). NG Casimir insufficient; non-Casimir mechanism needed. 3 paths: quark-diquark, junction mode removal, semiclassical WKB. See `equations/regge_intercept_derivation.py` Part I
- **Upgrade Koide phase t = 1/√Q_top to T1** — needs 5D Yukawa vortex integral
- **Derive CKM/PMNS from D6/D7 overlap** — light quark part promoted to P1
- **Derive ℏ from (α, β, c)** — blocked on α_em(0) identity. See `ISSUES.md` T8
- **Derive depth attenuation law exp(−S·d)** — gap (ii) CLOSED (C457, 9/10). Action density argument: instanton confined to kink core → dS/dd = S_inst/ξ → WKB gives exp(-S*d). See `equations/depth_attenuation_law.py`
- **Prove substrate Casimir self-energy = α** — 12 mechanisms tested (C462), 5 ruled out, none exact. Best: I₄×Q_top=8/3 (+1.8%). New identity: α×√(2α)/2=N_c [T1]. Most promising path: show V''/2 enters as effective action (non-perturbative), or BPS saturation. See `equations/substrate_casimir_alpha.py`
- **D4 gravity gap** — derive effective metric, spin-2 mode, G_N from V(φ). C469: G_eff(r) transition question MISCONCEIVED — perturbative coupling flat at G_N/F=G_N/22.87 at all r>>ξ. No gradual transition exists. 95.6% non-perturbative at ALL scales. Path: derive G_N from compression geometry directly (not from perturbative enhancement). See `equations/d4_geff_transition.py`, `foundations/d4_gravity_gap.md`

---

## Priority 4 — Known Failures

- **Nucleon magnetic moment ratio** — +2.75% off. C464: isospin violation from DFC M0 gives WRONG SIGN (ratio moves further from obs). Blocked on: Dirac equation in PT kink potential with EM field. See `equations/nucleon_magnetic_moments.py`
- **Proton charge radius** — −17.6% off, needs nucleon wavefunction
- **Nuclear symmetry energy J** — −36%, needs larger g_rho
- **Nuclear surface diffuseness** — −20%, DFC m_sigma too heavy
- **Triple-alpha Q value** — blocked by SEMF failure for A < 12

---

## Priority 5 — Exploratory

- **Freeform math exploration** — workspace: `equations/freeform_math_exploration.py`. Feed blocked items here: when a derivation is stuck, add its equations/targets as exploration candidates. Queued from blocked work: Γ(ρ→ee) VMD 30% gap, δ(Δα)^NP parton subtraction, mu_p/mu_n ≈ −3/2+1/(8π), D4 enhancement F=(25π/3)√(2/α)=22.87 algebraic decomposition, F/C=25/(54α) identity
- **Evaluate new open problems for DFC** — Navier-Stokes, baryon asymmetry, proton spin, quantum gravity
- **Investigate κ_q ≈ N_c·b₀/(2N_c+1) identity** — 0.03% match, coincidence or structural?
- **Investigate N_c·ln(2α)/2 ≈ α identity** — −5.2% match. See `equations/substrate_casimir_alpha.py`
- **Prove y(v) = exp(-(b₀+1/α)) from kink overlap** — T2a numerics confirmed (C459), needs structural derivation. See `equations/light_quark_mass_derivation.py`
- **Investigate mu_p/mu_n ≈ −3/2 + 1/(8π)** — 0.022% match on ratio. Is 1/(8π) derivable from kink binding? See `equations/freeform_math_exploration.py` E54
- **Investigate π+√N_c ≈ ln(1/α_em)** — −0.95% match. See E57
- **Neutron star max mass** — naive flux-tube approach failed (−77%). Connects to P1 Walecka

---

## Priority 6 — Documentation

- **Create new educational modules** — continual check: review recent results for topics deserving new `educational/` docs
  - **Hadron spectroscopy module** — Regge trajectories, string tension, mass ratios as √(rational), Y-junction intercepts. No existing module covers meson/baryon mass spectrum.
  - **Born rule from V(φ) module** — full derivation chain V(φ)→Schrödinger→⟨ε⟩∝|ψ|²→rate∝|ψ|². Only mentioned in passing in modules 17/19 despite being a major result.
- **Update prediction scorecard** — `educational/06_predictions.md`
- **Update open questions** — `educational/07_open_questions.md`
- **Document audits (continuous)** — pick 2-4 random docs, check for stale tiers/refs/language
- **Practical applications** — add entries to `practical_applications/`
- **Archive/organize project docs** — consolidate, merge redundant docs, clean up structure
