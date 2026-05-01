"""
DFC Josephson Effect — Cooper Pair Phase Dynamics and Topological Precision

Physical question:
    What does DFC predict about Josephson junctions? The Josephson constant K_J = 2e/h
    is an exact Tier 1 prediction from the D6 Cooper pair charge (2e) and the DFC/QM
    phase equation (dδ/dt = 2eV/ℏ). All other Josephson results (Shapiro steps, SQUID
    interference, Josephson inductance) follow as exact consequences of K_J and Φ₀ = h/(2e).

DFC mechanism:
    Two superconductors share a global D6 kink condensate phase θ. The Josephson junction
    interrupts this phase, creating a phase difference δ = θ₂ − θ₁. Pair tunneling
    amplitude ∝ e^{iδ} → current I = I_c sin(δ). Applied voltage V drives dδ/dt = 2eV/ℏ
    because a Cooper pair carries charge 2e = two D6 kinks × D5 winding number −1 each.

Key DFC results (Tier 1 — no free parameters beyond I_c):
    K_J = 2e/h  = 483 597.848 GHz/V   (exact; Cooper pair charge 2e + Planck's constant)
    V_n = n × f_rf / K_J               (Shapiro steps; n = integer)
    I_max(Φ) = 2I_c |cos(πΦ/Φ₀)|      (SQUID; Φ₀ = h/2e from superconductivity.py)

Key references:
    - phenomena/condensed_matter/josephson_effect.md — full DFC account
    - equations/superconductivity.py — K_J and Φ₀ first verified (Cycle 60)
    - foundations/complex_substrate.md — D5 vortex structure (Cycle 75)

Cycle 90 | phenomena/condensed_matter/josephson_effect.md
"""

import numpy as np
import scipy.constants as const

# ─────────────────────────────────────────────────────────────────────────────
# Fundamental constants
# ─────────────────────────────────────────────────────────────────────────────
h    = const.h       # Planck constant [J·s]
hbar = const.hbar    # Reduced Planck  [J·s]
e    = const.e       # Elementary charge [C]

# Derived Josephson constants
K_J   = 2 * e / h   # Josephson constant [Hz/V]
PHI_0 = h / (2 * e) # Flux quantum [Wb]

# CODATA reference values (exact since 2019 SI redefinition)
K_J_CODATA   = 483597.848416984e9   # Hz/V (exact by definition)
PHI_0_CODATA = 2.067833848e-15      # Wb   (exact by definition)


# ─────────────────────────────────────────────────────────────────────────────
# 1. DC Josephson effect — current-phase relation
# ─────────────────────────────────────────────────────────────────────────────

def dc_josephson_current(delta_rad, I_c):
    """
    DC Josephson current as a function of phase difference delta.

    I(δ) = I_c sin(δ)

    DFC origin: the pair tunneling amplitude across the barrier is e^{iδ}, where
    δ = θ₂ − θ₁ is the D6 condensate phase difference. The current is the
    imaginary part of this amplitude (the net tunneling rate), giving sin(δ).

    Args:
        delta_rad: phase difference [radians]
        I_c: critical current [A] (material-dependent; not from DFC topology)

    Returns: DC Josephson current [A]
    """
    return I_c * np.sin(delta_rad)


def current_phase_relation_table(I_c=1.0e-6):
    """
    Tabulate I(δ) at key phase values.
    I_c = 1 µA is a typical small junction value (illustrative).
    """
    phases = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2,
              2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi]
    labels = ['0', 'π/6', 'π/4', 'π/3', 'π/2',
              '2π/3', '3π/4', '5π/6', 'π']
    return [
        {
            'delta_label': labels[i],
            'delta_rad': phases[i],
            'I_over_Ic': np.sin(phases[i]),
            'I_nA': dc_josephson_current(phases[i], I_c) * 1e9,
        }
        for i in range(len(phases))
    ]


# ─────────────────────────────────────────────────────────────────────────────
# 2. AC Josephson effect — voltage-to-frequency conversion
# ─────────────────────────────────────────────────────────────────────────────

def josephson_frequency(V_volts):
    """
    AC Josephson frequency: f_J = K_J × V = 2eV/h [Hz]

    DFC origin: dδ/dt = 2eV/ℏ (energy 2eV drives the Cooper pair phase).
    One oscillation per 2π phase change → f = (1/2π)(2eV/ℏ) = 2eV/h.

    Args:
        V_volts: junction voltage [V]

    Returns: Josephson oscillation frequency [Hz]
    """
    return K_J * V_volts


def josephson_constant_verification():
    """
    Verify K_J = 2e/h against CODATA.
    K_J is exact since the 2019 SI redefinition.
    """
    error = abs(K_J - K_J_CODATA) / K_J_CODATA
    return {
        'K_J_computed': K_J,
        'K_J_CODATA': K_J_CODATA,
        'relative_error': error,
        'f_at_1mV_GHz': josephson_frequency(1e-3) / 1e9,
        'f_at_1uV_MHz': josephson_frequency(1e-6) / 1e6,
        'is_exact': error < 1e-8,
    }


def ac_josephson_table():
    """
    AC Josephson frequency at representative voltages.
    """
    voltages = [1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3]
    labels   = ['1 nV', '10 nV', '100 nV', '1 µV', '10 µV', '100 µV', '1 mV']
    return [
        {
            'V_label': labels[i],
            'V_volts': voltages[i],
            'f_Hz': josephson_frequency(voltages[i]),
            'f_GHz': josephson_frequency(voltages[i]) / 1e9,
        }
        for i in range(len(voltages))
    ]


# ─────────────────────────────────────────────────────────────────────────────
# 3. Shapiro steps — microwave-induced voltage quantization
# ─────────────────────────────────────────────────────────────────────────────

def shapiro_voltage(n, f_rf_Hz):
    """
    Shapiro step voltage: V_n = n × h f_rf / (2e) = n × f_rf / K_J

    Under microwave irradiation at f_rf, the Josephson phase locks to the
    driving field when f_J = n × f_rf. The resulting DC voltage is V_n.

    DFC origin: the same K_J = 2e/h that determines f_J fixes V_n — the
    Josephson oscillation must be commensurate with the driving frequency.

    Args:
        n: step index (integer)
        f_rf_Hz: microwave frequency [Hz]

    Returns: Shapiro step voltage [V]
    """
    return n * f_rf_Hz / K_J


def shapiro_table(f_rf_GHz=10.0, n_max=6):
    """
    Shapiro step voltages for a 10 GHz microwave source.

    The steps at V_n = n × (1/K_J) × f_rf are used to define the
    voltage standard: n steps of f_rf/K_J replicate a known voltage.

    Args:
        f_rf_GHz: microwave frequency [GHz]
        n_max: compute steps 0 through n_max

    Returns: list of step dicts
    """
    f_rf = f_rf_GHz * 1e9
    return [
        {
            'n': n,
            'V_muV': shapiro_voltage(n, f_rf) * 1e6,
            'V_V': shapiro_voltage(n, f_rf),
            'V_exact': n * PHI_0 * f_rf_GHz * 1e9,  # V_n = n Φ₀ f_rf (same formula)
        }
        for n in range(n_max + 1)
    ]


def shapiro_step_spacing(f_rf_GHz=10.0):
    """
    The spacing between adjacent Shapiro steps:
    ΔV = h f_rf / (2e) = Φ₀ × f_rf = f_rf / K_J

    This is the fundamental voltage step set by Josephson topology.
    """
    f_rf = f_rf_GHz * 1e9
    delta_V = h * f_rf / (2 * e)
    delta_V_check = f_rf / K_J
    return {
        'f_rf_GHz': f_rf_GHz,
        'delta_V_muV': delta_V * 1e6,
        'delta_V_check_muV': delta_V_check * 1e6,
        'consistency': abs(delta_V - delta_V_check) / delta_V,
    }


# ─────────────────────────────────────────────────────────────────────────────
# 4. SQUID — superconducting quantum interference device
# ─────────────────────────────────────────────────────────────────────────────

def squid_critical_current(Phi_Wb, I_c):
    """
    Maximum supercurrent of a symmetric DC SQUID as a function of enclosed flux.

    I_max(Φ) = 2 I_c |cos(π Φ / Φ₀)|

    DFC origin: the two junctions form two parallel tunneling paths for Cooper
    pairs around the ring. Single-valuedness of the condensate phase requires
    δ₂ − δ₁ = 2π Φ/Φ₀ (the same constraint as flux quantization). The
    interference of the two sine currents:

        I = I_c sin(δ̄ + πΦ/Φ₀) + I_c sin(δ̄ − πΦ/Φ₀) = 2I_c cos(πΦ/Φ₀) sin(δ̄)

    Maximum over δ̄ gives |2I_c cos(πΦ/Φ₀)|.

    Args:
        Phi_Wb: enclosed magnetic flux [Wb]
        I_c: single-junction critical current [A]

    Returns: maximum SQUID supercurrent [A]
    """
    return 2 * I_c * abs(np.cos(np.pi * Phi_Wb / PHI_0))


def squid_pattern(I_c=1.0e-6, n_periods=3, n_pts=500):
    """
    SQUID critical current vs. flux over multiple Φ₀ periods.

    Returns arrays (Phi_over_Phi0, I_max_nA) for plotting.
    """
    phi_over_phi0 = np.linspace(-n_periods, n_periods, n_pts)
    Phi_Wb = phi_over_phi0 * PHI_0
    I_max = squid_critical_current(Phi_Wb, I_c)
    return phi_over_phi0, I_max * 1e9  # [nA]


def squid_verification(I_c=1.0e-6):
    """
    Verify key SQUID properties:
    1. Maximum at Φ = 0 (I_max = 2I_c)
    2. Zero at Φ = Φ₀/2 (half-integer flux)
    3. Period = Φ₀ exactly
    """
    I_at_0      = squid_critical_current(0.0, I_c)
    I_at_half   = squid_critical_current(PHI_0 / 2, I_c)
    I_at_period = squid_critical_current(PHI_0, I_c)

    return {
        'I_at_Phi_0_nA':        I_at_0 * 1e9,
        'I_max_expected_nA':    2 * I_c * 1e9,
        'error_at_0':           abs(I_at_0 - 2 * I_c) / (2 * I_c),
        'I_at_half_Phi0_nA':    I_at_half * 1e9,
        'should_be_zero':       I_at_half < 1e-20,  # floating-point zero; cos(π/2) ~ 6e-17
        'I_at_full_Phi0_nA':    I_at_period * 1e9,
        'period_equals_Phi0':   abs(I_at_period - 2 * I_c) / (2 * I_c) < 1e-10,
        'flux_sensitivity_per_Phi0': 2 * I_c * np.pi,  # dI/dΦ at Φ=Φ₀/4 × Φ₀
    }


# ─────────────────────────────────────────────────────────────────────────────
# 5. Josephson energy and inductance
# ─────────────────────────────────────────────────────────────────────────────

def josephson_energy(I_c):
    """
    Josephson coupling energy: E_J = ℏ I_c / (2e) = I_c Φ₀ / (2π)

    This is the energy scale of the junction — how much energy is stored
    in the phase difference δ when the junction is biased away from δ = 0.
    The full potential energy is U(δ) = −E_J cos(δ).

    DFC origin: E_J = I_c × (ℏ/2e) = I_c × (Φ₀/2π). The ℏ/2e = Φ₀/2π
    factor is the same topological ratio that determines K_J.

    Args:
        I_c: critical current [A]

    Returns: Josephson energy [J]
    """
    return hbar * I_c / (2 * e)


def josephson_inductance(I_c, delta_rad):
    """
    Josephson inductance: L_J(δ) = ℏ / (2e I_c cos δ)

    The Josephson junction acts as a nonlinear inductor: for small oscillations
    around the bias phase δ, the effective inductance is L_J(δ). It diverges
    at δ = π/2 (the junction is at its current maximum) and has its minimum
    at δ = 0.

    DFC origin: the inductance is the second derivative of the energy U(δ) = −E_J cos(δ)
    with respect to the flux coordinate (which is Φ₀δ/2π). This gives:
    L_J = (Φ₀/2π)² / (d²U/dδ²) = (Φ₀/2π)² / (E_J cos δ) = ℏ/(2e I_c cos δ).

    Args:
        I_c: critical current [A]
        delta_rad: bias phase [radians]

    Returns: Josephson inductance [H] (infinite at δ = π/2)
    """
    cos_delta = np.cos(delta_rad)
    if abs(cos_delta) < 1e-15:
        return np.inf
    return hbar / (2 * e * I_c * cos_delta)


def josephson_inductance_table(I_c=1.0e-6):
    """
    Josephson inductance vs. bias phase for a 1 µA junction.
    """
    phases = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2 - 0.01]
    labels = ['0', 'π/6', 'π/4', 'π/3', '≈π/2']
    L_J0 = josephson_inductance(I_c, 0)  # minimum inductance
    rows = []
    for i, delta in enumerate(phases):
        L = josephson_inductance(I_c, delta)
        rows.append({
            'delta_label': labels[i],
            'cos_delta': np.cos(delta),
            'L_J_nH': L * 1e9,
            'L_J_over_L_J0': L / L_J0,
        })
    return rows, L_J0


# ─────────────────────────────────────────────────────────────────────────────
# Main output
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 68)
    print("DFC Josephson Effect — Cooper Pair Phase Dynamics")
    print("=" * 68)
    print("Cycle 90 | phenomena/condensed_matter/josephson_effect.md")
    print()

    # ── 1. Josephson constant verification ───────────────────────────────────
    print("── 1. Josephson Constant (Tier 1 — exact from D6 topology) ────")
    jv = josephson_constant_verification()
    print(f"  K_J (computed) = {jv['K_J_computed']:.9e} Hz/V")
    print(f"  K_J (CODATA)   = {jv['K_J_CODATA']:.9e} Hz/V")
    print(f"  Relative error = {jv['relative_error']:.2e}  {'✓ exact (2019 SI)' if jv['is_exact'] else '✗'}")
    print(f"  f_J at 1 mV    = {jv['f_at_1mV_GHz']:.3f} GHz")
    print(f"  f_J at 1 µV    = {jv['f_at_1uV_MHz']:.3f} MHz")
    print()
    print("  Free parameters: 0  (K_J = 2e/h; charge 2e from two D6 kinks;")
    print("  ℏ imported as postulate — see planck_constant_derivation.py)")
    print()

    # ── 2. DC current-phase relation ─────────────────────────────────────────
    print("── 2. DC Josephson Current-Phase Relation (Tier 1 — structural) ")
    print(f"  I(δ) = I_c sin(δ)  [I_c = 1 µA illustrative]")
    print()
    print(f"  {'δ':>6}  {'sin(δ)':>8}  {'I (nA)':>8}")
    print("  " + "─" * 30)
    rows = current_phase_relation_table(I_c=1e-6)
    for r in rows:
        print(f"  {r['delta_label']:>6}  {r['I_over_Ic']:>8.4f}  {r['I_nA']:>8.4f}")
    print()
    print("  Maximum at δ = π/2: I = I_c (junction at critical current)")
    print("  I_c is material-dependent — NOT a DFC prediction (OPEN)")
    print()

    # ── 3. AC Josephson table ────────────────────────────────────────────────
    print("── 3. AC Josephson: f_J = K_J × V (Tier 1 — exact) ───────────")
    print(f"  {'Voltage':>8}  {'f_J (GHz)':>12}")
    print("  " + "─" * 24)
    for row in ac_josephson_table():
        print(f"  {row['V_label']:>8}  {row['f_GHz']:>12.4f}")
    print()

    # ── 4. Shapiro steps ─────────────────────────────────────────────────────
    print("── 4. Shapiro Steps at f_rf = 10 GHz (Tier 1 — exact) ─────────")
    print(f"  ΔV per step = f_rf/K_J = {shapiro_step_spacing(10.0)['delta_V_muV']:.6f} µV")
    print()
    print(f"  {'n':>4}  {'V_n (µV)':>12}")
    print("  " + "─" * 20)
    for row in shapiro_table(f_rf_GHz=10.0, n_max=6):
        print(f"  {row['n']:>4}  {row['V_muV']:>12.4f}")
    ss = shapiro_step_spacing(10.0)
    print()
    print(f"  Two-path consistency (V_n = nΦ₀f_rf): {ss['consistency']:.2e}  ✓")
    print()

    # ── 5. SQUID verification ────────────────────────────────────────────────
    print("── 5. SQUID Interference (Tier 1 — exact from Φ₀) ─────────────")
    sv = squid_verification(I_c=1e-6)
    print(f"  I_max(Φ=0):      {sv['I_at_Phi_0_nA']:.4f} nA  (expected {sv['I_max_expected_nA']:.4f} nA; error {sv['error_at_0']:.2e}) ✓")
    print(f"  I_max(Φ=Φ₀/2):   {sv['I_at_half_Phi0_nA']:.2e} nA  {'✓ zero (half-integer flux)' if sv['should_be_zero'] else '✗'}")
    print(f"  I_max(Φ=Φ₀):     {sv['I_at_full_Phi0_nA']:.4f} nA  {'✓ period = Φ₀ exactly' if sv['period_equals_Phi0'] else '✗'}")
    print(f"  Max dI/dΦ:        {sv['flux_sensitivity_per_Phi0']*1e9:.4f} nA/Φ₀ (linear flux-to-current sensitivity)")
    print()

    # ── 6. Josephson energy and inductance ────────────────────────────────────
    print("── 6. Josephson Energy and Inductance (Tier 1 — structural) ────")
    I_c_ex = 1e-6  # 1 µA
    E_J = josephson_energy(I_c_ex)
    rows_L, L_J0 = josephson_inductance_table(I_c_ex)
    print(f"  E_J = ℏI_c/(2e) = {E_J:.4e} J = {E_J/const.e*1e6:.4f} µeV  (I_c = 1 µA)")
    print(f"  L_J0 = ℏ/(2eI_c) = {L_J0*1e9:.4f} nH  (δ = 0)")
    print()
    print(f"  {'δ':>6}  {'cos(δ)':>8}  {'L_J (nH)':>10}  {'L_J/L_J0':>10}")
    print("  " + "─" * 42)
    for r in rows_L:
        print(f"  {r['delta_label']:>6}  {r['cos_delta']:>8.4f}  {r['L_J_nH']:>10.4f}  {r['L_J_over_L_J0']:>10.4f}")
    print()
    print("  L_J → ∞ as δ → π/2 (junction at critical current)")
    print("  Josephson inductance used in superconducting qubits (transmon regime)")
    print()

    # ── 7. Summary ────────────────────────────────────────────────────────────
    print("── 7. Tier Summary ─────────────────────────────────────────────")
    print()
    print("  Tier 1 (exact from DFC topology; 0 free parameters):")
    print(f"    K_J = 2e/h = {K_J/1e9:.6f} GHz/V")
    print(f"    Φ₀  = h/2e = {PHI_0:.6e} Wb  (SQUID period)")
    print(f"    V_n = n × f_rf / K_J  (Shapiro steps — exact)")
    print(f"    I_max(Φ) = 2I_c |cos(πΦ/Φ₀)|  (SQUID — exact modulation)")
    print()
    print("  OPEN (material-dependent; not from DFC topology):")
    print("    I_c — critical current (depends on junction geometry, n_s, barrier)")
    print("    Junctions with non-sinusoidal CPR (high-transparency, higher harmonics)")
    print()
    print("  IMPORTED (not from DFC substrate):")
    print("    ℏ — Planck's constant (see planck_constant_derivation.py)")
    print()
    print("  DFC topological derivation chain for all Tier 1 results:")
    print("    β → g² = 8πβ/3 → Cooper pair charge = 2e")
    print("    → K_J = 2e/h   → Φ₀ = h/(2e)")
    print("    → Shapiro V_n = n×f/K_J   → SQUID I_max = 2I_c|cos(πΦ/Φ₀)|")


if __name__ == '__main__':
    main()
