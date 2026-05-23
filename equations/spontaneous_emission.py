"""
Spontaneous Emission — DFC Equation Module
===========================================

Physical question:
    Why do excited atoms spontaneously emit photons, and what controls the decay rate?
    Can DFC derive atomic lifetimes from the substrate parameters?

DFC mechanism:
    A D6 electron kink in an excited energy configuration relaxes to a lower-energy
    configuration. The energy difference is emitted as a D5 U(1) photon (massless mode
    of the D5 closure). The coupling α_em from the DFC β chain controls the decay rate.

    The Einstein A coefficient scales as:
        A ∝ α × ω³ × |r₁₂|²
    where ω is the transition frequency and |r₁₂| the dipole matrix element.

    When DFC's α is applied self-consistently (DFC-derived a₀ ∝ 1/α and Rydberg ∝ α²):
        a₀_DFC = a₀_obs × (α_obs/α_DFC)
        ω_DFC  = ω_obs  × (α_DFC/α_obs)²
    so that A ∝ α × (α²)³ × (1/α)² = α⁵ — a standard QED result.
    Self-consistent DFC gives ~10.5% error on A, ~11.7% long on τ.

    If instead ℏ, m_e, a₀, ω are treated as observed inputs and only α is replaced
    by α_DFC, the error is ~2.2% (same systematic as all EM predictions in DFC).

Key parameters:
    DFC α_em = 1/140.1 (from β=1/(9π), Tier 2a, Cycle 117)
    Observed α_em = 1/137.036
    Scaling: A_DFC/A_obs = (α_DFC/α_obs)^5 = 0.8953 (self-consistent DFC)

Key references:
    - equations/atomic_structure.py — H-atom energy levels from DFC coupling chain
    - equations/coupling_derivation.py — DFC α_em derivation chain
    - phenomena/quantum/atomic_structure.md — DFC atomic physics account
    - NIST Atomic Spectra Database (Wiese & Fuhr 2009) — tabulated A-values
"""

import math

# ─── Physical constants ────────────────────────────────────────────────────────
HBAR   = 1.0545718e-34    # J·s
C      = 2.99792458e8     # m/s
A0_OBS = 5.29177e-11      # m (Bohr radius, observed)
EV     = 1.60218e-19      # J per eV

# ─── DFC coupling constants ────────────────────────────────────────────────────
ALPHA_OBS = 1.0 / 137.036   # observed fine structure constant
ALPHA_DFC = 1.0 / 140.1     # DFC from β=1/(9π), Cycle 117 (Tier 2a)

# DFC-derived atomic units (consistent application of DFC α throughout)
A0_DFC    = A0_OBS * (ALPHA_OBS / ALPHA_DFC)   # a₀ ∝ 1/α
E_RYD_OBS = 13.606                               # eV
E_RYD_DFC = E_RYD_OBS * (ALPHA_DFC / ALPHA_OBS)**2   # Ry ∝ α²

# ─── NIST A-coefficient reference values ─────────────────────────────────────
# Source: NIST Atomic Spectra Database (Wiese & Fuhr 2009), observed values.
# Each entry: (A_obs s⁻¹, λ_obs nm, label)
TRANSITIONS = [
    # Lyman series (n→1)
    {"name": "Ly-α  2p→1s", "A_obs": 6.265e8, "lam_nm": 121.57,
     "n_u": 2, "n_l": 1},
    {"name": "Ly-β  3p→1s", "A_obs": 1.672e8, "lam_nm": 102.57,
     "n_u": 3, "n_l": 1},
    {"name": "Ly-γ  4p→1s", "A_obs": 6.819e7, "lam_nm":  97.23,
     "n_u": 4, "n_l": 1},
    # Balmer series (dominant E1 channel: nd→2p)
    {"name": "Hα    3d→2p", "A_obs": 6.465e7, "lam_nm": 656.28,
     "n_u": 3, "n_l": 2},
    {"name": "Hβ    4d→2p", "A_obs": 2.062e7, "lam_nm": 486.13,
     "n_u": 4, "n_l": 2},
    {"name": "Hγ    5d→2p", "A_obs": 8.193e6, "lam_nm": 434.05,
     "n_u": 5, "n_l": 2},
    # Paschen (dominant: nf→3d)
    {"name": "Pa-α  4f→3d", "A_obs": 9.391e6, "lam_nm": 1875.1,
     "n_u": 4, "n_l": 3},
    {"name": "Pa-β  5f→3d", "A_obs": 3.766e6, "lam_nm": 1281.8,
     "n_u": 5, "n_l": 3},
]


def hydrogen_freq(n_upper, n_lower, alpha):
    """Hydrogen transition angular frequency ω using given α (rad/s)."""
    E_Ry = E_RYD_OBS * (alpha / ALPHA_OBS)**2    # Rydberg scales as α²
    delta_eV = E_Ry * (1.0/n_lower**2 - 1.0/n_upper**2)
    return delta_eV * EV / HBAR


def dfc_A_coefficient(A_obs, alpha_ratio):
    """DFC A coefficient from self-consistent scaling A ∝ α⁵."""
    return A_obs * alpha_ratio**5


def lyman_alpha_first_principles(alpha, a0):
    """
    Compute 2p→1s Einstein A coefficient from first principles.

    Uses the exact H-atom radial matrix element:
        I_rad = ∫ R₁₀(r) r R₂₁(r) r² dr = (1536 / (243√24)) × a₀ = 1.2899 a₀

    Angular average for p→s transition (l_upper=1):
        |r̄₁₂|² = I_rad² / 3

    A = (4α/3c²) × ω³ × |r̄₁₂|²
    """
    # Exact radial matrix element (dimensionless, in units of a₀)
    I_rad_dimless = 1536.0 / (243.0 * math.sqrt(24.0))   # = 1.2899
    r12_sq = (I_rad_dimless * a0)**2 / 3.0   # averaged matrix element (m²)
    omega = hydrogen_freq(2, 1, alpha)
    return (4.0 * alpha * omega**3 * r12_sq) / (3.0 * C**2)


if __name__ == "__main__":
    print("=" * 72)
    print("Spontaneous Emission — DFC Module")
    print("=" * 72)
    print()

    alpha_ratio = ALPHA_DFC / ALPHA_OBS
    alpha_err = 100.0 * (alpha_ratio - 1.0)
    print(f"DFC α_em   = 1/{1.0/ALPHA_DFC:.2f}   (obs 1/{1.0/ALPHA_OBS:.3f},  Δα/α = {alpha_err:.2f}%)")
    print(f"DFC Rydberg = {E_RYD_DFC:.4f} eV  (obs {E_RYD_OBS:.3f} eV, error = {100*(E_RYD_DFC-E_RYD_OBS)/E_RYD_OBS:.2f}%)")
    print(f"DFC a₀      = {A0_DFC*1e10:.5f} Å   (obs {A0_OBS*1e10:.5f} Å,  error = {100*(A0_DFC-A0_OBS)/A0_OBS:.2f}%)")
    print()

    # --- α⁵ scaling: theoretical and numerical check ---
    alpha5_theory = alpha_ratio**5
    # Numerical: compute A_obs and A_DFC for 2p→1s from first principles
    A_fp_obs = lyman_alpha_first_principles(ALPHA_OBS, A0_OBS)
    A_fp_dfc = lyman_alpha_first_principles(ALPHA_DFC, A0_DFC)
    alpha5_numerical = A_fp_dfc / A_fp_obs
    residual = abs(alpha5_numerical - alpha5_theory) / alpha5_theory
    print(f"α⁵ scaling check (2p→1s from first principles):")
    print(f"  A_obs (first-principles) = {A_fp_obs:.4e} s⁻¹  (NIST: 6.265e8 s⁻¹, "
          f"err = {100*(A_fp_obs-6.265e8)/6.265e8:.2f}%)")
    print(f"  (α_DFC/α_obs)^5          = {alpha5_theory:.8f}")
    print(f"  A_DFC/A_obs (numerical)  = {alpha5_numerical:.8f}")
    print(f"  Residual                 = {residual:.2e}  {'✓' if residual < 1e-10 else '✗'}")
    print()

    # --- Full table using α⁵ scaling of NIST A-values ---
    print("DFC predictions (self-consistent α⁵ scaling of NIST A-values):")
    print(f"  Scaling factor (α_DFC/α_obs)^5 = {alpha5_theory:.6f} → A_DFC = {100*(alpha5_theory-1):+.1f}%")
    print()
    hdr = f"  {'Transition':<18} {'λ(nm)':>7} {'A_obs':>12} {'A_DFC':>12} {'τ_obs(ns)':>11} {'τ_DFC(ns)':>11} {'err τ':>7}"
    print(hdr)
    print("  " + "-" * 82)
    errs = []
    for t in TRANSITIONS:
        A_dfc = dfc_A_coefficient(t["A_obs"], alpha_ratio)
        tau_obs = 1.0e9 / t["A_obs"]
        tau_dfc = 1.0e9 / A_dfc
        err = 100.0 * (tau_dfc - tau_obs) / tau_obs
        errs.append(err)
        print(f"  {t['name']:<18} {t['lam_nm']:>7.2f} {t['A_obs']:>12.3e} {A_dfc:>12.3e} "
              f"{tau_obs:>11.4f} {tau_dfc:>11.4f} {err:>+6.1f}%")
    print()
    print(f"  All transitions: τ_DFC = τ_obs × (α_obs/α_DFC)^5 = τ_obs × {1.0/alpha5_theory:.6f}")
    print(f"  Mean τ error: {sum(errs)/len(errs):+.1f}%  (systematic: τ too long by 11.7%)")
    print()

    print("TIER STATUS:")
    print(f"  Einstein A ∝ α formula: Tier 1 (D5 photon × D6 kink coupling)")
    print(f"  α⁵ scaling (self-consistent DFC): Tier 1 (algebraic, a₀ ∝ 1/α, ω ∝ α²)")
    print(f"  DFC τ predictions: Tier 2b — {100*(1/alpha5_theory-1):.1f}% too long (same α_em systematic)")
    print(f"  Blocked: ℏ not derived from substrate (Tier 0 postulate)")
    print()
    print("CONNECTIONS:")
    print("  equations/atomic_structure.py  — H energy levels (Tier 2b, same systematic)")
    print("  equations/anomalous_magnetic_moment.py — g-2 from α chain")
    print("  equations/coupling_derivation.py — DFC α_em from β=1/(9π)")
    print("  equations/fine_structure.py     — Dirac hydrogen spectrum")
    print("  phenomena/quantum/atomic_structure.md")
