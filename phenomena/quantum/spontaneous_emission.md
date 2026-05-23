# Phenomenon: Spontaneous Emission

## One-Sentence Synthesis

> Spontaneous emission is the process by which a D6 electron kink in an excited closure
> configuration relaxes to a lower-energy configuration, emitting a D5 U(1) photon whose
> frequency equals the closure energy gap divided by Planck's constant; the rate is
> controlled by α_em from the DFC β chain, and the Einstein A coefficient scales as α⁵
> when DFC atomic units are applied self-consistently — giving lifetimes 11.7% too long
> (Tier 2b, same α_em systematic as all EM predictions).

---

## Observation

An atom in an excited electronic state spontaneously emits a photon and drops to a
lower energy state, even in the absence of any external radiation. Key features:

- **Discrete frequencies:** photon energy exactly equals the energy difference between
  levels (Einstein 1917, verified to < 1 part in 10¹²).
- **Exponential decay:** excited population decays as N(t) = N₀ exp(−A t), with
  characteristic lifetime τ = 1/A independent of intensity.
- **A coefficient:** the spontaneous emission rate A is proportional to the cube of
  the transition frequency and to the square of the transition dipole moment.
- **Universality:** hydrogen A values range from ~10⁶ s⁻¹ (infrared) to ~10⁹ s⁻¹
  (UV), with lifetimes of nanoseconds to microseconds.

Representative H-atom lifetimes (NIST):

| Transition | λ (nm) | τ_obs (ns) |
|---|---|---|
| 2p→1s (Ly-α) | 121.6 | 1.60 |
| 3d→2p (Hα) | 656.3 | 15.5 |
| 4f→3d (Pa-α) | 1875 | 106 |

---

## Standard Explanation

Einstein (1917) introduced the A and B coefficients: the spontaneous emission rate
A₂₁ is the probability per unit time for an atom in state 2 to emit a photon and
transition to state 1.

In QED, the Einstein A coefficient for an electric dipole transition is:

The spontaneous emission rate equals four-thirds times the fine structure constant
times the cube of the transition frequency divided by the square of the speed of
light, times the square of the transition dipole matrix element:

```
A = (4α ω³ |r₁₂|²) / (3c²)
```

where α is the fine structure constant, ω the transition angular frequency, and
|r₁₂|² the square of the dipole matrix element averaged over initial magnetic
substates and summed over final substates.

---

## Dimensional Folding Explanation

### Photon Emission as D6 Kink Relaxation

In DFC, the electron is a D6 closure — a kink configuration in the substrate at D6
depths. Atomic energy levels correspond to different excited configurations of the
D6 kink, organized by the boundary condition at the nucleus (the Coulomb potential
well from the D7-depth proton structure).

When the D6 kink occupies an excited configuration (higher-n closure state), the
substrate compression at that depth has stored energy equal to the level spacing.
The kink relaxes to a lower configuration, and the stored energy propagates outward
as a D5 U(1) mode — a photon.

The coupling constant controlling this process is α_em, which is the square of the
D5 gauge coupling g_eff²/4π in appropriate units. In DFC, α_em is derived from
the substrate quartic coupling β = 1/(9π) through the chain:

```
β → g_eff² = 8/27 → α_em^{UV} → RGE running → α_em(m_e) = 1/140.1
```

This is the same coupling chain used in atomic_structure.py, fine_structure.py,
and anomalous_magnetic_moment.py — all showing the same systematic error.

### α⁵ Scaling from Self-Consistent DFC

When DFC's α_em is applied self-consistently to all atomic quantities, a structural
result follows from simple power counting:

The Bohr radius is inversely proportional to the fine structure constant — a smaller
coupling means a larger orbital:
```
a₀ ∝ ℏ/(m_e c α)    →    a₀_DFC = a₀_obs × (α_obs/α_DFC) = a₀_obs × 1.0224
```

The Rydberg energy (and hence transition frequencies) is proportional to the square
of the fine structure constant — a smaller coupling means weaker binding:
```
E_Ry ∝ m_e c² α²    →    ω_DFC = ω_obs × (α_DFC/α_obs)²
```

Substituting into the Einstein A formula, all powers of α combine:
```
A_DFC/A_obs = (α_DFC/α_obs) × (ω_DFC/ω_obs)³ × (a₀_DFC/a₀_obs)²
            = α × (α²)³ × (1/α)²  =  α⁵
```

The spontaneous emission rate scales as the fifth power of the fine structure
constant. This is a standard QED result, here recovered as an algebraic identity
from the DFC coupling chain.

With α_DFC/α_obs = 137.036/140.1 = 0.9781:

```
A_DFC/A_obs = (0.9781)^5 = 0.8953
τ_DFC/τ_obs = 1/0.8953 = 1.117
```

Every atomic lifetime in hydrogen is predicted to be 11.7% too long — a uniform
systematic bias from the single source of error in α_em.

### First-Principles Verification for Lyman-α

For the 2p→1s transition, the dipole matrix element can be computed exactly:

The radial matrix element — the overlap integral of the 1s and 2p hydrogen
wavefunctions weighted by the electron's radial distance — equals 1.2899 times
the Bohr radius:
```
I_rad = ∫ R₁₀(r) r R₂₁(r) r² dr = (1536 / (243√24)) a₀ = 1.2899 a₀
```

The angular average for a p→s transition (dividing by three for the three initial
magnetic substates):
```
|r̄₁₂|² = I_rad² / 3
```

This gives A_obs = 6.269 × 10⁸ s⁻¹, matching NIST (6.265 × 10⁸ s⁻¹) to 0.06%.

---

## Formal Equations

The Einstein A coefficient — the spontaneous emission rate in units of inverse seconds —
equals four times the fine structure constant times the cube of the transition angular
frequency, divided by three times the square of the speed of light, times the squared
dipole matrix element averaged over initial and summed over final magnetic substates:

```
A₂₁ = (4α ω³ |r̄₁₂|²) / (3c²)
```

The lifetime is the reciprocal of the total rate:
```
τ = 1 / Σ_k A_{2k}
```

Under self-consistent application of DFC's α_em, the rate and lifetime scale as:
```
A_DFC = A_obs × (α_DFC/α_obs)^5
τ_DFC = τ_obs × (α_obs/α_DFC)^5 = τ_obs × 1.117
```

The exact Lyman-α radial integral, valid for all α and free of additional parameters:
```
I_rad(2p→1s) = 1536 / (243√24) × a₀_DFC
             = 1.2899 × a₀_obs × (α_obs/α_DFC)
```

DFC predictions for select H-atom lifetimes (from `equations/spontaneous_emission.py`):

| Transition | τ_obs (ns) | τ_DFC (ns) | Error |
|---|---|---|---|
| 2p→1s (Ly-α) | 1.596 | 1.783 | +11.7% |
| 3d→2p (Hα) | 15.47 | 17.28 | +11.7% |
| 4f→3d (Pa-α) | 106.5 | 119.0 | +11.7% |
| (all transitions) | — | — | +11.7% (uniform) |

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| A ∝ α formula from D5-D6 coupling | Tier 1 structural | QED standard | ✓ |
| A ∝ α⁵ self-consistent scaling | algebraic identity from a₀∝1/α, ω∝α² | QED standard | ✓ Tier 1 |
| 2p→1s A first-principles | 6.269×10⁸ s⁻¹ (0.06% error) | 6.265×10⁸ s⁻¹ | ✓ Tier 1 (obs α) |
| Ly-α lifetime τ (DFC α⁵) | 1.783 ns | 1.596 ns | ✗ +11.7% Tier 2b |
| All H lifetimes uniformly | +11.7% over-predicted | — | ✗ Tier 2b (same source) |
| Exponential decay law | N(t)=N₀e^{−At} | confirmed | ✓ structural |
| Photon frequency = level spacing / ℏ | E_photon = ℏω postulate | confirmed | ✗ ℏ not derived (Tier 0) |

---

## Open Questions

1. **ℏ from substrate:** The relation E = ℏω, connecting photon energy to frequency,
   imports ℏ as a Tier 0 postulate. Deriving ℏ from the substrate would make
   spontaneous emission fully parameter-free in DFC. Currently S_kink(D1)/ℏ ≈ 10⁴⁰;
   ~13.4 bifurcation events bridge this hierarchy (model has 4 — ~10²⁸ residual).

2. **Close the α_em gap:** The 11.7% lifetime error is purely the 2.2% α_em error
   amplified by the α⁵ power. Deriving α_em exactly (closing Bottleneck 2's remaining
   Tier 4 step: show DFC KK action coupling equals det(g_moduli) from first principles)
   would fix all EM predictions including atomic lifetimes.

3. **Non-hydrogen atoms:** Work functions, screening, and multi-electron configurations
   require a DFC account of collective D7 substrate potential for the nuclear charge.
   This is the condensed-matter sector of atomic physics in DFC, currently unformalized.

---

## Connections

- `equations/spontaneous_emission.py` — numerical module; α⁵ scaling verified; 8 H transitions
- `equations/atomic_structure.py` — H energy levels from DFC α chain (same 4.3% systematic)
- `equations/fine_structure.py` — Dirac hydrogen spectrum (same α_em systematic)
- `equations/anomalous_magnetic_moment.py` — g-2 from α chain (−2.01% Tier 2b)
- `equations/coupling_derivation.py` — DFC α_em from β=1/(9π)
- `foundations/planck_constant_derivation.md` — ℏ hierarchy; ~13.4 bifurcations; open
- `phenomena/quantum/atomic_structure.md` — H energy levels; same 4.2% bias
- `phenomena/electromagnetism/light.md` — E=ℏω as postulate (Cycle 42)
- `phenomena/quantum/photoelectric_effect.md` — threshold emission; same coupling chain
