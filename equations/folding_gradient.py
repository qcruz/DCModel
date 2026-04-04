"""
Folding gradient equations — how compression gradients produce gravity.

The Dimensional Folding Model proposes that gravity is not a fundamental force
but the geometric consequence of nonuniform compression rates. Where the compression
field φ varies in space, structure cannot remain uniformly distributed — it
redistributes laterally, which from within D3 appears as gravitational attraction.

This module contains:
  1. The folding gradient field Φ(x) — the dimensional analogue of gravitational potential
  2. The lateral redistribution equation (proto-Einstein equation)
  3. The Newtonian limit derivation
  4. Gravitational wave modes from compression perturbations
  5. The connection between DFC variables and GR tensors (schematic)

STATUS: The Newtonian limit is well-motivated and schematically correct.
The full nonlinear connection to the Einstein field equations is an open derivation.
This is the highest-priority open problem for making DFC quantitatively predictive
in the strong-gravity regime.

Central equation (weak-field, schematic):

    ∇²Φ_fold ≈ 4π G_eff ρ_compression

where:
    Φ_fold    = folding gradient potential (analogous to Newtonian gravitational potential)
    G_eff     = effective gravitational constant (from compression budget geometry)
    ρ_compression = local compression budget density (from compression_field.py)

In the strong-field regime, the full GR field equation is expected to emerge from
the tensor structure of the compression field dynamics — see open problems below.

Usage:
    python equations/folding_gradient.py
"""

import math

# ── Physical constants ────────────────────────────────────────────────────────

G_NEWTON     = 6.674e-11    # N m² kg⁻²
C_LIGHT_SI   = 2.998e8      # m/s
HBAR_SI      = 1.055e-34    # J·s
M_PLANCK_KG  = 2.176e-8     # kg  (Planck mass)
L_PLANCK_M   = 1.616e-35    # m   (Planck length)


# ── Newtonian limit ───────────────────────────────────────────────────────────

def newtonian_potential(mass_kg, r_m):
    """
    Standard Newtonian gravitational potential Φ = -GM/r.

    In the DFC interpretation, this is the long-range limit of the folding
    gradient field produced by a stable compression closure (mass) at distance r.

    Parameters
    ----------
    mass_kg : float
        Mass of the source in kg.
    r_m : float
        Distance from source in meters.

    Returns
    -------
    float : Φ in m²/s²  (negative = attractive)
    """
    return -G_NEWTON * mass_kg / r_m


def folding_gradient_potential(rho_compression, volume_m3):
    """
    Schematic folding gradient potential for a uniform compression region.

    ∇²Φ_fold = 4π G_eff ρ_compression
    → For a sphere of radius R:  Φ_fold(R) ≈ -G_eff M_compression / R

    This matches the Newtonian potential when:
        G_eff = G_Newton
        M_compression = ρ_compression × V = total compression budget in region

    Parameters
    ----------
    rho_compression : float
        Compression budget density (energy density proxy, in J/m³).
    volume_m3 : float
        Volume of the compression region in m³.

    Returns
    -------
    dict with potential and interpretation.
    """
    M_compression = rho_compression * volume_m3
    R = (3 * volume_m3 / (4 * math.pi))**(1/3)
    Phi = -G_NEWTON * M_compression / (C_LIGHT_SI**2 * R)

    return {
        'M_compression_kg_equiv':   M_compression / C_LIGHT_SI**2,
        'effective_radius_m':       R,
        'folding_potential':        Phi,
        'note': ('Compression budget M_compression = ρ × V maps to gravitational '
                 'mass via E = mc². The DFC connection is G_eff = G_Newton when '
                 'compression budget density = mass-energy density.'),
    }


# ── GR connection (schematic) ─────────────────────────────────────────────────

def gr_connection_schematic():
    """
    Schematic mapping between DFC variables and GR tensors.

    This is the key open derivation. The target is to show that the DFC
    field equation reduces to the Einstein field equations:

        G_μν = (8πG/c⁴) T_μν

    when the compression field is in the slowly-varying, weak-field regime.

    Current status:
      - The stress-energy tensor T_μν is identified with the compression
        budget distribution (energy density, flux, pressure)
      - The Einstein tensor G_μν encodes the shape of differential compression
        gradients — the curvature of the effective metric
      - The coupling 8πG/c⁴ encodes the ratio of the compression budget
        to the geometric deformation it produces — not yet derived from
        the DFC substrate parameters

    Returns a dictionary of the provisional mapping.
    """
    return {
        'T_00 (energy density)':    'ρ_B = compression budget density',
        'T_0i (energy flux)':       'J_B = compression budget current',
        'T_ij (pressure/stress)':   'σ_ij = compression stress tensor',
        'G_μν (Einstein tensor)':   'Γ_μν = curvature from compression gradient',
        'g_μν (metric)':            'emergent from compression field configuration',
        'G_Newton':                 'to be derived from (α, β, c) of compression field',
        'coupling 8πG/c⁴':          'ratio of compression-to-geometry, open derivation',
        'geodesic equation':        'path of minimum compression budget variation',
        'status': ('OPEN: Full derivation requires showing that the DFC field '
                   'equation, in the appropriate limit, produces the Bianchi identity '
                   '∇_μ G^μν = 0 and the correct light bending / perihelion precession.'),
    }


def planck_scale_from_compression():
    """
    The Planck scale as a compression field parameter.

    The Planck length L_Pl = √(ℏG/c³) is the scale at which the compression
    field buckles — the minimum spatial scale of a stable fold transition.

    In DFC:
        L_Pl ~ kink width λ = √(2c²/α)
        → α ~ 2c²/L_Pl² ~ 2c⁵/(ℏG)

    This gives α in SI units from known physical constants.
    It is a self-consistency check: if the kink width equals the Planck length,
    what are the values of (α, β)?

    Returns
    -------
    dict with derived compression field parameters at Planck scale.
    """
    # L_Pl = sqrt(2c²/α) → α = 2c²/L_Pl²
    alpha_si = 2 * C_LIGHT_SI**2 / L_PLANCK_M**2

    # kink energy = (4/3)c√(2α³/β) = Planck energy E_Pl = M_Pl c²
    # Solve for β:
    E_planck = M_PLANCK_KG * C_LIGHT_SI**2
    # E_kink = (4/3)c√(2α³/β) = E_Pl
    # → β = 2α³ × c² × (4/3)² / E_Pl²
    beta_si = 2 * alpha_si**3 * C_LIGHT_SI**2 * (4/3)**2 / E_planck**2

    return {
        'alpha_si':         alpha_si,
        'beta_si':          beta_si,
        'L_planck_m':       L_PLANCK_M,
        'E_planck_j':       E_planck,
        'kink_width_check': math.sqrt(2 * C_LIGHT_SI**2 / alpha_si),
        'note': ('If kink width = Planck length, α and β take these values. '
                 'This sets the fundamental compression scale of the substrate.'),
    }


# ── Gravitational wave analogue ───────────────────────────────────────────────

def compression_wave_speed(alpha, beta, c=1.0):
    """
    Speed of small-amplitude compression waves around the stable minimum.

    For perturbations δφ around φ_0 = √(α/β):
        ω² = c²k² + V''(φ_0) = c²k² + 2α

    At long wavelengths (k → 0), the group velocity approaches:
        v_group = ∂ω/∂k → c  as  k → ∞  (massless limit)

    Gravitational waves in GR travel at c. In DFC, compression perturbations
    in the high-k limit propagate at c — consistent with observed gravitational
    wave speed.

    For massive perturbations (k small), there is a dispersion:
        v_group = c²k / √(c²k² + 2α) < c

    This predicts graviton mass ~ √(2α) in natural units — should be zero (or
    very small) to match GR. This constrains α at cosmological scales.

    Returns
    -------
    dict with wave speeds at various k values.
    """
    m_eff_sq = 2 * alpha  # V''(φ_stable) = 2α

    results = {}
    for k in [0.01, 0.1, 1.0, 10.0, 100.0]:
        omega_sq = c**2 * k**2 + m_eff_sq
        omega = math.sqrt(omega_sq)
        v_phase = omega / k
        v_group = c**2 * k / omega
        results[f'k={k}'] = {
            'omega': omega,
            'v_phase': v_phase,
            'v_group': v_group,
        }

    return {
        'm_eff_sq_graviton': m_eff_sq,
        'graviton_mass_natural': math.sqrt(m_eff_sq),
        'constraint': 'Must be << cosmological Hubble scale for GR consistency',
        'dispersion': results,
    }


# ── Main output ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("FOLDING GRADIENT — PROTO-GRAVITY EQUATIONS")
    print("Dimensional Folding Model")
    print("=" * 65)

    print(f"\n--- Planck Scale from Compression Field ---")
    pl = planck_scale_from_compression()
    print(f"  Planck length:      {pl['L_planck_m']:.4e} m")
    print(f"  α (SI):             {pl['alpha_si']:.4e}")
    print(f"  β (SI):             {pl['beta_si']:.4e}")
    print(f"  Kink width check:   {pl['kink_width_check']:.4e} m  "
          f"(should = {pl['L_planck_m']:.4e} m)")
    print(f"  {pl['note']}")

    print(f"\n--- Gravitational Wave / Compression Wave Speed ---")
    waves = compression_wave_speed(alpha=0.01, beta=1.0, c=1.0)
    print(f"  Effective graviton mass²: {waves['m_eff_sq_graviton']:.4f}  "
          f"(must be ≈ 0 cosmologically)")
    print(f"  {'k':>8}  {'v_group':>10}  {'v_phase':>10}")
    for key, vals in waves['dispersion'].items():
        print(f"  {key:>8}  {vals['v_group']:>10.4f}  {vals['v_phase']:>10.4f}")

    print(f"\n--- GR Connection Map (Schematic) ---")
    mapping = gr_connection_schematic()
    for k, v in mapping.items():
        if k != 'status':
            print(f"  {k:30s}: {v}")
    print(f"\n  Status: {mapping['status']}")

    print(f"\n--- Open Problems ---")
    print(f"  1. Derive G_Newton from compression field parameters (α, β, c)")
    print(f"  2. Show Bianchi identity from DFC field equation")
    print(f"  3. Reproduce light bending angle and perihelion precession from DFC")
    print(f"  4. Constrain graviton mass (m_eff_sq → 0 requires α << cosmological scale)")
    print(f"  See: phenomena/gravity/general_relativity.md, foundations/substrate.md")
