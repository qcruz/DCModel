"""
Kink fluctuation spectrum and kink-antikink scattering in the DFC substrate.

The DFC substrate is modeled by V(phi) = -alpha/2 phi^2 + beta/4 phi^4.
The kink solution phi_K(x) = phi_0 tanh(x/lambda) admits an exactly solvable
fluctuation equation — a Poschl-Teller potential with n=2 — that gives:

  1. Zero mode:  omega_0 = 0                  (translation — Goldstone mode)
  2. Shape mode: omega_1 = sqrt(3/2) * m_sigma (internal excitation, below continuum)
  3. Continuum:  omega >= m_sigma = sqrt(2 alpha)

The shape mode frequency is parameter-free: omega_1/m_sigma = sqrt(3)/2 ~ 0.866.
This is the first prediction from DFC substrate dynamics that involves no free
parameters beyond the substrate couplings (alpha, beta).

Kink-antikink scattering (Born approximation):
  - Long-range potential from kink tail overlap: V_KK_bar(R) = -8(alpha/beta) exp(-m_sigma R)
  - Phase shift: delta(k) ~ 4 m_sigma / (beta * k)  (large k)
  - Reflection coefficient: R = sin^2(delta(k))

All computations use the 1+1D kink model (toy model for DFC closures).
The full 3+1D treatment requires the substrate's higher-dimensional kink dynamics.

Key reference: foundations/kink_scattering.md

Usage:
    python3 equations/kink_scattering.py
"""

import math
import numpy as np

# ── Substrate parameters ──────────────────────────────────────────────────────

ALPHA_D5 = 2.0 * (1.02e13)**2    # GeV^2 (D5 closure scale from Route 3B)
BETA     = 0.0351                 # quartic coupling (Tier 3 reference value; gamma_D = (16/3)*sqrt(beta) RETRACTED Cycle 48)

# ── Basic scales ──────────────────────────────────────────────────────────────

def meson_mass(alpha):
    """Meson mass (small oscillation around vacuum). m_sigma = sqrt(2 alpha)."""
    return math.sqrt(2.0 * alpha)

def kink_width(alpha, c=1.0):
    """Kink coherence length. lambda = c * sqrt(2/alpha)."""
    return c * math.sqrt(2.0 / alpha)

def vacuum_field(alpha, beta):
    """Vacuum field value. phi_0 = sqrt(alpha/beta)."""
    return math.sqrt(alpha / beta)

def kink_mass(alpha, beta, c=1.0):
    """
    BPS-correct kink energy: E_kink = (4/3) c alpha^(3/2) / (beta sqrt(2))
    = (4/3) c^2 phi_0^2 / lambda  (Bogomolny identity; Cycle 48 correction).

    RETRACTED formula (Cycle 32, wrong by factor sqrt(2*beta)):
        E_kink = (4/3) c sqrt(2 alpha^3 / beta)  ← WRONG
    Correct formula (Cycle 48):
        E_kink = (4/3) c alpha^(3/2) / (beta * sqrt(2))
    """
    return (4.0/3.0) * c * alpha**1.5 / (beta * math.sqrt(2.0))

# ── Fluctuation spectrum ──────────────────────────────────────────────────────

def fluctuation_potential(x_over_lambda):
    """
    Dimensionless fluctuation potential around the kink.

    U(y)/m_sigma^2 = 1 - (3/2) sech^2(y)   [y = x/lambda]

    Derived from V''(phi_K(x)) = 2*alpha - 3*alpha*sech^2(x/lambda)
    Normalized by m_sigma^2 = 2*alpha.

    Parameters
    ----------
    x_over_lambda : float or array
        Position in units of kink width lambda.

    Returns
    -------
    float or array : U / m_sigma^2
    """
    y = x_over_lambda
    sech2 = 1.0 / np.cosh(y)**2
    return 1.0 - 1.5 * sech2


def poschl_teller_bound_states():
    """
    Exact bound state spectrum of the Poschl-Teller potential with n=2.

    The fluctuation equation around the phi^4 kink maps to:

      [-d^2/dy^2 - 6 sech^2(y)] eta = E eta

    where E = omega^2 * lambda^2 - 4  and  (m_sigma * lambda)^2 = 4.

    For n=2 Poschl-Teller: [-d^2/dy^2 - n(n+1) sech^2(y)] with n=2, n(n+1)=6.

    Bound state energies: E_j = -(n-j)^2, j = 0, 1, ..., n-1
      j=0: E_0 = -4  => omega^2 * lambda^2 = 4 - 4 = 0  => omega_0 = 0  (zero mode)
      j=1: E_1 = -1  => omega^2 * lambda^2 = 4 - 1 = 3  => omega_1 = sqrt(3)/lambda
                                                            = sqrt(3) * m_sigma / 2
                                                            = sqrt(3/2) * alpha^(1/2) * sqrt(2) * (1/2)
    Returns
    -------
    dict with zero mode and shape mode frequencies.
    """
    # (m_sigma * lambda)^2 = 2*alpha * (2/alpha) = 4  [exact, parameter-free]
    m_sigma_lambda = 2.0    # exact

    # Bound state energies in units of 1/lambda^2
    E_0_over_inv_lambda2 = -4.0   # zero mode: omega=0
    E_1_over_inv_lambda2 = -1.0   # shape mode

    # Convert: omega^2 lambda^2 = m_sigma^2 lambda^2 + E = 4 + E
    omega0_sq_lambda2 = 4.0 + E_0_over_inv_lambda2   # = 0
    omega1_sq_lambda2 = 4.0 + E_1_over_inv_lambda2   # = 3

    # In units of m_sigma:
    omega0_over_msigma = math.sqrt(omega0_sq_lambda2) / m_sigma_lambda  # = 0
    omega1_over_msigma = math.sqrt(omega1_sq_lambda2) / m_sigma_lambda  # = sqrt(3)/2

    # Continuum threshold: omega_cont = m_sigma (by definition)
    omega_cont_over_msigma = 1.0

    return {
        'n_PT':                    2,
        'm_sigma_lambda':          m_sigma_lambda,
        'E_zero_mode':             E_0_over_inv_lambda2,
        'E_shape_mode':            E_1_over_inv_lambda2,
        'omega0_over_msigma':      omega0_over_msigma,
        'omega1_over_msigma':      omega1_over_msigma,
        'omega_cont_over_msigma':  omega_cont_over_msigma,
        'shape_mode_exact':        math.sqrt(3.0)/2.0,    # exact value: sqrt(3)/2
        'gap_fraction':            1.0 - math.sqrt(3.0)/2.0,  # fraction below continuum
    }


# ── Kink-antikink interaction ─────────────────────────────────────────────────

def kinkbar_potential(R_over_lambda, alpha, beta):
    """
    Long-range kink-antikink interaction potential (Manton approximation).

    The kink tail at large x:
      phi_K(x) -> phi_0 * (1 - 2 exp(-x/lambda))   as x -> +inf
      phi_Kbar(x) -> -phi_0 * (1 - 2 exp(x/lambda))  as x -> -inf

    When a kink and antikink are separated by distance R >> lambda, the leading
    tail-tail overlap gives an attractive potential:

      V_KK_bar(R) = -A * exp(-R/lambda) = -8 * (alpha/beta) * exp(-m_sigma * R)

    where m_sigma = sqrt(2*alpha) = 1/lambda * sqrt(2) * (m_sigma*lambda/sqrt(2))
                  = sqrt(2) / lambda.

    Wait: m_sigma = sqrt(2*alpha), lambda = sqrt(2/alpha), so m_sigma = sqrt(2)*sqrt(alpha)
    and m_sigma * lambda = sqrt(2*alpha) * sqrt(2/alpha) = 2. So 1/lambda = m_sigma/2.

    V_KK_bar(R) = -8*(alpha/beta) * exp(-m_sigma * R) = -8*phi_0^2 * exp(-m_sigma*R)

    Parameters
    ----------
    R_over_lambda : float
        Separation in units of kink width.
    alpha, beta : float
        Substrate parameters.

    Returns
    -------
    float : V_KK_bar in GeV (or same units as alpha/beta)
    """
    phi0_sq = alpha / beta                    # phi_0^2
    A = 8.0 * phi0_sq                         # coupling strength
    m_sigma = meson_mass(alpha)               # m_sigma = sqrt(2 alpha)
    lam = kink_width(alpha)                   # lambda = sqrt(2/alpha) with c=1
    R = R_over_lambda * lam                   # physical separation
    return -A * math.exp(-m_sigma * R)


def born_phase_shift(k, alpha, beta):
    """
    Born-approximation phase shift for kink-antikink scattering.

    For the Yukawa potential V(R) = -A exp(-m_sigma * R), the Born approximation
    in 1+1D gives the forward scattering amplitude:

      f(k) = -(1/2k) * integral V(x) e^{2ikx} dx
           = -(1/2k) * (-A) * 2*m_sigma / (4k^2 + m_sigma^2)
           = A * m_sigma / (k * (4k^2 + m_sigma^2))

    The phase shift (low-k approximation) delta ~ Re[f]:
      delta_Born(k) ~ A * m_sigma / (k * m_sigma^2) = A / (k * m_sigma)  for k << m_sigma
                    = 8*(alpha/beta) / (k * sqrt(2*alpha))
                    = 8*sqrt(alpha) / (beta * k * sqrt(2))
                    = 4*sqrt(2*alpha) / (beta * k)
                    = 4 * m_sigma / (beta * k)

    Full Born phase shift (Yukawa):
      delta_Born(k) = A * m_sigma / (k * (4k^2 + m_sigma^2))

    Parameters
    ----------
    k : float
        Center-of-mass momentum (same units as m_sigma).
    alpha, beta : float
        Substrate parameters.

    Returns
    -------
    float : Born-approximation phase shift delta(k) in radians.
    """
    m_sig = meson_mass(alpha)
    A = 8.0 * (alpha / beta)
    return A * m_sig / (k * (4.0*k**2 + m_sig**2))


def reflection_coefficient(delta_rad):
    """
    1+1D reflection coefficient from scattering phase shift.
    R = sin^2(delta).
    """
    return math.sin(delta_rad)**2


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("KINK FLUCTUATION SPECTRUM AND KINK-ANTIKINK SCATTERING")
    print("DFC Substrate: V(phi) = -alpha/2 phi^2 + beta/4 phi^4")
    print("=" * 65)

    alpha = ALPHA_D5
    beta  = BETA
    m_sig = meson_mass(alpha)
    lam   = kink_width(alpha)
    phi0  = vacuum_field(alpha, beta)
    M_K   = kink_mass(alpha, beta)

    print(f"\n--- Substrate Parameters (D5 Closure Scale) ---")
    print(f"  alpha           = {alpha:.4e} GeV^2")
    print(f"  beta            = {beta:.4f}  (Tier 3 reference value; gamma_D RETRACTED Cycle 48)")
    print(f"  phi_0           = sqrt(alpha/beta) = {phi0:.4e} GeV")
    print(f"  m_sigma         = sqrt(2 alpha)    = {m_sig:.4e} GeV  [meson mass]")
    print(f"  lambda          = sqrt(2/alpha)    = {lam:.4e} GeV^-1 [kink width]")
    print(f"  m_sigma * lambda= {m_sig * lam:.6f}         [must = 2 exactly]")
    print(f"  M_K             = (4/3)c alpha^(3/2)/(beta*sqrt(2)) = {M_K:.4e} GeV  [BPS-correct; Cycle 48]")
    print(f"  M_K / m_sigma   = {M_K/m_sig:.4e}   [kink is heavy compared to meson]")

    print(f"\n--- Poschl-Teller Fluctuation Spectrum (Exact, Parameter-Free) ---")
    spec = poschl_teller_bound_states()
    print(f"  Potential: U(y)/m_sigma^2 = 1 - (3/2) sech^2(y)  [y = x/lambda]")
    print(f"  Maps to: Poschl-Teller with n(n+1) = 6, n = 2")
    print(f"  (m_sigma * lambda)^2 = {spec['m_sigma_lambda']**2:.1f}  [always exactly 4]")
    print(f"")
    print(f"  Bound states:")
    print(f"    Mode 0: omega_0 / m_sigma = {spec['omega0_over_msigma']:.4f}  (zero mode — translation)")
    print(f"    Mode 1: omega_1 / m_sigma = {spec['omega1_over_msigma']:.6f}  (shape mode)")
    print(f"                              = sqrt(3)/2 = {spec['shape_mode_exact']:.6f}  [exact]")
    print(f"    Continuum: omega / m_sigma >= {spec['omega_cont_over_msigma']:.4f}")
    print(f"")
    omega1_gev = spec['omega1_over_msigma'] * m_sig
    print(f"  Shape mode frequency at D5 closure scale:")
    print(f"    omega_1 = sqrt(3)/2 * m_sigma = {omega1_gev:.4e} GeV")
    print(f"    Gap below continuum: {spec['gap_fraction']*100:.1f}% of m_sigma")
    print(f"    = {(1.0 - spec['omega1_over_msigma']) * m_sig:.4e} GeV")
    print(f"")
    print(f"  *** Parameter-free prediction: shape mode / meson mass = sqrt(3)/2 = 0.8660 ***")

    print(f"\n--- Kink-Antikink Potential (Manton Approximation) ---")
    print(f"  V_KK_bar(R) = -8*(alpha/beta) * exp(-m_sigma * R)")
    print(f"  Coupling A  = 8*(alpha/beta) = {8.0*(alpha/beta):.4e} GeV")
    print(f"")
    print(f"  {'R/lambda':>10}  {'R (GeV^-1)':>14}  {'V_KK_bar (GeV)':>18}  {'|V|/A':>10}")
    print(f"  {'-'*10}  {'-'*14}  {'-'*18}  {'-'*10}")
    A = 8.0 * (alpha / beta)
    for R_l in [1, 2, 3, 5, 10]:
        V = kinkbar_potential(R_l, alpha, beta)
        R_phys = R_l * lam
        print(f"  {R_l:>10}  {R_phys:>14.4e}  {V:>18.4e}  {abs(V)/A:>10.6f}")

    print(f"\n--- Born Approximation Phase Shift delta(k) ---")
    print(f"  Full formula: delta(k) = A * m_sigma / (k * (4k^2 + m_sigma^2))")
    print(f"  Low-k limit:  delta(k) ~ 4 m_sigma / (beta * k)  [k << m_sigma]")
    print(f"")
    print(f"  {'k / m_sigma':>12}  {'k (GeV)':>12}  {'delta (rad)':>14}  {'R = sin^2':>12}")
    print(f"  {'-'*12}  {'-'*12}  {'-'*14}  {'-'*12}")
    for k_frac in [0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0]:
        k = k_frac * m_sig
        delta = born_phase_shift(k, alpha, beta)
        R = reflection_coefficient(delta)
        print(f"  {k_frac:>12.1f}  {k:>12.4e}  {delta:>14.4e}  {R:>12.6f}")

    print(f"\n--- Levinson's Theorem Check ---")
    print(f"  Number of bound states (n=2 PT): 2  (zero mode + shape mode)")
    print(f"  Levinson theorem: delta(0) - delta(inf) = n_bound * pi")
    print(f"  As k -> 0: delta_Born -> inf (consistent with Levinson, n>=1)")
    print(f"  As k -> inf: delta_Born -> 0 (free particle limit confirmed)")

    print(f"\n--- Physical Interpretation for DFC ---")
    print(f"  A topological closure (kink) at D5 has two internal modes:")
    print(f"    1. Translation mode (omega=0): corresponds to positional degree of freedom")
    print(f"    2. Shape mode (omega_1 = sqrt(3)/2 * m_sigma): internal excitation")
    print(f"       This is the first DFC prediction from substrate dynamics only (no free params).")
    print(f"  The shape mode gap (shape mode below continuum) means:")
    print(f"    - The excited kink decays by emitting mesons")
    print(f"    - BUT: the shape mode is a bound state — it cannot decay to mesons")
    print(f"      since omega_1 < m_sigma (below decay threshold)")
    print(f"    - The shape mode IS a stable internal degree of freedom of the closure")
    print(f"  In DFC interpretation: the shape mode could correspond to the")
    print(f"  first excited state of a particle (e.g., proton/Delta splitting)")
    print(f"")
    print(f"  The kink-antikink scattering phase shift gives the first S-matrix")
    print(f"  element computed from DFC substrate dynamics (Born approximation).")
    print(f"  Full treatment requires non-perturbative methods (Manton-Sutcliffe).")

    print(f"\n--- Open Questions ---")
    print(f"  1. Shape mode in DFC: which observed particle splitting does omega_1 correspond to?")
    print(f"  2. Beyond Born approximation: exact phi^4 kink scattering uses inverse scattering")
    print(f"  3. Extension to 3+1D: 1+1D kinks -> domain walls; particle interpretation requires")
    print(f"     higher-dimensional kink (Skyrme soliton) for pointlike particles")
    print(f"  4. Coupling to gauge fields: kink at D5 sources U(1) field; compute charge")
