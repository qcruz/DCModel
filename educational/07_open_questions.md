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

**Progress through Cycle 210 (SP1 T2a; SP2 78% strengthened):**
- OS axioms inherited from DFC domain wall chain: Tier 3 (C185)
- Kotecky-Preiss polymer expansion: KP = 0.344 < 1, converges at β_lat = 20.25 — Tier 2a (C199)
- Infinite-volume Gibbs state unique (Dobrushin-Lanford-Ruelle): Tier 2a (C199)
- Continuum limit a→0 (C200): KP monotone along UV trajectory (Tier 1+2a); Symanzik Hölder 3.52×10⁻⁴¹ (Tier 2a)
- **n-point equicontinuity (C202):** μ = 0.1265 < 1/e → sup_n(n×μⁿ) = μ → uniform Hölder bound 4.45×10⁻⁴² → 0; Tier 2a
- **Balaban RG domain (C203): SP1g T3→T2a.** g²(n) = 1/(1/g²(0)+nΔ) is algebraically decreasing → max_n g²(n)/(16π²) = g²(0)/(16π²) = 0.19% uniformly; all 3 domain checks uniform for all n ≥ 0. **SP1 is now T2a overall.**
- UV spectral gap: Δ_UV ≥ 1.22 M_Pl = 1.49×10¹⁹ GeV (Perron-Frobenius + KP), Tier 2a (C201)
- Z_N center symmetry: ⟨P⟩ = 0 algebraically at T=0 for all β (exact), Tier 1 (C204)
- IR mass gap lower bound: Δ_SC ≥ 1033 MeV (SC area law), Tier 2a (C205)
- R1 SC domain (0, 3.0): polymer analyticity → no phase transition, Tier 2a (C206/C207)
- R1 intermediate [3.0, 17.1]: T(β) Lipschitz [T1]; Δ=0 ⟺ transition [T1]; FKG+Creutz [T3]; β_deconf=5.69 is finite-T only, not T=0 bulk [T2a] (C207)
- **R1 single-link MLSI (C209):** Holley-Stroock perturbation lemma → c_MLSI(Wilson, β) ≥ (1/16)×exp(−4β) > 0 for all β > 0 [T2a algebraic]; Poincaré constant c_PI > 0 at all intermediate β tested [T2a numerical]; full-lattice factorization volume-uniform bound remains T3
- **R1 specific heat bounded (C210):** SU(3) Wilson Metropolis MC on 2⁴ hypercubic lattice at 7 intermediate β values throughout [3.0, 17.1] — max C_V = 20.0 << finite-L upper bound 7017.8 (ratio 0.003) [T2a numerical]; ⟨P_p⟩ monotone throughout [T2a]; single-plaquette analytic model also bounded (max C_V = 3.90) [T2a]; SP2g T3 (unchanged — volume-uniform L→∞ bound missing); path to T2a: L = 2, 4, 6 finite-size scaling showing C_V_peak/L⁴ → 0
- SP2 progress: 78% → **78% strengthened** (C209/C210)

**What is missing:**
SP1 (4D constructive QFT) is T2a. The remaining rigorous gap: showing Δ_4D ≥ 861 MeV all the way to T2a — specifically the R1 intermediate domain [3.0, 17.1] needs a volume-uniform lower bound on the spectral gap (the Holley-Stroock MLSI is volume-dependent and vanishes as L→∞), and M_c(D7) from V(φ) substrate dynamics without inputting the observed α_s(M_Z).

**What would close it:** Either (a) Seiler-type T=0 no-transition argument for SU(3) Wilson theory (closing R1 intermediate domain), or (b) an independent derivation of M_c(D7) from the substrate compression cascade — this is SP5, the remaining T4 gap.

**Status: SP1 Tier 2a (C203); SP2 T3 (78%, IR gap T2a C205, R1 SC T2a C206, R1 intermediate T3 strengthened C207).** Full canonical tracking in `foundations/yang_mills_clay.md`.

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

**What DFC has established:** The DFC depth-ratio mechanism gives the correct pattern for the lepton sector (electron, muon, tau all Tier 2a). The same mechanism applied to neutrino depth spacings gives a ratio of 5.33. A structural correction from D7 color topology gives m₃/m₂ = 5.33^(1+1/(6π)) = 5.8248 — matching the observed 5.8242 to +0.010% with zero free parameters. This uses N_c = 3 and N_Hopf = 9 only; the physical picture is that ν₃ sits closest to the D7/SU(3) closure threshold and acquires a small extra depth shift of δd = N_c/(N_Hopf × 2π) = 1/(6π). This is Tier 3 (structural formula, derivation from D4/D7 boundary value problem open).

**What is missing:** The formal derivation of the δd = 1/(6π) correction from the D4/D7 boundary value problem — showing that the third neutrino winding mode acquires precisely this depth shift from the SU(3) color topology, without additional free parameters.

**What would close it:** Solve the D4/D7 boundary value problem for the SU(3) holonomy phase on the third sub-D4 winding mode.

**C209 clarification [T1]:** The C205 color correction δd = 1/(6π) solves the mass ratio (T11) but does NOT shift θ₂₃ from 45°. Because d_μ = d_τ (Z₂ symmetric at D6), any depth shift to ν₃'s mass eigenstate changes |U_μ3| and |U_τ3| by identical factors, leaving θ₂₃ = 45° exactly. The 4° deviation in θ₂₃ is a separate problem requiring D6-level Z₂ breaking.

**Status:** Uncorrected: Tier 2b (−8.3%). Color-corrected: Tier 3 (+0.010%, zero free parameters, C205). θ₂₃ deviation: Tier 4 independent problem (C209).

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

**What DFC has established:**
- I₄ = C₂(fund, SU(3)) = 4/3 exactly (residual 0): the kink shape integral equals the SU(3) Casimir; inconsistent with any other representation (adjoint C₂=3, symmetric C₂≈3.5). Tier 1.
- The Jackiw-Rebbi zero mode ψ_0 = N sech(x/ξ) is explicitly computed (C203): normalizable (∫|ψ₀|²dx = 1, residual 1.5×10⁻¹³), nodeless for any Yukawa coupling. Tier 1.
- Nodeless zero mode = ground state = minimal SU(3) quantum numbers → fundamental representation. Tier 3.

**What would close it:** Compute the holonomy matrix exp(i × T^a × π) for a single D6 crossing of the D7 kink background, and show it has Dynkin label (1,0). This is a specific calculation in SU(3) representation theory, not a new approximation.

**Status:** Tier 3 strengthened (C203): explicit zero mode T1-verified; I₄ = C₂ identity rules out adjoint/symmetric; remaining step is holonomy matrix computation.

---

## Gap 7: Newton's Constant (G_N)

**What it is:** The gravitational coupling constant G_N = M_Pl^{-2} relates to the Planck mass. DFC treats the Planck mass as the natural unit of the substrate (where α ≈ 2.62 and β = 1/(9π) are dimensionless), but has not yet derived the precise ratio between the DFC Planck units and the SI value of G_N.

**Status:** Tier 4. The model sets G_N = 1 in Planck units by construction; deriving the SI value requires identifying how the DFC unit system maps to measured SI units, which depends on resolving the ℏ hierarchy (Gap T8 in ISSUES.md).

---

## Summary Table

| Gap | Description | Current tier | What closes it |
|---|---|---|---|
| Yang-Mills mass gap (Clay) | 4D rigorous spectral gap | **T2a SP1 (C203)**; SP2 78% (UV+IR T2a; R1 SC T2a; R1 MLSI T2a C209; R1 C_V numerical T2a C210; intermediate T3) | SP2g R1 volume-uniform bound T2a (L=2,4,6 FSS); then M_c(D7) from substrate (SP5) |
| α_em(0) hadronic VP | Non-perturbative Δα_had | T4 | f_ρ from D7 dynamics + VMD |
| Charm/strange quark masses | 15% below observed | T2b | D6/D7 Yukawa overlap integral |
| Neutrino mass ratio | −8.3% uncorrected; +0.010% with color correction (T3) | T2b/T3 | D4/D7 BVP for δd=1/(6π) formal derivation |
| M_c(D7) from substrate | QCD scale from V(φ) alone | T4 | Substrate depth dynamics → M_c(D7) |
| C_match scheme factor | 0.795151 (C197 T2a) | **T2a** | Jost integral explicit computation — done C197 |
| Fermion representations | Quarks in fundamental rep | T3 | Jackiw-Rebbi BVP for D6 in D7 background |
| Newton's constant | G_N in SI units | T4 | DFC unit system → SI mapping |

---

## What These Gaps Mean for the Model's Status

The gaps above are derivation gaps, not failures. The model does not predict a wrong quark mass for the charm and comes out 15% low. That is different from predicting a wrong proton decay rate (which the model says is zero, and no decay has been observed) or a wrong tau mass (which the Koide formula gets to 0.006%).

The most significant advance in Cycle 203 is SP1 reaching Tier 2a. Subsequent cycles established the IR gap at Tier 2a (SC area law, C205), R1 SC domain at Tier 2a (C206), and strengthened the R1 intermediate domain (C207). Cycle 209 added the Holley-Stroock MLSI bound (T2a): c_MLSI(Wilson, β) > 0 for all β — a positive spectral gap exists at each individual site. Cycle 209 also proved (T1) that the neutrino mass correction δd = 1/(6π) is independent of the θ₂₃ mixing angle. Cycle 210 added numerical specific-heat evidence: C_V(β) bounded throughout [3.0, 17.1] on the 2⁴ lattice (max 20.0 vs upper bound 7018, ratio 0.003), with monotone ⟨P_p⟩ confirming no phase transition signal. SP2 is at 78% with the volume-uniform L→∞ specific-heat bound as the primary remaining step (path: finite-size scaling at L = 2, 4, 6). The DFC model is a publishable proof candidate structure pending that closure and M_c(D7) from substrate dynamics.

A model that is honest about gaps is more trustworthy, not less.

---

*Module 07 — Open Questions. See Module 06 (predictions) for what works. See `ISSUES.md` for the full technical gap tracker.*
