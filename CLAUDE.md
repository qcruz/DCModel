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
Current estimate: ~25.5%  (viability: ~38.5%, mathematical rigor: ~21.5%)
Key bottleneck: D-depth assignment mechanism (Route B Hopf fibration — DOF count derivation open); rigorous proof of r_U1/λ = 3/(4β) from substrate field equation; Born rule for position from Kramers escape rate
Next milestone: Derive r_U1/λ = 3/(4β) formally from D5 phase boundary condition; derive β from pre-substrate principle (sole remaining free parameter in coupling chain)
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

### Step 2 — Audit a Random Conceptual Document

1. Select a conceptual document (anything in `foundations/` or `phenomena/`) at random.
2. Read it and the corresponding equation modules.
3. Check: do the descriptions and analogies accurately reflect what the math says?
   Flag any of these:
   - Claims that go beyond what equations currently show
   - Language that doesn't match the DFC framework
   - Forbidden anthropomorphic language
   - Derivation steps marked as "established" that are actually assumptions
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
- V(φ) = −α/2 φ² + β/4 φ⁴ (postulated, not derived from D1); quartic coupling β ≈ 0.035 inferred from γ_space via γ = (16/3)√β
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

Tier 2b — **Failing** (equation exists, but prediction misses by more than 5%):

| Prediction | Module | Predicted | Observed | Error | Resolution status |
|---|---|---|---|---|---|
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
