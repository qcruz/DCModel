# DFC Model — Development Roadmap

**The single source of truth for what to do next.**

**Last updated:** Cycle 592 (2026-09-12)

---

## How This Document Works

- **This is a living roadmap and todo list.** Add items as they come up. Remove items when done.
- **Task selection:** Cycle through tiers in order (P1→P2→P3→P4→P5→P6→P7→P8→P1→...). Check the `Last tier worked:` marker below to determine the next tier. **Within each tier, always work the FIRST bullet point.** After working an item, move it to the BOTTOM of that tier's list. This ensures systematic coverage. If a tier has no actionable items, spend the cycle researching and adding new items to that tier. Update the marker after each cycle.
- **Item ordering:** Items within each tier are ordered by impact × tractability. UNBLOCKED items go to the top; BLOCKED/STUCK items go to the bottom. When new progress unblocks an item, move it up accordingly.
- **P5 = Exploratory, P6 = Documentation, P7 = Critical Review, P8 = Simulations.** P7 exists to prevent the project from becoming locked into assumptions. P8 builds numerical demonstrations that DFC dynamics actually produce the claimed behaviors from V(φ).
- **Last tier worked: P7** (C592 — parameter_provenance.md NEW: full input provenance for all 24 predictions, pre/post-diction audit, honest parameter counting)
- **Never skip items because they are hard.** Always attempt incremental progress. Ruling out wrong approaches, documenting blockers, and outlining next steps are all valid progress.
- **Keep items short.** Detailed notes belong in equation modules, `ISSUES.md`, or `push_history.md` — not here.
- **Spoke Dashboard:** Updated when a spoke's best tier, key gap, or last-touched cycle changes. Spokes not touched in 50+ cycles deserve priority attention during tier rotation.
- **Critical Blockers:** Updated when a blocker is resolved or a new multi-item blocker is discovered. When a blocker clears, promote newly-unblocked items upward in their tiers.
- **Pending Propagation:** Each P6 cycle picks one item from this queue. New results that need doc updates get added here immediately. Checked-off items are removed after 2 cycles.

---

## Model Completeness — Score-Moving Items

These 4 items have the highest leverage for improving overall model completeness scores
(viability ~87%, rigor ~73%, overall ~80%). They are prioritized at the top of their
respective tiers and tracked here as a collective goal.

| # | Item | Tier | Expected impact | Status |
|---|---|---|---|---|
| MC1 | Derive M₅³ from (α,β) → κ = 0.50 | P3 | +2% viability, +3% rigor | PROGRESS — κ=0.5107 (+2.14%) DEFINITIVE. C589: Lichnerowicz exact zero-mode proves gap irreducible at DFGH level. 90% excess within 2ξ. T2a prediction |
| MC2 | Close α_em(0) gap T4→T2a | P2 | +1% viability, +3% rigor | PROGRESS — shape mode closes 106.6%, 6.6% overshoot (C579) |
| MC3 | New T2a prediction (e.g. muon g−2) | P1 | +1% viability, +1% rigor | BLOCKED on MC2; gap-closed→1.1σ (C578) |
| MC4 | Derive nuclear binding from V(φ) | P1/P3 | +2% viability, +2% rigor | PROGRESS — C586: NLO TPE gives 33% of needed attraction. Needs N2LO or Brueckner |

**Target:** closing all 4 would move scores to ~93% viability, ~82% rigor, ~87% overall.

---

## Priority 1 — High-Impact Predictions

- **Derive pion mass from GMOR** — C537: NJL-LIMITED. m_pi = 136.9 MeV (−1.9%, T2a with lattice condensate). Pure DFC = 86 MeV (−38%, T3). BLOCKED: needs beyond-NJL condensate. See `equations/pion_mass_gmor.py`
- **Derive light quark masses (D6 Yukawa)** — C544: DOWNGRADED T2a→T2b (+24% at 2-loop). Formula structurally interesting (0 free params) but prediction is order-dependent. See `equations/light_quark_mass_derivation.py`
- **Derive proton-neutron mass difference from DFC** — C552: NJL route +17% (T2b). BLOCKED: vertex corrections needed to reduce C_QCD from 0.87 to ~0.50. See `equations/proton_neutron_mass_difference.py`
- **Beyond-mean-field Walecka EOS** — C560: C₂(NJL)/C₂(NL3) = 0.87. Remaining: NJL sigma mass (226 MeV) vs physical (500-648 MeV). See `equations/nuclear_kink_nonlinear_eos.py` Part G
- **Muon anomalous magnetic moment (g−2)_μ** [MC3] — BLOCKED on α_em gap. C578: gap-closed scenario shows DFC+lattice→1.1σ; bottleneck shifts to hadronic VP (data vs lattice = 10σ). DFC ρ spectral function could resolve controversy. Updated to Fermilab 2023 final (22×10⁻¹¹ unc). See `equations/anomalous_magnetic_moment.py` Part G
- **Derive V(phi) contact terms for deuteron binding** [MC4] — C586: NLO TPE (Kaiser-Brockmann-Weise effective Yukawa) gives OPE+TPE = -11.5 MeV at 1fm, 33% of needed ~-35 MeV. Chiral expansion converges slowly for NN. Next: N2LO 3π or Brueckner G-matrix with DFC bare couplings. See `equations/light_nuclei_binding.py` Part F

**Resolved (removed from P1):**
- ~~W mass~~ — RESOLVED C497: M_W = 80.38 GeV (+0.009%, T2a). See `equations/ew_radiative_corrections.py`
- ~~Top quark mass from Koide~~ — NOT VIABLE C494: K=2/3 fails for all quark triplets. See `equations/top_quark_koide.py`

---

## Priority 2 — Tier Upgrades

- **Upgrade cosmological Λ to T2a** — STUCK. CMB ℓ₁ (+0.89%) and BAO r_drag (−0.27%) already T2a. Only Λ_cosm remains T3 — bottleneck is Casimir=α combination rule (16 mechanisms tested, 7 ruled out). See `equations/cosmological_predictions.py`, `equations/substrate_casimir_alpha.py`
- **Upgrade nuclear symmetry energy J to T2a** — C490: +9.2% T3. Path: self-consistent m* from DFC Walecka + Fock integral with DFC g_ρ. See `equations/nuclear_symmetry_energy.py`
- **Close f_pi 1.6% gap** — C521: M(p) ruled out. Gap traces to m_rho undershoot. BLOCKED on m_rho/σ correction. See `equations/fpi_gap_closure.py`
- **Upgrade proton charge radius to T2a** — C545: VMD-regulated pion cloud (m_ρ cutoff) gives r_p = 0.809 fm (−3.8%, T2a). DFC-only with SU(6) κ_p=2 and VMD pion cloud, 0 free params. Remaining: derive κ_p from DFC magnetic moments (currently SU(6) approximation). See `equations/proton_charge_radius_dfc.py`
- **Upgrade Delta-N splitting to T2b** — C561: FORMALLY T3, NUMERICALLY T2b (−7.4%). C587: PARTIALLY UNBLOCKED — junction penalty now derived (Part K of regge_intercept_derivation.py). Mass ratio m_Δ/m_N = √(5/3) = −1.68%. Remaining: derive Y-junction penalty Δ=−7/4 for delta_n_splitting.py specifically (uses different parametrization than regge_intercept). See `equations/delta_n_splitting.py`
- **Derive hadronic VP δ(Δα)^NP = 0.00102** — C520: REFRAMED. Gap is from 36π formula, not VP. DFC VP overshoots data +27%. See `equations/hadronic_vp_dfc.py`
- **Prove alpha_em(0) identity A−B = ln(1/α_em(0))** [MC2] — C579: ONE-LOOP SHAPE MODE closes 106.6% of gap (overshoot 6.6%). Formula: δ(1/α_em) = −36π × C₂(SU2) × g_eff²/(16π²) × ln(√2) = −0.147 vs needed −0.138. Zero free params. T4→T3 upgrade candidate. NEXT: verify 1/(16π²) normalization from explicit kink fluctuation determinant. See `equations/alpha_em_gap_exploration.py` Part G
- **Upgrade baryon Regge intercept to T2a** — C587: UNBLOCKED. Part K derives junction penalty Δ=s_JR=1/2 from Y-junction force balance freezing 1 DOF. Formula: α₀(baryon,S)=S/Q_top−1/2. N=−1/4 ✓, Δ=+1/4 ✓. T3→T2a candidate. Weakest link: frozen DOF↔s_JR identification (structural). See `equations/regge_intercept_derivation.py` Part K

---

## Priority 3 — Structural Gaps

- **Derive correlated 2π-exchange NN attraction from V(φ)** [MC4] — C563: single OBE Yukawa with DFC g²/(4π)=7.4 is ~5× too weak for nuclear binding. Iterated OPE / box + crossed-box diagrams provide ~60% of nuclear attraction in Bonn models. DFC has pion dynamics (GMOR, g_piNN from GT) — can the 2π exchange effective coupling be derived from V(φ) chiral sector? This blocks ALL light nuclei predictions. See `equations/light_nuclei_binding.py` Part E
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
- **Derive CKM/PMNS from D6/D7 overlap** — C522: diagonal Z₃ FAILS for θ₁₂ (F(1)=F(2), T1 proof). Must be off-diagonal. Best: sin(θ_C)=1/π (+43%). GST sin=√(m_d/m_s) works at −0.6% — path is through DFC quark mass ratio. BLOCKED: need formal off-diagonal BVP. **ESCALATED C584:** 170 cycles at T4, most important stalled item — blocks CP phase for baryon asymmetry and full flavor sector. See `equations/ckm_from_d6d7_overlap.py`
- **Upgrade Lorentz emergence to T1 via analog gravity theorem** — Barcelo et al. (2001): non-dispersive medium => exact Lorentz invariance at low energy. DFC substrate is non-dispersive in vacuum (V''(phi_0)=const). Citation upgrades T3 -> T1. See `foundations/gravity_theory_integration.md`
- **Derive Hawking temperature from V(phi)** — analog gravity gives T_H from surface gravity of effective metric horizon. Substrate profile determines all ingredients. See `foundations/gravity_theory_integration.md`
- **Derive open→closed mode transition from coupled PDE** — C526: structural argument in place (T2a). Need formal derivation showing kink formation creates bound states for subsequent fluctuations. See `equations/depth_bifurcation_dynamics.py` Part A
- **Derive WHY SU(2) is broken but SU(3) is not from V(φ)** — C526: structural argument (EWSB vs confinement, T2a). Need to derive from substrate dynamics that D6 sector acquires VEV while D7 does not. See `equations/depth_bifurcation_dynamics.py` Part D
- **Derive threshold positions α₅, α₆, α₇** — C526: currently T4. Compute compression budget per bifurcation from V(φ). See `equations/depth_bifurcation_dynamics.py` Part F
- **GAUGE EMERGENCE: zero-mode degeneracy → local gauge symmetry** — C531: ENERGETIC ARGUMENT COMPLETE (24/24 PASS). Global vortex E=∞ (log divergence) → gauge field A_μ REQUIRED for finite E → δE/δA=0 gives Maxwell → e²=8/27 from moduli metric. 6-step chain F1-F6, steps F1-F5 T1, F6 T2a. Remaining gaps: G3 dynamical mechanism (Anderson-type, T3), G4 codimension 2+1D→3+1D (T3). See `equations/gauge_emergence_exploration.py`
- **U(n) → SU(n) FACTORING: derive why overall U(1) phase is redundant** — C529: U(n) isometry of S^{2n-1} is mathematical fact; factoring to SU(n) needs dynamical principle. Must show overall phase is D5 symmetry (already counted) via topological or conservation argument. See `educational/32_depth_bifurcation.md` §What Remains Open item 2
- **CHARGE INHERITANCE: prove D(n+1) modes transform under G_n** — C529: termination argument assumes D8 modes carry SU(3) charge. Need substrate derivation that deeper modes necessarily couple to shallower gauge structure. See `educational/32_depth_bifurcation.md` §What Remains Open item 6
- **Derive Y-junction penalty** — C587: RESOLVED. Part K derives Δ=s_JR=1/2 (in S/Q_top parametrization) from Y-junction force balance freezing 1 DOF. Formula: α₀(baryon,S)=S/Q_top−1/2. N=−1/4 ✓, Δ=+1/4 ✓. T3→T2a candidate. See `equations/regge_intercept_derivation.py` Part K
- **Baryon asymmetry magnitude** — C546: DFC leptogenesis gives η_B = 1.1×10⁻⁷ (184× overshoot, T4). M_c(D7) as RH neutrino mass, Casimir spectrum M_2/M_1=9/4, maximal CP phase. Overshoot suggests M_1 too high or single-flavor approximation inadequate. See `equations/baryon_asymmetry_magnitude.py`
- **Dark matter relic abundance mechanism** — C554: gravitational freeze-in requires T_RH=3×10¹⁷ GeV (too high). KZ overproduces by 10⁷×. Need DFC-specific production or lower m_DM. d_DM=4.5 not derived. See `equations/dark_matter_relic_abundance.py`
- **D4 gravity gap — close remaining 2.1%** [MC1] — C588: One-loop corrections too small (0.2-0.5%, wrong sign). Gap is CLASSICAL thick-wall effect: ∫e^{2.06A} closes to +0.24%. Path: Lichnerowicz equation on kink background. See `equations/kink_self_gravity.py` Part J

---

## Priority 4 — Known Failures

- **Lithium problem** — C555: ALL 6 DFC-specific mechanisms ruled out. DFC Li-7 shift +0.009% vs needed 66% reduction (factor 7247 short). DFC inherits lithium problem from standard BBN. No new physics at BBN scales. See `equations/bbn_predictions.py` Part H
- **Triple-alpha Q value / light nuclei binding** — C563: ROOT CAUSE REVISED. Not coupling asymmetry — OBE coupling strength itself too weak. g²/(4π)=7.4 gives V_net~few MeV at 1fm even with g_omega=0 and NJL sigma (226 MeV). No binding for any m_sigma [150-650 MeV]. Needs iterated OPE / correlated 2π exchange (~60% of nuclear attraction in Bonn models). See `equations/light_nuclei_binding.py` Part E
- **Nucleon magnetic moment ratio** — +2.75%. C571: NLO ChPT + Δ-pole RULED OUT for g_A/32 derivation (Δ gives 0.5% of κS, C_ct=124% unphysical). The ratio correction is driven by κS=−0.060 (sea quarks/orbital AM), not perturbative ChPT. Algebraic match −3/2+g_A/32 holds at 0.022% but derivation requires Skyrme-type sea computation. See `equations/nucleon_magnetic_moments.py` Part J
- **Nuclear surface diffuseness** — C581: pionic RPA (−2.2%) + tensor correlations (−1.0%) close remaining +2.8% → −0.5% (97% of original 20% gap closed). Pionic/tensor magnitudes from DFT systematics scaled by DFC f_π ratio (T2b). HF-only remains T2a (+2.8%). See `equations/sigma_mass_in_medium.py` (19/20 PASS)

**Resolved (removed from P4):**
- ~~M_W = 79.67 GeV (−0.88%)~~ — RESOLVED C497: tree-level gap closed to +0.009% by standard one-loop Sirlin Δr corrections. See `equations/ew_radiative_corrections.py` (10/10 PASS, T2a)
- ~~Charm/strange quark mass residual~~ — RESOLVED C274: κ_q=πN_c/2 gives charm +0.29%, strange +2.09% (both T2a). See `equations/quark_mass_kappa_derivation.py`
- ~~Neutrino mass ratio m₃/m₂~~ — RESOLVED C204: color phase correction κ^(1+1/(6π)) = 5.8248 matches observed 5.8242 to +0.010% (T3, 0 free params). See `equations/neutrino_color_correction.py`

---

## Priority 5 — Exploratory

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
- **Skyrme e_sk from V(φ)** — C582: e=1/√β=√(9π)=5.317 (−2.4% from ANW 5.45). Also e=m_σ/f_π=3π/2=4.71 (−13.5%). Both in lit range [4,6.5]. Skyrme M_N problem inherited (3-7× too high); DFC uses Regge for M_N. T3. NEXT: formal dimensional reduction β → e_sk. See `equations/skyrme_e_from_vphi.py`

**Completed (removed from P5):**
- ~~Analog gravity dispersive corrections~~ — C564 DONE. See `equations/analog_gravity_dispersion.py`
- ~~Literature reframing: Helfrich membrane~~ — C534 DONE. See `equations/helfrich_membrane_gravity.py`
- ~~Literature reframing: AdS/CFT dictionary~~ — C517 DONE. See `equations/adscft_topo_insulator_dfc.py`
- ~~Literature reframing: topological insulator~~ — C517 DONE. See `equations/adscft_topo_insulator_dfc.py`
- ~~Literature reframing: BCS gap → Λ_QCD~~ — C548 DONE. See `equations/bcs_gap_lambda_qcd.py`
- ~~Literature reframing: quantum Hall → coupling~~ — C556 DONE. See `equations/quantum_hall_coupling_quantization.py`
- ~~Literature reframing: SSH/polyacetylene → fermion zero modes~~ — C572 DONE. SSH gives 1/2 not 1/3; quark charges from Z₃ center vortex. See `equations/ssh_fractional_charge.py`
- ~~Cosmological constant from RS2~~ — C511: 10^124× too large. Standard CC problem persists
- ~~AdS/CFT dual of DFC bulk~~ — C511: central charge c=19.4. Recorded, not actionable

---

## Priority 6 — Documentation

- **Create new educational modules** — continual check. Remaining:
  - **Born rule from V(φ) module** — full derivation chain V(φ)→Schrödinger→⟨ε⟩∝|ψ|²→rate∝|ψ|²
  - ~~Electroweak precision tests module~~ — DONE C583. See `educational/34_electroweak_precision.md`
  - **Proton charge radius module** — C476 sign bug discovery + corrected prediction
- **Document audits (CONTINUOUS)** — pick 2-4 random docs, check for stale tiers/refs/language
- **ROADMAP review (CONTINUOUS)** — review all tiers for items to remove (resolved/not viable), consolidate (duplicates/same blocker), reorder (blocked items to bottom), and add (new follow-ups from recent work). Keep ROADMAP lean and actionable
- **Practical applications** — add entries to `practical_applications/`
- **Update open questions** — `educational/07_open_questions.md`. C485: updated recently
- **Update prediction scorecard** — `educational/06_predictions.md`. C573: added U(1) emergence (T1), analog gravity reflectionless (T1), C₂=N_c=3 (T3), graviton κ=1.29, Koide T1+structural upgrade, 6 new summary entries

---

## Priority 7 — Critical Review

This tier exists to keep the project honest and adaptive. The goal is not to defend
DFC but to stress-test it — compare against existing theories, identify where standard
approaches do better, question foundational assumptions, and adapt the model when
evidence warrants it. Mathematical verifiability is the standard; attachment to any
particular concept is not.

- **Adversarial prediction hunting** — deliberately search for quantities where DFC *must* disagree with observation. A model that can't be wrong can't be right
- **Literature reframing: cohesion/conflict audit Clusters C+D** — C524: Cluster A DONE. C574: Cluster B DONE. Remaining: Cluster C (condensed matter: BCS/NJL, Helfrich, graded elastic), Cluster D (new connections: topo insulator, CDT, QHE, Griffiths, Witten TFT). See `foundations/literature_reframing.md`
- **Rigorous free-parameter audit** — C566: 15 T2a predictions audited, 5/6 PASS. 4 DFC geometric params, Ratio 3.0 (generous). Key finding: g_eff²=8/27 is only truly 0-param result. See `equations/free_parameter_audit.py`. Follow-ups: (1) derive Δ(1/α)=9.136 from DFC to upgrade Tier 2b→2a, (2) fix mass_spectrum.py hidden 3rd param (dimple width=0.02), (3) fix lamb_shift.py F_higher self-calibration, (4) document M_Z embedded in coupling_derivation.py, (5) downgrade cosmology.py H₀ from "prediction" to "consistency check"
- **T4 stagnation deadlines (CONTINUOUS)** — C584: 10 items audited. 3 flagged STALLED (top mass 125 cyc, ℏ 203 cyc, thresholds 58 cyc). 4 PROGRESSING (η_B, DM, hadronic VP, Walecka). CKM/PMNS escalated to P3 (170 cyc, most important stalled item). See `foundations/t4_stagnation_audit.md`. Re-audit every 50 cycles

**Completed (removed from P7):**
- ~~Evaluate practical relevance~~ — C513 DONE. See `foundations/critical_review_predictions.md`
- ~~Explore alternative frameworks~~ — C536 DONE. See `equations/alternative_potentials.py`
- ~~Catalog what DFC cannot do~~ — C550 DONE. See `foundations/critical_review_blind_spots.md`
- ~~External literature comparison~~ — C558 DONE. See `foundations/critical_review_uniqueness.md`
- ~~Audit prediction quality~~ — C486 DONE. See `foundations/critical_review_predictions.md`
- ~~Identify unfalsifiable claims~~ — C493 DONE. See `foundations/critical_review_predictions.md`
- ~~Compare D-depth assignments~~ — C500 DONE. See `foundations/depth_assignment.md`
- ~~Parameter provenance audit~~ — C592 DONE. Full input tracing for 24 predictions: 2 genuinely 0-param, 6 pre-dictions, 10 post-dictions, 4 fitted. See `foundations/parameter_provenance.md`
- ~~Review mathematical rigor~~ — C519 DONE. See `foundations/critical_review_rigor.md`
- ~~Literature reframing: cohesion/conflict audit Cluster B~~ — C574 DONE. B1 KK (4/2/1), B2 Skyrme (6/1/1), B3 JR (8/0/1). JR strongest framework. See `foundations/literature_reframing.md`

---

## Priority 8 — Simulations & Numerical Experiments

Build out the simulation library. Every simulation should produce a standalone runnable
module in `equations/` with [PASS]/[FAIL] checks, and integrate results into framework
docs (educational/, equations/README.md, current_state.md). Simulations are the primary
way to demonstrate that DFC dynamics *work* — that the claimed behaviors actually emerge
from V(φ) when you solve the field equation numerically.

**Queue (ordered by impact):**

- **Kibble-Zurek: quench rate → kink density** — C590 DONE. σ=0.290 (+16% vs KZ 0.250), universal, Q=0 exact. See `equations/kibble_zurek_kink_density.py`
- **Kink with excited shape mode** — boost the internal PT shape mode of a kink before collision. Measure how internal excitation affects scattering outcome (resonance window shifts)
- **Kink-kink repulsion dynamics** — C591 DONE. Z_2 topological exclusion: Q=+2 impossible, E(Q=2)>>2E_kink. Yukawa m_eff/m_sigma=0.9954 (0.5%). KA resonance windows confirmed. See `equations/kink_kink_repulsion.py`
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
- multi_kink_gas_dynamics.py — 4 KA pairs, 4 annihilate, Q=0 exact, virial 1.25, pair creation from radiation, 9/9 PASS (C567)
- kink_gravity_gradient.py — kink in α(x) gradient: a=-(3/(2α))dα/dx matches to 0.6%, a∝ε to 1.1%, C_grav=1.49, 10/10 PASS (C575)
- vortex_antivortex_annihilation.py — 2+1D V+AV annihilation: Q=0 exact, ω_peak=1.12m_σ, cores annihilate, 11/11 PASS (C585)
- graviton_lichnerowicz_thick_wall.py — S7: graviton zero-mode on DFGH thick-wall: ψ₀=e^{3A/2} EXACT, κ=0.5107 (+2.14%) irreducible, volcano potential, 12/12 PASS (C589)
- kibble_zurek_kink_density.py — S1: KZ scaling σ=0.290 (+16% vs 0.250), Q=0 exact, universal across (α,β), spacing/ξ_hat~10 (O(1)), 15/15 PASS (C590)
- kink_kink_repulsion.py — S4: Z_2 topological exclusion (Pauli analogue), Yukawa m_eff/m_sigma=0.9954, KA resonance windows, K-AK-K annihilation, 13/13 PASS (C591)

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
| 1 | Coupling constants | T2a | alpha_em_prediction, alpha_em_selfconsistency, alpha_s_pure_dfc, d5_complex_from_instability | α_em(0) identity T3 (shape mode 1-loop, 6.6% overshoot); Casimir=α T3 | C579 |
| 2 | Electroweak | T2a | muon_lifetime, weinberg_angle_rg, z_boson_decays, ew_radiative_corrections, ewsb_cocrystallization, higgs_potential | Muon g−2 hadronic T4; ~~M_W~~ resolved +0.009% | C497 |
| 3 | Hadron spectroscopy | T2a | meson_regge_spectrum, baryon_mass_dfc, quarkonium_spectrum, pion_mass_gmor, rho_meson_dfc | Y-junction Δ=−1 T3; hadronic VP T4; quarkonium α_s T3 | C489 |
| 4 | Nuclear physics | T3 | nuclear_symmetry_energy, nuclear_saturation_dfc, nuclear_dfc_periodic_table, deuteron_tensor_ope, nuclear_kink_nonlinear_eos | Deuteron B_d −48% T4; Walecka g₂ 14× weak T4; NJL gap eq. | C490 |
| 5 | Cosmology | T2a | cosmological_predictions, cosmological_predictions_2, cosmological_predictions_3, bbn_predictions, cosmology | Λ combination rule T3; η_B magnitude T4; DM relic T4 | C414 |
| 6 | Bell / QM foundations | T2a | bell_joint_derivation, born_rule_derivation, born_rule_schrodinger, collapse_mechanism | Measurement dynamics T3; joint Born rule T3; emergent locality T3 | C482 |
| 7 | Neutrino physics | T3 | neutrino_masses, neutrino_theta23_z3_mechanism, neutrino_casimir_depth | θ₂₃ = 49.54° (+0.35σ, T3); m₃/m₂ −8.3% T3; absolute mass scale T4 | C496 |
| 8 | Atomic physics | T2a | atomic_structure, atomic_physics_predictions, lamb_shift, fine_structure | Lamb shift T2a (−0.69%); remaining atomic predictions inherit α_em(0) offset | C495 |
| 9 | Gravity (D4) | T2a | d4_coupled_kink_warp, d4_thick_wall_bvp, kink_self_gravity, kink_gravity_gradient + 15 more | Complete chain V(φ)→G_N; κ=0.511 (+2.1%, C580); remaining: close 2.1% gap | C580 |
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
| **α_em gap (+0.14)** — 36π overshoot | T3 (C579: shape mode 1-loop closes 106.6%, overshoot 6.6%; 0 free params) | α_em(0) identity; muon g−2; all atomic physics T2b→T2a |
| **D6/D7 overlap integral** (kink-vortex BVP) | T4 — θ₂₃ resolved without BVP (C496); still needed for CKM | CKM/PMNS; baryon asymmetry magnitude |
| **Y-junction penalty Δ = −1** | T3 — Casimir gives 12.5% | Baryon Regge intercept T2a; Δ-N splitting T2b |
| **NJL gap equation** with DFC condensate | T4 — composite σ dynamics | Walecka EOS; nuclear saturation; pion mass (pure DFC); μ_p/μ_n sea quarks |
| **2-loop α_s running** | T3 — 1-loop implemented | Quarkonium absolute masses; charmonium M(1S) +22% gap |
| **D4 thick-wall 2.1% gap** | T2a — κ=0.511 (+2.1%, C580; was +158% C576) | G_N derivation; gravitational predictions; Planck scale |

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
- [ ] C580: D4 gravity κ=0.511 (+2.1%) → update `educational/28_gravity_gap.md`, `educational/33_kink_self_gravity.md`, prediction scorecard
