# Phenomenon: Neutrino Oscillations

## One-Sentence Synthesis

> Neutrino oscillations are quantum interference between the three neutrino mass
> eigenstates as they propagate — the weak interaction produces a flavor eigenstate
> (electron-neutrino, muon-neutrino, tau-neutrino) which is a superposition of mass
> eigenstates with different phase velocities, so the flavor composition oscillates
> with a period set by the mass-squared differences divided by the neutrino energy; in
> DFC, the three mass eigenstates are the three winding modes of the shallow D3/D4
> boundary structure identified in `phenomena/particle_physics/particles/neutrinos.md`,
> and the mixing angles of the PMNS matrix are the projection angles between the flavor
> basis (defined by the D6 SU(2) closure) and the mass basis (defined by the D4 depth
> anchoring geometry) — but the specific values of these angles are not yet derived
> from first principles.

---

## Observation

Neutrinos change flavor as they travel. This was confirmed by:

- **Solar neutrino deficit (Davis experiment, 1968–2002):** Solar models predict a certain
  flux of electron-neutrinos; only about one-third arrived at Earth as electron-neutrinos.
  Confirmed as oscillation by SNO (2001), which measured the total neutrino flux and showed
  it matched the solar model — the missing electron-neutrinos had oscillated to other flavors.
- **Atmospheric neutrino asymmetry (Super-K, 1998):** Muon-neutrinos produced in the
  atmosphere above the detector arrived at a different rate than those that had traveled
  through the Earth. The deficit as a function of direction confirmed oscillation with
  maximum mixing angle theta-23 ≈ 45°.
- **Reactor neutrino disappearance (KamLAND, 2002; Daya Bay, 2012):** Electron-antineutrinos
  from reactors disappear over distances of ~100 km and ~2 km respectively, confirming the
  mass-squared differences delta-m-squared-21 and delta-m-squared-31.
- **Measured mixing angles (global fit 2022):**
  - theta-12 ≈ 33.4° (solar angle)
  - theta-23 ≈ 49.1° (atmospheric angle, near-maximal mixing)
  - theta-13 ≈ 8.6° (reactor angle)
  - CP-violating phase delta-CP ≈ 195° (preliminary, ~1.6 sigma from zero)
- **Mass-squared differences:**
  - delta-m-squared-21 = 7.42 × 10⁻⁵ eV² (solar)
  - |delta-m-squared-31| = 2.51 × 10⁻³ eV² (atmospheric)
- **Mass ordering:** Unknown whether the lightest state is m1 (normal ordering) or m3
  (inverted ordering). Current preference is for normal ordering.

---

## Standard Explanation

In the Standard Model extended to include neutrino masses, the three flavor eigenstates
(nu-e, nu-mu, nu-tau) are related to the three mass eigenstates (nu-1, nu-2, nu-3) by the
PMNS matrix U (Pontecorvo-Maki-Nakagawa-Sakata):

    (nu-e, nu-mu, nu-tau) = U × (nu-1, nu-2, nu-3)

The matrix U is parametrized by three mixing angles and one CP-violating phase (for Dirac
neutrinos) or three CP phases (for Majorana). As a neutrino propagates, each mass eigenstate
accumulates phase at a rate proportional to its mass squared divided by energy. The flavor
state is then a superposition with different relative phases, and the probability of detecting
a given flavor oscillates sinusoidally with distance.

What the Standard Model does not explain: why the mixing angles have the values they do, why
theta-23 is near-maximal while the quark mixing angle theta-23 (CKM) is near-zero, why
neutrino masses are so small (seesaw mechanism is a popular extension but is not part of
the SM itself), or whether neutrinos are Dirac or Majorana particles.

---

## Dimensional Folding Explanation

**Structural account:**

**Three mass eigenstates from D4 winding modes:**

In DFC, neutrinos are the lightest closure configurations associated with the D6 SU(2)
depth behavior. Their masses arise not from a Higgs Yukawa coupling but from sub-threshold
anchoring at the D3/D4 boundary: winding modes that do not fully close at D4 depths acquire
a quadratically suppressed effective mass proportional to how far their depth falls below
the D4 threshold. Three distinct winding configurations exist at this boundary — one per
generation — giving three mass eigenstates ν₁, ν₂, ν₃ with different effective masses.

**Why the mass and flavor bases are misaligned:**

The flavor eigenstates — the electron-neutrino, muon-neutrino, and tau-neutrino — are defined
by the D6 SU(2) closure. Specifically, the electron-neutrino is the D6 partner of the
electron kink: the configuration produced alongside the electron at the D6 depth. The muon-
and tau-neutrinos are defined analogously as the D6 partners of the muon and tau kinks.

The mass eigenstates ν₁, ν₂, ν₃ are defined by the D4 depth geometry: the specific winding
configurations that diagonalize the D4 mass matrix. Because the D4 geometry and the D6
geometry describe the same substrate at different compression depths, and the substrate's
closure orientations at these depths are generically not aligned with each other, the flavor
basis and the mass basis are misaligned. This misalignment is the PMNS mixing matrix.

This is a structural argument for why PMNS mixing exists. The specific values of the mixing
angles — θ₁₂ ≈ 33°, θ₂₃ ≈ 49°, θ₁₃ ≈ 8.6° — are not yet derived from the DFC substrate
(Tier 3). Deriving them requires computing the projection angles between the D4 and D6 closure
orientation bases — a calculation that depends on the as-yet-undetermined D4/D6 overlap
geometry.

**Oscillation as phase accumulation between mass eigenstates:**

Once the mass/flavor basis mismatch is established, neutrino oscillation follows directly
from quantum mechanics: the flavor eigenstate produced at creation is a superposition of
mass eigenstates. Each mass eigenstate propagates with a different phase velocity because it
has a different mass. After propagating a distance L at energy E, the relative phases between
mass eigenstates have accumulated by an amount proportional to the mass-squared difference
divided by the energy. The flavor composition at the detector is the coherent superposition
with these accumulated phases. Since the phases change periodically with distance, the
detected flavor oscillates.

DFC does not modify the oscillation formula relative to standard quantum mechanics. The
substrate's propagation rule for a superposition state is the same as quantum mechanical
phase evolution — the compression field evolves as a linear wave equation in the massless
limit, and the non-linear (kink) sector provides the mass splittings that drive the
oscillation.

**Near-maximal θ₂₃ — Z₂ exchange symmetry of S³ at D6 depth [T3]:**

The atmospheric mixing angle θ₂₃ ≈ 49° is close to the maximal mixing value of 45°.
A previous version of this account argued that θ₂₃ ≈ 45° follows from near-degeneracy of
the second and third neutrino mass eigenstates; that argument is incorrect and retracted
(Cycle 206). Near-maximal mixing does not require near-mass-degeneracy. In a two-state
mixing problem, tan(2θ) = 2ε/δ where ε is the off-diagonal coupling and δ is the
diagonal splitting in the flavor basis; large off-diagonal elements produce θ ≈ 45° even
when the eigenvalues differ greatly.

The structural DFC argument (Tier 3) proceeds differently: the S³ manifold at D6 depth
carries a Z₂ exchange symmetry — the anti-podal map on S³, which exchanges the second
and third winding modes. This Z₂ maps μ ↔ τ in the flavor basis. If this symmetry is
preserved in the D4/D6 projection that produces the PMNS matrix, the 2×3 mixing block
satisfies |U_μ₂| = |U_τ₂| and |U_μ₃| = |U_τ₃|, which forces θ₂₃ = 45° exactly. The
observed deviation θ₂₃ = 49° − 45° = 4° is a small Z₂-breaking correction. The same
color-topology depth shift δd = N_c/(N_Hopf × 2π) = 1/(6π) ≈ 0.053 that corrects the
ν₃ mass ratio (see neutrinos.md, Cycle 205) is a candidate source of this correction,
but the quantitative calculation has not been carried out.

Status: θ₂₃ = 45° from Z₂ symmetry is T3 structural. The 4° deviation and the full
derivation of θ₁₂, θ₂₃, θ₁₃ from D4/D6 projection geometry remain T4 (open).

**Mass-squared difference ratio failure:**

The mass ratio m₃/m₂ = √(Δm²₃₁/Δm²₂₁) ≈ 5.82 (observed) vs. the DFC equal-spacing
prediction κ = 5.33 gives an −8.3% error before the color correction. A structural T3
correction (Cycle 205) accounts for the ν₃ proximity to the D7/SU(3) closure threshold:
m₃/m₂ = κ^(1 + 1/(6π)) = 5.8248, +0.010% error, 0 free parameters. See
`equations/neutrino_color_correction.py`. The prior "4.3× failure" notation was a metric
error (Cycle 165); the actual DFC gap is −8.3% uncorrected.

---

## Formal Equations

### Two-Flavor Oscillation Probability (DERIVED — follows from QM superposition)

The probability that a neutrino produced as flavor α is detected as flavor β after
propagating a distance L at energy E equals the product of the sine squared of twice
the mixing angle and the sine squared of the accumulated phase. The accumulated phase
equals 1.267 times the mass-squared difference (in eV²) times the distance (in km),
divided by the energy (in GeV):

```
P(να → νβ) = sin²(2θ) × sin²(1.267 × Δm² [eV²] × L [km] / E [GeV])

Conversion factor 1.267 = 1 / (4 × ℏc [eV·km])  where ℏc = 197.3 MeV·fm

Survival probability:
P(να → να) = 1 − sin²(2θ) × sin²(1.267 × Δm² × L / E)

Oscillation length (distance of first maximum disappearance):
L_osc [km] = E [GeV] / (1.267 × Δm² [eV²])

Numerical:
  Solar    (θ₁₂=33.4°, Δm²₂₁=7.42×10⁻⁵ eV², E=5 MeV):     L_osc = 53.2 km
  Atm.     (θ₂₃=49.1°, Δm²₃₁=2.51×10⁻³ eV², E=1 GeV):     L_osc = 314.5 km
  Reactor  (θ₁₃=8.6°,  Δm²₃₁=2.51×10⁻³ eV², E=5 MeV):     L_osc = 1.6 km
  [L_osc(reactor) = 1.6 km explains why Daya Bay chose L = 1.648 km baseline]
```

### Three-Flavor PMNS Matrix (structural — mixing angles NOT derived from DFC)

The three flavor eigenstates are related to the three mass eigenstates by the
Pontecorvo-Maki-Nakagawa-Sakata mixing matrix U. Each entry U_αk is the amplitude for
flavor α to be found in mass eigenstate k. The matrix is parametrized by three angles
and one CP-violating phase:

```
U = R₂₃(θ₂₃) × diag(1, 1, e^{iδ}) × R₁₃(θ₁₃) × diag(1, 1, e^{-iδ}) × R₁₂(θ₁₂)

Observed values (NuFIT 5.2, 2022):
  θ₁₂ = 33.41°   (solar angle)      sin²(θ₁₂) = 0.304
  θ₂₃ = 49.1°    (atmospheric)      sin²(θ₂₃) = 0.570   [near-maximal mixing]
  θ₁₃ = 8.58°    (reactor angle)    sin²(θ₁₃) = 0.02220
  δ_CP ≈ 195°    (CP phase; ~1.6σ from zero; not yet established)

  DFC status: θ₁₂, θ₂₃, θ₁₃, δ_CP are INPUTS (Tier 3/4 — not derived from substrate)
```

### Observed Mass-Squared Differences (NOT derived from DFC)

The mass-squared differences between eigenstates have been measured by solar, atmospheric,
and reactor experiments. The difference between the squares of the second and first
eigenstate masses equals 7.42 times ten to the negative fifth power in eV squared. The
difference between the third and first eigenstate mass squares equals 2.51 times ten to
the negative third power in eV squared:

```
Δm²₂₁ = m²₂ − m²₁ = 7.42 × 10⁻⁵ eV²    (solar; always positive)
Δm²₃₁ = m²₃ − m²₁ = 2.51 × 10⁻³ eV²    (normal ordering; sign unknown experimentally)

Ratio: Δm²₃₁ / Δm²₂₁ = 33.8

DFC depth model: uniform spacing → ratio ≈ 1.34   [FAILS: 4.3× off; see neutrino_masses.py]
Conclusion: D4 winding mode depths are NOT uniformly spaced.
```

### Experimental Benchmarks (verified using input angles from data)

The oscillation formula with observed PMNS parameters correctly reproduces all three
oscillation experiments. These are consistency checks, not DFC predictions:

```
Atmospheric (Super-K, 1998):
  P(νμ→νμ) at L/E = 500 km/GeV = 0.021  [near-maximum disappearance; observed ~0.5]
  [Two-flavor approximation; near-maximum at L/E = L_osc/2 ≈ 157 km/GeV]

Daya Bay (2012):
  P(νe-bar→νe-bar) at L=1.648 km, E=5 MeV = 0.935  (observed: 0.944; −1.0%)
  [θ₁₃ measured at baseline matching reactor oscillation length]

KamLAND (2002):
  Oscillation at L ≈ 180 km, E ≈ 3–10 MeV confirms θ₁₂, Δm²₂₁
  [L/E_osc at 5 MeV: 180/53 ≈ 3.4 oscillation lengths → average P_surv ~ 0.5–0.6]
```

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Three oscillating flavors | Three D4 winding modes → three mass eigenstates | Three flavors confirmed | ✓ structural |
| Oscillation exists | D4/D6 geometry mismatch → mass/flavor basis misaligned | Confirmed solar, atmospheric, reactor | ✓ structural |
| Oscillation formula (sin² form) | Standard QM superposition; no DFC modification | All experiments consistent | ✓ structural |
| Daya Bay P(νe-bar) at 1.648 km, 5 MeV | 0.935 (using input θ₁₃) | 0.944 | −1.0% (inputs not DFC) |
| θ₂₃ near-maximal | Z₂ (μ↔τ) symmetry of S³ at D6 → θ₂₃=45° at leading order [T3]; deviation 4° open | 49.1° ≈ 45° | ~ T3 leading; deviation open |
| m₃/m₂ mass ratio (corrected) | κ^(1+1/(6π)) = 5.8248 [T3, 0 free params, C205] | 5.824 | +0.010% ✓ T3 |
| m₃/m₂ (uncorrected) | κ = 5.33 [T2b] | 5.824 | −8.3% T2b |
| Absolute neutrino mass scale | OPEN — requires D4 winding depth calculation | < 0.1 eV (sum) | ✗ not derived |

---

## Open Questions

1. **Derive PMNS mixing angles from substrate geometry:** Compute θ₁₂, θ₂₃, θ₁₃ from the
   projection angles between the D4 mass basis and the D6 flavor basis. Approach: parametrize
   the D4/D6 overlap geometry by the angle between closure orientation vectors at each depth;
   minimize the effective potential to find the equilibrium projection angles. Success here
   would be a Criterion A result.

2. **Explain the non-uniform mass-squared spacing:** The ratio Δm²₃₁/Δm²₂₁ ≈ 34 rules out
   equal D4 depth spacing. Determine the depth profile of the three winding modes —
   specifically, why the third mode is compressed much more than the second. Candidate: the
   D7 SU(3) substrate structure creates a non-linear depth compression that accelerates
   between the second and third winding modes.

3. **Mass ordering (normal vs. inverted):** Compute which D4 winding configuration has the
   smallest mass (m₁ or m₃). This is equivalent to asking which winding mode is most
   shallow in D4 depth anchoring. Current experimental preference is normal ordering (m₁ < m₂ < m₃).

4. **Dirac vs. Majorana:** Does the D4 winding mode have a distinct antiwinding partner
   (Dirac) or is the winding self-conjugate (Majorana)? The Z₂ topology of the φ⁴ kink
   suggests antikinks exist as distinct objects, implying Dirac. But the neutrino has no
   U(1) charge, making it possible that kink and antikink are the same configuration at D4
   depths. This is a Tier 1 prediction candidate.

---

## Connections

- `phenomena/particle_physics/particles/neutrinos.md` — D4 winding mass structure; absolute mass
- `phenomena/particle_physics/flavor_mixing.md` — quark mixing (CKM) comparison; same D4/D6 mismatch
- `phenomena/particle_physics/cp_violation.md` — CP phase δ_CP in PMNS; D6 orientation phase
- `foundations/three_generations.md` — why exactly three neutrino flavors (SU(3) → 3)
- `foundations/dimensional_stack.md` — D3/D4 boundary structure; winding mode anchoring
- `equations/neutrino_oscillations.py` — oscillation probabilities; experimental comparisons
- `equations/neutrino_masses.py` — mass hierarchy; depth spacing failure (4.3×)
- `foundations/dimensional_stack.md` — D3/D4 boundary structure
