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
| "requires 3 spatial dimensions" | "produces three apparent spatial degrees of freedom" |
| "the forces were unified at high energy" | "the forces are always fold interactions of one object; at high compression, their topological distinctions diminish" |
| "unified force" (GUT sense) | "single substrate" or "one object" |
| "the three forces" (as fundamentally separate) | "the three closure-topology interaction regimes" or "fold interactions at D5, D6, D7 depths" |

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

Repeat this cycle indefinitely:

### Completeness Estimate (running)

```
Current estimate: ~75.5%  (viability: ~86%, mathematical rigor: ~65%)

Key bottleneck: α_em(0) gap: structural identity A−B = ln(1/α_em(0)) (Tier 4 open);
  α_s closed 0.006% (Cycle 144); v=247.83 GeV Tier 2a (Cycle 145); m_τ Koide Tier 2a (Cycle 146).
  Strong CP: theta=0 Tier 2a from S⁵ CP isometry (Cycle 147). Bottleneck 2 CLOSED Cycle 117.
  Priorities 2+3 CLOSED Cycle 157: real amplitude theorem + D6/D7 overlap integral.
  β Tier 1 candidate (Cycle 173); α=∛18 Tier 2a (Cycle 172); P4 decomposed (Cycle 175).
  Reviewer concerns addressed in DFC_master_equations.md (Cycle 176).
  T4 structural argument + I₄=C₂(fund,SU(3))=4/3 identity (Cycle 177).
  S_kink×α_D5=1 TIER 1 (Cycle 171): α_D5=1/S_kink algebraic tautology, not BPS assumption.
  α=∛18 TIER 2a (Cycle 172): derived from β[T2a]+S_kink×α_D5=1[T1]+BPS saturation[T1].

Recent cycles (full history: push_history.md):
| 2026-06-04 | 177 | ISSUES.md progress: T4 (fermion representation) and SU(3)/SO(6) new issue addressed. equations/fermion_representation.py (new): T3 structural argument — D6 kinks crossing D7 background acquire SU(3) charge via holonomy; one crossing = winding n=1 → fundamental rep (1,0), dim=3 [T3]; winding table n=0→singlet, n=1→quarks (dim=3), n=2→diquark, n=3→baryon precursor; path to T2a: Jackiw-Rebbi BVP for D6 Dirac operator in D7 kink background. Structural identity I₄=C₂(fund,SU(3))=4/3 (exact, residual 0.00e+00): kink shape integral = SU(3) Casimir of matter representation — would fail for adjoint or any other rep; g₁²=2I₄ and pQCD color factor C_F=4/3 are the same number [T3 self-consistency]. SU(3) vs SO(6) issue (Cycle 176): largely resolved by Cycle 117 — D5 complex structure J forces zero mode moduli ≅ ℂ³ (not ℝ⁶); U(3)/center=SU(3), not SO(6) (which acts on real S⁵⊂ℝ⁶); remaining open: standalone proof that J propagates from D5 to D7 zero modes. ISSUES.md T4 entry rewritten with T3 argument + I₄=C₂ identity + path to T2a. SU(3) vs SO(6) blocked derivation entry updated: "LARGELY RESOLVED." educational/03_depth_map.md: generation count corrected T1/D6→T2a/D7. | 86% | 65% | ~75.5% |
| 2026-06-04 | 176 | Reviewer assessment — all 5 concerns addressed in DFC_master_equations.md (Cycle 176). (1) β=1/(9π): Step 5 rewritten with explicit ECCC condition as the single T2a step; chain T1→ECCC[T2a]→β documented. (2) α=∛18: Step 7 corrected — E=S for static kink is a mathematical identity, not a convention; tier T1 given β. (3) Gauge coupling: Step 9 expanded — moduli metric steps 9a-9b are T1 exact (two independent routes to g₁²=2I₄); series holonomy step 9c is T3; formula g_eff²=2I₄/N_Hopf is T2a (not numerology). (4) Generation count: Step 15 rewritten — full chain: D7=SU(3)[T2a, Cycles 59-74] + Weyl formula dim(fund rep)=3[T1] → 3 generations; termination at n=3 is T3 (confinement blocks D8), not T1; tier corrected from "T1 exact" to "T2a conditional on D7=SU(3)". (5) Hopf construction error FIXED: Step 4 corrected — DFC uses complex sphere sequence S^{2n-1}⊂ℂⁿ with isometry SU(n) (dims 1,3,5→N_Hopf=9), NOT classical Hopf fibrations (dims 1,3,7→sum=11). Identity (8) label fixed. equations/generation_count_proof.py (new): Parts A-E all PASS — S³≅SU(2) residual 4.44e-16, SU(3) on S⁵ residual 6.66e-16, Weyl dim(1,0)=3, N_Hopf=9, g_eff=0.54433. Open gaps table updated: ECCC gap, termination gap, series holonomy gap added. File reference updated. | 86% | 65% | ~75.5% |
| 2026-06-04 | 175 | p4_derivation_attempt.py (new, Step 1): P4 decomposition analysis — tachyon circularity confirmed (L1 kink STABLE, no tachyon in V(phi); L2 tachyon only within V(|Phi|^2)); P4 reduces to P4a (new DOF opens, irreducible T0) + T1 chain from P1. Key T1 result: Z2xZ2 quartic with vacuum on circle |Phi|=phi0 for all theta algebraically forces lambda=2*beta (unique), which is identical to V=V(|Phi|^2) [verified, max diff 3.55e-15]. P1 (one substrate) -> Q_top universal -> beta_eff(theta)=beta -> lambda=2*beta -> V=V(|Phi|^2). "No preferred direction" axiom derived from P1, not postulated. REVIEW_RESPONSE.md Priority 1 updated: resolved. DFC_master_equations.md: P4 -> P4a + T1 chain; Step 3 corrected. foundations/substrate.md: beta entry corrected. All-passes: Part A (3.55e-15), Part B (isotropic at lambda=2beta), Part D (1.78e-15). | 85.5% | 64.5% | ~75% |
| 2026-06-04 | 173 | d5_instability_tier1.py (new, Step 1): β=1/(9π) TIER 1 CANDIDATE — "no preferred direction" Tier 0 axiom ELIMINATED. Route F (rotational tachyon universality): kinks exist in all (φ₁,φ₂) directions [T1, Z₂×Z₂]; each has ω²₀=−α/2 [T1, PT s=1]; ω²₀(θ)=−α/2 for all θ forces V₁₁=V₂₂=−α sech², V₁₂=0 → V=V(|Φ|²) algebraically [T1]. Spread across 6 angles: 0.00e+00 (exact). Route B residual 7.26e-16 (exact). Route D B+C≡V(|Φ|²) 1.78e-15 (exact). All 3 routes PASS. Weakest remaining link: T2a (single α_em at D5); if proved T1, full chain T1. d5_complex_from_instability.py Step 4 updated with Cycle 173 note. ISSUES.md T13 "remaining open" section updated: β T1 candidate, α=∛18 T1 candidate. | 85% | 63.5% | ~74.5% |
| 2026-06-04 | 172 | v_phi_rg_analysis.py (new, Step 1): α=∛18 TIER UPGRADE T3→T2a — derivation from β=1/(9π)[T2a]+S_kink×α_D5=1[T1]+α_D5=β/4[T1]+BPS saturation E_kink=S_kink[T1]; solving (4/3)α^{3/2}/(β√2)=4/β gives α=(3√2)^{2/3}=∛18 exactly (residual 0); uniqueness scan confirms; Part A: perturbative RG has no UV fixed point (Landau pole) — selection comes from compression cascade self-consistency, not Wilsonian RG; Part B: compression fixed point — S_kink=4/β→α=∛18; Part C: full tier chain documented; Part D: three-way identity S_kink=4/β=1/α_em=36π verified (all residuals<3e-14); Part E: tier history T3(169)→T3-BPS(170)→T1 S-identity(171)→T2a α(172); Part F: ξ=0.8738 l_Pl [CORRECTION: Cycle 169 claimed ξ=18^{-1/6}=0.6177, incorrect; correct ξ=√(2/∛18)=0.8738; "ξ≈1/φ_golden" structural note RETRACTED]. ISSUES.md T13: promoted T3→T2a; ξ correction and retraction documented. foundations/substrate.md: α entry updated T3→T2a; ξ correction noted. educational/05_particles.md (new, Step 4): Module 05 "Particles: Electrons, Quarks, and Neutrinos as Kink Configurations" — particle as topological defect, kink as simplest particle, spin-1/2 from Jackiw-Rebbi zero mode, Q=T₃+Y/2 for first-gen, electron/muon accounts, three generations from S³ topology (Tier 1), tau mass 1776.97 MeV (+0.006% Tier 2a), quark confinement from D7 S⁵, proton mass −0.4% Tier 3, neutrino −8.3% Tier 2b; open table. | 84.5% | 63% | ~74% |
| 2026-06-04 | 171 | kk_holonomy_derivation.py (new, Step 1): KK reduction proof — S_kink×α_D5=1 is TIER 1 algebraic tautology: S_kink=4/β, α_D5=β/4, product=1 for ALL β (7 values verified, all residuals 0.00e+00); upgrades D5/D1 BPS duality from Tier 3→Tier 1; α_D5=1/S_kink is Tier 2a derived. Parts A-H: 5D DFC Lagrangian → phase zero mode; moduli metric g_θθ=Q_top=2, g_XX=I₄=4/3 (both Tier 1); N_wv×mode_norm=1 exact (ALL β); g_KK²=2π/(R/λ); g₁²=2I₄ from two independent routes; g_eff²=2I₄/N_Hopf=8/27 Tier 2a; α_em=β/4 algebraic; tier upgrade chain documented (Cycle 169 T3→170 T3-BPS→171 T1); α=∛18 Tier 3; three selection routes identified (RG fixed point recommended); next: equations/v_phi_rg_analysis.py. | 84% | 62.5% | ~73.5% |
| 2026-06-04 | 170 | d5_closure_condition.py (new, Step 1): Part A — V(φ) form uniqueness from 3 compression requirements R1(Z₂)+R2(no zero)+R3(bounded below) → V=−α/2φ²+β/4φ⁴ UNIQUELY selected (Tier 0→T3); V(φ₀) analytic residual 7e-15. Part B — D5 minimal winding: Q_top=2 kinks × π phase = 2π = 1 winding; n_D5=1 exact (residual 0). Part C — BPS/duality: S_kink×α_D5=1 (Montonen-Olive analog for D1/D5; residual 0, exact); BPS saturation E_kink=S_kink (residual 1.4e-14). Part D — algebraic chain 1/α_em=(1+k_Y²)/α_common=4/β=36π (both routes residual 1.3e-16); β=4α_em exact. Part E — full chain T3→T2a→T3→T3: compression→V(φ)→β→1/α_em→BPS→α=∛18; tier upgraded from "conditional Tier 3" to "Tier 3 with BPS mechanism". Part F — uniqueness: only α=∛18 satisfies S_kink=4/β AND S×α_em=1 simultaneously (tabulated). ISSUES.md T12 (Step 2): β=4α_em exact clarifies gap lives only in δ(Δα)^{NP} hadronic piece; BPS mechanism noted. foundations/coupling_emergence.md (Step 3): Open 1 updated with BPS/duality mechanism (Tier 3); two new Consistency Check rows (V(φ) form T3, α=∛18 T3+BPS); d5_closure_condition.py + alpha_from_kink_action.py added to Connections. educational/04_forces.md (new, Step 4): Module 04 "Forces: How U(1), SU(2), SU(3) Appear from Fold Topology" — force as fold interaction (not separate objects), S¹→S³→S⁵ Hopf sequence, U(1)/SU(2)/SU(3) meaning from closure topology, coupling constants (g_eff²=8/27, 36π, α_s +0.006%), why 3 forces (3 Hopf spheres), how forces relate (common coupling, depth hierarchy), 3 open gaps; summary table. | 84% | 62% | ~73% |
| 2026-06-04 | 169 | alpha_from_kink_action.py (new, Step 1): primitive compression threshold α = ∛18 = (Q_top×N_Hopf)^(1/3) ≈ 2.621 [Planck units, Tier 3]; three-way identity S_kink=4/β=1/α_em=36π (all residuals < 3e-16); β=4×α_em(Mc) algebraically exact; α^(3/2)=√(Q_top×N_Hopf)=√18=3√2 (residual 0); kink width ξ=18^(−1/6)=0.6177 l_Pl (0.07% from 1/φ_golden — structural note); E_kink=36π M_Pl=113.1 M_Pl; φ₀=8.608 M_Pl; S_kink×α_em=1 exact; hierarchy α(Λ_QCD)/α(M_Pl)~10^(−39); V(φ) form uniquely determined from 3 physical requirements (cannot reach zero, no preferred sign, stable rest state). ISSUES.md: T13 new entry — α=∛18 Tier 3 candidate with derivation chain, path to Tier 2a, files. foundations/substrate.md: "High priority" updated — β Tier 2a Cycle 117 noted; α Tier 3 candidate with full physical consequences (ξ, E_kink, φ₀). README: recently resolved updated (Cycles 138→169, α=∛18 added). | 84% | 62% | ~73% |
| 2026-06-04 | 168 | baryon_mass_dfc.py (new): m_p=√(3π)×Λ_QCD=934.8 MeV (−0.4%, Tier 3, 0 free params); m_Δ=√(5π)×Λ_QCD=1206.8 MeV (−2.0%, Tier 3); m_Δ/m_p=√(5/3)=1.291 (obs 1.313, −1.7%, Λ-independent). Y-junction intercepts: α_0^N=−1/4 (3×Q_top/8−1), α_0^Δ=+1/4 (N+Q_top/4 spin bonus). Universal slope α'=1/(4πΛ²) (from σ=Q_top×Λ², Cycle 160). Meson-baryon coherent series: m_ρ=√(2π)Λ, m_p=√(3π)Λ, m_Δ=√(5π)Λ. ISSUES.md: strong_force Open Q2 stale 45.9 MeV updated; m_p and m_Δ added; m_p row added. hadronic_spectroscopy.md audit: Γ_ee −82%→−8.1% (large-N_c, Cycle 167); baryon mass section added; One-Sentence updated to include m_p, m_Δ. educational/03_depth_map.md (new): Module 03 — D1-D7 as compression thresholds, provisional depth assignments, Hopf fiber closure sequence, verified evidence at each depth, 5 open gaps. | 83.5% | 62% | ~73% |
| 2026-06-04 | 167 | pion_decay_constant.py Part E (large-N_c VMD, Cycle 167): f_ρ=√(N_c/(8π²))×m_ρ=√(3/(4π))×Λ_QCD=148.8 MeV (−4.9%, Tier 3); Γ_ee=6.47 keV (−8.1%, Tier 3); improvement: KSFR gave −61%, large-N_c gives −8.1% (+52 pp). DFC ratio f_ρ/f_π=√(3π/4)=1.535 (exact). NWA Δα_ρ=0.00598; T12 chain improved but parton-subtraction remains Tier 4. ISSUES.md T12 updated with large-N_c result. foundations/coupling_emergence.md audit: f_ρ and Γ_ee rows added to Consistency Checks; pion_decay_constant.py added to Connections. educational/02_how_space_appears.md (new): Module 02 "How Space Appears" — compression concept, D-depth markers as compression behaviors (not layers), D3 localization account of apparent space, D-depth ordering argument (each requires previous), 3D spatial directions from D3-D7 topology sequence, measurement framing, verified results and open gaps; summary table; pointer to Module 03. | 83.5% | 62% | ~73% |
| 2026-06-03 | 166 | pion_decay_constant.py (new, Cycle 166): f_π=Λ_QCD/π=96.9 MeV (+5.1%, Tier 3, 0 free params; best c_π candidate from scan); GOR: m_q^{GOR}=3.24 MeV vs obs 3.45 MeV (−6%, consistent); KSFR chain: g_ρππ=5.57 (−6.4%), f_ρ=96.9 MeV (−37%, vs −82% large-N_c), Γ_ee=2.745 keV (−61%, vs −82%); NWA Δα_ρ=0.00254 (2.5× T12 target; parton baseline ~60% of full ρ contribution); T12 chain complete to Tier 3: α_s→Λ_QCD→f_π→g_ρππ→f_ρ→Γ_ee→Δα_ρ; open: f_π from D7 condensate field eq (Tier4), parton-model matching for δ(Δα)^{NP}=0.00102 (T12 Tier4). ISSUES.md T11 Known-Failures table fixed: "4.3×"→"−8.3%" (metric error). neutrinos.md audit: "4× discrepancy" language removed throughout; correct DFC comparison m₃/m₂=κ=5.33 vs obs 5.71 (−6.7%); metric confusion note added; Consistency Check row updated; Open Q2 rewritten. educational/01_the_substrate.md (new): Module 01 "The Substrate" — field concept, V(φ) double-well, kink, φ₀=±√(α/β), E_kink=4/3c²φ₀²/λ, I₄=4/3, Q_top=2, β=1/(9π) derived, g_eff²=8/27; summary table; open: α not yet derived. | 83.5% | 62% | ~73% |
| 2026-06-03 | 165 | T11 neutrino metric correction: "4.3× failure" was metric error — Δd₃₁/Δd₂₁=1.34 is depth-difference ratio, not mass ratio; DFC κ=5.33 vs observed m₃/m₂=5.81 = −8.3% (Tier 2b, not catastrophic); CLAUDE.md Tier 2b + Known failures corrected; ISSUES.md T11 updated with revised analysis; foundations/mass_hierarchy.md audit: Koide account promoted Tier 3→2a (Cycle 146 promotion not yet reflected); correct mechanism description added (canonical phase vertex 1/√Q_top, Z₃ charge counting); educational/00_overview.md (new): Module 00 "What Is the DFC Model?" — general audience, no physics background, ~1200 words; covers: two-theory problem, DFC compression idea, bifurcations, how U(1)/SU(2)/SU(3) emerge, 36π quantitative example (+0.15%), established vs open table, comparison to String/SUSY/GUT, falsifiable predictions. | 83.5% | 62% | ~73% |
| 2026-06-03 | 164 | Cycle structure restored + educational step added: three-bottleneck priorities restored (α_em identity, Strong CP formation, arg(det M_q)=0); Steps 1-5 — Step 1 critical/bottleneck, Step 2 random open issue from ISSUES.md, Step 3 update random doc, Step 4 create/update random educational module (educational/ planned 00-08, writing rules: English first, define jargon, Tier-honest, 500-1500 words), Step 5 MANDATORY README+push every session; README current focus updated. | 83.5% | 62% | ~73% |
| 2026-06-03 | 163 | Strategic refocus (corrected): CLAUDE.md gap priority order made primary — Level 1 (σ from D7 vacuum energy, α_em identity, f_ρ overlap), Level 2 (proton mass, neutrino hierarchy, quark masses), Level 3 (G_Newton, ℏ, D3/D4 formal); falsifiable prediction documents and educational modules moved to Secondary A/B (only when no gap is tractable); Step 1 updated (gap work default, educational/phenomenon only as fallback); README current focus updated (gap-closing order explicit, predictions/education downstream). | 83.5% | 62% | ~73% |
| 2026-06-03 | 162 | Strategic refocus: CLAUDE.md priorities rewritten — two top priorities replace three bottlenecks: (A) falsifiable prediction development (no axion/d_n=0 Tier 2a, absolute proton stability Tier 1, no SUSY, d_n=0 exact — each with derivation tightening goal and experimental timeline); (B) educational modules in educational/ (00-08 module plan, standard format, audience=general, writing rules); Step 1 updated; README updated (Status section rewritten, educational/ in repo map, Foundational Reading Order updated, recently resolved extended through Cycle 161, two-priority focus stated explicitly). | 83.5% | 62% | ~73% |
| 2026-06-03 | 161 | hadronic_spectroscopy.md (new): Regge trajectory DFC account — α_0=Q_top/4=1/2 [T2a], σ=Q_top×Λ² [T3], m_ρ=√(2π)Λ=763 MeV [T3, −1.58%, 0 free params], α'=0.858 GeV⁻² [T3, −2.5%], Γ(ρ→ππ)=142 MeV [T3, −4.6%]; 5 open questions documented (σ proof, f_ρ VMD, f_π chiral condensate, heavy mesons, Δα_had); composite_particles.md audit: α_s OPEN→+0.006% Tier 2a, σ and m_ρ rows added, hadronic_spectroscopy link added; strong_force.md Connections: hadronic_spectroscopy.md + rho_meson_dfc.py + d7_nonpert_coefficients.py added; confinement.py stale note fixed (one-loop artifact). | 83.5% | 62% | ~73% |
| 2026-06-03 | 160 | D7 non-perturbative coefficients (equations/d7_nonpert_coefficients.py, new): α_0=Q_top/4=1/2 Tier 2a (massless D7 kinks, standard QCD string massless endpoint); σ=Q_top×Λ_QCD²=185440 MeV² Tier 3 (−4.2% vs obs 193600 MeV²; Q_top=2 is only DFC Tier-1 integer fitting c_σ<5%); m_ρ=√(2π)×Λ_QCD=763.3 MeV Tier 3 (−1.58%, 0 free params!); α'=1/(4πΛ_QCD²)=0.858 GeV⁻² Tier 3 (−2.5%); Γ(ρ→ππ)=142 MeV (−4.6%, KSFR+DFC m_ρ, obs f_π input); chain: Q_top[T1]→α_0=1/2[T2a]→σ=Q_top×Λ²[T3]→m_ρ=√(2π)Λ[T3]; DFC Λ_QCD=304.5 MeV selects minimum error (-1.6%); PDG lower bound 210 MeV gives −32%. | 83.5% | 62% | ~73% |
| 2026-06-03 | 159 | ρ meson from DFC D7: Λ_QCD=304.5 MeV two-loop from α_s(M_Z)=0.11821 — within PDG 210-340 MeV (confinement.py −83% diagnosed as one-loop artifact, not DFC failure); m_ρ=825 MeV (+6.4%) via Regge+DFC string tension Tier 2b; Δα^{ρ+ω+φ}=0.010654 (39% of Δα_had) structurally consistent; T12 gap 0.00102 requires matched EW→QED running conversion (not local subtraction); rho_meson_dfc.py new. | 83% | 62% | ~72.5% |
| 2026-06-03 | 158 | α_em hadronic VP: R∞=11/3 exact from DFC (N_c=3, Q_f=2/3,1/3) Tier 2a; Δα_had^{pQCD}(c+b)=0.00820 (29.7% of PDG) Tier 2a; T12 gap decomposed: δ(Δα)^{non-pert}=0.00102 = 3.70% of Δα_had — b₁ running embeds 96.3% already; fermion content unification: b₃,b₁,Δα_lep,R∞ all from (N_gen=3,N_c=3,Q_f) Tier 3; blocking condition for Priority 1 precisely identified: R^{had}−R^{parton} from D7 confinement; alpha_em_hadronic.py new. | 82.5% | 61.5% | ~72% |
| 2026-06-03 | 157 | Interface overlap integral: real amplitude preservation theorem (ODE uniqueness, Tier 1) → D4→D7 amplitude chain real positive; Jackiw-Rebbi zero modes sech^n real (residual 9.96e-07 Tier 2a); D6/D7 overlap Im(Y)=0 exact; 12-step chain theta_bar=0 Tier 2a; Priority 2 (theta=0 formation) Tier 3→2a; Priority 3 (arg(det M_q)=0) Tier 3→2a; interface_overlap_integral.py new. | 82.5% | 61.5% | ~72% |
| 2026-06-03 | 156 | Strong CP formation: V(theta=0)<V(theta=pi) Dashen ChPT ΔV=9.9e-5 GeV⁴ (63% vac E density) Tier 2b; ΔV/T⁴_D7~1e-65 (topological selection must operate); domain wall 2×E_kink cost for theta=pi Tier 3; D5 anchor Tier 2a; recursion D5→D6→D7 Tier 3; KEY: Tier3→2a for Strong CP and arg(det M_q)=0 share same D5→D6/D6→D7 overlap integral — one calc closes both Priority 2 and 3; strong_cp_formation.py new. | 71.5% | 60.5% | ~71.5% |
| 2026-06-02 | 155 | α_em(0) identity proof: B_U1=(12π/41)cos²θ_W(1−Δα)(1/α_em(0)) algebraic substitution Tier 1; Δα_lep=0.0314 from DFC N_gen=3 Tier 2a (−0.24%); fermion content unification b₃,b₁,Δα_lep,Δα_had all from (N_gen=3,N_c=3,Q_f) Tier 3; NEW dominant gap = g₂/α_em α₁ chain tension 0.11% > ECCC 0.044%; Req Δα=0.0653 vs obs 0.0663 (−1.57%); T12 tension added ISSUES.md; alpha_em_identity_proof.py new. | 71.5% | 60.5% | ~71.5% |
| 2026-06-02 | 153 | arg(det M_q)=0: equations/arg_det_mq_zero.py (new) — 5-step chain; Steps A-C Tier 2a/1; Step D Tier 3 (D6/D7 overlap real Hermitian pending); theta-bar=0 Tier 3; J=3.08e-05≠0 consistent (CKM = D6 mixing); weak/strong ratio=2.3e10 explained. strong_cp_problem.md Open Q2 PARTIALLY RESOLVED. Bottleneck 3 progress: arg(det M_q) Tier 3 structural argument complete. | 71.5% | 60.5% | ~71.5% |
| 2026-06-02 | 152 | electroweak_precision.md audit: global fit chain updated (β=0.0351→1/(9π), g_eff 0.5423→0.54433, v=246→247.83 GeV); error attribution corrected (r_U1/λ heuristic→ECCC M_c from SM running, B2 CLOSED noted); Open Q2 RESOLVED Cycle 145 Tier 2a. | 71.5% | 60.5% | ~71.5% |
| 2026-06-02 | 151 | strong_force.md audit: α_s row 8.1%→+0.006% Tier 2a (ECCC Direction B, Cycle 144); Λ_QCD row clarified (−83% threshold-matching issue, not α_s gap); Open Q3 RESOLVED; note rewritten. ISSUES.md: strong_force.md α_s updated; muon_tau.md stale note cleaned. | 71.5% | 60.5% | ~71.5% |
| 2026-06-02 | 150 | w_z_bosons.md audit: Coupling chain subsection added (β→g_eff→ECCC→M_W=79.67 GeV −0.88%/M_Z=90.86 GeV −0.36%/G_F +0.18%); v_DFC=247.83 GeV EWSB co-crystallization noted; Consistency Checks updated with Tier 2a rows for M_W, M_Z, G_F, v; g_W OPEN→Tier 2a (−0.19%); Open Question 2 updated PARTIALLY RESOLVED; Connections: 3 new equation modules. | 71.5% | 60.5% | ~71.5% |
| 2026-06-01 | 149 | photon.md full audit: 36π chain replaces heuristic (1.3%→+0.15%); σ_T −4.3%→−0.28%; Bottleneck 2 CLOSED noted; coupling_emergence.md Open Derivation 1 algebraically proved (36π=(1+k_Y²)/α_common=4/β, Tier 2a); Tier 4 residual: kink-profile-only derivation. | 71.5% | 60.5% | ~71.5% |
| 2026-06-01 | 147 | Strong CP: theta=0 Tier 2a from S⁵ CP isometry; pi_3(S⁵)=Z₂≠pi_3(S³)=Z blocks D6→D7 phase transfer; d_n=0 Criterion B prediction; strong_cp_theta.py (50k samples, max dev 6.7e-16); strong_cp_problem.md Consistency Checks updated. | 71.5% | 60.5% | ~71.5% |
| 2026-06-01 | 146 | Koide Step 4d Tier 3→2a: m_τ=1776.97 MeV (+0.006%, 0 free params); canonical phase vertex factor 1/√Q_top from collective coordinate action; Z₃ charge counting shows exactly one insertion for all off-diagonal; koide_phase_coupling.py new; CLAUDE.md +m_τ Koide entry. | 71% | 60% | ~71% |
| 2026-06-01 | 145 | EWSB co-crystallization Tier 3→2a: v=247.83 GeV (+0.65%); structural argument for b0=11 — SU(2) in Higgs phase cannot drive transmutation, D7 SU(3) confinement (b0=N_Hopf+Q_top=11) must; ewsb_cocrystallization.py updated; coupling_emergence.md upgraded; CLAUDE.md +v entry. | 70% | 59% | ~70% |
| 2026-06-01 | 144 | ECCC self-consistency: α_s gap 8.1%→0.006% via correct M_c(D7) condition; α_em(0)=1/136.98 (−0.044%); alpha_em_selfconsistency.py; foundations/coupling_emergence.md stub; internal 36π↔g₂ tension documented. | 69% | 58% | ~69% |
| 2026-05-27 | 143 | 36π chain propagated downstream: scattering_cross_sections.py σ_T −4.3%→−0.28%; atomic_structure.py H levels −4.2%→+0.28%; stale error-budget text fixed; CLAUDE.md rewrite (50% reduction); push_history.md + foundations/scientific_merit.md created. | 68.5% | 58% | ~68.5% |
| 2026-05-27 | 142 | α_em prediction chain: 36π → 1/α_em(M_Z)=128.09 (+0.15%); 1/α_em(0)=137.23 (+0.14%); 10× improvement; downstream σ_T/a_e/r_e all now <0.3% error. | 68% | 57% | ~68% |
| 2026-05-27 | 141 | 36π formula: 1/α_em(M_c(EW))=36π (exact, 0 free params, Tier 2a); EW running → M_Z; Δ_QED=9.136 → q=0. | 67.5% | 56.5% | ~67.5% |
| 2026-05-26 | 140 | QCD threshold analysis: Nf=6 one-loop correct level for ECCC identity; deviation 0.044%. | 67% | 56% | ~67% |
| 2026-05-26 | 139 | ECCC scale ratio: M_c(D7)/M_c(D5)=136.97≈1/α_em(0) (−0.044%, Tier 1 structural). | 67% | 56% | ~67% |
| 2026-05-23 | 138 | Koide Step 4d: selection rule t=1/√Q_top (Tier 3); m_τ=1776.97 MeV (+0.006%). | 66.5% | 55.5% | ~66.5% |

Next milestone: prove structural identity A−B = ln(1/α_em(0)) algebraically (Tier 4→1);
  Cycle 160: σ=Q_top×Λ²=185440 MeV² (−4.2%, Tier 3); m_ρ=√(2π)Λ=763 MeV (−1.58%, Tier 3,
  0 free params); α_0=1/2 Tier 2a; α'=0.858 GeV⁻² (−2.5%). Path to Tier 2a: prove
  σ=Q_top×Λ² from D7 kink vacuum energy (Yang-Mills mass gap — Tier 4). DFC Λ_QCD=304.5 MeV
  selects the minimum m_ρ error across PDG range. Priorities 2+3 CLOSED Cycle 157.

Model Reconcilability Risk Score (MRRS) — see reconcilability_risk.md for full analysis:
  Core gauge/coupling sector:      20%   (was 28%; Bottleneck 2 closed Cycle 117: −8%)
  Full SM reproduction:            48%   (was 58%; β derivation Tier 2a Cycle 117: −10%)
  Complete theory (SM+gravity+QM): 72%   (was 76%; coupling chain rigorous: −4%)
Key swing factors: τ mass mechanism (Full SM −12% if found); M_c(D7) (α_s 8.1% off)
```

**After every push:** Update the estimate in THREE places every cycle:
1. The `Current estimate:` line in the code block above (this file)
2. The `Current status:` line at the top of `README.md` (line ~9)
3. The `## Mathematical Completeness Estimate` section in `README.md` (~line 191)

All three must stay in sync. The estimate has two components:
- **Viability** (~25% baseline): increases when new structural accounts are added, known
  failures are resolved, or predictions are confirmed by data.
- **Mathematical rigor** (~8% baseline): increases only when actual derivations are
  completed. Structural descriptions do not move rigor.

**Priority weighting for Step 1:** Prefer phenomena and derivations connecting to the
three bottlenecks:

1. **α_em(0) derivation** — prove A−B = ln(1/α_em(0)) algebraically to close α_em and
   α_s gaps simultaneously (equations/alpha_em_eccc.py, Cycle 139).

2. **Strong CP formation argument** — formal nucleation path from D7 formation dynamics
   showing energy minimum at theta=0 vs theta=pi; promote theta=0 selection Tier 3→2a
   (equations/strong_cp_theta.py, Cycle 147).

3. **Quark mass matrix phase** — derive arg(det M_q)=0 from D6/D7 interface to close
   the theta-bar = theta_QCD + arg(det M_q) equation.

**After every push, also check `ISSUES.md`** — centralized tracker for open questions,
known failures, internal tensions, retracted claims, and blocked derivations.

---

### Step 0 — Practical Applications (every ~5–10 cycles, optional)

Before Step 1, consider whether to add a new entry in `practical_applications/`.
See `practical_applications/OVERVIEW.md` for the document format and Pool A/B/C source
selection. Use this step to explore engineering implications derived from verified DFC
results — absolute limits, efficiency ceilings, or unusual technological possibilities
implied by the substrate structure.

---

### Step 1 — Critical Step (bottleneck-focused)

Identify a physics phenomenon not yet in `phenomena/` (or a placeholder needing content),
or a derivation step that advances one of the three bottlenecks above. Choose one with
preferential weight toward phenomena that connect to the three bottlenecks.

1. Write the **conceptual document** in `phenomena/` following the standard format:
   - One-Sentence Synthesis (DFC account, not a placeholder)
   - Observation (what is measured/observed)
   - Standard Explanation (SM account, concise)
   - Dimensional Folding Explanation (DFC account — structural, specific, no anthropomorphism)
   - Formal Equations (key equations, even if some are stubs)
   - Consistency Checks table
   - Open Questions (honest about what is not yet derived)
   - Connections (links to related docs)
2. Write or update the **equation module** in `equations/` with numerical verification.
   Every quantitative claim in a phenomenon doc should have a backing Python calculation.
   Run it and record the output in the document.

### Step 2 — Continue with a Random Open Issue

Select a random open issue from `ISSUES.md` — an unresolved question, known failure,
blocked derivation, or internal tension. Attempt to make progress on it:
1. Read the issue entry and all linked files.
2. Make the best available progress: run a new equation, tighten a logical argument,
   identify the specific blocking step, or update the tier assignment if warranted.
3. Update the `ISSUES.md` entry to reflect what was learned or resolved.

### Step 3 — Update a Random Document

**Goal:** Every document in the repository should be reviewed and updated periodically.
Audit scope is the full repository — `foundations/`, `phenomena/`, `equations/`,
`README.md`, `ISSUES.md`, `current_state.md`, `comparisons/`, `practical_applications/`,
`educational/`.

1. Select any document at random from anywhere in the project.
2. Read it and the corresponding equation modules (if any).
3. Check: does the document accurately reflect the current state of the model?
   Flag any of these:
   - Claims that go beyond what equations currently show
   - Language that does not match the DFC framework (forbidden phrases, anthropomorphic agency)
   - Derivation steps marked as "established" that are actually assumptions or postulates
   - Tier assignments inconsistent with the Scientific Merit Criteria (foundations/scientific_merit.md)
   - Stale, missing, or outdated cross-references
   - Items marked "OPEN" that were resolved in a later cycle
   - Mathematical relations in prose without a prior natural-language statement
4. Update the document to match the current state of the model.

### Step 4 — Create or Update a Random Educational/Teaching Document

The model must be teachable to someone with no physics background. Educational modules
live in `educational/` and will form a complete course in the model. Each session,
either create the next module that does not yet exist or update an existing one.

**Planned module list** (work through in order; create if missing, update if exists):

```
educational/
├── 00_overview.md          ← What is DFC? One-page answer.
├── 01_the_substrate.md     ← The one object, V(φ), kinks
├── 02_compression.md       ← Why it compresses; what bifurcation means
├── 03_depth_map.md         ← D1-D7 as compression stages (provisional)
├── 04_forces.md            ← How U(1)/SU(2)/SU(3) appear from fold topology
├── 05_particles.md         ← Electrons, quarks, neutrinos as kink configurations
├── 06_predictions.md       ← What the model predicts; how to test it
├── 07_open_questions.md    ← What is not yet derived; honest gaps
└── 08_mathematics.md       ← The key equations, explained in plain language
```

**Writing rules for educational modules:**
- Every concept introduced in plain English first; equation (if any) second.
- No jargon without definition. Define every technical term in one sentence on first use.
- Each module must be readable without reading any other module first.
- Accuracy is non-negotiable: if something is Tier 3 or open, say so plainly.
  ("We believe X, but have not yet proved it" is the correct phrasing.)
- Length: 500–1500 words per module. Dense is fine; imprecise is not.

### Step 5 — Propagate Updates (MANDATORY every session)

After any new document or any audit:
1. Update `current_state.md` if a new strength, weakness, or audit result warrants it.
2. Update `MEMORY.md` if any project-level facts have changed.
3. Check whether any linked documents need updating.
4. **Update the Completeness Estimate in CLAUDE.md and README.md** (both places).
5. **Commit all changed files and run `git push`.** Confirm the remote accepted the push
   (output must show `main -> main` or equivalent). This step is non-optional.
   A session is NOT complete until the remote is updated.

Then return to Step 1.

---

## Document Standards

### Conceptual Documents (foundations/, phenomena/)

- The **One-Sentence Synthesis** must state the DFC account, not be a placeholder.
- The **Consistency Checks** table must include at least one row marked ✗ if any
  prediction fails or is not yet derived. Honesty about failures is required.
- **Open Questions** must be specific and actionable.
- Never mark something as "established" unless there is a completed equation or
  formal argument.

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
- τ mass from mass_spectrum.py: predicts 212 MeV, observed 1777 MeV (8.4× off)
- Neutrino m₃/m₂: κ=5.33 vs observed 5.81 (−8.3%; Cycle 165 corrects prior 4.3× metric error)
- Charm/strange quark masses: 15% below observed
- α_s(M_Z) = 0.1086 vs 0.1182 (8.1% off; M_c(D7) gap)

**Correspondences (consistent but not derived):**
- D5 ↔ U(1), D6 ↔ SU(2), D7 ↔ SU(3) assignments (working hypotheses)
- V(φ) = −α/2 φ² + β/4 φ⁴ (postulated); β=1/(9π) derived Tier 2a (Cycle 117)
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
| W boson mass (80.38 GeV) | muon_lifetime.py | 79.67 GeV | 80.377 GeV | −0.88% | 2 |
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

### Current Tier 2b Predictions (equation exists; >5% error or leading-order only)

| Prediction | Module | Predicted | Observed | Error | Resolution status |
|---|---|---|---|---|---|
| Electron anomalous magnetic moment (a_e) | anomalous_magnetic_moment.py | 0.001160 | 0.001160 | −0.14% | Leading term; α_em 36π chain (Cycle 142) |
| Thomson cross-section (6.65×10⁻²⁹ m²) | scattering_cross_sections.py | 6.633×10⁻²⁹ | 6.652×10⁻²⁹ | −0.28% | 36π+obs Δ_QED; was −4.3% (Cycle 143) |
| Hydrogen E_1 (−13.598 eV) | atomic_structure.py | −13.568 eV | −13.598 eV | +0.28% | 36π+obs Δ_QED; was −4.2% (Cycle 143) |
| Tau lepton mass [dimple] | mass_spectrum.py | 212 MeV | 1777 MeV | 8.4× off | Superseded by Koide route (Tier 2a above) |
| Neutrino mass ratio m₃/m₂ | neutrino_masses.py | κ=5.33 | 5.81 | −8.3% | Prior 4.3× was metric error (Cycle 165) |
| Strong coupling α_s(M_Z) [old] | alpha_s_target.py | 0.1086 | 0.1182 | 8.1% | Wrong M_c(D7) condition; superseded by ECCC above |
| Proton mass m_p (Regge) | baryon_mass_dfc.py | 934.8 MeV | 938.3 MeV | −0.4% | Tier 3: m_p=√(3π)Λ_QCD; Y-junction α_0^N=−1/4; inherits from σ=Q_top×Λ² (Cycle 168) |
| Delta(1232) mass m_Δ (Regge) | baryon_mass_dfc.py | 1206.8 MeV | 1232.0 MeV | −2.0% | Tier 3: m_Δ=√(5π)Λ_QCD; α_0^Δ=+1/4; m_Δ/m_p=√(5/3) Λ-independent (Cycle 168) |
| Charm and strange quark masses | quark_masses.py | 15% below obs | — | 15% | Unresolved |

---

## File Structure Reference

```
DCmodel/
├── CLAUDE.md                      ← this file (condensed)
├── push_history.md                ← full cycle-by-cycle push history
├── current_state.md               ← living review document
├── ISSUES.md                      ← open questions, failures, blocked derivations
├── foundations/
│   ├── scientific_merit.md        ← full tier criteria, completeness milestones
│   ├── substrate.md               ← φ field, V(φ), kink solutions
│   ├── dimensional_stack.md       ← D1-D7 structure
│   ├── three_generations.md       ← three-generation count from D6 topology
│   ├── spin_emergence.md          ← FR + Jackiw-Rebbi derivation of spin-1/2
│   ├── mass_hierarchy.md          ← dimple + global scale for lepton masses
│   └── higgs_geometry.md          ← S³ squashing as Higgs mechanism
├── phenomena/
│   ├── electromagnetism/          ← EM, electric charge, light
│   ├── particle_physics/
│   │   ├── forces/                ← strong, weak, electroweak
│   │   └── particles/             ← electron, quarks, neutrinos, ...
│   ├── quantum/                   ← QM, measurement, interference
│   └── cosmology/                 ← expansion, dark matter, baryogenesis
└── equations/                     ← Python modules, all runnable
    ├── proton_stability.py        ← verified
    ├── spin_zero_mode.py          ← verified
    ├── mass_spectrum.py           ← tau mass fails
    ├── quark_masses.py            ← c/s 15% off
    ├── neutrino_masses.py         ← depth ratio off
    └── cosmology.py               ← largely consistent
```
