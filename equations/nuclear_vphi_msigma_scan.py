"""
V(phi) Constrained m_sigma Scan — Nuclear Saturation Along the Kink Line
=========================================================================

Physical question:
    C374 showed that g3 = 2*g2^2/(9*m_sigma^2) from V(phi) [T1 exact].
    Combined with g2 = -g_sigma*m_sigma/N_c [T3 from C373], this gives:

        g3 = 2*g_sigma^2/(9*N_c^2)   [m_sigma-INDEPENDENT]

    This is a remarkable algebraic result: the quartic Walecka coupling
    depends ONLY on g_sigma and N_c — not on the scalar mass. The value
    g3 = 2*pi^2*3*pi/(9*9) = 2*pi^3/27 = 2.297 is a pure DFC constant.

    Since the C370 value m_sigma = 648 MeV was derived for LINEAR Walecka
    (g2 = g3 = 0), it must be re-optimized for the nonlinear case. This
    module scans m_sigma along the V(phi) constraint line to find where
    nuclear saturation properties are best.

DFC mechanism:
    The V(phi) kink-fluctuation expansion gives a ONE-PARAMETER family
    of nonlinear Walecka models, parametrized by m_sigma alone:

        g2(m_sigma) = -g_sigma * m_sigma / N_c
        g3 = 2 * g_sigma^2 / (9 * N_c^2)    [constant]
        g_sigma = g_omega = pi*sqrt(3*pi)      [T1, C370]
        m_omega = 763.3 MeV                    [T3, C370]

    The scan determines which m_sigma gives observed saturation properties.

Key results:
    Part A: g3 m_sigma-independence [T1 algebraic]
    Part B: m_sigma scan along V(phi) constraint
    Part C: Optimal m_sigma and saturation properties
    Part D: Comparison with C370 linear and C373/C374 results
    Part E: Assessment

Key references:
    - equations/nuclear_kink_g3_vphi.py (C374, V(phi) quartic identity)
    - equations/nuclear_kink_fluctuation.py (C373, g2 sign and magnitude)
    - equations/nuclear_omega_coupling_dfc.py (C370, g_sigma = g_omega)
"""

import math
from fractions import Fraction

# =============================================================================
# Assertion infrastructure
# =============================================================================
n_assert = 0
n_pass = 0
n_fail = 0


def check(label, condition, value=None, tol=None):
    global n_assert, n_pass, n_fail
    n_assert += 1
    if tol is not None and value is not None:
        ok = abs(value) < tol
    elif isinstance(condition, bool):
        ok = condition
    else:
        ok = bool(condition)
    status = "PASS" if ok else "FAIL"
    if not ok:
        n_fail += 1
    else:
        n_pass += 1
    print(f"  [{status}] {label}")
    return ok


# =============================================================================
# Constants — DFC-derived, 0 free parameters
# =============================================================================
HBAR_C = 197.3269804  # MeV fm

# DFC couplings
G_SIGMA = math.pi * math.sqrt(3.0 * math.pi)  # = g_omega = 9.6453
G_OMEGA = G_SIGMA
M_OMEGA = 763.3    # MeV
M_N = 934.8         # MeV
N_C = 3
GAMMA = 4           # spin-isospin degeneracy

# Empirical reference values
RHO_0_EMP = 0.16
R_0_EMP = 1.20
E_A_EMP = -15.8
K_EMP_LOW = 200.0
K_EMP_HIGH = 300.0


# =============================================================================
# Part A: g3 is m_sigma-independent [T1 algebraic]
# =============================================================================
print("=" * 72)
print("Part A: g3 is m_sigma-independent — pure DFC constant")
print("=" * 72)
print()

# g2 = -g_sigma * m_sigma / N_c
# g3 = 2 * g2^2 / (9 * m_sigma^2)       [T1, C374]
#    = 2 * (g_sigma * m_sigma / N_c)^2 / (9 * m_sigma^2)
#    = 2 * g_sigma^2 / (9 * N_c^2)
#
# m_sigma cancels EXACTLY

G3_DFC = 2.0 * G_SIGMA**2 / (9.0 * N_C**2)

print(f"  g3 = 2 * g_sigma^2 / (9 * N_c^2)")
print(f"     = 2 * ({G_SIGMA:.4f})^2 / (9 * {N_C}^2)")
print(f"     = 2 * {G_SIGMA**2:.4f} / {9 * N_C**2}")
print(f"     = {G3_DFC:.6f}")
print()

# Verify m_sigma cancellation with several values
print(f"  m_sigma-independence check:")
test_masses = [400, 500, 600, 648, 700, 800, 1000]
g3_values = []
for ms in test_masses:
    g2_test = -G_SIGMA * ms / N_C
    g3_test = 2.0 * g2_test**2 / (9.0 * ms**2)
    g3_values.append(g3_test)
    print(f"    m_sigma = {ms:4d} MeV:  g2 = {g2_test:8.1f} MeV,  g3 = {g3_test:.6f}")

g3_spread = max(g3_values) - min(g3_values)
print(f"  Spread: {g3_spread:.2e} (machine zero)")
print()

check("A1: g3 m_sigma-independent (spread < 1e-12)", True, g3_spread, 1e-12)

# Exact symbolic form
# g_sigma = pi*sqrt(3*pi), so g_sigma^2 = pi^2 * 3*pi = 3*pi^3
# g3 = 2 * 3*pi^3 / (9 * 9) = 6*pi^3 / 81 = 2*pi^3 / 27
g3_symbolic = 2.0 * math.pi**3 / 27.0
g3_residual = abs(G3_DFC - g3_symbolic)

print(f"  Symbolic: g3 = 2*pi^3/27 = {g3_symbolic:.6f}")
print(f"  Residual: {g3_residual:.2e}")
print()

check("A2: g3 = 2*pi^3/27 exact", True, g3_residual, 1e-14)
print()

print(f"  KEY RESULT: g3 = 2*pi^3/27 = {G3_DFC:.4f} is a PURE DFC CONSTANT")
print(f"  It depends only on g_sigma = pi*sqrt(3*pi) [T1] and N_c = 3 [T1]")
print(f"  The V(phi) quartic identity [T1, C374] + g2 structural [T3, C373]")
print(f"  together fix g3 with NO dependence on m_sigma.")
print()


# =============================================================================
# Walecka solver (reused from C373/C374)
# =============================================================================

def scalar_density(k_F_fm, M_star_MeV):
    """Scalar density rho_s for symmetric nuclear matter."""
    k_max = k_F_fm * HBAR_C
    M_star = M_star_MeV
    N_pts = 400
    dk = k_max / N_pts
    integral = 0.0
    for i in range(N_pts + 1):
        k = i * dk
        E_k = math.sqrt(k**2 + M_star**2)
        f = k**2 * M_star / E_k
        if i == 0 or i == N_pts:
            w = 1.0
        elif i % 2 == 1:
            w = 4.0
        else:
            w = 2.0
        integral += w * f
    integral *= dk / 3.0
    return GAMMA / (2.0 * math.pi**2) * integral / HBAR_C**3


def baryon_density(k_F_fm):
    return GAMMA * k_F_fm**3 / (6.0 * math.pi**2)


def solve_sigma_nl(rho_s_fm3, g2, g3, m_sigma, tol=1e-6, max_iter=500):
    """Solve m_sigma^2*sigma + g2*sigma^2 + g3*sigma^3 = g_sigma*rho_s*hbar_c^3"""
    rhs = G_SIGMA * rho_s_fm3 * HBAR_C**3
    sigma_0 = rhs / m_sigma**2

    for _ in range(max_iter):
        f_val = m_sigma**2 * sigma_0 + g2 * sigma_0**2 + g3 * sigma_0**3 - rhs
        f_prime = m_sigma**2 + 2.0 * g2 * sigma_0 + 3.0 * g3 * sigma_0**2
        if abs(f_prime) < 1e-30:
            break
        delta = f_val / f_prime
        sigma_0 -= delta
        if sigma_0 < 0:
            sigma_0 = 0.01
        if abs(delta) < tol:
            break

    return sigma_0


def solve_self_consistent(k_F_fm, g2, g3, m_sigma, tol=1e-4, max_iter=500):
    """Solve M* = M_N - g_sigma*sigma_0 self-consistently."""
    M_star = M_N
    for _ in range(max_iter):
        rho_s = scalar_density(k_F_fm, M_star)
        sigma_0 = solve_sigma_nl(rho_s, g2, g3, m_sigma)
        M_star_new = M_N - G_SIGMA * sigma_0
        if M_star_new < 10:
            M_star_new = 10.0
        if abs(M_star_new - M_star) < tol:
            return M_star_new
        M_star = 0.3 * M_star + 0.7 * M_star_new
    return M_star


def energy_per_nucleon(k_F_fm, g2, g3, m_sigma):
    """E/A - M_N for nonlinear Walecka. Returns MeV."""
    M_star = solve_self_consistent(k_F_fm, g2, g3, m_sigma)

    k_max = k_F_fm * HBAR_C
    N_pts = 400
    dk = k_max / N_pts
    integral = 0.0
    for i in range(N_pts + 1):
        k = i * dk
        E_k = math.sqrt(k**2 + M_star**2)
        f = k**2 * E_k
        if i == 0 or i == N_pts:
            w = 1.0
        elif i % 2 == 1:
            w = 4.0
        else:
            w = 2.0
        integral += w * f
    integral *= dk / 3.0
    kinetic = GAMMA / (2.0 * math.pi**2) * integral / HBAR_C**3

    rho_s = scalar_density(k_F_fm, M_star)
    sigma_0 = solve_sigma_nl(rho_s, g2, g3, m_sigma)
    scalar_energy = (0.5 * m_sigma**2 * sigma_0**2
                     + (g2 / 3.0) * sigma_0**3
                     + (g3 / 4.0) * sigma_0**4) / HBAR_C**3

    rho_B = baryon_density(k_F_fm)
    vector_energy = G_OMEGA**2 * rho_B**2 * HBAR_C**3 / (2.0 * M_OMEGA**2)

    return (kinetic + scalar_energy + vector_energy) / rho_B - M_N


def find_saturation(g2, g3, m_sigma):
    """Find saturation point. Returns (k_F, rho, r0, E/A, K, M*/M_N) or None."""
    # Coarse scan
    best_kf = None
    best_ea = 1e10
    k_F_min, k_F_max = 0.8, 2.0
    N_scan = 120

    for i in range(N_scan + 1):
        kf = k_F_min + (k_F_max - k_F_min) * i / N_scan
        try:
            ea = energy_per_nucleon(kf, g2, g3, m_sigma)
        except Exception:
            continue
        if ea < best_ea:
            best_ea = ea
            best_kf = kf

    if best_kf is None:
        return None

    # Parabolic refinement
    for _ in range(5):
        dk = 0.01
        try:
            ea_p = energy_per_nucleon(best_kf + dk, g2, g3, m_sigma)
            ea_m = energy_per_nucleon(best_kf - dk, g2, g3, m_sigma)
            ea_c = energy_per_nucleon(best_kf, g2, g3, m_sigma)
        except Exception:
            break
        d2 = (ea_p - 2*ea_c + ea_m) / dk**2
        d1 = (ea_p - ea_m) / (2*dk)
        if abs(d2) > 1e-10:
            shift = -d1 / d2
            if abs(shift) < 0.5:
                best_kf += shift
            best_ea = energy_per_nucleon(best_kf, g2, g3, m_sigma)

    rho = baryon_density(best_kf)
    r0 = (3.0 / (4.0 * math.pi * rho))**(1.0/3.0)
    ea = energy_per_nucleon(best_kf, g2, g3, m_sigma)
    Mstar = solve_self_consistent(best_kf, g2, g3, m_sigma)

    # K
    dk_k = 0.005
    try:
        ea_p = energy_per_nucleon(best_kf + dk_k, g2, g3, m_sigma)
        ea_m = energy_per_nucleon(best_kf - dk_k, g2, g3, m_sigma)
        ea_c = energy_per_nucleon(best_kf, g2, g3, m_sigma)
        d2E = (ea_p - 2*ea_c + ea_m) / dk_k**2
        drho = GAMMA * best_kf**2 / (2.0 * math.pi**2)
        K = 9.0 * rho * d2E / drho**2
    except Exception:
        K = float('nan')

    return (best_kf, rho, r0, ea, K, Mstar / M_N)


# =============================================================================
# Part B: m_sigma scan along V(phi) constraint
# =============================================================================
print("=" * 72)
print("Part B: m_sigma scan along V(phi) constraint line")
print("=" * 72)
print()
print(f"  Constraint: g2 = -g_sigma*m_sigma/N_c,  g3 = 2*pi^3/27 = {G3_DFC:.4f}")
print()

print(f"{'m_sigma':>8s}  {'g2':>8s}  {'rho_0':>8s}  {'r_0':>6s}  {'E/A':>8s}  {'K':>8s}  {'M*/M_N':>8s}")
print("-" * 68)

scan_masses = [350, 400, 425, 450, 475, 500, 520, 540, 560, 580, 600,
               620, 648, 700, 750, 800]

results = {}
for ms in scan_masses:
    g2 = -G_SIGMA * ms / N_C
    g3 = G3_DFC

    sat = find_saturation(g2, g3, ms)
    if sat is not None:
        kf, rho, r0, ea, K, mstar_ratio = sat
        results[ms] = sat

        marker = ""
        if ms == 648:
            marker = "  <-- C370"
        if abs(rho - RHO_0_EMP) / RHO_0_EMP < 0.15:
            marker = "  <-- rho OK"
        if K_EMP_LOW <= K <= K_EMP_HIGH:
            marker += " K OK"

        print(f"{ms:>8.0f}  {g2:>8.0f}  {rho:>8.4f}  {r0:>6.3f}  {ea:>8.1f}  {K:>8.0f}  {mstar_ratio:>8.4f}{marker}")
    else:
        print(f"{ms:>8.0f}  {g2:>8.0f}  {'---':>8s}  {'---':>6s}  {'---':>8s}  {'---':>8s}  {'---':>8s}")

print()


# =============================================================================
# Part C: Find optimal m_sigma for rho_0 and E/A
# =============================================================================
print("=" * 72)
print("Part C: Optimal m_sigma for saturation")
print("=" * 72)
print()

# Fine scan around where rho_0 is closest to 0.16
best_rho_err = 1e10
best_ms_rho = None
best_EA_err = 1e10
best_ms_EA = None

for ms in range(350, 850, 5):
    g2 = -G_SIGMA * ms / N_C
    sat = find_saturation(g2, G3_DFC, ms)
    if sat is None:
        continue
    kf, rho, r0, ea, K, mstar = sat

    rho_err = abs(rho - RHO_0_EMP) / RHO_0_EMP
    if rho_err < best_rho_err:
        best_rho_err = rho_err
        best_ms_rho = ms

    ea_err = abs(ea - E_A_EMP) / abs(E_A_EMP)
    if ea < 0 and ea_err < best_EA_err:
        best_EA_err = ea_err
        best_ms_EA = ms

if best_ms_rho:
    print(f"  Best m_sigma for rho_0 match: {best_ms_rho} MeV")
    g2 = -G_SIGMA * best_ms_rho / N_C
    sat = find_saturation(g2, G3_DFC, best_ms_rho)
    if sat:
        kf, rho, r0, ea, K, mstar = sat
        rho_err = (rho - RHO_0_EMP) / RHO_0_EMP * 100
        ea_err = (ea - E_A_EMP) / abs(E_A_EMP) * 100
        print(f"    g2 = {g2:.0f} MeV")
        print(f"    rho_0 = {rho:.4f} fm^-3 ({rho_err:+.1f}%)")
        print(f"    E/A = {ea:.1f} MeV ({ea_err:+.1f}%)")
        print(f"    K = {K:.0f} MeV")
        print(f"    M*/M_N = {mstar:.4f}")
    print()

if best_ms_EA and best_ms_EA != best_ms_rho:
    print(f"  Best m_sigma for E/A match: {best_ms_EA} MeV")
    g2 = -G_SIGMA * best_ms_EA / N_C
    sat = find_saturation(g2, G3_DFC, best_ms_EA)
    if sat:
        kf, rho, r0, ea, K, mstar = sat
        rho_err = (rho - RHO_0_EMP) / RHO_0_EMP * 100
        ea_err = (ea - E_A_EMP) / abs(E_A_EMP) * 100
        print(f"    g2 = {g2:.0f} MeV")
        print(f"    rho_0 = {rho:.4f} fm^-3 ({rho_err:+.1f}%)")
        print(f"    E/A = {ea:.1f} MeV ({ea_err:+.1f}%)")
        print(f"    K = {K:.0f} MeV")
        print(f"    M*/M_N = {mstar:.4f}")
    print()

# Check if any m_sigma gives K in 200-300
best_K_err = 1e10
best_ms_K = None
for ms in range(350, 850, 5):
    g2 = -G_SIGMA * ms / N_C
    sat = find_saturation(g2, G3_DFC, ms)
    if sat is None:
        continue
    kf, rho, r0, ea, K, mstar = sat
    if ea < 0:  # only bound matter
        K_err = abs(K - 250)  # target middle of range
        if K_err < best_K_err:
            best_K_err = K_err
            best_ms_K = ms

if best_ms_K:
    print(f"  Best m_sigma for K match: {best_ms_K} MeV")
    g2 = -G_SIGMA * best_ms_K / N_C
    sat = find_saturation(g2, G3_DFC, best_ms_K)
    if sat:
        kf, rho, r0, ea, K, mstar = sat
        rho_err = (rho - RHO_0_EMP) / RHO_0_EMP * 100
        ea_err = (ea - E_A_EMP) / abs(E_A_EMP) * 100
        print(f"    g2 = {g2:.0f} MeV")
        print(f"    rho_0 = {rho:.4f} fm^-3 ({rho_err:+.1f}%)")
        print(f"    E/A = {ea:.1f} MeV ({ea_err:+.1f}%)")
        print(f"    K = {K:.0f} MeV")
        print(f"    M*/M_N = {mstar:.4f}")
    print()

# Combined optimization: minimize weighted sum of errors
best_combined = 1e10
best_ms_combined = None
for ms in range(350, 850, 2):
    g2 = -G_SIGMA * ms / N_C
    sat = find_saturation(g2, G3_DFC, ms)
    if sat is None:
        continue
    kf, rho, r0, ea, K, mstar = sat
    if ea >= 0:
        continue
    rho_frac = abs(rho - RHO_0_EMP) / RHO_0_EMP
    ea_frac = abs(ea - E_A_EMP) / abs(E_A_EMP)
    K_frac = abs(K - 250) / 250
    combined = rho_frac + ea_frac + K_frac
    if combined < best_combined:
        best_combined = combined
        best_ms_combined = ms

if best_ms_combined:
    print(f"  Best combined m_sigma: {best_ms_combined} MeV")
    g2 = -G_SIGMA * best_ms_combined / N_C
    sat = find_saturation(g2, G3_DFC, best_ms_combined)
    if sat:
        kf, rho, r0, ea, K, mstar = sat
        rho_err = (rho - RHO_0_EMP) / RHO_0_EMP * 100
        ea_err = (ea - E_A_EMP) / abs(E_A_EMP) * 100
        print(f"    g2 = {g2:.0f} MeV")
        print(f"    g3 = {G3_DFC:.4f} (= 2*pi^3/27)")
        print(f"    rho_0 = {rho:.4f} fm^-3 ({rho_err:+.1f}%)")
        print(f"    r_0 = {r0:.3f} fm")
        print(f"    E/A = {ea:.1f} MeV ({ea_err:+.1f}%)")
        print(f"    K = {K:.0f} MeV")
        print(f"    M*/M_N = {mstar:.4f}")
    print()


# =============================================================================
# Part D: Comparison table
# =============================================================================
print("=" * 72)
print("Part D: Model comparison")
print("=" * 72)
print()

# Get the best combined result
if best_ms_combined:
    g2_best = -G_SIGMA * best_ms_combined / N_C
    sat_best = find_saturation(g2_best, G3_DFC, best_ms_combined)
else:
    sat_best = None

print(f"{'Property':25s}  {'Observed':>10s}  {'Linear':>10s}  {'V(phi)648':>10s}  {'V(phi)opt':>10s}")
print("-" * 72)

# Linear (C371, m_sigma=648)
print(f"{'m_sigma (MeV)':25s}  {'---':>10s}  {'648':>10s}  {'648':>10s}  {best_ms_combined:>10d}" if best_ms_combined else "")
print(f"{'g2 (MeV)':25s}  {'---':>10s}  {'0':>10s}  {-G_SIGMA*648/N_C:>10.0f}  {g2_best:>10.0f}" if sat_best else "")
print(f"{'g3':25s}  {'---':>10s}  {'0':>10s}  {G3_DFC:>10.2f}  {G3_DFC:>10.2f}")

# C371 linear values
rho_lin, r0_lin, EA_lin, K_lin, Mstar_lin = 0.2275, 1.016, -9.4, 1646, 0.61

# C374 values (m_sigma=648, V(phi) g2+g3)
sat_648 = find_saturation(-G_SIGMA*648/N_C, G3_DFC, 648)
if sat_648:
    kf648, rho648, r0_648, ea648, K648, ms648 = sat_648
    print(f"{'rho_0 (fm^-3)':25s}  {'0.16':>10s}  {rho_lin:>10.4f}  {rho648:>10.4f}  {sat_best[1]:>10.4f}" if sat_best else "")
    print(f"{'r_0 (fm)':25s}  {'1.20':>10s}  {r0_lin:>10.3f}  {r0_648:>10.3f}  {sat_best[2]:>10.3f}" if sat_best else "")
    print(f"{'E/A - M_N (MeV)':25s}  {'-15.8':>10s}  {EA_lin:>10.1f}  {ea648:>10.1f}  {sat_best[3]:>10.1f}" if sat_best else "")
    print(f"{'K (MeV)':25s}  {'200-300':>10s}  {K_lin:>10.0f}  {K648:>10.0f}  {sat_best[4]:>10.0f}" if sat_best else "")
    print(f"{'M*/M_N':25s}  {'0.60-70':>10s}  {Mstar_lin:>10.2f}  {ms648:>10.4f}  {sat_best[5]:>10.4f}" if sat_best else "")

print()

# Checks
if sat_best:
    rho_err_best = abs(sat_best[1] - RHO_0_EMP) / RHO_0_EMP * 100
    ea_err_best = abs(sat_best[3] - E_A_EMP) / abs(E_A_EMP) * 100

    check("D1: optimal m_sigma exists", best_ms_combined is not None)
    check("D2: binding at optimal (E/A < 0)", sat_best[3] < 0)
    check("D3: rho_0 within 30%", rho_err_best < 30)
    check("D4: E/A within 50%", ea_err_best < 50)
    check("D5: K improved over linear (1646)", sat_best[4] < K_lin)
    check("D6: K in range 200-300", K_EMP_LOW <= sat_best[4] <= K_EMP_HIGH)
else:
    check("D1: optimal m_sigma exists", False)
print()


# =============================================================================
# Part E: Assessment
# =============================================================================
print("=" * 72)
print("Part E: Assessment")
print("=" * 72)
print()

print("RESULTS:")
print(f"  1. g3 = 2*pi^3/27 = {G3_DFC:.4f} is m_sigma-INDEPENDENT [T1 algebraic]")
print(f"     This is a pure DFC constant from g_sigma = pi*sqrt(3*pi) and N_c = 3.")
print()
print(f"  2. The V(phi) constraint reduces the nonlinear Walecka model to a")
print(f"     ONE-PARAMETER family in m_sigma. g2(m_sigma) = -g_sigma*m_sigma/N_c")
print(f"     and g3 = const.")
print()

if best_ms_combined and sat_best:
    print(f"  3. Best combined m_sigma = {best_ms_combined} MeV:")
    print(f"     rho_0 = {sat_best[1]:.4f} fm^-3 ({(sat_best[1]-RHO_0_EMP)/RHO_0_EMP*100:+.1f}%)")
    print(f"     E/A = {sat_best[3]:.1f} MeV ({(sat_best[3]-E_A_EMP)/abs(E_A_EMP)*100:+.1f}%)")
    print(f"     K = {sat_best[4]:.0f} MeV")
    print(f"     M*/M_N = {sat_best[5]:.4f}")
    print()

    if K_EMP_LOW <= sat_best[4] <= K_EMP_HIGH:
        print(f"  K IN OBSERVED RANGE — major improvement over linear and C373/C374!")
    elif sat_best[4] < K_lin:
        print(f"  K improved from {K_lin:.0f} to {sat_best[4]:.0f} MeV (still outside 200-300)")
    else:
        print(f"  K not improved over linear at optimal m_sigma")

print()
print("Tier assessment:")
print(f"  g3 = 2*pi^3/27 (m_sigma-independent): T1 algebraic")
print(f"  V(phi) quartic identity: T1 (C374)")
print(f"  g2 sign: T1 (C373)")
print(f"  One-parameter family: T3 structural")
print(f"  Saturation properties: T4 (mean-field limitations)")
print()
print("What remains open (T4):")
print("  - Mean-field approximation itself is the limitation")
print("  - Beyond-MF corrections: RPA, Fock terms, density-dependent couplings")
print("  - The V(phi) constraint is algebraically correct but QHD-I mean field")
print("    is too simple to simultaneously reproduce rho_0, E/A, K")
print("  - Shell corrections, pairing, tensor force still needed")
print()


# =============================================================================
# Final summary
# =============================================================================
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()
print(f"  Total assertions: {n_assert}")
print(f"  PASS: {n_pass}")
print(f"  FAIL: {n_fail}")
print()
if n_fail == 0:
    print("  ALL ASSERTIONS PASSED")
else:
    print(f"  {n_fail} ASSERTION(S) FAILED")
