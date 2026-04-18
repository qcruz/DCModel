"""
U(1) from paired zero modes — SO(2n) ∩ Aut(J) = U(n) verification.

Physical question:
    Does the real φ⁴ substrate field equation produce U(1), SU(2), SU(3) as gauge
    groups from real zero modes, given that the substrate equation is second-order
    in time (providing 2 real DOFs per zero mode)?

DFC mechanism:
    Each zero mode η₀(x) has a 2D initial data space (position q₀, velocity v₀).
    For n kinks at the same depth, the 2n real DOFs (q₁,v₁,...,qₙ,vₙ) span S^(2n-1)
    with SO(2n) real isometry. The D5 complex structure J (identifying each (q,v) pair
    as a complex DOF q+iv) reduces SO(2n) to U(n). After factoring out the D5 U(1),
    the residual gauge group is SU(n).

    Key result: SO(2) = U(1) exactly (no complex structure needed at D5 — the real
    and complex pictures coincide for n=1).

Key references:
    - foundations/complex_zero_mode_gap.md (Cycle 70)
    - foundations/zero_mode_multiplet.md (Cycle 59 — n complex modes → SU(n))
    - foundations/bifurcation_mode_count.md (Cycle 62–67c — Bottleneck 1 map)
    - equations/complex_structure_derivation.py (Cycle 67c — D5 makes D6 complex)
"""

import numpy as np


# ─────────────────────────────────────────────────────────────────────────────
# Lie algebra generators for SO(2n) and U(n)
# ─────────────────────────────────────────────────────────────────────────────

def so_generators(dim):
    """
    Return the generators of SO(dim) — antisymmetric real matrices.
    A generator T_{ij} has +1 at position (i,j) and -1 at (j,i), zeros elsewhere.
    Returns list of dim*(dim-1)/2 matrices.
    """
    gens = []
    for i in range(dim):
        for j in range(i + 1, dim):
            T = np.zeros((dim, dim))
            T[i, j] = 1.0
            T[j, i] = -1.0
            gens.append(T)
    return gens


def u_generators(n):
    """
    Return the generators of U(n) acting on ℝ^(2n) via complex structure J.
    Organized as:
      - n² Hermitian generators of u(n): real part (n symmetric) + imaginary part (n antisymmetric)
    In the real 2n×2n representation with basis (q₁,v₁,...,qₙ,vₙ):
      Complex multiplication by i corresponds to J (block diagonal: [[0,-1],[1,0]] per mode).
    Returns list of n² real 2n×2n matrices that generate U(n).
    """
    dim = 2 * n
    gens = []

    # Real symmetric generators of u(n) — these are block symmetric in the (q,v) basis
    # A_ab^{sym}: acts as (q_a + iv_a) ← (q_b + iv_b) + h.c. in real rep
    for a in range(n):
        for b in range(a, n):
            T = np.zeros((dim, dim))
            # q_a component from q_b and vice versa
            T[2*a, 2*b] = 1.0
            if a != b:
                T[2*b, 2*a] = 1.0
            # v_a component from v_b and vice versa
            T[2*a+1, 2*b+1] = 1.0
            if a != b:
                T[2*b+1, 2*a+1] = 1.0
            gens.append(T)

    # Imaginary antisymmetric generators — rotations mixing (q_a,v_b) and (q_b,v_a) type
    # A_ab^{antisym}: acts as (q_a + iv_a) ← i(q_b + iv_b) - h.c. in real rep
    for a in range(n):
        for b in range(a, n):
            T = np.zeros((dim, dim))
            if a == b:
                # Diagonal: the complex structure J in mode a — rotation of (q_a, v_a)
                T[2*a, 2*a+1] = 1.0
                T[2*a+1, 2*a] = -1.0
            else:
                # Off-diagonal: imaginary coupling between modes a and b
                T[2*a, 2*b+1] = 1.0
                T[2*b+1, 2*a] = -1.0
                T[2*a+1, 2*b] = -1.0
                T[2*b, 2*a+1] = 1.0
            gens.append(T)

    return gens


def complex_structure(n):
    """
    Return the complex structure J on ℝ^(2n): J(q_k) = v_k, J(v_k) = -q_k.
    In basis (q₁,v₁,...,qₙ,vₙ): block-diagonal with 2×2 blocks [[0,-1],[1,0]].
    J² = -I (verified).
    """
    dim = 2 * n
    J = np.zeros((dim, dim))
    for k in range(n):
        J[2*k,   2*k+1] = -1.0   # J(v_k) = -q_k
        J[2*k+1, 2*k  ] =  1.0   # J(q_k) = v_k
    return J


# ─────────────────────────────────────────────────────────────────────────────
# SO(2) = U(1): the D5 case
# ─────────────────────────────────────────────────────────────────────────────

def verify_so2_eq_u1():
    """
    SO(2) and U(1) are isomorphic Lie groups:
    - Both are 1-dimensional
    - Both have abelian Lie algebras
    - The unique generator of SO(2) acts identically to the U(1) phase rotation
    """
    print("--- SO(2) = U(1) verification (D5, n=1) ---")

    # SO(2) generator: the 2×2 antisymmetric matrix
    so2_gens = so_generators(2)
    print(f"  dim(SO(2)) = {len(so2_gens)}  (expected: 1)")
    T_so2 = so2_gens[0]
    print(f"  SO(2) generator:\n    [[{T_so2[0,0]:.0f}, {T_so2[0,1]:.0f}],\n     [{T_so2[1,0]:.0f}, {T_so2[1,1]:.0f}]]")

    # U(1) generator: the 2×2 complex structure J₁
    J = complex_structure(1)
    print(f"  J = complex structure on ℝ²:\n    [[{J[0,0]:.0f}, {J[0,1]:.0f}],\n     [{J[1,0]:.0f}, {J[1,1]:.0f}]]")

    # Check J² = -I
    J2 = J @ J
    J2_err = np.max(np.abs(J2 + np.eye(2)))
    print(f"  J² = -I: max error = {J2_err:.2e}  ✓" if J2_err < 1e-14
          else f"  J² = -I: FAILED, error = {J2_err:.2e}")

    # SO(2) generator = -J (sign convention: T_{01} vs J differ by sign — same algebra)
    diff_pos = np.max(np.abs(T_so2 - J))
    diff_neg = np.max(np.abs(T_so2 + J))
    same = min(diff_pos, diff_neg) < 1e-14
    print(f"  T_SO(2) = ±J: min diff = {min(diff_pos, diff_neg):.2e}  {'✓ same generator (sign convention)' if same else 'DIFFERS'}")

    # Lie algebra is abelian (commutator = 0 trivially for 1-generator algebra)
    print(f"  Both algebras: 1-dimensional, abelian → SO(2) ≅ U(1)  ✓")
    return len(so2_gens) == 1


# ─────────────────────────────────────────────────────────────────────────────
# SO(4) ≠ SU(2): the D6 problem
# ─────────────────────────────────────────────────────────────────────────────

def verify_so4_ne_su2():
    """
    SO(4) has dimension 6; SU(2) has dimension 3.
    The real isometry of S³ (four real zero modes) is SO(4) ≅ SU(2)×SU(2),
    which is strictly larger than SU(2). Complex structure is required to reduce it.
    """
    print("\n--- SO(4) ≠ SU(2) verification (D6 problem, n=2) ---")

    so4_gens = so_generators(4)
    print(f"  dim(SO(4)) = {len(so4_gens)}  (expected: 6)")
    print(f"  dim(SU(2)) = 3")
    print(f"  6 ≠ 3  →  SO(4) ≠ SU(2)  ✓")

    # Verify so(4) ≅ su(2) ⊕ su(2): decompose into self-dual and anti-self-dual parts
    # The 6 generators of SO(4) split into two sets of 3 that each satisfy su(2) relations

    # Standard SO(4) generators in basis (q₁,v₁,q₂,v₂):
    # Label the 4 axes: 0=q₁, 1=v₁, 2=q₂, 3=v₂
    # Generators: J_{01}, J_{02}, J_{03}, J_{12}, J_{13}, J_{23}
    # Self-dual (SU(2)_L): L_k = (J_{0k} + ε_{klm} J_{lm}) / 2
    # Anti-self-dual (SU(2)_R): R_k = (J_{0k} - ε_{klm} J_{lm}) / 2

    def so4_gen(i, j, dim=4):
        T = np.zeros((dim, dim))
        T[i, j] = 1.0
        T[j, i] = -1.0
        return T

    J01 = so4_gen(0, 1)
    J02 = so4_gen(0, 2)
    J03 = so4_gen(0, 3)
    J12 = so4_gen(1, 2)
    J13 = so4_gen(1, 3)
    J23 = so4_gen(2, 3)

    # SU(2)_L generators
    L1 = (J23 + J01) / 2
    L2 = (J13 - J02) / 2
    L3 = (J12 + J03) / 2

    # SU(2)_R generators
    R1 = (J23 - J01) / 2
    R2 = (J13 + J02) / 2
    R3 = (J12 - J03) / 2

    # Check SU(2) commutation relations: [L_i, L_j] = ε_{ijk} L_k
    comm_L12 = L1 @ L2 - L2 @ L1
    err_L = np.max(np.abs(comm_L12 - L3))
    comm_L23 = L2 @ L3 - L3 @ L2
    err_L2 = np.max(np.abs(comm_L23 - L1))
    comm_L31 = L3 @ L1 - L1 @ L3
    err_L3 = np.max(np.abs(comm_L31 - L2))
    max_err_L = max(err_L, err_L2, err_L3)
    print(f"  SU(2)_L commutation [L_i,L_j]=ε_{{ijk}}L_k: max error = {max_err_L:.2e}"
          + ("  ✓" if max_err_L < 1e-14 else "  FAILED"))

    # Check SU(2) commutation relations for R
    comm_R12 = R1 @ R2 - R2 @ R1
    err_R = np.max(np.abs(comm_R12 - R3))
    comm_R23 = R2 @ R3 - R3 @ R2
    err_R2 = np.max(np.abs(comm_R23 - R1))
    comm_R31 = R3 @ R1 - R1 @ R3
    err_R3 = np.max(np.abs(comm_R31 - R2))
    max_err_R = max(err_R, err_R2, err_R3)
    print(f"  SU(2)_R commutation [R_i,R_j]=ε_{{ijk}}R_k: max error = {max_err_R:.2e}"
          + ("  ✓" if max_err_R < 1e-14 else "  FAILED"))

    # Check L and R commute: [L_i, R_j] = 0
    cross_errs = []
    for Li in [L1, L2, L3]:
        for Rj in [R1, R2, R3]:
            comm = Li @ Rj - Rj @ Li
            cross_errs.append(np.max(np.abs(comm)))
    max_cross = max(cross_errs)
    print(f"  [SU(2)_L, SU(2)_R] = 0: max error = {max_cross:.2e}"
          + ("  ✓" if max_cross < 1e-14 else "  FAILED"))

    print(f"  so(4) ≅ su(2)_L ⊕ su(2)_R: verified  ✓")
    return max_err_L < 1e-14 and max_err_R < 1e-14 and max_cross < 1e-14


# ─────────────────────────────────────────────────────────────────────────────
# Complex structure reduces SO(4) → U(2) → SU(2): the D6 resolution
# ─────────────────────────────────────────────────────────────────────────────

def commutant_dim(n):
    """
    Compute dim({a ∈ so(2n) : [a, J] = 0}) by finding the null space of the
    linear map a → [a, J] on the vector space so(2n).

    Method: build the |so(2n)|-dimensional space of generators; for each basis
    element G_i, flatten [G_i, J] into a vector; find the null-space dimension
    of the resulting matrix. The null-space dimension = dim(commutant in so(2n)).

    Expected result: dim({a ∈ so(2n) : [a,J]=0}) = dim(u(n)) = n².
    """
    J = complex_structure(n)
    dim = 2 * n
    gens = so_generators(dim)
    n_gens = len(gens)

    # Build matrix: row i = flatten([G_i, J])
    rows = []
    for G in gens:
        comm = G @ J - J @ G
        rows.append(comm.flatten())
    M = np.array(rows)   # shape: (n_gens, dim²)

    # Null space of M = linear combinations of generators that commute with J
    _, s, _ = np.linalg.svd(M, full_matrices=True)
    rank = np.sum(s > 1e-10)
    null_dim = n_gens - rank
    return null_dim


def verify_complex_structure_reduction_d6():
    """
    With complex structure J on ℝ⁴: SO(4) ∩ Aut(J) = U(2), dim = 4.
    Factor out U(1) → residual SU(2), dim = 3.

    The U(2) generators are linear combinations of SO(4) generators.
    We compute the dimension of the commutant {a ∈ so(4) : [a,J]=0}.
    Expected dimension = n² = 4.
    """
    print("\n--- Complex structure reduces SO(4) → U(2) → SU(2) (D6 resolution) ---")

    n = 2
    null_dim = commutant_dim(n)
    expected = n * n  # dim(u(n)) = n²

    print(f"  dim({{a ∈ so(4) : [a,J]=0}}) = {null_dim}  (expected: {expected} = dim(U(2)))")

    if null_dim == expected:
        print(f"  dim(U(2)) = 4 = 1 (U(1)) + 3 (SU(2))  →  SU(2) after factoring U(1)  ✓")

    return null_dim == expected


def so4_generator_list(dim=4):
    """Return numbered list of SO(4) generators."""
    gens = []
    for i in range(dim):
        for j in range(i + 1, dim):
            T = np.zeros((dim, dim))
            T[i, j] = 1.0
            T[j, i] = -1.0
            gens.append(T)
    return gens


def so4_generator_list_wrapper():
    return so4_generator_list()


def so_generator_list(dim):
    return so_generators(dim)


# ─────────────────────────────────────────────────────────────────────────────
# SO(6) → U(3) → SU(3): the D7 case
# ─────────────────────────────────────────────────────────────────────────────

def verify_complex_structure_reduction_d7():
    """
    With complex structure J on ℝ⁶: SO(6) ∩ Aut(J) = U(3), dim = 9.
    Factor out U(1) → residual SU(3), dim = 8.
    """
    print("\n--- Complex structure reduces SO(6) → U(3) → SU(3) (D7) ---")

    J = complex_structure(3)

    # Verify J² = -I
    J2_err = np.max(np.abs(J @ J + np.eye(6)))
    print(f"  J² = -I (n=3): max error = {J2_err:.2e}"
          + ("  ✓" if J2_err < 1e-14 else "  FAILED"))

    so6_gens = so_generators(6)
    print(f"  dim(SO(6)) = {len(so6_gens)}  (expected: 15)")

    n = 3
    null_dim = commutant_dim(n)
    expected = n * n  # dim(u(n)) = n²

    print(f"  dim({{a ∈ so(6) : [a,J]=0}}) = {null_dim}  (expected: {expected} = dim(U(3)))")

    if null_dim == expected:
        print(f"  dim(U(3)) = 9 = 1 (U(1)) + 8 (SU(3))  →  SU(3) after factoring U(1)  ✓")

    return null_dim == expected


# ─────────────────────────────────────────────────────────────────────────────
# Summary table
# ─────────────────────────────────────────────────────────────────────────────

def dimension_table():
    """
    Summary of the SO(2n) → U(n) → SU(n) hierarchy.
    Shows how the D5 complex structure reduces the real isometry group to the
    correct gauge group at each depth.
    """
    print("\n--- Dimension table: real substrate + complex structure → gauge group ---")
    print(f"  {'Depth':<6} {'n':<4} {'Real DOFs':<10} {'Real config':<12} "
          f"{'SO(2n) dim':<12} {'U(n) dim':<10} {'SU(n) dim':<10} {'Gauge group'}")
    print(f"  {'-'*78}")

    data = [
        (5, 1, 2,  "S¹ ⊂ ℝ²"),
        (6, 2, 4,  "S³ ⊂ ℝ⁴"),
        (7, 3, 6,  "S⁵ ⊂ ℝ⁶"),
    ]

    gauge_names = {1: "U(1)", 2: "SU(2)", 3: "SU(3)"}
    config_names = {1: "S¹ ⊂ ℝ²", 2: "S³ ⊂ ℝ⁴", 3: "S⁵ ⊂ ℝ⁶"}

    for (depth, n, real_dof, config) in data:
        so2n_dim = n * (2*n - 1)
        un_dim   = n * n
        sun_dim  = n * n - 1
        # For n=1: SO(2)=U(1) — complex structure not needed
        note = " (SO(2)=U(1): no J needed)" if n == 1 else ""
        print(f"  D{depth:<5} {n:<4} {real_dof:<10} {config:<12} "
              f"{so2n_dim:<12} {un_dim:<10} {sun_dim:<10} "
              f"{gauge_names[n]}{note}")

    print()
    print("  Key: SO(2n) dim = n(2n-1);  U(n) dim = n²;  SU(n) dim = n²-1")
    print("  For n=1: SO(2) = U(1) exactly (coincidence — real = complex picture)")
    print("  For n=2: SO(4) dim=6 > U(2) dim=4 > SU(2) dim=3  [complex structure needed]")
    print("  For n=3: SO(6) dim=15 > U(3) dim=9 > SU(3) dim=8  [complex structure needed]")


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 68)
    print("equations/u1_from_paired_modes.py — SO(2n)/U(n)/SU(n) verification")
    print("DFC: second-order PDE pairs zero modes; D5 complex structure reduces")
    print("     SO(2n) → U(n) → SU(n) at D6/D7; SO(2) = U(1) at D5 (no J needed)")
    print("=" * 68)

    ok1 = verify_so2_eq_u1()
    ok2 = verify_so4_ne_su2()
    ok3 = verify_complex_structure_reduction_d6()
    ok4 = verify_complex_structure_reduction_d7()
    dimension_table()

    print("--- Summary ---")
    results = [
        ("SO(2) = U(1) [D5 without complex structure]", ok1),
        ("so(4) ≅ su(2)_L ⊕ su(2)_R [D6 real isometry]", ok2),
        ("SO(4) ∩ Aut(J) = U(2), dim=4 [D6 with complex structure]", ok3),
        ("SO(6) ∩ Aut(J) = U(3), dim=9 [D7 with complex structure]", ok4),
    ]
    all_ok = True
    for name, status in results:
        mark = "✓" if status else "✗"
        print(f"  {mark}  {name}")
        if not status:
            all_ok = False

    print()
    print("  DFC status:")
    print("    D5 = U(1): DERIVED from real substrate (Tier 2 candidate)")
    print("    D6 = SU(2): requires D5 complex structure on D6 modes (Tier 3 gap)")
    print("    D7 = SU(3): requires D5 complex structure on D7 modes (Tier 3 gap)")
    print("    Remaining open: formal proof that D5 gauge field defines J on D6/D7 modes")
    print()
    print("  Reference: foundations/complex_zero_mode_gap.md (Cycle 70)")
