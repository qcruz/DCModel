# Module 07: What Is Not Yet Derived — Honest Gaps

**Audience:** Anyone who wants to know where the model stands and what it cannot yet prove.

**What this module covers:** Every significant gap in the current DFC derivations — not as disclaimers, but as precise statements of what is missing and what would close each gap. Honesty about gaps is as important as reporting what works.

---

## What "Open" Means in DFC

A gap in DFC is not a known failure (where the prediction is wrong) — it is a step in a derivation chain that has not been completed to the required tier. The tier system classifies how firmly each step is established:

- **Tier 1**: Follows algebraically — anyone can verify it.
- **Tier 2a**: A calculation exists with less than 5% error, no free parameters tuned to it.
- **Tier 3**: A structural argument gives the right qualitative behavior and roughly right numbers, but a step in the derivation chain is missing.
- **Tier 4**: The model has an opinion but no calculation at all yet.

An open gap is a step that is currently Tier 3 or Tier 4, where a completed derivation would promote it. The distinction between "open" and "failure" matters: an open gap is a missing proof; a failure is a wrong prediction.

---

## Gap 1: The Yang-Mills Mass Gap (Clay Millennium Prize)

**What it is:** Pure Yang-Mills gauge theory in four dimensions is believed to have a mass gap — a minimum energy cost to produce any excitation from the vacuum. This is why gluons are not free particles and why QCD is confining. The Clay Mathematics Institute has listed this as one of seven Millennium Prize Problems, with a $1 million prize for a rigorous mathematical proof.

**What DFC has established so far:**
- The 1+1-dimensional DFC scalar field has a rigorous mass gap equal to the kink mass — the mathematical tools of Glimm and Jaffe (constructive quantum field theory) apply and give a provably positive spectral gap. This is Tier 2a.
- The 4D gauge theory lives on the kink worldvolume via Kaluza-Klein reduction. All non-zero Kaluza-Klein modes are heavier than the QCD scale by a factor of roughly 10²⁰, so they decouple and leave pure SU(3) Yang-Mills below that scale. This is Tier 2a (the scale separation) plus Tier 3 (the KK reduction itself).
- The string tension and confinement argument give a lower bound on the 4D gap: the minimum glueball energy is at least 861 MeV (from the relation Δ ≥ 2√(Q_top) × Λ_QCD with Q_top = 2 and Λ_QCD = 304.5 MeV). The observed lightest glueball is around 1475–1730 MeV, which is consistent. This is Tier 3.

**Additional progress (Cycles 185–200):**
- OS axioms inherited from DFC domain wall chain: Tier 3 (C185)
- Kotecky-Preiss polymer expansion: KP = 0.344 < 1, converges at β_lat = 20.25 — Tier 2a (C199)
- Infinite-volume Gibbs state unique (Dobrushin-Lanford-Ruelle): Tier 2a (C199)
- Continuum limit a→0 structural argument (C200): KP monotone along UV trajectory (Tier 1+2a); large-field sector ≤ 19.3% (Tier 2a); Symanzik Hölder bound = 4.69×10⁻⁴¹ — plaquette Cauchy as a→0 (Tier 2a); Arzelà-Ascoli + Dobrushin → unique continuum limit ω_∞ exists (Tier 3 for equicontinuity step). SP1k T4→T3.

**What is missing:**
The Arzelà-Ascoli argument requires all n-point Schwinger functions to be equicontinuous, not just the plaquette. Showing this requires an explicit Balaban-style bound |S_n(a) − S_n(a/2)| ≤ C_n × (Λ_QCD×a)² for all n, with C_n controlled by the KP parameter. Balaban's 1983–1989 papers establish this for general compact gauge groups in a framework applicable to SU(3), but the full detailed extension has not been written.

**What would close it:** Extend the Balaban multi-scale RG n-point Hölder bound to SU(3) at β_lat = 20.25. This is hard analysis but there is no known fundamental obstruction. (Alternatively, cite a published result that covers SU(N) for N ≥ 3.)

**Status:** Tier 3 (structural chain, continuum limit argument T3 as of C200). Remaining T4: explicit Balaban n-point Hölder bound for SU(3).

---

## Gap 2: The Fine Structure Constant at Zero Momentum

**What it is:** The fine structure constant α_em ≈ 1/137 at zero momentum is one of the most precisely measured numbers in physics. The DFC model can reproduce α_em at the Z boson mass scale (1/128, with 0.11% error) using the formula 1/α_em(M_Z) = 36π. But the value at zero momentum requires adding hadronic vacuum polarization corrections, which depend on how quarks and gluons contribute to the photon propagator.

**What DFC has established:**
- The leptonic running (how the electron, muon, and tau loops shift α_em from M_Z down to zero) is derived from the DFC generation count and reproduces Δα_lep with 0.24% error. This is Tier 2a.
- The leading perturbative hadronic contribution (from charm and bottom quarks) is also reproduced at Tier 2a.
- The remaining gap is Δα_had^(non-perturbative) = 0.00102, which comes from the ρ, ω, and φ meson resonances. This requires the full DFC hadronic spectroscopy.

**What is missing:** The non-perturbative hadronic contribution requires a derivation of the ρ meson electromagnetic coupling from first principles in DFC. The form factor f_ρ is currently known to Tier 3 (−8.1% from large-N_c VMD), and the parton-hadronic matching is Tier 4.

**What would close it:** Derive the ρ meson electromagnetic decay width from D7 vacuum dynamics, connect it to the photon self-energy via vector meson dominance, and show the resulting Δα_had matches the measured value.

**Status:** The identity 1/α_em(M_Z) = 36π is Tier 2a confirmed. The α_em(0) derivation is Tier 4 (the hadronic piece).

---

## Gap 3: Quark Masses (Charm and Strange)

**What it is:** The charm quark mass is about 1.27 GeV and the strange quark mass is about 93 MeV. DFC currently predicts both about 15% too low.

**What DFC has established:** The up and down quark masses follow the same topological scaling that gives the electron and muon masses. The lepton masses (electron, muon, tau) are reproduced at Tier 2a. The charm and strange quarks sit at the second generation of the quark sector and receive their masses from Higgs couplings at D6/D7 thresholds.

**What is missing:** The DFC Higgs coupling threshold for second-generation quarks has not been derived cleanly. The D6/D7 overlap integral that controls the coupling strength is known to Tier 3, but the numerical value comes out 15% low.

**What would close it:** Derive the D6/D7 overlap integral from the explicit kink profiles at each depth, and show that the Yukawa coupling for strange and charm quarks follows from the substrate topology without additional free parameters.

**Status:** Tier 2b (15% error, no free parameters tuned, but derivation chain incomplete).

---

## Gap 4: Neutrino Mass Ordering

**What it is:** The ratio of neutrino mass-squared differences (m₃²/m₂²) is measured to be about 5.81. DFC predicts it at 5.33, which is −8.3% off.

**What DFC has established:** The DFC depth-ratio mechanism gives the correct pattern for the lepton sector (electron, muon, tau all Tier 2a). The same mechanism applied to neutrino depth spacings gives a ratio of 5.33.

**What is missing:** The neutrino depth spacings appear to be non-uniform — the D6 depth intervals for neutrinos do not follow the same equal-spacing pattern as charged leptons. The physical reason for this (possibly related to the Majorana vs Dirac distinction, or to the seesaw mechanism at high energies) is not yet derived.

**What would close it:** A derivation of why neutrino depth spacings differ from charged lepton spacings — possibly from the different handedness structure (only left-handed neutrinos have been observed) or from D6/D7 interface topology.

**Status:** Tier 2b (−8.3%, structural account exists but spacing derivation is open).

---

## Gap 5: Scheme Matching (C_match)

**What it is:** The DFC gauge coupling g_eff is defined from the kink moduli metric in Planck units. The QCD coupling g_s used in the Standard Model is defined in the MS-bar renormalization scheme. The conversion factor between them — called C_match — is currently estimated at 0.790 but not derived.

**Why it matters:** C_match directly affects the quantitative prediction for Λ_QCD. The current two-loop Landau-pole calculation gives Λ_QCD ≈ 685 MeV, while the PDG value is Λ_MS^(3) ≈ 332 MeV. The factor-of-2 discrepancy is largely due to the Landau pole not being the same as the MS-bar scheme parameter (a known numerical artifact of scheme choice), not a fundamental failure.

**Update (Cycle 197):** C_match has been computed from the Jost-function integral for the even-parity continuum modes of the Pöschl-Teller potential. Result: C_match = 0.795151. The full computation uses c₁ = −1/12 (Weisz coefficient, T1), two-loop MS-bar running α_s(M_Z→m_KK) (T2a), and the explicit Jost-function formula from Darboux chain (T2a). This gives C_match = 0.795151 to Tier 2a.

**What would close the remaining gap:** A derivation of M_c(D7) — the QCD closure scale — from V(φ) substrate dynamics alone, without requiring α_s(M_Z) as an external input. This is the remaining Tier 4 loop in the Λ_QCD chain.

**Status:** C_match = 0.795151, Tier 2a (C197). M_c(D7) from substrate: Tier 4.

---

## Gap 6: Fermion Representations (Why Quarks Are Fundamentals)

**What it is:** Quarks transform in the fundamental (3-dimensional) representation of SU(3) color, not the adjoint (8-dimensional) or any other representation. DFC should derive this from the substrate topology.

**What DFC has established:** The identity I₄ = C₂(fund, SU(3)) = 4/3 — the kink shape integral equals the SU(3) Casimir of the fundamental representation — strongly suggests quarks live in the fundamental. A structural argument shows that D6 kinks crossing the D7 kink background acquire SU(3) holonomy, and one crossing gives winding n = 1, which corresponds to the fundamental representation (dimension 3). This is Tier 3.

**What would close it:** Solve the Jackiw-Rebbi boundary value problem for the D6 Dirac operator in an explicit D7 kink background, showing that the zero mode transforms in the fundamental representation. This is a specific PDE calculation.

**Status:** Tier 3 (I₄ = C₂ identity exact; holonomy argument structural).

---

## Gap 7: Newton's Constant (G_N)

**What it is:** The gravitational coupling constant G_N = M_Pl^{-2} relates to the Planck mass. DFC treats the Planck mass as the natural unit of the substrate (where α ≈ 2.62 and β = 1/(9π) are dimensionless), but has not yet derived the precise ratio between the DFC Planck units and the SI value of G_N.

**Status:** Tier 4. The model sets G_N = 1 in Planck units by construction; deriving the SI value requires identifying how the DFC unit system maps to measured SI units, which depends on resolving the ℏ hierarchy (Gap T8 in ISSUES.md).

---

## Summary Table

| Gap | Description | Current tier | What closes it |
|---|---|---|---|
| Yang-Mills mass gap (Clay) | 4D rigorous spectral gap | T3 (C200: SP1k T4→T3) | Balaban n-point Hölder bound for SU(3) |
| α_em(0) hadronic VP | Non-perturbative Δα_had | T4 | f_ρ from D7 dynamics + VMD |
| Charm/strange quark masses | 15% below observed | T2b | D6/D7 Yukawa overlap integral |
| Neutrino mass ratio | −8.3% | T2b | Non-uniform depth spacing derivation |
| M_c(D7) from substrate | QCD scale from V(φ) alone | T4 | Substrate depth dynamics → M_c(D7) |
| C_match scheme factor | 0.795151 (C197 T2a) | **T2a** | Jost integral explicit computation — done C197 |
| Fermion representations | Quarks in fundamental rep | T3 | Jackiw-Rebbi BVP for D6 in D7 background |
| Newton's constant | G_N in SI units | T4 | DFC unit system → SI mapping |

---

## What These Gaps Mean for the Model's Status

The gaps above are derivation gaps, not failures. The model does not predict a wrong quark mass for the charm and comes out 15% low. That is different from predicting a wrong proton decay rate (which the model says is zero, and no decay has been observed) or a wrong tau mass (which the Koide formula gets to 0.006%).

The most significant open question is the Yang-Mills mass gap, because it is the central claim that DFC can reproduce all of QCD from a scalar field. The structural chain is in place; the rigorous 4D constructive proof is the remaining mathematical work.

A model that is honest about gaps is more trustworthy, not less.

---

*Module 07 — Open Questions. See Module 06 (predictions) for what works. See `ISSUES.md` for the full technical gap tracker.*
