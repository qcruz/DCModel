# DFC Model — Open Issues

**Last updated:** Cycle 386 (2026-08-15)

This document tracks currently open issues in the DFC model. For detailed development
priorities, see `DEVELOPMENT_NEXT_STEPS.md`. For cycle-by-cycle history, see
`push_history.md` and `CLAUDE.md`.

---

## Currently Open Issues

### T8 — ℏ Hierarchy

S_kink(D1) = 1.13×10⁴⁰ ℏ reduces through ~4 bifurcations to ~10²⁸ ℏ residual.
ℏ cannot be derived from (α, β, c) alone without SI unit system identification.
Blocked by T12 (α_em chain must close first, then connect via α_em = e²/(4πε₀ℏc)).

**Status:** T4 open. **Files:** `planck_constant_derivation.md`

---

### T10 — θ₂₃ Neutrino Mixing Angle: 4° Deviation from 45°

DFC predicts θ₂₃ = 45° from Z₂ (μ↔τ) symmetry at D6 [T3]. Observed θ₂₃ ≈ 49°.
The C205 color correction δd = 1/(6π) does NOT shift θ₂₃ [T1 proved, C209] — T10 and
T11 are independent problems. Required asymmetry: ε_d ≈ 0.144 depth units (~2.7× δd).

**C364 Z₃ holonomy mechanism [T1 structural]:**
D7 SU(3) center Z₃ distinguishes tau (n=3, q=0, Z₃-neutral) from muon (n=2, q=2,
Z₃-charged). Center vortex factor F(q) = 1−cos(2πq/3): F(0)=0 for tau, F(2)=3/2
for muon. Asymmetry F(μ)−F(τ) = 3/2 is parameter-free [T1]. Sign prediction correct:
θ₂₃ > 45°. Multiple candidate formulas within 1σ of observed 49.26°: best candidates
ε_d = N_c/(2N_Hopf) = 1/6 → θ₂₃ = 49.75° (+0.49°), and ε_d = 1/(2π) → θ₂₃ = 49.54°
(+0.28°). Structural formula ε_d = F(2)/(2πI₄) = 9/(16π) → θ₂₃ = 50.1° (+0.84°).

**T4 candidates (2 remaining, mechanism identified):**
1. CKM-like D6/D7 interface mixing — Z₃ holonomy provides the structural source
2. Winding-number-dependent D4/D6 boundary condition asymmetry

(Candidate 3, CP phase shift, effectively ruled out — modern fits already marginalize δ_CP.)

**Status:** T4 open (mechanism identified T1, formula not derived from V(φ)).
**Files:** `equations/neutrino_theta23_z3_mechanism.py` (C364),
`equations/neutrino_theta23_correction.py` (C209),
`phenomena/particle_physics/neutrino_oscillations.md`

---

### T11 — Neutrino Mass Ratio m₃/m₂: Depth Correction

DFC κ = 5.33 vs observed m₃/m₂ ≈ 5.82 (−8.3% uncorrected, T2b). With color depth
correction δd = 1/(6π): m₃/m₂ = κ^(1+δd) = 5.8248 vs obs 5.8242 (+0.0096%, 0 free
params, 885× improvement). Three algebraically equivalent T1 forms for δd all trace to
the unifying identity N_c/N_Hopf = I₄−1 = 1/3.

C354 upgraded the depth shift mechanism from T3→T2a via JR-BPS derivation (17/17 PASS).

**Remaining open:** κ = 5.33 itself (T2b — D6 geometry); absolute neutrino mass scale
(requires f_ν from substrate dynamics).

**Status:** δd = 1/(6π) T2a; m₃/m₂ prediction T2a (+0.0096%); κ T2b.
**Files:** `equations/neutrino_depth_shift_bvp.py` (C354), `equations/neutrino_casimir_depth.py` (C349),
`equations/neutrino_color_correction.py` (C205), `equations/neutrino_d7_holonomy.py` (C219)

---

### T12 — α_em Chain: Hadronic Vacuum Polarization Gap

The DFC 36π chain predicts 1/α_em(M_Z) = 128.09 (+0.15%). The residual gap traces to
δ(Δα)^{NP} = 0.00102 — the non-perturbative hadronic VP contribution from ρ/ω/φ
resonances below √s ≈ 2 GeV. This same gap blocks the ECCC identity (Problems #1 and
#4 unified, proved T1 in C351). VP budget: DFC accounts for 98.5% of total VP at M_Z.

C356 computed the first quantitative dispersive integral: δ(Δα) = 0.004158 (4.08× target).
Overshoot from constant C_dual global duality model. C357–C358 attempted per-resonance
local duality: C357 narrow windows gave −0.63× (wrong sign); C358 wider windows (s_boundary
= 1.0 GeV, s_upper = 1.5 GeV) gave −0.35× (still wrong sign, improved). The two models
bracket the target: global +4.08× (too little subtraction) vs local −0.35× (too much
subtraction). Root cause: constant-C_dual model fundamentally over-subtracts when
C_dual > R_parton; exact closure requires D7 confinement spectral density (T4).

**Status:** T3 (two models bracket target; 4× and −0.35×); T4 for exact 0.00102 piece.
**Files:** `equations/hadronic_vp_dispersive.py` (C358), `equations/alpha_em_dfc_chain.py` (C351),
`equations/alpha_em_hadronic.py` (C158)

---

### T14 — Yang-Mills Clay Prize

Internally complete at ~99% proof standard. `equations/ym_clay_proof.tex` (12 citations,
zero T2a on critical path). 7/7 Jaffe-Witten criteria T1+cited. Sole remaining gap =
peer review. No further cycles planned unless a mathematical issue is found.

**Key parameters:** β_lat = 81/4 [T1], g_eff² = 8/27 [T2a], KP < 125/196 [T1],
Δ ≥ log(196/125) > 0 [T1+cited]. CPC: ~60%.

**Files:** `foundations/yang_mills_clay.md`, `equations/ym_clay_proof.tex`

---

### T15 — External AI Peer Review Points (Clay Prize)

10-point review conducted C319. Summary of outstanding items:

| Point | Status |
|---|---|
| 1. Clay-proper vs DFC-physics split | Documented C350; restructure planned |
| 2/3. I₄=C₂ selection mechanism | **Done C348** |
| 4. N_Hopf isometry error | **Fixed C317** |
| 5/6/10. Continuum limit a→0 | T2a; formal theorem C319 |
| 7. OS Reconstruction scope | **Addressed** |
| 8. Assumption A (JR holonomy) | **Closed C320** (T1+cited) |
| 9. Percentages as completeness claims | **Clarified** |

**Files:** `REVIEW_RESPONSE.md`

---

### T16 — Cosmological Constant

DFC reframes the 10¹²³ cancellation problem: deep-substrate and cosmic-scale energies
are at different compression depths and not additive. T3 structural argument.

C362: Quantitative prediction achieved (T3, 0 free parameters):
ρ_Λ = M_Pl⁴ × exp(-(27π² + 9π/2 + ∛18)). Exponent = 283.24 vs observed 283.09
(+0.05%). ρ_Λ^{1/4} = 2.16 meV vs observed 2.24 meV (−3.5%). Three terms:
S_inst = 27π² (instanton action, T2a), S_inst×δd = 9π/2 (neutrino depth correction,
T2a), α = ∛18 (compression parameter, T2a). Formula is T3 (structural, not derived
from V(φ)). Neutrino mass scale connection ρ_Λ^{1/4} ≈ m_ν noted but not derived.

**Status:** T3 quantitative prediction (was T4); structural reframe unchanged (T3, C328).
**Files:** `equations/cosmological_constant_prediction.py` (C362, 13/13 PASS),
`foundations/cosmological_constant_dfc.md` (C328)

---

### T17 — Nuclear Physics: N=126 Shell Closure

Six-step framework complete at T3. B(²⁹⁸Fl) = 2114 MeV = 7.09 MeV/nucleon [T3].
Magic numbers 2,8,20,28,50,82,**126** all reproduced [T3]. a_SO = I₄ × a₀ = 0.893 fm
[T3, 0.7% from FRDM].

C361: N=126 **CLOSED** via DFC effective SO strength κ_DFC = 33 = 36 × b₀/(4N_c) =
36 × 11/12 [T3]. The one-loop beta coefficient b₀=11 sets the fraction of SO coupling
surviving D7 confinement screening. Critical κ_c ≈ 33.27; κ_DFC = 33 safely below.
Gap at N=126: 1.07 MeV. All 7 standard magic numbers reproduced (24/24 PASS).

**T4 remaining:** N=184 superheavy magic number not reproduced at κ=33 in ²⁹⁸Fl spectrum.
Formal derivation of b₀/(4N_c) correction from D7 dynamics. a_V from D7 many-body
dynamics; half-life prediction for ²⁹⁸Fl.

**Status:** T3 overall; N=126 **T4→T3 CLOSED** (C361).
**Files:** `equations/nuclear_shell_kappa.py` (C361), `equations/nuclear_relativistic_so.py` (C347),
`equations/nuclear_shell_model.py`, `equations/nuclear_dfc_params.py`, `equations/nuclear_volume_term.py`

---

### T18 — f_pi: DFC Overshoot (reduced from +5.3% to −2.7%)

**Original:** f_pi = Λ/π = 96.9 MeV vs observed 92.07 MeV (+5.3%).

**C387 progress:** Pagels-Stokar formula with DFC inputs (0 free parameters):
f_pi = Λ × √((ln 7 − 6/7)/(4π)) = 89.63 MeV (−2.7%). Uses M_q = M_N/3
as constituent quark mass and Λ_UV = m_ω as UV cutoff. Key algebraic result:
m_ω/M_q = √6 exactly from DFC mass relations, giving PS integral I = ln(7) − 6/7.

**Impact chain (updated):** f_pi −2.7% → g_piNN +1.2% (was −6.4%) → nuclear force
predictions dramatically improved. BUT a_pair = f_pi/(N_c²−1) worsens to −6.6%
(pairing formula may need independent derivation).

**Remaining gap (2.7%):** Constant M_q approximation (QCD has momentum-dependent
quark mass), M_N(DFC) vs M_N(obs) (−0.45%), finite m_pi corrections (~1-2%).

**Path to full closure:** Momentum-dependent constituent mass M(p) in PS integral.
With M_N(obs) + 1% pion mass correction: f_pi ~ 90.7 MeV (−1.5%).

**Status:** T3 (improved from +5.3% to −2.7%; formula derived, not fitted).
**Files:** `equations/fpi_correction_t18.py` (C387), `equations/pion_decay_constant.py` (C166)

---

### T19 — Deuteron Binding Energy: −49% Underbinding

DFC sigma+omega central potential gives B_d = 1.14 MeV vs observed 2.2246 MeV (−49%).
Ground state exists but is too weakly bound.

**Root causes (3 identified):**
1. g_piNN = 12.28 is 6.4% low (from f_pi overshoot T18) — reduces potential depth
2. Tensor OPE force not included — provides ~50% of deuteron binding in full NN calculations;
   central OPE alone is repulsive in ³S₁ channel
3. No short-range regularization — unphysical excited state at B = 4.6 MeV appears

**Path to close:**
- **Immediate (tensor):** Implement coupled ³S₁-³D₁ Numerov solver with DFC OPE tensor force.
  Standard nuclear physics: tensor force is essential for deuteron, not optional.
- **Medium-term (f_pi):** Closing T18 would increase g_piNN toward 13.12, deepening potential.
- **Full solution:** sigma+omega+pion (central+tensor) with DFC couplings, plus hard-core
  or form-factor regularization at r < 0.5 fm.

**Status:** T4 open. **Files:** `equations/prediction_tests_phase2.py` (C386)

---

### T20 — Nucleon Magnetic Moment Ratio: SU(6) Preservation

DFC dressed-quark model gives mu_p = 2.833 (+1.4%) and mu_n = −1.888 (−1.3%) individually,
but the ratio mu_p/mu_n = −1.500 is unchanged from the NRQM SU(6) value (obs: −1.460, +2.7%).

The ratio is preserved because both mu_p and mu_n scale as 1/m_q in the constituent quark model.
Breaking the ratio requires isospin-violating physics.

**Path to close:**
1. **Strange quark sea:** s-sbar loop contributes to kappa_S (isoscalar anomalous moment).
   kappa_S(obs) = −0.060 ≠ 0 directly measures strange sea. DFC has m_s from C274.
2. **m_u ≠ m_d:** Different u,d quark masses give different magnetic moments.
   DFC needs light quark mass splitting (blocked by quark mass derivation T4).
3. **Pion cloud isospin asymmetry:** pi+ vs pi0 exchange contributes differently to p vs n.

**Status:** T4 open. **Files:** `equations/prediction_tests_phase2.py` (C386)

---

### T21 — Nolen-Schiffer Residual: ~7% from CSB Forces

After exchange + proton-size corrections, DFC still overshoots mirror nuclei CDEs by
7.2% RMS for A ≥ 11 (6.3% for A ≥ 20). This is the "true" Nolen-Schiffer anomaly
attributed to charge-symmetry breaking (CSB) nuclear forces.

**Three CSB sources (all derivable from DFC in principle):**
1. **ρ⁰-ω mixing** (~3-5%): mixing amplitude ε ∝ (m_d − m_u)/Λ_QCD produces isospin-
   violating nuclear potential. DFC has m_ω = √(2π)Λ. Needs m_d − m_u.
2. **Pion mass splitting** (~1-2%): m(π±) − m(π⁰) = 4.6 MeV from EM self-energy.
   DFC has α_em from D5; Cottingham formula is tractable.
3. **Neutron-proton mass difference** (~1%): m_n − m_p = 1.293 MeV affects kinetic terms.
   Requires both EM and quark mass contributions (blocked by light quark masses).

**Path to close:**
- **Highest impact:** Compute ρ-ω mixing correction to CDE using DFC meson masses.
  Even with empirical mixing amplitude, this would close ~3-5% of the residual.
- **Tractable now:** Pion EM mass splitting from α_em + Cottingham formula.

**Status:** T3 (residual correctly matches literature expectation; CSB sources identified
but not computed from DFC). **Files:** `equations/nuclear_nolen_schiffer.py` (C385)

---

### T22 — Nuclear Saturation: Linear Walecka Failures

Linear QHD-I model with DFC couplings (g_sigma = g_omega = 9.645) fails quantitatively:
- ρ₀ = 0.228 fm⁻³ (+42% from obs 0.16)
- r₀ = 1.016 fm (−15% from SEMF 1.20)
- E/A = −9.4 MeV (+40% from obs −15.8)
- K = 1646 MeV (+600% from obs 230)

These are known QHD-I limitations (not DFC-specific), but DFC must provide the path
to the correct nuclear EOS if its couplings are to be validated.

**Path to close:**
- **Nonlinear sigma terms from V(φ):** C373-C375 derived g₂ = −2083 MeV (T3, +1.2%
  of NL3) and g₃ from V(φ) quartic identity. g₂ sign is correct (T1, kink Z₂ breaking).
  But g₃ = 2.30 is too small for quantitative saturation.
- **Beyond mean-field:** Multi-loop corrections, Fock terms, or RPA correlations
  may tame the overbinding/stiffness.
- **Key test:** If V(φ) nonlinear terms can bring K from 1646 → ~250 MeV while keeping
  E/A ~ −16 MeV, the nuclear saturation problem is closed.

**Status:** T4 open (C371-C375). **Files:** `equations/nuclear_walecka_prediction.py` (C371),
`equations/nuclear_kink_fluctuation.py` (C373), `equations/nuclear_kink_g3_vphi.py` (C374)

---

### T23 — DFC Surface Diffuseness: −20% Below Empirical

DFC predicts nuclear surface diffuseness a = r_σ = ħc/m_σ = 0.432 fm vs empirical
Woods-Saxon a = 0.54 fm (−20%). The 20% gap means the DFC bare sigma mass (456.8 MeV)
produces a surface that is too sharp.

**Path to close:**
- The empirical 0.54 fm includes beyond-mean-field effects (pairing, shell structure)
  not in the bare sigma exchange range. The gap may be physical (bare vs dressed).
- Alternatively, if m_σ(effective) < m_σ(bare) at nuclear densities (as seen in
  C377's EOM analysis), the effective range lengthens toward 0.54 fm.
- Test: compute density-dependent m_σ(eff) at ρ₀ and check if a(eff) → 0.54 fm.

**Status:** T3 (−20%, within structural tolerance, origin identified).
**Files:** `equations/nuclear_nolen_schiffer.py` (C385), `equations/nuclear_msigma_resolution.py` (C377)

---

### T24 — M_W: DFC Undershoots by −0.88%

DFC predicts M_W = 79.67 GeV vs observed 80.377 GeV (−0.88%). This comes from the
DFC EWSB calculation. The gap is likely from missing one-loop EW radiative corrections
(Δρ_top, etc.) which shift M_W by ~1%.

**Path to close:** Compute one-loop EW corrections to M_W using DFC Higgs/top parameters.
Standard SM calculation with DFC inputs.

**Status:** T3 (structural). Linked to Open Blocked Derivations (EW loop corrections).
**Files:** `equations/muon_lifetime.py`

---

### T25 — Quantities Not Yet Derived from DFC

Observed values that DFC should eventually predict but currently uses as empirical inputs
or has not yet addressed:

| Quantity | Observed | DFC Status | Blocking Issue |
|---|---|---|---|
| m_pi | 139.57 MeV | Empirical input | Chiral symmetry breaking mechanism from DFC not derived |
| m_u, m_d (light quarks) | 2.2, 4.7 MeV | Not derived | Chiral SB + Yukawa coupling from substrate |
| r_p (proton charge radius) | 0.8409 fm | Empirical input | Pion cloud integral with DFC g_piNN (Phase 3 test) |
| m_n − m_p | 1.293 MeV | Not derived | Needs m_d − m_u + EM self-energy |
| Δ(1232) − N splitting | 293 MeV | Rough estimate only | Needs α_s at 1 GeV scale (running) |
| N=184 (superheavy magic) | Predicted by some models | Not reproduced at κ=33 | SO strength or deformation physics |
| CKM matrix elements | 4 params | Not derived | D6/D7 overlap integral |
| PMNS matrix (θ₁₂, θ₁₃) | Known | Not derived | D6 holonomy mechanism |
| Absolute neutrino masses | Constrained | Not derived | f_ν from substrate dynamics |
| σ_piN (sigma term) | 52 MeV | Blocked | Needs m_hat = (m_u+m_d)/2 |

**Status:** T4 for all. These are targets for future cycles.

---

### Open Blocked Derivations

| Target | Status | Key file |
|---|---|---|
| M_c(D7) from substrate | T2b (C208: −47.8% vs ECCC); needs 2-loop C_match correction | `equations/ym_sp5_mcdz_derivation.py` |
| ℏ from (α, β, c) | T4 open; blocked by T12 | — |
| CKM/PMNS matrices | T4; D6/D7 overlap integral not computed | — |
| EW loop corrections (Δρ_top) | T4; one-loop DFC calculation not done | — |
| SU(3) vs SO(6) | Largely resolved C117/C177; J propagation proof open | `equations/d5_complex_from_instability.py` |
| Koide t = 1/√Q_top derivation | T4; 5D Yukawa vortex integral open | `equations/koide_phase_coupling.py` |
| Series holonomy (Step 9c) | T3; KK reduction formal derivation open | — |
| Collapse mechanism | T2a (C360); trigger+selection upgraded; entanglement T3 | `equations/collapse_trigger_condition.py` (C360), `equations/collapse_mechanism.py` (C340) |

---

### Known Equation Module Issues

| Module | Issue |
|---|---|
| `gauge_couplings.py` | `squashing_correction()` returns None — placeholder |
| `quantum_emergence.py` | Born rule assigned by definition, not derived (use `born_rule_*.py` instead) |
| `neutrino_masses.py` | m₂, m₃ derived from input Δm² — not independent predictions |
| `bifurcation_dynamics.py` | `gamma_from_beta()` RETRACTED — unphysical output |
| `closure_topology.py` | No stable minimum for n≥3 (Derrick's theorem) |
| `pair_production.py` | Large errors at √s=29–55 GeV from missing γ-Z interference (not DFC-specific) |

---

## Retracted Claims

| Claim | Retracted | Replacement |
|---|---|---|
| γ_D = (16/3)√β | C48 | E_kink/E_total = 8/3 exactly (universal, β-independent) |
| β ≈ 0.035 from γ_D | C48 | β = 1/(9π) derived T2a (C117) |
| E_kink formula (pre-BPS) | C47 | BPS-correct: E_kink = (4/3)cα^(3/2)/(β√2) |
| σ_geom uncertainty ±0.8 GeV (Higgs) | C38 | Corrected to ±3.4 GeV; m_H = 124.4 ± 3.7 GeV |

---

## Summary of Prior Resolved Issues

Major issues resolved during model development (newest first):

- **Born rule P(x)=|ψ(x)|²** — T2a (C339/C359): full derivation chain V(φ)→Schrödinger→⟨ε⟩∝|ψ|². Two independent Step 6b routes: (A) σ² coupling selection from Z₂ + averaging + EFT (C339); (B) barrier dynamics — DC response Σ(x)=−S(x)/(2α) reduces spinodal distance, δΓ∝|Σ|∝|ψ|² in linear regime (C359, 14/14 PASS).
- **Strong CP (θ̄=0)** — T2a (C147/C157): S⁵ CP isometry → θ=0; real amplitude preservation theorem → arg(det M_q)=0; interface overlap integral Im(Y)=0. No axion prediction.
- **Tau lepton mass** — T2a (C146): Koide formula m_τ = 1776.97 MeV (+0.006%, 0 free params). Dimple model (8.4× off) superseded.
- **EWSB vacuum v** — T2a (C145): co-crystallization v = 247.83 GeV (+0.65%).
- **α_s(M_Z)** — T2a (C144): ECCC condition α_s = 0.11821 (+0.006%). Prior 8.1% error from wrong M_c(D7).
- **α_em(M_Z)** — T2a (C141): 36π chain 1/α_em(M_Z) = 128.09 (+0.15%, 0 free params).
- **Fermion representation** — T1+cited (C320): JR76 index theorem → triality t=1 → fundamental (1,0) uniquely.
- **k_Y² = 5/3** — T2a (C273): uniqueness theorem k_Y²(N_c) = 5/3 iff N_c = 3.
- **Bottleneck 2 (coupling derivation)** — T2a (C117): g_eff² = 8/27 from V(φ) tachyonic instability → complex scalar → U(1) → J → N_Hopf=9.
- **Bottleneck 1 (D7=SU(3))** — T2a (C59–74): n coincident modes → SU(n); PT s=2 non-degeneracy; D7 n=3 verified.
- **T9 (two closure scales)** — Resolved C79: M_c(D1) sets Higgs λ₀; M_c(D5/D6) sets gauge IC.
- **T13 (α free parameter)** — T2a (C172): α = ∛18 from β[T2a] + S_kink×α_D5=1[T1] + BPS saturation[T1].
- **g₂(M_Z)** — T2a (C353): self-consistent L from 36π chain; g₂ = 0.6531 (+0.29%).
- **Neutrino depth shift** — T2a (C354): δd = 1/(6π) from JR-BPS derivation.
- **Quark masses** — T2a (C274): κ_q = π×N_c/2 from center vortex; charm +0.29%, strange +2.09%.
