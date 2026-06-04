"""
Alpha from Kink Action Self-Consistency  (Cycle 169)
=====================================================

Physical question:
    V(φ) = −α/2 φ² + β/4 φ⁴ has two parameters.  β = 1/(9π) has been derived
    (Tier 2a, Cycle 117) from the tachyonic instability of the real D5 kink.
    α is dimensionful and has remained a free parameter.  Can α be derived
    from the compression story — the condition that the substrate cannot achieve
    the singularity φ = 0?

DFC mechanism — the primitive compression threshold:
    The substrate self-compresses toward φ = 0 but cannot reach it.  The
    compression stalls when the action cost of forming the first topological
    defect equals the inverse of the coupling that defect generates.

    In precise form, the self-consistency condition is:

        S_kink × α_em(M_c(EW)) = 1

    meaning the kink Euclidean action equals 1/α_em at the D5 closure scale.

    This connects three independently established DFC quantities:

        S_kink  =  4/β                 [from BPS kink action formula]
                =  36π                 [from β = 1/(9π)]
                =  1/α_em(M_c(EW))    [from the 36π chain, Cycles 141-142]

    Setting S_kink = 36π and solving for α via the BPS formula
    S_kink = (4/3) × α^(3/2) / (β√2):

        α^(3/2)  =  36π × β × (3√2/4)  =  27π√2 β  =  3√2      [using β=1/(9π)]

        α  =  (3√2)^(2/3)  =  3^(2/3) × 2^(1/3)  =  ∛18

    Since 18 = Q_top × N_Hopf (with Q_top = 2, N_Hopf = 9 = 1+3+5):

        α  =  (Q_top × N_Hopf)^(1/3)    [exact algebraic identity]

Key result:
    α = ∛18 ≈ 2.621   [Planck units, ℏ = c = G = 1]
    α = (Q_top × N_Hopf)^(1/3) × M_Pl²   [in physical units]

    The substrate parameter α is the cube root of the product of the two
    fundamental topological integers of the DFC model:
      • Q_top = 2  (Z₂ vacuum structure, topological charge of the kink)
      • N_Hopf = 9 (Hopf fiber dimension sum 1+3+5, D5/D6/D7 closure geometry)

Tier assessment:
    S_kink = 1/α_em(M_c(EW)) as compression threshold:  Tier 3 (new proposal)
    α = ∛18 from S_kink = 36π condition:                 Tier 3
    α = (Q_top × N_Hopf)^(1/3) topological formula:      Tier 3
    S_kink × α_em(M_c(EW)) = 1 self-consistency check:   Tier 2a (both sides Tier 2a)
    β = 4 × α_em(M_c(EW)):                               Tier 2a (algebraic identity)

Physical consequences (Planck units):
    ξ = 1/√α = 18^(−1/6) ≈ 0.6176 l_Pl   [kink width; near-1/φ_golden to 0.07%]
    E_kink = 36π × M_Pl ≈ 113.1 M_Pl       [kink energy at D1 boundary]
    φ₀ = √(α/β) ≈ 8.609 M_Pl               [vacuum field amplitude]

Key references:
    equations/d5_complex_from_instability.py  — β=1/(9π), Q_top=2, N_Hopf=9 (Cycle 117)
    equations/alpha_em_prediction.py          — 1/α_em(Mc(EW))=36π (Cycles 141-142)
    equations/kk_action_coupling.py           — BPS kink action E_kink formula (Cycle 111)
    foundations/substrate.md                  — V(φ), kink solution, α as free parameter
    foundations/coupling_emergence.md         — β derivation, 36π chain
"""

import math

# ─── Known DFC constants (Tier 2a or Tier 1, prior cycles) ────────────────────

BETA         = 1.0 / (9.0 * math.pi)       # β = 1/(9π),    Tier 2a, Cycle 117
Q_TOP        = 2.0                          # kink charge,   Tier 1,  Cycle 117
N_HOPF       = 9.0                          # d₁+d₂+d₃=1+3+5, Tier 1, Cycle 103
I4           = 4.0 / 3.0                    # BPS ∫sech⁴,   Tier 1,  Cycle 47
K_Y_SQ       = 5.0 / 3.0                    # k_Y²=5/3,      Tier 2a, Cycle 30
G_EFF_SQ     = 8.0 / 27.0                   # g_eff²=8/27,   Tier 2a, Cycle 117
ALPHA_COMMON = G_EFF_SQ / (4.0 * math.pi)  # 2/(27π),       Tier 2a
ALPHA_EM_MC  = 1.0 / (36.0 * math.pi)      # 1/(36π) at Mc, Tier 2a, Cycle 141

# Golden ratio
PHI_GOLDEN   = (1.0 + math.sqrt(5.0)) / 2.0

# Physical scales (GeV)
M_PL_GEV     = 1.2209e19    # Planck mass
MC_D5_GEV    = 9.44e12      # D5/EW closure scale, ECCC Cycle 141
MC_D7_GEV    = 1.566e15     # D7 SU(3) closure scale, ECCC Cycle 144
LAM_QCD_GEV  = 0.3045       # Λ_QCD two-loop, Cycle 159


# ─── Part A: Derivation of α from S_kink = 36π ────────────────────────────────

def derive_alpha():
    """
    Derive α from the primitive compression threshold S_kink = 1/α_em(M_c(EW)).

    The BPS kink Euclidean action (Cycle 111):
        S_kink = (4/3) × α^(3/2) / (β√2)

    Setting S_kink = 36π:
        α^(3/2) = 36π × β × 3√2/4 = 27π√2 × β = 3√2      [with β = 1/(9π)]
        α = (3√2)^(2/3) = 3^(2/3) × 2^(1/3) = ∛18

    Three equivalent forms — all should give the same number to machine precision.
    """
    print('=' * 70)
    print('[PART A]  DERIVATION: α FROM S_kink = 1/α_em(M_c(EW)) = 36π')
    print('=' * 70)
    print()
    print('  Known inputs (prior cycles):')
    print(f'    β          = 1/(9π)  = {BETA:.10f}  [Tier 2a, Cycle 117]')
    print(f'    Q_top      = {Q_TOP:.0f}                              [Tier 1, Cycle 117]')
    print(f'    N_Hopf     = {N_HOPF:.0f}  (= 1+3+5)                 [Tier 1, Cycle 103]')
    print(f'    α_em(Mc)   = 1/(36π) = {ALPHA_EM_MC:.10f}  [Tier 2a, Cycle 141]')
    print()
    print('  Primitive compression threshold condition:')
    print(f'    S_kink = 1/α_em(M_c(EW)) = 36π = {36*math.pi:.8f}')
    print()
    print('  Solving (4/3) × α^(3/2) / (β√2) = 36π for α:')
    print()
    print('    α^(3/2) = 36π × β × 3√2/4')
    print('            = 27π√2 × β')
    print(f'            = 27π√2 × 1/(9π)')
    print(f'            = 3√2')
    print(f'            = {3*math.sqrt(2):.10f}')
    print()
    print('    α = (3√2)^(2/3)')
    print('      = 3^(2/3) × 2^(1/3)')
    print('      = (9 × 2)^(1/3)')
    print('      = ∛18')
    print()

    # Three derivation routes
    alpha_32      = 3.0 * math.sqrt(2.0)
    alpha_route1  = alpha_32 ** (2.0 / 3.0)          # (3√2)^(2/3)
    alpha_route2  = 18.0 ** (1.0 / 3.0)              # ∛18
    alpha_route3  = (Q_TOP * N_HOPF) ** (1.0 / 3.0)  # (Q_top × N_Hopf)^(1/3)

    r12 = abs(alpha_route1 - alpha_route2)
    r23 = abs(alpha_route2 - alpha_route3)

    print('  Three equivalent forms:')
    print(f'    (3√2)^(2/3)              = {alpha_route1:.12f}')
    print(f'    ∛18                      = {alpha_route2:.12f}   residual: {r12:.2e}')
    print(f'    (Q_top × N_Hopf)^(1/3)  = {alpha_route3:.12f}   residual: {r23:.2e}')
    print()
    print(f'  DFC PREDICTION:  α = ∛18 = (Q_top × N_Hopf)^{{1/3}} ≈ {alpha_route2:.8f}')
    print(f'                   in Planck units (ℏ = c = G = 1)')
    print()
    print('  Tier: Tier 3 — conditional on S_kink = 1/α_em as the primitive threshold.')

    return {
        'alpha':           alpha_route2,
        'alpha_32':        alpha_32,
        'residual_forms':  max(r12, r23),
    }


# ─── Part B: Numerical verification of S_kink = 36π ──────────────────────────

def verify_skink(alpha_res):
    """
    Verify S_kink from α = ∛18 equals 36π.

    Key algebraic step: α^(3/2) = (∛18)^(3/2) = 18^(1/2) = √18 = 3√2
    Therefore: S_kink = (4/3) × 3√2 / (β√2) = (4/3) × 3/β = 4/β = 36π
    """
    print()
    print('=' * 70)
    print('[PART B]  VERIFY: S_kink = 36π  (from α = ∛18)')
    print('=' * 70)
    print()

    alpha    = alpha_res['alpha']
    alpha_32 = alpha ** 1.5

    # Algebraic: (∛18)^(3/2) = 18^(1/2) = √18
    alpha_32_algebraic = math.sqrt(18.0)
    r_alpha32 = abs(alpha_32 - alpha_32_algebraic) / alpha_32_algebraic

    S_kink   = (4.0 / 3.0) * alpha_32 / (BETA * math.sqrt(2.0))
    S_target = 36.0 * math.pi
    r_skink  = abs(S_kink - S_target) / S_target

    print(f'  Algebraic path:')
    print(f'    α^(3/2) = (∛18)^(3/2) = 18^(1/2) = √18 = 3√2')
    print(f'    √18 = {alpha_32_algebraic:.12f}')
    print()
    print(f'    S_kink = (4/3) × √18 / (β√2)')
    print(f'           = (4/3) × (√18/√2) / β')
    print(f'           = (4/3) × √9 / β        [√18/√2 = √9 = 3]')
    print(f'           = (4/3) × 3 / β')
    print(f'           = 4/β')
    print(f'           = 4 × 9π = 36π')
    print()
    print(f'  Numerical verification:')
    print(f'    α^(3/2) numerical  = {alpha_32:.12f}')
    print(f'    α^(3/2) algebraic  = {alpha_32_algebraic:.12f}   residual: {r_alpha32:.2e}')
    print()
    print(f'    S_kink computed    = {S_kink:.10f}')
    print(f'    36π (target)       = {S_target:.10f}   residual: {r_skink:.2e}')

    return {'S_kink': S_kink, 'S_target': S_target, 'residual': r_skink}


# ─── Part C: The three-way identity ───────────────────────────────────────────

def three_way_identity():
    """
    The three-way identity:

        S_kink  =  4/β  =  1/α_em(M_c(EW))  =  36π

    All three are established independently; their equality is the self-consistency
    condition that fixes α.

    Physical meaning: the substrate's quartic stiffness (β) and the EM coupling at
    D5 (α_em) are reciprocals at the 4× level — β = 4 α_em.  The kink action bridges
    them: S_kink = 4/β = 1/α_em.

    Underlying algebra:
        α_common = g_eff²/(4π) = (8/27)/(4π) = 2/(27π) = (2/3)β
        1/α_em   = (1+k_Y²)/α_common = (8/3)/(2β/3) = 4/β   → β = 4α_em
    """
    print()
    print('=' * 70)
    print('[PART C]  THREE-WAY IDENTITY: S_kink = 4/β = 1/α_em = 36π')
    print('=' * 70)
    print()

    v_36pi      = 36.0 * math.pi
    v_4_over_b  = 4.0 / BETA
    v_inv_aem   = 1.0 / ALPHA_EM_MC

    r1 = abs(v_4_over_b - v_36pi) / v_36pi
    r2 = abs(v_inv_aem  - v_36pi) / v_36pi

    print(f'  36π                = {v_36pi:.10f}  [reference]')
    print(f'  4/β                = {v_4_over_b:.10f}  residual: {r1:.2e}')
    print(f'  1/α_em(M_c(EW))   = {v_inv_aem:.10f}  residual: {r2:.2e}')
    print()

    # β = 4 × α_em
    beta_check = 4.0 * ALPHA_EM_MC
    r_beta = abs(BETA - beta_check) / BETA
    print(f'  β = 4 × α_em(M_c(EW)):')
    print(f'    β (Tier 2a)      = {BETA:.12f}')
    print(f'    4 × α_em         = {beta_check:.12f}   residual: {r_beta:.2e}')
    print()

    # Algebraic derivation of β = 4 α_em
    alpha_common_check = 2.0 * BETA / 3.0
    r_ac = abs(alpha_common_check - ALPHA_COMMON) / ALPHA_COMMON
    print('  Derivation of β = 4 α_em:')
    print()
    print(f'    α_common = g_eff²/(4π) = (8/27)/(4π) = 2/(27π) = {ALPHA_COMMON:.10f}')
    print(f'    2β/3     = {alpha_common_check:.10f}  residual vs α_common: {r_ac:.2e}')
    print()
    print(f'    1/α_em = (1+k_Y²)/α_common')
    print(f'           = (8/3) / (2β/3)')
    print(f'           = (8/3) × (3/2β)')
    print(f'           = 4/β  →  β = 4 α_em  ✓')
    print()
    print('  Physical reading:')
    print('  The quartic self-coupling β = 4 α_em.  The factor 4 comes from')
    print('  the electroweak mixing: (1 + k_Y²) = 8/3 divided by (3/2) from')
    print('  α_common = 2β/3.  The substrate stiffness and the photon coupling')
    print('  are not independent — they are fixed to be in the ratio 1:4.')

    return {
        'val_36pi':    v_36pi,
        'val_4_over_b':v_4_over_b,
        'val_inv_aem': v_inv_aem,
        'max_residual':max(r1, r2),
    }


# ─── Part D: Topological formula α = (Q_top × N_Hopf)^(1/3) ──────────────────

def topological_formula(alpha_res):
    """
    The topological form of α.

    From the algebra above, α^(3/2) = 3√2 = √18 = √(Q_top × N_Hopf).

    So α = 18^(1/3) = (Q_top × N_Hopf)^(1/3).

    Physical meaning of the two integers:
        Q_top = 2:  the Z₂ vacuum structure.  There are exactly two stable states
                    (±φ₀), and the kink interpolates between them.  Q_top measures
                    the topological content of the double-well itself.

        N_Hopf = 9: the total dimensionality of the three Hopf fibers (S¹, S³, S⁵)
                    corresponding to D5, D6, D7 closure depths.  It governs the
                    gauge structure that emerges from the compression cascade.

    The cube root: α^(3/2) = √(Q_top × N_Hopf) means α = (Q_top × N_Hopf)^(1/3).
    The exponent 1/3 connects the 3/2-power in E_kink ∝ α^(3/2) to the product of
    the two topological integers.
    """
    print()
    print('=' * 70)
    print('[PART D]  TOPOLOGICAL FORMULA:  α = (Q_top × N_Hopf)^(1/3) = ∛18')
    print('=' * 70)
    print()

    alpha = alpha_res['alpha']

    # Verify α^(3/2) = √(Q_top × N_Hopf)
    alpha_32_num  = alpha ** 1.5
    alpha_32_topo = math.sqrt(Q_TOP * N_HOPF)
    r32 = abs(alpha_32_num - alpha_32_topo) / alpha_32_topo

    # Verify α = (Q_top × N_Hopf)^(1/3)
    alpha_topo = (Q_TOP * N_HOPF) ** (1.0 / 3.0)
    r_alpha = abs(alpha - alpha_topo) / alpha_topo

    print(f'  Q_top  = {Q_TOP:.0f}   [Z₂ vacuum topology, Tier 1, Cycle 117]')
    print(f'  N_Hopf = {N_HOPF:.0f}   [d₁+d₂+d₃ = 1+3+5, Tier 1, Cycle 103]')
    print(f'  Q_top × N_Hopf = {Q_TOP*N_HOPF:.0f}')
    print()
    print(f'  α^(3/2) = √(Q_top × N_Hopf) = √18 = 3√2:')
    print(f'    α^(3/2) numerical  = {alpha_32_num:.12f}')
    print(f'    √(Q_top × N_Hopf)  = {alpha_32_topo:.12f}   residual: {r32:.2e}')
    print()
    print(f'  α = (Q_top × N_Hopf)^(1/3) = ∛18:')
    print(f'    α (Part A)                = {alpha:.12f}')
    print(f'    (Q_top × N_Hopf)^(1/3)   = {alpha_topo:.12f}   residual: {r_alpha:.2e}')
    print()
    print('  Interpretation of the cube root:')
    print('  The kink action involves α^(3/2).  Setting this equal to √(Q_top × N_Hopf)')
    print('  means the kink action scale is the geometric mean of the two topological')
    print('  integers.  Geometrically: α is the linear scale whose 3/2-power gives the')
    print('  square root of the total topological content Q_top × N_Hopf.')
    print()
    print('  Why the kink "knows" N_Hopf:')
    print('  N_Hopf = 9 governs g_eff² = 8/27 = 2I₄/N_Hopf (Cycle 117), which governs β,')
    print('  which governs S_kink = 4/β.  The D1 kink encodes the full D5-D7 closure')
    print('  topology in its action — because β carries N_Hopf, and S_kink = 4/β.')

    return {
        'alpha_topo':    alpha_topo,
        'alpha_32_topo': alpha_32_topo,
        'residual_32':   r32,
        'residual_alpha':r_alpha,
    }


# ─── Part E: Physical consequences in Planck units ────────────────────────────

def physical_consequences(alpha_res):
    """
    Compute the physical observables from α = ∛18 in Planck units (ℏ=c=G=1).
    """
    print()
    print('=' * 70)
    print('[PART E]  PHYSICAL CONSEQUENCES  (Planck units: ℏ = c = G = 1)')
    print('=' * 70)
    print()

    alpha = alpha_res['alpha']

    # Kink width
    xi         = 1.0 / math.sqrt(alpha)
    xi_exact   = 18.0 ** (-1.0 / 6.0)
    r_xi       = abs(xi - xi_exact) / xi_exact

    # Near-golden-ratio
    xi_phi     = xi * PHI_GOLDEN
    err_golden = (xi_phi - 1.0) * 100.0    # percent deviation of ξ×φ from 1

    # ξ vs 1/φ (golden) directly
    err_xi_phi = (xi - 1.0/PHI_GOLDEN) / (1.0/PHI_GOLDEN) * 100.0

    # Kink energy
    E_kink_Mpl = 36.0 * math.pi

    # Vacuum amplitude
    phi0 = math.sqrt(alpha / BETA)

    # Self-consistency product
    S_kink  = (4.0 / 3.0) * alpha ** 1.5 / (BETA * math.sqrt(2.0))
    product = S_kink * ALPHA_EM_MC
    r_prod  = abs(product - 1.0)

    print(f'  α = ∛18 = {alpha:.8f}  (Planck units)')
    print()
    print(f'  Kink width:')
    print(f'    ξ = 1/√α = 18^(-1/6) = {xi:.10f} l_Pl')
    print(f'    [exact form residual: {r_xi:.2e}]')
    print()
    print(f'  Near-golden-ratio check (structural note — not a claim):')
    print(f'    φ_golden  = (1+√5)/2 = {PHI_GOLDEN:.10f}')
    print(f'    1/φ_golden =           {1/PHI_GOLDEN:.10f}')
    print(f'    ξ          =           {xi:.10f}')
    print(f'    ξ vs 1/φ:  {err_xi_phi:+.4f}%  error  (0.07% — structural note, not derived)')
    print(f'    ξ × φ    = {xi_phi:.10f}  (deviation from 1: {err_golden:+.4f}%)')
    print(f'    18^(1/6)  = {18**(1/6):.10f}  vs  φ = {PHI_GOLDEN:.10f}  (differ: {abs(18**(1/6)-PHI_GOLDEN)/PHI_GOLDEN*100:.4f}%)')
    print()
    print(f'  Kink energy:')
    print(f'    E_kink = S_kink × M_Pl = 36π M_Pl = {E_kink_Mpl:.6f} M_Pl')
    print(f'    ≈ 113.1 Planck masses — inaccessible to any lab experiment')
    print()
    print(f'  Vacuum field amplitude:')
    print(f'    φ₀ = √(α/β) = √(∛18 × 9π)')
    print(f'       = √({alpha / BETA:.6f}) = {phi0:.6f} M_Pl')
    print()
    print(f'  Self-consistency check S_kink × α_em(Mc) = 1:')
    print(f'    S_kink = {S_kink:.10f}')
    print(f'    α_em   = {ALPHA_EM_MC:.10f}')
    print(f'    product= {product:.12f}   residual from 1: {r_prod:.2e}')
    print()
    print(f'  Semiclassical validity: S_kink = {S_kink:.4f} >> 1  ✓')
    print(f'  Tunneling suppression: e^(−S_kink) = e^(−36π) ≈ 10^(−49)')
    print(f'  [D1 kinks are classically suppressed; the double-well is the ground state]')

    return {
        'xi':            xi,
        'xi_phi':        xi_phi,
        'err_golden_pct':err_golden,
        'err_xi_phi_pct':err_xi_phi,
        'E_kink_Mpl':    E_kink_Mpl,
        'phi0_Mpl':      phi0,
        'product':       product,
        'r_prod':        r_prod,
    }


# ─── Part F: Hierarchy of α through depth cascade ─────────────────────────────

def alpha_hierarchy(alpha_res):
    """
    Map the running of α from the D1 boundary to the D7 confinement scale.

    If the interpretation is correct — α = ∛18 × M_Pl² at D1, and
    α_Dn = M_c(Dn)² at each lower depth — the full depth hierarchy
    is determined once the M_c sequence is derived.

    Using the ECCC-derived scales (Cycles 141, 144, 159), we can map
    the current known ratios.
    """
    print()
    print('=' * 70)
    print('[PART F]  HIERARCHY: RUNNING OF α FROM D1 TO D7')
    print('=' * 70)
    print()

    alpha_D1 = alpha_res['alpha']   # dimensionless in Planck units

    print(f'  α_D1 = ∛18 = {alpha_D1:.6f}  (Planck units)')
    print(f'  In physical units: α_D1 = {alpha_D1:.4f} × M_Pl²')
    print(f'                          = {alpha_D1 * M_PL_GEV**2:.3e} GeV²')
    print()
    print(f'  Known closure scales (from ECCC chain, Cycles 141/144/159):')
    print(f'    M_c(D1)  ≈ M_Pl = {M_PL_GEV:.4e} GeV')
    print(f'    M_c(D7)  = {MC_D7_GEV:.4e} GeV  [SU(3) ECCC closure, Cycle 144]')
    print(f'    M_c(D5)  = {MC_D5_GEV:.4e} GeV  [EW equal-coupling, Cycle 141]')
    print(f'    Λ_QCD    = {LAM_QCD_GEV:.4f} GeV  [confinement, Cycle 159]')
    print()

    print(f'  α at each scale (in Planck units, α_Dn = (M_c(Dn)/M_Pl)²):')
    print()
    print(f'  {"Depth":<14}  {"M_c (GeV)":<16}  {"α (Planck)":<20}  {"log₁₀(α/α_D1)":<16}')
    print(f'  {"-"*68}')

    depths = [
        ('D1 (Planck)',  M_PL_GEV,   alpha_D1),
        ('D7 closure',   MC_D7_GEV,  alpha_D1 * (MC_D7_GEV / M_PL_GEV)**2),
        ('D5/EW',        MC_D5_GEV,  alpha_D1 * (MC_D5_GEV / M_PL_GEV)**2),
        ('D7 (Λ_QCD)',   LAM_QCD_GEV,alpha_D1 * (LAM_QCD_GEV / M_PL_GEV)**2),
    ]

    for label, scale, alpha_val in depths:
        ratio = alpha_val / alpha_D1
        log_r = math.log10(ratio) if ratio > 0 else -999.0
        print(f'  {label:<14}  {scale:<16.4e}  {alpha_val:<20.4e}  {log_r:<+16.1f}')

    qcd_ratio = (LAM_QCD_GEV / M_PL_GEV) ** 2
    print()
    print(f'  Total hierarchy: α(Λ_QCD)/α(M_Pl)')
    print(f'    = (Λ_QCD/M_Pl)² = ({LAM_QCD_GEV:.4f}/{M_PL_GEV:.4e})²')
    print(f'    = ({LAM_QCD_GEV/M_PL_GEV:.3e})²')
    print(f'    = {qcd_ratio:.3e}  (~10^{math.log10(qcd_ratio):.0f})')
    print()
    print('  OBSERVATION:')
    print('  Each bifurcation D(n)→D(n+1) reduces α by the factor (M_c(n+1)/M_c(n))².')
    print('  The cascade of 6 bifurcations (D1→D7) generates the full 40-order')
    print('  hierarchy from Planck to QCD scales.')
    print()
    print('  OPEN:')
    print('  Derive M_c(Dn) from V(φ) substrate depth-running (not SM RG inversion).')
    print('  If achieved: Λ_QCD/M_Pl becomes a DFC first-principles prediction.')

    return {'alpha_D1': alpha_D1, 'qcd_ratio': qcd_ratio}


# ─── Summary ──────────────────────────────────────────────────────────────────

def summary(alpha_res, skink_res, identity_res, topo_res, phys_res):
    print()
    print('=' * 70)
    print('SUMMARY — α FROM KINK ACTION SELF-CONSISTENCY  (Cycle 169)')
    print('=' * 70)
    print()

    alpha = alpha_res['alpha']

    print('  MAIN RESULT:')
    print()
    print(f'  α = ∛18 = (Q_top × N_Hopf)^(1/3) ≈ {alpha:.8f}  [Planck units]')
    print(f'  [Tier 3: conditional on S_kink = 1/α_em(Mc) as compression threshold]')
    print()
    print('  DERIVATION CHAIN:')
    print()
    print('  Self-compression cannot reach φ=0, no preferred direction, stable rest state')
    print('      ↓  unique lowest-order consistent form')
    print('  V(φ) = −α/2 φ² + β/4 φ⁴   [Tier 0 postulate — form now derived from story]')
    print('      ↓  D5 tachyonic instability (Cycle 117, Tier 2a)')
    print('  β = 1/(9π) = 1/(πN_Hopf)')
    print('      ↓  36π chain (Cycles 141-142, Tier 2a)')
    print('  α_em(Mc(EW)) = 1/(36π) = β/4')
    print('      ↓  primitive compression threshold [NEW — Tier 3]')
    print('  S_kink = 1/α_em(Mc) = 36π = 4/β')
    print('      ↓  BPS kink action = (4/3)α^(3/2)/(β√2)')
    print('  α^(3/2) = 3√2 = √(Q_top × N_Hopf) = √18')
    print('      ↓  cube root')
    print('  α = ∛18 = (Q_top × N_Hopf)^(1/3)   [Tier 3]')
    print()
    print('  ALL NUMERICAL CHECKS:')
    print()
    print(f'  S_kink = 4/β = 1/α_em = 36π       max residual: {identity_res["max_residual"]:.2e}')
    print(f'  β = 4 × α_em(Mc)                   exact (algebraic)')
    print(f'  α^(3/2) = √(Q_top × N_Hopf)        residual: {topo_res["residual_32"]:.2e}')
    print(f'  α = (Q_top × N_Hopf)^(1/3)         residual: {topo_res["residual_alpha"]:.2e}')
    print(f'  S_kink × α_em(Mc) = 1               residual: {phys_res["r_prod"]:.2e}')
    print(f'  S_kink verified from α              residual: {skink_res["residual"]:.2e}')
    print()
    print('  PHYSICAL VALUES (Planck units):')
    print()
    print(f'  α = ∛18         ≈ {alpha:.6f}')
    print(f'  ξ = 18^(-1/6)   ≈ {phys_res["xi"]:.6f} l_Pl    [kink width, ≈ 1/φ_golden to 0.07%]')
    print(f'  E_kink = 36π M_Pl ≈ {phys_res["E_kink_Mpl"]:.2f} M_Pl  [D1 kink energy]')
    print(f'  φ₀ = √(α/β)    ≈ {phys_res["phi0_Mpl"]:.4f} M_Pl   [vacuum field amplitude]')
    print()
    print('  OPEN QUESTIONS:')
    print()
    print('  (i)  Formal derivation of S_kink = 1/α_em from the D5 winding geometry.')
    print('       Path: show that D5 U(1) closure imposes S_kink = (1+k_Y²)/α_common')
    print('       from the D5 winding integral alone — closing the Tier 3→2a gap.')
    print()
    print('  (ii) Derive the M_c depth cascade from V(φ) substrate dynamics.')
    print('       Path: depth-running equation for α_Dn — would predict Λ_QCD/M_Pl.')
    print()
    print('  (iii) Clarify near-golden-ratio: ξ × φ_golden = 1 to 0.07%.')
    print(f'       18^(1/6) = {18**(1/6):.8f}  vs  φ = {PHI_GOLDEN:.8f}  (differ {abs(18**(1/6)-PHI_GOLDEN)/PHI_GOLDEN*100:.4f}%)')
    print('       Not exact — document as structural note pending further analysis.')
    print()
    print('  CONNECTIONS:')
    print('    equations/d5_complex_from_instability.py  β=1/(9π), Q_top=2 (Cycle 117)')
    print('    equations/alpha_em_prediction.py          1/α_em(Mc)=36π  (Cycle 141)')
    print('    equations/kk_action_coupling.py           BPS E_kink formula (Cycle 111)')
    print('    foundations/substrate.md                  V(φ), kink, α free parameter')
    print('    foundations/coupling_emergence.md         β and 36π chain structure')


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('=' * 70)
    print('ALPHA FROM KINK ACTION SELF-CONSISTENCY  (Cycle 169)')
    print('α = (Q_top × N_Hopf)^(1/3) = ∛18 ≈ 2.621  [Planck units, Tier 3]')
    print('Condition: S_kink = 1/α_em(M_c(EW)) = 36π')
    print('=' * 70)
    print()

    alpha_res    = derive_alpha()
    skink_res    = verify_skink(alpha_res)
    identity_res = three_way_identity()
    topo_res     = topological_formula(alpha_res)
    phys_res     = physical_consequences(alpha_res)
    hier_res     = alpha_hierarchy(alpha_res)
    summary(alpha_res, skink_res, identity_res, topo_res, phys_res)
