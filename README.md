# Dimensional Folding Model — Repository

A theoretical physics model proposing that the Standard Model of particle physics is the observable
signature of twelve compactified extra dimensions with a specific product geometry.

---

## Core Claim

The universe has 16 dimensions. Four are the familiar spacetime. Twelve are compactified at scales
~10^-35 m — a billion billion times smaller than a proton. Their topology and geometry determine
every force, particle, and mass we observe.

---

## Repository Map

```
foundations/        Core postulates, geometry, and key structural choices
equations/          Runnable Python modules — input data, get predictions
phenomena/          Natural language explanations of physical observations
  particle_physics/ Masses, forces, proton stability, generations, Higgs
  cosmology/        Dark energy, expansion, inflation, early universe
  quantum/          Entanglement, measurement, gauge structure
comparisons/        This model vs. Standard Model, String Theory, GR, GUT
archive/            Original source documents (LaTeX and Markdown)
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
- Product geometry and proton stability argument
- Three-generation derivation from SU(3) fiber topology
- Geometric origin of Higgs potential (qualitative)
- Mass hierarchy mechanism (qualitative)

**In progress:**
- Quantitative Higgs mass prediction from compactification scale
- Neutrino mass spectrum from right-copy SU(3) flavor breaking
- Coupling constant unification via squashing parameter

**Open:**
- Derivation of fermion mixing angles (CKM, PMNS) from geometry
- Cosmological constant from compactification dynamics
- Dark matter candidates from stable higher KK modes

---

## Foundational Reading Order

For someone new to the model, read in this order:

1. `foundations/00_overview.md` — What the model is and isn't
2. `foundations/01_product_geometry.md` — The most important structural choice
3. `foundations/02_compactification.md` — The 16-dimensional setup
4. `foundations/03_three_generations.md` — Why exactly three families
5. `foundations/04_higgs_geometry.md` — The Higgs as shape
6. `foundations/05_mass_hierarchy.md` — Electron vs. muon mass
7. `foundations/06_dfc_substrate.md` — The deeper compression framework

---

## Relationship to Existing Theories

This model is not a replacement for the Standard Model or General Relativity. It is a geometric
interpretation that *reproduces* their structure from deeper principles. It is closest in spirit to
Kaluza-Klein theory and string compactification, but differs in:

- Using a rigid product geometry rather than a Calabi-Yau manifold
- Deriving the generation number topologically rather than from Hodge numbers
- Treating the Higgs as a metric modulus rather than a fundamental scalar
- Achieving coupling convergence through a squashing parameter rather than a single gauge coupling

See `comparisons/` for detailed side-by-side analyses.
