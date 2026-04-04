# Phenomenon: Quarks

## One-Sentence Synthesis

> *Placeholder — to be completed when the DFC derivation of color charge, quark masses, and confinement is formalized.*

---

## Observation

Quarks come in six types (flavors): up, down, strange, charm, bottom, top. Each flavor
comes in three colors (red, green, blue). Quarks carry color charge (strong force), weak
isospin (weak force), and electric charge (EM). They are never observed in isolation —
only in color-neutral bound states (hadrons). The top quark is the heaviest known
elementary particle at 173 GeV; the up quark is the lightest at ~2.2 MeV.

| Quark | Mass | Charge | Generation |
|---|---|---|---|
| up (u) | ~2.2 MeV | +2/3 | 1 |
| down (d) | ~4.7 MeV | −1/3 | 1 |
| strange (s) | ~96 MeV | −1/3 | 2 |
| charm (c) | ~1.27 GeV | +2/3 | 2 |
| bottom (b) | ~4.18 GeV | −1/3 | 3 |
| top (t) | ~173 GeV | +2/3 | 3 |

---

## Standard Explanation

Quarks are fundamental spin-1/2 fermions charged under all three Standard Model gauge
groups. Color charge is the SU(3) charge; confinement is the property that the strong
force grows with distance, making quark isolation energetically impossible. Masses come
from Yukawa couplings to the Higgs. The wide mass range (factor ~80,000 from up to top)
has no Standard Model explanation.

---

## Dimensional Folding Explanation

*Placeholder — DFC account to be developed.*

**Expected DFC account:** Quarks are stable closures that reach D7 (SU(3), color charge)
in addition to D5 and D6. Their three colors correspond to the three-dimensional
fundamental representation of the SU(3) closure at D7. The three generations arise from
the left/right SU(3) action at D7 (see `foundations/three_generations.md`). The mass
hierarchy is set by the depth-anchoring formula with κ_quark values.

**Key questions this document must answer:**
- Why are there exactly 6 quark flavors (3 generations × 2 isospin states)?
- Can quark masses be derived from depth-anchoring?
- What is confinement in DFC terms (why can't color-charged objects exist alone)?

---

## Formal Equations

*Placeholder — to be derived.*

The DFC depth-anchoring mass prediction: `equations/quark_masses.py`

---

## Connections to Other Phenomena

- **Strong force** — gluons mediate color charge exchange at D7; `phenomena/particle_physics/forces/strong_force.md`
- **Proton/neutron** — bound states of quarks; `phenomena/particle_physics/particles/composite_particles.md`
- **Three generations** — generation structure from D7 SU(3); `foundations/three_generations.md`
- **Proton stability** — quark → lepton transition forbidden (cross-closure D7→D5); `phenomena/particle_physics/proton_stability.md`
- **Mass hierarchy** — depth-anchoring; `foundations/mass_hierarchy.md`

---

## Open Questions

1. *Derive confinement from DFC: why does the compression field prevent isolated color-charged closures?*
2. *Derive quark mass ratios from depth-anchoring without free-fitting each generation*
3. *Explain why the top quark Yukawa coupling y_t ≈ 1 (near-unity, unlike all others)*
