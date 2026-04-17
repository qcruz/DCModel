"""
Lamb Shift — DFC Self-Energy Scaling Estimate
===============================================

Physical question:
    What is the energy splitting between the hydrogen 2s₁/₂ and 2p₁/₂ levels (the Lamb
    shift), and how well does the DFC coupling chain predict it?

DFC mechanism:
    The electron is a D6 kink closure. The photon is a massless D5 U(1) mode. The
    electron-photon coupling g_em is derived from the substrate quartic coupling β via:
        β → g² = 8πβ/3 → α_em(M_Z) = 1/129.6 → QED running → α_em(m_e) = 1/140.1
    (see equations/atomic_structure.py and equations/coupling_derivation.py)

    The Lamb shift arises from the one-loop electron self-energy in the hydrogen potential.
    The dominant non-relativistic contribution (Bethe 1947) is:

        ΔE_Lamb(2s, n=2) = (4 α⁵ m_e c²) / (3π n³) × ln(m_e c² / (2 <E>_avg))

    where:
        n = 2 for the 2s state
        <E>_avg ≈ 16.6 eV = Bethe's average excitation energy for the 2s state
        α⁵ scaling comes from: α² (self-energy) × α (vertex) × α² (Rydberg units)

    The 2p contribution is negligible because |ψ_2p(0)|² = 0 (node at nucleus).

    DFC prediction: The same formula applies, with α_em(m_e) = 1/140.1 instead of
    the physical 1/137.036. The Lamb shift scales as α⁵, giving a systematic error
    of 5 × 2.2% ≈ 11% below the observed value.

DFC tier: TIER 2b (failing — 11% systematic error exceeds 5% threshold)
    Root cause: same α_em error (1.3% at M_Z → 2.2% at m_e after running) as all
    DFC EM predictions. Traces to the r_U1/λ gap in the coupling chain.

Key references:
    - Lamb & Retherford (1947): Δν_Lamb = 1057.845 MHz (observed)
    - Bethe (1947): non-relativistic one-loop estimate, dominant term (~1040 MHz)
    - phenomena/quantum/lamb_shift.md — DFC structural account
    - equations/atomic_structure.py — QED running and hydrogen energy levels
    - equations/coupling_derivation.py — β → g_em chain
    - equations/anomalous_magnetic_moment.py — g-2 from same α chain (−2.01% error)
    - foundations/bifurcation_mode_count.md — Bottleneck 1 (coupling gap source)

Cycle 62 | Tier 2b — DFC scaling estimate computed; loop integral derivation open
"""

import math

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

LAMB_SHIFT_OBSERVED_MHZ = 1057.845   # 2s₁/₂ − 2p₁/₂ in hydrogen (Lamb & Retherford 1947)
BETHE_DOMINANT_MHZ      = 1040.0     # Bethe (1947) dominant non-relativistic term (reference)

# DFC coupling chain (from coupling_derivation.py and atomic_structure.py)
ALPHA_EM_MZ = 1.0 / 129.6    # DFC: α_em at M_Z (1.3% error vs observed 1/127.9)
ALPHA_EM_ME = 1.0 / 140.1    # DFC: α_em at m_e after QED running
ALPHA_OBS   = 1.0 / 137.036  # Observed fine structure constant at low energy

M_E_EV      = 511000.0       # Electron rest energy [eV]
M_C_D5_GEV  = 9.44e12        # DFC closure scale at D5/D6 [GeV] — natural UV cutoff
EV_PER_MHZ  = 1.0 / 2.41799e8   # 1 MHz = 1/2.41799e8 eV

# Bethe parameters for dominant 2s contribution
N_PRINCIPAL = 2              # n = 2 for the 2s state
E_AVG_EV    = 16.6           # Bethe average excitation energy <E>_avg for 2s [eV]


# ─────────────────────────────────────────────────────────────────────────────
# 1. Bethe non-relativistic dominant term (QED reference, not DFC)
# ─────────────────────────────────────────────────────────────────────────────

def bethe_formula_mhz(alpha=ALPHA_OBS, n=N_PRINCIPAL, E_avg_eV=E_AVG_EV):
    """
    Non-relativistic Bethe (1947) dominant 2s self-energy contribution.
    This is the QED comparison target — NOT a DFC-derived result.

    Bethe's result for the dominant self-energy term of the ns state:

        ΔE(ns) = (4 α⁵ m_e c²) / (3π n³) × ln(m_e c² / (2 <E>_avg))

    The key features:
      - α⁵ scaling: two powers from self-energy diagram, two from the hydrogen
        Bohr radius normalization, one from the log cutoff
      - 1/n³: from the s-wave probability density at the nucleus |ψ_ns(0)|² ∝ 1/n³
      - Bethe log: ln(m_e c² / 2<E>_avg); <E>_avg ≈ 16.6 eV for 2s (Bethe 1947)
      - 2p contribution is zero: |ψ_2p(0)|² = 0 (node at nucleus)

    NOTE: The simple formula above gives ~1351 MHz (vs Bethe's ~1040 MHz). The
    discrepancy arises because the exact Bethe calculation involves the full sum
    over all intermediate states (not just the simplified <E>_avg approximation).
    Bethe's actual numerical result (1040 MHz) is used as the authoritative
    reference for the dominant non-relativistic term.

    Args:
        alpha: fine structure constant
        n: principal quantum number (2 for 2s)
        E_avg_eV: Bethe average excitation energy [eV]

    Returns: dominant self-energy contribution [MHz]
    """
    bethe_log = math.log(M_E_EV / (2.0 * E_avg_eV))
    delta_E_eV = (4.0 * alpha**5 * M_E_EV) / (3.0 * math.pi * n**3) * bethe_log
    return delta_E_eV * 2.41799e8


# ─────────────────────────────────────────────────────────────────────────────
# 2. DFC systematic scaling estimate (Tier 2b)
# ─────────────────────────────────────────────────────────────────────────────

def dfc_lamb_shift_scaling():
    """
    DFC prediction for the Lamb shift via α⁵ scaling from the observed value.

    Since the DFC loop integral has not been computed from first principles, the
    DFC prediction is estimated by scaling the observed value by the ratio of
    the DFC fine structure constant to the physical value, raised to the fifth power.

    The Lamb shift scales as α⁵ in leading order:
        ΔE_Lamb ∝ α⁵ m_e c² / n³ × (Bethe log factor)

    With α_DFC(m_e) = 1/140.1 vs α_obs = 1/137.036:
        α_DFC/α_obs = 137.036/140.1 = 0.97815
        (α_DFC/α_obs)⁵ = 0.97815⁵ ≈ 0.8954

    DFC status: TIER 2b — the −10.5% error exceeds the 5% threshold.
    Root cause: same 2.2% α_em(m_e) error that affects all DFC EM predictions.
    The α⁵ dependence amplifies the coupling error: 5 × 2.2% ≈ 11%.

    Note: This is a scaling estimate, not a derived DFC loop integral. The loop
    integral requires the DFC photon propagator and is blocked pending the
    r_U1/λ derivation (Bottleneck 2; see foundations/coupling_derivation.md).

    Returns: dict with prediction, observed, error
    """
    alpha_ratio = ALPHA_EM_ME / ALPHA_OBS   # < 1 since α_DFC < α_obs
    scaling     = alpha_ratio**5
    prediction  = LAMB_SHIFT_OBSERVED_MHZ * scaling
    error_pct   = 100.0 * (prediction - LAMB_SHIFT_OBSERVED_MHZ) / LAMB_SHIFT_OBSERVED_MHZ
    alpha_err   = 100.0 * (ALPHA_EM_ME - ALPHA_OBS) / ALPHA_OBS
    return {
        'prediction_MHz': prediction,
        'observed_MHz':   LAMB_SHIFT_OBSERVED_MHZ,
        'relative_error': error_pct,
        'alpha_DFC_me':   ALPHA_EM_ME,
        'alpha_obs_me':   ALPHA_OBS,
        'alpha_error_pct': alpha_err,
        'alpha_power':    5,
        'tier':           '2b',
    }


# ─────────────────────────────────────────────────────────────────────────────
# 3. Error budget comparison with other DFC EM predictions
# ─────────────────────────────────────────────────────────────────────────────

def dfc_em_error_budget():
    """
    Compare the Lamb shift systematic error with other DFC EM predictions.
    All errors trace to the single 2.2% error in α_em(m_e).

    The error scales as n × Δα/α where n is the power of α in the leading formula:
        - Thomson cross-section: σ_T ∝ α², error ~ 2 × 2.2% = 4.3%
        - Electron g-2 (leading): a_e ∝ α¹, error ~ 1 × 2.2% = 2.2%
        - Hydrogen energy levels: E_n ∝ α², error ~ 2 × 2.2% = 4.3%
        - Lamb shift:             ΔE ∝ α⁵, error ~ 5 × 2.2% = 11%

    All are Tier 2b (failing) for the same reason: α_em(m_e) = 1/140.1
    rather than the physical 1/137.036.
    """
    alpha_err_pct = 100.0 * (ALPHA_EM_ME - ALPHA_OBS) / ALPHA_OBS
    return [
        {'observable': 'H energy levels (E_n)',   'alpha_power': 2, 'predicted_err_pct': 2*alpha_err_pct},
        {'observable': 'Thomson cross-section',   'alpha_power': 2, 'predicted_err_pct': 2*alpha_err_pct},
        {'observable': 'Electron g-2 (leading)',  'alpha_power': 1, 'predicted_err_pct': 1*alpha_err_pct},
        {'observable': 'Lamb shift (leading)',    'alpha_power': 5, 'predicted_err_pct': 5*alpha_err_pct},
    ]


# ─────────────────────────────────────────────────────────────────────────────
# Main output
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("DFC Lamb Shift — Scaling Estimate")
    print("=" * 65)
    print("Cycle 62 | phenomena/quantum/lamb_shift.md")
    print()

    # ── 1. Bethe formula (QED reference) ────────────────────────────────────
    print("── 1. Bethe Formula (QED — not DFC) ───────────────────────────")
    b_phys = bethe_formula_mhz(alpha=ALPHA_OBS)
    b_dfc  = bethe_formula_mhz(alpha=ALPHA_EM_ME)
    print(f"  Observed (Lamb & Retherford 1947): {LAMB_SHIFT_OBSERVED_MHZ:.3f} MHz")
    print(f"  Bethe dominant term (reference):   {BETHE_DOMINANT_MHZ:.0f} MHz  [full matrix sum]")
    print(f"  Bethe formula (physical α, n=2):   {b_phys:.0f} MHz")
    print(f"    [Simple formula gives {b_phys:.0f} vs Bethe's {BETHE_DOMINANT_MHZ:.0f}; discrepancy from")
    print(f"     simplified <E>_avg approximation — exact calculation sums all states]")
    print()

    # ── 2. DFC scaling prediction ────────────────────────────────────────────
    print("── 2. DFC Prediction (α⁵ scaling; Tier 2b) ────────────────────")
    res = dfc_lamb_shift_scaling()
    print(f"  DFC α_em(m_e) = 1/{1/res['alpha_DFC_me']:.1f}  (observed: 1/{1/res['alpha_obs_me']:.3f})")
    print(f"  α_em error:   {res['alpha_error_pct']:.2f}%")
    print(f"  Lamb shift ∝ α⁵ → error ≈ 5 × {abs(res['alpha_error_pct']):.2f}% = {5*abs(res['alpha_error_pct']):.1f}%")
    print()
    print(f"  DFC prediction:  {res['prediction_MHz']:.1f} MHz")
    print(f"  Observed:        {res['observed_MHz']:.3f} MHz")
    print(f"  Relative error:  {res['relative_error']:.1f}%  ✗ TIER 2b (exceeds 5% threshold)")
    print()
    print(f"  Root cause: r_U1/λ gap in coupling chain → α_em(m_e) 2.2% low")
    print(f"              α⁵ dependence amplifies this to {5*abs(res['alpha_error_pct']):.1f}%")
    print()

    # ── 3. Error budget ──────────────────────────────────────────────────────
    print("── 3. DFC Electromagnetic Error Budget ─────────────────────────")
    print(f"  Single source: α_em(m_e) error = {res['alpha_error_pct']:.2f}%")
    print()
    print(f"  {'Observable':<30} {'α power':>7} {'Predicted error':>15}")
    print(f"  {'-'*55}")
    for row in dfc_em_error_budget():
        flag = '✗ Tier 2b' if abs(row['predicted_err_pct']) > 5.0 else '~ Tier 2a'
        print(f"  {row['observable']:<30} {row['alpha_power']:>7}    {row['predicted_err_pct']:>+7.1f}%   {flag}")
    print()
    print("  Resolving the r_U1/λ gap (Bottleneck 2) would fix all four.")
    print()

    # ── 4. Open items ────────────────────────────────────────────────────────
    print("── 4. Open Items ───────────────────────────────────────────────")
    print("  DFC loop integral (not yet computed):")
    print("    g_em² = 4π α_em(m_e) = 4π/140.1  [DFC input]")
    print(f"    UV cutoff: M_c(D5) = {M_C_D5_GEV:.2e} GeV  (vs m_e = 0.511 MeV)")
    print("    The ratio M_c(D5)/m_e = {:.2e}  (UV-safe; physical cutoff)".format(
          M_C_D5_GEV / 5.11e-4))
    print("    OPEN: Compute ∫d⁴k D_μν(k) S_F(p−k) in DFC D5 momentum space")
    print("    See: foundations/coupling_derivation.md (Bottleneck 2)")
