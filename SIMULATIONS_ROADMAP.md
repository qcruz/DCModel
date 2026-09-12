# DFC Simulation Roadmap

**Purpose:** Strategic plan for simulation development — what to build, what to extract,
and how each simulation connects to the DFC model's predictions and open problems.

**Last updated:** Cycle 588 (2026-09-11)

---

## Guiding Principles

1. **Simulations are Tier 1 structural proofs.** When V(φ) dynamics produce a claimed
   behavior numerically, that is a mathematical theorem of the field equation — not
   an approximation or fit. Every simulation module should make clear what structural
   claim it demonstrates.

2. **Priority order for new simulations:**
   - (A) Simulations that could resolve T4 stalled items or known failures
   - (B) Simulations that demonstrate previously unverified DFC structural claims
   - (C) Simulations that extend existing results to higher dimensions or complexity
   - (D) Simulations that make new testable predictions

3. **Every simulation uses only DFC parameters:** α = ∛18, β = 1/(9π). No SM inputs
   unless explicitly marked as external.

4. **All simulations are standalone runnable:** `python3 equations/module.py` produces
   output with [PASS]/[FAIL] checks.

---

## Phase 1: Completed Simulations — What We Have Learned

### 1.1 Kink Formation and Structure (Foundation Layer)

| Module | What it demonstrates | Key quantitative result | Tier |
|--------|---------------------|------------------------|------|
| `substrate_simulation.py` (C540) | Kinks form spontaneously from tachyonic instability in V(φ) | Profile matches tanh(x/ξ) exactly; PT spectrum verified; open→closed mode transition | T1 |
| `poschl_teller_spectrum.py` (C543) | Kink fluctuation spectrum is exactly PT with s=2 | Shape mode mass 0.0005% of exact; 2 bound states + continuum | T1 |

**What we learned:** The kink is not postulated — it is a dynamical inevitability of V(φ).
Any initial perturbation near the unstable maximum spontaneously nucleates kink-antikink
pairs. The fluctuation spectrum (Pöschl-Teller) determines all subsequent physics:
the mass gap, the shape mode (which gives one-loop corrections to α_em and κ), and
the scattering properties.

### 1.2 Kink Interactions and Particle Physics Analogues

| Module | What it demonstrates | Key quantitative result | Tier |
|--------|---------------------|------------------------|------|
| `kink_antikink_annihilation.py` (C542) | KA collision: resonance windows, mass-gap radiation, E=mc² | Topological charge Q conserved exactly; radiation peaked above m_σ; energy partition measured | T1 |
| `oscillon_breather_formation.py` (C551) | Long-lived oscillating bound state (meson analogue) | ω = 0.75m_σ, Q = 4313, lifetime 1373 periods, sech profile | T3 |
| `multi_kink_gas_dynamics.py` (C567) | Multi-particle gas: annihilation, pair creation, thermalization | 4 KA pairs interact; Q=0 exact; virial ratio 1.25; pair creation from radiation | T2b |

**What we learned:** Kink-antikink annihilation converts topological rest mass to radiation
at frequencies above the mass gap — this is E = mc² as a theorem of V(φ). The oscillon
(meson analogue) shows that quasi-bound states emerge naturally from kink collisions,
with frequencies below the mass gap that prevent rapid decay. The multi-kink gas
demonstrates emergent statistical mechanics: thermalization, equipartition, and even
pair creation from radiation (the substrate analogue of pair production).

### 1.3 Gauge Structure Emergence (D5)

| Module | What it demonstrates | Key quantitative result | Tier |
|--------|---------------------|------------------------|------|
| `complex_field_u1_simulation.py` | U(1) vortex formation from 2+1D tachyonic instability | Winding number Q ∈ ℤ from topology; charge conservation exact | T1 |
| `tachyonic_complexification_sim.py` (C559) | Real kink unstable → complexifies to vortex; U(1) forced | γ = √(α/2) confirmed to 2.9%; 10381× amplification; Δθ = π | T2a |
| `vortex_antivortex_annihilation.py` (C585) | 2+1D vortex + antivortex annihilate; charge conserved | Q=0 exact (max |Q| = 0.008); radiation peaked at ω = 1.12m_σ | T2a |
| `gauge_emergence_exploration.py` (C531) | Gauge field necessity from energetic argument | Global vortex E=∞ → gauge field required → Maxwell from δE/δA=0 → e² = 8/27 | T2a |

**What we learned:** The D5 gauge structure is not assumed — it is forced by energetics.
A real kink in 2+ dimensions is tachyonically unstable; the only stable configuration
is a complex vortex with quantized winding number. The vortex demands a gauge field
(to avoid infinite gradient energy), and the gauge coupling e² = 8/27 follows from the
kink moduli metric. Vortex-antivortex annihilation demonstrates that topological charge
is created and destroyed only in ± pairs — the substrate analogue of particle-antiparticle
annihilation.

### 1.4 Gravity Mechanism (D4)

| Module | What it demonstrates | Key quantitative result | Tier |
|--------|---------------------|------------------------|------|
| `kink_gravity_gradient.py` (C575) | Kink accelerates in compression gradient — Newtonian regime | a = -(3/(2α))(dα/dx) matches theory to 0.6%; a ∝ ε linear; C_grav = 1.49 | T1 |
| `analog_gravity_dispersion.py` (C564) | PT reflectionless barrier → superluminal dispersion + Hawking robustness | PT λ=2 reflectionless T1; superluminal exp(-πkξ); Hawking spectrum robust | T1/T3 |

**What we learned:** Gravity in DFC is a gradient effect: kinks move to minimize their
rest mass M ∝ α^{3/2}, producing parabolic (Newtonian) trajectories. The acceleration
is perfectly linear in gradient strength — Newton's second law as a substrate theorem.
The analog gravity simulation shows that kink backgrounds are reflectionless (Pöschl-Teller),
which connects to the robustness of Hawking radiation predictions.

---

## Phase 2: Queued Simulations — What We Need Next

### 2.1 HIGH PRIORITY — Directly Addresses T4/Stalled Items

#### S1: Kibble-Zurek Kink Density vs Quench Rate
- **Module:** `equations/kibble_zurek_kink_density.py`
- **What to simulate:** Cool the substrate through the tachyonic phase transition
  (α(t) goes from negative to positive) at different quench rates τ_Q.
- **What to measure:** Kink density n_kink vs τ_Q. Theory: n ∝ τ_Q^{-ν/(1+νz)}
  with mean-field ν = 1/2, z = 2 → n ∝ τ_Q^{-1/4}.
- **DFC prediction:** The exponent depends only on the universality class of V(φ),
  which is mean-field (φ⁴ at upper critical dimension d=4).
- **Addresses:** Dark matter relic abundance (T4, C554) — Kibble-Zurek overproduces
  by 10⁷×. Can we identify the correct production mechanism from the simulation?
  Also connects to cosmological defect formation and BBN constraints.
- **Milestone:** Verify KZ scaling exponent; measure inter-kink spacing distribution;
  extract correlation length at freeze-out.

#### S2: Compression-Driven Bifurcation Cascade
- **Module:** `equations/compression_cascade_sim.py`
- **What to simulate:** Start with uniform field in a single minimum. Slowly increase
  α(t) (compression deepens). Watch for sequential symmetry breaking events that
  produce structures at successive depth scales.
- **What to measure:** Timing and order of bifurcation events; whether the cascade
  naturally produces structures at D3, D5, D6, D7-like depths; whether the hierarchy
  of scales matches DFC depth assignments.
- **Addresses:** D-label assignments (currently working hypotheses); threshold
  positions α₅, α₆, α₇ (T4, C526); the fundamental question of whether compression
  produces a depth hierarchy at all.
- **Milestone:** Observe at least 2 sequential bifurcation events; measure the
  compression ratios between them; compare to DFC depth spacing predictions.

#### S3: Y-Junction Dynamics and Baryon Formation
- **Module:** `equations/y_junction_dynamics.py`
- **What to simulate:** 2+1D complex field with 3 vortex strings meeting at a
  junction. Initialize a Y-junction configuration and evolve.
- **What to measure:** Junction stability; force balance angles (should be 120°
  for equal tensions); oscillation modes; whether the junction carries angular
  momentum; decay channels.
- **Addresses:** Baryon Regge intercept junction penalty (T3→T2a, C587);
  baryon structure generally; Y-junction BVP (P3 item).
- **Milestone:** Demonstrate stable Y-junction; verify 120° force balance;
  measure junction oscillation frequencies; check if junction carries zero
  angular momentum (confirming the frozen-DOF derivation from C587).

### 2.2 MEDIUM PRIORITY — Extends Verified Results

#### S4: Kink-Kink Repulsion (Pauli Exclusion Analogue)
- **Module:** `equations/kink_kink_repulsion.py`
- **What to simulate:** Two same-sign kinks (both kink, or both antikink)
  approaching each other.
- **What to measure:** Repulsive force vs separation; compare to Manton's
  prediction F ∝ exp(-m_σ d). Topological exclusion should prevent overlap.
- **Addresses:** Spin-statistics connection — topological exclusion of identical
  kinks is the substrate analogue of Pauli repulsion. Connects to Jackiw-Rebbi
  fermionic statistics.
- **Milestone:** Measure F(d) and confirm exponential Yukawa form; verify that
  kink-kink scattering is always repulsive (no resonance windows unlike KA).

#### S5: Kink with Excited Shape Mode
- **Module:** `equations/kink_shape_mode_collision.py`
- **What to simulate:** Kink with internally excited PT shape mode (oscillating
  width) collides with an antikink.
- **What to measure:** How internal excitation shifts resonance windows;
  energy transfer between translational and internal modes; whether shape
  mode excitation enhances or suppresses annihilation.
- **Addresses:** The role of the PT shape mode in particle interactions;
  connects to one-loop corrections (the shape mode that corrects α_em and κ
  is the same mode being excited here).
- **Milestone:** Map resonance window shifts as function of shape mode amplitude;
  verify energy conservation between translational + internal + radiation channels.

#### S6: 2+1D Vortex Scattering and Meson Formation
- **Module:** `equations/vortex_scattering_meson.py`
- **What to simulate:** Two vortices (same or opposite winding) in 2+1D
  complex field. Evolve at various impact parameters and velocities.
- **What to measure:** Scattering cross-section vs energy; bound state (meson)
  formation threshold; meson spectrum from FFT of bound state oscillations.
- **Addresses:** Meson spectrum from V(φ) dynamics (currently from Regge
  formula, not simulation); QCD string tension emergence; the transition from
  perturbative to non-perturbative regimes.
- **Milestone:** Observe vortex-antivortex bound state; measure its frequency;
  compare to oscillon frequency from 1+1D and to DFC Regge predictions.

#### S7: Graviton Zero-Mode on Thick-Wall Background
- **Module:** `equations/graviton_lichnerowicz_thick_wall.py`
- **What to simulate:** Solve the graviton Lichnerowicz equation
  [-ψ'' + V_grav(y)ψ = 0] on the numerically-computed A(y) from
  the DFGH BVP.
- **What to measure:** Exact graviton zero-mode profile ψ₀(y);
  normalization integral ∫|ψ₀|²dy; effective exponent n in the
  approximation ψ₀ ≈ e^{(n/2)A}.
- **Addresses:** D4 gravity κ gap (+2.1%, T2a). C588 showed that n ≈ 2.06
  (instead of RS n = 2) closes the gap to +0.24%. This simulation would
  compute n exactly, potentially closing the gap to T1.
- **Milestone:** Compute exact ψ₀(y); extract n; compute κ_exact;
  determine if the remaining gap is <1% (T2a→near-T1).

### 2.3 EXPLORATORY — New Structural Demonstrations

#### S8: SU(2) Doublet from Coupled Kinks
- **Module:** `equations/su2_doublet_coupled_kinks.py`
- **What to simulate:** Two coupled real scalar fields in 2+1D, each with
  V(φ), coupled via a cross-term. Look for SU(2) doublet structure in
  the zero-mode spectrum.
- **What to measure:** Whether the coupled system produces a spin-1/2
  doublet in the zero-mode sector; the effective weak mixing angle from
  the coupling structure; mass splittings.
- **Addresses:** D6 SU(2) emergence (currently structural, T2a). Would
  be the first simulation showing non-abelian gauge structure from V(φ).
- **Milestone:** Demonstrate SU(2) transformation of zero modes under
  coupled field rotations; measure effective coupling.

#### S9: Confinement from Triple-Vortex (SU(3) Analogue)
- **Module:** `equations/triple_vortex_confinement.py`
- **What to simulate:** Three vortices in 2+1D with Z₃ coupling (third
  roots of unity). Measure the string tension between them; look for
  confinement (linear potential at large separation) vs screening.
- **What to measure:** Inter-vortex potential V(r); string tension;
  whether flux tubes form between vortices; whether the system confines.
- **Addresses:** D7 SU(3) confinement (T2a structural); QCD string
  tension σ = Q_top × Λ² (currently derived, not simulated); color
  confinement mechanism.
- **Milestone:** Observe flux tube formation; measure string tension;
  compare to DFC prediction σ = Q_top × Λ_QCD².

#### S10: Cosmological Expansion from Substrate Dynamics
- **Module:** `equations/cosmological_expansion_sim.py`
- **What to simulate:** Large-scale substrate with many kinks, evolving
  under slow compression relaxation. Look for Hubble-like expansion
  behavior in the inter-kink separations.
- **What to measure:** Scale factor a(t); Hubble parameter H(t);
  whether the expansion follows Friedmann-like equations; whether the
  DFC prediction H₀ = 67.26 km/s/Mpc emerges from the simulation.
- **Addresses:** Cosmological predictions (T2a); dark energy / Λ (T3);
  the fundamental question of how substrate compression maps to
  cosmological expansion.
- **Milestone:** Observe systematic increase in inter-kink spacing;
  extract H(t) and compare to Friedmann model.

#### S11: Bell Correlations from Substrate Connectivity
- **Module:** `equations/bell_correlation_substrate.py`
- **What to simulate:** Two entangled kinks (connected via substrate)
  measured at spatially separated points. Compute correlations as a
  function of measurement angle.
- **What to measure:** E(a,b) correlation function; Bell parameter S;
  whether S > 2 (violating classical bound); whether the correlations
  match the quantum prediction -cos(a-b).
- **Addresses:** Bell inequality violation from substrate (T2a, C482);
  emergent relativistic locality (T3); the measurement problem.
- **Milestone:** Demonstrate S > 2 from substrate dynamics alone;
  verify -cos(θ) correlation function; show no superluminal signaling.

---

## Phase 3: Integration and Cross-Validation

### 3.1 Simulation-to-Prediction Pipeline

After each simulation, extract quantitative data and feed back into the
prediction framework:

| Simulation | Data extracted | Feeds into |
|-----------|---------------|-----------|
| S1 (KZ) | Kink density exponent | Dark matter relic abundance |
| S2 (Cascade) | Bifurcation thresholds | Depth assignments α₅, α₆, α₇ |
| S3 (Y-junction) | Junction mode spectrum | Baryon Regge intercept, proton mass |
| S4 (KK repulsion) | F(d) functional form | Spin-statistics, Pauli principle |
| S5 (Shape mode) | Resonance window shifts | One-loop corrections to α_em, κ |
| S6 (Vortex meson) | Bound state spectrum | Meson masses, Regge slope |
| S7 (Graviton LW) | Exact κ | D4 gravity, Planck mass |
| S8 (SU(2)) | Doublet structure | Weak force emergence |
| S9 (SU(3)) | String tension | QCD confinement |
| S10 (Expansion) | H(t) | Cosmological predictions |
| S11 (Bell) | E(a,b) | Quantum foundations |

### 3.2 Dimensional Progression

The simulations form a natural dimensional hierarchy:

```
1+1D (real scalar):   S4, S5 ← extend kink physics
        ↓
2+1D (complex scalar): S3, S6 ← vortex/gauge physics
        ↓
2+1D (coupled/Z₃):    S8, S9 ← non-abelian structure
        ↓
3+1D (cosmological):   S1, S2, S10 ← large-scale dynamics
        ↓
Entanglement:          S11 ← quantum correlations
```

Each level builds on the previous: 1+1D kink physics is the foundation;
2+1D vortex physics adds gauge structure; coupled fields add non-abelian
structure; and the full system addresses cosmology and quantum foundations.

### 3.3 Prioritized Build Order

Based on impact × tractability:

| Order | Simulation | Why this order |
|-------|-----------|----------------|
| 1 | **S7** (Graviton Lichnerowicz) | Directly closes κ gap (+2.1% → <1%); computationally simple (1D eigenvalue problem) |
| 2 | **S1** (Kibble-Zurek) | Addresses DM relic T4; well-understood theory to compare against; extends substrate_simulation.py |
| 3 | **S4** (KK repulsion) | Simple extension of kink_antikink; demonstrates Pauli analogue; quick win |
| 4 | **S3** (Y-junction) | Directly addresses baryon physics; builds on vortex_antivortex |
| 5 | **S5** (Shape mode collision) | Extends KA annihilation; connects to one-loop physics |
| 6 | **S2** (Cascade) | Addresses depth assignments; computationally moderate |
| 7 | **S6** (Vortex meson) | Extends 2+1D; connects to hadron spectrum |
| 8 | **S9** (Triple vortex) | Non-abelian confinement; computationally challenging |
| 9 | **S8** (SU(2) doublet) | Requires careful multi-field setup |
| 10 | **S10** (Cosmological) | Large-scale; requires many kinks; computationally expensive |
| 11 | **S11** (Bell) | Most conceptually challenging; requires measurement model |

---

## Success Criteria

A simulation is **complete** when:
1. Module runs: `python3 equations/module.py` produces output
2. All key measurements have [PASS]/[FAIL] checks
3. Comparison to DFC analytical predictions is quantitative
4. Results are integrated into ROADMAP (completed list, spoke dashboard)
5. Educational document created or updated if warranted

A simulation **upgrades a prediction tier** when:
- It demonstrates a behavior that was previously only argued structurally (T3→T2a)
- It produces a quantitative result matching an analytical prediction (<5% → T2a)
- It resolves a T4 blocker by providing numerical evidence for a mechanism

---

## Summary Statistics

| Category | Count | Status |
|----------|-------|--------|
| Completed simulations | 11 | All PASS |
| Queued (ROADMAP P8) | 4 | Ready to implement |
| Planned (this roadmap) | 11 | Prioritized and specified |
| Total simulation program | 22 | |
| T4 items addressable by simulation | 3 | DM relic, threshold positions, κ gap |
| New structural demonstrations | 4 | SU(2), SU(3), cosmological expansion, Bell |
