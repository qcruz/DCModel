# DFC Model — Open Issues

**Last updated:** Cycle 356 (2026-08-07)

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

**T4 candidates (2 remaining):**
1. CKM-like D6/D7 interface mixing
2. Winding-number-dependent D4/D6 boundary condition asymmetry

(Candidate 3, CP phase shift, effectively ruled out — modern fits already marginalize δ_CP.)

**Status:** T4 open. **Files:** `equations/neutrino_theta23_correction.py` (C209),
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
Overshoot from constant C_dual duality model. T3 overall — correct sign and order of
magnitude; quantitative match requires per-resonance duality or D7 confinement spectral
density.

**Status:** T3 (C356 approximation 4× target); T4 for exact 0.00102 piece.
**Files:** `equations/hadronic_vp_dispersive.py` (C356), `equations/alpha_em_dfc_chain.py` (C351),
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
are at different compression depths and not additive. T3 structural argument. Does NOT
derive ρ_Λ = (2.3 meV)⁴ from V(φ). Speculative connection: ρ_Λ^{1/4} ≈ m_ν may share
origin in δd = 1/(6π).

**Status:** T3 structural reframe; T4 for quantitative prediction.
**Files:** `foundations/cosmological_constant_dfc.md` (C328)

---

### T17 — Nuclear Physics: N=126 Shell Closure

Six-step framework complete at T3. B(²⁹⁸Fl) = 2114 MeV = 7.09 MeV/nucleon [T3].
Magic numbers 2,8,20,28,50,82 reproduced; N=184 predicted. a_SO = I₄ × a₀ = 0.893 fm
[T3, 0.7% from FRDM].

**T4 open:** N=126 not reproduced — a_SO alone insufficient for 1i₁₃/₂ intruder state
ordering. Requires relativistic Dirac-Woods-Saxon or κ < 36 condition. Also open: a_V
from D7 many-body dynamics; half-life prediction for ²⁹⁸Fl.

**Status:** T3 overall; N=126 T4 open.
**Files:** `equations/nuclear_relativistic_so.py` (C347), `equations/nuclear_shell_model.py`,
`equations/nuclear_dfc_params.py`, `equations/nuclear_volume_term.py`

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
| Collapse mechanism | T3 (C340); spinodal dynamics formalized | `equations/collapse_mechanism.py` |

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

- **Born rule P(x)=|ψ(x)|²** — T2a (C339): full derivation chain V(φ)→Schrödinger→⟨ε⟩∝|ψ|²→σ² unique coupling from V(φ) Z₂ symmetry + fringe shape + EFT suppression.
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
