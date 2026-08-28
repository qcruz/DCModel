# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

**Last updated:** Cycle 456 (2026-08-28)

---

## How This Document Works

- **This is a living roadmap and todo list.** Add items as they come up. Remove items when done.
- **Task selection:** Cycle through tiers in order (P1→P2→P3→P4→P5→P6→P1→...). Check the `Last tier worked:` marker below to determine the next tier. If a tier has no actionable items, spend the cycle researching and adding new items to that tier. Update the marker after each cycle.
- **P5 = Exploratory, P6 = Documentation.** Documentation is last so that new derivations and discoveries accumulate before the documentation pass, giving more material to document.
- **Last tier worked: P2** (C456)
- **Keep items short.** Detailed notes belong in equation modules, `ISSUES.md`, or `push_history.md` — not here.

---

## Priority 1 — High-Impact Predictions

- **Derive V(phi) contact terms for deuteron binding** — fix +187% overbinding. See `equations/deuteron_*.py`
- **Beyond-mean-field Walecka EOS** — fix NS radius, max mass, saturation density. See `equations/nuclear_saturation_dfc.py`
- **Derive proton-neutron mass difference** — predict 1.293 MeV. Blocked on light quark masses
- **Derive pion mass from GMOR** — blocked on light quark masses. See `equations/pion_mass_gmor.py`
- **Derive light quark masses (D6 Yukawa)** — HIGH-IMPACT BLOCKER (blocks 4+ items). Best candidate: exp(-b₀)×v/√2 at −7.8%. See `equations/light_quark_mass_derivation.py`

---

## Priority 2 — Tier Upgrades

- **Prove alpha_em(0) identity A−B = ln(1/α_em(0))** — oldest open bottleneck (T4→T1)
- **Derive hadronic VP δ(Δα)^NP = 0.00102** — close 1.5% gap in 36π chain
- **Upgrade cosmological constant combination rule** — gap (i) PI factorization CLOSED (C456, 12/12). Two gaps remain: (ii) depth attenuation, (iii) Casimir=α. See `equations/lambda_pi_factorization.py`
- **Close f_pi 1.6% gap** — traces to m_rho undershoot. See `equations/fpi_gap_closure.py`
- **Upgrade baryon Regge intercept to T2a** — Y-junction penalty Δ=−1 is T3 bottleneck. See `equations/regge_intercept_derivation.py`

---

## Priority 3 — Structural Gaps

- **D4 gravity gap** — derive effective metric, spin-2 mode, G_N from V(φ). See `foundations/d4_gravity_gap.md`
- **Derive neutrino θ₂₃ from V(φ)** — Z₃ holonomy mechanism identified. See `ISSUES.md` T10
- **Derive nuclear saturation from DFC couplings** — overlaps with P1 Walecka work
- **Derive Y-junction penalty = −1** — NG Casimir = 0 (T1), but gives Δ=−1/12 not −1
- **Upgrade Koide phase t = 1/√Q_top to T1** — needs 5D Yukawa vortex integral
- **Derive CKM/PMNS from D6/D7 overlap** — light quark part promoted to P1
- **Derive ℏ from (α, β, c)** — blocked on α_em(0) identity. See `ISSUES.md` T8
- **Derive depth attenuation law exp(−S·d)** — needed for Λ combination rule T2a
- **Prove substrate Casimir self-energy = α** — six mechanisms tested, none exact. See `equations/substrate_casimir_alpha.py`

---

## Priority 4 — Known Failures

- **Nucleon magnetic moment ratio** — +2.7% off, needs isospin violation
- **Proton charge radius** — −17.6% off, needs nucleon wavefunction
- **Delta-N mass splitting** — −7.4%, inherited from m_rho undershoot
- **Nuclear symmetry energy J** — −36%, needs larger g_rho
- **Nuclear surface diffuseness** — −20%, DFC m_sigma too heavy
- **Nolen-Schiffer residual** — ~7% CSB sources not computed
- **Chiral condensate undershoot** — −30% but NJL limitation, not DFC-specific. See `equations/chiral_condensate_running.py`
- **Triple-alpha Q value** — blocked by SEMF failure for A < 12

---

## Priority 5 — Exploratory

- **Freeform math exploration** — workspace: `equations/freeform_math_exploration.py`
- **Evaluate new open problems for DFC** — Navier-Stokes, baryon asymmetry, proton spin, quantum gravity
- **Investigate κ_q ≈ N_c·b₀/(2N_c+1) identity** — 0.03% match, coincidence or structural?
- **Investigate N_c·ln(2α)/2 ≈ α identity** — −5.2% match. See `equations/substrate_casimir_alpha.py`
- **Explore Δ/ξ = b₀/2 depth hypothesis** — 0.74% match for light quark Yukawa. See `equations/light_quark_mass_derivation.py`
- **Neutron star max mass** — naive flux-tube approach failed (−77%). Connects to P1 Walecka

---

## Priority 6 — Documentation

- **Create new educational modules** — continual check: review recent results for topics deserving new `educational/` docs
- **Update prediction scorecard** — `educational/06_predictions.md`
- **Update open questions** — `educational/07_open_questions.md`
- **Document audits (continuous)** — pick 2-4 random docs, check for stale tiers/refs/language
- **Practical applications** — add entries to `practical_applications/`
- **Archive/organize project docs** — consolidate, merge redundant docs, clean up structure
