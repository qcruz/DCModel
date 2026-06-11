#!/usr/bin/env python3
"""
ym_string_tension.py — Cycle 220: String tension σ = I₄ × Λ_QCD²
and Casimir scaling of color flux tubes.

Physical question:
  What is the color string tension in the DFC framework, and how does the
  kink shape integral I₄ = C₂(fund,SU(3)) = 4/3 control it?

DFC mechanism:
  The BPS Hamiltonian H ≥ I₄ × Q_top × m_hat [T2a, C218] shows that I₄ = C₂(fund)
  controls the mass gap. For the string tension (energy per unit length of the color
  flux tube connecting a quark-antiquark pair), the same I₄ appears as the color
  Casimir of the source representation. Casimir scaling (lattice-supported):
    σ_R / σ_fund = C₂(R) / C₂(fund) = C₂(R) / I₄

  Absolute string tension:  σ_fund = I₄ × Λ_QCD²  [T3]
  Casimir ratio (exact):    σ_adj/σ_fund = C₂(adj)/I₄ = N_c/I₄ = 9/4  [T1]

Key references:
  C205: SC area law σ_SC = 2.875 Λ_QCD² [T2a]
  C218: BPS H|_{Q=2n} ≥ n × I₄ × Q_top × m_hat [T2a]
  C219: δd = (I₄−1)/(2π) [T1] — structural web
  C160: σ = Q_top × Λ_QCD² = 2Λ² (kink-counting, T3, −1.7%)
  C177/C215: I₄ = C₂(fund,SU(3)) = 4/3 [T1]
"""

import numpy as np
from scipy.integrate import quad

# ============================================================
# Constants
# ============================================================
PI     = np.pi
N_C    = 3           # SU(3) color
I4     = 4.0 / 3.0   # kink shape integral = C₂(fund,SU(3)) [T1]
Q_TOP  = 2           # DFC topological charge per kink [T1]
N_HOPF = 9           # Hopf fiber dimension sum 1+3+5 [T1]
BETA   = 1.0/(9*PI)  # substrate quartic coupling [T2a, C117]
G_EFF2 = 8.0/27.0    # gauge coupling squared [T2a, C117]

# QCD scales (MeV)
LAMBDA_QCD_DFC = 304.5   # DFC 2-loop value [T2a, C159]
LAMBDA_QCD_PDG = 332.0   # PDG Λ_MS^(3)  [T2a]

# SC string tension coefficient (C205, T2a)
SIGMA_SC_COEFF = 2.875   # σ_SC = 2.875 × Λ_QCD²

# Observed string tension (phenomenology, √σ ≈ 420-440 MeV)
SQRT_SIGMA_OBS = 430.0   # MeV, central estimate

# ============================================================
# Part A: Casimir invariants [T1]
# ============================================================
print("=" * 60)
print("PART A: Casimir Invariants [T1]")
print("=" * 60)

# Fundamental: C₂(fund) = (N_c²-1)/(2N_c)
C2_fund = (N_C**2 - 1) / (2.0 * N_C)
res_A_identity = abs(C2_fund - I4)
print(f"C₂(fund,SU({N_C})) = (N_c²−1)/(2N_c) = {C2_fund:.10f}")
print(f"I₄ = ∫sech⁴(u) du  = 4/3           = {I4:.10f}")
print(f"Identity I₄ = C₂(fund): residual {res_A_identity:.2e}  [T1]")

# Adjoint: C₂(adj) = N_c
C2_adj = float(N_C)
print(f"\nC₂(adj,SU({N_C})) = N_c = {C2_adj:.4f}  [T1]")

# Casimir ratio
r_cas = C2_adj / C2_fund   # = 3 / (4/3) = 9/4
r_cas_exact = 9.0 / 4.0
res_A_ratio = abs(r_cas - r_cas_exact)
print(f"\nCasimir ratio C₂(adj)/C₂(fund) = N_c/I₄ = 3/(4/3) = 9/4")
print(f"  Computed: {r_cas:.10f}")
print(f"  Exact:    {r_cas_exact:.10f}")
print(f"  Residual: {res_A_ratio:.2e}  [T1]")

# Verify via integral
def sech4(u):
    return (1.0 / np.cosh(u))**4
integral_I4, err_I4 = quad(sech4, -30, 30)
res_A_integral = abs(integral_I4 - 4.0/3.0)
print(f"\nNumerical check: ∫sech⁴(u)du = {integral_I4:.10f}  (res {res_A_integral:.2e})  [T1]")

# ============================================================
# Part B: I₄ structural web [T1/T2a]
# ============================================================
print("\n" + "=" * 60)
print("PART B: I₄ Structural Web [T1/T2a]")
print("=" * 60)

print(f"I₄ = {I4:.6f} = C₂(fund,SU(3)) = 4/3 appears in four DFC sectors:")

# 1. Gauge coupling
g_eff2_web = 2.0 * I4 / N_HOPF
res_B1 = abs(g_eff2_web - G_EFF2)
print(f"\n  1. Gauge coupling  [T2a, C117]:")
print(f"     g_eff² = 2I₄/N_Hopf = 2×(4/3)/9 = {g_eff2_web:.8f}  (res {res_B1:.2e})")

# 2. BPS gap bound
print(f"\n  2. BPS gap bound   [T2a, C218]:")
print(f"     H|_{{Q=2n}} ≥ n × I₄ × Q_top × m = n × {I4:.4f} × {Q_TOP} × m = n × {I4*Q_TOP:.4f} × m")

# 3. Neutrino depth correction
delta_d_I4 = (I4 - 1.0) / (2.0 * PI)
delta_d_beta = BETA * N_C / 2.0
res_B3 = abs(delta_d_I4 - delta_d_beta)
print(f"\n  3. Neutrino depth  [T1, C219]:")
print(f"     δd = (I₄−1)/(2π) = ({I4:.4f}−1)/(2π) = {delta_d_I4:.10f}")
print(f"        = β × N_c/2   = {BETA:.8f} × 3/2 = {delta_d_beta:.10f}  (res {res_B3:.2e})")

# 4. String tension (this work)
print(f"\n  4. String tension  [T3, C220]:")
print(f"     σ_fund = I₄ × Λ_QCD²  →  √σ = √I₄ × Λ_QCD = {np.sqrt(I4):.4f} × Λ_QCD")

print(f"\n→ I₄ = C₂(fund,SU(3)) is the universal DFC color Casimir  [T3 synthesis]")

# ============================================================
# Part C: Casimir ratio σ_adj/σ_fund = 9/4 [T1 math + T3 physics]
# ============================================================
print("\n" + "=" * 60)
print("PART C: Casimir Ratio σ_adj/σ_fund = 9/4  [T3]")
print("=" * 60)

print("Casimir scaling (lattice-supported, not derived from DFC):")
print("  σ_R / σ_fund = C₂(R) / C₂(fund)")
print()
print(f"{'Representation':<20} {'C₂(R)':<10} {'σ_R/σ_fund':<14} {'C₂(R) × Λ_QCD² coeff'}")
print("-" * 60)
reps = [
    ('singlet (1)',     0.0,       '(0,0)', 1),
    ('fund (3)',        C2_fund,   '(1,0)', 3),
    ('anti-fund (3̄)',  C2_fund,   '(0,1)', 3),
    ('adjoint (8)',     C2_adj,    '(1,1)', 8),
    ('sextet (6)',      10.0/3.0,  '(2,0)', 6),
    ('10-plet',         6.0,       '(3,0)', 10),
]
for name, c2, dynkin, dim in reps:
    ratio = c2 / C2_fund if C2_fund > 0 else 0.0
    print(f"{name:<20} {c2:<10.4f} {ratio:<14.4f} {c2:.4f}")

print()
print(f"Key DFC prediction: σ_adj/σ_fund = C₂(adj)/C₂(fund) = N_c/I₄ = 9/4 = {r_cas:.4f}  [T1 math]")
print()

# Lattice QCD comparison
# Bali (2000) Phys.Rept. 343:1-136 and Deldar (1999) Phys.Rev.D62:034509
# report σ_adj/σ_fund ≈ 2.1–2.5 at intermediate distances (0.1–0.5 fm)
# before adjoint string breaking (which occurs at larger R)
lattice_central = 2.20   # conservative central estimate
lattice_range   = 0.20   # ± range (lattice/phenomenology variation)
err_Cas = (r_cas - lattice_central) / lattice_central
print(f"Lattice QCD (intermediate R, before string breaking):")
print(f"  σ_adj/σ_fund ≈ {lattice_central:.2f} ± {lattice_range:.2f}  (Bali, Deldar, various)")
print(f"  DFC 9/4 = {r_cas:.4f}  →  error {err_Cas*100:+.1f}% from lattice central  [T3]")
print(f"  (within systematic range {lattice_central-lattice_range:.2f}–{lattice_central+lattice_range:.2f} ✓)")

# ============================================================
# Part D: Absolute string tension comparison [T3]
# ============================================================
print("\n" + "=" * 60)
print("PART D: Absolute String Tension [T3]")
print("=" * 60)

# DFC Casimir route: σ = I₄ × Λ_QCD²
sigma_I4_DFC  = I4 * LAMBDA_QCD_DFC**2
sigma_I4_PDG  = I4 * LAMBDA_QCD_PDG**2
sqrt_I4_DFC   = np.sqrt(sigma_I4_DFC)
sqrt_I4_PDG   = np.sqrt(sigma_I4_PDG)
err_I4_DFC    = (sqrt_I4_DFC - SQRT_SIGMA_OBS) / SQRT_SIGMA_OBS
err_I4_PDG    = (sqrt_I4_PDG - SQRT_SIGMA_OBS) / SQRT_SIGMA_OBS

# C160 kink-counting route: σ = Q_top × Λ_QCD²
sigma_Q_DFC   = Q_TOP * LAMBDA_QCD_DFC**2
sqrt_Q_DFC    = np.sqrt(sigma_Q_DFC)
err_Q_DFC     = (sqrt_Q_DFC - SQRT_SIGMA_OBS) / SQRT_SIGMA_OBS

print(f"Method 1 — Casimir scaling: σ_fund = I₄ × Λ_QCD²")
print(f"  I₄ = {I4:.4f},  DFC Λ_QCD = {LAMBDA_QCD_DFC} MeV")
print(f"  σ_fund = {sigma_I4_DFC:.0f} MeV²,  √σ_fund = {sqrt_I4_DFC:.1f} MeV  ({err_I4_DFC*100:+.1f}%)  [T3]")
print(f"  With PDG Λ_QCD = {LAMBDA_QCD_PDG} MeV:")
print(f"  σ_fund = {sigma_I4_PDG:.0f} MeV²,  √σ_fund = {sqrt_I4_PDG:.1f} MeV  ({err_I4_PDG*100:+.1f}%)  [T3]")

print(f"\nMethod 2 — Kink counting (C160): σ = Q_top × Λ_QCD²  [T3, −1.7%]")
print(f"  Q_top = {Q_TOP},  DFC Λ_QCD = {LAMBDA_QCD_DFC} MeV")
print(f"  σ = {sigma_Q_DFC:.0f} MeV²,  √σ = {sqrt_Q_DFC:.1f} MeV  ({err_Q_DFC*100:+.1f}%)")

print(f"\nObserved: √σ ≈ {SQRT_SIGMA_OBS:.0f} MeV")

# Ratio between the two methods
ratio_methods = Q_TOP / I4   # = 2/(4/3) = 3/2
print(f"\nRatio σ(C160)/σ(C220): Q_top/I₄ = {Q_TOP}/{I4:.4f} = {ratio_methods:.4f} = 3/2")
print(f"  Q_top/I₄ = {Q_TOP}/{I4:.4f} = N_c/2 = {N_C/2:.4f}  [potential structural identity, T3]")
print(f"  Note: C160 (kink counting) is numerically more accurate T3;")
print(f"  C220 (Casimir) has stronger structural motivation from color geometry")

# Required Λ_QCD for exact Casimir fit
lambda_exact_I4 = SQRT_SIGMA_OBS / np.sqrt(I4)
lambda_exact_Q  = SQRT_SIGMA_OBS / np.sqrt(Q_TOP)
print(f"\nRequired Λ_QCD for exact fit:")
print(f"  Casimir (I₄): {lambda_exact_I4:.1f} MeV  (vs DFC {LAMBDA_QCD_DFC} MeV, ratio {lambda_exact_I4/LAMBDA_QCD_DFC:.3f})")
print(f"  Kink    (Q_top): {lambda_exact_Q:.1f} MeV  (vs DFC {LAMBDA_QCD_DFC} MeV, ratio {lambda_exact_Q/LAMBDA_QCD_DFC:.3f})")

# ============================================================
# Part E: Strong-coupling area law consistency [T2a]
# ============================================================
print("\n" + "=" * 60)
print("PART E: SC Area Law Consistency [T2a]")
print("=" * 60)

# SC area law gives σ_SC = 2.875 × Λ_QCD² (C205, T2a)
# Casimir adjoint gives σ_adj = C₂(adj) × Λ_QCD² = 3 × Λ_QCD²
sigma_adj_coeff  = C2_adj      # = 3
sigma_fund_coeff = I4          # = 4/3

ratio_SC_fund = SIGMA_SC_COEFF / sigma_fund_coeff   # = 2.875 / (4/3)
ratio_SC_adj  = SIGMA_SC_COEFF / sigma_adj_coeff    # = 2.875 / 3

print(f"From C205 [T2a]:  σ_SC = {SIGMA_SC_COEFF:.4f} × Λ_QCD²")
print(f"Casimir fund [T3]: σ_fund = I₄ × Λ_QCD² = {sigma_fund_coeff:.4f} × Λ_QCD²")
print(f"Casimir adj  [T3]: σ_adj = C₂(adj) × Λ_QCD² = {sigma_adj_coeff:.4f} × Λ_QCD²")

print(f"\nSC ratios:")
print(f"  σ_SC / σ_fund = {SIGMA_SC_COEFF:.4f} / {sigma_fund_coeff:.4f} = {ratio_SC_fund:.4f}")
print(f"  σ_SC / σ_adj  = {SIGMA_SC_COEFF:.4f} / {sigma_adj_coeff:.4f} = {ratio_SC_adj:.4f}")
print(f"  Casimir ratio 9/4 = {r_cas:.4f}")

res_E1 = abs(ratio_SC_fund - r_cas) / r_cas * 100
res_E2 = abs(ratio_SC_adj  - 1.0)   * 100
print(f"\n  σ_SC/σ_fund vs 9/4: {res_E1:.1f}% difference  [T2a: consistent within SC approximation]")
print(f"  σ_SC/σ_adj  vs 1.0: {res_E2:.1f}% difference  [T2a: SC area law ≈ adjoint string tension]")
print(f"\nInterpretation: The SC area law (strong coupling β ≈ 1) captures")
print(f"  predominantly adjoint (gluon) flux tube contributions, giving σ_SC ≈ σ_adj.")
print(f"  The fundamental string tension σ_fund = I₄ × Λ_QCD² is the subleading component.")
print(f"  The factor σ_SC/σ_fund ≈ 9/4 is consistent with the Casimir ratio σ_adj/σ_fund.  [T3]")

# ============================================================
# Part F: DFC holonomy character check — quark vs gluon [T1]
# ============================================================
print("\n" + "=" * 60)
print("PART F: D7 Kink Holonomy — χ_fund vs χ_adj [T1]")
print("=" * 60)

# The D7 kink in the T^3 direction with Q_top = 2 has:
# P_kink = exp(i T^3 × 2π) = diag(-1, -1, 1) in the fundamental [T1, C219]
# Here T^3 = diag(1/2, -1/2, 0) (Gell-Mann λ_3/2)

T3_eigenvalues = np.array([0.5, -0.5, 0.0])
phase = 2.0 * PI   # full kink phase shift (Q_top = 2 → 2π)
P_kink_eigenvalues = np.exp(1j * T3_eigenvalues * phase)

chi_fund = np.sum(P_kink_eigenvalues)
print(f"D7 kink holonomy in T^3 direction with Δθ = 2π (Q_top = 2):")
print(f"  P_kink = exp(i T^3 × 2π)  on fundamental")
print(f"  T^3 eigenvalues: {T3_eigenvalues}")
print(f"  P_kink eigenvalues: {np.round(P_kink_eigenvalues.real, 4)} + i×{np.round(P_kink_eigenvalues.imag, 4)}")

res_F1 = abs(chi_fund - (-1.0))
print(f"\n  χ_fund(P_kink) = Tr_fund(P_kink) = {chi_fund.real:+.6f}  (imag {chi_fund.imag:.2e})")
print(f"  Expected: -1,  residual {res_F1:.2e}  [T1]")

# Adjoint character: χ_adj = |χ_fund|² - 1 for SU(N)
chi_adj = abs(chi_fund)**2 - 1.0
print(f"\n  χ_adj(P_kink) = |χ_fund|² - 1 = {abs(chi_fund)**2:.6f} - 1 = {chi_adj:.6f}  [T1]")
print(f"  → D7 kink is TRANSPARENT to gluons (adjoint representation)  [T1]")
print(f"  → D7 kink is NON-TRIVIAL for quarks (fundamental): χ_fund = -1  [T1]")

# Anti-fundamental character
chi_antifund = np.conj(chi_fund)
print(f"\n  χ_anti-fund(P_kink) = χ_fund* = {chi_antifund.real:+.6f}  [T1]")
print(f"  χ_fund = χ_anti-fund = -1: cannot distinguish quark from anti-quark via T^3 alone")
print(f"  (Z₃ triality argument distinguishes them: D6 single crossing → triality-1 → quark) [T2a, C217]")

# Verify: P_kink = diag(-1,-1,1)
P_explicit = np.diag(P_kink_eigenvalues)
expected   = np.diag(np.array([-1.0+0j, -1.0+0j, 1.0+0j]))
res_F2 = np.max(np.abs(P_explicit - expected))
print(f"\n  P_kink = diag(-1,-1,1): max deviation from expected {res_F2:.2e}  [T1, C219]")

# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 60)
print("SUMMARY — Cycle 220 Results")
print("=" * 60)
print(f"[T1]  I₄ = C₂(fund,SU(3)) = 4/3  (res {res_A_identity:.2e})")
print(f"[T1]  Casimir ratio C₂(adj)/C₂(fund) = 9/4  (res {res_A_ratio:.2e})")
print(f"[T1]  χ_fund(P_kink) = -1  (res {res_F1:.2e})")
print(f"[T1]  χ_adj(P_kink)  =  0  — D7 kink transparent to gluons")
print(f"[T2a] σ_SC ≈ σ_adj: σ_SC/σ_adj = {ratio_SC_adj:.3f}  ({res_E2:.1f}% from 1.0)")
print(f"[T3]  σ_R = C₂(R)/C₂(fund) × σ_fund  (Casimir scaling, lattice-supported)")
print(f"[T3]  σ_fund = I₄ × Λ_QCD²  →  √σ = {sqrt_I4_DFC:.1f} MeV  ({err_I4_DFC*100:+.1f}%)")
print(f"[T3]  I₄ structural web: same constant in g_eff², gap, σ, δd")
print(f"\nC160 kink-counting σ = Q_top × Λ_QCD²  ({err_Q_DFC*100:+.1f}%) remains numerically superior T3")
print(f"C220 Casimir σ = I₄ × Λ_QCD²  ({err_I4_DFC*100:+.1f}%) has stronger color-geometric motivation")
print(f"Both complement each other in the structural picture of confinement.")

print(f"\nALL ASSERTIONS:")
assert abs(C2_fund - 4.0/3.0)  < 1e-14, f"C₂(fund) identity failed"
assert abs(r_cas   - 9.0/4.0)  < 1e-14, f"Casimir ratio 9/4 failed"
assert abs(integral_I4 - I4)   < 1e-8,  f"I₄ numerical failed"
assert abs(g_eff2_web - G_EFF2) < 1e-14, f"g_eff² web failed"
assert abs(res_B3)              < 1e-14, f"δd identity failed"
assert abs(chi_fund.real - (-1.0)) < 1e-14 and abs(chi_fund.imag) < 1e-14, f"χ_fund failed"
assert abs(chi_adj) < 1e-12, f"χ_adj failed"
assert abs(ratio_SC_adj - 1.0) < 0.05, f"SC/adj consistency >5%"
print("ALL ASSERTIONS PASSED")
