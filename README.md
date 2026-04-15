# Dimensional Folding Model — Repository

A theoretical physics model proposing that all of physics — forces, particles, mass, spacetime
itself — emerges from one self-compressing object: a continuous field that pulls inward on
itself, approaches a near-1D state through compression and bifurcation, and whose
self-closing bifurcation events produce the topological structures we observe as particles
and forces.

Forces are not fragments of a broken gauge symmetry. They are interaction behaviors between
different fold topologies of this one object — never three separate things at any energy,
always the same substrate appearing topologically distinct because its closures formed at
different compression thresholds.

---

## Core Claim

There is one thing. A continuous field that pulls inward on itself — this self-attraction
is the fundamental driver. That inward pull drives the field toward a near-1D state through
compression and bifurcation: when compression reaches a threshold, the field cannot compress
further without opening a new degree of freedom, and that opening is a bifurcation.

Bifurcations that close back on themselves — the field folding or wrapping back onto itself
due to compression — form topological closures. Those closures are what we observe as
particles, forces, and fields.

The three forces are not fragments of a broken unified force. They are always the same one
object's fold interactions, appearing as distinct force behaviors because their closures
formed at different compression thresholds with different topologies. The unity of this model
is deeper than gauge unification: there is one object, and its interactions with itself
at different fold depths are what we call electricity, the weak force, and color.

---

## Repository Map

```
WRITING_GUIDE.md          How to write phenomenon descriptions (read before contributing)

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
  bifurcation_dynamics.md γ_D = (16/3)√β RETRACTED (Cycle 48); E_kink/E_total(λ)=8/3 proved; Planck-length kink width; D-label disambiguation
  kink_scattering.md      Shape mode ω₁ = (√3/2)m_σ (parameter-free); first S-matrix from substrate (Born)
  bell_hidden_variables.md  DFC Bell resolution: Assumption 2 violated by D1/D2 connectivity; not conspiracy
  tsirelson_bound.md        Tsirelson CHSH ≤ 2√2 proved: C²=4I⊗I−[A₁,A₂]⊗[B₁,B₂]; SU(2) commutator norm ≤ 2
  kink_nucleation.md        Two-sector topology proved (φ⁴ kink); binary measurement outcomes; Born rule open
  depth_assignment.md       D-depth assignment problem: 5 constraints; Route B (Hopf S¹→S³→S⁵) most promising

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
  [STUBS — targets for future development]
  s_matrix.py             Full S-matrix beyond Born; exact kink-antikink; 3+1D Skyrme
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

phenomena/                Natural language explanations of physical observations
  particle_physics/
    proton_stability.md   Why the proton cannot decay (product topology argument)
    compton_scattering.md Thomson/Compton cross-section from DFC coupling chain (Cycle 50)
    muon_decay.md         W mass, Fermi constant, muon lifetime from DFC (Cycle 51; all <1%)
    forces/electroweak_precision.md  ρ, T, S parameters; five tree-level precision tests (Cycle 52)
  quantum/
    quantum_mechanics.md  Superposition, collapse, entanglement, tunneling, uncertainty
    interference.md       Wave interference as stationary field redistribution
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

**Current estimate: ~26.5%** (viability as a theory: ~40.5%; mathematical rigor: ~21.5%)

The model provides a coherent structural framework — the gauge sector, proton stability,
and several qualitative derivations are genuinely compelling. What it has not yet established
is that it *derives* rather than *reconstructs* the Standard Model. Three bottlenecks dominate:

1. **D-depth assignment mechanism** — why U(1) at D5, SU(2) at D6, SU(3) at D7 (not derived)
2. **First-principles coupling constants** — α_s, sin²θ_W, g_W (Route 3B gives sin²θ_W = 0.231; Cycle 51 extended the chain to M_W = 79.67 GeV, G_F = 1.168×10⁻⁵, τ_μ = 2.180 μs — all within 1%; deriving v = 246 GeV and M_c from substrate parameters is the next step)
3. **S-matrix derivation** — Cycle 50 computed Thomson σ_T (−4.3%); Cycle 51 computed weak sector predictions (all <1%); the r_U1/λ = 3/(4β) identification is blocked for pure real φ⁴ — requires substrate extension (complex scalar or gauge structure)

The Cycle 48 audit retracted the γ_D = (16/3)√β result (Cycle 32): the correct BPS E_kink
formula gives E_kink/E_total(λ) = 8/3 exactly — a universal constant, β-independent, and
greater than 1. The β ≈ 0.035 inference that depended on this is also retracted; β is now
Tier 3 (reference value). The next highest-value step: find an energy normalization
E_total(L) with macroscopic L derived from substrate dynamics that gives γ_D ∈ (0,1) with
β dependence — this would complete the depth-running derivation chain. The r_U1/λ formal
derivation requires extending the substrate beyond pure real φ⁴ — the U(1) phase has no
localizable mode on the real kink (both KK and worldvolume routes are blocked).

*Updated after every push. Full history in `CLAUDE.md`.*

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
