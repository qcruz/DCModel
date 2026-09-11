# DFC Model — Claude Instructions

This project is an exploratory theoretical physics model called **Dimensional Folding
Compression (DFC)**. It investigates what emerges from a single continuous scalar field
with a double-well potential V(φ) = −α/2 φ² + β/4 φ⁴ undergoing self-compression.
The field pulls inward on itself, driving toward a near-1D state through compression
and bifurcation. Self-closing bifurcation events form topological structures that
correspond to observed particles and forces. The project explores the consequences of
this setup — no pre-existing spatial dimensions, gauge groups, or separate forces are
assumed. What appears as "3D space," "gauge structure," or "three distinct forces" is
the downstream appearance of the substrate's fold topology at different compression depths.

**Project tone:** This is an exploratory project. Frame findings as interesting results,
not claims of truth. Let numbers speak for themselves. Do not be defensive or grandiose.
Avoid "Why should you take this seriously?" framing — just present what was found.

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
| "requires 3 spatial dimensions" | "produces three apparent spatial degrees of freedom" |
| "the forces were unified at high energy" | "the forces are always fold interactions of one object; at high compression, their topological distinctions diminish" |
| "unified force" (GUT sense) | "single substrate" or "one object" |
| "the three forces" (as fundamentally separate) | "the three closure-topology interaction regimes" or "fold interactions at D5, D6, D7 depths" |

**Parameter language rule:**

Do not call out "zero free parameters" or "0 free params" in predictions, commit messages,
or documentation. DFC predictions are parameter-free by default — only note when external
parameters ARE used (e.g., "uses m_t, m_H as inputs" or "inherits Λ_QCD from SM running").
The absence of free parameters is the norm, not the exception, and does not need flagging.

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
   The correct framing: the forces were never separate — they are always the same fold
   interactions, appearing topologically distinct because they closed at different compression
   thresholds. "Unified" is permitted and correct when it refers to the ontological unity of
   the substrate (one object). It is forbidden when it implies gauge-group unification.

---

## Mathematical Communication Standard

This rule applies to all conceptual documents (`foundations/`, `phenomena/`). It does **not**
apply to equation modules (`equations/`) or formal equation display blocks within docs.

**Rule:** Every mathematical relationship introduced in prose must first be stated in plain
natural language. The symbolic form may follow immediately in a display block as the formal
reference. A symbol expression alone — appearing in running text without a natural language
statement — is never sufficient.

**Examples:**

Bad: "ω = ck, so E = ℏω = hν."

Good: "In the massless limit, the angular frequency of a wave is proportional to its
wavenumber — the spatial rate of oscillation — with the speed of light as the
proportionality constant."

Bad: "g² = 8πβ/3 gives the gauge coupling."

Good: "The square of the gauge coupling constant equals eight times pi times the substrate
quartic self-coupling, divided by three."

**Enforcement:** When auditing any conceptual document, check that every equation appearing
in prose was preceded by a natural language statement. If not, add the natural language statement.

---

## Development Cycle

> ### ⚠ MANDATORY FINAL STEP — EVERY CYCLE WITHOUT EXCEPTION
> **After every commit, run `git push` before the cycle is considered complete.**
> A cycle is NOT finished until the remote is updated. This applies to every "continue"
> invocation, no matter how small the change. The last command of every cycle must be
> `git push` and you must confirm the remote accepted it (look for the branch update line
> in the output, e.g. `main -> main`). If you reach the end of a cycle and have not pushed,
> do not return to Step 1 — push first.

> ### ⚠ KEEP CYCLES SHORT — MANDATORY SCOPE CONSTRAINT
> **Each "continue" invocation must accomplish exactly ONE focused task.**
> Do not combine multiple steps into a single session. One new equation module OR one
> document audit OR one tracking update — not all three. If Step 1 produces a new
> equation file, commit and push immediately after running it, before doing Steps 2-5.
> Steps 2-5 are each separate optional follow-ups, not a required bundle. A short cycle
> that completes cleanly is always better than a long cycle that risks context overflow
> or incomplete execution. When in doubt, stop earlier and push.

### Current Development Phase: PREDICTION MAXIMIZATION + INFRASTRUCTURE

**Priority:** Maximize testable predictions from V(φ) while building robust simulation
and modularity infrastructure. The model's credibility rests on concrete, quantitative
predictions compared against observation, supported by numerical demonstrations that
the claimed dynamics actually emerge from V(φ).

**Hierarchy of value (highest first):**
1. **New testable predictions** — compute a number from DFC parameters that can be compared
   to experiment (e.g., cosmological observables, particle masses, cross-sections)
2. **Improving existing predictions** — tighten derivation chains, reduce tier levels
   (T3→T2a, T2a→T1), fix known failures
3. **Simulations and numerical demonstrations** — build the simulation library showing
   that V(φ) dynamics produce the claimed behaviors (kink scattering, oscillons, gauge
   emergence, Kibble-Zurek, compression cascades). These are Tier 1 structural proofs
4. **Mathematical exploration** — freeform manipulation of DFC constants and identities
   to discover new connections, uniqueness theorems, and blocked-item workarounds
5. **Modularity and infrastructure** — migrate equation modules to `dfc_core.py` shared
   constants, maintain `run_all_tests.py` test suite, keep equations/README.md current
6. **Structural exploration** — D4 gravity gap, metric emergence, etc. — valuable but
   should serve prediction goals, not be an end in itself

**All task priorities are tracked in `ROADMAP.md`.** That document is the single
source of truth for what to do next. See "How continue Works" below.

Repeat this cycle indefinitely:

### Completeness Estimate (running)

```
--- DFC MODEL (primary project) ---
Current estimate: ~80%  (viability: ~87%, mathematical rigor: ~73%)

--- CLAY PRIZE (separate sub-project — test case for DFC mathematical basis) ---
Clay Prize structural completeness: ~95%
  (How complete the DFC argument covering all 5 Jaffe-Witten criteria is at T2a level)
Clay Prize rigorous proof standard: ~99%
  Proof document: ym_clay_proof.tex (C322, 12 citations, 5 lemmas, Main Theorem).
  All 7/7 Jaffe-Witten criteria T1 or cited theorem. ZERO T2a on critical path.
  All critical gaps CLOSED: P1 (C314), P2 (C300), P3 (C298), P4 (C299), P5 (C303+C304),
  Assumption A (C320). Sole remaining gap: peer review.
  Full cycle-by-cycle Clay history: see push_history.md and yang_mills_clay.md.
  See yang_mills_clay.md §Path to Full Rigor)
Clay Prize Confidence Score (CPC): ~60%
  (P(DFC framework → valid Jaffe-Witten proof candidate | continued work))
  CPC is NOT the progress %; it measures reachability of the destination, not distance traveled.
  Key CPC swing events: SP1 Balaban closes (+15% — TRIGGERED C203), hard obstruction found (−15%),
  SU(N) generality issue (−10%), c_gauge explicit T1 (+5%).
  SU(N) generality confirmed (+10% — TRIGGERED C216): SP1+SP2 T2a all N≥2 via monotonicity.

NOTE: The Clay Prize is tracked independently from the DFC model. Structural completeness
  measures how well DFC covers the JW criteria. Rigorous proof standard measures proximity
  to a Clay-accepted mathematical proof (requires T1 or cited theorem, not T2a).
  OBJECTIVE (C297): Achieve a fully rigorous mathematical proof before any DFC publication.
  No paper or broader publication moves forward until the rigorous proof is complete.

Key milestones: D4 gravity κ=0.511 (+2.1%, was +158%; RS standard + M₅³=1/2 self-consistency, C580).
  α_em(0) gap T4→T3 (one-loop shape mode closes 106.6% of gap, 6.6% overshoot, C579).
  α_s closed 0.006% (C144). v=247.83 GeV T2a (C145). m_τ Koide T2a (C146).
  θ=0 T2a (C147). β T1 candidate (C173). α=∛18 T2a (C172).
  Full Clay Prize construction chain: SP1-SP5 all T2a/T3, no T4 gaps (C178-C322).
  S_kink×α_D5=1 T1 (C171). α=∛18 T2a (C172).

Recent cycles (full history: push_history.md):
| Date | Cycle | Summary | Viability | Rigor | Overall |
|---|---|---|---|---|---|
| 2026-09-11 | 584 | P7: t4_stagnation_audit.md NEW — 10 T4 items: 4 progressing, 3 flagged stalled (top mass, ℏ, thresholds), CKM escalated to P3 | 87% | 73% | ~80% |
| 2026-09-11 | 583 | P6: educational/34_electroweak_precision.md NEW — 10 EW predictions, all T2a; error budget from M_Z −0.36% | 87% | 73% | ~80% |
| 2026-09-11 | 582 | P5: skyrme_e_from_vphi.py NEW (5/9) — e=1/√β=√(9π)=5.317 (−2.4% from ANW 5.45); also e=m_σ/f_π=3π/2=4.71; T3 | 87% | 73% | ~80% |
| 2026-09-11 | 581 | P4: sigma_mass_in_medium.py Part G (19/20) — pionic RPA (−2.2%) + tensor (−1.0%) → a=0.537 fm (−0.5%); 97% of 20% gap closed; T2b | 87% | 73% | ~80% |
| 2026-09-11 | 580 | P3: kink_self_gravity.py Part I (14/14) — RS standard + M₅³=1/2 self-consistency → κ=0.5107 (+2.1%); 74× improvement over C576 (+158%); D4 spoke T3→T2a | 87% | 73% | ~80% |
| 2026-09-11 | 579 | P2: alpha_em_gap_exploration.py Part G (9/11) — ONE-LOOP SHAPE MODE closes 106.6% of gap (6.6% overshoot); T4→T3 | 87% | 73% | ~80% |
| 2026-09-11 | 578 | P1: anomalous_magnetic_moment.py Part G (14/15) — gap-closed→1.1σ (lattice); had VP 10σ bottleneck; Fermilab 2023; ROADMAP MC1-MC4 prioritized | 87% | 73% | ~80% |
| 2026-09-11 | 571 | P4: nucleon_magnetic_moments.py Part J (17/21) — Δ-pole 0.5% of κS; NLO ChPT RULED OUT for g_A/32 (C_ct=124%) | 87% | 73% | ~80% |
| 2026-09-11 | 570 | P3: d4_thick_wall_bvp.py Part H (16/0) — graviton zero-mode reduces κ 48.7% (2.04→1.29); M₅³≈4βπ=4/9 (−9.2%) | 87% | 73% | ~80% |
| 2026-09-11 | 569 | P2: alpha_em_gap_exploration.py Part F (6/8) — proper threshold: Casimir 5%, S³ curvature 10.3%, combined 5.3%; f=6.94 unmatched | 87% | 73% | ~80% |
| 2026-09-11 | 568 | P1: alpha_em_gap_exploration.py NEW (5/6) — 3 viable paths (C2 topological, C3 k_Y, C5 g_eff loop), all overshoot 15-23× | 87% | 73% | ~80% |
| 2026-09-11 | 577 | Doc: educational/33_kink_self_gravity.md NEW — how kinks attract, complete gravity chain, force hierarchy, 8 sections | 87% | 73% | ~80% |
| 2026-09-11 | 576 | D4: kink_self_gravity.py NEW (11/11) — complete chain V(φ)→G_N; confinement + attraction from same A(y); κ=1.29 (+158%) | 87% | 73% | ~80% |
| 2026-09-11 | 575 | P8: kink_gravity_gradient.py NEW (10/10) — a=-(3/(2α))dα/dx to 0.6%, a∝ε 1.1%, C_grav=1.49, parabolic 0.7% | 87% | 73% | ~80% |
| 2026-09-11 | 574 | P7: literature_reframing.md Cluster B audit — KK (4/2/1), Skyrme (6/1/1), JR (8/0/1); JR strongest framework; topology > geometry pattern | 87% | 73% | ~80% |
| 2026-09-11 | 573 | P6: 06_predictions.md updated — +3 structural sections (U(1) emergence, C₂=N_c, analog gravity), +6 summary entries, Koide T1 upgrade, κ→1.29 | 87% | 73% | ~80% |
| 2026-09-11 | 572 | P5: ssh_fractional_charge.py NEW (12/12) — SSH gives 1/2 not 1/3; quark charges from Z₃ center vortex; Kitaev table D5/D6/D7 | 87% | 73% | ~80% |
| 2026-09-10 | 567 | P8: multi_kink_gas_dynamics.py NEW (9/9) — 4 KA pairs annihilate, pair creation from radiation, Q=0 exact, virial 1.25 | 87% | 73% | ~80% |
| 2026-09-10 | 566 | P7: free_parameter_audit.py NEW (5/6) — 15 T2a predictions, 4 DFC geometric params, Ratio 3.0; only g_eff²=8/27 truly 0-param | 87% | 73% | ~80% |
| 2026-09-10 | 565 | P6: ROADMAP comprehensive review — removed 12 resolved/done items, consolidated 7 duplicates, added continuous review item | 87% | 73% | ~80% |
| 2026-09-10 | 564 | P5: analog_gravity_dispersion.py NEW (7/9) — PT reflectionless T1, superluminal exp(-πkξ), Hawking robust | 87% | 73% | ~80% |
| 2026-09-10 | 563 | P4: light_nuclei_binding.py Part E (5/12) — NJL sigma test: no binding any m_σ, even g_ω=0; root cause = OBE too weak | 87% | 73% | ~80% |
| 2026-09-09 | 562 | P3: koide_phase_coupling.py Part F (4/4) — 5D Yukawa overlap verified: profiles cancel exactly, step 4d T2a→T1+structural | 87% | 73% | ~80% |
| 2026-09-09 | 561 | P2: delta_n_splitting.py Part F (12/14) — empirical intercepts: N ground α₀=−0.256 matches DFC; T3→T2b BLOCKED on junction penalty | 87% | 73% | ~80% |
| 2026-09-09 | 560 | P1: nuclear_kink_nonlinear_eos.py Part G (16/18) — NJL→Walecka: C₂(NJL)/C₂(NL3)=0.87, gap closes 14×→1.15× | 87% | 73% | ~80% |
| 2026-09-09 | 559 | P8: tachyonic_complexification_sim.py NEW (11/11) — U(1) emerges: 10381× amplification, Δθ=π | 87% | 73% | ~80% |
| 2026-09-09 | 558 | P7: critical_review_uniqueness.md NEW — 8/18 predictions genuinely unique, 6 standard physics | 87% | 73% | ~80% |
| 2026-09-09 | 557 | P6: 06_predictions.md updated — +5 entries (Δm NJL, DM σ_SI, DM T_RH, Li-7, JR Chern) | 87% | 73% | ~80% |
| 2026-09-09 | 556 | P5: quantum_hall_coupling_quantization.py NEW (13/13) — gauge GROUP topological, COUPLING algebraic | 87% | 73% | ~80% |
| 2026-09-09 | 555 | P4: bbn_predictions.py Part H — 6 Li-7 mechanisms ruled out, DFC shift +0.009% vs needed 66% | 87% | 73% | ~80% |
| 2026-09-09 | 554 | P3: dark_matter_relic_abundance.py NEW (14/15) — grav freeze-in T_RH=3e17 too high, KZ 10⁷× over | 87% | 73% | ~80% |
| 2026-09-09 | 553 | P2: CLAUDE.md comprehensive cleanup — 6 stale sections updated | 87% | 73% | ~80% |
| 2026-09-09 | 552 | P1: proton_neutron_mass_difference.py Part G — NJL isovector charge, C_QCD=0.87 (+75% vs GL) | 87% | 73% | ~80% |
| 2026-09-09 | 551 | P8: oscillon_breather_formation.py NEW (14/14) — meson analogue, Q=4313, ω=0.75m_σ | 87% | 73% | ~80% |
| 2026-09-09 | 550 | P7: critical_review_blind_spots.md NEW — 18 blind spots, 8 fundamental, 6 contingent | 87% | 73% | ~80% |
| 2026-09-09 | 549 | P6: 06_predictions.md updated — M0 T2b, r_p T2a, κ_GL=3/2 T1, η_B T4 | 87% | 73% | ~80% |
| 2026-09-09 | 548 | P5: bcs_gap_lambda_qcd.py NEW (7/10) — NJL gap eq, κ_GL=3/2 Type II T1 | 87% | 73% | ~80% |
| 2026-09-09 | 547 | P4: sigma_mass_in_medium.py Part F — Fock correction, diffuseness +2.8% (was +8.1%) | 87% | 73% | ~80% |
| 2026-09-09 | 546 | P3: baryon_asymmetry_magnitude.py NEW (14/15) — η_B 184× overshoot, T4 | 87% | 73% | ~80% |
| 2026-09-09 | 545 | P2: proton_charge_radius_dfc.py Part G — VMD pion cloud, r_p=0.809 fm (−3.8%, T2a) | 87% | 73% | ~80% |
| 2026-09-08 | 544 | P1: light_quark_mass_derivation.py Part L — 2-loop downgrades M0 T2a→T2b (+24%) | 87% | 73% | ~80% |
| 2026-09-08 | 543 | P8: poschl_teller_spectrum.py FIXED (19/19) — shape mode 0.0005%, mass gap, eigenfunctions | 87% | 73% | ~80% |
| 2026-09-08 | 542 | Infra: kink_antikink_annihilation.py NEW (16/16) — resonance windows, E=mc² as theorem | 87% | 73% | ~80% |
| 2026-09-08 | 541 | Infra: run_all_tests.py NEW — 397 modules, 2797 PASS, 96.6% pass rate | 87% | 73% | ~80% |
| 2026-09-08 | 540 | Infra: dfc_core.py + README.md NEW — shared constants, recompute() for alt frameworks | 87% | 73% | ~80% |

Next milestone: prove structural identity A−B = ln(1/α_em(0)) algebraically (Tier 4→1).

Model Reconcilability Risk Score (MRRS) — see reconcilability_risk.md for full analysis:
  Core gauge/coupling sector:      20%
  Full SM reproduction:            48%
  Complete theory (SM+gravity+QM): 72%
```

**After every push:** Update the estimate in THREE places every cycle:
1. The `Current estimate:` line in the code block above (this file)
2. The `Current status:` line at the top of `README.md` (line ~9)
3. The `## Mathematical Completeness Estimate` section in `README.md` (~line 191)

**Clay Prize tracking — update when a swing event occurs (not every cycle):**
- `Clay Prize progress:` and `Clay Prize Confidence Score (CPC):` lines above (this file)
- `Overall Clay challenge progress:` and `Clay Prize Confidence Score (CPC):` in `README.md`
- CPC changes only on: SP1 Balaban closes (±15%), hard obstruction found (−15%), SU(N) generality confirmed/blocked (±10%), c_gauge explicit (±5%), or other significant structural shift.
- Progress % changes every Clay cycle.

All three must stay in sync. The estimate has two components:
- **Viability** (~25% baseline): increases when new structural accounts are added, known
  failures are resolved, or predictions are confirmed by data.
- **Mathematical rigor** (~8% baseline): increases only when actual derivations are
  completed. Structural descriptions do not move rigor.

---

### ⭐ PRIMARY OBJECTIVES

The Yang-Mills mass gap proof is considered **internally complete** as of Cycle 322
(`equations/ym_clay_proof.tex`, 12 cited references, no T2a on critical path).
The proof document is available for external submission when ready. No further
Yang-Mills cycles are planned unless a substantive mathematical issue is discovered.

The project now returns to its broader mandate: **developing the DFC model as a
complete, rigorous, and communicable physical theory.** Four parallel tracks run
each cycle — choose whichever is most tractable given current project state:

---

**Track A — Mathematical Formalization**

Deepen and tighten the DFC mathematical foundations. Every quantitative claim in
`foundations/` and `phenomena/` should eventually be backed by a verified equation
module in `equations/`. Priority areas:

- **α_em(0) identity**: prove A−B = ln(1/α_em(0)) algebraically (Tier 4→T1; Cycle 139)
- **Strong CP**: formal D7 dynamics → θ̄=0 selection (Cycles 147, 156–157)
- **Quark mass matrix phase**: arg(det M_q)=0 from D6/D7 interface (Cycle 153)
- **Neutrino mass hierarchy**: m₃/m₂ ratio −8.3% gap (Cycles 165, 205)
- **Hadronic VP**: δ(Δα)^{NP}=0.00102 from D7 confinement (Cycle 158)
- Any foundation or phenomenon document whose equation backing is missing or T3/T4

Standard: prefer upgrading T3→T2a→T1 on existing derivations over adding new T3 claims.

---

**Track B — Educational Development**

Build a complete, standalone educational series for DFC. Modules 00–32 exist.
Continue with new modules as topics arise from completed derivations.

```
educational/
├── 00_overview.md              ← what DFC is
├── 01–05                       ← substrate, compression, depth map, forces, particles
├── 06_predictions.md           ← master prediction scorecard (nuclear + cosmological)
├── 07_open_questions.md        ← honest gaps
├── 08_mathematics.md           ← formal mathematical structure
├── 09–11                       ← I₄ Casimir, cascade uniqueness, 36π topology
├── 12–14                       ← substrate topology, mass from compression, spacetime emergence
├── 14b_localization_deep_dive.md
├── 15_dark_matter.md           ← m_DM=35.6 keV, WDM predictions
├── 16_cosmology.md             ← Λ, BBN, CMB, BAO predictions
├── 17_quantum_mechanics.md     ← measurement, interference from fold perspective
├── 18_open_problems.md         ← honest map of what remains underived
├── 19_bell_inequalities.md     ← Bell correlations from substrate connectivity
├── 20_nuclear_physics.md       ← Walecka model, nuclear saturation
├── 21–25                       ← neutrinos, Yang-Mills proof, couplings, strong CP, N=126 shell
├── 26_cosmological_constant.md ← w_Λ=−0.992, EOS
├── 26_nuclear_saturation.md    ← Walecka saturation details
├── 27_theta23_z3_mechanism.md  ← atmospheric mixing from Z₃ holonomy
├── 28_gravity_gap.md           ← D4 gravity gap analysis (15 modules)
├── 29_mathematical_exploration.md ← freeform math discoveries
├── 30_hadron_spectroscopy.md   ← meson/baryon mass predictions
├── 31_proton_spin_puzzle.md    ← spin crisis from Jackiw-Rebbi perspective
├── 32_depth_bifurcation.md     ← depth bifurcation dynamics
├── 33_kink_self_gravity.md    ← how kinks attract: V(φ) → gravity
└── 34_electroweak_precision.md ← 10 EW predictions, error budget
```

Rules: plain English first, equations second; Tier-honest; 500–1500 words per module;
self-contained (readable without reading other modules).

**Continual check:** When concrete high-confidence derivations, connections, or predictions
are completed and no existing educational module covers the topic, create a new module.
This check runs every documentation cycle (P6) — review recent completed items and
equation modules to identify topics deserving their own educational doc.

---

**Track C — Practical Applications and Predictions**

Derive engineering-relevant limits and falsifiable predictions from verified DFC results.
Each entry in `practical_applications/` should follow the format in `OVERVIEW.md`.

Priority topics:
- Absolute energy density limits from kink width ξ (T1 structural)
- Communication speed limits from substrate propagation
- Precision measurement predictions: g−2 electron/muon from DFC α_em chain
- What DFC predicts for upcoming experiments (LHC Run 4, CMB-S4, etc.)
- Absence predictions: no axion (T2a), no proton decay (T1), no SUSY (T3)

---

**Track D — New Open Problem Exploration**

Identify a significant open problem in mathematics or physics that DFC can address
as a framework, analogous to how Yang-Mills was addressed. The test is not whether
DFC *solves* the problem immediately, but whether it provides a *novel structural
angle* — a new connection that existing approaches lack.

**Candidate problems to evaluate** (spend one cycle on each to assess viability):

| Problem | DFC angle | Status |
|---|---|---|
| Navier-Stokes regularity (Clay) | Substrate field equation □φ=V'(φ) as a nonlinear wave; kink turbulence | Explore |
| Baryon asymmetry | D6/D7 CP-phase asymmetry → matter dominance | Explored C546: η_B 184× overshoot (T4) |
| Dark matter identity | Stable kink configurations at intermediate depths | Explored: m_DM=35.6 keV (T4) |
| Cosmological constant problem | Vacuum energy from substrate compression depth | Explored: Λ −3.5% (T3) |
| Proton spin crisis | Spin from Jackiw-Rebbi zero modes vs. parton contribution | Explored C477: Δq=0.30 (−28%, T3) |
| Quantum gravity / Planck scale | D4 inertia → G_N; Planck scale from ξ≈l_Pl | Explored C366–C408: gravity gap open |
| Proton-neutron mass difference | NJL isovector charge → δM_QCD | Active C552: Route G1 +17% (T2b) |

For each: write a one-page structural argument (`foundations/new_problem_NAME.md`),
identify what DFC predicts, identify the key T2a→T1 upgrade path, and record
honestly where DFC has nothing new to say vs. existing approaches.

---

**Track E — Freeform Mathematical Exploration (core interactive activity)**

A discovery-oriented activity: take DFC-derived identities, constants, and relations
and subject them to random interesting mathematical transformations to see if new
structure emerges. This is a **core interactive activity of the model going forward** —
not supplementary, but a primary engine for discovering new connections.

The workspace is `equations/freeform_math_exploration.py`. Each session may add new
exploration sections. Techniques include:

- **Continued fractions** of DFC constants (α, κ, g_eff, S_kink, etc.)
- **Modular arithmetic** — what primes factor DFC integers? What residues appear?
- **Algebraic identities** — products, ratios, sums of DFC parameters; look for
  unexpected simplifications or integer relationships
- **Number theory** — factorizations, discriminants, uniqueness theorems
- **Exponential/log transformations** — exp(−S_inst), ln(α), etc.
- **Trigonometric forms** — DFC angles (Weinberg, Z₃ center, θ₂₃)
- **Mass ratio analysis** — generation scaling factor κ candidates
- **Decomposition of known results** — e.g., cosmological exponent into substrate terms

**Key findings so far (C417):**
- b₀ = N_c² + Q_top = 11 is UNIQUE to N_c = 3 (discriminant = 46² = 2116)
- I₄ × Q_top × N_Hopf = 24 = 4!
- All key DFC fractions use only primes {2, 3}
- (3√2)^(2/3) = 18^(1/3) = α (BPS saturation)
- Cosmological exponent = N_Hopf × π × (3π + 1/2) + α

When a freeform exploration yields a result that looks structurally significant
(e.g., a new uniqueness theorem, an unexpected identity), promote it to a proper
equation module in `equations/` for formal verification.

**Feed blocked items into exploration:** When working on a ROADMAP item that is
blocked (e.g., a derivation that can't proceed, a formula that doesn't match),
add the relevant equations, parameters, and target values as new exploration
candidates in `equations/freeform_math_exploration.py`. Freeform manipulation
of blocked quantities may reveal relationships useful for later development.

---

---

### How "continue" Works

**`ROADMAP.md` is the single source of truth for what to do next.**

When the user says "continue":
1. Open `ROADMAP.md`.
2. **Cycle through tiers in order.** Check the `Last tier worked:` marker at the top
   of ROADMAP.md. Pick an item from the NEXT tier (P1→P2→P3→P4→P5→P6→P7→P8→P1→...).
   **Within each tier, always work the FIRST bullet point item.** After completing
   work on an item, move it to the BOTTOM of that tier's bullet list. This ensures
   systematic coverage of all items rather than random selection.
   If the next tier has no actionable items, spend the cycle researching that tier
   and adding new actionable items to ROADMAP.md.
   After completing the task, update the `Last tier worked:` marker to the tier you just did.
3. Do ONE focused task from that item (one equation module, one document, one test).
   **Never skip an item because it is difficult.** Always attempt to make incremental
   progress. Ruling out incorrect approaches, documenting blockers in more detail,
   outlining the specific steps needed, and narrowing the solution space are all
   valid and valuable progress. A cycle that identifies three wrong paths and clarifies
   what remains is a successful cycle.
4. Update `ROADMAP.md`: remove completed items from the active lists. Add new items
   whenever they come up. Keep bullet points short — detailed notes go in equation
   modules, `ISSUES.md`, or `push_history.md`, not in ROADMAP.
5. Update `push_history.md` with the cycle entry.
6. Commit all changed files and run `git push`. Confirm `main -> main`.

A cycle is NOT finished until the remote is updated. One sub-step per cycle.
Do not combine multiple items. Short cycles that complete cleanly are always better
than long cycles that risk context overflow.

**Educational summary (MANDATORY end of every session):** After the final push of
a session, write a short plain-English explanation of what was accomplished and why
it matters. This should be 3-8 sentences aimed at building the user's deep understanding
of the model over time. Cover: what physical question was addressed, what the DFC
mechanism is, what the key numerical result was, and what it connects to. Avoid jargon
where possible; when technical terms are unavoidable, define them inline. These summaries
accumulate into a running education — each one should teach something new about DFC.
**Include a document update list:** End every summary with a brief list of all files
that were created or modified in the cycle, with a one-line note of what changed in each.
Example format:
- `equations/new_module.py` — NEW, 14/14 PASS
- `ROADMAP.md` — added 2 items to P3, moved oscillon to Completed in P8
- `push_history.md` — C551 entry
- `CLAUDE.md` — C551 entry

**Cross-application sweep (end of every session):** Before the final push, review
what was accomplished in the session and ask: does this result suggest follow-on work
in other areas? Add new ROADMAP items for: parallel updates to similar files/modules,
cross-applications of the same technique to other predictions, scorecard or documentation
updates triggered by new results, and any newly-discovered connections or open questions.
The goal is to capture all downstream implications while they are fresh — not just the
item that was worked on.

**ROADMAP item management (MANDATORY every cycle):**
- **Add new items:** If a cycle reveals a new blocker, open question, or derivation
  target that is not already on ROADMAP, add it to the appropriate priority tier.
- **Promote recurring blockers:** If the same blocker appears across multiple items
  or keeps coming up in successive cycles, promote it to a higher priority tier.
  A blocker that blocks 3+ items should be at least P2; one that blocks 5+ should be P1.
- **Add new failure items to P4:** If a cycle produces a quantitative result that
  clearly fails (>10% error), add it to P4 Known Failures.
- The ROADMAP should grow organically as work reveals new connections. A cycle that
  discovers nothing new to add is rare — most work reveals at least one follow-on.

**Document review is a continuous part of the development cycle**, not a separate
maintenance task. It is a permanent item on ROADMAP P5 and will be selected when
the tier rotation reaches P5. When selected:
- Pick 2-4 random docs from `educational/`, `foundations/`, or `phenomena/`.
- Check for: stale tier labels, outdated file references, cycle numbers in public docs,
  language rule violations, factual inconsistencies with current model state.
- Fix issues found; add newly-discovered open items to ROADMAP.

**Other periodic tasks:**
- **Educational updates:** When a new prediction lands, update `educational/06_predictions.md`.
- **Practical applications:** Every ~5-10 cycles, consider adding an entry in
  `practical_applications/` following `OVERVIEW.md` format.

### Propagate Updates (MANDATORY every session)

After any new work:
1. Update `ROADMAP.md` with results (check off items, add cycle numbers,
   update the `Last updated:` line and `Last tier worked:` marker).
2. Update `push_history.md` with the cycle entry.
3. Update `current_state.md` if a new strength, weakness, or result warrants it.
4. **Update the Completeness Estimate in CLAUDE.md and README.md** (both places).
5. **Commit all changed files and run `git push`.** Confirm `main -> main`.

---

## Document Standards

### Conceptual Documents (foundations/, phenomena/, educational/)

- The **One-Sentence Synthesis** must state the DFC account, not be a placeholder.
- The **Consistency Checks** table must include at least one row marked ✗ if any
  prediction fails or is not yet derived. Honesty about failures is required.
- **Open Questions** must be specific and actionable.
- Never mark something as "established" unless there is a completed equation or
  formal argument.
- **No internal processing text.** Documents must read as finished, public-facing writing.
  Do not leave in: self-corrections mid-paragraph ("Wait —", "Actually,", "More directly:"),
  tentative drafting language ("Let me state this more carefully"), or live revision notes.
  Write the correct version; remove the path to it.
- **No cycle numbers in public documents.** Cycle tracking is for `push_history.md`,
  `ISSUES.md`, `yang_mills_clay.md`, and `CLAUDE.md` only. `README.md`, `educational/`,
  `phenomena/`, and `foundations/` documents must not contain "(Cycle XX)" references.

### Equation Modules (equations/)

- Every module must be runnable: `python3 equations/module.py` produces output.
- Distinguish **inputs** (values taken from data) from **predictions** (values computed
  from DFC parameters). Label them clearly in output.
- If a prediction fails, print the failure prominently.
- All modules should include a docstring explaining: (a) what physical question it
  addresses, (b) what the DFC mechanism is, (c) what the key references are.

---

## What Is Verified vs. Open

Always maintain this distinction explicitly. The model's credibility depends on it.

**Verified (numerically or formally):**
- τ_neutron = 878.4 s (0.1% match) — `equations/proton_stability.py`
- Spin-1/2: FR winding N=1, BPST zero mode normalizable, J_min=1/2 — `equations/spin_zero_mode.py`
- m_μ/m_e = 206.77 from R/d ratio — `equations/mass_spectrum.py`
- Q = T₃ + Y/2 for all first-generation fermions — `phenomena/.../electroweak.md`
- H₀ = 67.26 km/s/Mpc (0.2% match) — `equations/cosmology.py`

**Known failures (not yet resolved):**
- τ mass from mass_spectrum.py: predicts 212 MeV, observed 1777 MeV (8.4× off; superseded by Koide T2a route)
- Neutrino m₃/m₂: κ=5.33 vs observed 5.81 (−8.3%)
- Light quark masses M0: +24% at 2-loop QCD running (T2b; 1-loop was fortuitous cancellation)
- Baryon asymmetry η_B: 184× overshoot (T4; Sakharov conditions met but magnitude wrong)
- Proton-neutron Δm: NJL route +17% (T2b; C_QCD overshoot)

**Correspondences (consistent but not derived):**
- D5 ↔ U(1), D6 ↔ SU(2), D7 ↔ SU(3) assignments (working hypotheses)
- V(φ) = −α/2 φ² + β/4 φ⁴ (postulated; β=1/(9π) derived T2a — see Tier 2a table)
- Weinberg angle sin²θ_W=0.231 from Route 3B (k_Y=3/5 derived; M_c from SM running)

---

## Scientific Merit Criteria

Full criteria, tier system explanations, completeness milestones, and evaluation checklist:
**see `foundations/scientific_merit.md`**

### Tier 0 — Core Postulates
1. One continuous self-compressing field (no pre-existing space, gauge groups, or structure)
2. V(φ) = −α/2 φ² + β/4 φ⁴ (double-well; α, β are free parameters)
3. Bifurcation events produce all particles, forces, and spacetime

### Current Tier 2a Predictions (all verified, <5% error)

| Prediction | Equation module | Predicted | Observed | Error | Free params |
|---|---|---|---|---|---|
| Muon-to-electron mass ratio (206.77) | mass_spectrum.py | 206.77 | 206.77 | 0.0% | 2 (R, d) |
| Neutron lifetime (878 s) | proton_stability.py | 878.4 s | 877.8 s | 0.1% | 0 |
| Hubble constant (67 km/s/Mpc) | cosmology.py | 67.26 | 67.40 | 0.2% | 2 (Ω_m, Ω_Λ) |
| Higgs boson mass (125 GeV) | higgs_potential.py | 124.4 ± 3.7 GeV | 125.25 GeV | 0.7% | 1 (λ₀) |
| Weinberg angle (0.231) | weinberg_angle_rg.py | 0.2312 | 0.2312 | 0.01% | 1 (M_c) |
| α_em(M_Z) — fine structure at Z scale | alpha_em_prediction.py | 1/128.09 | 1/127.9 | +0.15% | 0 (36π chain) |
| Common gauge coupling g_eff (0.5443) | d5_complex_from_instability.py | 0.54433 | 0.5443 | 0.006% | 0 |
| Quartic coupling β | d5_complex_from_instability.py | 1/(9π) | 1/(9π) | 0.000% | 0 |
| W boson mass (80.38 GeV) | ew_radiative_corrections.py | 80.38 GeV | 80.377 GeV | +0.009% | 2 (+m_t,m_H) |
| Z boson mass (91.19 GeV) | muon_lifetime.py | 90.86 GeV | 91.1876 GeV | −0.36% | 2 |
| Fermi constant G_F | muon_lifetime.py | 1.168×10⁻⁵ GeV⁻² | 1.166×10⁻⁵ | +0.18% | 2 |
| Muon lifetime (2.197 μs) | muon_lifetime.py | 2.180 μs | 2.197 μs | −0.80% | 3 |
| Z total width (2495 MeV) | z_boson_decays.py | 2456 MeV | 2495 MeV | −1.56% | 2 |
| Z invisible width (499 MeV) | z_boson_decays.py | 493 MeV | 499.0 MeV | −1.16% | 2 |
| R_l = Γ_had/Γ_ll (20.767) | z_boson_decays.py | 20.746 | 20.767 | −0.10% | 2 |
| R_b = Γ_bb̄/Γ_had (0.2163) | z_boson_decays.py | 0.2197 | 0.21629 | +1.58% | 2 |
| A_FB^lep (0.01626) | z_boson_decays.py | 0.01677 | 0.01626 | +3.17% | 2 |
| α_s(M_Z) [ECCC+α_em(0)] | alpha_em_selfconsistency.py | 0.11821 | 0.11820 | +0.006% | 0 (SM α_em(0) input) |
| EW VEV v (246 GeV) | ewsb_cocrystallization.py | 247.83 GeV | 246.22 GeV | +0.65% | 2 (M_c(D5,D6) from ECCC) |
| Tau lepton mass [Koide] | koide_phase_coupling.py | 1776.97 MeV | 1776.86 MeV | +0.006% | 0 (m_e, m_μ inputs) |
| Electron a_e (g−2, 4-loop) | anomalous_magnetic_moment.py | 0.001158 | 0.001160 | −0.14% | 36π chain + QED C₂-C₄ (Cycle 488) |
| Lamb shift 2S₁/₂−2P₁/₂ (1058 MHz) | lamb_shift.py | 1050.5 MHz | 1057.845 MHz | −0.69% | 36π chain α⁵ scaling (Cycle 495) |

### Current Tier 2b Predictions (equation exists; >5% error or leading-order only)

| Prediction | Module | Predicted | Observed | Error | Resolution status |
|---|---|---|---|---|---|
| Thomson cross-section (6.65×10⁻²⁹ m²) | scattering_cross_sections.py | 6.633×10⁻²⁹ | 6.652×10⁻²⁹ | −0.28% | 36π+obs Δ_QED; was −4.3% (Cycle 143) |
| Hydrogen E_1 (−13.598 eV) | atomic_structure.py | −13.568 eV | −13.598 eV | +0.28% | 36π+obs Δ_QED; was −4.2% (Cycle 143) |
| Tau lepton mass [dimple] | mass_spectrum.py | 212 MeV | 1777 MeV | 8.4× off | Superseded by Koide route (Tier 2a above) |
| Neutrino mass ratio m₃/m₂ | neutrino_masses.py | κ=5.33 | 5.81 | −8.3% | Prior 4.3× was metric error (Cycle 165) |
| Strong coupling α_s(M_Z) [old] | alpha_s_target.py | 0.1086 | 0.1182 | 8.1% | Wrong M_c(D7) condition; superseded by ECCC above |
| Proton mass m_p (Regge) | baryon_mass_dfc.py | 934.8 MeV | 938.3 MeV | −0.4% | Tier 3: m_p=√(3π)Λ_QCD; Y-junction α_0^N=−1/4; inherits from σ=Q_top×Λ² (Cycle 168) |
| Delta(1232) mass m_Δ (Regge) | baryon_mass_dfc.py | 1206.8 MeV | 1232.0 MeV | −2.0% | Tier 3: m_Δ=√(5π)Λ_QCD; α_0^Δ=+1/4; m_Δ/m_p=√(5/3) Λ-independent (Cycle 168) |
| Charm and strange quark masses | quark_mass_kappa_derivation.py | +2.45% (κ=3π/2) | ~1277/97 MeV | +2.45% | **T2a C274**: κ_q=π×N_c/2 from center vortex; charm +0.29%, strange +2.09% |
| Proton charge radius r_p | proton_charge_radius_dfc.py | 0.809 fm | 0.8414 fm | −3.8% | T2a: VMD pion cloud (C545) |
| Light quark mass M0 (2-loop) | light_quark_mass_derivation.py | 2.49 MeV | 2.01 MeV | +24% | T2b: 1-loop cancellation was fortuitous; 2-loop NLO 21% (C544) |
| Proton-neutron Δm (QCD) | proton_neutron_mass_difference.py | 1.508 MeV | 1.293 MeV | +17% | T2b: NJL C_QCD=0.87 overshoots GL=0.50 (C552) |
| Baryon asymmetry η_B | baryon_asymmetry_magnitude.py | 1.13×10⁻⁸ | 6.14×10⁻¹⁰ | 184× | T4: Sakharov conditions met, magnitude wrong (C546) |

---

## File Structure Reference

```
DCmodel/
├── CLAUDE.md                      ← this file (condensed)
├── ROADMAP.md                     ← task priorities, tier rotation tracking
├── push_history.md                ← full cycle-by-cycle push history
├── current_state.md               ← living review document
├── ISSUES.md                      ← open questions, failures, blocked derivations
├── reconcilability_risk.md        ← MRRS analysis
├── foundations/
│   ├── scientific_merit.md        ← full tier criteria, completeness milestones
│   ├── substrate.md               ← φ field, V(φ), kink solutions
│   ├── dimensional_stack.md       ← D1-D7 structure
│   ├── critical_review_blind_spots.md ← 18 honest blind spots catalog
│   ├── yang_mills_clay.md         ← Clay Prize proof tracking
│   └── ...                        ← three_generations, spin_emergence, mass_hierarchy, higgs_geometry
├── phenomena/
│   ├── electromagnetism/          ← EM, electric charge, light
│   ├── particle_physics/          ← forces/ + particles/
│   ├── quantum/                   ← QM, measurement, interference
│   └── cosmology/                 ← expansion, dark matter, baryogenesis
├── educational/                   ← 33 modules (00–32), standalone DFC education series
├── practical_applications/        ← engineering-relevant limits and predictions
└── equations/                     ← ~100+ Python modules, all runnable
    ├── dfc_core.py                ← shared constants and recompute() framework
    ├── run_all_tests.py           ← master test suite (397 modules, ~2800 tests)
    ├── README.md                  ← equation module index
    ├── ym_clay_proof.tex          ← Yang-Mills mass gap proof document
    └── ...                        ← proton_stability, mass_spectrum, cosmology, etc.
```
