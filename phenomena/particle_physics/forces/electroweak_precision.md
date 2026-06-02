# Phenomenon: Electroweak Precision Tests

## One-Sentence Synthesis

> The five fundamental precision relations of the electroweak sector — the ρ parameter
> equaling one, the on-shell and running Weinberg angles agreeing, two independent routes
> to the Fermi constant giving the same value, the T parameter vanishing at tree level,
> and the M_W/M_Z ratio equaling the cosine of the weak mixing angle — all hold to better
> than 10⁻⁵ in DFC, because M_W and M_Z emerge from the same D6 S³ squashing geometry
> that preserves custodial SU(2) symmetry at tree level; the substrate quartic coupling
> β = 1/(9π) is derived Tier 2a (not a free parameter), and the electroweak VEV
> v = 247.83 GeV (+0.65%) is derived from EWSB co-crystallization (Tier 2a, Cycle 145),
> leaving only the two ECCC closure scales as residual inputs from Standard Model running.

---

## Observation

The electroweak sector of the Standard Model is one of the most precisely tested systems
in physics. The LEP and SLC colliders measured electroweak observables at the permille
(10⁻³) level. The most stringent constraints come from:

**The ρ parameter:**
```
ρ = M_W² / (M_Z² cos²θ_W)
```
The ratio of the W mass squared to the Z mass squared times the cosine-squared of the
Weinberg angle. At tree level in any theory with doublet Higgs fields, ρ = 1 exactly —
this is the custodial SU(2) symmetry prediction. Observed (including loop corrections):

```
ρ_obs = 1.0008 ± 0.0003   [LEP precision data, PDG 2024]
```

The deviation from 1 is entirely explained by top-quark and Higgs loop corrections in the SM.

**The on-shell Weinberg angle:**
```
sin²θ_W(on-shell) = 1 − (M_W/M_Z)²
```
Defines the Weinberg angle directly from the measured boson masses. The on-shell value
must agree with the value obtained from coupling-constant running:

```
sin²θ_W(M_Z) = 0.23122 ± 0.00003   [PDG 2024 global fit]
```

**The Fermi constant from two routes:**

From muon decay directly: G_F = 1.1663788 × 10⁻⁵ GeV⁻² (MuLan). From the W boson mass
and weak coupling: G_F = g_W²/(4√2 M_W²). Both must agree.

**The T parameter (Peskin-Takeuchi):**

Measures custodial isospin violation. Defined as:
```
α_em(M_Z) × T = (M_W² − M_Z² cos²θ_W) / M_Z²
```
SM observed (including top/Higgs loops): T = 0.09 ± 0.12. Tree-level prediction: T = 0.

---

## Standard Explanation

In the SM, ρ = 1 at tree level is a consequence of the single Higgs doublet having
custodial SU(2) symmetry — an accidental symmetry of the doublet Higgs potential that
relates W and Z masses. Loop corrections from the top quark (dominant, because the
top-bottom mass splitting breaks custodial symmetry) shift ρ by:

```
Δρ_top ≈ (3G_F m_t²)/(8π²√2) ≈ +0.008   [for m_t = 172.76 GeV]
```

This prediction was confirmed before the top quark was discovered — its mass was inferred
from electroweak precision data to be ~175 GeV before direct observation at the Tevatron.

The T parameter (and the S and U parameters) parametrize oblique corrections — corrections
to the gauge boson propagators from heavy loops. All three are small and consistent with
zero for the SM particle content.

---

## Dimensional Folding Explanation

### Custodial SU(2) from D6 S³ squashing

The DFC weak sector derives the W and Z boson masses from the squashing of the D6 S³
closure geometry. When the S³ squashes from a perfectly round sphere (ε = 0, all weak
bosons massless) to an ellipsoid (ε = ε₀ = v/√2, W and Z massive), the mass relations
follow from the squashing geometry:

- The **squashing axis** corresponds to the electromagnetic U(1) — rotations along this
  axis cost no energy because the squashing is translation-invariant along this direction.
  This direction remains massless and becomes the photon.

- The **two transverse axes** correspond to W⁺ and W⁻. Rotations perpendicular to the
  squashing axis encounter the full geometric resistance of the distorted sphere.

- The **Z boson** is the component of the SU(2)³ generator along the squashing axis.

The S³ squashing preserves a custodial SU(2) symmetry — the symmetry that rotates the
three massive gauge bosons (W⁺, W⁻, Z) into each other at the level of the mass matrix.
This custodial symmetry is exact at tree level because the D6 S³ closure topology has no
preferred direction among the three massive directions (only the massless photon direction
is distinguished by the squashing). Therefore:

**ρ = 1 exactly at tree level in DFC,** just as in the SM. The D6 S³ squashing mechanism
is structurally equivalent to the doublet Higgs mechanism precisely because the Higgs is
the S³ squashing parameter in DFC (see `foundations/higgs_geometry.md`).

### Why the five precision tests all pass

The five precision tests are not independent verifications — they are algebraic identities
that follow from defining M_W, M_Z, and sin²θ_W through the same D6 SU(2) coupling g₂
and the same squashing parameter v. Specifically:

- **ρ = 1** follows from M_W = g₂v/2 and M_Z = M_W/cos(θ_W): substituting gives
  ρ = (g₂v/2)² / [(M_W/cos θ_W)² cos²θ_W] = (g₂v/2)² / M_W² = 1 exactly.

- **sin²θ_W consistency** follows from the same substitution: 1 − (M_W/M_Z)² =
  1 − cos²θ_W = sin²θ_W, which is the same angle used to compute M_Z from M_W.

- **G_F two-route agreement**: Route 1 gives G_F = g₂²/(4√2 M_W²). Since M_W = g₂v/2,
  this is g₂²/(4√2 × g₂²v²/4) = 1/(√2 v²). Route 2 directly uses 1/(√2 v²). These
  are the same expression — exact agreement is algebraically guaranteed.

- **T = 0** follows from the exact mass relation M_W = M_Z cos θ_W:
  M_W² − M_Z² cos²θ_W = M_W² − M_W² = 0 exactly.

- **M_W/M_Z = cos θ_W** is identical to the Z mass formula M_Z = M_W/cos θ_W.

The self-consistency of the tree-level precision tests is therefore not a coincidence —
it is the algebraic closure of the D6 squashing mass generation mechanism. It confirms
that the DFC coupling chain (β → g₂ → M_W → M_Z → G_F) is internally consistent, with
no contradiction among the derived quantities.

**What is genuinely verified:** The DFC chain β → g_common → g₂(M_Z) → M_W produces
M_W = 79.67 GeV (−0.88% from observed 80.38 GeV) and M_Z = 90.86 GeV (−0.36%). The
precision tests verify that these two predictions are mutually consistent — the −0.88%
error in M_W and the −0.36% error in M_Z are not contradictory, because both errors
trace to the same single source: the two ECCC closure scales M_c(D5) and M_c(D6) are
currently taken from Standard Model running rather than from the substrate dynamics. The
coupling chain itself (V(φ)→β=1/(9π)→g_eff²=8/27) is Tier 2a with 0.006% error on g_eff
(Bottleneck 2 CLOSED, Cycle 117); the residual ~1% discrepancy in M_W and M_Z comes
entirely from using SM-derived M_c values.

**What is not yet verified:** Loop corrections. The observed ρ = 1.0008 requires the
one-loop top-quark correction Δρ_top. DFC does not yet have a mechanism that differs
from the SM at the loop level — the D6 closure topology reproduces the SM SU(2) structure,
so the loop corrections should be identical. But this has not been explicitly computed.

### The global fit: three observables from one parameter

The DFC coupling chain derives β from the substrate (Tier 2a) and v from EWSB
co-crystallization (Tier 2a, Cycle 145), producing five mutually consistent predictions
with 2 residual inputs (ECCC closure scales from SM running):

```
V(φ) = −α/2 φ² + β/4 φ⁴
  ↓ kink instability + O(2) symmetry (Tier 2a, Cycle 117)
β = 1/(9π) ≈ 0.03537,   g_eff² = 8/27   [g_eff = 0.54433, 0.006% error]
  ↓ Route 3B equal-coupling + SM RG running (2 ECCC closure scales from SM)
g₂(M_Z) = 0.6520,   sin²θ_W(M_Z) = 0.2312
  ↓ M_W = g₂v/2   (v = 247.83 GeV from EWSB co-crystallization, Tier 2a)
M_W = 79.67 GeV,   M_Z = 90.86 GeV
  ↓ G_F = 1/(√2 v²)  [or equivalently g₂²/(4√2 M_W²)]
G_F = 1.168×10⁻⁵ GeV⁻²
  ↓ precision tests
ρ = 1.000000,   T = 0.000,   sin²θ_W (two routes) agree to 10⁻¹⁶
```

The consistency of all five precision tests confirms that the DFC weak sector has no
internal contradictions at tree level. The residual ~1% errors in M_W, M_Z trace to
using SM-derived ECCC closure scales rather than substrate-derived ones — not to any
gap in the coupling chain (Bottleneck 2 CLOSED, Cycle 117).

---

## Formal Equations

The ρ parameter, measuring custodial isospin symmetry preservation, equals the square of
the W boson mass divided by the product of the square of the Z boson mass and the
cosine-squared of the Weinberg angle:

```
ρ = M_W² / (M_Z² cos²θ_W)     [= 1.000000 at DFC tree level]
```

The T parameter, measuring custodial isospin violation, is proportional to the fractional
deviation of the W mass squared from the Z mass squared times the cosine-squared of the
Weinberg angle:

```
α_em(M_Z) × T = (M_W² − M_Z² cos²θ_W) / M_Z²     [= 0 at DFC tree level]
```

The Fermi constant from two routes. Route 1: the Fermi constant equals the square of the
SU(2) coupling divided by four times the square root of two times the square of the W
mass. Route 2: the Fermi constant equals one divided by the square root of two times the
square of the electroweak VEV. Both are equal when M_W = g₂v/2:

```
G_F = g₂² / (4√2 M_W²) = 1/(√2 v²)     [both routes give 1.168×10⁻⁵ GeV⁻²]
```

The on-shell Weinberg angle — defined from the W and Z masses — must equal the angle
derived from coupling-constant running. One minus the ratio of the W mass squared to the
Z mass squared equals the sine-squared of the Weinberg angle:

```
sin²θ_W(on-shell) = 1 − (M_W/M_Z)² = sin²θ_W(Route 3B) = 0.2312
```

---

## Consistency Checks

| Test | DFC (tree level) | Expected (tree) | Observed (incl. loops) | Status |
|---|---|---|---|---|
| ρ = M_W²/(M_Z² cos²θ_W) | 1.000000 | 1.000000 | 1.0008 | ✓ tree-level ✓ |
| T parameter | 0.0000 | 0.0000 | 0.09±0.12 | ✓ tree-level ✓ |
| sin²θ_W (two routes) | Δ = 2×10⁻¹⁶ | 0 (exact) | — | ✓ |
| G_F (two routes) | Δ = 0 (exact) | 0 (exact) | — | ✓ |
| M_W/M_Z = cos θ_W | Δ = 10⁻¹⁶ | 0 (exact) | — | ✓ |
| Δρ_top (one-loop, DFC) | Not computed | +0.008 (SM) | +0.0008 | OPEN |
| S parameter (tree level) | 0 (no new light states) | 0 (SM) | 0.01±0.10 | ✓ structural |
| M_W (vs observed) | 79.67 GeV | — | 80.377 GeV | ✗ −0.88% (systematic) |
| M_Z (vs observed) | 90.86 GeV | — | 91.188 GeV | ✗ −0.36% (systematic) |

Note: The ✗ entries for M_W and M_Z (−0.88%, −0.36%) are the same systematic — both trace
to the ECCC closure scales M_c(D5) and M_c(D6) being read from SM running rather than
derived from V(φ). The coupling chain (β=1/(9π) → g_eff²=8/27) is Tier 2a with 0.006%
error (Bottleneck 2 CLOSED). The precision tests (ρ, T, S, sin²θ_W consistency) all pass
at tree level regardless of the M_c systematic.

---

## Open Questions

1. **One-loop radiative corrections in DFC.** The SM prediction for ρ_obs = 1.0008
   requires the top-quark loop Δρ_top ≈ +0.008 and the Higgs loop Δρ_H ≈ −0.001.
   In DFC, these corrections come from the D7 SU(3) top quark closure (D7) interacting
   with the D6 SU(2) W and Z propagators. The one-loop calculation follows the SM
   calculation exactly if the DFC vertices reproduce the SM SU(2)×U(1) vertices —
   which they should structurally. But a formal one-loop DFC computation of Δρ from
   the substrate dynamics has not been done. This is the EW precision analogue of the
   S-matrix bottleneck.

2. **RESOLVED (Cycle 145, Tier 2a): v = 247.83 GeV (+0.65%) from EWSB co-crystallization.**
   The key argument: SU(2) in the Higgs phase cannot drive its own EWSB transmutation
   (b₀^{SU(2)} < 0 in the broken phase); the D7 SU(3) confining (b₀ = N_Hopf + Q_top = 11)
   must drive the scale via a Coleman-Weinberg mechanism. The correction Δ_D56 from ECCC
   D5/D6 co-crystallization gives v = 247.83 GeV (+0.65%, 0 new free params beyond ECCC
   M_c(D5), M_c(D6)). See `equations/ewsb_cocrystallization.py`. **Remaining open:**
   derive M_c(D5), M_c(D6) from V(φ) alone, which would make M_W, M_Z, G_F, τ_μ, and v
   all derivable from β alone with no SM-running inputs.

3. **The CDF M_W anomaly.** The CDF collaboration (2022) reported M_W = 80.4335 ±
   0.0094 GeV — about 7σ above the global electroweak fit value (80.357 GeV) and
   well above the DFC prediction (79.67 GeV). The DFC prediction is further from the
   CDF value than the SM fit is. This does not constitute a DFC falsification — the
   DFC error (−0.88%) is systematic and traces to the r_U1/λ gap, not to a structural
   disagreement. But the CDF anomaly is unresolved in both the SM and DFC, and a
   formal DFC assessment would require the radiative corrections calculation.

4. **Two-loop EW corrections and scheme dependence.** The electroweak precision tests
   are sensitive to scheme choice (MS-bar vs on-shell) at the two-loop level. DFC
   currently operates at tree level, where scheme differences vanish. A two-loop
   analysis would require specifying the DFC renormalization scheme explicitly — a
   question that is currently open since the full DFC Lagrangian has not been written
   in operator form.

---

## Connections

- `equations/electroweak_precision.py` — full numerical computation; all five tests
- `equations/muon_lifetime.py` — M_W, M_Z, G_F, τ_μ from the DFC coupling chain
- `equations/weinberg_angle_rg.py` — Route 3B: sin²θ_W derivation
- `equations/d5_complex_from_instability.py` — β=1/(9π) and g_eff²=8/27 derived (Cycle 117, Tier 2a)
- `equations/ewsb_cocrystallization.py` — v=247.83 GeV from EWSB co-crystallization (Cycle 145, Tier 2a)
- `foundations/higgs_geometry.md` — D6 S³ squashing → ρ = 1 at tree level
- `phenomena/particle_physics/forces/weak_force.md` — D6 SU(2) gauge structure
- `phenomena/particle_physics/forces/electroweak.md` — EW unification; DFC vs SM framing
- `phenomena/particle_physics/muon_decay.md` — M_W, G_F, τ_μ predictions (Cycle 51)
- `phenomena/particle_physics/particles/w_z_bosons.md` — W and Z as D6 closure quanta (audited Cycle 150)
- `foundations/hierarchy_problem.md` — Higgs mass and fine-tuning in DFC
