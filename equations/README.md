# DFC Equations Directory

This directory contains all runnable equation modules for the Dimensional Folding
Compression (DFC) model. Every file is a standalone Python script that can be run
directly to reproduce its predictions:

```bash
python3 equations/dfc_core.py              # parameter summary + self-test
python3 equations/substrate_simulation.py   # real-time kink dynamics
python3 equations/proton_stability.py       # neutron lifetime prediction
```

## Quick Start

**Want to understand the model?** Start here:

1. `dfc_core.py` — All parameters, constants, and core functions in one place
2. `substrate_simulation.py` — Watch kinks form from V(phi) in real time
3. `proton_stability.py` — See a concrete prediction (neutron lifetime, 0.1% match)

**Want to test an alternative framework?** Modify the core postulates:

```python
import dfc_core

# The entire model flows from these two numbers:
dfc_core.ALPHA = 3.0           # try a different alpha (default: 18^(1/3))
dfc_core.BETA = 0.05           # try a different beta  (default: 1/(9*pi))
dfc_core.recompute()           # propagate changes to all derived quantities

print(dfc_core.PHI_0)          # new vacuum value
print(dfc_core.M_SIGMA)        # new sigma mass
print(dfc_core.G_EFF_SQ)       # gauge coupling (unchanged — topological)
```

## Architecture

### Core Infrastructure

| File | Purpose |
|------|---------|
| `dfc_core.py` | **Shared constants, functions, and framework.** Import from here instead of redeclaring constants. Includes `V(phi)`, `kink_profile()`, `leapfrog_step()`, tier labels, and `recompute()` for testing alternatives. |
| `constants.py` | PDG observed values and SM parameters (legacy — `dfc_core.py` is preferred). |

### Simulations (Real-Time Dynamics)

These modules solve the field equation numerically and demonstrate DFC dynamics:

| File | What it simulates | Key result |
|------|-------------------|------------|
| `substrate_simulation.py` | 1+1D field evolution from phi=0 | Spontaneous kink formation, PT spectrum, open-to-closed mode transition |
| `complex_field_u1_simulation.py` | 2+1D complex field on Mexican hat | U(1) vortex formation, charge quantization from topology |
| `kink_kink_potential.py` | Kink-antikink interaction | Yukawa potential V ~ exp(-m_sigma * d), Manton comparison |
| `gauge_emergence_exploration.py` | Global-to-local gauge transition | Gauge field REQUIRED for finite energy (log divergence proof) |

### Prediction Modules (Quantitative Tests)

Each module computes one or more predictions from DFC parameters and compares to observation.
Modules print `[PASS]` or `[FAIL]` for each test.

#### Electroweak Sector

| File | Prediction | Error | Tier |
|------|------------|-------|------|
| `weinberg_angle_rg.py` | sin^2(theta_W) = 0.2312 | 0.01% | T2a |
| `muon_lifetime.py` | Z mass, G_F, muon lifetime | <1% | T2a |
| `z_boson_decays.py` | Z width, R_l, R_b, A_FB | <3% | T2a |
| `ew_radiative_corrections.py` | M_W with 1-loop Sirlin | 0.009% | T2a |
| `ewsb_cocrystallization.py` | EW VEV v = 247.83 GeV | 0.65% | T2a |
| `higgs_potential.py` | M_H = 124.4 GeV | 0.7% | T2a |

#### Strong Sector / QCD

| File | Prediction | Error | Tier |
|------|------------|-------|------|
| `alpha_em_selfconsistency.py` | alpha_s(M_Z) = 0.11821 | 0.006% | T2a |
| `d5_complex_from_instability.py` | g_eff^2 = 8/27 | 0.006% | T2a |
| `ym_string_tension.py` | sigma = Q_top * Lambda^2 | T2a | T2a |
| `meson_regge_spectrum.py` | rho, a2, rho3, a4 masses | <2.5% | T2a |
| `baryon_mass_dfc.py` | proton, Delta masses | <2% | T3 |
| `regge_intercept_derivation.py` | alpha_0 = 1/2 (meson) | T2a | T2a |

#### Lepton Masses

| File | Prediction | Error | Tier |
|------|------------|-------|------|
| `mass_spectrum.py` | mu/e mass ratio = 206.77 | 0.0% | T2a |
| `koide_phase_coupling.py` | tau mass from Koide | 0.006% | T2a |
| `quark_mass_kappa_derivation.py` | charm, strange masses | <2.5% | T2a |

#### Cosmology

| File | Prediction | Error | Tier |
|------|------------|-------|------|
| `cosmology.py` | H_0 = 67.26 km/s/Mpc | 0.2% | T2a |
| `bbn_predictions.py` | Y_p, D/H, He-3/H | <5% | T2a |
| `cosmological_predictions.py` | Lambda, CMB first peak | <1% | T2a-T3 |
| `cosmological_predictions_2.py` | w_Lambda, BAO, dark matter | T2a-T4 | mixed |

#### Atomic / Precision

| File | Prediction | Error | Tier |
|------|------------|-------|------|
| `anomalous_magnetic_moment.py` | electron g-2 (4-loop) | 0.14% | T2a |
| `lamb_shift.py` | 2S-2P splitting | 0.69% | T2a |
| `scattering_cross_sections.py` | Thomson cross-section | 0.28% | T2b |
| `atomic_structure.py` | hydrogen ground state | 0.28% | T2b |

#### Nuclear Physics

| File | Prediction | Error | Tier |
|------|------------|-------|------|
| `proton_stability.py` | neutron lifetime = 878.4 s | 0.1% | T2a |
| `nucleon_magnetic_moments.py` | mu_p/mu_n ratio | 2.75% | T3 |
| `nuclear_binding_energy.py` | SEMF coefficients from kink | mixed | T3 |
| `pion_mass_gmor.py` | m_pi from GMOR | 1.9% (route 3) | T2a |

#### Topological / Structural

| File | Prediction | Key result | Tier |
|------|------------|------------|------|
| `spin_zero_mode.py` | Spin-1/2 from JR zero mode | J_min = 1/2 exactly | T1 |
| `depth_bifurcation_dynamics.py` | V(phi) -> gauge groups | 12-step chain | T2a |
| `alternative_potentials.py` | Why phi^4? | 6 topological, 9 phi^4-specific | T2a |
| `helfrich_membrane_gravity.py` | Kink bending rigidity | kappa = 4.64 M_Pl^2 (overshoots) | T2a |

### Yang-Mills Mass Gap (Clay Prize)

| File | Purpose |
|------|---------|
| `ym_clay_proof.tex` | Complete LaTeX proof document (12 citations) |
| `ym_string_tension.py` | String tension from BPS bound |
| `ym_constructive_qft.py` | OS axioms verification |
| `ym_balaban_rg.py` | Balaban RG + Haar moments |
| `ym_seiler_simon_su3.py` | Seiler-Simon SU(3) moment bounds |

## How to Read an Equation Module

Every module follows the same pattern:

1. **Docstring** — what physical question it addresses, the DFC mechanism, key references
2. **Constants** — DFC parameters used (will migrate to `dfc_core.py` imports)
3. **Parts A, B, C...** — each part tests one aspect of the prediction
4. **Assertions** — `[PASS]` / `[FAIL]` checks with clear labels
5. **Summary** — total pass/fail count and tier assessment

## Tier System

| Tier | Meaning | Example |
|------|---------|---------|
| T0 | Core postulate (assumed) | V(phi) = -alpha/2 phi^2 + beta/4 phi^4 |
| T1 | Mathematically exact | Q_top = 2 (topological charge) |
| T2a | Verified prediction, <5% error | neutron lifetime (0.1%) |
| T2b | Equation exists, >5% error | neutrino mass ratio (8.3%) |
| T3 | Structural argument only | proton mass from Regge |
| T4 | Qualitative / speculative | dark matter mass |

## Testing Alternatives

The modular design lets you test what happens when you change any postulate:

**Different potential?** Override `V()` and `dVdphi()` in `dfc_core.py`, then run
any equation module. The phi^6, sine-Gordon, and double-cosine alternatives are
already compared in `alternative_potentials.py`.

**Different gauge group?** Change `N_C` and `Q_TOP` in `dfc_core.py` and call
`recompute()`. The I4 uniqueness theorem (`I4 = 4/3` selects N_c = 3) is in
`depth_bifurcation_dynamics.py`.

**Different number of generations?** The derivation from D6 SU(2) topology is in
`depth_bifurcation_dynamics.py` Part B. The count N_gen = 3 follows from PT s=2
giving exactly 1 bound state per kink.
