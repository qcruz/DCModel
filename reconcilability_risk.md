# Model Reconcilability Risk Score (MRRS)

*Last updated: 2026-04-26 (Cycle 79)*

---

## What This Document Tracks

The **Model Reconcilability Risk Score (MRRS)** answers: *what is the probability that the
current model postulates — one self-compressing field, V(φ) = −α/2 φ² + β/4 φ⁴, bifurcation
events only — are insufficient to resolve all known failures without introducing new fundamental
assumptions?*

This is distinct from the completeness estimate. The completeness estimate tracks how much
has been done. The MRRS tracks whether what remains can in principle be done within the current
framework.

Three scopes are tracked:

| Scope | Meaning |
|---|---|
| **Core gauge/coupling** | U(1)/SU(2)/SU(3) structure + complete coupling chain (α_em, sin²θ_W, α_s) all within 5% |
| **Full SM** | Core gauge + complete mass spectrum + all Tier 2b failures resolved |
| **Complete theory** | Full SM + gravity + ℏ + quantum mechanics sector |

---

## MRRS History

| Cycle | Date | Core gauge/coupling | Full SM | Complete theory | Key change |
|---|---|---|---|---|---|
| 78 | 2026-04-26 | **35%** | **65%** | **80%** | Baseline established |
| 79 | 2026-04-26 | **28%** | **58%** | **76%** | T9 resolved: labeling confusion, not genuine inconsistency |

*Score = probability that scope CANNOT be completed within current postulates. Lower is better.*

---

## Current Scores (Cycle 79)

```
MRRS — Cycle 79 (2026-04-26)
─────────────────────────────────────────────────────────────────────
Core gauge/coupling sector      28%   (was 35%; T9 resolved: −7%)
Full SM reproduction            58%   (was 65%; T9 resolved: −7%)
Complete theory (SM+gravity+QM) 76%   (was 80%; T9 resolved: −4%)
─────────────────────────────────────────────────────────────────────
```

T9 was a labeling confusion: M_c(D1) = M_Pl ≈ 10¹⁸ GeV (Higgs sector UV boundary)
and M_c(D5/D6) ≈ 10¹³ GeV (gauge coupling IC) refer to different depth events on the
same substrate. GUT-normalized coupling crossing verified at 1.03×10¹³ GeV (one-loop).
Residual MRRS for T9 items: ~20% (λ normalization ×1.5 and μ² derivation still open).

The 30-point gap between Core and Full SM reflects the mass sector: the gauge + coupling
chain is well-constrained (Bottleneck 1 closed; 12 Tier 2a predictions), while the mass
spectrum above the second generation and the free parameter β have no derivation path.

The 18-point gap between Full SM and Complete theory reflects the ℏ/G_Newton cluster: these
may require either reframing (ℏ as a unit-system artifact, not a derived quantity) or new
substrate sub-structure.

---

## Per-Failure Risk Assessment

### Quantitative Failures (Tier 2b)

| Failure | Error | Root cause | Practical path | Path quality | P(irreconcilable) |
|---|---|---|---|---|---|
| α_s(M_Z) | 11% | M_c(D7) not from substrate; need 2.094×10¹⁵ GeV (factor 2.62×) | 3 routes: depth-running γ_D7; non-perturbative threshold; SU(3) three-kink energy | High — target quantified, routes specific | **12%** |
| Charm/strange quarks | ~15% | Uniform depth scaling breaks near top/Higgs threshold | Threshold corrections to Yukawa running | Moderate-high — small error, clear cause | **12%** |
| τ lepton mass | 8.4× | No mechanism for 3rd-generation mass enhancement; dimple model gives 2×m_μ | D7 boundary conditions on D6 outer wall (unformalized) | Low — path vague; selectivity problem vs b quark | **45%** |
| Neutrino hierarchy | 4.3× | Uniform D4 mode spacing; T10 self-contradiction | Anharmonic D4 winding modes (φ⁴ substrate is non-harmonic) | Moderate-low — direction clear, no implementation | **30%** |

### Structural Gaps

| Gap | Root cause | Practical path | Path quality | P(irreconcilable) |
|---|---|---|---|---|
| g² = 8πβ/3 heuristic (Bottleneck 2) | r_U1/λ physical identification not derived | D5-D6 coupling integral: ∫j_x dx known (Cycle 67c); need normalization + 3+1D reduction | Moderate-high — ingredients partially known | **15%** |
| v = 246 GeV | μ² from D6/D7 overlap not computed; T9 resolved (Cycle 79); λ factor ~1.5 off | D6/D7 overlap integral; field normalization factor r_D6 | Moderate — T9 blocker removed; λ×1.5 mismatch remains | **25%** |
| T9 (two closure scales: 10¹³ vs 10¹⁸ GeV) | ~~Route 3B uses M_c ≈ 10¹³; Higgs derivation uses 10¹⁸~~ **RESOLVED Cycle 79** | M_c(D1) and M_c(D5/D6) are different depth events; crossing verified numerically | Resolved — see `two_scale_resolution.md`; residual: λ×1.5, μ² | **20%** |
| β ≈ 0.035 not derived | γ_D retracted; no replacement; g² = 8πβ/3 inverts, not derives | Pre-substrate stability condition; or from kink width = Planck length (requires ℏ) | Low — no current path after Cycle 48 retraction | **50%** |
| ℏ not derivable (T8) | S_kink(D1)/ℏ = 1.13×10⁴⁰; ~13 bifurcations needed; model has 4 | Via α_em derivation (proposed); or reframe as ℏ = unit convention | Very low for absolute derivation; moderate if reframed | **60%** |
| G_Newton | Blocked by ℏ; Einstein equations not derived | L_Pl ≡ λ_kink(D1) → G = ℏc/M_Pl² once ℏ resolved | Blocked | **50%** |

---

## What Moves the MRRS

### Decreases risk (improvements)

| Development | Core | Full SM | Complete |
|---|---|---|---|
| g² = 8πβ/3 proved rigorously (Bottleneck 2 closed) | −8% | −5% | −3% |
| α_s gap closed (M_c(D7) from substrate) | −5% | −5% | −3% |
| T9 resolved with formal two-event argument | −7% ✓ | −7% ✓ | −4% ✓ | Applied Cycle 79 |
| τ mass mechanism found (D7 boundary effect) | 0% | −12% | −8% |
| β derived from pre-substrate principle | −5% | −10% | −7% |
| ℏ reframed as unit convention (dimensionless predictions) | 0% | 0% | −15% |
| v = 246 GeV derived from D6/D7 integral | −3% | −5% | −3% |

### Increases risk (setbacks)

| Development | Core | Full SM | Complete |
|---|---|---|---|
| T9 shown to be genuine contradiction (not two events) | +10% | +10% | +5% |
| τ mass failure found to reflect φ⁴ fundamental limit | 0% | +15% | +10% |
| g² coupling integral gives different coefficient (heuristic was coincidence) | +12% | +8% | +5% |
| β underdetermination shown to be structural | +8% | +12% | +8% |

---

## Relationship to Completeness Estimate

The MRRS and completeness estimate are complementary:

- **Completeness** answers: *how much has been done?* (~42.5% overall)
- **MRRS** answers: *can the rest be done within current postulates?*

A model could be 80% complete with a 10% MRRS (nearly done, nearly certain to finish) or
60% complete with a 70% MRRS (a lot done but fundamental limits may be approaching). The
DFC model currently sits at 42.5% complete with a Full SM MRRS of 65% — meaning substantial
work remains and there is meaningful uncertainty about whether the current framework is
sufficient to complete it.

The MRRS is inherently subjective — it represents an informed assessment of path quality
and structural flexibility, not a formal calculation. It should be updated when:
- A new failure emerges (increase risk appropriately)
- A failure is resolved (decrease risk)
- A derivation path is blocked or discovered (update path quality)
- A retraction reveals that a claimed derivation was wrong (increase risk)

---

## Context: What "Irreconcilable" Means

A failure is irreconcilable if resolving it requires:
1. Adding a new postulate not implied by the existing three (one field, double-well V(φ), bifurcations)
2. Changing the form of V(φ) (e.g., from φ⁴ to a different potential)
3. Adding new fields not generated by the substrate dynamics
4. Abandoning one of the Tier 1 structural claims to fix a Tier 2b numerical failure

A failure is NOT irreconcilable simply because the calculation is hard, incomplete, or
requires techniques not yet applied to the substrate. "We haven't computed this yet" is not
the same as "the current postulates cannot produce this result."

---

## Connections

- `ISSUES.md` — full tracker for open failures, tensions, and blocked derivations
- `current_state.md` — strengths, weaknesses, and direction
- `CLAUDE.md` — completeness estimate, tier system, milestone definitions
- `comparisons/swot.md` — SWOT analysis including risk factors
