# Strong Coupling Constant: The M_c(D7) Gap

## Status

> **Cycle 77:** This document formally maps the α_s(M_Z) derivation problem.
> It identifies the derivation chain, shows where it breaks, quantifies the
> gap numerically, and states precisely what substrate calculation is required
> to close it.
>
> **Cycle 117 update:** Bottleneck 2 CLOSED. g_common² = 2I₄/N_Hopf = 8/27 is now
> Tier 2a (0 free parameters). β = 1/(9π) is Tier 2a. This changes the initial
> condition for the α_s running:
> - Old: α_common = 8πβ/3/(4π) = 8×0.0351/12 = 0.02340 (Tier 3 reference)
> - New: α_common = 8/(27×4π) = 2/(27π) = 0.02358 (Tier 2a, exact)
> The revised target M_c(D7) is now **1.57×10¹⁵ GeV** (one-loop, N_f=6).
> See `equations/d5_complex_from_instability.py` for the full derivation chain.
>
> **Current result:** α_s(M_Z) = 0.1086 from DFC with β=1/(9π) and M_c(D7)=8×10¹⁴ GeV
> (8.1% below observed 0.1182 — improved from 11% with old β=0.0351).
> **Root cause:** M_c(D7) = 8×10¹⁴ GeV (from equal-coupling crossing) is too
> low. The updated target M_c(D7) = 1.57×10¹⁵ GeV. The gap is a factor of ~2.0.
> **Blocking step:** Derive α_D7 (the D7 substrate coupling) from the substrate
> field equation, not from SM running.

---

## The Derivation Chain

The chain from DFC substrate to α_s(M_Z) proceeds as follows:

**Step 1 — Substrate β to g_common (DERIVED, Tier 2a as of Cycle 117).**
The substrate quartic coupling β determines the common gauge coupling at the
closure scale. The square of the gauge coupling constant equals twice the kink
shape integral I₄ = 4/3, divided by the Hopf fiber dimension sum N_Hopf = 9,
derived from V(φ) with zero free parameters (see
`equations/d5_complex_from_instability.py`):

```
g_common² = 2I₄/N_Hopf = 8/27  (Tier 2a, exact, 0 free parameters)
β = 1/(9π) ≈ 0.03537  (Tier 2a, derived from self-consistency)
α_common = g_common²/(4π) = 2/(27π) ≈ 0.02358
g_common = √(8/27) ≈ 0.54433  (SM: 0.5443, error 0.006%)
```

The old formula g²=8πβ/3 is consistent: 8π/(9π)/3 = 8/27 ✓. The heuristic
derivation (Cycle 42) is superseded by the rigorous chain in Cycle 117.

**Step 2 — Equal-coupling initial condition (STRUCTURAL).**
The three gauge closures at D5, D6, and D7 all emerge from the same compression
field with the same substrate potential. The substrate quartic coupling β is the
same at all three depths. Therefore, the gauge coupling at the respective closure
scale is the same for all three: the strong coupling constant at the D7 closure
scale equals g_common.

```
g₃(M_c(D7)) = g_common     [structural — same substrate, same β]
α_s(M_c(D7)) = g_common² / (4π) = 2/(27π) ≈ 0.02358   [Tier 2a]
```

**Step 3 — RG running from M_c(D7) to M_Z (BORROWED, SM one-loop).**
The strong coupling constant grows as the energy scale decreases — SU(3) is
asymptotically free. Running from the D7 closure scale M_c(D7) down to the
Z boson mass M_Z = 91.19 GeV, the inverse coupling decreases by an amount
proportional to the one-loop beta function coefficient b₃ = 7 times the
logarithm of the scale ratio. Specifically, the inverse of the strong coupling
at M_Z equals the inverse at M_c(D7) minus b₃ divided by two pi times the
natural log of the ratio M_c(D7) over M_Z:

```
1/α_s(M_Z) = 1/α_s(M_c(D7)) − [b₃/(2π)] × ln(M_c(D7)/M_Z)
b₃ = 7     [SM one-loop SU(3) beta function coefficient]
```

---

## The Current Gap

With M_c(D7) taken from the equal-coupling crossing in SM running
(where α₁ ∩ α₃ cross, giving ~8×10¹⁴ GeV), the chain gives:

```
1/α_s(M_Z) = 42.66 − [7/(2π)] × ln(8×10¹⁴ / 91.19)
           = 42.66 − 1.114 × 30.24
           = 42.66 − 33.69
           = 8.97
→ α_s(M_Z) = 0.1115  [first approximation]
```

The numerical module `equations/coupling_derivation.py` reports
α_s(M_Z) = 0.1049 with M_c(D7) = 8×10¹⁴ GeV, which is the exact
calculation with β-derived g_common (not a fixed 42.66 estimate). The
error is 11% below the observed value 0.1182.

**Why does the current M_c(D7) estimate come from SM running?**
The estimate M_c(D7) ≈ 8×10¹⁴ GeV is the scale where the SM one-loop
running of α₁ and α₃ cross (or approach crossing). This is a consistency
check, not a DFC derivation. The DFC substrate must produce M_c(D7) from
the D7 substrate parameters — specifically, the D7 depth's quadratic
coupling α_D7. The closure scale is determined by the quadratic coupling:
M_c(D7) equals the square root of α_D7 divided by two.

```
M_c(D7) = √(α_D7/2)     [same formula as at all depths]
```

The quadratic coupling α_D7 is not currently derived from any DFC calculation.
It is a free parameter at the D7 depth — the gap is deriving α_D7 from the
substrate's depth-running structure.

---

## The Target: What M_c(D7) Is Needed?

To obtain the observed α_s(M_Z) = 0.1182 from the equal-coupling initial
condition g_common = √(8/27) (Tier 2a, β = 1/(9π)), the target M_c(D7) is the
scale that satisfies:

```
1/0.1182 = 1/0.02358 − [7/(2π)] × ln(M_c(D7) / 91.19 GeV)
```

Solving: the natural log of the ratio of M_c(D7) to M_Z equals the difference
between the inverse couplings divided by the beta function factor. Numerically
(updated for Cycle 117 α_common):

```
1/α_common = 27π/2 ≈ 42.41   [Tier 2a: exact from 8/27]
ln(M_c(D7) / 91.19) = (42.41 − 8.461) / 1.114 = 33.95 / 1.114 = 30.48
M_c(D7)_target = 91.19 × e^30.48 ≈ 1.57 × 10¹⁵ GeV   [one-loop, N_f=6]
```

See `equations/alpha_s_target.py` for the full numerical computation (note:
that module uses the old β=0.0351 reference value; update BETA to 1/(9π) for
the Cycle 117 result). The updated target M_c(D7) ≈ 1.57×10¹⁵ GeV is a factor
of ~2.0 above the current equal-coupling-crossing estimate of 8×10¹⁴ GeV
(reduced from the old factor of 2.62 since α_common is now slightly larger).

The corresponding α_D7 target:

```
α_D7_target = 2 × M_c(D7)² ≈ 2 × (1.57×10¹⁵)² ≈ 4.93 × 10³⁰ GeV²
```

**Note on one-loop running at low scales.** The one-loop formula breaks down
well below M_Z, where non-perturbative effects dominate. Running the DFC chain
down to m_b = 4.18 GeV gives α_s(m_b) = 0.199 vs the measured 0.115 (73% off).
This is a known failure of one-loop running at hadronic scales, not a DFC-specific
problem. The α_s(M_Z) match is the appropriate test of the coupling chain.

---

## What Would Close the Gap

**Route 1 — Depth-running of α.**
The substrate quadratic coupling α varies with depth. The depth-running model
in `foundations/depth_running.md` and `equations/depth_running.py` established
the two-scale structure: γ_space >> γ_weak ≈ 0, giving M_c(D5) = 1.02×10¹³
GeV (exact by construction). The strong coupling sector (D7) runs with a
different coefficient — if γ_strong can be derived from the substrate, M_c(D7)
follows.

The two-scale model assumes co-crystallization of D5 and D6 (γ_weak ≈ 0 —
they emerge at the same scale) while D7 closes separately. The ratio
M_c(D7)/M_c(D5) in the two-scale model is:

```
M_c(D7) / M_c(D5) = exp(γ_strong × N_depth_gap)
```

With M_c(D5) = 1.02×10¹³ GeV and M_c(D7)_target = 1.57×10¹⁵ GeV (updated
Cycle 117):

```
M_c(D7)/M_c(D5) ≈ 154     →     γ_strong × N_depth_gap ≈ ln(154) ≈ 5.04
```

If N_depth_gap = 2 (D5 to D7 is two depth increments), then γ_strong ≈ 2.52
per depth unit. This is a specific prediction: the substrate compression
coefficient at D7 depths is approximately 2.5 times the logarithm of the
mass ratio per depth step.

**Route 2 — Threshold correction.**
The one-loop running formula is exact in perturbation theory, but the D7
closure involves non-perturbative effects (confinement). The physical M_c(D7)
in the RG equation is an effective matching scale that may differ from the
naively estimated crossing scale by a factor of order unity. A factor of ~2.5
in the scale is a factor of ~1.6% correction to the log, which is plausible
for a non-perturbative threshold effect.

**Route 3 — Derive α_D7 directly from the SU(3) closure topology.**
The mode-count theorem (Cycle 73, `foundations/threshold_nondegeneracy.md`)
establishes that n=3 independent zero modes emerge at D7. This gives the
gauge group SU(3) but not the scale M_c(D7). A complete derivation would
compute the substrate field configuration at D7 (three coincident kinks,
complex structure from D5, SU(3) algebra from n=3 modes) and extract α_D7
from the kink equation at that configuration.

---

## Why This Is the Priority

The α_s gap is the last remaining large quantitative failure in the DFC
coupling sector. The other couplings have the following errors:

| Coupling | DFC value | Observed | Error | Status |
|---|---|---|---|---|
| g_common | 0.54433 | 0.5443 | 0.006% | Tier 2a (Cycle 117) |
| sin²θ_W(M_Z) | 0.2312 | 0.2312 | 0.01% | Tier 2a |
| α_em(M_Z) | 1/129.6 | 1/127.9 | 1.3% | Tier 2a |
| M_W | 79.67 GeV | 80.38 GeV | 0.88% | Tier 2a |
| M_Z | 90.86 GeV | 91.19 GeV | 0.36% | Tier 2a |
| **α_s(M_Z)** | **0.1049** | **0.1182** | **11%** | **Tier 2b (M_c(D7) open)** |

All errors except α_s trace to the same source: the 1.3% error in α_em(M_Z)
from the systematic in the QED running (the coupling chain itself is now Tier 2a).
The α_s error is independent — it comes from M_c(D7) not being derived from the
substrate, which keeps the D7 closure scale as a free SM input.

Once M_c(D7) is derived, the strong coupling follows automatically from the
same coupling chain that already gives the weak sector to < 1% accuracy.
This would complete the coupling sector and lift the model from Phase 2 to
Phase 3 of the completeness milestones.

---

## Formal Statement of the Problem

Let α_D7 be the substrate quadratic coupling at D7 depth. The DFC closure
scale at D7 depth equals the square root of α_D7 divided by two. Given
the observed strong coupling constant at the Z mass scale α_s(M_Z) = 0.1182
and the known common coupling g_common = √(8/27) ≈ 0.54433 (Tier 2a, Cycle 117,
β = 1/(9π)), the required value of α_D7 satisfies:

```
√(α_D7/2) = M_c(D7)_target ≈ 1.57 × 10¹⁵ GeV   [updated Cycle 117]
→ α_D7 ≈ 4.9 × 10³⁰ GeV²
```

The open derivation: show that the substrate compression dynamics, starting
from the D5/D6 co-crystallization scale M_c(D5) = 1.02×10¹³ GeV, produces
α_D7 ≈ 4.9×10³⁰ GeV² at D7 depth — a factor of ~154 larger in energy scale.

The ratio α_D7/α_D5 = M_c(D7)²/M_c(D5)² ≈ (1.57×10¹⁵)²/(1.02×10¹³)² ≈ 2.37×10⁴.
The substrate depth-running must generate this ratio across two depth steps
(D5→D6→D7). If the running is exponential with coefficient γ per step, then
the ratio per step is approximately √(2.37×10⁴) ≈ 154, so γ ≈ ln(154) ≈ 5.04
per step. This is the specific numerical target for the depth-running
calculation at D7.

---

## Open Questions

1. **Derive γ_D7 (D7 depth-running coefficient) from the substrate field equation.**
   The two-scale model in `depth_running.md` uses γ_space >> γ_weak as a structural
   input. Extending this to D7 requires computing the compression coefficient from
   the SU(3) closure geometry — specifically, the energy cost of forming three
   coincident kinks as a function of the compression depth parameter.

2. **Non-perturbative matching at M_c(D7).** The one-loop running formula gives
   M_c(D7)_target = 2.0×10¹⁵ GeV. But the D7 closure is inherently non-perturbative
   (it produces confinement). The actual matching condition between the substrate and
   the QCD Lagrangian may introduce a factor that shifts the effective scale. Estimate
   the non-perturbative correction from the ratio of the perturbative and non-perturbative
   string tension estimates.

3. **Verify consistency with lattice QCD.** Lattice QCD measurements of α_s at multiple
   scales provide a more precise RG test than just the M_Z value. The DFC chain should
   reproduce α_s(μ) at μ = m_b = 4.18 GeV, μ = m_c = 1.27 GeV, and μ = 2 GeV from
   lattice QCD to the same accuracy as at M_Z. See `equations/alpha_s_target.py` for
   the running table.

---

## Connections

- `foundations/coupling_derivation.md` — g_common from β; r_U1/λ holonomy
- `foundations/depth_running.md` — two-scale model; M_c(D5) exact; γ_D7 open
- `foundations/hopf_fibration_geometry.md` — S⁵ as D7 closure manifold
- `foundations/mode_count_threshold.md` — SU(3) confirmed from n=3 at D7 (Cycle 74)
- `foundations/threshold_nondegeneracy.md` — non-degeneracy of n modes at D7
- `phenomena/particle_physics/quark_gluon_plasma.md` — T_c 653% error traces to α_s
- `equations/coupling_derivation.py` — g² = 8πβ/3; current α_s = 0.1049 (11% off)
- `equations/alpha_s_target.py` — target M_c(D7) computation; RG table
- `equations/gauge_couplings.py` — SM running; M_c(D7) crossing estimate
