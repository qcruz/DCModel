"""
Depth-running of the substrate compression parameter α.

Physical question:
  The DFC substrate has a compression parameter α at each depth D.
  The closure scale at depth D is M_c(D) = √(α_D / 2) [natural units].
  Known constraints:
    M_c(D1) ≈ M_Pl = 1.22 × 10^19 GeV   (Planck-scale compression at D1)
    M_c(D5) ≈ M_c(D6) ≈ 10^13 GeV       (D5/D6 co-crystallization, Route 3B)
    sin²θ_W(M_Z) = 0.231 reproduced at M_c(D5) = 1.02 × 10^13 GeV

  Open: how does α_D evolve from D1 to D5/D6/D7?
  This module explores candidate depth-running models and identifies which are
  self-consistent with all known constraints.

DFC mechanism (working hypothesis):
  At each bifurcation depth D, the substrate opens a new degree of freedom.
  This costs compression budget. The residual compression drives the next bifurcation.
  The depth-running equation: α_{D+1} = α_D × (1 - γ_D)
  where γ_D = fraction of compression budget consumed at depth D.

  Candidate models for γ_D:
    Model 1 (Uniform): γ_D = γ for all D
    Model 2 (DOF-weighted): γ_D ∝ n_DOF opened at depth D
    Model 3 (Topology-weighted): γ_D ∝ dim(gauge group closed at D)
    Model 4 (Two-scale): large γ for D1-D4 (spacetime), small γ for D5-D7 (gauge)
    Model 5 (Fitted): γ_D values chosen to reproduce all known M_c constraints

  Key test: Model must produce M_c(D5) = M_c(D6) (co-crystallization) AND
  M_c(D5) ≈ 10^13 GeV AND M_c(D1) ≈ M_Pl.

See also:
  foundations/d_depth_lagrangians.md — the closure scale formula M_c = √(α/2)
  foundations/depth_running.md — derivation of depth-running from substrate mechanics
  equations/weinberg_angle_rg.py — confirms M_c(D5/D6) ≈ 10^13 GeV from sin²θ_W

Output format:
  For each model, prints M_c(D) at each depth and assesses consistency.
"""

import math
from typing import List, Dict, Tuple

# ─── Physical Constants ───────────────────────────────────────────────────────

M_PLANCK_GEV = 1.220910e19     # Reduced Planck mass in GeV (= √(ħc/G))
M_c_D5_TARGET = 1.02e13        # GeV — M_c(D5) from Route 3B (α₁=α₂ crossing)
M_c_D6_TARGET = 1.02e13        # GeV — co-crystallization: D5 and D6 form together
M_Z_GEV = 91.187               # GeV — Z boson mass
F_PI_GEV = 0.093               # GeV — pion decay constant (F_π = 93 MeV)
V_HIGGS_GEV = 246.0            # GeV — Higgs VEV

# Degrees of freedom opened at each depth transition (working assignments)
# These represent the new independent configuration space dimensions that appear
N_DOF_AT_DEPTH = {
    1: 0,   # D1: maximum compression, no apparent DOF yet
    2: 1,   # D2: scalar propagation mode (wave)
    3: 3,   # D3: 3 apparent spatial localization DOFs
    4: 1,   # D4: 1 temporal/inertia DOF
    5: 1,   # D5: 1 U(1) phase DOF (EM winding)
    6: 3,   # D6: 3 SU(2) generator DOFs (weak winding)
    7: 8,   # D7: 8 SU(3) generator DOFs (color winding)
}

# Gauge group closed at each depth (number of independent generators)
N_GENERATORS_AT_DEPTH = {
    1: 0, 2: 0, 3: 0, 4: 0,  # spacetime depths: no gauge closure
    5: 1,   # U(1): 1 generator
    6: 3,   # SU(2): 3 generators
    7: 8,   # SU(3): 8 generators
}


def alpha_to_mc(alpha_D: float) -> float:
    """M_c(D) = √(α_D / 2), in whatever units α_D is in."""
    return math.sqrt(alpha_D / 2.0)


def mc_to_alpha(M_c: float) -> float:
    """Inverse: α_D = 2 × M_c(D)²."""
    return 2.0 * M_c**2


def run_depth_model(gamma_list: List[float],
                    alpha_D1: float = None) -> List[Dict]:
    """
    Run the depth-running model given a list of γ values for each depth transition.

    gamma_list[i] = γ at depth (i+1) → (i+2), i.e.:
      gamma_list[0] = γ_{D1→D2}
      gamma_list[1] = γ_{D2→D3}
      ...
      gamma_list[5] = γ_{D6→D7}

    α_{D+1} = α_D × (1 - γ_D)
    M_c(D) = √(α_D / 2)

    Returns list of dicts: [{depth, alpha, M_c_GeV, log10_Mc}, ...]
    """
    if alpha_D1 is None:
        alpha_D1 = mc_to_alpha(M_PLANCK_GEV)

    alpha = alpha_D1
    results = []

    for depth in range(1, 8):
        M_c = alpha_to_mc(alpha)
        results.append({
            'depth': depth,
            'alpha': alpha,
            'M_c_GeV': M_c,
            'log10_Mc': math.log10(M_c),
        })
        if depth < 7:
            gamma = gamma_list[depth - 1]  # γ at depth → depth+1
            alpha = alpha * (1.0 - gamma)

    return results


def assess_model(results: List[Dict]) -> Dict:
    """
    Check consistency of a depth-running model with known constraints.
    Returns a dict of pass/fail checks.
    """
    mc_D5 = results[4]['M_c_GeV']  # D5 is index 4
    mc_D6 = results[5]['M_c_GeV']  # D6 is index 5
    mc_D1 = results[0]['M_c_GeV']

    # Co-crystallization: D5 and D6 should be at same scale
    cocryst_ratio = mc_D5 / mc_D6
    cocryst_ok = 0.1 < cocryst_ratio < 10  # within 1 order of magnitude

    # D5 scale: should be ≈ 10^13 GeV
    mc_D5_ok = 0.1 < mc_D5 / M_c_D5_TARGET < 10

    # D1 scale: should be ≈ M_Pl
    mc_D1_ok = 0.1 < mc_D1 / M_PLANCK_GEV < 10

    # D5/D6 within factor 2 (tight co-crystallization)
    tight_cocryst = 0.5 < cocryst_ratio < 2.0

    return {
        'mc_D5_GeV': mc_D5,
        'mc_D6_GeV': mc_D6,
        'mc_D7_GeV': results[6]['M_c_GeV'],
        'D1_at_Planck': mc_D1_ok,
        'D5_at_target': mc_D5_ok,
        'cocryst_order': cocryst_ok,
        'cocryst_tight': tight_cocryst,
        'mc_D5_vs_target': mc_D5 / M_c_D5_TARGET,
        'mc_D5_D6_ratio': cocryst_ratio,
    }


def fit_gamma_for_mc_D5(target_mc_D5: float = M_c_D5_TARGET,
                         gamma_list_template: List[float] = None,
                         n_depth_steps: int = 4,
                         alpha_D1: float = None) -> float:
    """
    Find the uniform γ that gives the target M_c at depth 5, starting from M_Pl at D1.

    If gamma_list_template is None, uses uniform γ over n_depth_steps transitions.

    The formula:
      M_c(D5) = M_Pl × (1-γ)^{n_steps/2}    [since M_c ∝ √α and α ∝ (1-γ)^n]
      (1-γ)^{n_steps/2} = M_c(D5) / M_Pl
      (1-γ) = (M_c(D5) / M_Pl)^{2/n_steps}
    """
    if alpha_D1 is None:
        alpha_D1 = mc_to_alpha(M_PLANCK_GEV)

    ratio = target_mc_D5 / M_PLANCK_GEV
    gamma_uniform = 1.0 - ratio**(2.0 / n_depth_steps)
    return gamma_uniform


def solve_two_scale_model(mc_D5: float = M_c_D5_TARGET,
                           mc_D7_over_D6: float = 1.0,
                           gamma_gauge: float = 0.0) -> List[float]:
    """
    Two-scale model:
      - D1→D4: uniform γ_space (macroscopic structure — large suppression)
      - D4→D5: γ_em (EM closure)
      - D5→D6: γ_weak ≈ 0 (co-crystallization — nearly zero suppression)
      - D6→D7: γ_color (SU(3) closure — different suppression)

    Constraints:
      M_c(D1) = M_Pl
      M_c(D5) = mc_D5 (from Route 3B)
      M_c(D5) ≈ M_c(D6)  →  γ_D5→D6 ≈ 0

    Free parameters:
      gamma_space: suppression per D1→D4 step (fixed by M_Pl → M_c(D5) constraint)
      gamma_em:    suppression at D4→D5
      mc_D7_over_D6: ratio M_c(D7)/M_c(D6) — determines γ_color

    Returns gamma_list for all 6 transitions.
    """
    alpha_D1 = mc_to_alpha(M_PLANCK_GEV)
    alpha_D5 = mc_to_alpha(mc_D5)

    # D1 → D5 involves 4 transitions (D1→2, D2→3, D3→4, D4→5)
    # For co-crystallization: D5→D6 has γ = gamma_gauge ≈ 0
    # Total suppression from D1 to D5: (1-γ_space)^3 × (1-γ_em)^1
    # Simplify: assume γ_em = γ_space (all pre-gauge steps equal)
    total_suppression = alpha_D5 / alpha_D1
    gamma_space = 1.0 - total_suppression**(1.0 / 4.0)  # 4 uniform steps

    # D5→D6: gamma_weak ≈ gamma_gauge (small, set by caller)
    gamma_weak = gamma_gauge

    # D6→D7: set by mc_D7_over_D6
    alpha_D6 = alpha_D5 * (1.0 - gamma_weak)
    alpha_D7 = mc_to_alpha(alpha_to_mc(alpha_D6) * mc_D7_over_D6)
    if alpha_D6 > 0:
        gamma_color = 1.0 - alpha_D7 / alpha_D6
    else:
        gamma_color = 0.0

    return [gamma_space,   # D1→D2
            gamma_space,   # D2→D3
            gamma_space,   # D3→D4
            gamma_space,   # D4→D5
            gamma_weak,    # D5→D6 (co-crystallization)
            gamma_color]   # D6→D7


# ─── Main Output ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 68)
    print("DEPTH-RUNNING OF SUBSTRATE COMPRESSION PARAMETER α")
    print("Dimensional Folding Model — M_c(D) = √(α_D / 2)")
    print("=" * 68)

    print(f"\n  M_Planck = {M_PLANCK_GEV:.3e} GeV  (D1 anchor)")
    print(f"  M_c(D5)  = {M_c_D5_TARGET:.3e} GeV  (Route 3B target)")
    print(f"  log10(M_Pl/M_c5) = {math.log10(M_PLANCK_GEV/M_c_D5_TARGET):.2f}")
    print(f"  α_D1/α_D5 = (M_Pl/M_c5)² = 10^{2*math.log10(M_PLANCK_GEV/M_c_D5_TARGET):.1f}")

    # ── Model 1: Uniform γ across all 6 steps ────────────────────────────────
    print("\n" + "─" * 68)
    print("MODEL 1: Uniform γ (same suppression at every depth transition)")
    print("─" * 68)
    g_uniform = fit_gamma_for_mc_D5(n_depth_steps=6)
    gammas_1 = [g_uniform] * 6
    res1 = run_depth_model(gammas_1)
    a1 = assess_model(res1)
    print(f"  γ_uniform = {g_uniform:.6f}  (= 1 - 10^{{-{-math.log10(1-g_uniform):.3f}}}/step)")
    print(f"  {'D':4s}  {'M_c (GeV)':14s}  {'log10(M_c)':10s}  {'Note'}")
    print(f"  {'─'*4}  {'─'*14}  {'─'*10}  {'─'*30}")
    for r in res1:
        note = ''
        if r['depth'] == 1: note = '← D1 anchor (M_Pl)'
        elif r['depth'] == 5: note = f"← D5 target: ×{a1['mc_D5_vs_target']:.2f}"
        elif r['depth'] == 6: note = f"← D6 ratio D5/D6: {a1['mc_D5_D6_ratio']:.3f}"
        elif r['depth'] == 7: note = f"← D7 predicted"
        print(f"  D{r['depth']}    {r['M_c_GeV']:14.3e}  {r['log10_Mc']:10.2f}  {note}")
    print(f"\n  D5 at target? {a1['D5_at_target']}  |  "
          f"Co-cryst (×{a1['mc_D5_D6_ratio']:.3f})? {a1['cocryst_tight']}")
    print(f"  PROBLEM: D5/D6 ratio = {a1['mc_D5_D6_ratio']:.3f} ≠ 1.0  "
          f"(uniform γ cannot produce co-crystallization)")

    # ── Model 2: DOF-weighted γ (proportional to DOF opened) ─────────────────
    print("\n" + "─" * 68)
    print("MODEL 2: DOF-weighted γ (suppression ∝ degrees of freedom opened)")
    print("─" * 68)
    # Weights proportional to n_DOF at destination depth
    dof_weights = [N_DOF_AT_DEPTH[d] for d in range(2, 8)]  # D2 through D7
    total_weight = sum(dof_weights)
    # Normalize: find γ_base such that total suppression gives M_c(D5) at depth 5
    # Total suppression D1→D5 = Π_{D=1}^{4} (1 - γ_base × w_D / w_mean)
    # This requires iteration
    def total_suppression_to_D5(gamma_base):
        alpha = mc_to_alpha(M_PLANCK_GEV)
        for d in range(1, 5):  # D1→D2, D2→D3, D3→D4, D4→D5
            w = N_DOF_AT_DEPTH[d + 1]  # DOF opened at next depth
            gamma_d = min(gamma_base * w, 0.9999)
            alpha *= (1.0 - gamma_d)
        return alpha_to_mc(alpha)

    # Binary search for γ_base
    lo, hi = 1e-10, 0.9999
    for _ in range(60):
        mid = (lo + hi) / 2
        if total_suppression_to_D5(mid) > M_c_D5_TARGET:
            lo = mid
        else:
            hi = mid
    gamma_base_dof = (lo + hi) / 2

    gammas_2 = [min(gamma_base_dof * N_DOF_AT_DEPTH[d+1], 0.9999) for d in range(1, 7)]
    res2 = run_depth_model(gammas_2)
    a2 = assess_model(res2)
    print(f"  γ_base = {gamma_base_dof:.6f}  (γ_D = γ_base × n_DOF_opened)")
    print(f"  Transition γ values: " +
          ", ".join(f"D{d}→{d+1}: {gammas_2[d-1]:.4f}(n={N_DOF_AT_DEPTH[d+1]})"
                    for d in range(1, 7)))
    print(f"  {'D':4s}  {'M_c (GeV)':14s}  {'log10(M_c)':10s}")
    for r in res2:
        print(f"  D{r['depth']}    {r['M_c_GeV']:14.3e}  {r['log10_Mc']:10.2f}")
    print(f"\n  D5 at target? {a2['D5_at_target']}  |  "
          f"Co-cryst (×{a2['mc_D5_D6_ratio']:.3f})? {a2['cocryst_tight']}")
    if not a2['cocryst_tight']:
        print(f"  PROBLEM: D5/D6 ratio = {a2['mc_D5_D6_ratio']:.3f}  "
              f"(DOF model: SU(2) has 3× more DOF than U(1) → D6 much suppressed)")

    # ── Model 3: Two-scale (spacetime vs gauge) ───────────────────────────────
    print("\n" + "─" * 68)
    print("MODEL 3: Two-scale (large γ for spacetime D1-D4; γ≈0 for D5-D6 co-cryst)")
    print("─" * 68)
    for gamma_weak_val in [0.0, 0.001, 0.01]:
        gammas_3 = solve_two_scale_model(mc_D5=M_c_D5_TARGET,
                                          mc_D7_over_D6=1.0,
                                          gamma_gauge=gamma_weak_val)
        res3 = run_depth_model(gammas_3)
        a3 = assess_model(res3)
        print(f"\n  γ_weak = {gamma_weak_val:.3f}  (D5→D6 suppression)")
        print(f"  γ_space = {gammas_3[0]:.6f}  (D1→D2 through D4→D5)")
        print(f"  {'D':4s}  {'M_c (GeV)':14s}  {'log10(M_c)':10s}")
        for r in res3:
            print(f"  D{r['depth']}    {r['M_c_GeV']:14.3e}  {r['log10_Mc']:10.2f}")
        print(f"  D5/D6 ratio: {a3['mc_D5_D6_ratio']:.4f}  "
              f"Co-cryst tight: {a3['cocryst_tight']}")

    # ── Model 4: Two-scale with D7 prediction ────────────────────────────────
    print("\n" + "─" * 68)
    print("MODEL 4: Two-scale + D7 prediction from topology-gap hypothesis")
    print("  Hypothesis: γ_D6→D7 ∝ dim(SU(3)) / dim(SU(2)) = 8/3")
    print("─" * 68)
    # Use Model 3 with γ_weak = 0.001
    gamma_weak_ref = 0.001
    gammas_base = solve_two_scale_model(mc_D5=M_c_D5_TARGET,
                                         mc_D7_over_D6=1.0,
                                         gamma_gauge=gamma_weak_ref)
    gamma_space_ref = gammas_base[0]

    # Topology-gap: γ_D6→D7 = γ_space × (8/3) relative scaling
    # Here we parameterize by the ratio dim(SU3)/dim(SU2) as suppression amplifier
    print(f"\n  γ_space = {gamma_space_ref:.6f}  (D1→D5)")
    print(f"  γ_weak  = {gamma_weak_ref:.6f}  (D5→D6, co-crystallization)")
    print(f"\n  D7 predictions for different γ_color values:")
    print(f"  {'γ_D6→D7':10s}  {'M_c(D7) GeV':14s}  {'log10(M_c7)':12s}  {'Physical scale'}")
    print(f"  {'─'*10}  {'─'*14}  {'─'*12}  {'─'*25}")

    alpha_D6 = mc_to_alpha(M_c_D5_TARGET) * (1 - gamma_weak_ref)

    # Also compute the α_s-constrained prediction for M_c(D7):
    # If SU(3) starts with equal coupling at M_c(D7) [α_s(M_c(D7)) = α_U],
    # then using SM running from M_Z:
    # 1/α_s(M_c7) = 1/α_s(M_Z) + (7/2π) ln(M_c7/M_Z)  →  M_c7 ~ 8×10^14 GeV
    # → implying M_c(D7) > M_c(D5/D6). This requires α_D7 > α_D6, which means
    #   D7 formed EARLIER (at higher compression depth, before D5/D6).
    # This reverses the naive depth ordering: SU(3) at D5, SU(2) at D6, U(1) at D7.
    # OR: D-depth ordering and energy ordering are independent — D-depth labels
    #     the bifurcation sequence, which may not coincide with energy ordering.
    alpha_s_mz = 0.118
    M_Z = 91.187
    alpha_U_from_D56 = (1.0 / (1.0/0.024))  # α_U at D5/D6 crossing ≈ 0.024
    # M_c(D7): solve 1/α_s(M_c7) = α_U^{-1}
    # 1/0.024 = 1/0.118 + (7/(2π)) ln(M_c7/91.187)
    # ln(M_c7/91.187) = 2π/7 × (1/0.024 - 1/0.118)
    log_mc7 = (2*math.pi/7) * (1/0.024 - 1/alpha_s_mz)
    M_c_D7_alphas_constraint = M_Z * math.exp(log_mc7)
    print(f"\n  Equal-coupling constraint on M_c(D7):")
    print(f"  If α_s(M_c(D7)) = α_U ≈ 0.024 [same initial condition as D5/D6],")
    print(f"  then M_c(D7) = {M_c_D7_alphas_constraint:.2e} GeV  (log10 = {math.log10(M_c_D7_alphas_constraint):.2f})")
    print(f"  This is ABOVE M_c(D5/D6) = 10^13 GeV → D7 formed before D5/D6")
    print(f"  (depth ordering ≠ energy ordering, OR D-depth labels are inverted)")

    for gamma_color in [0.0, gamma_weak_ref, gamma_space_ref/3, gamma_space_ref]:
        alpha_D7 = alpha_D6 * (1.0 - gamma_color)
        mc_D7 = alpha_to_mc(alpha_D7)
        if mc_D7 > 1e15:
            scale = "above GUT scale"
        elif mc_D7 > 1e12:
            scale = "~D5/D6 co-cryst range"
        elif mc_D7 > 1e9:
            scale = "intermediate"
        elif mc_D7 > 1e6:
            scale = "TeV-PeV range"
        elif mc_D7 > 1e2:
            scale = "GeV range"
        else:
            scale = "sub-GeV (confinement)"
        print(f"  {gamma_color:10.6f}  {mc_D7:14.3e}  {math.log10(mc_D7):12.2f}"
              f"  {scale}")

    # ── Constraint Summary ────────────────────────────────────────────────────
    print("\n" + "─" * 68)
    print("CONSTRAINT SUMMARY: What fixes the depth-running parameters?")
    print("─" * 68)
    print(f"""
  Known constraints on depth-running:
  Constraint                         DFC expression
  ---------------------------------  ----------------------------------------
  M_c(D1) = M_Pl                     alpha_D1 = 2 x M_Pl^2 (D1 anchor)
  M_c(D5) = M_c(D6) ~ 10^13 GeV     gamma_D5toD6 ~ 0, 4 steps from M_Pl
  sin2_W(M_Z) = 0.231                M_c(D5/D6) = 1.02e13 GeV
  F_pi = 93 MeV                      constrains alpha_D7/beta_D7
  v_Higgs = 246 GeV                  constrains eps x alpha_D6/beta_D6

  Free parameters:
    γ_space: single suppression per D1→D5 step → fixed by M_Pl ÷ M_c(D5)
    γ_weak:  D5→D6 suppression → must be ≈ 0 (co-crystallization)
    γ_color: D6→D7 suppression → OPEN; predicts M_c(D7)

  Two-scale model result (γ_weak = 0.001):
    γ_space = {gamma_space_ref:.6f}  per step
    M_c(D5) = {M_c_D5_TARGET:.3e} GeV  (input)
    M_c(D6) ≈ {M_c_D5_TARGET * (1 - gamma_weak_ref):.3e} GeV  (near D5, co-cryst ✓)
    M_c(D7) = depends on γ_color  [OPEN — next derivation target]

  The remaining open problem: derive γ_space and γ_color from the substrate
  mechanics (α, β, c) rather than fitting them to M_Pl and M_c(D5).
  This is the depth-running derivation problem.
""")

    # ── α_s status: the equal-coupling M_c(D7) estimate vs DFC prediction ──────
    print("\n" + "─" * 68)
    print("α_s STATUS: equal-coupling M_c(D7) estimate vs observed α_s(M_Z)")
    print("─" * 68)
    # DFC β-derived common coupling
    BETA_DFC = 0.0351
    g_common_sq = 8 * math.pi * BETA_DFC / 3.0
    alpha_common = g_common_sq / (4 * math.pi)   # ≈ 0.02340

    # Running formula: 1/α_s(M_Z) = 1/α_s(M_c) − (b₃/2π)×ln(M_c/M_Z)
    b3 = 7.0
    MC_D7_ESTIMATE = M_c_D7_alphas_constraint  # ≈ 8×10¹⁴ GeV (equal-coupling SM crossing)
    inv_alpha_mz = 1.0/alpha_common - (b3/(2*math.pi))*math.log(MC_D7_ESTIMATE/M_Z)
    alpha_s_current = 1.0/inv_alpha_mz if inv_alpha_mz > 0 else None

    # Target M_c(D7) for α_s = 0.1182
    alpha_s_obs = 0.1182
    inv_diff = 1.0/alpha_common - 1.0/alpha_s_obs
    ln_ratio = inv_diff / (b3/(2*math.pi))
    mc_target = M_Z * math.exp(ln_ratio)

    print(f"\n  β = {BETA_DFC} → g_common² = 8πβ/3 → α_common = {alpha_common:.5f}")
    print(f"  M_c(D7) from SM equal-coupling crossing:  {MC_D7_ESTIMATE:.2e} GeV")
    if alpha_s_current:
        err = 100*(alpha_s_current/alpha_s_obs - 1)
        print(f"  → α_s(M_Z) from this M_c(D7):  {alpha_s_current:.4f}  (error: {err:+.1f}%)")
        print(f"  ✗ 11% below observed 0.1182  — M_c(D7) estimate is too low")
    print(f"\n  Target M_c(D7) for α_s(M_Z) = 0.1182:  {mc_target:.3e} GeV")
    print(f"  Factor: {mc_target/MC_D7_ESTIMATE:.2f}× larger than current estimate")
    print(f"  γ_color required: produces M_c(D7) = {mc_target:.3e} GeV from M_c(D6)={M_c_D5_TARGET:.2e} GeV")
    if M_c_D5_TARGET > 0:
        alpha_D6_ref = mc_to_alpha(M_c_D5_TARGET)
        alpha_D7_target = mc_to_alpha(mc_target)
        if alpha_D7_target > alpha_D6_ref:
            print(f"  NOTE: α_D7_target ({alpha_D7_target:.2e}) > α_D6 ({alpha_D6_ref:.2e})")
            print(f"  This means D7 formed at HIGHER compression than D5/D6")
            print(f"  → D-depth label ordering and energy ordering differ at gauge depths")
    print(f"\n  See equations/alpha_s_target.py for full target analysis.")

    print("\n" + "─" * 68)
    print("CONCLUSION: Two-scale model (γ_space for spacetime, γ_weak ≈ 0 for")
    print("D5/D6 co-cryst) is self-consistent. γ_color is the remaining free")
    print("parameter. Deriving γ_space from (α, β, c) closes the derivation.")
    print("CRITICAL GAP: M_c(D7) target = 2.094×10¹⁵ GeV (not 8×10¹⁴ from SM")
    print("  crossing). The 11% α_s error traces to this M_c(D7) underestimate.")
