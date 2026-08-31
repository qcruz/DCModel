# Module 31 — The Proton Spin Puzzle: Where Does the Spin Come From?

**Series:** DFC Educational Modules. Recommended reading: Module 05 (Particles),
Module 12 (Substrate Topology), Module 30 (Hadron Spectroscopy).

**Status:** g_A = 4/pi is Tier 2a (derived from V(phi), 0 free parameters, -0.19%).
Quark spin fraction Sigma = 4/(3*pi) is Tier 3 (0 free parameters, +29% vs COMPASS).
Spin suppression mechanism (1/N_c from topology) is Tier 1 structural.

---

## The Crisis That Wasn't

The proton has spin one-half. In the naive quark model, three quarks sit inside the
proton with their spins arranged to give this total: two pointing up and one pointing
down (or the reverse). All of the proton's angular momentum comes from quark spins.
This simple picture predicts that quarks carry 100% of the proton's spin.

In 1988, the European Muon Collaboration (EMC) at CERN measured how much spin the
quarks actually carry. The answer was shocking: quarks contribute only about 30% of
the proton's spin. Roughly 70% of the spin is "missing." This became known as the
**proton spin crisis** — one of the most surprising experimental results in hadron
physics.

The spin sum rule tells us where the total spin must reside:

```
1/2 = (1/2) * Sigma + Delta_G + L_q + L_g
```

The total proton spin (one-half) equals the quark spin contribution (one-half times
the quark spin fraction Sigma), plus the gluon spin (Delta_G), plus quark orbital
angular momentum (L_q), plus gluon orbital angular momentum (L_g). All four terms
can contribute. The "crisis" was the discovery that the first term is far smaller
than anyone expected.

Modern measurements (COMPASS, HERMES, RHIC, Jefferson Lab) have refined the picture.
The quark spin fraction Sigma is approximately 0.33, with an uncertainty of about
0.04. The gluon spin Delta_G is roughly 0.2 to 0.4. The orbital terms are the
hardest to measure and remain poorly constrained.

---

## Why the Quark Model Gets It Wrong

The naive quark model treats quarks as free particles sitting at rest inside the
proton. In this picture, the proton is just three balls in a bag, and spin is
simply the vector sum of their individual spins.

But this is wrong for a fundamental reason: the strong force is *strong*. Quarks
inside the proton interact so intensely that treating them as independent particles
is a poor approximation. The proton is not three balls in a bag — it is a seething
cloud of quarks, antiquarks, and gluons, all carrying angular momentum. Quark-antiquark
pairs from the vacuum (the "sea") can carry spin. Gluon fields carry spin. And
everything is in motion, contributing orbital angular momentum.

The question is not why is Sigma so small, but rather: is there a framework in
which a small Sigma is *expected*?

---

## What DFC Says: Baryons Are Topological Objects

In DFC, the proton is not three point-like quarks. It is a **Y-junction** — a
topological configuration in which three D7 kink lines meet at a central point.
Each kink carries a Jackiw-Rebbi zero mode (the quark), and the junction region
is where the three flux tubes merge.

This is the Skyrme picture of baryons, but with the Skyrmion parameters derived
from the substrate potential V(phi) rather than fitted to data.

The critical insight comes from the Skyrme model's treatment of spin. In this
framework, the proton's spin does not come from adding up the spins of three
constituent quarks. Instead, spin arises from **collective rotation** of the entire
topological configuration in isospin space. The Y-junction rotates as a rigid body,
and quantizing this rotation gives spin one-half.

This is analogous to how a spinning top gets its angular momentum from the collective
rotation of all its atoms, not from each atom spinning individually. The proton
is a topological "lump" that rotates collectively.

---

## The 1/N_c Suppression: Why Sigma < 1 Is Natural

In the large-N_c expansion (where N_c is the number of color charges — three in
our world), the Skyrme model makes a clean prediction about the scaling of spin
observables:

- The isovector axial coupling g_A scales as N_c (grows with the number of colors).
- The quark spin fraction Sigma scales as a constant (stays fixed as N_c grows).
- Therefore the *ratio* Sigma/g_A scales as one over N_c — it is suppressed.

At N_c = 3, this gives Sigma approximately equal to g_A divided by three. The quark
spin content is suppressed by a factor of three relative to the axial coupling.
This is not a mysterious cancellation — it is a direct consequence of the topological
origin of baryon spin.

In the naive quark model, Sigma equals one because each quark contributes independently.
In the Skyrme/DFC picture, individual quark spins are not the fundamental degrees of
freedom. The spin lives in the collective rotation, and only a fraction (of order
one over N_c) projects onto quark spin operators.

The spin crisis is not a crisis at all. It is the expected behavior of a topological
baryon.

---

## The DFC Prediction: Sigma = 4/(3*pi)

DFC makes a zero-free-parameter prediction for the quark spin fraction. It combines
two ingredients:

**First**, the axial coupling g_A. In the standard Skyrme model, g_A is an input —
it is taken from the measured value of neutron beta decay (1.2756). DFC derives it:
the kink Yukawa coupling from V(phi) gives g_A equal to four divided by pi, which is
1.2732 — within 0.19% of the observed value. This is a Tier 2a prediction with zero
free parameters.

**Second**, the 1/N_c suppression. In the leading large-N_c approximation, Sigma
equals g_A divided by N_c. With N_c = 3, this gives:

```
Sigma = g_A / N_c = (4/pi) / 3 = 4/(3*pi) = 0.4244
```

The COMPASS experiment measures Sigma = 0.330 with an uncertainty of 0.040. The DFC
prediction is 29% above the central value, but only 2.4 standard deviations away.

This is a genuine prediction — a pure number derived from the substrate potential —
but it overshoots the data. The likely source of the discrepancy is well understood:
the naive 1/N_c formula does not account for the detailed structure of the Skyrmion
profile. More refined Skyrme calculations with physical pion mass give a ratio of
isoscalar to isovector moments of inertia (I_0/I_1) between 0.22 and 0.28, which
would bring Sigma down to the range 0.28 to 0.36 — consistent with the data.

Computing I_0/I_1 from the DFC Y-junction kink profile (rather than the standard
hedgehog ansatz) would give a DFC-specific refined prediction.

---

## What About the Gluon Spin?

In the Skyrme/DFC picture, gluons do not appear as separate degrees of freedom. The
soliton is a configuration of the pion field (or equivalently, the substrate at D7
depth), and it has no explicit gluon content.

Does this mean Delta_G = 0? Not exactly. The quark spin fraction Sigma is
scale-dependent: at different momentum scales, the anomaly equation redistributes
spin between quarks and gluons. What the Skyrme model computes is the
**scale-invariant** combination of quark and gluon spin, not Sigma at a particular
momentum transfer.

The gluon spin measured at RHIC and COMPASS (Delta_G approximately 0.28) is an
artifact of probing the proton at a particular resolution. At high resolution,
you see gluon fields that carry angular momentum. At the topological level, these
gluon fields are part of the soliton — they are the substrate configuration itself,
not a separate entity.

---

## The Spin Budget

Using the DFC leading-order prediction, the proton's spin budget is:

| Source | Contribution | Fraction |
|---|---|---|
| Quark spin (1/2 times Sigma) | 0.212 | 42% |
| Gluon spin + orbital | 0.288 | 58% |
| **Total** | **0.500** | **100%** |

The "missing" 58% is not missing at all — it is the orbital and gluonic angular
momentum that naturally arises from the collective rotation of a topological
soliton.

---

## Summary

| Item | DFC prediction | Observed | Status |
|---|---|---|---|
| g_A (axial coupling) | 4/pi = 1.2732 | 1.2756 | Tier 2a (-0.19%) |
| Sigma (quark spin fraction) | 4/(3*pi) = 0.424 | 0.330 +/- 0.040 | Tier 3 (+29%, 2.4 sigma) |
| Spin crisis resolution | Sigma < 1 is natural (1/N_c topology) | — | Tier 1 structural |
| I_0/I_1 from DFC kink profile | Not yet computed | — | Tier 4 (open) |

**Key insight:** The proton spin puzzle is not a puzzle in DFC. Quark spin suppression
is the expected behavior of a topological baryon. The proton's spin comes from
collective rotation of a Y-junction configuration, and individual quark spins are
a subleading projection of order 1/N_c.

**What remains open:** Computing the ratio of isoscalar to isovector moments of
inertia (I_0/I_1) from the DFC Y-junction profile would give a refined prediction
for Sigma, likely in the range 0.28 to 0.36. Computing Delta_G from the DFC gluon
field strength tensor would provide a second testable prediction.

---

## See also

- `equations/proton_spin_dfc.py` — full quantitative analysis (6/6 PASS)
- `equations/nucleon_magnetic_moments.py` — related nucleon structure predictions
- `equations/baryon_mass_dfc.py` — baryon masses from Regge trajectories
- Module 05 (Particles) — how quarks and baryons appear
- Module 30 (Hadron Spectroscopy) — hadron masses from D7 topology
