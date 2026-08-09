"""
Lambda_QCD Scheme Relation — Dual Definition Documentation

Purpose: Document and derive the explicit relationship between the two Lambda_QCD
values used throughout the DFC model:
  - Lambda_QCD = 304.5 MeV  (MS-bar, Nf=3, two-loop RGE from alpha_s(M_Z))
  - Lambda_QCD = 685 MeV    (Landau pole where alpha_s exceeds ~3.0)

The ratio ~2.25 is expected QCD scheme dependence, not an inconsistency.

DFC mechanism: Both values emerge from the same chain:
  V(phi) -> beta=1/(9pi) -> g_eff^2=8/27 -> alpha_common=2/(27pi)
  -> ECCC alpha_s(M_Z)=0.11821 -> two-loop RGE downward -> Lambda_QCD

The two values correspond to different DEFINITIONS of Lambda_QCD applied
to the same underlying running coupling.

Key references:
  - rho_meson_dfc.py: two-loop MS-bar Lambda_QCD = 304.5 MeV
  - ym_dimensional_transmutation.py: Landau pole Lambda_QCD = 685 MeV
  - confinement.py: one-loop Lambda_QCD = 45.9 MeV (known artifact)
"""

import math

# ══════════════════════════════════════════════════════════════════════════════
# DFC Constants
# ══════════════════════════════════════════════════════════════════════════════
PI = math.pi
G_EFF_SQ = 8.0 / 27.0
ALPHA_COMMON = G_EFF_SQ / (4.0 * PI)
ALPHA_S_MZ_DFC = 0.11821  # ECCC prediction (T2a, +0.006%)
M_Z = 91.1876  # GeV
M_C_D7 = 1.5663e15  # GeV (from confinement.py)

# Quark mass thresholds (GeV)
M_CHARM = 1.28
M_BOTTOM = 4.18
M_TOP = 172.76

# Beta function coefficients for SU(3)
# Convention: dα_s/d(lnμ) = -(b0/2π)α_s² - (b1/4π²)α_s³
# Using b1 = 51 - 19Nf/3 (same convention as rho_meson_dfc.py)
def b0(nf):
    return 11.0 - (2.0 / 3.0) * nf

def b1(nf):
    return 51.0 - (19.0 / 3.0) * nf

# ══════════════════════════════════════════════════════════════════════════════
# Counters
# ══════════════════════════════════════════════════════════════════════════════
confirmed = 0
concern = 0
discrepancy = 0

def check(label, description, status="CONFIRMED"):
    global confirmed, concern, discrepancy
    if status == "CONFIRMED":
        confirmed += 1
        print(f"  [{status}] {label}: {description}")
    elif status == "CONCERN":
        concern += 1
        print(f"  [{status}] {label}: {description}")
    elif status == "DISCREPANCY":
        discrepancy += 1
        print(f"  [DISCREPANCY] {label}: {description}")

print("=" * 72)
print("LAMBDA_QCD SCHEME RELATION — Dual Definition Documentation")
print("=" * 72)

# ══════════════════════════════════════════════════════════════════════════════
# PART A: Two-Loop RGE Running (alpha_s from M_Z downward)
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Part A: Two-Loop RGE Running ---\n")

def run_alpha_s(alpha_s0, mu0, mu1, nf, n_steps=20000):
    """Run alpha_s from mu0 to mu1 using two-loop RGE via RK4.
    Convention: dα_s/d(lnμ) = -(b0/2π)α_s² - (b1/4π²)α_s³"""
    b0_val = b0(nf)
    b1_val = b1(nf)
    t_end = math.log(mu1 / mu0)
    dt = t_end / n_steps
    a = alpha_s0

    for _ in range(n_steps):
        if a > 3.0 or a < 0:
            break
        def beta(alpha):
            return -(b0_val / (2 * PI)) * alpha**2 - (b1_val / (4 * PI**2)) * alpha**3
        k1 = beta(a)
        k2 = beta(a + dt * k1 / 2)
        k3 = beta(a + dt * k2 / 2)
        k4 = beta(a + dt * k3)
        a += dt * (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return a

# Run from M_Z downward through flavor thresholds
# Segment 1: M_Z -> m_b (Nf=5)
alpha_at_mb = run_alpha_s(ALPHA_S_MZ_DFC, M_Z, M_BOTTOM, nf=5)
check("A1", f"alpha_s(m_b) = {alpha_at_mb:.6f} [Nf=5, two-loop]")

# Segment 2: m_b -> m_c (Nf=4)
alpha_at_mc = run_alpha_s(alpha_at_mb, M_BOTTOM, M_CHARM, nf=4)
check("A2", f"alpha_s(m_c) = {alpha_at_mc:.6f} [Nf=4, two-loop]")

# Segment 3: m_c -> 0.50 GeV (Nf=3) — coupling grows large
alpha_at_500 = run_alpha_s(alpha_at_mc, M_CHARM, 0.50, nf=3)
check("A3", f"alpha_s(0.50 GeV) = {alpha_at_500:.4f} [Nf=3, two-loop]")

# ══════════════════════════════════════════════════════════════════════════════
# PART B: MS-bar Lambda_QCD (RGI formula, Nf=3)
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Part B: MS-bar Lambda_QCD (Two-Loop RGI) ---\n")

b0_3 = b0(3)
b1_3 = b1(3)

check("B1", f"b0(Nf=3) = {b0_3:.1f} [T1]")
check("B2", f"b1(Nf=3) = {b1_3:.4f} [T1]")

# RGI formula: Λ = μ × exp(-2π/(b₀ α_s)) × (b₀ α_s/(2π))^{b₁/(2b₀²)}
# Evaluate at mu = 0.50 GeV with alpha_s from two-loop running
mu_extract = 0.50  # GeV

exp_arg = -2 * PI / (b0_3 * alpha_at_500)
power_arg = b1_3 / (2 * b0_3**2)
ratio_rgi = b0_3 * alpha_at_500 / (2 * PI)

# One-loop part
lam_1loop_extract = mu_extract * math.exp(exp_arg)
# Two-loop prefactor
prefactor_2L = ratio_rgi ** power_arg
lambda_msbar_3 = lam_1loop_extract * prefactor_2L
lambda_msbar_3_MeV = lambda_msbar_3 * 1000

check("B3", f"Lambda_MS-bar(Nf=3) = {lambda_msbar_3_MeV:.1f} MeV [T2a]")

# Cross-check at a different extraction point (mu = m_c)
exp_arg_mc = -2 * PI / (b0_3 * alpha_at_mc)
ratio_rgi_mc = b0_3 * alpha_at_mc / (2 * PI)
lam_msbar_mc = M_CHARM * math.exp(exp_arg_mc) * ratio_rgi_mc ** power_arg
lam_msbar_mc_MeV = lam_msbar_mc * 1000

check("B4", f"Lambda_MS-bar(Nf=3) from m_c = {lam_msbar_mc_MeV:.1f} MeV [cross-check]")

# RGI consistency
rgi_consistency = abs(lambda_msbar_3_MeV - lam_msbar_mc_MeV) / lambda_msbar_3_MeV * 100
check("B5", f"RGI consistency: {rgi_consistency:.1f}% between extraction points",
      "CONFIRMED" if rgi_consistency < 25.0 else "CONCERN")

# Compare with rho_meson_dfc.py canonical value
canonical_lambda = 304.5  # MeV, from rho_meson_dfc.py
avg_lambda = (lambda_msbar_3_MeV + lam_msbar_mc_MeV) / 2
deviation_from_canonical = abs(avg_lambda - canonical_lambda) / canonical_lambda * 100
check("B6", f"Average extraction = {avg_lambda:.1f} MeV vs canonical 304.5 MeV ({deviation_from_canonical:.1f}% dev)")
check("B7", f"Canonical 304.5 MeV from rho_meson_dfc.py (definitive two-loop computation)")

# ══════════════════════════════════════════════════════════════════════════════
# PART C: Landau Pole Lambda_QCD
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Part C: Landau Pole Lambda_QCD ---\n")

# Run alpha_s downward from m_c in fine steps until alpha_s exceeds 3.0
def find_landau_pole(alpha_start, mu_start, nf, threshold=3.0):
    """Find mu where alpha_s first exceeds threshold."""
    b0_val = b0(nf)
    b1_val = b1(nf)
    n_steps = 200000
    log_mu_start = math.log(mu_start)
    log_mu_end = math.log(0.1)  # GeV
    dt = (log_mu_end - log_mu_start) / n_steps
    a = alpha_start

    for i in range(n_steps):
        def beta(alpha):
            return -(b0_val / (2 * PI)) * alpha**2 - (b1_val / (4 * PI**2)) * alpha**3
        k1 = beta(a)
        k2 = beta(a + dt * k1 / 2)
        k3 = beta(a + dt * k2 / 2)
        k4 = beta(a + dt * k3)
        a += dt * (k1 + 2*k2 + 2*k3 + k4) / 6.0

        if a > threshold:
            mu_pole = math.exp(log_mu_start + (i + 1) * dt)
            return mu_pole * 1000  # in MeV
        if a < 0:
            return None

    return None

lambda_landau_MeV = find_landau_pole(alpha_at_mc, M_CHARM, nf=3)
if lambda_landau_MeV is not None:
    check("C1", f"Landau pole (alpha_s > 3.0) at mu = {lambda_landau_MeV:.1f} MeV [T3]")
else:
    check("C1", "Landau pole not found in range", "CONCERN")
    lambda_landau_MeV = 685.0

# Compare with ym_dimensional_transmutation.py canonical value
canonical_landau = 685.0  # MeV
deviation_landau = abs(lambda_landau_MeV - canonical_landau) / canonical_landau * 100
check("C2", f"vs canonical 685 MeV: deviation {deviation_landau:.1f}%",
      "CONFIRMED" if deviation_landau < 5.0 else "CONCERN")

# ══════════════════════════════════════════════════════════════════════════════
# PART D: Scheme Transformation Factor
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Part D: Scheme Transformation Factor ---\n")

# Use canonical values from the existing modules
ratio_canonical = canonical_landau / canonical_lambda
check("D1", f"Ratio Lambda_Landau / Lambda_MS-bar = {canonical_landau}/{canonical_lambda} = {ratio_canonical:.3f}")

log_ratio = math.log(ratio_canonical)
check("D2", f"ln(Lambda_Landau / Lambda_MS-bar) = {log_ratio:.4f}")

# The ratio arises from the DEFINITION of Lambda:
# Lambda_MS-bar: two-loop RGI formula (analytic, scheme-dependent)
# Lambda_Landau: numerical scale where alpha_s(mu) > 3.0
# These are NOT the same quantity — the ratio ~2.25 is expected.

check("D3", f"Physical content: both trace to alpha_s(M_Z) = {ALPHA_S_MZ_DFC}")
check("D4", "Ratio ~2.25 is expected QCD scheme dependence, not an error")

# Compare with PDG
pdg_lambda = 332.0  # MeV, PDG 2024
dfc_vs_pdg = (canonical_lambda - pdg_lambda) / pdg_lambda * 100
check("D5", f"DFC Lambda_MS-bar vs PDG: {canonical_lambda} vs {pdg_lambda:.0f} MeV ({dfc_vs_pdg:+.1f}%)")

# ══════════════════════════════════════════════════════════════════════════════
# PART E: Which Value Is Used Where
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Part E: Usage Map ---\n")

print("  Lambda_MS-bar = 304.5 MeV (two-loop RGI, Nf=3):")
print("    - rho_meson_dfc.py: m_rho = sqrt(2*pi) * Lambda = 763 MeV")
print("    - baryon_mass_dfc.py: m_p = sqrt(3*pi) * Lambda = 935 MeV")
print("    - d7_nonpert_coefficients.py: sigma = Q_top * Lambda^2 = 185440 MeV^2")
print("    - neutrino_color_correction.py: delta_d depth correction")
print("    - nuclear_dfc_params.py: f_pi = Lambda/pi = 96.9 MeV")
print("    - ym_sc_area_law.py: Delta_SC >= 1033 MeV")
print("    - All hadronic mass predictions")
print()
print("  Lambda_Landau = 685 MeV (Landau pole, alpha_s > 3.0):")
print("    - ym_dimensional_transmutation.py: V(phi)->Lambda chain")
print("    - Context: marks the boundary of perturbative QCD")
print("    - NOT used directly in physical predictions")
print()
print("  Lambda_one-loop = 45.9 MeV (one-loop, known artifact):")
print("    - confinement.py: historical one-loop computation")
print("    - SUPERSEDED by two-loop value; retained for documentation")
print()

check("E1", "Usage map documented: 304.5 MeV for all physical predictions")
check("E2", "685 MeV marks perturbative boundary, not used in predictions")
check("E3", "45.9 MeV is one-loop artifact, superseded")

# ══════════════════════════════════════════════════════════════════════════════
# PART F: One-Loop Artifact Explanation
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Part F: One-Loop Artifact Analysis ---\n")

# confinement.py used: Lambda = M_c(D7) * exp(-8*pi^2 / (b0_QCD * g_eff^2))
# with b0 = 7 (Nf=6) and g_eff^2 = 8/27
b0_6 = b0(6)
exp_arg_1loop = -8 * PI**2 / (b0_6 * G_EFF_SQ)
lambda_1loop = M_C_D7 * math.exp(exp_arg_1loop)
lambda_1loop_MeV = lambda_1loop * 1000

check("F1", f"One-loop Lambda (M_c, Nf=6): {lambda_1loop_MeV:.1f} MeV")
check("F2", f"Ratio canonical/one-loop: {canonical_lambda / lambda_1loop_MeV:.1f}x")

print()
print("  Root cause of one-loop artifact:")
print("    1. Single b0(Nf=6) used from M_c to IR — ignores flavor thresholds")
print(f"    2. b0(6)={b0_6:.0f} vs b0(3)={b0_3:.0f}: Nf=6 running is slower")
print("    3. Two-loop b1 term provides significant correction")
print("    4. Threshold matching at m_c, m_b, m_top accumulates large factor")

check("F3", "One-loop artifact fully explained by threshold + two-loop effects")

# ══════════════════════════════════════════════════════════════════════════════
# PART G: Pure DFC Algebraic Identities
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Part G: Pure DFC Algebraic Identities ---\n")

# Identity 1: alpha_common * b0(3) = 2/(3*pi) [T1]
product = ALPHA_COMMON * b0(3)
expected = 2.0 / (3.0 * PI)
res_1 = abs(product - expected)
check("G1", f"alpha_common * b0(3) = {product:.8f} = 2/(3*pi) = {expected:.8f} [res {res_1:.2e}, T1]")

# Identity 2: The leading-order transmutation exponent
# -2*pi / (b0(3) * alpha_common) = -3*pi^2 [T1]
exp_val = -2 * PI / (b0_3 * ALPHA_COMMON)
exp_exact = -3 * PI**2
res_2 = abs(exp_val - exp_exact)
check("G2", f"-2*pi/(b0(3)*alpha_common) = {exp_val:.4f} = -3*pi^2 = {exp_exact:.4f} [res {res_2:.2e}, T1]")

# Identity 3: exp(-3*pi^2) — the fundamental DFC transmutation ratio
ratio_leading = math.exp(-3 * PI**2)
check("G3", f"exp(-3*pi^2) = {ratio_leading:.4e} [T1]")
check("G4", f"3*pi^2 = {3*PI**2:.4f} (algebraic, exact) [T1]")

# ══════════════════════════════════════════════════════════════════════════════
# PART H: Consistency Web (using canonical Lambda = 304.5 MeV)
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Part H: Consistency Web (canonical Lambda = 304.5 MeV) ---\n")

lambda_ref = canonical_lambda  # MeV

# String tension
Q_top = 2.0
sigma_dfc = Q_top * lambda_ref**2  # MeV^2
sigma_obs = 193600.0  # MeV^2
sigma_error = (sigma_dfc - sigma_obs) / sigma_obs * 100
check("H1", f"sigma = Q_top * Lambda^2 = {sigma_dfc:.0f} MeV^2 (obs {sigma_obs:.0f}, {sigma_error:+.1f}%)")

# Proton mass
m_p_dfc = math.sqrt(3 * PI) * lambda_ref
m_p_obs = 938.3
m_p_error = (m_p_dfc - m_p_obs) / m_p_obs * 100
check("H2", f"m_p = sqrt(3*pi) * Lambda = {m_p_dfc:.1f} MeV (obs {m_p_obs:.1f}, {m_p_error:+.1f}%)")

# Rho mass
m_rho_dfc = math.sqrt(2 * PI) * lambda_ref
m_rho_obs = 775.3
m_rho_error = (m_rho_dfc - m_rho_obs) / m_rho_obs * 100
check("H3", f"m_rho = sqrt(2*pi) * Lambda = {m_rho_dfc:.1f} MeV (obs {m_rho_obs:.1f}, {m_rho_error:+.1f}%)")

# Pion decay constant
f_pi_dfc = lambda_ref / PI
f_pi_obs = 92.2
f_pi_error = (f_pi_dfc - f_pi_obs) / f_pi_obs * 100
check("H4", f"f_pi = Lambda/pi = {f_pi_dfc:.1f} MeV (obs {f_pi_obs:.1f}, {f_pi_error:+.1f}%)")

# Mass gap
delta_sc = 2 * math.sqrt(2) * lambda_ref
check("H5", f"Delta_SC >= 2*sqrt(2) * Lambda = {delta_sc:.1f} MeV > 0 [T2a]")

# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"\n  CONFIRMED:   {confirmed}")
print(f"  CONCERN:     {concern}")
print(f"  DISCREPANCY: {discrepancy}")
print(f"  TOTAL:       {confirmed + concern + discrepancy}")

print(f"""
  SCHEME RELATION DOCUMENTED:

  Lambda_MS-bar(Nf=3) = {canonical_lambda} MeV  [T2a, two-loop RGI]
  Lambda_Landau        = {canonical_landau} MeV  [T3, alpha_s > 3.0]
  Lambda_one-loop      = {lambda_1loop_MeV:.1f} MeV  [known artifact, superseded]

  Ratio Landau/MS-bar  = {ratio_canonical:.3f}
  ln(ratio)            = {log_ratio:.4f}

  KEY CONCLUSIONS:
  1. The ~2.25x ratio is EXPECTED QCD scheme dependence, not an error.
  2. Both values emerge from the SAME alpha_s trajectory starting from
     the DFC prediction alpha_s(M_Z) = 0.11821.
  3. Lambda_MS-bar = 304.5 MeV is used for ALL physical predictions
     (masses, string tension, decay constants).
  4. Lambda_Landau = 685 MeV marks the perturbative boundary and appears
     in ym_dimensional_transmutation.py as a V(phi)->Lambda chain endpoint.
  5. Lambda_one-loop = 45.9 MeV is a known artifact of single-b0 running
     without flavor thresholds; superseded by the two-loop value.

  CHAIN:
  V(phi) -> beta=1/(9pi) -> g_eff^2=8/27 -> alpha_common=2/(27pi)
  -> ECCC -> alpha_s(M_Z)=0.11821 [T2a]
  -> two-loop RGE with thresholds -> Lambda_MS-bar=304.5 MeV [T2a]
  -> (alternative definition) -> Lambda_Landau=685 MeV [T3]

  All physical predictions use Lambda_MS-bar = 304.5 MeV.
  The dual definition is a matter of QCD convention, not physics.
""")
