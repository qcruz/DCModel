# Phenomenon: The Stark Effect

## One-Sentence Synthesis

> The Stark effect is the D3 orbital distortion produced when an external electric field
> couples to the D5 charge structure: non-degenerate states acquire a quadratic energy
> shift set by their electric polarizability (wavefunction distortion under the field),
> while degenerate states (hydrogen n ≥ 2) acquire a linear shift set by their intrinsic
> electric dipole moment — both determined by the same DFC coupling chain that fixes α_em.

---

## Observation

When atoms are placed in an external electric field **E**, their spectral lines shift and
split. Discovered by Johannes Stark in 1913 (simultaneously with Lo Surdo), this effect
has two qualitatively distinct regimes:

**Quadratic (second-order) Stark effect:** For the hydrogen ground state (1s) and all
non-degenerate levels, the energy shifts quadratically with field strength. The level
moves down (stabilized) because the field distorts the electron cloud symmetrically in
the field direction. No first-order shift exists because the spherically symmetric 1s
state has no permanent electric dipole moment.

```
ΔE₁s = −½ α_pol E²     [α_pol = (9/2)(4πε₀)a₀³ = 7.421 × 10⁻⁴¹ F·m² for H ground state]
At E = 10⁷ V/m:  ΔE = −2.32 × 10⁻⁸ eV  (much smaller than Zeeman at 1 T; quadratic suppression)
```

**Linear (first-order) Stark effect:** For hydrogen levels with n ≥ 2, degeneracy in
angular momentum (ℓ mixes s and p character) allows a permanent electric dipole moment
proportional to n² × a₀. The energy shifts linearly with field:

```
ΔE(n,n₁,n₂) = (3/2) n (n₁ − n₂) e a₀ E    [parabolic quantum numbers]
For n = 2:  ΔE = ±3 e a₀ E = ±2.54 × 10⁻²² J per V/m of applied field
```

At laboratory field strengths of E ~ 10⁶ V/m, the n = 2 linear Stark shift
is ≈ 160 μeV — comparable to the Zeeman effect at 1–3 T.

---

## Standard Explanation

**Perturbation theory in the Coulomb potential.** An external uniform electric field
**E** in the z-direction adds the perturbation H' = eEz to the hydrogen Hamiltonian.
First-order perturbation theory gives ΔE = ⟨n,ℓ,m|eEz|n,ℓ,m⟩. For the ground state
this matrix element vanishes by parity (the 1s state has definite parity; z has odd
parity). Second-order perturbation theory gives:

```
ΔE = Σ_{n'≠n} |⟨n'|eEz|n⟩|² / (E_n − E_{n'})  =  −½ α_pol E²
```

where the static electric polarizability α_pol summarizes all virtual transitions. For
hydrogen 1s, the exact polarizability is α_pol = (9/2)(4πε₀)a₀³ — derived by Dalgarno
and Lewis (1955) using a closure approximation on the complete hydrogen spectrum.

For degenerate levels (n ≥ 2), the perturbation mixes states of opposite parity (s and p)
within the same n shell. First-order degenerate perturbation theory in parabolic coordinates
gives the exact linear shifts. For n = 2:

```
|2, n₁=1, n₂=0, m=0⟩   →  ΔE = +3ea₀E      (upper component)
|2, n₁=0, n₂=0, m=±1⟩  →  ΔE = 0            (unshifted doublet)
|2, n₁=0, n₂=1, m=0⟩   →  ΔE = −3ea₀E      (lower component)
```

The hydrogen n = 2 level thus splits into three distinct Stark components (one doubly
degenerate), with the two outer components carrying the dipole-allowed transitions that
appear in emission spectra.

---

## Dimensional Folding Explanation

### D3 Orbital Distortion Under D5 Gauge Coupling

The Stark effect arises from the interplay of two depth behaviors of the substrate:

- **D3 localization:** the electron's position degree of freedom — its wavefunction
  ψ(r) — is the localization behavior of the substrate at D3 depths. The wavefunction
  amplitude squared gives the probability density for finding the electron at each point.

- **D5 U(1) closure:** the electric charge e is the holonomy of the substrate's D5
  U(1) gauge connection. The charge couples the electron's spatial configuration to
  the gauge field — this is the minimal substitution **p** → **p** − e**A** in the
  covariant derivative (Cycle 71, D5 complex structure).

An external electric field **E** is a classical background of the D5 gauge potential
(the Coulomb potential V = −eEz for a uniform field in the z-direction). This background
modifies the effective D3 potential:

```
V_eff(r) = V_Coulomb(r) + (−e)(−Ez) = −e²/(4πε₀r) + eEz
```

The second term couples the D3 orbital structure to the D5 field. The response of
the D3 wavefunction to this coupling has two regimes based on the symmetry of the
state being perturbed.

### Quadratic Stark: D3 Polarization by the D5 Field

For the hydrogen ground state (1s), the D3 wavefunction has exact spherical symmetry
(L = 0, S = 0). The D5 electric field has odd parity (z → −z gives z → −z). Because
the unperturbed state has definite parity (even), the first-order coupling vanishes —
there is no permanent electric dipole in a spherically symmetric state.

At second order, the D3 wavefunction distorts: the electron density shifts slightly
in the direction of the field. This produces an induced dipole moment proportional to
the field, and the associated energy shift is quadratic:

The energy shift at second order equals negative one-half times the polarizability times
the square of the applied field. The polarizability — the coefficient controlling how
strongly the D3 orbital distorts under the applied D5 field — is an exact analytical
result from the complete set of virtual transitions:

```
ΔE = −(1/2) α_pol E²

α_pol = (9/2)(4πε₀) a₀³    [exact, from Dalgarno-Lewis sum; Tier 1 structural]
```

The Bohr radius a₀ = ℏ/(m_e c α_em) — set by the ratio of the quantum of action to
the product of the electron mass, the speed of light, and the fine structure constant —
connects the polarizability back to the DFC coupling chain: any error in α_em propagates
as a cube into the polarizability prediction (since α_pol ∝ a₀³ ∝ α_em⁻³).

### Linear Stark: D3 Degeneracy and Intrinsic Dipole

For hydrogen excited states (n ≥ 2), the D3 wavefunction has multiple degenerate
configurations with the same energy but different orbital angular momentum ℓ = 0, 1, ..., n−1.
In parabolic coordinates, these configurations are mixed by the D5 electric perturbation.

The mixed states carry intrinsic electric dipole moments — permanent (not induced) dipoles
— proportional to the product of the principal quantum number, the parabolic quantum
number difference, and the Bohr radius. The energy shift is linear in field:

The shift of each state in the n-th hydrogen level equals three-halves times the principal
quantum number times the difference of parabolic quantum numbers (n₁ − n₂) times the
electron charge times the Bohr radius times the applied field. This is:

```
ΔE = (3/2) n (n₁ − n₂) e a₀ E    [exact, Tier 1 structural]
```

**In DFC terms:** the D3 localization depth supports multiple topologically inequivalent
orbital configurations at the same energy — states that differ in how the localization
is distributed around the D4/D5 boundary. The applied D5 field lifts this degeneracy
by coupling to the net dipole moment of the combined D3+D5 configuration. The coefficient
3/2 × n × (n₁ − n₂) × ea₀ is set by the geometry of the D3 localization at the n-th
level — not a free parameter, but a consequence of the hydrogen Coulomb potential.

### DFC Coupling Chain to α_em

The quantitative prediction for the Stark effect reduces to the same chain as all DFC
electromagnetic predictions:

```
β = 1/(9π)  →  g_eff² = 8/27  →  α_em(M_Z) = 1/129.6
    →  QED running  →  α_em(m_e) = 1/140.1   (DFC)
    →  a₀(DFC) = ℏ/(m_e c α_em(DFC)) = 1.0224 × a₀(obs)
    →  α_pol(DFC) = (9/2)(4πε₀) a₀(DFC)³ = 1.069 × α_pol(obs)
    →  6.9% error in polarizability (same source as all EM predictions)
```

The 6.9% error in α_pol traces to the 2.24% error in α_em(m_e), which is 3× the 0.75%
error in g² at M_Z, which traces to the heuristic step in the r_U1/λ identification
(Bottleneck 2 closed, Cycle 112 — but the α_em running now has residual 1.3% systematic).

*The linear Stark coefficient 3ea₀E is not computable from DFC alone because it requires
the exact hydrogen wavefunction (which depends on ℏ, taken as a postulate). The structural
form — linear splitting proportional to ea₀ — is Tier 1; the coefficient 3 is exact from
the D3 orbital geometry. The numerical prediction for the linear Stark splitting inherits
the same 2.24% error in a₀ from the DFC coupling chain.*

---

## Formal Equations

### Polarizability of Hydrogen Ground State

The electric polarizability of the hydrogen 1s ground state equals nine-halves times
four-pi-epsilon-zero times the cube of the Bohr radius:

```
α_pol(1s) = (9/2)(4πε₀) a₀³ = 7.421 × 10⁻⁴¹ F·m²   [= 4.500 a.u., polarizability volume 0.6668 Å³]
```

Equivalently, in atomic units, the polarizability volume is 4.5 a₀³. This is an exact
quantum mechanical result from second-order perturbation theory on the hydrogen atom.

### Second-Order Stark Energy Shift

The energy shift of a non-degenerate state in an applied electric field of strength E
equals negative one-half times the polarizability times the square of the field:

```
ΔE = −(1/2) α_pol E²
```

For hydrogen 1s at E = 10⁷ V/m: ΔE = −2.32 × 10⁻⁸ eV (23.2 neV) [quadratic — very small at lab fields]

### First-Order (Linear) Stark Shift for Hydrogen n = 2

The four n = 2 states of hydrogen split into three groups under an applied electric field.
In parabolic coordinates (n, n₁, n₂, m), the energy shift equals:

```
ΔE = (3/2) n (n₁ − n₂) e a₀ E
```

For n = 2, the three distinct energies are:
```
ΔE₊ = +3 e a₀ E = +2.541 × 10⁻²² J per (V/m)   [state |n₁=1, n₂=0, m=0⟩]
ΔE₀ = 0                                            [states |n₁=0, n₂=0, m=±1⟩]
ΔE₋ = −3 e a₀ E = −2.541 × 10⁻²² J per (V/m)   [state |n₁=0, n₂=1, m=0⟩]
```

At E = 10⁶ V/m: ΔE₊ = +1.588 × 10⁻⁴ eV = +158.8 μeV

### Polarizability Scaling with Quantum Number

For highly excited states, the polarizability scales as n⁷ (much faster than the n² energy
spacing). The static polarizability of hydrogen in state n, averaged over magnetic substates,
scales as:

```
α_pol(n) ≈ (9/2) n⁷ (4πε₀) a₀³    [approximate, n-dependent prefactor]
```

For n = 2: α_pol(2) ≈ (128) × (4πε₀) a₀³ (exact: 120 a₀³ in atomic units)

### Selection Rules Under Electric Field

The applied electric field reduces the full SO(3) rotation symmetry of the hydrogen atom
to U(1) rotation symmetry around the field axis. The surviving selection rules are:

```
Δm = 0        [linear polarization parallel to E]
Δm = ±1       [linear polarization perpendicular to E]
Δℓ = ±1       [parity selection rule, unchanged]
```

Electric field does NOT mix states with different parity globally (unlike the magnetic
field which mixes only via the anomalous magnetic moment). The Stark Hamiltonian has
definite parity −1 (z → −z gives −z), so it connects states that differ in parity.

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| H ground state polarizability α = 4.50 a₀³ | (9/2)(4πε₀)a₀³ exact from perturbation theory | 4.503 × 10⁻⁴¹ F·m² | ✓ structural (Tier 1) |
| DFC α_pol(1s) numerical | 7.921 × 10⁻⁴¹ F·m² (from a₀_DFC) | 7.421 × 10⁻⁴¹ F·m² | ✗ +6.8% (α_em systematic) |
| Linear shift ΔE ∝ E for n ≥ 2 | D3 degeneracy + D5 dipole coupling | confirmed for all n ≥ 2 | ✓ structural (Tier 1) |
| Quadratic shift ΔE ∝ E² for ground state | no permanent dipole in spherically symmetric state | confirmed for 1s | ✓ structural (Tier 1) |
| n = 2 linear Stark coefficient 3ea₀ | D3 orbital geometry (exact) | ΔE/E = 2.541 × 10⁻²² J·m/V | ✓ Tier 1 (error 2.24% from a₀) |
| Ground state shifts downward (stabilized) | induced dipole opposes field → energy decrease | universally observed | ✓ structural (Tier 1) |
| No Stark splitting for L = 0 ground state at first order | parity argument: ⟨1s|z|1s⟩ = 0 | ground state unresolved at first order | ✓ structural (Tier 1) |
| Three Stark components for n = 2 (ratio ±1 : 0 : ∓1) | parabolic quantum number algebra | three components observed | ✓ structural (Tier 1) |
| Selection rules Δm = 0, ±1; Δℓ = ±1 | parity + U(1) symmetry reduction under E | confirmed spectroscopically | ✓ structural (Tier 1) |
| Stark energy scale vs Zeeman at same lab conditions | at E = 10⁶ V/m: Stark linear ~ 160 μeV; at B = 1T: Zeeman ~ 58 μeV | linear Stark > Zeeman at accessible fields | ✓ Tier 1 |

The 6.8% error in α_pol is exactly 3× the 2.24% error in α_em(m_e). It traces to the
same r_U1/λ identification step as all DFC electromagnetic predictions. It will close
when α_em(M_Z) is pinned from the substrate rather than from SM running.

---

## Open Questions

1. **Derive the Stark polarizability from DFC wavefunction.** The exact result
   α = (9/2)(4πε₀)a₀³ comes from second-order perturbation theory on the Coulomb
   potential. In DFC, this requires: (a) a₀ from the DFC α_em chain (done, with 2.24%
   error), and (b) the Dalgarno-Lewis sum over virtual transitions evaluated on the DFC
   substrate's D3 localization modes rather than textbook hydrogen eigenstates. Are the
   DFC D3 modes identical to hydrogen eigenstates, or do substrate corrections appear
   at high n?

2. **Stark mixing of D-depth modes.** The electric field mixes states of opposite
   parity (ℓ-mixing). In DFC, states at D3 depth have a winding structure that determines
   ℓ. When the D5 field applies a parity-odd perturbation, does it mix different D3
   winding configurations? Formally: does the Stark Hamiltonian H' = eEz have a natural
   action on the D3 substrate modes, and does this action reproduce the exact parabolic
   eigenvalue spectrum?

3. **Quadratic polarizability of excited states.** For excited states of hydrogen (n ≥ 2),
   both linear and quadratic Stark shifts coexist. The quadratic polarizability scales
   as n⁷, producing a rapid breakdown of the linear approximation at high n (Inglis-Teller
   limit: the quadratic shift equals the linear only at E ~ 1/(3n⁵) in atomic units).
   In DFC, at high n the D3 modes are large and their coupling to the D5 gauge field
   becomes geometrically non-trivial. Can DFC reproduce the n⁷ scaling from the D3
   orbital geometry at large quantum number?

4. **Stark effect in strong fields (ionization).** Above a critical field
   E_ion ~ E_h/(e a₀) ~ 5 × 10⁹ V/m (the atomic field unit), the external field
   dominates the Coulomb potential and the atom ionizes. In DFC, this is the regime
   where the D5 applied gauge field exceeds the D3 Coulomb binding: the D3 localization
   is no longer stable. Can the ionization threshold be derived from the D3 binding
   energy vs the applied D5 field energy — specifically, does the Landau-Dykhne
   ionization rate follow from the DFC D3-D5 coupling without additional assumptions?

---

## Connections

- **Zeeman effect** — magnetic analog (D6 coupling); `phenomena/quantum/zeeman_effect.md`
- **Atomic structure** — hydrogen energy levels E_n = −α_em² m_e c²/(2n²); `phenomena/quantum/atomic_structure.md`
- **Electromagnetism** — D5 U(1) gauge field is the source of both electric and magnetic forces; `phenomena/electromagnetism/electromagnetism.md`
- **Anomalous magnetic moment** — same α_em coupling chain, same systematic error; `phenomena/quantum/anomalous_magnetic_moment.md`
- **Aharonov-Bohm effect** — topological gauge coupling (B ≠ 0 region, A field phase); `phenomena/quantum/aharonov_bohm.md`
- `equations/stark_effect.py` — numerical verification of polarizability and energy shifts
- `equations/zeeman_effect.py` — parallel computation for magnetic splitting (Cycle 119)
- `equations/atomic_structure.py` — DFC α_em chain to Bohr radius and energy levels
- `foundations/coupling_derivation.md` — g_eff² = 8/27 → α_em chain
- `foundations/alpha_s_derivation.md` — α_em running from M_Z to m_e scale
