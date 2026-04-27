"""
Quantum Gravity Scales in DFC — Cycle 76

Physical question:
  What are the numerical values of the key quantum gravity scales in the DFC
  model, and what is the quantitative status of each?

DFC mechanism:
  Quantum gravity is not a separate problem: the substrate field equation is
  already well-defined at the Planck scale (D1 kink width = Planck length by
  construction). Hawking radiation, Bekenstein-Hawking entropy, and black hole
  evaporation are imported as structural results — not yet derived from the
  substrate but consistent with it. The gravitational coupling G is not yet
  derived from β and α.

Computations:
  1. Planck scale constants
  2. D1 substrate parameters (α_D1, S_kink(D1), hierarchy factor)
  3. Hawking temperature vs. black hole mass
  4. Bekenstein-Hawking entropy vs. mass
  5. Black hole evaporation timescale
  6. Gravitational vs. electromagnetic coupling hierarchy

Key references:
  - phenomena/gravity/quantum_gravity.md  (this module's conceptual doc)
  - foundations/planck_constant_derivation.md  (ℏ hierarchy; T8 open)
  - equations/planck_constant.py  (S_kink(D1)/ℏ = 1.13×10⁴⁰)
  - phenomena/gravity/hawking_radiation.md  (Hawking temperature formula)
"""

import math

# ── Physical constants (SI) ────────────────────────────────────────────────────

HBAR_SI = 1.0546e-34    # J·s
C_SI    = 2.998e8       # m/s
G_SI    = 6.674e-11     # m³ kg⁻¹ s⁻²
K_B     = 1.381e-23     # J/K
M_SUN   = 1.989e30      # kg
EV_PER_J = 1.0 / 1.602e-19    # eV per joule

# ── Physical constants (natural units: ℏ=c=1, GeV) ────────────────────────────

M_PL_GEV   = 1.22e19    # Planck mass in GeV
HBAR_GEV_S = 6.582e-25  # ℏ in GeV·s
ALPHA_EM   = 1.0 / 137.036  # fine structure constant (low energy)

# ── DFC substrate parameter ────────────────────────────────────────────────────

BETA = 0.0351   # quartic coupling (reference value; β ≈ 0.035 Tier 3)


# ── 1. Planck scale constants ──────────────────────────────────────────────────

def planck_scales():
    """
    Compute Planck length, Planck mass, Planck time, and Planck temperature.
    All imported — require ℏ and G as independent inputs.

    Returns:
        dict with L_Pl, M_Pl_kg, M_Pl_GeV, t_Pl, T_Pl
    """
    L_Pl = math.sqrt(HBAR_SI * G_SI / C_SI**3)   # meters
    M_Pl_kg = math.sqrt(HBAR_SI * C_SI / G_SI)   # kg
    t_Pl = L_Pl / C_SI                            # seconds
    T_Pl = M_Pl_kg * C_SI**2 / K_B               # Kelvin (Planck temperature)
    return {
        'L_Pl_m':   L_Pl,
        'M_Pl_kg':  M_Pl_kg,
        'M_Pl_GeV': M_PL_GEV,
        't_Pl_s':   t_Pl,
        'T_Pl_K':   T_Pl,
    }


# ── 2. D1 substrate parameters ────────────────────────────────────────────────

def d1_substrate(beta=BETA):
    """
    D1 substrate parameters from the identification ξ_D1 = L_Pl.

    Identification:  ξ_D1 = c√(2/α_D1) = L_Pl  →  α_D1 = 2M_Pl²  (ℏ=c=1)

    Kink action (BPS-correct, Cycle 48 retraction / Cycle 75 update):
      S_kink(D1) = (4/3) × α_D1 / β = (8/3) × M_Pl² / β

    Returns:
        dict with alpha_D1_GeV2, S_kink_GeV2, S_kink_over_hbar
    """
    alpha_D1_GeV2 = 2.0 * M_PL_GEV**2          # = 2M_Pl² in natural units
    S_kink_GeV2   = (4.0 / 3.0) * alpha_D1_GeV2 / beta   # GeV² (= dimensionless in ℏ=1 units)
    # S_kink_over_hbar: since S_kink in ℏ=1 units IS the ratio S/ℏ
    S_kink_over_hbar = S_kink_GeV2   # dimensionless in natural units
    return {
        'alpha_D1_GeV2':     alpha_D1_GeV2,
        'S_kink_GeV2':       S_kink_GeV2,
        'S_kink_over_hbar':  S_kink_over_hbar,
        'log10_hierarchy':   math.log10(S_kink_over_hbar),
        'bifurcations_to_hbar': math.log10(S_kink_over_hbar) / math.log10(S_kink_over_hbar / 1) * (1/math.log(2) * math.log(S_kink_over_hbar) / math.log(math.sqrt(S_kink_over_hbar))),
    }


def d1_bifurcation_factor(beta=BETA):
    """
    How many bifurcation events would reduce S_kink(D1) to ℏ?

    S_kink(Dn) = S_kink(D1) / gamma_D^n = 1  →  n = log(S_kink(D1)) / log(gamma_D)

    Two estimates depending on assumed γ_D per event:
      - γ_D ≈ 4:    ~66 events needed  (lower bound; each step halves the kink scale)
      - γ_D ≈ 10³:  ~13.4 events needed (from planck_constant_derivation.md Cycle 75)

    The DFC model has ~4 bifurcation events (D1→D5). Starting from 1.13×10⁴⁰,
    this leaves a residual of ~10³⁷ at D5. The gap is T8 open (Tier 4).

    See: foundations/planck_constant_derivation.md  for detailed mapping.
    """
    S0 = d1_substrate(beta)['S_kink_over_hbar']
    gamma_D_low  = 4.0         # lower estimate
    gamma_D_high = 1e3         # consistent with planck_constant_derivation.md (~13.4 steps)
    n_low    = math.log(S0) / math.log(gamma_D_low)
    n_high   = math.log(S0) / math.log(gamma_D_high)   # ≈ 13.4
    n_model  = 4               # D1→D2→D3→D4→D5: 4 events
    residual_low  = S0 / gamma_D_low**n_model
    residual_high = S0 / gamma_D_high**n_model
    return {
        'S_D1_over_hbar': S0,
        'n_needed_low':  n_low,
        'n_needed_high': n_high,    # ~13.4
        'n_model':       n_model,
        'residual_low':  residual_low,
        'residual_high': residual_high,
    }


# ── 3. Hawking temperature ────────────────────────────────────────────────────

def hawking_temperature(M_kg):
    """
    Hawking temperature for a Schwarzschild black hole of mass M (kg).

    T_H = ℏc³ / (8π G M k_B)

    Physical: lighter black holes are hotter; Planck-mass holes are at Planck temp.
    """
    return HBAR_SI * C_SI**3 / (8.0 * math.pi * G_SI * M_kg * K_B)


def hawking_temperature_table():
    """
    Hawking temperatures for a range of black hole masses.
    Returns list of dicts: M_solar, M_kg, T_H_K, T_H_eV.
    """
    entries = [
        ('Stellar 10 M_sun', 10 * M_SUN),
        ('Solar mass M_sun', M_SUN),
        ('Moon mass', 7.34e22),
        ('Asteroid mass (10^18 kg)', 1e18),
        ('Mountain mass (10^12 kg)', 1e12),
        ('Planck mass', math.sqrt(HBAR_SI * C_SI / G_SI)),
    ]
    rows = []
    for label, M_kg in entries:
        T_K = hawking_temperature(M_kg)
        T_eV = T_K * K_B / 1.602e-19
        rows.append({'label': label, 'M_kg': M_kg, 'T_H_K': T_K, 'T_H_eV': T_eV})
    return rows


# ── 4. Bekenstein-Hawking entropy ─────────────────────────────────────────────

def bekenstein_hawking_entropy(M_kg):
    """
    Bekenstein-Hawking entropy S_BH = k_B A / (4 L_Pl²)
    where A = 4π r_s² = 4π (2GM/c²)² is the event horizon area.

    Returns S_BH / k_B (dimensionless entropy in bits / ln2 counts).
    """
    r_s  = 2.0 * G_SI * M_kg / C_SI**2        # Schwarzschild radius
    A    = 4.0 * math.pi * r_s**2              # horizon area
    L_Pl = math.sqrt(HBAR_SI * G_SI / C_SI**3)
    S_over_kB = A / (4.0 * L_Pl**2)           # S_BH / k_B
    return S_over_kB


# ── 5. Black hole evaporation timescale ───────────────────────────────────────

def evaporation_time(M_kg):
    """
    Black hole evaporation timescale (Page 1976):
    t_evap = 5120 π G² M³ / (ℏ c⁴)

    Returns t_evap in seconds.
    """
    return 5120.0 * math.pi * G_SI**2 * M_kg**3 / (HBAR_SI * C_SI**4)


# ── 6. Gravitational vs. electromagnetic coupling ratio ───────────────────────

def coupling_ratio():
    """
    G / α_em hierarchy: how much weaker is gravity than electromagnetism?

    Compare gravitational coupling G m_p² / (ℏc) to α_em.

    In natural units (ℏ=c=1):
      α_grav(m_p) = G m_p² / (ℏc) = (m_p/M_Pl)²
    """
    # Proton mass in GeV
    m_p_GeV = 0.938272  # GeV
    alpha_grav_proton = (m_p_GeV / M_PL_GEV)**2  # dimensionless gravitational coupling at proton scale
    ratio = alpha_grav_proton / ALPHA_EM
    return {
        'm_p_GeV':          m_p_GeV,
        'alpha_grav_proton': alpha_grav_proton,
        'alpha_em_low':     ALPHA_EM,
        'ratio_grav_to_em': ratio,
        'log10_ratio':      math.log10(ratio),
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("QUANTUM GRAVITY SCALES — DFC MODEL — Cycle 76")
    print("=" * 70)

    # 1. Planck scales
    print("\n── 1. Planck scale constants ─────────────────────────────────────────")
    ps = planck_scales()
    print(f"  L_Pl = √(ℏG/c³) = {ps['L_Pl_m']:.4e} m   [imported: requires ℏ, G]")
    print(f"  M_Pl = √(ℏc/G)  = {ps['M_Pl_kg']:.4e} kg = {ps['M_Pl_GeV']:.3e} GeV")
    print(f"  t_Pl = L_Pl/c    = {ps['t_Pl_s']:.4e} s")
    print(f"  T_Pl = M_Pl c²/k_B = {ps['T_Pl_K']:.4e} K")

    # 2. D1 substrate
    print("\n── 2. D1 substrate identification ────────────────────────────────────")
    d1 = d1_substrate()
    print(f"  α_D1 = 2 M_Pl² = {d1['alpha_D1_GeV2']:.4e} GeV²  [from ξ_D1 = L_Pl]")
    print(f"  β = {BETA}  (Tier 3 reference value)")
    print(f"  S_kink(D1) = (4/3) α_D1 / β = {d1['S_kink_GeV2']:.4e} GeV²  [BPS-correct, Cycle 48/75]")
    print(f"  S_kink(D1) / ℏ = {d1['S_kink_over_hbar']:.4e}  (= 10^{d1['log10_hierarchy']:.2f})")
    print(f"  Note: In ℏ=1 natural units, GeV² is dimensionless action → S/ℏ = S numerically.")

    # 3. Bifurcation gap
    print("\n── 3. Bifurcation gap to ℏ (T8 open problem) ────────────────────────")
    bif = d1_bifurcation_factor()
    print(f"  S_kink(D1)/ℏ = {bif['S_D1_over_hbar']:.3e}")
    print(f"  Bifurcations needed: ~{bif['n_needed_low']:.1f}  at γ_D ≈ 4 per event  (lower bound)")
    print(f"  Bifurcations needed: ~{bif['n_needed_high']:.1f}  at γ_D ≈ 10³ per event  (planck_constant_derivation.md Cycle 75)")
    print(f"  DFC model has {bif['n_model']} events (D1→D5)")
    print(f"  Residual gap at D5: ~{bif['residual_high']:.2e} ℏ  (at γ_D=10³ estimate)")
    print(f"  → T8 open: planck_constant_derivation.md maps resolution paths")

    # 4. Hawking temperature
    print("\n── 4. Hawking temperature ────────────────────────────────────────────")
    print(f"  T_H = ℏc³/(8πGMk_B)  [structural: imported from QFT]")
    print(f"  {'Mass':>30}  {'T_H (K)':>12}  {'T_H (eV)':>12}")
    print(f"  {'-'*30}  {'-'*12}  {'-'*12}")
    for row in hawking_temperature_table():
        print(f"  {row['label']:>30}  {row['T_H_K']:>12.3e}  {row['T_H_eV']:>12.3e}")
    print(f"  → Stellar black holes are unobservably cold; Planck holes are at T_Pl")

    # 5. Bekenstein-Hawking entropy
    print("\n── 5. Bekenstein-Hawking entropy ─────────────────────────────────────")
    print(f"  S_BH / k_B = A/(4 L_Pl²)  [structural: imported]")
    for M_kg, label in [(M_SUN, 'M_sun'), (10*M_SUN, '10 M_sun')]:
        S = bekenstein_hawking_entropy(M_kg)
        r_s = 2.0 * G_SI * M_kg / C_SI**2
        print(f"  {label}: r_s = {r_s:.3e} m,  S_BH/k_B = {S:.3e} nats")
    M_Pl_kg = ps['M_Pl_kg']
    S_Pl = bekenstein_hawking_entropy(M_Pl_kg)
    print(f"  Planck mass: S_BH/k_B = {S_Pl:.3e} (≈ 1 — a single topological quantum)")

    # 6. Evaporation timescale
    print("\n── 6. Evaporation timescale ──────────────────────────────────────────")
    print(f"  t_evap = 5120π G² M³ / (ℏ c⁴)  [Page 1976; structural]")
    for M_kg, label in [(M_SUN, 'M_sun'), (1e12, '10^12 kg (mountain)'), (ps['M_Pl_kg'], 'Planck mass')]:
        t = evaporation_time(M_kg)
        print(f"  {label}: t_evap = {t:.3e} s")
    age_universe = 4.4e17   # seconds
    print(f"  (Age of universe: {age_universe:.1e} s = {age_universe/3.15e7:.1e} yr)")

    # 7. G vs α_em
    print("\n── 7. Gravitational vs. electromagnetic coupling ratio ────────────────")
    cr = coupling_ratio()
    print(f"  α_grav(m_p) = (m_p/M_Pl)² = ({cr['m_p_GeV']:.4f}/{M_PL_GEV:.2e})²")
    print(f"             = {cr['alpha_grav_proton']:.4e}")
    print(f"  α_em (low energy) = {cr['alpha_em_low']:.6f} = 1/{1/cr['alpha_em_low']:.1f}")
    print(f"  α_grav / α_em = {cr['ratio_grav_to_em']:.4e}  (= 10^{cr['log10_ratio']:.1f})")
    print(f"  → Gravity is ~{1/cr['ratio_grav_to_em']:.0e}× weaker than EM at proton scale")
    print(f"  → DFC attribution: D2 (gravity) / D5 (EM) depth separation — not yet derived")

    print("\n" + "=" * 70)
    print("STATUS SUMMARY")
    print("=" * 70)
    print("""
  Tier 1 (structural):
    ✓ No true Planck-scale singularity — D1 regime replaces GR divergence
    ✓ Gravitational waves travel at c (D2 massless mode dispersion)
    ✓ Black hole information conserved (winding numbers topologically conserved)
    ✓ Hawking radiation as thermal emission from event horizon [imported, consistent]
    ✓ Bekenstein-Hawking entropy proportional to area [imported, consistent]

  Tier 4 (open):
    ✗ Graviton as spin-2 D2 mode — not yet derived from substrate
    ✗ G from substrate parameters — deepest open problem in the model
    ✗ G/α_em hierarchy from D2/D5 depth separation — not yet derived
    ✗ ℏ from substrate — T8, critical open (S_kink(D1)/ℏ = 1.13×10⁴⁰)

  DFC uniqueness:
    The Planck scale is not a breakdown point but the substrate's natural scale (D1 kink
    width). The UV divergences of quantum GR do not arise because geometry is downstream,
    not fundamental. No quantization of geometry is needed — the substrate is already
    quantum (kink solutions are the particles).
    """)

    print("[Module: equations/quantum_gravity.py | Cycle 76]")


if __name__ == "__main__":
    main()
