# Phenomenon: Compton Scattering and the Thomson Cross-Section

## One-Sentence Synthesis

> The Thomson cross-section — the probability that a photon scatters off an electron
> at low energy, observed at 6.65×10⁻²⁹ m² — is predicted by DFC through an unbroken
> chain from the substrate quartic coupling β to the electromagnetic fine-structure
> constant to the classical electron radius: the D5 closure radius, set by the kink
> phase stiffness, determines the coupling strength, which determines how tightly the
> electron closure responds to an incident D2 mode, giving σ_T = (8π/3)(α_em/m_e)²
> with a 4.3% shortfall that traces entirely to the 1.3% gap in α_em(M_Z) from the
> r_U1/λ holonomy identification.

---

## Observation

When electromagnetic radiation (photons) interacts with free electrons, it scatters.
The probability of scattering per unit area — the cross-section — depends on photon
energy:

- **Thomson limit (low energy, hν ≪ m_e c²):** The electron reradiates the incident
  photon elastically (without energy loss). The total scattering cross-section is:

  ```
  σ_T = 6.6524587158 × 10⁻²⁹ m²   [CODATA 2018]
  ```

  This is one of the most precisely measured quantities in atomic physics. It sets the
  opacity of ionized plasma to radiation, determines the mean free path of cosmic
  microwave background photons before recombination, and sets the scale for all
  electromagnetic scattering.

- **Classical electron radius:** The Thomson cross-section equals eight-thirds of pi
  times the square of the classical electron radius:

  ```
  r_e = 2.8179403227 × 10⁻¹⁵ m   (2.818 fm)
  ```

  The classical electron radius is the distance at which the electrostatic self-energy
  of the electron equals its rest-mass energy.

- **Compton limit (high energy, hν ≳ m_e c²):** At higher energies, quantum recoil
  reduces the cross-section below the Thomson value. The Klein-Nishina formula
  describes the full energy dependence. At photon energy equal to the electron rest
  mass (511 keV), the cross-section falls to approximately 43% of the Thomson value.

---

## Standard Explanation

In QED, the Thomson cross-section is derived from the tree-level Feynman diagram for
photon-electron scattering (two vertices, each contributing a factor of the QED coupling
constant e). The amplitude squared, summed over polarizations and averaged over initial
states, gives:

The Thomson cross-section equals eight-thirds of pi times the square of the ratio of
the electromagnetic coupling constant to the electron mass (in natural units where ℏ =
c = 1). Equivalently, it equals eight-thirds of pi times the square of the classical
electron radius:

```
σ_T = (8π/3) r_e²   where   r_e = α_em / m_e   [natural units]
```

In the QED formulation, α_em = 1/137.036 is a free parameter taken from experiment.
The electron mass m_e = 0.511 MeV is also a free parameter. Both must be measured;
neither is derived. The formula for σ_T is exact; its numerical value is input-dependent.

---

## Dimensional Folding Explanation

### The DFC derivation chain

In DFC, the Thomson cross-section is not computed from two independent inputs. It follows
from a single substrate parameter — the quartic coupling β — through an unbroken chain.

**Step 1: β → gauge coupling.** The kink background at D5 depth has a phase stiffness
— the restoring force per unit phase winding around the closure. The phase stiffness is
proportional to the square of the kink amplitude divided by the kink width (the precise
coefficient being four-thirds, which is the value of the definite integral of the fourth
power of the hyperbolic secant function over all space):

```
f² = (4/3) φ₀²/λ
```

The ratio of the closure radius to the kink width equals three divided by four times the
quartic coupling:

```
r_U1 / λ = 3 / (4β)
```

The holonomy — the phase accumulated by transporting a field quantum around the D5
closure once — gives the gauge coupling squared as two pi divided by this ratio:

```
g² = 8πβ/3
```

**Step 2: g → α_em(M_Z).** The electromagnetic fine-structure constant at the Z boson
mass scale is obtained by decomposing the common gauge coupling through the electroweak
structure (Weinberg angle θ_W):

```
α_em(M_Z) = α_common × sin²θ_W  →  1/129.6  (DFC)
```

**Step 3: QED running α_em(M_Z) → α_em(0).** The electromagnetic coupling decreases
logarithmically as the energy scale decreases. All charged fermions lighter than M_Z
contribute to the running. The total shift in the inverse coupling from M_Z to zero
momentum transfer — summing the electron, muon, tau, and the five light quarks (u, d,
s, c, b) — is:

```
Δ(1/α) = (2/3π) × Σ_f  N_c × Q_f² × ln(M_Z / m_f)  ≈ 10.46
```

where N_c is the number of colors, Q_f is the electric charge, and the sum runs over all
charged fermions with mass below M_Z. This gives:

```
α_em(0) [DFC] = 1/140.1   (observed: 1/137.036,  −2.2% error)
```

**Step 4: α_em(0) + m_e → σ_T.** The classical electron radius is the fine-structure
constant divided by the electron mass (in natural units). The Thomson cross-section is
eight-thirds of pi times the square of the classical electron radius:

```
r_e = α_em(0) / m_e  →  σ_T = (8π/3) r_e²  =  (8π/3)(α_em(0)/m_e)²
```

DFC prediction:

```
σ_T (DFC) = 6.368 × 10⁻²⁹ m²   (observed: 6.652 × 10⁻²⁹ m²,  −4.3% error)
```

### Error budget

The −4.3% error in σ_T is exactly twice the −2.2% error in α_em(0), because the
cross-section scales as the square of the coupling. The −2.2% error in α_em(0) is
inherited from the 1.3% error in α_em(M_Z), amplified by the running. The error in
α_em(M_Z) traces to a single gap: the physical identification r_U1/λ = 3/(4β) has
been derived from the kink phase stiffness by a heuristic argument, but the formal
derivation of the closure radius r_U1 from substrate dynamics — via a Kaluza-Klein
reduction on the D5 circle or a domain-wall worldvolume calculation — has not yet
been completed (see `foundations/coupling_derivation.md`).

No free parameters are introduced at Steps 2–4. The electron mass m_e is taken from
data (not yet derived from the substrate). When the r_U1/λ derivation is completed,
the entire chain β → g → α_em → σ_T will have no free parameters beyond β itself.

### The Compton cross-section shape

At finite photon energies, the DFC prediction for the Klein-Nishina cross-section shape
— the ratio σ_KN/σ_T as a function of the dimensionless photon energy ε = hν/m_e c² — is
identical to the QED result. This is because the shape depends only on the ratio of
photon energy to electron mass, and both the photon energy and the electron mass appear
in the ratio ε with no additional coupling factors. The shape is a structural prediction
of the QED interaction vertex; DFC reproduces the QED vertex structure through the D2
photon coupling to the D5/D6 electron closure. The normalization (σ_T itself) carries
the 4.3% error; the shape carries none.

---

## Formal Equations

The Thomson cross-section equals eight-thirds of pi times the square of the classical
electron radius, which equals the square of the ratio of the electromagnetic coupling
to the electron mass:

```
σ_T = (8π/3) r_e²   where   r_e = α_em / m_e   [ℏ = c = 1]
```

In SI units, multiply r_e by ℏc to convert from GeV⁻¹ to meters:

```
r_e [m] = α_em × ℏc / (m_e c²)
```

The Klein-Nishina total cross-section, where ε = E_γ / (m_e c²) is the dimensionless
photon energy, gives the reduction factor below the Thomson limit:

```
σ_KN = (3/4) σ_T × { (1+ε)/ε³ × [2ε(1+ε)/(1+2ε) − ln(1+2ε)] + ln(1+2ε)/(2ε) − (1+3ε)/(1+2ε)² }
```

In the limit ε → 0 this reduces exactly to σ_T. At ε = 1 (photon energy = electron
rest mass), σ_KN/σ_T ≈ 0.431.

The DFC coupling chain from β to σ_T:

```
β = 0.0351  [Tier 3 substrate quartic coupling]
  ↓
g² = 8πβ/3 = 0.2941   (g = 0.5423)
  ↓
α_em(M_Z) = g² sin²θ_W / (4π) = 1/129.6   [Route 3B: sin²θ_W = 3/8 at M_c]
  ↓
Δ(1/α) = 10.46   [one-loop QED running, all fermions]
  ↓
α_em(0) = 1/140.1
  ↓
r_e = α_em(0) / m_e,   σ_T = (8π/3)r_e²  =  6.368 × 10⁻²⁹ m²
```

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| σ_T (Thomson limit) | 6.368×10⁻²⁹ m² | 6.652×10⁻²⁹ m² | ✗ −4.3% (systematic) |
| r_e (classical electron radius) | 2.757×10⁻¹⁵ m | 2.818×10⁻¹⁵ m | ✗ −2.2% (systematic) |
| α_em(0) | 1/140.1 | 1/137.036 | ✗ −2.2% (source of all errors) |
| σ_KN → σ_T as E_γ → 0 | verified (exact limit) | exact | ✓ structural |
| σ_KN/σ_T at ε=1 (E_γ = m_e c²) | 0.4307 | ~0.43 | ✓ |
| Error = 2 × α_em error | 4.3% = 2 × 2.2% | — | ✓ error budget confirmed |
| Zero free parameters beyond β and m_e | 0 new params | — | ✓ |

All discrepancies are systematic and inherit from the single 1.3% error in α_em(M_Z),
which itself traces to the unresolved r_U1/λ = 3/(4β) holonomy derivation.

---

## Open Questions

1. **Derive r_U1/λ = 3/(4β) from substrate dynamics:** The physical identification
   of the D5 closure radius r_U1 in terms of the kink parameters φ₀, β, f² has been
   argued heuristically. The formal route is either a Kaluza-Klein reduction of the
   D5 circle or a domain-wall worldvolume calculation. Completing this derivation
   would close the α_em(M_Z) gap and reduce σ_T error from 4.3% to <1%.
   See `foundations/coupling_derivation.md` and `foundations/phase_stiffness_derivation.md`.

2. **Derive the kink-photon interaction vertex from substrate dynamics:** The DFC
   derivation above reproduces the Thomson formula by identifying the D2 massless
   mode (photon) coupling to the D5 kink charge. The vertex factor — which enters
   as e² = α_em in QED — has been supplied by the coupling chain. The substrate
   dynamics that generate this vertex (the D2/D5 interaction term in the DFC
   effective Lagrangian) have not been formally derived. This derivation would promote
   σ_T from a "coupling chain + formula" prediction to a genuine substrate S-matrix
   result. See `equations/s_matrix.py` (stub).

3. **Derive m_e from substrate:** The electron mass appears in σ_T as m_e = 0.511 MeV,
   taken from data. DFC currently takes m_e as input. A substrate derivation of m_e —
   from the dimple potential depth in `foundations/mass_hierarchy.md` — would make
   σ_T derivable from β alone (zero experimental inputs beyond the Planck-scale
   normalization). See `equations/mass_spectrum.py` for the current partial model.

---

## Connections

- `foundations/coupling_derivation.md` — holonomy formula; r_U1/λ derivation gap
- `foundations/phase_stiffness_derivation.md` — kink phase stiffness f² = (4/3)φ₀²/λ
- `equations/scattering_cross_sections.py` — full numerical verification and coupling chain
- `equations/coupling_derivation.py` — β → g → α_em(M_Z) derivation
- `equations/atomic_structure.py` — QED running α_em(M_Z) → α_em(0); hydrogen spectrum
- `equations/kink_scattering.py` — kink-antikink Born phase shift (substrate S-matrix foundation)
- `equations/s_matrix.py` — full S-matrix (stub; needed for vertex derivation)
- `phenomena/light/light.md` — photon as near-D2 massless mode
- `phenomena/particle_physics/particles/electron.md` — electron as D5/D6 kink closure
- `phenomena/quantum/atomic_structure.md` — hydrogen spectrum from same α_em chain
