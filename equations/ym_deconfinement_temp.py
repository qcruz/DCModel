"""
equations/ym_deconfinement_temp.py

SP2/SP3: Deconfinement temperature from DFC string tension.

Physical question: What does DFC predict for the pure-YM deconfinement
temperature T_c? Does the result support the confinement/mass-gap chain?

DFC input: sigma_phys = Q_top * Lambda_QCD^2 = 185440 MeV^2 [T2a, C222]
           sqrt(sigma) = 430.6 MeV

Method: Apply the well-established lattice ratio T_c / sqrt(sigma) from
pure SU(3) YM (quenched). This ratio is scheme-independent and has been
measured precisely by multiple groups.

  T_c / sqrt(sigma) = 0.6295 +/- 0.0075  (Boyd et al 1996, SU(3))

DFC predicts: T_c = 0.6295 * sqrt(Q_top) * Lambda_QCD

Physical interpretation: T_c is the temperature at which the Z_3 center
symmetry is spontaneously broken and the Polyakov loop <P> acquires a
nonzero expectation value. The DFC prediction [T1, C204]: <P>=0 at T=0
for all beta by center symmetry; T_c marks the boundary.

Key results (Cycle 227):
  Part A [T2a]: sqrt(sigma) = 430.6 MeV from C222
  Part B [T1]:  T_c/sqrt(sigma) ratio is universal (lattice input)
  Part C [T3]:  T_c^DFC = 271 MeV  (+0.4% vs lattice 270 MeV)
  Part D [T2a]: T_c > 0 — deconfinement exists; <P>=0 phase has finite T range
  Part E [T3]:  T_c/Lambda_QCD = 0.89 (dimensionless DFC prediction)

References:
  C222: sigma = Q_top * Lambda_QCD^2 = 185440 MeV^2 [T2a]
  C204: <P>=0 at T=0 algebraically [T1]
  Boyd et al 1996: T_c/sqrt(sigma) = 0.6295+-0.0075, SU(3) pure gauge
  Datta-Gupta 2010: T_c = 270+-3 MeV (SU(3) pure YM lattice)

Cycle 227
"""

import numpy as np

print("=" * 60)
print("SP2/SP3: Deconfinement Temperature — Cycle 227")
print("=" * 60)

# -----------------------------------------------------------------------
# DFC parameters
# -----------------------------------------------------------------------
Q_TOP      = 2.0        # [T1 exact]
LAMBDA_QCD = 304.5      # MeV [T2a, C159]

# -----------------------------------------------------------------------
# Part A: String tension input [T2a, C222]
# -----------------------------------------------------------------------
print("\nPart A: String tension [T2a, C222]")
sigma_phys = Q_TOP * LAMBDA_QCD**2   # MeV^2
sqrt_sigma  = np.sqrt(sigma_phys)    # MeV

print(f"  sigma = Q_top * Lambda^2 = {sigma_phys:.0f} MeV^2  [T2a]")
print(f"  sqrt(sigma) = {sqrt_sigma:.2f} MeV")

assert abs(sigma_phys - 185440) < 10
assert abs(sqrt_sigma - 430.6) < 1.0

# -----------------------------------------------------------------------
# Part B: Lattice calibration ratio [T1 universal]
# -----------------------------------------------------------------------
print("\nPart B: Lattice calibration ratio [Boyd et al 1996, T1]")
# Pure SU(3) YM (quenched), Boyd et al 1996, Nucl. Phys. B469:419-444
Tc_ratio       = 0.6295    # T_c / sqrt(sigma)
Tc_ratio_err   = 0.0075    # uncertainty

print(f"  T_c / sqrt(sigma) = {Tc_ratio} +/- {Tc_ratio_err}  (SU(3) lattice)")
print(f"  This ratio is universal for pure SU(3) YM (scheme-independent)")

# -----------------------------------------------------------------------
# Part C: DFC prediction for T_c [T3]
# -----------------------------------------------------------------------
print("\nPart C: Deconfinement temperature prediction [T3]")
Tc_DFC   = Tc_ratio * sqrt_sigma    # MeV

# Observed (pure SU(3) YM, quenched lattice, Datta-Gupta 2010)
Tc_obs   = 270.0    # MeV  (+/- 3 MeV)
Tc_obs_err = 3.0

err_Tc   = (Tc_DFC - Tc_obs) / Tc_obs * 100.0

print(f"  T_c^DFC = {Tc_ratio} * {sqrt_sigma:.2f} = {Tc_DFC:.1f} MeV  [T3]")
print(f"  T_c^obs = {Tc_obs:.0f} +/- {Tc_obs_err:.0f} MeV  (pure YM lattice)")
print(f"  Error: {err_Tc:+.1f}%")
print(f"  Within 1-sigma: {abs(Tc_DFC - Tc_obs) < Tc_obs_err}")

# Upper / lower bound using ratio uncertainty
Tc_hi = (Tc_ratio + Tc_ratio_err) * sqrt_sigma
Tc_lo = (Tc_ratio - Tc_ratio_err) * sqrt_sigma
print(f"  DFC range from ratio uncertainty: [{Tc_lo:.1f}, {Tc_hi:.1f}] MeV")

assert Tc_DFC > 0,                          "T_c positive"
assert abs(err_Tc) < 5.0,                   "T_c within 5% of lattice"
assert Tc_lo < Tc_obs < Tc_hi + 10,        "obs within DFC range (generous)"

# -----------------------------------------------------------------------
# Part D: Phase structure — <P>=0 for T < T_c [T2a]
# -----------------------------------------------------------------------
print("\nPart D: Phase structure [T2a + T1]")
print(f"  T=0: <P>=0 algebraically [T1, C204 center symmetry]")
print(f"  T<T_c: confined phase  (<P>=0, area law, gap > 0)")
print(f"  T>T_c: deconfined phase (<P>!=0, Polyakov loop condenses)")
print(f"  T_c = {Tc_DFC:.1f} MeV — finite, nonzero [T2a: sigma>0 => T_c>0]")
print(f"  Confinement has a finite temperature range: (0, {Tc_DFC:.0f} MeV)")

assert Tc_DFC > LAMBDA_QCD * 0.5,   "T_c above Lambda/2 (physical)"
assert Tc_DFC < LAMBDA_QCD * 5.0,   "T_c below 5*Lambda (physical)"

# -----------------------------------------------------------------------
# Part E: Dimensionless ratio T_c / Lambda_QCD [T3]
# -----------------------------------------------------------------------
print("\nPart E: Dimensionless ratio [T3]")
ratio_TcLambda = Tc_DFC / LAMBDA_QCD

print(f"  T_c / Lambda_QCD = {Tc_DFC:.1f} / {LAMBDA_QCD:.1f} = {ratio_TcLambda:.3f}  [T3]")
print(f"  Pure DFC result: T_c = {ratio_TcLambda:.3f} * Lambda_QCD")
print(f"  = {Tc_ratio:.4f} * sqrt(Q_top) * Lambda_QCD")
print(f"  = {Tc_ratio:.4f} * {np.sqrt(Q_TOP):.4f} * {LAMBDA_QCD:.1f} MeV")

assert 0.5 < ratio_TcLambda < 2.0,  "ratio T_c/Lambda sensible"

# -----------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------
print(f"\n{'='*60}")
print("Summary: Deconfinement Temperature (Cycle 227)")
print(f"{'='*60}")
print(f"  Input:   sigma = Q_top*Lambda^2 = {sigma_phys:.0f} MeV^2  [T2a, C222]")
print(f"           sqrt(sigma) = {sqrt_sigma:.1f} MeV")
print(f"  [T3] T_c = {Tc_DFC:.1f} MeV  ({err_Tc:+.1f}% vs pure YM lattice 270 MeV)")
print(f"  [T2a] T_c > 0 — confinement exists in finite T range (0, {Tc_DFC:.0f} MeV)")
print(f"  [T3] T_c / Lambda_QCD = {ratio_TcLambda:.3f}  (dimensionless DFC prediction)")
print(f"  [T1] <P>=0 at T=0 by Z_3 center symmetry [C204]")
print(f"\n  ALL ASSERTIONS PASSED")
print(f"\n  Tier: T3 (uses lattice calibration ratio T_c/sqrt(sigma))")
print(f"  Supports: SP2/SP3 — confinement + gap in T>0 phase structure")
print(f"  Path to T2a: derive T_c/sqrt(sigma) from DFC domain wall dynamics")
print("=" * 60)
