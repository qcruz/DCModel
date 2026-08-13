# Module 26 — Nuclear Saturation: Why Nuclei Don't Collapse

**Series:** DFC Educational Modules — each module is self-contained and can be read
independently. For background on the nuclear physics framework, see Module 20
(Nuclear Physics). For the N=126 shell closure, see Module 25.

**Context:** This module documents the resolution of three T4 gaps in the nuclear
binding energy formula — the volume term mechanism (a_V), the surface term (a_S),
and the pairing energy (a_pair) — from Cycle 369. It is written in a journaling
style, capturing the reasoning and discovery process.

---

## The Problem: What Holds Nuclei Together — And What Stops Them Collapsing?

Every atomic nucleus is a competition between attraction and repulsion. The strong
nuclear force pulls protons and neutrons together; the electromagnetic force pushes
protons apart. But there is a deeper puzzle: why does nuclear binding energy per
nucleon saturate at about 8.5 MeV, roughly independent of how many nucleons are
present? Why doesn't adding more nucleons just keep increasing the binding?

This is the saturation problem. In a naive picture where every nucleon attracts
every other, binding energy would grow as A(A-1)/2 — proportional to the number of
pairs. That would make heavy nuclei enormously more tightly bound per nucleon than
light ones. Instead, the binding energy per nucleon rises quickly from hydrogen to
iron, then barely changes from iron to uranium. Nuclear matter behaves like a liquid
with a definite density, not like a gas that keeps compressing.

The semi-empirical mass formula (SEMF), due to Bethe and Weizsacker, captures
this beautifully:

The binding energy of a nucleus with A nucleons and Z protons equals a volume
term proportional to A, minus a surface correction proportional to A to the
two-thirds, minus a Coulomb repulsion term, minus an asymmetry penalty for
unequal numbers of protons and neutrons, plus or minus a pairing bonus.

B(A,Z) = a_V A - a_S A^{2/3} - a_C Z(Z-1)/A^{1/3} - a_A (A-2Z)^2/A +/- delta

The five coefficients — a_V, a_S, a_C, a_A, and a_pair — encode different physics.
DFC had already derived the Coulomb coefficient a_C from its electromagnetic coupling
(+0.9%) and the asymmetry coefficient a_A from Fermi kinetic energy (+6.3%). But the
volume term a_V, the surface term a_S, and the pairing energy were all marked T4 —
open gaps with no DFC account.

This module describes how all three were closed to T3 in Cycle 369.

---

## The False Start: Why Pion Exchange Doesn't Work

The obvious starting point for nuclear binding is pion exchange. Pions are the lightest
strongly interacting particles, and they mediate the long-range nuclear force. DFC
derives the pion-nucleon coupling from the Goldberger-Treiman relation: g_piNN equals
the axial coupling times the nucleon mass divided by the pion decay constant. This
gives g_piNN = 12.31 (observed: 13.45, about 8% low).

The one-pion exchange (OPE) potential between two nucleons is a Yukawa interaction —
attractive, falling off exponentially with a range set by the pion Compton wavelength
(about 1.4 fm). If you compute the Hartree mean-field energy of nuclear matter using
this potential, you get a volume binding energy of about 26.7 MeV per nucleon — far
too large. The observed value is 15.8 MeV.

But the problem is worse than just getting the wrong number. **The OPE Hartree
contribution to symmetric nuclear matter vanishes exactly.** This is a T1 result —
it follows from pure isospin algebra with no model dependence.

Here is why. The pion couples to nucleons through the isospin operator tau. The OPE
potential between two nucleons carries a factor of tau_1 dot tau_2 — the dot product
of the two nucleons' isospin vectors. In the Hartree (direct) mean field, you average
the isospin of each nucleon independently over the filled Fermi sea. For symmetric
nuclear matter with equal numbers of protons and neutrons, the average isospin is
zero:

The average of the third component of isospin, summed over the filled Fermi sea,
equals Z times plus one-half plus N times minus one-half, which equals zero when
Z equals N.

The average tau_1 dotted with the average tau_2 is therefore zero times zero equals
zero. The Hartree OPE contribution vanishes identically.

This is not a cancellation that happens to be small — it is algebraically exact.
The OPE Fock (exchange) contribution is nonzero but turns out to be repulsive in the
spin-averaged channel, making matters worse. Pion exchange alone does not bind
nuclear matter.

---

## The Correct Mechanism: Sigma-Omega Cancellation

If pions don't do it, what does? The answer, understood since Walecka's work in the
1970s, is that nuclear binding comes from a near-cancellation between two heavier
meson exchanges:

**Sigma (scalar, J^PC = 0++).** An isoscalar scalar meson that couples to the
nucleon scalar density. This produces a uniform attractive potential throughout
the nuclear interior. The attraction is strong — several hundred MeV per nucleon.

**Omega (vector, J^PC = 1--).** An isoscalar vector meson that couples to the
nucleon baryon current. This produces a repulsive potential, also several hundred
MeV per nucleon.

The binding energy per nucleon — about 16 MeV — is the small difference between
two large numbers, each of order 300-400 MeV. This is why nuclear saturation works:
the attractive and repulsive potentials scale differently with density, and at
nuclear saturation density they nearly cancel, leaving just the observed 8.5 MeV/A
binding.

### What DFC contributes

DFC provides two inputs to the Walecka model:

**The omega mass.** The omega meson sits on the same Regge trajectory as the rho
meson. DFC predicts m_rho = m_omega = sqrt(2 pi) times Lambda_QCD = 763.3 MeV.
The observed omega mass is 782.7 MeV, so the DFC value is 2.5% low — well within T3.

**The sigma coupling constant.** In the linear sigma model — where the sigma is the
chiral partner of the pion — the sigma-nucleon coupling is determined by chiral
symmetry:

The sigma coupling equals the nucleon mass divided by the pion decay constant.

g_sigma = M_N / f_pi = 934.8 / 96.9 = 9.65

This is a structural result from chiral symmetry, not a fit. The value falls in the
standard Walecka range of 8-10, which is encouraging.

### The saturation curve

With g_sigma fixed, the saturation condition — requiring that the energy per nucleon
has a minimum at observed nuclear density with the correct depth of 15.8 MeV —
becomes a constraint relating the omega coupling g_omega and the sigma mass m_sigma.
For each choice of g_omega, there is exactly one m_sigma that satisfies saturation.

The self-consistency curve spans the standard Walecka parameter range:

| g_omega / g_sigma | g_omega | m_sigma (MeV) |
|---|---|---|
| 1.0 | 9.6 | 648 |
| 1.2 | 11.6 | 565 |
| 1.4 | 13.5 | 498 |

Every point on this curve reproduces a_V = 15.835 MeV by construction. DFC does not
yet select a unique point on the curve — the individual values of g_omega and m_sigma
remain T4. But the mechanism is identified, and the DFC-derived g_sigma constrains the
allowed region.

---

## Surface Energy: A Ratio of Length Scales

The surface term a_S accounts for nucleons at the nuclear surface having fewer
neighbors than those in the interior. Its value is controlled by two length scales:
the range of the nuclear force and the size of the nucleus.

The range of the nuclear force is set by the pion Compton wavelength — the distance
over which the pion-mediated attraction extends:

The pion range r_pi equals hbar-c divided by the pion mass, approximately 1.41 fm.

r_pi = hbar*c / m_pi = 1.41 fm

The nuclear size scale is r_0 = 1.2 fm, the radius parameter in the nuclear density
profile.

A nucleon sitting at the surface is missing neighbors on one side. The fraction of
its binding that is lost is proportional to how far the nuclear force reaches beyond
the geometrical surface — that is, proportional to r_pi / r_0. This gives:

a_S = a_V times r_pi divided by r_0.

a_S = a_V x r_pi / r_0 = 15.835 x 1.414 / 1.2 = 18.66 MeV

The observed value is 18.33 MeV. The DFC structural estimate is 1.8% high — a T3
result with no free parameters beyond the already-established a_V, m_pi, and r_0.

---

## Pairing Energy: Cooper Pairs from Color

The pairing term in the SEMF gives a small binding bonus to nuclei with even numbers
of protons and even numbers of neutrons, and a penalty to odd-odd nuclei. It arises
from the same physics as Cooper pairing in superconductors: time-reversed pairs of
fermions at the Fermi surface can lower their energy by forming a correlated pair.

In conventional nuclear physics, the pairing gap is typically fit to about 12 MeV
divided by the square root of the mass number. The energy scale — 12 MeV — has
no standard derivation from QCD.

In DFC, the pairing interaction between nucleons is mediated by the residual D7
(color) interaction. The pairing energy scale is set by the pion decay constant
f_pi — the fundamental chiral symmetry breaking scale at D7 depth. The
suppression factor counts the number of gluon exchange channels available:

The pairing coefficient equals f_pi divided by the number of gluon modes,
which is N_c squared minus one.

a_pair = f_pi / (N_c^2 - 1) = 96.9 / 8 = 12.12 MeV

The observed value is 12.0 MeV. The DFC prediction is 1.0% high — a T3 structural
result.

The physics is straightforward: f_pi sets the energy scale of the strongest
residual interaction between color-neutral nucleons. The factor of 8 = N_c^2 - 1
counts the number of SU(3) generators (gluon modes). Only one linear combination
of these modes contributes to the color-singlet pairing channel, diluting the
interaction by a factor of 8.

---

## Where We Stand

After Cycle 369, the DFC SEMF coefficient status is:

| Coefficient | DFC value (MeV) | Observed (MeV) | Error | Tier | Source |
|---|---|---|---|---|---|
| a_V | 15.835 | 15.835 | by construction | T3 | Walecka curve |
| a_S | 18.66 | 18.33 | +1.8% | T3 | r_pi/r_0 ratio |
| a_C | 0.720 | 0.714 | +0.9% | T3 | DFC alpha_em |
| a_A | 24.67 | 23.20 | +6.3% | T3 | 2 x T_kin |
| a_pair | 12.12 | 12.0 | +1.0% | T3 | f_pi/(N_c^2-1) |

All five SEMF coefficients now have DFC structural accounts at T3 or better. The
nuclear binding energy formula — the single most important equation in nuclear
physics — is fully covered.

### Update: Omega Coupling and Sigma Mass Pinned

The KSRF (Kawarabayashi-Suzuki-Riazuddin-Fayyazuddin) relation connects the
omega-nucleon coupling to the pion decay constant and the omega mass:

The omega coupling equals the square root of the number of colors, times the
omega mass, divided by the square root of two times the pion decay constant.

g_omega = sqrt(N_c) * m_omega / (sqrt(2) * f_pi)

Substituting the three DFC-derived quantities — m_omega = sqrt(2 pi) Lambda_QCD,
M_N = sqrt(3 pi) Lambda_QCD, and f_pi = Lambda_QCD / pi — produces an algebraic
identity: the Lambda_QCD factors cancel exactly, and the result simplifies to
pi times the square root of three pi. This is the same expression as the sigma
coupling g_sigma = M_N / f_pi from the linear sigma model.

g_omega = g_sigma = pi * sqrt(3*pi) = 9.645

This is not an approximation. It is a T1 algebraic consequence of DFC's mass
relations: the omega mass, the nucleon mass, and the pion decay constant all
share a common Lambda_QCD factor that cancels in the KSRF ratio.

With g_omega = g_sigma, the saturation curve from the previous section is pinned
at a single point. The sigma mass follows uniquely:

m_sigma = 648 MeV

The scalar and vector potentials at saturation density are 272 MeV (attractive)
and 196 MeV (repulsive) — each individually large, with the small difference
producing the observed 16 MeV/A binding. This is nuclear saturation in action.

### What remains open (T4)

- **Shell corrections.** The magic numbers require the nuclear spin-orbit coupling,
  which is partially addressed (Module 25 covers N=126).
- **r_0 from DFC.** The nuclear radius parameter 1.2 fm enters a_S and a_C as an
  empirical input — it is not yet derived from D7 dynamics.

---

**See also:** `equations/nuclear_saturation_dfc.py` (C369, 16/16 PASS),
`equations/nuclear_omega_coupling_dfc.py` (C370, 14/14 PASS),
`equations/nuclear_volume_term.py` (C343), `equations/nuclear_dfc_params.py` (C342),
Module 20 (Nuclear Physics), Module 25 (N=126 Shell Closure).
