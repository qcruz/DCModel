# Phenomenon: The Electron

## One-Sentence Synthesis

> *Placeholder — to be completed when the DFC derivation of the electron's mass, charge, and spin is formalized.*

---

## Observation

The electron is the lightest stable charged particle. It has mass m_e = 0.511 MeV,
electric charge −e = −1.602 × 10⁻¹⁹ C, and spin 1/2. It does not decay. It carries
electromagnetic charge (couples to photons at D5) and weak isospin (couples to W/Z at D6),
but no color charge (does not reach D7). It is the carrier of electric current in matter.

---

## Standard Explanation

In the Standard Model the electron is a fundamental spin-1/2 fermion, a member of the
first generation lepton doublet with the electron neutrino. Its mass comes from a Yukawa
coupling to the Higgs field (coupling y_e ≈ 2.9 × 10⁻⁶). Its charge is the fundamental
unit of electromagnetic charge. The Standard Model gives no explanation for why y_e has
the value it does, or why the electron is the lightest charged lepton.

---

## Dimensional Folding Explanation

*Placeholder — DFC account to be developed.*

**Expected DFC account:** The electron is a stable closure that reaches D5 (U(1),
electromagnetic charge) and D6 (SU(2), weak isospin) but not D7 (no color charge). Its
mass arises from the depth-anchoring formula m(d) = m_ref × exp(κ·Δd) with κ_lepton ≈ 5.33.
Its stability follows from charge conservation at D5 (no lighter charged particle to decay
into). Its spin-1/2 follows from the SU(2) representation at D6.

**Key question this document must answer:** Can the electron mass (0.511 MeV) and Yukawa
coupling (y_e ≈ 2.9 × 10⁻⁶) be derived from the depth-anchoring parameters without
free-fitting?

---

## Formal Equations

*Placeholder — to be derived.*

```
m_e = 0.511 MeV    [observed]
y_e = m_e / v_Higgs = 0.511 MeV / 246 GeV ≈ 2.9 × 10⁻⁶    [Yukawa coupling]
```

DFC depth-anchoring prediction: see `equations/lepton_masses.py`

---

## Connections to Other Phenomena

- **Quantum mechanics** — electron is the canonical quantum particle; Schrödinger equation
  describes its slow-envelope dynamics; `phenomena/quantum/quantum_mechanics.md`
- **Electromagnetism** — electron is the source of the U(1) field; `phenomena/electromagnetism/electromagnetism.md`
- **Weak force** — electron participates in beta decay via D6 SU(2); `phenomena/particle_physics/forces/weak_force.md`
- **Mass generation** — Higgs coupling sets m_e; `phenomena/particle_physics/particles/higgs_boson.md`
- **Three generations** — electron is first-generation; `foundations/three_generations.md`
- **Neutrinos** — paired with electron neutrino in SU(2) doublet; `phenomena/particle_physics/particles/neutrinos.md`

---

## Open Questions

1. *Derive m_e from DFC depth-anchoring without free parameters*
2. *Explain why the electron Yukawa coupling is so small (y_e ~ 10⁻⁶)*
3. *Derive electron spin-1/2 from D6 SU(2) representation theory*
