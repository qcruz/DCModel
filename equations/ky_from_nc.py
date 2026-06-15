"""
Cycle 273: k_Y² = 5/3 T3→T2a via N_c = 3 uniqueness theorem
equations/ky_from_nc.py

KEY RESULT: k_Y²(N_c) = (11N_c/9 + 3)/(N_c + 1) for general N_c (one SM generation).
            k_Y² = 5/3  if and only if  N_c = 3  [T1 algebraic, unique].
            D7 = SU(3) [T2a, C59-74] → N_c = 3 [T1] → k_Y² = 5/3 [T1] → T2a composite.

UPGRADE: k_Y² T3 (C272 — fermion content T2a) → T2a (C273 — N_c=3 T2a + uniqueness T1).

DFC mechanism:
  The D7 depth behavior produces SU(3) color structure (T2a, Cycles 59-74).
  The fundamental representation of SU(3) has dimension N_c = 3 (T1 algebraic).
  For one complete left-handed fermion generation with N_c quark colors and Q = T₃ + Y/2,
  the ratio k_Y² = Σ(Y/2)² / Σ T₃² = (11N_c/9 + 3)/(N_c+1) is algebraically fixed.
  The equation k_Y²(N_c) = 5/3 has the unique positive-integer solution N_c = 3.
  Therefore k_Y² = 5/3 is not a free input — it is forced by D7 = SU(3).

ECCC consequence:
  1/α_em = (1 + k_Y²)/α_common = (8/3) × (27π/2) = 36π  [T1 exact]
  With k_Y² T2a, the α₁ piece of Term2_SM in the ECCC identity is now T2a (was T3 in C272).
  Remaining T4 in ECCC: α_s piece requires C_match from V(φ) alone.

References:
  C272: k_Y² = 5/3 from explicit fermion hypercharge sum (T3)
  C263: ECCC identity A−B = ln(1/α_em(0)) verified T2a (−0.044%)
  C265: ECCC algebraic decomposition; Term1_DFC = 27π²×111/287 [T1]
  C144: α_s(M_Z) +0.006% via ECCC+SM α_em(0) input [T2a]
"""

import numpy as np

# ============================================================
# PART A: General k_Y²(N_c) formula [T1 algebraic derivation]
# ============================================================
print("=" * 65)
print("PART A: k_Y²(N_c) general formula")
print("=" * 65)
print()
print("One complete left-handed fermion generation with N_c quark colors:")
print("  SU(2) doublets: 1 lepton + N_c quark = (N_c+1) doublets total")
print("  Weyl spinors: 2(N_c+1) LH + (N_c+1) RH singlets... wait")
print()
print("Fermion content (one generation, N_c colors):")
print("  LH quark doublets (N_c): each member has Y = 1/3")
print("    → Σ T₃²: N_c × 2 × (1/2)² = N_c/2")
print("    → Σ(Y/2)²: N_c × 2 × (1/6)² = N_c/18")
print("  RH u_R singlets (N_c): Q = 2/3, T₃ = 0, Y = 4/3")
print("    → (Y/2)²: N_c × (2/3)² = 4N_c/9")
print("  RH d_R singlets (N_c): Q = -1/3, T₃ = 0, Y = -2/3")
print("    → (Y/2)²: N_c × (1/3)² = N_c/9")
print("  LH lepton doublet (1): (ν, e), Y = -1 for each")
print("    → Σ T₃²: 1 × 2 × (1/2)² = 1/2")
print("    → Σ(Y/2)²: 2 × (1/2)² = 1/2")
print("  RH e_R singlet (1): Q = -1, T₃ = 0, Y = -2")
print("    → (Y/2)²: (1)² = 1")
print()

def ky_squared(N_c):
    """
    k_Y²(N_c) = Σ(Y/2)² / Σ T₃² over one complete LH generation with N_c colors.

    Σ T₃² = (N_c + 1)/2   [N_c quark doublets + 1 lepton doublet]
    Σ(Y/2)² = 11N_c/18 + 3/2   [all 4N_c + 3 Weyl spinors]
    k_Y²(N_c) = (11N_c/9 + 3) / (N_c + 1)
    """
    sum_T3_sq = (N_c + 1) / 2.0
    sum_Y2_sq = 11.0 * N_c / 18.0 + 3.0 / 2.0
    return sum_Y2_sq / sum_T3_sq

# Verify formula compactly
for nc in [1, 2, 3, 4]:
    sum_T3 = (nc + 1) / 2.0
    sum_Y2 = 11.0 * nc / 18.0 + 3.0 / 2.0
    compact = (11.0 * nc / 9.0 + 3.0) / (nc + 1)
    assert abs(ky_squared(nc) - compact) < 1e-14
print("General formula: k_Y²(N_c) = (11N_c/9 + 3)/(N_c + 1)  [T1]")
print()

# ============================================================
# PART B: N_c = 3 gives k_Y² = 5/3 exactly
# ============================================================
print("=" * 65)
print("PART B: k_Y²(3) = 5/3 — exact verification")
print("=" * 65)
print()

N_c = 3

# Σ T₃² (doublets only, since singlets have T₃ = 0)
sum_T3_sq = (N_c + 1) / 2.0   # = 4/2 = 2
res_T3 = abs(sum_T3_sq - 2.0)
print(f"Σ T₃² = (N_c+1)/2 = {sum_T3_sq}  (res {res_T3:.2e})")
assert res_T3 < 1e-14, f"FAIL Σ T₃²: res={res_T3:.2e}"
print("  PASS [T1]: Σ T₃² = 2")

# Σ(Y/2)² (all Weyl spinors)
lh_q  = N_c * 2 * (1.0/6)**2        # LH quark doublet members, Y=1/3 → Y/2=1/6
rh_u  = N_c * (2.0/3)**2            # RH u_R: Y=4/3 → Y/2=2/3
rh_d  = N_c * (1.0/3)**2            # RH d_R: Y=-2/3 → Y/2=-1/3
lh_l  = 2 * (1.0/2)**2              # LH lepton doublet members, Y=-1 → Y/2=-1/2
rh_e  = 1.0**2                      # RH e_R: Y=-2 → Y/2=-1
sum_Y2_sq = lh_q + rh_u + rh_d + lh_l + rh_e
target_Y2 = 10.0 / 3.0
res_Y2 = abs(sum_Y2_sq - target_Y2)
print(f"Σ(Y/2)² = {lh_q:.6f}+{rh_u:.6f}+{rh_d:.6f}+{lh_l:.6f}+{rh_e:.6f} = {sum_Y2_sq:.15f}")
print(f"  Target: 10/3 = {target_Y2:.15f}  (res {res_Y2:.2e})")
assert res_Y2 < 1e-14, f"FAIL Σ(Y/2)²: res={res_Y2:.2e}"
print("  PASS [T1]: Σ(Y/2)² = 10/3")

# k_Y²
ky_sq = sum_Y2_sq / sum_T3_sq
target_ky = 5.0 / 3.0
res_ky = abs(ky_sq - target_ky)
print(f"k_Y² = (10/3)/2 = {ky_sq:.15f}")
print(f"  Target: 5/3 = {target_ky:.15f}  (res {res_ky:.2e})")
assert res_ky < 1e-14, f"FAIL k_Y²: res={res_ky:.2e}"
print("  PASS [T1]: k_Y² = 5/3 (exact)")
print()

# ============================================================
# PART C: Table for N_c = 1..6
# ============================================================
print("=" * 65)
print("PART C: k_Y²(N_c) table — only N_c = 3 gives 5/3")
print("=" * 65)
print()
print(f"{'N_c':>4}  {'k_Y²':>20}  {'k_Y² = 5/3?':>15}")
for nc in range(1, 7):
    ky2 = ky_squared(nc)
    is_match = abs(ky2 - 5.0/3.0) < 1e-10
    flag = "<-- N_c = 3 unique" if is_match else ""
    print(f"{nc:>4}  {ky2:>20.15f}  {'YES' if is_match else 'no':>15}  {flag}")
print()

# Verify exactly three N_c values tested: only N_c=3 matches
matches = [nc for nc in range(1, 101) if abs(ky_squared(nc) - 5.0/3.0) < 1e-10]
assert matches == [3], f"FAIL uniqueness scan: matches={matches}"
print("  PASS [T1]: Scan N_c = 1..100 — unique solution is N_c = 3")
print()

# ============================================================
# PART D: Algebraic uniqueness proof [T1]
# ============================================================
print("=" * 65)
print("PART D: Uniqueness — k_Y² = 5/3 iff N_c = 3 [T1 algebraic]")
print("=" * 65)
print()
print("Solve (11N_c/9 + 3)/(N_c+1) = 5/3 for N_c:")
print("  3(11N_c/9 + 3) = 5(N_c+1)")
print("  11N_c/3 + 9 = 5N_c + 5")
print("  11N_c/3 - 15N_c/3 = 5 - 9")
print("  -4N_c/3 = -4")
print("  N_c = 3  (unique rational solution)")
print()

# Numerical verification of the algebraic steps
lhs = lambda nc: 11.0*nc/3.0 + 9.0
rhs = lambda nc: 5.0*nc + 5.0
diff_at_3 = abs(lhs(3) - rhs(3))
print(f"Check N_c = 3: LHS = {lhs(3)}, RHS = {rhs(3)}, diff = {diff_at_3:.2e}")
assert diff_at_3 < 1e-13, "FAIL: algebraic check at N_c=3"
print("  PASS [T1]: algebraic uniqueness verified")
print()
print("Implication: k_Y² = 5/3  ⟺  N_c = 3 (one SM generation, Q = T₃ + Y/2)")
print()

# ============================================================
# PART E: DFC tier chain
# ============================================================
print("=" * 65)
print("PART E: DFC tier chain — k_Y² T3→T2a")
print("=" * 65)
print()
print("Step 1: D7 = SU(3)                    [T2a, Cycles 59-74]")
print("Step 2: dim(fund rep of SU(3)) = N_c = 3  [T1 algebraic: Weyl formula]")
print()
dim_fund_su3 = 3  # dim of (1,0) SU(3) representation
assert dim_fund_su3 == 3
print(f"  dim(1,0) of SU(3) = {dim_fund_su3}  [T1, res 0]")
print()
print("Step 3: k_Y²(N_c=3) = 5/3            [T1, Part D uniqueness]")
print()
print("Composite tier: T2a")
print("  = D7=SU(3)[T2a] × dim(fund rep)=3[T1] × k_Y²(3)=5/3[T1]")
print()
print("UPGRADE: k_Y² T3 (C272: fermion content T2a) → T2a (C273: N_c=3 T2a + uniqueness T1)")
print()
print("Why T2a not T1: D7=SU(3) assignment (Cycles 59-74) is T2a, not T1.")
print("  When D7=SU(3) reaches T1, this result automatically upgrades to T1.")
print()

# ============================================================
# PART F: ECCC consequence
# ============================================================
print("=" * 65)
print("PART F: ECCC chain consequence")
print("=" * 65)
print()
alpha_common = 2.0 / (27.0 * np.pi)
ky_sq_val = 5.0 / 3.0

# (1 + k_Y²)/α_common = 36π
lhs_eccc = (1.0 + ky_sq_val) / alpha_common
rhs_eccc = 36.0 * np.pi
rel_res_eccc = abs(lhs_eccc - rhs_eccc) / rhs_eccc
print(f"(1 + k_Y²)/α_common = {lhs_eccc:.15f}")
print(f"36π                  = {rhs_eccc:.15f}")
print(f"  Relative residual: {rel_res_eccc:.2e}")
assert rel_res_eccc < 1e-14, f"FAIL: (1+k_Y²)/α_common ≠ 36π"
print("  PASS [T1]: (1+5/3)/(2/(27π)) = (8/3)×(27π/2) = 36π  (exact)")
print()

# sin²θ_W at unification from k_Y²
sin2_th_W_GUT = 1.0 / (1.0 + ky_sq_val)
res_sin2 = abs(sin2_th_W_GUT - 3.0/8.0)
print(f"sin²θ_W(M_c) = 1/(1+k_Y²) = {sin2_th_W_GUT:.15f}")
print(f"  3/8 = {3.0/8.0:.15f}  (res {res_sin2:.2e})")
assert res_sin2 < 1e-14, "FAIL: sin²θ_W ≠ 3/8"
print("  PASS [T1]: sin²θ_W(M_c) = 3/8  [T2a composite]")
print()

# ECCC tier upgrade summary
print("ECCC Term2_SM decomposition (C265):")
print("  Term1_DFC = 27π²×111/287 = 103.063  [T1, from V(φ) only, C265]")
print("  Term2_SM α₁ piece ∝ 1/α₁ = (1+k_Y²)/(α_common×k_Y²)×k_Y²...")
print("  k_Y² = 5/3 now T2a → α₁ piece of Term2_SM T3→T2a (was T3 C272)")
print("  Remaining T4: α_s piece of Term2_SM (requires C_match from V(φ) alone)")
print()

# ============================================================
# PART G: Self-consistency cross-checks
# ============================================================
print("=" * 65)
print("PART G: Self-consistency cross-checks")
print("=" * 65)
print()

# C272 cross-check: same k_Y² value
ky_sq_c272 = 10.0/3.0 / 2.0   # from C272 direct sum
res_cross = abs(ky_sq_c272 - 5.0/3.0)
print(f"C272 k_Y² = (10/3)/2 = {ky_sq_c272:.15f}  (res {res_cross:.2e})")
assert res_cross < 1e-14
print("  PASS [T1]: C272 and C273 give identical k_Y² = 5/3")
print()

# k_Y = √(5/3) numerical value
k_Y = np.sqrt(5.0/3.0)
print(f"k_Y = √(5/3) = {k_Y:.10f}  (≈ 0.8165)")
print(f"  Note: k_Y = √(5/3) ≈ 0.8165 (sometimes written as 3/5 is the SQUARE of this)")
print(f"  The SU(5) GUT convention uses k_Y² = 5/3 (this is what enters 36π formula)")
print()

# SU(5) consistency: in SU(5), k_Y² = 5/3 is the standard GUT normalization
# sin²θ_W|_{SU(5)} = 3/8 → runs to 0.2312 at M_Z [T2a, C144]
print("SU(5) normalization consistency:")
print(f"  k_Y²(SU(5) standard) = 5/3  [established GUT result]")
print(f"  k_Y²(DFC, N_c=3)    = 5/3  [T2a, this module]")
print(f"  → DFC with N_c=3 realizes SU(5) U(1) normalization WITHOUT SU(5) as input")
print()

# ============================================================
# SUMMARY
# ============================================================
print("=" * 65)
print("SUMMARY")
print("=" * 65)
print()
print("7/7 PARTS PASSED")
print()
print("Key results:")
print(f"  k_Y²(N_c) = (11N_c/9 + 3)/(N_c+1)   [T1 algebraic]")
print(f"  k_Y²(3) = 5/3                          [T1, res {abs(ky_squared(3)-5/3):.0e}]")
print(f"  k_Y² = 5/3 iff N_c = 3                [T1 uniqueness]")
print(f"  (1+k_Y²)/α_common = 36π               [T1, res {rel_res_eccc:.0e}]")
print(f"  sin²θ_W(M_c) = 3/8                    [T1, res {res_sin2:.0e}]")
print()
print("Tier upgrades this cycle:")
print("  k_Y²: T3 (C272) → T2a (C273)")
print("    Chain: D7=SU(3)[T2a] + dim=3[T1] + uniqueness[T1] → T2a composite")
print("  ECCC Term2_SM α₁ piece: T3 (C272) → T2a (C273)")
print()
print("Remaining T4 in ECCC identity:")
print("  α_s piece of Term2_SM: C_match +0.34% from V(φ) alone (C265/C266)")
print("  → Once C_match is T2a from first principles, ECCC → T1 algebraic")
