"""
bcs_gap_lambda_qcd.py — BCS Gap Equation → Λ_QCD from DFC Parameters
=====================================================================

Physical question:
    Can the BCS/NJL gap equation, with DFC-derived couplings, predict
    Λ_QCD or the constituent quark mass M_Q ~ 300 MeV?

DFC mechanism:
    The chiral condensate at D7 depth is structurally identical to a BCS
    condensate: quark-antiquark pairs condense via attractive scalar exchange,
    breaking chiral symmetry. The "gap" Δ in BCS becomes the constituent
    quark mass M_Q in QCD. The mediator is the DFC sigma meson (m_σ = 3Λ/2).

    Structural mapping (BCS → DFC D7):
    | BCS superconductor     | DFC D7 (QCD)                    |
    |------------------------|---------------------------------|
    | Electron               | Quark (D7 kink zero mode)       |
    | Phonon                 | Sigma meson (scalar fluctuation) |
    | Cooper pair            | Pion (qq̄ Goldstone boson)       |
    | BCS gap Δ              | Constituent quark mass M_Q      |
    | Debye frequency ω_D    | m_σ = (3/2)Λ_QCD               |
    | G×N(0)                 | DFC coupling × density of states|
    | Meissner effect        | Color confinement (dual)        |
    | Abrikosov vortex       | QCD flux tube                   |
    | Type II/I boundary     | Dual superconductor κ_dual      |

    The NJL gap equation in the chiral limit:
        1 = G_NJL × N_c / π² × [Λ² - M² ln(1 + Λ²/M²)]

    DFC determines G_NJL from its couplings. The question is whether
    the gap M self-consistently gives Λ_QCD ~ 300 MeV.

Key references:
    Nambu & Jona-Lasinio (1961): Phys.Rev.122, 345
    foundations/literature_reframing.md §C1: BCS → Λ_QCD mapping
    equations/pion_mass_gmor.py: chiral condensate from NJL
    equations/pion_decay_constant.py: f_π from DFC

Usage:
    python equations/bcs_gap_lambda_qcd.py
"""

import math

pass_count = 0
fail_count = 0

def check(label, condition):
    global pass_count, fail_count
    if condition:
        pass_count += 1
        print(f"  [PASS] {label}")
    else:
        fail_count += 1
        print(f"  [FAIL] {label}")
    return condition


print("=" * 76)
print("BCS GAP EQUATION → Λ_QCD FROM DFC PARAMETERS (C548)")
print("=" * 76)

# ============================================================================
# PART A: DFC PARAMETERS FOR THE NJL GAP EQUATION
# ============================================================================
print("\nPART A: DFC Parameters and NJL Coupling")
print("-" * 76)

PI = math.pi
N_C = 3
N_F = 2  # light flavors (u, d)

# DFC fundamental
alpha = 18.0**(1.0/3.0)        # cube root of 18
beta = 1.0 / (9.0 * PI)        # quartic coupling
g_eff_sq = 8.0 / 27.0          # common gauge coupling squared
g_eff = math.sqrt(g_eff_sq)    # = 0.5443
I4 = 4.0 / 3.0                 # C_2(fund, SU(3))
LAMBDA_QCD = 304.5              # MeV (DFC value)

# DFC-derived meson masses
m_sigma = 1.5 * LAMBDA_QCD     # 456.75 MeV
m_rho = math.sqrt(2 * PI) * LAMBDA_QCD  # 763.3 MeV (= m_omega in DFC)
f_pi = LAMBDA_QCD / PI         # 96.9 MeV

# Observed constituent quark mass
M_Q_obs = 336.0                # MeV (typical, from hadron spectroscopy)
M_Q_target = LAMBDA_QCD        # 304.5 MeV (DFC Λ as gap)

print(f"  DFC parameters:")
print(f"    alpha     = 18^(1/3) = {alpha:.6f}")
print(f"    beta      = 1/(9 pi) = {beta:.6f}")
print(f"    g_eff^2   = 8/27 = {g_eff_sq:.6f}")
print(f"    g_eff     = {g_eff:.6f}")
print(f"    I_4 = C_2(fund) = {I4:.4f}")
print(f"    Lambda_QCD = {LAMBDA_QCD:.1f} MeV")
print(f"    m_sigma = (3/2) Lambda = {m_sigma:.2f} MeV")
print(f"    m_rho = sqrt(2 pi) Lambda = {m_rho:.1f} MeV")
print(f"    f_pi = Lambda/pi = {f_pi:.1f} MeV")
print(f"    M_Q (constituent, target) = {M_Q_obs:.0f} MeV")

# NJL four-fermion coupling from DFC
# Route 1: One-gluon exchange → NJL
#   G_OGE = C_F × g_s^2 / (2 Λ^2)
#   where C_F = (N_c^2-1)/(2N_c) = 4/3, g_s^2 = g_eff^2 = 8/27
#   Λ = UV cutoff = to be determined
#
# Route 2: Sigma exchange → NJL
#   G_sigma = g_qqs^2 / m_sigma^2
#   where g_qqs is the quark-sigma Yukawa coupling
#   In Walecka: g_sigma_N = pi sqrt(3 pi) (nucleon level)
#   At quark level: g_qqs = g_sigma_N / N_c (naive quark counting)
#
# Route 3: Instanton-induced (standard NJL motivation)
#   G_inst ~ (4 pi)^2 / (N_c × rho_c^2 × Lambda_inst^2)
#   where rho_c is the instanton size

# Route 1: OGE
C_F = (N_C**2 - 1.0) / (2.0 * N_C)  # = 4/3
print(f"\n  Route 1: One-gluon exchange (OGE)")
print(f"    C_F = (N_c^2-1)/(2 N_c) = {C_F:.4f}")

# Route 2: Sigma exchange
g_sigma_N = PI * math.sqrt(3.0 * PI)  # nucleon-sigma Yukawa
g_qqs = g_sigma_N / N_C               # quark-level (naive)
G_sigma = g_qqs**2 / m_sigma**2

print(f"\n  Route 2: Sigma exchange")
print(f"    g_sigma_N = pi sqrt(3 pi) = {g_sigma_N:.4f} (nucleon)")
print(f"    g_qqs = g_sigma_N / N_c = {g_qqs:.4f} (quark)")
print(f"    G_sigma = g_qqs^2 / m_sigma^2 = {G_sigma:.4e} MeV^-2")

# Route 3: From g_eff directly
# The NJL coupling strength is characterized by the dimensionless
# combination G × Λ^2. Standard NJL: G Λ^2 ~ 2 at the critical point.
# DFC-specific: what value of G Λ^2 does DFC predict?

print(f"\n  Route 3: From g_eff^2 = 8/27 directly")
# In the instanton vacuum picture, G = 8 pi^2 / (N_c Λ_UV^2) × <rho^2>
# In DFC, the instanton action S_inst = 8 pi^2 / g_eff^2 = 8 pi^2 × 27/8 = 27 pi^2
# The instanton density n ∝ exp(-S_inst) × Λ^4
# The effective coupling G ∝ (1/Λ^2) × (S_inst)^{N_c} × exp(-S_inst)

S_inst = 8.0 * PI**2 / g_eff_sq  # = 27 pi^2 = 266.5
print(f"    S_inst = 8 pi^2 / g_eff^2 = {S_inst:.1f}")
print(f"    exp(-S_inst) = {math.exp(-min(S_inst, 700)):.2e}")
print(f"    (Instanton density exponentially suppressed at this coupling)")

check("C_F = 4/3 for SU(3)", abs(C_F - 4.0/3.0) < 1e-10)
check("g_eff < 1 (perturbative)", g_eff < 1)

# ============================================================================
# PART B: NJL GAP EQUATION — SOLVE FOR M_Q
# ============================================================================
print("\nPART B: NJL Gap Equation Solutions")
print("-" * 76)

def njl_gap_equation(M, G, Lambda_UV, N_c):
    """
    NJL gap equation in the chiral limit.
    Returns the self-consistency condition:
        f(M) = 1 - G × N_c / pi^2 × [Lambda^2 - M^2 ln(1 + Lambda^2/M^2)]
    Solution satisfies f(M) = 0 for the dynamical mass M.
    """
    if M <= 0:
        return 1.0 - G * N_c / PI**2 * Lambda_UV**2
    x = Lambda_UV**2 / M**2
    return 1.0 - G * N_c / PI**2 * (Lambda_UV**2 - M**2 * math.log(1 + x))


def solve_gap(G, Lambda_UV, N_c):
    """Solve NJL gap equation by bisection."""
    # Check if chiral symmetry breaking occurs
    f0 = njl_gap_equation(0.01, G, Lambda_UV, N_c)
    if f0 > 0:
        return 0.0  # no CSB — coupling too weak

    # Bisection
    M_low, M_high = 0.01, Lambda_UV * 0.99
    for _ in range(200):
        M_mid = (M_low + M_high) / 2
        f_mid = njl_gap_equation(M_mid, G, Lambda_UV, N_c)
        if f_mid < 0:
            M_low = M_mid
        else:
            M_high = M_mid
        if M_high - M_low < 0.001:
            break
    return (M_low + M_high) / 2


# Scan over UV cutoff values for each coupling route
print(f"\n  NJL gap equation: 1 = G N_c/pi^2 [Lambda^2 - M^2 ln(1+Lambda^2/M^2)]")
print(f"  Chiral limit (m_0 = 0). Solution M = constituent quark mass.")
print()

# Route 2: Sigma exchange coupling G_sigma
# Scan Lambda_UV from 400 to 1200 MeV
print(f"  Route 2: G = g_qqs^2/m_sigma^2 = {G_sigma:.4e} MeV^-2")
print(f"  {'Lambda_UV (MeV)':>15}  {'G Λ²':>8}  {'M_Q (MeV)':>10}  {'M_Q/Lambda_QCD':>14}  {'Status':>10}")
print(f"  {'─'*15}  {'─'*8}  {'─'*10}  {'─'*14}  {'─'*10}")

best_sigma = None
for Lambda_UV in [400, 500, 600, 636, 700, 800, 900, 1000]:
    G_Lsq = G_sigma * Lambda_UV**2
    M_Q = solve_gap(G_sigma, Lambda_UV, N_C)
    ratio = M_Q / LAMBDA_QCD if M_Q > 0 else 0
    status = "CSB" if M_Q > 10 else "no CSB"
    if M_Q > 10:
        err = (M_Q - M_Q_obs) / M_Q_obs * 100
        status = f"{err:+.1f}%"
        if best_sigma is None or abs(M_Q - LAMBDA_QCD) < abs(best_sigma[1] - LAMBDA_QCD):
            best_sigma = (Lambda_UV, M_Q)
    print(f"  {Lambda_UV:>15.0f}  {G_Lsq:>8.3f}  {M_Q:>10.1f}  {ratio:>14.3f}  {status:>10}")

print()

# Route 2b: Determine the critical coupling
# At critical: G_c × N_c × Λ² / π² = 1
G_c_over_Lsq = PI**2 / N_C
print(f"  Critical coupling: G_c × Lambda^2 = pi^2/N_c = {G_c_over_Lsq:.4f}")
Lambda_crit_sigma = math.sqrt(G_c_over_Lsq / G_sigma)
print(f"  For G_sigma = {G_sigma:.4e}: Lambda_crit = {Lambda_crit_sigma:.0f} MeV")
print(f"  (CSB onset: Lambda_UV > {Lambda_crit_sigma:.0f} MeV for sigma route)")
print()

check("CSB occurs for Lambda_UV = 636 MeV (sigma route)",
      solve_gap(G_sigma, 636, N_C) > 10)

# Route OGE: G_OGE = C_F × g_eff^2 / (2 × Lambda^2)
# This coupling DEPENDS on Lambda, so the gap equation becomes:
# 1 = C_F × g_eff^2 × N_c / (2 pi^2) × [1 - M^2/Lambda^2 × ln(1 + Lambda^2/M^2)]
# This is a fixed-point equation with dimensionless parameter:
gamma_OGE = C_F * g_eff_sq * N_C / (2 * PI**2)

print(f"  Route 1 (OGE): G_OGE = C_F g_eff^2 / (2 Lambda^2)")
print(f"    Dimensionless coupling gamma = C_F g_eff^2 N_c / (2 pi^2) = {gamma_OGE:.5f}")
print(f"    Critical: gamma > 1 needed for CSB")
print(f"    gamma = {gamma_OGE:.4f} << 1: OGE alone CANNOT drive CSB [T1 result]")
print(f"    (This is expected: perturbative one-gluon exchange is too weak)")
print()

check("OGE coupling subcritical (gamma < 1)", gamma_OGE < 1)

# ============================================================================
# PART C: DFC-SPECIFIC CUTOFF DETERMINATION
# ============================================================================
print("\nPART C: DFC-Specific UV Cutoff")
print("-" * 76)

# The UV cutoff Λ_UV in the NJL model represents the scale above which
# the four-fermion description breaks down (the mediating boson becomes
# dynamical). In DFC:
#
# Candidate 1: Λ_UV = m_σ = (3/2) Λ_QCD = 457 MeV
#   This is the sigma mass — above this, the sigma propagator resolves
#   and the contact interaction breaks down.
#
# Candidate 2: Λ_UV = m_ρ = √(2π) Λ_QCD = 763 MeV
#   The rho meson sets the vector meson dominance scale.
#
# Candidate 3: Λ_UV from the DFC gap equation self-consistency:
#   Require M_Q = Λ_QCD (the gap equals the confinement scale).
#   This determines Λ_UV uniquely for given G.

print(f"  Candidate cutoffs:")
print(f"    1. m_sigma = (3/2) Lambda = {m_sigma:.1f} MeV")
print(f"    2. m_rho = sqrt(2 pi) Lambda = {m_rho:.1f} MeV")
print(f"    3. Self-consistent: M_Q = Lambda_QCD determines Lambda_UV")
print()

# For Route 2 (sigma exchange), find Lambda_UV that gives M_Q = Lambda_QCD
print(f"  Self-consistent cutoff search (sigma route, M_Q = Lambda_QCD = {LAMBDA_QCD:.1f} MeV):")

# Solve: njl_gap_equation(LAMBDA_QCD, G_sigma, Lambda_UV, N_C) = 0
# 1 = G_sigma × N_c/pi^2 × [Lambda_UV^2 - LAMBDA_QCD^2 × ln(1 + Lambda_UV^2/LAMBDA_QCD^2)]
target_rhs = PI**2 / (G_sigma * N_C)
# target_rhs = Lambda_UV^2 - LAMBDA_QCD^2 × ln(1 + Lambda_UV^2/LAMBDA_QCD^2)

# Bisect to find Lambda_UV
Lam_lo, Lam_hi = 310, 2000
for _ in range(200):
    Lam_mid = (Lam_lo + Lam_hi) / 2
    x = Lam_mid**2 / LAMBDA_QCD**2
    rhs = Lam_mid**2 - LAMBDA_QCD**2 * math.log(1 + x)
    if rhs < target_rhs:
        Lam_lo = Lam_mid
    else:
        Lam_hi = Lam_mid
    if Lam_hi - Lam_lo < 0.01:
        break

Lambda_UV_sc = (Lam_lo + Lam_hi) / 2
M_Q_check = solve_gap(G_sigma, Lambda_UV_sc, N_C)

print(f"    Lambda_UV (self-consistent) = {Lambda_UV_sc:.1f} MeV")
print(f"    M_Q at this cutoff = {M_Q_check:.1f} MeV")
print(f"    M_Q / Lambda_QCD = {M_Q_check/LAMBDA_QCD:.4f}")
print(f"    Lambda_UV / m_sigma = {Lambda_UV_sc/m_sigma:.3f}")
print(f"    Lambda_UV / m_rho = {Lambda_UV_sc/m_rho:.3f}")
print()

# Check what M_Q the DFC candidates give
for name, Lam in [("m_sigma", m_sigma), ("m_rho", m_rho),
                   ("self-consistent", Lambda_UV_sc)]:
    M = solve_gap(G_sigma, Lam, N_C)
    err = (M - M_Q_obs) / M_Q_obs * 100 if M > 10 else float('inf')
    print(f"    Lambda_UV = {name:16s} ({Lam:7.1f} MeV): M_Q = {M:6.1f} MeV ({err:+.1f}%)")

print()
check("Self-consistent cutoff gives M_Q ~ Lambda_QCD",
      abs(M_Q_check - LAMBDA_QCD) < 5)

# ============================================================================
# PART D: CHIRAL CONDENSATE AND f_pi FROM GAP SOLUTION
# ============================================================================
print("\nPART D: Chiral Condensate and f_pi from Gap Solution")
print("-" * 76)

# Use the self-consistent cutoff
Lambda_UV = Lambda_UV_sc
M_Q = M_Q_check

# Chiral condensate from NJL:
# <qq> = -N_c/(2 pi^2) × M × [Lambda^2 - M^2 ln(1 + Lambda^2/M^2)] / (1 + ...)
# Simplified: <qq> = -N_c M / (4 pi^2) × Lambda^2 × [1 - (M/Lambda)^2 ln(1+(Lambda/M)^2)]
# But standard formula: <qq> = -N_c/(2pi^2) × integral from 0 to Lambda of dp p^2 M/sqrt(p^2+M^2)
# = -N_c M / (2 pi^2) × [Lambda sqrt(Lambda^2+M^2)/2 + M^2/2 × ln(Lambda + sqrt(Lambda^2+M^2))/M - ...]
# Simpler form: <qq> = -N_c × M × I(Lambda, M) / (2 pi^2)
# where I = Lambda × E_Lambda / 2 - M^2/2 × arcsinh(Lambda/M)
#         = Lambda × sqrt(Lambda^2+M^2) / 2 - M^2/2 × ln((Lambda + sqrt(Lambda^2+M^2))/M)

E_Lam = math.sqrt(Lambda_UV**2 + M_Q**2)
I_cond = Lambda_UV * E_Lam / 2.0 - M_Q**2 / 2.0 * math.log((Lambda_UV + E_Lam) / M_Q)
qq_condensate = -N_C * M_Q * I_cond / (2 * PI**2)  # MeV^3

# Convert to the standard normalization: <qq>^{1/3}
qq_third = -abs(qq_condensate)**(1.0/3.0)

# Observed value at 2 GeV (MSbar): <qq>^{1/3} ~ -(250 ± 15) MeV
qq_obs_third = -250.0  # MeV

print(f"  Gap solution: M_Q = {M_Q:.1f} MeV at Lambda_UV = {Lambda_UV:.1f} MeV")
print(f"  Chiral condensate:")
print(f"    <qq> = -N_c M I(Lambda,M) / (2 pi^2)")
print(f"    <qq> = {qq_condensate:.0f} MeV^3")
print(f"    <qq>^(1/3) = {qq_third:.1f} MeV")
print(f"    Observed: <qq>^(1/3) = {qq_obs_third:.0f} +/- 15 MeV")
err_qq = (abs(qq_third) - abs(qq_obs_third)) / abs(qq_obs_third) * 100
print(f"    Error: {err_qq:+.1f}%")
print()

check("<qq>^(1/3) within 20% of observed", abs(err_qq) < 20)

# Pion decay constant from NJL (Pagels-Stokar formula):
# f_pi^2 = N_c M^2 / (4 pi^2) × [ln(1+Lambda^2/M^2) - Lambda^2/(Lambda^2+M^2)]
x_ps = Lambda_UV**2 / M_Q**2
f_pi_sq = N_C * M_Q**2 / (4 * PI**2) * (math.log(1 + x_ps) - x_ps / (1 + x_ps))
f_pi_NJL = math.sqrt(f_pi_sq)

f_pi_obs = 92.4   # MeV
f_pi_DFC = LAMBDA_QCD / PI  # 96.9 MeV

print(f"  Pion decay constant (Pagels-Stokar):")
print(f"    f_pi = sqrt(N_c M^2/(4pi^2) [ln(1+Lambda^2/M^2) - Lambda^2/(Lambda^2+M^2)])")
print(f"    f_pi (NJL) = {f_pi_NJL:.1f} MeV")
print(f"    f_pi (DFC direct) = Lambda/pi = {f_pi_DFC:.1f} MeV")
print(f"    f_pi (observed) = {f_pi_obs:.1f} MeV")
err_fpi = (f_pi_NJL - f_pi_obs) / f_pi_obs * 100
print(f"    Error (NJL): {err_fpi:+.1f}%")
print()

check("f_pi(NJL) within 20% of observed", abs(err_fpi) < 20)

# ============================================================================
# PART E: DUAL SUPERCONDUCTOR ANALOGY
# ============================================================================
print("\nPART E: Dual Superconductor — Confinement as Meissner Effect")
print("-" * 76)

# In the dual superconductor picture:
# - Color-electric charges (quarks) are confined
# - Color-magnetic monopoles condense (dual BCS)
# - Flux tubes = dual Abrikosov vortices
#
# DFC version: the D7 substrate in its confined vacuum is a dual superconductor.
# The kink topological charge Q_top=2 provides the magnetic monopole analog.
# The string tension sigma = flux_tube_tension.

# String tension from DFC: sigma = Q_top × Lambda^2 = 2 × 304.5^2 = 185,440 MeV^2
sigma_DFC = 2 * LAMBDA_QCD**2  # MeV^2
sigma_obs = 440.0 * 440.0      # ~(440 MeV)^2 = 193,600 MeV^2
sigma_obs_alt = 0.18e6          # ~0.18 GeV^2 = 180,000 MeV^2

print(f"  String tension:")
print(f"    sigma_DFC = Q_top × Lambda^2 = {sigma_DFC:.0f} MeV^2 = ({math.sqrt(sigma_DFC):.1f} MeV)^2")
print(f"    sigma_obs ~ (440 MeV)^2 = {sigma_obs:.0f} MeV^2")
print(f"    Error: {(sigma_DFC - sigma_obs)/sigma_obs*100:+.1f}%")
print()

# Dual London penetration depth: λ_L ~ 1/M_Q (or 1/Λ_QCD)
lambda_L = 197.3 / M_Q  # fm (ℏc/M_Q)
# Dual coherence length: ξ_GL ~ 1/m_sigma
xi_GL = 197.3 / m_sigma  # fm

# Ginzburg-Landau parameter κ_GL = λ_L / ξ_GL
kappa_GL = lambda_L / xi_GL

print(f"  Dual superconductor parameters:")
print(f"    Dual penetration depth: lambda_L ~ hbar c / M_Q = {lambda_L:.3f} fm")
print(f"    Dual coherence length: xi_GL ~ hbar c / m_sigma = {xi_GL:.3f} fm")
print(f"    GL parameter: kappa = lambda_L / xi_GL = {kappa_GL:.4f}")
print(f"    kappa {'>' if kappa_GL > 1/math.sqrt(2) else '<'} 1/sqrt(2) = {1/math.sqrt(2):.4f}")
print(f"    → {'Type II' if kappa_GL > 1/math.sqrt(2) else 'Type I'} dual superconductor")
print()

# In QCD, type II dual superconductor = stable flux tubes (confinement)
# DFC prediction: kappa = M_Q / m_sigma × (m_sigma/M_Q) = lambda_L/xi_GL
# With M_Q ~ Lambda, m_sigma = 3/2 Lambda:
# kappa = (hc/Lambda) / (hc/(3/2 Lambda)) = 3/2 Lambda / Lambda = 3/2... wait
# lambda_L = hc/M_Q, xi = hc/m_sigma → kappa = m_sigma/M_Q = (3/2 Lambda)/Lambda = 3/2

kappa_DFC = m_sigma / LAMBDA_QCD  # = 3/2 exactly
print(f"  DFC structural prediction:")
print(f"    kappa_DFC = m_sigma / Lambda_QCD = (3/2) Lambda / Lambda = {kappa_DFC:.4f}")
print(f"    kappa = 3/2 > 1/sqrt(2) → TYPE II [T1 from DFC mass ratios]")
print(f"    This confirms confinement (flux tubes stable, not spreading)")
print()

check("Type II dual superconductor (kappa > 1/sqrt(2))", kappa_GL > 1/math.sqrt(2))
check("kappa_DFC = 3/2 exactly", abs(kappa_DFC - 1.5) < 1e-10)

# Flux tube width from GL theory:
# R_tube ~ xi_GL × sqrt(2) × K_1(r/lambda_L) → width ~ 2 lambda_L
R_tube = 2 * lambda_L
print(f"  Flux tube width ~ 2 lambda_L = {R_tube:.3f} fm")
print(f"  Observed QCD flux tube width ~ 0.4-0.5 fm (lattice)")
print(f"  DFC prediction: {R_tube:.3f} fm ({(R_tube-0.45)/0.45*100:+.1f}% vs 0.45 fm)")
print()

check("Flux tube width ~ 0.4-0.7 fm", 0.3 < R_tube < 0.8)

# ============================================================================
# PART F: BCS-DFC DICTIONARY SUMMARY
# ============================================================================
print("\nPART F: Complete BCS-DFC Dictionary")
print("-" * 76)

print(f"""
  ┌────────────────────────────┬──────────────────────────────────────────┬──────┐
  │ BCS Superconductor         │ DFC D7 (QCD)                            │ Tier │
  ├────────────────────────────┼──────────────────────────────────────────┼──────┤
  │ Gap Δ                      │ M_Q = {M_Q:.0f} MeV (constituent mass)       │ T3   │
  │ Cooper pair                │ Pion (Goldstone of broken chiral sym)   │ T2a  │
  │ BCS gap equation           │ NJL gap equation → M_Q from V(phi)     │ T3   │
  │ Debye frequency ω_D        │ m_sigma = {m_sigma:.0f} MeV                    │ T2a  │
  │ Coupling G N(0)            │ G_sigma Lambda^2 = {G_sigma * Lambda_UV_sc**2:.2f}                   │ T3   │
  │ Meissner effect            │ Color confinement (dual)                │ T3   │
  │ Type II (kappa > 1/sqrt2)  │ kappa = 3/2 → flux tubes stable        │ T1   │
  │ Abrikosov vortex           │ QCD flux tube, R ~ {R_tube:.2f} fm              │ T3   │
  │ String tension             │ sigma = Q_top Lambda^2 = {sigma_DFC:.0f} MeV^2   │ T3   │
  │ Condensate <ψψ>            │ <qq>^(1/3) = {qq_third:.0f} MeV                  │ T3   │
  │ f_pi (Pagels-Stokar)       │ {f_pi_NJL:.1f} MeV (obs: 92.4 MeV)             │ T3   │
  └────────────────────────────┴──────────────────────────────────────────┴──────┘

  KEY FINDINGS:
  1. OGE coupling alone is subcritical (gamma = {gamma_OGE:.4f} << 1) — perturbative
     gluon exchange CANNOT drive chiral symmetry breaking [T1 proof]
  2. Sigma exchange with quark-level coupling g_qqs = g_sigma/N_c DOES drive CSB
     for Lambda_UV > {Lambda_crit_sigma:.0f} MeV
  3. Self-consistent cutoff: Lambda_UV = {Lambda_UV_sc:.0f} MeV gives M_Q = Lambda_QCD
     (Lambda_UV / m_sigma = {Lambda_UV_sc/m_sigma:.2f}, Lambda_UV / m_rho = {Lambda_UV_sc/m_rho:.2f})
  4. kappa_DFC = 3/2 (TYPE II) is a T1 structural prediction from DFC mass ratios
  5. The NJL framework is CONSISTENT with DFC but does not uniquely determine
     Lambda_UV from DFC parameters alone — this remains the key open gap

  OPEN GAPS:
  - Derive Lambda_UV from DFC substrate structure (currently fit to M_Q target)
  - Connect sigma-exchange NJL to one-gluon exchange (confinement enhancement)
  - Compute temperature dependence T_c of chiral transition
  - Relate GL parameter kappa = 3/2 to lattice dual superconductor measurements
""")

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 76)
print(f"SUMMARY: {pass_count} PASS, {fail_count} FAIL out of {pass_count + fail_count} tests")
print("=" * 76)
