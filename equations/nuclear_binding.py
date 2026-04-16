"""
Nuclear Binding Energies — DFC Stub Module
============================================

Physical question:
    What are the binding energies of atomic nuclei, and can DFC derive them from the
    substrate parameters?

DFC mechanism:
    Nucleons (protons and neutrons) are composite D7 SU(3) closures — bound configurations
    of three D6 kinks (quarks) held together by D7 gluon exchange (the strong force).
    Nuclear binding is the residual interaction between these composite closures, mediated
    by pion exchange at the hadronic scale.

    The pion is the lightest D7 composite — a kink-antikink bound state with spin 0 and
    isospin 1. Pion exchange between nucleons produces the Yukawa potential:
        V_Yukawa(r) = −(f²_πNN / 4π) × exp(−m_π r) / r
    where the potential energy between two nucleons at separation r equals minus the square
    of the pion-nucleon coupling constant divided by four pi, times the exponential decay
    factor exp(−m_π r) over r. The exponential decay rate is set by the pion mass m_π.

    Nuclear structure is then described by the many-body problem of nucleons interacting
    via this Yukawa potential (plus short-range repulsion).

    The Bethe-Weizsäcker semi-empirical mass formula gives the binding energy of a nucleus
    with mass number A and proton number Z:
        B(A,Z) = aV×A − aS×A^{2/3} − aC×Z(Z−1)/A^{1/3} − aA×(A−2Z)²/A ± δ
    The five terms are:
    - Volume term: binding energy proportional to the number of nucleons A (aV ≈ 15.8 MeV)
    - Surface term: surface nucleons have fewer neighbors; subtracts aS×A^{2/3} (aS ≈ 18.3 MeV)
    - Coulomb term: electrostatic repulsion between protons (aC ≈ 0.714 MeV)
    - Asymmetry term: energetic cost of neutron-proton imbalance (aA ≈ 23.2 MeV)
    - Pairing term: δ = +12/√A for even-even, −12/√A for odd-odd, 0 for odd A (MeV)

    The coefficients aV, aS, aC, aA are empirical inputs — not yet derived from DFC.
    The DFC goal is to derive them from the D7 substrate's SU(3) closure dynamics.

Key references:
    - Bethe & Weizsäcker (1935/1936): semi-empirical mass formula
    - phenomena/particle_physics/nuclear_binding.md — DFC structural account (if it exists)
    - equations/coupling_derivation.py — α_s from DFC (11% error; M_c(D7) not from substrate)

Status:
    STUB — the pion-nucleon coupling and nuclear binding coefficients are not yet derived
    from the DFC substrate. The Bethe-Weizsäcker formula is implemented here with
    empirical coefficients as a reference for comparison when DFC derivation is complete.

    Key failures to document:
        - α_s(M_Z) = 0.105 (DFC) vs 0.118 (observed): 11% error
        - Pion mass m_π: structural (Goldstone from chiral symmetry breaking) but not
          computed from DFC substrate parameters
        - Nucleon mass m_N ≈ 938 MeV: arises mostly from QCD confinement dynamics
          (not from Higgs mechanism); DFC account requires D7 strong-force dynamics
"""

import math

# ─── Empirical Bethe-Weizsäcker coefficients (MeV) ────────────────────────────
# These are the reference values to compare against once DFC derivation is available.

A_VOLUME   = 15.835    # Volume coefficient (MeV)
A_SURFACE  = 18.33     # Surface coefficient (MeV)
A_COULOMB  = 0.714     # Coulomb coefficient (MeV)
A_ASYMM    = 23.20     # Asymmetry coefficient (MeV)
A_PAIRING  = 12.0      # Pairing coefficient (MeV)

# ─── Pion exchange parameters (empirical) ─────────────────────────────────────
M_PI_MEV = 139.57      # Charged pion mass (MeV) — input from data
F_PI_NN_SQ_OVER_4PI = 0.0795   # Pion-nucleon coupling squared / 4π (empirical; dimensionless)
M_NUCLEON_MEV = 938.9  # Average nucleon mass (MeV) — input from data

# ─── DFC status ───────────────────────────────────────────────────────────────
ALPHA_S_DFC = 0.105    # DFC prediction for α_s(M_Z) — 11% below observed 0.1182
ALPHA_S_OBS = 0.1182   # Observed α_s(M_Z) — PDG 2022

# ─── Key nuclei (A, Z, observed binding energy in MeV) ───────────────────────
KEY_NUCLEI = [
    ("H-2 (deuteron)",  2, 1,   2.224),
    ("He-4 (alpha)",    4, 2,  28.296),
    ("C-12",           12, 6,  92.162),
    ("Fe-56",          56, 26, 492.26),
    ("U-235",         235, 92, 1783.87),
]

# ─── Fusion/fission Q-values (MeV) ───────────────────────────────────────────
# D-T fusion: D + T → He-4 + n + 17.59 MeV
# U-235 fission: U-235 + n → ~17 MeV × 20 fragments → ~200 MeV total
Q_DT_FUSION_MEV = 17.59
Q_U235_FISSION_MEV = 200.0


def pairing_term(A, Z):
    """Pairing term δ for Bethe-Weizsäcker formula."""
    N = A - Z
    if A % 2 == 1:
        return 0.0          # Odd A: no pairing
    elif Z % 2 == 0 and N % 2 == 0:
        return +A_PAIRING / math.sqrt(A)   # Even-even: favored
    else:
        return -A_PAIRING / math.sqrt(A)   # Odd-odd: disfavored


def binding_energy_bw(A, Z):
    """
    Bethe-Weizsäcker semi-empirical binding energy B(A,Z) in MeV.
    Uses empirical coefficients — not derived from DFC.

    Args:
        A: mass number (total nucleons)
        Z: proton number

    Returns:
        float: Binding energy in MeV (positive = bound)
    """
    if A <= 0 or Z < 0 or Z > A:
        return 0.0

    volume   = A_VOLUME  * A
    surface  = A_SURFACE * A**(2.0/3.0)
    coulomb  = A_COULOMB * Z * (Z - 1) / A**(1.0/3.0)
    asymm    = A_ASYMM   * (A - 2*Z)**2 / A
    pairing  = pairing_term(A, Z)

    return volume - surface - coulomb - asymm + pairing


def binding_energy_per_nucleon(A, Z):
    """Binding energy per nucleon B/A in MeV."""
    return binding_energy_bw(A, Z) / A


def yukawa_potential_mev(r_fm):
    """
    One-pion-exchange Yukawa potential between two nucleons at separation r.

    Args:
        r_fm: nucleon separation in femtometers (fm = 10⁻¹⁵ m)

    Returns:
        float: Potential energy in MeV (negative = attractive)
    Note:
        pion Compton wavelength: ℏ c / m_π c² ≈ 1.41 fm
        This sets the range of the nuclear force.
    """
    # Convert r from fm to natural units: r in units of 1/m_π
    # ℏc = 197.3 MeV·fm, so m_π in 1/fm is m_π/ℏc
    HBAR_C_MEV_FM = 197.3269804   # MeV·fm
    m_pi_inv_fm = M_PI_MEV / HBAR_C_MEV_FM    # m_π in units of 1/fm

    # Yukawa: V(r) = −(f²/4π) × m_π² × exp(−m_π r) / (m_π r)
    # In natural units where we express the result in MeV:
    x = m_pi_inv_fm * r_fm   # dimensionless: m_π × r
    V = -F_PI_NN_SQ_OVER_4PI * M_PI_MEV * math.exp(-x) / x
    return V


if __name__ == "__main__":
    print("=" * 68)
    print("Nuclear Binding Energies — DFC Module (STUB)")
    print("=" * 68)
    print()
    print("STATUS: STUB — binding coefficients are empirical inputs, not DFC predictions.")
    print("        DFC goal: derive aV, aS, aC, aA from D7 SU(3) substrate dynamics.")
    print()

    # DFC α_s status
    alpha_s_err = 100.0 * (ALPHA_S_DFC - ALPHA_S_OBS) / ALPHA_S_OBS
    print(f"DFC α_s(M_Z):      {ALPHA_S_DFC:.4f}  (observed: {ALPHA_S_OBS:.4f},  error: {alpha_s_err:.1f}%)")
    print(f"  [M_c(D7) not derived from substrate — 11% α_s error blocks strong-force predictions]")
    print()

    # Bethe-Weizsäcker predictions for key nuclei
    print(f"{'Nucleus':<22} {'A':>5} {'Z':>5} {'B_obs (MeV)':>13} {'B_BW (MeV)':>12} {'Error':>8}")
    print("-" * 68)
    for name, A, Z, B_obs in KEY_NUCLEI:
        B_bw = binding_energy_bw(A, Z)
        err = 100.0 * (B_bw - B_obs) / B_obs if B_obs > 0 else float('nan')
        print(f"{name:<22} {A:>5} {Z:>5} {B_obs:>13.2f} {B_bw:>12.2f} {err:>7.1f}%")
    print()

    # Binding energy per nucleon (iron peak)
    print("Binding energy per nucleon B/A (MeV) — maximum at Fe-56:")
    for name, A, Z, B_obs in KEY_NUCLEI:
        BperA = binding_energy_per_nucleon(A, Z)
        BperA_obs = B_obs / A
        err = 100.0 * (BperA - BperA_obs) / BperA_obs
        print(f"  {name:<20}: {BperA:.3f} MeV/nucleon  (obs: {BperA_obs:.3f},  err: {err:.1f}%)")
    print()

    # Yukawa potential at key separations
    print("One-pion-exchange Yukawa potential (empirical f²_πNN/4π = 0.0795):")
    for r_fm in [0.5, 1.0, 1.41, 2.0, 3.0]:
        V = yukawa_potential_mev(r_fm)
        print(f"  V({r_fm:.2f} fm) = {V:.2f} MeV")
    print()

    # Q-values
    print(f"D-T fusion Q-value:        {Q_DT_FUSION_MEV:.2f} MeV  (observed: 17.59 MeV)")
    print(f"U-235 fission Q-value:     ~{Q_U235_FISSION_MEV:.0f} MeV  (observed: ~200 MeV)")
    print()
    print("OPEN: Derive Bethe-Weizsäcker coefficients from D7 SU(3) kink dynamics:")
    print("  aV from bulk D7 closure binding energy per unit volume")
    print("  aS from surface D7 mode count relative to bulk")
    print("  aC from D5 Coulomb coupling (derived from β chain — 1.3% error)")
    print("  aA from D6 isospin breaking at the nucleon level")
    print("  Requires: M_c(D7) from substrate (currently blocked at 11% α_s error)")
