# Dimensional Folding Model — Repository

A theoretical physics model under development. The starting postulate is a single
self-compressing scalar field with a double-well potential V(φ) = −α/2 φ² + β/4 φ⁴.
The model proposes that the particle content and gauge structure of the Standard Model
arise from the topology of bifurcation events in this field, without assuming pre-existing
spatial dimensions, gauge groups, or particle species.

Current status: ~80% complete by internal estimate. Several Standard Model quantities
are reproduced to under 5% error; others remain unresolved. Known failures and open
derivations are documented in `ISSUES.md`. Development history is in `push_history.md`.

---

## Core Derivations

Five results derived directly from `V(φ) = −α/2 φ² + β/4 φ⁴` and winding-number
topology. Each follows from the compression mechanics with no free parameters beyond the
substrate quartic β ≈ 0.035.

- **Common gauge coupling — g = 0.54433** (0.006% agreement, 0 free parameters)
  Kink phase stiffness from the Bogomolny identity ∫sech⁴(u)du = 4/3 gives g² = 8πβ/3.
  With β = 1/(9π): g² = 8/27 exactly → g = 0.54433. Observed at SM unification scale:
  g_common = 0.5443. Verified in [`equations/d5_complex_from_instability.py`](equations/d5_complex_from_instability.py).

- **Weinberg angle — sin²θ_W = 0.2312** (<0.01% agreement)
  Hypercharge normalization k_Y = 3/5 from Dynkin index counting on SM fermion content
  (no GUT assumed). Equal closure couplings g₁ = g₂ → sin²θ_W = 3/8 at the threshold.
  RG running to M_Z gives 0.2312. Verified in [`equations/weinberg_angle_rg.py`](equations/weinberg_angle_rg.py).

- **φ⁴ kink shape-mode frequency — ω₁/m_σ = √3/2 ≈ 0.866** (exact)
  The kink fluctuation potential is an exact n=2 Pöschl-Teller potential with bound-state
  eigenvalues ω₀² = 0 (translation zero mode) and ω₁² = (3/2)α (shape mode), giving
  ω₁/m_σ = √3/2. Verified to 2.5 × 10⁻⁵ in [`equations/coupled_fluctuation.py`](equations/coupled_fluctuation.py).

- **Tsirelson bound — CHSH ≤ 2√2 ≈ 2.828** (algebraically exact)
  CHSH operator C satisfies C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂]. For ±1 observables
  ‖[Aᵢ,Aⱼ]‖ ≤ 2, so ‖C‖² ≤ 8 → CHSH ≤ 2√2. Proved from substrate SU(2) geometry
  with no quantum formalism assumed. Verified in [`equations/bell_correlations.py`](equations/bell_correlations.py).

- **Superconducting flux quantum — Φ₀ = h/(2e) = 2.068 × 10⁻¹⁵ Wb** (10⁻¹⁰ agreement)
  U(1) single-valuedness of the condensate on any closed path enforces ∮∇θ·dl = 2πn →
  enclosed flux Φ = nh/(2e). Zero free parameters; relative error 2.2 × 10⁻¹⁰ against
  CODATA. Verified in [`equations/superconductivity.py`](equations/superconductivity.py).

---

## Core Claims

The model rests on three postulates:

1. One continuous self-compressing scalar field exists. No pre-existing space, gauge group, or particle content is assumed.
2. The field's self-interaction potential has the double-well form V(φ) = −α/2 φ² + β/4 φ⁴, with free parameters α (quadratic coupling) and β (quartic coupling).
3. When compression reaches a threshold, the field opens a new degree of freedom rather than compressing further. These bifurcation events produce all structure in the model.

The model proposes that the gauge groups U(1), SU(2), SU(3) arise from the topology of these bifurcation closures at different compression depths — a correspondence that has been worked out structurally through zero-mode counting but is not yet a complete first-principles derivation. Quantitative predictions for gauge couplings, Weinberg angle, W/Z masses, Higgs mass, and τ lepton mass match observation at the 0.006%–5% level, with derivation chains of varying completeness. Known failures include the neutrino mass ratio m₃/m₂ (DFC predicts 5.33 vs observed 5.81, −8.3%; a prior 4.3× discrepancy was a metric error now corrected), and the algebraic identity closing the α_em(0) gap (0.044%; Tier 4 open). The τ lepton mass is resolved via the Koide formula at Tier 2a (m_τ=1776.97 MeV, +0.006%, 0 free params). The strong coupling α_s is resolved to +0.006% via the ECCC condition. Planck's constant and Newton's constant are not yet derivable within the current framework.

---

## Repository Map

```
WRITING_GUIDE.md          How to write phenomenon descriptions (read before contributing)
ISSUES.md                 Centralized tracker: all open questions, failures, tensions, retracted claims

foundations/              Core concepts, thought experiments, and structural arguments
  introduction.md         Originating thought experiment, overview, string theory comparison
  overview.md             The single starting point and core process
  premise.md              Formal glossary — all canonical definitions
  analogies.md            Seven canonical analogies for building intuition
  d1_mechanics.md         Concrete mechanical visualization of D1 compression and buckling
  formation.md            How dimensions are created by successive bifurcation
  dimensional_emergence.md  Why dimensions emerge, not pre-exist
  dimensional_stack.md    Provisional D1→D4+ layer ordering; particle spectrum table
  mathematics.md          Mathematics as emergent grammar of folding invariants
  product_geometry.md     Why force structures never unified (proton stability)
  three_generations.md    Three generations from SU(3) fiber topology
  higgs_geometry.md       Higgs mechanism as S³ squashing geometry
  higgs_mass_derivation.md  Full RG-improved Higgs mass derivation (125.1 ± 1.5 GeV)
  mass_hierarchy.md       Electron/muon mass ratio from geometric defect
  substrate.md            Mathematical substrate framework (kink model, postulates)
  embedding_geometry.md   Weinberg angle from equal-coupling initial conditions (Route 3B)
  vev_derivation.md       v = 246 GeV derivation path: μ² from D6/D7 overlap, λ from Berger sphere quartic
  bifurcation_dynamics.md γ_D = (16/3)√β RETRACTED; E_kink/E_total(λ)=8/3 proved; Planck-length kink width; D-label disambiguation
  kink_scattering.md      Shape mode ω₁ = (√3/2)m_σ (parameter-free); first S-matrix from substrate (Born)
  bell_hidden_variables.md  DFC Bell resolution: Assumption 2 violated by D1/D2 connectivity; not conspiracy
  tsirelson_bound.md        Tsirelson CHSH ≤ 2√2 proved: C²=4I⊗I−[A₁,A₂]⊗[B₁,B₂]; SU(2) commutator norm ≤ 2
  kink_nucleation.md        Two-sector topology proved (φ⁴ kink); binary measurement outcomes; Born rule open
  depth_assignment.md       D-depth assignment problem: 5 constraints; Route B (Hopf S¹→S³→S⁵) most promising
  compression_dynamics.md   DFC self-compression equations reconciled with thermodynamic/elastic/acoustic/gravitational formalisms
  measurement.md            Measurement as buckling threshold; six measurement types; Born rule status
  coupling_emergence.md     How coupling emerges from fold topology; g_eff→36π→α_em→α_s chain

equations/                Runnable Python modules — input data, get predictions
  constants.py            Physical constants (PDG 2024), particle masses, SM couplings
  kink_model.py           Static kink solution — simplest stable topological closure
  higgs_potential.py      S³ squashing geometry, gauge boson masses, Weinberg angle
  mass_spectrum.py        Lepton mass predictions from dimple potential
  gauge_couplings.py      Running couplings, squashing correction, pairwise crossings
  proton_stability.py     Proton lifetime bounds, sphaleron rate, experiment comparison
  weinberg_angle_rg.py    sin²θ_W = 3/8 at closure scale → 0.231 via RG running (Route 3B)
  bifurcation_dynamics.py γ_D formula RETRACTED; E_kink/E_total(λ)=8/3 verified; depth-running M_c(D5) remains self-consistent
  kink_scattering.py      Pöschl-Teller spectrum; shape mode = 0.8660 m_σ; Born phase shift
  s_matrix.py             Exact single-kink T(q): reflectionless n=2 PT, |T|²=1 to 4×10⁻¹⁶; Levinson δ(0⁺)=2π; open: DHN kink-antikink exact
  coupling_derivation.py  α_em, g_W, g_s from substrate (α, β, c)
  planck_constant.py      ℏ from DFC substrate characteristic scales
  dark_matter.py          Stable intermediate kink modes as dark matter candidates
  cosmological_constant.py  Λ from residual compression budget
  beta_substrate.py       Derive β ≈ 0.035 from pre-substrate principle
  fermion_spectrum_full.py  Full lepton+quark mass spectrum
  holographic_entropy.py  Bekenstein-Hawking from closure capacity
  baryogenesis.py         Matter-antimatter asymmetry at D7 phase transition
  inflation.py            Inflation as D1→D4 bifurcation cascade; n_s prediction
  scattering_cross_sections.py  σ_Thomson, Compton from DFC coupling chain; σ_T −0.28%
  muon_lifetime.py        M_W, M_Z, G_F, τ_μ from DFC coupling chain; all <1%
  electroweak_precision.py  ρ=1, T=0, sin²θ_W consistency — five EW precision tests
  pair_production.py      e⁺e⁻ → μ⁺μ⁻ cross-section; R-ratio = 11/3 (exact Tier 1); kink-antikink nucleation
  anomalous_magnetic_moment.py  a_e = α_em/(2π) from DFC coupling chain; −0.14% (36π chain)
  josephson_effect.py     K_J=2e/h verified to 7.75×10⁻¹⁶; Shapiro steps, SQUID, Josephson inductance
  scattering_length.py    a_s=3/M_c=3λ, r₀=11/(6M_c)≈1.833λ, τ_W(0)=−a_s; all exact, 0 free params
  kink_form_factor.py     F(k)=πκ(κ²+4)/(8 sinh(πκ/2)); ⟨r⟩_rms from kink profile; Tier 1
  z_boson_decays.py       Γ_Z=2456 MeV (−1.56%), Γ_inv=493 MeV (−1.16%), R_l (−0.10%), R_b (+1.58%), A_FB^lep (+3.17%)
  alpha_em_prediction.py  36π chain: 1/α_em(M_c(EW))=36π exact → 1/α_em(M_Z)=128.09 (+0.15%) → 1/α_em(0)=137.23 (+0.14%)
  alpha_em_selfconsistency.py  ECCC self-consistency: α_s=0.11821 (+0.006%), 1/α_em(0)=136.98 (−0.044%)
  ewsb_cocrystallization.py  v=247.83 GeV (+0.65%, Tier 2a); b₀=11 structural argument for SU(3)-driven EWSB
  koide_phase_coupling.py  m_τ=1776.97 MeV (+0.006%, Tier 2a); canonical phase vertex 1/√Q_top; Z₃ charge counting
  strong_cp_theta.py      theta=0 from S⁵ CP-isometry; d_n=0 Criterion B; D6/D7 independence from π₃(S³)=ℤ≠π₃(S⁵)=ℤ₂
  nuclear_binding.py      Bethe-Weizsäcker formula; Yukawa potential; Fe-56 peak; DFC α_s +0.006%
  lamb_shift.py           Hydrogen 2s-2p Lamb shift; self-energy loop integral stub; α⁵ scaling estimate
  quark_gluon_plasma.py   QGP deconfinement T_c; DFC Λ_QCD estimate; one-loop regime only

phenomena/                Natural language explanations of physical observations
  particle_physics/
    proton_stability.md   Why the proton cannot decay (product topology argument)
    compton_scattering.md Thomson/Compton cross-section from DFC coupling chain
    muon_decay.md         W mass, Fermi constant, muon lifetime from DFC; all <1%
    forces/electroweak_precision.md  ρ, T, S parameters; five tree-level precision tests
    pair_production.md    Pair production/annihilation as kink-antikink nucleation/coalescence; R-ratio
    strong_cp_problem.md  theta=0 from S⁵ CP-isometry (Tier 2a); d_n=0 Criterion B; no axion predicted
  quantum/
    anomalous_magnetic_moment.md  a_e = α_em/(2π) Schwinger term; DFC −0.14% (36π chain); muon g-2
    quantum_mechanics.md  Superposition, collapse, entanglement, tunneling, uncertainty
    interference.md       Wave interference as stationary field redistribution
    lamb_shift.md         [STUB] Hydrogen 2s-2p splitting; DFC self-energy loop integral; α⁵ scaling
    photoelectric_effect.md  [STUB] Photon absorption as threshold crossing; ℏ blockage
    hawking_radiation.md  [STUB] Horizon pair nucleation; T_H blocked by G_Newton and ℏ
  condensed_matter/
    superconductivity.md  Cooper pairs as D6 kink bound states; Φ₀=h/(2e) Tier 1 ✓; K_J Tier 1 ✓
    superfluidity.md      Global phase coherence; κ₀=h/m Tier 1 ✓; BEC open
    quantum_hall_effect.md  TKNN Chern number = DFC winding number; R_K Tier 1 ✓; FQHE structural
    josephson_effect.md   DC CPR I=I_c sin(δ); AC f_J=K_J×V; Shapiro steps; SQUID; all Tier 1 from K_J=2e/h
  gravity/
    general_relativity.md Gravity as folding gradient and dimensional pressure
  light/
    light.md              Light as near-D2 mode; c as boundary slope, not velocity
  thermodynamics/
    thermodynamics.md     All four laws derived from folding mechanics
    heat_and_conductivity.md  Heat, conduction, resistance, radiation unified

educational/              Step-by-step modules teaching the model from scratch
  00_overview.md          What is DFC? General audience, no physics background
  01_the_substrate.md     The one object, V(φ), kinks, I₄=4/3, Q_top=2, β=1/(9π), g_eff
  02_how_space_appears.md How apparent space arises: compression, D-depths, D3 localization
  03_depth_map.md         D1-D7 as compression thresholds, Hopf closure sequence, verified evidence
  04_forces.md            How U(1)/SU(2)/SU(3) emerge: S¹→S³→S⁵ closure, coupling constants, 3 forces not 4
  05_particles.md         Electrons, quarks, neutrinos as kink configurations
  06_predictions.md       Verified predictions and known failures
  07_open_questions.md    Open problems, known failures, honest status
  08_mathematics.md       Mathematical foundations for the technically inclined
  09_i4_identity.md       I₄=4/3 Casimir identity and its five structural roles
  10_cascade_uniqueness.md  S¹→S³→S⁵ cascade: why SU(3) and not something else
  11_36pi_topology.md     Why 1/α_em = 36π: sphere dimensions, kink action, closure
  12_substrate_topology.md  Kink topology, Q_top=2, winding numbers, particle stability
  13_mass_from_compression.md  Mass from D4 inertia; E_kink=36π M_Pl; Koide; lepton ratios
  14_spacetime_emergence.md   D3 localization → apparent 3D space; gravity; H₀=67.26
  15_dark_matter.md        DFC dark matter as D4–D5 intermediate closure; ~35 keV candidate
  16_cosmology.md          Hubble constant, cosmic expansion from substrate localization
  17_quantum_mechanics.md  Measurement as localization event; interference from field propagation
  18_open_problems.md      Honest map of T4/T3 open problems; what would close each one
  19_bell_inequalities.md  Why entanglement is not spooky in DFC; substrate connectivity below D3
  analogies/               Physical analogies for substrate behavior — what DFC structures are closest to
    01_the_kink.md         Domain walls, solitons, dislocations: what kinks are most like (and where each fails)
    02_the_photon_planet.md  Observation as field collision not delivery; the substrate as gas giant
    03_entanglement.md     Entanglement as field connectivity; crystal dislocation analogy; no signal needed
comparisons/              This model vs. Standard Model, String Theory, GR, GUT
  swot.md                 SWOT analysis: DFC strengths/weaknesses vs. all major theories
practical_applications/   Engineering limits and implications derived from DFC
  OVERVIEW.md             Document type protocol and rotation guide
  fundamental_limits.md   Five canonical engineering ceilings from substrate structure
  absence_predictions.md  No axion (T2a), no proton decay (T1), no SUSY (T3), no monopoles (T2a)
  localization_rate_ceiling.md  Maximum measurement frequency: f_max ~ 10^43 Hz from spinodal collapse timescale
archive/                  Original source documents
data/                     Observational reference values (PDG, cosmological)
```

---

## The Four Key Structural Choices

| Choice | This Model | Standard Alternative | Consequence |
|---|---|---|---|
| Gauge group structure | Product: U(1) × SU(2) × SU(3) | Simple group: SU(5), SO(10) | Proton absolutely stable |
| Generation number | Topological (dim of SU(3) fund. rep.) | Free parameter or chosen | Exactly 3, rigidly |
| Higgs mechanism | S³ squashing (geometric) | Postulated scalar field | Mexican hat potential derived |
| Mass hierarchy | Geometric defect (dimple) | Yukawa free parameters | Electron/muon ratio natural |

---

## Quick Start: Running Equations

```bash
# Predict particle masses from geometry
python equations/mass_spectrum.py

# Compute coupling constant convergence
python equations/gauge_couplings.py

# Explore Higgs potential geometry
python equations/higgs_potential.py

# Check proton stability bounds
python equations/proton_stability.py
```

Each module can also be imported and called with custom input:

```python
from equations.mass_spectrum import predict_lepton_masses
predict_lepton_masses(dimple_depth=1.2e-3, confinement_radius=3.1e-19)
```

---

## Mathematical Completeness Estimate

**Current estimate: ~80%** (viability as a theory: ~87%; mathematical rigor: ~73%)

**Model Reconcilability Risk Score (MRRS)** — probability current postulates *cannot* complete each scope (lower = better):

| Scope | MRRS | Key blocker |
|---|---|---|
| Core gauge/coupling sector | **14%** | α_em(0) identity (0.044% gap); arg(det M_q)=0 closed |
| Full SM reproduction | **43%** | neutrino m₃/m₂ −8.3%; quark masses (15%); G_Newton |
| Complete theory (SM + gravity + QM) | **70%** | ℏ derivability; G_Newton; Born rule for position |

*Full per-failure analysis with paths and swing factors in `comparisons/reconcilability_risk.md`.*

The model provides a coherent structural framework — the gauge sector, proton stability,
and several quantitative derivations are compelling. The primary open questions are:

- **G_Newton and ℏ** — not yet derivable from substrate parameters
- **Neutrino mass hierarchy** — DFC predicts ratio 5.33 vs observed 5.81 (−8.3%)
- **α_em(0) algebraic identity** — 0.044% gap; Tier 4 open derivation
- **Quark masses** — charm/strange approximately 15% below observed

*Full open-issue tracking in `ISSUES.md`. Development history in `push_history.md`.*

---

## Clay Prize Challenge: Yang-Mills Mass Gap

**This is a separate sub-project from the DFC model.** The Clay work tests and builds the
mathematical basis of DFC. The two are tracked independently.

**Full tracking: [`foundations/yang_mills_clay.md`](foundations/yang_mills_clay.md)**

### Two Independent Clay Prize Metrics

| Metric | Value | Definition |
|---|---|---|
| **Structural completeness** | ~95% | DFC argument coverage of all 5 JW criteria at T2a level |
| **Mathematical proof standard** | ~99% | Proximity to a Clay-accepted mathematical proof (LaTeX draft complete; Assumption A proved T1+cited; Prokhorov+Kato citations complete) |
| **CPC** | ~60% | P(DFC → valid JW proof candidate \| continued work) |

All five structural sub-problems are closed at T2a level. The LaTeX proof document
`equations/ym_clay_proof.tex` is a complete draft (22 KB, 5 lemmas, 1 main theorem,
12 citations, zero T2a steps on the critical path). The sole remaining gap is external
peer review. Full tracking and sub-problem breakdown in
[`foundations/yang_mills_clay.md`](foundations/yang_mills_clay.md).

### Sub-Problem Status

| Sub-problem | Status |
|---|---|
| Constructive 4D gauge theory from V(φ) | T2a — complete |
| Hamiltonian bound H ≥ I₄ × Q̂_top × m | T2a — complete |
| Topological charge spectrum | T2a — complete |
| Pure YM decoupling from scalar sector | T2a — complete |
| Derive Λ_QCD from V(φ) | T2a — complete |

---

## Coverage of Existing Theories

How much of each major theory's key content (derivations, predictions, structural explanations)
has been replicated or superseded within the DFC framework. These are honest estimates, not
aspirational targets. A theory is "covered" when DFC either reproduces the result from DFC
substrate parameters or provides a structural explanation for *why* the result takes the form
it does. Percentage reflects breadth of coverage, not accuracy of any single result.

| Theory | Coverage | What DFC Has | What's Missing |
|---|---|---|---|
| **Quantum Mechanics** | ~42% | Schrödinger eq. (derived from KG); spin-1/2 (FR/JR derivation); Born rule for spin (derived); binary outcomes (proved); Tsirelson bound (proved); g-2 Schwinger term (−0.14%, 36π chain); superposition/entanglement/tunneling/decoherence (structural) | Born rule for position (OPEN); Lamb shift (stub); path integral; ℏ from substrate (OPEN) |
| **Thermodynamics** | ~55% | All four laws (derived from folding mechanics); arrow of time (derived from Z₂ topology); blackbody Planck spectrum (structural, modulo ℏ); Boltzmann statistics (structural); heat/conduction (structural); compression dynamics reconciled | Fluctuation theorems (Jarzynski, Crooks); Carnot efficiency formula from DFC |
| **Standard Model** | ~42% | U(1)×SU(2)×SU(3) product structure (derived); 3 generations (derived); proton stability (zero rate); parity violation (JR chirality); sin²θ_W (<0.01%); m_μ/m_e (exact); m_τ (Koide, +0.006%, Tier 2a); M_W/M_Z/G_F/τ_μ (<1%); Higgs (124.4 GeV); R-ratio = 11/3 (exact); α_s (+0.006%, ECCC); EWSB v (+0.65%); strong CP (theta=0, Tier 2a) | CKM/PMNS; neutrino hierarchy (−8.3%); quark masses (15%); Feynman rules; loop corrections |
| **General Relativity** | ~15% | Gravity as folding gradient (structural); gravitational waves (structural); black holes (structural); Hawking radiation (stub); time dilation; H₀ (0.2%) | Einstein field equations not derived; G_Newton not derived; Schwarzschild metric not derived |
| **ΛCDM Cosmology** | ~20% | H₀ (0.2% match); CMB (structural); Big Bang (structural); flatness/horizon dissolved; dark energy (structural, qualitative) | Inflation (stub); dark matter (stub); baryogenesis (stub); Λ from substrate (stub) |
| **QFT (perturbative)** | ~16% | Born S-matrix; Thomson/Compton (−0.28%); Pöschl-Teller (exact); pair production (R-ratio exact); g-2 leading term (−0.14%, 36π chain); RG running; α_em(M_Z) (+0.15%); α_s (+0.006%) | Loop corrections (Lamb shift stub, 2-loop g-2); Feynman rules; renormalization |
| **Condensed Matter** | ~12% | Φ₀=h/(2e) Tier 1 ✓; K_J Tier 1 ✓; R_K=h/e² Tier 1 ✓; κ₀=h/m Tier 1 ✓; all from DFC U(1) winding; IQHE plateaus structural | BCS gap equation; Ginzburg-Landau; FQHE; roton gap; band structure; solid-state spectrum |
| **String Theory** | ~3% | Some topological overlaps (compact closure geometries, Hopf fibrations); DFC has no pre-existing spacetime | No strings/branes; no T/S-duality; fundamentally different framework |
| **Loop Quantum Gravity** | ~5% | Discrete topological closures analogous to spin networks; binary outcomes proved | No Ashtekar variables; no spin foams; no area/volume quantization |

*Estimates updated after each push cycle. Coverage increases when a derivation is completed
or a structural explanation is formalized. See CLAUDE.md Tier system for claim classifications.*

---

## Status and Open Problems

The model is in active development. For detailed tracking of open derivations, known failures, and internal tensions, see `ISSUES.md`. Full development history is in `push_history.md`.

**Established results:**

- Product topology and absolute proton stability (no proton decay at any energy, topological argument)
- Three-generation count from SU(3) fiber topology — exactly 3, not a free parameter
- Higgs mass: 124.4 ± 3.7 GeV (observed: 125.25 GeV)
- All four thermodynamic laws from folding mechanics
- Weinberg angle: sin²θ_W = 3/8 → 0.231 (no free parameters)
- Common gauge coupling g_eff = 0.54433 (0.006% agreement, 0 free parameters)
- τ lepton mass: m_τ = 1776.97 MeV (+0.006%, Tier 2a, 0 free params; Koide formula)
- Strong coupling α_s(M_Z): +0.006% via ECCC self-consistency condition
- Electroweak VEV: v = 247.83 GeV (+0.65%, Tier 2a)
- Fine structure constant: 1/α_em(M_c) = 36π ≈ 113.1 (+0.15%, Tier 2a)
- Strong CP: θ̄ = 0 from S⁵ CP-isometry (Tier 2a); no axion predicted
- arg(det M_q) = 0: closed via D6/D7 real amplitude theorem (Tier 2a)
- BPS duality S_kink × α_D5 = 1 (Tier 1 algebraic identity)
- α quadratic coupling: α = ∛18 (Tier 2a)
- β quartic coupling: β = 1/(9π) (Tier 2a/Tier 1 candidate)
- Yang-Mills mass gap: T2a complete; LaTeX proof draft with 12 citations, zero T2a steps on critical path

**Primary open derivations:**

- **α_em(0) algebraic identity** — A−B = ln(1/α_em(0)) gap of 0.044% (Tier 4)
- **Neutrino mass ratio m₃/m₂** — DFC predicts κ=5.33 vs observed 5.81 (−8.3%, Tier 2b)
- **Quark masses** — charm/strange approximately 15% below observed
- **G_Newton and ℏ** — not yet derivable from substrate parameters
- **Hadronic vacuum polarization** — δ(Δα)^{NP}=0.00102 from ρ+ω+φ; parton subtraction open
- **Fermion representation** — winding n=1 → fundamental rep (T3); Jackiw-Rebbi BVP path to T2a
- **String tension σ from D7 kink vacuum energy** — Tier 3 structural; formal proof requires constructive 4D QFT

---

## Foundational Reading Order

**Quickest entry point:** `educational/` — step-by-step modules written for any reader,
no physics background required. Modules 00–05 are complete; start with `00_overview.md`.

| Module | Topic |
|---|---|
| `00_overview.md` | What is DFC? One-page answer |
| `01_the_substrate.md` | The one object, V(φ), kinks |
| `02_how_space_appears.md` | Why space is emergent, not fundamental |
| `03_depth_map.md` | D1–D7 as compression stages |
| `04_forces.md` | How U(1)/SU(2)/SU(3) appear from fold topology |
| `05_particles.md` | Electrons, quarks, neutrinos as kink configurations |

**Technical reading order** (for those comfortable with physics notation):

**Conceptual foundations:**
1. `foundations/introduction.md` — Thought experiment, overview, string theory comparison
2. `foundations/overview.md` — The single starting point and core process
3. `foundations/premise.md` — Formal definitions of all terms (reference throughout)
4. `foundations/analogies.md` — Seven canonical analogies for building intuition
5. `foundations/d1_mechanics.md` — Concrete mechanical picture of D1 compression and buckling
6. `foundations/dimensional_emergence.md` — How dimensions are created by bifurcation
7. `foundations/formation.md` — D1→D4 buckling sequence; dimensional stack genesis
8. `foundations/dimensional_stack.md` — Layer ordering and particle spectrum as valences
9. `foundations/mathematics.md` — Why math is the residue of folding, not its substrate

**Structural predictions:**
10. `foundations/product_geometry.md` — Why force structures do not merge (proton stability)
11. `foundations/three_generations.md` — Why exactly three families of matter
12. `foundations/higgs_geometry.md` — Mass and symmetry breaking as field shape
13. `foundations/mass_hierarchy.md` — Electron vs. muon mass from local vs. global geometry
14. `foundations/substrate.md` — The mathematical substrate framework (kink model)

**Phenomena:**
15. `phenomena/gravity/general_relativity.md` — Gravity as folding gradient
16. `phenomena/light/light.md` — Light as near-D2 propagation mode
17. `phenomena/thermodynamics/thermodynamics.md` — Four laws derived from folding
18. `phenomena/quantum/quantum_mechanics.md` — QM as cross-dimensional structure behavior
19. `phenomena/quantum/interference.md` — Interference as field redistribution

---

## Relationship to Existing Theories

This model is not a replacement for the Standard Model or General Relativity. It provides a
generative substrate from which both emerge. It is not string theory, not loop quantum gravity,
not Kaluza-Klein, not grand unification — all of those begin by assuming some pre-existing
geometric structure. This model begins before geometry exists and builds it from compression
dynamics.

Key distinctions:
- **vs. String theory:** No pre-existing spacetime; dimensions are not curled up, they are
  created by bifurcation events in one self-compressing field.
- **vs. GUT (SU(5)/SO(10)):** GUT says three forces were once one force (a unified gauge
  group) that broke apart as the universe cooled. This model says the forces were never
  three separate things at any energy — they are always fold interactions of one object at
  different topological depths. This is a deeper unity, not a different route to the same
  conclusion: the substrate never "splits into three forces"; it always was one object
  whose fold interactions appear as three topological regimes.
- **vs. Kaluza-Klein:** No "extra" dimensions hidden inside larger ones; all dimensions are
  the same kind of thing — degrees of freedom opened by compression bifurcations — differing
  only in their self-interaction character.
- **vs. LQG:** No pre-existing quantum geometry to discretize; discreteness emerges from
  stable topological closure configurations in a continuous self-compressing field.

See `comparisons/` for detailed side-by-side analyses.
