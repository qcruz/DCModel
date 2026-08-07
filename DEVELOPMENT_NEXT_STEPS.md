# DFC Model — Development Next Steps

**Based on:** Independent Verification (40/40 items, 0 discrepancies, 26 concerns)

---

## Priority 1: Close the EW VEV Gap (High Impact)

**Problem:** EW predictions (M_W, M_Z, G_F, muon lifetime) use observed v = 246.22 GeV, not DFC-derived v = 247.83 GeV.

**Target:** Derive v from DFC parameters alone (g_eff², beta, Lambda_QCD). Recompute M_W, M_Z, G_F from DFC v and characterize the ~0.7% offset.

**Status:** COMPLETE — `equations/ew_vev_gap_analysis.py` (30/30 CONFIRMED, 0 discrepancies). Two independent error sources identified: g₂ coupling (−0.25%) and VEV co-crystallization (+0.65%). With v_DFC: M_W +0.40%, M_Z +0.93%, G_F −1.30%, τ_μ +2.19% — all within T2a threshold. Offset propagates as power law (v¹, v⁻², v⁴) confirmed to 0.01%. Path to closing: derive M_c(D5), M_c(D6) from pure-DFC ECCC (Priority 5).

---

## Priority 2: Derive lambda_0 for Higgs Mass (High Impact)

**Problem:** Higgs prediction (124.4 GeV) depends on lambda_0 = 0.013 from SM vacuum stability, not V(phi).

**Target:** Extract lambda_0 from V(phi) = (1 - phi²)² structure. If quartic self-coupling derives from g_eff² or beta, this becomes a zero-input prediction.

**Status:** COMPLETE (T2a) — `equations/higgs_quartic_from_vphi.py` (30/30 CONFIRMED, 0 discrepancies). Direct derivation: λ₀ = β/4 = 1/(36π) ≈ 0.00884 from V(|Φ|²) coefficient identification [T1 algebraic]. Chain: V(φ) [T0] → V(|Φ|²) [T2a, C117] → λ = β/4 [T1] → SM RG → m_H. Results: m_H(v_DFC) = 122.9 GeV (−1.9%), within T2a 5% threshold. Berger sphere R₄ = 0 confirms quartic from substrate, not curvature [T2a, C58]. Uncertainty: 3.7 → 1.4 GeV (2.7× improvement). T3 improvement: λ₀ = β × sin²θ_W = 1/(24π) gives m_H = 125.1 GeV (−0.12%) via `higgs_lambda0_derivation.py` — the 3/2 factor requires deriving EW projection at D6.

---

## Priority 3: Upgrade String Tension to T2a (Medium Impact)

**Problem:** String tension sigma = Q_top * Lambda_QCD² is T3 (structural/dimensional). Proton mass (934.8 MeV) and rho mass (763.3 MeV) depend on it.

**Target:** Derive sigma from V(phi) via kink profile energy density. S_kink = 4/beta = 36pi is T1 — connect to confining string tension to upgrade three predictions.

**Status:** COMPLETE — σ = Q_top × Λ_QCD² upgraded T3→T2a via center vortex formal proof (`equations/ym_sigma_i4_formal.py`, C295; `equations/ym_sigma_i4_chain.py`, C243). σ_pred = 185440 MeV² (−4.2%, 0 free params). m_p and m_ρ remain T3 (Regge coefficients structural).

---

## Priority 4: Document Lambda_QCD Dual Definition (Low Effort, High Clarity)

**Problem:** Lambda_QCD appears as 304.5 MeV (MS-bar, Nf=3) and 685 MeV (Landau pole) across 82 files. Relationship not documented.

**Target:** Add derivation showing Lambda_Landau = Lambda_MS-bar * exp(factor) with factor from scheme transformation.

**Status:** COMPLETE — `equations/lambda_qcd_scheme_relation.py` (32 checks, 0 discrepancies)

---

## Priority 5: Pure-DFC alpha_s (Medium Impact)

**Problem:** alpha_s ECCC chain uses observed alpha_em(0) = 1/137.036 as input.

**Target:** Close the loop: compute alpha_em(0) entirely from DFC (36pi -> running chain), feed into ECCC.

**Status:** COMPLETE (T2a) -- `equations/alpha_s_pure_dfc.py` (17/17 PASS, 0 discrepancies). Loop closed: 36pi [T1] -> EW running [T2a] -> VP subtraction (leptonic + pQCD, excl. T4 delta^NP) -> 1/alpha_em(0)^DFC = 137.034 (-0.001%) [T2a, error cancellation C351] -> ECCC Direction B -> alpha_s(M_Z) = 0.11821 (+0.006%) with ZERO observed coupling constants as input. T4 gap (delta^NP = 0.00102) shifts alpha_s by only 0.014% due to error cancellation. g_2(M_Z) weakest link CLOSED: T2b -> T2a via `equations/g2_mz_derivation.py` (15/15 PASS, C353). Self-consistent L = ln(M_c/M_Z) from 36pi chain eliminates M_c as independent input; g_2(M_Z) = 0.6531 (+0.29%). Entire chain now T2a throughout.

---

## Priority 6: Neutrino Color Correction T3 -> T2a (Medium Impact)

**Problem:** Color correction delta_d = 1/(6pi) brings neutrino m3/m2 from -8.5% to +0.04%, but correction is T3.

**Target:** Derive delta_d = 1/(6pi) from depth-anchoring mechanism and SU(3) color structure.

**Status:** PLANNED

---

## Priority 7: Mass Mechanism Unification (Ambitious)

**Problem:** Three separate mass mechanisms: Koide (tau), depth-anchoring kappa = ln(m_mu/m_e) (neutrinos), center vortex kappa = 3pi/2 (quarks).

**Target:** Show all three kappa values emerge from a single V(phi) mechanism at different depth levels.

**Status:** PLANNED

---

## Tracking

| # | Item | Effort | Impact | Status |
|---|------|--------|--------|--------|
| 1 | EW VEV from DFC | Medium | High | COMPLETE |
| 2 | Higgs lambda_0 | Hard | High | COMPLETE |
| 3 | String tension derivation | Medium | Medium | COMPLETE |
| 4 | Lambda_QCD documentation | Easy | Medium | COMPLETE |
| 5 | Pure-DFC alpha_s | Hard | Medium | COMPLETE |
| 6 | Neutrino color correction | Medium | Medium | PLANNED |
| 7 | Mass mechanism unification | Very Hard | High | PLANNED |
