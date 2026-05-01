"""
Z Boson Partial Decay Widths — DFC Module (Cycle 93)
====================================================

Physical question addressed:
    Can the DFC electroweak coupling chain predict the Z boson partial and
    total decay widths, the invisible width, and electroweak precision
    asymmetries — all from β with no additional free parameters?

DFC mechanism:
    The Z boson is the neutral gauge boson of the D6 SU(2) closure topology,
    lifted in mass by the S³ squashing (the DFC Higgs mechanism). Its
    coupling strength to each fermion follows from the product topology
    U(1) × SU(2) × SU(3): each fermion's quantum numbers (weak isospin T₃
    and hypercharge Y, hence electric charge Q = T₃ + Y/2) are structurally
    determined by which closure sectors it participates in.

    The partial width of the Z boson decaying to a fermion-antifermion pair
    is set by two quantities:
      (1) the overall weak decay scale G_F M_Z³ — which comes from the DFC
          coupling chain β → g_common → (sin²θ_W, M_Z, G_F)
      (2) the sum of squared vector and axial couplings (g_V)² + (g_A)² —
          which is fixed by the fermion's T₃ and Q quantum numbers

    The vector coupling strength g_V equals the fermion's weak isospin T₃
    minus twice its electric charge Q times sin²θ_W.
    The axial coupling strength g_A equals the fermion's weak isospin T₃.

    The partial width formula (massless fermion limit) is:
        Γ(Z→ff̄) = (N_c G_F M_Z³) / (6π√2) × [(g_V)² + (g_A)²]
    where N_c = 3 for quarks (color factor) and N_c = 1 for leptons.
    Quark channels receive an additional QCD correction factor (1 + α_s/π).

FREE PARAMETERS: β = 0.0351 (entire coupling chain), v = 246 GeV (Higgs VEV)
  — the same two parameters as all other electroweak Tier 2a predictions.
  The quantum numbers T₃, Q, N_c are Tier 1 structural predictions.

Key references:
    equations/muon_lifetime.py         (G_F, M_Z, sin²θ_W, g₂ from DFC chain)
    equations/electroweak_precision.py  (ρ=1, T=0 precision checks)
    equations/coupling_derivation.py    (β → g_common → α_em)
    phenomena/particle_physics/particles/w_z_bosons.md
    phenomena/particle_physics/forces/electroweak.md
"""

import math
import sys
import os

# ── Import DFC coupling chain ─────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(__file__))
from muon_lifetime import (
    weak_coupling_from_chain,
    w_boson_mass,
    z_boson_mass,
    fermi_constant,
)
from coupling_derivation import coupling_chain_from_beta

# ── DFC electroweak inputs (from coupling chain) ──────────────────────────────
BETA     = 0.0351      # quartic coupling (Tier 3 reference)
V_EW     = 246.0       # Higgs VEV in GeV (input; Bottleneck 3 derivation open)

_ew  = weak_coupling_from_chain()
sin2 = _ew['sin2_tw']
g2   = _ew['g2']
m_w  = w_boson_mass(g2, v=V_EW)                  # DFC: 79.67 GeV
m_z  = z_boson_mass(m_w, sin2)                   # DFC: 90.86 GeV
G_F  = fermi_constant(g2, m_w)                   # DFC: 1.168×10⁻⁵ GeV⁻²

# DFC strong coupling at M_Z (11% off — see alpha_s_target.py, Cycle 77)
_chain     = coupling_chain_from_beta(BETA)
alpha_s_mz = _chain["alpha_s_mz"]                # 0.105 (11% below SM 0.1182)

# ── PDG reference values ──────────────────────────────────────────────────────
PDG = {
    "M_Z":          91.1876,   # GeV
    "Gamma_Z":      2.4952,    # GeV (total)
    "Gamma_ee":     0.083984,  # GeV (also mu, tau at tree level)
    "Gamma_mumu":   0.083984,
    "Gamma_tautau": 0.083793,  # slight tau mass effect
    "Gamma_inv":    0.4990,    # GeV (3 neutrino species)
    "Gamma_had":    1.7444,    # GeV
    "Gamma_nunu":   0.1660,    # GeV per neutrino flavour
    "R_l":          20.767,    # Gamma_had / Gamma_ll (average lepton)
    "R_b":          0.21629,   # Gamma_bb / Gamma_had
    "A_FB_lep":     0.01626,   # leptonic forward-backward asymmetry
    "A_FB_b":       0.0996,    # b-quark forward-backward asymmetry
    "sin2_theta_eff": 0.23122, # effective leptonic weak mixing angle
}

# ── Fermion quantum numbers: (name, T3, Q, N_c) ──────────────────────────────
FERMIONS = [
    # leptons
    ("nu_e",   +0.5,   0.0,  1),   # electron neutrino
    ("nu_mu",  +0.5,   0.0,  1),   # muon neutrino
    ("nu_tau", +0.5,   0.0,  1),   # tau neutrino
    ("e",      -0.5,  -1.0,  1),   # electron
    ("mu",     -0.5,  -1.0,  1),   # muon
    ("tau",    -0.5,  -1.0,  1),   # tau lepton
    # quarks (massless limit; top excluded — m_t > M_Z/2)
    ("u",      +0.5,  +2/3,  3),   # up
    ("c",      +0.5,  +2/3,  3),   # charm
    ("d",      -0.5,  -1/3,  3),   # down
    ("s",      -0.5,  -1/3,  3),   # strange
    ("b",      -0.5,  -1/3,  3),   # bottom
]


# ─────────────────────────────────────────────────────────────────────────────
# Core functions
# ─────────────────────────────────────────────────────────────────────────────

def couplings(t3, q, sin2_theta_w):
    """
    The vector and axial coupling strengths of the Z boson to a fermion
    with weak isospin T₃ and electric charge Q.

    The vector coupling equals T₃ minus twice Q times sin²θ_W.
    The axial coupling equals T₃.
    """
    g_v = t3 - 2.0 * q * sin2_theta_w
    g_a = t3
    return g_v, g_a


def partial_width_unit(m_z_gev, G_F_gev):
    """
    The overall decay scale Γ_unit = G_F M_Z³ / (6π√2) in GeV.

    This is the natural unit for all Z partial widths: every partial width
    equals N_c × Γ_unit × (g_V² + g_A²) × QCD_correction.
    """
    return G_F_gev * m_z_gev**3 / (6.0 * math.pi * math.sqrt(2.0))


def partial_width(t3, q, n_c, m_z, G_F, sin2_theta_w, alpha_s=0.0, is_quark=False):
    """
    Partial width Γ(Z→ff̄) in GeV for a fermion with quantum numbers
    (T₃, Q, N_c), using the massless fermion approximation.

    For quarks (is_quark=True), multiply by the QCD correction factor
    (1 + α_s/π). This adds one power of the strong coupling strength to
    the decay rate.
    """
    g_v, g_a = couplings(t3, q, sin2_theta_w)
    gamma_unit = partial_width_unit(m_z, G_F)
    width = n_c * gamma_unit * (g_v**2 + g_a**2)
    if is_quark and alpha_s > 0:
        width *= (1.0 + alpha_s / math.pi)
    return width


def asymmetry_parameter(g_v, g_a):
    """
    The asymmetry parameter A_f = 2 g_V g_A / (g_V² + g_A²).

    This measures how much the Z coupling distinguishes left-handed from
    right-handed fermions: A_f = 0 for a pure vector coupling, A_f = ±1
    for a pure axial coupling. A_f for charged leptons is small because
    g_V ≪ g_A near sin²θ_W = 1/4.
    """
    denom = g_v**2 + g_a**2
    if denom < 1e-30:
        return 0.0
    return 2.0 * g_v * g_a / denom


def forward_backward_asymmetry(af_e, af_f):
    """
    The forward-backward asymmetry at the Z pole:
        A_FB^f = (3/4) × A_e × A_f

    The three-quarters factor comes from integrating cos²θ in the angular
    distribution of a spin-1 resonance decay.
    """
    return (3.0 / 4.0) * af_e * af_f


# ─────────────────────────────────────────────────────────────────────────────
# Compute all DFC predictions
# ─────────────────────────────────────────────────────────────────────────────

def all_partial_widths(sin2_theta_w=None, m_z_gev=None, G_F_gev=None,
                       alpha_s=None):
    """
    Compute all Z partial widths and derived observables from the DFC
    coupling chain. Returns a dict of (predicted, observed, error_pct) tuples.
    """
    if sin2_theta_w is None: sin2_theta_w = sin2
    if m_z_gev      is None: m_z_gev      = m_z
    if G_F_gev      is None: G_F_gev      = G_F
    if alpha_s      is None: alpha_s      = alpha_s_mz

    results = {}
    widths  = {}

    for name, t3, q, n_c in FERMIONS:
        is_q = (n_c == 3)
        w = partial_width(t3, q, n_c, m_z_gev, G_F_gev, sin2_theta_w,
                          alpha_s=alpha_s, is_quark=is_q)
        widths[name] = w

    # Individual leptonic widths
    results["Gamma_ee"]     = widths["e"]
    results["Gamma_mumu"]   = widths["mu"]
    results["Gamma_tautau"] = widths["tau"]   # same at tree level (massless)

    # Invisible: 3 × Γ(Z→νν̄)
    gamma_nu = widths["nu_e"]                # all three equal at tree level
    results["Gamma_nunu_each"] = gamma_nu
    results["Gamma_inv"]  = 3.0 * gamma_nu

    # Hadronic: sum over u, c, d, s, b
    gamma_had = sum(widths[q] for q in ["u","c","d","s","b"])
    results["Gamma_had"]  = gamma_had

    # Total width
    gamma_lep = widths["e"] + widths["mu"] + widths["tau"]
    gamma_Z   = gamma_lep + results["Gamma_inv"] + gamma_had
    results["Gamma_Z"]    = gamma_Z

    # R_l = Gamma_had / Gamma_ll (one lepton flavor)
    results["R_l"]        = gamma_had / widths["e"]

    # R_b = Gamma_bb / Gamma_had
    results["R_b"]        = widths["b"] / gamma_had

    # Asymmetry parameters
    gv_e, ga_e = couplings(-0.5, -1.0, sin2_theta_w)
    gv_b, ga_b = couplings(-0.5, -1/3, sin2_theta_w)

    A_e = asymmetry_parameter(gv_e, ga_e)
    A_b = asymmetry_parameter(gv_b, ga_b)

    results["A_e"]         = A_e
    results["A_b"]         = A_b
    results["A_FB_lep"]    = forward_backward_asymmetry(A_e, A_e)
    results["A_FB_b"]      = forward_backward_asymmetry(A_e, A_b)

    # Effective sin²θ from lepton asymmetry (tree-level: same as input)
    # A_e = (1 - 4sin²θ_eff^lep) / sqrt(1 - 4sin²θ_eff + 8sin²²θ_eff) ... simplified:
    # At tree level sin²θ_eff = sin²θ_W
    results["sin2_theta_eff"] = sin2_theta_w   # tree level; loop corrections not computed

    return results, widths


# ─────────────────────────────────────────────────────────────────────────────
# Main output
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("  Z Boson Decay Widths — DFC Predictions (Cycle 93)")
    print("=" * 70)

    print(f"\n--- DFC Electroweak Inputs (from coupling chain) ---")
    print(f"  β (quartic coupling)    = {BETA}")
    print(f"  v (Higgs VEV, input)    = {V_EW} GeV")
    print(f"  sin²θ_W(M_Z)            = {sin2:.6f}  (Route 3B: 0.2312)")
    print(f"  M_Z (DFC)               = {m_z:.4f} GeV  (obs: 91.1876 GeV)")
    print(f"  G_F (DFC)               = {G_F:.6e} GeV⁻²")
    print(f"  α_s(M_Z) (DFC)          = {alpha_s_mz:.4f}  (obs: 0.1182; 11% off)")

    # Common scale
    gamma_unit = partial_width_unit(m_z, G_F)
    print(f"\n--- Common decay scale ---")
    print(f"  Γ_unit = G_F M_Z³/(6π√2)  = {gamma_unit*1000:.3f} MeV")
    print(f"  (Sets the natural scale for all Z partial widths)")

    # Coupling strengths
    print(f"\n--- Z coupling strengths g_V, g_A for each fermion type ---")
    print(f"  {'Fermion':<10} {'T₃':>6} {'Q':>6} {'N_c':>4} "
          f"{'g_V':>8} {'g_A':>8} {'g_V²+g_A²':>12}")
    print("  " + "-" * 62)
    printed_types = set()
    for name, t3, q, n_c in FERMIONS:
        key = (t3, q, n_c)
        if key in printed_types:
            continue
        printed_types.add(key)
        gv, ga = couplings(t3, q, sin2)
        print(f"  {name:<10} {t3:>+6.1f} {q:>+6.4f} {n_c:>4d} "
              f"  {gv:>+7.4f}  {ga:>+7.4f}   {gv**2+ga**2:>10.5f}")

    # All partial widths
    results, widths = all_partial_widths()

    print(f"\n--- Z Partial Widths: DFC vs Observed ---")
    print(f"  {'Channel':<22} {'DFC (MeV)':>12} {'Obs (MeV)':>12} {'Error':>8}  Status")
    print("  " + "-" * 72)

    def row(label, dfc_gev, obs_gev, tier=""):
        dfc_mev  = dfc_gev * 1000
        obs_mev  = obs_gev * 1000
        err      = (dfc_gev / obs_gev - 1.0) * 100.0
        status   = "✓" if abs(err) < 5.0 else "✗"
        print(f"  {label:<22} {dfc_mev:>12.3f} {obs_mev:>12.3f} "
              f"  {err:>+6.2f}%  {status}{tier}")

    row("Z→νν̄ (each gen.)",     results["Gamma_nunu_each"], PDG["Gamma_nunu"])
    row("Z→e⁺e⁻",               results["Gamma_ee"],       PDG["Gamma_ee"])
    row("Z→μ⁺μ⁻",               results["Gamma_mumu"],     PDG["Gamma_mumu"])
    row("Z→τ⁺τ⁻",               results["Gamma_tautau"],   PDG["Gamma_tautau"])
    row("Z→inv (3×νν̄)",         results["Gamma_inv"],      PDG["Gamma_inv"])
    row("Z→hadrons",             results["Gamma_had"],       PDG["Gamma_had"])
    row("Z total",               results["Gamma_Z"],         PDG["Gamma_Z"])

    print(f"\n--- Electroweak Precision Observables ---")
    print(f"  {'Observable':<26} {'DFC':>10} {'Observed':>10} {'Error':>8}  Status")
    print("  " + "-" * 68)

    def row2(label, dfc, obs, unit=""):
        err    = (dfc / obs - 1.0) * 100.0
        status = "✓" if abs(err) < 5.0 else "✗"
        print(f"  {label:<26} {dfc:>10.5f} {obs:>10.5f} "
              f"  {err:>+6.2f}%  {status}  {unit}")

    row2("R_l = Γ_had/Γ_ll",        results["R_l"],           PDG["R_l"])
    row2("R_b = Γ_bb̄/Γ_had",       results["R_b"],           PDG["R_b"])
    row2("A_FB^lep",                 results["A_FB_lep"],      PDG["A_FB_lep"])
    row2("A_FB^b",                   results["A_FB_b"],        PDG["A_FB_b"])
    row2("sin²θ_eff^lep (tree)",     results["sin2_theta_eff"],PDG["sin2_theta_eff"])

    # N_nu from invisible width
    # Using DFC Γ(Z→νν̄) per generation from SM formula (tree-level prediction)
    g_v_nu, g_a_nu = couplings(+0.5, 0.0, sin2)
    gamma_nu_SM_formula = partial_width(+0.5, 0.0, 1, m_z, G_F, sin2)
    N_nu_DFC = results["Gamma_inv"] / gamma_nu_SM_formula   # = 3.0 by construction
    N_nu_obs = PDG["Gamma_inv"] / PDG["Gamma_nunu"]         # = 3.006 (data)
    print(f"\n--- Neutrino counting from invisible width ---")
    print(f"  DFC structural prediction: N_ν = 3  (3 generations, Tier 1 exact)")
    print(f"  Observed: Γ_inv/Γ_ν = {N_nu_obs:.4f}  (consistent with 3.000)")
    print(f"  DFC check: {N_nu_DFC:.6f} (confirms N_ν = 3 by construction)")

    # Summary table
    print(f"\n--- Summary ---")
    print(f"  All Z partial width predictions follow from the SAME coupling")
    print(f"  chain as M_W, M_Z, G_F, τ_μ (Tier 2a, Cycles 51–52).")
    print(f"  FREE PARAMETERS: β = {BETA} (coupling chain), v = {V_EW} GeV (VEV)")
    print(f"")
    print(f"  Error pattern: Γ_Z error ≈ 3× M_Z error (−0.36%×3 ≈ −1.1%)")
    print(f"    [width ∝ M_Z³ → fractional width error ≈ 3 × fractional M_Z error]")
    print(f"  QCD correction to hadrons: factor (1 + α_s/π) = {1 + alpha_s_mz/math.pi:.4f}")
    print(f"    [DFC α_s = {alpha_s_mz:.4f} vs SM {0.1182}; 11% off → Γ_had 0.35% extra error]")

    print(f"\n--- Consistency Checks ---")
    checks = [
        ("Γ(Z→e⁺e⁻)",         results["Gamma_ee"]*1000,  PDG["Gamma_ee"]*1000, "MeV"),
        ("Γ(Z→νν̄) per gen",   results["Gamma_nunu_each"]*1000, PDG["Gamma_nunu"]*1000, "MeV"),
        ("Γ_inv (3ν)",          results["Gamma_inv"]*1000, PDG["Gamma_inv"]*1000, "MeV"),
        ("Γ_had",               results["Gamma_had"]*1000, PDG["Gamma_had"]*1000, "MeV"),
        ("Γ_Z (total)",         results["Gamma_Z"]*1000,   PDG["Gamma_Z"]*1000,  "MeV"),
        ("R_l",                 results["R_l"],             PDG["R_l"],            ""),
        ("R_b",                 results["R_b"],             PDG["R_b"],            ""),
        ("A_FB^lep",            results["A_FB_lep"],        PDG["A_FB_lep"],       ""),
        ("A_FB^b",              results["A_FB_b"],          PDG["A_FB_b"],         ""),
        ("N_ν = 3",             3.0,                        N_nu_obs,              "(structural)"),
    ]
    print(f"  {'Check':<24} {'DFC':>12} {'Obs':>12} {'Err %':>8}  Status")
    print("  " + "-" * 70)
    for label, dfc, obs, unit in checks:
        err    = (dfc / obs - 1.0) * 100.0
        status = "✓" if abs(err) < 5.0 else "✗"
        print(f"  {label:<24} {dfc:>12.4f} {obs:>12.4f}  {err:>+7.2f}%  {status}  {unit}")

    print(f"\n  TIER: Γ_Z and partial widths = Tier 2a (all errors < ~2%)")
    print(f"        A_FB^b = Tier 2b (error +5.4% — loop corrections significant)")
    print(f"        N_ν = 3 = Tier 1 (exact structural prediction, no computation needed)")
    print(f"  Note: All errors trace to M_Z −0.36% (from β chain) and α_s 11% (Bottleneck 3).")
    print(f"        The M_Z error propagates as 3×(−0.36%) ≈ −1.1% into Γ_Z.")
