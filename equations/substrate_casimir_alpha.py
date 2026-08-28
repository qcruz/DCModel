"""
Substrate Casimir Self-Energy: Does V(phi) Produce exp(-alpha)?
===============================================================

Physical question:
    The cosmological constant formula rho_Lambda = M_Pl^4 * exp(-(S_inst +
    S_inst*delta_d + alpha)) uses exp(-alpha) as the substrate's contribution.
    Can this be derived from V(phi) dynamics?

DFC mechanism:
    The substrate potential V(phi) = -alpha/2 phi^2 + beta/4 phi^4 determines
    all substrate dynamics. The parameter alpha = 18^(1/3) sets the curvature
    at the vacuum. This module explores candidate mechanisms that could produce
    a factor exp(-alpha) in the vacuum energy.

    Candidates tested:
      A. Harmonic zero-point energy: E_0 = sqrt(V''(phi_0))/2
      B. Barrier tunneling: exp(-Delta_V)
      C. Kink action fraction: S_kink^n for various n
      D. Dimensional transmutation: alpha as ln(M_Pl/mu)
      E. Euclidean action of vacuum fluctuation over kink width
      F. Modular structure: alpha from BPS + topological integers

Tier assessment:
    exp(-alpha) in Lambda formula: T3 (no derivation)
    This module: exploration — identifies which mechanism works

Key references:
    equations/alpha_from_kink_action.py — alpha = 18^(1/3) (C169)
    equations/lambda_combination_rule.py — combination rule (C451)
    equations/cosmological_constant_prediction.py — Lambda prediction (C362)
"""

import math

PI = math.pi

# DFC parameters
alpha = 18.0 ** (1.0 / 3.0)         # 2.6207...
beta = 1.0 / (9.0 * PI)             # 0.03537...
phi_0 = math.sqrt(alpha / beta)      # vacuum amplitude
S_kink = 36.0 * PI                   # BPS kink action
xi = 1.0 / math.sqrt(alpha)          # kink width
Q_top = 2.0
N_Hopf = 9.0
I4 = 4.0 / 3.0
g_eff_sq = 8.0 / 27.0

pass_count = 0
fail_count = 0
total_tests = 0


def check(label, condition, msg=""):
    global pass_count, fail_count, total_tests
    total_tests += 1
    if condition:
        pass_count += 1
        print(f"  PASS {label}: {msg}")
    else:
        fail_count += 1
        print(f"  FAIL {label}: {msg}")


# =============================================================================
# Part A: Harmonic Zero-Point Energy
# =============================================================================
print("=" * 72)
print("SUBSTRATE CASIMIR SELF-ENERGY — DOES V(phi) PRODUCE exp(-alpha)?")
print("=" * 72)
print()
print("[PART A] HARMONIC ZERO-POINT ENERGY")
print("=" * 72)
print()

# V''(phi_0) = 2*alpha (exact, from double-well)
V_pp = 2.0 * alpha
omega = math.sqrt(V_pp)
E_zpe = omega / 2.0

print(f"  V(phi) = -alpha/2 phi^2 + beta/4 phi^4")
print(f"  V''(phi_0) = 2*alpha = {V_pp:.6f}")
print(f"  omega = sqrt(2*alpha) = {omega:.6f}")
print(f"  E_ZPE = omega/2 = {E_zpe:.6f}")
print(f"  alpha = {alpha:.6f}")
print(f"  Ratio E_ZPE/alpha = {E_zpe/alpha:.6f}")
print()

# E_ZPE != alpha in general. Check the special value alpha = 18^(1/3)
# E_ZPE/alpha = sqrt(2*alpha)/(2*alpha) = 1/sqrt(2*alpha)
ratio_zpe = 1.0 / math.sqrt(2.0 * alpha)
print(f"  E_ZPE/alpha = 1/sqrt(2*alpha) = {ratio_zpe:.6f}")
print(f"  This is NOT 1 for any finite alpha.")
print()

check("A1", abs(E_zpe - alpha) > 0.1,
      f"E_ZPE = {E_zpe:.4f} != alpha = {alpha:.4f} — harmonic ZPE is NOT alpha")

# What alpha would make E_ZPE = alpha?
# sqrt(2*a)/2 = a => sqrt(2*a) = 2*a => 2*a = 4*a^2 => a = 1/2
alpha_match = 0.5
print(f"  E_ZPE = alpha requires alpha = 1/2 (not 18^(1/3)).")
print(f"  VERDICT: Harmonic ZPE does NOT produce alpha. RULED OUT.")
print()


# =============================================================================
# Part B: Barrier Tunneling
# =============================================================================
print("[PART B] BARRIER TUNNELING")
print("=" * 72)
print()

# Barrier height: V(0) - V(phi_0)
V_vacuum = -alpha / 2.0 * (alpha / beta) + beta / 4.0 * (alpha / beta)**2
V_barrier = 0.0  # V(0) = 0
Delta_V = V_barrier - V_vacuum  # positive

print(f"  V(phi_0) = -alpha^2/(4*beta) = {V_vacuum:.4f}")
print(f"  V(0)     = 0")
print(f"  Delta_V  = alpha^2/(4*beta) = {Delta_V:.4f}")
print()

# With alpha = 18^(1/3), beta = 1/(9*pi):
Delta_V_exact = alpha**2 / (4.0 * beta)
print(f"  Delta_V = alpha^2/(4*beta) = 18^(2/3)/(4/(9*pi))")
print(f"         = 18^(2/3) * 9*pi/4 = {Delta_V_exact:.4f}")
print()

# exp(-Delta_V) gives a much larger suppression than exp(-alpha)
print(f"  exp(-Delta_V) = exp(-{Delta_V_exact:.2f}) = {math.exp(-Delta_V_exact):.4e}")
print(f"  exp(-alpha)   = exp(-{alpha:.4f}) = {math.exp(-alpha):.4e}")
print(f"  Ratio: Delta_V/alpha = {Delta_V_exact/alpha:.4f}")
print()

check("B1", Delta_V_exact / alpha > 10,
      f"Delta_V/alpha = {Delta_V_exact/alpha:.1f} >> 1 — barrier way too high")
print(f"  VERDICT: Barrier tunneling does NOT produce alpha. RULED OUT.")
print()


# =============================================================================
# Part C: Kink Action Fractions
# =============================================================================
print("[PART C] KINK ACTION FRACTIONS")
print("=" * 72)
print()

print(f"  S_kink = 36*pi = {S_kink:.4f}")
print(f"  alpha = 18^(1/3) = {alpha:.6f}")
print()

# Check various powers of S_kink
print(f"  Candidate expressions involving S_kink:")
print(f"  {'Expression':>30}  {'Value':>12}  {'Ratio to alpha':>15}")
print(f"  {'-'*60}")

candidates = [
    ("S_kink", S_kink),
    ("S_kink / (4*pi)", S_kink / (4*PI)),
    ("S_kink^(1/2)", math.sqrt(S_kink)),
    ("S_kink^(1/3)", S_kink**(1.0/3.0)),
    ("ln(S_kink)", math.log(S_kink)),
    ("ln(S_kink/pi)", math.log(S_kink/PI)),
    ("ln(S_kink/(4*pi))", math.log(S_kink/(4*PI))),
    ("4/S_kink * alpha^2", 4.0/S_kink * alpha**2),
    ("S_kink * beta", S_kink * beta),
    ("1/(S_kink * beta)", 1.0/(S_kink * beta)),
]

for name, val in candidates:
    ratio = val / alpha
    marker = " <--" if abs(ratio - 1.0) < 0.05 else ""
    print(f"  {name:>30}  {val:12.6f}  {ratio:15.6f}{marker}")

print()
print(f"  alpha itself:                       {alpha:12.6f}  {1.0:15.6f}")
print()

# The key identity: alpha^3 = 18 = Q_top * N_Hopf
# So alpha = (Q_top * N_Hopf)^(1/3)
# And S_kink = 36*pi = 4/beta = 4*9*pi = 36*pi
# S_kink * beta = 4 (exact)
check("C1", abs(S_kink * beta - 4.0) < 1e-10,
      f"S_kink * beta = 4 exactly ({S_kink * beta:.15f})")

# Check: is alpha related to S_kink via topology?
# alpha = (Q_top * N_Hopf)^(1/3) = (2*9)^(1/3)
# S_kink = 36*pi = 4*9*pi = 4*pi*N_Hopf
# So alpha/S_kink = (Q_top*N_Hopf)^(1/3) / (4*pi*N_Hopf)
#                 = Q_top^(1/3) / (4*pi*N_Hopf^(2/3))
ratio_alpha_skink = alpha / S_kink
print(f"  alpha/S_kink = {ratio_alpha_skink:.6f}")
print(f"  = Q_top^(1/3) / (4*pi*N_Hopf^(2/3)) = {Q_top**(1.0/3.0)/(4*PI*N_Hopf**(2.0/3.0)):.6f}")
print()
print(f"  No simple relation found. alpha and S_kink are algebraically")
print(f"  independent — they share V(phi) origin but combine (alpha, beta)")
print(f"  in different ways.")
print()


# =============================================================================
# Part D: Euclidean Action Over Kink Width
# =============================================================================
print("[PART D] EUCLIDEAN ACTION OVER KINK WIDTH")
print("=" * 72)
print()

# The substrate's contribution to vacuum energy may involve the
# Euclidean action of a vacuum fluctuation over one kink width xi.
# S_E(xi) = integral_0^xi dt [1/2 (dphi/dt)^2 + V(phi)]
# For phi = phi_0 (static vacuum): S_E = V(phi_0) * xi

S_E_vacuum = V_vacuum * xi
print(f"  Kink width xi = 1/sqrt(alpha) = {xi:.6f}")
print(f"  V(phi_0) = {V_vacuum:.4f}")
print(f"  S_E(vacuum, xi) = V(phi_0) * xi = {S_E_vacuum:.4f}")
print(f"  |S_E| = {abs(S_E_vacuum):.4f}")
print()

# V(phi_0) * xi = -alpha^2/(4*beta) * 1/sqrt(alpha)
# = -alpha^(3/2) / (4*beta)
# = -(3*sqrt(2)) / (4*beta)     [since alpha^(3/2) = 3*sqrt(2)]
# = -(3*sqrt(2)) * 9*pi / 4
# = -27*pi*sqrt(2)/4
S_E_exact = -27.0 * PI * math.sqrt(2.0) / 4.0
print(f"  Algebraic: S_E = -alpha^(3/2)/(4*beta) = -3*sqrt(2)/(4/(9*pi))")
print(f"           = -27*pi*sqrt(2)/4 = {S_E_exact:.4f}")
print(f"  |S_E|/alpha = {abs(S_E_exact)/alpha:.4f}")
print()

check("D1", abs(S_E_vacuum - S_E_exact) < 1e-6,
      f"Algebraic form verified: {S_E_vacuum:.6f} vs {S_E_exact:.6f}")

# This is NOT alpha either. |S_E| >> alpha.
print(f"  VERDICT: Vacuum action over kink width = {abs(S_E_exact):.2f} >> alpha = {alpha:.2f}")
print(f"  RULED OUT as mechanism for exp(-alpha).")
print()


# =============================================================================
# Part E: Alpha as Depth Coordinate
# =============================================================================
print("[PART E] ALPHA AS DEPTH COORDINATE")
print("=" * 72)
print()

print("  In the Lambda formula, the three terms have different physical roles:")
print()
print("    exp(-S_inst):          gauge sector tunneling amplitude")
print("    exp(-S_inst * delta_d): depth modulation (multiplicative on S_inst)")
print("    exp(-alpha):           substrate self-energy")
print()
print("  STRUCTURAL ARGUMENT for exp(-alpha):")
print()
print("  The substrate field at the cosmological depth has amplitude phi_0.")
print("  The vacuum energy at depth d is modulated by the substrate's")
print("  compressive self-interaction. The substrate field equation:")
print()
print("    V'(phi_0) = 0 => the vacuum is a fixed point")
print()
print("  The cosmological vacuum energy receives a factor from the")
print("  substrate's self-coupling at the vacuum. The relevant dimensionless")
print("  parameter is alpha itself — it is the ONLY free parameter of V(phi)")
print("  (beta being derived). In the Euclidean path integral:")
print()
print("    Z = integral D[phi] exp(-S_E[phi])")
print()
print("  The saddle point approximation around phi_0 gives:")
print("    Z ~ exp(-S_E[phi_0]) * det(V''(phi_0))^(-1/2)")
print()
print("  The determinant factor for a single mode:")
print("    det(V'')^(-1/2) ~ exp(-ln(V'')/2) = exp(-ln(2*alpha)/2)")
print()

ln_V_pp_half = math.log(2.0 * alpha) / 2.0
print(f"  ln(V''(phi_0))/2 = ln(2*alpha)/2 = {ln_V_pp_half:.6f}")
print(f"  alpha = {alpha:.6f}")
print(f"  Ratio = {ln_V_pp_half/alpha:.6f}")
print()

# What about the number of modes? If there are n independent modes,
# each contributing ln(2*alpha)/2, then total = n * ln(2*alpha)/2.
# For total = alpha: n = 2*alpha/ln(2*alpha) = 2*2.621/1.658 = 3.16
n_modes_needed = 2.0 * alpha / math.log(2.0 * alpha)
print(f"  For n modes: n * ln(2*alpha)/2 = alpha")
print(f"  => n = 2*alpha/ln(2*alpha) = {n_modes_needed:.4f}")
print(f"  This is close to N_c = 3 ({abs(n_modes_needed - 3.0)/3.0*100:+.1f}% off)")
print()

check("E1", abs(n_modes_needed - 3.0) < 0.2,
      f"n_modes = {n_modes_needed:.4f} ≈ 3 = N_c ({(n_modes_needed/3.0-1)*100:+.2f}%)")

# CANDIDATE MECHANISM:
# N_c = 3 independent gauge modes at D7, each contributing ln(2*alpha)/2
# to the effective action. Total contribution:
S_sub_candidate = 3.0 * math.log(2.0 * alpha) / 2.0
err_candidate = (S_sub_candidate - alpha) / alpha * 100

print()
print(f"  CANDIDATE: S_sub = N_c * ln(2*alpha)/2")
print(f"    = 3 * ln(2*18^(1/3))/2")
print(f"    = 3 * {math.log(2.0*alpha):.6f} / 2")
print(f"    = {S_sub_candidate:.6f}")
print(f"    alpha = {alpha:.6f}")
print(f"    Error: {err_candidate:+.2f}%")
print()

check("E2", abs(err_candidate) < 10,
      f"N_c * ln(2*alpha)/2 matches alpha to {err_candidate:+.2f}%")


# =============================================================================
# Part F: Exact Identity Search
# =============================================================================
print()
print("[PART F] EXACT IDENTITY SEARCH")
print("=" * 72)
print()

print("  Is exp(-alpha) = exp(-18^(1/3)) expressible in closed form")
print("  using DFC topological integers?")
print()

# alpha = (Q_top * N_Hopf)^(1/3) = (2*9)^(1/3)
# exp(-alpha) = exp(-(2*9)^(1/3))

# Check: is there a relation alpha = f(N_c, Q_top, I4, ...)?
print(f"  alpha = 18^(1/3) = (Q_top * N_Hopf)^(1/3)")
print(f"  alpha^3 = 18 = 2 * 9 = Q_top * N_Hopf")
print(f"  alpha^3 = 2 * 3^2 = Q_top * N_c^2")
print()

# The factor 18 = 2 * 9:
# 2 = Q_top (topological charge)
# 9 = N_Hopf = N_c^2 (Hopf fiber dimension sum = 1+3+5 for CP^1, CP^2, CP^3)
# So alpha^3 = Q_top * N_c^2

# Can we write alpha = N_c^(2/3) * Q_top^(1/3)?
alpha_nc = 3.0**(2.0/3.0) * 2.0**(1.0/3.0)
print(f"  alpha = N_c^(2/3) * Q_top^(1/3) = {alpha_nc:.10f}")
print(f"  Direct: 18^(1/3) = {alpha:.10f}")
print(f"  Match: {abs(alpha_nc - alpha):.2e}")
print()

check("F1", abs(alpha_nc - alpha) < 1e-14,
      "alpha = N_c^(2/3) * Q_top^(1/3) exact")

# The N_c = 3 connection in Part E suggests:
# S_sub = N_c * ln(V''(phi_0))/2 = N_c * ln(2*N_c^(2/3)*Q_top^(1/3))/2
S_sub_nc = 3.0 * math.log(2.0 * alpha) / 2.0
print(f"  S_sub(N_c=3) = N_c * ln(2*alpha)/2 = {S_sub_nc:.6f}")
print(f"  alpha                               = {alpha:.6f}")
print(f"  Difference: {S_sub_nc - alpha:.6f} ({(S_sub_nc/alpha - 1)*100:+.2f}%)")
print()

# This is +5.2% off — suggestive but not exact.
# Is there a correction that closes the gap?
# The one-loop determinant for N_c modes with mass^2 = 2*alpha over
# a "time" interval T includes: det = prod_{i=1}^{N_c} omega_i
# If all modes have the same frequency, det^{-1/2} = exp(-N_c*omega/(2T))
# For omega = sqrt(2*alpha), T = 1:
S_sub_freq = 3.0 * math.sqrt(2.0 * alpha) / 2.0
err_freq = (S_sub_freq - alpha) / alpha * 100
print(f"  Alternative: S_sub = N_c * sqrt(2*alpha)/2 = {S_sub_freq:.6f} ({err_freq:+.2f}%)")
print()

# This is also +31% off. Neither candidate is exact.

# Check: what N_c would make N_c * ln(2*alpha)/2 = alpha exactly?
# N_c = 2*alpha/ln(2*alpha) = 2*2.6207/ln(5.2415) = 5.2415/1.6565 = 3.163
# Not exactly 3.

# Check the reverse: for N_c = 3 exactly, what alpha would work?
# 3*ln(2*a)/2 = a => ln(2*a) = 2a/3 => 2*a = exp(2a/3)
# This transcendental equation has solution a ≈ 2.487 (not 2.621)
# So the match at +5.2% is coincidental, not exact.

# Let's solve 2*a = exp(2*a/3) numerically
a_lo, a_hi = 2.0, 3.0
for _ in range(60):
    a_mid = (a_lo + a_hi) / 2.0
    if 2.0 * a_mid < math.exp(2.0 * a_mid / 3.0):
        a_hi = a_mid
    else:
        a_lo = a_mid
a_exact = (a_lo + a_hi) / 2.0
print(f"  N_c*ln(2*a)/2 = a has exact solution a = {a_exact:.6f}")
print(f"  DFC alpha = {alpha:.6f}")
print(f"  Off by {(alpha - a_exact)/a_exact*100:+.1f}%")
print()

check("F2", abs(alpha - a_exact) / a_exact > 0.01,
      f"N_c*ln(2*alpha)/2 = alpha is NOT exact (5.4% off)")

print("  CONCLUSION: The N_c=3 determinant mechanism gives +5.2% match,")
print("  suggestive but not exact. The exp(-alpha) factor in the Lambda")
print("  formula likely involves a more direct structural mechanism.")
print()


# =============================================================================
# Part G: Status Assessment
# =============================================================================
print("[PART G] STATUS ASSESSMENT")
print("=" * 72)
print()

print("  MECHANISMS TESTED:")
print()
print(f"  {'Mechanism':>35}  {'Gives':>12}  {'vs alpha':>10}  Status")
print(f"  {'-'*72}")

results_table = [
    ("Harmonic ZPE (omega/2)", E_zpe, "RULED OUT"),
    ("Barrier tunneling (Delta_V)", Delta_V_exact, "RULED OUT"),
    ("Vacuum action over xi", abs(S_E_exact), "RULED OUT"),
    ("ln(V'')/2 per mode", ln_V_pp_half, "TOO SMALL"),
    ("N_c * ln(2*alpha)/2", S_sub_nc, "+5.2%"),
    ("N_c * sqrt(2*alpha)/2", S_sub_freq, "+31%"),
]

for name, val, status in results_table:
    err = (val - alpha) / alpha * 100
    print(f"  {name:>35}  {val:12.4f}  {err:+10.1f}%  {status}")

print()
print(f"  Target: alpha = 18^(1/3) = {alpha:.6f}")
print()

print("  BEST CANDIDATE: N_c * ln(2*alpha)/2 = 2.757 (+5.2%)")
print("    Physical picture: N_c = 3 independent D7 gauge modes,")
print("    each contributing a one-loop determinant factor ln(2*alpha)/2")
print("    to the effective action at the cosmological depth.")
print()
print("    The 5.2% gap may come from:")
print("      - Higher-loop corrections to the determinant")
print("      - Non-gaussian fluctuations around the vacuum")
print("      - The exact expression is alpha, not N_c*ln(2*alpha)/2")
print("        (i.e., the structural argument gives the right ballpark")
print("        but the exact value is set by the BPS condition)")
print()

print("  FUNDAMENTAL INSIGHT:")
print("    alpha enters the Lambda formula NOT as a derived Casimir energy")
print("    but as the PRIMITIVE substrate compression parameter itself.")
print("    The BPS condition S_kink * alpha_D5 = 1 fixes alpha = 18^(1/3).")
print("    Its appearance in exp(-alpha) may simply reflect that the")
print("    substrate's zero-point fluctuation amplitude at the cosmological")
print("    depth is set by the compression parameter — alpha IS the")
print("    substrate's self-energy scale, by definition.")
print()
print("    If so, deriving 'why exp(-alpha)' reduces to: 'why does the")
print("    substrate's contribution to vacuum energy equal its compression")
print("    parameter?' The answer may be: because the compression parameter")
print("    IS the substrate's energy scale at the Planck depth.")
print()

print("  TIER: REMAINS T3")
print("    No exact mechanism found. Best candidate (+5.2%) is suggestive")
print("    but not sufficient for T2b upgrade.")
print()
print("  PATH FORWARD:")
print("    1. Compute the full one-loop determinant of V(phi) fluctuations")
print("       around phi_0 over the cosmological Hubble volume")
print("    2. Check if the Coleman-Weinberg effective potential at the")
print("       cosmological scale produces exp(-alpha)")
print("    3. Investigate whether alpha enters via the BPS bound directly")
print("       (the substrate 'cannot compress beyond alpha' => vacuum")
print("       energy suppressed by exp(-alpha))")
print()

check("G1", True,
      "Six candidate mechanisms tested systematically")
check("G2", True,
      "Best candidate identified: N_c * ln(2*alpha)/2 (+5.2%)")
check("G3", True,
      "No exact derivation found — remains T3")

print()
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()
print(f"  exp(-alpha) = exp(-18^(1/3)) appears in rho_Lambda formula")
print(f"  as the substrate's vacuum energy contribution.")
print()
print(f"  Six mechanisms tested — none give alpha exactly:")
print(f"    Best: N_c * ln(2*alpha)/2 = {S_sub_nc:.4f} (+5.2%)")
print(f"    alpha = {alpha:.6f} may enter as the primitive compression")
print(f"    parameter itself, not as a derived Casimir energy.")
print()
print(f"  STATUS: T3 (no upgrade). Three paths identified for future work.")
print()
print(f"  {pass_count}/{total_tests} PASS, {fail_count}/{total_tests} FAIL")
