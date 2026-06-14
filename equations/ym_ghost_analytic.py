"""
ym_ghost_analytic.py — Cycle 260: Analytic sech⁶ Fourier Transform for c_ghost

Physical question:
    C259 computed c_ghost = 2.466 using numerical quad integration of the
    oscillatory product sech⁶(κy) × ψ_ghost^+(y,k), which hit scipy's subdivision
    limit (200-300) on every k-value, making c_ghost unreliable.

    This file derives ANALYTIC Fourier transforms of sech⁶(κy) and
    sech⁶(κy)tanh(κy) using the differential-operator recurrence, then constructs
    V_ghost_norm analytically. The c_ghost integrand becomes a smooth rational
    function of q = k/κ divided by sinh²(πq/2) — trivially convergent.

Derivation summary:
    Step 1 — Recurrence relation (differential-operator identity):

        d²/du²[sech²(u)] = 4 sech²(u) − 6 sech⁴(u)           [T1: calculus]
        d²/du²[sech⁴(u)] = 16 sech⁴(u) − 20 sech⁶(u)          [T1: calculus]

    Applying FT to each and using FT[f''](q) = −q² FT[f](q):

        FT[sech²](q)  = π q / sinh(πq/2)                         [T1]
        FT[sech⁴](q)  = π q(q²+4) / (6 sinh(πq/2))              [T1]
        FT[sech⁶](q)  = π q(q²+4)(q²+16) / (120 sinh(πq/2))     [T1]

    Consistency checks: at q→0 each formula reproduces ∫sech^{2n}du = 2, 4/3, 16/15.

    Step 2 — Fourier transform of sech⁶ tanh (integration by parts):

        sech⁶(u)tanh(u) = −(1/6) d/du[sech⁶(u)]
        FT[sech⁶ tanh](q) as sine FT = (q/6) × FT[sech⁶](q) as cosine FT    [T1]

    Step 3 — Ghost even-parity mode (from Darboux step; verified in C259):

        ψ_ghost^+(y,k) = Re[e^{iδ₁}(f₁(y,k)+f₁(−y,k))]
                       = 2[k cos(ky) − κ tanh(κy) sin(ky)] / √(k²+κ²)       [T1]

    Step 4 — V_ghost_unnorm(k) = ∫ sech⁶(κy) × ψ_ghost^+(y,k) dy

        Substituting u = κy, q = k/κ:
            k J₁ − κ J₂ = π q²(q²+4)(q²+16)/sinh(πq/2) × (1/120 − 1/720)
                        = π q²(q²+4)(q²+16) / (144 sinh(πq/2))
            √(k²+κ²) = κ√(q²+1)

        V_ghost_unnorm(k) = 2π q²(q²+4)(q²+16) / [144 κ √(q²+1) sinh(πq/2)]

    Step 5 — V_ghost_norm(k) = V_ghost_unnorm / F₆ where F₆ = xi × 16/15 = 16/(15κ):

        V_ghost_norm(k) = 5π q²(q²+4)(q²+16) / [384 √(q²+1) sinh(πq/2)]     [T1]

        where q = k/κ. This is dimensionless and SMOOTH — no oscillations.

    Step 6 — c_ghost integral (change variable k → q = k/κ):

        c_ghost = (N_adj/π) ∫_κ^∞ |V_ghost_norm(k)|² dk
               = (N_adj × κ / π) ∫_1^∞ |V_ghost_norm(qκ)|² dq
               = N_adj × κ × 25π ∫_1^∞ q⁴(q²+4)²(q²+16)² / [384²(q²+1)sinh²(πq/2)] dq

        Integrand is smooth, decays as e^{−πq}, integrates to machine precision.

Key result:
    c_ghost_analytic [T1 formula, T2a numeric] vs c_gauge_C197 = 2.773063 [T2a]
    → c_net = c_gauge − c_ghost  →  δC  →  C_match_total  [T2a]

Tier assignments:
    Part A [T1]:  Verify FT[sech⁶] and FT[sech⁶tanh] formulas numerically
    Part B [T1]:  Verify V_ghost_norm_analytic matches C259 numerical values
    Part C [T2a]: Compute c_ghost from smooth analytic integrand
    Part D [T2a]: Net correction δC; C_match_total assessment

References:
    C259: ym_ghost_jost.py — c_ghost = 2.466 (convergence-limited, unreliable)
    C197: ym_jost_function.py — c_gauge = 2.773063 [T2a, sech⁸ vertex]
    C191: ym_cmatch_msbar.py  — C_match_tree = 0.789948 [T2a]
    C256: ym_sp5_complete_chain.py — C_match_needed = 0.789937 [T2a]
"""

import numpy as np
from scipy.integrate import quad

print("=" * 70)
print("Cycle 260 — Analytic sech⁶ FT: c_ghost without subdivision limits")
print("=" * 70)

# ─── DFC Parameters ───────────────────────────────────────────────────────────
alpha    = 18.0 ** (1.0/3.0)       # ∛18 [T2a, C172]
beta     = 1.0 / (9.0 * np.pi)    # 1/(9π) [T2a, C117]
xi       = np.sqrt(2.0 / alpha)    # kink width ξ = √(2/α) [T1]
kappa    = 1.0 / xi                # κ = 1/ξ [T1]
g_eff_sq = 8.0 / 27.0             # g_eff² = 2I₄/N_Hopf [T2a, C171]
N_adj    = 8                       # dim(adj SU(3)) [T1]

# Established values [T2a]
c_gauge_C197   = 2.773063   # sech⁸ vertex, s=2 PT [C197, T2a]
C_match_tree   = 0.789948   # MS-bar tree-level [C191, T2a]
C_match_Jost   = 0.795151   # gauge-only Jost [C197, T2a]
C_match_needed = 0.789937   # required for exact α_s(M_Z) [C256, T2a]

print(f"\nParameters:")
print(f"  α = ∛18 = {alpha:.8f},  ξ = {xi:.8f} M_Pl⁻¹")
print(f"  κ = 1/ξ = {kappa:.8f} M_Pl,  g_eff² = {g_eff_sq:.8f}")
print(f"\nEstablished C_match values [T2a]:")
print(f"  C_match_tree   = {C_match_tree:.6f}  (C191)")
print(f"  C_match_Jost   = {C_match_Jost:.6f}  (C197, gauge-only)")
print(f"  C_match_needed = {C_match_needed:.6f}  (C256)")
print()

# ═══════════════════════════════════════════════════════════════════════════════
# PART A — Verify Analytic Fourier Transform Formulas  [T1]
# ═══════════════════════════════════════════════════════════════════════════════
print("─" * 70)
print("PART A: Verify FT[sech⁶](q) and FT[sech⁶ tanh](q)  [T1]")
print("─" * 70)
print()
print("  Recurrence derivation:")
print("    d²/du²[sech²] = 4sech² − 6sech⁴  →  FT[sech⁴] = (q²+4)/6 × FT[sech²]")
print("    d²/du²[sech⁴] = 16sech⁴ − 20sech⁶  →  FT[sech⁶] = (q²+16)/20 × FT[sech⁴]")
print()
print("    FT[sech²](q) = πq/sinh(πq/2)")
print("    FT[sech⁴](q) = πq(q²+4)/(6 sinh(πq/2))")
print("    FT[sech⁶](q) = πq(q²+4)(q²+16)/(120 sinh(πq/2))")
print()

def ft_sech2_analytic(q):
    """Analytic FT of sech²(u): ∫ sech²(u)cos(qu) du = πq/sinh(πq/2)."""
    if abs(q) < 1e-10:
        return 2.0   # L'Hôpital: πq/(πq/2) = 2
    return np.pi * q / np.sinh(np.pi * q / 2)

def ft_sech4_analytic(q):
    """Analytic FT of sech⁴(u): πq(q²+4)/(6 sinh(πq/2))."""
    if abs(q) < 1e-10:
        return 4.0 / 3.0   # πq(0+4)/(6 πq/2) = 8/6 = 4/3
    return np.pi * q * (q**2 + 4) / (6.0 * np.sinh(np.pi * q / 2))

def ft_sech6_analytic(q):
    """Analytic FT of sech⁶(u): πq(q²+4)(q²+16)/(120 sinh(πq/2))."""
    if abs(q) < 1e-10:
        return 16.0 / 15.0  # πq(0+4)(0+16)/(120 πq/2) = 4×16/60 = 16/15
    return np.pi * q * (q**2 + 4) * (q**2 + 16) / (120.0 * np.sinh(np.pi * q / 2))

def ft_sech6tanh_analytic(q):
    """Analytic FT of sech⁶(u)tanh(u) as sin FT: (q/6)×FT[sech⁶](q)."""
    if abs(q) < 1e-10:
        return 0.0
    return (q / 6.0) * ft_sech6_analytic(q)

# Verify by numerical integration
all_pass_A = True
print(f"  Verification of FT[sech⁶](q) = πq(q²+4)(q²+16)/(120 sinh(πq/2)):")
print(f"  {'q':<6} {'Numeric':<16} {'Analytic':<16} {'Residual':<12} {'Pass'}")
print(f"  {'─'*6} {'─'*16} {'─'*16} {'─'*12} {'─'*4}")
for q_test in [0.0, 0.5, 1.0, 2.0, 3.0, 5.0]:
    if q_test == 0.0:
        num_val, _ = quad(lambda u: 1.0/np.cosh(u)**6, -50.0, 50.0, limit=200)
    else:
        num_val, _ = quad(lambda u: np.cos(q_test*u)/np.cosh(u)**6, -50.0, 50.0, limit=400)
    ana_val = ft_sech6_analytic(q_test)
    res = abs(num_val - ana_val)
    ok = res < 5e-8
    if not ok: all_pass_A = False
    print(f"  {q_test:<6.1f} {num_val:<16.10f} {ana_val:<16.10f} {res:<12.2e} {'PASS' if ok else 'FAIL'}")

print()
print(f"  Verification of FT[sech⁶tanh](q) as sin FT = (q/6)×FT[sech⁶](q):")
print(f"  {'q':<6} {'Numeric':<16} {'Analytic':<16} {'Residual':<12} {'Pass'}")
print(f"  {'─'*6} {'─'*16} {'─'*16} {'─'*12} {'─'*4}")
for q_test in [0.5, 1.0, 2.0, 3.0, 5.0]:
    num_val, _ = quad(lambda u: np.tanh(u)*np.sin(q_test*u)/np.cosh(u)**6,
                      -50.0, 50.0, limit=400)
    ana_val = ft_sech6tanh_analytic(q_test)
    res = abs(num_val - ana_val)
    ok = res < 5e-8
    if not ok: all_pass_A = False
    print(f"  {q_test:<6.1f} {num_val:<16.10f} {ana_val:<16.10f} {res:<12.2e} {'PASS' if ok else 'FAIL'}")

print()
print(f"  Part A: {'PASS [T1]' if all_pass_A else 'FAIL'}")
print()

# ═══════════════════════════════════════════════════════════════════════════════
# PART B — Analytic V_ghost_norm vs C259 Numeric  [T1]
# ═══════════════════════════════════════════════════════════════════════════════
print("─" * 70)
print("PART B: Analytic V_ghost_norm(k)  [T1]")
print("─" * 70)
print()
print("  Derivation (all steps [T1]):")
print("    ψ_ghost^+(y,k) = 2[k cos(ky) − κ tanh(κy) sin(ky)] / √(k²+κ²)")
print("    V_ghost_unnorm = ∫sech⁶(κy)×ψ_ghost^+(y,k) dy")
print("    = 2/√(k²+κ²) × [k×J₁ − κ×J₂]")
print("    k J₁ = πq²(q²+4)(q²+16)/(120 sinh(πq/2))")
print("    κ J₂ = πq²(q²+4)(q²+16)/(720 sinh(πq/2))")
print("    k J₁ − κ J₂ = πq²(q²+4)(q²+16)/(144 sinh(πq/2))  [factor: 1/120−1/720 = 5/720]")
print()
print("    F₆ = ξ × 16/15 = 16/(15κ)  [sech⁶ norm]")
print()
print("    V_ghost_norm(k) = V_ghost_unnorm / F₆")
print("                    = 5π q²(q²+4)(q²+16) / [384 √(q²+1) sinh(πq/2)]")
print("    where q = k/κ. Dimensionless, smooth.  [T1]")
print()

def V_ghost_norm_analytic(k):
    """
    Analytic ghost vertex form factor.
    V_ghost_norm(k) = 5π q²(q²+4)(q²+16) / [384 √(q²+1) sinh(πq/2)]
    where q = k/κ.  [T1]
    """
    q = k / kappa
    if q < 1e-6:
        return 0.0
    num = 5.0 * np.pi * q**2 * (q**2 + 4.0) * (q**2 + 16.0)
    den = 384.0 * np.sqrt(q**2 + 1.0) * np.sinh(np.pi * q / 2.0)
    return num / den

# Recompute C259's numeric V_ghost_norm for comparison
def psi_jost_s1(y, k):
    t = np.tanh(kappa * y)
    return np.exp(1j * k * y) * (k + 1j * kappa * t) / (k + 1j * kappa)

def psi_ghost_even_numeric(y, k):
    d1 = np.arctan(kappa / k)
    f1_y  = psi_jost_s1( y, k)
    f1_my = psi_jost_s1(-y, k)
    return np.real(np.exp(1j * d1) * (f1_y + f1_my))

def psi_ghost_even_analytic(y, k):
    """ψ_ghost^+(y,k) = 2[k cos(ky) − κ tanh(κy) sin(ky)] / √(k²+κ²)  [T1]"""
    t = np.tanh(kappa * y)
    return 2.0 * (k * np.cos(k * y) - kappa * t * np.sin(k * y)) / np.sqrt(k**2 + kappa**2)

F6 = xi * 16.0 / 15.0  # sech⁶ norm ∫sech⁶(κy)dy

def V_ghost_norm_numeric(k):
    result, _ = quad(
        lambda y: (1.0/np.cosh(kappa*y)**6) * psi_ghost_even_numeric(y, k),
        -15.0*xi, 15.0*xi, limit=300, epsabs=1e-12, epsrel=1e-10
    )
    return result / F6

# Verify psi_ghost_even analytic = psi_ghost_even numeric [T1]
print("  Verify ψ_ghost^+ analytic = 2[k cos(ky) − κt sin(ky)]/√(k²+κ²):")
all_pass_psi = True
for q_test in [1.5, 2.0, 3.0, 5.0]:
    k_test = q_test * kappa
    y_vals = [0.3 * xi, xi, 2.0 * xi]
    max_res = max(abs(psi_ghost_even_numeric(y, k_test) - psi_ghost_even_analytic(y, k_test))
                  for y in y_vals)
    ok = max_res < 1e-11
    if not ok: all_pass_psi = False
    print(f"    q={q_test:.1f}: max |ψ_num − ψ_analytic| = {max_res:.2e}  [{'PASS' if ok else 'FAIL'}]")
print()
if not all_pass_psi: all_pass_A = False

# Compare V_ghost_norm analytic vs numeric at several k values
print("  V_ghost_norm comparison: analytic [T1 formula] vs C259 numeric:")
print(f"  {'k/κ':<6} {'Analytic':<16} {'Numeric (C259)':<18} {'Residual':<12} {'Pass'}")
print(f"  {'─'*6} {'─'*16} {'─'*18} {'─'*12} {'─'*4}")

k_compare = [1.05, 1.2, 1.5, 2.0, 3.0, 5.0]
all_pass_B = True
V_analytic_vals = {}
for qk in k_compare:
    k_val = qk * kappa
    Va = V_ghost_norm_analytic(k_val)
    Vn = V_ghost_norm_numeric(k_val)
    res = abs(Va - Vn) / (abs(Vn) + 1e-15)
    ok = res < 1e-5   # analytic formula should match numeric to 1e-5 relative
    if not ok: all_pass_B = False
    V_analytic_vals[qk] = Va
    print(f"  {qk:<6.2f} {Va:<16.8f} {Vn:<18.8f} {res:<12.2e} {'PASS' if ok else 'FAIL'}")

print()
print(f"  Part B: {'PASS [T1]' if all_pass_B else 'FAIL'}")
print()

# ═══════════════════════════════════════════════════════════════════════════════
# PART C — c_ghost from Smooth Analytic Integrand  [T2a]
# ═══════════════════════════════════════════════════════════════════════════════
print("─" * 70)
print("PART C: c_ghost from smooth analytic integrand  [T2a]")
print("─" * 70)
print()
print("  Smooth integrand (change variables k → q = k/κ):")
print("    g(q) = N_adj × κ × 25π × q⁴(q²+4)²(q²+16)² / [384²(q²+1)sinh²(πq/2)]")
print("    c_ghost = ∫_1^∞ g(q) dq   [no oscillations, no subdivision limit]")
print()

def integrand_smooth(q):
    """
    Smooth integrand for c_ghost after analytic FT substitution.
    g(q) = N_adj × κ/π × |V_ghost_norm_analytic(qκ)|²  (times κ for dq measure)
    = N_adj × κ × 25π × q⁴(q²+4)²(q²+16)² / [384²(q²+1)sinh²(πq/2)]
    """
    if q < 1e-6:
        return 0.0
    numerator   = N_adj * kappa * 25.0 * np.pi * q**4 * (q**2+4)**2 * (q**2+16)**2
    denominator = 384.0**2 * (q**2 + 1.0) * np.sinh(np.pi * q / 2.0)**2
    return numerator / denominator

# Check integrand at threshold and decay
print("  Integrand g(q) values:")
print(f"  {'q':<6} {'g(q)':<18}")
for q_val in [1.0, 1.5, 2.0, 3.0, 5.0, 7.0, 10.0]:
    print(f"  {q_val:<6.1f} {integrand_smooth(q_val):<18.8f}")
print()

# Integrate — no subdivision warnings expected
c_ghost_analytic, err_ghost = quad(integrand_smooth, 1.0, np.inf,
                                    limit=100, epsabs=1e-10, epsrel=1e-8)

print(f"  c_ghost_analytic = {c_ghost_analytic:.8f}  (integration error ≤ {err_ghost:.2e})")
print(f"  c_ghost_C259     = 2.466136              (convergence-limited, unreliable)")
print()

# Also compute from k-space directly (cross-check, should agree)
def integrand_k_analytic(k):
    return N_adj / np.pi * V_ghost_norm_analytic(k)**2

c_ghost_k, err_k = quad(integrand_k_analytic, kappa, np.inf,
                          limit=100, epsabs=1e-10, epsrel=1e-8)

print(f"  Cross-check (k-space analytic): c_ghost = {c_ghost_k:.8f}  (err {err_k:.2e})")
c_ghost_agree = abs(c_ghost_analytic - c_ghost_k) / c_ghost_analytic
print(f"  q-space vs k-space agreement: {100*c_ghost_agree:.4f}%")
print()

# Split integral for verification
c_g1, _ = quad(integrand_smooth, 1.0, 2.0, limit=50, epsabs=1e-12, epsrel=1e-10)
c_g2, _ = quad(integrand_smooth, 2.0, 5.0, limit=50, epsabs=1e-12, epsrel=1e-10)
c_g3, _ = quad(integrand_smooth, 5.0, np.inf, limit=50, epsabs=1e-12, epsrel=1e-10)
print(f"  c_ghost [q: 1, 2]  = {c_g1:.8f}")
print(f"  c_ghost [q: 2, 5]  = {c_g2:.8f}")
print(f"  c_ghost [q: 5, ∞]  = {c_g3:.8f}  (tail)")
print(f"  c_ghost total      = {c_g1+c_g2+c_g3:.8f}  (sum of parts)")
print()

# ═══════════════════════════════════════════════════════════════════════════════
# PART D — Net Correction δC = c_gauge − c_ghost; C_match_total  [T2a]
# ═══════════════════════════════════════════════════════════════════════════════
print("─" * 70)
print("PART D: Net correction δC and C_match_total  [T2a]")
print("─" * 70)
print()

c_net = c_gauge_C197 - c_ghost_analytic

print(f"  c_gauge (sech⁸, s=2 PT, threshold 2κ) = {c_gauge_C197:.8f}  [C197, T2a]")
print(f"  c_ghost (sech⁶, s=1 PT, threshold  κ) = {c_ghost_analytic:.8f}  [T1 formula, T2a]")
print(f"  c_net = c_gauge − c_ghost              = {c_net:.8f}")
print()

# Convert to C_match correction:
# In background-field gauge: δ(1/g²) = c_net × g²/(16π²)
# δC ≈ δ(1/g²) × g²/C_tree  (first-order)
delta_g2_net = c_net * g_eff_sq / (16.0 * np.pi**2)
delta_C_net  = delta_g2_net * g_eff_sq / C_match_tree
C_match_total = C_match_tree + delta_C_net

print(f"  δ(1/g²)_net = c_net × g²/(16π²)       = {delta_g2_net:.8f}")
print(f"  δC_net = δ(1/g²)_net × g²/C_tree       = {delta_C_net:+.8f}")
print(f"  → δC_net = {100*delta_C_net/C_match_tree:+.4f}% of C_match_tree")
print()
print(f"  C_match_tree    = {C_match_tree:.8f}  [C191]")
print(f"  C_match_total   = {C_match_total:.8f}  [tree + ghost+gauge KK correction]")
print(f"  C_match_needed  = {C_match_needed:.8f}  [C256]")
print()

gap_from_needed = (C_match_total - C_match_needed) / C_match_needed * 100
gap_from_tree   = (C_match_total - C_match_tree)   / C_match_tree   * 100

print(f"  Gap from needed: {gap_from_needed:+.4f}%")
print(f"  Gap from tree:   {gap_from_tree:+.4f}%")
print()

# Bracketing: C_match_needed should lie between tree (no corrections) and gauge-only
print(f"  Bracketing summary:")
print(f"    Tree-level only:  C_match = {C_match_tree:.6f}  (−0.001% from needed)")
print(f"    + gauge (C197):   C_match = {C_match_Jost:.6f}  (+0.659% from needed)")
print(f"    + ghost (C260):   C_match = {C_match_total:.6f}  ({gap_from_needed:+.3f}% from needed)")
print()

# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("SUMMARY: Assertions and Tier Assignments")
print("=" * 70)
print()

n_pass = 0
n_total = 0

def check(label, condition, tier, desc):
    global n_pass, n_total
    n_total += 1
    if condition: n_pass += 1
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}: {desc}  [{tier}]")
    return condition

check("A1", all_pass_A, "T1",
      "FT[sech⁶](q) = πq(q²+4)(q²+16)/(120sinh(πq/2)): all q values match numeric")

check("A2", all_pass_psi, "T1",
      "ψ_ghost^+ analytic = 2[k cos−κt sin]/√(k²+κ²): matches C259 Darboux formula")

check("B1", all_pass_B, "T1",
      "V_ghost_norm_analytic matches C259 numeric to < 1e-5 relative error")

check("C1", err_ghost < 1e-6, "T2a",
      f"c_ghost smooth integration converged: err = {err_ghost:.2e}")

check("C2", c_ghost_agree < 1e-6, "T2a",
      f"q-space vs k-space c_ghost agree to {100*c_ghost_agree:.4f}%")

check("C3", c_ghost_analytic > c_gauge_C197, "T2a",
      f"c_ghost = {c_ghost_analytic:.4f} > c_gauge = {c_gauge_C197:.4f} (expected: lower threshold κ < 2κ + wider sech⁶ > sech⁸)")

check("D1", c_ghost_analytic > 0, "T2a",
      f"c_ghost = {c_ghost_analytic:.6f} > 0")

check("D2", abs(gap_from_needed) < 2.0, "T2a",
      f"C_match_total gap from needed = {gap_from_needed:+.4f}% (< 2%)")

check("D3", abs(C_match_total - C_match_needed) < abs(C_match_Jost - C_match_needed), "T2a",
      f"Ghost correction reduces C_match gap vs gauge-only: |{C_match_total:.6f}−{C_match_needed:.6f}| < |{C_match_Jost:.6f}−{C_match_needed:.6f}|")

print()
print(f"  Passed {n_pass}/{n_total} assertions")
print()
print("─" * 70)
print("Final: SP5 C_match analytic result")
print("─" * 70)
print()
print(f"  KEY RESULTS [T1 formula → T2a numerics]:")
print(f"    FT[sech⁶](q)    = πq(q²+4)(q²+16)/(120 sinh(πq/2))  [T1]")
print(f"    V_ghost_norm(k) = 5πq²(q²+4)(q²+16)/(384√(q²+1)sinh(πq/2))  [T1]")
print(f"    c_ghost_analytic = {c_ghost_analytic:.6f}  [T2a, smooth integrand]")
print(f"    c_gauge          = {c_gauge_C197:.6f}  [T2a, C197]")
print(f"    c_net            = {c_net:.6f}  [{'+' if c_net >= 0 else ''}]")
print()
print(f"    C_match corrections:")
print(f"      Tree:        {C_match_tree:.6f}")
print(f"      +gauge(C197): {C_match_Jost:.6f}  (+0.659%)")
print(f"      +ghost(C260): {C_match_total:.6f}  ({gap_from_needed:+.3f}% from needed)")
print(f"      Needed:      {C_match_needed:.6f}")
print()

if abs(gap_from_needed) < 0.5:
    tier_label = "T2a"
    conclusion = f"C_match bracketed to < 0.5%: gauge-only +0.659%, ghost+gauge {gap_from_needed:+.3f}% (gap from needed)"
elif abs(gap_from_needed) < 2.0:
    tier_label = "T3"
    conclusion = f"C_match gap reduced: {gap_from_needed:+.3f}% from needed — ghost prescription T3"
else:
    tier_label = "T3"
    conclusion = f"C_match gap {gap_from_needed:+.3f}%: ghost+gauge correction characterised but gap remains"

print(f"  Tier: SP5 C_match — {tier_label}")
print(f"  {conclusion}")
print()
print(f"  Note: JW5 (mass gap Δ≥1033 MeV) is T2a INDEPENDENTLY of C_match,")
print(f"  via SC area law: g_eff²→β_lat=20.25→u_SC=0.0564<1→σ_SC>0→Δ≥1033 MeV.")
print(f"  C_match accuracy is supplementary to JW5.")
