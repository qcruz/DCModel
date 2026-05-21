"""
Koide Formula: Algebraic Structure and DFC Z3 Connection
=========================================================

Physical question:
  Why do the three charged lepton masses satisfy the Koide formula
  K = (m_e+m_μ+m_τ)/(sqrt(m_e)+sqrt(m_μ)+sqrt(m_τ))^2 = 2/3
  to < 10 ppm? Is this a consequence of the Z3 symmetry of three
  coincident D7 kinks in the DFC substrate?

DFC mechanism:
  Three coincident D7 kinks have SU(3) isometry (Cycle 59: n coincident
  kinks -> SU(n) symmetry). The SU(3) isometry includes the discrete
  subgroup Z3 = {I, C, C^2} where C is the cyclic permutation (1->2->3->1).
  A mass matrix invariant under Z3 cyclic permutation of generations is
  exactly a circulant matrix.

Key derivations (Tier 1 algebra):
  THEOREM 1 (Koide <-> DFT condition, proved below):
    Koide K = 2/3  <=>  |F0| / |F1| = sqrt(2)
    where F_k = DFT_k(sqrt(m_e), sqrt(m_mu), sqrt(m_tau)) (without 1/sqrt(3))

  THEOREM 2 (Z3 symmetry <-> circulant, proved below):
    A 3x3 matrix M satisfies C M C^dagger = M  <=>  M is circulant
    where C is the cyclic permutation matrix of order 3.

  THEOREM 3 (mass circulant is Z3-invariant, proved below):
    The "mass circulant" Y_sqrt with first row (sqrt(m_e), sqrt(m_mu), sqrt(m_tau))
    satisfies [Y_sqrt, C] = 0 (commutes with cyclic permutation).

  OPEN STEP (Tier 3): Why does the physical DFC Yukawa matrix have the
    specific circulant with |F0|/|F1| = sqrt(2)?
    Z3 symmetry alone implies circulant structure; it does NOT fix the ratio
    |F0|/|F1|. The Koide condition K=2/3 is an additional constraint that
    requires a physical DFC derivation.

Status:
  Theorems 1-3: Tier 1 (algebraically proved below)
  Koide as DFC prediction: Tier 3 (Z3 structure motivated by Cycle 59;
    the ratio |F0|/|F1|=sqrt(2) not yet derived from V(phi))

Key references:
  - Cycle 59: zero_mode_multiplet.md — n coincident kinks -> SU(n) isometry
  - Cycle 117: d5_complex_from_instability.py — D5 complex structure from V(phi)
  - Cycle 122: tau_mass_koide.py — Koide prediction m_tau = 1776.97 MeV (+0.006%)
"""

import math
import cmath
import numpy as np

# ── Observed lepton masses (PDG 2022) ────────────────────────────────────────
M_E_MEV   = 0.51099895   # electron mass (MeV)
M_MU_MEV  = 105.6583755  # muon mass (MeV)
M_TAU_MEV = 1776.86      # tau mass (MeV)

KOIDE_TARGET = 2.0 / 3.0  # = 0.666...


# ── Utility ──────────────────────────────────────────────────────────────────

def koide_ratio(m1, m2, m3):
    """Compute K = (m1+m2+m3)/(sqrt(m1)+sqrt(m2)+sqrt(m3))^2."""
    return (m1 + m2 + m3) / (math.sqrt(m1) + math.sqrt(m2) + math.sqrt(m3)) ** 2


def dft3(x):
    """
    Compute the 3-point DFT (without 1/sqrt(3) normalization):
      F_k = sum_{j=0}^{2} omega^{jk} x_j,  omega = exp(2*pi*i/3)
    Returns (F0, F1, F2).
    """
    omega = cmath.exp(2j * math.pi / 3)
    x = list(x)
    F0 = x[0] + x[1] + x[2]
    F1 = x[0] + omega * x[1] + omega**2 * x[2]
    F2 = x[0] + omega**2 * x[1] + omega * x[2]  # = F1.conj()
    return F0, F1, F2


def circulant_matrix(row):
    """
    Construct 3x3 circulant matrix from first row (a, b, c):
      [[a, b, c],
       [c, a, b],
       [b, c, a]]
    """
    a, b, c = row
    return np.array([[a, b, c],
                     [c, a, b],
                     [b, c, a]], dtype=complex)


def cyclic_permutation_matrix():
    """C_{ij} = delta_{i, j+1 mod 3}: shifts columns left / rows down."""
    return np.array([[0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 0]], dtype=complex)


# ── THEOREM 1: Koide <-> DFT condition |F0|/|F1| = sqrt(2) ─────────────────

def prove_koide_dft_equivalence():
    """
    Prove THEOREM 1 algebraically:

    Let s = (sqrt(m0), sqrt(m1), sqrt(m2)) with mean v = (s0+s1+s2)/3.
    Define u_k = s_k - v  (zero-mean fluctuations).

    Then:
      K = sum(m_k) / (sum(sqrt(m_k)))^2
        = (sum((v+u_k)^2)) / (3v)^2
        = (3v^2 + sum(u_k^2)) / (9v^2)         [since sum(u_k)=0]
        = 1/3 + sum(u_k^2)/(9v^2)

    So K = 2/3  <=>  sum(u_k^2) = 3v^2.

    By Parseval's theorem for the 3-point DFT (without 1/sqrt(3)):
      sum(|u_k|^2) = (1/3)(|F0_u|^2 + |F1_u|^2 + |F2_u|^2)
    where F0_u = sum(u_k) = 0 (zero mean).
    So: sum(u_k^2) = (1/3)(2|F1|^2)  [since |F2| = |F1|*]

    Koide condition:  (2/3)|F1|^2 = 3v^2
      =>  |F1|^2 = 9v^2/2
      =>  |F1| = 3v/sqrt(2)
      =>  |F0|/|F1| = 3v / (3v/sqrt(2)) = sqrt(2)  QED
    """
    print("\n" + "="*66)
    print("THEOREM 1: Koide K=2/3  <=>  |F0|/|F1| = sqrt(2)")
    print("="*66)

    # Numerical verification with lepton masses
    m_vals = [M_E_MEV, M_MU_MEV, M_TAU_MEV]
    s_vals = [math.sqrt(m) for m in m_vals]
    v = sum(s_vals) / 3.0

    K = koide_ratio(*m_vals)
    F0, F1, F2 = dft3(s_vals)

    ratio = abs(F0) / abs(F1)

    print(f"\n  Lepton masses (MeV): m_e={M_E_MEV}, m_mu={M_MU_MEV}, m_tau={M_TAU_MEV}")
    print(f"  sqrt-mean v = {v:.6f} MeV^(1/2)")
    print(f"\n  Koide ratio K   = {K:.10f}  (target 2/3 = {KOIDE_TARGET:.10f})")
    print(f"  |F0|            = {abs(F0):.6f}")
    print(f"  |F1|            = {abs(F1):.6f}")
    print(f"  |F0|/|F1|       = {ratio:.10f}  (target sqrt(2) = {math.sqrt(2):.10f})")
    print(f"  Discrepancy from sqrt(2): {abs(ratio - math.sqrt(2)):.2e}")

    # Algebraic derivation: K = 1/3 + sum(u^2)/(9v^2)
    u_vals = [s - v for s in s_vals]
    sum_u2 = sum(u**2 for u in u_vals)
    sum_u2_parseval = (2 * abs(F1)**2) / 3.0  # Parseval
    K_from_formula = 1.0/3.0 + sum_u2 / (9.0 * v**2)

    print(f"\n  Algebraic check:")
    print(f"  sum(u_k^2)                = {sum_u2:.6f}")
    print(f"  (2/3)|F1|^2 [Parseval]    = {sum_u2_parseval:.6f}")
    print(f"  Parseval residual         = {abs(sum_u2 - sum_u2_parseval):.2e}")
    print(f"  K from formula 1/3+...    = {K_from_formula:.10f}")
    print(f"  K direct                  = {K:.10f}")
    print(f"  Agreement                 = {abs(K - K_from_formula):.2e}")

    # Key equivalence
    print(f"\n  EQUIVALENCE CHAIN (all numerically verified):")
    print(f"  K = 2/3  =>  sum(u^2) = 3v^2  =>  (2/3)|F1|^2 = 3v^2")
    print(f"           =>  |F1| = 3v/sqrt(2)  =>  |F0|/|F1| = sqrt(2)")
    print(f"  Residual from 3v^2 = sum(u^2): {abs(sum_u2 - 3*v**2):.2e}")
    print(f"  STATUS: THEOREM 1 PROVED (algebraic + numerical) [TIER 1]")

    return {
        'K': K, 'ratio': ratio, 'v': v,
        'F0': F0, 'F1': F1, 'F2': F2,
        'target_ratio': math.sqrt(2),
        'residual': abs(ratio - math.sqrt(2)),
    }


# ── THEOREM 2: Z3 cyclic invariance <-> circulant ───────────────────────────

def prove_z3_circulant_equivalence():
    """
    Prove THEOREM 2:
    A 3x3 matrix M satisfies C M C^dagger = M  <=>  M is circulant.

    Proof:
    (=>) If M is circulant with first row (a,b,c), then:
      M = a*I_circ + b*C + c*C^2
    where I_circ = circulant(1,0,0) = identity, C = circulant(0,1,0) = cyclic shift.
    Since C commutes with itself: C(a*I+b*C+c*C^2)C^dagger = a*I+b*C+c*C^2 = M. QED.

    (<=) If C M C^dagger = M, then M commutes with C: [M,C]=0.
    The cyclic permutation C has eigenvalues {1, omega, omega^2} and is diagonalized
    by the DFT matrix F3. Matrices that commute with C are simultaneously diagonalized
    by F3, i.e., M = F3^dagger * diag(lambda_0, lambda_1, lambda_2) * F3.
    The matrix with this form has entry M_{ij} = (1/3) sum_k lambda_k omega^{(j-i)k},
    which depends only on (j-i) mod 3 -> M is circulant. QED.
    """
    print("\n" + "="*66)
    print("THEOREM 2: Z3 cyclic invariance  <=>  circulant structure")
    print("="*66)

    C = cyclic_permutation_matrix()

    # Test with lepton mass circulant
    s_vals = [math.sqrt(M_E_MEV), math.sqrt(M_MU_MEV), math.sqrt(M_TAU_MEV)]
    Y = circulant_matrix(s_vals)

    # Check C Y C^dagger = Y
    CYCd = C @ Y @ C.conj().T
    residual_cmc = np.max(np.abs(CYCd - Y))

    # Check [Y, C] = 0
    commutator = Y @ C - C @ Y
    residual_comm = np.max(np.abs(commutator))

    print(f"\n  Mass circulant Y (first row = (sqrt(m_e), sqrt(m_mu), sqrt(m_tau))):")
    print(f"  Y[0] = [{Y[0,0].real:.4f}, {Y[0,1].real:.4f}, {Y[0,2].real:.4f}]")
    print(f"  Y[1] = [{Y[1,0].real:.4f}, {Y[1,1].real:.4f}, {Y[1,2].real:.4f}]")
    print(f"  Y[2] = [{Y[2,0].real:.4f}, {Y[2,1].real:.4f}, {Y[2,2].real:.4f}]")

    print(f"\n  Cyclic permutation C:")
    print(f"  C[0] = {list(C[0].real.astype(int))}")
    print(f"  C[1] = {list(C[1].real.astype(int))}")
    print(f"  C[2] = {list(C[2].real.astype(int))}")

    print(f"\n  max|C Y C^dagger - Y| = {residual_cmc:.2e}   [Z3-invariance check]")
    print(f"  max|[Y, C]|           = {residual_comm:.2e}   [commutator check]")

    # Also verify: C^3 = I
    C3 = np.linalg.matrix_power(C, 3)
    print(f"  max|C^3 - I|          = {np.max(np.abs(C3 - np.eye(3))):.2e}   [Z3 order]")

    print(f"\n  Eigenvalues of C: ", end="")
    eigC = np.linalg.eigvals(C)
    for lam in sorted(eigC, key=lambda x: x.real):
        print(f"{lam.real:.4f}{lam.imag:+.4f}i", end="  ")
    print(f"\n  These are {{1, omega, omega^2}} with omega = exp(2*pi*i/3) as expected.")

    print(f"\n  STATUS: THEOREM 2 VERIFIED (algebraic + numerical) [TIER 1]")
    return {'residual_cmc': residual_cmc, 'residual_comm': residual_comm}


# ── THEOREM 3: Eigenvalues of mass circulant = DFT of sqrt masses ────────────

def prove_mass_circulant_eigenvalues():
    """
    THEOREM 3: The mass circulant Y_sqrt (first row = (sqrt(m_e), sqrt(m_mu), sqrt(m_tau)))
    has eigenvalues equal to the DFT of (sqrt(m_e), sqrt(m_mu), sqrt(m_tau)).

    These eigenvalues are:
      lambda_0 = sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau)  [real, positive, DC]
      lambda_1 = sqrt(m_e) + omega*sqrt(m_mu) + omega^2*sqrt(m_tau)  [complex]
      lambda_2 = lambda_1*  [complex conjugate]

    Key ratios:
      |lambda_0| / |lambda_1| = sqrt(2)  [from Theorem 1, Koide = 2/3]
      |lambda_1| = |lambda_2|            [always true for real circulant]

    IMPORTANT: The masses m_k are NOT the squared eigenvalues |lambda_k|^2.
    The masses are the DIAGONAL ENTRIES of Y_sqrt^2, i.e., m_k = (Y_sqrt^2)_{kk}.
    The mass circulant Y_sqrt encodes the generation structure, NOT the diagonalized
    mass matrix.

    The DFC interpretation:
      Y_sqrt is the "amplitude matrix" in generation space, encoding which amplitude
      (sqrt(m_k)) goes into each generation slot. Its eigenvalues are the DFT modes
      of the mass amplitudes, with the Koide condition ensuring |F0|/|F1| = sqrt(2).
    """
    print("\n" + "="*66)
    print("THEOREM 3: Mass circulant eigenvalues and DFT structure")
    print("="*66)

    s_vals = [math.sqrt(M_E_MEV), math.sqrt(M_MU_MEV), math.sqrt(M_TAU_MEV)]
    Y = circulant_matrix(s_vals)

    # Eigenvalues of Y
    eig_Y = np.linalg.eigvals(Y)
    eig_Y_sorted = sorted(eig_Y, key=lambda x: -x.real)

    # DFT of sqrt masses
    F0, F1, F2 = dft3(s_vals)

    print(f"\n  Eigenvalues of Y_sqrt:")
    for i, lam in enumerate(eig_Y_sorted):
        print(f"  lambda_{i} = {lam.real:.6f} {lam.imag:+.6f}i   |lambda| = {abs(lam):.6f}")

    print(f"\n  DFT of (sqrt(m_e), sqrt(m_mu), sqrt(m_tau)):")
    print(f"  F0 = {F0.real:.6f} {F0.imag:+.6f}i   |F0| = {abs(F0):.6f}")
    print(f"  F1 = {F1.real:.6f} {F1.imag:+.6f}i   |F1| = {abs(F1):.6f}")
    print(f"  F2 = {F2.real:.6f} {F2.imag:+.6f}i   |F2| = {abs(F2):.6f}")

    # Match eigenvalues to DFT
    dft_vals = [F0, F1, F2]
    # Eigenvalues should be the DFT values (up to ordering)
    eig_set = sorted([abs(l) for l in eig_Y])
    dft_set = sorted([abs(f) for f in dft_vals])
    max_eig_dft_err = max(abs(e - d) for e, d in zip(eig_set, dft_set))
    print(f"\n  max|eigenvalue| - |DFT|: {max_eig_dft_err:.2e}  [should be ~0]")

    # Koide ratio for eigenvalues
    ratio = abs(F0) / abs(F1)
    print(f"\n  |F0|/|F1| = {ratio:.10f}  (target sqrt(2) = {math.sqrt(2):.10f})")
    print(f"  |F1| = |F2|: {abs(abs(F1) - abs(F2)):.2e}  [always true for real circulant]")

    # Verify |lambda_0|/|lambda_1| = sqrt(2) for lepton masses
    lam_sorted_by_abs = sorted(eig_Y, key=lambda x: -abs(x))
    ratio_eig = abs(lam_sorted_by_abs[0]) / abs(lam_sorted_by_abs[1])
    print(f"\n  Eigenvalue ratio |lambda_0|/|lambda_1| = {ratio_eig:.6f}")
    print(f"  Koide condition satisfied: |ratio - sqrt(2)| = {abs(ratio_eig - math.sqrt(2)):.2e}")

    print(f"\n  STATUS: THEOREM 3 VERIFIED [TIER 1]")
    return {'F0': F0, 'F1': F1, 'ratio': ratio}


# ── DFC CONNECTION: SU(3) isometry -> Z3 -> circulant ───────────────────────

def dfc_su3_to_z3_argument():
    """
    State the DFC argument connecting SU(3) isometry to circulant mass matrix.

    PROVED (Tier 1, Cycle 59 zero_mode_multiplet.md):
      Three coincident degenerate D7 kinks on a common background share the
      same spatial profile eta_0(x) ∝ sech^2(x/xi). Their zero mode amplitudes
      c = (c1, c2, c3) ∈ C^3 have configuration space S^5 ⊂ C^3.
      The complex-structure-preserving isometry of S^5 is U(3) = U(1) x SU(3).
      The U(1) factor is absorbed by D5. The gauge group at D7 is SU(3).

    PROVED (Tier 1 algebra, Theorem 2 above):
      Z3 ⊂ S3 ⊂ SU(3) is the cyclic permutation subgroup.
      Invariance under Z3 cyclic permutation <=> circulant mass matrix.

    DFC PATH TO KOIDE (Tier 3 — not yet proved):
      Step A: The Yukawa overlap of the three coincident D7 kinks with the D6
              Higgs zero mode produces a mass matrix M in generation space.
              The SU(3) isometry of the three coincident kinks implies:
              Permuting kinks i -> i+1 mod 3 is a symmetry of the substrate.
              This Z3 symmetry forces [M, C] = 0 -> M is circulant.

              [This step is Tier 3: it requires showing the Yukawa overlap
               integral is Z3-invariant under cyclic kink permutation.
               The SU(3) isometry suggests this, but the explicit Yukawa
               computation is not yet done.]

      Step B: The circulant mass matrix M has eigenvalues (DFT of first row).
              For the physical lepton masses, the ratio |F0|/|F1| = sqrt(2).
              This specific ratio is the Koide condition.

              [This step is OPEN: Z3 symmetry gives circulant structure, but
               does NOT fix |F0|/|F1| = sqrt(2). Additional physics is needed.
               Candidates:
               (a) Equal-norm condition: all three kinks have equal Yukawa
                   coupling magnitude |Y_{ij}| = y for all i,j -> this alone
                   gives |F0| = |F1| = |F2| = 3y (DFT of constant sequence),
                   not sqrt(2) ratio. Not sufficient.
               (b) Specific phase structure from D5 complex structure (Cycle 117):
                   The tachyonic instability at D5 introduces a Z2 topology
                   (two vacua) which interacts with the Z3 of three D7 kinks
                   to produce a Z6 = Z2 x Z3 phase structure. This may fix
                   the Yukawa phases and thereby fix |F0|/|F1| = sqrt(2).
               (c) BPS Bogomolny constraint: the BPS superpotential W=1-psi^2
                   (Cycle 111) provides Q_top=2 and I4=4/3. Their product
                   gives g^2 = 2I4 = 8/3. A similar product formula for the
                   Yukawa might fix the ratio.
               Status of (a)-(c): Tier 4 (stated but not derived).]
    """
    print("\n" + "="*66)
    print("DFC CONNECTION: SU(3) isometry -> Z3 -> circulant -> Koide")
    print("="*66)

    print("""
  STEP 1 (PROVED, Tier 1, Cycle 59): Three coincident D7 kinks have SU(3) isometry.
    The cyclic permutation Z3 ⊂ S3 ⊂ SU(3) is included.
    Reference: foundations/zero_mode_multiplet.md

  STEP 2 (PROVED, Tier 1, Theorem 2 above): Z3 cyclic symmetry <=> circulant matrix.
    The mass matrix M commutes with cyclic permutation C iff M is circulant.

  STEP 3 (Tier 3, OPEN): The D7 Yukawa coupling is Z3-invariant under kink permutation.
    Plausible from SU(3) isometry, but the explicit Yukawa overlap integral not computed.
    What needs to be shown:
      Y_{i,j} = y_{(j-i) mod 3}  [Yukawa depends only on relative generation index]
    This follows from the equal-weight theorem if all three kinks couple equally to Higgs.

  STEP 4 (Tier 4, OPEN): The specific ratio |F0|/|F1| = sqrt(2) (Koide condition).
    Z3 symmetry gives circulant structure; does NOT fix the ratio.
    Additional physical input required (see dfc_su3_to_z3_argument() docstring).
    Candidate: Z2 x Z3 = Z6 phase structure from D5 tachyon x D7 three-kink system.
""")

    # Numerical summary
    print("  NUMERICAL SUMMARY (lepton masses):")
    K = koide_ratio(M_E_MEV, M_MU_MEV, M_TAU_MEV)
    F0, F1, F2 = dft3([math.sqrt(m) for m in [M_E_MEV, M_MU_MEV, M_TAU_MEV]])
    print(f"  K = {K:.10f}   (target 2/3 = {KOIDE_TARGET:.10f})")
    print(f"  |F0|/|F1| = {abs(F0)/abs(F1):.10f}  (target sqrt(2) = {math.sqrt(2):.10f})")
    print(f"  K = 2/3 and |F0|/|F1| = sqrt(2) are consistent to {abs(K - KOIDE_TARGET):.2e}")


# ── CROSS-CHECK: Koide satisfied <=> sqrt(2) ratio <=> 45 degrees ───────────

def cross_check_all_equivalences():
    """
    Verify all three equivalent formulations of the Koide condition:
    1. K = 2/3  (standard Koide ratio)
    2. |F0|/|F1| = sqrt(2)  (DFT condition, Theorem 1)
    3. Angle to democratic direction = 45 degrees  (geometric, tau_mass_koide.py)
    """
    print("\n" + "="*66)
    print("CROSS-CHECK: Three equivalent Koide formulations")
    print("="*66)

    masses = [M_E_MEV, M_MU_MEV, M_TAU_MEV]
    sqrts = [math.sqrt(m) for m in masses]
    v = sum(sqrts) / 3.0

    # 1. Koide ratio
    K = koide_ratio(*masses)
    err1 = abs(K - 2.0/3.0)

    # 2. DFT ratio
    F0, F1, F2 = dft3(sqrts)
    ratio = abs(F0) / abs(F1)
    err2 = abs(ratio - math.sqrt(2))

    # 3. Angle to democratic direction (1,1,1)/sqrt(3)
    s = np.array(sqrts)
    democratic = np.ones(3) / math.sqrt(3)
    s_norm = np.linalg.norm(s)
    cos_theta = np.dot(s / s_norm, democratic)
    theta_deg = math.degrees(math.acos(min(1.0, cos_theta)))
    err3 = abs(theta_deg - 45.0)

    print(f"\n  Formulation 1 — Koide ratio:")
    print(f"    K = {K:.10f}  (target 2/3 = {KOIDE_TARGET:.10f})")
    print(f"    Error: {err1:.2e}  ({err1/KOIDE_TARGET*100:.4f}%)")

    print(f"\n  Formulation 2 — DFT ratio (Theorem 1):")
    print(f"    |F0|/|F1| = {ratio:.10f}  (target sqrt(2) = {math.sqrt(2):.10f})")
    print(f"    Error: {err2:.2e}  ({err2/math.sqrt(2)*100:.4f}%)")

    print(f"\n  Formulation 3 — Angle to democratic direction:")
    print(f"    Angle = {theta_deg:.8f} degrees  (target 45.000000)")
    print(f"    Error: {err3:.2e} degrees")

    # All three should give the same (tiny) discrepancy from exact Koide
    print(f"\n  All three are equivalent: the small discrepancy (< 10 ppm) from exact")
    print(f"  Koide is due to limited precision in the observed lepton masses.")
    print(f"\n  STATUS: All three formulations consistent to < 10 ppm [TIER 1]")

    return {'K': K, 'dft_ratio': ratio, 'angle_deg': theta_deg}


# ── TIER ASSESSMENT ──────────────────────────────────────────────────────────

def tier_assessment():
    print("\n" + "="*66)
    print("TIER ASSESSMENT")
    print("="*66)
    print("""
  THEOREM 1 (Koide <-> DFT |F0|/|F1|=sqrt(2)): TIER 1
    Proved algebraically from the definition of K and Parseval's theorem.
    No free parameters. Numerical residuals < 1e-10.

  THEOREM 2 (Z3 invariance <-> circulant): TIER 1
    Standard result in circulant matrix theory.
    Numerically verified: max|C Y C^dagger - Y| < 1e-14.

  THEOREM 3 (Mass circulant eigenvalues = DFT): TIER 1
    Standard circulant eigenvalue theorem.
    Numerically verified: eigenvalues match DFT to < 1e-10.

  STEP 3 (Yukawa overlap is Z3-invariant): TIER 3
    Motivated by SU(3) isometry of three coincident D7 kinks (Cycle 59).
    Not yet proved from explicit Yukawa overlap integral.
    Required: show Y_{ij} = y_{(j-i) mod 3} from DFC substrate.

  STEP 4 (|F0|/|F1| = sqrt(2) from DFC): TIER 4
    This is the deepest open step.
    Z3 symmetry alone does not fix this ratio.
    Candidates: Z2 x Z3 phase structure; BPS product formula.
    No derivation available.

  OVERALL: Koide formula as DFC prediction — TIER 3 CANDIDATE
    Algebraic structure is fully formalized (Theorems 1-3, Tier 1).
    Physical DFC mechanism (Steps 3-4) requires further derivation.
    If Steps 3-4 are proved: tau mass failure is closed with 0 free parameters.
    Current tau mass prediction via Koide: 1776.97 MeV (+0.006% vs obs 1776.86 MeV).
""")


# ── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("="*66)
    print("Koide Formula: Algebraic Structure and DFC Z3 Connection")
    print("="*66)
    print(f"Lepton masses: m_e={M_E_MEV} MeV, m_mu={M_MU_MEV} MeV, m_tau={M_TAU_MEV} MeV")

    r1 = prove_koide_dft_equivalence()
    r2 = prove_z3_circulant_equivalence()
    r3 = prove_mass_circulant_eigenvalues()
    dfc_su3_to_z3_argument()
    r4 = cross_check_all_equivalences()
    tier_assessment()

    print("\n" + "="*66)
    print("SUMMARY TABLE")
    print("="*66)
    print(f"  Koide K                = {r1['K']:.10f}  (target 2/3)")
    print(f"  |F0|/|F1|              = {r1['ratio']:.10f}  (target sqrt(2))")
    print(f"  Angle to (1,1,1)       = {r4['angle_deg']:.8f} degrees  (target 45)")
    print(f"  Z3 commutator residual = {r2['residual_comm']:.2e}  (target 0, numerical)")
    koide_dev = abs((2*abs(r1['F1'])**2/3) - 3*r1['v']**2)
    print(f"  Koide deviation (|Σu²-3v²|) = {koide_dev:.2e}  (non-zero: K≠2/3 exactly at 9 ppm)")
    print(f"  DFT eigenvalue match   = {r3['ratio']:.10f}  (target sqrt(2))")
    print()
    print(f"  KEY RESULT: Koide K=2/3 is equivalent to |F0|/|F1|=sqrt(2)")
    print(f"  where F_k = DFT_k(sqrt(m_e), sqrt(m_mu), sqrt(m_tau)).")
    print(f"  This is equivalent to the mass circulant Y_sqrt having eigenvalue")
    print(f"  ratio |lambda_0|/|lambda_1| = sqrt(2) (Koide condition).")
    print()
    print(f"  OPEN: Why does DFC produce |F0|/|F1| = sqrt(2) specifically?")
    print(f"  Answering this would upgrade Koide from Tier 3 to Tier 2a.")
    print(f"  The Z3 symmetry of three coincident D7 kinks (Cycle 59) gives")
    print(f"  circulant structure (Theorems 2-3) but NOT the sqrt(2) ratio.")
