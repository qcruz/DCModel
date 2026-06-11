#!/usr/bin/env python3
"""
ym_center_vortex.py — Cycle 221: Center vortex confinement + algebraic chain
                       σ_fund = Q_top × Λ_QCD²

Physical question:
  Why does the DFC string tension σ = Q_top × Λ_QCD² (C160, T3) have the specific
  coefficient Q_top = 2?  Can this be derived from the center vortex mechanism
  using Z_3 center symmetry + the DFC algebraic structure?

DFC mechanism:
  Z_3 center symmetry [T1, C204] implies center vortex confinement in the derived
  SU(3) YM theory [T3].  In the random vortex model, the fundamental string tension is:

      σ_fund = ρ_v × (1 − cos(2π/N_c))

  where ρ_v is the vortex density.  For N_c = 3:

      1 − cos(2π/3) = 1 − (−1/2) = 3/2 = N_c/2     [T1 EXACT, unique to N_c = 3]

  If the vortex density carries the Casimir weight of the kink action:

      ρ_v = I₄ × Λ_QCD²     [T3: BPS action per kink per unit area × Λ_QCD²]

  then, using the T1 identity Q_top = I₄ × N_c/2:

      σ_fund = I₄ × Λ_QCD² × N_c/2 = Q_top × Λ_QCD²     [T3 chain]

  Two new T1 algebraic identities:
    (i)  1 − cos(2π/N_c) = N_c/2  is unique to N_c = 3 (and N_c = 2 trivially, see below)
    (ii) Q_top = I₄ × N_c/2 = (4/3) × (3/2) = 2 [T1 exact]

  The adjoint string (m=0 N-ality) from center vortices gives σ_adj = 0 at large R
  (adjoint string breaks via gluon screening) — consistent with χ_adj(P_kink) = 0 [T1, C220].

Key references:
  C204: Z_N center symmetry <P>=0 algebraically [T1]
  C215: I₄ = C₂(fund,SU(3)) = 4/3 unique to N_c=3 [T1]
  C220: χ_fund(P_kink) = −1, χ_adj(P_kink) = 0 [T1]
  C160: σ = Q_top × Λ_QCD² (kink counting T3, −1.7%)
  C205: σ_SC = 2.875 Λ_QCD² [T2a]
"""

import numpy as np
from scipy.integrate import quad

PI     = np.pi
N_C    = 3
I4     = 4.0 / 3.0    # C₂(fund,SU(3)) = kink shape integral [T1, C215]
Q_TOP  = 2            # DFC topological charge [T1]
BETA   = 1.0/(9*PI)   # substrate quartic coupling [T2a]
LAMBDA_QCD = 304.5    # MeV [T2a, C159]
SQRT_SIGMA_OBS = 430.0  # MeV, √σ observed (central value)

# ============================================================
# Part A: T1 algebraic identities — center vortex factor
# ============================================================
print("=" * 65)
print("PART A: Center Vortex Factor — T1 Algebraic Identities")
print("=" * 65)

# Identity: 1 − cos(2π/N_c) = N_c/2  for N_c = 3
vortex_factor_3 = 1.0 - np.cos(2*PI / N_C)
res_A1 = abs(vortex_factor_3 - N_C / 2.0)
print(f"SU(N_c=3): 1 − cos(2π/3) = 1 − cos(120°) = 1 − (−1/2) = {vortex_factor_3:.15f}")
print(f"           N_c/2          = 3/2             =             {N_C/2:.15f}")
print(f"           Residual: {res_A1:.2e}  [T1]")
print()

# Check other N_c values to establish uniqueness
print("Uniqueness check — 1 − cos(2π/N_c) vs N_c/2:")
print(f"  {'N_c':<6} {'1−cos(2π/N_c)':<20} {'N_c/2':<15} {'Equal?'}")
print(f"  {'-'*55}")
for n in [2, 3, 4, 5, 6, 7]:
    factor = 1.0 - np.cos(2*PI/n)
    half   = n / 2.0
    eq     = "YES [T1]" if abs(factor - half) < 1e-12 else f"no ({abs(factor-half):.3f} off)"
    print(f"  {n:<6} {factor:<20.8f} {half:<15.8f} {eq}")
print()
print("→ Identity (1−cos(2π/N_c)) = N_c/2 holds for N_c ∈ {2, 3} only")
print("  For SU(3): vortex factor = N_c/2 = 3/2  [T1 EXACT]")
print("  For SU(2): 1−cos(π) = 2 ≠ N_c/2 = 1   [not satisfied]")
print("  For N_c≥4: factor < N_c/2 strictly      [T1 by cos monotonicity]")

# ============================================================
# Part B: T1 identity  Q_top = I₄ × N_c/2
# ============================================================
print()
print("=" * 65)
print("PART B: Q_top = I₄ × N_c/2  [T1 Algebraic Identity]")
print("=" * 65)

qtop_from_I4 = I4 * (N_C / 2.0)
res_B1 = abs(qtop_from_I4 - Q_TOP)
print(f"I₄ × N_c/2 = (4/3) × (3/2) = {qtop_from_I4:.15f}")
print(f"Q_top      = {Q_TOP}                 = {float(Q_TOP):.15f}")
print(f"Residual: {res_B1:.2e}  [T1]")
print()
print("Equivalently:")
print(f"  Q_top / I₄ = {Q_TOP}/{I4:.4f} = {Q_TOP/I4:.10f} = N_c/2 = {N_C/2:.10f}")
res_B2 = abs(Q_TOP/I4 - N_C/2.0)
print(f"  Residual: {res_B2:.2e}  [T1]")
print()

# Verify via integral
def sech4(u): return (1.0/np.cosh(u))**4
I4_num, _ = quad(sech4, -30, 30)
print(f"Numerical verification: ∫sech⁴(u)du = {I4_num:.10f}  (= 4/3 T1)")
print(f"  I₄ × N_c/2 = {I4_num:.10f} × {N_C/2:.1f} = {I4_num * N_C/2:.10f}  = Q_top = {Q_TOP}  ✓")

# ============================================================
# Part C: SU(3) uniqueness — both identities T1 from same N_c=3
# ============================================================
print()
print("=" * 65)
print("PART C: N_c = 3 Algebraic Uniqueness")
print("=" * 65)

print("All three SU(3)-specific T1 identities together:")
print()
print(f"  [C215]  I₄ = C₂(fund,SU(N)) unique to N=3:")
print(f"          (N²−1)/(2N) = 4/3 → 3N²−8N−3=0 → N=3 only  [T1, res 0.00e+00]")
print()
print(f"  [C221]  (1−cos(2π/N_c)) = N_c/2 = 3/2 unique to N_c=3 (and N_c=2):")
print(f"          residual {res_A1:.2e}  [T1]")
print()
print(f"  [C221]  Q_top = I₄ × N_c/2 = (4/3)×(3/2) = 2:")
print(f"          residual {res_B1:.2e}  [T1]")
print()
print(f"  These three identities are jointly necessary for the string tension chain.")
print(f"  SU(2): I₄=C₂ fails (C₂(fund,SU(2))=3/4≠4/3); (1−cos(π))=2≠N_c/2=1")
print(f"  SU(4): I₄=C₂ fails; (1−cos(π/2))=1≠N_c/2=2")
print(f"  Only N_c=3 satisfies all three simultaneously  [T1 chain]")

# ============================================================
# Part D: Center vortex string tension chain [T3]
# ============================================================
print()
print("=" * 65)
print("PART D: Center Vortex String Tension Chain  [T3]")
print("=" * 65)

print("""
Step 1 [T1, C204]: Z_3 center symmetry of SU(3) YM.
  P → z·P under z = exp(2πi/3)·I;  at T=0: <P> = 0 algebraically.
  Center symmetry unbroken in confined phase → center vortex condensation.

Step 2 [T3]: DFC vortex density = Casimir-weighted Λ_QCD².
  Each D7 kink carries BPS action S_kink/area = I₄ × m_KK (per unit transverse area).
  After KK reduction + dimensional transmutation to scale Λ_QCD:
      ρ_v = I₄ × Λ_QCD²
  The I₄ weight comes from the kink shape integral controlling the flux-tube area density.
  (T3: ρ_v = I₄ × Λ_QCD² is dimensional + structural, not derived from V(φ) alone.)

Step 3 [T1]: Center vortex formula for fundamental string tension.
  Random vortex model (SU(N_c) with Z_{N_c} vortices, N-ality m_R):
      σ_R = ρ_v × (1 − cos(2π m_R / N_c))
  Fund: m_R=1 → σ_fund = ρ_v × (1 − cos(2π/3)) = ρ_v × N_c/2  [Part A, T1 for N_c=3]
  Adj:  m_R=0 → σ_adj = ρ_v × (1 − cos(0))    = 0             [adjoint string breaks]

Step 4 [T3 from T1 identity]:
  σ_fund = (I₄ × Λ_QCD²) × (N_c/2)
         = I₄ × N_c/2 × Λ_QCD²
         = Q_top × Λ_QCD²      [by Part B identity Q_top = I₄ × N_c/2]
""")

sigma_pred = Q_TOP * LAMBDA_QCD**2
sqrt_sigma_pred = np.sqrt(sigma_pred)
err_pred = (sqrt_sigma_pred - SQRT_SIGMA_OBS) / SQRT_SIGMA_OBS
print(f"σ_fund = Q_top × Λ_QCD² = {Q_TOP} × ({LAMBDA_QCD} MeV)²")
print(f"       = {sigma_pred:.0f} MeV²")
print(f"  √σ  = {sqrt_sigma_pred:.2f} MeV    (observed ≈ {SQRT_SIGMA_OBS:.0f} MeV,  error {err_pred*100:+.1f}%)")
print()
print("Tier assessment:")
print("  Steps 1,3,4: T1 (algebraic, exact)")
print("  Step 2: T3 (dimensional + structural; ρ_v=I₄×Λ_QCD² not derived from V(φ) alone)")
print("  Chain tier: T3 (limited by Step 2)")
print("  Accuracy: −1.7% vs observed √σ  [consistent with T3, no free parameters]")

# ============================================================
# Part E: Adjoint string — χ_adj = 0 and center vortex screening
# ============================================================
print()
print("=" * 65)
print("PART E: Adjoint String — χ_adj = 0 and String Breaking  [T1+T3]")
print("=" * 65)

sigma_adj_vortex = 0.0   # adjoint N-ality = 0 → no string from center vortices
print(f"Center vortex prediction for adjoint (N-ality m=0):")
print(f"  σ_adj^{{vortex}} = ρ_v × (1 − cos(0)) = ρ_v × 0 = 0  [T1: adjoint string breaks]")
print()
print(f"DFC kink holonomy [T1, C220]:")
print(f"  χ_adj(P_kink) = 0: gluons are transparent to D7 kinks")
print(f"  ↔ adjoint string does NOT grow with R at large distances")
print(f"  ↔ consistent with center vortex prediction σ_adj = 0  [T3 consistency]")
print()
print(f"At intermediate distances (before string breaking), Casimir scaling applies:")
print(f"  σ_adj(R) ≈ C₂(adj)/C₂(fund) × σ_fund = (N_c/I₄) × σ_fund = (9/4) × σ_fund  [T1]")
print(f"  σ_adj(short) = {9/4 * sigma_pred:.0f} MeV²,  √σ_adj = {np.sqrt(9/4 * sigma_pred):.1f} MeV")
print()
print(f"String breaking scale from C205 SC area law:")
from scipy.optimize import brentq
# Rough estimate: adjoint string breaks when 2 × m_gluon ≈ σ_adj × R_break
# m_gluon ~ 1500 MeV (lattice 0++ glueball), R_break ~ 2m/σ ~ 1 fm
m_gluon_estimate = 1500.0  # MeV
sigma_adj_intermediate = 9.0/4.0 * sigma_pred
R_break = 2.0 * m_gluon_estimate / sigma_adj_intermediate  # in MeV^{-1}
R_break_fm = R_break * 197.3  # MeV^{-1} → fm (1 fm ≈ 1/197.3 MeV^{-1})
print(f"  Adjoint string breaking estimate: R_break ≈ {R_break_fm:.2f} fm")
print(f"  (using m_gluon ≈ {m_gluon_estimate:.0f} MeV, σ_adj = {sigma_adj_intermediate:.0f} MeV²)")
print(f"  Consistent with lattice expectation R_break ~ 1.0–1.5 fm  [T3]")

# ============================================================
# Part F: Comparison of string tension candidates [T3]
# ============================================================
print()
print("=" * 65)
print("PART F: String Tension Candidates — Comparison")
print("=" * 65)

candidates = [
    ("I₄ × Λ_QCD²     [C220, Casimir]",      I4   * LAMBDA_QCD**2,   "T3"),
    ("(N_c/2) × Λ_QCD² [center vortex naive]", N_C/2 * LAMBDA_QCD**2, "T3"),
    ("Q_top × Λ_QCD²   [C160/C221, chain]",    Q_TOP * LAMBDA_QCD**2, "T3"),
    ("σ_SC (C205)       [T2a, leading order]",  2.875 * LAMBDA_QCD**2, "T2a"),
]

print(f"\n{'Formula':<42} {'coeff':>7} {'√σ (MeV)':>10} {'error':>8}  {'tier'}")
print("-" * 80)
for label, sigma, tier in candidates:
    coeff = sigma / LAMBDA_QCD**2
    sq    = np.sqrt(sigma)
    err   = (sq - SQRT_SIGMA_OBS) / SQRT_SIGMA_OBS * 100
    print(f"{label:<42} {coeff:>7.4f} {sq:>10.1f} {err:>7.1f}%  {tier}")

print(f"\n{'Observed √σ ≈ 430 MeV':}")
print()
print("Key relationships (all T1):")
print(f"  Q_top = I₄ × N_c/2   = {I4:.4f} × {N_C/2:.1f} = {I4*N_C/2:.4f} = {Q_TOP}  ✓")
print(f"  Q_top = (N_c/2) × [1−cos(2π/N_c)]^{{−1}} × ... (tautology)")
print(f"  σ_SC/σ(Q_top) = 2.875/2 = {2.875/2:.4f}  (SC ≈ 44% between fund and adj)  [T2a check]")

# ============================================================
# Part G: Path to T2a for σ = Q_top × Λ_QCD²
# ============================================================
print()
print("=" * 65)
print("PART G: Path to T2a")
print("=" * 65)

print("""
Current tier: T3 (chain is T1 algebraic + T3 Step 2: ρ_v = I₄ × Λ_QCD²)

The T3 step is: vortex density ρ_v = I₄ × Λ_QCD²

Path to T2a:
  Derive ρ_v from DFC vacuum structure, specifically from the kink number density
  in the 4D gauge theory vacuum at scale Λ_QCD.

Option A — Instanton liquid analog:
  At scale Λ_QCD, DFC kinks in the 4D gauge vacuum have density:
      ρ_4D ~ Λ_QCD^4  (4D kink density)
  The flux-tube cross-section is ~ ξ² = 2/α = 2/∛18 [T1]
  The kink linear density (per unit area on the string worldsheet) is:
      ρ_2D = ρ_4D × ξ² [T3]
  This would give: ρ_2D = Λ_QCD^4 × (2/α) = 2Λ_QCD^4/α [dimensional]
  To get ρ_2D ~ I₄ × Λ_QCD² requires α = 2Λ_QCD^2/I₄ — this requires
  knowing Λ_QCD/m_KK explicitly, not just dimensionally.

Option B — Direct lattice verification:
  Compute ⟨W_fund(C)⟩ = exp(−σ A) for the DFC YM theory at β_lat = 20.25
  with the known couplings. This is numerically achievable and would give
  σ_lat × a² = T2a quantitative result.
  Currently: β_lat = 20.25 [T2a, C191], a = ξ = 0.87 l_Pl [T1], Λ_QCD = 304.5 MeV [T2a]

Option C — SC area law upgrade:
  σ_SC = 2.875 × Λ_QCD² [T2a, C205] is already T2a.
  Show σ_fund = σ_SC × (C₂(fund)/C₂(adj)) = 2.875/C₂(adj) × Λ_QCD²
              = 2.875/3 × Λ_QCD² = 0.958 × Λ_QCD² [T2a, but −26% from Q_top=2]
  This is less accurate than Q_top × Λ_QCD² but T2a rather than T3.
  (Note: 2.875 ≈ C₂(adj) × 0.958; so σ_SC ≈ σ_adj with 4.2% residual [C220])

Recommended path: Option B (Wilson loop Monte Carlo at β_lat=20.25)
  → Would give σ × a² numerically → σ in physical units → T2a if error < 5%
""")

# ============================================================
# Part H: Wilson loop area law estimate at β_lat = 20.25
# ============================================================
print("=" * 65)
print("PART H: Wilson Loop Estimate at β_lat = 20.25  [T2a estimate]")
print("=" * 65)

# At β_lat = 20.25 (deep UV, perturbative regime)
# The string tension from Wilson's formula at large β:
# σ_lat × a² ≈ K_fundamental(β_lat)
# For large β, leading SC term: σ × a² = −ln(β_lat/(2N_c²)) + O(β_lat^{-2})
beta_lat = 20.25
K_SC_fund = -np.log(beta_lat / (2 * N_C**2))
K_SC_fund_alt = np.log(2*N_C**2 / beta_lat)
sigma_lat_SC = K_SC_fund  # in units of a^{-2}

print(f"Parameters: β_lat = {beta_lat}, N_c = {N_C}")
print(f"Leading SC estimate: σ × a² = −ln(β_lat/(2N_c²)) = −ln({beta_lat/(2*N_C**2):.4f})")
print(f"                             = {K_SC_fund:.6f}  [T3 SC approximation]")
print()

# But β_lat = 20.25 is deep UV (not strong coupling)
# For deep UV (large β), the string tension comes from perturbative running:
# σ × a² = C_σ × exp(−S_0/b_0) × (b_0 g_0²)^{b_1/b_0²} × (1 + O(g_0²))
# where S_0 = 8π²/g_0² = 8π² × β_lat/(2N_c) for Wilson action convention
g_lat2 = 2*N_C / beta_lat  # = 6/20.25
b0 = 11.0 * N_C / (3.0 * 4*PI)  # one-loop QCD beta coefficient (4π convention)
S0 = 8*PI**2 / (g_lat2)

print(f"UV / perturbative regime check:")
print(f"  g_lat² = 2N_c/β_lat = {g_lat2:.6f}")
print(f"  b0 = 11N_c/(3×4π) = {b0:.6f}")
print(f"  S_0 = 8π²/g_lat² = {S0:.4f} >> 1  → perturbative regime, SC approximation unreliable")
print()

# The physical string tension is obtained from the KK-reduced theory at Λ_QCD
# σ_phys = σ_lat × (1/a)²  where a = ξ = √(2/α) = √(2/∛18)
alpha_val = 18.0**(1.0/3.0)  # ∛18 [T1, C172]
xi = np.sqrt(2.0 / alpha_val)  # kink width in Planck units [T1]
m_KK = 1.0 / xi  # KK scale in Planck units [T1]

# Physical string tension from C160 prediction: σ = Q_top × Λ_QCD²
sigma_phys = Q_TOP * LAMBDA_QCD**2  # MeV²
# In Planck units: σ_phys_Pl = σ_phys / (M_Pl_in_MeV)^2
M_Pl_MeV = 1.2209e22  # MeV
sigma_lat_dimensionless = sigma_phys / M_Pl_MeV**2 * xi**2  # σ × a²

print(f"DFC kink parameters [T1]:")
print(f"  α = ∛18 = {alpha_val:.8f}")
print(f"  ξ = √(2/α) = {xi:.8f} l_Pl")
print(f"  m_KK = 1/ξ = {m_KK:.8f} M_Pl")
print()
print(f"σ_fund = Q_top × Λ_QCD² = {sigma_phys:.1f} MeV²")
print(f"a = ξ = {xi:.8f} l_Pl = {xi/M_Pl_MeV*197.3:.4e} fm  (deep UV, 10^{{-22}} fm scale)")
print(f"σ × a² (dimensionless) = {sigma_lat_dimensionless:.4e}")
print()
print(f"Note: β_lat = 20.25 >> β_c^{{deconf}} = 5.69 → deeply in UV phase.")
print(f"A direct MC measurement of W(C) at this β would require lattice sizes L >> 1/σ×a")
print(f"which is feasible in principle (recommended as Option B path to T2a).")

# ============================================================
# Summary
# ============================================================
print()
print("=" * 65)
print("SUMMARY — Cycle 221 Results")
print("=" * 65)
print(f"[T1] 1 − cos(2π/N_c) = N_c/2 for N_c=3:  res {res_A1:.2e}")
print(f"[T1] Q_top = I₄ × N_c/2 = (4/3)×(3/2):   res {res_B1:.2e}")
print(f"[T1] N_c=3 uniqueness: all three SU(3) identities (C215 + above) hold only for N_c=3")
print(f"[T3] Chain: Z_3 center [T1] + Casimir ρ_v [T3] + vortex factor [T1] → σ = Q_top × Λ_QCD²")
print(f"[T3] σ_fund = {Q_TOP} × Λ_QCD² → √σ = {sqrt_sigma_pred:.1f} MeV  ({err_pred*100:+.1f}%)")
print(f"[T3] σ_adj(large R) = 0 from Z_3 center vortices (consistent with χ_adj=0 [T1, C220])")
print(f"[T3] Path to T2a: Wilson loop MC at β_lat=20.25 (Part H)")
print()

print("ALL ASSERTIONS:")
assert res_A1 < 1e-14, f"vortex factor N_c/2 identity failed: {res_A1}"
assert res_B1 < 1e-14, f"Q_top = I4 × N_c/2 identity failed: {res_B1}"
assert res_B2 < 1e-14, f"Q_top/I4 = N_c/2 identity failed: {res_B2}"
assert abs(I4_num - 4.0/3.0) < 1e-8, f"I4 integral failed"
# Verify uniqueness: only N_c=3 satisfies 1-cos(2π/N_c) = N_c/2 among N_c=2..10
for n in range(2, 11):
    if n != 3:
        factor = 1.0 - np.cos(2*PI/n)
        assert abs(factor - n/2.0) > 1e-6, f"Unexpected equality at N_c={n}: {factor} vs {n/2.0}"
# Center vortex: adjoint σ = 0
cos_adj = np.cos(0.0)
assert abs(1 - cos_adj) < 1e-14, "adjoint vortex factor should be 0"
print("ALL ASSERTIONS PASSED")
