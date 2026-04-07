# Phenomenon: Parity Violation

## One-Sentence Synthesis

> Parity violation — the weak force's exclusive coupling to left-handed fermions — is a
> structural consequence of the D6 SU(2) closure topology: the Jackiw-Rebbi zero mode
> bound to the kink background is inherently a left-handed Weyl spinor, so all matter
> arising from D6 closures with odd winding number inherits left-handed SU(2)_L coupling;
> right-handed fermions (SU(2)_R singlets) arise from a different mechanism and are
> not connected to the D6 SU(2) closure.

---

## Observation

The weak force violates parity (mirror symmetry) maximally.

**What parity means:** Under parity, the spatial coordinates invert: x → −x. Momentum
(a polar vector) changes sign: p → −p. Angular momentum (an axial vector) does not:
L = r × p → (−r) × (−p) = +L. Helicity (spin component along momentum) therefore
changes sign under parity: a left-handed particle (spin antiparallel to momentum) becomes
right-handed.

**The observation (Wu experiment, 1957):** In the beta decay Co-60 → Ni-60 + e⁻ + ν̄_e,
the emitted electrons preferentially travel opposite to the nuclear spin — the emission
pattern is not symmetric under spatial reflection. If parity were conserved, the mirror-image
experiment would give the same result; it does not.

**The pattern — maximal violation:**

- The W boson couples **only to left-handed** fermions (negative helicity for massless
  particles): left-handed quarks, left-handed leptons. Right-handed fermions have zero
  weak isospin charge.
- Neutrinos (at the massless limit) are exclusively left-handed. No right-handed neutrino
  has ever been observed coupling to the W or Z.
- The charged current interaction: j^μ_W ∝ ψ̄_L γ^μ ψ_L, where ψ_L = (1 − γ⁵)/2 · ψ.
  The factor (1 − γ⁵) projects onto the left-handed component.

**The Standard Model accounts for this** by defining SU(2)_L as acting only on left-handed
fermion doublets. Right-handed fermions are placed in SU(2)_L singlets — they carry no
SU(2) charge. The "L" subscript is not an explanation; it is a label for the observed fact.

The Standard Model has no explanation for *why* nature chose left-handed coupling. Parity
violation is an input assumption of the SM gauge structure, not a derived consequence.

---

## Standard Explanation

In the SM, quarks and leptons are assigned to representations of SU(2)_L:

```
Left-handed:   Q_L = (u_L, d_L),  L_L = (ν_L, e_L)  [SU(2)_L doublets, T₃ = ±1/2]
Right-handed:  u_R, d_R, e_R                           [SU(2)_L singlets, T₃ = 0]
```

The gauge boson W couples only through the doublet representation — so only left-handed
particles participate in charged weak interactions. This is a postulate, not a derivation.

Why SU(2)_L and not SU(2)_R? The SM is silent on this. A parity-symmetric theory
would require SU(2)_L × SU(2)_R (the Pati-Salam / left-right symmetric model), with
a second set of heavy W_R bosons. No W_R has been observed; the current experimental
bound is M(W_R) > 6 TeV. The SM discards SU(2)_R as absent from nature — again without
a reason why.

The violation is related to the CKM matrix and CP violation (the CKM phase generates
both CP violation and parity asymmetry in decays), but the root cause — why the weak
interaction is chirally asymmetric at all — remains unexplained.

---

## Dimensional Folding Explanation

### The D6 Closure and Left-Handedness

In DFC, the weak force arises from the D6 SU(2) closure topology. The key physical
mechanism is the **Jackiw-Rebbi zero mode** (see `phenomena/quantum/spin.md`): a
topological kink background at D6 binds a fermionic zero mode — the matter field — to
the kink center.

The Jackiw-Rebbi zero mode is the solution to:

```
D̸ψ_0 = (∂_x + M φ_kink(x)) ψ_0 = 0
```

In 1+1 dimensions, this zero mode has a definite chirality — it is a left-handed Weyl
spinor. Extending to 3+1 dimensions: the zero mode of the Dirac operator in the kink
background is a left-handed Weyl fermion.

**Why left-handed?** The kink background φ_kink = φ₀ tanh(x/λ) breaks the spatial
reflection symmetry x → −x (the kink is not mirror-symmetric — it goes from −φ₀ on
one side to +φ₀ on the other). The zero mode inherits this asymmetry. For the kink
oriented with positive winding (N=+1), the zero mode is left-handed. For N=−1, the
zero mode is right-handed.

The electron is a kink with N=+1 winding. Its SU(2) coupling is left-handed by
construction — it is the chirality of the N=+1 Jackiw-Rebbi zero mode, not a postulate.

### Why SU(2)_L, Not SU(2)_R

The D6 SU(2) closure is the gauge structure of the kink's internal topology. The kink
(N=+1) nucleates with a definite orientation — its zero mode is left-handed. If the
kink had N=−1 (antifermion), the zero mode would be right-handed, and the coupling
would be SU(2)_R.

In the DFC picture:
```
N = +1 kink (electron, quarks, neutrinos):  left-handed zero mode  →  SU(2)_L coupling
N = −1 kink (positron, antiquarks):         right-handed zero mode  →  SU(2)_R coupling
```

But SU(2)_R is not the gauge group at D6 — it would be the gauge group of the N=−1
sector. The observed world is built predominantly from N=+1 matter (matter dominates
over antimatter — see `phenomena/cosmology/baryogenesis.md`), so the dominant coupling
is SU(2)_L.

**The asymmetry is not put in by hand.** The kink orientation (N=+1 vs N=−1) determines
the chirality. The observed parity violation of the weak force follows from the fact
that we live in a matter-dominated universe where N=+1 kinks are the building blocks.

### Right-Handed Fermions

Right-handed fermions (e_R, u_R, d_R) are observed — they carry electric charge and
strong charge. Why do they not couple to SU(2)?

In DFC, right-handed fermions are **not** the zero modes of D6 SU(2) kinks. They are:

1. **Excitations of D5 or D7 kinks:** The right-handed electron could be a localized
   mode of the D5 U(1) closure — not bound to an SU(2) kink at all. It would then
   carry U(1) charge (electric charge from D5) but no SU(2) charge.

2. **N=−1 sector modes:** Right-handed fermions could be the N=−1 zero modes, which
   exist but are the antiparticle sector. The positron is right-handed (it is the N=−1
   mode); the electron is left-handed (N=+1). The W only couples to one sector.

The precise mechanism for right-handed fermions is an **open question** in DFC — see
Open Questions below. What DFC can say: the left-handedness of the weak force follows
structurally from the kink topology; right-handed fermions do not arise from the same
mechanism, which is consistent with their absence from SU(2) coupling.

### The Absence of W_R

The non-observation of a W_R boson (right-handed W) is natural in DFC. A W_R would
require a separate SU(2)_R gauge closure at some depth. In the product topology
(U(1) × SU(2) × SU(3)), there is exactly one SU(2) closure — at D6 depth. The substrate
does not produce a second SU(2) at a different depth. A W_R boson would require a D6'
(a duplicate D6 closure), which the substrate's compression dynamics do not produce.

The experimental bound M(W_R) > 6 TeV is consistent with no D6' closure existing at
any scale up to 6 TeV. DFC predicts M(W_R) → ∞ (no W_R at any scale): there is no
mechanism to produce it, not just no observed production.

---

## Formal Equations

### The Chirality Projection

The left-handed projection of a Dirac spinor:

```
ψ_L = P_L ψ = (1 − γ⁵)/2 · ψ

where γ⁵ = iγ⁰γ¹γ²γ³  (in 3+1D, eigenvalues ±1)

Left-handed:   γ⁵ ψ_L = −ψ_L  (chirality = −1)
Right-handed:  γ⁵ ψ_R = +ψ_R  (chirality = +1)
```

The Jackiw-Rebbi zero mode in the D6 kink background satisfies:

```
γ⁵ ψ_JR = −ψ_JR    [for N=+1 kink]
```

This is a structural consequence of the kink orientation, not an assumption.

### The Weak Charged Current

The interaction vertex for the W boson with fermions:

```
L_cc = (g₂/√2) W^μ_+ ψ̄_L γ_μ ψ_L' + h.c.

     = (g₂/√2) W^μ_+ ψ̄ γ_μ (1−γ⁵)/2 ψ' + h.c.
```

In DFC: g₂ is the SU(2) coupling at D6; ψ_L is the Jackiw-Rebbi zero mode (inherently
left-handed); ψ_L' is the SU(2) partner in the doublet (e.g., ν_L pairs with e_L).

The (1−γ⁵)/2 projector is not imposed — it is the operator that selects the N=+1 sector
Jackiw-Rebbi mode from the full Dirac spinor.

### The V-A Structure

Parity violation in weak decay rates is measured by the degree of V-A (vector minus
axial vector) structure. For maximal parity violation:

```
V-A structure: j^μ = ψ̄ γ^μ (1 − γ⁵) ψ = 2 ψ̄_L γ^μ ψ_L

V+A (parity-conserving): ψ̄ γ^μ ψ  →  both helicities contribute equally
V-A (maximal violation): ψ̄ γ^μ (1−γ⁵) ψ  →  left-handed only
```

The Wu experiment measures the degree of V-A. The observed maximum parity violation
corresponds to a pure (1−γ⁵) coupling — exactly what the Jackiw-Rebbi left-handed
zero mode produces.

---

## Consistency Checks

| Property | DFC mechanism | Status |
|---|---|---|
| W couples only to left-handed fermions | Jackiw-Rebbi N=+1 zero mode is left-handed | Structural ✓ |
| V-A structure (maximal parity violation) | Pure left-handed zero mode → pure (1−γ⁵) | Structural ✓ |
| No W_R observed (M > 6 TeV) | No D6' duplicate closure in product topology | Structural ✓ |
| Right-handed fermions carry electric/color charge | U(1)/SU(3) coupling independent of D6 | Structural ✓ |
| Neutrinos are left-handed | Zero mode chirality = left-handed for N=+1 | Structural ✓ |
| Chirality explanation has no free parameters | Follows from kink topology, not postulated | Structural ✓ |
| Precise form of (1−γ⁵): from DFC derivation | Zero mode satisfies γ⁵ψ_JR = −ψ_JR exactly | OPEN — 3+1D extension needed ✗ |
| Right-handed fermion mechanism | D5 or D7 excitation vs. N=−1 sector | OPEN ✗ |
| CKM phase from D6-D7 boundary angles | Fold orientation angles between generations | OPEN ✗ |

---

## Open Questions

1. **Derive the chirality of the Jackiw-Rebbi zero mode in 3+1D.** The 1+1D argument
   (γ⁵ψ_JR = −ψ_JR for N=+1) is structural. The full 3+1D DFC substrate has three apparent
   spatial DOFs from D3 localization. The zero mode calculation must be extended to 3+1D
   to confirm that the chirality assignment is preserved in the full substrate, not just the
   1+1D kink model. This requires the same extension needed in Open Question 1 of
   `phenomena/quantum/spin.md`.

2. **Identify the right-handed fermion mechanism.** Right-handed fermions (e_R, u_R, d_R)
   are observed with electric and color charge. They do not have SU(2) charge. Two
   candidates: (a) localized modes of D5 U(1) kinks (no D6 winding → no SU(2) charge);
   (b) N=−1 D6 kink modes (the antifermion sector modes, which are right-handed). These
   give different predictions for right-handed neutrinos: mechanism (a) predicts no ν_R
   at any scale; mechanism (b) predicts ν_R at D6 with right-handed SU(2) coupling at
   the closure scale.

3. **Derive the CKM quark mixing angles.** The CKM matrix entries (θ₁₂, θ₁₃, θ₂₃, δ_CP)
   encode the mixing between quark generations. In DFC, generations arise from the SU(3)
   fiber topology at D7 (`foundations/three_generations.md`), and the CKM angles should
   correspond to the fold orientation angles between different generation modes at the
   D6–D7 boundary. Computing these from the D7 kink geometry would yield quantitative
   CKM predictions — a high-value target for Bottleneck 2.

4. **The seesaw mechanism and neutrino masses.** The observed smallness of neutrino masses
   (< 0.1 eV) suggests either (a) right-handed neutrinos with very large Majorana masses
   (seesaw mechanism), or (b) a different mechanism. In DFC, if ν_R does not arise from
   a D6 kink (mechanism (a) for right-handed fermions above), the seesaw is not available.
   An alternative DFC mechanism for neutrino mass suppression — perhaps from the very
   small D6–D7 coupling leaking — has not been derived.

---

## Connections

- **Spin and chirality** — Jackiw-Rebbi zero mode, N=+1 → left-handed:
  `phenomena/quantum/spin.md`
- **Weak force** — D6 SU(2) closure, W/Z boson masses:
  `phenomena/particle_physics/forces/weak_force.md`
- **Three generations** — SU(3) fundamental rep, generation mixing (CKM source):
  `foundations/three_generations.md`
- **Baryogenesis** — matter dominance (N=+1 over N=−1) determines observed chirality:
  `phenomena/cosmology/baryogenesis.md`
- **Neutrinos** — left-handed neutrinos, mass spectrum, ν_R question:
  `phenomena/particle_physics/particles/neutrinos.md`
- **Spin zero mode equations** — Jackiw-Rebbi calculation, winding number, zero mode:
  `equations/spin_zero_mode.py`
- **CP violation** — CKM phase from D6–D7 boundary angles:
  `phenomena/particle_physics/cp_violation.md`
- **Depth assignment** — why D6 = SU(2)_L (left-handed), not SU(2)_R:
  `foundations/depth_assignment.md`
