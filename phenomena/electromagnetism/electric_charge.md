# Phenomenon: Electric Charge

## One-Sentence Synthesis

> Electric charge is the topological winding number of a particle's U(1) closure at D5 —
> an integer count of how many times the fold orientation angle θ wraps around the U(1)
> circle — which is why charge is quantized, exactly conserved, and why antiparticles
> carry the opposite sign.

---

## Observation

Electric charge is quantized in integer multiples of e = 1.602 × 10⁻¹⁹ C for leptons,
or e/3 for quarks. Charge is exactly conserved in every known interaction — no process
has ever created or destroyed net charge. The proton and electron charges are equal and
opposite to better than one part in 10²¹. Antiparticles carry exactly the opposite charge
of their partners.

---

## Standard Explanation

U(1) gauge symmetry. Representations of U(1) are labeled by integers → charge quantized.
Charge conservation is Noether's theorem applied to the global U(1) symmetry. The equality
|q_proton| = |q_electron| requires anomaly cancellation — the sum of all charges in each
generation must satisfy certain consistency conditions for the quantum theory to be
self-consistent. The Standard Model takes e as a measured input; it does not predict its
value.

---

## Dimensional Folding Explanation

### What Charge Is

Electric charge is the **winding number** of the D5 U(1) closure.

Recall that the D5 closure creates a U(1) topology — the fold orientation angle θ wraps
around a circle. For an extended matter field ψ = |ψ| e^{iθ}, the winding number n counts
how many complete revolutions θ makes as you trace a closed path encircling the particle:

```
n = (1/2π) ∮ dθ = (1/2π) ∮ ∂_i θ dx^i
```

This integer n is the electric charge (in units of e). A particle with n = 1 is a unit
positive charge. n = −1 is a unit negative charge (antiparticle). n = 0 is electrically
neutral.

### Why Charge Is Quantized

Winding numbers are integers by definition — there is no such thing as a non-integer
number of complete revolutions. You cannot have a field that wraps 1.7 times around the
circle: it either wraps once (n=1) or twice (n=2) or not at all (n=0). The quantization
is topological, not dynamical.

This is sharper than the standard "representations of U(1) are labeled by integers"
statement. It is not that we choose to label representations with integers — it is that
the winding number of a physical fold orientation around a physical circle can only be
an integer. Fractional charge would require fractional winding, which is topologically
forbidden for a single closed path.

### Why Charge Is Exactly Conserved

Winding numbers cannot change continuously. To change n from 1 to 0 would require the
fold orientation to "unwrap" — which requires the magnitude |ψ| to pass through zero at
every point on the encircling path simultaneously. This is a discontinuous, high-energy
event (a topological transition), not something that occurs through ordinary smooth field
evolution.

In the absence of a topological transition:
```
∂_t n = 0     [topological conservation of winding number]
```

This is exact — not approximate, not suppressed by any coupling constant, not dependent
on any symmetry being unbroken. It is the same reason you cannot continuously deform a
loop that winds twice around a pole into one that winds once without cutting it.

Charge conservation in electromagnetism is not the result of a symmetry that might be
broken. It is the result of winding numbers being topologically stable.

In field theory language, this corresponds to the conserved current:
```
J^μ = (e/2πi)(ψ* D^μ ψ − ψ (D^μ ψ)*)     [Noether current of U(1) symmetry]
∂_μ J^μ = 0                                  [conservation law]
```

### Antiparticles Have Opposite Charge

An antiparticle is a closure with opposite winding direction: where the particle has
θ winding counterclockwise (n = +1), the antiparticle winds clockwise (n = −1). The two
exactly cancel:

```
n_particle + n_antiparticle = +1 + (−1) = 0
```

Particle-antiparticle annihilation is the unwinding of opposite-winding closures. The
result (n = 0) is consistent with photons, which carry no D5 winding (they are the gauge
field A_μ, not a matter field ψ).

Pair creation is the reverse: a photon (n = 0) splits into two closures of opposite
winding, n = +1 and n = −1, consistent with total charge conservation.

---

## Formal Statement

### Winding Number as Topological Charge

For a U(1) matter field ψ(x) = |ψ(x)| e^{iθ(x)}, the winding number around a closed
surface S enclosing a particle is:

```
q = e × (1/2π) ∮_S ∇θ · dS
```

For a configuration where θ winds n times: q = ne.

The topological charge density can be written:
```
j^0 = e × ε^{ijk} ∂_i (θ ∂_j ∂_k θ) / (4π)
```

Integrating over all space gives the quantized total charge Q = ne.

### Charge-Current Conservation

The electromagnetic 4-current:
```
J^μ = (e/m) |ψ|² (∂^μ θ − eA^μ)     [probability current × charge]
```

is conserved: ∂_μ J^μ = 0. This follows from the field equation for ψ and is equivalent
to the statement that winding numbers do not change under smooth field evolution.

---

## The Fractional Charge Problem

Quarks carry charges of ±1/3 e and ±2/3 e — apparently fractional. This is the one
observation that is not immediately explained by the integer winding number picture.

**The resolution requires the D5/D7 consistency condition.**

Quarks reach D7 (SU(3), color charge) in addition to D5 (U(1), electric charge). The
SU(3) closure at D7 has a fundamental representation of dimension 3 — three colors. For
the composite (three-quark) system to be color-neutral and carry integer electric charge,
each individual quark must carry charge ±1/3 or ±2/3.

This is not a free choice. The consistency condition between the D5 and D7 closure
topologies — specifically, the requirement that all gauge anomalies cancel (which is the
quantum consistency of the theory) — forces quark charges to take values ±1/3, ±2/3
and lepton charges to be 0, −1.

The anomaly cancellation conditions for one generation are:
```
[SU(3)²·U(1)]:   2 × (2/3) + 1 × (−1/3) + 1 × (−1/3) = 0     [per color]
[U(1)³]:         3×(2/3)³ + 3×(−1/3)³ + 3×(−1/3)³ + (0)³ + (−1)³ = 0   ✓
[SU(2)²·U(1)]:   3×(1/6) + 3×(1/6) + (−1/2) + (−1/2) = 0     ✓
```

These conditions are satisfied exactly by the observed charge assignments — not by
accident, but because charge is defined by the D5 winding number and quarks must be
consistent with the D7 color structure.

**In DFC terms:** the fractional quark charges are not truly fractional winding numbers.
They are integer D5 windings viewed per color unit. Three colors sharing one unit of
D5 winding gives 1/3 per color. The full proton (three quarks, color-neutral) carries
integer charge 1 — one complete D5 winding. The "fractional" charges are a consequence
of looking at one component of a color-triplet system.

*This is currently a working interpretation consistent with the model, not a completed
derivation. The formal derivation requires working out the D5/D7 topology consistency
condition explicitly.*

### Proton-Electron Charge Equality

|q_proton| = |q_electron| to 1 part in 10²¹ is the most precise equality in physics.

In DFC: this follows from the anomaly cancellation argument above. The sum of quark
charges per generation is:
```
q_u + q_u + q_d = 2/3 + 2/3 − 1/3 = 1 = |q_electron|
```

This is not an empirical coincidence. It is the D5/D7 topological consistency condition:
the total D5 winding of all quarks in a generation must equal the D5 winding of the
paired lepton. Any departure would make the quantum gauge theory inconsistent
(anomalous), which in DFC means the D5 and D7 closures could not coexist stably.

*Deriving this from first principles in DFC — showing that the D5/D7 topology forces
anomaly-free charge assignments — is the key open derivation for this document.*

---

## What This Explains

| Observation | DFC mechanism |
|---|---|
| Charge quantized in units of e | Winding numbers are integers — topology |
| Charge exactly conserved | Winding numbers topologically stable under smooth evolution |
| Antiparticles have opposite charge | Opposite winding direction |
| Pair creation/annihilation conserves charge | n=0 photon → n=+1 + n=−1 or reverse |
| Neutral particles (neutrinos, neutron) | Zero net D5 winding number |
| Quark charges ±1/3, ±2/3 | D5/D7 consistency: integer winding shared across 3 colors |
| |q_p| = |q_e| to 10⁻²¹ | Anomaly cancellation = D5/D7 topological consistency |

---

## Connections to Other Phenomena

- **Electromagnetism** — A_μ is the connection forced by local θ symmetry; charge is
  the source of A_μ; `phenomena/electromagnetism/electromagnetism.md`
- **Quarks** — fractional charges from D5/D7 consistency; `phenomena/particle_physics/particles/quarks.md`
- **Electron** — unit charge, n = −1 at D5; `phenomena/particle_physics/particles/electron.md`
- **Antimatter** — opposite winding number; `phenomena/particle_physics/particles/antimatter.md`
- **Product geometry** — D5, D6, D7 independence; `foundations/product_geometry.md`
- **Proton stability** — why quark→lepton is forbidden (D7→D5 transition);
  `phenomena/particle_physics/proton_stability.md`

---

## Open Questions

1. **Formal derivation of D5/D7 consistency condition:** The argument that quarks carry
   fractional charge because of D5/D7 topological consistency is physically motivated
   but not yet formally derived within DFC. A complete derivation would show that the
   D5 and D7 closure topologies can coexist stably only when charge assignments satisfy
   the anomaly cancellation conditions — expressing this as a statement about winding
   numbers and closure geometry rather than as a quantum field theory calculation.

2. **Derive the value of e from D5 geometry:** The elementary charge e = 1.602 × 10⁻¹⁹ C
   sets the coupling strength between the matter field ψ and the gauge field A_μ. In DFC,
   e should be determined by the geometric properties of the U(1) closure at D5 — its
   winding density, compression scale, or coupling to the D3 localization layer. This
   is equivalent to deriving the fine structure constant α = e²/4πε₀ℏc ≈ 1/137.

3. **Why is charge the only absolutely conserved quantum number?** Baryon number and
   lepton number are approximately conserved but can in principle be violated (sphaleron
   processes, hypothetical proton decay). Electric charge appears to be absolutely
   conserved. In DFC, the distinction should follow from the topological robustness of
   the D5 U(1) winding relative to the D6/D7 winding numbers — U(1) is the simplest
   topology (a circle) and its winding is harder to unwind than SU(2) or SU(3).
