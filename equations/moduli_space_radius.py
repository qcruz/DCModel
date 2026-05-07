"""
moduli_space_radius.py — Cycle 108: Prove R_n/λ = πd_n/I₄ from moduli space metric

Physical question:
    Can we derive R_n/λ = πd_n/I₄ from the DFC substrate field equation?
    This is the one remaining open step blocking Bottleneck 2 (Tier 3 → Tier 2a).

Strategy — moduli space metric approach (Route A):
    n coincident φ⁴ kinks form a moduli space ℂⁿ. The natural radius of the n-th
    modulus (the phase zero mode at depth D(4+n)) is determined by the L² metric
    on the moduli space, which comes directly from V(φ).

    For a single complex kink φ(x) = φ_real(x) × e^{iθ}, the phase modulus has:
        g_{θθ} = ∫ |∂_θ φ|² dx = ∫ φ_real(x)² dx

    The integral ∫ φ_real(x)² dx = φ₀² × I₂ × λ where I₂ = ∫ sech⁴(u) du = 4/3 = I₄.

    Wait — let me be careful. φ_real(x) is the kink profile:
        φ_kink(x) = φ₀ tanh(x/λ)   where λ = √(2/α), φ₀ = √(α/β)

    ∫ φ_kink(x)² dx diverges (kink profile is ±φ₀ at infinity).
    The relevant quantity is the DEVIATION from the vacuum:
        δφ(x) = φ_kink(x) − φ₀  →  ∫ δφ² dx  (also diverges for tanh profile)

    Correct approach: the phase zero mode is NOT ∂_θ(φ_kink e^{iθ}) = iφ_kink e^{iθ}.
    Instead, for n coincident kinks at the same location, the correct zero mode is the
    TRANSLATION zero mode η₀ = ∂_x φ_kink / ‖∂_x φ_kink‖.

    The PHASE modulus corresponds to rotating between the n identical kink zero modes.
    With n kinks at coincident positions, the configuration space is:
        {c₁ η₀, c₂ η₀, ..., c_n η₀} with Σ|c_j|² = 1  →  S^{2n-1} ⊂ ℂⁿ

    The moduli space radius R_n is the norm of the zero mode in field space:
        R_n² = ‖η₀‖² × (something geometric)

    Alternative approach — Hopf fiber as orbit radius:
    The Hopf U(1) acts on the normalized zero mode coefficients c = (c₁,...,c_n).
    The Hopf fiber through c₀ = (1,0,...,0) is {(e^{iθ},0,...,0) : θ ∈ [0,2π)}.
    The speed of this orbit in the L² metric is:
        |dc/dθ|² = |ie^{iθ}|² × ‖η₀‖² = 1 × ‖η₀‖²

    So the circumference of the Hopf fiber in the L² metric is:
        L_Hopf = 2π × ‖η₀‖  [if η₀ is not normalized]
        or L_Hopf = 2π       [if η₀ IS normalized, i.e., ‖η₀‖ = 1]

    If η₀ IS normalized (‖η₀‖=1), the Hopf fiber has circumference 2π in field space.

    The KK coupling is g² = 2π/(L_Hopf/λ_phys) where λ_phys is the physical length scale.
    But this gives g=1 independent of β — not what we want.

    The missing ingredient: the Hopf fiber lives in FIELD SPACE with metric g_{ij} = δ_{ij},
    but the PHYSICAL radius in POSITION SPACE is R_n, related by:
        R_n (position) = 1/M_c (kink scale) × f (phase stiffness normalization)

    The phase stiffness f² = I₄ φ₀²/λ (Cycle 47, exact). The position-space radius is:
        R_n = (energy of one Hopf orbit) / (energy density) → R_n = f × λ / (2π)

    Let's compute: f² = I₄ φ₀²/λ.
    The Hopf fiber orbit energy = (1/2) × f² × (2π)² / (2πR_n)² × Vol(orbit)
    This needs careful dimensional analysis.

Cleaner approach — direct computation from the KK reduction formula:
    In KK reduction on S^{d_n}(R_n), the gauge coupling is:
        g_KK² = (κ_d)² / (R_n^{d_n} × Vol(S^{d_n}(1)))
    where κ_d comes from the KK kinetic normalization.

    For d=1 (S¹): Vol(S¹(R)) = 2πR, g² = 1/(2πR × mode_norm_position)
    From DFC: g² = 2πβI₄, R = 3λ/(4β) → g² = 2π/(R/λ) = 2πλ/R = 2πβI₄×(4/3) wait...

    Let me just verify the key formula numerically and then identify what physical
    condition fixes R_n.

Physical picture (revised):
    The Hopf fiber on S^{d_n}(R_n) describes the phase of n kink zero modes.
    Each zero mode η_j(x) = η₀(x) × e_j where e_j ∈ ℂⁿ are orthonormal unit vectors.
    The phase rotation η → e^{iθ}η has velocity |dη/dθ|_L² = ‖η₀‖ × 1 = 1 (normalized).

    The POSITION-SPACE radius R_n is NOT the L² radius (which = 1 for normalized modes).
    R_n is fixed by the MATCHING condition: the D6 zero mode must fit inside the D5/D6/D7
    closure region. This requires the kink's phase to wind exactly once around S^{d_n}(R_n)
    when traversing the D(4+n) closure radius.

    The condition: kink phase winding = 1 when traversing distance R_n along the substrate.
    Kink phase gradient: ∂_x(arg φ) = (Im φ* ∂_x φ)/|φ|² ≈ (1/λ) at the kink center.
    Winding condition: (1/λ) × R_n = 1 → R_n = λ.

    But this gives R_n = λ independent of d_n! Wrong scaling.

    The correct condition must include the d_n zero modes and their orthogonality.
    Orthogonality of d_n zero modes requires them to be separated by angles 2π/d_n.
    The phase gradient at the j-th kink: ∂_x arg = (j/d_n)/λ.
    Total winding for d_n modes: d_n × (1/λ) × R_n = d_n → R_n = λ (same!).

    This approach doesn't produce the d_n dependence. The factor d_n must come from
    somewhere else — likely from the SPHERE GEOMETRY of S^{d_n}.

Hopf fiber Laplacian route (most promising):
    The Obata theorem says: on S^d(R), the first eigenvalue of the Laplacian is:
        λ₁ = d/R²

    The DFC kink Laplacian has characteristic eigenvalue 1/λ² (from kink width λ).
    The matching condition: λ₁(S^{d_n}(R_n)) = (1/λ²) × (some ratio).

    If λ₁(S^{d_n}(R_n)) = d_n/R_n² = (1/λ²) × (1/π²):
        R_n = λ√(π²d_n) = πλ√d_n  [gives R_n ∝ √d_n, not d_n]

    If λ₁(S^{d_n}(R_n)) = d_n/R_n² = I₄/(π²λ²):
        R_n = πλ√(d_n/I₄)  [still √d_n]

    Linear scaling R_n ∝ d_n would require: d_n/R_n² = const/d_n → λ₁ ∝ 1/d_n.
    The Obata eigenvalue IS d_n/R_n² (linear in d_n for fixed R_n).
    For R_n = πd_nλ/I₄: λ₁ = d_n/(πd_nλ/I₄)² = I₄²/(π²d_nλ²) ∝ 1/d_n.

    So the matching condition that gives R_n ∝ d_n is:
        λ₁(S^{d_n}(R_n)) = I₄²/(π²d_nλ²)

    This can be rewritten as: d_n/R_n² = I₄²/(π²d_nλ²) → R_n² = π²d_n²λ²/I₄² → R_n = πd_nλ/I₄ ✓

    WHAT PHYSICAL CONDITION GIVES λ₁ = I₄²/(π²d_nλ²)?

    One candidate: the kink zero mode η₀(x) ∝ sech²(x/λ) has a "width" characterized by
    its L² norm squared per unit kink energy:
        ‖η₀‖² = (I₄/λ) × (φ₀/λ)² × λ = I₄φ₀²/λ = f²  (the phase stiffness!)

    Another candidate: the zero mode Fourier content peaks at k_peak = 2/(πλ) (the momentum
    that maximizes sech²̂(k) = πkλ²/sinh(πkλ/2)). Then:
        k_peak = 2/(πλ) → 1/R_n = k_peak/d_n = 2/(πλd_n) → R_n = πd_nλ/2

    This gives R_n = πd_nλ/2, but we need R_n = πd_nλ/I₄ = 3πd_nλ/4.
    Close but not exact (factor 2 vs 4/3).

Let me try the CORRECT peak of the kink zero mode Fourier transform:

η₀(k) = ∫ sech²(x/λ) e^{ikx} dx = πkλ²/sinh(πkλ/2)

The peak is at k=0: η₀(0) = 2λ (trivially). Not useful.

Better: use the MOMENTUM-SPACE width. The characteristic momentum of η₀ is:
    k_char = √(∫k²|η₀(k)|²dk / ∫|η₀(k)|²dk)

This equals the RMS momentum, related to the kink shape by Parseval:
    ∫k²|η₀(k)|²dk = ∫(∂_x η₀)² dx = ∫(sech²)' sech²  ... = (2/3)α (kink Laplacian eigenvalue)

Actually the shape mode calculation: the TRANSLATION zero mode η₀ satisfies Lη₀=0 where
    L = -∂_x² + α - 3α sech²(x/λ) / 2  wait — let me get this right.

For V = -α/2 φ² + β/4 φ⁴, kink φ = φ₀ tanh(x/λ), λ=1/M_c=√(2/α):
    V''(φ_kink) = -α + 3βφ_kink² = -α + 3β φ₀² tanh²(x/λ)
                = -α + 3α tanh²(x/λ)   [since βφ₀²=α]
                = -α(1 - 3tanh²) = α(3tanh²-1) = α(3-3sech²-1) = 2α - 3α sech²(x/λ)

Fluctuation operator: L = -∂_x² + V''(φ_kink) = -∂_x² + 2α - 3αsech²(x/λ)
With λ=√(2/α): L = -∂_x² + α(2 - 3sech²(x/λ))

In PT form with u = x/λ: L = -(1/λ²)∂_u² + (α/1)(2 - 3sech²(u))

Zero mode Lη₀ = 0 → η₀ ∝ sech²(u) (confirmed: -(sech²)'' + 2sech² - 3sech⁴ = 0
   -(sech²)'' = 2sech²tanh² - 2sech⁴ = 2sech²(1-sech²) - 2sech⁴ = 2sech² - 4sech⁴
   so 2sech² - 4sech⁴ + 2sech² - 3sech⁴ = 4sech² - 7sech⁴ ≠ 0... let me recalculate.

Actually: -(d/du)²sech²(u) = -2(-2tanh²(u)sech²(u) + sech²(u)(−sech²(u)))...
Let f = sech²u. Then f' = -2 sech²u tanhu = -2f tanhu.
f'' = -2f' tanhu - 2f sech²u = 4f tanh²u - 2f sech²u = 4f(1-sech²u) - 2f sech²u
    = 4f - 6f² (using tanh²=1-sech², sech²u = f)
So -f'' = -4f + 6f² = 6f² - 4f = 6sech⁴u - 4sech²u.

The operator L/λ² acting on η₀ ∝ sech²u:
  L η₀/λ² = (-∂_u²/λ² + (2/λ² - 6sech²u/λ²)) (sech²u... wait I messed up units.

Let me just do this numerically.
"""

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
from scipy.fft import fft, fftfreq

PI = np.pi
I4 = 4.0 / 3.0  # ∫sech⁴(u) du (Bogomolny)


def kink_zero_mode_properties(alpha=1.0, beta=0.035, N=5000):
    """
    Compute properties of the kink translation zero mode η₀(x) = N_0 × sech²(x/λ).

    Returns: λ, φ₀, η₀ normalization, characteristic momentum, and related scales.
    """
    lam = np.sqrt(2.0 / alpha)  # kink width
    phi0 = np.sqrt(alpha / beta)  # kink amplitude

    x = np.linspace(-30 * lam, 30 * lam, N)
    dx = x[1] - x[0]

    # Zero mode profile (unnormalized)
    eta0_raw = (1.0 / lam) * (1.0 / np.cosh(x / lam))**2

    # L² norm
    norm_sq = np.trapezoid(eta0_raw**2, x)
    norm = np.sqrt(norm_sq)

    # Normalized zero mode
    eta0 = eta0_raw / norm

    # Characteristic momentum: k_rms = sqrt(∫k²|η̂₀(k)|²dk / ∫|η̂₀(k)|²dk)
    # = sqrt(∫(η₀')²dx / ∫η₀²dx) [Parseval]
    eta0_prime = np.gradient(eta0, x)
    k_rms_sq = np.trapezoid(eta0_prime**2, x) / np.trapezoid(eta0**2, x)
    k_rms = np.sqrt(k_rms_sq)

    # Phase stiffness f² = I₄ φ₀²/λ (Cycle 47)
    f_sq = I4 * phi0**2 / lam

    # Norm of unnormalized zero mode = f (in units where φ₀=1, λ=1 it's √I₄)
    norm_unnorm = phi0 / lam * np.sqrt(I4 * lam)  # = φ₀ √(I₄/λ)

    return {
        'alpha': alpha, 'beta': beta,
        'lam': lam, 'phi0': phi0,
        'eta0_norm_sq': norm_sq,      # ∫η₀_raw² dx
        'eta0_norm': norm,
        'k_rms': k_rms,
        'k_rms_lam': k_rms * lam,    # k_rms × λ (dimensionless)
        'f_sq': f_sq,
        'norm_unnorm': norm_unnorm,
    }


def compute_k_rms_analytically():
    """
    Compute k_rms for η₀_raw(x) = sech²(x/λ)/λ analytically.

    ∫(η₀_raw')² dx = ∫(d/dx [sech²(x/λ)/λ])² dx
                   = (1/λ)² × ∫(-2sech²(u)tanh(u)/λ)² × λ du  [u = x/λ]
                   = (1/λ)³ × 4 × ∫sech⁴(u)tanh²(u) du

    ∫sech⁴tanh² du = ∫sech⁴(1-sech²) du = I₄ - I₆
    where I₆ = ∫sech⁶ du = 16/15.

    I₄ - I₆ = 4/3 - 16/15 = 20/15 - 16/15 = 4/15.

    So ∫(η₀_raw')² dx = 4/λ³ × (4/15) = 16/(15λ³).

    ∫η₀_raw² dx = (1/λ²) × ∫sech⁴(u) du × λ = I₄/λ = 4/(3λ).

    k_rms² = [16/(15λ³)] / [4/(3λ)] = [16/(15λ³)] × [3λ/4] = 4/(5λ²).

    k_rms = 2/(√5 × λ) ≈ 0.8944/λ.

    k_rms × λ = 2/√5 ≈ 0.8944.
    """
    I6 = 16.0 / 15.0
    numerator = 4 * (I4 - I6)   # = 4 × 4/15 = 16/15
    denominator = I4             # = 4/3
    k_rms_lam_sq = numerator / denominator  # = (16/15) / (4/3) = 4/5
    k_rms_lam = np.sqrt(k_rms_lam_sq)
    return {
        'k_rms_lam': k_rms_lam,
        'k_rms_lam_sq': k_rms_lam_sq,
        'k_rms_lam_exact': 2.0 / np.sqrt(5.0),
        'error': abs(k_rms_lam - 2.0 / np.sqrt(5.0)),
    }


def obata_matching_condition(d_n_list=[1, 3, 5]):
    """
    For R_n/λ = πd_n/I₄, the Obata eigenvalue is:
        λ₁(S^{d_n}(R_n)) = d_n/R_n² = d_n × I₄²/(π²d_n²λ²) = I₄²/(π²d_nλ²)

    This is the eigenvalue that the fiber sphere Laplacian should produce to give
    R_n = πd_nλ/I₄ via the Obata formula λ₁ = d_n/R_n².

    Question: what kink-substrate condition gives λ₁ = I₄²/(π²d_nλ²)?

    Rewrite: λ₁ = (I₄/πλ)² / d_n = k_char² / d_n

    where k_char = I₄/(πλ) is a characteristic inverse length of the kink.

    Observation: the CORRECT k_char should come from the kink shape.
    We have k_rms = 2/(√5 λ) ≈ 0.894/λ.
    We need k_char = I₄/(πλ) = (4/3)/(π λ) ≈ 0.424/λ.

    These differ by factor 2/(√5 × π/I₄) ≈ 2/(√5 × π × 3/4) ≈ 2/(2.36) ≈ 0.848.

    Different kink integral: what gives I₄/π?

    I₄/(π) = (4/3)/π ≈ 0.424.
    This appears as: (1/π) × ∫sech⁴ du = I₄/π.

    Connection: the sech⁴ integral appears in the PHASE STIFFNESS f² = I₄φ₀²/λ.
    The characteristic coupling-derived scale is g² = 2πβI₄ → at β=1/(9π):
        g² = 2πI₄/(9π) = 2I₄/9 = 8/27
        g = √(8/27) ≈ 0.544

    And r_U1/λ = 1/(βI₄) = 9π/I₄ × 1/... wait:
        r_U1/λ = 1/(βI₄) = 1/(I₄/(9π)) = 9π/I₄... no:
        β = 1/(9π) → r_U1/λ = 1/(βI₄) = 9π/I₄ = 9π × 3/4 = 27π/4 ≈ 21.2 ✓
    """
    results = []
    k_char = I4 / PI  # The candidate characteristic wave vector from kink shape
    for d in d_n_list:
        R_n_over_lam = PI * d / I4  # series holonomy result
        lambda1_Sdn = d / R_n_over_lam**2  # Obata eigenvalue × λ²
        # What is λ₁ × λ² for our R_n?
        # λ₁ × λ² = d_n/R_n² × λ² = d_n/(πd_n/I₄)² = I₄²/(π²d_n)
        lambda1_lamsq = I4**2 / (PI**2 * d)
        # k_char that would give this: k_char² = λ₁ × d_n = I₄²/π²
        k_eff = I4 / PI  # = √(I₄²/π²) = I₄/π
        results.append({
            'd': d,
            'R_n_lam': R_n_over_lam,
            'lambda1_lamsq': lambda1_lamsq,
            'k_eff_lam': k_eff,  # = I₄/π ≈ 0.424 (same for all d!)
        })
    return results, k_char


def fourier_zero_mode():
    """
    Compute the Fourier transform of the kink zero mode η₀(x) = sech²(x/λ)/λ.

    FT: η̂₀(k) = ∫ sech²(x/λ) e^{ikx} dx/λ = (λ/λ) × ∫ sech²(u) e^{ikλu} du
              = πkλ/sinh(πkλ/2)

    Peak: at k=0, η̂₀(0) = 2 (L'Hôpital). But the peak is at k=0 — it's a smooth
    function that monotonically decays. No characteristic k from peak position.

    Derivative dη̂/dk = 0 at k=0 only. The function has no secondary peak.

    Alternative: use the INFLECTION POINT of |η̂₀(k)|² or the 1/e half-width.

    The function πkλ/sinh(πkλ/2):
    - At k→0: η̂ → 2 (using sinh(x)≈x)
    - At k→∞: η̂ → 0 exponentially
    - Inflection: (d²/dk²)(kλ/sinh(πkλ/2)) = 0

    The 1/e point: kλ/sinh(πkλ/2) = (2/e) → solve numerically.
    """
    def eta_hat(kl):
        """η̂₀(k) × 1 for kλ = kl. Returns value normalized to η̂(0)=2."""
        if abs(kl) < 1e-10:
            return 2.0
        return PI * kl / np.sinh(PI * kl / 2.0)

    kl_vals = np.linspace(0, 5, 1000)
    eta_sq = np.array([eta_hat(kl)**2 for kl in kl_vals])

    # Find 1/e half-width
    target = eta_sq[0] / np.e
    idx_half = np.argmin(np.abs(eta_sq - target))
    kl_half = kl_vals[idx_half]

    # Find inflection point
    d2eta = np.gradient(np.gradient(np.sqrt(eta_sq), kl_vals), kl_vals)
    idx_infl = np.argmin(np.abs(d2eta[1:]))  # first zero crossing after k=0
    kl_infl = kl_vals[idx_infl + 1]

    return {
        'kl_half_e': kl_half,     # kλ at 1/e point of |η̂|
        'kl_inflect': kl_infl,    # kλ at inflection of |η̂|
        'I4_over_pi': I4 / PI,    # target k_char × λ = I₄/π ≈ 0.424
    }


def moduli_space_metric_n_kinks(n=1, alpha=1.0, beta=0.035, N=4000):
    """
    For n coincident kinks, compute the phase moduli space metric.

    The n zero modes are η₀^(j)(x) = η₀(x) × e_j for j=1,...,n (orthonormal).
    The Hopf U(1) fiber corresponds to overall phase rotation: c → e^{iθ}c.
    The fiber metric (in field L² space) has radius = 1 (for normalized η₀).

    The PHYSICAL radius R_n corresponds to: how far in position space does the
    Hopf fiber sweep? This requires mapping field-space distance to position-space.

    Claim: R_n = (phase stiffness × phase angle × λ) / (2π × something)

    Direct computation: the zero mode η₀(x) carries energy density T_00.
    The Hopf fiber in ℂⁿ at radius 1 (field space) corresponds to actual
    field configurations with phase angle 0 to 2π.

    The PHYSICAL circumference of this orbit in configuration space is:
        L_phys = 2π × ‖η₀‖_L²  [= 2π × 1 for normalized modes]

    But we need L_phys in units of position-space λ.
    The L² norm of the normalized zero mode is 1 (by definition).
    This means: L_phys = 2π in field-space units.

    To convert to position-space units, we need the ratio of field-space to
    position-space: this comes from the kink profile φ₀.
    """
    lam = np.sqrt(2.0 / alpha)
    phi0 = np.sqrt(alpha / beta)
    Mc = 1.0 / lam  # kink mass scale

    x = np.linspace(-20 * lam, 20 * lam, N)
    dx = x[1] - x[0]

    # Zero mode (unnormalized): ∂_x φ_kink ∝ sech²(x/λ)
    eta0_raw = (phi0 / lam) * (1.0 / np.cosh(x / lam))**2
    # Norm² = (φ₀/λ)² × I₄ × λ = φ₀² I₄/λ = f² (phase stiffness)
    norm_sq = np.trapezoid(eta0_raw**2, x)
    f_sq_computed = norm_sq
    f_sq_formula = I4 * phi0**2 / lam

    # Normalized zero mode
    eta0 = eta0_raw / np.sqrt(norm_sq)

    # For n kinks: Hopf fiber circumference in L² field space = 2π × 1 = 2π
    # Converting to "position units" via phase stiffness:
    # The kink field amplitude is φ₀. A phase rotation by dθ changes the field by
    # dφ = i φ₀ × (something). The position-space effect has length scale λ.
    # Physical circumference = 2π × φ₀ × λ / f (schematically)

    # From Cycle 47: f = √(I₄ φ₀²/λ), so φ₀/f = √(λ/I₄)/φ₀ × φ₀ = √(λ/I₄)
    # L_phys = 2π × √(λ/I₄) × λ  ← not right dimensionally

    # Correct: The moduli space metric for position X gives:
    # g_XX = ∫(∂_X φ)² dx = ∫η₀_raw² dx = f²  [in (field/length)² × length = field²/length units]
    # So position-space displacement ds² = f² dX² → dX = ds/f
    # The Hopf fiber in field space: ds = 1 (normalized). Physical dX = 1/f.
    # Full Hopf orbit: L_phys = 2π/f? No — f has units of field/√length.

    # Actually:
    # The moduli space for one kink: X ∈ ℝ, metric g_XX = f² = ∫η₀_raw² dx
    # The position distance is ds_position = |dX|
    # The field-space distance is ds_field = f × |dX|
    # So L_Hopf_field = 2π × (field-space norm of η₀) × R_fieldspace
    # For the phase modulus on S^{2n-1}: R_fieldspace = 1 (normalized modes)
    # L_Hopf_field = 2π
    # Corresponding position-space radius: R_n = L_Hopf_field / (2π × something)

    # The something is the conversion factor from field-space distances to position-space.
    # For the translation modulus: g_XX = f² → position-metric = f (not f²).
    # For the phase modulus: similar.

    # Key insight: the moduli space is curved (it's S^{2n-1}), not flat.
    # The radius of S^{2n-1} IN FIELD SPACE is R_field = 1 (normalized modes).
    # The radius in POSITION SPACE is R_n = R_field / M_c = λ (just one kink width!?)

    # That gives R_n = λ, independent of d_n. Not right.

    # The factor d_n must come from: n kinks need to be SEPARATED by at least
    # one kink width each to be independent → R_n ≈ n × λ.
    # For d_n = 2n-1: d_1=1, d_2=3, d_3=5...
    # n=1: d_1=1, R_1=λ; n=2: d_2=3, R_2=3λ; n=3: d_3=5, R_3=5λ.
    # But we need R_n = πd_nλ/I₄ ≈ (3π/4)d_nλ ≈ 2.36 d_n λ.
    # The factor π/I₄ = π×3/4 ≈ 2.36 is still missing.

    # π/I₄ = π/(4/3) = 3π/4. Where does 3π/4 come from?
    # It's the ratio of the Hopf fiber circumference 2πR to 2R (diameter-based):
    # 3π/4 = π/I₄... this is just an algebraic identity, not an explanation.

    return {
        'lam': lam, 'phi0': phi0, 'n': n,
        'f_sq_computed': f_sq_computed,
        'f_sq_formula': f_sq_formula,
        'f_sq_error': abs(f_sq_computed - f_sq_formula) / f_sq_formula,
        'R_n_over_lam_claim': PI * (2*n-1) / I4,
        'n_kink_separation': 2*n-1,  # number of kink widths for n separated kinks
        'pi_over_I4': PI / I4,       # the extra factor needed beyond n_kink_separation × λ
    }


def run_all():
    print("=" * 70)
    print("moduli_space_radius.py — Cycle 108")
    print("Probing R_n/λ = πd_n/I₄ from kink moduli space")
    print("=" * 70)

    # --- Step 1: Zero mode properties ---
    print("\nStep 1: Kink zero mode η₀(x) = sech²(x/λ)/λ — key integrals")
    print("-" * 60)
    props = kink_zero_mode_properties()
    print(f"  λ = {props['lam']:.4f},  φ₀ = {props['phi0']:.4f}")
    print(f"  ‖η₀_raw‖² = ∫sech⁴/λ dx = I₄/λ × φ₀² = f² = {props['eta0_norm_sq']:.6f}")
    print(f"  f² formula = I₄φ₀²/λ = {props['f_sq']:.6f}  [Cycle 47]")

    anal = compute_k_rms_analytically()
    print(f"\n  Characteristic momentum k_rms × λ = 2/√5 = {anal['k_rms_lam_exact']:.6f}")
    print(f"  [from ∫(η₀')²/∫η₀² = (I₄−I₆)/I₄ × 4/λ² = 4/(5λ²)]")
    print(f"  Target k_char × λ = I₄/π = {I4/PI:.6f}")
    print(f"  Ratio k_char/k_rms = (I₄/π)/(2/√5) = {(I4/PI)/(2/np.sqrt(5)):.6f}")

    # --- Step 2: Fourier analysis ---
    print("\nStep 2: Fourier transform η̂₀(k) = πkλ/sinh(πkλ/2)")
    print("-" * 60)
    ft = fourier_zero_mode()
    print(f"  η̂₀(0) = 2  [L'Hôpital limit]")
    print(f"  1/e half-width: kλ = {ft['kl_half_e']:.4f}")
    print(f"  Inflection point: kλ = {ft['kl_inflect']:.4f}")
    print(f"  Target I₄/π: kλ = {ft['I4_over_pi']:.4f}")
    print(f"\n  Note: I₄/π ≈ 0.424 is between the 1/e width and k=0.")
    print(f"  The Fourier transform does not have a natural peak at I₄/π.")

    # --- Step 3: Obata matching condition ---
    print("\nStep 3: Obata eigenvalue matching — what condition gives R_n = πd_nλ/I₄?")
    print("-" * 60)
    results, k_char = obata_matching_condition()
    print(f"  For R_n/λ = πd_n/I₄, Obata gives:")
    print(f"  λ₁(S^{{d_n}}(R_n)) × λ² = I₄²/π²  for ALL d_n")
    print(f"  This is d-INDEPENDENT — same eigenvalue (in λ² units) for all fibers.")
    print(f"\n  {'d_n':<6} {'R_n/λ':<12} {'λ₁×λ²':<15} {'k_eff×λ=I₄/π':<15}")
    for r in results:
        print(f"  {r['d']:<6} {r['R_n_lam']:<12.4f} {r['lambda1_lamsq']:<15.8f} {r['k_eff_lam']:<15.8f}")
    print(f"\n  KEY RESULT: λ₁ × λ² = I₄²/π² = {I4**2/PI**2:.8f} for all d_n.")
    print(f"  This means: the effective 'kink eigenvalue' = I₄²/π² × (1/d_n) per fiber.")
    print(f"  Or: the fiber Laplacian eigenvalue matches the kink at scale I₄/(πλ).")
    print(f"\n  What produces I₄/π in the kink spectrum?")
    print(f"  I₄/π = (4/3)/π ≈ 0.4244.")
    print(f"  This is NOT k_rms (≈0.894/λ) or any obvious kink spectral feature.")

    # --- Step 4: Moduli space radius for n kinks ---
    print("\nStep 4: Moduli space radius for n coincident kinks")
    print("-" * 60)
    print(f"  {'n':<5} {'d_n=2n-1':<12} {'R_n/λ claim':<15} {'n×λ':<10} {'ratio':<10}")
    for n in [1, 2, 3]:
        d = 2*n - 1
        R_claim = PI * d / I4
        print(f"  {n:<5} {d:<12} {R_claim:<15.4f} {n:<10.1f} {R_claim/n:.4f}")
    print(f"\n  R_n/λ / (2n-1) = π/I₄ = {PI/I4:.4f}  [constant factor!]")
    print(f"  π/I₄ = π/(4/3) = 3π/4 ≈ {3*PI/4:.4f}")
    print(f"\n  Physical picture: n kinks at separation ~d_n λ = (2n-1)λ each,")
    print(f"  but with a geometric factor π/I₄ = 3π/4 ≈ 2.36 from the kink shape.")
    print(f"  The factor 3π/4 = 3π/(4) has a possible origin:")
    print(f"  3 from I₄=4/3 (kink shape integral); π from Hopf fiber winding.")

    # --- Step 5: Alternative — Wronskian / phase condition ---
    print("\nStep 5: Phase winding condition on ℝ")
    print("-" * 60)
    print(f"  One approach: the kink phase must wind by 2π over distance R_n.")
    print(f"  Phase gradient at kink center: ∂_x(arg φ) = 1/λ  [from tanh profile].")
    print(f"  Winding condition (naive): (1/λ) × R_n = 2π → R_n = 2πλ.")
    print(f"  But this gives d_n-independent R, so it's not the right condition.")
    print(f"\n  For n kinks: average phase gradient = n/(d_n × λ) = 1/λ (trivially).")
    print(f"  The RIGHT condition must count the number of kink ZERO MODES d_n.")
    print(f"\n  CANDIDATE CONDITION (to be proved in Cycle 109+):")
    print(f"  The Hopf fiber length in the MODULI SPACE equals 2π/M_c = 2πλ.")
    print(f"  But the sphere S^{{d_n}}(R_n) has Hopf fiber circumference 2πR_n.")
    print(f"  For consistency: 2πR_n × (d_n / something) = 2πλ → R_n = λ × something/d_n?")
    print(f"  This gives R_n ∝ 1/d_n — wrong direction.")
    print(f"\n  ALTERNATIVE: the n zero modes occupy a BAND of width d_n × λ.")
    print(f"  R_n = π/(I₄) × d_n × λ where π/I₄ is the Hopf circumference factor.")
    print(f"  This is CONSISTENT with the series holonomy result but not yet derived.")

    # --- Summary ---
    print("\n" + "=" * 70)
    print("SUMMARY — Cycle 108 Findings")
    print("=" * 70)
    print()
    print("Established:")
    print("  The Obata matching condition for R_n = πd_nλ/I₄ is:")
    print("    λ₁(S^{d_n}(R_n)) = I₄²/(π²d_nλ²)  for all d_n ∈ {1,3,5}")
    print("  This is d_n-DEPENDENT (∝ 1/d_n), meaning each fiber has a different")
    print("  effective matching eigenvalue. The kink scale I₄/π appears universally.")
    print()
    print("The key factor π/I₄ = 3π/4 ≈ 2.356 cannot be derived from:")
    print("  - k_rms of η₀ (gives 2/√5 ≈ 0.894, ratio ≈ 0.474 off)")
    print("  - 1/e Fourier width of η₀ (numerical, no clean algebraic form)")
    print("  - Phase winding 1/λ (gives R_n = 2πλ, d-independent)")
    print()
    print("Most promising routes:")
    print("  (A) Moduli space metric for n kinks: n-kink separation = (2n-1)λ")
    print("      PLUS geometric factor π/I₄ from Hopf fiber / kink phase relation.")
    print("      Need: show the Hopf fiber circumference IS 2π × (π/I₄) × d_n × λ")
    print("      which requires a new computation linking phase stiffness to fiber radius.")
    print()
    print("  (B) Direct normalization integral on S^{d_n}(R_n) × ℝ:")
    print("      ∫∫ |η₀(x)|² × |K_Hopf(Ω)|²/(R_n^{d_n-1} Vol S^{d_n}) dx dΩ")
    print("      = ‖η₀‖² × |K_Hopf|²/Vol = 1 × R_n²/(C_d R_n^{d_n}) = R_n^{2-d_n}/C_d")
    print("      Set this equal to required mode_norm = 9/(64π):")
    print("      R_n^{2-d_n}/C_d = 9/(64π) → solves for R_n given d_n.")
    print("      This is the most directly computable route. Computing next.")
    print()
    print("Tier status: R_n/λ = πd_n/I₄ remains Tier 4 OPEN.")
    print("Next computation: solve R_n^{2-d_n}/C_{d_n} = 9/(64π) for d_n=1,3,5.")
    print("Check if R_n = πd_nλ/I₄ satisfies this equation.")


if __name__ == '__main__':
    run_all()
