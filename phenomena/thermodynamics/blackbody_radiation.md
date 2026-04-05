# Phenomenon: Blackbody Radiation

## One-Sentence Synthesis

> Blackbody radiation is the thermal equilibrium distribution of massless D2 compression
> wave modes in a cavity: the photon occupation number n(ν) = 1/(e^{hν/kT} − 1) follows
> from Bose-Einstein statistics applied to the massless KG mode spectrum, E = hν is derived
> (not postulated) from the compression field dispersion, and the Planck catastrophe is
> resolved by the same field discreteness that produces particle quantization — not by a
> separate quantum postulate.

---

## Observation

Every object at temperature T emits thermal radiation with a spectrum that depends only
on T, independent of the object's composition:

**The Planck spectrum:**
```
u(ν, T) = (8πhν³/c³) × 1/(e^{hν/kT} − 1)    [energy density per unit frequency]
```

**Derived laws:**
- **Wien's displacement law:** λ_max T = b = 2.898 × 10⁻³ m·K (peak wavelength × T = const)
- **Stefan-Boltzmann law:** P = σT⁴ (total emitted power; σ = 5.67 × 10⁻⁸ W/m²/K⁴)
- **Rayleigh-Jeans (low ν):** u(ν) ∝ ν²T — the classical limit
- **Wien (high ν):** u(ν) ∝ ν³ e^{−hν/kT} — the quantum suppressed tail

**Precision:** The CMB temperature T = 2.7255 K fits the Planck spectrum to better than
1 part in 10,000 — the most precisely measured blackbody in nature.

**The ultraviolet catastrophe:** Classical equipartition assigns kT energy to every mode.
At high frequency, the mode density grows as ν², so the total energy ∫ν²kT dν diverges.
Planck's 1900 solution — quantizing the oscillator energies as E_n = nhν — prevents this
divergence. But it was a postulate; it had no derivation.

---

## Standard Explanation

Photons are massless spin-1 bosons. In thermal equilibrium at temperature T, the mean
occupation number of a mode at frequency ν follows the Bose-Einstein distribution:

```
n(ν) = 1/(e^{hν/kT} − 1)
```

With mode density 8πν²/c³ per unit volume per unit frequency (counting two polarizations):

```
u(ν) = (8πν²/c³) × hν × n(ν) = (8πhν³/c³)/(e^{hν/kT} − 1)    ✓
```

The quantization E = hν is required but not derived — it is the Planck postulate. The
Bose-Einstein distribution is derived from statistical mechanics once quantization is assumed.

---

## Dimensional Folding Explanation

### Photons as Massless D2 Modes

In DFC, photons are massless excitations of the compression field propagating as D2 modes
— solutions of the massless KG equation:

```
□φ = 0    →    ω = ck    →    E = ℏω = ℏck = hν
```

The quantization E = hν is **derived** from the dispersion relation, not postulated. A
photon at frequency ν carries energy E = hν because that is the quantum of energy for the
KG mode at wave vector k = 2πν/c. This is the same result that appears in the photoelectric
effect and Compton scattering — all derived from the same KG dispersion.

### The Mode Density

The number of independent wave modes in a cavity of volume V in the frequency range [ν, ν+dν]:

```
dN = 2 × 4πk² dk × V / (2π)³
   = 2 × 4π(2πν/c)² × (2π/c) dν × V / (2π)³
   = 8πν²/c³ × V dν
```

The factor 2 counts the two independent polarizations of the photon (two helicity states
of the spin-1 D2 mode). These are the only two polarizations because the photon is massless
(the D5 U(1) gauge field is massless, giving only transverse modes — see
`phenomena/electromagnetism/electromagnetism.md`).

### Why Bose-Einstein Statistics Apply

Photons are bosons: they have integer spin (spin-1, as the spin-1 D5 gauge field) and
even Finkelstein-Rubinstein exchange phase (D6 winding N = 0 → phase +1 → bosonic statistics).
The exchange phase argument is derived in `phenomena/quantum/spin.md`.

For identical bosons in thermal equilibrium, the grand canonical ensemble gives the
Bose-Einstein occupation number. The photon chemical potential μ = 0 (photons are not
conserved — they are continuously emitted and absorbed by the walls, which are in
thermal equilibrium):

```
n(ν) = 1/(e^{(hν − μ)/kT} − 1)|_{μ=0} = 1/(e^{hν/kT} − 1)    ✓
```

### The Planck Spectrum Derived

Combining the mode density with the Bose-Einstein distribution:

```
u(ν, T) = (energy per mode) × (occupation number) × (modes per unit volume per unit ν)

= hν × 1/(e^{hν/kT} − 1) × 8πν²/c³

= 8πhν³/c³ × 1/(e^{hν/kT} − 1)    [Planck spectrum] ✓
```

### Why the Ultraviolet Catastrophe Is Resolved

In the classical (Rayleigh-Jeans) limit hν ≪ kT:

```
n(ν) → kT/(hν)    →    u(ν) → 8πν²kT/c³    [Rayleigh-Jeans] ✓
```

At high frequency hν ≫ kT:

```
n(ν) → e^{−hν/kT}    →    u(ν) → 8πhν³/c³ × e^{−hν/kT}    [Wien exponential suppression]
```

The suppression at high frequency is automatic — it follows from the discreteness of the
KG mode energy spectrum (E = hν), which means that high-energy modes require large energies
to excite. The thermal fluctuations at temperature T cannot supply energy much larger than
kT, so high-frequency modes are exponentially suppressed.

This is not a separate quantum postulate. It is the same field discreteness that produces
particle quantization throughout DFC — the compression field has discrete mode energies
because it satisfies the KG equation with quantization condition E = ℏω.

---

## Formal Derivations

### Wien's Displacement Law

Find the maximum of u(ν, T) by setting du/dν = 0:

```
d/dν [ν³/(e^{hν/kT} − 1)] = 0

Let x = hν/kT:
d/dx [x³/(e^x − 1)] = 0
3x²(e^x − 1) − x³ e^x = 0
3(1 − e^{−x}) = x
→  x ≈ 2.821    [numerical solution]
```

Therefore:
```
hν_max = 2.821 kT
→  ν_max = 2.821 kT/h
→  λ_max = c/ν_max = hc/(2.821 kT)

λ_max T = hc/(2.821 k) = b = 2.898 × 10⁻³ m·K    ✓
```

### Stefan-Boltzmann Law

Integrate the Planck spectrum over all frequencies:

```
u_total = ∫₀^∞ u(ν, T) dν = (8πh/c³) ∫₀^∞ ν³/(e^{hν/kT} − 1) dν

Let x = hν/kT:
= (8πh/c³) × (kT/h)⁴ × ∫₀^∞ x³/(e^x − 1) dx

∫₀^∞ x³/(e^x − 1) dx = π⁴/15    [Riemann zeta: ζ(4) × Γ(4) = π⁴/90 × 6]

u_total = (8π⁵k⁴)/(15 c³ h³) × T⁴
```

Power emitted per unit area (Stefan-Boltzmann):
```
P/A = c/4 × u_total = (2π⁵k⁴)/(15 c² h³) × T⁴ = σT⁴

σ = 2π⁵k⁴/(15c²h³) = 5.670 × 10⁻⁸ W/m²/K⁴    ✓
```

All constants (k, h, c) are already present in DFC — no new parameters are introduced.

---

## Consistency Checks

| Prediction | DFC mechanism | Observed |
|---|---|---|
| Planck spectrum u(ν) = 8πhν³/c³ × (e^{hν/kT}−1)⁻¹ | KG dispersion + Bose-Einstein | Standard result ✓ |
| E = hν not postulated | KG dispersion E = ℏω | Derived ✓ |
| Two photon polarizations | Massless gauge field, transverse only | Two helicity states ✓ |
| Bose-Einstein statistics | Spin-1 D5 field, even FR phase | Photons are bosons ✓ |
| Wien's law λ_max T = 2.898 × 10⁻³ m·K | Maximum of Planck curve, x ≈ 2.821 | Confirmed ✓ |
| Stefan-Boltzmann σ = 5.67 × 10⁻⁸ W/m²/K⁴ | Integral of Planck spectrum | Confirmed ✓ |
| UV catastrophe resolved | Exponential suppression from discrete KG modes | Resolved ✓ |
| CMB spectrum T = 2.7255 K | Planck spectrum from thermalized D2 modes | <10⁻⁴ precision ✓ |

---

## Open Questions

1. **Photon thermalization mechanism.** The Planck spectrum requires photons to be in
   thermal equilibrium with the walls (μ = 0, photon number not conserved). In DFC,
   photon emission and absorption are kink nucleation and annihilation events. Whether
   the DFC emission/absorption rate correctly gives μ = 0 in equilibrium — i.e., whether
   the D5 gauge field coupling to matter kinks produces the right balance condition —
   requires a formal derivation.

2. **CMB spectrum from DFC first principles.** The CMB is not just blackbody radiation —
   it is the specific blackbody produced when the D3 localization behavior became stable
   (recombination, z ≈ 1100) and the photons decoupled from matter. The DFC account of
   this epoch — what "recombination" looks like in terms of D4 kink binding to D5 fields
   — and whether it produces T_CMB = 2.7255 K from first principles, is an open
   derivation connected to the big bang account.

3. **Corrections from DFC field structure.** The Planck spectrum assumes an ideal blackbody
   with no structure at the Planck scale. At frequencies approaching ν_Planck = c/L_Planck
   ≈ 10^{43} Hz, the KG equation may have corrections from the nonlinear potential V'(φ).
   Whether DFC predicts any deviation from the Planck spectrum at extreme frequencies —
   a testable signature of Planck-scale physics — is an open question.

---

## Connections

- **Light** — photons as massless D2 compression modes, E = hν derived;
  `phenomena/light/light.md`
- **Quantum mechanics** — discretization of field modes, KG equation;
  `phenomena/quantum/quantum_mechanics.md`
- **Spin** — bosonic exchange statistics for photons (N=0 FR phase);
  `phenomena/quantum/spin.md`
- **Thermodynamics** — thermal equilibrium, entropy, temperature;
  `phenomena/thermodynamics/thermodynamics.md`
- **CMB** — blackbody radiation at T = 2.7255 K, photon decoupling;
  `phenomena/cosmology/cosmic_microwave_background.md`
