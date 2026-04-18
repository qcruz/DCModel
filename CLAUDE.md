# DFC Model — Claude Instructions

This project is a theoretical physics model called **Dimensional Folding Compression (DFC)**.
It proposes that all known physics emerges from one self-compressing object: a continuous
field that pulls inward on itself, driving toward a near-1D state through compression and
bifurcation, whose self-closing bifurcation events form the topological structures we observe
as particles and forces. There are no pre-existing spatial dimensions, gauge groups, or
separate forces. What appears as "3D space," "gauge structure," or "three distinct forces"
is the downstream appearance of the substrate's fold topology at different compression depths.
The substrate is the only thing that exists. Forces are not fragments of a broken symmetry —
they are the interaction behaviors between different fold topologies of this one object.
This is a deeper unity than gauge unification: the forces were never three separate things
at any energy; they were always fold interactions of the same object, appearing topologically
distinct because they closed at different compression thresholds.

---

## Model Architecture

The substrate is one continuous object. The D-labels below are **working markers** for
depth behaviors observed on that object — not discrete layers, not separate spaces, and
not fixed ontological boundaries. The substrate at any depth can curl, twist, wrap back,
inherit properties from adjacent depths, or produce closure configurations not yet identified.

The current working map (provisional — depth assignments under exploration):

| Depth marker | Current working hypothesis | Apparent physics |
|---|---|---|
| D1 | Maximum compression — undifferentiated | Precursor state |
| D2 | First propagation behavior emerges | Wave modes, massless excitations |
| D3 | Localization behavior emerges | Apparent position, particle identity |
| D4 | Inertia behavior emerges | Apparent mass, resistance to change |
| D5 | U(1)-type closure behavior | Hypercharge / electromagnetism |
| D6 | SU(2)-type closure behavior | Weak force, spin-1/2 |
| D7 | SU(3)-type closure behavior | Strong force, color |

**Critical:** The D5=U(1), D6=SU(2), D7=SU(3) assignments are correspondences under
active exploration, not established derivations. The substrate may produce these behaviors
through winding, wrapping, or curling configurations that overlap depth ranges. Discovering
which configuration actually reproduces the observed values — while obeying the core
mechanics of compression — is a primary research goal.

Key field equation: `V(φ) = −α/2 φ² + β/4 φ⁴`, kink solutions φ₀ = ±√(α/β).

---

## Language Rules

These rules are non-negotiable. Enforce them in all documentation.

**Forbidden phrases and their replacements:**

| Forbidden | Replacement |
|---|---|
| "preferred orientation" | "intrinsic orientation" or "orientation defined by the substrate configuration" |
| "forces X into existence" | "produces X" or "X exists as a consequence of" |
| "forces/allows A to B" | "A exists — the structure in which B occurs" |
| "preferred point/direction" | "geometrically distinguished point/direction" (or remove entirely) |
| "energetically preferred" | "energetically stable" |
| "the model prefers / chooses" | passive voice or "the structure produces" |
| Any anthropomorphic agency | Remove or rephrase as structural consequence |
| "spatial dimensions" (as fundamental) | "apparent spatial degrees of freedom" or "the substrate's localization behavior" |
| "3D space" / "3+1 dimensional spacetime" (as container) | "three apparent spatial degrees of freedom" or "the D3 localization behavior of the substrate" |
| "reconcile with spatial dimensions" | never reconcile — the spatial appearance IS substrate behavior |
| "the D6 layer" / "the D7 sector" (as separate objects) | "D6 depth behavior" / "the substrate at D7 depths" |
| "requires 3 spatial dimensions" | "produces three apparent spatial degrees of freedom" or "the rotation behavior emerging at D3 has [property]" |

**Three foundational rules:**

1. **No spatial dimensions as fundamental.** The substrate is one object. Space is not a
   container the substrate lives in. What appears as three spatial degrees of freedom is
   downstream behavior of the substrate's D3 localization. Never write as if space is
   primary and the substrate secondary.

2. **D-labels are provisional depth markers, not discrete layers.** The substrate can wrap,
   curl, and interact with itself across depths. D5/D6/D7 are working hypotheses about where
   certain closure behaviors emerge. Writing "the D6 SU(2) layer" as if it is a separate
   sealed space is wrong. Write "the D6 depth behavior" or "the substrate's SU(2) closure
   at D6 depths."

3. **Forces are fold interactions of one object — never three separate things.**
   The three forces (U(1), SU(2), SU(3)) are not fragments of a broken gauge symmetry.
   They are interaction behaviors between different closure topologies of the same substrate.
   Writing as if forces "were once unified and then separated" imports the GUT narrative,
   which is wrong here. The correct framing: the forces were never separate — they are
   always the same fold interactions, appearing topologically distinct because they closed
   at different compression thresholds. "Unified" is permitted and correct when it refers
   to the ontological unity of the substrate (one object). It is forbidden when it implies
   gauge-group unification (three forces becoming one force at high energy).

**Language table additions:**
| Forbidden | Replacement |
|---|---|
| "the forces were unified at high energy" | "the forces are always fold interactions of one object; at high compression, their topological distinctions diminish" |
| "the model has no force unification" | "the model has deeper unity than gauge unification: one object, not three forces that once merged" |
| "unified force" (GUT sense) | "single substrate" or "one object" |
| "the three forces" (as fundamentally separate) | "the three closure-topology interaction regimes" or "fold interactions at D5, D6, D7 depths" |

**Reason:** All three errors embed an incorrect ontology — they make the substrate's downstream
behaviors (space, separate forces, discrete layers) appear to be primary, hiding the real
explanatory structure.

---

## Mathematical Communication Standard

This rule applies to all conceptual documents (`foundations/`, `phenomena/`). It does **not**
apply to equation modules (`equations/`) or formal equation display blocks within docs, where
symbolic notation is necessary for computation and precision.

**Rule:** Every mathematical relationship introduced in prose must first be stated in plain
natural language. The symbolic form may follow immediately in a display block as the formal
reference. A symbol expression alone — appearing in running text without a natural language
statement — is never sufficient.

**Why this rule exists:** Mathematical notation is a compressed shorthand for relationships
between quantities. Readers unfamiliar with the notation cannot evaluate whether a claimed
relationship is correct or what it physically means. Natural language forces the author to
commit to a specific physical interpretation, which makes the claim auditable without
requiring fluency in the notation. It also makes circular or incomplete reasoning more
visible — it is easier to hide a missing step inside a symbol chain than inside a sequence
of English sentences.

**What "natural language" means here:** State the relationship between the named physical
quantities in words. Identify what each quantity is (not just its symbol), and state the
direction of the relationship (proportional to, inversely proportional to, equals the
product of, etc.).

**Examples:**

Bad: "ω = ck, so E = ℏω = hν."

Good: "In the massless limit, the angular frequency of a wave is proportional to its
wavenumber — the spatial rate of oscillation — with the speed of light as the
proportionality constant. Combining this linear dispersion relationship with the quantum
of action (the minimum excitation energy per cycle of oscillation), the energy of the
wave packet is proportional to its frequency."

Bad: "g² = 8πβ/3 gives the gauge coupling."

Good: "The square of the gauge coupling constant — the number that sets the strength
of the force — equals eight times pi times the substrate quartic self-coupling, divided
by three. The quartic self-coupling is the coefficient controlling how steeply the
field's potential energy rises away from equilibrium."

**What symbols may still appear in prose:** After a quantity has been defined in natural
language, its symbol may be used as a shorthand in subsequent sentences in the same
section. Mathematical symbols in table cells, headers, and equation display blocks are
not subject to this rule. Code blocks are exempt.

**Enforcement:** When auditing any conceptual document, check that every equation
appearing in prose was preceded by a natural language statement of the same relationship.
If not, add the natural language statement.

---

## Development Cycle

Repeat this cycle indefinitely:

### Completeness Estimate (running)

```
Current estimate: ~38%  (viability: ~51%, mathematical rigor: ~27%)
Key bottleneck: D-depth assignment (Bottleneck 1 derivation chain COMPLETE Cycles 67c+70+71: D5=U(1) from real substrate; U(1) gauge action = complex structure J [J²=−I, verified]; SO(4)∩Aut(J)=U(2)→SU(2); D5/D6/D7 all Tier 2 candidates assuming mode count n; Tier 4 remaining = mode count n at D(4+n) from substrate field equation); r_U1/λ blocked (Bottleneck 2); v=246 GeV (α_D6 in GeV open, Bottleneck 3)
Next milestone: Derive mode count n at each D(4+n) threshold from substrate field equation (Tier 4→Tier 3 promotion for mode count assumption); derive D6/D7 overlap integral for μ² (Bottleneck 2); substrate extension for r_U1/λ
```

**Push history (viability / rigor / overall):**
| Push | Cycles | Change | Viability | Rigor | Overall |
|---|---|---|---|---|---|
| Baseline | 1–13 | Initial formalization pass | 25% | 8% | ~10% |
| 2026-04-05 | 14–18 | W/Z, Higgs, neutrinos, composite particles, gluons, spin | 26% | 8% | ~10% |
| 2026-04-05 | 19 | Antimatter; measurement/closure_topology corrections | 26% | 8% | ~10% |
| 2026-04-05 | 20 | Dark matter; Pauli exclusion, neutrino audit | 26.5% | 8% | ~10.5% |
| 2026-04-05 | 21 | Dark energy (CC problem dissolved); GR table; GW polarization gap | 27% | 8% | ~11% |
| 2026-04-05 | 22 | Route 3B: sin²θ_W = 3/8 → 0.231 self-consistently from equal couplings | 27% | 10% | ~12% |
| 2026-04-05 | 23 | Big Bang formalized (flatness/horizon dissolved structurally); product_geometry/gauge_couplings audited for Route 3B and ontological unity corrections | 27.5% | 10% | ~12.5% |
| 2026-04-05 | 24–25 | GW waves and black holes formalized; radioactive_decay and substrate audited; kink_model and weinberg_angle audited (label/overclaim fixes) | 28% | 10% | ~13% |
| 2026-04-05 | 26 | Phase transitions formalized (V_eff bifurcations, EWSB crossover, QCD confinement, D-depth sequence); mass_generation and compression_field audited | 28.5% | 10% | ~13% |
| 2026-04-05 | 27 | CMB formalized (Planck spectrum ✓, uniformity structural ✓, A_s OPEN); weak_force Weinberg angle updated to Route 3B result; entropy_production clean | 29% | 10% | ~13.5% |
| 2026-04-05 | 28 | Route 1 exploration doc written (Skyrme/FR — J=1/2 verified, N-Δ splitting, Jackiw-Rebbi; comparison with Route 3B; F_π/e_sk derivation as shared bottleneck); three_generations and spin_zero_mode audited | 29.5% | 10% | ~14% |
| 2026-04-05 | 29 | d_depth_lagrangians.md written (closure scale = √(α/2), effective gauge Lagrangians from DFC scalar, depth-running problem formalized, derivation sequence mapped); spin_emergence audited (cross-refs, language fixes); mass_spectrum.py audited (tau 8.4× failure prominently labeled, fine-tuning problem documented, "extra dimension" language removed); mass_hierarchy.md updated | 30% | 10% | ~14.5% |
| 2026-04-05 | 30 | k_Y = 3/5 DERIVED (not borrowed): from DFC equal-coupling + SM matter content Dynkin index matching; verified numerically; all anomaly conditions satisfied; sin²θ_W error +0.050%; Open Problem 4 in embedding_geometry.md resolved; hypercharge_normalization.md + .py new | 31% | 12% | ~15.5% |
| 2026-04-05 | 31 | Depth-running exploration: uniform γ falsified by co-crystallization; two-scale model (γ_space >> γ_weak≈0) self-consistent; M_c(D7) ≈ 8×10^14 GeV predicted from equal-coupling on α_s; depth-order ≠ energy-order structural finding; depth_running.md + .py new | 31.5% | 12.5% | ~16% |
| 2026-04-05 | 32 | γ_D = (16/3)√β DERIVED from E_kink/E_total(λ) — all α,c dependence cancels; β ≈ 0.035 inferred; kink width at D1 = Planck length (self-consistent); D-label Scheme A/B ambiguity formally documented in bifurcation.py; bifurcation_dynamics.md + .py new | 32% | 14% | ~17% |
| 2026-04-05 | 33 | First S-matrix from DFC substrate: shape mode ω₁ = (√3/2)m_σ parameter-free (Pöschl-Teller n=2 spectrum, exact); kink-antikink Born phase shift δ(k) = 4m_σ/(βk); Levinson consistency verified; kink_scattering.md + .py new; formation.md audited (added cross-refs + quantitative γ note) | 32.5% | 15.5% | ~18% |
| 2026-04-05 | Prep | Equation stubs (11 modules) + comparisons/swot.md — roadmap to completeness | — | — | — |
| 2026-04-05 | 34 | Bell/DFC hidden variable formalization: Assumption 2 violated by D1/D2 substrate connectivity (not conspiracy); E(a,b) = -cos(θ) verified; CHSH = 2√2 ≈ 2.828 verified to 4×10^-16; no-signaling P(A)=0.5 verified; Tsirelson bound from SU(2) geometry (formal proof OPEN); bell_hidden_variables.md + bell_correlations.py new | 33% | 16% | ~19% |
| 2026-04-05 | 35 | Tsirelson bound PROVED algebraically: C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂] → λ_max=8 → ‖C‖≤2√2; identity error 9×10^-16; commutator norms = 2.000000 exactly at optimal angles; tsirelson_proof() function verified; three_generations.md audited (bifurcation_dynamics + fermion_spectrum_full cross-refs added); gauge_couplings.py audited (M_c(D5) consistency note added; squashing_correction PLACEHOLDER clearly labeled) | 33.5% | 17% | ~20% |
| 2026-04-05 | 36 | kink_nucleation.md (new): two-sector topology proved (π₀ of φ⁴ configs = Z₂ for |N|=1); V''(0)=−α<0 saddle instability; ΔV/E_kink=0.71 at β=0.035; nucleation binary by continuity; Tsirelson chain now closed conditional only on D6=φ⁴; Born rule from first-passage stats remains open. substrate.md audited: Open Problems updated (Schrödinger DERIVED, binary outcomes PROVED; Born rule + ℏ still open); cross-refs to Cycles 32–36 added. kink_model.py audited: stale KinkDynamics reference removed; cross-refs added; ρ(x) profile now shows ρ−ρ_vac (excess above vacuum) alongside absolute density | 34% | 18% | ~21% |
| 2026-04-05 | 37 | depth_assignment.md (new): formal mapping of Bottleneck 1; 5 structural constraints identified; Route B (Hopf fibrations: S¹→S³→S⁵ at D5/D6/D7 gives U(1)/SU(2)/SU(3) isometry groups) identified as most promising; DOF count per bifurcation from substrate dynamics is the key missing derivation; termination at SU(3) conjectured from D7 confinement. entanglement.md audited: Tsirelson open question marked RESOLVED (Cycle 35); Cycles 34–36 cross-refs added. weinberg_angle_rg.py audited: k_Y=3/5 RESOLVED note added (Cycle 30 derivation); M_c(12) from substrate marked as remaining open; depth_assignment.md referenced | 34.5% | 18% | ~21.5% |
| 2026-04-06 | 38 | born_rule_derivation.md (new): Born rule for spin DERIVED (P(↑,n̂)=cos²(θ/2)) from SU(2) spinor geometry + binary nucleation (no free parameters); position Born rule structural argument (Kramers escape rate OPEN); born_rule_spin() verified in quantum_emergence.py (9 angles, normalization = 1.000000). higgs_geometry.md audited: Consistency Checks table added (two closure scale TENSION ✗); Open Questions 1–4 added; Weinberg angle language corrected to Route 3B. higgs_potential.py audited: σ_geom error found in higgs_mass_derivation.md (0.8 GeV was wrong → 3.4 GeV correct); m_H corrected to 124.4 ± 3.7 GeV (PDG m_t=172.76); one-loop 397.9 GeV warning added; mass_derivation.md uncertainty table corrected | 35% | 18.5% | ~22% |
| 2026-04-06 | 39 | planck_constant_derivation.md (new): ℏ hierarchy formally mapped; S_kink(D1)/ℏ = 4.24×10^39 derived and verified (bifurcation_dynamics.py); ~13.2 bifurcations required to reach ℏ scale (model has 4 → leaves 10^27 residual); shows ℏ not independently derivable from (α,β,c) alone — requires identification with SI unit system; hierarchy problem restated as S_kink(D1)/ℏ = (8/3)×2M_P²/√β; Route to ℏ via α_em derivation identified. measurement.md audited: Born rule entry updated (spin DERIVED Cycle 38); Open Question 1 updated; D-assignment note added to observables table; Connections section added. bifurcation_dynamics.py audited: S_kink/ℏ section added showing hierarchy 4e39→3e27 across D1–D5; 13.2 bifurcations to ℏ scale verified | 35.5% | 19% | ~22.5% |
| 2026-04-06 | 40 | coupling_derivation.md (new): Bottleneck 2 formally mapped; g_common ≈ 0.543 at M_c(12)=9.44×10^12 GeV confirmed from SM running (gauge_couplings.py: α₁=α₂=0.02358, 1/α_common=42.4); dimensional analysis gives g_DFC~2 (14× too large — geometric suppression required); key target: r_U1/λ_D5 ≈ 21.6 from holonomy integral over D5 S¹ fiber; chain from g_common → α_em = 1/128 mapped (Route 3B complete). spin.md audited: fixed "no spin-3/2 particles" (Δ, Ω⁻ are spin-3/2 composites → correct to "no elementary spin-3/2"); fixed D6 kink width ≠ Planck length error (L_Planck is D1 width; D6 is electroweak ~10⁻¹⁸ m); born_rule_derivation.md added to Connections. gauge_couplings.py audited: common coupling section added (g_common output verified); no duplication bug (34-line output) | 36% | 19.5% | ~23% |
| 2026-04-06 | 41 | parity_violation.md (new): explains why weak force couples only to left-handed fermions from D6 SU(2) Jackiw-Rebbi zero mode chirality (N=+1 kink → left-handed Weyl spinor → pure (1−γ⁵) coupling); no W_R prediction (no D6' closure in product topology); right-handed fermion mechanism identified as open question. product_geometry.md audited: S³ notation clarified (SU(2) ≅ S³ as manifold; gauge group is SU(2)); Connections section added (coupling_derivation.md, parity_violation.md cross-refs). proton_stability.py audited: truncated sphaleron status output fixed ([:40] removed); "KK modes" language replaced with correct DFC "closure-depth excitations" language | 36.5% | 19.5% | ~23.5% |
| 2026-04-11 | 42 | hopf_fibration_geometry.md (new): Route B formalized — S¹/S³/S⁵ → U(1)/SU(2)/SU(3) correspondence precisely mapped; DOF pattern (1,2,3 complex DOFs at D5/D6/D7); termination at SU(3) from confinement; equal-coupling ↔ equal-sphere-radii prediction; r_U1/λ = 2π/g² ≈ 21.3 geometric target. light.md audited: CRITICAL circular-logic fix — E=hν was claimed derived from massless KG dispersion but used E=ℏω as input (same statement: h=2πℏ, ω=2πν); one-sentence synthesis, abstract, derivation section, and table all corrected; E=ℏω now clearly labeled POSTULATE imported from QFT; note added that E=ℏω and E=hν are the SAME relation. coupling_derivation.py MAJOR REWRITE: g_common²=8πβ/3 heuristically derived (kink phase stiffness f²=(4/3)φ₀²/λ → r_U1/λ=3/(4β) → holonomy g²=8πβ/3); β=0.0351 → g_common=0.5423 vs SM 0.5443 (0.37%); RG sign bug fixed (SU(2)/SU(3) asymptotic freedom: subtract not add); α_em(M_Z)=0.00772 vs 0.00782 (1.3%); α_s(M_Z)=0.1049 vs 0.1182 (11%, M_c(D7) not yet from substrate) | 37% | 20.5% | ~24% |
| 2026-04-11 | 43 | tension_analysis.md (new): 10 conceptual tensions classified — T1 graviton/T3 strong CP/T7 hierarchy problem = DFC Supersedes (not reconciliation targets); T2 CKM/PMNS/T4 fundamental rep/T8 ℏ hierarchy/T9 two-closure-scale = DFC Internal Tension (must resolve); T5 dark matter/T6 dark energy/T10 proton mass = Open Assessment (deferred). magnetic_monopoles.md COMPLETED: π₂(S¹) = 0 topological proof written out (lifting criterion via universal cover ℝ, contractibility of ℝ); Bianchi identity dF = d²A = 0 → ∇·B = 0 derived structurally; DFC prediction Φ_m = 0 (stronger than Parker bound); falsifiability criterion stated. magnetic_monopoles.py (new): π₂(S¹) = 0 proof verified step-by-step; winding number quantization verified for all SM charges; Bianchi identity checked numerically; Parker bound vs DFC prediction tabulated; Dirac quantization shown consistent but vacuous. No free parameters used. | 37.5% | 21% | ~24.5% |
| 2026-04-11 | 44 | atomic_structure.md COMPLETED: DFC coupling chain extended to atomic physics — β → g²=8πβ/3 → α_em(M_Z)=1/129.6 → QED running (Δ1/α=10.46) → α_em(m_e)=1/140.0 → E_1=-13.03 eV. All spectral errors (4.2%) are systematic and trace to single 1.3% error in α_em(M_Z); ratio of any two lines is exact. atomic_structure.py (new): full QED one-loop threshold matching from M_Z to m_e; hydrogen energy levels E_n=-m_e α²/(2n²); Lyman/Balmer/Paschen series computed; error budget confirmed (all ≈4.2% from common source). decoherence.md audited: STUB label removed (content was already written). neutrino_masses.py audited: CRITICAL — Δm² "predictions" marked CIRCULAR (m₂,m₃ are derived from input Δm² values, not predicted); D-label integer spacing assumption flagged; only genuine output is m₁ = m_e × f_ν². | 38% | 21.5% | ~25% |
| 2026-04-12 | 45 | arrow_of_time.md COMPLETED: irreversibility from Z₂ topology formalized (ΔV/E_kink=0.71 computed from kink_model.py, Γ_forward/Γ_reverse=exp(ΔV/k_BT)≫1 at any observable T); low initial entropy of D1 state explained without fine-tuning (W=1 for pre-cascade substrate); S=k_B log W structural argument written; CPT/weak arrow distinguished from thermodynamic arrow; formal equations section added; consistency checks updated (irreversibility DERIVED, others structural or open). depth_running.md audited: one forbidden-language fix ("unified structure" → "two independent closures that co-emerge simultaneously"). depth_running.py audited: runs correctly, outputs honest about inputs vs predictions, free parameters correctly identified; no changes needed. | 38.5% | 21.5% | ~25.5% |
| 2026-04-12 | 46 | strong_cp_problem.md COMPLETED (STUB → full doc): strong CP dissolved by S⁵ CP symmetry — complex conjugation is exact Z₂ isometry of S⁵ (verified numerically); theta=0 selected as CP-symmetric fixed point at D7 formation; no axion predicted (Criterion B); theta=pi ruled out experimentally (d_n would be 10⁹ × bound); product topology independence of D6 CKM and D7 theta formalized; quark mass matrix phase identified as open. strong_cp.py (new): CP symmetry verified (10k random S⁵ points, max deviation 0.00e+00); CP fixed points on S⁵ = S² (real 2-sphere); theta=0 vs pi comparison; future nEDM projections tabulated; homotopy groups pi_3(SU(3))=Z vs pi_3(S⁵)=Z₂ documented; axion search falsifiability table. | 39% | 21.5% | ~26% |
| 2026-04-13 | 47 | phase_stiffness_derivation.md (new): f² = (4/3)φ₀²/λ proved exactly via ∫sech⁴(u)du = 4/3 (Bogomolny identity verified numerically: error 6.5e-14); holonomy formula g² = 2π/(r_U1/λ) stated; gap precisely located: r_U1/λ = 3/(4β) is physical identification r_U1 = φ₀²/(β×f²) not derived from substrate; Route A (KK reduction on S¹) and Route B (domain-wall worldvolume) proposed for next step; AUDIT FINDING: kink_model.py formula (4/3)c√(2α³/β) wrong by factor 2√β vs BPS-correct (4/3)c²φ₀²/λ; γ_D derivation (Cycle 32) depends on wrong formula — retraction flagged. | 39% | 22% | ~26% |
| 2026-04-13 | 48 | RETRACTION — kink_model.py corrected: E_kink formula changed from (4/3)c√(2α³/β) to BPS-correct (4/3)c²φ₀²/λ = (4/3)cα^(3/2)/(β√2); γ_D = (16/3)√β retracted — with correct E_kink, E_kink/E_total(λ) = 8/3 exactly (universal constant, β-independent, > 1); bifurcation_dynamics.py audited: gamma_from_beta() labeled RETRACTED, gamma_ratio_correct() added (verifies 8/3 for all β); bifurcation_dynamics.md updated; ΔV/E_kink corrected 0.71 → 0.265 (at α=1, β=0.035) in 6 files: kink_nucleation.md, kink_model.py, arrow_of_time.md, balloon_analogy.md, fundamental_limits.md, OVERVIEW.md. | 38.5% | 20% | ~24.5% |
| 2026-04-13 | 49 | hierarchy_problem.md COMPLETED (STUB → full doc): DFC dissolution formalized — Higgs has no bare mass parameter (radiative CW generation only); S³ Goldstone structure gives m_H → 0 as y_t → 0 (symmetry protection without SUSY); 5 bifurcation events separate D1 from D6 (exponential decoupling of Planck-scale corrections); desert prediction (no new particles between TeV and M_c); T9 tension formally quantified: Δ_FT(Route 3B) ≈ 10²⁰ (12-order improvement over SM), Δ_FT(higgs_md) ≈ 10³⁰ (no improvement — depends on which M_c is correct); hierarchy_problem.py (new): fine-tuning Δ_FT(SM)=3.56e32, Δ_FT(R3B)=2.49e20 verified; CW mass estimate; desert table. | 39% | 20% | ~25% |
| 2026-04-15 | 50 | compton_scattering.md (new): first physical cross-section from DFC — Thomson σ_T = (8π/3)(α_em/m_e)² derived through unbroken chain β→g²=8πβ/3→α_em(M_Z)=1/129.6→QED running→α_em(0)=1/140.1→σ_T=6.37×10⁻²⁹ m² (observed 6.65×10⁻²⁹; −4.3% systematic error = 2×α_em error; single source: r_U1/λ gap); Klein-Nishina Compton cross-section shape derived structurally (ε-dependent suppression exact). scattering_cross_sections.py COMPLETED (STUB → full implementation): full coupling chain verified; QED running imports atomic_structure.py (all fermions e,μ,τ,u,d,s,c,b; Δ(1/α)=10.46); r_e, σ_T, σ_KN(ε) implemented; error budget confirmed (2.2% in α → 4.3% in σ). strong_force.md audited: Consistency Checks table added (α_s(M_Z)=0.105 vs 0.118 failure noted, 8 gluons/confinement structural). higgs_geometry.md audited: stale γ_D cross-ref corrected. coupling_derivation.py audited: BETA/GAMMA_D provenance corrected (γ_D retraction labeled). | 39.5% | 20.5% | ~25.5% |
| 2026-04-15 | 51 | muon_decay.md (new): weak sector fully derived — β → g_common → g₂(M_Z) → M_W = 79.67 GeV (−0.88%), M_Z = 90.86 GeV (−0.36%), G_F = 1.168×10⁻⁵ GeV⁻² (+0.18%), τ_μ = 2.180 μs (−0.80%); all within 1%; most accurate cluster in the model. Six-step derivation chain documented end-to-end. muon_lifetime.py (new): full numerical computation of all four quantities from β. muon_tau.md audited: stale "< 0.1%" τ_μ claim corrected to actual −0.80% DFC prediction; Consistency Checks row and Connections updated. weinberg_angle_rg.py audited: Cycle 51 cross-ref to muon_lifetime.py added. r_U1/λ blockage analyzed: Routes A and B both blocked for pure real φ⁴ (no U(1) phase to localize); requires substrate extension. M_W, M_Z, G_F, τ_μ added to Tier 2a. | 40% | 21% | ~26% |
| 2026-04-15 | 52 | electroweak_precision.md (new): five tree-level precision tests computed — ρ = 1.000000, T = 0, sin²θ_W two-route agreement Δ<10⁻¹⁵, G_F two-route agreement exact, M_W/M_Z = cos θ_W to 10⁻¹⁶; all confirm DFC weak sector is internally self-consistent. electroweak_precision.py (new): full numerical verification; open: loop corrections (Δρ_top = +0.008, not yet computed); v = 246 GeV derivation gap identified as next target. radioactive_decay.md audited: G_F OPEN entry corrected to Tier 2a (Cycle 51); stale "only prediction within 1%" text corrected; cross-refs added. proton_stability.py audited: neutron_lifetime_treelevel() was computed but never printed in __main__ — added new section showing both PDG-G_F (τ_n=878.4 s, −0.11%) and DFC-chain G_F (τ_n=875.3 s, −0.47%) routes. | 40.5% | 21.5% | ~26.5% |
| 2026-04-15 | 53 | vev_derivation.md (new): v = 246 GeV problem formally mapped — μ² from D6/D7 overlap integral, λ from Berger sphere S³ quartic expansion (R₄ coefficient); two-scale T9 resolution formally stated (gauge scale ≠ modulus activation scale); completing this removes v from 4 Tier 2a predictions; Berger sphere R₄ calculation identified as tractable. bifurcation_dynamics.md audited: open-problem numbering bug fixed (two "### 2." items); stale Connections note corrected (RETRACTED label preserved). mass_spectrum.py verified: tau failure prominent, module runs correctly, no changes needed. | 41% | 21.5% | ~27% |
| 2026-04-15 | 54 | pair_production.md (new): pair production/annihilation as kink-antikink nucleation/coalescence; threshold E_γ ≥ 2m_e = 1.022 MeV (exact); σ(e⁺e⁻→μ⁺μ⁻) = 4πα²_em(√s)/(3s) Tier 2b (~4% systematic from α_em); R-ratio = N_c × Σ Q_q² = 11/3 above bottom threshold (Tier 1 — EXACT structural prediction from D7 SU(3) 3-color count); BaBar comparison at 10.58 GeV: DFC 0.847 nb vs obs 0.873 nb (−3.1%). pair_production.py (new): full numerical module with QED running, R-ratio thresholds, σ(e⁺e⁻→μ⁺μ⁻) table. substrate.md audited: CRITICAL — three stale errors fixed: wrong E_kink formula (retracted Cycle 48) replaced with BPS-correct form; γ_D "DERIVED" relabeled "RETRACTED"; stale "8.6× mismatch" in coupling description replaced with current accuracy (sin²θ_W <0.01%, α_em 1.3%, M_W/M_Z/G_F/τ_μ all <1%). gauge_couplings.py audited: stale γ_D attribution for M_c(D5) corrected (derivation is from SM α₁=α₂ crossing, not retracted γ_D formula); module verified. | 41.5% | 21.5% | ~27.5% |
| 2026-04-16 | 55 | anomalous_magnetic_moment.md (new): one-loop Schwinger term a_e = α_em/(2π) from DFC coupling chain; DFC predicts 0.001136 vs observed 0.001160 (−2.01%); error traces entirely to α_em(M_Z) systematic; muon g-2 leading term computed (same source); Fermilab anomaly identified as HVP contribution blocked by 11% α_s error. anomalous_magnetic_moment.py (new): DFC coupling chain → α_em(m_e) = 1/140.1 → a_e; SM 4-loop comparison (error 2×10⁻⁶%); error budget. spin.md audited: Open Q4 updated with Cycle 55 g-2 result; cross-refs to new anomalous_magnetic_moment files added. coupling_derivation.py audited: runs correctly, all claims honest, no changes needed. a_e added to Tier 2b table. | 42% | 21.5% | ~28% |
| 2026-04-16 | 56 | ROADMAP EXPANSION: compression_dynamics.md (new, full doc): DFC self-compression equations reconciled with thermodynamic/hydraulic/Navier-Stokes/elasticity/acoustics/Jeans/Heisenberg compression formalisms; 5 structural divergences identified; 5 open derivations mapped. 6 new phenomenon stubs: lamb_shift.md, photoelectric_effect.md, hawking_radiation.md (quantum/), superconductivity.md, superfluidity.md, quantum_hall_effect.md (condensed_matter/ — new domain). 3 new equation stubs: nuclear_binding.py (full Bethe-Weizsäcker + Fe-56 ✓), lamb_shift.py (α⁵ scaling stub), quark_gluon_plasma.py (T_c 653% error — α_s blockage confirmed). measurement.md updated: compression_dynamics.md cross-ref added. CLAUDE.md Step 2 expanded: audit scope now covers full repository, not just foundations/phenomena/. README.md: full roadmap updated with all new stubs and condensed_matter/ domain. | 43% | 21.5% | ~29% |
| 2026-04-18 | 71 | d5_complex_structure.md (new): Bottleneck 1 Tier 3 gap closed — U(1) gauge action on charged fields IS the complex structure J; φ→e^{iqθ}φ → infinitesimal generator J_q(A,B)=(−qB,qA) → J_q²=q²(−I)=−I for |q|=1; complete Bottleneck 1 derivation chain: D5=U(1) [Cycle 70] → D6 modes carry U(1) charge [Cycle 67c] → U(1) charge = J [Cycle 71] → SO(4)∩Aut(J)=U(2)→SU(2) [Cycle 70]; D5/D6/D7 all promoted to Tier 2 candidates (assuming mode count n); Tier 4 remaining: (a) derive mode count n at D(4+n) from substrate field equation; (b) termination at D7. d5_j_connection.py (new): all 4 verification steps pass — J²=−I and antisymmetric for n=1,2,3 (errors 0.00e+00); commutant dim n²=1/4/9 for n=1/2/3 ✓; J_gauge = J_Cycle70 (identical matrix, max diff 0.00e+00); fractional charges q=±1/3,±2/3,±1 all give J_norm²=−I (errors 0.00e+00); "✓ ALL CHECKS PASS". photoelectric_effect.md audited: d5_complex_structure.md cross-ref added; document already accurate, no other changes. proton_stability.py audited: module runs correctly (τ_n=878.4 s, −0.11%), language clean, no changes needed. | 51% | 27% | ~38% |
| 2026-04-18 | 70 | complex_zero_mode_gap.md (new): D5=U(1) from real substrate proved — second-order PDE → 2 real DOFs per zero mode (position q + velocity v) → for n kinks: 2n real DOFs → S^(2n-1) → SO(2n) real isometry; SO(2)=U(1) at D5 (no complex structure needed — Tier 2 candidate); SO(4)≠SU(2) (dim 6≠3), SO(4)∩Aut(J)=U(2) dim=4 → SU(2) at D6; SO(6)∩Aut(J)=U(3) dim=9 → SU(3) at D7. u1_from_paired_modes.py (new): SO(2)=U(1) verified; so(4)≅su(2)_L⊕su(2)_R verified (error 0.00e+00); commutant dim U(2)=4 verified (SVD null-space); commutant dim U(3)=9 verified. depth_assignment.md audited: γ_D retraction propagated (removed stale formula), Cycle 70 progress added to Status section, Open Problems reordered by current priority, cross-refs to Cycles 59–70 added. neutrino_masses.py audited: Δm² values corrected to PDG 2024 (7.42e-5, 2.517e-3) consistent with flavor_mixing.py (Cycle 69); cross-refs to neutrino_oscillations.py and flavor_mixing.py added. | 50% | 26.5% | ~37% |
| 2026-04-17 | 69 | flavor_mixing.md (STUB → full doc): DFC Explanation completed — two-basis picture (flavor=D6 SU(2), mass=D4/D7); CKM small from D6/D7 adjacency; PMNS large from D4/D6 depth gap + near-degeneracy (T10 tension documented); CP violation requires N≥3 structural proof; J=0 for N=2, J=3.07×10⁻⁵ for N=3 verified. flavor_mixing.py (new): CKM/PMNS matrices constructed; unitarity checked (max deviation 2×10⁻¹⁶ for CKM, 1×10⁻¹⁶ for PMNS); Jarlskog invariant formula and matrix agree; N=2 J=0 proved; depth-gap mixing estimate (ratio 3.8×); Δm² ratio failure 33.9 vs 2.67 documented. strong_force.md audited: "screening anti-screening" garbled text fixed; zero_mode_multiplet.md + coupling_derivation.py + quark_gluon_plasma.md cross-refs added. fermion_spectrum_full.py audited: CRITICAL — nu_mu=1e-4 MeV and nu_tau=0.015 MeV were wrong by 4-6 orders of magnitude vs oscillation data; corrected to nu_2=8.6e-9 MeV, nu_3=5.0e-8 MeV; Cycle 59/65/69 cross-refs added. | 50% | 26% | ~36% |
| 2026-04-17 | 68 | inflation.md (STUB → full doc): DFC inflation = D1→D4 bifurcation cascade; flatness/horizon dissolved structurally (no pre-existing space); monopoles absent for independent topological reason (π₂(S¹)=0); n_s = 0.9667 at N_e=60 (+0.4σ of observed 0.9649) — structural consistency confirmed; N_e(naive) = ln(M_Pl/M_c(D4)) = 10.5 (factor 5.7 deficit, prominently labeled); de Sitter rate from V_false = α²/(4β); extended cascade table (all endpoints below 10 MeV required); A_s, r both blocked; three N_e resolution candidates identified. inflation.py upgraded (STUB → full module): 5 computations, n_s table vs σ, reheating BBN check, extended cascade endpoints. nuclear_binding.md audited: deuteron B-W failure (−365%, known limitation) added to Consistency Checks table; equation module cross-ref added; empirical-inputs label added to Fe-56 prediction. ISSUES.md updated: Bottleneck 1 structural chain progress from Cycles 66–67c documented. | 49.5% | 26% | ~35.5% |
| 2026-04-17 | 67c | complex_structure_derivation.py (new, Bottleneck 1 Computation 3): D5 Z₂ kink = half-vortex of U(1); phase profile θ₅(x)=(π/2)(1−tanh(x/ξ)) winds π→0; W=−1/2 verified (error 5.55×10⁻¹⁷). Dressed D6 mode η₀^dressed=η₀^real×e^{iθ₅}: norm preserved, arg=θ₅(x)≠0, overlap with real mode =0.774<1. U(1) current j_x=η₀²×∂_xθ₅; ∫j_x dx=−2π/(5ξ)=−1.2566 proved exactly (∫sech⁶=16/15 exact, error 0). BOTTLENECK 1 STRUCTURAL CHAIN COMPLETE: D6 kink is complex+charged in D5 half-vortex → gauge coupling (not scalar) → n zero modes → SU(n). Tier 3 gap remaining: D5=U(1) from substrate alone (Hopf S¹ Route B). Integer Q=−e from SU(2) doublet (T₃+Y/2=−1) explained. bifurcation_mode_count.md updated with full chain. Completeness ~34.5%→~35%. | 49% | 26% | ~35% |
| 2026-04-17 | 67 | gauge_coupling_zero_modes.py (new, Bottleneck 1 Computation 2): three cases proved — (1) real kink: j_μ=Im(φ*∂_μφ)=0 identically for real φ → gauge coupling = 0 → n modes trivially ✓; (2) complex kink: static E[a] invariant under rigid shift (φ₆,A_0)→(φ₆(·-δa),A_0(·-δa)) → dE/da=0 → ω²=0 exact, E_kinetic std = 2.2×10⁻¹⁶; (3) scalar coupling: δω²|_{a=0} = −2g×α/(5β) proved analytically (integrals ∫sech⁴tanh²=4/15, ∫sech⁴=4/3 verified to 4×10⁻¹⁶), lift grows to −2gφ₀² at large separation. bifurcation_mode_count.md updated: Computation 2 documented; final gap = derive D6 kink complex structure (phase DOF) from D5 coupling in substrate. Completeness ~34%→~34.5%. | 48.5% | 25.5% | ~34.5% |
| 2026-04-17 | 66 | d5_d6_coupling.py (new, Bottleneck 1 Computation 1): biquadratic diagonal identity V_eff_5=V_eff_6 proved and verified (0.00e+00); full 2×2 biquadratic: H_+/H_- decoupled; Goldstone protects 1 zero mode (not 2) for g>0; n_zero=1 at g/β=1.0 is P-T coincidence (s=1.0, E₁=0 exactly — mode threshold crossing, not protected). Linear coupling correct cross-term g (constant): ω²(±)=±g verified, instability confirmed; Z₂ broken. KEY FINDING: scalar coupling reduces n modes to 1; n zero modes require gauge (derivative) coupling between depth sectors. bifurcation_mode_count.md updated with Computation 1 results and refined remaining gap. glossary.md updated: α_s, M_c, φ₀, g_common, zero mode, P-T potential, k_Y, running coupling added; quick-reference equations expanded (g²=8πβ/3, BPS kink energy, sin²θ_W, Δm²). | 48% | 25% | ~34% |
| 2026-04-17 | 65 | neutrino_oscillations.md COMPLETED (STUB → full doc): Dimensional Folding Explanation completed — D4 winding modes as mass eigenstates, D4/D6 geometry mismatch as source of PMNS mixing, near-maximal θ₂₃ from near-degeneracy argument (shown to fail: m₃ ≫ m₂ conflicts with argument), mass ratio failure Δm²₃₁/Δm²₂₁ = 34 vs DFC 1.34 (4.3×, non-uniform depth spacing required). Formal Equations section added: two-flavor oscillation formula P = sin²(2θ)sin²(1.267 Δm²L/E); PMNS matrix; mass-squared differences; reactor oscillation length 1.6 km explains Daya Bay baseline; Daya Bay P = 0.935 vs 0.944 (−1.0%, using input θ₁₃). equations/neutrino_oscillations.py (new): oscillation lengths for solar/atmospheric/reactor; Daya Bay comparison; mass-ratio failure labeled. mass_hierarchy.md audited: CRITICAL — "generates hierarchy for all three generations" overclaim corrected (tau fails 8.4×); "dimple emerges from D7 squashing" relabeled as working hypothesis (Tier 3). kink_scattering.py and s_matrix.py audited: both clean. | 47.5% | 24.75% | ~33.5% |
| 2026-04-17 | 64 | casimir_effect.md COMPLETED (STUB → full doc): Dimensional Folding Explanation completed (mode deficit mechanism, 1/d⁴ from dimensional analysis, attractive sign, thermal crossover); Formal Equations section added (Casimir pressure P=−π²ℏc/(240d⁴), energy/area, 1/d⁴ scaling derivation — no ℏ needed, zeta-function mode sum, thermal length scale λ_T = ℏc/(k_BT) = 7.6 µm at 300 K); Consistency Checks updated (7 rows, 6 ✓ structural/derived, 1 ✗ BLOCKED on ℏ); Connections expanded with new cross-refs. equations/casimir_effect.py (new): pressure/force/energy functions; zeta regularization demo (ζ(−1)=−1/12, ζ(−3)=1/120); pressure table at 100 nm–10 µm (verified P(1µm)=−1.3001 mN/m² vs Lamoreaux 1997 −1.30 mN/m²); thermal correction ratio; Wolfram Alpha string. quark_gluon_plasma.py audited: CRITICAL fix — α_s running past Landau pole was silently clamped to 0.01 (showed identical DFC/obs at 1 GeV, masking perturbative breakdown). Fixed to return None past Landau pole; output now shows NON-PERT at 1 GeV and 0.3 GeV. | 47% | 24.5% | ~33% |
| 2026-04-17 | 63 | coupled_fluctuation.py (new): n independent φ⁴ kink fields at x=0 → n IDENTICAL zero modes (profile η₀ ∝ sech²(x/ξ), same for all n) → coincident and degenerate → SU(n). Zero mode error 1.9×10⁻⁵ (numerical grid); shape mode ω₁² = (3/2)α verified (error 2.5×10⁻⁵ — also CORRECTS docstring error in hopf_dof_count.py which had ω₁² = (3/4)α). Overlap vs. separation: SU(n) at sep=0 → U(1)ⁿ at sep≫ξ (exponential decay). bifurcation_mode_count.md updated with n-field picture and coupled_fluctuation.py cross-ref. hawking_radiation.md COMPLETED (Formal Equations stub → full content): T_H = ℏc³/(8πGMk_B) with numerical values; evaporation timescale M³ scaling; Schwinger analog rate; Bekenstein-Hawking entropy S = A/(4Gℏ/c³); BEC sonic analog (one blockage removed vs. astrophysical). comparisons/swot.md updated (Cycles 58–63): Bottleneck 1 status corrected; condensed matter cluster added to Opportunities; completeness updated 27.5% → 32%. | 46.5% | 24.25% | ~32.5% |
| 2026-04-17 | 62 | bifurcation_mode_count.md (new): Bottleneck 1 first half formally mapped — codimension-1 bifurcation theorem gives one new soft mode per threshold; D5 U(1) complex structure forces subsequent modes to be complex → S^(2n-1) at D(4+n); structural argument complete; requires coupled fluctuation spectrum (D5+D6 two-component field) to close; 4 specific open computations identified. lamb_shift.py AUDITED AND FIXED: missing 1/n³ factor for n=2 corrected; DFC α⁵ scaling estimate computed (947 MHz vs observed 1057.845 MHz; −10.5% error — Tier 2b); error budget table (all EM predictions from same α_em source); Bethe formula runs cleanly. lamb_shift.md updated: Formal Equations section completed from [STUB]; DFC prediction 947 MHz labeled Tier 2b; error budget table; Consistency Checks updated. | 46% | 24% | ~32% |
| 2026-04-16 | 61 | quantum_hall_effect.md COMPLETED (Formal Equations stub → full content): R_K = h/e² = 25812.807 Ω verified to 3.6×10⁻¹⁰ (Tier 1); G₀ = e²/h = 38.74 µS verified; IQHE plateaus σ_xy = ν×e²/h (ν=1–5); Jain sequence p/(2p±1) structural; Landau levels at B=10 T computed. equations/quantum_hall.py (new). superfluidity.md COMPLETED (Formal Equations stub → full content): κ₀ = h/m_He4 = 9.969×10⁻⁸ m²/s verified to 7.1×10⁻⁵ (Tier 1, 0 free params); quantized circulation table n=1–5; BEC T_c labeled BLOCKED (requires ℏ); Landau criterion structural; unified topological comparison table (Φ₀, Φ₀_e, κ₀, G₀, K_J all from same DFC U(1) winding). equations/superfluidity.py (new). All three condensed matter phenomena (superconductivity, superfluidity, QHE) now have complete Formal Equations sections with Tier 1 verified results. | 45.5% | 23.75% | ~31.5% |
| 2026-04-16 | 60 | superconductivity.md COMPLETED (Formal Equations stub → full content): Flux quantization Φ₀ = h/(2e) from DFC winding number verified to 2.2×10⁻¹⁰ (Tier 1, 0 free params); Josephson constant K_J = 2e/h verified to 2×10⁻¹² (Tier 1); Anderson-Higgs at condensate scale vs EW scale compared (same mechanism, ratio 10²⁷ in mass); BCS gap Δ/(k_BT_c) = 1.764 labeled IMPORTED (phonon kink binding open); equations/superconductivity.py (new). higgs_geometry.md audited: m_H corrected 125.1 ± 1.5 → 124.4 ± 3.7 GeV (Cycle 38 correction now propagated); quartic source corrected (NOT S³ curvature — R₄=0 from Cycle 58; λ = β/4 from substrate; Ricci contributes to −μ²ε² not +λε⁴); berger_sphere.py cross-ref added. coupling_derivation.py audited: berger_sphere + zero_mode_multiplet cross-refs added; module clean. | 45% | 23.5% | ~31% |
| 2026-04-16 | 59 | zero_mode_multiplet.md (new): second half of Bottleneck 1 proved — n coincident degenerate zero modes sharing one kink background → configuration space S^(2n−1) ⊂ ℂⁿ → complex-structure-preserving isometry = U(n) = U(1)×SU(n) → gauge group SU(n); proved algebraically from Pöschl-Teller uniqueness (one zero mode per kink), norm conservation (|c|² = const), and U(n) isometry theorem; gauge boson counts 1/3/8 verified for n=1,2,3; SU(2) Pauli and SU(3) Gell-Mann algebras verified (max error 1.11×10⁻¹⁶). hopf_dof_count.py (new): full numerical module — Pöschl-Teller spectrum (ω₀²=0 exact, ω₁=√3/2 m_σ exact), zero mode normalization (analytical = numerical to 1.32×10⁻¹⁶), SU(n) generator counts, gauge boson predictions (all ✓ for n=1,2,3; n=4 correctly ✗). First half of Bottleneck 1 still OPEN: why D(4+n) opens exactly n coincident modes from substrate dynamics. kink_scattering.py audited: old retracted kink mass formula corrected to BPS-correct (Cycle 48); gamma_D provenance note updated. electron.md audited: "D5+D6 closure level" phrasing fixed; tau mass 8.4× failure row added to Consistency Checks; zero_mode_multiplet.md cross-ref added to Connections. | 44.5% | 23% | ~30.5% |
| 2026-04-16 | 58 | berger_sphere.py (new): Ricci scalar of biaxial Berger sphere derived analytically via Cartan structure equations; R(ε) = 24−16ε−8ε² exact (polynomial terminates at degree 2); R₄ = 0 proved (numeric verification: 1.5×10⁻¹²); CORRECTS vev_derivation.md claim that λ_DFC = R₄/r_D6⁴. Physical consequence: Ricci term DESTABILIZES ε=0 (contributes to −μ²ε²); quartic stabilizer λ = β/4 ≈ 0.0088 from substrate β, not from geometry; V(ε) = −α_D6/2 ε² + β/4 ε⁴ identified directly as the substrate potential at D6 depth; VEV = √(2α_D6/β) in substrate units; remaining gap = α_D6 in GeV (requires M_c(D6) from Bottleneck 1). vev_derivation.md CORRECTED: Open Problem 1 (Berger R₄) marked RESOLVED; new Open Problems 2–5 restructured around normalization and overlap integral. higgs_potential.py AUDITED: docstring corrected (quartic from β not curvature; m_H uncertainty corrected to ±3.7 GeV); berger_sphere.py cross-ref added. ISSUES.md: Berger R₄ moved to Resolved. | 44% | 22.5% | ~30% |
| 2026-04-16 | 57 | quark_gluon_plasma.md (STUB → full doc): Formal Equations section added (string tension T_c estimate, Debye screening λ_D ~ 1/(g_s T), DFC T_c prediction 1160 MeV vs 154 MeV with 653% error explained, KSS viscosity bound η/s ≥ 1/(4π), Polyakov loop order parameter); Consistency Checks updated (6 rows, 4 ✓ structural, 2 ✗ blocked); 4 specific Open Questions added. kink_model.py audited: stale γ_D=(16/3)√β retraction label corrected (Cycle 48); compression_dynamics.md cross-ref added. comparisons/swot.md major update (Cycles 34–57): γ_D retraction removed from Strengths; weak sector <1% cluster added; Tsirelson proved, Born rule spin derived, first cross-sections, strong CP dissolved, hierarchy dissolved, magnetic monopole prediction, k_Y derived documented; completeness 18% → 27.5% → 29.5% corrected; all 5 comparison tables updated; Summary Scorecard expanded with k_Y and strong CP rows. | 43.5% | 21.5% | ~29.5% |

**After every push:** Update the estimate here and in `README.md` after every commit push,
even if the change is small (e.g., ~10% → ~10.5%). The estimate has two components:
- **Viability** (~25% baseline): increases when new structural accounts are added, known
  failures are resolved, or predictions are confirmed by data. Formalizing placeholder
  docs adds small increments (~0.5% each for major phenomena).
- **Mathematical rigor** (~8% baseline): increases only when actual derivations are
  completed — a coupling constant from (α, β, c), an S-matrix result, a formal proof.
  Structural descriptions and consistency checks do not move rigor.

The overall estimate is the average of the two. Track the push-by-push history in the
running record below the estimate block so progress is visible over time.

**Priority weighting for Step 1:** When choosing which phenomenon or foundation doc to work on,
give preferential weight to those that connect to the three critical bottlenecks:

1. **D-depth assignment mechanism** — why does U(1) emerge at D5, SU(2) at D6, SU(3) at D7?
   Prefer docs that explore the substrate's self-interaction structure at these depths, the
   winding/wrapping configurations that produce each closure, or alternative depth orderings.

2. **First-principles coupling constants** — α_em, sin²θ_W, α_s, Yukawa couplings.
   Prefer docs where a coupling constant might be derived from geometric parameters rather
   than taken from experiment. Even partial progress here (e.g. the ratio of two couplings)
   is high-value.

3. **S-matrix / scattering amplitudes from the substrate** — no observable has yet been
   computed from the field dynamics (only from imported equations). Prefer docs that
   connect the substrate dynamics to actual measurable cross-sections or decay rates.

These bottlenecks are the difference between a conceptual framework (~25% viable) and a
predictive, mathematically rigorous theory (~80%+). All other work is valuable but secondary.

**After every push, also check `ISSUES.md`** — the centralized tracker for all open questions,
known failures, internal tensions, retracted claims, and blocked derivations. When an issue is
resolved, move it to the Resolved section. When a new failure or conflict is discovered, add it.

---

### Step 0 — Practical Applications (every ~5–10 cycles, optional)

Before Step 1, consider whether to add a new entry in `practical_applications/`.
See `practical_applications/OVERVIEW.md` for the document format and Pool A/B/C source selection.
Use this step to explore engineering implications derived from verified DFC results —
absolute limits, efficiency ceilings, or unusual technological possibilities implied by
the substrate structure. These entries do not advance rigor directly but make the model's
scope concrete and communicate its implications beyond fundamental physics.

---

### Step 1 — Add a New Phenomenon

1. Identify a physics phenomenon not yet in `phenomena/` (or a placeholder needing content).
   Choose one systematically or randomly from the list of unformalized docs, with preferential
   weight toward phenomena that connect to the three critical bottlenecks above.
2. Write the **conceptual document** in `phenomena/` following the standard format:
   - One-Sentence Synthesis (DFC account, not a placeholder)
   - Observation (what is measured/observed)
   - Standard Explanation (SM account, concise)
   - Dimensional Folding Explanation (DFC account — structural, specific, no anthropomorphism)
   - Formal Equations (key equations, even if some are stubs)
   - Consistency Checks table
   - Open Questions (honest about what is not yet derived)
   - Connections (links to related docs)
3. Write or update the **equation module** in `equations/` with numerical verification.
   Every quantitative claim in a phenomenon doc should have a backing Python calculation.
   Run it and record the output in the document.

### Step 2 — Audit a Random Document

**Goal:** Every document in the repository should be reviewed and updated periodically.
Nothing should fall through the cracks. Audit scope is the full repository — not just
`foundations/` and `phenomena/`, but also `equations/`, `README.md`, `ISSUES.md`,
`comparisons/`, `practical_applications/`, `current_state.md`, and any other file.
Select any document at random from anywhere in the project.

1. Select any document in the repository at random — conceptual documents in `foundations/`
   or `phenomena/`, equation modules in `equations/`, overview and tracker files
   (`README.md`, `ISSUES.md`, `current_state.md`, `OVERVIEW.md`), comparison documents
   in `comparisons/`, practical application entries in `practical_applications/`, or any
   other file in the project tree.
2. Read it and the corresponding equation modules (if any).
3. Check: does the document accurately reflect the current state of the model?
   Flag any of these:
   - Claims that go beyond what equations currently show
   - Language that does not match the DFC framework (forbidden phrases, anthropomorphic agency)
   - Derivation steps marked as "established" that are actually assumptions or postulates
   - Tier assignments inconsistent with the Scientific Merit Criteria (e.g., a Tier 3
     item called a prediction, or a retracted result still labeled as derived)
   - Cross-references that are stale, missing, or point to documents that have since
     been updated in ways that change the cross-ref's meaning
   - Completeness estimates or confidence statements that have not been updated to
     reflect results from later cycles (e.g., an "OPEN" item that was resolved in a
     later cycle still marked open)
   - New results from later cycles that should be reflected here but are not
   - Mathematical relations appearing in prose without a prior natural-language statement
     (per the Mathematical Communication Standard)
4. Update the document to match the current state of the model.

### Step 3 — Audit a Random Equation Module

1. Select an equation module in `equations/` at random.
2. Run it. Check:
   - Does it actually produce the claimed outputs?
   - Are failures clearly labeled as failures (not quietly passed over)?
   - Are inputs vs. predictions clearly distinguished?
   - Are all free parameters identified as such?
3. Update the module to reflect any discovered discrepancies or failures.
4. Update the corresponding conceptual docs if the equation reveals a gap or failure.

### Step 4 — Propagate Updates

After any new document or any audit:
1. Update `current_state.md` if a new strength, weakness, or audit result warrants it.
2. Update `MEMORY.md` if any project-level facts have changed.
3. Check whether any linked documents need updating.
4. If the cycle produced a significant change (new verified prediction, resolved bottleneck,
   major discovered failure), update the Completeness Estimate above and in `README.md`.

Then return to Step 1.

---

## Document Standards

### Conceptual Documents (foundations/, phenomena/)

- The **One-Sentence Synthesis** must state the DFC account, not be a placeholder.
  It should be possible to read this single sentence and understand what DFC says.
- The **Consistency Checks** table must include at least one row marked ✗ if any
  prediction fails or is not yet derived. Honesty about failures is required.
- **Open Questions** must be specific and actionable — not "derive X" but "derive X
  by computing [specific integral/topology] using [specific approach]."
- Never mark something as "established" unless there is a completed equation or
  formal argument. Use "under derivation," "consistent but not derived," or
  "working description" for everything else.

### Equation Modules (equations/)

- Every module must be runnable: `python3 equations/module.py` produces output.
- Distinguish **inputs** (values taken from data) from **predictions** (values computed
  from DFC parameters). Label them clearly in output.
- If a prediction fails, print the failure prominently. Do not hide discrepancies in
  "close enough" rationale without justification.
- All modules should include a docstring explaining: (a) what physical question it
  addresses, (b) what the DFC mechanism is, (c) what the key references are.

---

## What Is Verified vs. Open

Always maintain this distinction explicitly. The model's credibility depends on it.

**Verified (numerically or formally):**
- τ_neutron = 878.4 s (0.1% match) — `equations/proton_stability.py`
- Spin-1/2: FR winding N = 1, BPST zero mode normalizable, J_min = 1/2, Jackiw-Rebbi
  residual ~ 10⁻⁶ — `equations/spin_zero_mode.py`
- m_μ/m_e = 206.77 from R/d ratio — `equations/mass_spectrum.py`
- Q = T₃ + Y/2 for all first-generation fermions — `phenomena/.../electroweak.md`
- H₀ = 67.26 km/s/Mpc (0.2% match) — `equations/cosmology.py`

**Known failures (not yet resolved):**
- τ mass from mass_spectrum.py: predicts 212 MeV, observed 1777 MeV (8.4× off)
- Neutrino depth spacing ratio: 1.34 vs observed 5.71
- Charm/strange quark masses: 15% below observed

**Correspondences (consistent but not derived):**
- D5 ↔ U(1), D6 ↔ SU(2), D7 ↔ SU(3) assignments
- V(φ) = −α/2 φ² + β/4 φ⁴ (postulated, not derived from D1); quartic coupling β ≈ 0.035 is a Tier 3 reference value — the γ = (16/3)√β inference (Cycle 32) was retracted in Cycle 48 (wrong E_kink formula); β constrained by kink width at D1 = Planck length and heuristic g² = 8πβ/3
- Weinberg angle sin²θ_W ≈ 0.231 (Route 3B gives 0.231 from equal-coupling initial condition + SM running; k_Y = 3/5 now derived from Dynkin normalization condition on SM matter content — no GUT needed; M_c(12) from SM running, not substrate parameters — remaining open item)

---

## Scientific Merit Criteria

This section defines the objective standards by which this project evaluates its own
scientific status. These criteria are permanent and apply at every stage of development.
They exist to distinguish genuine progress from apparent progress, and to keep the
project anchored to physics rather than to internal narrative consistency.

---

### Tier System for Claims

Every claim in this project is assigned to one of five tiers. The tier determines what
is required to consider the claim substantiated. **Tier assignment is not permanent** —
a claim moves up when additional derivation is completed.

---

**Tier 0 — Core Postulates** *(inputs; not derived; define the model)*

Tier 0 items are the starting assumptions of the model. They cannot be evaluated as
right or wrong in isolation — only their consequences can be tested. They must be stated
explicitly and kept minimal. Any postulate that can be derived from another within the
model should be demoted to a lower tier, because it was not a genuine starting assumption.

Current Tier 0 postulates:
1. There is one continuous self-compressing field. No pre-existing space, gauge group,
   or dimensional structure is assumed.
2. The field's self-interaction potential has the double-well form: the potential energy
   as a function of field amplitude equals negative one-half times a quadratic coupling
   times the amplitude squared, plus one-quarter times a quartic coupling times the
   amplitude to the fourth power. The quadratic coupling alpha and quartic coupling beta
   are free parameters of the model.
3. Bifurcation events — points at which the compressed field opens a new degree of
   freedom rather than compressing further — produce all structure observed as particles,
   forces, and spacetime.

Requirement to stay Tier 0: The postulate is stated as an assumption, not a derivation.
If a derivation of a Tier 0 item is found, it is promoted to Tier 1 or Tier 2, and the
list above is updated.

---

**Tier 1 — Structural Predictions** *(logical consequences of Tier 0; no quantitative free parameters)*

Tier 1 claims are qualitative or topological: they assert that a specific structure exists
or a specific symmetry holds, without requiring a numerical match to experiment. A Tier 1
claim is substantiated when: (a) the logical argument from Tier 0 to the claim is
written out completely, with no missing steps, and (b) the claim matches the observed
qualitative feature.

Current Tier 1 claims and their status:

| Claim | Logical basis | Status |
|---|---|---|
| Proton absolutely stable — no decay mode exists | Product topology U(1)×SU(2)×SU(3) has no path between baryon and lepton sectors | Argument written; no equation needed ✓ |
| Exactly three fermion generations | SU(3) fundamental representation has dimension three; no fourth generation is topologically available | Argument written; Cycle 35 ✓ |
| Photon is massless and propagates at c | Massless limit of Klein-Gordon field equation has linear (massless) dispersion: frequency is proportional to wavenumber | Derived from field equation ✓ |
| Exactly two photon polarization states | One angular degree of freedom (phase angle on a circle) has exactly two transverse projections | Structural argument written ✓ |
| Parity violation in weak force | Jackiw-Rebbi zero mode bound to a positively wound kink is inherently left-handed | Argument written; Cycle 41 ✓ |
| Spin-1/2 exists and is the minimum spin | Finkelstein-Rubinstein winding N=1 with Jackiw-Rebbi zero mode | Verified numerically; Cycle 33 ✓ |
| Space appears three-dimensional | Three apparent degrees of freedom emerge at D3 localization depth | Structural argument; not yet a derivation ✗ |
| Binary measurement outcomes | Two-sector topology of the substrate field (Z₂ configuration space) | Proved topologically; Cycle 36 ✓ |

---

**Tier 2 — Quantitative Predictions** *(numerical outputs computed from substrate parameters; compared to measured values)*

A Tier 2 claim is substantiated when all four conditions are met:
1. There is a runnable equation module that takes the substrate parameters as input and
   produces the claimed number as output.
2. The derivation chain from postulate to equation has no circular steps — the target
   quantity does not appear as an input anywhere in the chain.
3. The predicted value matches the observed value within 5% (or within the stated
   theoretical uncertainty for cases where the derivation itself introduces uncertainty).
4. The number of free parameters used in the derivation is explicitly stated.

Tier 2a — **Verified** (all four conditions met):

| Prediction | Equation module | Predicted | Observed | Error | Free params |
|---|---|---|---|---|---|
| Muon-to-electron mass ratio (206.77) | mass_spectrum.py | 206.77 | 206.77 | 0.0% | 2 (R, d) |
| Neutron lifetime (878 seconds) | proton_stability.py | 878.4 s | 877.8 s | 0.1% | 0 (imported rates) |
| Hubble constant (67 km/s/Mpc) | cosmology.py | 67.26 | 67.66 | 0.2% | 2 (Ω_m, Ω_Λ) |
| Higgs boson mass (125 GeV) | higgs_potential.py | 124.4 ± 3.7 GeV | 125.25 GeV | 0.7% | 1 (λ₀ boundary) |
| Weinberg angle (0.231) | weinberg_angle_rg.py | 0.2312 | 0.2312 | 0.01% | 1 (M_c from SM running) |
| Electromagnetic fine structure constant at the Z boson mass scale (1/128) | coupling_derivation.py | 1/129.6 | 1/127.9 | 1.3% | 1 (β; heuristic derivation) |
| Common gauge coupling at unification scale (0.543) | coupling_derivation.py | 0.5423 | 0.5443 | 0.4% | 1 (β; heuristic derivation) |
| Thomson scattering cross-section (6.65×10⁻²⁹ m²) | scattering_cross_sections.py | 6.368×10⁻²⁹ m² | 6.652×10⁻²⁹ m² | −4.3% | 1 (β; m_e from data) |
| W boson mass (80.38 GeV) | muon_lifetime.py | 79.67 GeV | 80.377 GeV | −0.88% | 2 (β; v=246 GeV from data) |
| Z boson mass (91.19 GeV) | muon_lifetime.py | 90.86 GeV | 91.1876 GeV | −0.36% | 2 (β; v=246 GeV from data) |
| Fermi constant G_F (1.166×10⁻⁵ GeV⁻²) | muon_lifetime.py | 1.168×10⁻⁵ GeV⁻² | 1.166×10⁻⁵ GeV⁻² | +0.18% | 2 (β; v=246 GeV from data) |
| Muon lifetime (2.197 μs) | muon_lifetime.py | 2.180 μs | 2.197 μs | −0.80% | 3 (β; v=246 GeV; m_μ from data) |

Tier 2b — **Failing** (equation exists, but prediction misses by more than 5%):

| Prediction | Module | Predicted | Observed | Error | Resolution status |
|---|---|---|---|---|---|
| Electron anomalous magnetic moment (leading Schwinger term) | anomalous_magnetic_moment.py | 0.001136 | 0.001160 | −2.01% | Within 5% but leading term only; same α_em systematic |
| Tau lepton mass | mass_spectrum.py | 212 MeV | 1777 MeV | 8.4× off | Unresolved |
| Neutrino mass hierarchy ratio | neutrino_masses.py | 1.34 | 5.71 | 4.3× off | Unresolved |
| Strong coupling constant at the Z boson mass scale | coupling_derivation.py | 0.105 | 0.1182 | 11% | M_c(D7) not derived from substrate |
| Charm and strange quark masses | quark_masses.py | 15% below observed | — | 15% | Unresolved |

---

**Tier 3 — Correspondences** *(consistent with observation; not yet derived from Tier 0)*

A Tier 3 claim is an assignment or structural choice that is consistent with observation
and has a plausible path to derivation, but has not been derived. Tier 3 items must be
labeled as "working hypothesis" in all documents. They must not be presented as derived
results. The goal of the project is to either promote Tier 3 items to Tier 2 (by
completing the derivation) or to discard them (if the derivation path closes).

Current Tier 3 items:

| Item | Why it is Tier 3 | Path to Tier 2 |
|---|---|---|
| D5 depth produces U(1) behavior | Consistent with Hopf S¹ correspondence, not derived from compression dynamics | Derive DOF count per bifurcation from substrate field equation (Route B) |
| D6 depth produces SU(2) behavior | Same as above for S³ | Same path |
| D7 depth produces SU(3) behavior | Same as above for S⁵; confinement argument supports termination | Same path plus formal confinement argument |
| Quartic coupling beta equals approximately 0.035 | Inferred from the energy fraction per bifurcation; not derived from a pre-substrate constraint | Derive beta from the condition that the substrate field equation admits a stable kink at the Planck scale |
| The double-well potential form V = -α/2 φ² + β/4 φ⁴ | Postulated; consistent with known physics of symmetry breaking | Derive from the self-interaction dynamics of a compressing one-dimensional field |

---

**Tier 4 — Claims Awaiting Resolution** *(stated but neither derived nor falsified)*

Tier 4 items are claims present in the documentation that have no supporting derivation
and no equation module. They are placeholders for future work, not results. They must be
labeled "open" in all documents.

Examples: derivation of Planck's constant from substrate; derivation of the cosmological
constant; derivation of matter-antimatter asymmetry; quark mass spectrum beyond
electron/muon; neutrino masses beyond qualitative correspondence.

---

### Criteria for Novel Scientific Contribution

The project makes a genuine novel scientific contribution if and only if it satisfies at
least one of the following four criteria. These are the standards a referee would apply.

**Criterion A — Derives a SM postulate without circular import:**
The model produces a quantity that the Standard Model takes as an unexplained input
parameter, and does so without importing that quantity (or an equivalent quantity) at
any step. The derivation chain is fully explicit.

Current candidates: gauge coupling from beta (heuristic; not yet rigorous); three
generations from SU(3) topology (structural; complete); proton stability from product
topology (structural; complete).

**Criterion B — Makes a prediction the SM cannot make:**
The model predicts a specific numerical value for a quantity that the Standard Model does
not predict (either because the SM has a free parameter there, or because the phenomenon
falls outside the SM's scope), and the prediction is testable in principle.

Current candidates: absolute proton stability (SM predicts only suppressed decay, not
zero rate; DFC predicts strictly zero from topology); the relationship between the quartic
coupling beta and the gauge coupling strength (if the holonomy derivation is made rigorous).

**Criterion C — Provides a structural explanation for a SM pattern:**
The model explains why a feature of the Standard Model has the form it does — not just
reproduces its numerical value, but identifies the structural reason. The explanation
must be specific enough to rule out alternatives.

Current candidates: why parity is violated in the weak force (chirality of the
Jackiw-Rebbi zero mode at D6 depths); why there are exactly three generations (SU(3)
fundamental representation dimension); why the gauge group is a product and not a simple
group (independent closure thresholds produce independent topological structures).

**Criterion D — Passes an independent consistency check:**
A quantity computed by two different paths within the model gives the same answer. The
agreement is not guaranteed by construction (i.e., the two paths use different inputs).

Current candidate: the common gauge coupling at the closure scale is obtained both from
SM running down from high energy and from the substrate formula using only beta. These
two paths agree to 0.4%. If the substrate derivation is made rigorous, this constitutes
a genuine internal consistency check.

---

### Completeness Milestones

The following milestones define what "scientifically complete" means at each phase. The
overall completeness estimate in the header of this document measures progress toward
Phase 5.

**Phase 1 — Structural coherence (~30%):** All Tier 1 claims have complete logical
arguments with no missing steps. No Tier 1 item is marked as "structural argument" when
an actual derivation exists or is straightforward. The qualitative structure of the model
is internally consistent.

**Phase 2 — Quantitative contact (~50%):** At least five Tier 2a predictions match
observation to within 5%, with complete derivation chains and explicitly stated free
parameters. The three most fundamental quantities — electromagnetic coupling, Weinberg
angle, and the Higgs mass — are all in Tier 2a.

**Phase 3 — Coupling sector complete (~70%):** All three force coupling constants
(electromagnetic, weak, strong) are derived from the substrate parameters to within 5%
with no free parameters beyond the two substrate couplings (alpha, beta). The D-depth
assignment mechanism (Tier 3 items for U(1), SU(2), SU(3)) has been promoted to Tier 2.

**Phase 4 — Parameter-free (~85%):** The substrate quartic coupling beta is derived from
a pre-substrate condition rather than inferred from data. The double-well potential form
is derived from compression dynamics rather than postulated. The number of free parameters
reaches zero beyond the Planck-scale normalization.

**Phase 5 — Scientifically rigorous (~95%):** All Tier 4 failures are either resolved
(promoted to Tier 2b or better) or formally shown to require extension beyond the current
model. At least one prediction satisfies Criterion A or B above — that is, the model
makes a genuinely new statement about physics that could in principle be tested and has
not been made by any other theory.

---

### Evaluation Checklist for New Derivations

When a new derivation is completed and a claim is being promoted up the tier ladder,
apply this checklist before updating the tier assignment:

- [ ] Can the derivation be stated in natural language without any symbol that cannot be
      defined in words?
- [ ] Does the derivation chain start only from Tier 0 postulates and previously
      substantiated results?
- [ ] Is the target quantity absent from the right-hand side of every step in the
      derivation?
- [ ] Is there a runnable equation module that produces the predicted number?
- [ ] Is the percent discrepancy from observation computed and printed by the module?
- [ ] Is the number of free parameters explicitly counted and printed?
- [ ] Is there at least one Consistency Check table row that tests the result against an
      independent check (not just against the same data used to calibrate the model)?

If any item is unchecked, the claim remains at its current tier until the item is
satisfied.

---

## File Structure Reference

```
DCmodel/
├── CLAUDE.md                  ← this file
├── current_state.md           ← living review document, update periodically
├── foundations/               ← core model documents
│   ├── substrate.md           ← φ field, V(φ), kink solutions
│   ├── dimensional_stack.md   ← D1-D7 structure
│   ├── three_generations.md   ← three-generation count from D6 topology
│   ├── spin_emergence.md      ← FR + Jackiw-Rebbi derivation of spin-1/2
│   ├── mass_hierarchy.md      ← dimple + global scale for lepton masses
│   └── higgs_geometry.md      ← S³ squashing as Higgs mechanism
├── phenomena/
│   ├── electromagnetism/      ← EM, electric charge, light
│   ├── particle_physics/
│   │   ├── forces/            ← strong, weak, electroweak
│   │   └── particles/         ← electron, quarks, neutrinos, ...
│   ├── quantum/               ← QM, measurement, interference
│   └── cosmology/             ← expansion, dark matter, baryogenesis
└── equations/                 ← Python modules, all runnable
    ├── proton_stability.py    ← verified
    ├── spin_zero_mode.py      ← verified
    ├── mass_spectrum.py       ← tau mass fails
    ├── quark_masses.py        ← c/s 15% off
    ├── neutrino_masses.py     ← depth ratio off
    └── cosmology.py           ← largely consistent
```
