"""
Kink charge form factor from the zero-mode density distribution.

In DFC, a kink closure is an extended object — not a point particle. Its zero mode
η₀(x) ∝ sech²(M_c x) describes the spatial distribution of the kink's internal degree
of freedom. The square of this profile, ρ(x) = η₀(x)² ∝ sech⁴(M_c x), is the density
of the kink's localized "charge" (generically: whatever conserved current the kink couples
to — momentum, winding number, gauge charge at D5 depths).

The form factor F(k) is the Fourier transform of this normalized density:

    F(k) = ∫ ρ(x) e^{ikx} dx / ∫ ρ(x) dx

It measures how the kink's response to a probe of momentum k deviates from that of a
point source (for which F(k)=1 for all k). F(k) < 1 for k > 0 means the kink is spatially
extended relative to the probe wavelength.

Key results (Cycle 92):

1. Exact form factor from the Fourier transform of sech⁴ (proved analytically via
   the Beta integral B(2−iκ/2, 2+iκ/2)):

       F(k) = πκ(κ²+4) / (8 sinh(πκ/2))    κ = k/M_c

   F(0) = 1 exactly (normalization).

2. Charge radius from the small-k expansion:

       F(k) = 1 − k² <r²>/6 + O(k⁴)

       <r²> = (π²−6)/(4 M_c²)

       <r>_rms = √((π²−6)/4) / M_c ≈ 0.9836 / M_c ≈ 0.9836 λ

   The RMS charge radius is approximately one kink width. Parameter-free. Tier 1.

3. Connection to the scattering sector (Cycles 89–91):

       a_s = 3/M_c = 3λ          (scattering length: Cycle 91)
       r₀  = 11/(6M_c) ≈ 1.833λ  (effective range: Cycle 91)
       <r>_rms ≈ 0.984λ           (charge radius: THIS MODULE)

   These three lengths all live at the kink width scale λ = 1/M_c.

4. Connection to Bottleneck 2:

       r_U1 = 3λ/(4β) ≈ 21.4λ  (gauge holonomy radius, Cycle 42/85)

   The U(1) gauge coupling radius is ~21 times larger than the charge radius.
   The 1/(4β) factor is the quartic coupling suppression of the orbit relative
   to the kink core.

Derivation route for the FT[sech⁴] formula:
   ∫ sech⁴(u) e^{iκu} du = 8 ∫_0^∞ t^{1−iκ/2}/(1+t)^4 dt   [substitution t=e^{−2u}]
   = 8 B(2−iκ/2, 2+iκ/2) / Γ(4)
   = 8 × Γ(2−iκ/2)Γ(2+iκ/2) / 6

   Using Γ(2±iκ/2) = (1±iκ/2)(±iκ/2)Γ(±iκ/2) and
   Γ(iκ/2)Γ(−iκ/2) = 2π/(κ sinh(πκ/2)) [from reflection formula]:

   = πκ(κ²+4) / (6 sinh(πκ/2))   [exact for all κ]

   Dividing by I₄ = 4/3 (the norm) gives F(k) = πκ(κ²+4)/(8 sinh(πκ/2)).

Key references:
  - equations/scattering_length.py   (Cycle 91: a_s, r₀, τ_W)
  - equations/s_matrix.py            (Cycle 89: exact T-matrix, PT n=2)
  - foundations/kink_scattering.md   (kink fluctuation spectrum, zero mode)
  - equations/bottleneck2_coupling_integral.py  (Cycle 85: r_U1/λ gap)

Usage:
    python3 equations/kink_form_factor.py
"""

import math
from scipy import integrate

# ── Constants (M_C = 1 sets scale; all results in units of λ = 1/M_C) ──────────
M_C   = 1.0      # kink width inverse: M_c = 1/λ = √(α/2)/c
I4    = 4.0/3.0  # ∫ sech⁴(u) du = 4/3  (Bogomolny integral I₄)
BETA  = 0.0351   # quartic coupling (Tier 3 reference value)


# ── Form factor (exact analytic formula) ─────────────────────────────────────

def form_factor(k, M_c=M_C):
    """
    Normalized kink charge form factor.

    The form factor equals the Fourier transform of the normalized zero-mode
    density ρ(x) = sech⁴(M_c x) / I₄, where I₄ = 4/3.

    F(k) = πκ(κ²+4) / (8 sinh(πκ/2))    κ = k/M_c

    Parameters
    ----------
    k   : float  — momentum transfer (same units as M_c)
    M_c : float  — kink mass scale (inverse kink width); default 1.

    Returns
    -------
    float : F(k), the form factor.  F(0) = 1, F(k) < 1 for k > 0.
    """
    kappa = k / M_c
    if abs(kappa) < 1e-10:
        # L'Hôpital limit: πκ(κ²+4)/(8 sinh(πκ/2)) → 4/3 / (4/3) = 1
        return 1.0
    num  = math.pi * kappa * (kappa**2 + 4.0)
    den  = 8.0 * math.sinh(math.pi * kappa / 2.0)
    return num / den


def ft_sech4(kappa):
    """
    Fourier transform of sech⁴(u):  ∫ sech⁴(u) e^{iκu} du  (real part, κ real).

    Exact formula: πκ(κ²+4) / (6 sinh(πκ/2))

    Note: F(k) = ft_sech4(k/M_c) / I₄  (normalized form factor).
    """
    if abs(kappa) < 1e-10:
        return I4  # = 4/3
    return math.pi * kappa * (kappa**2 + 4.0) / (6.0 * math.sinh(math.pi * kappa / 2.0))


# ── Numerical verification via direct Fourier integration ────────────────────

def ft_sech4_numerical(kappa, limit=50.0):
    """
    Numerically compute ∫_{-∞}^∞ sech⁴(u) cos(κu) du via scipy.integrate.quad.
    (The imaginary part ∫ sech⁴(u) sin(κu) du = 0 by symmetry.)
    """
    def integrand(u):
        return (1.0 / math.cosh(u))**4 * math.cos(kappa * u)
    result, _ = integrate.quad(integrand, -limit, limit, limit=200)
    return result


# ── Charge radius (analytical) ────────────────────────────────────────────────

def charge_radius_squared(M_c=M_C):
    """
    RMS charge radius squared from the small-k expansion of F(k).

    F(k) = 1 − k²<r²>/6 + O(k⁴)
    → <r²> = (π²−6) / (4 M_c²)

    Derivation of the coefficient:
      F(κ) = πκ(κ²+4)/(8 sinh(πκ/2))
      sinh(πκ/2) ≈ πκ/2 × (1 + π²κ²/24) for small κ
      F(κ) ≈ (κ²+4)/4 × (1 − π²κ²/24)
           = 1 + κ²/4 − π²κ²/24
           = 1 − κ²(π²/24 − 1/4)

      Since F(k) = 1 − k²<r²>/6:
          k²<r²>/6 = k²/M_c² × (π²/24 − 1/4)
          <r²> = 6/M_c² × (π²/24 − 1/4) = (π²−6)/(4 M_c²)
    """
    return (math.pi**2 - 6.0) / (4.0 * M_c**2)


def charge_radius_rms(M_c=M_C):
    """
    RMS charge radius: <r>_rms = √((π²−6)/4) / M_c ≈ 0.9836 λ  [Tier 1, 0 free params]
    """
    return math.sqrt(charge_radius_squared(M_c))


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("DFC Kink Charge Form Factor")
    print("From the zero-mode density ρ(x) ∝ sech⁴(M_c x)")
    print("Extends equations/scattering_length.py (Cycle 91)")
    print("=" * 65)
    print("Cycle 92 | foundations/kink_scattering.md\n")

    # ── 1. Verify FT[sech⁴] formula at κ=0 (normalization) ─────────────────
    print("── 1. Form Factor Normalization ────────────────────────────────")
    F0_analytic  = form_factor(0.0)
    F0_numerical = ft_sech4_numerical(0.0) / I4
    print(f"  F(0) analytic:   {F0_analytic:.10f}  (= 1 exactly)")
    print(f"  F(0) numerical:  {F0_numerical:.10f}  (= ∫sech⁴ / I₄)")
    print(f"  I₄ = ∫sech⁴ du = {I4:.6f}  (= 4/3 exactly)")
    print()

    # ── 2. FT[sech⁴] formula verification ───────────────────────────────────
    print("── 2. FT[sech⁴(u)](κ) = πκ(κ²+4)/(6 sinh(πκ/2)) — Verification")
    kappa_vals = [0.5, 1.0, 2.0, 3.0, 5.0]
    print(f"  {'κ':>6}  {'analytic':>12}  {'numerical':>12}  {'error':>10}")
    print("  " + "─"*50)
    max_err = 0.0
    for kappa in kappa_vals:
        a = ft_sech4(kappa)
        n = ft_sech4_numerical(kappa)
        err = abs(a - n) / max(abs(a), 1e-15)
        max_err = max(max_err, err)
        print(f"  {kappa:6.1f}  {a:12.6f}  {n:12.6f}  {err:10.2e}")
    print(f"  Max relative error: {max_err:.2e}  {'✓' if max_err < 1e-6 else '✗'}")
    print()

    # ── 3. Form factor table ─────────────────────────────────────────────────
    print("── 3. Form Factor F(k) vs Momentum Transfer k/M_c ─────────────")
    print("  F(k) = πκ(κ²+4)/(8 sinh(πκ/2))   κ = k/M_c\n")
    print(f"  {'k/M_c':>8}  {'F(k)':>8}  {'1−F(k)':>10}  interpretation")
    print("  " + "─"*58)
    k_vals = [0.0, 0.1, 0.2, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0]
    for k in k_vals:
        F = form_factor(k)
        dev = 1.0 - F
        if k == 0.0:
            note = "point-particle limit"
        elif k < 0.3:
            note = "low-q (long-wavelength)"
        elif k <= 1.0:
            note = "comparable to M_c"
        elif k <= 3.0:
            note = "sub-kink-width probes"
        else:
            note = "ultrashort — kink resolved"
        print(f"  {k:8.1f}  {F:8.4f}  {dev:10.4f}  {note}")
    print()

    # ── 4. Charge radius (exact) ─────────────────────────────────────────────
    print("── 4. Charge Radius (Tier 1 — exact, 0 free parameters) ────────")
    r2      = charge_radius_squared()
    r_rms   = charge_radius_rms()
    r2_coef = math.pi**2 - 6.0  # (π²−6) ≈ 3.870
    print(f"  <r²>    = (π²−6)/(4 M_c²) = {r2_coef:.4f}/(4 M_c²) = {r2:.6f} λ²")
    print(f"  <r>_rms = √((π²−6)/4) / M_c = √({r2_coef/4:.4f}) λ = {r_rms:.6f} λ")
    print()
    print(f"  DERIVATION:")
    print(f"    F(k) = 1 − k²<r²>/6 + O(k⁴)")
    print(f"    Small-κ expansion of F(κ) gives coefficient (π²/24 − 1/4)")
    print(f"    → <r²> = 6 × (π²/24 − 1/4)/M_c² = (π²−6)/(4 M_c²)")
    print()

    # Numerical verification of charge radius from small-k fit
    dk = 1e-5
    F0p = form_factor(dk)
    F0m = form_factor(-dk)
    r2_numerical = -6.0 * (F0p - 1.0) / dk**2
    print(f"  Numerical check (from F''(0)): <r²> = {r2_numerical:.6f} λ²")
    print(f"  Analytic:                      <r²> = {r2:.6f} λ²")
    err_r2 = abs(r2_numerical - r2) / r2
    print(f"  Relative error: {err_r2:.2e}  {'✓' if err_r2 < 1e-5 else '✗'}")
    print()

    # ── 5. Scale comparison ──────────────────────────────────────────────────
    print("── 5. Scale Comparison (all in units of λ = 1/M_c) ─────────────")
    a_s     = 3.0 / M_C      # scattering length (Cycle 91)
    r0_eff  = 11.0 / (6.0 * M_C)  # effective range (Cycle 91)
    r_U1    = 3.0 / (4.0 * BETA * M_C)   # U(1) holonomy radius (Bottleneck 2)
    print(f"  Kink width:      λ = 1/M_c          = 1.000 λ")
    print(f"  Charge radius:   <r>_rms             = {r_rms:.3f} λ   [Cycle 92, Tier 1]")
    print(f"  Effective range: r₀ = 11/(6M_c)      = {r0_eff:.3f} λ   [Cycle 91, Tier 1]")
    print(f"  Scattering len:  a_s = 3/M_c          = {a_s:.3f} λ   [Cycle 91, Tier 1]")
    print(f"  Holonomy radius: r_U1 = 3/(4βM_c)    = {r_U1:.1f} λ  [Bottleneck 2, Tier 3]")
    print()
    print(f"  Ratios:")
    print(f"    a_s / <r>_rms = {a_s / r_rms:.3f}  (scattering length / charge radius)")
    print(f"    r_U1 / a_s    = {r_U1 / a_s:.3f}  (= 1/(4β) ≈ gauge suppression)")
    print(f"    r_U1 / <r>    = {r_U1 / r_rms:.1f}  (orbit radius / kink size)")
    print()

    # ── 6. Summary ────────────────────────────────────────────────────────────
    print("── 6. Summary of New Tier 1 Predictions ────────────────────────")
    print()
    print(f"  Form factor:  F(k) = πκ(κ²+4)/(8 sinh(πκ/2))   κ=k/M_c")
    print(f"                Proved via Beta integral B(2−iκ/2, 2+iκ/2)")
    print()
    print(f"  Charge radius: <r>_rms = √((π²−6)/4) / M_c")
    print(f"                         ≈ {r_rms:.4f} / M_c  =  {r_rms:.4f} λ")
    print(f"                π²−6 = {r2_coef:.6f}")
    print()
    print(f"  The kink is an extended object with RMS charge radius ≈ 0.984λ.")
    print(f"  At momentum transfer k = M_c, the form factor is F = {form_factor(1.0):.4f}")
    print(f"  (14% suppression relative to point source).")
    print()
    print(f"  Tier: Tier 1 (structural/exact from PT n=2 zero mode; 0 free params)")
    print(f"  Free parameters: 0 (beyond M_c which sets the scale)")
