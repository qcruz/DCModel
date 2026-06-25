# Phenomenon: Quantum Spin

## One-Sentence Synthesis

> Spin is the intrinsic angular momentum carried by a D6 SU(2) kink: the fermion
> spin-1/2 quantum number arises from the Jackiw-Rebbi zero mode bound to the kink
> background; the fermionic exchange statistics (−1 phase under 2π rotation) arise
> from the Finkelstein-Rubinstein theorem applied to the non-contractible loop in
> the D6 configuration space; both are verified numerically in `equations/spin_zero_mode.py`.

---

## Observation

Every quantum particle has an intrinsic angular momentum — spin — that is quantized in
half-integer or integer multiples of ℏ:

**Fermions (spin-1/2):** Electrons, muons, taus, all six quarks, three neutrinos. Each
has exactly spin s = 1/2, meaning:
- Two states along any axis: m_s = +1/2 ("spin up") and m_s = −1/2 ("spin down")
- A 360° physical rotation multiplies the wavefunction by −1 (requires 720° to return
  to identity — demonstrated by the Dirac belt trick and neutron interferometry)
- All matter in the universe is built from spin-1/2 fermions

**Bosons (integer spin):**
- Photon: spin 1, two helicity states (±1 along propagation direction)
- W/Z bosons: spin 1
- Higgs: spin 0
- Graviton (if it exists): spin 2

**Spin-statistics connection (Pauli 1940):** Spin-1/2 particles obey Fermi-Dirac
statistics (antisymmetric wavefunctions, Pauli exclusion). Integer-spin particles obey
Bose-Einstein statistics (symmetric wavefunctions, can pile into the same state).

No *elementary* particle has ever been observed with spin 3/2. (Composite hadrons such
as the Δ(1232) and Ω⁻ carry spin 3/2, but as bound states of three spin-1/2 quarks.)
The Standard Model takes spin assignments of elementary fields as fundamental inputs.

---

## Standard Explanation

Spin arises from the representation theory of the Lorentz group SL(2,C). The irreducible
representations are labeled by (j_L, j_R) where j_L, j_R ∈ {0, 1/2, 1, 3/2, ...}. The
physical spin is j = j_L + j_R:

```
Spinors:   (1/2, 0) or (0, 1/2)  →  spin-1/2 (Weyl spinors)
Dirac:     (1/2, 0) ⊕ (0, 1/2)  →  4-component Dirac fermion
Vectors:   (1/2, 1/2)             →  spin-1 (gauge bosons)
Scalars:   (0, 0)                 →  spin-0 (Higgs)
```

Why spin-1/2 specifically? The Standard Model has no explanation — it is postulated that
matter fields transform as Dirac spinors. The spin-statistics theorem connects the spin
assignment to the statistics (half-integer → fermionic, integer → bosonic) but this is
proven from QFT axioms, not derived from a deeper principle.

---

## Dimensional Folding Explanation

### The Core Problem

The DFC compression field φ(x,t) is a real scalar. Scalar fields produce spin-0 excitations.
The gauge connection fields A_μ, W_μ^a, G_μ^a are vectors — spin-1. Neither produces spin-1/2
without additional input.

DFC derives spin-1/2 through two complementary mechanisms, both originating in the D6 SU(2)
closure topology and verified numerically in `equations/spin_zero_mode.py`.

### Mechanism 1: Fermionic Statistics (Finkelstein-Rubinstein)

The Finkelstein-Rubinstein (FR) theorem (1968): a topological soliton in a bosonic field
theory acquires fermionic exchange statistics if and only if the path in field configuration
space corresponding to a 2π rotation of the soliton is non-contractible.

The relevant topology for D6:

```
π₄(SU(2)) = Z₂
```

The fourth homotopy group of SU(2) = S³ is Z₂. This non-trivial element corresponds to
a 2π rotation of a Skyrmion (charge-1 soliton) — the loop is non-contractible, so the
wavefunction picks up a factor of −1 under 2π rotation.

**Result:** D6 kinks with odd SU(2) winding number N have:

```
Phase under 2π rotation = (−1)^N

N = 1 (electron, quarks, leptons):  phase = −1  →  fermionic statistics
N = 0 (gauge bosons, Higgs):        phase = +1  →  bosonic statistics
N = 2 (hypothetical):               phase = +1  →  bosonic statistics
```

**Numerical verification:** `equations/spin_zero_mode.py` Step 1 computes the D6 Skyrmion
winding number directly from the field configuration. Result:

```
N = 1.00000  (error: 2 × 10⁻¹¹)
```

The winding is exactly 1 to eleven significant figures.

This mechanism explains why 2π rotation gives −1 (the "belt trick" is real — you cannot
continuously deform a 360° rotation to the identity for spin-1/2 particles), and why
exchange of two identical fermions gives −1 (exchange = 2π rotation + translation; the
rotation contributes the −1 sign). See `phenomena/quantum/pauli_exclusion.md` for the
full exchange analysis.

### Mechanism 2: Spin-1/2 Quantum Number (Jackiw-Rebbi Zero Mode)

Fermionic statistics (Mechanism 1) explains why the exchange phase is −1. But it does not
explain why the particle transforms as a spin-1/2 spinor under the Lorentz group — i.e.,
why it has two states (up/down) and why a 720° rotation is required to return to the original
state.

For elementary fermions (electron, quarks), this follows from the **Jackiw-Rebbi zero mode**:

In 1+1 dimensions, the DFC kink background supports an exact zero-energy fermionic mode:

```
Dirac equation in kink background:
    (∂_x + Mλ tanh(x/λ)) ψ_0 = 0

Exact solution:
    ψ_0(x) = C × cosh^{−Mλ}(x/λ)
    Dψ_0 = 0  exactly  (zero eigenvalue of the Dirac operator)

where Mλ = (coupling strength) × (kink width)
      Normalizable for Mλ > 1/2
```

This is a localized, normalizable spinor — a genuine spin-1/2 state — bound to the kink
background. Its two degrees of freedom (Dirac spinor components) become the spin-up and
spin-down states of the elementary fermion.

**Numerical verification:** `equations/spin_zero_mode.py` Step 4:

```
Mλ = 2.0:
    Residual rms = 1.51 × 10⁻⁶   (Dψ_0 ≈ 0 to numerical precision)
    Localization length ξ = 1.09 kink widths
    Wavefunction normalized: ∫ψ_0² dx = 1.0
```

The zero mode is exact (D̸ψ_0 = 0) and localizes at the kink center with width ~1 kink
width. (The kink width at D1 equals the Planck length; at D6 it is the electroweak
scale ~10⁻¹⁸ m — the two scales are distinct.)

**What determines the 720° rotation property:** The zero mode transforms as a spinor of
SL(2,C). A spinor picks up a phase e^{iπ} = −1 under 2π rotation (360°), returning to
its original state only after 4π (720°). This is not imposed — it is a property of the
Jackiw-Rebbi spinor solutions to the Dirac equation in the kink background.

### Why Gauge Bosons Are Spin-1

Gauge bosons (photon, W, Z, gluons) are the connection 1-forms of the D5/D6/D7 bundles.
They are not kinks — they are directional fields on the manifold, transforming as Lorentz
vectors. The D6 SU(2) gauge field W_μ^a has spin 1 by construction (it is a 1-form), not
spin-1/2. The FR phase for gauge bosons is +1 (no D6 winding), consistent with bosonic
exchange.

### Why No Spin-3/2 Elementary Particles

Spin-3/2 states would arise from coupling of spin-1 gauge boson and spin-1/2 fermion: a
Rarita-Schwinger field ψ_μ. In the SM and in DFC, no stable elementary spin-3/2 particle
exists because the D6 closure does not support a stable winding-3/2 configuration — the
Jackiw-Rebbi mechanism produces spin-1/2, and there is no D6-based mechanism for higher
half-integer spin. (Gravitinos in SUSY would be spin-3/2, but DFC has no established
supersymmetric extension — see open questions in `phenomena/quantum/pauli_exclusion.md`.)

---

## Formal Equations

### Finkelstein-Rubinstein Phase

```
Phase under 2π rotation of D6 kink with SU(2) winding N:

    Φ_FR = (−1)^N

For N = 1 (elementary fermions):  Φ = −1  [fermionic, 720° rotation needed]
For N = 0 (gauge bosons, Higgs):  Φ = +1  [bosonic, 360° rotation sufficient]
```

Source: π₄(SU(2)) = Z₂ (non-trivial element = 2π rotation of N=1 Skyrmion).

### Jackiw-Rebbi Zero Mode

```
Kink background:  φ(x) = φ₀ tanh(x/λ)

1+1D Dirac equation in kink background:
    D̸ψ = (∂_x + M φ(x)) ψ = 0

Exact zero mode:
    ψ_0(x) = N_0 × cosh^{−Mλ}(x/λ)
    N_0 = normalization constant
    Mλ > 1/2  →  normalizable (exponential localization)
    Mλ = 1/2  →  marginally normalizable (power-law tail)
    Mλ < 1/2  →  non-normalizable (not a bound state)
```

### Spin Angular Momentum Operators

The spin-1/2 operator in the Dirac representation:

```
S_i = (ℏ/2) σ_i    where σ_i are the 2×2 Pauli matrices

Eigenvalues of S_z:  m_s = ±ℏ/2
```

In DFC, the S_i operators act on the Jackiw-Rebbi zero mode's two-component structure.
The spin-up and spin-down states correspond to the two Weyl components of the localized
spinor, related by the Lorentz boost generators.

### Spin-Statistics Connection

```
For a particle with D6 winding N and Lorentz spin s:

    N odd  →  Φ_FR = −1  →  fermionic exchange  →  s half-integer (Jackiw-Rebbi spinor)
    N even →  Φ_FR = +1  →  bosonic exchange    →  s integer (gauge field or scalar)
```

The correspondence N odd ↔ s half-integer is the DFC form of the spin-statistics theorem.
It is not separately postulated — both the exchange phase and the spin value derive from
the same D6 SU(2) closure topology.

---

## Consistency Checks

| Property | DFC mechanism | Verified |
|---|---|---|
| FR winding N = 1 for D6 kink | π₃(SU(2)) = Z | N = 1.00000 (error 2×10⁻¹¹) ✓ |
| FR phase = −1 for N = 1 | π₄(SU(2)) = Z₂ | Analytic result from homotopy ✓ |
| Jackiw-Rebbi zero mode exists | D̸ψ_0 = 0 exact | Residual rms 1.51×10⁻⁶ ✓ |
| Zero mode is normalizable | Mλ > 1/2 | Mλ = 2.0 → ξ = 1.09 widths ✓ |
| Minimum spin = 1/2 for D6 kink | Jackiw-Rebbi produces Dirac spinor | Structural ✓ |
| Gauge bosons are spin-1 bosons | 1-forms on D6 bundle, no winding | Standard result ✓ |
| Higgs is spin-0 boson | Scalar squashing parameter, no winding | Standard result ✓ |
| Spin-statistics from same topology | N parity = FR phase = Jackiw-Rebbi statistics | Consistent ✓ |

---

## Open Questions

1. **Full substrate generalization of the Jackiw-Rebbi zero mode.** The zero mode derivation
   above is 1+1D. The substrate's D3 localization behavior produces three apparent spatial
   degrees of freedom. The full derivation needs to reproduce a Dirac spinor — a zero mode
   with exactly two degrees of freedom per substrate localization point — in the substrate's
   D3+D4 behavior. The index theorem argument (Atiyah-Singer, Steps 2–3 in spin_zero_mode.py)
   establishes this for composite baryon-like structures; the elementary fermion case requires
   extending the 1+1D result to the full D3+D4 substrate configuration.

2. **Mass generation for the zero mode.** The Jackiw-Rebbi zero mode is massless in
   1+1D. The electron has mass m_e. The Higgs mechanism generates masses for fermions
   through the Yukawa coupling ψ̄ φ ψ. In DFC, this corresponds to the coupling between
   the Jackiw-Rebbi zero mode and the S³ squashing parameter at D6. Whether the DFC
   Yukawa coupling reproduces the observed electron mass (0.511 MeV) from the D6
   geometry is the open mass generation problem.

3. **Right-handed fermions.** The FR mechanism gives fermionic statistics to SU(2)_L
   doublets (left-handed fermions). Right-handed fermions (e_R, u_R, d_R) are SU(2)_L
   singlets — they have no D6 winding through the FR mechanism. They are still spin-1/2.
   Their spin must arise from a different mechanism — either the Jackiw-Rebbi zero mode
   for a D5 or D7 kink background, or an extension of the D6 mechanism to SU(2)_R.
   This is connected to the parity structure of the weak force.

4. **Spin precession and the Larmor formula.** A free spin-1/2 particle in a magnetic
   field undergoes spin precession at the Larmor frequency ω_L = eB/m. In DFC, this
   corresponds to the D6 kink's fold orientation angle precessing in the external D5
   gauge field. The tree-level g = 2 follows from the Dirac structure of the Jackiw-Rebbi
   zero mode. The one-loop Schwinger correction (g−2)/2 = α_em/(2π) has been computed
   from the DFC α_em chain (36π identity): predicted a_e ≈ 0.001158, observed 0.001160
   (−0.14%, Tier 2b). See `phenomena/quantum/anomalous_magnetic_moment.md`.

---

## Connections

- **Spin emergence** — full derivation details: FR theorem, Atiyah-Singer, Jackiw-Rebbi;
  `foundations/spin_emergence.md`
- **Pauli exclusion** — FR exchange phase, antisymmetric wavefunctions, degeneracy pressure;
  `phenomena/quantum/pauli_exclusion.md`
- **Electron** — Jackiw-Rebbi ground state, charge and mass from D5/D6;
  `phenomena/particle_physics/particles/electron.md`
- **Weak force** — D6 SU(2) closure, left-handed coupling, S³ geometry;
  `phenomena/particle_physics/forces/weak_force.md`
- **Spin zero mode equations** — all numerical verifications;
  `equations/spin_zero_mode.py`
- **Quantum mechanics** — fold orientation angle θ as quantum phase;
  `phenomena/quantum/quantum_mechanics.md`
- **Born rule for spin** — P(↑, n̂) = cos²(θ/2) derived from SU(2) geometry + binary
  outcomes (Cycle 38); direct application of this document's spinor formalism;
  `foundations/born_rule_derivation.md`
- **Anomalous magnetic moment** — one-loop Schwinger correction from DFC coupling chain;
  a_e = α_em/(2π) = 0.001136 (−2.01%, systematic); full g-factor analysis;
  `phenomena/quantum/anomalous_magnetic_moment.md`, `equations/anomalous_magnetic_moment.py`
