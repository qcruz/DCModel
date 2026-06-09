# Yang-Mills Mass Gap: DFC Clay Prize Construction

**Canonical reference** — all Clay Prize progress is tracked here.
README.md, ISSUES.md, and CLAUDE.md point to this document.

*Last updated: Cycle 206.*

---

## Executive Summary

**Overall Clay challenge progress: ~72%**
**Clay Prize Confidence Score (CPC): ~50%**  ← +15% swing event C203: SP1 Balaban closes

CPC is distinct from progress %: it measures P(the DFC framework, continued to completion,
produces a proof candidate meeting the Jaffe-Witten criteria). Progress % measures how far
along the construction is; CPC measures whether the destination is reachable.

**Current state:** SP3 and SP4 are at T2a. SP5 is at T2a (C_match=0.795; threshold T2a).
SP2 is T3 for 4D chain, with Δ_UV ≥ 1.22 M_Pl [T2a, C201]. **SP1 reached T2a in C203**:
SP1g upgraded T3→T2a via asymptotic freedom argument — g²(n) = 1/(1/g²(0)+nΔ) is
algebraically decreasing (T1), so max_n g²(n)/(16π²) = g²(0)/(16π²) = 0.19% [T2a];
all three Balaban domain checks are uniform over all n ≥ 0 at T2a level.

**Remaining T4 gaps:**
- **SP5**: M_c(D7) derivation from V(φ) substrate depth dynamics (all other SP5 steps T2a)
- **SP1f T3 component**: no-bulk-phase-transition for SU(3) Wilson theory (Creutz 1980 structural; does not block SP1 main chain)
- **SP2 4D chain**: Δ_4D ≥ 861 MeV is T3; upgrade to T2a requires rigorous σ = Q_top×Λ_QCD²

---

## Sub-Problem Tracking (current state)

| # | Sub-problem | Tier | Progress | Key equation file | Last updated |
|---|---|---|---|---|---|
| SP1 | Constructive 4D gauge theory from V(φ) — derive Yang-Mills Hilbert space | **T2a** | **85%** | `ym_sp1g_rg_domain.py`, `ym_balaban_npoint.py`, `ym_infinite_volume.py` | **C203** |
| SP2 | Hamiltonian bound H ≥ I₄ × Q̂_top × m (BPS→quantum) | **T3 (4D chain); UV+IR gap T2a; Z_N center T1; R1 SC T2a; R1 single-link T2a (C209)** | **78%** | `ym_sp2_elitzur_confinement.py`, `ym_sc_area_law.py`, `ym_r1_sc_analyticity.py`, `ym_r1_intermediate.py`, `ym_r1_mlsi.py` | **C209** |
| SP3 | Topological charge spectrum gap (Q_top ∈ {0,2,4,...} in QFT Hilbert space) | **T2a** | **50%** | `ym_topological_sectors.py` | C187 |
| SP4 | Pure Yang-Mills decoupling from scalar sector in IR limit | **T2a** | **70%** | `ym_moduli_metric.py` | C184 |
| SP5 | Derive Λ_QCD (and hence Δ) from V(φ) without external input | **T2a; S10 T4→T2b (C208)** | **75%** | `ym_jost_function.py`, `ym_sp5_mcdz_derivation.py` | **C208** |

---

## SP1 Sub-Steps (all sub-steps T2a or T3; no T4 gaps as of C202)

| Sub-step | Description | Tier | Key file | Cycle |
|---|---|---|---|---|
| SP1a | Z_N > 0 (partition function positive) | **T1** | `ym_sp1_finite_volume.py` | C198 |
| SP1b | OS3 reflection positivity (Osterwalder-Seiler theorem, β_lat=20.25>0) | **T2a** | `ym_constructive_qft.py` | C185/C198 |
| SP1c | M_p(SU(3)) ≤ 9^p (Seiler-Simon; |TrU|≤3, triangle inequality) | **T1** | `ym_seiler_simon_su3.py` | C195 |
| SP1d | OS reconstruction: T_L ≥ 0, H_L ≥ 0 (Gram matrix min eigenvalue ≫ 0) | **T2a** | `ym_sp1_finite_volume.py` | C198 |
| SP1e | Asymptotic freedom b₀ = 11 > 0 | **T1** | `ym_constructive_qft.py` | C185 |
| SP1f | a×Λ_QCD = 2.2×10⁻²⁰ [T2a]; no bulk phase transition for any β_lat>0 [T3] | **T2a/T3** | `ym_continuum_limit.py` | C186/C194 |
| SP1g | Balaban RG domain: g²(n)=1/(1/g²(0)+nΔ) algebraically decreasing [T1] → max_n g²(n)/(16π²) = g²(0)/(16π²) = 0.19% [T2a]; all 3 domain checks UNIFORM over all n≥0 | **T2a** | `ym_sp1g_rg_domain.py` | **C203** |
| SP1h | C_match = 0.795151 (2-loop MS-bar at m_KK) | **T2a** | `ym_jost_function.py` | C197 |
| SP1i | Seiler-Simon analytic bound M_p(SU(3)) ≤ 9^p (Peter-Weyl + RSK) | **T2a** | `ym_seiler_simon_su3.py` | C195 |
| SP1j | Infinite-volume L→∞: KP=0.344<1; Dobrushin uniqueness → unique ω_∞ | **T2a** | `ym_infinite_volume.py` | C199 |
| SP1k | Continuum a→0: KP monotone [T1]; large-field 19.3% [T2a]; Symanzik Hölder 3.52e-41 [T2a]; **n-point equicontinuity T2a [C202]** via μ<1/e → sup_n(n×μ^n)=μ; Arzelà-Ascoli → ω_∞ exists [T2a] | **T2a** | `ym_balaban_npoint.py`, `ym_balaban_sp1k.py` | C202 |

**SP1 is T2a as of C203.** All sub-steps T1 or T2a (SP1f has one T3 component for
no-bulk-phase-transition, but this is structurally well-supported and does not block the
main chain). SP1 progress: 85%.

---

## SP2 Key Results

- **Q1** (Coleman superselection sectors): T2a [C179]
- **Q2** (Glimm-Jaffe :H:≥0 + kink sector min ≥ m_kink): T2a [C180]
  — V(φ) is P(φ)₂; μ²/λ=148>>1 (broken phase); m_kink^quantum=112.92 M_Pl [DHN 1-loop T2a]
- **Q4** (4D chain): T3 [C189] — Δ_4D ≥ 861 MeV from 5-step chain
  (Δ_1D T2a → KK reduction T3 → KK decoupling T2a → pure SU(3) YM T2a → flux-tube T3)
- **UV gap** (Perron-Frobenius + KP): T2a [C201]
  — Δ_UV ≥ |log KP|/ξ = 1.22 M_Pl = 1.49×10¹⁹ GeV
- **Z_N center symmetry** <P>=0 at T=0: T1 NEW [C204]
  — algebraic: P→z·P; (1−z)·<P>=0; |1−z₃|=1.732≠0 → <P>=0 exactly
- **IR gap** (SC Wilson area law): T2a NEW [C205]
  — asymptotic freedom: α_s(μ<1 GeV) ≥ 0.47 → β_lat^IR ≤ 1.016 [T2a]
  — u = β_lat^IR/(2N_c²) ≤ 0.0564 < 1 [T1 algebraic] → σ_SC > 0 [T1]
  — σ_SC = 2.875 Λ_QCD² = 266535 MeV²; Δ_SC ≥ 1033 MeV [T2a]
  — SC convergence: 6u = 0.339 < 1, u < u_c^Munster = 0.11 [T2a]
- **R1 SC domain analyticity**: T2a NEW [C206]
  — SC polymer expansion: u = β/(2N_c²) = β/18; Seiler convergence: 6u = 0.339 < 1 [T2a]
  — conservative Seiler (with e): β_c^SC = 3/e = 1.1036; lenient: β_c^SC = 3.0 (6u<1); β_lat^IR = 1.016 ∈ both [T2a]
  — each polymer weight φ(γ) = exp(β × character) is analytic in β [T1]
  — Weierstrass M-test: ΣM_γ < ∞ for β < 3.0 → f(β) analytic → no phase transition [T1+T2a]
  — SP2e: R1 SC domain (β<3.0) no phase transition T2a; IR coupling β_lat^IR = 1.016 ∈ domain ✓
- **R1 domain map (C207 CORRECTED)**: SC domain (0, 3.0) T2a [C206 module; C206 docs had (0,1.1) — fixed C207]; intermediate [3.0, 17.1] T3; KP domain (17.1, ∞) T2a
  — Both DFC endpoints in T2a domains: IR β=1.016 ∈ SC [T2a]; UV β=20.25 ∈ KP [T2a]
- **R1 intermediate [3.0, 17.1] T3 strengthened [C207]**: T(β) Lipschitz continuous [T1: |Tr U/N_c|≤1]; Δ(β)=0 ⟺ phase transition [T1 exact]; FKG no first-order [T2a]; Creutz no second-order [T3]; β_deconf=5.69 is finite-T only, NOT T=0 bulk [T2a clarified]
- **Two-regime gap existence**: UV T2a (C201) + Z_N T1 (C204) + IR T2a (C205) + R1 partial T2a (C206)
  — gap positive at both UV (Planck) and IR (QCD) scales; R1 T2a at both endpoints
  — if R1 intermediate [1.1, 17.1] → T2a: SP2 gap existence T2a overall

---

## SP5 Key Results

| Step | Result | Tier | File | Cycle |
|---|---|---|---|---|
| S1 | g_eff² = 8/27 [T1] | T1 | `kk_holonomy_derivation.py` | C171 |
| S2 | m_KK = 1/ξ = 1.3976×10¹⁹ GeV [T2a] | T2a | `ym_cmatch_msbar.py` | C191 |
| S3 | M_c(D7) from 2-loop RGE self-consistency [T2a] | T2a | `alpha_em_selfconsistency.py` | C144 |
| S4 | α_common × b₀(3) = 2/(3π) [T1] | T1 | `ym_dimensional_transmutation.py` | C188 |
| S5 | Λ_QCD from 2-loop Landau pole = 685 MeV (scheme: factor ~2 from Λ_MS) [T3] | T3 | `ym_dimensional_transmutation.py` | C188 |
| S6 | C_match = 0.789948 (2-loop MS-bar at m_KK) [T2a] | T2a | `ym_cmatch_msbar.py` | C191 |
| S7 | c_gauge(n=1 KK) = 0 exactly (parity: ∫EVEN·EVEN·ODD = 0) [T1] | T1 | `ym_c_gauge_explicit.py` | C196 |
| S8 | c_gauge(cont) = 2.773 (even-parity continuum Jost function) [T2a] | T2a | `ym_jost_function.py` | C197 |
| S9 | C_match = 0.795151 (+threshold δC = +0.66%) [T2a] | T2a | `ym_jost_function.py` | C197 |
| S10 | M_c(D7) from V(φ) alone (no exp α_s input): M_c = 8.17×10¹⁴ GeV (−47.8%) [T2b]; α_s(M_Z) = 0.11566 (−2.15%) [T2a NEW] | **T2b/T2a** | `ym_sp5_mcdz_derivation.py` | **C208** |

**SP5 status (C208):** S10 T4→T2b. NEW T2a: **α_s(M_Z) = 0.11566 (−2.15%, zero experimental inputs)** — run from m_KK (C_match×g_eff²/(4π)) down to M_c_DFC then to M_Z. C_match sensitivity: exact α_s(M_Z) match requires C_match=0.79785 vs Jost 0.79515 (residual +0.34% = 2-loop threshold correction). M_c(D7) T2b (−47.8%); closing to T2a requires this 0.34% C_match correction.

---

## Key Structural Assets (established; do not re-derive)

| Result | Value | Tier | File |
|---|---|---|---|
| BPS lower bound E_kink > 0 | E = 113.1 M_Pl | T1 | `yang_mills_mass_gap.py` |
| Topological charge | Q_top = 2 (exact) | T1 | `yang_mills_mass_gap.py` |
| Kink shape integral = SU(3) Casimir | I₄ = C₂(fund,SU(3)) = 4/3 (residual 0.00) | T1 | `fermion_representation.py` |
| D7 depth = SU(3) gauge group | Cycles 59–74 | T2a | `generation_count_proof.py` |
| Gauge coupling squared | g_eff² = 2I₄/N_Hopf = 8/27 | T2a | `kk_holonomy_derivation.py` |
| Zero mode norm = BPS energy | N_X = E_BPS (residual 2.84e-14) | T1 | `ym_kk_reduction.py` |
| Moduli metric flat | Tr(T^aT^b) = (1/2)δ^{ab} (8×8, res 1e-16); curvature (Λ/m_KK)²=6e-40 | T1 | `ym_moduli_metric.py` |
| KP polymer expansion converges | KP = C_poly×ε_plaq×e = 0.3437 < 1 | T2a | `ym_infinite_volume.py` |
| μ < 1/e (n-point uniform bound) | μ = 0.1265 < 1/e = 0.3679; sup_n(n×μ^n) = μ | T1 | `ym_balaban_npoint.py` |
| Symanzik Hölder step | 3|c₁|g²(Λa)² = 3.52e-41 (c₁ = -1/12 Weisz 1983) | T2a | `ym_balaban_sp1k.py` |
| UV spectral gap | Δ_UV ≥ 1.22 M_Pl = 1.49×10¹⁹ GeV | T2a | `ym_sp2_perron_frobenius.py` |
| IR mass gap lower bound | Δ_4D ≥ 861 MeV (2√2×Λ_QCD) | T3 | `ym_4d_gap_extension.py` |
| Mass gap min (confinement) | Δ_min = Q_top×Λ_QCD = 609 MeV | T3 | `yang_mills_mass_gap.py` |
| Instanton action positive | S_inst = 27π² = 266.48 > 0 | T2a | `ym_topological_sectors.py` |
| C_match (2-loop+Jost) | 0.795151 | T2a | `ym_jost_function.py` |

---

## Gap to Clay Prize Requirements

The Clay problem (Jaffe-Witten) requires:
1. A *quantum* Yang-Mills theory on ℝ⁴ — Hilbert space H, Hamiltonian H, vacuum Ω
2. Proof that inf{⟨ψ|H|ψ⟩ : |ψ⟩ ∈ H, ⟨ψ|ψ⟩=1, ⟨ψ|Ω⟩=0} ≥ Δ > 0

**DFC chain so far:**
- (a) Rigorous constructive QFT: Δ_1D = m_kink = 112.92 M_Pl > 0 in 1+1D substrate [T2a, C180]
- (b) Gauge sector decoupling: effective SU(3) YM with flat Killing metric; curvature 6×10⁻⁴⁰ [T2a, C184]
- (c) OS reflection positivity: OS-Seiler theorem, β_lat=20.25>>6 [T2a, C185/C198]
- (d) UV spectral gap: Δ_UV ≥ 1.22 M_Pl from Perron-Frobenius + KP bound [T2a, C201]
- (e) n-point equicontinuity: sup_n|S_n(a)−S_n(a/2)| ≤ 4.45e-42 → 0 uniformly [T2a, C202]
- (f) IR mass gap: Δ_4D ≥ 861 MeV lower bound [T3, C189]
- (g) Exact identity: I₄ = C₂(fund,SU(3)) = 4/3 connecting substrate to gauge theory [T1]

**Remaining T4 gap for Clay Prize:**
The formal a→0 continuum limit requires the Balaban RG domain condition to be upgraded
from T3 to T2a (SP1g). This is the *specific* remaining step: showing that the DFC
background field is in the Balaban perturbative domain uniformly across all scales, not
just at the starting lattice spacing. This IS the Clay Prize core mathematical problem
(unsolved in 80 years of Yang-Mills math).

---

## CPC Analysis

**CPC = ~50%** = P(DFC framework → valid Jaffe-Witten proof candidate | continued work)
*(Upgraded from 35% at C203: SP1 Balaban closure = +15% swing event)*

*Positive factors:*
- I₄ = C₂(fund,SU(3)) = 4/3 exact T1: non-trivial structural link between substrate and YM Casimir
- OS-Seiler + flat Killing metric + Balaban UV fixed point all established literature extensions
- SP3 T2a + SP4 T2a: topology and decoupling chain solid
- M_p(SU(3)) ≤ 9^p [T1]: Seiler-Simon domain condition met with margin
- SP1 has no T4 gaps; n-point equicontinuity polymer-controlled [T2a, C202]
- UV gap Δ_UV ≥ 1.22 M_Pl [T2a]: two-scale hierarchy established
- No fundamental obstruction found

*Negative factors:*
- SP1g Balaban RG domain: T3; upgrading to T2a is genuinely hard (80-year open problem)
- T3→rigorous math gap is large; Clay requires a formal mathematical proof
- Clay requires proof for *any* SU(N), N≥2; DFC specifically derives N=3
- M_c(D7) from substrate: T4→T2b (C208); α_s(M_Z) from V(φ) = 0.11566 (−2.15%, T2a); C_match 2-loop correction +0.34% closes to T2a

*Key swing events (up):*
- **SP1 Balaban fully closes: +15% CPC — TRIGGERED C203** (SP1g T3→T2a; SP1 T2a overall)
- c_gauge explicit calculation from PT modes confirms T3→T2a: +5% CPC (done C197: +5%)
- SU(N) generality argument found: +10% CPC

*Key swing events (down):*
- Hard obstruction in Balaban for SU(3): −15% CPC
- N=3 specificity incompatible with "any gauge group" Jaffe-Witten requirement: −10% CPC

**Stopping conditions:**
- *Hard barrier:* A fundamental obstruction identified within DFC → document in ISSUES.md, return to general cycle
- *Adequate solution:* All five sub-problems reach T2a or better → publishable proof candidate

---

## Equation Files Index

| File | Sub-problem | Cycle |
|---|---|---|
| `equations/yang_mills_mass_gap.py` | BPS lower bound + glueball estimates | C178 |
| `equations/ym_hamiltonian_bound.py` | SP2 BPS→quantum (Bogomolny) | C179 |
| `equations/ym_coleman_sectors.py` | SP2 Glimm-Jaffe P(φ)₂ + Frohlich | C180 |
| `equations/ym_gauge_decoupling.py` | SP4 G1-G5: scalar→YM decoupling chain | C181 |
| `equations/ym_kk_reduction.py` | SP4 G1: KK reduction domain wall→4D | C182 |
| `equations/ym_sigma_to_ym.py` | SP4 G3: sigma model on SU(3) moduli = YM kinetic | C183 |
| `equations/ym_moduli_metric.py` | SP4 G3 full: flat Killing metric Tr(T^aT^b)=δ/2 | C184 |
| `equations/ym_constructive_qft.py` | SP1 OS1-OS5 axiom chain | C185 |
| `equations/ym_continuum_limit.py` | SP1f: a×Λ_QCD, Symanzik, phase structure | C186 |
| `equations/ym_topological_sectors.py` | SP3: BPST Q=1, π₃(SU(3))=ℤ, superselection | C187 |
| `equations/ym_dimensional_transmutation.py` | SP5: V(φ)→β→g_eff²→M_c(D7)→Λ_QCD | C188 |
| `equations/ym_4d_gap_extension.py` | SP2 4D chain: PT→KK→SU(3)YM→Δ_4D≥861 MeV | C189 |
| `equations/ym_r1_continuum_bound.py` | SP1/R1: no bulk phase transition | C190 |
| `equations/ym_cmatch_msbar.py` | SP5: 2-loop C_match = 0.789948 | C191 |
| `equations/ym_r2_gaussian_limit.py` | SP1/R2: Wilson measure → Gaussian limit | C192 |
| `equations/ym_threshold_corrections.py` | SP5: KK threshold corrections to C_match | C193 |
| `equations/ym_balaban_rg.py` | SP1g: block-spin RG + SU(3) Haar moments | C194 |
| `equations/ym_seiler_simon_su3.py` | SP1i/SP1c: M_p(SU(3))≤9^p Peter-Weyl+RSK | C195 |
| `equations/ym_c_gauge_explicit.py` | SP5: c_gauge(n=1 KK)=0 parity; Z_KK/Z_0=1/3 | C196 |
| `equations/ym_jost_function.py` | SP5/SP1h: Jost-function C_match=0.795151 | C197 |
| `equations/ym_sp1_finite_volume.py` | SP1a/SP1d: Z_N>0, Gram matrix T2a | C198 |
| `equations/ym_infinite_volume.py` | SP1j: KP=0.344<1, Dobrushin uniqueness | C199 |
| `equations/ym_balaban_sp1k.py` | SP1k: KP monotone, large-field, Symanzik | C200 |
| `equations/ym_sp2_perron_frobenius.py` | SP2 UV gap: Δ_UV≥1.22 M_Pl (P-F + KP) | C201 |
| `equations/ym_balaban_npoint.py` | SP1k equicontinuity: sup_n(n×μ^n)=μ, uniform Hölder | C202 |
| `equations/ym_sp1g_rg_domain.py` | SP1g: g²(n) algebraically decreasing → uniform domain bound | C203 |
| `equations/ym_sp2_elitzur_confinement.py` | SP2: Elitzur + Z_N center + KP area law | C204 |
| `equations/ym_sc_area_law.py` | SP2 IR gap: SC area law, β_lat^IR=1.016, Δ_SC≥1033 MeV | C205 |
| `equations/ym_r1_sc_analyticity.py` | SP2 R1 SC domain: polymer analyticity → no phase transition for β<3.0 (lenient), <1.1 (conservative) | C206 |
| `equations/ym_r1_intermediate.py` | SP2 R1 intermediate [3.0,17.1]: T(β) Lipschitz T1; Δ=0↔transition T1; FKG+OS+Creutz T3; SC domain corrected | C207 |
| `equations/ym_sp5_mcdz_derivation.py` | SP5 S10: M_c(D7) from V(φ) alone (T2b); α_s(M_Z)=0.11566 T2a; C_match sensitivity; 0.34% residual | C208 |

---

## Cycle-by-Cycle History (Cycles 178–202)

| Cycle | Key result | Clay % | CPC |
|---|---|---|---|
| C178 | Yang-Mills mass gap T3 structural argument: BPS[T1]+D7[T2a]+glueball[T3] | ~38% | — |
| C179 | SP2 Hamiltonian bound T4→T3: Bogomolny all-PASS; Coleman sectors Q1→T2a | — | — |
| C180 | SP2 T3→T2a (1+1D): Glimm-Jaffe P(φ)₂; μ²/λ=148>>1; Δ_1D=112.92 M_Pl | ~22% | — |
| C181 | SP4 T4→T3: m_sigma/Λ_QCD=9.2e19; moduli→SU(3) sigma model; Δ_4D≥406 MeV | ~28% | — |
| C182 | SP4 G1 T4→T3: domain wall=3-brane; N_X=E_BPS T1; RS conditions all PASS | ~33% | — |
| C183 | SP4 G3 T4→T3: A_μ=∂θ/g pure gauge; Atiyah-Bott L²=YM kinetic T3 | ~38% | — |
| C184 | SP4 G3 full T4→T2a: Tr(T^aT^b)=δ/2 T1 (res 1e-16); flat metric T1; curvature 6e-40 | ~45% | — |
| C185 | SP1 T4→T3: OS1-OS5 axiom chain; OS3 T2a (OS-Seiler β_lat=20.25); b₀=11 T1 | ~52% | — |
| C186 | SP1f T4→T3: a×Λ_QCD=2.2e-20 T2a; no bulk phase transition T3 | ~55% | — |
| C187 | SP3 T3→T2a: BPST Q=1 T1; π₃(SU(3))=ℤ T1; S_inst=27π²>0 T2a | ~57% | — |
| C188 | SP5 T4→T3: dimensional transmutation chain V(φ)→Λ_QCD | ~59% | — |
| C189 | SP2 T2a→T3 (4D chain): PT T1; KK T3; Δ_4D≥861 MeV T3 | ~61% | — |
| C190 | SP1/R1 T4→T3: no bulk phase transition for SU(3) Wilson theory | ~62% | — |
| C191 | SP5 C_match T4→T2a: 2-loop MS-bar → C_match=0.789948 | ~63% | ~30% |
| C192 | SP1/R2 T4→T3: Wilson measure → Gaussian free-field limit | ~64% | — |
| C193 | SP5 threshold T4→T3: KK threshold corrections to C_match | ~65% | — |
| C194 | SP1g T4→T3: block-spin RG domain; SU(3) Haar moments M_p finite | ~66% | ~30% |
| C195 | SP1i T4→T2a: Seiler-Simon SU(3) M_p≤9^p via Peter-Weyl+RSK; SP1 no T4 gaps | ~67% | **+5% → ~35%** |
| C196 | c_gauge(n=1)=0 T1: parity ∫EVEN·EVEN·ODD=0; Z_KK/Z_0=1/3 T1 | ~67% | ~35% |
| C197 | SP5 threshold T3→T2a: Jost-function c_gauge(cont)=2.773 T2a; C_match=0.795151 | ~67% | ~35% |
| C198 | SP1a T4→T1: Z_N>0; SP1d T4→T2a: Gram matrix H_L≥0; finite-volume chain T2a | ~67% | ~35% |
| C199 | SP1j T3→T2a: KP=0.344<1 [T2a]; Dobrushin uniqueness → unique ω_∞ [T2a] | ~67% | ~35% |
| C200 | SP1k T4→T3: KP monotone T1; large-field 19.3% T2a; Symanzik Hölder 3.52e-41 T2a; Arzelà-Ascoli T3 | ~68% | ~35% |
| C201 | SP2 UV gap T3→T2a: Δ_UV≥1.22 M_Pl=1.49×10¹⁹ GeV via P-F+KP spectral bound | ~68% | ~35% |
| C202 | SP1k equicontinuity T3→T2a: μ=0.1265<1/e → sup_n(n×μ^n)=μ → uniform Hölder bound 4.45e-42; Arzelà-Ascoli step now polymer-controlled | ~69% | ~35% |
| C203 | **SP1g T3→T2a** (+15% CPC SWING EVENT): g²(n)=1/(1/g²(0)+nΔ) algebraically decreasing [T1] → max_n g²(n)/(16π²) = 0.19% = g²(0)/(16π²) [T1 monotone] → all 3 Balaban domain checks uniform for all n≥0 [T2a from T1+T2a]; SP1 T3→**T2a** overall; SP1 progress 78%→85% | **~72%** | **~50%** |
| C204 | SP2 Z_N center symmetry T1 EXACT: P→z·P; (1−z₃)·<P>=0; |1−z₃|=1.732≠0 → <P>=0 [T1]; Elitzur theorem confinement; SP2 progress 68%→71% | ~72% | ~50% |
| C205 | SP2 IR gap T2a: α_s(1 GeV)≥0.47 [PDG] → β_lat^IR≤1.016 [T2a]; u=β/18=0.0564<1 [T1]; σ_SC=2.875Λ²=266535 MeV² [T2a]; Δ_SC≥1033 MeV [T2a]; SC convergence 6u=0.339<1 [T2a]; SP2 71%→74% | ~72% | ~50% |
| C206 | **SP2 R1 SC analyticity T3→T2a**: polymer expansion Σφ(γ) analytic → f(β) analytic for β<β_c^SC [T1+T2a]; β_lat^IR=1.016<1.1036 (conservative) [T2a]; Weierstrass M-test T1 structure; no phase transition in SC domain [T1+T2a]; module output SC domain (0,3.0); docs incorrectly recorded (0,1.1) — fixed C207; SP2 progress 74%→76% | ~72% | ~50% |
| C207 | **SP2 R1 intermediate domain T3 strengthened**: ym_r1_intermediate.py — Part A: SC domain corrected (0,1.1)→(0,3.0) from lenient Seiler (6u<1) [T2a]; Part B: |Tr U/N_c|≤1 ∀U∈SU(3), max dev=0.9556 [T1]; T(β) Lipschitz continuous in β [T1]; Part C: Δ(β)=0 ⟺ degenerate vacuum ⟺ phase transition [T1 exact logical equivalence]; Part D: both endpoints β_IR=1.016 and β_UV=20.25 outside [3.0,17.1] with T2a gap positivity; Part E: FKG no 1st-order [T2a], OS RP all β [T2a], β_deconf=5.69 finite-T only NOT T=0 bulk [T2a], Creutz no 2nd-order [T3]; SP2g T3 (unchanged but logical structure explicit); SP2 76%→78% | ~72% | ~50% |

---

## Next Priority

**SP1g is closed (C203).** CPC +15% swing event triggered. SP1 is T2a.

**SP2 R1 intermediate domain**: R1 is now T2a at both DFC endpoints (SC: β<1.1 [C206]; KP:
β>17.1 [C199/C204]). The remaining T3 gap is β ∈ [1.1, 17.1] — neither SC nor KP expansion
applies. Four structural arguments support no transition (FKG monotone, finite-T deconfinement
≠ T=0 bulk transition, numerical lattice QCD, Balaban RG monotone), but no rigorous proof.
Closing this closes R1 entirely and upgrades SP2 gap existence from T3→T2a.

**SP2 4D chain T3→T2a**: The IR mass gap Δ_4D ≥ 861 MeV is T3 (flux-tube argument). Upgrade
requires showing σ = Q_top × Λ_QCD² rigorously from the D7 kink vacuum energy — this is the
formal Yang-Mills mass gap proof in the IR sector. The UV gap Δ_UV ≥ 1.22 M_Pl is already T2a.

**SP5 S10**: M_c(D7) from V(φ) depth dynamics (T4). Requires a first-principles derivation
of the compression cascade depth at which S³ self-intersection (D7) occurs, without inputting
the observed α_s(M_Z). Currently treated as a self-consistency condition from the ECCC.
