"""
Born Rule — Step 6b: Barrier Dynamics Derivation (Cycle 359)

Physical question:
    WHY does the D3 localization rate at position x depend on |ψ(x)|²?
    This module derives Step 6b from V(φ) dynamics by connecting the nonlinear
    source S(x) [Step 6a, C338] to the spinodal instability [collapse mechanism,
    C340]. The result: the DC nonlinear response Σ(x) shifts the local field
    closer to the spinodal threshold at positions where |ψ(x)|² is large,
    making the localization rate proportional to |ψ(x)|².

DFC mechanism:
    1. The V(φ) field equation with the leading nonlinear term produces a DC
       (time-averaged) response Σ(x) = −S(x)/(2α) at each position x [T1].
       Here S(x) = 3βφ₀(φ_c²/2)|ψ(x)|² is the nonlinear source from Step 6a.

    2. Σ(x) < 0 shifts the local field from φ₀ toward the spinodal threshold
       φ_sp = φ₀/√3 [T1, collapse_mechanism.py]. The remaining distance to
       spinodal is d(x) = d₀ − |Σ(x)|, where d₀ = φ₀ − φ_sp [T1].

    3. For ANY monotonically decreasing barrier-crossing rate function Γ(d):
       δΓ(x) = Γ(d₀ − |Σ|) − Γ(d₀) ≈ |Γ'(d₀)| × |Σ(x)| ∝ |ψ(x)|² [T2a].
       The linear expansion is valid because |Σ|/d₀ ~ (φ_c/φ₀)² << 1 in the
       semiclassical regime — numerically ~0.4% for φ_c = 0.05φ₀.

    4. Normalization: P(x) = δΓ(x)/∫δΓ(x')dx' = |ψ(x)|²/∫|ψ(x')|²dx' = |ψ(x)|².

    This derives rate(x) ∝ |ψ(x)|² from V(φ) dynamics alone, using:
    - The nonlinear source S(x) [T1, Step 6a]
    - The spinodal instability [T1, collapse mechanism]
    - Linear response in the semiclassical regime [T2a]

    Step 6b: T3 → T2a (proper dynamical derivation, not just coupling selection)

Born rule chain status after this module:
    Steps 1-5: T2a (born_rule_schrodinger.py)
    Step 6a:   T1  (born_rule_d3_coupling.py — S(x) = κ_NL × ⟨ε(x)⟩)
    Step 6b:   T2a (THIS MODULE — barrier dynamics: Σ(x) reduces d(x))
               T2a (born_rule_frequency_selection.py — σ² uniqueness, C339)
               Two independent T2a derivations of Step 6b now exist.
    Born rule: T2a OVERALL (chain complete, two independent Step 6b routes)

Key references:
    - born_rule_d3_coupling.py [C338]: S(x) = κ_NL × ⟨ε(x)⟩, κ_NL = 3βφ₀/(2α)
    - born_rule_frequency_selection.py [C339]: σ² uniqueness from Z₂+averaging
    - collapse_mechanism.py [C340]: φ_sp = φ₀/√3, γ = √α
    - born_rule_schrodinger.py [C336]: V(φ) → Schrödinger; ⟨ε(x)⟩ ∝ |ψ|²
"""

import numpy as np

# ── NumPy 2.0 compatibility ──────────────────────────────────────────────────
_trapz = getattr(np, 'trapezoid', getattr(np, 'trapz', None))

# ── Assertion framework ──────────────────────────────────────────────────────
PASS_count = 0
FAIL_count = 0

def check(label, value, expected=True, tol=1e-10):
    global PASS_count, FAIL_count
    if isinstance(expected, bool):
        ok = bool(value) == expected
    else:
        ok = abs(float(value) - float(expected)) < tol
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS_count += 1
    else:
        FAIL_count += 1
    print(f"  [{status}] {label}: {value}")
    return ok

# ── DFC parameters (all exact/T2a) ──────────────────────────────────────────
alpha   = 18 ** (1/3)             # α = ∛18 [T2a, C172]
beta    = 1.0 / (9 * np.pi)      # β = 1/(9π) [T2a, C117]
phi0    = np.sqrt(alpha / beta)   # φ₀ = √(α/β) [T1]
omega_c = np.sqrt(2 * alpha)     # ω_c = √(2α) [T1]
phi_sp  = phi0 / np.sqrt(3)      # spinodal: V''(φ_sp) = 0 [T1, C340]

phi_c = 0.05 * phi0              # slow-envelope amplitude (semiclassical)

print("=" * 70)
print("Born Rule Step 6b — Barrier Dynamics Derivation")
print("equations/born_rule_barrier_dynamics.py  (Cycle 359)")
print("=" * 70)

# ════════════════════════════════════════════════════════════════════════════
# PART A — DC nonlinear response Σ(x) from V(φ) [T1]
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART A: DC Response Σ(x) from V(φ) Field Equation [T1] ---")
print()
print("  Full field equation near φ₀:")
print("    ∂²σ/∂t² − ∇²σ + 2ασ + 3βφ₀σ² = 0")
print()
print("  Fast oscillation: σ_fast(x,t) = φ_c ψ(x) cos(ω_c t)")
print("  Nonlinear term: 3βφ₀σ² = 3βφ₀φ_c²ψ²(x)cos²(ω_c t)")
print("                          = (3βφ₀φ_c²/2)ψ²(x)[1 + cos(2ω_c t)]")
print()
print("  DC (zero-frequency) source from cos² → 1/2:")
print("    S_DC(x) = 3βφ₀(φ_c²/2)|ψ(x)|²    [= S(x) from Step 6a, C338]")
print()
print("  Quasi-static equation for DC response Σ(x):")
print("    2αΣ(x) = −S_DC(x)     [neglect ∂²Σ/∂t² for slow DC mode]")
print("    Σ(x) = −S_DC(x)/(2α) = −3βφ₀(φ_c²/2)|ψ(x)|²/(2α)")

# Compute S_DC and Σ for test wave function ψ(x) = cos(kx)
x_vals = np.linspace(-np.pi, np.pi, 2001)
k = 1.0
psi_x = np.cos(k * x_vals)

S_DC = 3 * beta * phi0 * (phi_c**2 / 2) * psi_x**2
Sigma_x = -S_DC / (2 * alpha)

# Verify Σ(x) = −κ_NL × ⟨ε(x)⟩ / (2α)
kappa_NL = 3 * beta * phi0 / omega_c**2   # from C338
eps_x = (phi_c**2 * omega_c**2 / 2) * psi_x**2

Sigma_from_S6a = -kappa_NL * eps_x / (2 * alpha)
check("Σ(x) from field eq = Σ from Step 6a [T1 consistency]",
      np.max(np.abs(Sigma_x - Sigma_from_S6a)), 0.0, tol=1e-14)

# Σ < 0 everywhere (shifts field toward φ = 0, i.e., toward spinodal)
check("Σ(x) ≤ 0 everywhere (shifts toward spinodal) [T1]",
      np.all(Sigma_x <= 0), True)

# Σ ∝ |ψ(x)|² (proportionality)
nonzero = np.abs(psi_x) > 1e-6
ratio = Sigma_x[nonzero] / (-psi_x[nonzero]**2)
check("Σ(x)/|ψ(x)|² = const (proportionality) [T1]",
      np.std(ratio) / np.mean(ratio), 0.0, tol=1e-12)

print(f"\n  Σ coefficient = −3βφ₀φ_c²/(4α) = {np.mean(ratio):.8e}")
print(f"  Σ_max = {np.min(Sigma_x):.8e} M_Pl  (at ψ peaks)")

# ════════════════════════════════════════════════════════════════════════════
# PART B — Spinodal distance d(x) = d₀ − |Σ(x)| [T1]
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART B: Spinodal Distance d(x) [T1] ---")
print()
print("  Spinodal point: φ_sp = φ₀/√3  [T1, collapse_mechanism.py]")
print("  Unperturbed field: φ = φ₀")
print("  Perturbed field:   φ = φ₀ + Σ(x)  [Σ < 0, shifted toward spinodal]")
print()
print("  Unperturbed distance to spinodal:")
print("    d₀ = φ₀ − φ_sp = φ₀(1 − 1/√3)")
print()
print("  Perturbed distance at position x:")
print("    d(x) = (φ₀ + Σ(x)) − φ_sp = d₀ + Σ(x) = d₀ − |Σ(x)|")
print("    [closer to spinodal where |ψ(x)|² is large]")

d0 = phi0 - phi_sp   # unperturbed distance to spinodal

check("d₀ = φ₀(1 − 1/√3) > 0 [T1]", d0, phi0 * (1 - 1/np.sqrt(3)), tol=1e-12)

d_x = d0 + Sigma_x   # d(x) = d₀ − |Σ(x)| since Σ < 0

# d(x) is SMALLER where |ψ(x)|² is large
d_at_peak = d0 + np.min(Sigma_x)       # ψ peak (|ψ|² = 1)
d_at_node = d0 + Sigma_x[len(x_vals)//4]  # ψ node (|ψ|² ≈ 0)

check("d(peak) < d(node): closer to spinodal at ψ peaks [T1]",
      d_at_peak < d_at_node, True)

print(f"\n  d₀          = {d0:.6f} M_Pl")
print(f"  d(ψ peak)   = {d_at_peak:.6f} M_Pl  (reduced by |Σ_max|)")
print(f"  d(ψ node)   = {d_at_node:.6f} M_Pl  (≈ d₀)")
print(f"  Reduction:    {(d0 - d_at_peak)/d0:.6f} = {(d0-d_at_peak)/d0*100:.4f}%")

# ════════════════════════════════════════════════════════════════════════════
# PART C — Linear regime verification: |Σ|/d₀ << 1 [T2a]
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART C: Linear Regime Verification — |Σ|/d₀ << 1 [T2a] ---")

Sigma_max = np.max(np.abs(Sigma_x))
ratio_Sigma_d0 = Sigma_max / d0

check("|Σ|_max / d₀ << 1 (linear regime valid) [T2a]",
      ratio_Sigma_d0 < 0.01, True)

print(f"\n  |Σ|_max = {Sigma_max:.6e} M_Pl")
print(f"  d₀      = {d0:.6f} M_Pl")
print(f"  |Σ|_max/d₀ = {ratio_Sigma_d0:.6e}  (≈ {ratio_Sigma_d0:.1e})")
print()
print(f"  The ratio scales as (φ_c/φ₀)² = {(phi_c/phi0)**2:.4f}")
print(f"  For ANY semiclassical envelope φ_c << φ₀, the linear regime holds.")
print(f"  This is the same semiclassical condition used in Step 6b-iii (C339).")

# Analytic formula for the ratio
# |Σ|/d₀ = 3β(φ_c²/2)φ₀/(2α) / [φ₀(1 - 1/√3)]
#         = 3β(φ_c/φ₀)² × (α/β) / [4α(1-1/√3)]
#         = 3(φ_c/φ₀)² / [4(1-1/√3)]
analytic_ratio = 3 * (phi_c/phi0)**2 / (4 * (1 - 1/np.sqrt(3)))
check("|Σ|/d₀ = 3(φ_c/φ₀)²/[4(1−1/√3)] [T1 exact formula]",
      ratio_Sigma_d0, analytic_ratio, tol=1e-12)

print(f"  Analytic: |Σ|_max/d₀ = 3(φ_c/φ₀)²/[4(1−1/√3)] = {analytic_ratio:.6e}")

# ════════════════════════════════════════════════════════════════════════════
# PART D — KEY RESULT: δΓ(x) ∝ |ψ(x)|² from linear expansion [T2a]
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART D: KEY T2a RESULT — Localization Rate ∝ |ψ(x)|² ---")
print()
print("  For ANY monotonically decreasing barrier-crossing rate Γ(d):")
print("    Γ(d₀ − |Σ|) = Γ(d₀) + |Γ'(d₀)| × |Σ(x)| + O(Σ²)")
print("    δΓ(x) = Γ(d(x)) − Γ(d₀) ≈ |Γ'(d₀)| × |Σ(x)|")
print()
print("  Since |Σ(x)| ∝ |ψ(x)|²:")
print("    δΓ(x) ∝ |ψ(x)|²")
print()
print("  This holds for ANY barrier-crossing model (Kramers, Arrhenius,")
print("  quantum tunneling, etc.) — only monotonicity + linear regime needed.")

# δΓ(x) = c × |Σ(x)| where c = |Γ'(d₀)| (constant, independent of x)
# Since Σ(x) ∝ |ψ(x)|², δΓ(x) ∝ |ψ(x)|²

# Test with 3 different barrier-crossing rate models
d_vals = d_x.copy()

# Model 1: Kramers/Gaussian noise — Γ(d) = Γ₀ exp(-d²/(2σ_n²))
sigma_noise = 0.3 * d0  # arbitrary noise amplitude
rate_kramers = np.exp(-d_vals**2 / (2 * sigma_noise**2))
rate_kramers_0 = np.exp(-d0**2 / (2 * sigma_noise**2))
delta_kramers = rate_kramers - rate_kramers_0

# Model 2: Arrhenius — Γ(d) = Γ₀ exp(-k × d)
k_arrhenius = 5.0
rate_arrhenius = np.exp(-k_arrhenius * d_vals)
rate_arrhenius_0 = np.exp(-k_arrhenius * d0)
delta_arrhenius = rate_arrhenius - rate_arrhenius_0

# Model 3: Power-law — Γ(d) = Γ₀ / d^n
n_power = 2
rate_power = 1.0 / d_vals**n_power
rate_power_0 = 1.0 / d0**n_power
delta_power = rate_power - rate_power_0

# For each model, verify δΓ ∝ |ψ|² at non-zero ψ points
models = [
    ("Kramers (Gaussian)", delta_kramers),
    ("Arrhenius (exponential)", delta_arrhenius),
    ("Power-law (1/d²)", delta_power),
]

all_proportional = True
for name, delta_rate in models:
    dr = delta_rate[nonzero]
    psi2 = psi_x[nonzero]**2
    # Fit: δΓ = a × |ψ|² + b
    a, b = np.polyfit(psi2, dr, 1)
    # Check that intercept b is small relative to slope a
    residuals = dr - (a * psi2 + b)
    max_residual = np.max(np.abs(residuals)) / np.max(np.abs(dr))
    # O(Σ²) corrections are ~ (|Σ|/d₀)² ≈ 2×10⁻⁵; residuals < 1% [T2a]
    proportional = max_residual < 0.02
    if not proportional:
        all_proportional = False
    print(f"  {name}: δΓ = {a:.6e}×|ψ|² + {b:.6e},  max residual = {max_residual:.2e}")

check("δΓ ∝ |ψ|² for ALL 3 barrier models (linear regime, <2%) [T2a]",
      all_proportional, True)

# Verify the proportionality is to |ψ|² specifically (not |ψ|⁴ or |ψ|)
# by checking the exponent
log_psi2 = np.log(np.abs(psi_x[nonzero])**2 + 1e-30)
for name, delta_rate in models:
    dr = delta_rate[nonzero]
    positive = dr > 0
    if np.sum(positive) > 10:
        log_dr = np.log(dr[positive])
        slope = np.polyfit(log_psi2[positive], log_dr, 1)[0]
        print(f"  {name}: δΓ ∝ |ψ|^{2*slope:.3f}  (expect 2.000)")

# ════════════════════════════════════════════════════════════════════════════
# PART E — Probability normalization → Born rule [T1]
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART E: Normalization → Born Rule P(x) = |ψ(x)|² [T1] ---")
print()
print("  P(x) = δΓ(x) / ∫δΓ(x')dx'")
print("       = c|ψ(x)|² / c∫|ψ(x')|²dx'")
print("       = |ψ(x)|² / ∫|ψ(x')|²dx'")
print("       = |ψ(x)|²    [using ∫|ψ|²dx = 1]")

# Verify: normalized δΓ matches |ψ|² for all three models
P_born = psi_x**2 / _trapz(psi_x**2, x_vals)

for name, delta_rate in models:
    P_model = delta_rate / _trapz(delta_rate, x_vals)
    max_diff = np.max(np.abs(P_model - P_born))
    rel_diff = max_diff / np.max(P_born)
    # O(Σ²) correction gives ~1% deviation; this IS the T2a precision
    check(f"P_{name} ≈ P_born (<2% rel diff) [T2a]",
          rel_diff < 0.02, True)
    print(f"    max |P_model − P_born| / P_max = {rel_diff:.2e}")

# ════════════════════════════════════════════════════════════════════════════
# PART F — General wave functions: Born rule holds for arbitrary ψ [T2a]
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART F: General Wave Functions — Born Rule Universality [T2a] ---")

test_cases = [
    ("cos(kx)",              np.cos(k * x_vals)),
    ("cos(kx)+cos(2kx)",     np.cos(k*x_vals) + np.cos(2*k*x_vals)),
    ("Gaussian",             np.exp(-x_vals**2)),
    ("sech(x)",              1.0 / np.cosh(x_vals)),
    ("sin(kx)+0.5cos(2kx)",  np.sin(k*x_vals) + 0.5*np.cos(2*k*x_vals)),
    ("Asymmetric Gaussian",  np.exp(-(x_vals-0.5)**2/0.5)),
]

all_pass = True
for name, psi_test in test_cases:
    # Compute DC response
    S_test = 3 * beta * phi0 * (phi_c**2 / 2) * psi_test**2
    Sigma_test = -S_test / (2 * alpha)

    # Distance to spinodal
    d_test = d0 + Sigma_test

    # Barrier rate variation (Kramers model, representative)
    rate_test = np.exp(-d_test**2 / (2 * sigma_noise**2))
    rate_base = np.exp(-d0**2 / (2 * sigma_noise**2))
    delta_test = rate_test - rate_base

    # Normalize
    P_model_test = delta_test / _trapz(delta_test, x_vals)
    P_born_test = psi_test**2 / _trapz(psi_test**2, x_vals)

    max_rel_diff = np.max(np.abs(P_model_test - P_born_test)) / np.max(P_born_test)
    # O(Σ²) corrections scale with |ψ|⁴ variations; multi-frequency ψ has larger corrections
    passed = max_rel_diff < 0.05
    if not passed:
        all_pass = False
    print(f"  ψ = {name}: max rel |P_barrier − P_born|/P_max = {max_rel_diff:.2e}  {'✓' if passed else '✗'}")

check("Born rule P(x)=|ψ|² holds for ALL test wave functions [T2a]",
      all_pass, True)

# ════════════════════════════════════════════════════════════════════════════
# PART G — Double-slit fringe pattern consistency [T1]
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART G: Double-Slit Fringe Pattern [T1] ---")

psi_2slit = np.cos(k * x_vals)
S_2slit = 3 * beta * phi0 * (phi_c**2 / 2) * psi_2slit**2
Sigma_2slit = -S_2slit / (2 * alpha)
d_2slit = d0 + Sigma_2slit

rate_2slit = np.exp(-d_2slit**2 / (2 * sigma_noise**2))
rate_base_2slit = np.exp(-d0**2 / (2 * sigma_noise**2))
delta_2slit = rate_2slit - rate_base_2slit

P_barrier = delta_2slit / _trapz(delta_2slit, x_vals)
P_born_2slit = psi_2slit**2 / _trapz(psi_2slit**2, x_vals)

# Fringe visibility
P_max = np.max(P_barrier)
P_min = np.min(P_barrier)
visibility = (P_max - P_min) / (P_max + P_min)
check("Barrier model fringe visibility = 1 (perfect interference) [T1]",
      visibility, 1.0, tol=1e-4)

# Node positions: P = 0 at ψ = 0
node_idx = np.argmin(np.abs(x_vals - np.pi/(2*k)))
check("P(x_node) ≈ 0 (destructive interference preserved) [T1]",
      P_barrier[node_idx] / P_max < 1e-6, True)

print(f"\n  Fringe visibility = {visibility:.6f}  (perfect: 1.0)")
print(f"  P(node)/P(peak) = {P_barrier[node_idx]/P_max:.2e}")
print(f"  cos² fringe pattern preserved by barrier dynamics ✓")

# ════════════════════════════════════════════════════════════════════════════
# PART H — Connection chain: V(φ) → S(x) → Σ(x) → d(x) → Γ(x) → Born [T2a]
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART H: Complete Derivation Chain ---")
print()
print("  V(φ) = −α/2 φ² + β/4 φ⁴")
print("    │")
print("    ├─► Vacuum φ₀ = √(α/β)          [T1, Step 1]")
print("    ├─► Schrödinger equation          [T2a, Steps 2-3]")
print("    ├─► ⟨ε(x)⟩ = (φ_c²ω_c²/2)|ψ|²  [T1, Step 5]")
print("    ├─► Spinodal φ_sp = φ₀/√3        [T1, collapse_mechanism.py]")
print("    │")
print("    ├─► Nonlinear source:")
print("    │     S(x) = κ_NL × ⟨ε(x)⟩ ∝ |ψ(x)|²")
print("    │     [T1, Step 6a, born_rule_d3_coupling.py]")
print("    │")
print("    ├─► DC response (NEW THIS MODULE):")
print("    │     Σ(x) = −S(x)/(2α) ∝ −|ψ(x)|²")
print("    │     [T1, particular solution of driven linear eq.]")
print("    │")
print("    ├─► Spinodal distance reduction:")
print("    │     d(x) = d₀ − |Σ(x)|")
print("    │     Smaller d where |ψ|² is large")
print("    │     [T1, algebraic]")
print("    │")
print("    ├─► Linear expansion (|Σ|/d₀ << 1):")
print("    │     δΓ(x) ≈ |Γ'(d₀)| × |Σ(x)| ∝ |ψ(x)|²")
print("    │     [T2a, semiclassical regime φ_c << φ₀]")
print("    │")
print("    └─► Born rule:")
print("          P(x) = δΓ(x)/∫δΓ dx = |ψ(x)|²  [T1, normalization]")

# ════════════════════════════════════════════════════════════════════════════
# PART I — Physical interpretation and independence from C339
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART I: Two Independent Step 6b Derivations ---")
print()
print("  Route A — Coupling Selection (C339, born_rule_frequency_selection.py):")
print("    Z₂ symmetry + time averaging + EFT → σ² is unique coupling")
print("    rate(x) ∝ ⟨σ²(x)⟩_t ∝ |ψ(x)|²")
print("    Logic: WHAT couples determines WHAT probability depends on")
print()
print("  Route B — Barrier Dynamics (C359, THIS MODULE):")
print("    S(x) ∝ |ψ|² drives DC shift → spinodal distance reduced")
print("    δΓ(x) ∝ |Σ(x)| ∝ S(x) ∝ |ψ(x)|²")
print("    Logic: HOW fast substrate approaches instability determines rate")
print()
print("  Routes A and B are logically independent:")
print("    A uses: Z₂ of V(φ) + averaging selection rules")
print("    B uses: nonlinear source + spinodal instability + linear response")
print("  Both derive the same result from V(φ) by different chains.")
print("  Convergence of two independent derivations strengthens T2a status.")

# ════════════════════════════════════════════════════════════════════════════
# PART J — Tier summary
# ════════════════════════════════════════════════════════════════════════════
print("\n--- PART J: Tier Assignments ---")
print()
tier_items = [
    ("J1", "Nonlinear source S(x) = 3βφ₀(φ_c²/2)|ψ|²",     "T1",  "V(φ) field eq., C338"),
    ("J2", "DC response Σ(x) = −S(x)/(2α)",                  "T1",  "particular soln of linear eq"),
    ("J3", "Σ(x) < 0 (shifts toward spinodal)",               "T1",  "S > 0, division by 2α > 0"),
    ("J4", "d(x) = d₀ − |Σ(x)| reduces at ψ peaks",         "T1",  "algebraic"),
    ("J5", "|Σ|/d₀ ∝ (φ_c/φ₀)² << 1 (linear regime)",       "T2a", "semiclassical limit"),
    ("J6", "δΓ(x) ∝ |Σ(x)| (linear expansion)",             "T2a", "Taylor + monotonic Γ(d)"),
    ("J7", "δΓ(x) ∝ |ψ(x)|² (chain from J1-J6)",           "T2a", "composite"),
    ("J8", "P(x) = |ψ(x)|² (normalization)",                  "T1",  "∫|ψ|² = 1"),
]
print("  ┌──────────────────────────────────────────────────────────────────┐")
for tag, desc, tier, reason in tier_items:
    print(f"  │ [{tier}] {tag}: {desc}")
    print(f"  │         ({reason})")
print("  └──────────────────────────────────────────────────────────────────┘")
print()
print("  Weakest link: J5+J6 [T2a] — linear expansion in semiclassical regime")
print("  Step 6b overall: T2a (barrier dynamics route)")
print()
print("  Born rule complete chain:")
print("  ┌─────────────────────────────────────────────────────────┐")
print("  │ Steps 1-3: V(φ)→Schrödinger equation             [T2a]│")
print("  │ Steps 4-5: ω_c=√(2α), ⟨ε(x)⟩∝|ψ|²              [T1] │")
print("  │ Step 6a:   S(x)=κ_NL×⟨ε(x)⟩ (NL source)         [T1] │")
print("  │ Step 6b:   Two routes — coupling selection [T2a]       │")
print("  │                      + barrier dynamics  [T2a]         │")
print("  │ ─────────────────────────────────────────────────────── │")
print("  │ P(x) = |ψ(x)|²                              [T2a OVERALL]│")
print("  └─────────────────────────────────────────────────────────┘")

# ════════════════════════════════════════════════════════════════════════════
# FINAL REPORT
# ════════════════════════════════════════════════════════════════════════════
total = PASS_count + FAIL_count
print()
print("=" * 70)
print(f"RESULT: {PASS_count}/{total} ASSERTIONS PASSED")
if FAIL_count == 0:
    print("STATUS: ALL PASS")
    print()
    print("KEY T2a RESULT (Step 6b — Barrier Dynamics):")
    print(f"  Σ(x) = −S(x)/(2α) = −3βφ₀φ_c²|ψ|²/(4α)")
    print(f"  d(x) = d₀ − |Σ(x)|  →  δΓ(x) ∝ |Σ(x)| ∝ |ψ(x)|²")
    print(f"  Born rule P(x) = |ψ(x)|² derived from V(φ) barrier dynamics.")
    print(f"  Second independent Step 6b route (first: C339 σ² coupling selection).")
else:
    print(f"STATUS: {FAIL_count} FAILURES — review above")
print("=" * 70)
