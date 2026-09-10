# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

**Last updated:** Cycle 566 (2026-09-10)

---

## How This Document Works

- **This is a living roadmap and todo list.** Add items as they come up. Remove items when done.
- **Task selection:** Cycle through tiers in order (P1→P2→P3→P4→P5→P6→P7→P8→P1→...). Check the `Last tier worked:` marker below to determine the next tier. **Within each tier, always work the FIRST bullet point.** After working an item, move it to the BOTTOM of that tier's list. This ensures systematic coverage. If a tier has no actionable items, spend the cycle researching and adding new items to that tier. Update the marker after each cycle.
- **Item ordering:** Items within each tier are ordered by impact × tractability. UNBLOCKED items go to the top; BLOCKED/STUCK items go to the bottom. When new progress unblocks an item, move it up accordingly.
- **P5 = Exploratory, P6 = Documentation, P7 = Critical Review, P8 = Simulations.** P7 exists to prevent the project from becoming locked into assumptions. P8 builds numerical demonstrations that DFC dynamics actually produce the claimed behaviors from V(φ).
- **Last tier worked: P7** (C566 — Free parameter audit: 15 T2a predictions, 5/6 PASS, 4 DFC geometric params, Ratio 3.0)
- **Never skip items because they are hard.** Always attempt incremental progress. Ruling out wrong approaches, documenting blockers, and outlining next steps are all valid progress.
- **Keep items short.** Detailed notes belong in equation modules, `ISSUES.md`, or `push_history.md` — not here.
- **Spoke Dashboard:** Updated when a spoke's best tier, key gap, or last-touched cycle changes. Spokes not touched in 50+ cycles deserve priority attention during tier rotation.
- **Critical Blockers:** Updated when a blocker is resolved or a new multi-item blocker is discovered. When a blocker clears, promote newly-unblocked items upward in their tiers.
- **Pending Propagation:** Each P6 cycle picks one item from this queue. New results that need doc updates get added here immediately. Checked-off items are removed after 2 cycles.

---

## Priority 1 — High-Impact Predictions

- **Muon anomalous magnetic moment (g−2)_μ** — BLOCKED on α_em(0) identity. C525: Path (a) TWO-LOOP RULED OUT. Gap is structural (+0.11%), not perturbative. Remaining: (b) DFC-specific running, (c) sub-percent ECCC/k_Y correction. See `equations/alpha_em_two_loop_correction.py`
- **Derive pion mass from GMOR** — C537: NJL-LIMITED. m_pi = 136.9 MeV (−1.9%, T2a with lattice condensate). Pure DFC = 86 MeV (−38%, T3). BLOCKED: needs beyond-NJL condensate. See `equations/pion_mass_gmor.py`
- **Derive light quark masses (D6 Yukawa)** — C544: DOWNGRADED T2a→T2b (+24% at 2-loop). Formula structurally interesting (0 free params) but prediction is order-dependent. See `equations/light_quark_mass_derivation.py`
- **Derive proton-neutron mass difference from DFC** — C552: NJL route +17% (T2b). BLOCKED: vertex corrections needed to reduce C_QCD from 0.87 to ~0.50. See `equations/proton_neutron_mass_difference.py`
- **Beyond-mean-field Walecka EOS** — C560: C₂(NJL)/C₂(NL3) = 0.87. Remaining: NJL sigma mass (226 MeV) vs physical (500-648 MeV). See `equations/nuclear_kink_nonlinear_eos.py` Part G
- **Derive V(phi) contact terms for deuteron binding** — BLOCKED: C473 B_d=−48%. C563: OBE too weak regardless of sigma mass or coupling ratio. Needs iterated OPE / 2π exchange (see P3). See `equations/deuteron_tensor_ope.py`, `equations/light_nuclei_binding.py` Part E

**Resolved (removed from P1):**
- ~~W mass~~ — RESOLVED C497: M_W = 80.38 GeV (+0.009%, T2a). See `equations/ew_radiative_corrections.py`
- ~~Top quark mass from Koide~~ — NOT VIABLE C494: K=2/3 fails for all quark triplets. See `equations/top_quark_koide.py`

---

## Priority 2 — Tier Upgrades

- **Derive hadronic VP δ(Δα)^NP = 0.00102** — C520: REFRAMED. Gap is from 36π formula, not VP. DFC VP overshoots data +27%. See `equations/hadronic_vp_dfc.py`
- **Upgrade baryon Regge intercept to T2a** — BLOCKED on Y-junction penalty Δ=−1 (P3 item). See `equations/regge_intercept_derivation.py`
- **Prove alpha_em(0) identity A−B = ln(1/α_em(0))** — BLOCKED. C525: two-loop/threshold corrections RULED OUT (path a). Gap is structural (+0.11%), not perturbative. Remaining: path (b) DFC-specific running, path (c) sub-percent ECCC/k_Y correction. See `equations/alpha_em_two_loop_correction.py`
- **Upgrade cosmological Λ to T2a** — STUCK. CMB ℓ₁ (+0.89%) and BAO r_drag (−0.27%) already T2a. Only Λ_cosm remains T3 — bottleneck is Casimir=α combination rule (16 mechanisms tested, 7 ruled out). See `equations/cosmological_predictions.py`, `equations/substrate_casimir_alpha.py`
- **Upgrade nuclear symmetry energy J to T2a** — C490: +9.2% T3. Path: self-consistent m* from DFC Walecka + Fock integral with DFC g_ρ. See `equations/nuclear_symmetry_energy.py`
- **Close f_pi 1.6% gap** — C521: M(p) ruled out. Gap traces to m_rho undershoot. BLOCKED on m_rho/σ correction. See `equations/fpi_gap_closure.py`
- **Upgrade proton charge radius to T2a** — C545: VMD-regulated pion cloud (m_ρ cutoff) gives r_p = 0.809 fm (−3.8%, T2a). DFC-only with SU(6) κ_p=2 and VMD pion cloud, 0 free params. Remaining: derive κ_p from DFC magnetic moments (currently SU(6) approximation). See `equations/proton_charge_radius_dfc.py`
- **Upgrade Delta-N splitting to T2b** — C561: FORMALLY T3, NUMERICALLY T2b (−7.4%). Part F added: empirical intercepts from 6 PDG states show α₀^N(ground)=−0.26 (matches DFC −0.25) but excited states deviate (trajectory curvature). Mass ratio m_Δ/m_N = √(5/3) = −1.68% (0 free params). BLOCKED: formal upgrade requires deriving Y-junction penalty Δ=−7/4 (P3 item). See `equations/delta_n_splitting.py`

---

## Priority 3 — Structural Gaps

- **D4 gravity gap — reduce κ overshoot** — C508: thick-wall κ=2.04 (4.1×). C534: Helfrich κ=4.64 (9.3×, no backreaction). Problem is EXCESS, not deficit. C528: 1+1D Yukawa confirmed; power-law needs transverse integration. NEXT: gravitational self-consistency, 5D→4D normalization, emergent diffeomorphism (graviton mass protection). See `equations/d4_thick_wall_bvp.py`, `equations/helfrich_membrane_gravity.py`, `equations/kink_kink_potential.py`
- **Prove substrate Casimir self-energy = α** — STUCK. 16 mechanisms tested, 7 ruled out. Best: I₄×Q_top=8/3 (+1.8%). See `equations/substrate_casimir_alpha.py`
- **Derive nuclear saturation from DFC couplings** — BLOCKED. C481: composite qq̄ nature of nuclear σ is root cause. Next: NJL gap equation. See `equations/nuclear_kink_nonlinear_eos.py`
- **Derive Bekenstein-Hawking entropy from V(φ)** — C511: S/A = 1/(2k) = 0.2486 (-0.57%, inherits kappa gap). Not independent prediction. Can kink thermodynamics give deeper derivation?
- **Warp-modified Yukawa overlap** — C511: warp factor reduces needed separation by 18% for e/t hierarchy. k*xi=1.76 is significant. Integrate warp into C510 overlap derivation
- **Warp factor correction to generation spacing** — C511: spacing ratio 1.89 (not constant). Connects to kappa_q=3pi/2 generation parameter
- **Derive ℏ from (α, β, c)** — BLOCKED on α_em(0) identity. See `ISSUES.md` T8
- **Bell: measurement dynamics from V(φ)** — how does kink nucleation implement spinor projection? T3 structural. See `equations/bell_joint_derivation.py` Part F step 6
- **Bell: joint Born rule substrate justification** — extend Born rule to tensor-product measurements. See `equations/bell_joint_derivation.py` Part F step 7
- **Bell: emergent relativistic locality** — show substrate connection produces no preferred frame. See `foundations/bell_hidden_variables.md`
- **Heavy quarkonium spectrum** — C489: 5/7 PASS. Bottomonium M(1S) +3.3%, Δ(3S-1S) −18%. Charmonium splittings −7% to −16% but absolute mass +22% (α_s 25% low at m_c from 1-loop running). Path: 2-loop α_s. See `equations/quarkonium_spectrum.py`
- **Upgrade neutrino θ₂₃ to T2a** — C496: θ₂₃ = arctan(exp(1/(2π))) = 49.54° (+0.28°, 0.35σ, T3). For T2a: prove JR excess-norm governs Yukawa perturbation formally. See `equations/neutrino_theta23_z3_mechanism.py`
- **Derive CKM/PMNS from D6/D7 overlap** — C522: diagonal Z3 FAILS for θ₁₂ (F(1)=F(2), T1 proof). Must be off-diagonal. Best: sin(θ_C)=1/π (+43%). GST sin=√(m_d/m_s) works at -0.6% — path is through DFC quark mass ratio. BLOCKED: need formal off-diagonal BVP. See `equations/ckm_from_d6d7_overlap.py`
- **Upgrade Lorentz emergence to T1 via analog gravity theorem** — Barcelo et al. (2001): non-dispersive medium => exact Lorentz invariance at low energy. DFC substrate is non-dispersive in vacuum (V''(phi_0)=const). Citation upgrades T3 -> T1. See `foundations/gravity_theory_integration.md`
- **Derive Hawking temperature from V(phi)** — analog gravity gives T_H from surface gravity of effective metric horizon. Substrate profile determines all ingredients. See `foundations/gravity_theory_integration.md`
- **Derive open→closed mode transition from coupled PDE** — C526: structural argument in place (T2a). Need formal derivation showing kink formation creates bound states for subsequent fluctuations. See `equations/depth_bifurcation_dynamics.py` Part A
- **Derive WHY SU(2) is broken but SU(3) is not from V(φ)** — C526: structural argument (EWSB vs confinement, T2a). Need to derive from substrate dynamics that D6 sector acquires VEV while D7 does not. See `equations/depth_bifurcation_dynamics.py` Part D
- **Derive threshold positions α₅, α₆, α₇** — C526: currently T4. Compute compression budget per bifurcation from V(φ). See `equations/depth_bifurcation_dynamics.py` Part F
- **GAUGE EMERGENCE: zero-mode degeneracy → local gauge symmetry** — C531: ENERGETIC ARGUMENT COMPLETE (24/24 PASS). Global vortex E=∞ (log divergence) → gauge field A_μ REQUIRED for finite E → δE/δA=0 gives Maxwell → e²=8/27 from moduli metric. 6-step chain F1-F6, steps F1-F5 T1, F6 T2a. Remaining gaps: G3 dynamical mechanism (Anderson-type, T3), G4 codimension 2+1D→3+1D (T3). See `equations/gauge_emergence_exploration.py`
- **U(n) → SU(n) FACTORING: derive why overall U(1) phase is redundant** — C529: U(n) isometry of S^{2n-1} is mathematical fact; factoring to SU(n) needs dynamical principle. Must show overall phase is D5 symmetry (already counted) via topological or conservation argument. See `educational/32_depth_bifurcation.md` §What Remains Open item 2
- **CHARGE INHERITANCE: prove D(n+1) modes transform under G_n** — C529: termination argument assumes D8 modes carry SU(3) charge. Need substrate derivation that deeper modes necessarily couple to shallower gauge structure. See `educational/32_depth_bifurcation.md` §What Remains Open item 6
- **Derive Y-junction penalty = −1** — critical blocker for baryon Regge, Δ-N splitting. C463: NG Casimir gives Δ=1/8 (12.5%). C539: quark-diquark massive-endpoint path RULED OUT (requires m_D=148 MeV, unphysically small; classical formula double-counts kink mass already in JR mode). Remaining paths: junction mode quantization, WKB, Y-junction BVP. See `equations/regge_intercept_derivation.py` Part J
- **Baryon asymmetry magnitude** — C546: DFC leptogenesis gives η_B = 1.1×10⁻⁷ (184× overshoot, T4). M_c(D7) as RH neutrino mass, Casimir spectrum M_2/M_1=9/4, maximal CP phase. Overshoot suggests M_1 too high or single-flavor approximation inadequate. See `equations/baryon_asymmetry_magnitude.py`
- **Dark matter relic abundance mechanism** — C554: gravitational freeze-in requires T_RH=3×10¹⁷ GeV (too high). KZ overproduces by 10⁷×. Need DFC-specific production or lower m_DM. d_DM=4.5 not derived. See `equations/dark_matter_relic_abundance.py`
- **Derive correlated 2π-exchange NN attraction from V(φ)** — C563: single OBE Yukawa with DFC g²/(4π)=7.4 is ~5× too weak for nuclear binding. Iterated OPE / box + crossed-box diagrams provide ~60% of nuclear attraction in Bonn models. DFC has pion dynamics (GMOR, g_piNN from GT) — can the 2π exchange effective coupling be derived from V(φ) chiral sector? This blocks ALL light nuclei predictions. See `equations/light_nuclei_binding.py` Part E

---

## Priority 4 — Known Failures

- **Nucleon magnetic moment ratio** — +2.75%. C509: ratio = −3/2 + g_A/32 matches to 0.022% (g_A = 4/π from DFC). Potential T2a upgrade if 1/32 coefficient derivable from NLO ChPT. Counterterm cancellation ~75% (upper edge of expected range). BLOCKED on deriving counterterm coefficient. See `equations/nucleon_magnetic_moments.py`
- **Nuclear surface diffuseness** — C547: Fock exchange correction reduces gap from +7% to +2.8% (86% of original 20% gap closed). Remaining +2.8% from higher-order terms (pionic fluctuations, RPA). See `equations/sigma_mass_in_medium.py` (15/16 PASS)
- **Lithium problem** — C555: ALL 6 DFC-specific mechanisms ruled out. DFC Li-7 shift +0.009% vs needed 66% reduction (factor 7247 short). DFC inherits lithium problem from standard BBN. No new physics at BBN scales. See `equations/bbn_predictions.py` Part H
- **Triple-alpha Q value / light nuclei binding** — C563: ROOT CAUSE REVISED. Not coupling asymmetry — OBE coupling strength itself too weak. g²/(4π)=7.4 gives V_net~few MeV at 1fm even with g_omega=0 and NJL sigma (226 MeV). No binding for any m_sigma [150-650 MeV]. Needs iterated OPE / correlated 2π exchange (~60% of nuclear attraction in Bonn models). See `equations/light_nuclei_binding.py` Part E

**Resolved (removed from P4):**
- ~~M_W = 79.67 GeV (−0.88%)~~ — RESOLVED C497: tree-level gap closed to +0.009% by standard one-loop Sirlin Δr corrections. See `equations/ew_radiative_corrections.py` (10/10 PASS, T2a)
- ~~Charm/strange quark mass residual~~ — RESOLVED C274: κ_q=πN_c/2 gives charm +0.29%, strange +2.09% (both T2a). See `equations/quark_mass_kappa_derivation.py`
- ~~Neutrino mass ratio m₃/m₂~~ — RESOLVED C204: color phase correction κ^(1+1/(6π)) = 5.8248 matches observed 5.8242 to +0.010% (T3, 0 free params). See `equations/neutrino_color_correction.py`

---

## Priority 5 — Exploratory

- **Literature reframing: SSH/polyacetylene → fermion zero modes** — map full SSH toolkit (fractional charge, topological protection indices, bulk-boundary) to DFC. Quark e/3 charge from domain wall fractionalization? See `foundations/literature_reframing.md` §B3
- **Literature reframing: Skyrme e_sk from V(φ)** — derive Skyrme stabilization coefficient from substrate self-interaction at D6. Independent proton mass route vs current Regge. See `foundations/literature_reframing.md` §B2
- **Literature reframing: graded elastic media → mode spectrum** — import transfer matrix, WKB, impedance matching methods from GRIN optics / metamaterials for kink fluctuation spectrum. See `foundations/literature_reframing.md` §C3
- **Literature reframing: CDT spectral dimension flow** — does DFC predict spectral dimension 4→2 at short distances (ω ~ 1/ξ)? If so, matches CDT quantum gravity result. See `foundations/literature_reframing.md` §D2
- **Literature reframing: Griffiths/FKG → substrate ordering** — Mermin-Wagner constraints on closure behaviors at each effective dimensionality. Kosterlitz-Thouless for topological ordering at D5. See `foundations/literature_reframing.md` §D4
- **Literature reframing: Witten TFT → substrate invariants** — Chern-Simons invariant in D7 SU(3) closure determines θ_QCD. Topological invariants classify closure types. See `foundations/literature_reframing.md` §D5
- **DFC predictions for LHC Run 4** — high visibility. What does DFC predict differently from SM? Any distinctive signatures?
- **CMB-S4 predictions** — timely. n_s refinement, r upper bound, N_eff precision from DFC
- **Freeform math exploration** — workspace: `equations/freeform_math_exploration.py`. Feed blocked items here. C471: F*C = 300π² (T1 identity). Always available
- **Investigate κ_q ≈ N_c·b₀/(2N_c+1) identity** — 0.03% match, coincidence or structural?
- **Investigate mu_p/mu_n = −3/2 + g_A/32** — 0.022% match. C509: 1/(8π) = g_A/32 since g_A = 4/π. Connects ratio to DFC axial coupling. Derive 1/32 coefficient from NLO ChPT? See `equations/nucleon_magnetic_moments.py` Part I
- **Investigate π+√N_c ≈ ln(1/α_em)** — −0.95% match. See E57
- **Investigate N_c·ln(2α)/2 ≈ α identity** — −5.2% match. See `equations/substrate_casimir_alpha.py`
- **Gravitational wave spectrum from D4** — spin-2 composite tensor mode propagation. Any GR deviation?
- **DFC implications for quantum computing** — qubit coherence limits from substrate structure
- **Neutron star max mass** — naive flux-tube failed (−77%). Connects to P1 Walecka
- **Condensed matter from V(φ)** — BCS gap, T_c predictions from existing modules
- **Evaluate new open problems for DFC** — Navier-Stokes, quantum gravity (proton spin DONE C477)
- **Proton spin puzzle — vector meson / 1/N_c corrections** — C498: e-scan shows I₀/I₁ saturates at ~0.186 for all e > 3. Pure ANW Skyrme gives Σ ≈ 0.23 regardless of e (systematic −28%). Next: include ρ/ω vector mesons (HLS) or compute 1/N_c corrections. See `equations/proton_spin_dfc.py`
- **Internal consistency web audit** — C501: PHASE 1 DONE. 7/7 core checks PASS. 35 stale BETA/g_eff values across 31 files found. Λ_QCD spread 124.6% (scheme differences). Phase 2: fix stale values, add cross-module derived-quantity checks. See `equations/consistency_web_audit.py`
- **Parameter sensitivity / fragility analysis** — perturb α=∛18, β=1/(9π), g_eff²=8/27 by ±0.1% and measure cascade of prediction errors. Distinguish robust from fragile predictions
- **Module migration to dfc_core (CONTINUOUS)** — migrate equation modules from local constant declarations to `from dfc_core import *`. 53 modules still use local ALPHA=18**(1/3). DONE: kink_kink_potential, gauge_emergence_exploration, alternative_potentials, helfrich_membrane_gravity
- **Independent derivation paths** — for key results (α_s, sin²θ_W, m_p), find completely different derivation routes within DFC
- **Rigorous free-parameter accounting** — count every observational input across all modules. True prediction-to-parameter ratio
- **Phase diagram & extreme regime predictions** — QCD deconfinement T_c, neutron star max mass, EW phase transition order
- **Prove y(v) = exp(-(b₀+1/α)) from kink overlap** — C510: d_eff = 7.9 kink widths. BOTTLENECK: derive D5-D7 depth separation. See `equations/light_quark_mass_derivation.py` Part K
- **Analog system comparison** — condensed matter systems with double-well kinks (polyacetylene, ferroelectrics). Do they show emergent gauge-like behaviors?

**Completed (removed from P5):**
- ~~Analog gravity dispersive corrections~~ — C564 DONE. See `equations/analog_gravity_dispersion.py`
- ~~Literature reframing: Helfrich membrane~~ — C534 DONE. See `equations/helfrich_membrane_gravity.py`
- ~~Literature reframing: AdS/CFT dictionary~~ — C517 DONE. See `equations/adscft_topo_insulator_dfc.py`
- ~~Literature reframing: topological insulator~~ — C517 DONE. See `equations/adscft_topo_insulator_dfc.py`
- ~~Literature reframing: BCS gap → Λ_QCD~~ — C548 DONE. See `equations/bcs_gap_lambda_qcd.py`
- ~~Literature reframing: quantum Hall → coupling~~ — C556 DONE. See `equations/quantum_hall_coupling_quantization.py`
- ~~Cosmological constant from RS2~~ — C511: 10^124× too large. Standard CC problem persists
- ~~AdS/CFT dual of DFC bulk~~ — C511: central charge c=19.4. Recorded, not actionable

---

## Priority 6 — Documentation

- **Update prediction scorecard** — `educational/06_predictions.md`. C557: added Δm NJL route (+17%, T2b), DM direct detection (10⁻¹¹⁴ cm², T3), DM production T_RH (T4), Li-7 6-mechanism ruling (T4), JR Chern number (T1). Remaining: quarkonium to hadron spectroscopy module
- **Create new educational modules** — continual check. Remaining:
  - **Born rule from V(φ) module** — full derivation chain V(φ)→Schrödinger→⟨ε⟩∝|ψ|²→rate∝|ψ|²
  - **Electroweak precision tests module** — collect M_W, M_Z, G_F, sin²θ_W, Γ_Z results
  - **Proton charge radius module** — C476 sign bug discovery + corrected prediction
- **Document audits (CONTINUOUS)** — pick 2-4 random docs, check for stale tiers/refs/language
- **ROADMAP review (CONTINUOUS)** — review all tiers for items to remove (resolved/not viable), consolidate (duplicates/same blocker), reorder (blocked items to bottom), and add (new follow-ups from recent work). Keep ROADMAP lean and actionable
- **Practical applications** — add entries to `practical_applications/`
- **Update open questions** — `educational/07_open_questions.md`. C485: updated recently

---

## Priority 7 — Critical Review

This tier exists to keep the project honest and adaptive. The goal is not to defend
DFC but to stress-test it — compare against existing theories, identify where standard
approaches do better, question foundational assumptions, and adapt the model when
evidence warrants it. Mathematical verifiability is the standard; attachment to any
particular concept is not.

- **Literature reframing: cohesion/conflict audit** — C524: Cluster A DONE. Remaining: Cluster B (gauge/topology), Cluster C (condensed matter), Cluster D (new connections). See `foundations/literature_reframing.md`
- **Set T4 stagnation deadlines** — C493: items stuck at T4 for 100+ cycles should be honestly flagged as likely unresolvable within current framework. Review α_em(0) identity, Casimir=α, D4 gravity overshoot
- **Adversarial prediction hunting** — deliberately search for quantities where DFC *must* disagree with observation. A model that can't be wrong can't be right
- **Rigorous free-parameter audit** — C566: 15 T2a predictions audited, 5/6 PASS. 4 DFC geometric params, Ratio 3.0 (generous). Key finding: g_eff²=8/27 is only truly 0-param result. See `equations/free_parameter_audit.py`. Follow-ups: (1) derive Δ(1/α)=9.136 from DFC to upgrade Tier 2b→2a, (2) fix mass_spectrum.py hidden 3rd param (dimple width=0.02), (3) fix lamb_shift.py F_higher self-calibration, (4) document M_Z embedded in coupling_derivation.py, (5) downgrade cosmology.py H₀ from "prediction" to "consistency check"

**Completed (removed from P7):**
- ~~Evaluate practical relevance~~ — C513 DONE. See `foundations/critical_review_predictions.md`
- ~~Explore alternative frameworks~~ — C536 DONE. See `equations/alternative_potentials.py`
- ~~Catalog what DFC cannot do~~ — C550 DONE. See `foundations/critical_review_blind_spots.md`
- ~~External literature comparison~~ — C558 DONE. See `foundations/critical_review_uniqueness.md`
- ~~Audit prediction quality~~ — C486 DONE. See `foundations/critical_review_predictions.md`
- ~~Identify unfalsifiable claims~~ — C493 DONE. See `foundations/critical_review_predictions.md`
- ~~Compare D-depth assignments~~ — C500 DONE. See `foundations/depth_assignment.md`
- ~~Review mathematical rigor~~ — C519 DONE. See `foundations/critical_review_rigor.md`

---

## Priority 8 — Simulations & Numerical Experiments

Build out the simulation library. Every simulation should produce a standalone runnable
module in `equations/` with [PASS]/[FAIL] checks, and integrate results into framework
docs (educational/, equations/README.md, current_state.md). Simulations are the primary
way to demonstrate that DFC dynamics *work* — that the claimed behaviors actually emerge
from V(φ) when you solve the field equation numerically.

**Queue (ordered by impact):**

- **Multi-kink gas dynamics** — start with 5-10 random kink-antikink pairs at various positions and velocities. Evolve and observe: annihilation events, scattering, thermalization, energy equipartition. Demonstrates how a "particle gas" emerges from pure field dynamics
- **Kink in slowly varying background** — place a kink in a gently curved potential well (spatially varying α(x)). Measure how the kink accelerates toward deeper wells. This is the D4 gravity mechanism in miniature: kinks respond to substrate compression gradients
- **Vortex-antivortex annihilation (2+1D)** — complex field analogue of kink-antikink. Demonstrates U(1) charge conservation and radiation spectrum in 2+1D
- **Kibble-Zurek: quench rate → kink density** — cool the system through the phase transition at different rates. Measure kink density vs quench rate. Connects to cosmological defect formation
- **Kink with excited shape mode** — boost the internal PT shape mode of a kink before collision. Measure how internal excitation affects scattering outcome (resonance window shifts)
- **Kink-kink repulsion dynamics** — two same-sign kinks repel. Measure the repulsive force, compare to Manton prediction. Topological exclusion = "Pauli repulsion" for identical kinks
- **Compression-driven bifurcation** — simulate a substrate under slow uniform compression (time-dependent α(t)). Watch for spontaneous symmetry breaking, kink formation, and depth-like cascade behavior

**Completed simulations:**
- substrate_simulation.py — spontaneous kink formation from tachyonic instability (C540)
- complex_field_u1_simulation.py — 2+1D vortex formation, charge quantization
- kink_kink_potential.py — kink-antikink interaction: Yukawa V_int ∝ exp(−m_σ d) (C528)
- kink_antikink_annihilation.py — collision dynamics, resonance windows, mass gap radiation (C542)
- gauge_emergence_exploration.py — gauge field necessity from energetic argument (C531)
- poschl_teller_spectrum.py — PT s=2 spectrum: 2 bound states, shape mode 0.0005%, mass gap, eigenfunctions (C543)
- oscillon_breather_formation.py — oscillon from bubble collapse: omega=0.75*m_sigma, Q=4313, lifetime 1373 periods, sech profile (C551)
- tachyonic_complexification_sim.py — real kink → complex vortex: γ=√(α/2) confirmed 2.9%, 10381× amplification, Δθ=π, U(1) emergence demonstrated (C559)

**Integration rule:** After each new simulation, update:
1. `equations/README.md` — add to simulation table
2. `educational/` — create or update relevant module
3. `current_state.md` — note new findings
4. This list — move item to Completed

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
| 9 | Gravity (D4) | T1 | d4_coupled_kink_warp, d4_thick_wall_bvp, gravity_cross_applications + 15 more | Thin-wall κ=0.497 (−0.57% T1); thick-wall κ=2.04 (4.1× overshoot); cross-spoke connections mapped C511 | C511 |
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
| **D4 thick-wall factor-4 gap** | T3 — κ_thick=2.04 vs target 0.5 (C508) | G_N derivation; gravitational predictions; Planck scale |

---

## Pending Propagation

Results that have landed but need to be propagated to documentation, scorecards,
or other tracking. Each P6 cycle should pick one item from this queue. Check off
items when done; remove checked items after 2 cycles.

- [ ] C482: Bell chain T2a → update `educational/19_bell_inequalities.md`
- [ ] C484: proton spin Σ → update `educational/31_proton_spin_puzzle.md`
- [ ] Stellar census module → add to prediction scorecard
- [ ] C508: thick-wall κ=2.04 → update `educational/28_gravity_gap.md`
- [ ] C564: analog gravity dispersion → add to prediction scorecard (exponential onset prediction)
- [ ] C566: free parameter audit → update `foundations/critical_review_predictions.md` with ratio findings
