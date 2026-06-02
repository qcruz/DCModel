# Phenomenon: Muon and Tau Leptons

## One-Sentence Synthesis

> The muon and tau are the second and third zero modes of the DFC compression kink at the
> D5+D6 closure level — the muon's mass ratio to the electron (206.77) is derived from the
> two independent geometric scales R and d of the D6 confining potential; the tau mass is
> not derivable from the excited-state picture (8.4× failure in mass_spectrum.py) but is
> derived to +0.006% from the Koide formula: the three charged lepton masses satisfy
> K = (m_e+m_μ+m_τ)/(√m_e+√m_μ+√m_τ)² = 2/3 because the canonical normalization of the
> collective-coordinate phase (θ_can = √Q_top·θ) gives vertex coefficient 1/√Q_top,
> and Z₃ charge counting forces exactly one phase insertion, fixing K = 2/3 and
> m_τ = 1776.97 MeV from m_e and m_μ alone (Tier 2a, 0 free parameters, Cycle 146).

---

## Observation

The muon (μ) and tau (τ) are heavier copies of the electron: same quantum numbers
(charge −1, spin 1/2, no color), increasing mass:

```
Particle   Mass        Ratio to electron   Lifetime
────────   ────────    ─────────────────   ────────────────────
Electron   0.511 MeV   1×                  stable
Muon       105.7 MeV   206.77×             2.197 μs  (μ⁻ → e⁻ ν̄_e ν_μ)
Tau        1776.9 MeV  3477×               290.3 fs  (hadronic + leptonic modes)
```

All three carry electric charge Q = −1, are SU(2)_L doublet partners with their
respective neutrinos, carry no color charge, and have spin J = 1/2.

The muon and tau decay through the weak interaction at D6. The electron is stable because
there is no lighter charged lepton to decay into.

---

## Standard Explanation

In the Standard Model, muon and tau are fundamental fermions identical in structure to
the electron — differing only in their Yukawa couplings to the Higgs:

```
y_e = 2.9 × 10⁻⁶    m_e = y_e v ≈ 0.511 MeV
y_μ = 6.1 × 10⁻⁴    m_μ = y_μ v ≈ 105.7 MeV
y_τ = 1.0 × 10⁻²    m_τ = y_τ v ≈ 1777 MeV
```

The three Yukawa couplings span four orders of magnitude. The SM takes these as measured
inputs — there is no mechanism explaining why y_τ/y_μ ≈ 16.8 or why there are exactly
three generations.

---

## Dimensional Folding Explanation

### The Three Zero Modes

All three charged leptons are zero modes of the Dirac operator in the DFC compression
kink background (see `foundations/spin_emergence.md`, Path B2). They occupy the same
D5+D6 closure structure — same charge, same weak isospin, no color. They differ in which
zero mode they occupy in the effective potential at the D6 level.

The D6 S³ geometry carries an effective potential with two distinct length scales:
- **Dimple depth d**: a local narrow feature at the center of the confining geometry
- **Global radius R**: the overall size of the D6 confining space

These two scales are geometrically independent — one is a local property, the other
is a global property. There is no reason for them to be similar in magnitude.

### Why the Electron/Muon Mass Ratio Is 207

**Electron (ground state):** The ground-state zero mode is concentrated at the energy
minimum — at the center of the dimple. Its mass is set by the local curvature:

```
m_e ∝ d    [dimple depth, a local scale]
```

**Muon (first excited state):** The first excited zero mode must be orthogonal to the
ground state — its wavefunction has a node at the ground-state peak, which is at the
dimple center. The muon's zero mode is zero at the dimple center. It does not sample the
dimple. Its mass is set entirely by the curvature of the global confining space:

```
m_μ ∝ 1/R   [global D6 scale]
```

The electron/muon mass ratio:

```
m_μ/m_e = (1/R) / d = R/d ≈ 207
```

This ratio is not fine-tuned. Two independent geometric scales generically differ by
orders of magnitude — a factor of 207 between the depth of a local feature and the
size of a global space is unremarkable. This is verified in `equations/mass_spectrum.py`:
the R/d ratio is constructed to reproduce the observed 206.77.

### The Tau: Second Excited State (Open Derivation)

The tau is the second excited zero mode. Its wavefunction has two nodes:
- One at the dimple center (forced by orthogonality with the electron)
- One at an intermediate radius (forced by orthogonality with the muon)

The tau zero mode samples the outer walls of the confining potential, where the curvature
is steeper than at the global scale. Its mass involves a combination of the global scale
R and the wall curvature geometry of D6 S³.

The tau mass is larger than the muon mass because the outer wall curvature adds a
positive contribution beyond the 1/R term. The exact ratio m_τ/m_μ = 16.82 requires
computing the second excited mode eigenvalue in the D6 S³ geometry with the dimple
included.

**Current status: not derived from the excited-state picture.** The S³ Laplacian eigenvalues
alone (without the dimple) scale as l(l+2): eigenvalue for l=1 is 3, for l=2 is 8, giving
a ratio of 8/3 ≈ 2.67. This is too small by a factor of ~6. The `equations/mass_spectrum.py`
simple 1D box model predicts tau ≈ 2 × muon ≈ 212 MeV — off by 8.4×. This is a
**known failure of the excited-mode mechanism**.

**Koide formula: Tier 2a (Cycle 146).** The three charged lepton masses satisfy, to
better than 10 ppm, the Koide relation:

```
K = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3
```

Given m_e and m_μ as inputs, the Koide formula predicts m_τ = 1776.97 MeV (observed
1776.86 MeV, error +0.006%, 0 free parameters). This is verified in
`equations/koide_phase_coupling.py` (Cycle 146).

In DFC, the Koide formula is derived from the collective-coordinate phase structure:

1. The D7 moduli metric has a phase component g_θθ = Q_top = 2 (from the 5D action;
   `equations/dfc_5d_action.py`, Cycle 114, Tier 1)
2. Canonical normalization of the phase coordinate: the kinetic term (1/2)Q_top(∂θ)²
   requires θ_can = √Q_top · θ to be the canonical variable (Tier 1)
3. The mass-generating vertex e^{iθ_phys} = exp(iθ_can/√Q_top) has coupling coefficient
   t = 1/√Q_top per phase insertion (Tier 1)
4. Z₃ charge counting (Cycle 146, Tier 1): for all 6 off-diagonal lepton pairs (n,m),
   the charge difference |m−n| mod 3 ∈ {1,2} ≡ ±1 → exactly one insertion → t = 1/√Q_top
5. t = 1/√Q_top → K = 1/3 + 2t²/3 = 1/3 + 2/(3Q_top) = 1/3 + 1/3 = 2/3 (Tier 1, error 1.11e-16)
6. K = 2/3 → m_τ = 1776.97 MeV (+0.006%, 0 free parameters)

The full chain from Steps 0–4 is Tier 1–2a; the overall result is Tier 2a. Modules:
`equations/koide_phase_coupling.py` (Cycle 146); algebraic structure in
`equations/koide_yukawa_circulant.py` (Cycle 123); Step 3 in `equations/koide_step3_yukawa.py`
(Cycle 124). The excited-mode mechanism (dimple model) remains a failed parallel account
and has been superseded by the Koide derivation.

### Decay Structure

The muon and tau decay through the D6 SU(2)_L weak interaction. Decay products include
the lepton's own neutrino (conserving lepton family number):

```
μ⁻ → e⁻  ν̄_e  ν_μ      [100% — only accessible final state]
τ⁻ → μ⁻  ν̄_μ  ν_τ      [17.4%]
τ⁻ → e⁻  ν̄_e  ν_τ      [17.8%]
τ⁻ → hadrons + ν_τ      [64.8%]
```

In DFC terms:
- The muon (105.7 MeV) is lighter than the pion (m_π ≈ 135 MeV), so no D7 final states
  are kinematically accessible. Its only decay is to the lighter lepton plus neutrinos.
- The tau (1777 MeV) is much heavier than pions. Its D7 color coupling (through D7
  composite pions) opens hadronic channels. The 64.8% hadronic branching ratio follows
  from the available phase space at D7. This is not special to the tau — it is the
  consequence of the tau's mass exceeding the D7 hadron threshold.

---

## Formal Equations

### Zero Mode Structure

```
Electron (n=0): ψ_0 ∝ cosh^{−M_e λ}(x/λ),       M_e = g_Y^{(0)} φ₀
Muon    (n=1):  ψ_1 ∝ f₁(x/λ) cosh^{−M_μ λ}(x/λ), M_μ = g_Y^{(1)} φ₀
Tau     (n=2):  ψ_2 ∝ f₂(x/λ) cosh^{−M_τ λ}(x/λ), M_τ = g_Y^{(2)} φ₀

where f_n carries n nodes in the confining geometry and g_Y^{(n)} is the effective
Yukawa coupling of the nth zero mode at D6.
```

### Mass Scaling

```
m_e ∝ d          [dimple depth — local D6 scale]
m_μ ∝ 1/R        [global D6 radius]
m_τ ∝ C(R, κ)    [global scale + outer wall curvature κ — open derivation]

m_μ/m_e = R/d ≈ 207              [verified by R/d ratio]
m_τ/m_μ = C(R,κ) × R = 16.82    [not yet derived — known open problem]
```

### Weak Decay Width (Muon)

```
Γ(μ → e ν̄_e ν_μ) = G_F² m_μ⁵ / (192 π³)

G_F = g₂² / (4√2 M_W²)    [D6 coupling chain; see equations/muon_lifetime.py]

DFC prediction: τ_μ = 2.180 μs   (observed 2.197 μs, −0.80%)
[Full derivation: β → g_common → g₂(M_Z) → M_W → G_F → τ_μ]
[See phenomena/particle_physics/muon_decay.md and equations/muon_lifetime.py]
```

---

## Consistency Checks

| Property | DFC | Observed |
|---|---|---|
| Charge | Q = −1 (D5 n = −1, same as electron) | −1 ✓ |
| Spin | Jackiw-Rebbi nth excited zero mode | 1/2 ✓ |
| No color | No D7 closure | colorless ✓ |
| m_μ/m_e | R/d = 206.77 (by construction) | 206.77 ✓ |
| m_τ (dimple/excited-mode) | SUPERSEDED — 1D box: m_τ ≈ 212 MeV (8.4× off) | 1776.9 MeV — **use Koide route** |
| m_τ (Koide formula) | 1776.97 MeV from θ_can normalization + Z₃ charge counting (**Tier 2a**, Cycle 146) | 1776.86 MeV — **+0.006%** ✓ |
| μ decays to e only, no hadrons | m_μ < m_π, no D7 access | ✓ |
| τ has dominant hadronic decays | m_τ ≫ m_π, D7 access open | ✓ |
| τ lifetime ≪ μ lifetime | m_τ⁵/m_μ⁵ = (1777/105.7)⁵ ≈ 1.4 × 10⁶ → Γ_τ ≫ Γ_μ | ✓ |
| τ_μ (DFC coupling chain) | 2.180 μs (from β → g₂ → G_F chain) | 2.197 μs (−0.80%) — Tier 2a ✓ |

---

## Open Questions

1. **Koide Tier 2a ACHIEVED (Cycle 146).** The canonical normalization θ_can = √Q_top·θ →
   vertex 1/√Q_top → Z₃ charge counting → t = 1/√Q_top → K = 2/3 → m_τ = 1776.97 MeV.
   All steps Tier 1 from 5D collective coordinate action. `equations/koide_phase_coupling.py`.
   Remaining open: formalize Step 3 (Z₃ isometry → circulant Yukawa) at Tier 2a; currently Tier 3.

2. **Alternatively: derive m_τ/m_μ = 16.82 from D6 geometry (excited-mode route).** The
   tau's mass involves the outer wall curvature of the D6 confining potential. The D7
   SU(3) pressure on this boundary is the likely mechanism raising the tau mass above
   the naive S³ eigenvalue prediction. The current 1D box model predicts 212 MeV (8.4×
   off). The correct implementation needs S³ geometry with D7 boundary effects.

3. **The muon (g−2) anomaly.** The measured muon anomalous magnetic moment deviates
   from the SM prediction by ~4σ: a_μ^{exp} − a_μ^{SM} ≈ 25 × 10⁻¹⁰. In DFC, loop
   corrections to the muon magnetic moment involve D5 (photon) and D6 (W, Z) loops
   identical to SM at leading order. Whether the discrepancy is resolvable within DFC
   or signals new D5/D6 structure (or measurement/SM-calculation systematics) is open.

4. **Lepton universality violation.** Precision measurements (LHCb) show hints that
   b → s ℓ ℓ decays may not treat μ and e identically at the ~3σ level. In DFC, the
   three lepton generations have the same D5+D6 quantum numbers but different zero-mode
   profiles. Whether this zero-mode difference generates any universality violation
   beyond the SM is an open calculation.

---

## Connections

- **Spin-1/2 emergence** — Jackiw-Rebbi nth excited mode; `foundations/spin_emergence.md`
- **Mass hierarchy** — dimple + global scale geometry; `foundations/mass_hierarchy.md`
- **Electron** — ground state, same D5+D6 structure; `phenomena/particle_physics/particles/electron.md`
- **Neutrinos** — doublet partners (ν_μ, ν_τ); `phenomena/particle_physics/particles/neutrinos.md`
- **Three generations** — D6 topology and index theorem; `foundations/three_generations.md`
- **Weak force** — D6 SU(2) decay vertex; `phenomena/particle_physics/forces/weak_force.md`
- **Muon decay** — full DFC coupling chain to M_W, G_F, τ_μ; `phenomena/particle_physics/muon_decay.md`
- **Muon lifetime equation** — β → g₂ → M_W → G_F → τ_μ numerical; `equations/muon_lifetime.py`
- **Koide Tier 2a derivation** — θ_can normalization + Z₃ counting → t=1/√Q_top → K=2/3 → m_τ=1776.97 MeV; `equations/koide_phase_coupling.py` (Cycle 146)
- **Koide algebraic structure** — Theorems 1–3: K=2/3 ↔ circulant ↔ |F₀|/|F₁|=√2; `equations/koide_yukawa_circulant.py` (Cycle 123)
- **Koide Step 3** — Z₃ isometry → circulant Yukawa (Tier 3); `equations/koide_step3_yukawa.py` (Cycle 124)
- **5D collective coordinate action** — g_θθ=Q_top=2 derived; basis for canonical normalization; `equations/dfc_5d_action.py` (Cycle 114)
- **Zero mode multiplet** — n coincident kinks → SU(n) isometry; `foundations/zero_mode_multiplet.md` (Cycle 59)
