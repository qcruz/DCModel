# Phenomenon: The Proton Does Not Decay

## Observation

Protons are extraordinarily stable. Experiments at Super-Kamiokande — a 50,000-ton detector filled
with ultra-pure water, watched by 11,000 photomultiplier tubes — have been watching protons for
decades and have never seen one decay.

Current limit: a proton's lifetime is more than 1.6 × 10^34 years for the most sensitive decay
channel (p → π⁰ + e⁺). The universe is 1.38 × 10^10 years old. The proton's lifetime exceeds
the age of the universe by at least a factor of 10^24.

## Why This Is Surprising

The proton is the lightest particle containing quarks. Normally in physics, heavier particles decay
into lighter ones unless conservation laws forbid it. The proton is heavier than pions and
electrons, so if baryon number were not conserved, there's nothing stopping it from decaying.

Every Grand Unified Theory predicts proton decay. This is actually a selling point of those
theories — it's a testable prediction. The minimal SU(5) model predicted a proton lifetime of
about 10^30 years. This was ruled out by experiments in the 1980s. More sophisticated versions
push the prediction to 10^34-10^36 years, right at the current experimental boundary.

The situation with GUT theories is progressively uncomfortable. Every time Super-Kamiokande
improves the bound, more of the available parameter space gets cut away.

## How This Model Explains It

The proton is absolutely stable in this model. Not approximately stable, not stable with a very
long lifetime. Absolutely stable by construction.

**The reason:** There are no X or Y bosons.

In SU(5) and similar theories, the large symmetry group contains force carriers — called X and Y
bosons, or leptoquarks — that couple to both quarks and leptons simultaneously. These are the
agents of proton decay: they can turn a quark into a lepton, which destabilizes the proton.

In the Dimensional Folding Model, the three forces come from three separate fiber spaces:
- Electromagnetism: U(1) circle
- Weak force: S³ sphere
- Strong force: SU(3) manifold

These fibers sit at every point in spacetime, but they are **separate**. There is no shared space
that contains both the color charge (from SU(3)) and the lepton number (from U(1) × S³). A force
carrier in the SU(3) fiber talks to quarks. A force carrier in the U(1) fiber talks to charged
leptons. They live in different rooms. Neither can reach into the other's room.

**Analogy:** Imagine two rooms in a house, connected only by an intercom. The intercom can carry
messages (interactions between particles in each room), but you cannot physically move an object
from one room to the other through the intercom. In the SU(5) model, the two rooms are connected
by a hallway (the leptoquark bosons that live in the coset). In this model, there is no hallway
— just an intercom. You cannot turn a quark into a lepton because there is no carrier that can
physically bridge the two spaces.

## Why This Requires a Structural Change

This is not a matter of making the X boson masses very heavy so the proton decay rate is
suppressed. The X bosons simply do not exist in the theory's spectrum. The question "how long does
a proton take to decay via X boson exchange?" is like asking "how long does it take to drive
from New York to London?" The answer isn't "a very long time" — the question does not apply.

The only decay channels that remain are:
1. **Gravitational operators** — quantum gravity effects at the Planck scale can violate baryon
   number, but the rate is suppressed by M_Planck^4 / m_proton^5 ≈ 10^-150 per year per proton.
   This gives a lifetime of ~10^150 years — far beyond any conceivable measurement.

2. **Quantum tunneling** — topological effects analogous to sphalerons can change baryon + lepton
   number, but at zero temperature (room temperature, underground in a detector) these are
   exponentially suppressed to undetectable rates.

## Comparison to Other Theories

| Theory | Proton Decay | Lifetime Prediction |
|---|---|---|
| Standard Model alone | Allowed (very suppressed) | ~10^31 years (not observed) |
| Minimal SU(5) | Via X boson | ~10^30 years **(ruled out)** |
| SUSY SU(5) | Via dimension-5 operators | ~10^34 years (under pressure) |
| SO(10) | Via X boson | ~10^35-36 years (constrained) |
| **This model** | **Forbidden by structure** | **>10^44 years (gravitational only)** |

## The Falsifiability

If proton decay is ever observed (in any channel), this model must find an explanation.

The structural argument rules out gauge-mediated decay, but not:
- Proton decay via higher-dimensional operators from unknown physics above the compactification scale
- Proton decay via some currently-unmodeled topological effect

If the decay mode is observed and the rate is far too fast to be gravitational, this model would
be in serious trouble. This remains a genuine experimental test.

## Current Experimental Status

Best bounds (Super-Kamiokande, 2020):
- p → π⁰ + e⁺: τ > 1.6 × 10^34 years
- p → K⁺ + ν̄: τ > 5.9 × 10^33 years
- Hyper-Kamiokande (under construction): expected to improve these by ~10×

The model predicts no signal in any of these channels. Every future null result is consistent
with — but does not confirm — the model. A positive signal in any channel would require
explanation.

## See Also

- `../../foundations/01_product_geometry.md` — the structural reason no X,Y bosons exist
- `../../equations/proton_stability.py` — lifetime calculations
- `../../comparisons/vs_grand_unification.md` — detailed comparison with SU(5) and SO(10)
