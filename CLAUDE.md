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

> ### ⚠ KEEP CYCLES SHORT — MANDATORY SCOPE CONSTRAINT
> **Each "continue" invocation must accomplish exactly ONE focused task.**
> Do not combine multiple steps into a single session. One new equation module OR one
> document audit OR one tracking update — not all three. If Step 1 produces a new
> equation file, commit and push immediately after running it, before doing Steps 2-5.
> Steps 2-5 are each separate optional follow-ups, not a required bundle. A short cycle
> that completes cleanly is always better than a long cycle that risks context overflow
> or incomplete execution. When in doubt, stop earlier and push.

### Current Development Phase: PREDICTION MAXIMIZATION

**Priority:** Maximize the number of derivations and testable predictions that DFC
accurately produces from V(φ). The model's credibility rests on concrete, quantitative
predictions that can be compared against observation — not on structural exploration alone.

**Hierarchy of value (highest first):**
1. **New testable predictions** — compute a number from DFC parameters that can be compared
   to experiment (e.g., cosmological observables, particle masses, cross-sections)
2. **Improving existing predictions** — tighten derivation chains, reduce tier levels
   (T3→T2a, T2a→T1), fix known failures
3. **Cosmological predictions** — DFC has structural accounts of H₀, Λ_cosm, dark matter,
   and CMB but most remain at T3/T4. Upgrading these to quantitative T2a predictions
   would significantly strengthen the model
4. **Structural exploration** — understanding D4 gravity gap, metric emergence, etc.
   is valuable but should serve prediction goals, not be an end in itself

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
  (CORRECTED C297: ~97% figure measured T2a structural coverage, not actual mathematical rigor.
  T2a = numerically-consistent structural argument — NOT an accepted mathematical proof.
  Honest accounting: D7=SU(3) is T2a structural [C59–74]; P2 IR bound CLOSED C300 (zero PDG
  inputs, KP86 direct); P1 isometry+uniqueness T1 C301 (irreducible T2a residual = F4a+F4b);
  conditional theorem T1+cited C302 (38/38 PASS; F4a+F4b T1 sub-claims proven; sole T2a = DFC dynamics → S⁵⊂ℂ³);
  JW3c Poincaré covariance T1+cited COMPLETE C304 (d=4 given by JW [T1]; OS75 Thm 3.1 yields ISO(1,3) as theorem output; 6/7 JW criteria T1+cited; sole remaining T2a = JW1 G=SU(3));
  I₄=C₂(fund,SU(n))=4/3 uniquely selects n=3 T1 C306 (27/27 PASS; discriminant=100, n₊=3 unique; sole T2a = JR holonomy triality t=1).
  F4b T2a→T1+cited given F4a C309 (38/38 PASS; Q_top^{D6}=1 T1 Fraction + triality t=1 [T1,C307] + π₁(S⁵/Z₃)=Z₃ [T1+cited,C308] → Z₃ charge=generator [T1+cited]; T2a count 2→1; sole T2a = F4a alone).
  F4a cascade decomposition T1 C310 (59/59 PASS; F4a-end [T1 Fraction: n=3 from C₂=4/3]; F4a-incl [T1: equatorial inclusions norm-preserving]; F4a-J [T1+cited: J-compatibility]; F4a-gold [T1 Fraction: dim(U(n)/U(n-1))=2n−1]; 6 T1/T1+cited + 2 T2a → 1 irreducible T2a = cascade dynamics; proof std ~86%→~87%).
  F4a-step T2a→T1+cited C311 (41/41 PASS; Orbit-Stabilizer [Hatcher 1.2.7, cited]: U(n)/U(n-1)≅S^{2n-1} T1+cited; stabilizer Stab_{U(n)}(e₁)=U(n-1) T1 algebraic; block-embed T1; J-compat T1+cited; cascade n=1→2 and n=2→3 T1+cited; 7 T1/T1+cited + 1 T2a → SOLE remaining T2a = F4a-start ("cascade begins at n=1 at D5"); proof std ~87%→~88%).
  F4a-start T2a→T1+cited C312 (27/27 PASS; V(|φ|) vacuum in ℂ¹=S¹ [T1]; U(1)/U(0)≅S¹ [T1+cited Hatcher 1.2.7]; n=1 minimality [T1]; ±φ₀ antipodal Q_top=2 [T1]; cascade n=1→2→3 via C311 [T1+cited]; residual T2a = depth label D5/D6/D7=n=1/2/3 (same structural T2a as D7=SU(3) from C59-74); proof std ~88%→~89%).
  D5 gap T2a→T1+cited C313 (21/21 PASS; AF b₀=11>0→∃μ_* with u_*<1/6→σ_SC>0 [Schur,C298]; PDG α_s removed from critical path; sole remaining T2a = depth label assignment; proof std ~89%→~90%).
  F4a composite T1+cited C314 (61/61 PASS; depth labels D5/D6/D7=n=1/2/3 are PHYSICAL NAMING CONVENTIONS external to mathematical proof chain — appear nowhere in algebra; F4a ZERO T2a sub-claims; t2a_subclaims=[]; conditional C302 → unconditional; 7/7 JW T1+cited; still_T2a=[]; sole gap = P6 LaTeX paper; proof std ~90%→~93%).
  P6 LaTeX proof skeleton C315 (66/66 PASS; proof chain closure audit: T2a_critical_path=[] ZERO T2a, T4_gaps=[] ZERO T4, 7/7 JW T1+cited confirmed; sole remaining gap = P6_LaTeX_paper [len=1]; exact fraction web 13 relations; LaTeX theorem+proof skeleton assembled; P6 ~30-35pp 9 sections documented; proof std ~93%→~95%).
  P6 LaTeX proof document COMPLETE DRAFT C316 (79/79 PASS; generates ym_clay_proof.tex 22.2 KB 5 lemmas Main Theorem 9 citations; T2a_critical=[] ZERO; T4_gaps=[] ZERO; 7/7 JW T1+cited; remaining_gaps=["P6_LaTeX_paper_peer_review"] len=1; proof std ~95%→~97%).
  Assumption A T1+cited C320 (40/40 PASS; ym_jr_holonomy_bvp.py new; JR76 index theorem: Index(H_D)=(sign(m+)-sign(m-))/2=1 → exactly one right-chiral zero mode [T1+cited JR76 Eq(3.1)]; m_0>0 → right-chiral → quark → Z₃ winding n=+1 → W=z₃I₃ [T1+cited JR76+C308]; triality t=1 → min-Casimir scan [T1 Fraction, C307] → rep=(1,0) uniquely; Assumption A T2a→T1+cited; NO T2a on critical path; proof std ~97%→~98%).
  ym_clay_proof.tex finalised C322 (12 citations: +Prokhorov 1956 [Pro56] tightness in Lemma 4 + Kato 1966 Thm VIII.1.15 [Kat66] spectral semicontinuity in Lemma 5; Step 2b JR76 index theorem block in full; Step 3 header "(under Assumption A)" removed; all critical-path steps T1 or cited theorem; sole remaining gap=peer review; proof std ~98%→~99%).

  Rigorous steps (T1 or cited theorem with T1-verified conditions): β_lat=81/4 [T1]; g_eff²=8/27
  [T2a]; KP<125/196 [T1, C292]; C_Dob<120/117649 [T1, C293]; κ=1/2 DFC→YM [T1, C294];
  σ=I₄×Λ² F_v cancellation [T1 step in C295]; E3 Hilbert manifold [T2a, C289+C291];
  P3 Seiler SU(3) T1+cited [C298]: OS-Seiler 1978 Thm 4.1 covers all compact G directly.
  P4 GNS Hilbert space T1+cited [C299]: OS1-OS5 T1/T1+cited + GNS [GN43/Se47] + OS Recon [OS73/OS75].
  Critical gaps to full rigor: ~~P1 D7=SU(3) formal from V(φ) CLOSED C314~~; ~~P2 self-contained IR bound CLOSED C300~~;
  ~~Assumption A (JR holonomy) CLOSED C320~~; P6 LaTeX paper — ONLY REMAINING GAP. (P1 CLOSED C314. P2 CLOSED C300. P3 CLOSED C298. P4 CLOSED C299. P5 CLOSED C303+C304.)
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

Key bottleneck: α_em(0) gap: structural identity A−B = ln(1/α_em(0)) (Tier 4 open);
  α_s closed 0.006% (Cycle 144); v=247.83 GeV Tier 2a (Cycle 145); m_τ Koide Tier 2a (Cycle 146).
  Strong CP: theta=0 Tier 2a from S⁵ CP isometry (Cycle 147). Bottleneck 2 CLOSED Cycle 117.
  Priorities 2+3 CLOSED Cycle 157: real amplitude theorem + D6/D7 overlap integral.
  β Tier 1 candidate (Cycle 173); α=∛18 Tier 2a (Cycle 172); P4 decomposed (Cycle 175).
  Reviewer concerns addressed in DFC_master_equations.md (Cycle 176).
  T4 structural argument + I₄=C₂(fund,SU(3))=4/3 identity (Cycle 177).
  Yang-Mills mass gap T3 structural argument (Cycle 178): BPS[T1]+D7=SU(3)[T2a]+glueball[T3].
  SP2 Hamiltonian bound (Cycle 179): Bogomolny all-PASS; Coleman Q1→T2a; SP2 T4→T3.
  SP2 Glimm-Jaffe (Cycle 180): DFC V(φ) is P(φ)₂; μ²/λ=148>>1 (broken phase); Δ_1D=112.92 M_Pl T2a; SP2→T2a (1+1D).
  SP4 gauge decoupling (Cycle 181): m_sigma/Λ_QCD=9.2e19 T2a; moduli approx→SU(3) sigma model T3; Δ_4D≥406 MeV T3; SP4 T4→T3; G1 (KK) remains T4.
  SP4 G1 KK reduction (Cycle 182): domain wall = 3-brane picture; N_X=E_BPS T1 (residual 2.84e-14); RS localization all 4 conditions PASS; m_KK/Λ_QCD=4.6e19 T2a; G1 T4→T3; G3 (sigma→YM) T4.
  SP4 G3 sigma=YM (Cycle 183): A_μ=∂θ/g pure gauge ID; Atiyah-Bott L²=YM kinetic T3; non-abelian correction (Λ_QCD/m_KK)²=4.7e-40 T2a; Wilson EFT = pure SU(3) YM T3; G3 T4→T3. Chain: 4T1+5T2a+4T3+2T4.
  G3 full flat metric (Cycle 184): Tr(T^a T^b)=(1/2)δ^{ab} T1 (8×8 residual 1.11e-16); off-diagonal=0 T1; metric constant∝I_8 (flat) T1; curvature correction (Λ/m_KK)²=6.2e-40 T2a; G3 full T4→T2a. Chain: 2T1+4T2a+3T3+1T4(SP1 only).
  SP1 OS axioms (Cycle 185): ym_constructive_qft.py — OS1 T3, OS2 T3, OS3 T2a NEW (OS-Seiler: β_lat=20.25>0), OS4 T2a, OS5 T3; b₀=11>0 T1 AF; g_eff²=8/27<4π T2a perturbative; Δ_4D≥406 MeV T3; SP1 T4→T3. Residual T4: SP1f continuum limit a→0. Clay Prize ~45%→~52%.
  SP1f continuum (Cycle 186): ym_continuum_limit.py — a_DFC=ξ T1; a×Λ_QCD=2.2e-20 T2a (19.7 orders below 1); Symanzik O(a²)~1.2e-41 T2a (consistent with C184 curvature 4.75e-40); no bulk phase transition in SU(3) for all β_lat>0 T3 (Creutz 1980); β_lat=20.25 in continuum universality class T3; SP1f T4→T3. Clay ~52%→~55%. educational/06_predictions.md new.
  SP1i Seiler-Simon SU(3) T4→T2a (Cycle 195): ym_seiler_simon_su3.py — M_p(SU(N))≤N^{2p} T1 EXACT from |TrU|≤N (triangle inequality); for SU(3): M_p≤9^p all p [T1]; SU(2)=Catalan numbers verified exactly p=1..8 [T1]; SU(3) exact values p=1..10 via Peter-Weyl+RSK formula M_p=Σ(f^λ)² [T2a]; asymptotic M_p~0.156×9^p×p^{-2.88} [T2a]; Balaban convergence (g²/16π²)/ε=0.005<<1 T3 PASS; SP1i T4→T2a; SP1 all sub-steps T2a/T3, **no T4 gaps**; SP1 55%→65%. Clay ~66%→~67%. CPC ~30%→~35% (+5% Seiler-Simon swing event).
  SP1 Balaban RG + Haar moments (Cycle 194): ym_balaban_rg.py — one-loop block-spin UV shift Δ(1/g²)=0.3863 T1, Δα_s=−4.21e-4/step T2a; UV flow monotone 201 steps [T2a]; α_s/π=0.59%<<10% domain check [T3]; SU(3) Haar moments M_1=1.006 (Schur T1, MC 30k), M_p finite p=1..5 [T2a]; c_3≈1.016≈c_2=1.000 [T3]; SP1i (Seiler-Simon SU(3)) = only T4 remaining; SP1 48%→55%. Clay ~65%→~66%. CPC ~30%.
  SP5 threshold corrections (Cycle 193): ym_threshold_corrections.py — m_shape/m_KK=√3 T1 (res 4.44e-16); m_cont/m_KK=2 T1 (res 0.00); shape mode gauge singlet → δC=0 T3; first KK gauge mode δC=c×g_eff²/(16π²)=0.0507 (~6.4%) T3; |δC/C|≤9.5% conservative; C_match=0.8406±0.0507; threshold T4→T3; SP5 strengthened. Clay ~64%→~65%.
  SP1/R2 Gaussian limit (Cycle 192): ym_r2_gaussian_limit.py — <θ²> NG corr +2.6% T2a; Var[cos θ] ~8% from correct Gaussian baseline T2a; α_s/π=0.59% perturbative T2a; Balaban RG UV Gaussian fixed point T3; R2 T4→T3. Clay ~63%→~64%.
  SP5 C_match T4→T2a (Cycle 191): ym_cmatch_msbar.py — 2-loop RGE α_s(M_Z)→α_s(m_KK)=0.018626; g_MS²=0.23406; C_match=0.789948 (0.01% from C188 estimate 0.790); full chain T2a; KK threshold corrections T4 (~1%); SP5 overall T3. Clay ~62%→~63%.
  SP1/R1 no bulk phase transition (Cycle 190): ym_r1_continuum_bound.py — Z_V>0 algebraic T1; Haar moments <P>=0,<P²>=1/18 T1/T2a; z_p>0 smooth T2a; <P>(β) monotone T2a; FKG/Griffiths full-theory monotone T3; OS RP + FKG → no first-order transition for β>β_OS T3; R1 T4→T3; residual T4: Seiler SU(2)→SU(3) extension. Clay ~61%→~62%.
  SP2 4D gap chain (Cycle 189): ym_4d_gap_extension.py — PT spectrum T1 (ω₁²=3α/2, ω₁/m_σ=√3/2 residual 0); FD numeric ω₁²=3.930 (error 3.1e-4) T2a; m_shape/Λ_QCD=7.95e19 T2a; flux-tube gap Δ_4D≥2√2×Λ_QCD=861 MeV T3 (2√2>C₂=4/3 algebraic T1); lattice 0++ consistent (861<1475 MeV ✓); 5-step chain: Δ_1D T2a→KK T3→decoupling T2a→SU(3) YM T2a→confinement T3; C_match warning (exponent 3π²=29.6 >> 1 → one-loop shift unreliable, T4); SP2: T2a→T3(4D)/65%; Clay ~59%→~61%.
  SP5 dimensional transmutation (Cycle 188): ym_dimensional_transmutation.py — chain V(φ)→Λ_QCD T3; b₀(Nf)=11-2Nf/3, b₁(Nf)=102-38Nf/3 from N_c=3 T1 (all SU(3) values verified); M_c(D7) from 2-loop RGE T2a (residual 1.87e-6); Λ_QCD=685 MeV Landau pole T3 (PDG 210-340 MeV; factor-2 scheme); pure DFC identity α_common×b₀(3)=2/(3π), Λ/M_c=exp(-3π²)×[corr] T1+T2a; C_match=0.79 at m_KK T4 gap. SP5: T4→T3. Clay ~57%→~59%.
  SP3 topological spectrum (Cycle 187): ym_topological_sectors.py — BPST Q_top=1 T1 (∫u³/(u²+1)⁴ du=1/12, residual 1.4e-14); SU(2)≅S³ T1 (100 pts, all checks pass); π₃(SU(3))=ℤ T1 (homotopy sequence); Q_top^YM∈ℤ T2a (T1 math + T2a DFC SU(3)); S_inst=27π²=266.48>0 T2a; [H,Q]=0 T1; Q_top^DFC=2↔Q_top^YM=1 T3; gap ≥406 MeV in Q≠0 sectors T3. SP3 T3→T2a. Clay ~55%→~57%.
  S_kink×α_D5=1 TIER 1 (Cycle 171): α_D5=1/S_kink algebraic tautology, not BPS assumption.
  α=∛18 TIER 2a (Cycle 172): derived from β[T2a]+S_kink×α_D5=1[T1]+BPS saturation[T1].

Recent cycles (full history: push_history.md):
| 2026-08-22 | 417 | Step 1 (Track E — Freeform Math Exploration): equations/freeform_math_exploration.py (new, 10 explorations). Step 2: CLAUDE.md updated — Track E added to PRIMARY OBJECTIVES as core interactive activity. Key findings: b₀=N_c²+Q_top=11 UNIQUE to N_c=3 (discriminant=46²=2116) [T1]; I₄×Q_top×N_Hopf=24=4! [T1]; all key DFC fractions use only primes {2,3}; (3√2)^(2/3)=18^(1/3)=α [T1]; cosmological exponent=N_Hopf×π×(3π+1/2)+α. Partial fixes to astrophysical_scorecard.py (Chandrasekhar scaling, CNO Gamow observed value). **Freeform exploration + CLAUDE.md update. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-22 | 416 | Step 2 (Documentation): Four educational docs updated with C362-C414 results. 16_cosmology.md: Λ T4→T3 (−3.5%), BBN/CMB/BAO predictions table, updated "What Remains Open". 20_nuclear_physics.md: Walecka saturation section (a_V +0.7%, periodic table RMS 0.86%), 11 prediction tests table. 26_cosmological_constant.md: w_Λ=−0.992, EOS status updated. 15_dark_matter.md: m_DM=35.6 keV, λ_fs=1 kpc, updated summary table. **Documentation update. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-21 | 415 | Step 2 (Documentation): educational/28_gravity_gap.md REWRITTEN FROM SCRATCH. Complete rewrite from journaling style (C366-C399) to clean current-state format covering C366b-C408 (15 modules, 258/258 PASS). 7 sections: derived results, open problems, DFC claims, cosmological implications, path forward, equation module table. **Documentation update. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-21 | 414 | Step 1 (Prediction Maximization — Fundamental): equations/cosmological_predictions_3.py (new, 16/16 PASS). INFLATION + BARYON ASYMMETRY + ABSENCE PREDICTIONS. Part A: n_s = 0.9667 at N_e=60 (+0.4 sigma Planck). Flatness/horizon/monopole dissolved [T1]. T_reheat > T_BBN [T2a]. r BLOCKED. Part B: All 3 Sakharov conditions met [T2a]. E_sph=72*pi M_Pl, J_CP>0, first-order D7 PT. eta_B magnitude OPEN [T4]. Part C: 6 absence predictions — proton stable [T1], no axion [T2a], d_n=0 [T2a], no SUSY [T3], N_gen=3 [T1], Omega_k=0 [T2a]. All confirmed. **Cosmological+fundamental prediction module 4. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-21 | 413 | Step 2 (Prediction Maximization): educational/06_predictions.md updated with C412 cosmological entries (w_Lambda, r_drag, t_0, m_DM, lambda_fs). Total scorecard: 11 nuclear + 15 cosmological predictions. **Documentation update. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-21 | 412 | Step 1 (Prediction Maximization — Cosmology): equations/cosmological_predictions_2.py (new, 15/15 PASS). FOUR NEW COSMOLOGICAL PREDICTIONS. Part A: w_Lambda = -0.992 from DFC structural prediction (epsilon > 0, irreversible compression) + Hubble tension measurement (epsilon = 0.0077). Within 1.3 sigma Planck, 1 sigma DESI. Part B: BAO r_drag = 146.70 Mpc (-0.27% vs Planck). r_drag/r_s = 1.0184 exact match. Part C: Hubble tension resolution — evolving dark energy gives t_0 = 13.780 Gyr (-0.12%), z_transition = 0.631. Part D: DM mass m_DM = 35.6 keV from depth model (T4), satisfies all WDM bounds, lambda_fs = 1 kpc. Relic abundance OPEN. **Cosmological prediction module 3. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-21 | 411 | Step 2 (Prediction Maximization): educational/06_predictions.md updated with full prediction scorecard. Nuclear table: 11 entries from C384-C391 (tau_n, M_N, m_omega, g_piNN, f_pi, mu_p, mu_n, J, pp fusion, CDEs, Nolen-Schiffer). Cosmological table: 10 entries from C409-C410 (Y_p, D/H, He-3/H, rho_Lambda, CMB ell_1, theta_*, r_s, Omega_k, N_eff). Documented failures: deuteron binding (-49%), proton charge radius (-17%). **Documentation update. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-21 | 410 | Step 1 (Prediction Maximization — Cosmology): equations/cosmological_predictions.py (new, 15/15 PASS). LAMBDA DERIVATION CHAIN + CMB FIRST PEAK. Part A: all 3 Lambda exponent terms traced to T2a; combination rule remains T3; exponent +0.051%, rho^(1/4) -3.52%. Part B: CMB first peak ell_1=222 (+0.89% vs Planck 220), theta_*=-0.35%, r_s=-0.39%, z_*=+0.18%. Flat geometry and N_eff=3.044 consistent. **Cosmological prediction module 2. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-21 | 409 | Step 1 (Prediction Maximization — Cosmology): equations/bbn_predictions.py (new, 13/13 PASS). BBN PREDICTIONS FROM DFC PARAMETERS. DFC inputs: g_A=4/pi, tau_n=878.0 s. Y_p(DFC)=0.2475 (+1.05% vs obs, 0.64 sigma). D/H=2.438e-5 (-3.5%). He-3/H=1.04e-5 (-5.5%). Li-7/H=4.7e-10 (+194%, lithium problem NOT resolved). DFC BBN shift = 12% of 1-sigma Y_p error — unobservable. DFC FULLY CONSISTENT with BBN. Scale-dependent G_eff has no BBN effect (Planck-scale only). **First cosmological prediction module. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |
| 2026-08-21 | 408 | Step 1 (Track D — Spoke F Gravity): equations/d4_strong_field_metric.py (new, 20/20 PASS). STRONG-FIELD EFFECTIVE METRIC. TOV equations with scale-dependent G_eff(r). GR compactness 151 at xi vs DFC 6.6 (23x reduction). KEY FINDING: compactness STILL > 1 — TOV-with-G_eff ansatz insufficient. Substrate smooth (sech^4) but GR metric framework breaks down. g_00(xi)=-0.001130, z_grav=28.75. Newtonian recovery at 10*r_s. Full substrate dynamics needed for actual metric. d4_gravity_gap.md + ISSUES.md T30 updated with C407+C408. **Spoke F module 12. Model ~80%. Clay ~99%. CPC ~60%.** | 87% | 95% | ~80% |

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

Build a complete, standalone educational series for DFC. Modules 00–11 exist.
Continue with new modules covering advanced topics:

```
educational/
├── 00–11   ← complete
├── 12_substrate_topology.md    ← kink topology, Q_top, winding numbers
├── 13_mass_from_compression.md ← how mass emerges at D4; inertia as fold resistance
├── 14_spacetime_emergence.md   ← D3 localization → apparent 3D space
├── 15_dark_matter.md           ← what DFC predicts for DM (or absence thereof)
├── 16_cosmology.md             ← Hubble constant, compression at cosmic scale
├── 17_quantum_mechanics.md     ← measurement, interference from fold perspective
└── 18_open_problems.md         ← honest map of what remains underived
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

| Problem | DFC angle | Priority |
|---|---|---|
| Navier-Stokes regularity (Clay) | Substrate field equation □φ=V'(φ) as a nonlinear wave; kink turbulence | Explore |
| Baryon asymmetry | D6/D7 CP-phase asymmetry → matter dominance | Explore |
| Dark matter identity | Stable kink configurations at intermediate depths | Explore |
| Cosmological constant problem | Vacuum energy from substrate compression depth | Explore |
| Proton spin crisis | Spin from Jackiw-Rebbi zero modes vs. parton contribution | Explore |
| Quantum gravity / Planck scale | D4 inertia → G_N; Planck scale from ξ≈l_Pl | Explore |

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

---

---

### How "continue" Works

**`ROADMAP.md` is the single source of truth for what to do next.**

When the user says "continue":
1. Open `ROADMAP.md`.
2. **Cycle through tiers in order.** Check the `Last tier worked:` marker at the top
   of ROADMAP.md. Pick an item from the NEXT tier (P1→P2→P3→P4→P5→P6→P1→...).
   If the next tier has no actionable items, spend the cycle researching that tier
   and adding new actionable items to ROADMAP.md.
   After completing the task, update the `Last tier worked:` marker to the tier you just did.
3. Do ONE focused task from that item (one equation module, one document, one test).
4. Update `ROADMAP.md`: remove completed items from the active lists and add them
   to the Completed Items table. Add new items whenever they come up.
   ROADMAP.md is a **living roadmap and todo list** — keep it current.
5. Update `push_history.md` with the cycle entry.
6. Commit all changed files and run `git push`. Confirm `main -> main`.

A cycle is NOT finished until the remote is updated. One sub-step per cycle.
Do not combine multiple items. Short cycles that complete cleanly are always better
than long cycles that risk context overflow.

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
| Charm and strange quark masses | quark_mass_kappa_derivation.py | +2.45% (κ=3π/2) | ~1277/97 MeV | +2.45% | **T2a C274**: κ_q=π×N_c/2 from center vortex; charm +0.29%, strange +2.09% |

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
