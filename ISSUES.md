# DFC Model — Open Issues, Failures, and Conflicts

Centralized tracker for all known failures, internal tensions, blocked derivations,
retracted claims, and open questions across the repository. Check and update after
every push. Resolve by removing entries or moving to the `## Resolved` section.

**Last updated:** 2026-04-16 (Cycles 47–57)

---

## Critical (Block core claims)

### T9 — Two closure-scale inconsistency
- **Weinberg angle / Route 3B** uses M_c(D5/D6) ≈ 10¹³ GeV (from SM α₁=α₂ crossing)
- **Higgs mass derivation** uses M_c(Higgs) ≈ 10¹⁸ GeV (where tree-level λ₀ ≈ 0.013)
- Both cannot be "the DFC closure scale" without two distinct closure processes
- Quantitative impact: fine-tuning Δ_FT changes by 10¹⁰ depending on which scale is used
- Files: `foundations/higgs_geometry.md` (Open Q1), `equations/weinberg_angle_rg.py` (Open Problem 2), `foundations/hierarchy_problem.md`
- Path: either (a) identify two distinct closure events at D6 vs. D6-squashing, or (b) find the derivation error

### T8 — ℏ hierarchy (10²⁷ gap)
- S_kink(D1) ≈ 4×10³⁹ ℏ; model has ~4 bifurcations → reduces to ~4×10²⁷ ℏ residual
- ℏ is not derivable from (α, β, c) alone without identification with SI unit system
- Files: `foundations/planck_constant_derivation.md`, `equations/planck_constant.py` [STUB]
- Path: route via α_em derivation proposed; requires completing coupling chain first

### Bottleneck 1 — D-depth assignment not derived
- D5=U(1), D6=SU(2), D7=SU(3) are Tier 3 working hypotheses, not derivations
- Route B (Hopf fibrations: S¹→S³→S⁵) is the leading candidate; DOF count per bifurcation from substrate dynamics is the missing step
- Files: `foundations/depth_assignment.md`, `foundations/hopf_fibration_geometry.md`
- Path: derive DOF count per bifurcation event from V(φ) = −α/2 φ² + β/4 φ⁴ compression dynamics

### Bottleneck 2 — r_U1/λ = 3/(4β) not formally derived
- The key coupling chain step g² = 8πβ/3 depends on identifying r_U1 = φ₀²/(β f²)
- Route A (KK reduction) blocked: real φ⁴ scalar has no U(1) vector zero modes on kink
- Route B (domain-wall worldvolume) blocked: U(1) phase of complex scalar is NOT localized on real kink
- Requires substrate extension beyond pure real φ⁴ (complex scalar or gauge structure)
- Files: `foundations/phase_stiffness_derivation.md` (Open Q1–Q2), `foundations/coupling_derivation.md`
- Downstream: all coupling predictions carry ~1.3% systematic error until resolved

---

## Known Prediction Failures (Tier 2b)

| Prediction | Module | DFC | Observed | Error | Path to Fix |
|---|---|---|---|---|---|
| Tau lepton mass | `mass_spectrum.py` | 212 MeV | 1777 MeV | **8.4×** | D7 boundary conditions on D6 outer wall; D7 SU(3) squashing pressure |
| Neutrino mass hierarchy ratio Δm²₃₁/Δm²₂₁ | `neutrino_masses.py` | 1.34 | 5.71 | **4.3×** | D-label spacing assumption; f_ν derivation |
| Strong coupling α_s(M_Z) | `coupling_derivation.py` | 0.105 | 0.1182 | **11%** | M_c(D7) not derived from substrate; depth-running |
| Charm/strange quark masses | `quark_masses.py` | ~15% below | — | **15%** | Non-uniform Higgs threshold scaling |

---

## Internal Tensions

### T2 — CKM small / PMNS large
- DFC proposes angle hierarchy from D6/D7 mismatch; qualitative only
- No formula derived for mixing angles; SM values not reproduced
- Files: `foundations/tension_analysis.md`, `phenomena/particle_physics/flavor_mixing.md`

### T4 — Fermion representation origin (fundamental vs. adjoint)
- Why do D7 fermions appear in the fundamental rep of SU(3), not the adjoint?
- Route B Hopf fiber provides structural motivation; formal derivation of representation content missing
- Files: `foundations/tension_analysis.md`, `foundations/three_generations.md`

### α_s error vs M_c(D7) uncertainty
- DFC-derived α_s(M_Z) = 0.105 (11% off); error traces to M_c(D7) ≈ 8×10¹⁴ GeV from equal-coupling extrapolation, not from substrate
- D5/D6 co-crystallization explains why M_c(D5) ≈ M_c(D6); D7 is a separate bifurcation event with unknown scale
- Files: `equations/coupling_derivation.py`, `foundations/depth_running.md`

---

## Retracted Claims

| Claim | Retracted in | What Replaced It | Files Corrected |
|---|---|---|---|
| γ_D = (16/3)√β (bifurcation energy fraction derived from substrate) | Cycle 48 | E_kink/E_total(λ) = 8/3 exactly (universal constant, β-independent, > 1); γ_D cannot be physical prediction | `bifurcation_dynamics.py` (RETRACTED label), `bifurcation_dynamics.md`, 6 files with ΔV/E_kink corrected 0.71→0.265 |
| β ≈ 0.035 derived from γ_D inference | Cycle 48 | β = 0.0351 is Tier 3 reference value; provenance note in `coupling_derivation.py` | `coupling_derivation.py`, CLAUDE.md |
| E_kink = (4/3)c√(2α³/β) | Cycle 47 (audit finding) | BPS-correct: E_kink = (4/3)c²φ₀²/λ = (4/3)cα^(3/2)/(β√2) | `kink_model.py` |
| σ_geom uncertainty = ±0.8 GeV in Higgs mass | Cycle 38 | Corrected to ±3.4 GeV; m_H = 124.4 ± 3.7 GeV (PDG m_t) | `higgs_mass_derivation.md`, `higgs_potential.py` |

---

## Blocked Derivations

| Target | Why Blocked | Files | Required Extension |
|---|---|---|---|
| r_U1/λ = 3/(4β) from substrate | Real φ⁴ has no localizable U(1) phase; Routes A and B both blocked | `phase_stiffness_derivation.md` | Complex scalar or gauge field in substrate |
| M_c(D7) from substrate | γ_color (D6→D7) depth-running not computed; E_total normalization open after Cycle 48 retraction | `depth_running.py`, `bifurcation_dynamics.py` | Find E_total(L) with macroscopic coherence length L from substrate dynamics |
| β ≈ 0.035 from pre-substrate principle | No pre-substrate condition identified that selects β | `beta_substrate.py` [STUB] | New theoretical input (pre-bifurcation stability condition) |
| Born rule for position | Spin case DERIVED (Cycle 38); Kramers escape rate Γ(x) ∝ \|φ(x)\|² not rigorously derived | `measurement.md`, `born_rule_derivation.md` | Escape rate calculation from V(φ) saddle topology |
| ℏ from (α, β, c) | S_kink(D1)/ℏ = 4×10³⁹ — 13.2 bifurcations needed to reach ℏ scale; model has only 4 | `planck_constant_derivation.md` | Either additional sub-bifurcation structure or route via α_em derivation |
| Confinement formal proof | Requires nonlinear SU(3) analysis; equivalent to Yang-Mills mass gap problem | `strong_force.md` (Open Q1), `strong_cp.md` | Nonlinear D7 field theory; beyond perturbation theory |
| v = 246 GeV from substrate | μ² not yet derived from (α, β, c); λ = β/4 identified (Cycle 58) | `higgs_geometry.md` (Open Q2), `foundations/vev_derivation.md`, `equations/berger_sphere.py` | λ = β/4 ≈ 0.0088 (R₄=0 proved; substrate β is the source); derive μ² from D7/D6 overlap integral; resolve field normalization factor ~1.5; T9 must be resolved first |
| CKM and PMNS matrices | Holonomy mismatch integral over D6/D7 boundary not computed | `flavor_mixing.md`, `tension_analysis.md` | D6/D7 overlap geometry → mixing angle computation |
| Electroweak loop corrections (Δρ_top) | One-loop DFC calculation from D6+D7 dynamics not done | `electroweak_precision.md` (Open Q1) | Standard Feynman diagram computation in DFC effective Lagrangian |

---

## Equation Module Stubs (No Implementation)

| Module | Target | Priority |
|---|---|---|
| `s_matrix.py` | Full S-matrix beyond Born; exact kink-antikink; 3+1D Skyrme | High — Bottleneck 3 |
| `planck_constant.py` | ℏ from DFC substrate characteristic scales | High — Bottleneck 2 |
| `fermion_spectrum_full.py` | Full lepton+quark mass spectrum (τ/top failures to fix) | High — Tier 2b failures |
| `beta_substrate.py` | Derive β ≈ 0.035 from pre-substrate principle | High — only free substrate parameter |
| `dark_matter.py` | Stable intermediate kink modes as dark matter candidates | Medium |
| `cosmological_constant.py` | Λ from residual compression budget | Medium |
| `holographic_entropy.py` | Bekenstein-Hawking from closure capacity | Medium |
| `baryogenesis.py` | Matter-antimatter asymmetry at D7 phase transition | Medium |
| `inflation.py` | Inflation as D1→D4 bifurcation cascade; n_s prediction | Medium |

---

## Equation Module Placeholders / Circular Logic

| Module | Function | Issue |
|---|---|---|
| `gauge_couplings.py` | `squashing_correction()` | Returns None — PLACEHOLDER, geometric derivation pending |
| `quantum_emergence.py` | Born rule probability | CIRCULAR: assigns Ω/Ω_total = \|ψ\|² by definition, not derivation |
| `neutrino_masses.py` | m₂, m₃ predictions | CIRCULAR: m₂, m₃ derived from input Δm² values — not independent predictions |
| `bifurcation_dynamics.py` | `gamma_from_beta()` | RETRACTED — output is unphysical (ratio > 1); labeled but still present |
| `closure_topology.py` | `closure_energy()` | No stable minimum for SU(2)/SU(3) — Derrick's theorem violation for n≥3 |

---

## Open Questions by Document

### foundations/

**`substrate.md`**
- Born rule for position (from Kramers escape rate) — OPEN
- ℏ from substrate — OPEN (T8)

**`higgs_geometry.md`**
- Open Q1: T9 two-closure-scale tension — CRITICAL
- Open Q2: Derive μ², λ from (α, β, c)
- Open Q3: λ₀ ≈ 0 from modulus symmetry — needs formal proof
- Open Q4: Higgs as metric modulus vs. kink (conceptual clarification needed)

**`higgs_mass_derivation.md`**
- λ₀ boundary condition at M_c — currently matched to observed m_H; not independently predicted

**`depth_assignment.md`**
- DOF count per bifurcation from substrate dynamics — the key missing step for Bottleneck 1
- Why bifurcation cascade terminates at SU(3) — conjectured from D7 confinement; not proved

**`embedding_geometry.md`**
- M_c from substrate parameters (α, β, c) — currently read from SM running (not a DFC derivation)

**`mass_hierarchy.md`**
- Exponent κ (mass-to-depth scaling) — currently fitted from spectrum; not derived from substrate

**`three_generations.md`**
- Second excited state eigenvalue in D6 S³ geometry with D7 boundary — tau mass failure

**`coupling_derivation.md`**
- Holonomy integral: physical identification r_U1 = φ₀²/(β f²) not derived from substrate
- KK reduction on S¹ (Route A) and domain-wall worldvolume (Route B) both blocked

**`bifurcation_dynamics.md`**
- γ_D ∈ (0,1) from substrate — RETRACTED result; no replacement yet
- E_total(L) normalization with macroscopic coherence length L — required to revive depth-running

**`kink_nucleation.md`**
- Born rule from first-passage / nucleation statistics — structural argument only

**`born_rule_derivation.md`**
- Position Born rule (Kramers escape rate) — OPEN; spin case complete

**`depth_assignment.md`**
- Route B (Hopf fibrations S¹→S³→S⁵) most promising; DOF count calculation not yet done

### phenomena/

**`particle_physics/forces/strong_force.md`**
- Formal proof of confinement from DFC (Open Q1) — Yang-Mills mass gap equivalent
- Derive Λ_QCD from D7 closure parameters (Open Q2)
- Derive α_s from D7 geometry (Open Q3) — 11% error currently
- Non-perturbative D7 dynamics: confinement, hadron masses, nuclear binding (Open Q4)

**`particle_physics/forces/electroweak_precision.md`**
- One-loop radiative corrections (Δρ_top) — not yet computed in DFC (Open Q1)
- Derive v = 246 GeV from substrate (Open Q2) — removes free parameter from 4 predictions
- CDF M_W anomaly (80.4335 GeV) — DFC prediction (79.67 GeV) is further from CDF than SM fit (Open Q3)

**`particle_physics/muon_decay.md`**
- Derive v = 246 GeV from substrate (Open Q1) — same as above
- Radiative corrections to M_W (Open Q3) — ~1% improvement possible at one loop
- Derive m_μ from substrate (Open Q4) — currently taken from data

**`particle_physics/hierarchy_problem.md`**
- Formal proof of geometric protection (Goldstone argument at all loop orders) (Open Q1)
- Resolve T9 two-closure-scale tension (Open Q2) — critical

**`particle_physics/strong_cp_problem.md`**
- Formal derivation of θ = 0 from S⁵ formation dynamics — currently structural argument
- Physical θ = θ_QCD + arg(det M_q): D6/D7 quark phase relation not derived

**`particle_physics/particles/neutrinos.md`**
- Derive f_ν from substrate dynamics — blocks absolute neutrino mass scale
- Depth spacing ratio 1.34 vs observed 5.71 — [KNOWN_FAILURE]

**`particle_physics/particles/muon_tau.md`**
- τ mass: dimple+global-box model predicts 212 MeV, observed 1777 MeV — [KNOWN_FAILURE 8.4×]

**`quantum/quantum_mechanics.md`**
- Born rule for position — OPEN (spin case derived, Cycle 38)

**`cosmology/big_bang.md` / `dark_energy.md`**
- Λ from substrate parameters — OPEN (displaced from fine-tuning to initial-conditions problem)
- Equation of state parameter ε: w_Λ = −1 + ε ≈ 0.007 from observation, not substrate

**`gravity/general_relativity.md`**
- Derive G_Newton from substrate — OPEN
- Derive Einstein field equations from dimensional folding gradient dynamics — OPEN

---

## Resolved Issues (move here when closed)

| Issue | Resolved in | How |
|---|---|---|
| k_Y = 3/5 origin (was borrowed from SU(5)) | Cycle 30 | Derived from Dynkin index matching on SM matter content — no GUT needed |
| Tsirelson bound CHSH ≤ 2√2 unprovable claim | Cycle 35 | Proved algebraically: C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂] → ‖C‖ ≤ 2√2 |
| Schrödinger equation "assumed" | Cycle 36 | Derived from KG in non-relativistic limit; labeled DERIVED in substrate.md |
| Binary measurement outcomes "postulated" | Cycle 36 | Proved topologically: Z₂ configuration space of φ⁴ kink |
| Born rule for spin "assumed" | Cycle 38 | Derived: P(↑,n̂) = cos²(θ/2) from SU(2) spinor geometry + binary nucleation |
| E_kink formula wrong | Cycle 47–48 | BPS-correct formula derived; γ_D retracted; all downstream files corrected |
| G_F as pure experimental input | Cycle 51 | G_F derived from β via coupling chain (+0.18%); added to Tier 2a |
| Berger sphere R₄ as source of Higgs quartic λ | Cycle 58 | R₄ = 0 exactly proved (analytic + numeric); λ comes from substrate β/4 ≈ 0.0088; see `equations/berger_sphere.py` |
| Neutron lifetime hidden in `proton_stability.py` | Cycle 52 | Added to `__main__` output; both G_F routes shown |
| sin²θ_W(M_Z) Route 3B derivation (open since model inception) | Cycle 22 | sin²θ_W = 3/8 at M_c → 0.231 at M_Z from equal-coupling + SM running; 0.01% error |
| E=hν claimed "derived" from massless KG dispersion | Cycle 42 | Corrected: E=ℏω is a QFT postulate imported from outside DFC; labeled as such |
| muon_tau.md: τ_μ = 2.197 μs "< 0.1% match" (false) | Cycle 51 | Corrected to DFC prediction 2.180 μs (−0.80%); actual chain derivation added |
