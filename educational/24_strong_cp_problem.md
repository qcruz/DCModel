# Module 24 — The Strong CP Problem: Why QCD Conserves CP Without an Axion

**Series:** DFC Educational Modules. Recommended reading: Module 04 (Forces),
Module 10 (Cascade Uniqueness), Module 05 (Particles).

**Status:** theta = 0 is Tier 2a (S⁵ CP isometry verified numerically; real amplitude
preservation theorem proved). arg(det M_q) = 0 is Tier 2a. No axion prediction is
Tier 2a (Criterion B — DFC makes a statement the Standard Model cannot).

---

## The Puzzle

The strong nuclear force has a mysterious property: it conserves CP symmetry —
the combined symmetry of charge conjugation (swapping particles for antiparticles)
and parity (reflecting spatial coordinates) — to extraordinary precision. Experiments
constrain any CP violation in the strong force to less than one part in ten billion.

This is surprising because nothing in the Standard Model requires it. The QCD
Lagrangian contains a term — the "theta term" — that would violate CP for any
nonzero value of the vacuum angle theta. This angle is a free parameter: it could
be anything from zero to two pi. The experimental constraint forces
|theta| < 5 × 10⁻¹¹. Why is theta so absurdly close to zero?

This is the **strong CP problem**, and it has been one of the major open questions
in particle physics since the late 1970s.

---

## The Standard Solution: Axions

The most popular resolution was proposed by Peccei and Quinn in 1977. They
introduced a new symmetry (PQ symmetry) that promotes theta from a fixed parameter
to a dynamical field. The potential of this field has a minimum at theta = 0, so the
system naturally relaxes to the CP-conserving value.

The particle associated with this new field is the **axion** — a very light, very
weakly interacting boson. Axions are also a dark matter candidate. Experiments like
ADMX, ABRACADABRA, CASPEr, and HAYSTAC are actively searching for axions. As of
2025, none has been found.

The axion mechanism works, but it raises new questions: why should PQ symmetry exist?
Why should there be a new undiscovered particle to solve a fine-tuning problem?

---

## The DFC Explanation: Theta = 0 by Topology

DFC resolves the strong CP problem without introducing any new symmetry or particle.
The argument has three parts.

### Part 1: The D7 Closure Lives on S⁵

In DFC, the strong force (SU(3) color) emerges as the third closure behavior of the
substrate, at D7 compression depth (see Module 04). The D7 closure configuration is
constrained to S⁵ — the unit sphere in three-dimensional complex space (ℂ³),
a five-real-parameter manifold defined by the closure topology. The condition defining S⁵ is simply that the squared magnitudes
of three complex coordinates sum to one.

The gauge group SU(3) arises as the isometry group of this sphere — the set of
transformations that preserve both the sphere condition and the complex structure
of ℂ³ (see Module 10 for why n = 3 uniquely).

### Part 2: CP Is a Built-In Symmetry of S⁵

The CP transformation on ℂ³ acts as complex conjugation: it sends each complex
coordinate to its conjugate. The key observation is immediate: complex conjugation
preserves the sphere condition, because the modulus of any complex number equals
the modulus of its conjugate. So CP maps S⁵ to itself — it is an exact symmetry
of the D7 closure manifold.

This means the D7 topology cannot distinguish a configuration from its
CP-conjugate. There is no geometrically distinguished direction on S⁵ that
breaks CP.

### Part 3: The D7 Closure Nucleates at the CP-Symmetric Fixed Point

The D7 closure is the *first* occurrence of SU(3) structure in the substrate.
Before it forms, there is no color field, no instanton vacuum, no theta angle.
The theta angle comes into existence at the moment the D7 closure nucleates.

At nucleation:
- No prior SU(3) structure exists — there is no theta to inherit.
- The formation is governed by the S⁵ topology, which is CP-symmetric.
- The CP transformation acts on theta as theta → −theta.
- The unique CP-symmetric fixed point is **theta = 0**.

The D7 closure is locked to theta = 0 by the geometry of its own formation.
This is not fine-tuning — it is topological necessity.

A second, more formal argument strengthens this: the real amplitude preservation
theorem shows that V(|Φ|²) preserves real initial conditions exactly (by ODE
uniqueness). Since the substrate at D4 is real, and each subsequent depth
inherits real amplitudes from the previous one, the D7 amplitude is real
positive — which corresponds to theta = 0.

---

## Why Weak CP Violation Is Independent

The weak nuclear force (SU(2), at D6 depth) violates CP through the CKM phase —
a complex phase in the mixing matrix between quark mass eigenstates. This CP
violation is real and experimentally confirmed (delta_CP is approximately 1 radian).

How can the strong force conserve CP while the weak force violates it? In DFC,
the answer is structural: the D6 (SU(2)) and D7 (SU(3)) closures are independent
topological structures. The CKM phase lives in the D6 S³ closure; the theta angle
lives in the D7 S⁵ closure. They do not share phases.

The homotopy groups confirm this independence: the third homotopy group of S³
is the integers (allowing the rich CP structure of the weak force), while the
third homotopy group of S⁵ is Z₂ (a much simpler structure that blocks the
transfer of D6 phases to D7).

The Standard Model puzzle — why is the strong CP phase ten billion times smaller
than the weak CP phase? — dissolves: they are parameters of independent topological
structures, not two values of the same quantity.

---

## What About arg(det M_q)?

The physical theta parameter is actually theta-bar = theta_QCD + arg(det M_q),
where M_q is the quark mass matrix. Even if theta_QCD = 0, a nonzero phase in
the quark mass determinant could reintroduce CP violation.

DFC addresses this too. The D6/D7 overlap integral — which determines the quark
Yukawa couplings — has been computed explicitly. Because the Jackiw-Rebbi zero
modes at both D6 and D7 are real functions (sech profiles), and the Higgs VEV
is real and positive, all Yukawa couplings Y_ij are real and positive. Therefore
det(M_q) is real and positive, and arg(det M_q) = 0 exactly.

The full result: theta-bar = 0 + 0 = 0. Both contributions vanish independently.

---

## The Prediction: No Axion

If theta is zero by topology, the axion has no role to play. DFC predicts:

- **No axion exists.** There is no Peccei-Quinn symmetry and no axion field.
- **d_n = 0 exactly.** The neutron electric dipole moment is zero, not merely
  small. This is a Criterion B prediction: DFC makes a definitive statement that
  the Standard Model cannot.
- **All axion searches will return null results** in the QCD axion mass range.

This prediction is sharply falsifiable. Any future detection of an axion, or any
nonzero measurement of the neutron electric dipole moment at any precision, would
directly contradict the DFC strong CP argument. Upcoming experiments (nEDM@PSI,
TUCAN, SNS-nEDM) aim for sensitivity below 10⁻²⁸ e·cm.

---

## Summary

| Item | DFC prediction | Status |
|---|---|---|
| theta_QCD | 0 (exact, from S⁵ CP isometry) | Tier 2a |
| arg(det M_q) | 0 (exact, from real amplitude theorem) | Tier 2a |
| theta-bar | 0 (exact) | Tier 2a |
| Neutron EDM d_n | 0 (exact) | Tier 2a, Criterion B |
| Axion | Does not exist | Tier 2a, Criterion B |
| Weak/strong CP ratio | Explained by independent D6/D7 topologies | Tier 2a |

**What remains open:** A fully formal nucleation dynamics derivation showing that
the D7 formation saddle point is CP-symmetric would upgrade the structural argument
further. The instanton vacuum structure within DFC (what cancellation of opposite-winding
sectors means for the substrate) is not yet fully developed.

---

## See also

- `phenomena/particle_physics/strong_cp_problem.md` — full technical account
- `equations/strong_cp_theta.py` — S⁵ CP isometry verification
- `equations/arg_det_mq_zero.py` — arg(det M_q) = 0 chain
- `equations/interface_overlap_integral.py` — real amplitude theorem
- `equations/strong_cp_formation.py` — V(theta) from ChPT
- Module 04 (Forces) — how U(1), SU(2), SU(3) appear
- Module 10 (Cascade Uniqueness) — why n = 3
