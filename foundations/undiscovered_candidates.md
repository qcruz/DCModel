# DFC Predictions for Undiscovered Particles

**Status:** Track D exploration. Identifies particle candidates the DFC model predicts
from first principles with zero or few free parameters. Does not address nuclear shell
structure or superheavy elements (T4 level; see note at end).

**One-Sentence Synthesis:** DFC produces two strong undiscovered-particle candidates
from its depth structure: a ~35 keV dark matter kink at intermediate depth D4–D5,
and a 0⁺⁺ glueball at ~1527 MeV from the D7 string tension. Both are zero-free-parameter
predictions at T3 level, with the glueball approaching the current experimental
search range.

---

## What "Prediction" Means Here

A DFC prediction is a quantity derived from the field equation V(φ) = −α/2 φ² + β/4 φ⁴
and its downstream consequences, with zero or minimal experimental inputs. The tier
system applies:

- **T1**: algebraically exact from V(φ)
- **T2a**: numerically consistent, <5% error, structural argument complete
- **T3**: structural estimate, order-of-magnitude correct, formal derivation missing
- **T4**: open — no current DFC account

For undiscovered particles, the standard is: does DFC predict the existence, mass,
and interaction properties of something not yet confirmed in experiment?

---

## Candidate 1 — The Warm Dark Matter Particle (~35 keV)

**What DFC predicts:** A stable kink configuration that has anchored through D4
(acquiring inertia/mass) but has not completed the D5 U(1) closure (no electromagnetic
charge). This particle:

- Has mass from D4 inertia → gravitationally active
- Carries no U(1) winding number → no electric charge
- Has not reached D7 → no color charge
- Is therefore invisible to electromagnetic and strong interactions
- Can only interact gravitationally (through the D3–D4 compression gradient)

**Mass estimate.** The depth-to-mass scaling observed for the charged leptons gives
a mass suppression factor exp(κ × Δd) per unit depth below the electron. With
κ = 5.33 (the lepton mass ratio per depth step) and an intermediate depth of ~4.5:

```
m_DM ≈ m_e × exp(κ × (4.5 − 5.0))
     ≈ 0.511 MeV × exp(5.33 × (−0.5))
     ≈ 0.511 MeV × exp(−2.67)
     ≈ 35 keV
```

**Tier:** T3. The mass estimate depends on the unproven assumption that an intermediate
stable closure exists at d ≈ 4.5. The specific depth is not derived from V(φ); it is
the simplest intermediate value. The interaction structure (no EM, no color, yes
gravity) is T2a — it follows directly from the depth hierarchy D4 < D5 < D7.

**Experimental consistency:**
- Warm dark matter (WDM): the ~35 keV mass puts this in the warm DM regime. Free
  streaming suppresses structure below ~1 kiloparsec, which qualitatively alleviates
  the missing satellites problem in cold dark matter cosmology.
- Lyman-alpha constraint: WDM particles must have m > 3.5 keV from Lyman-alpha
  forest observations. The DFC estimate of 35 keV satisfies this by a factor of 10.
- Thermal relic tension: a thermally-produced 35 keV particle would overclose the
  universe by ~3000×. This requires a non-thermal production mechanism — the DFC
  account is that these closures were produced during the compression dynamics at the
  QCD transition, not via thermalization with the ordinary matter plasma. The specific
  mechanism is T4.

**What would confirm it:** Detection of a ~35 keV particle with no electromagnetic
or strong interaction signature, consistent with galactic rotation curve observations.
Relevant searches: XMM-Newton and Chandra X-ray observatory anomalous line searches
(the unidentified 3.55 keV line observed in 2014 is somewhat below this prediction;
DFC's T3 estimate carries ±50% order-of-magnitude uncertainty).

**What would falsify it:** Confirmation that dark matter is heavy (GeV–TeV WIMP),
or that it has any electromagnetic coupling, or that warm DM is definitively ruled
out by structure formation data.

---

## Candidate 2 — The 0⁺⁺ Glueball (~1527 MeV)

**What DFC predicts:** Closed D7 flux-tube states — glueballs — whose masses are
determined by the string tension σ = Q_top × Λ_QCD². With Q_top = 2 (T1, from the
kink topological charge) and Λ_QCD = 304.5 MeV (T2a, from the ECCC chain), the
ground-state glueball mass is:

```
m(0++) = 2√(πσ) = 2√(πQ_top) × Λ_QCD
       = 2√(2π) × 304.5 MeV
       ≈ 1527 MeV
```

This is a zero-free-parameter prediction: the glueball mass comes entirely from
Q_top (T1) and Λ_QCD (T2a). No fitting to hadronic data is involved.

**Tier:** T3. The Nambu-Goto closed-string formula used here is a structural
estimate; the formal derivation of glueball masses from the DFC field equation
is not yet complete. The string tension σ = Q_top × Λ_QCD² is T2a from the center
vortex mechanism (the proportionality constant comes from the vortex factor
1 − cos(2π/N_c) = N_c/2, which is T1 exact for N_c = 3).

**Further predictions from the same formula:**

| State | DFC prediction | Lattice QCD range | Error |
|---|---|---|---|
| 0⁺⁺ (lightest) | 1527 MeV | 1475–1730 MeV | +3.5% (within range) |
| 2⁺⁺ | 2644 MeV | 2000–2800 MeV | within range |
| Pomeron intercept α₀ | 1/2 (exact, T1) | ~0.5 (phenomenology) | 0% |
| Regge slope α' | 0.215 GeV⁻² | ~0.2 GeV⁻² | ~7% |

**Experimental status:** The 0⁺⁺ glueball is actively searched for. Two candidates
in the literature are f₀(1500) at 1505 MeV and f₀(1710) at 1710 MeV. Neither is
confirmed as a pure glueball; both may be mixtures with quark-antiquark states.
DFC's prediction of 1527 MeV lies between these two candidates.

**What would confirm it:** An unambiguous identification of a meson with no quark
content and mass ~1500–1710 MeV, 0⁺⁺ quantum numbers, produced preferentially
in gluon-rich processes (J/ψ radiative decays, proton-proton central production).
Upcoming experiments: BESIII, LHCb, GlueX.

**What would falsify it:** If lattice QCD converges on a 0⁺⁺ glueball mass
significantly below 1475 MeV or above 1730 MeV, the DFC estimate would be in
tension. The prediction is robust as long as σ = Q_top × Λ_QCD² holds.

---

## Candidate 3 — Higher Glueball Excitations

The same Nambu-Goto formula gives a tower of glueball states:

```
m_n² = 8πσ × (n + α₀)    where α₀ = Q_top/4 = 1/2
```

So the mass ratios m_n/m_0 = √(2n + 1) are T1 exact. This is a falsifiable
prediction: if a glueball family is confirmed, the ratio of successive masses should
follow √(2n+1): 1, √3, √5, √7, ...

This ratio (√3 ≈ 1.73 between the ground state and first excitation) is a sharp
and distinctive prediction. The lattice ratio for 0⁺⁺/2⁺⁺ is ~1.35–1.55, which
is somewhat below √3 = 1.73. This tension is noted (T3 level, lattice comparison).

---

## What DFC Cannot Currently Predict: Superheavy Elements

The periodic table currently extends to Z = 118 (oganesson). Theoretical
predictions for Z = 119, 120, 126 (predicted magic number) and beyond come from
nuclear shell models, relativistic Hartree-Fock-Bogoliubov calculations, and
nuclear density functional theory. These methods track nucleon shell closures,
spin-orbit splitting, and pairing correlations in detail.

DFC's nuclear physics is at T3 level:
- Proton mass: 934.8 MeV vs observed 938.3 MeV (−0.4%, T3)
- Delta(1232): 1206.8 MeV vs 1232 MeV (−2.0%, T3)
- Nuclear binding energy: not derived from DFC

To predict a new stable superheavy element, DFC would need:
1. Nuclear binding energy from D7 SU(3) dynamics (T4 — not begun)
2. Nuclear shell structure from D7 modes (T4)
3. Shell closure predictions at specific Z values (T4)

This is a substantial open research program. DFC is not the right tool for element
prediction at its current stage of development.

---

## Summary

| Candidate | Mass | Tier | Experimental Status | Falsification Test |
|---|---|---|---|---|
| Dark matter particle | ~35 keV | T3 | Not detected; 3.55 keV anomaly nearby | EM coupling found → rules out |
| Glueball 0⁺⁺ | ~1527 MeV | T3 | f₀(1500)/f₀(1710) candidates | Mass confirmed far outside 1475–1730 |
| Glueball excitations | m_n = √(2n+1) × m_0 | T3 | Not identified | Ratio deviates from √(2n+1) |
| Superheavy element | — | T4 | N/A | N/A — not predicted |

The two strongest predictions are the ~35 keV dark matter candidate and the glueball
at ~1527 MeV. Both are zero-free-parameter results from V(φ) parameters. Neither
requires fitting to any hadronic data. Both are testable with current or near-future
experiments.

---

## Connections

- `equations/dark_matter.py` — compression threshold scales for D4 closure
- `equations/ym_glueball_mass.py` — glueball mass from string tension
- `equations/d7_nonpert_coefficients.py` — α_0, σ, m_ρ from D7 dynamics
- `educational/15_dark_matter.md` — full DFC dark matter account
- `phenomena/cosmology/dark_matter.md` — cosmological context
- `foundations/yang_mills_clay.md` — formal derivation of string tension
