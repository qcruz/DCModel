"""
DFC Toy Model: Kink solutions as mass analogs.

Implements the 1D compression field dynamics from the Dimensional Folding/Compression
(DFC) substrate framework. This is the mathematical foundation underlying the full
16D geometric model.

The model:
    φ_tt = c² φ_xx - dV/dφ
    V(φ) = -α/2 φ² + β/4 φ⁴

    Static kink solution:
        φ_kink(x) = √(α/β) × tanh((x - x₀) / λ),  λ = √(2c²/α)

    Kink energy (mass analog):
        E_kink = (4/3) c √(2α³/β)

Usage:
    python equations/kink_model.py

    Or:
        from equations.kink_model   KinkDynamics
"""

import math
from typing import Tuple, List, Optional


# ─── Static Kink Solution ─────────────────────────────────────────────────────

def vacuum_values(alpha: float, beta: float) -> Tuple[float, float]:
    """
    The two stable vacuum states of the buckling potential.

    V(φ) = -α/2 φ² + β/4 φ⁴  has minima at φ = ±√(α/β)

    Returns (phi_minus, phi_plus).
    """
    phi_0 = math.sqrt(alpha / beta)
    return (-phi_0, +phi_0)


def kink_width(alpha: float, c: float = 1.0) -> float:
    """
    Characteristic kink width λ = √(2c²/α).

    The kink interpolates between vacua over a length scale ~λ.
    Sharper kink (smaller λ) = higher energy cost = heavier mass analog.
    """
    return math.sqrt(2 * c**2 / alpha)


def kink_solution(x: float, x0: float, alpha: float, beta: float, c: float = 1.0) -> float:
    """
    Static kink solution φ_kink(x) = √(α/β) × tanh((x - x₀) / λ).

    Interpolates from φ = -√(α/β) at x → -∞ to φ = +√(α/β) at x → +∞.
    This is a topologically protected, localized field configuration.

    Parameters
    ----------
    x : float
        Position.
    x0 : float
        Kink center.
    alpha : float
        Potential parameter (drives symmetry breaking).
    beta : float
        Potential parameter (stabilizes at large φ).
    c : float
        Wave speed (sets energy scale and kink width).

    Returns
    -------
    float : field value φ at position x.
    """
    phi_0 = math.sqrt(alpha / beta)
    lam   = kink_width(alpha, c)
    return phi_0 * math.tanh((x - x0) / lam)


def antikink_solution(x: float, x0: float, alpha: float, beta: float, c: float = 1.0) -> float:
    """
    Anti-kink: φ_antikink = -φ_kink. Interpolates from +φ_0 to -φ_0.

    In DFC interpretation, the kink/antikink pair represents particle/antiparticle.
    """
    return -kink_solution(x, x0, alpha, beta, c)


def kink_energy(alpha: float, beta: float, c: float = 1.0) -> float:
    """
    Total energy (mass) of a static kink:

        E_kink = (4/3) c √(2α³/β)

    This is finite, localized, and topologically protected.
    It cannot be continuously deformed to zero without passing through the unstable
    φ = 0 configuration (the "top of the Mexican hat").

    Parameters
    ----------
    alpha, beta : float
        Potential parameters.
    c : float
        Wave speed.

    Returns
    -------
    float : kink energy (in same units as V × length).
    """
    return (4.0 / 3.0) * c * math.sqrt(2 * alpha**3 / beta)


def potential_energy(phi: float, alpha: float, beta: float) -> float:
    """
    Buckling potential V(φ) = -α/2 φ² + β/4 φ⁴.

    Properties:
        V(0) = 0                   (unstable maximum, unfolded state)
        V(±√(α/β)) = -α²/(4β)    (stable minima, folded states)
        Barrier height = α²/(4β)  (energy cost to deform between vacua)
    """
    return -alpha / 2 * phi**2 + beta / 4 * phi**4


def barrier_height(alpha: float, beta: float) -> float:
    """
    Energy barrier between the two vacuum states.

    This sets the stability scale for closures. A higher barrier means
    more stable, harder to destroy.
    """
    return alpha**2 / (4 * beta)


# ─── Compression Budget ───────────────────────────────────────────────────────

def energy_density(phi: float, dphi_dx: float, alpha: float, beta: float, c: float = 1.0) -> float:
    """
    Local energy density of the compression field:

        ρ = (1/2)(∂φ/∂t)² + (c²/2)(∂φ/∂x)² + V(φ)

    For a static kink, ∂φ/∂t = 0 and this reduces to:
        ρ = (c²/2)(∂φ/∂x)² + V(φ)

    Parameters
    ----------
    phi : float
        Field value φ(x).
    dphi_dx : float
        Spatial gradient ∂φ/∂x.
    alpha, beta : float
        Potential parameters.
    c : float
        Wave speed.

    Returns
    -------
    float : energy density at this point.
    """
    kinetic = 0.5 * c**2 * dphi_dx**2
    potential = potential_energy(phi, alpha, beta)
    return kinetic + potential


def kink_gradient(x: float, x0: float, alpha: float, beta: float, c: float = 1.0) -> float:
    """
    Spatial gradient of the kink solution: ∂φ_kink/∂x = (φ_0/λ) × sech²((x-x₀)/λ)
    """
    phi_0 = math.sqrt(alpha / beta)
    lam   = kink_width(alpha, c)
    sech  = 1.0 / math.cosh((x - x0) / lam)
    return (phi_0 / lam) * sech**2


# ─── Kink-Antikink Pair (Particle-Antiparticle Analog) ───────────────────────

def kink_antikink_field(x: float, x1: float, x2: float,
                         alpha: float, beta: float, c: float = 1.0) -> float:
    """
    Approximate superposition of a kink at x1 and antikink at x2.

    This represents a particle-antiparticle pair. The field interpolates:
    -φ₀ → +φ₀ (kink at x1) → -φ₀ (antikink at x2)

    For x2 >> x1 + λ (well-separated pair), the superposition is a good approximation.
    The pair has finite total energy 2 × E_kink.

    DFC interpretation: The pair can annihilate (kink meets antikink → vacuum),
    releasing energy as coherent propagating modes (radiation analog).
    """
    # Simple additive superposition (valid when well-separated)
    return kink_solution(x, x1, alpha, beta, c) + antikink_solution(x, x2, alpha, beta, c)


# ─── Profile and Budget Analysis ─────────────────────────────────────────────

def kink_profile(x_range: Tuple[float, float], n_points: int,
                  x0: float, alpha: float, beta: float, c: float = 1.0) -> List[dict]:
    """
    Compute the kink field profile and local energy density across a range.

    Parameters
    ----------
    x_range : (x_min, x_max)
    n_points : int
    x0 : float    kink center
    alpha, beta, c : float   model parameters

    Returns
    -------
    list of dicts: [{x, phi, gradient, energy_density}, ...]
    """
    x_min, x_max = x_range
    dx = (x_max - x_min) / (n_points - 1)
    results = []
    for i in range(n_points):
        x = x_min + i * dx
        phi = kink_solution(x, x0, alpha, beta, c)
        grad = kink_gradient(x, x0, alpha, beta, c)
        rho = energy_density(phi, grad, alpha, beta, c)
        results.append({'x': x, 'phi': phi, 'gradient': grad, 'energy_density': rho})
    return results


# ─── Main Output ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("DFC TOY MODEL — KINK SOLUTIONS AS CLOSURES")
    print("Dimensional Folding/Compression Framework")
    print("=" * 60)

    # Example parameters
    alpha = 1.0
    beta  = 1.0
    c     = 1.0

    phi_minus, phi_plus = vacuum_values(alpha, beta)
    lam  = kink_width(alpha, c)
    E    = kink_energy(alpha, beta, c)
    V_B  = barrier_height(alpha, beta)

    print(f"\n--- Potential Parameters ---")
    print(f"  α = {alpha},  β = {beta},  c = {c}")
    print(f"  V(φ) = -α/2 φ² + β/4 φ⁴")
    print(f"  Stable vacua:   φ = ±{phi_plus:.4f}")
    print(f"  Barrier height: {V_B:.4f}  (energy cost to destroy closure)")

    print(f"\n--- Kink Solution ---")
    print(f"  φ_kink(x) = {phi_plus:.4f} × tanh((x - x₀) / {lam:.4f})")
    print(f"  Kink width λ = {lam:.4f}")
    print(f"  Kink energy  = {E:.4f}  (mass analog, finite, topologically protected)")

    print(f"\n--- Field Profile (kink centered at x₀ = 0) ---")
    print(f"  {'x':>8}  {'φ(x)':>10}  {'ρ(x)':>12}")
    print(f"  {'-'*8}  {'-'*10}  {'-'*12}")
    for x in [-3*lam, -2*lam, -lam, 0, lam, 2*lam, 3*lam]:
        phi = kink_solution(x, 0, alpha, beta, c)
        grad = kink_gradient(x, 0, alpha, beta, c)
        rho = energy_density(phi, grad, alpha, beta, c)
        print(f"  {x:8.4f}  {phi:10.6f}  {rho:12.6f}")

    print(f"\n--- Physical Interpretation ---")
    print(f"  Kink = stable closure = particle (mass analog)")
    print(f"  Anti-kink = anticlosure = antiparticle")
    print(f"  Topological protection: kink cannot dissolve without barrier crossing")
    print(f"  Budget (compression energy) stored in kink = {E:.4f} units")
    print(f"  This budget is conserved and cannot vanish — only transfer to other modes")

    print(f"\n--- Parameter Scaling ---")
    print(f"  E_kink ∝ c × (α³/β)^(1/2):")
    for scale in [0.5, 1.0, 2.0, 4.0]:
        E_scaled = kink_energy(alpha * scale, beta, c)
        lam_scaled = kink_width(alpha * scale, c)
        print(f"    α={alpha*scale:.1f}: E={E_scaled:.4f}  λ={lam_scaled:.4f}  "
              f"(α × {scale}: heavier and {'sharper' if scale > 1 else 'wider'} kink)")
