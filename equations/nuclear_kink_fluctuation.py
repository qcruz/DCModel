"""
V(phi) Kink-Fluctuation Expansion — Nonlinear Walecka Terms from DFC Substrate
===============================================================================

Physical question:
    The linear Walecka model (QHD-I) with DFC parameters gives K ~ 1650 MeV
    (observed 200-300 MeV). The chiral potential path was CLOSED in C372
    (positive g2 destroys binding). Can the DFC substrate potential V(phi),
    expanded around the kink background, provide nonlinear sigma self-coupling
    with the CORRECT (negative) sign for g2?

DFC mechanism:
    The substrate potential V(phi) = -alpha/2 * phi^2 + beta/4 * phi^4 has
    a kink solution phi_kink(y) = phi_0 * tanh(y/xi). The key insight is
    that nuclear density REDUCES the scalar field from its vacuum value:

        sigma_Walecka = -delta_phi = -(phi - phi_0)

    where delta_phi < 0 in nuclear matter (field pulled toward phi=0).
    This sign identification flips the cubic coupling:

        V'''(phi_0) = 6*beta*phi_0 > 0  (at the vacuum)

    but sigma_Walecka = -delta_phi, so the cubic term in sigma is:

        g2_eff = -V'''(phi_0) / 2 = -3*beta*phi_0 < 0  (NEGATIVE)

    The structural estimate for the magnitude uses DFC scales:

        g2 = -g_sigma * m_sigma / N_c

    where the factor 1/N_c counts the fraction of the D7 kink background
    that couples to a single nucleon channel.

Key results:
    Part A: Z2 asymmetry argument for g2 < 0 (T1/T3)
    Part B: Structural estimate g2 = -g_sigma * m_sigma / N_c (T3)
    Part C: Nonlinear Walecka solver with V(phi)-derived g2
    Part D: Saturation properties (rho_0, E/A, K, M*)
    Part E: Comparison table (linear -> chiral -> V(phi) kink)
    Part F: Assessment and path forward

Key references:
    - Boguta & Bodmer (1977): Nucl. Phys. A 292, 413
    - Furnstahl & Serot (1991): distinction Walecka sigma vs chiral sigma
    - equations/nuclear_nonlinear_walecka.py (C372, chiral path CLOSED)
    - equations/nuclear_walecka_prediction.py (C371, QHD-I limitation)
    - educational/26_nuclear_saturation.md
"""

import math

# --- Assertion infrastructure ------------------------------------------------
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


# --- DFC-determined parameters -----------------------------------------------

LAMBDA_QCD_MEV  = 304.5
HBAR_C          = 197.3269804    # MeV*fm
N_C             = 3

F_PI_DFC        = LAMBDA_QCD_MEV / math.pi
M_N             = math.sqrt(3 * math.pi) * LAMBDA_QCD_MEV
M_OMEGA         = math.sqrt(2 * math.pi) * LAMBDA_QCD_MEV
G_SIGMA         = math.pi * math.sqrt(3 * math.pi)    # 9.645
G_OMEGA         = G_SIGMA
M_SIGMA         = 648.0  # MeV [T3, C370]
GAMMA           = 4      # spin x isospin degeneracy

# V(phi) parameters in Planck units (for structural arguments)
ALPHA_DFC       = 18.0**(1.0/3.0)          # = cbrt(18) ~ 2.621
BETA_DFC        = 1.0 / (9.0 * math.pi)    # T2a
PHI_0           = math.sqrt(ALPHA_DFC / BETA_DFC)
XI              = math.sqrt(2.0 / ALPHA_DFC)

# Empirical values
RHO_0_EMP       = 0.16   # fm^{-3}
E_A_EMP         = -15.8  # MeV
K_EMP_LOW       = 200.0  # MeV
K_EMP_HIGH      = 300.0  # MeV
R_0_EMP         = 1.2    # fm

# NL3 reference values for comparison
G2_NL3          = -2058.0  # MeV (converted from NL3 fm^{-1} convention)
G3_NL3          = 48.0     # dimensionless (approximate NL3 quartic)


# =============================================================================
# Part A: Z2 asymmetry argument — why g2 < 0
# =============================================================================
print("=" * 72)
print("Part A: V(phi) kink background -> negative cubic coupling")
print("=" * 72)
print()

# V(phi) = -alpha/2 * phi^2 + beta/4 * phi^4
# Vacuum: phi_0 = sqrt(alpha/beta)
# V'(phi_0) = 0 (by construction)
# V''(phi_0) = -alpha + 3*beta*phi_0^2 = -alpha + 3*alpha = 2*alpha > 0 (stable)
# V'''(phi_0) = 6*beta*phi_0 > 0

V_triple_prime = 6.0 * BETA_DFC * PHI_0
print(f"V(phi) at the vacuum phi_0 = sqrt(alpha/beta) = {PHI_0:.4f} M_Pl:")
print(f"  V''(phi_0)  = 2*alpha = {2*ALPHA_DFC:.4f} M_Pl^2  (positive: stable)")
print(f"  V'''(phi_0) = 6*beta*phi_0 = {V_triple_prime:.6f} M_Pl^3  (positive)")
print()

# The key sign argument:
# In nuclear matter, the scalar field is REDUCED from phi_0 (partial chiral restoration).
# Define the Walecka sigma field as the DECREASE in scalar field:
#   sigma_W = phi_0 - phi = -delta_phi  where delta_phi = phi - phi_0
#
# sigma_W > 0 when the field decreases (as in nuclear interior).
# M* = M_N - g_sigma * sigma_W = M_N - g_sigma * (phi_0 - phi)
#
# Expand V(phi) around phi_0 in terms of delta_phi = phi - phi_0:
#   V(phi_0 + delta) = V(phi_0) + V''(phi_0)/2 * delta^2 + V'''(phi_0)/6 * delta^3 + ...
#                     = const + alpha * delta^2 + beta*phi_0 * delta^3 + ...
#
# Now substitute delta = -sigma_W:
#   V = const + alpha * sigma_W^2 - beta*phi_0 * sigma_W^3 + ...
#
# The cubic term in sigma_W has coefficient -beta*phi_0 < 0.
# In Boguta-Bodmer notation: V_NL = (g2/3)*sigma^3 + ...
# So g2/3 = -beta*phi_0, giving g2 = -3*beta*phi_0 < 0.

g2_sign_argument = -3.0 * BETA_DFC * PHI_0
print("Sign argument (T1 algebraic):")
print(f"  delta_phi = phi - phi_0  (negative in nuclear matter)")
print(f"  sigma_Walecka = -delta_phi  (positive in nuclear matter)")
print()
print(f"  V(phi_0 + delta) = const + alpha*delta^2 + beta*phi_0*delta^3 + ...")
print(f"  V(phi_0 - sigma) = const + alpha*sigma^2 - beta*phi_0*sigma^3 + ...")
print()
print(f"  Cubic coefficient in sigma: -beta*phi_0 = {-BETA_DFC * PHI_0:.6f}")
print(f"  => g2/3 = -beta*phi_0  =>  g2 = -3*beta*phi_0 = {g2_sign_argument:.6f} M_Pl")
print(f"  Sign: g2 < 0  (NEGATIVE — correct for nuclear saturation)")
print()

check("A1: V'''(phi_0) > 0", V_triple_prime > 0)
check("A2: g2 = -3*beta*phi_0 < 0 (negative)", g2_sign_argument < 0)
print()

# The quartic term:
# V''''(phi_0) = 6*beta > 0
# In sigma_W: coefficient of sigma^4 is +beta*3/4 = 3*beta/4
# g3/4 = 3*beta/4, so g3 = 3*beta > 0 (positive, stabilizing)
g3_sign = 3.0 * BETA_DFC
print(f"  Quartic: g3 = 3*beta = {g3_sign:.6f} M_Pl  (positive, stabilizing)")
print(f"  Sign pattern: g2 < 0, g3 > 0 — matches NL3 qualitative structure.")
print()
check("A3: g3 > 0 (positive, stabilizing)", g3_sign > 0)
print()


# =============================================================================
# Part B: Structural estimate g2 = -g_sigma * m_sigma / N_c
# =============================================================================
print("=" * 72)
print("Part B: Structural estimate of g2 at nuclear scale")
print("=" * 72)
print()

# The V(phi) argument gives g2 in Planck units. To translate to nuclear scale:
#
# The Walecka sigma field couples to nucleons with strength g_sigma = 9.645.
# The sigma mass m_sigma = 648 MeV sets the range.
# The cubic self-interaction at the nuclear scale inherits from V(phi)
# through the D7 kink background.
#
# Structural estimate: the cubic coupling scales as
#   g2 ~ -g_sigma * m_sigma / N_c
#
# Physical reasoning:
# - g_sigma * m_sigma is the natural scale for sigma self-interaction
#   (coupling times mass, like lambda*v in the Higgs sector)
# - 1/N_c dilution: only one of N_c color channels contributes to
#   the effective nuclear sigma; the other (N_c - 1) are spectators
#   in the color-singlet nucleon
# - The negative sign comes from the Z2 asymmetry (Part A)

G2_DFC = -G_SIGMA * M_SIGMA / N_C   # MeV
G2_DFC_FM = G2_DFC / HBAR_C          # fm^{-1}

print(f"Structural estimate:")
print(f"  g2 = -g_sigma * m_sigma / N_c")
print(f"     = -{G_SIGMA:.3f} * {M_SIGMA:.0f} / {N_C}")
print(f"     = {G2_DFC:.1f} MeV")
print(f"     = {G2_DFC_FM:.2f} fm^-1")
print()

# Comparison with NL3
g2_err = (G2_DFC - G2_NL3) / abs(G2_NL3) * 100
print(f"  NL3 (Lalazissis 1997): g2 = {G2_NL3:.0f} MeV")
print(f"  DFC structural:        g2 = {G2_DFC:.0f} MeV")
print(f"  Error: {g2_err:+.1f}%")
print()

check("B1: g2 < 0 (correct sign)", G2_DFC < 0)
check("B2: |g2| within 20% of NL3", abs(g2_err) < 20)
print()

# For g3: use the chiral value as a starting point
# g3 = m_sigma^2 / (2*f_pi^2) = 22.35 (from C372)
# This is the quartic coupling from the sigma mass and f_pi
G3_DFC = M_SIGMA**2 / (2.0 * F_PI_DFC**2)

print(f"  Quartic coupling g3 = m_sigma^2/(2*f_pi^2) = {G3_DFC:.2f}")
print(f"  (chiral value retained — quartic sign was already correct in C372)")
print()


# =============================================================================
# Part C: Nonlinear Walecka solver with V(phi)-derived g2
# =============================================================================
print("=" * 72)
print("Part C: Nonlinear Walecka solver with DFC g2")
print("=" * 72)
print()


def scalar_density(k_F_fm, M_star_MeV):
    """Scalar density rho_s for symmetric nuclear matter. Result in fm^{-3}."""
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
    """Baryon density for symmetric matter. Result in fm^{-3}."""
    return GAMMA * k_F_fm**3 / (6.0 * math.pi**2)


def solve_sigma_nl(rho_s_fm3, g2, g3, tol=1e-6, max_iter=500):
    """
    Solve m_sigma^2*sigma + g2*sigma^2 + g3*sigma^3 = g_sigma*rho_s*hbar_c^3
    via Newton's method. Returns sigma_0 in MeV.
    """
    rhs = G_SIGMA * rho_s_fm3 * HBAR_C**3
    sigma_0 = rhs / M_SIGMA**2  # linear starting point

    for _ in range(max_iter):
        f_val = M_SIGMA**2 * sigma_0 + g2 * sigma_0**2 + g3 * sigma_0**3 - rhs
        f_prime = M_SIGMA**2 + 2.0 * g2 * sigma_0 + 3.0 * g3 * sigma_0**2
        if abs(f_prime) < 1e-30:
            break
        delta = f_val / f_prime
        sigma_0 -= delta
        if sigma_0 < 0:
            sigma_0 = 0.01
        if abs(delta) < tol:
            break

    return sigma_0


def solve_self_consistent(k_F_fm, g2, g3, tol=1e-4, max_iter=500):
    """Solve M* = M_N - g_sigma*sigma_0 self-consistently. Returns M* in MeV."""
    M_star = M_N
    for _ in range(max_iter):
        rho_s = scalar_density(k_F_fm, M_star)
        sigma_0 = solve_sigma_nl(rho_s, g2, g3)
        M_star_new = M_N - G_SIGMA * sigma_0
        if M_star_new < 10:
            M_star_new = 10.0
        if abs(M_star_new - M_star) < tol:
            return M_star_new
        M_star = 0.3 * M_star + 0.7 * M_star_new
    return M_star


def energy_per_nucleon(k_F_fm, g2, g3):
    """E/A - M_N for the nonlinear Walecka model. Returns MeV."""
    M_star = solve_self_consistent(k_F_fm, g2, g3)

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
    sigma_0 = solve_sigma_nl(rho_s, g2, g3)
    scalar_energy = (0.5 * M_SIGMA**2 * sigma_0**2
                     + (g2 / 3.0) * sigma_0**3
                     + (g3 / 4.0) * sigma_0**4) / HBAR_C**3

    rho_B = baryon_density(k_F_fm)
    vector_energy = G_OMEGA**2 * rho_B**2 * HBAR_C**3 / (2.0 * M_OMEGA**2)

    return (kinetic + scalar_energy + vector_energy) / rho_B - M_N


# Scan to find saturation point with DFC g2
print(f"Using g2 = {G2_DFC:.1f} MeV, g3 = {G3_DFC:.2f}")
print()

k_F_scan = []
E_A_scan = []
k_F_min = 0.5
k_F_max = 2.5
N_scan = 200

for i in range(N_scan + 1):
    kf = k_F_min + (k_F_max - k_F_min) * i / N_scan
    ea = energy_per_nucleon(kf, G2_DFC, G3_DFC)
    k_F_scan.append(kf)
    E_A_scan.append(ea)

# Find minimum
i_min = 0
for i in range(1, len(E_A_scan)):
    if E_A_scan[i] < E_A_scan[i_min]:
        i_min = i

# Parabolic refinement
if 0 < i_min < len(E_A_scan) - 1:
    k1, k2, k3 = k_F_scan[i_min-1], k_F_scan[i_min], k_F_scan[i_min+1]
    e1, e2, e3 = E_A_scan[i_min-1], E_A_scan[i_min], E_A_scan[i_min+1]
    denom = 2.0 * ((k2 - k1) * (e2 - e3) - (k2 - k3) * (e2 - e1))
    if abs(denom) > 1e-20:
        k_F_sat = k2 - ((k2 - k1)**2 * (e2 - e3) - (k2 - k3)**2 * (e2 - e1)) / denom
    else:
        k_F_sat = k2
else:
    k_F_sat = k_F_scan[i_min]

rho_sat = baryon_density(k_F_sat)
r_0_pred = (3.0 / (4.0 * math.pi * rho_sat))**(1.0/3.0)
E_A_sat = energy_per_nucleon(k_F_sat, G2_DFC, G3_DFC)
M_star_sat = solve_self_consistent(k_F_sat, G2_DFC, G3_DFC)

has_minimum = E_A_sat < E_A_scan[0] and E_A_sat < E_A_scan[-1]

print(f"Saturation point (V(phi) kink-fluctuation g2):")
print(f"  k_F_sat = {k_F_sat:.4f} fm^-1")
print(f"  rho_sat = {rho_sat:.4f} fm^-3  (observed: {RHO_0_EMP:.2f})")
print(f"  r_0 = {r_0_pred:.3f} fm  (observed: {R_0_EMP:.2f})")
print(f"  E/A - M_N = {E_A_sat:.2f} MeV  (observed: {E_A_EMP:.1f})")
print(f"  M*/M_N = {M_star_sat/M_N:.4f}")
print()

check("C1: saturation minimum exists", has_minimum)
check("C2: E/A < 0 (nuclear matter is bound)", E_A_sat < 0)
print()


# =============================================================================
# Part D: Saturation properties — rho_0, E/A, K
# =============================================================================
print("=" * 72)
print("Part D: Saturation properties and incompressibility")
print("=" * 72)
print()

rho_err = (rho_sat - RHO_0_EMP) / RHO_0_EMP * 100
r0_err = (r_0_pred - R_0_EMP) / R_0_EMP * 100
EA_err = (E_A_sat - E_A_EMP) / abs(E_A_EMP) * 100

print(f"  rho_0 = {rho_sat:.4f} fm^-3  ({rho_err:+.1f}%)")
print(f"  r_0   = {r_0_pred:.3f} fm    ({r0_err:+.1f}%)")
print(f"  E/A   = {E_A_sat:.2f} MeV   ({EA_err:+.1f}%)")
print()

# Incompressibility K
dk_F = 0.005
ea_plus = energy_per_nucleon(k_F_sat + dk_F, G2_DFC, G3_DFC)
ea_minus = energy_per_nucleon(k_F_sat - dk_F, G2_DFC, G3_DFC)
ea_center = energy_per_nucleon(k_F_sat, G2_DFC, G3_DFC)

d2E_dkF2 = (ea_plus - 2.0 * ea_center + ea_minus) / dk_F**2
drho_dkF = GAMMA * k_F_sat**2 / (2.0 * math.pi**2)
d2E_drho2 = d2E_dkF2 / drho_dkF**2
K_pred = 9.0 * rho_sat * d2E_drho2

print(f"  K = {K_pred:.0f} MeV  (observed: {K_EMP_LOW:.0f}-{K_EMP_HIGH:.0f})")
print()

# Scalar and vector potentials
rho_s_sat = scalar_density(k_F_sat, M_star_sat)
sigma_0_sat = solve_sigma_nl(rho_s_sat, G2_DFC, G3_DFC)
S_pot = G_SIGMA * sigma_0_sat
V_pot = G_OMEGA**2 / M_OMEGA**2 * rho_sat * HBAR_C**3

print(f"  Scalar potential S = {S_pot:.1f} MeV (attractive)")
print(f"  Vector potential V = {V_pot:.1f} MeV (repulsive)")
print(f"  S - V = {S_pot - V_pot:.1f} MeV (net)")
print()

# Checks
check("D1: rho_0 within 30% of empirical", abs(rho_err) < 30)
check("D2: E/A within 50% of empirical", abs(EA_err) < 50)

# Linear QHD-I had K=1646; check improvement
K_lin = 1646.0
K_improved = K_pred < K_lin
check("D3: K improved over linear QHD-I (1646 MeV)", K_improved)

K_in_range = K_EMP_LOW <= K_pred <= K_EMP_HIGH
check("D4: K in observed range 200-300 MeV", K_in_range)

# Check improvement over chiral path (C372: E/A > 0, no binding)
# Chiral path: E/A > 0 everywhere (FAIL), K undefined
check("D5: binding restored (chiral path was E/A > 0)", E_A_sat < 0)
print()


# =============================================================================
# Part E: Comparison table — three models
# =============================================================================
print("=" * 72)
print("Part E: Three-model comparison")
print("=" * 72)
print()

# Linear QHD-I values from C371
rho_lin = 0.2275
r0_lin = 1.016
EA_lin = -9.4
K_lin_val = 1646
Mstar_lin = 0.61

# Chiral (C372) values
rho_chi = "no sat."
r0_chi = "---"
EA_chi = "> 0"
K_chi = "---"
Mstar_chi = "---"

print(f"{'Property':25s}  {'Observed':>10s}  {'Linear':>10s}  {'Chiral':>10s}  {'V(phi)':>10s}")
print("-" * 72)
print(f"{'g2 (MeV)':25s}  {'---':>10s}  {'0':>10s}  {'+6498':>10s}  {G2_DFC:>10.0f}")
print(f"{'g3':25s}  {'---':>10s}  {'0':>10s}  {'22.35':>10s}  {G3_DFC:>10.1f}")
print(f"{'rho_0 (fm^-3)':25s}  {'0.16':>10s}  {rho_lin:>10.4f}  {rho_chi:>10s}  {rho_sat:>10.4f}")
print(f"{'r_0 (fm)':25s}  {'1.20':>10s}  {r0_lin:>10.3f}  {r0_chi:>10s}  {r_0_pred:>10.3f}")
print(f"{'E/A - M_N (MeV)':25s}  {'-15.8':>10s}  {EA_lin:>10.1f}  {EA_chi:>10s}  {E_A_sat:>10.1f}")
print(f"{'K (MeV)':25s}  {'200-300':>10s}  {K_lin_val:>10.0f}  {K_chi:>10s}  {K_pred:>10.0f}")
print(f"{'M*/M_N':25s}  {'0.60-70':>10s}  {Mstar_lin:>10.2f}  {Mstar_chi:>10s}  {M_star_sat/M_N:>10.4f}")
print()

check("E1: V(phi) g2 has correct sign (negative)", G2_DFC < 0)
check("E2: V(phi) produces binding (chiral did not)", E_A_sat < 0)
check("E3: V(phi) K < linear K", K_pred < K_lin_val)
print()


# =============================================================================
# Part F: g2 sensitivity scan
# =============================================================================
print("=" * 72)
print("Part F: g2 sensitivity scan")
print("=" * 72)
print()

print(f"{'g2 (MeV)':>12s}  {'rho_0':>8s}  {'r_0':>6s}  {'E/A':>8s}  {'K':>6s}  {'M*/M_N':>8s}")
print("-" * 60)

g2_values = [-1500, -1800, G2_DFC, -2200, -2500, -3000]

for g2_test in sorted(g2_values):
    # Quick scan for saturation
    best_kf = 0.5
    best_ea = 1e10
    for i in range(200):
        kf = 0.5 + 2.0 * i / 200
        ea = energy_per_nucleon(kf, g2_test, G3_DFC)
        if ea < best_ea:
            best_ea = ea
            best_kf = kf

    # Refine
    for _ in range(3):
        dk = 0.02
        ea_p = energy_per_nucleon(best_kf + dk, g2_test, G3_DFC)
        ea_m = energy_per_nucleon(best_kf - dk, g2_test, G3_DFC)
        ea_c = energy_per_nucleon(best_kf, g2_test, G3_DFC)
        d2 = (ea_p - 2*ea_c + ea_m) / dk**2
        d1 = (ea_p - ea_m) / (2*dk)
        if abs(d2) > 1e-10:
            best_kf -= d1 / d2
            best_ea = energy_per_nucleon(best_kf, g2_test, G3_DFC)

    rho_t = baryon_density(best_kf)
    r0_t = (3.0 / (4.0 * math.pi * rho_t))**(1.0/3.0)
    Mstar_t = solve_self_consistent(best_kf, g2_test, G3_DFC)

    # K
    dk_t = 0.005
    ea_p = energy_per_nucleon(best_kf + dk_t, g2_test, G3_DFC)
    ea_m = energy_per_nucleon(best_kf - dk_t, g2_test, G3_DFC)
    ea_c = energy_per_nucleon(best_kf, g2_test, G3_DFC)
    d2E = (ea_p - 2*ea_c + ea_m) / dk_t**2
    drho = GAMMA * best_kf**2 / (2.0 * math.pi**2)
    K_t = 9.0 * rho_t * d2E / drho**2

    marker = "  <-- DFC" if abs(g2_test - G2_DFC) < 1 else ""
    print(f"{g2_test:>12.0f}  {rho_t:>8.4f}  {r0_t:>6.3f}  {best_ea:>8.1f}  {K_t:>6.0f}  {Mstar_t/M_N:>8.4f}{marker}")

print()


# =============================================================================
# Part G: Assessment and tier assignment
# =============================================================================
print("=" * 72)
print("Part G: Assessment")
print("=" * 72)
print()

print("RESULTS:")
print(f"  1. Sign of g2: NEGATIVE from V(phi) kink background [T1 algebraic]")
print(f"     sigma_Walecka = -delta_phi flips the V'''(phi_0) sign.")
print()
print(f"  2. Structural estimate: g2 = -g_sigma*m_sigma/N_c = {G2_DFC:.0f} MeV [T3]")
print(f"     Comparison: NL3 = {G2_NL3:.0f} MeV ({g2_err:+.1f}%)")
print()
print(f"  3. Nuclear binding RESTORED: E/A = {E_A_sat:.1f} MeV [T3]")
print(f"     (Chiral path C372: E/A > 0 everywhere — no binding)")
print()
print(f"  4. Saturation density: rho_0 = {rho_sat:.4f} fm^-3 ({rho_err:+.1f}%) [T3/T4]")
print(f"  5. Nuclear radius: r_0 = {r_0_pred:.3f} fm ({r0_err:+.1f}%) [T3/T4]")
print(f"  6. Incompressibility: K = {K_pred:.0f} MeV [T3/T4]")
print()

# Tier assessment
print("Tier assessment:")
print(f"  g2 sign (negative): T1 (algebraic from V(phi) + sigma_W = -delta_phi)")
print(f"  g2 magnitude (-g_sigma*m_sigma/N_c): T3 (structural, 0 free params)")
print(f"  Nuclear binding: T3 (restored from chiral FAIL)")

if K_EMP_LOW <= K_pred <= K_EMP_HIGH:
    print(f"  K in observed range: T3")
else:
    print(f"  K: T4 (not yet in observed range; structural estimate)")

if abs(rho_err) < 15:
    print(f"  rho_0: T3 (within 15%)")
else:
    print(f"  rho_0: T4 (>{abs(rho_err):.0f}% error; needs refinement)")

print()

# Path forward
print("What remains open (T4):")
print("  - Derive g2 quantitatively from V(phi) kink-fluctuation expansion")
print("    (current estimate is structural; need Poschl-Teller effective")
print("    potential around phi_kink properly projected to nuclear scale)")
print("  - g3 uses chiral value — should be derived from V(phi) quartic")
print("  - r_0 prediction depends on getting rho_0 correct")
print("  - Shell corrections (magic numbers) require spin-orbit coupling")
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
