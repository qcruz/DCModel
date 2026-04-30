"""
Derivation of the substrate quartic coupling beta from first principles.

STATUS (Cycle 87):
  Routes A–E all fail to derive beta from pure substrate mechanics.
  Route F (NEW — Cycle 87): beta is self-consistently determined by combining
  the compact form g² = 2π×β×I₄ (Bottleneck 2, Cycle 85) with the SM equal-coupling
  condition at M_c. This is not an ab initio derivation, but it removes beta as a
  genuinely free parameter — it is the unique value consistent with both the DFC
  compact form and the observed gauge couplings.

ROUTE F RESULT:
  β_predicted = 3 g_common² / (8π)  [from g² = 8πβ/3 inverted]
  g_common = 0.5443  [from SM running at M_c(12) — α₁ = α₂ crossing]
  β_predicted = 3 × 0.5443² / (8π) = 0.03537
  β_reference  = 0.0351  (Tier 3)
  Agreement: 0.76%

  This means: IF the compact form g² = 2π×β×I₄ is formally proved (Bottleneck 2),
  THEN β is DERIVED from SM running — no longer a free parameter.

WHAT IS NOT YET DERIVED:
  The compact form g² = 2π×β×I₄ is heuristically motivated (Cycles 42–85) but not
  formally proved from the V(φ) field equation. Until that proof is complete, Route F
  is a self-consistency condition, not a rigorous derivation.

  Even with Route F, the CHAIN is:
    SM running  →  g_common  →  [compact form, heuristic]  →  β
  The SM running itself uses g_common from the α₁=α₂ crossing, which DFC explains
  structurally (equal-coupling IC from same substrate kinetics, Route 3B). This is
  not circular — SM gives g_common independently, DFC gives β from it.

ROUTES OVERVIEW:
  A: Kink stability (ω₁ < m_σ) — does not constrain β. FAILS.
  B: Minimum coupling (M_K/|V_min|^{1/4} = const) — gives β(α), not a pure number. FAILS.
  C: Topological winding Q = M_Pl — gives β = 8 (factor ~230× too large). FAILS.
  D: β from α_U (coupling identity) — factor 1.46 off. Fails.
  E: Shape mode resonance — β-independent (always satisfied). FAILS.
  F: β from g_common + compact form g²=8πβ/3 (Cycle 87) — 0.76% error. BEST AVAILABLE.
     Status: Tier 3 self-consistency (not ab initio; requires Bottleneck 2 proof).

Key references:
  - foundations/phase_stiffness_derivation.md  (f² = (4/3)φ₀²/λ exact; Bottleneck 2 gap)
  - equations/bottleneck2_coupling_integral.py  (Cycle 85: g²=2π×β×I₄ compact form)
  - equations/coupling_derivation.py            (g_common = 0.5443 from SM running)
  - equations/gauge_couplings.py               (α₁ = α₂ at M_c(12) = 9.44×10¹² GeV)
  - foundations/bifurcation_dynamics.md        (NOTE: γ_D = (16/3)√β RETRACTED Cycle 48)

Usage:
    python3 equations/beta_substrate.py
"""

import math

# ─── Reference Values ─────────────────────────────────────────────────────────

BETA_REFERENCE    = 0.0351      # Tier 3 reference value (self-consistent, not ab initio)
I4                = 4.0 / 3.0   # ∫sech⁴(u) du = 4/3 (kink shape integral, exact)
G_COMMON_SM       = 0.5443      # from SM running at M_c(12): α₁=α₂ (gauge_couplings.py)
ALPHA_U_SM        = G_COMMON_SM**2 / (4 * math.pi)   # ≈ 0.02358

# ─── Route F: β from compact form + SM equal-coupling ────────────────────────

def route_f_beta_from_gcommon(g_common=G_COMMON_SM):
    """
    Route F (Cycle 87): β derived from the compact form g² = 2π×β×I₄ inverted.

    The compact form (Cycles 42–85):
        g_common² = 2π × β × I₄   where I₄ = 4/3

    Inverting:
        β = g_common² / (2π × I₄) = 3 × g_common² / (8π)

    The input g_common comes from SM running: the D5/D6 equal-coupling scale M_c(12)
    where α₁(M_c) = α₂(M_c). This is independent of β (it comes from SM precision
    electroweak data). The compact form then determines β.

    Physical interpretation:
      β is not a free parameter — it is the unique quartic coupling consistent with
      DFC kink structure AND the observed equal-coupling scale. The kink shape integral
      I₄ = 4/3 (from the Bogomolny identity) locks β to g_common.

    Status: Tier 3 self-consistency. Becomes Tier 2 derivation once the compact form
      g² = 2π×β×I₄ is formally proved from V(φ) (Bottleneck 2).

    Returns β_predicted and comparison to β_reference.
    """
    beta_predicted = g_common**2 / (2.0 * math.pi * I4)
    g_check        = math.sqrt(2.0 * math.pi * beta_predicted * I4)
    error_pct      = (beta_predicted / BETA_REFERENCE - 1.0) * 100.0
    return {
        'g_common_input':   g_common,
        'I4':               I4,
        'beta_predicted':   beta_predicted,
        'beta_reference':   BETA_REFERENCE,
        'error_pct':        error_pct,
        'g_check':          g_check,              # should equal g_common
        'g_error_pct':      (g_check/g_common - 1.0) * 100.0,
    }


def route_f_sensitivity(g_lo=0.540, g_hi=0.550, n=11):
    """
    Sensitivity of β_predicted to g_common.

    Shows how β changes across the range of plausible g_common values
    (SM running gives 0.5443 ± ~0.5% from M_c uncertainty).
    """
    results = []
    for i in range(n):
        g = g_lo + (g_hi - g_lo) * i / (n - 1)
        beta = g**2 / (2.0 * math.pi * I4)
        results.append({'g_common': g, 'beta': beta,
                        'error_pct': (beta/BETA_REFERENCE - 1.0)*100.0})
    return results


# ─── Routes A–E (documented failures) ───────────────────────────────────────

def route_a_stability():
    """Route A: kink stability does not constrain β (always satisfied)."""
    # ω₁ = √(3/2 α) < m_σ = √(2α) for all α,β > 0
    # Ratio ω₁/m_σ = √(3/4) = √3/2 ≈ 0.866 — independent of β
    ratio = math.sqrt(3.0 / 4.0)
    return {'ratio_omega1_msigma': ratio, 'beta_independent': True, 'result': 'FAILS'}


def route_b_minimum_coupling(alpha=1.0):
    """
    Route B: M_K / |V_min|^{1/4} = constant?

    M_K = (4/3) α^{3/2} / (β √2)   [BPS-correct, Cycle 48]
    |V_min|^{1/4} = (α²/(4β))^{1/4} = α^{1/2} / (4β)^{1/4}

    Ratio = M_K / |V_min|^{1/4}
          = (4/3) α^{3/2}/(β√2) × (4β)^{1/4} / α^{1/2}
          = (4/3) × 4^{1/4} × α / (β^{3/4} × √2)

    This ratio depends on α (not just β), so setting it to a constant
    gives β(α), not a universal number. Route fails.
    """
    M_K_coeff  = (4.0/3.0) * alpha**1.5 / math.sqrt(2.0)  # × 1/β
    Vmin_coeff = math.sqrt(alpha) / (4.0)**0.25            # × 1/β^{1/4}
    # ratio = M_K_coeff/(β) / (Vmin_coeff/β^{1/4}) = M_K_coeff/(Vmin_coeff × β^{3/4})
    # Setting = 1: β^{3/4} = M_K_coeff/Vmin_coeff
    beta_solution = (M_K_coeff / Vmin_coeff) ** (4.0/3.0)
    return {'beta_solution': beta_solution, 'alpha_dependent': True,
            'alpha_used': alpha, 'result': 'FAILS (β depends on α)'}


def route_c_topological_winding():
    """
    Route C: topological charge Q = 2φ₀ = M_Pl.

    2 √(α_D1/β) = M_Pl  with  α_D1 = 2M_Pl²  →  β = 8.
    """
    M_Pl = 1.221e19  # GeV
    alpha_D1 = 2.0 * M_Pl**2
    # Q = 2√(α/β) = M_Pl → β = 4α/M_Pl² = 4×2M_Pl²/M_Pl² = 8
    beta = 4.0 * alpha_D1 / M_Pl**2
    return {'beta': beta, 'factor_off': beta / BETA_REFERENCE, 'result': 'FAILS (β=8, 230× too large)'}


def route_d_coupling_identity():
    """
    Route D: β from the equal-coupling constant α_U.

    Tests several simple relations between β and α_U = g²/(4π) ≈ 0.02358.
    The closest is β = α_U (factor 1.49 off).
    """
    alpha_U = ALPHA_U_SM
    candidates = {
        '4π α_U':          4.0 * math.pi * alpha_U,
        'α_U':             alpha_U,
        'α_U × π/8':       alpha_U * math.pi / 8.0,
        '3α_U/(8π) × 4π²': 3.0 * alpha_U / (8.0 * math.pi) * 4.0 * math.pi**2,
    }
    results = {k: {'beta': v, 'factor': v/BETA_REFERENCE} for k, v in candidates.items()}
    # None give β ≈ 0.035 cleanly
    return {'alpha_U': alpha_U, 'candidates': results,
            'closest': 'α_U (factor 1.49 off)', 'result': 'FAILS'}


def route_e_shape_mode():
    """
    Route E: shape mode at ω₁ = √(3α/2) is β-independent. No constraint on β.
    """
    return {'omega1_sq_over_alpha': 1.5, 'beta_independent': True, 'result': 'FAILS'}


# ─── Summary ──────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('=' * 65)
    print('β SUBSTRATE DERIVATION — Route Analysis (Cycle 87)')
    print('Dimensional Folding Compression model')
    print('=' * 65)

    print(f'\nTarget: β_reference = {BETA_REFERENCE}  (Tier 3, self-consistent)')
    print(f'        g_common(SM) = {G_COMMON_SM}  (from α₁=α₂ crossing at M_c)')
    print(f'        α_U(SM)      = {ALPHA_U_SM:.5f}  (= g_common²/4π)')

    print(f'\n── Route F (NEW — Cycle 87): β from compact form + SM running ──')
    rf = route_f_beta_from_gcommon()
    print(f'   Compact form: g² = 2π × β × I₄  (I₄ = 4/3 = ∫sech⁴ du)')
    print(f'   Inverted:     β  = g²/(2π × I₄) = 3g²/(8π)')
    print(f'   g_common(SM) = {rf["g_common_input"]:.4f}  [from SM α₁=α₂ crossing]')
    print(f'   β_predicted  = {rf["beta_predicted"]:.5f}')
    print(f'   β_reference  = {rf["beta_reference"]:.5f}  (Tier 3)')
    print(f'   Error        = {rf["error_pct"]:+.2f}%')
    print(f'   → β is self-consistently determined to <1% by the compact form.')
    print(f'   → Status: Tier 3 self-consistency. Becomes Tier 2 once Bottleneck 2')
    print(f'     proof of g²=2π×β×I₄ is complete.')

    print(f'\n   Sensitivity of β_predicted to g_common (g in [{0.540:.3f},{0.550:.3f}]):')
    sens = route_f_sensitivity()
    for r in sens[::2]:
        print(f'     g_common = {r["g_common"]:.4f}  →  β = {r["beta"]:.5f}  '
              f'({r["error_pct"]:+.2f}% from reference)')

    print(f'\n── Routes A–E (failed) ──')
    ra = route_a_stability()
    print(f'   A (kink stability): ω₁/m_σ = {ra["ratio_omega1_msigma"]:.4f}  β-independent  [{ra["result"]}]')

    rb = route_b_minimum_coupling(alpha=1.0)
    print(f'   B (minimum coupling): β(α=1) = {rb["beta_solution"]:.4f}  α-dependent  [{rb["result"]}]')

    rc = route_c_topological_winding()
    print(f'   C (topological winding Q=M_Pl): β = {rc["beta"]:.1f}  [{rc["result"]}]')

    rd = route_d_coupling_identity()
    print(f'   D (β from α_U = {rd["alpha_U"]:.5f}):')
    for name, val in rd['candidates'].items():
        print(f'       {name:25s} = {val["beta"]:.5f}  (factor {val["factor"]:.2f})')
    print(f'       {rd["closest"]}')

    re = route_e_shape_mode()
    print(f'   E (shape mode resonance): β-independent  [{re["result"]}]')

    print(f'\n── Summary ──')
    print(f'   Route F is the only route giving β within 1% of the reference value.')
    print(f'   β = 3g_common²/(8π) = {rf["beta_predicted"]:.5f}  ({rf["error_pct"]:+.2f}% error)')
    print(f'   Interpretation: β is NOT a free parameter — it is determined by the')
    print(f'   observed equal-coupling g_common = {G_COMMON_SM} at M_c(D5/D6).')
    print(f'   This removes β from the free parameter count IF (and only if) the')
    print(f'   compact form g² = 2π×β×I₄ is formally derived (Bottleneck 2).')
    print(f'')
    print(f'   Tier status: Tier 3  (self-consistent; not yet ab initio derivation)')
