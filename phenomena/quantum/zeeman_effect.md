# Phenomenon: The Zeeman Effect

## One-Sentence Synthesis

> The Zeeman effect — the splitting of atomic spectral lines in a magnetic field — arises
> in DFC because the D3 orbital angular momentum degree of freedom and the D5 gauge field
> (the electromagnetic potential A_μ) couple through the minimal substitution in the
> covariant derivative, producing an energy shift proportional to the orbital quantum
> number m_l and the magnetic field strength B; the anomalous Zeeman effect additionally
> involves the D6 spin degree of freedom whose g-factor is 2 from the Dirac equation
> (with QED corrections already derived from the DFC coupling chain in Cycle 55).

---

## Observation

When atoms are placed in a magnetic field B, their spectral lines split into multiple
components. This was observed by Pieter Zeeman in 1896.

**Normal Zeeman effect** (applies when spin is negligible, or to specific J transitions):
Each spectral line splits into exactly **three** components at:
```
ν = ν₀,    ν₀ + ν_L,    ν₀ − ν_L
```
where the Larmor frequency equals the ratio of the electron charge to four times pi times
the electron mass, multiplied by the magnetic field strength:
```
ν_L = eB / (4π m_e)    [Larmor frequency, Hz]
```
At B = 1 T: ν_L = 13.996 GHz. The three lines are separated by exactly ν_L regardless
of which transition is studied — a universal, atom-independent splitting.

**Anomalous Zeeman effect** (general case including spin): Lines split into more than
three components, with splittings that depend on the quantum numbers (J, L, S) of each
level through the Landé g-factor:
```
g_J = 1 + [J(J+1) + S(S+1) − L(L+1)] / [2J(J+1)]
```

**The Paschen-Back effect**: at very strong fields (B >> spin-orbit splitting), the spin
and orbital moments precess independently and the pattern returns to the normal Zeeman form.

---

## Standard Explanation

In quantum mechanics, the magnetic interaction Hamiltonian for an electron in field B
(along z-axis) is:
```
H_mag = −μ · B = (e / 2m_e)(L + g_S S) · B
```
where L is orbital angular momentum, S is spin angular momentum, and g_S ≈ 2.0023 is the
electron spin g-factor (g_S = 2 from Dirac equation; 0.0023 from QED loop corrections).

The energy shift for a state |J, m_J⟩ in field B is:
```
ΔE = g_J m_J μ_B B
```
where μ_B = eℏ/(2m_e) is the Bohr magneton and g_J is the Landé g-factor. This produces
2J+1 equally spaced sublevels in each J-state.

---

## Dimensional Folding Explanation

### D5 Gauge Coupling to D3 Motion

In DFC, the Zeeman effect is the response of the D3 orbital motion to the D5 gauge
field background. The magnetic field B is the spatial part of the D5 U(1) connection
field strength F_μν = ∂_μ A_ν − ∂_ν A_μ (specifically, B_i = ε_{ijk} F_{jk}).

The electron's orbital motion at D3 depth couples to this D5 background through the
minimal substitution in the covariant derivative: the momentum operator p is replaced by
p − eA/c. This replacement is not a choice — it is required by U(1) gauge invariance of
the D5 closure, which demands that any field carrying D5 charge (including the D3-localized
electron) couples this way. The substitution is the unique gauge-invariant coupling consistent
with the D5 topology.

The resulting Hamiltonian contains the cross-term −(e/2m_e) L · B from expanding
(p − eA)² around the equilibrium configuration. The energy shift for orbital
quantum number m_l is:

The energy shift of a state with orbital magnetic quantum number m_l equals negative
one times m_l times the Bohr magneton times the field strength:
```
ΔE_orb = −m_l μ_B B    where  μ_B = eℏ / (2m_e)
```

Since m_l ∈ {−l, −l+1, ..., +l}, a level with orbital quantum number l splits into
2l+1 equally spaced sublevels. For a p-state (l = 1): three components with m_l = −1, 0, +1.
For a d-state (l = 2): five components. The selection rule Δm_l = 0, ±1 from the
D5 photon coupling (D5 = U(1), one photon carries one unit of angular momentum) means
only three lines appear in each transition.

This is the **normal Zeeman effect**: three lines at ν_L = eB/(4π m_e) regardless of n, l.

### D6 Spin Coupling and Anomalous Splitting

The D6 spin degree of freedom carries its own magnetic moment — the spin magnetic moment:
```
μ_S = −g_S μ_B S
```
where g_S is the spin g-factor. From the Jackiw-Rebbi zero mode structure at D6 depth
(Cycle 38 — the spin-1/2 identification is Tier 1), the Dirac equation for a relativistic
spin-1/2 field in an electromagnetic background gives g_S = 2 exactly at tree level. The
one-loop QED correction gives:

The quantum correction to the spin g-factor — the anomalous magnetic moment — equals
the electromagnetic fine structure constant divided by two pi (Schwinger term), already
derived in Cycle 55 from the DFC coupling chain:
```
g_S = 2(1 + a_e)    where  a_e = α_em/(2π) [DFC: α_em from β = 1/(9π)]
```

DFC prediction: a_e = α_em(m_e)/(2π) = 0.001136 (Tier 2b; 2.01% off from 0.001160).
This inherits the same α_em systematic as all DFC EM predictions.

The total magnetic moment, combining orbital and spin contributions, determines the
Landé g-factor through the quantum mechanical addition of angular momenta (Wigner-Eckart
theorem applied to the total angular momentum J = L + S). The Landé g-factor:

The Landé g-factor of a state with total angular momentum J, orbital angular momentum L,
and spin angular momentum S equals one plus the ratio of J(J+1) plus S(S+1) minus
L(L+1) to twice J(J+1):
```
g_J = 1 + [J(J+1) + S(S+1) − L(L+1)] / [2J(J+1)]
```

This formula is Tier 1 in DFC: it follows purely from the vector model of angular
momentum addition (D3 rotational behavior + D6 spin), with no free parameters.

### Selection Rules from D5 Topology

Photon emission is the creation of a D5 gauge excitation. Because the D5 gauge field
carries angular momentum ±1 (two circular polarization states: helicity ±1), only
transitions with Δm_J = 0, ±1 are allowed. This is not imposed separately — it follows
from the D5 U(1) topology: π₁(S¹) = ℤ with |ΔN| = 1 for single-photon emission.

The three types of radiation:
- **π polarization** (Δm_J = 0): linear polarization parallel to B; one central line
- **σ± polarization** (Δm_J = ±1): circular polarization; two outer lines

---

## Formal Equations

The Bohr magneton — the fundamental unit of magnetic moment — equals the product of the
elementary charge and the quantum of action, divided by twice the electron mass:
```
μ_B = eℏ / (2m_e) = 9.2740 × 10⁻²⁴ J/T = 5.7884 × 10⁻⁵ eV/T
```
In DFC: e from D5 winding (Tier 1, integer charge); ℏ postulate; m_e experimental input.

The energy shift of a state with magnetic quantum number m_J in field B is:
```
ΔE = g_J m_J μ_B B
```

The Larmor frequency — the classical precession frequency of a magnetic dipole in field B
— equals the ratio of the electron charge to four times pi times the electron mass,
times the field:
```
ν_L = eB / (4πm_e) = μ_B B / h    [Hz]
```

The normal Zeeman spectrum consists of three lines at frequencies ν₀ − ν_L, ν₀, ν₀ + ν_L.

The Landé g-factor formula (Tier 1 from angular momentum addition):
```
g_J = 1 + [J(J+1) + S(S+1) − L(L+1)] / [2J(J+1)]
```
Examples:
- g_J(²P₁/₂): J=1/2, L=1, S=1/2 → g_J = 2/3
- g_J(²P₃/₂): J=3/2, L=1, S=1/2 → g_J = 4/3
- g_J(²S₁/₂): J=1/2, L=0, S=1/2 → g_J = 2 (= g_S to tree level)

---

## Consistency Checks

| Check | DFC mechanism | Observed | Status |
|---|---|---|---|
| Three lines in normal Zeeman | U(1) coupling to L, photon Δm_l=±1,0 | Three lines | ✓ Tier 1 |
| Larmor frequency ν_L=eB/(4πm_e) | Orbital-B coupling from minimal substitution | 13.996 GHz/T | ✓ Tier 1 (ℏ postulate) |
| Landé g-factor formula | Angular momentum addition of D3+D6 DOF | Agreement to <10⁻⁴ | ✓ Tier 1 |
| g_J(²P₁/₂) = 2/3 | J=1/2, L=1, S=1/2 from quantum numbers | 2/3 = 0.6667 | ✓ exact |
| g_J(²P₃/₂) = 4/3 | J=3/2, L=1, S=1/2 from quantum numbers | 4/3 = 1.3333 | ✓ exact |
| g_S ≈ 2.002272 from DFC | Dirac g_S=2 + QED a_e=α_em/(2π) from β chain | 2.002319 | ✓ 0.002% (Cycle 55) |
| μ_B = 5.7884×10⁻⁵ eV/T | eℏ/(2m_e) with e, ℏ from DFC, m_e experimental | 5.7884×10⁻⁵ eV/T | ✓ exact given inputs |
| Selection rules Δm_J = 0, ±1 | D5 U(1) photon carries angular momentum ±1 | confirmed | ✓ structural |
| Paschen-Back limit → normal Zeeman | L, S decouple; orbital term dominates | confirmed | ✓ structural |
| H-alpha wavelength shift Δλ at B=1T | Δλ = −λ²/c × ν_L ≈ −20 pm | ~20 pm | ✓ Tier 1 |

---

## Open Questions

1. **Derive μ_B from DFC parameters.** Currently μ_B = eℏ/(2m_e) uses ℏ as a postulate
   (not derived from DFC substrate) and m_e as experimental input. If ℏ is derived from
   the substrate (see `foundations/planck_constant_derivation.md`), μ_B becomes Tier 2a.

2. **Stark effect.** The Stark effect (electric field splitting) is the analogue for the
   E-field component of A_μ. The coupling is again through the covariant derivative, but
   the E-field couples to the dipole moment rather than the angular momentum. In DFC:
   the D3 orbital charge distribution couples to the D5 electric potential — the analysis
   is structurally identical to the Zeeman effect.

3. **Spin-orbit coupling source.** The spin-orbit coupling that produces fine structure
   (prerequisite for the anomalous Zeeman pattern) is the relativistic interaction of
   the D6 spin with the D5 magnetic field seen in the electron's rest frame. The DFC
   account of spin-orbit coupling connects D6 zero mode dynamics to D5 gauge field
   gradients — not yet formally derived.

4. **QED higher-order corrections.** The g_S = 2.002272 prediction (Cycle 55) is only
   the leading Schwinger term. Higher-loop contributions (α²/π², etc.) require the
   full DFC S-matrix for multi-photon processes, which connects to the open Bottleneck 2
   problem of deriving the full scattering amplitude.

---

## Connections

- `phenomena/quantum/atomic_structure.md` — hydrogen energy levels from DFC (Cycle 44)
- `phenomena/quantum/anomalous_magnetic_moment.md` — g_S = 2 + α_em/π from DFC (Cycle 55)
- `phenomena/quantum/spin.md` — D6 spin-1/2 from Jackiw-Rebbi (Cycle 33+38)
- `phenomena/electromagnetism/electromagnetism.md` — D5 U(1) gauge structure
- `phenomena/electromagnetism/electric_charge.md` — integer charge from D5 winding
- `equations/zeeman_effect.py` — numerical verification of all consistency check entries
- `equations/anomalous_magnetic_moment.py` — DFC coupling chain to a_e (Cycle 55)
- `equations/atomic_structure.py` — hydrogen energy levels; QED running of α_em
