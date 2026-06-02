"""
Koide Step 4d: Canonical Phase Mode Coupling — Tier 2a Derivation
=================================================================

Physical question:
    Why does the off-diagonal Yukawa coupling Y_{nm} (n≠m) in the Koide circulant
    matrix have amplitude t = 1/√Q_top relative to the diagonal?

DFC mechanism:
    The three DFC fermion generations carry distinct Z₃ charges in the D5/D6 phase
    space. The collective coordinate action for the phase zero mode has kinetic term
    (1/2)g_θθ(∂θ)² with g_θθ = Q_top (proved Tier 1, Cycle 114). The vertex operator
    e^{iθ_phys}, when expressed in the canonical variable θ_can = √Q_top × θ_phys,
    has one-mode-insertion coefficient 1/√Q_top. The Z₃ charge difference between
    any two distinct generations is ±1 (mod 3), which requires exactly one phase
    mode insertion. Together these give t = |Y_nm|/Y_nn = 1/√Q_top = 1/√Q_top.

Key result (Cycle 146):
    t = 1/√Q_top = 1/√2 = 0.70710678  (exact, 0 free params, Tier 2a)
    K = 2/3  (from K = 1/3 + 2t²/3 = 1/3 + 2/(3Q_top) = 1/3 + 1/3 = 2/3)
    m_τ = 1776.97 MeV  (observed: 1776.86 MeV,  +0.006%, Tier 2a)

Derivation steps (all Tier 1 inputs):
    Step A — Moduli metric (Cycle 114, Tier 1):
        Collective coordinate action from DFC 5D complex scalar:
            S_CC = (1/2) g_XX ∫(∂X)² + (1/2) g_θθ ∫(∂θ)²
        with g_XX = I₄ = 4/3,  g_θθ = Q_top = 2  (both exact, error 0.00e+00)

    Step B — Canonical normalization:
        Physical phase θ_phys has kinetic term (1/2)Q_top(∂θ_phys)².
        Canonical field: θ_can = √Q_top × θ_phys
        Canonical kinetic term: (1/2)(∂θ_can)² ✓

    Step C — Vertex factor for e^{iθ_phys}:
        e^{iθ_phys} = exp(i × θ_can / √Q_top)
        Taylor expansion: = 1 + (i/√Q_top) θ_can + (i/√Q_top)² θ_can²/2! + ...
        Coefficient of θ_can^1 (one-mode term): i/√Q_top
        Amplitude for one canonical phase mode insertion: 1/√Q_top

    Step D — Z₃ charge counting:
        Three generations carry Z₃ charges q_n = 2πn/3, n = 0, 1, 2.
        Charge difference: Δq_{nm} = q_m - q_n = 2π(m-n)/3
        For n ≠ m: (m-n) mod 3 ∈ {1, 2}
            (m-n) = 1: Δq = +2π/3 = +γ  → one θ-mode insertion
            (m-n) = 2: Δq = +4π/3 = -2π/3 + 2π = -γ (mod 2π), equivalently -γ
                       → one θ†-mode insertion (conjugate), same amplitude 1/√Q_top
        For n = m: Δq = 0 → no phase mode → no suppression

        Counting: EXACTLY ONE phase mode insertion for ALL off-diagonal elements.
        No off-diagonal element requires zero or two insertions.

    Step E — Off-diagonal Yukawa amplitude:
        Y_nn = y⟨H⟩ × I₄  [no phase mode; direct overlap]
        Y_nm = y⟨H⟩ × I₄ × e^{iγ} × (1/√Q_top)  [one mode insertion]
        t = |Y_nm| / Y_nn = 1/√Q_top

Tier assignment: Tier 2a
    All inputs (Q_top, I₄, Z₃ from 3-gen, g_θθ from S_CC) are Tier 1.
    No free parameters; derivation is a consequence of the moduli metric.

References:
    - equations/kk_moduli_metric.py      (g_θθ = Q_top, Cycle 112, Tier 1)
    - equations/dfc_5d_action.py         (S_CC derivation, Cycle 114, Tier 1)
    - equations/koide_step4d_action.py   (selection rule, Cycle 138, Tier 3)
    - equations/koide_complex_circulant.py (Koide structure, Tier 1)
    - equations/tau_mass_koide.py        (m_τ from Koide, Cycle 138)
"""

import math


# ─── DFC substrate constants (all Tier 1) ─────────────────────────────────────
Q_TOP   = 2.0           # topological charge of kink, FTC, Cycle 114
I4      = 4.0 / 3.0     # Bogomolny integral ∫sech⁴du, Cycle 47
G_THTTH = Q_TOP         # moduli metric component g_θθ = Q_top, Cycle 112

# ─── Koide inputs (Tier 1) ────────────────────────────────────────────────────
M_E     = 0.51099895e-3  # GeV = 0.511 MeV
M_MU    = 0.105658375    # GeV = 105.658 MeV
GAMMA   = 2.0 * math.pi / 3.0  # Z₃ phase step = 2π/3

# ─── Observed ─────────────────────────────────────────────────────────────────
M_TAU_OBS = 1.77686      # GeV = 1776.86 MeV


def vertex_factor(g_theta_theta=G_THTTH):
    """
    Vertex factor for one canonical phase mode insertion.

    For kinetic term (1/2)g(∂θ)², canonical field θ_can = √g × θ_phys.
    The vertex e^{iθ_phys} = e^{iθ_can/√g}.
    Coefficient of θ_can^1 in Taylor expansion: i/√g.
    Amplitude magnitude for one insertion: 1/√g.
    """
    return 1.0 / math.sqrt(g_theta_theta)


def z3_charge_analysis():
    """
    Z₃ charge differences between three generations.
    Returns dict: {(n,m): (charge_diff_units, n_insertions)} for all pairs.
    """
    result = {}
    for n in range(3):
        for m in range(3):
            diff = (m - n) % 3  # charge difference in units of 2π/3
            if n == m:
                result[(n, m)] = (0, 0)   # diagonal: no phase mode
            elif diff == 1:
                result[(n, m)] = (1, 1)   # +γ: one mode
            elif diff == 2:
                result[(n, m)] = (-1, 1)  # -γ: one conjugate mode (same amplitude)
    return result


def yukawa_ratio(g_theta_theta=G_THTTH):
    """
    t = |Y_nm| / Y_nn for n ≠ m.
    From vertex factor: 1/√g_θθ.
    """
    return vertex_factor(g_theta_theta)


def koide_K(t_sq=None):
    """
    Koide sum constant from t.
    K = (1/3) + (2/3) t²
    For t² = 1/Q_top: K = 1/3 + 2/(3Q_top) = 1/3 + 1/3 = 2/3 (exact)
    """
    if t_sq is None:
        t_sq = 1.0 / Q_TOP
    return 1.0/3.0 + (2.0/3.0) * t_sq


def koide_tau_mass(me=M_E, mmu=M_MU, K=None):
    """
    Predict m_τ from Koide sum rule:
        K = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3

    Solving for m_τ: let x = √m_τ, a = √m_e + √m_μ, S = m_e + m_μ.
        S + x² = K × (a + x)²
        S + x² = K(a² + 2ax + x²)
        (K-1)x² + 2Kax + Ka² - S = 0

    For K = 2/3:
        x² - 4ax + (3S - 2a²) = 0  [multiply through by -3/(K-1) = 3]
        x = 2a ± √(6a² - 3S)

    Physical solution: x = 2a + √(6a² - 3S)  [larger root gives m_τ >> m_μ]
    """
    if K is None:
        K = koide_K()
    sqe  = math.sqrt(me)
    sqmu = math.sqrt(mmu)
    a = sqe + sqmu
    S = me + mmu
    # General quadratic: (K-1)x² + 2Kax + (Ka² - S) = 0
    A = K - 1.0
    B = 2.0 * K * a
    C = K * a**2 - S
    discriminant = B**2 - 4.0 * A * C
    if discriminant < 0:
        raise ValueError("Negative discriminant — check K value.")
    sqrt_disc = math.sqrt(discriminant)
    x1 = (-B + sqrt_disc) / (2.0 * A)
    x2 = (-B - sqrt_disc) / (2.0 * A)
    # Physical solution: x = √m_τ > 0 and m_τ > m_μ
    candidates = [x for x in [x1, x2] if x > 0]
    x = max(candidates)
    return x**2


if __name__ == "__main__":
    print()
    print("=" * 70)
    print("  KOIDE STEP 4d — CANONICAL PHASE MODE COUPLING  (Cycle 146)")
    print("  Selection rule t = 1/√Q_top from collective coordinate action")
    print("=" * 70)
    print()

    # ─── Step A: Moduli metric ─────────────────────────────────────────────────
    print("─" * 70)
    print("STEP A — Moduli metric (Tier 1, Cycle 114)")
    print("─" * 70)
    print(f"  S_CC = (1/2) g_XX ∫(∂X)² + (1/2) g_θθ ∫(∂θ)²")
    print(f"  g_XX = I₄    = {I4:.8f}   [Bogomolny integral, Tier 1]")
    print(f"  g_θθ = Q_top = {Q_TOP:.8f}   [topological charge, FTC, Tier 1]")
    print()

    # ─── Step B: Canonical normalization ──────────────────────────────────────
    print("─" * 70)
    print("STEP B — Canonical normalization")
    print("─" * 70)
    print(f"  Kinetic term: (1/2) Q_top (∂θ_phys)²  with Q_top = {Q_TOP}")
    print(f"  Canonical field: θ_can = √Q_top × θ_phys = {math.sqrt(Q_TOP):.8f} × θ_phys")
    print(f"  In terms of θ_can: kinetic term = (1/2)(∂θ_can)²  ✓")
    print()

    # ─── Step C: Vertex factor ─────────────────────────────────────────────────
    print("─" * 70)
    print("STEP C — Vertex factor for e^{iθ_phys}")
    print("─" * 70)
    vf = vertex_factor()
    print(f"  e^{{iθ_phys}} = exp(i × θ_can / √Q_top)")
    print(f"              = Σ_n (i/√Q_top)^n × θ_can^n / n!")
    print(f"  Coefficient of θ_can^1 (one-mode term):  i/√Q_top")
    print(f"  |Amplitude for one canonical θ_can insertion|  = 1/√Q_top")
    print(f"  = 1/√{Q_TOP:.0f} = {vf:.8f}")
    print()

    # ─── Step D: Z₃ charge counting ───────────────────────────────────────────
    print("─" * 70)
    print("STEP D — Z₃ charge counting for three generations")
    print("─" * 70)
    charges = z3_charge_analysis()
    print(f"  Z₃ phase step γ = 2π/3 = {GAMMA:.6f} rad")
    print(f"  {'(n,m)':<8} {'charge diff':<14} {'insertions':<12} {'type'}")
    print(f"  {'-'*8} {'-'*14} {'-'*12} {'-'*20}")
    for (n, m), (diff, ins) in sorted(charges.items()):
        if n == m:
            kind = "diagonal — no phase mode"
        elif diff == 1:
            kind = "off-diag — one θ insertion"
        else:
            kind = "off-diag — one θ† insertion"
        diff_str = f"{diff:+d} × γ"
        print(f"  ({n},{m})     {diff_str:<14} {ins:<12} {kind}")
    print()
    all_offdiag_count = {v[1] for (n,m),v in charges.items() if n != m}
    print(f"  All off-diagonal elements: {all_offdiag_count} phase mode insertion(s) — EXACTLY ONE.")
    print(f"  (For (m-n)=2 mod 3: charge = -γ, equivalent to conjugate insertion;")
    print(f"   same amplitude 1/√Q_top by unitarity.)")
    print()

    # ─── Step E: Yukawa ratio t ────────────────────────────────────────────────
    print("─" * 70)
    print("STEP E — Off-diagonal Yukawa amplitude t = 1/√Q_top")
    print("─" * 70)
    t = yukawa_ratio()
    t_sq = t**2
    K    = koide_K(t_sq)
    print(f"  Y_nn  = y⟨H⟩ × I₄             [direct, no phase mode]")
    print(f"  Y_nm  = y⟨H⟩ × I₄ × e^{{iγ}} × (1/√Q_top)  [one insertion]")
    print(f"  t     = |Y_nm| / Y_nn = 1/√Q_top = {t:.8f}")
    print(f"  t²    = 1/Q_top       = 1/{Q_TOP:.0f} = {t_sq:.8f}")
    print(f"  K     = 1/3 + 2t²/3  = 1/3 + 2/(3×{Q_TOP:.0f}) = {K:.8f}")
    K_exact = 2.0/3.0
    print(f"  K_exact = 2/3         = {K_exact:.8f}   [exact: Tier 1]")
    print(f"  |K - 2/3|             = {abs(K - K_exact):.2e}   [numerical error]")
    print()

    # ─── Tau mass prediction ───────────────────────────────────────────────────
    print("─" * 70)
    print("TAU MASS PREDICTION")
    print("─" * 70)
    m_tau_pred = koide_tau_mass()
    m_tau_mev  = m_tau_pred * 1e3
    m_tau_obs_mev = M_TAU_OBS * 1e3
    err = 100.0 * (m_tau_pred - M_TAU_OBS) / M_TAU_OBS
    print(f"  Inputs:")
    print(f"    m_e   = {M_E*1e3:.5f} MeV  [PDG, Tier 1 input]")
    print(f"    m_μ   = {M_MU*1e3:.3f} MeV  [PDG, Tier 1 input]")
    print(f"    K     = 2/3  [DFC, 0 free params, Tier 2a]")
    print(f"  Prediction:")
    print(f"    m_τ   = {m_tau_mev:.2f} MeV   (obs: {m_tau_obs_mev:.2f} MeV,  err: {err:+.3f}%)")
    print()

    # ─── Derivation chain summary ──────────────────────────────────────────────
    print("=" * 70)
    print("DERIVATION CHAIN — Steps 0 through 4d (complete)")
    print("=" * 70)
    print()
    print("  Step 0: g_XX = I₄, g_θθ = Q_top (moduli metric, Cycle 112, Tier 1)")
    print("  Step 1: Direct coupling → t=1 for ANY Higgs profile (proved Tier 1)")
    print("  Step 2: Odd Higgs (ψ=tanh) → Y=0, cannot mediate (proved Tier 1)")
    print("  Step 3: Z₃ symmetry → circulant Yukawa matrix (Cycle 124, Tier 1)")
    print("  Step 4a: γ = 2π/3 from Z₃ (Tier 1)")
    print("  Step 4b: K = 1/3 + 2t²/3 from Koide structure (Tier 1)")
    print("  Step 4c: K = 2/3 ↔ t² = 1/Q_top (Tier 1)")
    print("  Step 4d: t = 1/√Q_top from canonical phase vertex factor")
    print("           (THIS MODULE — Tier 2a derivation, Cycle 146)")
    print()
    chain_status = [
        ("Steps 0–3",  "Tier 1",  "from V(φ)"),
        ("Step 4a–4c", "Tier 1",  "from Koide structure + Z₃"),
        ("Step 4d",    "Tier 2a", "canonical phase vertex factor (Cycle 146)"),
    ]
    print(f"  {'Steps':<14} {'Tier':<10} {'Basis'}")
    print(f"  {'-'*14} {'-'*10} {'-'*38}")
    for name, tier, basis in chain_status:
        print(f"  {name:<14} {tier:<10} {basis}")
    print()
    print(f"  CONCLUSION: m_τ = {m_tau_mev:.2f} MeV  (+{abs(err):.3f}%,  0 free params, Tier 2a)")
    print()
    print("  Free parameters: ZERO")
    print("  All inputs (Q_top, I₄, m_e, m_μ) from Tier 0/1 — no adjustable inputs.")
    print("  (m_e and m_μ are SM measurements used as boundary conditions,")
    print("   same status as α_s in the ECCC prediction chain.)")
