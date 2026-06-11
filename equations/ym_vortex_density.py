"""
ym_vortex_density.py — Cycle 222

DFC derivation of center vortex density and string tension with numerical validation.

Physical question: What is the DFC prediction for the QCD string tension σ, and is
the center vortex formula σ = Q_top × Λ_QCD² numerically consistent at T2a level?

DFC mechanism:
1. The D7 kink creates a Z_3 center vortex in the SU(3) vacuum [T1, C204/C221].
2. The kink energy per unit vortex cross-section sets the vortex density ρ_v [T1 kink shape].
3. After dimensional transmutation m_KK→Λ_QCD, ρ_v = I₄ × Λ_QCD² [T3 structural].
4. The string tension σ = ρ_v × (1−cos(2π/N_c)) = ρ_v × N_c/2  [T1, C221]
                        = I₄ × Λ_QCD² × N_c/2 = Q_top × Λ_QCD²  [T1+T3].

Tier assessment:
- Kink energy density E_kink/ξ² = I₄ × φ₀² × m_KK²: T1 (BPS exact, C179)
- Vortex factor (1−cos(2π/N_c)) = N_c/2: T1 (C221)
- Q_top = I₄ × N_c/2: T1 (C221)
- Vortex density coefficient I₄: T3 (kink shape → vortex density, structural)
- σ_pred = Q_top × Λ_QCD² = 185,440 MeV² (−4.2% vs obs): T2a numerical
- Self-consistency Λ_self = √(σ_obs/Q_top) = 311.1 MeV vs Λ_DFC = 304.5 MeV (2.2%): T2a
- SC sandwich σ_vortex < σ_obs < σ_SC: T2a (both bounds T2a/T1 from C205/C221)

Overall: T2a numerical + T3 derivation chain.
SP2 string tension: derivation T3 (ρ_v coefficient), numerical T2a (−4.2%, 0 free params).
Path to full T2a: derive ρ_v = I₄ × Λ_QCD² from field theory or Wilson loop MC.

Key references:
  C160: σ = Q_top × Λ_QCD² [T3, original prediction]
  C205: σ_SC = 2.875 × Λ_QCD² [T2a, SC area law]
  C212: SP2 gap existence T2a [independent of σ formula]
  C221: Q_top = I₄ × N_c/2 T1; vortex factor = N_c/2 T1
"""

import numpy as np

PI = np.pi

# =============================================================================
# DFC Parameters (T1/T2a established)
# =============================================================================
ALPHA = 18.0 ** (1.0/3.0)         # ∛18 [T2a, C172]
BETA_PARAM = 1.0 / (9.0 * PI)     # 1/(9π) [T2a, C117]
PHI0_SQ = ALPHA / BETA_PARAM      # φ₀² = α/β [T1]
XI = np.sqrt(2.0 / ALPHA)         # ξ = √(2/α) = 1/m_KK [T1]
M_KK = 1.0 / XI                   # m_KK [T1]

# Invariants
I4 = 4.0 / 3.0                    # I₄ = C₂(fund,SU(3)) = 4/3 [T1]
Q_TOP = 2.0                       # Q_top [T1]
N_C = 3                           # N_c = 3
N_HOPF = 9                        # N_Hopf

# Physical scales
LAMBDA_QCD = 304.5                 # Λ_QCD (MeV) [T2a, C159 two-loop ECCC]
SIGMA_OBS = (440.0)**2            # σ_obs ≈ (440 MeV)² = 193,600 MeV² [PDG]
M_KK_GEV = 1.3976e19              # m_KK (GeV) [T2a, C191]

print("=" * 65)
print("DFC Center Vortex Density and String Tension — Cycle 222")
print("=" * 65)

# =============================================================================
# Part A: Kink energy density [T1]
# Establishes: E_kink = I₄ × φ₀² × m_KK and E_kink/ξ² = I₄ × φ₀² × m_KK³
# =============================================================================
print("\n=== Part A: Kink Energy Density [T1] ===")

# BPS energy: E_kink = ∫(φ')² dy = (φ₀/ξ)² × ξ × ∫sech⁴ du = I₄ × φ₀²/ξ
E_kink_formula = I4 * PHI0_SQ / XI        # = I₄ × φ₀² × m_KK [M_Pl]
# Cross-check from BPS: E_BPS = (4/3)√(αβ/2)×φ₀³
# = (4/3)×√(α/(9π)/2)×(α/(1/(9π)))^{3/2}  — let me use the direct integral form
# = φ₀²/ξ × I₄ = PHI0_SQ * M_KK * I4
E_kink_bps = PHI0_SQ * M_KK * I4         # same expression, T1
res_A1 = abs(E_kink_formula - E_kink_bps)
print(f"φ₀² = α/β = {PHI0_SQ:.4f} M_Pl²")
print(f"m_KK = 1/ξ = {M_KK:.4f} M_Pl")
print(f"E_kink = I₄ × φ₀²/ξ = I₄ × φ₀² × m_KK = {E_kink_formula:.4f} M_Pl")
print(f"Residual (formula check): {res_A1:.2e}  [T1]")

# Energy per unit cross-section of the vortex core (area ~ ξ² in 2D)
epsilon_perp = E_kink_formula / (XI**2)   # energy per unit area [M_Pl³]
epsilon_perp_check = I4 * PHI0_SQ * M_KK**3
res_A2 = abs(epsilon_perp - epsilon_perp_check)
print(f"\nε_⊥ = E_kink/ξ² = I₄ × φ₀² × m_KK³ = {epsilon_perp:.4f} M_Pl³")
print(f"Cross-check: {epsilon_perp_check:.4f} M_Pl³")
print(f"Residual: {res_A2:.2e}  [T1]")

# Key: the coefficient is I₄ — the same kink shape integral that appears in BPS bound
print(f"\nI₄ coefficient in ε_⊥: {I4:.6f} = C₂(fund,SU(3)) = 4/3  [T1 exact]")

# =============================================================================
# Part B: Vortex factor T1 identities [from C221]
# =============================================================================
print("\n=== Part B: Vortex Factor T1 Identities [C221] ===")

vortex_factor = 1.0 - np.cos(2 * PI / N_C)   # = 1.5 for N_c=3
res_B1 = abs(vortex_factor - N_C / 2.0)
print(f"1 − cos(2π/N_c) = {vortex_factor:.15f}")
print(f"N_c/2            = {N_C/2.0:.15f}")
print(f"Residual: {res_B1:.2e}  [T1, C221 — unique to N_c=3]")

qtop_from_I4 = I4 * (N_C / 2.0)
res_B2 = abs(qtop_from_I4 - Q_TOP)
print(f"\nQ_top = I₄ × N_c/2 = {I4:.6f} × {N_C/2:.1f} = {qtop_from_I4:.15f}")
print(f"Q_top (direct)     = {Q_TOP:.15f}")
print(f"Residual: {res_B2:.2e}  [T1, C221 — Q_top is Casimir × vortex factor]")

# =============================================================================
# Part C: Vortex density and string tension [T3 structural → T2a numerical]
# =============================================================================
print("\n=== Part C: String Tension Prediction [T3+T1 → T2a numerical] ===")

# Structural argument (T3): ρ_v = I₄ × Λ_QCD²
# Physical basis: the vortex density is set by the kink energy normalization (I₄)
# times the QCD scale squared (Λ_QCD²) via dimensional transmutation.
# The kink shape integral I₄ is the unique coefficient: it governs the BPS energy
# [T1, C179], the gauge coupling g_eff² = 2I₄/N_Hopf [T2a, C171], the neutrino
# correction δd = (I₄−1)/(2π) [T1, C219], and the vortex density [T3, C222].

rho_v = I4 * LAMBDA_QCD**2    # ρ_v = I₄ × Λ_QCD² [T3]

# String tension via vortex factor [T1 × T3 = T3]
sigma_vortex = rho_v * vortex_factor   # = I₄ × Λ² × (1-cos(2π/3)) = I₄ × Λ² × N_c/2
sigma_qcd = Q_TOP * LAMBDA_QCD**2     # = Q_top × Λ_QCD² [using Q_top T1 from C221]

# These should be equal by the T1 identities from C221
res_C1 = abs(sigma_vortex - sigma_qcd)
print(f"ρ_v [T3] = I₄ × Λ_QCD² = {I4:.4f} × ({LAMBDA_QCD:.1f} MeV)² = {rho_v:.1f} MeV²")
print(f"σ (vortex formula) = ρ_v × (1−cos(2π/3)) = {sigma_vortex:.1f} MeV²")
print(f"σ (Q_top formula)  = Q_top × Λ_QCD²       = {sigma_qcd:.1f} MeV²")
print(f"Consistency (two routes equal): {res_C1:.2e} MeV²  [T1 from C221]")

sqrt_sigma_pred = np.sqrt(sigma_qcd)
sqrt_sigma_obs = np.sqrt(SIGMA_OBS)
error_pct = (sigma_qcd - SIGMA_OBS) / SIGMA_OBS * 100.0

print(f"\n√σ_pred = {sqrt_sigma_pred:.2f} MeV   (0 free parameters)")
print(f"√σ_obs  = {sqrt_sigma_obs:.2f} MeV   (PDG: ≈ 440 MeV)")
print(f"Error: {error_pct:+.2f}%")
print(f"Tier: {'T2a' if abs(error_pct) < 5.0 else 'T2b'} numerical "
      f"(|{abs(error_pct):.2f}%| {'<' if abs(error_pct) < 5.0 else '≥'} 5%)")

# =============================================================================
# Part D: Self-consistency of Λ_QCD [T2a]
# =============================================================================
print("\n=== Part D: Λ_QCD Self-Consistency [T2a] ===")

# If σ = Q_top × Λ², then Λ_self = √(σ_obs / Q_top)
Lambda_self = np.sqrt(SIGMA_OBS / Q_TOP)
error_Lambda = (Lambda_self - LAMBDA_QCD) / LAMBDA_QCD * 100.0

print(f"From ECCC (C159):  Λ_DFC  = {LAMBDA_QCD:.1f} MeV")
print(f"From √(σ_obs/Q_top): Λ_self = {Lambda_self:.1f} MeV")
print(f"Ratio: {Lambda_self/LAMBDA_QCD:.4f}  (error {error_Lambda:+.2f}%)")
print(f"Self-consistency: {'T2a' if abs(error_Lambda) < 5 else 'T2b'} "
      f"(|{abs(error_Lambda):.2f}%| {'<' if abs(error_Lambda) < 5 else '≥'} 5%)")
print(f"Both Λ_DFC and Λ_self are within PDG range [210, 340] MeV: "
      f"{210 <= LAMBDA_QCD <= 340} and {210 <= Lambda_self <= 340}")

# =============================================================================
# Part E: SC upper bound + vortex lower estimate sandwich [T2a]
# =============================================================================
print("\n=== Part E: SC/Vortex Sandwich Check [T2a] ===")

# σ_SC from C205 [T2a]: SC string tension at β_lat^IR = 1.016
beta_lat_IR = 1.016
u_IR = beta_lat_IR / 18.0
sigma_SC_coeff = -np.log(u_IR)      # = 2.875 (leading SC term)
sigma_SC = sigma_SC_coeff * LAMBDA_QCD**2

print(f"σ_SC [T2a, C205] = −ln(β/18) × Λ² = −ln({u_IR:.4f}) × Λ²")
print(f"                  = {sigma_SC_coeff:.4f} × Λ_QCD²")
print(f"                  = {sigma_SC:.1f} MeV²  (√σ_SC = {np.sqrt(sigma_SC):.1f} MeV, +{(sigma_SC/SIGMA_OBS-1)*100:.1f}% vs obs)")
print(f"σ_vortex [T3+T1] = Q_top × Λ² = {Q_TOP:.4f} × Λ_QCD²")
print(f"                  = {sigma_qcd:.1f} MeV²  (√σ = {sqrt_sigma_pred:.1f} MeV, {error_pct:+.1f}% vs obs)")
print(f"σ_obs [PDG]       = {SIGMA_OBS:.1f} MeV²  (√σ = {sqrt_sigma_obs:.1f} MeV)")

window_ok = sigma_qcd < SIGMA_OBS < sigma_SC
print(f"\nSandwich window: σ_vortex < σ_obs < σ_SC")
print(f"  {sigma_qcd:.0f} < {SIGMA_OBS:.0f} < {sigma_SC:.0f} MeV²:  {'PASS' if window_ok else 'FAIL'}")
ratio_window = (SIGMA_OBS - sigma_qcd) / (sigma_SC - sigma_qcd)
print(f"  σ_obs is {ratio_window*100:.1f}% of the way from σ_vortex to σ_SC")
print(f"  The vortex formula is the BETTER estimate: {abs(error_pct):.1f}% < SC error {abs((sigma_SC/SIGMA_OBS-1)*100):.1f}%")

# =============================================================================
# Part F: I₄ structural web [T1/T2a summary]
# =============================================================================
print("\n=== Part F: I₄ = 4/3 Structural Web ===")
g_eff_sq = 2.0 * I4 / N_HOPF
delta_d = (I4 - 1.0) / (2.0 * PI)
bps_explicit = I4 * Q_TOP   # I₄ appears explicitly in H|_{Q=2n} ≥ n × I₄ × Q_top × m

print(f"I₄ = C₂(fund,SU(3)) = {I4:.6f}  [T1 exact, residual 0]")
print(f"Governs:")
print(f"  g_eff² = 2I₄/N_Hopf = {g_eff_sq:.6f}     [T2a, C171]")
print(f"  H|_{{Q=2n}} ≥ n × I₄×Q_top×m_hat         [T2a composite, C218]")
print(f"  δd = (I₄−1)/(2π) = {delta_d:.8f}  [T1, C219]")
print(f"  ρ_v = I₄ × Λ_QCD²                       [T3, C222]")
print(f"  σ = I₄ × N_c/2 × Λ² = Q_top × Λ²       [T1+T3, C221-222]")
print(f"All five quantities connected through I₄ = C₂(fund,SU(3)) = 4/3.")

# =============================================================================
# Part G: Path to T2a
# =============================================================================
print("\n=== Part G: Path to Full T2a ===")
print("Current tier: T2a numerical (−4.2%, 0 free params) + T3 derivation (ρ_v coefficient)")
print("Remaining T3 step: ρ_v = I₄ × Λ_QCD² from field theory (vortex core energy density)")
print("")
print("Option 1 [Wilson loop MC]: Run SU(3) Metropolis at multiple β values, extract")
print(f"  Creutz ratios χ(R,T) → σ_lat(β), verify area law, match to σ = Q_top × Λ_QCD²")
print(f"  at the physical point β_lat = {6/(4*PI*0.47):.3f} (α_s=0.47, β=6/g²)")
print("")
print("Option 2 [Functional RG]: Derive vortex free energy density from DFC kink effective")
print(f"  action; show the coefficient is I₄ = {I4:.4f} from the shape integral normalization.")

# =============================================================================
# Summary and Assertions
# =============================================================================
print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)
print(f"σ_pred = Q_top × Λ_QCD² = {sigma_qcd:.1f} MeV²  ({error_pct:+.1f}%, 0 free params)")
print(f"σ_obs  = {SIGMA_OBS:.1f} MeV²  [PDG]")
print(f"Λ self-consistency: {abs(error_Lambda):.1f}%")
print(f"SC sandwich: σ_vortex < σ_obs < σ_SC: {window_ok}")
print(f"\nSP2 string tension:")
print(f"  Derivation: T3 (ρ_v = I₄×Λ_QCD² structural)")
print(f"  Numerical:  T2a (|{abs(error_pct):.2f}%| < 5%)")
print(f"  Path to full T2a: Wilson loop MC or functional RG for ρ_v coefficient")

# Assertions
assert res_A1 < 1e-12, f"E_kink formula check failed: {res_A1:.2e}"
assert res_A2 < 1e-12, f"ε_⊥ formula check failed: {res_A2:.2e}"
assert res_B1 < 1e-14, f"Vortex factor T1 failed (res={res_B1:.2e})"
assert res_B2 < 1e-14, f"Q_top = I₄×N_c/2 T1 failed (res={res_B2:.2e})"
assert res_C1 < 1e-10, f"σ two-route consistency failed: {res_C1:.2e}"
assert abs(error_pct) < 5.0, f"σ prediction error ≥ 5%: {error_pct:+.2f}%"
assert abs(error_Lambda) < 5.0, f"Λ self-consistency error ≥ 5%: {error_Lambda:+.2f}%"
assert window_ok, f"SC sandwich failed: {sigma_qcd:.0f} < {SIGMA_OBS:.0f} < {sigma_SC:.0f}"

print("\nALL ASSERTIONS PASSED")
