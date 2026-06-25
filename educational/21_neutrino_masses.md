# Module 21 — Neutrino Masses: Why the Third Generation Gets a Depth Correction

**Series:** DFC Educational Modules — each module is self-contained. For background on
the substrate, kinks, and compression depths, see Module 01 (The Substrate) and Module 03
(The Depth Map). Module 05 (Particles) introduces the lepton generations.

**Status:** The neutrino mass prediction is Tier 3 structural. The derivation of the depth
correction δd = 1/(6π) has multiple T1 algebraic forms (all equivalent) but the explicit
BVP calculation confirming it from first principles remains open (T3→T2a path identified).

---

## The Puzzle

Neutrinos barely interact with anything. They travel through the Earth as if it were not
there. For a long time, physicists assumed they were massless. Then, in the late 1990s,
experiments detected something unexpected: neutrinos change type — an electron-neutrino
born in the Sun occasionally arrives at a detector as a muon-neutrino or tau-neutrino.
This "oscillation" is only possible if neutrinos have mass, and if the three types have
different masses.

This creates a puzzle with two layers:

1. **Why are neutrino masses so tiny?** The electron mass is 0.511 MeV. Neutrino masses
   are below 0.1 eV — at least five million times lighter. No other known particles are
   so much lighter than their charged partners.

2. **Why are the three masses so unequally spaced?** The three neutrinos (ν₁, ν₂, ν₃)
   have masses in a ratio roughly m₁ : m₂ : m₃ ≈ 1 : 5 : 30. The charged leptons
   (electron, muon, tau) have a similarly steep mass hierarchy, but the neutrino pattern
   is distinct — especially in how the ratio m₃/m₂ ≈ 5.82 relates to the ratio m₂/m₁.

The Standard Model does not explain either of these features. Neutrino masses are inserted
by hand. DFC offers a structural account.

---

## The DFC Account: Depths and Mass Ratios

In DFC, particles are not fundamental objects — they are topological configurations (kinks)
in a single compression field at different compression depths. Each lepton generation
corresponds to a different compression threshold in the D6 depth behavior.

The mass of a particle is determined by how deep its kink configuration sits in the
compression sequence. If the first-generation neutrino sits at depth d₁, the
second-generation at d₂, and the third at d₃, then their masses relate as:

The mass ratio between adjacent generations is approximately constant: m₂/m₁ ≈ κ and
m₃/m₂ ≈ κ for some fixed "step ratio" κ that depends on the D6 compression topology.
This produces a geometric mass sequence — each generation heavier than the last by the
same multiplicative factor.

For neutrinos, the DFC prediction for the step ratio is κ ≈ 5.33, derived from the
D6 SU(2) geometry. With this value:

- m₂/m₁ ≈ 5.33 (prediction)
- m₃/m₂ ≈ 5.33 (prediction at leading order)

The observed value of m₃/m₂ from oscillation experiments is approximately 5.82.

At leading order, 5.33 is 8.3% off — a real discrepancy that the model must explain.

---

## The Depth Correction: Why the Third Neutrino Is Different

Here is where DFC makes a structural prediction that distinguishes it from simpler models.
The third neutrino (ν₃) sits at the deepest compression threshold in the D6 sequence —
it is the closest of the three neutrinos to the D7 SU(3) closure depth, where color
charge (the strong force) is born.

The D7 depth behavior involves a topological winding that affects any field configuration
that passes near it. The first and second neutrinos (ν₁, ν₂) are far enough from D7 that
they are unaffected. The third neutrino sits close enough to D7 that its compression depth
receives a small correction from the D7 SU(3) topology.

This correction is called the **depth shift** δd. In DFC, it evaluates to:

The depth shift equals (I₄ − 1) divided by 2π, where I₄ is the kink shape integral equal
to the SU(3) Casimir of the fundamental representation (4/3). This gives δd = (1/3)/(2π) = 1/(6π).

Numerically, 1/(6π) ≈ 0.0531 — a small but nonzero correction to the compression depth
of ν₃.

The corrected mass ratio prediction becomes:

The ratio m₃/m₂ equals κ raised to the power (1 + δd), which equals 5.33 raised to the
power (1 + 1/(6π)).

Computing this: 5.33^(1 + 1/(6π)) = 5.33^1.0531 ≈ 5.8248.

The observed ratio is 5.8242. The DFC prediction is off by +0.010% — essentially exact.

---

## Why 1/(6π) and Not Some Other Number

The depth correction δd = 1/(6π) is not adjusted to fit the data. It follows from three
independent algebraic identities, all of which give the same result:

**Form 1:** δd = N_c / (N_Hopf × 2π)

The number of colors N_c = 3. The number of complex sphere dimensions in the DFC
compression cascade (the "Hopf number") N_Hopf = 9. The 2π is the winding phase
normalization. Result: 3/(9 × 2π) = 1/(6π).

**Form 2:** δd = β × N_c / 2

The quartic self-coupling of the substrate field is β = 1/(9π), derived independently
from the ECCC consistency condition. N_c = 3. Result: (1/(9π)) × (3/2) = 1/(6π).

**Form 3:** δd = (I₄ − 1) / (2π)

The kink shape integral I₄ = 4/3 is both the integral ∫sech⁴(u)du and the SU(3)
fundamental Casimir C₂(fund, SU(3)) — the same number that governs the gauge coupling,
the string tension, and the mass gap. The correction above the color-singlet baseline
(where δd = 0) is exactly (I₄ − 1)/(2π) = (1/3)/(2π) = 1/(6π).

All three forms give exactly the same number. The common root is a single algebraic
identity:

The ratio N_c/N_Hopf equals I₄ minus 1, which equals 1/3.

That is: 3/9 = 4/3 − 1 = 1/3. This is the underlying fact from which δd = 1/(6π)
follows in all three derivations.

---

## Why ν₃ and Not ν₁ or ν₂

The depth correction applies specifically to the third neutrino because it is a property
of color representation. In DFC, the depth shift from D7 depends on the color Casimir
of the particle:

- Color-singlet states (no color charge): depth shift = 0
- Fundamental-representation states (quarks, ν₃ near D7 threshold): shift = (I₄ − 1)/(2π)
- Adjoint-representation states (gluons): shift = (C_A − 1)/(2π) = 2/(2π) = 1/π

The adjoint shift is exactly 6 times larger than the fundamental shift — a ratio that
follows directly from the Casimir values and makes a falsifiable prediction for any
future measurement sensitive to gluon-sector depth effects.

The first and second neutrinos sit farther from D7. They do not overlap with the SU(3)
closure topology in the same way. Their depth correction is zero to leading order, which
is why they follow the simple κ = 5.33 geometric pattern without modification.

This is a structural prediction, not a fit parameter. If the correction appeared at ν₂
instead of ν₃, DFC would require a different assignment of compression depths.

---

## The Open Gap

The 0.010% agreement is striking, but the tier status is T3 — structural argument
rather than a derivation from first principles. What would make it T2a?

The missing step is an explicit boundary-value calculation (BVP): solve the Dirac equation
for a ν₃-like mode in the D7 Pöschl-Teller background field m(x) = m_KK tanh(x/ξ), and
show that the bound-state frequency shifts by exactly β × (N_c/2) × m_KK = m_KK/(6π).

The Pöschl-Teller Dirac system has a known analytic spectrum, so this calculation is
tractable in principle. It would confirm whether δd = 1/(6π) arises from the Dirac
dynamics in the D7 background or whether additional ingredients are needed.

Until that calculation is complete, the 0.010% agreement is a structural prediction
supported by three algebraically distinct T1 routes — but not a proved derivation.

---

## Summary

| Item | DFC prediction | Observed | Error | Tier |
|---|---|---|---|---|
| Neutrino step ratio κ | 5.33 (D6 geometry) | — | — | T2a |
| Depth correction δd | 1/(6π) ≈ 0.0531 | — | — | T3 |
| m₃/m₂ (with correction) | 5.8248 | 5.8242 | +0.010% | T3 |
| m₂/m₁ (no correction) | 5.33 | ~5.3–5.6 | ~0–4% | T2b |
| δd(adj)/δd(fund) | 6 exactly | — | — | T1 (prediction) |

The depth correction δd = 1/(6π) is algebraically exact from three independent routes.
Whether it arises from the D7 Dirac dynamics is the remaining open question.

---

**See also:** Module 05 (Particles) for the lepton generation structure. Module 03
(The Depth Map) for the D6/D7 depth assignments. `equations/neutrino_casimir_depth.py`
for the algebraic verification. `phenomena/particle_physics/particles/neutrinos.md`
for the full DFC account including oscillation data.
