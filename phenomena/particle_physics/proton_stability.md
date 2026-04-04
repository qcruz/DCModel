# Phenomenon: The Proton Does Not Decay

## One-Sentence Synthesis

> The proton is absolutely stable — not approximately stable, not stable with a very
> long lifetime — because the product geometry U(1)×SU(2)×SU(3) consists of three
> independent closure topologies with no shared space between them, and without
> a shared space there is no carrier that can turn a quark into a lepton.

---

## Observation

Protons are extraordinarily stable. Super-Kamiokande — a 50,000-ton detector filled with
ultra-pure water, watched by 11,000 photomultiplier tubes — has been observing protons for
decades and has never seen one decay.

Current lower bound: τ_proton > 1.6 × 10³⁴ years for the channel p → π⁰ + e⁺.

The universe is 1.38 × 10¹⁰ years old. The proton's lifetime exceeds the age of the
universe by at least a factor of 10²⁴.

---

## Standard Explanation

The proton is the lightest baryon. If baryon number were not conserved, nothing in
principle prevents it from decaying into lighter particles — pions and positrons are
both available final states.

In the Standard Model, accidental symmetries (baryon number B and lepton number L)
forbid this decay at the renormalizable level, but higher-dimensional operators
suppressed by a large mass scale M can violate it. The Standard Model alone has no
deep reason why M should be large enough.

Grand Unified Theories make the situation explicit: in SU(5), there are gauge bosons
(X and Y, called leptoquarks) living in the coset SU(5)/(SU(3)×SU(2)×U(1)) that
mediate quark → lepton transitions. The predicted lifetime:

```
τ_SU(5) ~ M_X⁴ / m_proton⁵   with M_X ~ 10¹⁵ GeV
         ~ 10³⁰ years    [RULED OUT by Super-K in the 1980s]
```

More sophisticated versions push M_X higher, extending predictions to 10³⁴–10³⁶ years —
right at the experimental boundary. Every improvement by Super-K and Hyper-K cuts
further into available parameter space.

---

## Dimensional Folding Explanation

### Why This Model Predicts Absolute Stability

In the Dimensional Folding Model, the three gauge forces arise as independent closure
events at different compression depths:

```
D5:  U(1) closure  →  electromagnetism (couples to electric charge)
D6:  SU(2) closure →  weak force (couples to weak isospin)
D7:  SU(3) closure →  strong force (couples to color charge)
```

These are three separate buckling events. Each produces its own independent closure
topology. The gauge group of the model is the direct product:

```
G = U(1) × SU(2) × SU(3)
```

In a direct product group, every gauge boson belongs to exactly one factor.
A U(1) boson couples only to U(1) charge. An SU(3) gluon couples only to color.
**There is no gauge boson that simultaneously couples to both color charge (D7)
and lepton number (D5/D6)** — such a boson would require a representation that
mixes factors of the product, which does not exist in a product group.

In contrast, SU(5) contains the product group as a subgroup *plus* the coset
SU(5)/(SU(3)×SU(2)×U(1)). The X and Y bosons live in that coset. They exist
because the three sectors share a common larger space. In DFC, there is no common
larger space — the three closures are independent events at different depths with
no shared topology.

**The X and Y bosons are not heavy. They do not exist.**

This is not a matter of making their mass large enough to suppress the decay rate.
Asking how long a proton takes to decay via X-boson exchange is like asking how
long it takes to drive from New York to London. The mechanism does not exist;
the question does not apply.

---

### Perspective 1: From Particle Physics

Quark → lepton requires changing color charge (SU(3) quantum number) into lepton
number (U(1) quantum number). This requires a carrier that has both a color index
and a lepton number — i.e., a carrier that is simultaneously charged under both
SU(3) and U(1). In a product group, no such carrier exists.

The argument is exact and applies to all orders in perturbation theory: at no loop
order can a product-group interaction generate an effective vertex that mixes
color-charged and lepton-number-carrying legs.

### Perspective 2: From the Compression Field

At D7, the compression field has closed into the SU(3) topology. Quarks are
structures whose compression fold reaches depth D7 and carries SU(3) winding number
(color charge). Leptons are structures that close at D5 (U(1)) and D6 (SU(2)) but
do not reach D7.

A quark-to-lepton transition would require a carrier that bridges D7 (SU(3) closure)
to D5 (U(1) closure) — a topological transition between two independent closure
depths. There is no such carrier in the compression field spectrum, because the two
closures formed independently at different depths with no shared topological structure.

---

## Formal Equations

### Why Gauge-Mediated Decay Rate is Exactly Zero

For a gauge-mediated dimension-6 proton decay operator (e.g., from X-boson exchange):

```
Γ_gauge ~ g_X⁴ / M_X⁴ × m_proton⁵

where g_X = coupling of X to quarks and leptons
      M_X = X-boson mass
```

In DFC: g_X = 0 exactly (no X boson couples to both color and lepton number),
regardless of M_X. Therefore:

```
Γ_gauge = 0    [exact structural zero, not suppression]
τ_gauge = ∞
```

This zero is protected by the product group structure to all orders in perturbation
theory — no loop diagram can generate a non-zero g_X because no intermediate state
exists that carries both SU(3) and U(1) quantum numbers simultaneously.

### Allowed Channel 1: Gravitational Operators

Gravity is not a gauge force of U(1)×SU(2)×SU(3). It couples to all energy equally,
and quantum gravitational effects can, in principle, violate global symmetries like
baryon number. The leading contribution comes from Planck-suppressed dimension-6
operators:

```
O_dim6 ~ (qqql) / M_Planck²

Γ_grav ~ m_proton⁵ / M_Planck⁴

τ_grav ~ M_Planck⁴ / m_proton⁵
       = (1.22 × 10¹⁹ GeV)⁴ / (0.938 GeV)⁵
       ≈ 5 × 10⁴⁴ years
```

This is the **dominant decay channel** in DFC — and it predicts a proton lifetime
10 orders of magnitude beyond current experimental reach.

### Allowed Channel 2: Electroweak Sphalerons

Sphaleron processes (topological transitions in the SU(2) sector) violate B+L but
preserve B−L. For proton decay p → π⁰ + e⁺:

```
ΔB = −1,  ΔL = −1  →  ΔB + ΔL = −2
```

Sphalerons change B and L by integer multiples of N_generations = 3, so the minimum
change is ΔB = ΔL = ±3 — incompatible with single-proton decay (ΔB = −1). At room
temperature, the sphaleron rate is additionally exponentially suppressed:

```
Γ_sph ~ exp(−E_sph / T)   with E_sph ~ 9 TeV
```

At T = 300 K ≈ 2.6 × 10⁻¹¹ GeV: exp(−E_sph/T) ~ exp(−3.5 × 10¹⁴) ≈ 0.
Sphalerons do not contribute to proton decay.

### Comparison Table

| Model | Decay mechanism | Predicted τ_proton | Status |
|---|---|---|---|
| Minimal SU(5) | X-boson (dim-6) | ~10³⁰ years | **Ruled out** |
| SUSY SU(5) | Dim-5 operators | ~10³⁴ years | Under pressure |
| SO(10) | X-boson variants | ~10³⁵–36 years | Constrained |
| Standard Model alone | Accidental symmetry | ~10³¹ years (soft) | Not observed |
| **DFC (this model)** | **None (gauge)** | **>10⁴⁴ years (grav. only)** | **Consistent** ✓ |

Current experimental limit: τ > 1.6 × 10³⁴ years (Super-K, p → π⁰e⁺)
DFC prediction: τ_grav ~ 5 × 10⁴⁴ years — **10 orders of magnitude above current reach**

See `equations/proton_stability.py` for numerical calculations.

---

## The Sharp Falsifiability

The DFC prediction is more than "consistent with" the experimental bound — the decay
mechanism is structurally absent. Every improvement in experimental sensitivity is
a consistency check, not a test that could ever confirm the prediction.

**What would falsify the model:**

1. **Any gauge-mediated decay observed** at a rate faster than ~10⁴⁴ years — this
   would require a carrier that mixes color and lepton number, which is impossible in
   a product group. This would be immediate, irrecoverable falsification.

2. **A decay rate in the range 10³⁴–10⁴⁴ years** — this is too slow for gauge
   operators but too fast for pure gravitational operators. It would suggest a new
   mechanism the model has not accounted for, requiring explanation.

3. **Proton decay observed at all** in any channel by Hyper-Kamiokande (which will
   improve sensitivity ~10× over Super-K) — any positive signal demands reconciliation
   with the product group argument.

**What would not falsify it:** A null result, no matter how sensitive the experiment.
Null results are consistent with the prediction but cannot confirm a structural zero.

---

## Baryogenesis Connection

If the proton is absolutely stable and sphalerons can only violate B+L (not B−L),
the baryon asymmetry of the universe must have been generated through B−L violation
at some early epoch. In DFC, this points to the D7 closure event itself — the
formation of the SU(3) closure topology may have produced a small asymmetry in
baryon vs. antibaryon winding numbers, which then became frozen as the closure
stabilized. This is an open question but the model provides a natural candidate:
the D7 buckling event as the origin of baryogenesis.

---

## Connections to Other Phenomena

- **Product geometry** — the structural source of absolute stability; three independent
  closure topologies with no shared space; `foundations/product_geometry.md`
- **Three generations** — the right-copy SU(3) at D7 gives three generations; the same
  D7 topology that forbids proton decay determines the generation count;
  `foundations/three_generations.md`
- **Higgs geometry** — the SU(2) closure at D6 is the S³ geometry; independent of
  SU(3), consistent with proton stability; `foundations/higgs_geometry.md`
- **Closure topology** — the formal description of independent closure events;
  `equations/closure_topology.py`
- **Proton stability equations** — all numerical calculations; `equations/proton_stability.py`

---

## Open Questions

1. **Gravitational operator coefficient:** The estimate τ_grav ~ M_Planck⁴/m_proton⁵
   uses a coefficient of order 1. The actual coefficient depends on the specific
   quantum gravitational mechanism at the Planck scale — in DFC, this should be
   calculable from the Planck-scale compression field dynamics (α, β at L_Pl). A more
   precise prediction would move τ_grav up or down by several orders of magnitude.

2. **Baryogenesis at D7 closure:** If B+L violation cannot produce a net baryon
   asymmetry (since sphalerons preserve B−L), the asymmetry must have been generated
   through a process that distinguishes baryons from antibaryons at the closure scale.
   The D7 buckling event is the natural candidate. Can an asymmetry in SU(3) winding
   numbers be generated during an irreversible closure event?

3. **Proton stability under quantum gravity:** The gravitational operator argument uses
   the effective field theory expansion in 1/M_Planck. At the Planck scale, the
   compression field is fully nonlinear and the EFT expansion breaks down. Whether
   the proton is truly stable to all quantum gravitational effects — or whether
   Planck-scale physics introduces additional decay channels — cannot be answered
   without the complete nonlinear DFC theory at the Planck scale.

4. **Neutron lifetime in DFC:** The neutron decays in ~15 minutes (n → p + e⁻ + ν̄_e)
   via weak interaction. This is gauge-mediated (SU(2) W-boson exchange) and is
   consistent with the product group — the W-boson couples within the D6 closure, not
   across closure boundaries. The DFC prediction for the neutron lifetime should match
   the Standard Model result exactly. Verifying this consistency is open.
