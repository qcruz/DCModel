# Module 30 — Hadron Spectroscopy: Masses from Topology

*Prerequisites: Module 04 (Forces), Module 05 (Particles) recommended.*

---

## The Problem: Why Do Hadrons Have These Masses?

Protons weigh 938 MeV. Rho mesons weigh 775 MeV. Delta baryons weigh 1232 MeV. In standard QCD, these masses emerge from lattice simulations — enormous numerical calculations that produce the right numbers but offer limited insight into *why* each particle has the mass it does. The quark masses contribute less than 2% of the proton's mass; the rest is binding energy from the strong force.

DFC provides an alternative account: hadron masses arise from the **Regge trajectory** structure of D7 kink configurations, with string tension and intercepts determined entirely by the substrate potential V(phi). Every hadron mass ratio is the square root of a ratio of small integers — pure topology, with no free parameters.

---

## String Tension from the Substrate

When two D7 kinks (quarks) are separated, the substrate between them forms a flux tube — a region of compressed field connecting the two endpoints. The energy per unit length of this tube is the **string tension**, which is the fundamental scale of hadron spectroscopy.

The DFC string tension is determined by the topological charge and the QCD scale:

```
sigma = Q_top * Lambda_QCD^2
```

where the topological charge per kink is two (from the D7 homotopy) and the QCD scale is 304.5 MeV (derived from the substrate's dimensional transmutation chain). This gives a string tension of 185,440 MeV squared, within 4.2% of the value extracted from lattice QCD and Regge phenomenology.

---

## Regge Trajectories: Spin and Mass on a Line

A Regge trajectory is a relationship between a hadron's spin J and the square of its mass: particles with the same quantum numbers but increasing spin lie on a straight line when plotted as J versus mass squared. The trajectory equation is:

```
J = alpha_0 + alpha' * m^2
```

The intercept (the value of the trajectory at zero mass squared) and the slope (inversely proportional to the string tension) together determine the mass of every particle on the trajectory.

In DFC, the Regge slope is the inverse of twice the string tension times the circle constant:

```
alpha' = 1 / (2 * pi * sigma) = 1 / (4 * pi * Lambda_QCD^2)
```

This gives 0.858 inverse GeV squared, within 2.5% of the observed value of approximately 0.88 inverse GeV squared.

---

## Meson Masses

A meson is a flux tube with two endpoints — two D7 kinks connected by a string. Each endpoint contributes a topological charge fraction to the Regge intercept. With two endpoints:

```
alpha_0^meson = 2 * Q_top / 8 = 1/2
```

The rho meson (spin-1, lightest vector meson) sits on this trajectory at J = 1:

```
m_rho^2 = (J - alpha_0) / alpha' = (1 - 1/2) / alpha' = 2 * pi * Lambda_QCD^2
```

This predicts a rho mass of 763 MeV, compared to the observed 775 MeV — an error of 1.6% with zero free parameters.

Higher-spin mesons follow the same trajectory. The mass squared increases by a fixed amount for each unit of spin, producing the famous linear Regge trajectory that is one of the oldest and most robust patterns in hadron physics.

---

## Baryon Masses: The Y-Junction

A baryon contains three quarks — three D7 kinks meeting at a **Y-shaped junction**. This is topologically distinct from the two-endpoint meson. The Y-junction introduces a penalty: one fewer independent oscillator compared to what three separate strings would give. This penalty shifts the intercept by negative one unit.

The nucleon (proton/neutron) trajectory intercept:

```
alpha_0^N = 3 * Q_top/8 - 1 = 3/4 - 1 = -1/4
```

The proton (spin-1/2) sits at J = 1/2 on this trajectory:

```
m_p^2 = (1/2 - (-1/4)) / alpha' = (3/4) / alpha' = 3 * pi * Lambda_QCD^2
```

This predicts a proton mass of 934.8 MeV, compared to the observed 938.3 MeV — an error of 0.4% with zero free parameters.

The Delta baryon (spin-3/2) sits on a higher trajectory with a spin-alignment bonus of half a unit of topological charge:

```
alpha_0^Delta = -1/4 + Q_top/4 = -1/4 + 1/2 = +1/4
```

This gives:

```
m_Delta^2 = (3/2 - 1/4) / alpha' = (5/4) / alpha' = 5 * pi * Lambda_QCD^2
```

Predicted: 1206.8 MeV. Observed: 1232.0 MeV. Error: 2.0%.

---

## Mass Ratios Are Pure Topology

The most striking feature of these predictions: every hadron mass **ratio** is the square root of a ratio of small integers. The QCD scale cancels entirely.

| Ratio | DFC prediction | Observed | Error |
|---|---|---|---|
| m_p / m_rho | sqrt(3/2) = 1.2247 | 1.2102 | +1.2% |
| m_Delta / m_p | sqrt(5/3) = 1.2910 | 1.3130 | -1.7% |
| m_Delta / m_rho | sqrt(5/2) = 1.5811 | 1.5891 | -0.5% |

These ratios depend on nothing but the topological integers 2, 3, and 5 — the number of string endpoints (2 for mesons, 3 for baryons), the spin values, and the Y-junction penalty. No adjustable parameters enter.

The mass-squared spacing on any trajectory is exactly twice the circle constant times the string tension. This means the mass squared of any hadron on a given trajectory is an integer (or half-integer) multiple of a fixed quantum — a prediction that can be tested against every known meson and baryon resonance.

---

## What Remains Open

| Question | Status |
|---|---|
| String tension sigma = Q_top * Lambda_QCD^2 | Tier 3 (4.2% error; prove from D7 kink vacuum energy) |
| Meson intercept alpha_0 = 1/2 | Tier 2a (verified) |
| Baryon Y-junction penalty = -1 | Tier 3 (not yet derived from dynamics) |
| Proton mass 934.8 MeV | Tier 3 (-0.4%, 0 free params) |
| Delta mass 1206.8 MeV | Tier 3 (-2.0%, 0 free params) |
| Rho mass 763 MeV | Tier 3 (-1.6%, 0 free params) |
| Higher resonance masses | Not yet systematically tested |
| Hadron widths (decay rates) | Open — requires coupling calculations |

The mass predictions are at Tier 3 because the Y-junction penalty and string tension derivation are not yet completed at Tier 2a. The mass *ratios* are more robust than the absolute masses because they do not depend on the QCD scale.

The main gap: derive the Y-junction penalty of negative one from the D7 kink dynamics rather than importing it from Nambu-Goto string theory. This is an active research item.

---

## Summary

Hadron masses in DFC are not outputs of numerical simulations — they are consequences of the number of kink endpoints, their topological charges, and the junction topology. A meson has two endpoints and spin on a line. A baryon has three endpoints meeting at a Y-junction. The string tension is fixed by the substrate potential. Every mass ratio reduces to the square root of a ratio of small integers.

The pattern is simple enough to state in one line: the proton mass is the square root of three times the circle constant, multiplied by the QCD scale. Whether this simplicity survives to higher resonances and whether the junction penalty can be derived from first principles are the open questions.

---

*Next: Module 31 (when created) — or return to Module 06 (Predictions) for the full scorecard.*
