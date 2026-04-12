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

**STUB — full derivation not yet written.**

**DFC mechanism direction:**

The key structural elements already identified in `phenomena/particle_physics/particles/neutrinos.md`:

1. **Three mass eigenstates:** The three neutrino mass eigenstates correspond to three
   distinct winding modes of the substrate at the D3/D4 boundary. These are genuine
   distinct configurations with different depth-anchoring depths, giving different
   effective masses through the quadratic sub-threshold anchoring suppression.

2. **Flavor vs. mass basis mismatch:** The flavor eigenstates (nu-e, nu-mu, nu-tau) are
   defined by the D6 SU(2) closure — specifically by which D6 winding state the neutrino
   partners with (it partners with the electron at D6, defining nu-e, etc.). The mass
   eigenstates are defined by the D4 depth anchoring geometry. These two bases are
   generically misaligned, producing mixing.

3. **PMNS mixing angles from closure geometry:** The mixing angles should be determined
   by the projection angles between the D6-defined flavor basis and the D4-defined mass
   basis. Near-maximal mixing of theta-23 ≈ 45° suggests a near-equal projection between
   the second-generation D6 orientation and the second/third mass eigenstates — a
   geometric coincidence that may follow from the SU(3) structure of D7 at the
   three-generation level, but this is not yet derived.

4. **Oscillation formula:** The standard oscillation probability formula (Probability of
   nu-alpha to nu-beta equals the sum over mass eigenstates of squared PMNS matrix elements
   times an oscillatory phase) follows directly from quantum mechanics applied to the
   superposition of mass eigenstates. DFC does not modify this formula — it provides a
   structural account of why the mixing angles and mass splittings have the values they do,
   which the SM takes as inputs.

5. **Why near-maximal mixing (theta-23 ≈ 45°):** This may follow from the near-equality
   of the second and third winding mode depths at the D3/D4 boundary — an approximate
   degeneracy that produces large mixing in the same way that two nearly-degenerate energy
   levels mix strongly.

**Key open derivation:** Compute the PMNS mixing angles from the D4 winding mode geometry.
The target values are theta-12 ≈ 33°, theta-23 ≈ 49°, theta-13 ≈ 8.6°. A successful
derivation would be a Criterion A result (derives SM inputs from first principles).

---

## Consistency Checks

| Check | DFC prediction | Observed | Status |
|---|---|---|---|
| Three oscillating flavors | Three winding modes at D3/D4 boundary → three mass eigenstates | Three flavors confirmed | ✓ structural |
| Oscillation exists | Mass/flavor basis mismatch from D4/D6 geometry mismatch | Confirmed by solar, atmospheric, reactor | ✓ structural |
| theta-23 near-maximal | Near-degeneracy of 2nd/3rd winding modes | 49.1° (near 45°) | not yet derived ✗ |
| theta-13 small | D3/D4-D5/D6 coupling suppression | 8.6° | not yet derived ✗ |
| Mass splittings ratio | Ratio of winding mode depth differences | delta-m-32/delta-m-21 ≈ 34 | not yet derived ✗ |

---

## Open Questions

1. **Derive PMNS mixing angles:** Compute theta-12, theta-23, theta-13 from the geometry of
   winding modes at the D3/D4 boundary and the D6 flavor basis projection angles.

2. **Derive mass-squared differences:** Compute delta-m-squared-21 and delta-m-squared-31
   from the depth spacings of the three winding modes. This requires the same derivation
   as the absolute neutrino mass scale.

3. **Dirac vs. Majorana:** Does the DFC winding-mode neutrino carry a definite CP winding
   orientation (Dirac) or is it self-conjugate (Majorana)? The answer depends on whether
   the D4 winding mode has an antiwinding partner or is its own antiwinding configuration.

4. **CP violation in neutrino sector:** The CP-violating phase delta-CP in the PMNS matrix
   is an additional mixing parameter. Its DFC interpretation is the relative phase angle
   between the D6 flavor orientations and the D4 mass eigenstates across generations.

---

## Connections

- `phenomena/particle_physics/particles/neutrinos.md` — mass and D4 winding structure
- `phenomena/particle_physics/flavor_mixing.md` — quark mixing (CKM) comparison
- `phenomena/particle_physics/cp_violation.md` — CP phase in PMNS matrix
- `foundations/three_generations.md` — why there are exactly three neutrino flavors
- `foundations/dimensional_stack.md` — D3/D4 boundary structure
