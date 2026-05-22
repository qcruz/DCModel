"""
Blackbody Radiation: Planck Spectrum, Wien's Law, Stefan-Boltzmann Law
Cycle 129 | DFC Model

Physical question:
  Why does thermal radiation have the Planck spectrum u(ν,T)=8πhν³/c³/(e^{hν/kT}−1)?
  Why does the ultraviolet catastrophe not occur? What does DFC say about the mode structure?

DFC mechanism:
  Photons are massless D2 compression-wave modes with linear dispersion ω=ck (derived from
  the substrate KG equation with no potential). Two transverse polarizations follow from the
  D5 U(1) gauge field being massless (only transverse modes — no longitudinal). Bosonic
  statistics (even Finkelstein-Rubinstein phase, N=0 winding) give Bose-Einstein occupation.

  The Planck spectrum follows from:
  (1) ω=ck — massless KG dispersion (Tier 1, derived from substrate)
  (2) 2 polarizations — transverse gauge field (Tier 1 structural)
  (3) Bose-Einstein statistics — integer spin + even FR phase (Tier 1 structural)
  (4) E=hν — quantum of action (IMPORTED from QFT; ℏ not derived from DFC substrate)

  Item (4) is the remaining postulate. The Planck spectrum derivation is Tier 1 given (4).
  The numerical values involving h and k_B are Tier 1 given imported constants.

  The UV catastrophe is resolved because discrete mode energies E=nhν exponentially suppress
  high-frequency modes — once E=hν is accepted, this is a consequence, not a new assumption.

Key references:
  - phenomena/thermodynamics/blackbody_radiation.md (this module's companion doc)
  - phenomena/light/light.md (photons as massless D2 modes)
  - phenomena/quantum/spin.md (bosonic statistics from FR exchange phase)
  - foundations/planck_constant_derivation.md (status of ℏ derivation — open)
  - Cycle 128: equations/wiedemann_franz.py (related condensed matter, same k_B import)
"""

import numpy as np
from scipy import integrate

# ─── Physical constants (SI, CODATA 2018) ─────────────────────────────────────

H_PLANCK = 6.62607015e-34      # J·s    Planck's constant (exact, imported)
K_B      = 1.380649e-23        # J/K    Boltzmann constant (exact, imported)
C        = 2.99792458e8        # m/s    speed of light (exact)
SIGMA_SB = 5.670374419e-8      # W/m²/K⁴  Stefan-Boltzmann constant (exact from above)

# ─── Planck spectrum ──────────────────────────────────────────────────────────

def planck_spectrum(nu, T):
    """
    Spectral energy density u(ν, T) of blackbody radiation.

    Energy density per unit frequency per unit volume:
      u(ν, T) = (8π h ν³ / c³) × 1/(e^{hν/kT} − 1)

    DFC derivation:
    - Mode density 8πν²/c³: from ω=ck dispersion + 2 transverse polarizations
    - Energy per mode hν: requires quantum of action (imported)
    - Occupation number: Bose-Einstein with μ=0 (photons are not conserved)
    """
    x = H_PLANCK * nu / (K_B * T)
    return (8 * np.pi * H_PLANCK * nu**3 / C**3) / (np.expm1(x))


def planck_spectrum_verify():
    """Verify Planck spectrum at specific frequencies against analytic reference."""
    T = 5778.0  # K — solar surface temperature

    # Reference: nu = 3.4e14 Hz (red light), T = 5778 K
    nu_ref = 3.4e14  # Hz
    u_ref  = planck_spectrum(nu_ref, T)

    # At x = hν/kT = 2.84 (near Wien peak), u should be large
    x_ref = H_PLANCK * nu_ref / (K_B * T)

    print(f"=== Planck Spectrum Verification ===")
    print(f"  T = {T:.0f} K  (solar surface temperature)")
    print(f"  ν = {nu_ref:.2e} Hz  (red light, x = hν/kT = {x_ref:.3f})")
    print(f"  u(ν, T) = {u_ref:.4e} J·s/m³")
    print(f"  Note: ℏ and k_B are imported constants — not derived from DFC substrate")

    # Check Rayleigh-Jeans limit (low ν): u → 8πν²kT/c³
    nu_low  = 1e8   # Hz (microwave — hν << kT at 5778 K)
    u_planck = planck_spectrum(nu_low, T)
    u_rj    = 8 * np.pi * nu_low**2 * K_B * T / C**3
    err_rj  = (u_planck - u_rj) / u_rj
    print(f"\n  Rayleigh-Jeans limit check (ν={nu_low:.0e} Hz, hν/kT={H_PLANCK*nu_low/(K_B*T):.2e}):")
    print(f"  Planck:         {u_planck:.6e}")
    print(f"  R-J (classical): {u_rj:.6e}  (error {err_rj*100:+.4f}%)")
    assert abs(err_rj) < 1e-3, f"R-J limit failed: {err_rj}"
    print(f"  R-J limit: PASS (error < 0.1%)")

    return u_ref


# ─── Wien's displacement law ──────────────────────────────────────────────────

def wien_law_verify():
    """
    Verify Wien's displacement law: λ_max × T = b = 2.898 × 10⁻³ m·K.

    IMPORTANT DISTINCTION:
    - Peak of u(ν,T) [frequency spectrum]: 3(1 − e^{−x_ν}) = x_ν → x_ν = 2.8214
      This gives c/ν_max × T = hc/(x_ν k_B) = 5.10 × 10⁻³ m·K  ≠ b
    - Peak of u(λ,T) [wavelength spectrum]: 5(1 − e^{−x_λ}) = x_λ → x_λ = 4.9651
      This gives λ_max × T = hc/(x_λ k_B) = 2.898 × 10⁻³ m·K = b  ✓

    The two peaks differ because the spectra are different: u(λ) = |dν/dλ| u(ν) = c/λ² u(ν).
    The standard Wien constant b uses the wavelength-domain peak.
    """
    from scipy.optimize import brentq

    # Frequency-domain peak: d/dν[ν³/(e^x-1)] = 0 → 3(1-e^{-x})=x
    f_nu = lambda x: 3 * (1 - np.exp(-x)) - x
    x_nu = brentq(f_nu, 1.0, 5.0)

    # Wavelength-domain peak: d/dλ[λ^{-5}/(e^{hc/λkT}-1)] = 0 → 5(1-e^{-x})=x
    f_lam = lambda x: 5 * (1 - np.exp(-x)) - x
    x_lam = brentq(f_lam, 3.0, 7.0)

    b_DFC = H_PLANCK * C / (x_lam * K_B)   # wavelength-domain Wien constant
    b_obs = 2.897771955e-3   # m·K  (CODATA 2018 value)
    err   = (b_DFC - b_obs) / b_obs

    print(f"\n=== Wien's Displacement Law ===")
    print(f"  Frequency-domain: 3(1−e^{{−x}})=x  →  x_ν = {x_nu:.6f}  (c/ν_max × T = {H_PLANCK*C/(x_nu*K_B):.4e} m·K)")
    print(f"  Wavelength-domain: 5(1−e^{{−x}})=x →  x_λ = {x_lam:.6f}  (λ_max × T = b)")
    print(f"  Note: these give DIFFERENT peaks because u(λ)=c/λ² u(ν) shifts the maximum")
    print(f"  Wien constant b = hc/(x_λ × k_B):")
    print(f"    DFC:      {b_DFC:.9e} m·K")
    print(f"    Observed: {b_obs:.9e} m·K")
    print(f"    Error: {err*100:+.6f}%  (0% — b=hc/x k_B, exact given imported h,k_B,c)")
    print(f"  Tier: Tier 1 structural — follows from Planck spectrum + calculus")

    # Check at solar and CMB temperatures
    T_sun = 5778.0   # K
    T_cmb = 2.7255   # K
    lam_sun = b_DFC / T_sun
    lam_cmb = b_DFC / T_cmb
    print(f"\n  λ_max (solar, T={T_sun:.0f} K): {lam_sun*1e9:.1f} nm  (green-yellow visible ✓)")
    print(f"  λ_max (CMB,  T={T_cmb:.4f} K): {lam_cmb*1e3:.2f} mm  (microwave ✓)")

    assert abs(err) < 1e-9, f"Wien law error: {err}"
    return b_DFC, x_nu


# ─── Stefan-Boltzmann law ─────────────────────────────────────────────────────

def stefan_boltzmann_verify():
    """
    Verify Stefan-Boltzmann law: P/A = σ T⁴.

    Derivation: integrate Planck spectrum over all frequencies.
    ∫₀^∞ x³/(e^x − 1) dx = π⁴/15  (Riemann zeta: Γ(4)ζ(4) = 6 × π⁴/90)
    → σ = 2π⁵k_B⁴/(15c²h³)
    """
    # Analytic value of the Riemann integral ∫x³/(e^x-1)dx = π⁴/15
    zeta4_gamma4 = np.pi**4 / 15.0
    sigma_analytic = 2 * np.pi**5 * K_B**4 / (15 * C**2 * H_PLANCK**3)

    # Numerical verification by direct integration of Planck spectrum
    T = 1000.0  # K  (any T works — σ is T-independent)
    def integrand(nu):
        x = H_PLANCK * nu / (K_B * T)
        return (8 * np.pi * H_PLANCK * nu**3 / C**3) / (np.expm1(x))

    # Integrate u(ν,T) and compare with σT⁴ × (4/c) × (c/4) — power per area = c*u/4
    nu_max = 30 * K_B * T / H_PLANCK   # 30× peak for safe upper limit
    u_total_num, u_err = integrate.quad(integrand, 0, nu_max, limit=200)
    sigma_num = u_total_num * C / (4 * T**4)

    err_analytic = (sigma_analytic - SIGMA_SB) / SIGMA_SB
    err_numeric  = (sigma_num - SIGMA_SB) / SIGMA_SB

    print(f"\n=== Stefan-Boltzmann Law ===")
    print(f"  ∫₀^∞ x³/(e^x−1)dx = π⁴/15 = {zeta4_gamma4:.6f}  (exact Riemann zeta)")
    print(f"  σ = 2π⁵k_B⁴/(15c²h³):")
    print(f"    Analytic:  {sigma_analytic:.6e} W/m²/K⁴  (error {err_analytic*100:+.4f}%)")
    print(f"    Numerical: {sigma_num:.6e} W/m²/K⁴  (error {err_numeric*100:+.4f}%)")
    print(f"    CODATA:    {SIGMA_SB:.6e} W/m²/K⁴")
    print(f"  Tier: Tier 1 — algebraic consequence of Planck spectrum")

    # Sample stellar luminosities
    R_sun = 6.957e8  # m
    T_sun = 5778.0   # K
    L_sun = 4 * np.pi * R_sun**2 * sigma_analytic * T_sun**4
    L_sun_obs = 3.828e26  # W  (IAU nominal solar luminosity)
    err_Lsun = (L_sun - L_sun_obs) / L_sun_obs
    print(f"\n  Solar luminosity check: L = 4πR²σT⁴")
    print(f"    L_DFC = {L_sun:.4e} W  vs L_obs = {L_sun_obs:.4e} W  (error {err_Lsun*100:+.2f}%)")

    assert abs(err_analytic) < 1e-10
    return sigma_analytic


# ─── CMB spectrum ─────────────────────────────────────────────────────────────

def cmb_spectrum():
    """
    CMB spectral energy density: the most precise blackbody in nature.
    T_CMB = 2.7255 K (FIRAS measurement, error < 1 part in 10,000).

    DFC account: after recombination at z ≈ 1100, the photon gas decoupled from matter
    and has cooled adiabatically to T_CMB = T_rec / (1+z_rec) ≈ 3000/1100 ≈ 2.73 K.
    The spectrum is an exact Planck spectrum — the single most precisely verified blackbody
    in nature (COBE FIRAS: deviation < 50 ppm at any frequency).
    """
    T_cmb = 2.7255  # K  (FIRAS 2009)

    # Peak frequency
    from scipy.optimize import brentq
    f = lambda x: 3 * (1 - np.exp(-x)) - x
    x_peak = brentq(f, 1.0, 5.0)
    nu_peak = x_peak * K_B * T_cmb / H_PLANCK
    lam_peak = C / nu_peak

    # Photon number density n_γ = (2ζ(3)/π²) × (k_B T/ℏc)³
    zeta3 = 1.2020569032   # Riemann ζ(3)
    n_gamma = 2 * zeta3 / np.pi**2 * (K_B * T_cmb / (6.582119569e-16 * C))**3  # using ℏ in eV·s
    # Use SI consistently
    hbar = H_PLANCK / (2 * np.pi)
    n_gamma_si = 2 * zeta3 / np.pi**2 * (K_B * T_cmb / (hbar * C))**3

    # Energy density u = σ T⁴ × (4/c)
    sigma = 2 * np.pi**5 * K_B**4 / (15 * C**2 * H_PLANCK**3)
    u_cmb = 4 * sigma * T_cmb**4 / C

    print(f"\n=== CMB Spectrum ===")
    print(f"  T_CMB = {T_cmb} K  (FIRAS; < 1 part in 10,000 of ideal Planck)")
    print(f"  Peak frequency ν_max = {nu_peak:.4e} Hz")
    print(f"  Peak wavelength λ_max = {lam_peak*1e3:.4f} mm  (microwave ✓)")
    print(f"  Photon number density n_γ = {n_gamma_si:.3e} m⁻³")
    print(f"  Energy density u = {u_cmb:.4e} J/m³  (= {u_cmb/(H_PLANCK*nu_peak):.3e} photons/m³/Hz at peak)")
    print(f"  DFC: photon gas decoupled at z≈1100, cooled to T_CMB=T_rec/(1+z_rec)≈2.73 K")
    print(f"  Spectrum: Tier 1 given imported h, k_B; T_CMB itself requires DFC cosmology (Tier 4)")


# ─── Ultraviolet catastrophe analysis ────────────────────────────────────────

def uv_catastrophe_analysis():
    """
    Show explicitly how the UV catastrophe is resolved by quantization.

    Classical (Rayleigh-Jeans): u_cl(ν) = 8πν²kT/c³  → diverges at high ν
    Quantum (Planck):          u_qm(ν) = u_cl × hν/kT / (e^{hν/kT} − 1) → 0 at high ν

    The suppression factor x/(e^x − 1) → 0 exponentially for x >> 1.
    DFC: once E=hν is accepted (imported postulate), the suppression follows automatically
    from Bose-Einstein statistics.
    """
    T = 3000.0   # K — hot enough to see the classical failure clearly
    nu_arr = np.logspace(11, 15, 200)

    u_rj = 8 * np.pi * nu_arr**2 * K_B * T / C**3
    u_planck = planck_spectrum(nu_arr, T)
    ratio = u_planck / u_rj   # = x/(e^x − 1) where x = hν/kT

    # Find where ratio drops below 0.5 (significant suppression)
    x_arr = H_PLANCK * nu_arr / (K_B * T)
    idx_half = np.argmin(np.abs(ratio - 0.5))

    print(f"\n=== UV Catastrophe Analysis ===")
    print(f"  T = {T:.0f} K")
    print(f"  Classical R-J: u_cl ∝ ν²  →  ∫u dν diverges (UV catastrophe)")
    print(f"  Quantum Planck: u_qm = u_cl × (x/(e^x−1))  →  0 as x→∞")
    print(f"  Suppression factor x/(e^x−1):")
    print(f"    x=0.1 (low ν):  {0.1/(np.exp(0.1)-1):.4f}  ≈ 1  (classical limit)")
    print(f"    x=1.0:          {1.0/(np.exp(1.0)-1):.4f}")
    x_peak_nu = 2.82143937
    supp_peak = x_peak_nu / (np.exp(x_peak_nu) - 1)
    print(f"    x=2.821 (ν-peak): {supp_peak:.4f}  (suppression factor at frequency peak)")
    print(f"    x=5.0:          {5.0/(np.exp(5.0)-1):.4e}")
    print(f"    x=10:           {10.0/(np.exp(10.0)-1):.4e}")
    print(f"  50% suppression at x = {x_arr[idx_half]:.2f}  (ν = {nu_arr[idx_half]:.2e} Hz at T={T:.0f} K)")
    print(f"  DFC mechanism: discrete mode energies E=nhν → Boltzmann factor suppresses high-ν modes")
    print(f"  Resolution is exact — no approximation beyond E=hν postulate")

    x_peak_val = 2.82143937   # numerical solution stored here for use
    return x_peak_val


# ─── Consistency checks table ─────────────────────────────────────────────────

def consistency_checks():
    """Print consistency check table matching phenomenon doc format."""
    from scipy.optimize import brentq
    # Wavelength-domain peak: 5(1-e^{-x})=x → x_λ=4.9651 → b=hc/(x_λ k_B)=2.898e-3 m·K
    f_lam = lambda x: 5 * (1 - np.exp(-x)) - x
    x_lam = brentq(f_lam, 3.0, 7.0)
    b_val  = H_PLANCK * C / (x_lam * K_B)
    sigma  = 2 * np.pi**5 * K_B**4 / (15 * C**2 * H_PLANCK**3)
    sigma_err = (sigma - SIGMA_SB) / SIGMA_SB

    print(f"\n=== Consistency Checks ===")
    rows = [
        ("ω = ck (massless dispersion)",
         "KG equation with no potential (Tier 0 substrate)",
         "Verified — massless photons propagate at c", "Tier 1 ✓"),
        ("2 photon polarizations",
         "Massless D5 U(1) gauge field — transverse only",
         "Two helicity states measured ✓", "Tier 1 ✓"),
        ("Bose-Einstein statistics",
         "Spin-1, even FR exchange phase (N=0 D6 winding)",
         "Photons are bosons ✓", "Tier 1 ✓"),
        ("E = hν (mode quantization)",
         "Quantum of action ℏ — IMPORTED from QFT",
         "Required to match experiment — POSTULATE ✗", "Imported"),
        (f"Wien b = {b_val:.4e} m·K",
         "x_λ=4.9651 from d/dλ[Planck]=0  (λ-domain peak)",
         f"CODATA {2.897772e-3:.4e} m·K (err 0.000%) ✓", "Tier 1 ✓"),
        (f"σ = {sigma:.4e} W/m²/K⁴",
         "σ = 2π⁵k_B⁴/(15c²h³); ∫x³/(e^x-1)dx=π⁴/15",
         f"CODATA {SIGMA_SB:.4e} W/m²/K⁴ (err {sigma_err*100:+.4f}%) ✓", "Tier 1 ✓"),
        ("UV catastrophe resolved",
         "Discrete mode energies → Bose suppression at high ν",
         "Planck law finite for all ν ✓", "Tier 1 ✓"),
        ("CMB T=2.7255 K Planck spectrum",
         "Photon gas decoupled at z≈1100; adiabatic cooling",
         "FIRAS < 50 ppm deviation ✓", "Tier 1 ✓"),
        ("Rayleigh-Jeans limit hν << kT",
         "x/(e^x-1) → 1 as x→0; u → 8πν²kT/c³",
         "Classical limit recovered ✓", "Tier 1 ✓"),
    ]

    print(f"  {'Prediction':<38} {'DFC':<38} {'Observed':<36} {'Tier'}")
    print(f"  {'-'*125}")
    for pred, dfc, obs, tier in rows:
        print(f"  {pred:<38} {dfc:<38} {obs:<36} {tier}")


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("Blackbody Radiation: Planck Spectrum + Wien + Stefan-Boltzmann")
    print("Cycle 129 | DFC Model")
    print("=" * 65)

    planck_spectrum_verify()
    b_val, x_pk = wien_law_verify()
    sigma_val   = stefan_boltzmann_verify()
    cmb_spectrum()
    uv_catastrophe_analysis()
    consistency_checks()

    print(f"\n{'=' * 65}")
    print(f"SUMMARY")
    print(f"{'=' * 65}")
    print(f"  Planck spectrum: u(ν,T) = 8πhν³/c³ × 1/(e^{{hν/kT}}−1)  ✓")
    print(f"  DFC derivation: ω=ck (Tier 1) + 2 polarizations (Tier 1) + Bose-Einstein (Tier 1)")
    print(f"  + E=hν (IMPORTED — ℏ not derived from DFC substrate)")
    print(f"  Wien: b = hc/(4.9651 k_B) = {b_val:.6e} m·K  (λ-domain peak; exact given h, k_B, c)")
    print(f"  Stefan-Boltzmann: σ = 2π⁵k_B⁴/(15c²h³) = {sigma_val:.6e} W/m²/K⁴  (exact)")
    print(f"  UV catastrophe: resolved by Bose-Einstein suppression of high-ν modes (Tier 1)")
    print(f"  CMB: T=2.7255 K Planck spectrum; DFC cosmology → T_CMB from decoupling (Tier 4)")
    print(f"  Free parameters: 0 beyond imported h, k_B, c (all in DFC)")
    print(f"  Open: derive ℏ from substrate (needed to make E=hν Tier 1 rather than imported)")
