# Dimensional Folding Model — Repository

A theoretical physics model proposing that all of physics — forces, particles, mass, spacetime
itself — emerges from a single process: the compression and bifurcation of a near-1D unified
energy field.

---

## Core Claim

There is one thing. A fully interconnected energy field under compression toward a unified
one-dimensional state. As compression approaches its limit, bifurcation events occur — local
pockets collapse and eject energy, creating new dimensions. Repeated bifurcations produce
increasingly complex ejections that self-interact, forming stable knots and bottlenecks.
Those stable structures are what we observe as particles, forces, and fields.

---

## Repository Map

```
WRITING_GUIDE.md    How to write phenomenon descriptions (read before contributing)
foundations/        Core concepts, thought experiments, and structural arguments
  introduction.md   Originating thought experiment, overview, string theory comparison
  overview.md       The single starting point and core process
  ...               (other foundations docs)
equations/          Runnable Python modules — input data, get predictions
phenomena/          Natural language explanations of physical observations
  particle_physics/ Masses, forces, proton stability, generations, Higgs
  cosmology/        Dark energy, expansion, inflation, early universe
  quantum/          Entanglement, measurement, gauge structure
comparisons/        This model vs. Standard Model, String Theory, GR, GUT
archive/            Original source documents
data/               Observational reference values (PDG, cosmological)
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

## Status and Open Problems

The model is in active development. Current priorities:

**Completed (structural):**
- Product topology and proton stability argument
- Three-generation derivation from SU(3) knot topology
- Geometric origin of Higgs potential (qualitative)
- Mass hierarchy mechanism (qualitative)

**In progress:**
- Quantitative Higgs mass prediction from bifurcation scale
- Neutrino mass spectrum from flavor knot structure
- Coupling constant convergence via squashing parameter

**Open:**
- Governing equation for the pre-bifurcation field
- Derivation of U(1), SU(2), SU(3) topologies from compression dynamics
- Why exactly 4 observable dimensions (3 space + 1 time)
- Cosmological constant from compression budget
- Dark matter candidates from stable intermediate knot modes

---

## Foundational Reading Order

For someone new to the model, read in this order:

1. `foundations/introduction.md` — Thought experiment, overview, string theory comparison
2. `foundations/overview.md` — The single starting point and core process
3. `foundations/dimensional_emergence.md` — How dimensions are created by bifurcation
4. `foundations/product_geometry.md` — Why force structures do not merge (proton stability)
5. `foundations/three_generations.md` — Why exactly three families of matter
6. `foundations/higgs_geometry.md` — Mass and symmetry breaking as field shape
7. `foundations/mass_hierarchy.md` — Electron vs. muon mass from local vs. global geometry
8. `foundations/substrate.md` — The mathematical substrate framework (kink model)

---

## Relationship to Existing Theories

This model is not a replacement for the Standard Model or General Relativity. It provides a
generative substrate from which both emerge. It is not string theory, not loop quantum gravity,
not Kaluza-Klein, not grand unification — all of those begin by assuming some pre-existing
geometric structure. This model begins before geometry exists and builds it from compression
dynamics.

Key distinctions:
- **vs. String theory:** No pre-existing spacetime; dimensions are not curled up, they are created
- **vs. GUT (SU(5)/SO(10)):** No single broken symmetry; force structures emerge at different
  bifurcation stages with different knot topologies — they were never "one force"
- **vs. Kaluza-Klein:** No "extra" dimensions hidden inside larger ones; all dimensions are the
  same kind of thing, differing only in their self-interaction character
- **vs. LQG:** No pre-existing quantum geometry to discretize; discreteness emerges from
  stable knot configurations in a continuous field

See `comparisons/` for detailed side-by-side analyses.
