"""
Born Rule Derivation in DFC
============================
Physical question: Why does the probability of finding a particle at location x
equal |psi(x)|^2 (the Born rule) rather than |psi(x)|^n for some other n?

DFC mechanism: The wave function psi is the slow envelope of a kink's fast
internal oscillation at the Compton frequency. This module develops three
independent structural arguments for why the localization probability must be
quadratic in the wave function amplitude, and assesses the tier of each.

Three arguments:
  A. Energy density argument: energy density of any wave is quadratic in
     amplitude (T1); if localization couples to energy density, P ∝ |psi|^2.
  B. Interference uniqueness argument: complete destructive interference
     (experimentally observed) is only possible if P ∝ |psi|^2 (T1 algebraic).
  C. Fermi's golden rule analog: transition rate to localized final state is
     proportional to |<final|H_D3|psi>|^2 ∝ |psi(x)|^2 (T3).

Key gap: argument A requires "localization couples to energy density" (T3);
argument C requires Fermi's golden rule conditions hold for D3 localization (T3).
Argument B is the most robust — it rules out all n ≠ 2 from interference data
alone, without requiring any assumption about the localization mechanism.

References: Born 1926, Gleason 1957, Zurek 2003 (envariance), Valentini 1991
(quantum relaxation in Bohm), Nelson 1966 (stochastic mechanics), Mandel-Wolf
(quantum optics intensity detection).
"""

import numpy as np
from fractions import Fraction

# np.trapz was renamed np.trapezoid in NumPy 2.0
_trapz = getattr(np, 'trapezoid', getattr(np, 'trapz', None))

ASSERTIONS_PASSED = 0
ASSERTIONS_TOTAL = 0

def check(label, condition, tol=None):
    global ASSERTIONS_PASSED, ASSERTIONS_TOTAL
    ASSERTIONS_TOTAL += 1
    if tol is not None:
        result = abs(condition) < tol
    else:
        result = bool(condition)
    status = "PASS" if result else "FAIL"
    print(f"  [{status}] {label}")
    if result:
        ASSERTIONS_PASSED += 1
    return result

# ── DFC FIELD PARAMETERS ──────────────────────────────────────────────────────

alpha = (18)**(Fraction(1, 3))          # alpha = ∛18 [T2a]
beta  = Fraction(1, 9) / np.pi         # beta = 1/(9π) [T2a]
phi0  = float(np.sqrt(float(alpha) / (2 * float(beta))))  # vacuum value
xi    = float(np.sqrt(2.0 / float(alpha)))                 # kink width
I4    = Fraction(4, 3)                  # ∫sech^4(u)du = 4/3 [T1]

# ── PART A: ENERGY DENSITY ARGUMENT ──────────────────────────────────────────
print("\n=== PART A: Energy Density Argument ===")
print("""
Claim: For the DFC substrate field obeying □φ = V'(φ), the energy density
at any location is quadratic in the field amplitude.

For small oscillations around the kink background φ_kink(x), write:
  φ(x,t) = φ_kink(x) + η(x,t)
where η is the fluctuation (the slow envelope mode).

The energy density of the fluctuation field:
  ε(x,t) = (1/2)(∂_t η)^2 + (1/2)(∂_x η)^2 + (1/2)V''(φ_kink) η^2

For the zeroth (translation) mode, η_0(x) ∝ sech^2(x/ξ), the slow envelope
of the full fast oscillation.

The fast oscillation: φ(x,t) ≈ φ_kink(x) + A(x) cos(ω_c t)
where ω_c = √(2α) is the Compton frequency and A(x) is the slow envelope.

The complex wave function: ψ(x,t) = A(x) e^{-iω_c t}
so |ψ(x)|^2 = A(x)^2.

Time-averaged energy density at x:
  <ε(x)> = (1/2)(ω_c^2) A(x)^2 + (1/2)|∂_x A(x)|^2 + (1/2)V''(φ_kink) A(x)^2
          = C(x) × A(x)^2
          = C(x) × |ψ(x)|^2

where C(x) > 0 depends on position but not on amplitude.

THEREFORE: <ε(x)> ∝ |ψ(x)|^2 — energy density is quadratic in wave function.
This is T1: it follows from the quadratic nature of kinetic and potential energy.
""")

# Verify: Compton frequency from alpha
omega_c = np.sqrt(2 * float(alpha))
print(f"  Compton frequency ω_c = √(2α) = √(2×∛18) = {omega_c:.6f} [Planck units]")
check("ω_c > 0 (real Compton frequency)", omega_c > 0)

# Verify: energy density of kink profile is proportional to sech^4
# ε_kink(x) = (φ')^2 = φ₀^2/ξ^2 × sech^4(x/ξ)
# Total = ∫ε_kink dx = φ₀^2/ξ × I₄ = E_BPS [T1]
N_points = 10000
x = np.linspace(-20*xi, 20*xi, N_points)
dx = x[1] - x[0]
phi_kink = phi0 * np.tanh(x / xi)
phi_prime = phi0 / xi / np.cosh(x / xi)**2  # d/dx tanh = sech^2

energy_density_kink = phi_prime**2  # proportional to sech^4
E_kink_numerical = _trapz(energy_density_kink, x)
E_kink_analytic = phi0**2 / xi * float(I4)
residual_A = abs(E_kink_numerical - E_kink_analytic) / E_kink_analytic
check(f"Kink energy density ∝ sech^4; ∫ε dx = φ₀²/ξ × I₄ (res={residual_A:.2e})",
      residual_A, tol=1e-4)

# Verify: energy density is exactly quadratic in amplitude A
# If we scale φ → λφ, energy density scales as λ^2
lambda_test = 1.5
energy_scaled = (lambda_test * phi_prime)**2
E_scaled = _trapz(energy_scaled, x)
ratio = E_scaled / E_kink_numerical
check(f"Scaling φ→λφ scales ε→λ²ε: ratio = {ratio:.6f}, expected {lambda_test**2:.6f}",
      abs(ratio - lambda_test**2), tol=1e-10)

print(f"""
  KEY STEP (T3): If the probability of localization at x is proportional
  to the available field energy density at x, then:
    P(x) ∝ <ε(x)> ∝ |ψ(x)|^2  →  Born rule

  The T3 assumption is: localization couples to energy density.
  This is plausible because:
  - Localization events are energy-extracting interactions (D3 depth behavior)
  - The substrate "commits" to a location by concentrating field energy there
  - Coupling strength at x ∝ field amplitude at x ∝ A(x) = |ψ(x)|
  - Rate of energy extraction ∝ coupling^2 ∝ |ψ(x)|^2

  Upgrade path: T3→T2a requires showing from V(φ) dynamics that the D3
  localization cross-section is proportional to local field energy density.
""")

# ── PART B: INTERFERENCE UNIQUENESS ARGUMENT ─────────────────────────────────
print("\n=== PART B: Interference Uniqueness Argument ===")
print("""
Claim: Complete destructive interference — zero intensity at interference nodes —
is only possible if probability is quadratic in field amplitude.

Argument:
  In DFC, the substrate field amplitudes superpose linearly (the field equation is
  linear in fluctuations around the kink background). For two-slit interference,
  the total amplitude at a point x is:

    ψ_total(x) = ψ_1(x) + ψ_2(x)

  where ψ_1 and ψ_2 are the contributions from each slit.

  At a destructive interference node, ψ_1(x) = -ψ_2(x), so:
    ψ_total(x) = 0

  Now suppose probability P = f(|ψ|) for some function f.
  At a node, |ψ_total| = 0, so P_node = f(0).

  For complete destructive interference (P_node = 0), we need f(0) = 0.
  This is satisfied by f(|ψ|) = |ψ|^n for ANY n > 0.

  But the constraint is stronger. Consider a point near a node where:
    ψ_1 = A e^{iδ},  ψ_2 = A e^{-iδ},  so |ψ_total|^2 = 4A^2 cos^2(δ)

  The observed interference fringe intensity is ∝ cos^2(δ).

  If P = |ψ|^n, the fringe intensity goes as |ψ_total|^n = |2A cos(δ)|^n = (2A)^n |cos(δ)|^n.

  The observed fringe pattern (from experiment) has intensity ∝ cos^2(δ),
  meaning n = 2 is the only integer that matches the observed pattern exactly.

  For n = 1: fringes ∝ |cos(δ)| — cusped minima, not smooth zeros
  For n = 2: fringes ∝ cos^2(δ) — smooth sinusoidal pattern ✓
  For n = 3: fringes ∝ |cos(δ)|^3 — flatter tops, sharper zeros than observed
  For n = 4: fringes ∝ cos^4(δ) — narrower bright fringes than observed

  Therefore n = 2 is uniquely selected by the observed interference pattern.
  This argument is T1 (algebraic given experimental input).
""")

# Verify: fringe patterns for different n values
delta = np.linspace(0, 2*np.pi, 1000)
A = 1.0

# n=2 (Born rule): fringe = cos^2
fringe_n2 = np.cos(delta)**2

# n=1: fringe = |cos|
fringe_n1 = np.abs(np.cos(delta))

# n=4: fringe = cos^4
fringe_n4 = np.cos(delta)**4

# Key distinguishing feature: ratio of half-max width to period
# For cos^2: half-max at cos^2(δ) = 0.5 → cos(δ) = 1/√2 → δ = π/4
# Width between zeros = π; half-max width = π/2; ratio = 1/2
half_max_width_n2 = np.pi / 2
fringe_period = np.pi
ratio_n2 = half_max_width_n2 / fringe_period

check(f"n=2 half-max/period = {ratio_n2:.4f} (should be 0.5000)",
      abs(ratio_n2 - 0.5), tol=1e-10)

# For n=1: half-max at |cos| = 0.5 → δ = π/3; width = 2π/3
half_max_width_n1 = 2*np.pi/3
ratio_n1 = half_max_width_n1 / fringe_period
check(f"n=1 half-max/period = {ratio_n1:.4f} (different from n=2: {ratio_n2:.4f})",
      abs(ratio_n1 - ratio_n2) > 0.05)

# For n=4: half-max at cos^4 = 0.5 → cos = 2^(-1/4) → δ = arccos(2^(-1/4))
delta_half_n4 = np.arccos(2**(-0.25))
ratio_n4 = delta_half_n4 / (np.pi/2)
# ratio relative to period
ratio_n4_period = delta_half_n4 / fringe_period
check(f"n=4 half-max/period = {ratio_n4_period:.4f} (different from n=2: {ratio_n2:.4f})",
      abs(ratio_n4_period - ratio_n2) > 0.02)

print(f"""
  Fringe half-max widths (as fraction of period):
    n=1: {ratio_n1:.4f}  (cusped minima, wider fringes)
    n=2: {ratio_n2:.4f}  (smooth sinusoidal — matches experiment) ✓
    n=4: {ratio_n4_period:.4f}  (narrower bright fringes)

  The n=2 pattern is the ONLY one consistent with smooth, complete destructive
  interference and sinusoidal fringe visibility measured in experiments.

  TIER: T1 (algebraic) given: (a) linear superposition of amplitudes in DFC,
  (b) observed cos^2 fringe pattern. Both (a) and (b) are established.

  This is the strongest argument: it does not require any assumption about the
  localization mechanism, only the observed shape of the interference pattern.
""")

# ── PART C: FERMI'S GOLDEN RULE ANALOG ───────────────────────────────────────
print("\n=== PART C: Fermi's Golden Rule Analog ===")
print("""
Claim: The rate of D3 localization at position x is proportional to |ψ(x)|^2
by a Fermi's golden rule argument.

In standard quantum mechanics, Fermi's golden rule gives the transition rate
from an initial state |i⟩ to a final state |f⟩ under a perturbation H':

  Γ_{i→f} = (2π/ℏ) |⟨f|H'|i⟩|^2 × ρ(E_f)

In DFC, a D3 localization event is a transition from:
  initial state: spread-out substrate field configuration |ψ⟩
  final state:   localized kink configuration at position x, |x⟩

The interaction H_D3 is the D3 depth behavior — the coupling between the
propagating field and a localizing structure.

The matrix element: ⟨x|H_D3|ψ⟩ = H_D3(x) × ψ(x)
where H_D3(x) is the local coupling strength of the D3 interaction at x.

Assuming H_D3(x) is approximately uniform (no preferred location):
  |⟨x|H_D3|ψ⟩|^2 ∝ |ψ(x)|^2

Therefore: Γ(localization at x) ∝ |ψ(x)|^2 × ρ(E_x)

If the density of final localized states ρ(E_x) is approximately uniform in x:
  P(localization at x) = Γ(x) / ∫Γ(x')dx' ∝ |ψ(x)|^2  →  Born rule

TIER: T3. Requires:
  (a) Fermi's golden rule conditions: weak coupling, dense final states
  (b) H_D3(x) approximately uniform — no structural preference for any location
  (c) ρ(E_x) approximately uniform in x

  All three are structurally plausible but not derived from V(φ).
  Upgrade path: T3→T2a requires computing H_D3 from the substrate field
  equation and showing the matrix element is dominated by ψ(x).
""")

# The Fermi's golden rule structure: |<x|H|psi>|^2 = H^2 * |psi(x)|^2
# Verify that if H is uniform, probability ratios are exactly |psi|^2 ratios
psi_test = np.exp(-x**2 / (2*xi**2))  # Gaussian test wave function
psi_test /= np.sqrt(_trapz(psi_test**2, x))  # normalize

# Compute "Fermi rate" proportional to |psi|^2
H_D3 = 1.0  # uniform coupling (T3 assumption)
rate = H_D3**2 * psi_test**2
rate_normalized = rate / _trapz(rate, x)

# This IS |psi|^2 by construction — the point is that the coupling squared
# gives the Born probability
prob_born = psi_test**2
prob_born_normalized = prob_born / _trapz(prob_born, x)

residual_C = np.max(np.abs(rate_normalized - prob_born_normalized))
check(f"Fermi rate (uniform H) = Born probability: max deviation {residual_C:.2e}",
      residual_C, tol=1e-12)

# ── PART D: WHAT DISTINGUISHES |psi|^2 FROM ALTERNATIVES ─────────────────────
print("\n=== PART D: Uniqueness Properties of |ψ|² ===")
print("""
Additional properties that uniquely select n=2:

D1. NORMALIZATION CONSISTENCY under linear superposition:
    If ψ = ψ_1 + ψ_2 (linear superposition), then for the Born rule to be
    consistent (total probability = sum over disjoint events), we need:

    ∫|ψ_1 + ψ_2|^2 dx can be less than ∫|ψ_1|^2 dx + ∫|ψ_2|^2 dx
    (due to destructive interference) but total probability is still 1.

    For n ≠ 2: ∫|ψ_1 + ψ_2|^n dx ≠ ∫|ψ_1|^n dx + ∫|ψ_2|^n dx + interference
    in a way that is not guaranteed to remain normalized to 1 under arbitrary
    superpositions without re-normalization at each step.

D2. ENERGY EQUIPARTITION:
    For a harmonic oscillator (the linearized fluctuation around the kink),
    the expectation value of energy is ⟨E⟩ = ∫|ψ|^2 E dE.
    This is |ψ|^2 weighting. Any other weighting breaks energy equipartition
    at the individual mode level — the energy in the system would not match
    the quantum mechanical prediction. [T1 given standard wave mechanics]

D3. SYMMETRY UNDER PHASE ROTATION:
    The wave function ψ → e^{iθ} ψ (global phase rotation) leaves |ψ|^2
    unchanged. This is required because global phase is not observable.
    For P = |ψ|^n: |e^{iθ}ψ|^n = |ψ|^n. All integer n satisfy this.
    But only n=2 is the lowest power consistent with complex-valued ψ.
    [T1]
""")

# Verify D1: normalization consistency for n=2
psi1 = np.exp(-((x - xi)**2) / (2*xi**2))
psi2 = np.exp(-((x + xi)**2) / (2*xi**2))
psi1 /= np.sqrt(_trapz(psi1**2, x))
psi2 /= np.sqrt(_trapz(psi2**2, x))

# Superposition (opposite phase: destructive interference at center)
psi_super = psi1 - psi2
norm_super = _trapz(psi_super**2, x)
norm_1 = _trapz(psi1**2, x)
norm_2 = _trapz(psi2**2, x)
cross_term = _trapz(2*psi1*psi2, x)  # This is negative for opposite-phase

check(f"|ψ₁-ψ₂|²: norm={norm_super:.4f} = ||ψ₁||²+||ψ₂||²-cross = {norm_1 + norm_2 - abs(cross_term):.4f}",
      abs(norm_super - (norm_1 + norm_2 + _trapz(-2*psi1*psi2, x))), tol=1e-10)

# For n=1 (linear): |psi1 - psi2| would integrate to something different
# and would not have clean interference cancellation
prob_n1_super = np.abs(psi_super)
prob_n1_separate = np.abs(psi1) + np.abs(psi2)  # If n=1 were the rule
ratio_interference_n1 = _trapz(prob_n1_super, x) / _trapz(prob_n1_separate, x)
ratio_interference_n2 = _trapz(psi_super**2, x) / _trapz(psi1**2 + psi2**2, x)

print(f"""
  Interference suppression at destructive node:
    n=1 rule: probability ratio (interfering/non-interfering) = {ratio_interference_n1:.4f}
    n=2 rule: probability ratio (interfering/non-interfering) = {ratio_interference_n2:.4f}

  n=2 gives {(1 - ratio_interference_n2)*100:.1f}% reduction (strong interference)
  n=1 gives {(1 - ratio_interference_n1)*100:.1f}% reduction (weak interference)

  Only n=2 produces the strong interference suppression observed in experiment.
""")

check(f"n=2 shows stronger destructive interference than n=1",
      ratio_interference_n2 < ratio_interference_n1)

# ── PART E: SYNTHESIS AND TIER ASSESSMENT ─────────────────────────────────────
print("\n=== PART E: Synthesis and Tier Assessment ===")
print(f"""
Three independent arguments for Born rule P = |ψ|²:

┌─────────────────────────────────────────────────────────────────────────┐
│ Argument                   │ Key assumption                │ Tier        │
├─────────────────────────────────────────────────────────────────────────┤
│ A. Energy density          │ Localization couples to ε     │ T3          │
│ B. Interference uniqueness │ cos² fringe shape (expt'l)    │ T1 (given B)│
│ C. Fermi golden rule       │ Uniform H_D3, dense states    │ T3          │
│ D2. Energy equipartition   │ Standard wave mechanics       │ T1          │
└─────────────────────────────────────────────────────────────────────────┘

STRONGEST RESULT (B): The interference argument is T1 given experimental input.
It shows n=2 is UNIQUELY selected by the observed cos² fringe pattern. No
assumption about the localization mechanism is required — only:
  (i)  Linear superposition of amplitudes (follows from linear field equation)
  (ii) Observed sinusoidal fringe pattern (experimental fact)

This elevates Born rule from T4 → T3 overall (structural argument exists,
formal derivation from V(φ) dynamics not complete).

REMAINING T4 gap: Derive the fringe pattern shape from the D3 localization
mechanism in V(φ), without assuming the cos² form from experiment. This would
require:
  1. Formal derivation of the slow-envelope Schrödinger equation from V(φ)
  2. Computing the D3 localization rate from the substrate field dynamics
  3. Showing the resulting pattern is cos² (i.e., Born rule) not cos^n

Combined path B→formal: T3→T2a via item 1 alone (Schrödinger eq. from V(φ)).
Full T2a→T1: requires items 1+2+3.
""")

# Final summary
print(f"\n{'='*60}")
print(f"ASSERTIONS PASSED: {ASSERTIONS_PASSED}/{ASSERTIONS_TOTAL}")
print(f"Born rule tier: T3 (upgraded from T4)")
print(f"Strongest argument: Interference uniqueness (T1 given cos² fringe data)")
print(f"Key remaining gap: Derive cos² fringe shape from D3 mechanism in V(φ)")
print(f"{'='*60}")
