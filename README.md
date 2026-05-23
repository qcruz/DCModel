# Dimensional Folding Model — Repository

A theoretical physics model under development. The starting postulate is a single
self-compressing scalar field with a double-well potential V(φ) = −α/2 φ² + β/4 φ⁴.
The model proposes that the particle content and gauge structure of the Standard Model
arise from the topology of bifurcation events in this field, without assuming pre-existing
spatial dimensions, gauge groups, or particle species.

Current status: ~63% complete by internal estimate. Several Standard Model quantities
are reproduced to <1–5%, others remain unresolved. See the completeness estimate and
known failures below.

---

## Core Derivations

Five results derived directly from `V(φ) = −α/2 φ² + β/4 φ⁴` and winding-number topology. Each follows from the compression mechanics with no free parameters beyond the substrate quartic β ≈ 0.035. All expressions are Wolfram Alpha-verifiable.

- **Gauge coupling constant** — paste `sqrt(8*pi*0.035/3)` → **0.5423**
  Kink phase stiffness f² = (4/3)(φ₀²/ξ) from the Bogomolny identity ∫sech⁴(u)du = 4/3. Holonomy radius r = 3ξ/(4β) gives g² = 8πβ/3. With β = 0.035: g = 0.5423. Observed at SM unification scale: g_common = 0.5443 (**0.4% agreement**; [`equations/coupling_derivation.py`](equations/coupling_derivation.py)).

- **Weinberg angle** — paste `(3/5) / (1 + 3/5)` → **3/8 = 0.375**
  Hypercharge normalization k_Y = 3/5 from Dynkin index matching on SM matter content (no GUT assumed). Equal closure couplings g₁ = g₂ → sin²θ_W = k_Y/(k_Y + 1) = 3/8 at threshold. RG running to M_Z: sin²θ_W = 0.2312. Observed: 0.2312 (**<0.01% agreement**; [`equations/weinberg_angle_rg.py`](equations/weinberg_angle_rg.py)).

- **φ⁴ kink shape-mode frequency** — paste `sqrt(3)/2` → **0.8660**
  The φ⁴ kink fluctuation potential V''(φ_kink) = 2α − (6/ξ²)sech²(x/ξ) is an exact n=2 Pöschl-Teller potential. Bound-state eigenvalues: ω₀² = 0 (translation zero mode) and ω₁² = (3/2)α (shape mode). Ratio: ω₁/m_σ = √((3/2)α)/√(2α) = √3/2. Verified numerically to 2.5 × 10⁻⁵ ([`equations/coupled_fluctuation.py`](equations/coupled_fluctuation.py)).

- **Tsirelson bound (quantum Bell inequality)** — paste `sqrt(8)` → **2√2 ≈ 2.828**
  CHSH operator C = A₁⊗B₁ + A₁⊗B₂ + A₂⊗B₁ − A₂⊗B₂ satisfies C² = 4I⊗I − [A₁,A₂]⊗[B₁,B₂]. For ±1 observables ‖[Aᵢ,Aⱼ]‖ ≤ 2, so ‖C‖² ≤ 4 + 4 = 8 → CHSH ≤ 2√2. Proved algebraically from substrate SU(2) geometry with no quantum formalism assumed ([`equations/bell_correlations.py`](equations/bell_correlations.py)).

- **Superconducting flux quantum** — paste `6.626e-34 / (2 * 1.602e-19)` → **2.068 × 10⁻¹⁵ Wb**
  U(1) single-valuedness of the condensate configuration Ψ = |Ψ|e^{iθ} on any closed path → ∮∇θ·dl = 2πn → enclosed flux Φ = nh/(2e). Zero free parameters; relative error 2.2 × 10⁻¹⁰ against CODATA ([`equations/superconductivity.py`](equations/superconductivity.py)).

---

## Core Claims

The model rests on three postulates:

1. One continuous self-compressing scalar field exists. No pre-existing space, gauge group, or particle content is assumed.
2. The field's self-interaction potential has the double-well form V(φ) = −α/2 φ² + β/4 φ⁴, with free parameters α (quadratic coupling) and β (quartic coupling).
3. When compression reaches a threshold, the field opens a new degree of freedom rather than compressing further. These bifurcation events produce all structure in the model.

The model proposes that the gauge groups U(1), SU(2), SU(3) arise from the topology of these bifurcation closures at different compression depths — a correspondence that has been worked out structurally through zero-mode counting (Cycles 59–74) but is not yet a complete first-principles derivation. Quantitative predictions for gauge couplings, Weinberg angle, W/Z masses, and Higgs mass match observation at the 0.01%–5% level, with derivation chains of varying completeness. Known failures include the τ lepton mass (dimple model 8.4× off; Koide formula Tier 3 candidate gives <0.01% with 0 free params), neutrino hierarchy (4.3× off), and α_s (8.1% off). Planck's constant and Newton's constant are not yet derivable within the current framework.

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
  bifurcation_dynamics.md γ_D = (16/3)√β RETRACTED (Cycle 48); E_kink/E_total(λ)=8/3 proved; Planck-length kink width; D-label disambiguation
  kink_scattering.md      Shape mode ω₁ = (√3/2)m_σ (parameter-free); first S-matrix from substrate (Born)
  bell_hidden_variables.md  DFC Bell resolution: Assumption 2 violated by D1/D2 connectivity; not conspiracy
  tsirelson_bound.md        Tsirelson CHSH ≤ 2√2 proved: C²=4I⊗I−[A₁,A₂]⊗[B₁,B₂]; SU(2) commutator norm ≤ 2
  kink_nucleation.md        Two-sector topology proved (φ⁴ kink); binary measurement outcomes; Born rule open
  depth_assignment.md       D-depth assignment problem: 5 constraints; Route B (Hopf S¹→S³→S⁵) most promising
  compression_dynamics.md   DFC self-compression equations reconciled with thermodynamic/elastic/acoustic/gravitational formalisms
  measurement.md            Measurement as buckling threshold; six measurement types; Born rule status

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
  s_matrix.py             Exact single-kink T(q) (Cycle 89): reflectionless n=2 PT, |T|²=1 to 4×10⁻¹⁶; Levinson δ(0⁺)=2π; open: DHN kink-antikink exact
  coupling_derivation.py  α_em, g_W, g_s from substrate (α, β, c) — Bottleneck 2
  planck_constant.py      ℏ from DFC substrate characteristic scales
  dark_matter.py          Stable intermediate kink modes as dark matter candidates
  cosmological_constant.py  Λ from residual compression budget
  beta_substrate.py       Derive β ≈ 0.035 from pre-substrate principle
  fermion_spectrum_full.py  Full lepton+quark mass spectrum (τ/top failures to fix)
  holographic_entropy.py  Bekenstein-Hawking from closure capacity
  baryogenesis.py         Matter-antimatter asymmetry at D7 phase transition
  inflation.py            Inflation as D1→D4 bifurcation cascade; n_s prediction
  scattering_cross_sections.py  σ_Thomson, Compton from DFC coupling chain (Cycle 50; −4.3% systematic)
  muon_lifetime.py        M_W, M_Z, G_F, τ_μ from DFC coupling chain (Cycle 51; all <1%)
  electroweak_precision.py  ρ=1, T=0, sin²θ_W consistency — five EW precision tests (Cycle 52)
  pair_production.py      e⁺e⁻ → μ⁺μ⁻ cross-section; R-ratio = 11/3 (exact Tier 1); kink-antikink nucleation (Cycle 54)
  anomalous_magnetic_moment.py  a_e = α_em/(2π) from DFC coupling chain; −2.01% systematic (Cycle 55)
  josephson_effect.py     K_J=2e/h verified to 7.75×10⁻¹⁶; Shapiro steps, SQUID, Josephson inductance (Cycle 90)
  scattering_length.py    a_s=3/M_c=3λ, r₀=11/(6M_c)≈1.833λ, τ_W(0)=−a_s; all exact, 0 free params (Cycle 91)
  kink_form_factor.py     F(k)=πκ(κ²+4)/(8 sinh(πκ/2)); ⟨r⟩_rms=√((π²���6)/4)/M_c≈0.984λ; Tier 1 (Cycle 92)
  z_boson_decays.py       Γ_Z=2456 MeV (−1.56%), Γ_inv=493 MeV (−1.16%), R_l (−0.10%), R_b (+1.58%), A_FB^lep (+3.17%); 7 Tier 2a predictions from β+v (Cycle 93)
  [STUBS — structural account written, quantitative derivation open]
  nuclear_binding.py      Bethe-Weizsäcker formula; Yukawa potential; Fe-56 peak; DFC α_s 11% blocks strong predictions
  lamb_shift.py           Hydrogen 2s-2p Lamb shift; self-energy loop integral stub; α⁵ scaling estimate
  quark_gluon_plasma.py   QGP deconfinement T_c; DFC Λ_QCD estimate; −80% (Cycle 120 RG fix; one-loop breakdown)

phenomena/                Natural language explanations of physical observations
  particle_physics/
    proton_stability.md   Why the proton cannot decay (product topology argument)
    compton_scattering.md Thomson/Compton cross-section from DFC coupling chain (Cycle 50)
    muon_decay.md         W mass, Fermi constant, muon lifetime from DFC (Cycle 51; all <1%)
    forces/electroweak_precision.md  ρ, T, S parameters; five tree-level precision tests (Cycle 52)
    pair_production.md    Pair production/annihilation as kink-antikink nucleation/coalescence; R-ratio (Cycle 54)
  quantum/
    anomalous_magnetic_moment.md  a_e = α_em/(2π) Schwinger term; DFC −2.01% systematic; muon g-2 (Cycle 55)
    quantum_mechanics.md  Superposition, collapse, entanglement, tunneling, uncertainty
    interference.md       Wave interference as stationary field redistribution
    lamb_shift.md         [STUB] Hydrogen 2s-2p splitting; DFC self-energy loop integral; α⁵ scaling
    photoelectric_effect.md  [STUB] Photon absorption as threshold crossing; ℏ blockage
    hawking_radiation.md  [STUB] Horizon pair nucleation; T_H blocked by G_Newton and ℏ
  condensed_matter/
    superconductivity.md  Cooper pairs as D6 kink bound states; Φ₀=h/(2e) Tier 1 ✓; K_J Tier 1 ✓ (Cycle 60)
    superfluidity.md      Global phase coherence; κ₀=h/m Tier 1 ✓; BEC BLOCKED (Cycle 61)
    quantum_hall_effect.md  TKNN Chern number = DFC winding number; R_K Tier 1 ✓; FQHE structural (Cycle 61)
    josephson_effect.md   DC CPR I=I_c sin(δ); AC f_J=K_J×V; Shapiro steps; SQUID; all Tier 1 from K_J=2e/h (Cycle 90)
  gravity/
    general_relativity.md Gravity as folding gradient and dimensional pressure
  light/
    light.md              Light as near-D2 mode; c as boundary slope, not velocity
  thermodynamics/
    thermodynamics.md     All four laws derived from folding mechanics
    heat_and_conductivity.md  Heat, conduction, resistance, radiation unified

comparisons/              This model vs. Standard Model, String Theory, GR, GUT
  swot.md                 SWOT analysis: DFC strengths/weaknesses vs. all major theories
practical_applications/   Engineering limits and implications derived from DFC
  OVERVIEW.md             Document type protocol and rotation guide
  fundamental_limits.md   Five canonical engineering ceilings from substrate structure
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

**Current estimate: ~63%** (viability as a theory: ~74%; mathematical rigor: ~52%)

**Model Reconcilability Risk Score (MRRS)** — probability current postulates *cannot* complete each scope (lower = better):

| Scope | MRRS | Key blocker |
|---|---|---|
| Core gauge/coupling sector | **20%** | α_s (8.1% off, M_c(D7) open); τ mass |
| Full SM reproduction | **48%** | τ mass mechanism; M_c(D7) derivation |
| Complete theory (SM + gravity + QM) | **72%** | ℏ derivability; G_Newton |

*Cycle 117: Bottleneck 2 closed (β=1/(9π) Tier 2a); Core reduced 28→20%, Full 58→48%.*

*Full per-failure analysis with paths and swing factors in `comparisons/reconcilability_risk.md`.*

The model provides a coherent structural framework — the gauge sector, proton stability,
and several qualitative derivations are genuinely compelling. What it has not yet established
is that it *derives* rather than *reconstructs* the Standard Model. Three bottlenecks dominate:

1. **D-depth assignment mechanism** — Bottleneck 1 FULLY CLOSED (Cycle 73): PT parameter s=2 exact for φ⁴ kink → s=2 PT has exactly 2 bound states → zero mode unique by Sturm-Liouville → each threshold adds exactly 1 zero mode → n thresholds → SU(n). Combined with Cycles 59–72: D5=U(1), D6=SU(2), D7=SU(3) derived from V(φ). Remaining open: threshold positions α₅, α₆, α₇ from substrate.
2. **First-principles coupling constants** — Route 3B gives sin²θ_W = 0.231; Cycles 51–52 extended to M_W, G_F, τ_μ (all <1%); Cycle 93: Z boson widths Γ_Z/Γ_inv/R_l/R_b/A_FB^lep (all <5%, Tier 2a); Cycle 94: full DFC–SM Lagrangian assembled (foundations/dfc_sm_lagrangian.md). Bottleneck 2: g² = 2π×β×I₄ compact form proved; 3-step chain f²→r_U1→g² complete given β; β=1/(9π) from Hopf fiber dim sum N_Hopf=9 → g²=8/27 exactly (0.006% vs SM); Cycles 110–112: g_1²=2I₄ derived from V(φ) via BPS superpotential (Q_top=2, I₄=4/3, det(g)=2I₄, Tier 1); Cycle 114: DFC 5D collective coordinate action derived explicitly — both g_XX=I₄ and g_θθ=Q_top=2 shown from the 5D action integrals; two independent routes to g₁²=2I₄ (moduli det and KK formula) agree exactly. Cycle 115: R₁=π/I₄ PROVED algebraically (fiber_radius_derivation.py) — R₁=2π/g₁²=π/I₄ is a consequence of g₁²=det(g)=2I₄; Cycle 106 series holonomy R_n=πd_n/I₄ is now a THEOREM (all three fibers verified, errors 0.00e+00); Tier upgrades: R₁ Tier 4→2, R_n Tier 3→2/3. Cycle 116: d_n=2n−1 DERIVED from V(φ) at Tier 3 (fiber_dimension_derivation.py). Cycle 117: BOTTLENECK 2 CLOSED — Tier 2a (d5_complex_from_instability.py) — D5 complex structure J derived from V(φ) via tachyonic instability: L₂=−∂²−αsech²(x/ξ) is PT s=1 with exact ω²₀=−α/2 < 0 for all α (1 negative eigenvalue); Tier 0 "no preferred direction" → O(2) symmetry → unique V(|Φ|²); U(1) → J (J²=−I error 0.00e+00) → d_n=2n−1 → g_eff²=8/27 (error 0.00e+00, 0 free params, 0.006% vs SM) → β=1/(9π). Full chain tier: all Tier 1 from V(φ), result Tier 2a. Bottleneck 3: v = 246 GeV from D6/D7 overlap integral; λ_H = β/4 UV BC stabilizes Higgs vacuum (Tier 1, Cycle 86).
3. **S-matrix derivation** — Cycle 89: exact single-kink T-matrix (reflectionless n=2 PT, Tier 1); Cycle 91: effective range theory a_s=3λ, r₀=1.833λ (exact); Cycle 92: kink form factor F(k) exact. α_s: target M_c(D7) = 1.566×10¹⁵ GeV (8.1% gap; Cycle 119). τ lepton mass: Koide formula gives m_τ=1776.97 MeV (+0.006%, 0 free params) from Z₃ circulant Yukawa structure (Cycle 122, Tier 3); Koide ↔ DFT |F₀|/|F₁|=√2 proved algebraically (Cycle 123); Step 3 (Z₃ isometry → circulant Yukawa) formalized at Tier 3 (Cycle 124: koide_step3_yukawa.py); Step 4 (|F₀|/|F₁|=2/√Q_top=√2 since Q_top=2) formalized at Tier 3 (Cycle 125: koide_step4_bps.py; algebraic proof error 3.55e-15; r²=Q_top to 18 ppm; open Tier 4: derive r=√Q_top from DFC 5D action).

The Cycle 48 audit retracted the γ_D = (16/3)√β result (Cycle 32): the correct BPS E_kink
formula gives E_kink/E_total(λ) = 8/3 exactly — β-independent. β is Tier 3 (reference value);
self-consistently determined as β = 3g_common²/(8π) = 0.03536 (Cycle 87) conditional on Bottleneck 2 proof.

*Updated after every push. Full push history in `CLAUDE.md`.*

---

## Coverage of Existing Theories

How much of each major theory's key content (derivations, predictions, structural explanations)
has been replicated or superseded within the DFC framework. These are honest estimates, not
aspirational targets. A theory is "covered" when DFC either reproduces the result from DFC
substrate parameters or provides a structural explanation for *why* the result takes the form
it does. Percentage reflects breadth of coverage, not accuracy of any single result.

| Theory | Coverage | What DFC Has | What's Missing |
|---|---|---|---|
| **Quantum Mechanics** | ~42% | Schrödinger eq. (derived from KG); spin-1/2 (FR/JR derivation); Born rule for spin (derived); binary outcomes (proved); Tsirelson bound (proved); g-2 Schwinger term (−2.01% systematic); superposition/entanglement/tunneling/decoherence (structural) | Born rule for position (OPEN); Lamb shift (stub); path integral; ℏ from substrate (OPEN) |
| **Thermodynamics** | ~55% | All four laws (derived from folding mechanics); arrow of time (derived from Z₂ topology); blackbody Planck spectrum (structural, modulo ℏ); Boltzmann statistics (structural); heat/conduction (structural); compression dynamics reconciled (Cycle 56) | Fluctuation theorems (Jarzynski, Crooks); Carnot efficiency formula from DFC |
| **Standard Model** | ~36% | U(1)×SU(2)×SU(3) product structure (derived); 3 generations (derived); proton stability (zero rate); parity violation (JR chirality); sin²θ_W (<0.01%); m_μ/m_e (exact); M_W/M_Z/G_F/τ_μ (<1%); Higgs (124.4 GeV); R-ratio = 11/3 (exact) | CKM/PMNS; τ mass (8.4× off); α_s (11% off); Feynman rules; loop corrections |
| **General Relativity** | ~15% | Gravity as folding gradient (structural); gravitational waves (structural); black holes (structural); Hawking radiation (stub); time dilation; H₀ (0.2%) | Einstein field equations not derived; G_Newton not derived; Schwarzschild metric not derived |
| **ΛCDM Cosmology** | ~20% | H₀ (0.2% match); CMB (structural); Big Bang (structural); flatness/horizon dissolved; dark energy (structural, qualitative) | Inflation (stub); dark matter (stub); baryogenesis (stub); Λ from substrate (stub) |
| **QFT (perturbative)** | ~14% | Born S-matrix; Thomson/Compton (−4.3%); Pöschl-Teller (exact); pair production (R-ratio exact, σ −3.1%); g-2 leading term (−2.01%); RG running | Loop corrections (Lamb shift stub, 2-loop g-2); Feynman rules; renormalization |
| **Condensed Matter** | ~12% | Φ₀=h/(2e) Tier 1 ✓ (Cycle 60); K_J Tier 1 ✓; R_K=h/e² Tier 1 ✓ (Cycle 61); κ₀=h/m Tier 1 ✓; all three from same DFC U(1) winding; IQHE plateaus structural | BCS gap equation; Ginzburg-Landau; FQHE; roton gap; band structure; solid-state spectrum |
| **String Theory** | ~3% | Some topological overlaps (compact closure geometries, Hopf fibrations); DFC has no pre-existing spacetime | No strings/branes; no T/S-duality; fundamentally different framework |
| **Loop Quantum Gravity** | ~5% | Discrete topological closures analogous to spin networks; binary outcomes proved | No Ashtekar variables; no spin foams; no area/volume quantization |

*Estimates updated after each push cycle. Coverage increases when a derivation is completed
or a structural explanation is formalized. See CLAUDE.md Tier system for claim classifications.*

---

## Status and Open Problems

The model is in active development. Current priorities:

**Completed (structural):**
- Product topology and proton stability argument
- Three-generation derivation from SU(3) knot topology
- Higgs mass: 124.4 ± 3.7 GeV (observed: 125.25 GeV); uncertainty dominated by unresolved λ₀ boundary condition
- Mass hierarchy mechanism (qualitative)
- All four thermodynamic laws derived from folding mechanics
- Gravity, light, QM, interference derived from folding framework
- Mathematics reframed as emergent folding grammar (19-field ordered map)
- Weinberg angle: sin²θ_W = 3/8 at closure scale → 0.231 via SM RG running (self-consistent, no new free parameters)

**In progress:**
- Neutrino mass spectrum from flavor knot structure
- Coupling constant convergence via squashing parameter
- Carnot efficiency formula derived from folding geometry (not ideal gas)

**Open:**
- Governing equation for the pre-bifurcation field
- Derivation of U(1), SU(2), SU(3) topologies from compression dynamics
- Why exactly 4 observable dimensions (3 space + 1 time)
- Cosmological constant from compression budget
- Dark matter candidates from stable intermediate knot modes
- Derivation of E = hν from folding geometry (Planck relation)
- Fluctuation theorems (Jarzynski, Crooks) from folding mechanics
- Einstein field equations from dimensional folding gradient dynamics
- Holographic entropy bound from closure capacity

---

## Foundational Reading Order

For someone new to the model, read in this order:

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
