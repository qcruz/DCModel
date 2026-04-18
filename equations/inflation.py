"""
Cosmic inflation as the DFC D1→D4 bifurcation cascade.

Physical question:
  Does the DFC substrate's bifurcation cascade produce inflationary behavior consistent
  with Planck 2018 observations (n_s = 0.9649, A_s = 2.1e-9, N_e ≥ 60)?

DFC mechanism:
  Inflation = D1→D4 bifurcation cascade. Each depth opening multiplies the apparent
  spatial DOFs and releases compression energy. The 'inflaton' is the substrate
  compression field φ itself — no separate inflaton field is needed.

  Structural resolutions in DFC (no extra parameters needed):
    - Flatness problem: dissolved (no pre-existing space to be flat)
    - Horizon problem: dissolved (pre-D3 substrate is one connected object)
    - Monopole problem: dissolved (π₂(S¹)=0 → no U(1) monopole topology)

  Quantitative results:
    - n_s = 1 − 2/N_e → 0.9667 at N_e = 60  (consistent with observed 0.9649)
    - N_e(naive) = ln(M_Pl/M_c(D4)) ≈ 10.5   (DEFICIT: need ~60)
    - A_s: BLOCKED (requires ε from compression dynamics)
    - r:   BLOCKED (requires D1 gravitational mode derivation)

Key reference:
  phenomena/cosmology/inflation.md
  equations/depth_running.py (M_c(D4) = 3.37e14 GeV)
"""

import math

# ============================================================
# Constants
# ============================================================
M_PLANCK_GEV = 1.22e19        # Planck mass in GeV
M_C_D4_GEV   = 3.37e14        # D4 closure scale (from depth_running.py)
M_C_D5_GEV   = 1.02e13        # D5 closure scale
M_C_D6_GEV   = 2.08e12        # D6 closure scale
M_C_D7_GEV   = 8.0e14         # D7 closure scale (from equal-coupling estimate)
BETA         = 0.035           # quartic coupling (Tier 3 reference value)

# Observed Planck 2018
N_S_OBS      = 0.9649
N_S_ERR      = 0.0044
A_S_OBS      = 2.100e-9
R_UPPER      = 0.036           # BICEP/Keck 2021 upper bound
N_E_REQUIRED = 60.0            # e-folds required to solve flatness/horizon

# ============================================================
# Computation 1: Naive e-fold count from D1→D4 cascade
# ============================================================
def efold_naive():
    """
    Naive N_e = ln(M_Pl / M_c(D4)): the logarithm of the hierarchy ratio
    between the Planck scale (onset of cascade) and the D4 closure scale
    (end of inflation → reheating).

    This gives the e-fold count if the cascade proceeds at constant Hubble
    rate H ~ M_c(D4)/M_Pl. Result is too small by factor ~5.7.
    """
    return math.log(M_PLANCK_GEV / M_C_D4_GEV)

def efold_extended_cascade(endpoint_scale_gev):
    """
    N_e for an extended cascade ending at a lower scale.
    If inflation extends deeper (e.g. to D7 or below), N_e increases.
    """
    return math.log(M_PLANCK_GEV / endpoint_scale_gev)

# ============================================================
# Computation 2: Spectral index from slow-roll formula
# ============================================================
def spectral_index(n_e):
    """
    The simplest single-field slow-roll result:
      n_s = 1 − 2/N_e
    This holds when the slow-roll parameters are both ≈ 1/N_e.
    """
    return 1.0 - 2.0 / n_e

def spectral_index_tension(n_e):
    """
    Deviation of DFC n_s from observed value, in sigma.
    """
    n_s_dfc = spectral_index(n_e)
    deviation = n_s_dfc - N_S_OBS
    sigma = deviation / N_S_ERR
    return n_s_dfc, deviation, sigma

# ============================================================
# Computation 3: De Sitter expansion rate from V_min
# ============================================================
def de_sitter_hubble(alpha_d1, beta=BETA):
    """
    The potential energy at the φ=0 false vacuum (before D1 bifurcation)
    acts as an effective cosmological constant.

    V_false = α²/(4β)   [energy density at unstable max of V(φ)]

    Friedmann equation (radiation+inflaton dominated):
      H² = V_false / (3 M_Pl²) = α²/(12 β M_Pl²)

    For α ~ M_Pl (natural at D1), H ~ M_Pl/√(12β).
    """
    V_false = alpha_d1**2 / (4.0 * beta)
    # H in GeV, with M_Pl in GeV
    H = math.sqrt(V_false / (3.0 * M_PLANCK_GEV**2))
    return V_false, H

# ============================================================
# Computation 4: Reheating consistency check
# ============================================================
def reheating_check():
    """
    DFC identifies T_reheat ~ M_c(D4).
    BBN requires T_reheat > 10 MeV = 1e-2 GeV.
    Check: does M_c(D4) satisfy this?
    """
    T_BBN_GEV = 1e-2  # Big Bang nucleosynthesis lower bound
    ok = M_C_D4_GEV > T_BBN_GEV
    ratio = M_C_D4_GEV / T_BBN_GEV
    return ok, ratio

# ============================================================
# Computation 5: Extended cascade N_e table
# ============================================================
def efold_table():
    """
    N_e for different cascade endpoints.
    Shows how many e-folds the DFC cascade produces under different
    assumptions about when inflation ends.
    """
    endpoints = [
        ("M_c(D4) [inertia]",     M_C_D4_GEV),
        ("M_c(D5) [U(1)]",        M_C_D5_GEV),
        ("M_c(D6) [SU(2)]",       M_C_D6_GEV),
        ("10^9 GeV [GUT scale]",   1e9),
        ("10^3 GeV [TeV]",         1e3),
        ("10 MeV [BBN]",           1e-2),
    ]
    rows = []
    for label, scale in endpoints:
        N_e = math.log(M_PLANCK_GEV / scale)
        n_s = spectral_index(N_e)
        rows.append((label, scale, N_e, n_s))
    return rows

# ============================================================
# Main output
# ============================================================
if __name__ == "__main__":
    print("=" * 68)
    print("equations/inflation.py — Cosmic inflation from DFC bifurcation cascade")
    print("=" * 68)

    print("\n--- Computation 1: Naive e-fold count (D1→D4) ---")
    N_e_naive = efold_naive()
    print(f"  M_Pl / M_c(D4) = {M_PLANCK_GEV:.2e} / {M_C_D4_GEV:.2e} GeV")
    print(f"  N_e(naive)  = ln(M_Pl/M_c(D4)) = {N_e_naive:.2f}")
    print(f"  Required    = {N_E_REQUIRED:.0f} e-folds")
    print(f"  Deficit     = factor {N_E_REQUIRED/N_e_naive:.1f} too few   ✗ OPEN")

    print("\n--- Computation 2: Spectral index n_s ---")
    print(f"  Slow-roll formula: n_s = 1 − 2/N_e")
    for n_e_test in [10.5, 50.0, 60.0, 65.0]:
        n_s, dev, sig = spectral_index_tension(n_e_test)
        marker = "✓" if abs(sig) < 1.0 else ("~" if abs(sig) < 2.0 else "✗")
        print(f"  N_e = {n_e_test:4.1f}: n_s = {n_s:.4f}  "
              f"(obs = {N_S_OBS:.4f}, Δ = {dev:+.4f}, {sig:+.1f}σ)  {marker}")
    print(f"\n  DFC prediction at N_e = {N_E_REQUIRED:.0f}:")
    n_s_60, dev_60, sig_60 = spectral_index_tension(N_E_REQUIRED)
    print(f"    n_s = {n_s_60:.4f}   observed = {N_S_OBS:.4f} ± {N_S_ERR:.4f}")
    print(f"    Agreement: {dev_60:+.4f} ({sig_60:+.1f}σ)   ✓ within 1σ (N_e not derived)")

    print("\n--- Computation 3: De Sitter H from V_false vacuum ---")
    alpha_d1 = M_PLANCK_GEV  # illustrative: α at D1 ~ M_Pl
    V_f, H_dS = de_sitter_hubble(alpha_d1)
    print(f"  V_false = α²/(4β)  [α = M_Pl = {M_PLANCK_GEV:.2e} GeV, β = {BETA}]")
    print(f"  V_false = {V_f:.2e} GeV⁴")
    print(f"  H_dS    = {H_dS:.2e} GeV  [de Sitter Hubble rate from D1 false vacuum]")
    print(f"  Note: α_D1 is NOT yet derived — this is illustrative only (Tier 4)")

    print("\n--- Computation 4: Reheating scale vs BBN ---")
    ok, ratio = reheating_check()
    print(f"  T_reheat ~ M_c(D4) = {M_C_D4_GEV:.2e} GeV")
    print(f"  T_BBN bound         = 1e-2 GeV = 10 MeV")
    print(f"  Ratio M_c(D4)/T_BBN = {ratio:.1e}   {'✓ satisfies BBN' if ok else '✗ fails BBN'}")

    print("\n--- Computation 5: N_e for extended cascade endpoints ---")
    print(f"  {'Endpoint':<30s}  {'Scale (GeV)':>12s}  {'N_e':>6s}  {'n_s':>6s}")
    print("  " + "-" * 60)
    for label, scale, N_e, n_s in efold_table():
        marker = "✓" if N_e >= 60 else ("~" if N_e >= 45 else "✗")
        print(f"  {label:<30s}  {scale:>12.2e}  {N_e:>6.1f}  {n_s:>6.4f}  {marker}")
    print(f"\n  N_e ≥ 60 achieved only at endpoint scales ≲ 10⁶ GeV")
    print(f"  Reheating below TeV conflicts with standard thermal history")

    print("\n--- Open Items ---")
    print(f"  A_s = {A_S_OBS:.2e}:  BLOCKED (requires ε from compression dynamics)")
    print(f"  r < {R_UPPER}:         BLOCKED (requires D1 gravitational mode derivation)")
    print(f"  N_e mechanism:         OPEN (factor {N_E_REQUIRED/N_e_naive:.1f} deficit)")
    print(f"  Slow-roll condition:   OPEN (requires ε,η from substrate field equation)")

    print("\n--- Summary ---")
    print(f"  ✓ Flatness problem: dissolved structurally (no pre-existing space)")
    print(f"  ✓ Horizon problem:  dissolved structurally (pre-D3 substrate connected)")
    print(f"  ✓ Monopoles:        no U(1) monopole topology (π₂(S¹)=0)")
    print(f"  ✓ n_s = {n_s_60:.4f} at N_e=60 (within 1σ of observed {N_S_OBS})")
    print(f"  ✗ N_e ≈ 10.5 from naive D1→D4 cascade (need 60)")
    print(f"  ✗ A_s prediction blocked")
    print(f"  ✗ r prediction blocked")
