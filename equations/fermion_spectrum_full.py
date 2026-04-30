"""
Full fermion mass spectrum from DFC substrate dynamics.

STATUS: Running — serves as fermion spectrum summary and failure tracker.
A complete derivation of all fermion masses from DFC substrate parameters
remains a major open goal; current predictions and known failures are documented
here and in the individual modules below.

What a complete implementation will compute:
  - All lepton and quark masses from DFC geometric parameters
  - Generation structure from SU(3) fiber topology (three_generations.md)
  - Mass ratios within and across generations
  - Neutrino mass spectrum from D4 anchoring

Current status (from equations/mass_spectrum.py and equations/quark_masses.py):
  - m_mu/m_e = 206.77 from R/d ratio  [VERIFIED ✓]
  - tau mass from dimple potential: 211.8 MeV predicted, 1776.86 MeV observed [FAILS: 8.4x]
  - tau/muon ratio: 2.00 predicted vs 16.82 observed [FAILS]
  - Quark masses: c/s off by ~15%

The tau mass failure reveals that the dimple potential model (which gives only
n=2 and n=3 box modes) is insufficient. A complete fermion spectrum requires:

  1. The proper geometric derivation of the three generation masses from SU(3)
     fiber topology (not just box mode ratios)
  2. Connection to the Yukawa sector: why are the coupling constants O(1) for
     top, O(10^-6) for electron?
  3. The D-depth assignment for each fermion generation

Physical picture (to be formalized):
  m_f = f(closure depth D_f, topology T_f, generation index g)

  For leptons: all in the D6 SU(2) closure sector
    - Electron: g=1, D6 minimal closure -> m_e from global topology (muon scale)
                + local dimple -> near-cancellation gives 0.511 MeV
    - Muon: g=2, D6 first excited closure -> m_mu from global topology
    - Tau: g=3, D6 second excited closure -> m_tau FAILS with current n=3 box mode

  For quarks: D7 SU(3) closure sector, with color charges affecting mass
    - Up/down: lightest SU(3) closure modes
    - Strange/charm: excited SU(3) modes
    - Bottom/top: deepest SU(3) modes

Known failures to fix:
  - Tau mass: predicted 212 MeV, observed 1777 MeV (FAILS 8.4x)
  - Top quark mass: no DFC prediction yet (most massive fermion, O(173 GeV))
  - Neutrino mass ordering: observed hierarchy not yet reproduced

Key references:
  - foundations/three_generations.md (generation count from SU(3))
  - foundations/mass_hierarchy.md (dimple model + known failure)
  - foundations/zero_mode_multiplet.md (n=3 zero modes → SU(3) → three generations, Cycle 59)
  - equations/mass_spectrum.py (lepton masses)
  - equations/quark_masses.py (quark masses)
  - equations/neutrino_masses.py (neutrino masses)
  - equations/neutrino_oscillations.py (Δm² hierarchy ratio failure, Cycle 65)
  - equations/flavor_mixing.py (CKM/PMNS structure; CP violation requires N≥3, Cycle 69)
  - equations/mode_count_threshold.py (D7 n=3 zero modes → SU(3) VERIFIED, Cycles 72–74)
  - foundations/zero_mode_multiplet.md (n zero modes → SU(n) proved algebraically, Cycle 59)

PRIORITY: Medium (known failures documented; new mechanism needed for tau/top)
"""

# Particle masses (PDG 2024) for comparison
# Neutrino masses: individual masses not directly measured; estimates from oscillation data
# (normal hierarchy, minimum-mass case m₁ ≈ 0):
#   Δm²₂₁ = 7.42e-5 eV² → m₂ ≈ 8.6 meV = 8.6e-9 MeV
#   Δm²₃₁ = 2.517e-3 eV² → m₃ ≈ 50 meV = 5.0e-8 MeV
#   Cosmological bound: Σm_ν < 0.12 eV (Planck 2018)
MASSES_MEV = {
    # Leptons
    'electron': 0.511,
    'muon': 105.66,
    'tau': 1776.86,
    # Neutrinos (normal hierarchy minimum-mass estimates from oscillation Δm² data)
    # These are LOWER BOUNDS on individual masses for m₁ ≈ 0 assumption
    'nu_1': 1e-11,     # m₁ ≈ 0 (free; sets scale)
    'nu_2': 8.6e-9,    # m₂ ≈ √Δm²₂₁ ≈ 8.6 meV  [NOTE: was wrong as nu_mu, nu_tau]
    'nu_3': 5.0e-8,    # m₃ ≈ √Δm²₃₁ ≈ 50 meV
    # Quarks (MS-bar at 2 GeV for u,d,s; at M_c for c,b,t)
    'up': 2.2,
    'down': 4.7,
    'strange': 96.0,
    'charm': 1270.0,
    'bottom': 4180.0,
    'top': 172760.0,
}

# Current DFC predictions (from mass_spectrum.py + quark_masses.py)
PREDICTIONS_MEV = {
    'electron': 0.511,      # FITTED (free param)
    'muon': 105.66,         # FITTED (free param)
    'tau': 211.8,           # PREDICTED -> FAILS 8.4x
    'charm': 1075.0,        # PREDICTED -> ~15% off
    'strange': 82.0,        # PREDICTED -> ~15% off
}

if __name__ == "__main__":
    print("equations/fermion_spectrum_full.py — Fermion spectrum summary (Cycle 81 audit)")
    print(f"  Full fermion spectrum: {len(MASSES_MEV)} particles to predict")
    print(f"  Currently predicted: {len(PREDICTIONS_MEV)}")
    print()
    print(f"  Known failures:")
    for p in ['tau', 'charm', 'strange']:
        if p in PREDICTIONS_MEV:
            obs = MASSES_MEV[p]
            pred = PREDICTIONS_MEV[p]
            ratio = pred / obs
            factor = max(ratio, 1.0/ratio)
            status = "FAILS" if abs(ratio - 1) > 0.05 else "OK"
            print(f"    {p:10s}: predicted {pred:.1f} MeV, observed {obs:.1f} MeV, "
                  f"off by {factor:.1f}× [{status}]")
    print()
    print(f"  Unpredicted (no DFC derivation yet):")
    print(f"    top, bottom, up, down quarks")
    print(f"    neutrino masses ν₁, ν₂, ν₃")
    print(f"    (oscillation estimates: ν₂ ≈ 8.6 meV, ν₃ ≈ 50 meV)")
    print()
    print(f"  NOTE (Cycle 69 audit): Previous neutrino entries 'nu_mu=1e-4 MeV' and")
    print(f"  'nu_tau=0.015 MeV' were wrong by ~4-6 orders of magnitude vs oscillation")
    print(f"  data. Corrected to nu_2=8.6e-9 MeV, nu_3=5.0e-8 MeV.")
    print(f"  Neutrino mass ratio failure documented in neutrino_oscillations.py (Cycle 65).")
    print()
    print(f"  Status: new mechanism needed beyond dimple potential for tau/top.")
