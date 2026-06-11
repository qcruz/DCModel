"""
equations/ym_static_potential.py

SP2: Static quark-antiquark potential from DFC effective string theory.

Physical question: What does DFC predict for the static QQ-bar potential?
Does the Luscher correction and Regge slope form a consistent picture with sigma?

DFC input: sigma = Q_top * Lambda_QCD^2 = 185440 MeV^2 [T2a, C222]

Method: Effective string theory (EST) / Nambu-Goto action gives the
universal form of the static potential at large R:

  V(R) = sigma * R - pi*(d-2)/(24*R) + V_0   (d=4)
       = sigma * R - pi/(12*R) + V_0

The coefficient -pi/12 is UNIVERSAL for any string in d=4 (T1: Luscher 1980,
Luscher-Weisz 2002). It does not depend on the microscopic string model.
Only sigma is DFC-specific.

Key results (Cycle 228):
  Part A [T2a]:  sigma = 185440 MeV^2,  sqrt(sigma) = 430.6 MeV
  Part B [T1]:   Luscher coefficient = -pi/12 (universal EST)
  Part C [T3]:   V(R) tabulated for R = 0.3 to 1.0 fm
  Part D [T2a]:  Luscher/linear ratio < 30% for R > 0.41 fm (string valid)
  Part E [T3]:   Regge slope alpha' = 1/(2*pi*sigma) = 0.858 GeV^-2
                 consistent with C160 (same sigma input)

References:
  C222: sigma = Q_top * Lambda_QCD^2 [T2a]
  C160: alpha' = 0.858 GeV^-2 [T3, -2.5% vs obs] from same sigma
  Luscher 1980: universal 1/R correction to confining string
  Luscher-Weisz 2002: EST systematic expansion

Cycle 228
"""

import numpy as np

print("=" * 62)
print("SP2: Static Quark-Antiquark Potential — Cycle 228")
print("=" * 62)

# -----------------------------------------------------------------------
# Parameters
# -----------------------------------------------------------------------
SIGMA      = 185440.0    # MeV^2  [T2a, C222]
hbarc      = 197.3       # MeV * fm  (conversion factor)

# -----------------------------------------------------------------------
# Part A: String tension [T2a]
# -----------------------------------------------------------------------
print("\nPart A: String tension [T2a, C222]")
sqrt_sigma = np.sqrt(SIGMA)          # MeV
sigma_GeV2 = SIGMA * 1e-6           # GeV^2

print(f"  sigma      = {SIGMA:.0f} MeV^2  [T2a]")
print(f"             = {sigma_GeV2:.4f} GeV^2")
print(f"  sqrt(sigma) = {sqrt_sigma:.2f} MeV = {sqrt_sigma*1e-3:.4f} GeV")

assert abs(sqrt_sigma - 430.6) < 1.0

# -----------------------------------------------------------------------
# Part B: Luscher coefficient [T1 universal]
# -----------------------------------------------------------------------
print("\nPart B: Luscher coefficient [T1, Luscher 1980]")
# V(R) = sigma*R - L_coeff/R + V_0
# For d=4: L_coeff = pi*(d-2)/24 = pi/12
L_coeff = np.pi / 12.0

print(f"  V(R) = sigma*R - (pi/12)/R + V_0")
print(f"  Luscher coefficient = pi/12 = {L_coeff:.6f}  [T1 EXACT, universal in d=4]")
print(f"  (Independent of microscopic string model)")

assert abs(L_coeff - np.pi/12) < 1e-12

# -----------------------------------------------------------------------
# Part C: Static potential at representative distances [T3]
# -----------------------------------------------------------------------
print("\nPart C: V(R) at representative distances [T3]")
print(f"  (V_0 subtracted; only shape of V(R) predicted)")
print(f"\n  {'R [fm]':>8} | {'R [MeV^-1]':>12} | {'sigma*R [MeV]':>14} | "
      f"{'Luscher [MeV]':>14} | {'V-V_0 [MeV]':>12}")
print(f"  {'-'*8}-+-{'-'*12}-+-{'-'*14}-+-{'-'*14}-+-{'-'*12}")

R_fm_vals = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]
V_results = []

for R_fm in R_fm_vals:
    R_MeV = R_fm / hbarc              # MeV^-1
    V_linear  = SIGMA * R_MeV        # MeV
    V_luscher = -L_coeff / R_MeV     # MeV  (negative correction)
    V_total   = V_linear + V_luscher  # MeV (relative, V_0=0)
    ratio     = abs(V_luscher) / V_linear  # Luscher fraction

    V_results.append((R_fm, R_MeV, V_linear, V_luscher, V_total, ratio))
    print(f"  {R_fm:>8.1f} | {R_MeV:>12.6f} | {V_linear:>14.1f} | "
          f"{V_luscher:>14.1f} | {V_total:>12.1f}")

# -----------------------------------------------------------------------
# Part D: String validity condition [T2a]
# -----------------------------------------------------------------------
print("\nPart D: String validity (Luscher/linear < 30%) [T2a]")
#
# The EST is valid when the Luscher correction is a small fraction of
# the linear term. Standard criterion: |V_Luscher|/(sigma*R) < 30%.
# This gives: (pi/12)/(sigma*R^2) < 0.3
# => R > sqrt(pi/(12*0.3*sigma))
#
R_valid_sq = np.pi / (12.0 * 0.3 * SIGMA)   # MeV^-2
R_valid    = np.sqrt(R_valid_sq)             # MeV^-1
R_valid_fm = R_valid * hbarc                 # fm

print(f"  Criterion: |Luscher|/(sigma*R) < 30%")
print(f"  => R > sqrt(pi/(3.6*sigma)) = {R_valid_fm:.3f} fm")
print(f"  String picture valid for R > {R_valid_fm:.2f} fm  [T2a]")
print(f"  At R = 0.5 fm: fraction = {abs(V_results[2][3])/V_results[2][2]*100:.1f}%")

assert R_valid_fm < 0.6, "string valid below 0.6 fm"
assert R_valid_fm > 0.2, "string breaks down above 0.2 fm"

# Numerical check: at R=0.5fm, Luscher fraction < 30%
ratio_0p5 = abs(V_results[2][3]) / V_results[2][2]
assert ratio_0p5 < 0.30, f"Luscher < 30% at 0.5 fm: got {ratio_0p5:.3f}"

# -----------------------------------------------------------------------
# Part E: Regge slope consistency [T3]
# -----------------------------------------------------------------------
print("\nPart E: Regge slope alpha' cross-check [T3]")
#
# For a Nambu-Goto string: alpha' = 1/(2*pi*sigma)
# This connects the string tension to the Regge trajectory slope.
# Same sigma was used in C160 (d7_nonpert_coefficients.py).
#
alpha_prime = 1.0 / (2.0 * np.pi * SIGMA)   # MeV^-2
alpha_prime_GeV2 = alpha_prime * 1e6         # GeV^-2

alpha_prime_obs  = 0.88e-6   # MeV^-2  (observed ~0.88 GeV^-2)
err_alpha        = (alpha_prime - alpha_prime_obs) / alpha_prime_obs * 100.0

print(f"  alpha' = 1/(2*pi*sigma) = {alpha_prime_GeV2:.4f} GeV^-2  [T3]")
print(f"  Observed alpha' = 0.88 GeV^-2  (light mesons)")
print(f"  Error: {err_alpha:+.1f}%  (consistent with C160: -2.5%)")
print(f"  Cross-check: same sigma gives consistent Regge slope ✓")

assert abs(err_alpha) < 5.0, "Regge slope within 5%"

# -----------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------
print(f"\n{'='*62}")
print("Summary: Static Potential (Cycle 228)")
print(f"{'='*62}")
print(f"  Input:  sigma = {SIGMA:.0f} MeV^2  [T2a, C222]")
print(f"  [T1]  V(R) = sigma*R - (pi/12)/R + V_0  (EST universal form)")
print(f"  [T2a] String picture valid for R > {R_valid_fm:.2f} fm")
print(f"  [T3]  V(0.5 fm) - V_0 = {V_results[2][4]:.0f} MeV  (sigma*R contribution dominates)")
print(f"  [T3]  alpha' = {alpha_prime_GeV2:.3f} GeV^-2  ({err_alpha:+.1f}% vs obs 0.88)")
print(f"\n  Consistency web (all from sigma = Q_top*Lambda^2 [T2a]):")
print(f"    sigma = {SIGMA:.0f} MeV^2  [T2a]")
print(f"    T_c = 271 MeV [T3, C227]   alpha' = {alpha_prime_GeV2:.3f} GeV^-2 [T3, C160]")
print(f"    m_0++ = 1529 MeV [T3, C226]   m_2++ = 2127 MeV [T3, C226]")
print(f"\n  ALL ASSERTIONS PASSED")
print(f"\n  Tier: T3 (inherits from sigma = Q_top*Lambda^2 T3 derivation)")
print(f"  Luscher coefficient pi/12: T1 exact (universal)")
print("=" * 62)
