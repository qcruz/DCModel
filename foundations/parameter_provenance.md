# DFC Prediction Provenance Table

**Purpose:** Complete transparency about every claimed prediction — what goes in,
what comes out, what was fitted, what was derived, and whether each result was
obtained before or after comparison with experiment.

**Last updated:** Cycle 592

---

## Input Classification

Every input to a DFC prediction falls into one of four categories:

| Category | Symbol | Description | Examples |
|----------|--------|-------------|----------|
| **A: DFC-derived** | (DFC) | Computed from V(phi) postulates with no observational input | alpha, beta, g_eff, I_4, Q_top, S_kink |
| **B: SM structural** | (SM) | Mathematical consequences of gauge theory; not free parameters | Beta function coefficients, QED loop integrals, CKM structure |
| **C: Observational** | (OBS) | Numerical values taken from experiment | m_e, m_t, M_Z, alpha_em(0), Omega_m |
| **D: DFC geometric** | (GEO) | Model-specific adjustable parameters fitted to data | R (dimple ratio), d (dimple depth), lambda_0, M_c |

A prediction with only Category A inputs is genuinely parameter-free.
A prediction using Category C or D inputs inherits those values from experiment.

---

## Core DFC Constants (Category A)

These are derived from V(phi) = -alpha/2 phi^2 + beta/4 phi^4 and its topology:

| Constant | Value | Derivation | Tier |
|----------|-------|-----------|------|
| alpha | cuberoot(18) = 2.6207 | BPS saturation condition | T2a |
| beta | 1/(9*pi) = 0.03537 | Instanton normalization on S^3 | T2a |
| phi_0 | sqrt(alpha/beta) = 8.608 | Vacuum amplitude (derived) | T1 |
| xi | sqrt(2/alpha) = 0.8736 | Kink half-width (derived) | T1 |
| m_sigma | sqrt(2*alpha) = 2.289 | Scalar mass at vacuum (derived) | T1 |
| g_eff^2 | 8/27 = 0.2963 | 2*I_4/N_Hopf from kink Yukawa | T2a |
| I_4 | 4/3 | Exact kink integral | T1 |
| Q_top | 2 | BPST topological charge | T1 |
| N_Hopf | 9 | dim(S^3) + dim(S^5) + dim(fiber) | T1 |
| S_kink | 4*sqrt(2*alpha)/(3*beta) | BPS energy (Bogomolny bound) | T1 |

---

## Full Provenance Table

### Tier 2a Predictions (< 5% error)

---

#### 1. Common gauge coupling g_eff = 0.5443

| Field | Value |
|-------|-------|
| **Module** | `d5_complex_from_instability.py` |
| **Starting assumptions** | V(phi) double-well; D5 tachyonic complexification produces O(2) extension; kink-antikink Yukawa coupling |
| **Derivation** | g_eff^2 = 2*I_4 / N_Hopf = 2*(4/3)/9 = 8/27; g_eff = sqrt(8/27) = 0.54433 |
| **DFC inputs** | I_4 = 4/3 (T1 exact integral), Q_top = 2, N_Hopf = 9 |
| **SM structural inputs** | None |
| **Observational inputs** | None |
| **Fitted/geometric params** | None |
| **Output** | g_eff = 0.54433 |
| **Observed** | SM coupling ~0.5443 |
| **Error** | 0.006% |
| **Pre/post-diction** | **Pre-diction** — derived from V(phi) topology before comparison |
| **Honest assessment** | Genuinely 0 free parameters. Pure DFC algebra. The strongest prediction. |

---

#### 2. Quartic coupling beta = 1/(9*pi)

| Field | Value |
|-------|-------|
| **Module** | `d5_complex_from_instability.py` |
| **Starting assumptions** | O(2) symmetric extension of V(phi); moduli space metric |
| **Derivation** | R_1 = 2*pi/g_1^2 = pi/I_4; self-consistency gives beta = 1/(N_Hopf * pi) = 1/(9*pi) |
| **DFC inputs** | I_4 = 4/3, N_Hopf = 9 |
| **SM structural inputs** | None |
| **Observational inputs** | None |
| **Fitted/geometric params** | None |
| **Output** | beta = 1/(9*pi) = 0.03537 |
| **Observed** | (postulated, not independently measurable) |
| **Error** | N/A (defines the model) |
| **Pre/post-diction** | **Pre-diction** — derived from consistency of V(phi) |
| **Honest assessment** | Pure DFC. But beta is part of the model definition, so calling it a "prediction" is slightly misleading — it's a self-consistency result. |

---

#### 3. Muon-to-electron mass ratio = 206.77

| Field | Value |
|-------|-------|
| **Module** | `mass_spectrum.py` |
| **Starting assumptions** | Leptons are quantum modes of fermion in D6 closure potential with Gaussian dimple |
| **Derivation** | Infinite square well + dimple perturbation. n=1 (electron) gets full dimple shift; n=2 (muon) has node at dimple center, gets zero dimple correction. Ratio = 4*E_box / (E_box - E_dimple) |
| **DFC inputs** | D6 closure geometry (structural) |
| **SM structural inputs** | None |
| **Observational inputs** | m_e = 0.511 MeV (PDG), m_mu = 105.66 MeV (PDG) — used to FIT parameters |
| **Fitted/geometric params** | **R (dimple radius ratio), d (dimple depth) — 2 fitted parameters** |
| **Output** | m_mu/m_e = 206.77 |
| **Observed** | 206.77 |
| **Error** | 0.0% |
| **Pre/post-diction** | **Post-diction (fitted)** — R and d are chosen to reproduce m_e and m_mu. The ratio is guaranteed by construction. |
| **Honest assessment** | This is a FIT, not a prediction. Two parameters fitted to two data points gives zero predictive content for the ratio itself. The actual prediction (tau mass from n=3 mode) fails at 8.4x. Superseded by Koide route. |

---

#### 4. Neutron lifetime = 878.4 s

| Field | Value |
|-------|-------|
| **Module** | `proton_stability.py` |
| **Starting assumptions** | DFC product topology U(1) x SU(2) x SU(3); proton stability from topological charge conservation; neutron decay via standard SU(2) weak process |
| **Derivation** | Standard Fermi beta-decay: Gamma = G_F^2 * m_e^5 * |V_ud|^2 * f(Q) / (2*pi^3); phase space integral f(Q) computed numerically; EW radiative correction +3.9% |
| **DFC inputs** | Topological stability of proton (Q_top conservation) |
| **SM structural inputs** | Fermi V-A theory; EW radiative corrections; phase space integral |
| **Observational inputs** | G_F = 1.166e-5 GeV^-2 (PDG), m_n, m_p, m_e (PDG), V_ud = 0.97373 (CKM), hbar |
| **Fitted/geometric params** | None |
| **Output** | tau_n = 878.4 s |
| **Observed** | 879.4 s (PDG average) |
| **Error** | 0.1% |
| **Pre/post-diction** | **Post-diction** — uses standard SM weak decay formula. DFC adds proton stability (topological) but the neutron lifetime calculation is standard physics. |
| **Honest assessment** | DFC's contribution is proton stability (T1 topological), not the neutron lifetime value. The lifetime is computed from SM inputs. Labeling this as a "DFC prediction" overstates the DFC-specific content. |

---

#### 5. Hubble constant H_0 = 67.26 km/s/Mpc

| Field | Value |
|-------|-------|
| **Module** | `cosmology.py` |
| **Starting assumptions** | Compression field lateral redistribution produces Hubble expansion; Friedmann-like equation |
| **Derivation** | H^2 = (8*pi*G/3) * rho_total; standard LCDM with DFC interpretation |
| **DFC inputs** | Conceptual framework (compression = expansion) |
| **SM structural inputs** | Friedmann equation; LCDM cosmology |
| **Observational inputs** | **Omega_m = 0.315, Omega_Lambda = 0.685 (Planck 2018), G_N, T_CMB — 2+ observational inputs** |
| **Fitted/geometric params** | None beyond cosmological parameters |
| **Output** | H_0 = 67.26 km/s/Mpc |
| **Observed** | 67.4 km/s/Mpc (Planck 2018) |
| **Error** | -0.2% |
| **Pre/post-diction** | **Post-diction** — uses Planck-measured density parameters as inputs |
| **Honest assessment** | This is standard LCDM cosmology with DFC providing an interpretation, not a novel derivation of H_0. The value comes from the observed Omega values. |

---

#### 6. Higgs boson mass = 124.4 +/- 3.7 GeV

| Field | Value |
|-------|-------|
| **Module** | `higgs_potential.py` |
| **Starting assumptions** | DFC beta = 1/(9*pi) sets boundary condition for Higgs quartic lambda at M_c; S^3 squashing geometry |
| **Derivation** | lambda(M_c) ~ 0.013 from DFC boundary condition; SM 1-loop RG running M_c -> v gives lambda(v) ~ 0.129; m_H^2 = 2*lambda(v)*v^2 |
| **DFC inputs** | beta = 1/(9*pi) (boundary condition at M_c) |
| **SM structural inputs** | SM beta functions for lambda, g_t, g_s; vacuum stability analysis |
| **Observational inputs** | v = 246 GeV (EW VEV), m_t = 172.76 GeV (PDG), M_Z, M_W |
| **Fitted/geometric params** | **lambda_0 = 0.013 +/- 0.007 (from SM vacuum stability, 1 param)** |
| **Output** | m_H = 124.4 +/- 3.7 GeV |
| **Observed** | 125.25 GeV |
| **Error** | 0.7% |
| **Pre/post-diction** | **Mixed** — the DFC boundary condition was set before LHC discovery, but the RG running and lambda_0 range come from SM vacuum stability analysis (Buttazzo+ 2013). The prediction overlaps the observed value. |
| **Honest assessment** | The DFC-specific content is the boundary condition beta -> lambda(M_c). The SM RG running is standard. The large uncertainty (+/- 3.7 GeV) encompasses the observed value but is not sharply predictive. Uses 1 geometric param + 3-4 SM mass inputs. |

---

#### 7. Weinberg angle sin^2(theta_W) = 0.2312

| Field | Value |
|-------|-------|
| **Module** | `weinberg_angle_rg.py` |
| **Starting assumptions** | Equal-coupling initial condition alpha_1 = alpha_2 at closure scale M_c (Route 3B); sin^2(theta_W)(M_c) = 3/8 |
| **Derivation** | sin^2(theta_W)(M_Z) = 3/8 - [109/(48*pi)] * alpha_em * ln(M_c/M_Z); M_c from SM coupling crossing |
| **DFC inputs** | Equal-coupling condition at M_c (structural) |
| **SM structural inputs** | Beta functions b_1 = 41/10, b_2 = 19/6; GUT normalization k_Y = sqrt(5/3) |
| **Observational inputs** | alpha_em(M_Z) = 1/127.9, M_Z = 91.188 GeV |
| **Fitted/geometric params** | **M_c (closure scale, 1 param — determined by self-consistent crossing)** |
| **Output** | sin^2(theta_W) = 0.2312 |
| **Observed** | 0.23122 |
| **Error** | 0.01% |
| **Pre/post-diction** | **Post-diction** — the 3/8 initial condition is standard GUT physics (Georgi-Glashow 1974). DFC reframes it as "equal coupling at closure" but the formula and M_c determination use the same SM running as GUT models. |
| **Honest assessment** | The calculation is identical to standard GUT sin^2(theta_W) running. DFC provides a reinterpretation (closure scale = unification scale) but the numerical result is not novel. 1 geometric param (M_c). |

---

#### 8. alpha_em(M_Z) = 1/128.09

| Field | Value |
|-------|-------|
| **Module** | `alpha_em_prediction.py` |
| **Starting assumptions** | ECCC: 1/alpha_em(M_c) = 36*pi at the EW closure scale; EW running M_c -> M_Z |
| **Derivation** | 1/alpha_em(M_Z) = 36*pi + (11/(6*pi)) * ln(M_c/M_Z) |
| **DFC inputs** | g_eff^2 = 8/27 (determines 36*pi via co-crystallization) |
| **SM structural inputs** | EW running rate 11/(6*pi); beta function structure |
| **Observational inputs** | M_Z = 91.188 GeV (to set endpoint of running) |
| **Fitted/geometric params** | None (M_c determined by ECCC self-consistency) |
| **Output** | 1/alpha_em(M_Z) = 128.09 |
| **Observed** | 1/127.9 |
| **Error** | +0.15% |
| **Pre/post-diction** | **Pre-diction** — the 36*pi formula is derived from g_eff before comparison with data. The running to M_Z uses SM machinery. |
| **Honest assessment** | The 36*pi result is genuinely DFC-derived and predictive. The running uses SM beta functions. Overall: 0 adjustable params, 1 SM structural input (beta function), 1 observational input (M_Z). |

---

#### 9. alpha_s(M_Z) = 0.11821

| Field | Value |
|-------|-------|
| **Module** | `alpha_em_selfconsistency.py` |
| **Starting assumptions** | ECCC closure condition: alpha_3(M_c(D7)) = alpha_common; structural identity M_c(D7)/M_c(D5) = 1/alpha_em(0) |
| **Derivation** | (1) t_5 from g_2; (2) t_7 = t_5 + ln(1/alpha_em(0)); (3) invert beta_3 to get alpha_s |
| **DFC inputs** | ECCC identity (structural), g_eff^2 = 8/27 |
| **SM structural inputs** | Beta function b_3 = 7; SM coupling running |
| **Observational inputs** | **alpha_em(0) = 1/137.036 (INPUT from CODATA)** |
| **Fitted/geometric params** | None |
| **Output** | alpha_s(M_Z) = 0.11821 |
| **Observed** | 0.11820 |
| **Error** | +0.006% |
| **Pre/post-diction** | **Post-diction** — uses observed alpha_em(0) as input to predict alpha_s. The ECCC identity connecting the two is the DFC content. |
| **Honest assessment** | This is a genuine and impressive RELATIONSHIP prediction: given alpha_em(0), DFC predicts alpha_s to 0.006%. But it uses 1 observational input. The DFC-specific content is the ECCC identity linking electromagnetic and strong couplings. |

---

#### 10. W boson mass = 80.38 GeV (1-loop corrected)

| Field | Value |
|-------|-------|
| **Module** | `ew_radiative_corrections.py` |
| **Starting assumptions** | DFC coupling chain -> tree M_W; SM Sirlin Delta_r corrections |
| **Derivation** | M_W from M_Z, alpha_em, G_F via Sirlin formula; Delta_r includes top loop (Delta_rho), EW VP (Delta_alpha), Higgs screening |
| **DFC inputs** | DFC alpha_em chain |
| **SM structural inputs** | Sirlin Delta_r formalism; SM loop integrals |
| **Observational inputs** | **M_Z = 91.188 GeV, m_t = 172.76 GeV, m_H = 125.25 GeV, G_F (4 inputs)** |
| **Fitted/geometric params** | None beyond the 4 observational inputs |
| **Output** | M_W = 80.38 GeV |
| **Observed** | 80.377 GeV |
| **Error** | +0.009% |
| **Pre/post-diction** | **Post-diction** — standard EW precision calculation using observed masses |
| **Honest assessment** | This is standard SM EW precision physics. DFC provides the coupling chain but the numerical result is determined by the 4 observed inputs. Labeling "(+m_t, m_H)" as the free params is correct and honest. |

---

#### 11. Z boson mass = 90.86 GeV

| Field | Value |
|-------|-------|
| **Module** | `muon_lifetime.py` |
| **Starting assumptions** | M_Z = M_W / cos(theta_W); couplings from DFC chain |
| **Derivation** | Tree-level EW relation |
| **DFC inputs** | sin^2(theta_W) from Route 3B, g_2 from coupling chain |
| **SM structural inputs** | EW tree relation rho = 1 |
| **Observational inputs** | v = 246 GeV (EW VEV) |
| **Fitted/geometric params** | 2 (v, coupling chain) |
| **Output** | M_Z = 90.86 GeV |
| **Observed** | 91.188 GeV |
| **Error** | -0.36% |
| **Pre/post-diction** | **Pre-diction** — derived from coupling chain without using M_Z as input |
| **Honest assessment** | Genuine prediction from the coupling chain. The -0.36% error reflects accumulated errors in sin^2(theta_W) and v. |

---

#### 12. Fermi constant G_F = 1.168e-5 GeV^-2

| Field | Value |
|-------|-------|
| **Module** | `muon_lifetime.py` |
| **Starting assumptions** | G_F = g_2^2 / (4*sqrt(2)*M_W^2) from EW gauge theory |
| **Derivation** | Standard tree-level relation |
| **DFC inputs** | g_2 from coupling chain |
| **SM structural inputs** | Tree EW relation |
| **Observational inputs** | v = 246 GeV, M_W from DFC chain |
| **Fitted/geometric params** | 2 (inherits from coupling chain) |
| **Output** | G_F = 1.168e-5 GeV^-2 |
| **Observed** | 1.1664e-5 GeV^-2 |
| **Error** | +0.18% |
| **Pre/post-diction** | **Pre-diction** — derived from coupling chain |

---

#### 13. Muon lifetime = 2.180 microseconds

| Field | Value |
|-------|-------|
| **Module** | `muon_lifetime.py` |
| **Starting assumptions** | Fermi theory with DFC G_F |
| **Derivation** | tau_mu = 192*pi^3*hbar / (G_F^2 * m_mu^5) |
| **DFC inputs** | G_F from coupling chain |
| **SM structural inputs** | Fermi V-A theory |
| **Observational inputs** | **m_mu = 105.66 MeV (PDG), hbar** |
| **Fitted/geometric params** | 3 (inherited: v, coupling chain, m_mu) |
| **Output** | tau_mu = 2.180 microseconds |
| **Observed** | 2.197 microseconds |
| **Error** | -0.80% |
| **Pre/post-diction** | **Pre-diction** — m_mu is an input but tau_mu is derived |

---

#### 14. Z total width = 2456 MeV

| Field | Value |
|-------|-------|
| **Module** | `z_boson_decays.py` |
| **Starting assumptions** | SM Z decay formulas with DFC-derived couplings |
| **Derivation** | Gamma(Z->ff) = N_c * G_F * M_Z^3 / (6*pi*sqrt(2)) * (g_V^2 + g_A^2); sum over all channels |
| **DFC inputs** | sin^2(theta_W), alpha_s from DFC chain |
| **SM structural inputs** | Z decay rate formula; QCD correction (1 + alpha_s/pi) |
| **Observational inputs** | **M_Z = 91.188 GeV, alpha_s = 0.118** |
| **Fitted/geometric params** | 2 |
| **Output** | Gamma_Z = 2456 MeV |
| **Observed** | 2495 MeV |
| **Error** | -1.56% |
| **Pre/post-diction** | **Pre-diction** — decay rates derived from coupling structure |

---

#### 15. Tau lepton mass (Koide) = 1776.97 MeV

| Field | Value |
|-------|-------|
| **Module** | `koide_phase_coupling.py` |
| **Starting assumptions** | Z_3 subset of SU(3) at 3 coincident D7 kinks; circulant Yukawa matrix Y_nm = Y_nn * exp(i*gamma) / sqrt(Q_top) |
| **Derivation** | t = 1/sqrt(Q_top) = 1/sqrt(2); K = 1/3 + 2*t^2/3 = 2/3; invert Koide formula with K=2/3, m_e, m_mu -> m_tau |
| **DFC inputs** | Q_top = 2 (determines Koide phase parameter t = 1/sqrt(2)) |
| **SM structural inputs** | Koide formula structure |
| **Observational inputs** | **m_e = 0.511 MeV (INPUT), m_mu = 105.66 MeV (INPUT)** |
| **Fitted/geometric params** | None |
| **Output** | m_tau = 1776.97 MeV |
| **Observed** | 1776.86 MeV |
| **Error** | +0.006% |
| **Pre/post-diction** | **Pre-diction** — the DFC connection Q_top -> Koide phase was derived before computing m_tau. But: Koide himself found K=2/3 empirically in 1981, so the VALUE was known. DFC provides a REASON for K=2/3 (from Q_top=2), not the formula itself. |
| **Honest assessment** | Impressive: 2 inputs (m_e, m_mu) -> 1 output (m_tau) with 0.006% accuracy. DFC contributes the reason K=2/3 (from Q_top). But this is an empirical formula with a DFC interpretation, not a first-principles derivation of m_tau from V(phi). Steps 0-3 are T2a; step 4 (|F_0|/|F_1|=sqrt(2)) remains T4. |

---

#### 16. Electron anomalous magnetic moment a_e

| Field | Value |
|-------|-------|
| **Module** | `anomalous_magnetic_moment.py` |
| **Starting assumptions** | 36*pi chain -> alpha_em(0) = 1/137.226; QED perturbative series |
| **Derivation** | a_e = sum_n C_n (alpha/pi)^n; C_1=1/2, C_2=-0.3285, C_3=+1.1812, C_4=-1.9130 |
| **DFC inputs** | alpha_em from 36*pi chain (0.14% offset from observed) |
| **SM structural inputs** | **QED 4-loop coefficients C_1-C_4 (exact U(1) vertex integrals)** |
| **Observational inputs** | None beyond DFC alpha |
| **Fitted/geometric params** | None |
| **Output** | a_e = 0.001158 |
| **Observed** | 0.001160 |
| **Error** | -0.14% |
| **Pre/post-diction** | **Post-diction** — the 36*pi alpha was known to differ from observed alpha before computing a_e. The QED coefficients are standard (Aoyama+ 2019). |
| **Honest assessment** | DFC provides alpha; QED provides the formula. The 0.14% error directly inherits from the alpha gap. If the alpha gap were closed, a_e would match. Not an independent test of DFC — it's a consistency check of the alpha chain. |

---

#### 17. Lamb shift = 1050.5 MHz

| Field | Value |
|-------|-------|
| **Module** | `lamb_shift.py` |
| **Starting assumptions** | 36*pi alpha; Bethe self-energy + Uehling VP |
| **Derivation** | Leading: Delta_E proportional to alpha^5; includes Bethe logarithm ln(K_0)=2.8118 |
| **DFC inputs** | alpha_em from 36*pi chain |
| **SM structural inputs** | **QED self-energy (Bethe 1947), vacuum polarization (Uehling), higher-order corrections** |
| **Observational inputs** | Bethe logarithm calibrated to H atom |
| **Fitted/geometric params** | None |
| **Output** | 1050.5 MHz |
| **Observed** | 1057.845 MHz |
| **Error** | -0.69% |
| **Pre/post-diction** | **Post-diction** — uses DFC alpha in standard QED formula |
| **Honest assessment** | Same as a_e: error inherits from alpha gap. Standard QED calculation with DFC alpha substituted. |

---

### Tier 2b Predictions (equation exists; >5% error or partial)

---

#### 18. Thomson cross-section = 6.633e-29 m^2

| Field | Value |
|-------|-------|
| **Module** | `scattering_cross_sections.py` |
| **Starting assumptions** | sigma_T = 8*pi*r_e^2/3; r_e = alpha/(m_e*c^2) |
| **DFC inputs** | alpha_em from 36*pi chain |
| **Observational inputs** | m_e (PDG) |
| **Error** | -0.28% |
| **Pre/post-diction** | Post-diction (standard formula with DFC alpha) |

---

#### 19. Hydrogen ground state E_1 = -13.568 eV

| Field | Value |
|-------|-------|
| **Module** | `atomic_structure.py` |
| **Starting assumptions** | E_1 = -m_e * alpha^2 / 2 (Bohr model) |
| **DFC inputs** | alpha_em from 36*pi chain |
| **Observational inputs** | m_e (PDG) |
| **Error** | +0.28% |
| **Pre/post-diction** | Post-diction (Bohr formula with DFC alpha) |

---

#### 20. Neutrino mass ratio m_3/m_2

| Field | Value |
|-------|-------|
| **Module** | `neutrino_masses.py` |
| **Starting assumptions** | D3.x shallow anchoring to D4; three winding modes |
| **Derivation** | Exponential suppression at D3-D4 boundary |
| **DFC inputs** | Anchoring depth model |
| **Observational inputs** | **Delta_m^2_21, |Delta_m^2_31| (oscillation data)** |
| **Fitted/geometric params** | f_nu (anchoring fraction) |
| **Output** | kappa = 5.33 |
| **Observed** | 5.81 |
| **Error** | -8.3% |
| **Pre/post-diction** | Post-diction (oscillation data used as input) |

---

#### 21. Proton mass (Regge) = 934.8 MeV

| Field | Value |
|-------|-------|
| **Module** | `baryon_mass_dfc.py` |
| **Starting assumptions** | m_p = sqrt(3*pi) * Lambda_QCD; Y-junction intercept alpha_0^N = -1/4 |
| **DFC inputs** | Q_top = 2 (Regge slope sigma = Q_top * Lambda^2), s_JR = 1/2 (junction penalty) |
| **SM structural inputs** | Regge trajectory formula |
| **Observational inputs** | **Lambda_QCD ~ 304 MeV (from SM running)** |
| **Fitted/geometric params** | None beyond Lambda_QCD |
| **Output** | m_p = 934.8 MeV |
| **Observed** | 938.3 MeV |
| **Error** | -0.4% |
| **Pre/post-diction** | **Pre-diction** — the formula m_p = sqrt(3*pi)*Lambda_QCD with alpha_0^N=-1/4 was derived from DFC before comparison. But Lambda_QCD is an SM input. |

---

#### 22. EW VEV v = 247.83 GeV

| Field | Value |
|-------|-------|
| **Module** | `ewsb_cocrystallization.py` |
| **Starting assumptions** | D5/D6 co-crystallization; ECCC mechanism |
| **DFC inputs** | g_eff^2 = 8/27, N_Hopf, Q_top, beta |
| **SM structural inputs** | Dimensional transmutation; SM beta functions |
| **Observational inputs** | SM coupling running (implicit) |
| **Fitted/geometric params** | **M_c(D5), M_c(D6) — 2 closure scales from ECCC** |
| **Output** | v = 247.83 GeV |
| **Observed** | 246.22 GeV |
| **Error** | +0.65% |
| **Pre/post-diction** | **Mixed** — ECCC provides structure, but closure scales are determined from SM running which knows v. |

---

#### 23. Charm and strange quark masses

| Field | Value |
|-------|-------|
| **Module** | `quark_mass_kappa_derivation.py` |
| **Starting assumptions** | Center vortex gives kappa_q = pi*N_c/2 generation scaling |
| **DFC inputs** | N_c = 3 (from D7 closure topology), pi (geometric) |
| **SM structural inputs** | None |
| **Observational inputs** | **m_s = 93.4 MeV, m_c = 1270 MeV (PDG — used as CHECK)** |
| **Fitted/geometric params** | None — kappa_q is derived |
| **Output** | m_c/m_s = pi*N_c/2 = 4.712; m_c = 1273.7 MeV, m_s = 95.4 MeV |
| **Observed** | m_c = 1270 MeV, m_s = 93.4 MeV |
| **Error** | +0.29% (charm), +2.09% (strange) |
| **Pre/post-diction** | **Pre-diction** — kappa_q derived from center vortex before comparison |

---

#### 24. Proton charge radius r_p = 0.809 fm

| Field | Value |
|-------|-------|
| **Module** | `proton_charge_radius_dfc.py` |
| **Starting assumptions** | VMD pion cloud model; kink width xi determines core |
| **DFC inputs** | xi, alpha, beta |
| **SM structural inputs** | VMD; pion cloud physics |
| **Observational inputs** | **f_pi, m_pi, Lambda_QCD** |
| **Error** | -3.8% |
| **Pre/post-diction** | Post-diction |

---

## Summary Statistics

### By pre/post-diction status

| Status | Count | Examples |
|--------|-------|---------|
| **Genuine pre-diction** (derived before comparison) | 6 | g_eff, beta, alpha_em(M_Z), M_Z (tree), G_F, charm/strange kappa |
| **Structural pre-diction** (DFC gives reason for known formula) | 3 | Koide m_tau (DFC explains K=2/3), proton mass (Regge), Delta mass |
| **Post-diction** (uses observed values as input) | 10 | tau_n, H_0, a_e, Lamb shift, m_mu/m_e, sin^2(theta_W) |
| **Mixed/ambiguous** | 5 | m_H, v_EW, W mass, alpha_s (ECCC) |

### By input category

| Category | Truly 0-param (Cat A only) | 1-2 SM inputs | 3+ SM inputs | Fitted |
|----------|--------------------------|---------------|---------------|--------|
| Count | 2 (g_eff, beta) | 8 | 10 | 4 |

### Honest parameter count

| Parameter type | Count | Values |
|----------------|-------|--------|
| **DFC core constants** (derived from V(phi)) | 2 | alpha = cuberoot(18), beta = 1/(9*pi) |
| **DFC topological invariants** (exact) | 3 | I_4 = 4/3, Q_top = 2, N_Hopf = 9 |
| **DFC geometric (fitted)** | 4 | R, d (mass spectrum), lambda_0, M_c |
| **SM structural (inherited)** | ~7 | b_1, b_2, b_3, k_Y, C_2-C_4, N_f=6 |
| **Observational (from PDG)** | ~10 | m_e, m_mu, m_t, m_H, M_Z, alpha_em(0), G_F, V_ud, Omega_m, Lambda_QCD |

### Overall assessment

The DFC model has **2 genuinely parameter-free predictions** (g_eff and beta) that are
pure V(phi) algebra. An additional **~6 predictions** use only DFC-derived inputs plus
SM structural formulas (no observational tuning). The remaining **~16 predictions** use
1-4 observational inputs from PDG and should be labeled as such.

The model's strongest results are:
1. **g_eff^2 = 8/27** — pure topology, 0.006% match
2. **alpha_s from ECCC** — 1 SM input (alpha_em), 0.006% match (relationship prediction)
3. **Koide m_tau** — 2 inputs (m_e, m_mu), DFC explains WHY K=2/3
4. **36*pi chain** — alpha_em(M_Z) from DFC algebra, 0.15% match

The model's most overstated claims are:
1. **m_mu/m_e = 206.77** — listed as "0.0% error" but is a 2-parameter fit
2. **tau_n = 878.4 s** — is standard SM physics, not DFC-specific
3. **H_0 = 67.26** — is standard LCDM with observed Omega values
