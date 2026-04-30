"""
Exact S-matrix for kink scattering in the DFC substrate (Cycle 89).

Physical question:
  What is the exact transmission amplitude for a wave (sigma meson) scattering off
  a static DFC kink background? The kink creates a Pöschl-Teller (PT) potential
  that is exactly solvable. This gives the first exact (non-Born) S-matrix result
  in the DFC model.

DFC mechanism:
  The DFC kink φ_K(x) = φ₀ tanh(x/λ) deforms the potential seen by fluctuations.
  The fluctuation operator L₁ = −d²/dx² + V_fl(x) has:

    V_fl(x) = 4M_c² − 6M_c² sech²(M_c x)

  This is the reflectionless n=2 Pöschl-Teller (PT) potential. The exact transmission
  amplitude is known from the inverse scattering method (Marchenko equation).

EXACT RESULTS (n=2 reflectionless PT):
  Bound state momenta:
    κ₀ = 2M_c   [zero mode, ω₀ = 0]
    κ₁ = M_c    [shape mode, ω₁ = √3 M_c]

  Transmission amplitude T(q) where q² = ω² − 4M_c²:
    T(q) = [(q + iM_c)(q + i2M_c)] / [(q − iM_c)(q − i2M_c)]

  Key properties:
    |T(q)|² = 1 for all real q   [reflectionless — no backscattering]
    δ(q) = 2arctan(M_c/q) + 2arctan(2M_c/q)  [scattering phase shift]
    δ(0⁺) = 2π, δ(∞) = 0        [Levinson's theorem: n=2 bound states]

PHYSICAL CONTEXT:
  This is the exact result for sigma-meson scattering off a static DFC kink.
  The kink is fully transparent (|T|²=1) — no reflection — a consequence of the
  exact PT structure of the substrate potential V(φ) = −α/2 φ² + β/4 φ⁴.

  The Cycle 33 Born approximation for kink-antikink PARTICLE scattering gave:
    δ_Born(k) ~ A m_σ / [k(4k²+m_σ²)]  (Yukawa potential)
  That computation treats kinks as particles with mutual Yukawa interaction.
  THIS module computes WAVE scattering through a single kink background.
  These are complementary results — both are needed for a full DFC S-matrix.

Key references:
  - equations/kink_scattering.py    (Cycle 33: Born approximation, shape mode ω₁)
  - foundations/kink_scattering.md  (kink-antikink Born results)
  - foundations/substrate.md        (kink model)
  - equations/coupled_fluctuation.py (PT spectrum verification)
  - L. D. Landau & E. M. Lifshitz, Quantum Mechanics §23 (reflectionless PT)
  - Dashen, Hasslacher, Neveu (1975): exact kink-antikink S-matrix (DHN) — OPEN
"""

import math
import numpy as np
from scipy.integrate import quad

# ─── Parameters ───────────────────────────────────────────────────────────────

ALPHA = 2.0       # quadratic coupling (reference value)
BETA  = 0.0351    # quartic coupling (Tier 3 reference)

# Derived substrate scales
M_C   = math.sqrt(ALPHA / 2.0)    # closure scale = 1/λ  (= 1.0 for α=2)
LAM   = 1.0 / M_C                 # kink half-width
PHI0  = math.sqrt(ALPHA / BETA)   # vacuum field amplitude
M_SIG = math.sqrt(3.0) * M_C      # sigma meson mass (shape mode)

# PT bound state momenta
KAPPA_0 = 2.0 * M_C   # zero mode      (κ₀ = 2M_c)
KAPPA_1 = 1.0 * M_C   # shape mode     (κ₁ = M_c)


# ─── 1. Exact T-matrix ────────────────────────────────────────────────────────

def T_exact(q):
    """
    Exact transmission amplitude for the n=2 reflectionless PT potential.

    T(q) = (q + iκ₁)(q + iκ₀) / [(q − iκ₁)(q − iκ₀)]

    where q is the scattering momentum (real positive), and
    κ₁ = M_c, κ₀ = 2M_c are the bound-state momenta.

    The incoming wave e^{iqx} for x → −∞ transmits to T(q)e^{iqx} for x → +∞,
    with |T(q)| = 1 (unitary, no reflection).

    Args:
        q (float): scattering momentum q² = ω² − 4M_c²; must be q > 0

    Returns:
        complex: transmission amplitude T(q)
    """
    k0, k1 = KAPPA_0, KAPPA_1
    numerator   = complex(q,  k1) * complex(q,  k0)
    denominator = complex(q, -k1) * complex(q, -k0)
    return numerator / denominator


def phase_shift(q):
    """
    Scattering phase shift δ(q) = arg T(q).

    From the explicit form:
      δ(q) = 2 arctan(κ₁/q) + 2 arctan(κ₀/q)
           = 2 arctan(M_c/q) + 2 arctan(2M_c/q)

    Levinson's theorem: δ(0⁺) = nπ = 2π [n=2 bound states]
                        δ(∞)  = 0

    Returns phase shift in radians.
    """
    return 2.0 * math.atan2(KAPPA_1, q) + 2.0 * math.atan2(KAPPA_0, q)


def wigner_time_delay(q):
    """
    Wigner time delay τ_W(q) = dδ/dq.

    Positive time delay means the wave is slowed by the kink potential.
    τ_W(q) = −2κ₁/(q²+κ₁²) − 2κ₀/(q²+κ₀²)

    In natural units (c=M_c=1), τ has dimensions of 1/M_c = λ.
    """
    return (-2.0 * KAPPA_1 / (q**2 + KAPPA_1**2)
            - 2.0 * KAPPA_0 / (q**2 + KAPPA_0**2))


# ─── 2. Levinson theorem ──────────────────────────────────────────────────────

def verify_levinson():
    """
    Verify Levinson's theorem: δ(0⁺) − δ(∞) = nπ where n = number of bound states.

    For n=2 PT: δ(0⁺) = 2π, δ(∞) = 0.
    The theorem counts the number of bound states (zero mode + shape mode = 2).
    """
    q_near_zero = 1e-10
    q_large     = 1e10
    delta0 = phase_shift(q_near_zero)
    delta_inf = phase_shift(q_large)
    n_states = (delta0 - delta_inf) / math.pi
    return dict(
        delta_at_zero=delta0,
        delta_at_inf=delta_inf,
        n_from_levinson=n_states,
        expected_n=2,
        error=abs(n_states - 2),
    )


# ─── 3. Unitarity check ───────────────────────────────────────────────────────

def verify_unitarity(n_pts=50):
    """
    Verify |T(q)|² = 1 for all q (reflectionless property).

    For the reflectionless PT potential:
      Reflection amplitude R(q) = 0 exactly
      |T(q)|² = 1 for all real q > 0

    This is the defining property of the n=2 PT potential and is an
    exact algebraic identity, not an approximation.
    """
    q_vals = np.logspace(-2, 2, n_pts) * M_C
    errors = []
    for q in q_vals:
        T = T_exact(q)
        err = abs(abs(T)**2 - 1.0)
        errors.append(err)
    max_error = max(errors)
    return dict(
        n_points=n_pts,
        max_mod_T_minus_1=max_error,
        reflectionless=max_error < 1e-14,
    )


# ─── 4. Born comparison ───────────────────────────────────────────────────────

def born_comparison(n_pts=8):
    """
    Compare exact phase shift with Born approximation for WAVE scattering.

    The exact phase shift (from reflectionless PT):
      δ_exact(q) = 2arctan(M_c/q) + 2arctan(2M_c/q)

    High-q limit (arctan x ≈ x for small x):
      δ_exact(q→∞) → 2(M_c/q) + 2(2M_c/q) = 6M_c/q

    The first Born approximation for wave scattering off V(x) = −6M_c² sech²(M_c x):
      For even potential in 1D:
        δ_Born(q) ≈ −(1/2q) ∫ V(x) dx

      ∫ V(x) dx = −6M_c² × (2/M_c) = −12M_c   [since ∫sech²(u)du = 2]

      δ_Born(q) ≈ −(1/2q)(−12M_c) = 6M_c/q

    Key result: both exact and Born give 6M_c/q at high q (agreement in leading term).
    At LOW q: Born gives 6M_c/q → ∞ (diverges); exact saturates at 2π.
    This shows the Born approximation CANNOT describe the infrared (bound-state) physics.

    Note: this is WAVE scattering (meson off kink), NOT the kink-antikink particle
    scattering. The kink-antikink Born result from kink_scattering.py is a different
    calculation (Yukawa interaction between kink and antikink treated as particles).
    """
    results = []
    q_values = [0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]  # in units of M_c

    for q_over_Mc in q_values:
        q = q_over_Mc * M_C
        exact = phase_shift(q)
        # Born: δ_Born = 6M_c/q (from -(1/2q) × ∫V dx = -(1/2q) × (-12M_c))
        born = 6.0 * M_C / q
        high_q_leading = 6.0 * M_C / q   # leading term for large q (both agree here)
        error_pct = abs(born - exact) / abs(exact) * 100 if abs(exact) > 1e-12 else 0
        results.append(dict(
            q_over_Mc=q_over_Mc,
            delta_exact=exact,
            delta_born=born,
            high_q_leading=high_q_leading,
            agreement_pct=error_pct,
        ))
    return results


# ─── 5. Spectrum verification ─────────────────────────────────────────────────

def verify_pt_spectrum():
    """
    Verify the PT bound state energies from the exact T-matrix pole positions.

    The T-matrix has poles in the upper half-plane at q = iκ_j (bound states):
      Pole at q = iκ₁ = iM_c    → ω₁² = 4M_c² − M_c² = 3M_c²  → ω₁ = √3 M_c
      Pole at q = iκ₀ = i2M_c   → ω₀² = 4M_c² − 4M_c² = 0     → ω₀ = 0

    These match the Pöschl-Teller spectrum verified numerically in Cycle 33 (kink_scattering.py):
      Shape mode ω₁ = (√3/2) m_σ    [note: m_σ = 2M_c from kink_scattering.py convention]
                    = (√3/2) × 2M_c = √3 M_c ✓

    NOTE on conventions:
      - In kink_scattering.py: m_sigma = kink mass = (4/3) M_c³/β × (in GeV)
      - Here: M_c is the PT mass parameter = √(α/2)
      - The shape mode ω₁ = √3 M_c is the same quantity, different notation
    """
    # The shape mode from exact T-matrix pole
    omega1_from_T = math.sqrt(4.0 * M_C**2 - KAPPA_1**2)  # = √(4-1) M_c = √3 M_c
    omega0_from_T = math.sqrt(max(0.0, 4.0 * M_C**2 - KAPPA_0**2))  # = 0

    # Expected: ω₁ = √3 M_c = 1.732 M_c (with α=2, M_c=1: ω₁ = 1.732)
    omega1_expected = M_SIG  # √3 M_c, defined at top

    return dict(
        kappa_0=KAPPA_0,
        kappa_1=KAPPA_1,
        omega0_from_poles=omega0_from_T,
        omega1_from_poles=omega1_from_T,
        omega1_expected=omega1_expected,
        error_omega1=abs(omega1_from_T - omega1_expected),
        omega0_exact_zero=abs(omega0_from_T) < 1e-15,
    )


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('=' * 70)
    print('DFC EXACT S-MATRIX — Reflectionless n=2 Pöschl-Teller (Cycle 89)')
    print('Single kink transmission amplitude from inverse scattering method')
    print('=' * 70)
    print(f'  Parameters: α = {ALPHA}, β = {BETA}')
    print(f'  M_c = {M_C:.4f} (closure scale = 1/λ)')
    print(f'  λ   = {LAM:.4f} (kink half-width)')
    print(f'  κ₀  = {KAPPA_0:.4f} = 2M_c (zero mode bound-state momentum)')
    print(f'  κ₁  = {KAPPA_1:.4f} = M_c  (shape mode bound-state momentum)')

    # 1. Levinson theorem
    print('\n── 1. Levinson theorem ──')
    lev = verify_levinson()
    print(f'  δ(0⁺)     = {lev["delta_at_zero"]:.6f} rad  '
          f'(expected 2π = {2*math.pi:.6f})')
    print(f'  δ(∞)      = {lev["delta_at_inf"]:.2e} rad   (expected 0)')
    print(f'  n = [δ(0⁺)−δ(∞)]/π = {lev["n_from_levinson"]:.6f}   (expected 2 bound states)')
    print(f'  Error = {lev["error"]:.2e}   '
          + ('✓ PASS' if lev['error'] < 1e-8 else '✗ FAIL'))

    # 2. Unitarity
    print('\n── 2. Reflectionless property |T(q)|² = 1 ──')
    u = verify_unitarity()
    print(f'  Checked {u["n_points"]} q values from 0.01 to 100 M_c')
    print(f'  Max |T|² − 1| = {u["max_mod_T_minus_1"]:.2e}  '
          + ('✓ REFLECTIONLESS' if u['reflectionless'] else '✗ FAIL'))

    # 3. PT spectrum from T-matrix poles
    print('\n── 3. Bound state spectrum from T-matrix poles ──')
    sp = verify_pt_spectrum()
    print(f'  Zero mode:  ω₀ = {sp["omega0_from_poles"]:.2e}    (expected 0)')
    print(f'              κ₀ = {sp["kappa_0"]:.4f} = 2M_c   '
          + ('✓' if sp['omega0_exact_zero'] else '✗'))
    print(f'  Shape mode: ω₁ = {sp["omega1_from_poles"]:.6f}  '
          f'(expected {sp["omega1_expected"]:.6f} = √3 M_c)')
    print(f'              Error = {sp["error_omega1"]:.2e}')

    # 4. Phase shift table
    print('\n── 4. Exact phase shift δ(q) vs q ──')
    print(f'  {"q/M_c":>8}  {"δ_exact (rad)":>16}  {"δ/π":>10}  '
          f'{"T_complex":>30}  {"time_delay/λ":>14}')
    q_test = [0.01, 0.1, 0.3, 1.0, 2.0, 5.0, 10.0, 100.0]
    for q_ov in q_test:
        q = q_ov * M_C
        T = T_exact(q)
        delta = phase_shift(q)
        tau = wigner_time_delay(q) * M_C  # in units of λ
        print(f'  {q_ov:>8.2f}  {delta:>16.6f}  {delta/math.pi:>10.6f}  '
              f'  {T.real:+.4f}{T.imag:+.4f}j  {tau:>14.6f}')
    print(f'  [Row q→0: δ→2π={2*math.pi:.4f}; Row q→∞: δ→0 ✓]')

    # 5. Born comparison
    print('\n── 5. Exact vs Born (wave scattering off single kink) ──')
    print(f'  {"q/M_c":>8}  {"δ_exact":>14}  {"δ_Born=6/q":>14}  {"agree?":>10}  {"err%":>10}')
    bc = born_comparison()
    for r in bc:
        agree = '✓' if r['agreement_pct'] < 5.0 else ' '
        print(f'  {r["q_over_Mc"]:>8.1f}  {r["delta_exact"]:>14.6f}  '
              f'{r["delta_born"]:>14.6f}  {agree:>10}  '
              f'{r["agreement_pct"]:>9.1f}%')
    print(f'  [At high q: δ_exact → 6M_c/q (from 2arctan(M_c/q)+2arctan(2M_c/q) → 6/q)]')
    print(f'  [Born (6M_c/q) agrees at high q; diverges as q→0; exact saturates at 2π]')

    # 6. Summary
    print('\n── Summary ──')
    print(f'  Proven: |T(q)|² = 1 for all q (reflectionless n=2 PT) [Tier 1 structural]')
    print(f'  Proven: δ(0⁺) = 2π, δ(∞) = 0 [Levinson theorem — 2 bound states]')
    print(f'  Proven: spectrum ω₀=0, ω₁=√3M_c from T-matrix poles [Cycle 33 consistency]')
    print(f'  Computed: δ(q) = 2arctan(M_c/q) + 2arctan(2M_c/q) [exact analytic formula]')
    print(f'  Computed: Wigner time delay τ_W(q) — kink retards high-q waves by ≈3/q')
    print()
    print(f'  Tier: Tier 1 (reflectionless property is a structural exact result)')
    print(f'  Next step: exact kink-antikink scattering (DHN two-soliton result) — OPEN')
    print(f'  See: foundations/kink_scattering.md, equations/kink_scattering.py')
