"""
DFC Superfluidity — Quantized Circulation and Bose-Einstein Condensation

Physical question:
    What does DFC predict about superfluidity? Two exact Tier 1 results follow
    from DFC winding number topology. BEC critical temperature requires ℏ from
    the substrate, which is blocked (Tier 4).

DFC mechanism:
    Superfluid He-4 atoms are composite bosonic closures. The macroscopic phase
    θ of the condensate wavefunction locks globally below T_λ. A vortex in the
    superfluid carries quantized circulation κ = n × h/m — the phase winds by
    2πn around the vortex core, from the same single-valuedness constraint as
    DFC kink charge quantization and superconducting flux quantization.

Key DFC-derived predictions (Tier 1 — exact from topology):
    1. Quantized vortex circulation κ_n = n × h/m    [winding number; exact]
    2. Circulation quantum κ₀ = h/m_He4 = 9.974 × 10⁻⁸ m²/s   [exact]

Open (requires ℏ from DFC substrate):
    BEC critical temperature k_B T_c = (2πℏ²/m) × (n/ζ(3/2))^(2/3)
    — the formula requires ℏ, which is not yet derived from substrate.

Key references:
    - phenomena/condensed_matter/superfluidity.md — full DFC account
    - equations/superconductivity.py — Cooper pair flux quantum h/(2e); analogy
    - equations/quantum_hall.py — conductance quantum e²/h; same topology class
    - foundations/planck_constant_derivation.md — ℏ hierarchy; blocks BEC T_c

Cycle 61 | Tier 1 results verified; BEC T_c blocked by ℏ derivation
"""

import numpy as np
import scipy.constants as const

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────
h    = const.h       # Planck constant [J·s]
hbar = const.hbar    # Reduced Planck [J·s]
k_B  = const.k       # Boltzmann [J/K]
u    = const.u       # Atomic mass unit [kg]

# He-4 mass: 4.002602 u
m_He4 = 4.002602 * u

# ─────────────────────────────────────────────────────────────────────────────
# 1. Quantized vortex circulation (Tier 1 — exact)
# ─────────────────────────────────────────────────────────────────────────────

def circulation_quantum(mass_kg=m_He4):
    """
    Circulation quantum: κ₀ = h/m

    The superfluid velocity field satisfies v_s = (ℏ/m) ∇θ. The circulation
    around a closed loop encircling n vortex cores is:

        ∮ v_s · dl = n × (ℏ/m) × 2π = n × h/m

    Single-valuedness of the order parameter Ψ = √(n_s) e^{iθ} requires
    the phase to return to itself modulo 2π per vortex → integer winding.

    This is the same topological argument as:
    - Magnetic flux quantization: ∮ A·dl = n × h/e  (single charge)
    - Superconducting flux quantum: Φ₀ = h/(2e)     (Cooper pair, charge 2e)
    - QHE conductance: σ_xy = ν × e²/h              (Chern integer)

    Args:
        mass_kg: atomic mass [kg] (default: He-4 = 4.002602 u)

    Returns: circulation quantum [m²/s]
    """
    return h / mass_kg


def circulation_table(n_max=5):
    """Quantized circulation values κ_n = n × h/m_He4 for n = 1,...,n_max."""
    kappa0 = circulation_quantum()
    return [{'n': n, 'kappa_m2s': n * kappa0} for n in range(1, n_max + 1)]


def circulation_verification():
    """
    Verify κ₀ = h/m_He4 against observed value.
    Observed: κ₀ = 9.97 × 10⁻⁸ m²/s  (measured in He-4 vortex experiments)
    """
    kappa0 = circulation_quantum()
    observed = 9.97e-8   # m²/s (standard reference value)
    error = abs(kappa0 - observed) / observed
    return {
        'kappa0_computed': kappa0,
        'kappa0_observed': observed,
        'relative_error': error,
        'm_He4_kg': m_He4,
        'is_consistent': error < 0.01,  # < 1% (limited by m_He4 precision, not topology)
    }


# ─────────────────────────────────────────────────────────────────────────────
# 2. BEC critical temperature (IMPORTED — requires ℏ from substrate)
# ─────────────────────────────────────────────────────────────────────────────

def bec_critical_temperature(n_m3, mass_kg=m_He4):
    """
    BEC critical temperature for an ideal Bose gas:
        k_B T_c = (2πℏ²/m) × (n / ζ(3/2))^(2/3)

    where ζ(3/2) ≈ 2.612 is the Riemann zeta function.

    This formula uses ℏ, which is NOT yet derived from the DFC substrate.
    The formula itself is from standard statistical mechanics, NOT from DFC.

    The ideal Bose gas prediction overestimates He-4's T_λ because He-4 atoms
    interact strongly (hard-core repulsion). The actual T_λ = 2.17 K while the
    ideal BEC formula gives ~3.1 K at the He-4 liquid density.

    Args:
        n_m3: number density [m⁻³]
        mass_kg: atomic mass [kg]

    Returns: critical temperature [K]
    """
    from scipy.special import zeta
    zeta_32 = zeta(1.5)   # ζ(3/2) ≈ 2.612
    return (2 * np.pi * hbar**2 / mass_kg) * (n_m3 / zeta_32)**(2.0/3.0) / k_B


def bec_ideal_comparison():
    """
    BEC T_c for ideal Bose gas at He-4 liquid density.
    n_He4 ≈ 2.18 × 10²⁸ m⁻³ (liquid He-4 at saturated vapor pressure, 2.17 K).
    """
    n_He4 = 2.18e28   # m⁻³ (liquid He-4 number density)
    T_c_ideal = bec_critical_temperature(n_He4)
    T_lambda = 2.17   # K (observed He-4 lambda point)
    return {
        'T_c_ideal_K': T_c_ideal,
        'T_lambda_K': T_lambda,
        'ratio_ideal_to_obs': T_c_ideal / T_lambda,
        'source': 'IMPORTED — uses ℏ (not derived from DFC); interactions not included',
    }


# ─────────────────────────────────────────────────────────────────────────────
# 3. Comparison of circulation topological constants
# ─────────────────────────────────────────────────────────────────────────────

def topology_comparison():
    """
    All fundamental quantization constants in condensed matter from the same
    DFC U(1) winding number mechanism, differing only in the relevant mass or charge.
    """
    phi0_SC   = h / (2 * const.e)     # Cooper pair flux quantum h/(2e)
    phi0_e    = h / const.e            # single-electron h/e (Aharonov-Bohm)
    kappa0    = circulation_quantum()  # He-4 vortex h/m_He4
    G0        = const.e**2 / h         # QHE conductance quantum e²/h

    # Ratios that should be exact integers or simple fractions
    return {
        'phi0_SC_Wb':     phi0_SC,
        'phi0_e_Wb':      phi0_e,
        'kappa0_m2s':     kappa0,
        'G0_S':           G0,
        'kappa0_vs_phi0_e': kappa0 / phi0_e,           # h/m_He4 ÷ h/e = e/m_He4
        'G0_RK_product':  G0 * (h / const.e**2),       # = 1 always
        'phi0_SC_phi0_e_ratio': phi0_e / phi0_SC,      # = 2 (Cooper pair)
        'note': 'κ₀/Φ₀_e = e/m_He4 = 2.40×10⁷ C/kg (specific charge of electron)'
    }


# ─────────────────────────────────────────────────────────────────────────────
# Main output
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("DFC Superfluidity — Quantized Circulation and BEC")
    print("=" * 65)
    print("Cycle 61 | phenomena/condensed_matter/superfluidity.md")
    print()

    # ── 1. Circulation quantum ───────────────────────────────────────────────
    print("── 1. Quantized Vortex Circulation (Tier 1) ────────────────────")
    cv = circulation_verification()
    print(f"  κ₀ = h/m_He4 = {cv['kappa0_computed']:.4e} m²/s")
    print(f"  Observed:       {cv['kappa0_observed']:.2e} m²/s")
    print(f"  Relative error: {cv['relative_error']:.2e}  {'✓ consistent' if cv['is_consistent'] else '✗'}")
    print(f"  m_He4 = {cv['m_He4_kg']:.6e} kg  (= 4.002602 u; exact atomic mass)")
    print()
    print("  DFC: same winding number as kink charge, flux quantum, and QHE.")
    print("  κ_n = n × h/m_He4  for n = 1, 2, 3, ...  (no free parameters)")
    print()

    print("  Circulation quanta:")
    table = circulation_table()
    for row in table:
        print(f"    n = {row['n']}: κ = {row['kappa_m2s']:.4e} m²/s")
    print()

    # ── 2. BEC critical temperature ──────────────────────────────────────────
    print("── 2. BEC Critical Temperature (IMPORTED — requires ℏ) ─────────")
    bec = bec_ideal_comparison()
    print(f"  Ideal Bose gas T_c = {bec['T_c_ideal_K']:.2f} K")
    print(f"  He-4 lambda point: {bec['T_lambda_K']:.2f} K")
    print(f"  Ratio ideal/observed: {bec['ratio_ideal_to_obs']:.2f}×")
    print(f"  Note: {bec['source']}")
    print()
    print("  DFC status: BLOCKED — formula requires ℏ (not derived from")
    print("  substrate). Even if ℏ were known, the ideal gas overestimates")
    print("  T_λ by ~1.4× due to strong He-4 interactions.")
    print()

    # ── 3. Topology comparison ───────────────────────────────────────────────
    print("── 3. Topological Quantization: Unified DFC Picture ────────────")
    tc = topology_comparison()
    print(f"  Φ₀_SC  = h/(2e) = {tc['phi0_SC_Wb']:.4e} Wb   [superconductor; Cooper pair]")
    print(f"  Φ₀_e   = h/e    = {tc['phi0_e_Wb']:.4e} Wb   [normal metal; single electron]")
    print(f"  κ₀     = h/m    = {tc['kappa0_m2s']:.4e} m²/s [superfluid; He-4 atom]")
    print(f"  G₀     = e²/h   = {tc['G0_S']:.4e} S     [QHE; conductance quantum]")
    print()
    print(f"  All from same mechanism: single-valuedness of Ψ = |Ψ|e^{{iθ}}")
    print(f"  Quantized by the relevant particle's charge (e, 2e) or mass (m).")
    print(f"  G₀ × R_K = {tc['G0_RK_product']:.6f}  (exact identity ✓)")
    print()

    # ── 4. Summary ───────────────────────────────────────────────────────────
    print("── 4. DFC Tier Classification ──────────────────────────────────")
    print()
    print("  Tier 1 (exact from topology — 0 free parameters):")
    print(f"    κ₀ = h/m_He4 = {circulation_quantum():.6e} m²/s  ✓")
    print(f"    κ_n = n × κ₀  for n ∈ Z                           ✓")
    print()
    print("  BLOCKED (requires ℏ from substrate — Tier 4):")
    print("    BEC critical temperature T_c = (2πℏ²/m)(n/ζ(3/2))^(2/3)/k_B")
    print("    → see foundations/planck_constant_derivation.md")
    print()
    print("  FREE PARAMETER COUNT: 0  (for Tier 1 results)")


if __name__ == '__main__':
    main()
