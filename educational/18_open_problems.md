# Module 18 — Open Problems: What DFC Does Not Yet Explain

**Audience:** This module assumes you have read the preceding modules. It is a summary
of what remains unresolved — written honestly, without softening the gaps.

**Purpose:** Every physical theory has boundaries. The value of a theory is partly
in what it explains and partly in how clearly it locates what it does not explain.
This module maps the open problems in DFC, organized by how far the model has gotten
toward each one.

---

## Two Kinds of Open Problems

Not all open problems are alike. Some have a structural argument in place — a plausible
mechanism that points in the right direction, though the formal derivation is missing.
Others have no current account at all: the model simply has not reached them.

Throughout this module, we use the DFC tier system introduced in Module 08:
- **T2a**: a numerically consistent structural argument exists
- **T3**: a plausible structural story, but not numerically confirmed
- **T4**: no current account — the gap is genuine

A T3 problem is close; a T4 problem requires new structural insight.

---

## Category 1 — Mass Scale

**The electron mass (T4)**

DFC can predict *ratios* of lepton masses. The muon-to-electron mass ratio of 206.77
is derived from the depth structure with no free parameters. The tau mass follows from
the Koide relation at +0.006% error. But the actual value of the electron mass —
0.511 million electron volts — is not derived. It requires knowing the absolute scale
of the compression field, which in turn requires connecting the compression parameter α
to the Planck scale in a way that has not yet been done rigorously.

This is the most fundamental open mass problem. All particle masses ultimately multiply
the electron mass by depth ratios; if the electron mass is not derived, neither are the
absolute masses of quarks, the W and Z bosons, or the Higgs.

**The neutrino mass scale (T3)**

DFC gives a structural argument for why neutrinos are much lighter than other fermions:
they acquire mass through a depth correction from the D7 confinement dynamics, rather
than through the direct D4 inertia mechanism. The predicted correction gives a mass ratio
m₃/m₂ = 5.33, compared to the observed 5.81 — an 8.3% error. This is T2b (a real
prediction that is close but outside the T2a threshold). What remains missing is a
formal derivation of the depth correction formula from the substrate dynamics.

---

## Category 2 — Quantum Mechanics

**The Born rule (T2a — closed)**

As described in Module 17, the quantum wave function is identified with the slow
envelope of a kink's fast internal oscillation. This explains why quantum mechanics
has complex numbers and the Schrödinger equation. It also now explains why the
probability of finding a particle at a given location is the *square* of the wave
function amplitude rather than the amplitude itself — the Born rule is established at T2a.

The derivation proceeds from V(φ) alone in two steps. First, the slow-envelope derivation
gives the Schrödinger equation (the Compton frequency satisfies ω_c² = 2α exactly, so the
fast-oscillation terms cancel identically), and the time-averaged energy density satisfies
⟨ε(x)⟩ ∝ |ψ(x)|² exactly — energy density is proportional to the square of the wave
function (T2a, `equations/born_rule_schrodinger.py`). Second, V(φ)'s Z₂ symmetry —
V(−φ) = V(φ) — forbids all odd coupling powers. Time-averaging then selects ⟨σ²⟩ as the
unique leading non-zero coupling, giving a localization rate ∝ |ψ(x)|². The alternative σ⁴
coupling is ruled out by interference fringe shape (it would produce cos⁴ fringes, not the
observed cos²) and suppressed by a factor of 10⁻⁶ at atomic energies. The complete chain
V(φ)→Schrödinger→⟨ε⟩∝|ψ|²→rate∝|ψ|² is now T2a (see `equations/born_rule_frequency_selection.py`).

**The collapse mechanism (T3)**

Module 17 identifies measurement as a D3 localization event — an interaction that forces
the substrate field to commit to a particular location. The structural picture is
consistent, but the specific dynamics by which this happens — the speed of the
transition, the role of entanglement with the measuring apparatus, the threshold for
when an interaction is "sufficient" — are not derived from the field equation.

---

## Category 3 — Cosmology

**The cosmological constant (T4)**

The observed dark energy density — the energy per cubic meter of empty space driving
the accelerating expansion of the universe — is roughly 10¹²³ times smaller than the
naive expectation from the Planck scale. This enormous discrepancy is the cosmological
constant problem, one of the largest unresolved puzzles in fundamental physics.

DFC reframes the problem: the observed dark energy density is the substrate's energy
density at cosmic compression depth (the D1–D3 shallow regime), not a sum of virtual
particle modes. The two scales — deep compression (kink energy, Planck scale) and
shallow compression (cosmic scale) — refer to different depth behaviors of the same
object and need not cancel. But DFC has no current derivation of *why* the cosmic
compression energy is as small as it is. The reframing is structural (T3); the
quantitative prediction is T4.

**Dark matter abundance (T4)**

Module 15 describes the DFC dark matter candidate — a closure that anchors through D4
(acquiring inertia) but not through D5 (no electromagnetic charge). This gives a
structurally natural account of what dark matter is. What DFC cannot yet explain is
*why* the ratio of dark matter to ordinary matter in the universe is approximately
five to one. The production mechanism — how D4-depth closures were generated in the
early universe — is an open problem, and the cosmological abundance is T4.

---

## Category 4 — Force Structure

**The electromagnetic coupling at zero energy (T4)**

DFC derives the gauge coupling at the unification scale from the substrate's compression
topology: 1/α_em = 36π at the D5 closure threshold. Running this down to laboratory
energies gives 1/α_em(0) ≈ 137.04, with a 0.044% error using standard model inputs
for the running. The deeper structural identity connecting the running of α_em to DFC
parameters — the algebraic reason the number 137 emerges — is an open problem (T4).
Closing it would require deriving the hadronic contribution to the running of α_em from
the D7 confinement dynamics alone, without experimental input.

**Newton's constant from the field equation (T3)**

DFC identifies gravity as a consequence of compression gradient fields — the tendency
of the substrate to relieve local compression by redistributing into neighboring
configurations. The Planck scale is set by the kink width, which is approximately one
Planck length (a T2a result from the compression self-consistency condition). But the
precise formula G_N = 1/φ₀² — connecting Newton's constant to the field vacuum value —
has not been derived at better than a T3 structural argument. A rigorous derivation
would require showing that the DFC substrate dynamics produces an effective action
equivalent to the Einstein-Hilbert action at low energies.

**The cascade termination (T3)**

DFC produces gauge closure behaviors at depths D5, D6, and D7, corresponding to U(1),
SU(2), and SU(3). The natural question is: why does the cascade stop at D7? Why is
there no D8 or D9 gauge group?

The structural argument is confinement: the D7 SU(3) dynamics produce a mass gap —
a minimum energy for all excitations — which freezes out further bifurcation. No
free color charges exist to seed deeper closures. This argument is T3. Making it
rigorous is equivalent to the Yang-Mills mass gap problem, which the DFC framework
addresses as a separate research track.

---

## Category 5 — Formal Foundations

**D-depth assignments from the field equation (T2a)**

The identifications D5=U(1), D6=SU(2), D7=SU(3) are derived from the compression
cascade in the following sense: the cascade S¹→S³→S⁵ is forced by V(|Φ|) having
U(n) symmetry, and the self-consistency condition C₂(fund, SU(n)) = I₄ uniquely
selects n=3. This chain is T2a (numerically consistent, with the cascade mechanism
formally proved at T1+cited). What remains T2a rather than T1 is the identification
of depth labels with physical gauge groups: the assignment D5↔n=1, D6↔n=2, D7↔n=3
is a naming convention — it matches the physics, but the dynamics that places the
closures at these specific compression depths (rather than any others) has not been
derived from V(φ) alone.

---

## What Progress Would Look Like

For each open problem, there is a specific kind of progress that would close it:

| Problem | What would close it |
|---|---|
| Electron mass (T4) | Derive α (Planck units) → m_e from substrate + Planck scale identification |
| Born rule (**T2a — closed**) | V(φ) Z₂ symmetry + σ² uniqueness — Step 6 closed at T2a |
| Cosmological constant (T4) | Derive D1–D3 cosmic compression energy density from V(φ) |
| Dark matter abundance (T4) | Derive D4-depth closure production rate in early substrate |
| α_em(0) identity (T4) | Derive hadronic VP contribution from D7 confinement dynamics |
| Neutrino hierarchy (T2b) | Formal derivation of depth correction δd=1/(6π) from V(φ) |
| G_N from V(φ) (T3) | Derive Einstein-Hilbert action as low-energy limit of substrate dynamics |
| Cascade termination (T3) | Formal proof that D7 mass gap prevents D8 closures |

---

## Summary

DFC explains a remarkable range of physics from a single starting point — one
self-compressing field and one potential. But honesty requires acknowledging what it
does not yet explain. The T4 problems above are genuine open problems, not gaps that
can be closed by a brief calculation. They require either new structural insight or
a formal derivation of substantially greater depth than anything yet completed.

The T3 problems have plausible structural accounts but lack rigor. Each is a concrete
research target.

The T2b result (neutrino mass ratio) is a prediction that is close but not confirmed
at the T2a level. It may be resolvable with a more careful calculation.

What the model has: verified coupling constants, particle mass ratios, Hubble constant,
absolute proton stability, spin-1/2 from topology, and three generations from the
cascade uniqueness theorem. What it lacks: absolute mass scales, quantum foundations,
and cosmological abundances.

---

**Previous:** [Module 17 — Quantum Mechanics: Measurement from Fold Topology](17_quantum_mechanics.md)

**See also:**
- `ISSUES.md` — full tracker of open problems with equations and file references
- `foundations/scientific_merit.md` — tier system and completeness milestones
- `phenomena/cosmology/dark_matter.md` — dark matter account in detail
- `equations/` — runnable modules for all verified predictions
