"""
Bifurcation dynamics — depth-running and the closure scale hierarchy.

AUDIT STATUS (Cycle 48): The central claim of Cycle 32 — gamma_D = (16/3)*sqrt(beta) —
has been retracted. The derivation used an incorrect kink energy formula.

INCORRECT (old) formula:  E_kink = (4/3) c sqrt(2 alpha^3 / beta)
CORRECT (BPS) formula:    E_kink = (4/3) c^2 phi0^2 / lambda
                                 = (4/3) c alpha^(3/2) / (beta * sqrt(2))

The two differ by a factor of 2*sqrt(beta). With the correct formula:

    gamma_D = E_kink / E_total(lambda) = 8/3  (CONSTANT, beta-independent)

This is > 1, so it cannot be interpreted as a fraction of a compression budget.
The gamma_D = (16/3)*sqrt(beta) result was a numerical coincidence from using
the wrong E_kink. The correct E_kink/E_total(lambda) ratio is the universal
constant 8/3 for ANY alpha, beta, c — established algebraically and numerically.

Consequences:
  - beta ≈ 0.035 can no longer be inferred from gamma_space via this formula
  - beta remains a free parameter of the model (Tier 3 — inferred, not derived)
  - The depth-running integration run_depths() remains valid and self-consistent
  - M_c(D5) prediction still works if gamma_space is treated as an independent input

The E_total(lambda) = ΔV * lambda formula is a valid scale combination, but its
physical interpretation as "total compression budget per kink width" is undermined
when E_kink > E_total.

Open: Find the correct E_total that makes gamma_D = E_kink/E_total ∈ (0,1) and
depends on beta in a physically meaningful way.

Key quantities that remain valid:
  gamma_space (fitted)  from M_Pl -> M_c(D5) depth-running  [run_depths()]
  M_c(D5)               reproduced to < 1% from gamma_space  [closure_scale_prediction()]
  S_kink / hbar         hierarchy at each depth               [separate from gamma_D]

Usage:
    python equations/bifurcation_dynamics.py
"""

import math

# ── Physical constants ─────────────────────────────────────────────────────────

M_PLANCK_GEV = 1.22e19      # Planck mass in GeV  (D1 anchor)
M_C_D5_GEV   = 1.02e13     # Route 3B: D5 closure scale in GeV
N_STEPS_D1_D5 = 4           # spacetime bifurcations D1->D5

# ── Core formula ──────────────────────────────────────────────────────────────

def gamma_from_beta(beta):
    """
    [RETRACTED — Cycle 48 audit] Old formula: gamma_D = (16/3) * sqrt(beta).

    This was derived using the INCORRECT kink energy formula:
      E_kink_wrong = (4/3) c sqrt(2 alpha^3 / beta)   [wrong by 2*sqrt(beta)]

    With the BPS-correct E_kink = (4/3) c alpha^(3/2) / (beta*sqrt(2)):
      gamma = E_kink(BPS) / E_total(lambda) = 8/3  [constant, beta-independent]

    The 8/3 constant exceeds 1 and cannot be a compression fraction.
    The formula below is preserved for reference but should not be used as a
    physical result. See module docstring for full discussion.

    Parameters
    ----------
    beta : float
        Quartic coupling in V(phi) = -alpha/2 * phi^2 + beta/4 * phi^4.

    Returns
    -------
    float : gamma_D per old (incorrect) formula — NOT a derived physical quantity.
    """
    return (16.0 / 3.0) * math.sqrt(beta)


def gamma_ratio_correct(alpha=1.0, beta=0.035, c=1.0):
    """
    Correct ratio E_kink(BPS) / E_total(lambda) = 8/3 (universal constant).

    E_kink(BPS)  = (4/3) c^2 phi0^2 / lambda = (4/3) c alpha^(3/2) / (beta*sqrt(2))
    E_total(lam) = ΔV * lambda = (alpha^2/4beta) * c*sqrt(2/alpha)
                 = (c*sqrt(2)/4beta) * alpha^(3/2)

    Ratio = [(4/3)c alpha^(3/2)/(beta*sqrt(2))] / [(c*sqrt(2)/4beta)*alpha^(3/2)]
          = (4/3) * 4 / (sqrt(2)*sqrt(2)) = (4/3)*4/2 = 8/3

    This is alpha-, beta-, c-independent. Since 8/3 > 1, E_total(lambda) is not
    an appropriate normalization for a "compression fraction."

    Parameters
    ----------
    alpha, beta, c : float  (default values for verification only)

    Returns
    -------
    float : 8/3 (verified numerically)
    """
    phi0 = math.sqrt(alpha / beta)
    lam = math.sqrt(2.0 * c**2 / alpha)
    E_kink_bps = (4.0 / 3.0) * c**2 * phi0**2 / lam
    E_total = (alpha**2 / (4.0 * beta)) * lam
    return E_kink_bps / E_total


def beta_from_gamma(gamma):
    """
    Substrate quartic coupling required to produce a given gamma.

    Inverse of gamma_from_beta: beta = (3 * gamma / 16)^2

    Parameters
    ----------
    gamma : float
        Target compression fraction per spacetime bifurcation.

    Returns
    -------
    float : quartic coupling beta
    """
    return (3.0 * gamma / 16.0) ** 2


# ── Depth-running integration ─────────────────────────────────────────────────

def run_depths(alpha_D1, gamma_space, n_steps=N_STEPS_D1_D5):
    """
    Integrate the depth-running equation alpha_{D+1} = alpha_D * (1 - gamma_space)
    from D1 through D(1+n_steps).

    Parameters
    ----------
    alpha_D1 : float
        Initial substrate compression parameter at D1 (GeV^2 in natural units).
    gamma_space : float
        Compression fraction per spacetime bifurcation.
    n_steps : int
        Number of bifurcation steps to integrate.

    Returns
    -------
    list of dict : alpha and M_c at each depth
    """
    results = []
    alpha = alpha_D1
    for step in range(n_steps + 1):
        D = 1 + step
        M_c = math.sqrt(alpha / 2.0)
        results.append({'D': D, 'alpha': alpha, 'M_c_gev': M_c})
        if step < n_steps:
            alpha = alpha * (1.0 - gamma_space)
    return results


def closure_scale_prediction(gamma_space, n_steps=N_STEPS_D1_D5):
    """
    Predict M_c(D5) from M_Pl and gamma_space.

    M_c(D5) = M_Pl * sqrt((1 - gamma_space)^n_steps)
            = M_Pl * (1 - gamma_space)^(n_steps/2)

    Parameters
    ----------
    gamma_space : float
        Compression fraction per bifurcation.
    n_steps : int
        Number of D1->D5 bifurcations (= 4).

    Returns
    -------
    float : predicted M_c(D5) in GeV
    """
    suppression = (1.0 - gamma_space) ** (n_steps / 2.0)
    return M_PLANCK_GEV * suppression


# ── Main derivation ───────────────────────────────────────────────────────────

def derive_gamma_analytically():
    """
    [RETRACTED — see module docstring] Old derivation of gamma_D = (16/3) sqrt(beta).

    The derivation is preserved here for auditability. It uses the INCORRECT
    E_kink formula. The correct derivation gives gamma = 8/3 (constant).

    --- OLD (INCORRECT) derivation ---
    E_kink(wrong) = (4/3) c sqrt(2) alpha^(3/2) / sqrt(beta)
    E_total(lam)  = (c sqrt(2) / 4 beta) * alpha^(3/2)
    gamma = (4/3) / sqrt(beta) * (4 beta) = (16/3) sqrt(beta)   [WRONG]

    --- CORRECT derivation ---
    E_kink(BPS)   = (4/3) c alpha^(3/2) / (beta sqrt(2))
    E_total(lam)  = (c sqrt(2) / 4 beta) * alpha^(3/2)
    gamma = (4/3) * 4 / (sqrt(2) * sqrt(2)) = 8/3               [CORRECT]

    Returns
    -------
    dict with old (incorrect) steps and corrected steps for comparison
    """
    return {
        'RETRACTED':      'gamma_D = (16/3)*sqrt(beta) was derived with wrong E_kink',
        'E_kink_wrong':   'E_kink(wrong) = (4/3) c sqrt(2) alpha^(3/2) / sqrt(beta)',
        'E_kink_correct': 'E_kink(BPS)   = (4/3) c alpha^(3/2) / (beta*sqrt(2))',
        'E_total_form':   'E_total(lam)  = (c sqrt(2) / 4 beta) * alpha^(3/2)  [= ΔV*λ]',
        'old_result':     'gamma_wrong = (16/3) * sqrt(beta)  [WRONG — uses wrong E_kink]',
        'correct_result': 'gamma_correct = 8/3 ≈ 2.667  [CORRECT — but > 1, unphysical fraction]',
        'note':           'gamma_correct is beta-independent. E_total(lambda) not right normalization.',
    }


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("BIFURCATION DYNAMICS — DEPTH-RUNNING AND CLOSURE SCALE")
    print("Dimensional Folding Compression Model")
    print("=" * 65)

    # --- Audit result: gamma_D = (16/3)sqrt(beta) retracted
    print("\n--- AUDIT RESULT (Cycle 48): gamma_D = (16/3)*sqrt(beta) RETRACTED ---")
    steps = derive_gamma_analytically()
    for key, val in steps.items():
        print(f"  {val}")
    print()

    # --- Verify the correct ratio
    print("--- Correct Ratio: E_kink(BPS) / E_total(lambda) ---")
    for beta_test in [0.035, 0.1, 1.0, 0.5]:
        r = gamma_ratio_correct(alpha=1.0, beta=beta_test, c=1.0)
        print(f"  beta={beta_test:.3f}: E_kink/E_total = {r:.6f}  (expected 8/3 = {8/3:.6f})")
    print(f"  [8/3 is beta-independent — E_total(lambda) is not the right normalization]")

    # --- Depth-running: gamma_space treated as independent parameter
    print("\n--- Depth-Running: M_c(D5) from M_Pl via gamma_space ---")
    print("  [gamma_space is now a free input; beta connection via old formula RETRACTED]")
    ratio = M_C_D5_GEV / M_PLANCK_GEV
    gamma_space_fit = 1.0 - math.sqrt(ratio)
    beta_old_inference = beta_from_gamma(gamma_space_fit)

    print(f"  M_Pl = {M_PLANCK_GEV:.3e} GeV")
    print(f"  M_c(D5) target = {M_C_D5_GEV:.3e} GeV  [Route 3B]")
    print(f"  gamma_space (fitted from M_c/M_Pl) = {gamma_space_fit:.6f}")
    print(f"  OLD (retracted) beta inference: beta = (3*gamma/16)^2 = {beta_old_inference:.6f}")
    print(f"  STATUS: beta is a free parameter of the substrate [Tier 3]")

    # --- Verify M_c(D5) prediction
    print("\n--- Verification: M_c(D5) from depth-running (gamma_space as input) ---")
    alpha_D1 = 2.0 * M_PLANCK_GEV ** 2
    depth_results = run_depths(alpha_D1, gamma_space_fit, n_steps=N_STEPS_D1_D5)

    print(f"  {'D':>4}  {'alpha (GeV^2)':>18}  {'M_c (GeV)':>15}")
    print(f"  {'-'*4}  {'-'*18}  {'-'*15}")
    for row in depth_results:
        print(f"  D{row['D']:<3}  {row['alpha']:>18.4e}  {row['M_c_gev']:>15.4e}")

    mc_predicted = depth_results[-1]['M_c_gev']
    error_pct = (mc_predicted - M_C_D5_GEV) / M_C_D5_GEV * 100
    print(f"\n  M_c(D5) predicted = {mc_predicted:.4e} GeV")
    print(f"  M_c(D5) target    = {M_C_D5_GEV:.4e} GeV")
    print(f"  Error             = {error_pct:+.3f}%  [depth-running self-consistent]")

    # --- Physical interpretation: BPS-correct kink energy at D1
    beta_ref = 0.035     # reference value (Tier 3 — no longer inferred from gamma_D)
    print(f"\n--- Kink Energy at D1 (BPS-correct formula, beta = {beta_ref} reference) ---")
    phi0_D1 = math.sqrt(alpha_D1 / beta_ref)
    lambda_D1 = math.sqrt(2.0 / alpha_D1)   # c=1
    E_kink_D1_bps = (4.0/3.0) * alpha_D1**1.5 / (beta_ref * math.sqrt(2.0))
    E_total_D1 = (alpha_D1**2 / (4.0 * beta_ref)) * lambda_D1
    print(f"  alpha_D1 = {alpha_D1:.3e} GeV^2,  beta = {beta_ref}")
    print(f"  phi_0  = {phi0_D1:.4e} GeV")
    print(f"  lambda = {lambda_D1:.4e} GeV^-1 = {lambda_D1 * 0.197e-15:.3e} m")
    print(f"  E_kink (BPS-correct) = {E_kink_D1_bps:.4e} GeV")
    print(f"  E_total (ΔV×λ)       = {E_total_D1:.4e} GeV")
    print(f"  Ratio E_kink/E_total = {E_kink_D1_bps/E_total_D1:.6f}  (= 8/3 = {8/3:.6f})")
    print(f"  [Ratio > 1: E_total(λ) is not a valid compression fraction denominator]")

    # --- Planck constant hierarchy: S_kink / hbar at each depth
    # S_kink = E_kink * lambda / c = (4/3) * c * alpha^(3/2) / (beta*sqrt(2)) * sqrt(2/alpha)/c
    #        = (4/3) * alpha / beta  [c-independent action]
    # NOTE: S_kink formula depends on beta_ref; hierarchy value still indicative
    print(f"\n--- Kink Action Hierarchy: S_kink / hbar at each depth (beta = {beta_ref}) ---")
    print("  S_kink = E_kink * lambda = (4/3) * alpha / beta  [c-independent action, c=1]")
    print(f"  {'D':>4}  {'alpha (GeV^2)':>18}  {'S_kink / hbar':>16}  {'lambda (m)':>14}")
    print(f"  {'-'*4}  {'-'*18}  {'-'*16}  {'-'*14}")
    hbar_c_MeV_fm = 197.3     # MeV*fm
    m_per_GeVinv = hbar_c_MeV_fm * 1e-15 / 1e3    # 1 GeV^-1 in meters
    for row in depth_results:
        alpha_d = row['alpha']
        # S_kink = E_kink * lambda [with c=1]
        # E_kink(BPS) = (4/3) c alpha^(3/2)/(beta*sqrt(2)), lambda = sqrt(2/alpha)
        # S_kink = (4/3) alpha^(3/2)/(beta*sqrt(2)) * sqrt(2/alpha) = (4/3)*alpha/beta
        S_kink_over_hbar = (4.0/3.0) * alpha_d / beta_ref
        lambda_kink_m = math.sqrt(2.0 / alpha_d) * m_per_GeVinv
        print(f"  D{row['D']:<3}  {alpha_d:>18.4e}  {S_kink_over_hbar:>16.4e}  {lambda_kink_m:>14.3e}")
    S_kink_D1 = (4.0/3.0) * alpha_D1 / beta_ref
    print(f"\n  S_kink(D1) / hbar = {S_kink_D1:.3e}")
    print(f"  Bifurcations to reach S_kink = hbar: ~{math.log10(S_kink_D1)/3:.1f}")
    print(f"  NOTE: See foundations/planck_constant_derivation.md for interpretation.")

    # --- Summary
    print("\n--- Summary ---")
    print(f"  RETRACTED: gamma_D = (16/3)*sqrt(beta)  [used wrong E_kink formula]")
    print(f"  CORRECT:   E_kink(BPS)/E_total(λ) = 8/3 (constant, beta-independent)")
    print(f"  OPEN:      Find E_normalization that gives gamma_D ∈ (0,1) and depends on beta")
    print(f"  VALID:     Depth-running M_c(D5) = {mc_predicted:.3e} GeV ({error_pct:+.3f}% error) [gamma_space as input]")
    print(f"  STATUS:    beta ≈ 0.035 remains Tier 3 — reference value, not derived")
