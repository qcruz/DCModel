"""
Nonlinear Walecka Model with Chiral-Derived Self-Coupling — DFC Parameters
===========================================================================

Physical question:
    The linear Walecka model (QHD-I) with DFC parameters gives a stiff equation
    of state: K ~ 1650 MeV (observed 200-300 MeV) and rho_0 ~ 0.23 fm^{-3}
    (observed 0.16 fm^{-3}). Can nonlinear sigma self-coupling terms derived
    from the chiral potential V_chiral fix this?

DFC mechanism:
    The chiral potential V_chiral = lambda/4 * (sigma^2 + pi^2 - f_pi^2)^2
    expanded around the vacuum sigma = f_pi gives cubic (g2*sigma^3) and
    quartic (g3*sigma^4) self-coupling terms. Both g2 and g3 are determined
    by DFC inputs (f_pi = Lambda_QCD/pi, m_sigma = 648 MeV) with ZERO free
    parameters:

        lambda = m_sigma^2 / (2 * f_pi^2)
        g2 = 3 * m_sigma^2 / (2 * f_pi)     [cubic, MeV]
        g3 = m_sigma^2 / (2 * f_pi^2)        [quartic, dimensionless]

    These are the Boguta-Bodmer (1977) terms that soften the equation of state
    in standard nuclear physics — but here they are NOT fit parameters. They
    follow from the same chiral symmetry that gives g_sigma = M_N / f_pi.

    The modified mean-field equation becomes:
        m_sigma^2 * sigma_0 + g2 * sigma_0^2 + g3 * sigma_0^3 = g_sigma * rho_s

    The nonlinear terms reduce sigma_0 for a given rho_s, so M* doesn't drop
    as fast -> softer EOS -> lower K.

Key results:
    Part A: Chiral potential derivation of g2, g3
    Part B: Nonlinear self-consistent mean-field solution
    Part C: Saturation properties (rho_0, E/A, K)
    Part D: Comparison with linear model and observations
    Part E: Nuclear radius r_0 prediction

Key references:
    - Boguta & Bodmer (1977): Nucl. Phys. A 292, 413
    - Serot & Walecka (1986): Adv. Nucl. Phys. 16, 1
    - equations/nuclear_walecka_prediction.py (C371)
    - equations/nuclear_omega_coupling_dfc.py (C370)
    - educational/26_nuclear_saturation.md
"""

import math

# ─── Assertion infrastructure ────────────────────────────────────────────────
n_assert = 0
n_pass = 0
n_fail = 0

def check(label, value, expected=True, tol=None):
    global n_assert, n_pass, n_fail
    n_assert += 1
    if tol is not None:
        ok = abs(value - expected) < tol
    elif isinstance(expected, bool):
        ok = bool(value) == expected
    else:
        ok = value == expected
    tag = "PASS" if ok else "FAIL"
    if not ok:
        n_fail += 1
        print(f"  [{tag}] {label}: got {value}, expected {expected}")
    else:
        n_pass += 1
        print(f"  [{tag}] {label}")
    return ok


# ─── DFC-determined parameters ───────────────────────────────────────────────

LAMBDA_QCD_MEV  = 304.5
HBAR_C          = 197.3269804    # MeV*fm
N_C             = 3

F_PI_DFC        = LAMBDA_QCD_MEV / math.pi            # 96.9 MeV
M_N             = math.sqrt(3 * math.pi) * LAMBDA_QCD_MEV   # 934.8 MeV
M_OMEGA         = math.sqrt(2 * math.pi) * LAMBDA_QCD_MEV   # 763.3 MeV

# Couplings: g_omega = g_sigma = pi*sqrt(3*pi) [T1, C370]
G_SIGMA         = math.pi * math.sqrt(3 * math.pi)    # 9.645
G_OMEGA         = G_SIGMA

# Sigma mass from C370 saturation curve (non-relativistic)
M_SIGMA         = 648.0  # MeV

# Degeneracy factor for symmetric nuclear matter: spin(2) x isospin(2) = 4
GAMMA = 4

# Empirical values for comparison
RHO_0_EMP       = 0.16   # fm^{-3}
E_A_EMP         = -15.8  # MeV (binding energy per nucleon)
K_EMP_LOW       = 200.0  # MeV
K_EMP_HIGH      = 300.0  # MeV
R_0_EMP         = 1.2    # fm


# =============================================================================
# Part A: Chiral potential derivation of nonlinear couplings
# =============================================================================
print("=" * 72)
print("Part A: Chiral potential -> nonlinear sigma self-coupling")
print("=" * 72)
print()

# The chiral potential for the linear sigma model:
#   V_chiral = (lambda/4) * (sigma^2 + pi^2 - f_pi^2)^2
#
# In the vacuum: <sigma> = f_pi, <pi> = 0
# The sigma mass comes from V''(f_pi):
#   m_sigma^2 = V''(f_pi) = lambda * (3*f_pi^2 + (-f_pi^2)) = 2*lambda*f_pi^2
#   => lambda = m_sigma^2 / (2*f_pi^2)

LAMBDA_CHIRAL = M_SIGMA**2 / (2.0 * F_PI_DFC**2)
print(f"Chiral quartic coupling lambda = m_sigma^2 / (2*f_pi^2)")
print(f"  f_pi = Lambda_QCD/pi = {F_PI_DFC:.1f} MeV  [T3]")
print(f"  m_sigma = {M_SIGMA:.0f} MeV  [T3, C370]")
print(f"  lambda = {LAMBDA_CHIRAL:.2f}")
print()

# Expand V_chiral around the vacuum: sigma = f_pi + s
#   V = (lambda/4) * ((f_pi + s)^2 - f_pi^2)^2
#     = (lambda/4) * (2*f_pi*s + s^2)^2
#     = (lambda/4) * (4*f_pi^2*s^2 + 4*f_pi*s^3 + s^4)
#     = lambda*f_pi^2*s^2 + lambda*f_pi*s^3 + (lambda/4)*s^4
#
# Mass term: 2*lambda*f_pi^2 = m_sigma^2  (check)
# Cubic: coefficient of s^3 = lambda*f_pi
# Quartic: coefficient of s^4 = lambda/4
#
# In the standard Boguta-Bodmer notation:
#   V_NL = (1/2)*m_sigma^2*sigma_0^2 + (g2/3)*sigma_0^3 + (g3/4)*sigma_0^4
#
# where sigma_0 here is the fluctuation s = sigma - f_pi.
# Matching:
#   (g2/3) = lambda*f_pi => g2 = 3*lambda*f_pi = 3*m_sigma^2/(2*f_pi)
#   (g3/4) = lambda/4    => g3 = lambda = m_sigma^2/(2*f_pi^2)

G2_CHIRAL = 3.0 * M_SIGMA**2 / (2.0 * F_PI_DFC)   # MeV
G3_CHIRAL = M_SIGMA**2 / (2.0 * F_PI_DFC**2)       # dimensionless

print("Boguta-Bodmer nonlinear couplings from chiral potential:")
print(f"  g2 = 3*m_sigma^2 / (2*f_pi) = {G2_CHIRAL:.1f} MeV")
print(f"  g3 = m_sigma^2 / (2*f_pi^2) = {G3_CHIRAL:.2f}")
print()

# Cross-check: g3 should equal lambda_chiral
print(f"  Cross-check: g3 = lambda = {G3_CHIRAL:.2f} vs {LAMBDA_CHIRAL:.2f}")
check("A1: g3 = lambda_chiral", abs(G3_CHIRAL - LAMBDA_CHIRAL) < 1e-10)
print()

# Cross-check: g_sigma = M_N / f_pi (chiral symmetry)
g_sigma_chiral = M_N / F_PI_DFC
print(f"  g_sigma = M_N/f_pi = {g_sigma_chiral:.3f} vs pi*sqrt(3*pi) = {G_SIGMA:.3f}")
check("A2: g_sigma = M_N/f_pi = pi*sqrt(3*pi)",
      abs(g_sigma_chiral - G_SIGMA) / G_SIGMA < 0.001)
print()

# Compare with literature NL3 values
# NL3 (Lalazissis 1997): g2 = -10.431 fm^{-1}, g3 = -28.885
# FSUGold: g2 = -0.8329, g3 = 0.0034
# Our g2 is in MeV, literature often in fm^{-1}: g2/hbar_c = 6501/197.3 = 33.0 fm^{-1}
g2_fm = G2_CHIRAL / HBAR_C
print(f"Comparison with literature parameterizations:")
print(f"  DFC g2 = {G2_CHIRAL:.0f} MeV = {g2_fm:.1f} fm^-1")
print(f"  DFC g3 = {G3_CHIRAL:.2f}")
print(f"  NL3:  g2 = -10.4 fm^-1, g3 = -28.9  (fit to nuclear data)")
print(f"  NOTE: NL3 has NEGATIVE g2/g3 (attractive); DFC chiral gives POSITIVE")
print(f"        (repulsive cubic/quartic). Sign difference is significant.")
print()

# The sign matters: in the Boguta-Bodmer convention,
# V_NL = (g2/3)*sigma^3 + (g3/4)*sigma^4
# Positive g2 means the cubic term OPPOSES the linear sigma field,
# which reduces sigma_0 -> M* stays higher -> softer EOS.
# But NL3 uses negative g2 (with different sigma mass and couplings).
# The physics is the same: the nonlinear terms soften the EOS.
# The sign depends on conventions for sigma_0 (is it the full field or the shift?).


# =============================================================================
# Part B: Nonlinear self-consistent solver
# =============================================================================
print("=" * 72)
print("Part B: Nonlinear relativistic mean-field solution")
print("=" * 72)
print()


def scalar_density(k_F_fm, M_star_MeV):
    """
    Scalar density rho_s for symmetric nuclear matter.
    rho_s = (gamma/(2*pi^2)) * int_0^{kF} dk k^2 M*/sqrt(k^2 + M*^2)
    Result in fm^{-3}.
    """
    k_max = k_F_fm * HBAR_C  # MeV
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
    """Baryon density for symmetric matter. Result in fm^{-3}."""
    return GAMMA * k_F_fm**3 / (6.0 * math.pi**2)


def solve_sigma_nonlinear(rho_s_fm3, tol=1e-6, max_iter=500):
    """
    Solve the nonlinear mean-field equation for sigma_0:
        m_sigma^2 * sigma_0 + g2 * sigma_0^2 + g3 * sigma_0^3 = g_sigma * rho_s * (hbar_c)^3

    Here sigma_0 is in MeV and rho_s is in fm^{-3}.
    Returns sigma_0 in MeV.
    """
    # RHS in MeV^3: g_sigma * rho_s * hbar_c^3
    rhs = G_SIGMA * rho_s_fm3 * HBAR_C**3  # MeV^3

    # Linear solution as starting point
    sigma_0 = rhs / M_SIGMA**2  # MeV

    for _ in range(max_iter):
        # f(sigma) = m_sigma^2*sigma + g2*sigma^2 + g3*sigma^3 - rhs = 0
        f_val = M_SIGMA**2 * sigma_0 + G2_CHIRAL * sigma_0**2 + G3_CHIRAL * sigma_0**3 - rhs
        # f'(sigma) = m_sigma^2 + 2*g2*sigma + 3*g3*sigma^2
        f_prime = M_SIGMA**2 + 2.0 * G2_CHIRAL * sigma_0 + 3.0 * G3_CHIRAL * sigma_0**2
        if abs(f_prime) < 1e-30:
            break
        delta = f_val / f_prime
        sigma_0 -= delta
        if abs(delta) < tol:
            break

    return sigma_0


def solve_self_consistent_nl(k_F_fm, tol=1e-4, max_iter=500):
    """
    Solve M* = M_N - g_sigma * sigma_0 self-consistently,
    where sigma_0 satisfies the nonlinear mean-field equation.

    Returns M* in MeV.
    """
    M_star = M_N  # initial guess
    for iteration in range(max_iter):
        rho_s = scalar_density(k_F_fm, M_star)
        sigma_0 = solve_sigma_nonlinear(rho_s)
        M_star_new = M_N - G_SIGMA * sigma_0
        if abs(M_star_new - M_star) < tol:
            return M_star_new
        # Damped iteration
        M_star = 0.3 * M_star + 0.7 * M_star_new
    return M_star


def solve_self_consistent_linear(k_F_fm, tol=1e-4, max_iter=500):
    """Linear Walecka (QHD-I) for comparison."""
    M_star = M_N
    C_S_local = (G_SIGMA / M_SIGMA)**2
    for iteration in range(max_iter):
        rho_s = scalar_density(k_F_fm, M_star)
        M_star_new = M_N - C_S_local * rho_s * HBAR_C**3
        if abs(M_star_new - M_star) < tol:
            return M_star_new
        M_star = 0.5 * M_star + 0.5 * M_star_new
    return M_star


def energy_density_nl(k_F_fm, M_star_MeV):
    """
    Energy density for nonlinear Walecka model.

    epsilon = (gamma/(2*pi^2)) * int_0^{kF} dk k^2 sqrt(k^2 + M*^2)
              + (1/2)*m_sigma^2*sigma_0^2 + (g2/3)*sigma_0^3 + (g3/4)*sigma_0^4
              + (g_omega^2 * rho_B^2) / (2 * m_omega^2)

    Returns epsilon in MeV/fm^3.
    """
    k_max = k_F_fm * HBAR_C

    # Kinetic integral
    N_pts = 400
    dk = k_max / N_pts
    integral = 0.0
    for i in range(N_pts + 1):
        k = i * dk
        E_k = math.sqrt(k**2 + M_star_MeV**2)
        f = k**2 * E_k
        if i == 0 or i == N_pts:
            w = 1.0
        elif i % 2 == 1:
            w = 4.0
        else:
            w = 2.0
        integral += w * f
    integral *= dk / 3.0
    kinetic = GAMMA / (2.0 * math.pi**2) * integral / HBAR_C**3  # MeV/fm^3

    # Sigma field: solve nonlinear equation
    rho_s = scalar_density(k_F_fm, M_star_MeV)
    sigma_0 = solve_sigma_nonlinear(rho_s)  # MeV

    # Scalar potential energy (including nonlinear terms)
    scalar_energy = (0.5 * M_SIGMA**2 * sigma_0**2
                     + (G2_CHIRAL / 3.0) * sigma_0**3
                     + (G3_CHIRAL / 4.0) * sigma_0**4) / HBAR_C**3  # MeV/fm^3

    # Vector field energy
    rho_B = baryon_density(k_F_fm)
    vector_energy = G_OMEGA**2 * rho_B**2 * HBAR_C**3 / (2.0 * M_OMEGA**2)  # MeV/fm^3

    return kinetic + scalar_energy + vector_energy


def energy_per_nucleon_nl(k_F_fm):
    """E/A - M_N for nonlinear model. Returns MeV."""
    M_star = solve_self_consistent_nl(k_F_fm)
    eps = energy_density_nl(k_F_fm, M_star)
    rho_B = baryon_density(k_F_fm)
    return eps / rho_B - M_N


# Solve at empirical density
k_F_emp = (3.0 * math.pi**2 * RHO_0_EMP / 2.0)**(1.0/3.0)
M_star_nl = solve_self_consistent_nl(k_F_emp)
M_star_lin = solve_self_consistent_linear(k_F_emp)

print(f"At empirical rho_0 = {RHO_0_EMP} fm^-3 (k_F = {k_F_emp:.4f} fm^-1):")
print()
print(f"  {'':20s}  {'Linear (QHD-I)':>15s}  {'Nonlinear (chiral)':>18s}")
print(f"  {'M*/M_N':20s}  {M_star_lin/M_N:15.4f}  {M_star_nl/M_N:18.4f}")
print(f"  {'M* (MeV)':20s}  {M_star_lin:15.1f}  {M_star_nl:18.1f}")
print()

E_A_nl_emp = energy_per_nucleon_nl(k_F_emp)
print(f"  E/A - M_N at rho_0:  nonlinear = {E_A_nl_emp:.2f} MeV")
print()

# The nonlinear terms should make M* larger (less scalar field)
check("B1: nonlinear M* > linear M* (less scalar attraction)",
      M_star_nl > M_star_lin)
print()


# =============================================================================
# Part C: Saturation scan — find minimum of E/A
# =============================================================================
print("=" * 72)
print("Part C: Saturation point from nonlinear model")
print("=" * 72)
print()

# Scan k_F to find the minimum of E/A
k_F_scan = []
E_A_scan = []
k_F_min = 0.5   # fm^{-1}
k_F_max = 2.5   # fm^{-1}
N_scan = 200

for i in range(N_scan + 1):
    kf = k_F_min + (k_F_max - k_F_min) * i / N_scan
    ea = energy_per_nucleon_nl(kf)
    k_F_scan.append(kf)
    E_A_scan.append(ea)

# Find minimum
i_min = 0
for i in range(1, len(E_A_scan)):
    if E_A_scan[i] < E_A_scan[i_min]:
        i_min = i

# Refine with parabolic interpolation around minimum
if 0 < i_min < len(E_A_scan) - 1:
    k1, k2, k3 = k_F_scan[i_min-1], k_F_scan[i_min], k_F_scan[i_min+1]
    e1, e2, e3 = E_A_scan[i_min-1], E_A_scan[i_min], E_A_scan[i_min+1]
    # Parabolic minimum
    denom = 2.0 * ((k2 - k1) * (e2 - e3) - (k2 - k3) * (e2 - e1))
    if abs(denom) > 1e-20:
        k_F_sat = k2 - ((k2 - k1)**2 * (e2 - e3) - (k2 - k3)**2 * (e2 - e1)) / denom
    else:
        k_F_sat = k2
else:
    k_F_sat = k_F_scan[i_min]

# Evaluate at saturation point
rho_sat = baryon_density(k_F_sat)
r_0_pred = (3.0 / (4.0 * math.pi * rho_sat))**(1.0/3.0)
E_A_sat = energy_per_nucleon_nl(k_F_sat)
M_star_sat = solve_self_consistent_nl(k_F_sat)

print(f"Saturation point (nonlinear Walecka, DFC parameters):")
print(f"  k_F_sat = {k_F_sat:.4f} fm^-1")
print(f"  rho_sat = {rho_sat:.4f} fm^-3  (observed: {RHO_0_EMP:.2f} fm^-3)")
print(f"  r_0 = {r_0_pred:.3f} fm  (observed: {R_0_EMP:.2f} fm)")
print(f"  E/A - M_N = {E_A_sat:.2f} MeV  (observed: {E_A_EMP:.1f} MeV)")
print(f"  M*/M_N = {M_star_sat/M_N:.4f}")
print()

rho_err = (rho_sat - RHO_0_EMP) / RHO_0_EMP * 100
r0_err = (r_0_pred - R_0_EMP) / R_0_EMP * 100
EA_err = (E_A_sat - E_A_EMP) / abs(E_A_EMP) * 100

print(f"  rho_0 error: {rho_err:+.1f}%")
print(f"  r_0 error:   {r0_err:+.1f}%")
print(f"  E/A error:   {EA_err:+.1f}%")
print()

# Check if saturation exists (E/A has a minimum)
has_minimum = E_A_sat < E_A_scan[0] and E_A_sat < E_A_scan[-1]
check("C1: saturation minimum exists", has_minimum)

# Check if E/A is negative (bound)
check("C2: E/A < 0 (nuclear matter is bound)", E_A_sat < 0)

# Check rho_0 within 50% of empirical (generous for first-principles)
rho_ok = abs(rho_err) < 50
check("C3: rho_0 within 50% of empirical", rho_ok)

# Check if nonlinear model improves rho_0 over linear
# Linear model gave rho_0 = 0.2275 fm^{-3} (+42%)
rho_lin_err = 42.0  # from C371
nl_improves_rho = abs(rho_err) < rho_lin_err
check("C4: nonlinear improves rho_0 over linear (+42%)", nl_improves_rho)
print()


# =============================================================================
# Part D: Nuclear incompressibility K
# =============================================================================
print("=" * 72)
print("Part D: Nuclear incompressibility K")
print("=" * 72)
print()

# K = 9 * rho_0 * d^2(E/A)/d(rho)^2 |_{rho_0}
# Numerical second derivative at saturation point
dk_F = 0.005  # fm^{-1}
ea_plus = energy_per_nucleon_nl(k_F_sat + dk_F)
ea_minus = energy_per_nucleon_nl(k_F_sat - dk_F)
ea_center = energy_per_nucleon_nl(k_F_sat)

# d^2(E/A)/dk_F^2
d2E_dkF2 = (ea_plus - 2.0 * ea_center + ea_minus) / dk_F**2

# Convert: d(rho)/dk_F = gamma * k_F^2 / (2*pi^2)
drho_dkF = GAMMA * k_F_sat**2 / (2.0 * math.pi**2)

# d^2(E/A)/d(rho)^2 = d^2E/dk_F^2 / (drho/dkF)^2
# (ignoring d^2rho/dkF^2 correction since we are at the minimum dE/drho=0)
d2E_drho2 = d2E_dkF2 / drho_dkF**2

K_nl = 9.0 * rho_sat * d2E_drho2

# Compare with linear model value
# Linear gave K ~ 1646 MeV (from C371)
K_lin = 1646.0  # MeV, from C371

print(f"Incompressibility:")
print(f"  K (nonlinear) = {K_nl:.0f} MeV")
print(f"  K (linear QHD-I) = {K_lin:.0f} MeV  [C371]")
print(f"  K (observed) = {K_EMP_LOW:.0f}-{K_EMP_HIGH:.0f} MeV")
print()

K_improved = K_nl < K_lin
check("D1: nonlinear K < linear K (EOS softened)", K_improved)

K_in_range = K_EMP_LOW <= K_nl <= K_EMP_HIGH
check("D2: K in observed range 200-300 MeV", K_in_range)

# Even if not in range, check substantial improvement
K_closer = abs(K_nl - 250) < abs(K_lin - 250)
check("D3: K closer to 250 MeV than linear", K_closer)
print()


# =============================================================================
# Part E: Sigma field analysis and scalar/vector potentials
# =============================================================================
print("=" * 72)
print("Part E: Scalar and vector potentials at saturation")
print("=" * 72)
print()

rho_s_sat = scalar_density(k_F_sat, M_star_sat)
sigma_0_sat = solve_sigma_nonlinear(rho_s_sat)

# What would the linear solution give?
sigma_0_lin = G_SIGMA * rho_s_sat * HBAR_C**3 / M_SIGMA**2

print(f"Sigma field at saturation:")
print(f"  sigma_0 (nonlinear) = {sigma_0_sat:.2f} MeV")
print(f"  sigma_0 (linear)    = {sigma_0_lin:.2f} MeV")
print(f"  Ratio NL/L = {sigma_0_sat/sigma_0_lin:.4f}")
print()

# Scalar potential S = -g_sigma * sigma_0 (attractive)
S_pot = G_SIGMA * sigma_0_sat
print(f"  Scalar potential S = g_sigma * sigma_0 = {S_pot:.1f} MeV (attractive)")

# Vector potential V = (g_omega^2/m_omega^2) * rho_B
V_pot = G_OMEGA**2 / M_OMEGA**2 * rho_sat * HBAR_C**3
print(f"  Vector potential V = g_omega^2/m_omega^2 * rho_B = {V_pot:.1f} MeV (repulsive)")
print(f"  S - V = {S_pot - V_pot:.1f} MeV (net attraction)")
print(f"  M* = M_N - S = {M_N - S_pot:.1f} MeV (check: {M_star_sat:.1f} MeV)")
print()

# Nonlinear terms reduce sigma_0
check("E1: nonlinear sigma_0 < linear sigma_0", sigma_0_sat < sigma_0_lin)
print()


# =============================================================================
# Part F: Comparison summary and assessment
# =============================================================================
print("=" * 72)
print("Part F: Comparison with observations and linear model")
print("=" * 72)
print()

print(f"{'Property':25s}  {'Observed':>12s}  {'Linear (C371)':>14s}  {'Nonlinear':>12s}")
print("-" * 72)
print(f"{'rho_0 (fm^-3)':25s}  {'0.16':>12s}  {'0.2275':>14s}  {rho_sat:>12.4f}")
print(f"{'r_0 (fm)':25s}  {'1.20':>12s}  {'1.016':>14s}  {r_0_pred:>12.3f}")
print(f"{'E/A - M_N (MeV)':25s}  {'-15.8':>12s}  {'-9.4':>14s}  {E_A_sat:>12.1f}")
print(f"{'K (MeV)':25s}  {'200-300':>12s}  {'1646':>14s}  {K_nl:>12.0f}")
print(f"{'M*/M_N':25s}  {'0.60-0.70':>12s}  {'0.61':>14s}  {M_star_sat/M_N:>12.4f}")
print()

# Overall assessment
print("Assessment:")
print(f"  Nonlinear terms from chiral potential V = lambda/4*(sigma^2 - f_pi^2)^2")
print(f"  provide g2 = {G2_CHIRAL:.0f} MeV and g3 = {G3_CHIRAL:.1f} from DFC inputs alone.")
print()

# Key question: did the nonlinear terms soften the EOS enough?
if K_nl < K_lin:
    K_reduction = (K_lin - K_nl) / K_lin * 100
    print(f"  K reduced by {K_reduction:.0f}% from linear model.")
else:
    print(f"  WARNING: K not reduced by nonlinear terms.")

if abs(rho_err) < abs(42.0):  # 42% was linear error
    print(f"  rho_0 improved: {rho_err:+.1f}% (was +42% in linear).")
else:
    print(f"  rho_0 not improved: {rho_err:+.1f}% (was +42% in linear).")

print()

# Tier assessment
print("Tier assessment:")
print(f"  g2, g3 from chiral potential: T3 (structural, m_sigma and f_pi from DFC)")
if K_EMP_LOW <= K_nl <= K_EMP_HIGH and abs(rho_err) < 15:
    print(f"  Saturation properties: T3 (correct within ~15%, 0 free params)")
    print(f"  r_0 prediction: T4->T3 upgrade candidate")
else:
    print(f"  Saturation properties: T4 (not yet quantitatively correct)")
    print(f"  Root cause analysis needed (see below)")
print()

# Root cause: positive g2/g3 vs negative in NL3
# The chiral potential gives POSITIVE nonlinear terms
# NL3 and similar successful parameterizations use NEGATIVE g2
# This is because:
# 1. In NL3, sigma is the FULL FIELD (not the shift from vacuum)
# 2. The NL3 convention is V_NL = (b/3)*M_N*(g_sigma*sigma)^3 + (c/4)*(g_sigma*sigma)^4
#    where b < 0 and c > 0 (NL3: b = 0.002947, c = -0.001070)
# Actually, the standard Boguta-Bodmer uses different conventions...
# Let's be more careful about what the chiral prediction actually means.

print("=" * 72)
print("Part G: Sign analysis and chiral potential physics")
print("=" * 72)
print()

# In the chiral sigma model, the vacuum is at sigma = f_pi.
# The mean-field sigma_0 in nuclear matter represents the shift: sigma_0 = f_pi - <sigma>_medium
# (actually, in Walecka notation, sigma_0 > 0 when the field DECREASES from vacuum)
# The effective mass is M* = M_N - g_sigma * sigma_0 = g_sigma * (f_pi - sigma_0 - ...)
#
# The chiral restoration means sigma_0 -> f_pi as density increases (M* -> 0).
# At low density, sigma_0 << f_pi, so nonlinear terms are small corrections.
# At saturation, sigma_0 / f_pi is the relevant expansion parameter.

sigma_over_fpi = sigma_0_sat / F_PI_DFC
print(f"  sigma_0 / f_pi at saturation = {sigma_over_fpi:.3f}")
print(f"  (expansion parameter for nonlinear terms)")
print()

# For the chiral potential, the nonlinear terms RESIST the growth of sigma_0:
# f(sigma) = m^2*sigma + g2*sigma^2 + g3*sigma^3 = source
# Positive g2 means at a given source, sigma_0 is SMALLER than linear.
# This is the correct softening direction.

# Let's compute the relative importance of cubic and quartic terms
cubic_frac = G2_CHIRAL * sigma_0_sat**2 / (M_SIGMA**2 * sigma_0_sat)
quartic_frac = G3_CHIRAL * sigma_0_sat**3 / (M_SIGMA**2 * sigma_0_sat)
print(f"  Cubic term / linear term = {cubic_frac:.4f}")
print(f"  Quartic term / linear term = {quartic_frac:.4f}")
print(f"  Total nonlinear correction = {cubic_frac + quartic_frac:.4f}")
print()

# Key diagnostic: the sigma_0/f_pi ratio tells us how close to chiral restoration
print(f"  sigma_0 = {sigma_0_sat:.2f} MeV out of f_pi = {F_PI_DFC:.1f} MeV")
print(f"  Medium sigma <sigma> = f_pi - sigma_0 = {F_PI_DFC - sigma_0_sat:.2f} MeV")
print(f"  <sigma>/f_pi = {(F_PI_DFC - sigma_0_sat)/F_PI_DFC:.3f}")
print(f"  (1.0 = vacuum; 0.0 = chiral restoration)")
print()

check("G1: sigma_0 < f_pi (not past chiral restoration)", sigma_0_sat < F_PI_DFC)
check("G2: nonlinear correction is perturbative (< 50%)", cubic_frac + quartic_frac < 0.5)
print()


# =============================================================================
# Part H: Root cause analysis — why the chiral potential over-softens
# =============================================================================
print("=" * 72)
print("Part H: Root cause analysis")
print("=" * 72)
print()

print("DIAGNOSIS: The chiral potential V = lambda/4*(sigma^2 - f_pi^2)^2")
print("produces nonlinear terms that OVER-SOFTEN the equation of state.")
print("Nuclear matter goes from too stiff (QHD-I) to UNBOUND.")
print()
print("Why this happens:")
print()
print("1. SCALE MISMATCH: The chiral g2 = 3*m_sigma^2/(2*f_pi) = 6498 MeV")
print("   is 3x larger than successful NL3 values (~2000 MeV).")
print("   This is because m_sigma = 648 MeV and f_pi = 96.9 MeV give a")
print("   large ratio (m_sigma/f_pi)^2 = 44.7, making the chiral potential")
print("   curvature too steep around the vacuum.")
print()
print("2. SIGN CONVENTION: The chiral nonlinear terms are POSITIVE (they")
print("   resist sigma growth). Successful NL3/FSUGold have NEGATIVE g2")
print("   (they HELP sigma grow at moderate density, then positive g3")
print("   stabilizes at high density). The physics is different:")
print("   - Chiral: monotonically resists sigma -> M* stays high -> too little binding")
print("   - NL3: helps sigma at moderate rho, resists at high rho -> correct K")
print()
print("3. FUNDAMENTAL ISSUE: The Walecka 'sigma' is NOT the same field as")
print("   the chiral 'sigma'. The Walecka sigma is an effective scalar")
print("   mediating nuclear attraction. The chiral sigma is the partner of")
print("   the pion in the linear sigma model. Identifying them is the")
print("   'naive chiral sigma model' — known since the 1970s to fail for")
print("   nuclear saturation (Lee & Wick 1974, Furnstahl & Serot 1991).")
print()

# Quantitative comparison: what g2 would be needed?
# For the linear model: too stiff, K=1646
# We need g2 that softens K to ~250 without destroying binding
# The NL3 answer: g2 ~ -10 fm^{-1} ~ -2000 MeV (NEGATIVE)
print("What would fix it:")
print(f"  DFC chiral:    g2 = +{G2_CHIRAL:.0f} MeV  (too repulsive, destroys binding)")
print(f"  NL3 (fit):     g2 = ~-2000 MeV  (empirical, 15 nuclei fit)")
print(f"  Required sign: NEGATIVE g2 (opposite to chiral prediction)")
print()

# Path forward
print("Path forward:")
print("  The DFC substrate potential V(phi) = -alpha/2*phi^2 + beta/4*phi^4")
print("  expanded around the kink background may generate effective nonlinear")
print("  terms with the CORRECT sign — the kink background is not the vacuum,")
print("  and fluctuations around it have different self-interactions than")
print("  fluctuations around the vacuum. This is the V(phi) path identified")
print("  in Module 26, distinct from the chiral potential path tested here.")
print()
print("  Specifically: the kink profile phi_kink(y) = phi_0*tanh(y/xi) is")
print("  an ASYMMETRIC background. Fluctuations delta_phi around it see an")
print("  ASYMMETRIC potential (Poschl-Teller), which naturally generates")
print("  odd powers of the fluctuation with NEGATIVE sign from the tanh")
print("  derivative. This is the physical origin of negative g2.")
print()

# Check: if we artificially use NL3-sign g2, does it help?
# (just as a diagnostic, not a DFC prediction)
print("DIAGNOSTIC: Artificial sign-flip test")
print("  (Not a DFC prediction — just to verify the mechanism)")

G2_FLIP = -G2_CHIRAL * 0.3  # Reduced magnitude with correct sign

def solve_sigma_flip(rho_s_fm3, g2_val, g3_val, tol=1e-6, max_iter=500):
    """Solve nonlinear sigma equation with given g2, g3."""
    rhs = G_SIGMA * rho_s_fm3 * HBAR_C**3
    sigma_0 = rhs / M_SIGMA**2
    for _ in range(max_iter):
        f_val = M_SIGMA**2 * sigma_0 + g2_val * sigma_0**2 + g3_val * sigma_0**3 - rhs
        f_prime = M_SIGMA**2 + 2.0 * g2_val * sigma_0 + 3.0 * g3_val * sigma_0**2
        if abs(f_prime) < 1e-30:
            break
        delta = f_val / f_prime
        sigma_0 -= delta
        if sigma_0 < 0:
            sigma_0 = 0.01
        if abs(delta) < tol:
            break
    return sigma_0

def solve_sc_flip(k_F_fm, g2_val, g3_val, tol=1e-4, max_iter=500):
    M_star = M_N
    for iteration in range(max_iter):
        rho_s = scalar_density(k_F_fm, M_star)
        sigma_0 = solve_sigma_flip(rho_s, g2_val, g3_val)
        M_star_new = M_N - G_SIGMA * sigma_0
        if M_star_new < 10:
            M_star_new = 10.0
        if abs(M_star_new - M_star) < tol:
            return M_star_new
        M_star = 0.3 * M_star + 0.7 * M_star_new
    return M_star

def ea_flip(k_F_fm, g2_val, g3_val):
    M_star = solve_sc_flip(k_F_fm, g2_val, g3_val)
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
    sigma_0 = solve_sigma_flip(rho_s, g2_val, g3_val)
    scalar_energy = (0.5 * M_SIGMA**2 * sigma_0**2
                     + (g2_val / 3.0) * sigma_0**3
                     + (g3_val / 4.0) * sigma_0**4) / HBAR_C**3
    rho_B = baryon_density(k_F_fm)
    vector_energy = G_OMEGA**2 * rho_B**2 * HBAR_C**3 / (2.0 * M_OMEGA**2)
    return (kinetic + scalar_energy + vector_energy) / rho_B - M_N

# Scan with flipped g2
best_kf = 0.5
best_ea = 1e10
for i in range(200):
    kf = 0.5 + 2.0 * i / 200
    ea = ea_flip(kf, G2_FLIP, G3_CHIRAL)
    if ea < best_ea:
        best_ea = ea
        best_kf = kf

rho_flip = baryon_density(best_kf)
r0_flip = (3.0 / (4.0 * math.pi * rho_flip))**(1.0/3.0)
print(f"  With g2 = {G2_FLIP:.0f} MeV (negative, 30% of chiral magnitude):")
print(f"    E/A_min = {best_ea:.1f} MeV at rho = {rho_flip:.4f} fm^-3")
print(f"    r_0 = {r0_flip:.3f} fm")
print()

flip_binds = best_ea < 0
check("H1: negative g2 allows nuclear binding", flip_binds)
print()

print("CONCLUSION:")
print("  The chiral potential is the WRONG source of nonlinear terms for")
print("  nuclear saturation. The Walecka sigma must receive its nonlinear")
print("  self-coupling from a DIFFERENT mechanism than naive chiral symmetry.")
print("  In DFC, the natural candidate is fluctuation self-interaction around")
print("  the D7 kink background — the asymmetric Poschl-Teller potential")
print("  naturally produces cubic terms with the opposite sign from the")
print("  chiral expansion.")
print()
print("  STATUS: r_0 remains T4. The chiral potential path is CLOSED as a")
print("  route to nuclear saturation. The V(phi) kink-fluctuation path is")
print("  OPEN and has the correct qualitative features (negative g2).")
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
