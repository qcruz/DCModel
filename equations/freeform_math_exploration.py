"""
Freeform Mathematical Exploration — DFC Model

This module is a living workspace for taking DFC derivations, identities, and
parameters and running them through interesting mathematical transformations
to see what emerges. The goal is not to prove anything specific, but to
discover unexpected connections, simplifications, or patterns.

Each exploration is self-contained with its own section. Results that look
promising get flagged for follow-up in dedicated equation modules.

STATUS: Active exploration workspace. Not a prediction module.
"""

import math
from fractions import Fraction

print("=" * 76)
print("FREEFORM MATHEMATICAL EXPLORATION — DFC MODEL")
print("=" * 76)
print()

# ─────────────────────────────────────────────────────────────────────────────
# DFC FUNDAMENTAL PARAMETERS (for reference)
# ─────────────────────────────────────────────────────────────────────────────

alpha = 18**(1/3)                        # primitive compression parameter
beta = Fraction(1, 9) / math.pi          # quartic coupling (1/(9*pi))
beta_f = 1.0 / (9 * math.pi)
phi_0 = math.sqrt(alpha / beta_f)        # vacuum expectation value
xi = math.sqrt(2 / alpha)                # kink width
E_kink = (4/3) * alpha**(3/2) / (beta_f * math.sqrt(2))  # kink energy (Planck units)
I4 = Fraction(4, 3)                      # kink shape integral = C_2(fund, SU(3))
N_Hopf = 9                               # Hopf sphere count = N_c^2
g_eff_sq = Fraction(8, 27)               # effective gauge coupling squared
Q_top = 2                                # topological charge per kink
S_kink = 4.0 / beta_f                    # kink action = 36*pi
alpha_em_Mc = beta_f / 4                 # alpha_em at M_c = beta/4
Lambda_QCD = 304.5                       # MeV
M_N = math.sqrt(3 * math.pi) * Lambda_QCD  # nucleon mass (MeV)
kappa = 5.33                             # inter-generation mass ratio

print("Reference parameters:")
print(f"  alpha = 18^(1/3) = {alpha:.6f}")
print(f"  beta  = 1/(9*pi) = {beta_f:.8f}")
print(f"  phi_0 = {phi_0:.4f} M_Pl")
print(f"  xi    = {xi:.6f} l_Pl")
print(f"  E_kink = {E_kink:.2f} M_Pl  (= 4/beta = {4/beta_f:.4f}? No: S_kink = {S_kink:.4f})")
print(f"  S_kink = 4/beta = 36*pi = {36*math.pi:.4f}  (check: {S_kink:.4f})")
print(f"  I_4   = 4/3")
print(f"  g_eff^2 = 8/27 = {float(g_eff_sq):.8f}")
print(f"  Q_top = {Q_top}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 1: Algebraic relations among DFC constants
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 1: Algebraic Relations Among DFC Constants")
print("=" * 76)
print()

# Known exact identities — let's see what other combinations are interesting.

# Identity 1: S_kink * alpha_em(M_c) = 1  [T1, C171]
id1 = S_kink * (beta_f / 4)
print(f"  S_kink * alpha_em(M_c) = {id1:.15f}  (should be 1)")

# Identity 2: g_eff^2 = 2*I_4 / N_Hopf  [T2a]
id2 = 2 * float(I4) / N_Hopf
print(f"  2*I_4/N_Hopf = {id2:.15f}  (should be {float(g_eff_sq):.15f})")

# Identity 3: Q_top = I_4 * N_c / 2  [T1]
id3 = float(I4) * 3 / 2
print(f"  I_4 * N_c / 2 = {id3:.15f}  (should be {Q_top})")

# Identity 4: alpha^3 = 18  [definition]
id4 = alpha**3
print(f"  alpha^3 = {id4:.15f}  (should be 18)")

# Identity 5: S_kink = 36*pi  [from beta = 1/(9*pi)]
print(f"  S_kink = {S_kink:.10f},  36*pi = {36*math.pi:.10f}")
print()

# Now let's explore PRODUCTS and RATIOS of these
print("  Exploring products and ratios:")
print()

# What is alpha * I_4?
prod1 = alpha * float(I4)
print(f"  alpha * I_4 = {prod1:.6f}")
print(f"    = 18^(1/3) * 4/3 = 4 * 18^(1/3) / 3 = 4 * (2/3)^(1/3) * 3^(1/3-1)")
print(f"    = 4 * 6^(1/3) / 3 = {4 * 6**(1/3) / 3:.6f}  (check)")

# What is alpha * beta?
prod2 = alpha * beta_f
print(f"  alpha * beta = {prod2:.8f}")
print(f"    = 18^(1/3) / (9*pi) = 2^(1/3) * 3^(2/3) / (9*pi) = 2^(1/3) / (3^(4/3) * pi)")
print(f"    compare: 1/(3*pi) = {1/(3*math.pi):.8f}")

# phi_0^2 = alpha / beta
phi0_sq = alpha / beta_f
print(f"  phi_0^2 = alpha/beta = {phi0_sq:.4f}")
print(f"    = 18^(1/3) * 9*pi = 9*pi * 18^(1/3) = {9*math.pi*alpha:.4f}")

# xi * phi_0 — the "amplitude-width product"
xi_phi0 = xi * phi_0
print(f"  xi * phi_0 = {xi_phi0:.6f}")
print(f"    = sqrt(2/alpha) * sqrt(alpha/beta) = sqrt(2/beta) = sqrt(18*pi)")
print(f"    = {math.sqrt(18*math.pi):.6f}  (check: {xi_phi0:.6f})")

# E_kink in terms of simple combinations
print(f"  E_kink = {E_kink:.4f} M_Pl")
print(f"    S_kink / (2*pi) = {S_kink/(2*math.pi):.4f}")
print(f"    = 18 (check: {S_kink/(2*math.pi):.4f})")
print(f"    So E_kink / M_Pl = S_kink = 36*pi, and S_kink/(2*pi) = 18 = alpha^3")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 2: The "DFC number" — combining all fundamental constants
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 2: Characteristic DFC Numbers")
print("=" * 76)
print()

# What dimensionless numbers can we form from {alpha, beta, I_4, N_Hopf, Q_top}?
# These are the 5 key DFC parameters (all dimensionless in Planck units).

# Already known: g_eff^2 = 8/27, S_inst = 27*pi^2, etc.
# Let's look for less obvious ones.

# Ratio: S_inst / S_kink = instanton action / kink action
S_inst = 27 * math.pi**2
ratio_inst_kink = S_inst / S_kink
print(f"  S_inst / S_kink = 27*pi^2 / (36*pi) = 3*pi/4 = {3*math.pi/4:.6f}")
print(f"    (check: {ratio_inst_kink:.6f})")
print(f"    Note: 3*pi/4 ≈ {3*math.pi/4:.4f} — close to nothing obvious")
print()

# The cosmological constant exponent involves S_inst + S_inst*delta_d + alpha
delta_d = 1.0 / (6 * math.pi)
cosmo_exp = S_inst + S_inst * delta_d + alpha
print(f"  Cosmological exponent = S_inst*(1+delta_d) + alpha")
print(f"    = 27*pi^2 + 9*pi/2 + 18^(1/3) = {cosmo_exp:.4f}")
print(f"    Observed: 283.09")
print(f"    Error: {(cosmo_exp/283.09 - 1)*100:+.3f}%")
print()

# Product: I_4 * Q_top * N_Hopf
prod_iqn = float(I4) * Q_top * N_Hopf
print(f"  I_4 * Q_top * N_Hopf = (4/3)*2*9 = {prod_iqn:.1f}")
print(f"    = 24 = 4! (factorial)")
print(f"    Interesting: the product of the three key DFC integers is 4!")
print()

# What about I_4 * Q_top = 8/3
print(f"  I_4 * Q_top = {float(I4)*Q_top:.6f} = 8/3")
print(f"  I_4 + Q_top = {float(I4)+Q_top:.6f} = 10/3")
print(f"  I_4^Q_top = (4/3)^2 = {float(I4)**Q_top:.6f} = 16/9")
print(f"  Q_top^I_4 = 2^(4/3) = {Q_top**float(I4):.6f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 3: Continued fraction representations
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 3: Continued Fraction Representations")
print("=" * 76)
print()

def continued_fraction(x, n_terms=10):
    """Return the continued fraction coefficients of x."""
    coeffs = []
    for _ in range(n_terms):
        a = int(math.floor(x))
        coeffs.append(a)
        frac = x - a
        if abs(frac) < 1e-12:
            break
        x = 1.0 / frac
    return coeffs

values = {
    "alpha = 18^(1/3)": alpha,
    "1/alpha_em(0) = 137.036": 137.036,
    "g_eff = sqrt(8/27)": math.sqrt(float(g_eff_sq)),
    "S_kink/(2*pi) = 18": 18.0,
    "kappa = 5.33": kappa,
    "xi = sqrt(2/alpha)": xi,
    "phi_0": phi_0,
    "E_kink/M_Pl": E_kink,
    "S_inst = 27*pi^2": S_inst,
    "delta_d = 1/(6*pi)": delta_d,
}

for name, val in values.items():
    cf = continued_fraction(val)
    print(f"  {name} = {val:.6f}")
    print(f"    CF = {cf}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 4: Exponential and logarithmic transformations
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 4: Exponential/Log Transformations")
print("=" * 76)
print()

# What does exp(-alpha) give?
print(f"  exp(-alpha) = exp(-18^(1/3)) = {math.exp(-alpha):.8f}")
print(f"  exp(-I_4) = exp(-4/3) = {math.exp(-float(I4)):.8f}")
print(f"  exp(-Q_top) = exp(-2) = {math.exp(-Q_top):.8f}")
print(f"  exp(-pi*alpha) = {math.exp(-math.pi*alpha):.8f}")
print()

# Logarithmic combinations
print(f"  ln(alpha) = ln(18^(1/3)) = ln(18)/3 = {math.log(alpha):.8f}")
print(f"  ln(S_kink) = ln(36*pi) = {math.log(S_kink):.8f}")
print(f"  ln(1/alpha_em(0)) = ln(137.036) = {math.log(137.036):.8f}")
print(f"  ln(S_kink) - ln(1/alpha_em) = {math.log(S_kink) - math.log(137.036):.8f}")
print(f"    = ln(36*pi/137.036) = ln({36*math.pi/137.036:.6f})")
print()

# The ECCC identity: exp(t7 - t5) ≈ 137
# What about exp(ln(S_kink) - ln(something))?
print(f"  S_kink / (1/alpha_em) = 36*pi / 137.036 = {36*math.pi/137.036:.6f}")
print(f"    ≈ {36*math.pi/137.036:.4f} — close to nothing simple")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 5: Mass ratios from DFC parameters
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 5: Mass Ratios and Generation Scaling")
print("=" * 76)
print()

# The inter-generation mass ratio kappa = 5.33
# Can we express this in terms of DFC parameters?
print(f"  kappa = {kappa}")
print(f"  Candidates:")
print(f"    I_4 * Q_top * 2 = {float(I4)*Q_top*2:.4f}")
print(f"    alpha * 2 = {alpha*2:.4f}")
print(f"    N_Hopf / sqrt(alpha) = {N_Hopf/math.sqrt(alpha):.4f}")
print(f"    4*I_4 = {4*float(I4):.4f}")
print(f"    pi * sqrt(alpha) = {math.pi*math.sqrt(alpha):.4f}")
print(f"    exp(I_4) + 1 = {math.exp(float(I4))+1:.4f}")
print(f"    2*alpha = {2*alpha:.4f}")
print(f"    N_Hopf * beta * pi = {N_Hopf*beta_f*math.pi:.4f} (= 1)")
print(f"    alpha^2 / (phi_0/xi) = ... ")
print()

# Exact: kappa = exp(I_4 * something)?
# ln(kappa) = 1.6734
ln_kappa = math.log(kappa)
print(f"  ln(kappa) = {ln_kappa:.6f}")
print(f"    I_4 = {float(I4):.6f}  (ratio: {ln_kappa/float(I4):.6f})")
print(f"    I_4 * ln(kappa)/I_4 = ... not clean")
print(f"    pi/2 = {math.pi/2:.6f}  (ratio: {ln_kappa/(math.pi/2):.6f})")
print(f"    sqrt(alpha) = {math.sqrt(alpha):.6f}  (ratio: {ln_kappa/math.sqrt(alpha):.6f})")
print(f"    1/(delta_d * 2*pi) = {1/(delta_d*2*math.pi):.6f}  (= 3, ratio: {ln_kappa/3:.6f})")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 6: Modular arithmetic and number theory
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 6: Number Theory of DFC Integers")
print("=" * 76)
print()

# The key DFC integers: N_c=3, N_Hopf=9, Q_top=2, b_0=11
# And from I_4 = 4/3: numerator 4, denominator 3
# From g_eff^2 = 8/27: numerator 8, denominator 27

print("  Key integers appearing in DFC:")
print(f"    N_c = 3 (prime)")
print(f"    N_Hopf = 9 = 3^2")
print(f"    Q_top = 2 (prime)")
print(f"    b_0 = 11 (prime)")
print(f"    S_kink/(2*pi) = 18 = 2 * 3^2")
print(f"    I_4 num/den = 4/3 = 2^2/3")
print(f"    g_eff^2 num/den = 8/27 = 2^3/3^3")
print(f"    beta_lat = 81/4 = 3^4/2^2")
print()

# Pattern: everything is built from powers of 2 and 3!
print("  OBSERVATION: All key DFC integers factor into powers of 2 and 3 only.")
print("  The only primes appearing in DFC numerics are {2, 3}.")
print(f"    Exception: b_0 = 11 (= 11, a prime not 2 or 3)")
print(f"    But b_0 = 11*N_c/3 - 2*N_f/3 = 11 for N_f=0, N_c=3")
print(f"    11 = 3^2 + 2 = 9 + 2 = N_Hopf + Q_top")
print(f"    (check: {N_Hopf + Q_top})")
print()

print("  So b_0 = N_Hopf + Q_top = 9 + 2 = 11.  This is EXACT.")
print(f"    b_0 = 11*N_c/3 = 11 for N_c=3 and N_f=0")
print(f"    But also b_0 = N_c^2 + Q_top = 9 + 2 = 11")
print(f"    Is this a coincidence or structural?")
print()

# Check: for general N_c, is b_0(pure YM) = N_c^2 + Q_top(N_c)?
# b_0(pure YM) = 11*N_c/3; Q_top(N_c) = I_4(N_c) * N_c/2
# I_4 = C_2(fund) = (N_c^2-1)/(2*N_c)
# Q_top(N_c) = (N_c^2-1)/(2*N_c) * N_c/2 = (N_c^2-1)/4
# So b_0 = N_c^2 + (N_c^2-1)/4 = (5*N_c^2-1)/4
# But b_0 = 11*N_c/3
# (5*N_c^2-1)/4 = 11*N_c/3 → 15*N_c^2 - 3 = 44*N_c → 15*N_c^2 - 44*N_c - 3 = 0
# discriminant = 1936 + 180 = 2116 = 46^2; N_c = (44+46)/30 = 3
# So b_0 = N_c^2 + Q_top is UNIQUE TO N_c = 3!

disc = 44**2 + 4*15*3
print(f"  Solving b_0 = N_c^2 + Q_top for general N_c:")
print(f"    15*N_c^2 - 44*N_c - 3 = 0")
print(f"    discriminant = {disc} = {int(math.sqrt(disc))}^2 (perfect square!)")
print(f"    N_c = (44 + 46) / 30 = {(44+46)/30:.1f}")
print(f"    N_c = 3 is the UNIQUE positive integer solution.")
print()
print("  *** FINDING: b_0 = N_c^2 + Q_top is a new identity unique to N_c = 3 ***")
print("  *** This connects asymptotic freedom (b_0) to topology (Q_top, N_Hopf). ***")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 7: Trigonometric identities with DFC angles
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 7: DFC Angles and Trigonometry")
print("=" * 76)
print()

# Z_3 center: z = exp(2*pi*i/3), angle = 2*pi/3 = 120 degrees
# Weinberg angle: sin^2(theta_W) = 3/8 at M_c
# theta_W(M_c) = arcsin(sqrt(3/8))

theta_W_Mc = math.asin(math.sqrt(3/8))
print(f"  Weinberg angle at M_c: theta_W = {math.degrees(theta_W_Mc):.4f} degrees")
print(f"    sin^2(theta_W) = 3/8 = {3/8}")
print(f"    cos^2(theta_W) = 5/8 = {5/8}")
print(f"    tan^2(theta_W) = 3/5 = {3/5}")
print(f"    theta_W = {theta_W_Mc:.6f} rad = {math.degrees(theta_W_Mc):.4f} deg")
print()

# Z_3 angle
z3_angle = 2 * math.pi / 3
print(f"  Z_3 center angle: 2*pi/3 = {math.degrees(z3_angle):.1f} degrees")
print(f"    cos(2*pi/3) = {math.cos(z3_angle):.6f} = -1/2")
print(f"    1 - cos(2*pi/3) = {1 - math.cos(z3_angle):.6f} = 3/2 = N_c/2")
print(f"    This IS the vortex factor [T1, C221]")
print()

# Ratio of angles
print(f"  theta_W / (2*pi/3) = {theta_W_Mc/z3_angle:.6f}")
print(f"  (2*pi/3) / theta_W = {z3_angle/theta_W_Mc:.6f}")
print(f"  theta_23(obs) = 49.1 degrees = {math.radians(49.1):.6f} rad")
print(f"  theta_23 / theta_W(M_c) = {49.1/math.degrees(theta_W_Mc):.6f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 8: Dimensional analysis — what ratios are "natural"?
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 8: Natural Ratios from V(phi)")
print("=" * 76)
print()

# V(phi) has exactly two parameters: alpha, beta.
# All DFC physics comes from ratios of these plus topology.
# What dimensionless ratios can we form?

print(f"  alpha/beta = phi_0^2 = {alpha/beta_f:.4f}")
print(f"  sqrt(alpha*beta) = {math.sqrt(alpha*beta_f):.8f}")
print(f"    = sqrt(18^(1/3)/(9*pi)) = {math.sqrt(alpha/(9*math.pi)):.8f}")
print(f"  alpha^(3/2)/beta = E_kink * sqrt(2) * (3/4) = {alpha**1.5/beta_f:.4f}")
print(f"    = S_kink * sqrt(2*alpha)/4? No... S_kink = 4/beta = {4/beta_f:.4f}")
print()

# The kink energy in terms of alpha alone (using beta = 1/(9*pi)):
# E_kink = (4/3) * phi_0^3 * beta * sqrt(2) ... let's be precise
# E_kink = (4/(3*sqrt(2))) * alpha^(3/2) / beta
E_check = (4/(3*math.sqrt(2))) * alpha**(1.5) / beta_f
print(f"  E_kink check: {E_check:.4f} (should be {E_kink:.4f})")
print(f"  Actually E_kink = S_kink = 4/beta for static kink where E=S")
print(f"  E_kink = 4/beta = {4/beta_f:.4f} = 36*pi = {36*math.pi:.4f}")
print()

# Interesting: alpha is determined by S_kink * alpha_em = 1
# So alpha = (S_kink^2 * beta / 4)^(1/3)... let's verify
# S_kink = 4/beta, alpha_em = beta/4
# S_kink * alpha_em = (4/beta)(beta/4) = 1 always (tautology for any beta)
# alpha enters through BPS: E_kink = S_kink requires alpha = (3*sqrt(2)*beta*S/4)^(2/3)
# With S = 4/beta: alpha = (3*sqrt(2)*beta*(4/beta)/4)^(2/3) = (3*sqrt(2))^(2/3) = 18^(1/3)
print(f"  BPS check: (3*sqrt(2))^(2/3) = {(3*math.sqrt(2))**(2/3):.8f}")
print(f"  alpha = 18^(1/3) = {18**(1/3):.8f}")
print(f"  Match: {abs((3*math.sqrt(2))**(2/3) - 18**(1/3)) < 1e-14}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 9: The 24 = 4! observation
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 9: Why 24?")
print("=" * 76)
print()

# I_4 * Q_top * N_Hopf = (4/3) * 2 * 9 = 24 = 4!
# Is this related to anything known?

print(f"  I_4 * Q_top * N_Hopf = {float(I4) * Q_top * N_Hopf:.0f} = 4!")
print()
print("  Known appearances of 24 in math/physics:")
print("    - 24 = 4! (permutations of 4 objects)")
print("    - Ramanujan: 1+2+3+...= -1/12, and 24 * (-1/12) = -2")
print("    - 24-cell: unique self-dual regular 4D polytope (24 octahedral cells)")
print("    - Leech lattice: 24 dimensions")
print("    - Modular forms: weight 12 cusp form, dim = 1; Ramanujan tau")
print("    - String theory: bosonic string requires 24+2=26 dimensions")
print("    - 2nd Bernoulli number: B_2 = 1/6, and 24 * B_2 = 4")
print()

# In DFC: 24 = I_4 * Q_top * N_Hopf = C_2 * (winding) * (sphere count)
# = (4/3) * 2 * 9 = (4/3) * 18 = 4 * 18 / 3 = 4 * 6 = 24
# Also: 24 = 4 * N_c! = 4 * 6  (for N_c = 3)
# Or: 24 = 8 * N_c = 8 * 3 (where 8 = dim SU(3))
# Or: 24 = 2 * 12 = Q_top * (dim SU(3) - dim SU(2)) ... no, 12 ≠ 8-3=5

# Most natural: 24 = 4 * 3! = 4 * 6 = (I_4 numerator) * N_c!
print(f"  24 = 4 * N_c! = 4 * 6 = (I_4 numerator) * (N_c factorial)")
print(f"  24 = 8 * N_c = (dim SU(3)) * N_c")
print(f"     dim SU(3) = N_c^2 - 1 = 8")
print(f"     8 * 3 = 24 ✓")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 10: The instanton action and cosmological constant
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 10: Decomposing the Cosmological Exponent")
print("=" * 76)
print()

# rho_Lambda = M_Pl^4 * exp(-(27*pi^2 + 9*pi/2 + 18^(1/3)))
# = M_Pl^4 * exp(-S_inst) * exp(-S_inst*delta_d) * exp(-alpha)
#
# Can we write the total exponent differently?

total_exp = 27*math.pi**2 + 9*math.pi/2 + alpha
print(f"  Total exponent = {total_exp:.6f}")
print(f"    Term 1: 27*pi^2 = {27*math.pi**2:.6f}  ({27*math.pi**2/total_exp*100:.2f}%)")
print(f"    Term 2: 9*pi/2 = {9*math.pi/2:.6f}  ({9*math.pi/2/total_exp*100:.2f}%)")
print(f"    Term 3: alpha = {alpha:.6f}  ({alpha/total_exp*100:.2f}%)")
print()

# Can we write this as a single expression?
# 27*pi^2 + 9*pi/2 + 18^(1/3)
# = 27*pi^2(1 + 1/(6*pi) + 18^(1/3)/(27*pi^2))
# = S_inst(1 + delta_d + alpha/S_inst)
ratio_alpha_Sinst = alpha / S_inst
print(f"  alpha / S_inst = {ratio_alpha_Sinst:.8f}")
print(f"  delta_d = {delta_d:.8f}")
print(f"  delta_d / (alpha/S_inst) = {delta_d/ratio_alpha_Sinst:.4f}")
print(f"    ≈ {delta_d/ratio_alpha_Sinst:.2f} — not a clean ratio")
print()

# What if we write total = pi * (27*pi + 9/2) + alpha?
alt1 = math.pi * (27*math.pi + 4.5) + alpha
print(f"  pi*(27*pi + 9/2) + alpha = {alt1:.6f}  (same: {abs(alt1-total_exp)<1e-10})")
print()

# Factor 9 out: 9*(3*pi^2 + pi/2) + alpha
alt2 = 9*(3*math.pi**2 + math.pi/2) + alpha
print(f"  9*(3*pi^2 + pi/2) + alpha = {alt2:.6f}  (same: {abs(alt2-total_exp)<1e-10})")
print(f"  = 9*pi*(3*pi + 1/2) + alpha")
print(f"  = N_Hopf * pi * (3*pi + 1/2) + alpha")
print()

print("  Summary: The cosmological exponent 283.24 = 9*pi*(3*pi + 1/2) + 18^(1/3)")
print("  All three terms trace to {N_Hopf, pi, alpha} — substrate topology + curvature.")
print()

# ═══════════════════════════════════════════════════════════════════════════
# SUMMARY OF FINDINGS
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("SUMMARY OF POTENTIALLY INTERESTING FINDINGS")
print("=" * 76)
print()
print("  1. All key DFC fractions factor into {2, 3} only (primes 2 and 3).")
print("  2. b_0 = N_c^2 + Q_top = 11 is UNIQUE to N_c = 3 (discriminant = 46^2).")
print("     This connects asymptotic freedom to DFC topology.")
print("  3. I_4 * Q_top * N_Hopf = 24 = 4! — the product of the three key")
print("     topological integers equals the 4th factorial.")
print("  4. xi * phi_0 = sqrt(18*pi) — the amplitude-width product is determined")
print("     by alpha and beta together through a single square root.")
print("  5. (3*sqrt(2))^(2/3) = 18^(1/3) = alpha — the BPS saturation condition")
print("     that fixes alpha involves only the integers 2 and 3.")
print("  6. The cosmological exponent = N_Hopf * pi * (3*pi + 1/2) + alpha.")
print()
print("  Flagged for follow-up:")
print("    - b_0 = N_c^2 + Q_top uniqueness → new equation module?")
print("    - 24 = 4! product → any connection to 4D or polytope structure?")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 11: Diophantine structure — integer equations from DFC
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 11: Diophantine Structure of DFC")
print("=" * 76)
print()

# DFC produces several integer relations. Let's catalog them and look for
# Diophantine equations (polynomial equations with integer solutions).

# Equation 1: N_c^2 = N_Hopf (sphere count = color number squared)
# Equation 2: Q_top = I_4 * N_c / 2 = (N_c^2 - 1) / 4
# Equation 3: b_0(pure YM) = 11*N_c/3
# Equation 4: b_0 = N_c^2 + Q_top (unique to N_c = 3)
# Equation 5: dim(SU(N_c)) = N_c^2 - 1

# From Eq 2: Q_top = (N_c^2 - 1)/4. For Q_top to be integer, need N_c odd.
# N_c = 1: Q_top = 0 (trivial)
# N_c = 3: Q_top = 2
# N_c = 5: Q_top = 6
# N_c = 7: Q_top = 12

print("  Q_top(N_c) = (N_c^2 - 1)/4 for odd N_c:")
for Nc in [1, 3, 5, 7, 9, 11]:
    if Nc % 2 == 1:
        Qt = (Nc**2 - 1) // 4
        b0_ym = Fraction(11 * Nc, 3)
        Nh = Nc**2
        product = Fraction(Nc**2 - 1, 2*Nc) * Qt * Nh
        test = Nh + Qt
        b0_check = Fraction(11*Nc, 3)
        print(f"    N_c={Nc}: Q_top={Qt}, N_Hopf={Nh}, b_0={float(b0_ym):.2f}, "
              f"N_c^2+Q_top={test}, b_0={float(b0_check):.2f}, match={abs(test-float(b0_check))<0.01}")
print()

# NEW: Can we find a Diophantine equation that ONLY N_c=3 satisfies
# among all positive integers?
# From C306: C_2(fund,SU(n)) = (n^2-1)/(2n) = 4/3 → 3n^2 - 8n - 3 = 0
# discriminant = 64 + 36 = 100 = 10^2; n = (8+10)/6 = 3
# This is the CASCADE uniqueness. Let's look for MORE such equations.

# New Diophantine: N_Hopf = N_c^2 AND Q_top = (N_c^2-1)/4 AND b_0 = N_c^2 + Q_top
# Substituting: b_0 = N_c^2 + (N_c^2-1)/4 = (5*N_c^2 - 1)/4
# Also b_0 = 11*N_c/3
# So: (5*N_c^2 - 1)/4 = 11*N_c/3 → 15*N_c^2 - 44*N_c - 3 = 0
# Already found: disc = 2116 = 46^2, N_c = 3 unique.

# Another: what if we require I_4 * Q_top to be integer?
# I_4 * Q_top = (N_c^2-1)/(2*N_c) * (N_c^2-1)/4 = (N_c^2-1)^2 / (8*N_c)
# For N_c=3: (8)^2/(24) = 64/24 = 8/3 (NOT integer)
# For it to be integer: 8*N_c | (N_c^2-1)^2

# Instead: require I_4 * Q_top * N_Hopf to be integer (= 24 for N_c=3)
# I_4 * Q_top * N_Hopf = (N_c^2-1)/(2*N_c) * (N_c^2-1)/4 * N_c^2
#                       = N_c * (N_c^2-1)^2 / 8
print("  I_4 * Q_top * N_Hopf = N_c*(N_c^2-1)^2/8 for general N_c:")
for Nc in range(1, 12):
    val = Fraction(Nc * (Nc**2 - 1)**2, 8)
    is_int = val.denominator == 1
    fac_str = ""
    if is_int:
        v = int(val)
        # Check if it's a factorial
        for k in range(1, 15):
            if v == math.factorial(k):
                fac_str = f" = {k}!"
                break
    print(f"    N_c={Nc:2d}: {float(val):10.2f}  integer={is_int}  "
          f"{'= '+str(int(val)) if is_int else ''}{fac_str}")
print()

# KEY: N_c=3 gives 24 = 4!, the ONLY factorial in the sequence!
print("  *** FINDING: N_c=3 is the ONLY value where I_4*Q_top*N_Hopf is a factorial. ***")
print("  *** 24 = 4! appears uniquely at N_c=3. ***")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 12: Pell equations and quadratic irrationals from DFC
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 12: Quadratic Irrationals in DFC")
print("=" * 76)
print()

# alpha = 18^(1/3) is a CUBIC irrational (not quadratic).
# But several DFC quantities involve QUADRATIC irrationals:
# sqrt(2), sqrt(3), sqrt(alpha) = 18^(1/6) = (2*3^2)^(1/6) = 2^(1/6)*3^(1/3)

# The Weinberg angle involves sqrt(3/8) and sqrt(5/8).
# The vortex factor involves sqrt(3).
# Let's look at the minimal polynomials.

print("  Minimal polynomials of DFC irrationals:")
print()
print("  alpha = 18^(1/3):  x^3 - 18 = 0  (degree 3, cubic)")
print(f"    alpha = {alpha:.8f}")
print(f"    alpha^3 - 18 = {alpha**3 - 18:.2e}")
print()

# sqrt(alpha) = 18^(1/6): x^6 - 18 = 0 (degree 6)
sqrt_alpha = math.sqrt(alpha)
print(f"  sqrt(alpha) = 18^(1/6):  x^6 - 18 = 0  (degree 6)")
print(f"    sqrt(alpha) = {sqrt_alpha:.8f}")
print(f"    sqrt(alpha)^6 - 18 = {sqrt_alpha**6 - 18:.2e}")
print()

# xi = sqrt(2/alpha) = sqrt(2) * alpha^(-1/2) = sqrt(2) * 18^(-1/6)
# xi^6 = 8/18 = 4/9 → 9*xi^6 - 4 = 0 (degree 6)
print(f"  xi = sqrt(2/alpha):  9*x^6 - 4 = 0  (degree 6)")
print(f"    xi = {xi:.8f}")
print(f"    9*xi^6 - 4 = {9*xi**6 - 4:.2e}")
print()

# phi_0 = sqrt(alpha/beta) = sqrt(alpha * 9*pi)
# Not algebraic (involves pi). But phi_0^2/pi = 9*alpha = 9*18^(1/3)
print(f"  phi_0^2 / pi = 9*alpha = {phi_0**2/math.pi:.6f}")
print(f"    = 9*18^(1/3) = {9*alpha:.6f}")
print(f"    = (phi_0/sqrt(pi))^2 ... phi_0 involves pi, so transcendental")
print()

# Key finding: alpha is the SIMPLEST DFC irrational — cubic with minimal
# polynomial x^3 = 18. The Galois group is S_3 (degree 3 irreducible over Q).
# This is the same group as the permutation group of 3 objects = N_c objects!
print("  *** OBSERVATION: The minimal polynomial of alpha has degree 3 = N_c. ***")
print("  *** Its Galois group is S_3 = permutation group of N_c objects. ***")
print("  *** alpha's algebraic structure mirrors the number of colors. ***")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 13: Bernoulli numbers and DFC sums
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 13: Bernoulli Numbers and Zeta Values")
print("=" * 76)
print()

# The instanton action S_inst = 27*pi^2 involves pi^2.
# pi^2 = 6*zeta(2) where zeta(2) = sum(1/n^2) = pi^2/6.
# So S_inst = 27 * 6 * zeta(2) = 162 * zeta(2).

print(f"  S_inst = 27*pi^2 = 162 * zeta(2) = {162 * math.pi**2/6:.6f}")
print(f"    check: {27*math.pi**2:.6f}")
print(f"    162 = 2 * 81 = 2 * 3^4 = 2 * N_Hopf^2")
print()

# Also: S_inst = 8*pi^2/g_eff^2 = 8*pi^2 * 27/8 = 27*pi^2.
# The "8" cancels! S_inst = (N_Hopf * pi)^2 / N_c = 81*pi^2/3 = 27*pi^2.
# Hmm, that's N_Hopf^2 * pi^2 / N_c.

S_inst_check = N_Hopf**2 * math.pi**2 / 3
print(f"  S_inst = N_Hopf^2 * pi^2 / N_c = {S_inst_check:.6f}")
print(f"    = {N_Hopf}^2 * pi^2 / 3 = 81*pi^2/3 = 27*pi^2 ✓")
print()

# Bernoulli connection: B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, ...
# zeta(2k) = (-1)^(k+1) * (2*pi)^(2k) * B_{2k} / (2 * (2k)!)
# S_inst / pi^2 = 27 = 3^3 = N_c^3

print(f"  S_inst / pi^2 = 27 = N_c^3 = 3^3")
print(f"  S_kink / pi = 36 = 4 * 9 = 4 * N_Hopf = 4 * N_c^2")
print(f"  Cosmological exponent / pi = {total_exp/math.pi:.6f}")
print(f"    = 27*pi + 9/2 + alpha/pi = {27*math.pi + 4.5 + alpha/math.pi:.6f}")
print()

# Summarize the pi-free parts:
print("  Pi-free skeleton of DFC constants:")
print(f"    S_inst/pi^2 = {27}  (= N_c^3)")
print(f"    S_kink/pi   = {36}  (= 4*N_c^2)")
print(f"    delta_d*2*pi = 1/3  (= 1/N_c)")
print(f"    g_eff^2 = {Fraction(8,27)}  (= 8/N_c^3)")
print(f"    beta_lat = {Fraction(81,4)}  (= N_c^4/4)")
print()
print("  *** FINDING: Removing factors of pi, every DFC constant is a ***")
print("  *** rational power of N_c=3 times a small integer. ***")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 14: The {2,3} prime structure — deeper analysis
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 14: The {2,3} Prime Structure — Complete Census")
print("=" * 76)
print()

# Catalog EVERY numerical DFC parameter and its prime factorization.
# Separate the pi-dependence (transcendental) from the rational part.

params = [
    ("I_4", Fraction(4, 3), "kink shape integral"),
    ("g_eff^2", Fraction(8, 27), "effective gauge coupling squared"),
    ("Q_top", Fraction(2, 1), "topological charge"),
    ("N_Hopf", Fraction(9, 1), "Hopf sphere count"),
    ("N_c", Fraction(3, 1), "number of colors"),
    ("b_0(N_f=0)", Fraction(11, 1), "AF coefficient (pure YM)"),  # 11 is a new prime!
    ("b_1(N_f=0)", Fraction(102, 1), "2-loop AF (= 2*3*17)"),   # 17 is also new
    ("beta_lat", Fraction(81, 4), "lattice coupling"),
    ("kappa_DFC", Fraction(1, 2), "DFC→YM action map"),
    ("S_kink/pi", Fraction(36, 1), "kink action / pi"),
    ("S_inst/pi^2", Fraction(27, 1), "instanton action / pi^2"),
    ("delta_d * 6*pi", Fraction(1, 1), "depth correction * 6*pi"),
    ("C_2(fund)", Fraction(4, 3), "fundamental Casimir"),
    ("C_2(adj)", Fraction(3, 1), "adjoint Casimir"),
    ("k_Y^2", Fraction(5, 3), "hypercharge normalization"),  # 5 is new!
    ("sin^2(theta_W) at M_c", Fraction(3, 8), "Weinberg angle squared"),
    ("dim(SU(3))", Fraction(8, 1), "Lie algebra dimension"),
    ("1/alpha_em(M_c) / pi", Fraction(36, 1), "= S_kink/pi"),
    ("a_pair/f_pi", Fraction(1, 8), "pairing/pion ratio (N_c^2-1)^-1"),
]

# Count which primes appear
from collections import Counter

def prime_factors(n):
    """Return prime factorization of positive integer n."""
    if n <= 1:
        return {}
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

prime_census = Counter()
non_23_params = []

for name, val, desc in params:
    num = abs(val.numerator)
    den = abs(val.denominator)
    num_f = prime_factors(num) if num > 1 else {}
    den_f = prime_factors(den) if den > 1 else {}
    all_primes = set(num_f.keys()) | set(den_f.keys())
    prime_census.update(all_primes)

    has_other = any(p not in {2, 3} for p in all_primes)
    status = "  *** OTHER PRIMES ***" if has_other else ""
    if has_other:
        non_23_params.append((name, val, all_primes - {2, 3}))

    print(f"  {name:25s} = {str(val):10s}  num={num_f}  den={den_f}{status}")

print()
print(f"  Prime census across all parameters: {dict(prime_census)}")
print()

if non_23_params:
    print("  Parameters with primes beyond {2, 3}:")
    for name, val, other_p in non_23_params:
        print(f"    {name} = {val}  extra primes: {other_p}")
    print()
    print("  INTERPRETATION: b_0=11 introduces the prime 11, b_1=102=2*3*17 introduces 17,")
    print("  and k_Y^2=5/3 introduces the prime 5. These are the ONLY exceptions.")
    print("  b_0 and b_1 come from QFT beta function (loop structure).")
    print("  k_Y^2 = 5/3 comes from the SM fermion hypercharge assignments.")
    print("  The {2,3}-only parameters are the TOPOLOGICAL ones (I_4, Q_top, N_Hopf,")
    print("  g_eff^2, beta_lat, S_kink). The non-{2,3} primes enter through DYNAMICS.")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 15: Power towers and iterated exponentials
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 15: Nested Exponentials and Self-Reference")
print("=" * 76)
print()

# DFC has a self-referential structure: the substrate describes itself.
# Does this show up in iterated operations?

# exp(exp(-S_inst)) — the double-exponential of the instanton action
double_exp = math.exp(-S_inst)
print(f"  exp(-S_inst) = exp(-27*pi^2) = {double_exp:.4e}")
print(f"    ≈ 10^(-{-math.log10(double_exp):.1f})")
print(f"  This is the instanton fugacity — essentially zero.")
print()

# What about the tower: alpha, alpha^alpha, alpha^(alpha^alpha)?
print(f"  Power tower of alpha = 18^(1/3) = {alpha:.4f}:")
a1 = alpha
a2 = alpha**alpha
a3 = alpha**(alpha**alpha)
print(f"    alpha = {a1:.6f}")
print(f"    alpha^alpha = {a2:.6f}")
print(f"    alpha^(alpha^alpha) = {a3:.6f}")
print(f"    Ratio a2/a1 = {a2/a1:.6f}")
print(f"    Ratio a3/a2 = {a3/a2:.6f}")
print()

# Self-consistent equation: x = alpha^(1/x)?
# → x^x = alpha → x*ln(x) = ln(alpha) = ln(18)/3
# Solve numerically
from scipy.optimize import brentq

def self_eq(x):
    return x * math.log(x) - math.log(alpha)

try:
    x_sc = brentq(self_eq, 1.001, 10.0)
    print(f"  Self-consistent: x^x = alpha → x = {x_sc:.8f}")
    print(f"    Check: x^x = {x_sc**x_sc:.8f}, alpha = {alpha:.8f}")
    print(f"    x ≈ {x_sc:.4f} — not an obvious DFC parameter")
except Exception:
    print("  Self-consistent equation x^x = alpha: numerical solver unavailable")
print()

# Tetration-related: what integer n satisfies alpha^alpha^...^alpha (n times) ≈ some DFC constant?
# alpha↑↑2 = alpha^alpha ≈ 15.0 (close to 15.8 = a_V, but not exact)
print(f"  alpha↑↑2 = alpha^alpha = {a2:.4f}")
print(f"    Close to a_V(nuclear volume) ≈ 15.8 MeV? Ratio = {a2/15.8:.4f} — no.")
print(f"    Close to 4*I_4*pi = {4*float(I4)*math.pi:.4f}? Ratio = {a2/(4*float(I4)*math.pi):.4f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 16: DFC determinant — the "characteristic matrix"
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 16: DFC Characteristic Matrix")
print("=" * 76)
print()

# Arrange the 4 key DFC topological parameters into a 2x2 matrix:
#   M = [[I_4, Q_top], [N_c, N_Hopf]] = [[4/3, 2], [3, 9]]
# What is its determinant, trace, eigenvalues?

import numpy as np

M = np.array([[float(I4), float(Q_top)],
              [float(3), float(N_Hopf)]])

det_M = np.linalg.det(M)
tr_M = np.trace(M)
eigvals = np.linalg.eigvals(M)

print(f"  M = [[I_4, Q_top], [N_c, N_Hopf]] = [[4/3, 2], [3, 9]]")
print(f"  det(M) = I_4*N_Hopf - Q_top*N_c = (4/3)*9 - 2*3 = 12 - 6 = {det_M:.6f}")
print(f"  tr(M) = I_4 + N_Hopf = 4/3 + 9 = 31/3 = {tr_M:.6f}")
print(f"  Eigenvalues: {eigvals[0]:.6f}, {eigvals[1]:.6f}")
print(f"    lambda_1 * lambda_2 = det = {eigvals[0]*eigvals[1]:.6f}")
print()

# det = 6 exactly (with Fraction arithmetic)
det_exact = Fraction(4, 3) * 9 - 2 * 3
print(f"  det(M) exact = {det_exact} = {float(det_exact)}")
print(f"    = 6 = N_c! = 3! (the number of permutations of N_c objects)")
print()

# Alternative matrix: [[Q_top, I_4], [N_Hopf, N_c]] — transpose-swap
M2 = np.array([[float(Q_top), float(I4)],
               [float(N_Hopf), float(3)]])
det_M2 = np.linalg.det(M2)
print(f"  M' = [[Q_top, I_4], [N_Hopf, N_c]] det = {det_M2:.6f}")
print(f"    = Q_top*N_c - I_4*N_Hopf = 6 - 12 = -6 = -N_c!")
print()

# 3x3 matrix with b_0
M3 = np.array([[float(I4), float(Q_top), 0],
               [0, float(3), float(N_Hopf)],
               [1, 0, float(11)]])
det_M3 = np.linalg.det(M3)
print(f"  3x3: [[I_4, Q_top, 0], [0, N_c, N_Hopf], [1, 0, b_0]]")
print(f"  det = {det_M3:.4f}")
# I_4*(3*11 - 0) - Q_top*(0 - 9) + 0 = I_4*33 + Q_top*9 = 44 + 18 = 62
print(f"    = I_4*33 + Q_top*9 = {float(I4)*33 + Q_top*9:.4f}")
print()

print("  *** FINDING: det([[I_4, Q_top], [N_c, N_Hopf]]) = 6 = N_c! = 3! ***")
print("  *** The determinant of the DFC topological matrix equals ***")
print("  *** the number of permutations of N_c objects. ***")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 17: Euler's identity and DFC — the e^(i*pi) connection
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 17: DFC and Euler-Type Identities")
print("=" * 76)
print()

# Euler: e^(i*pi) + 1 = 0 connects {e, i, pi, 1, 0}.
# DFC: S_kink * alpha_em = 1 connects {S_kink, alpha_em}.
# Can we write a DFC identity connecting e, pi, and DFC parameters?

# We have: S_kink = 36*pi, alpha_em = 1/(36*pi)
# exp(-S_inst) = exp(-27*pi^2) ≈ 0 (essentially zero — like e^(i*pi)+1=0!)
# More precisely: rho_Lambda = exp(-(S_inst + S_inst*delta_d + alpha)) M_Pl^4

# DFC "Euler identity": exp(-S_inst) × M_Pl^4 ≈ 0 (to 116 orders of magnitude)
# The cosmological constant IS the DFC version of "approximately zero."

print("  Standard Euler: e^(i*pi) + 1 = 0")
print("  DFC analog: exp(-27*pi^2) ≈ 0  (to 116 decimal places)")
print(f"    exp(-S_inst) = {math.exp(-S_inst):.4e}")
print()

# More interesting: the DFC "Euler product"
# Product of e, pi, and all DFC topological integers:
euler_prod = math.e * math.pi * float(I4) * Q_top * N_Hopf
print(f"  e * pi * I_4 * Q_top * N_Hopf = e * pi * 24 = {euler_prod:.6f}")
print(f"    = 24*e*pi = {24*math.e*math.pi:.6f}")
print(f"    ≈ {euler_prod:.2f}")
print(f"    204.9 ≈ nothing obvious")
print()

# But: e * pi ≈ 8.54 ≈ 8.5 = 17/2 (near-miss)
# Not structurally interesting.

# What IS interesting: alpha^3 = 18 = 2*3^2 = 2*(e^1)^... no.
# The most interesting Euler-type identity in DFC is:
# S_kink * alpha_em = 1  [T1, exact, C171]
# This is the DFC "balance equation": kink action × electromagnetic coupling = unity.
print("  DFC balance identity: S_kink × alpha_em(M_c) = 1  [T1, C171]")
print("  In words: the kink action and the fine structure constant are reciprocals")
print("  of each other at the electromagnetic unification scale.")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 18: Partition function structure
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 18: Integer Partitions of DFC Numbers")
print("=" * 76)
print()

# How many ways can we partition key DFC integers?
# p(n) = number of partitions of n
def partition_count(n, max_val=None):
    """Count partitions of n using parts ≤ max_val."""
    if max_val is None:
        max_val = n
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, min(n, max_val) + 1):
        for j in range(k, n + 1):
            dp[j] += dp[j - k]
    return dp[n]

dfc_integers = {"Q_top": 2, "N_c": 3, "N_c!": 6, "dim(SU(3))": 8,
                "N_Hopf": 9, "b_0": 11, "alpha^3": 18, "4!": 24,
                "S_kink/pi": 36}

print("  Integer partitions p(n) of DFC integers:")
for name, n in dfc_integers.items():
    p = partition_count(n)
    print(f"    p({n:2d}) = {p:6d}  ({name})")
print()

# Partitions using only DFC primes {2, 3}
print("  Partitions using only parts from {2, 3} (DFC primes):")
for name, n in dfc_integers.items():
    # Count partitions of n using parts 2 and 3 only
    count = 0
    for n3 in range(n // 3 + 1):
        remainder = n - 3 * n3
        if remainder >= 0 and remainder % 2 == 0:
            count += 1
    print(f"    p_{{2,3}}({n:2d}) = {count:3d}  ({name})")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 19: Sum of DFC parameters = anything interesting?
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 19: Sums and Harmonic Means")
print("=" * 76)
print()

# Sum of the "topological quartet": I_4 + Q_top + N_c + N_Hopf
topo_sum = float(I4) + Q_top + 3 + N_Hopf
print(f"  I_4 + Q_top + N_c + N_Hopf = 4/3 + 2 + 3 + 9 = {topo_sum:.4f}")
print(f"    = 43/3 = {Fraction(4,3)+2+3+9}")
print()

# Harmonic mean
hm = 4 / (1/float(I4) + 1/Q_top + 1/3 + 1/N_Hopf)
print(f"  Harmonic mean of {{I_4, Q_top, N_c, N_Hopf}} = {hm:.6f}")
print(f"    = 4 / (3/4 + 1/2 + 1/3 + 1/9)")
denom = Fraction(3,4) + Fraction(1,2) + Fraction(1,3) + Fraction(1,9)
hm_exact = Fraction(4, 1) / denom
print(f"    = 4 / {denom} = {hm_exact} = {float(hm_exact):.6f}")
print()

# Geometric mean
gm = (float(I4) * Q_top * 3 * N_Hopf)**0.25
print(f"  Geometric mean of {{I_4, Q_top, N_c, N_Hopf}} = {gm:.6f}")
print(f"    = (4/3 * 2 * 3 * 9)^(1/4) = 24^(1/4) = (4!)^(1/4)")
print(f"    = {24**0.25:.6f}")
print(f"    ≈ {24**0.25:.4f} — close to alpha = {alpha:.4f}? Ratio = {24**0.25/alpha:.4f}")
print(f"    (4!)^(1/4) / alpha = {24**0.25/alpha:.6f} — not exact")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 20: Graph theory — DFC parameter network
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 20: DFC Identity Network")
print("=" * 76)
print()

# How many INDEPENDENT identities connect the key DFC parameters?
# List all known exact identities:
print("  Known exact (T1) identities among DFC parameters:")
print("    1. g_eff^2 = 2*I_4/N_Hopf = 8/27")
print("    2. Q_top = I_4*N_c/2 = 2")
print("    3. N_Hopf = N_c^2 = 9")
print("    4. b_0 = N_c^2 + Q_top = 11 (unique to N_c=3)")
print("    5. S_kink = 4/beta = 36*pi")
print("    6. S_inst = 8*pi^2/g_eff^2 = 27*pi^2")
print("    7. alpha^3 = 18 = 2*N_Hopf = 2*N_c^2")
print("    8. S_kink * alpha_em(M_c) = 1")
print("    9. beta_lat = 2*N_c/g_eff^2 = 81/4")
print("   10. 1/alpha_em(M_c) = 36*pi (= S_kink)")
print("   11. delta_d = 1/(6*pi) = (I_4-1)/(2*pi) = N_c/(N_Hopf*2*pi)")
print("   12. kappa_DFC = beta_lat*g_eff^2/(4*N_c) = 1/2")
print()

# Parameters: {alpha, beta, I_4, Q_top, N_c, N_Hopf, g_eff^2, b_0, S_kink, S_inst}
# That's 10 parameters with 12 identities.
# In principle, 10 params - 12 constraints = "overdetermined" by 2.
# But some identities are not independent.

# Independent count: N_c is the "base" parameter. Given N_c=3:
# N_Hopf = N_c^2 (from 3)
# I_4 = (N_c^2-1)/(2*N_c) (from definition, implied by C_2)
# Q_top = I_4*N_c/2 (from 2)
# g_eff^2 = 2*I_4/N_Hopf (from 1)
# b_0 = 11*N_c/3 (from QFT, identity 4 is then a CHECK)
# beta = 1/(9*pi) (from ECCC, T2a)
# alpha = 18^(1/3) (from BPS, T2a)
# S_kink = 4/beta (algebraic)
# S_inst = 8*pi^2/g_eff^2 (algebraic)

print("  Degrees of freedom analysis:")
print("    Given N_c = 3 (one integer), ALL topological parameters are fixed.")
print("    Given beta = 1/(9*pi) (one transcendental), ALL action-scale parameters are fixed.")
print("    Given alpha = 18^(1/3) (one algebraic), the potential shape is fixed.")
print("    Total: 3 inputs → all DFC parameters.")
print("    Of these, alpha = f(beta, BPS) reduces it to 2 independent inputs:")
print("      N_c = 3  and  beta = 1/(9*pi)")
print()
print("  *** FINDING: The entire DFC parameter space has dimension 2: ***")
print("  *** one integer (N_c = 3) and one coupling (beta = 1/(9*pi)). ***")
print("  *** Everything else is derived. ***")
print()

# ═══════════════════════════════════════════════════════════════════════════
# UPDATED SUMMARY
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("UPDATED SUMMARY OF FINDINGS (Explorations 1-20)")
print("=" * 76)
print()
print("  STRUCTURAL:")
print("  1. b_0 = N_c^2 + Q_top = 11 unique to N_c=3 [T1, C417]")
print("  2. I_4 * Q_top * N_Hopf = 24 = 4! unique factorial at N_c=3 [NEW]")
print("  3. det([[I_4, Q_top], [N_c, N_Hopf]]) = 6 = N_c! [NEW]")
print("  4. DFC parameter space has dimension 2: {N_c, beta} [NEW]")
print()
print("  NUMBER-THEORETIC:")
print("  5. All topological DFC parameters factor into primes {2, 3} only [C417]")
print("  6. Non-{2,3} primes enter only through dynamics: b_0=11, b_1→17, k_Y^2→5 [NEW]")
print("  7. alpha = 18^(1/3) has minimal polynomial degree N_c = 3 [NEW]")
print("  8. Pi-free skeleton: S/pi^k always yields N_c^j × small integer [NEW]")
print()
print("  ALGEBRAIC:")
print("  9. (3*sqrt(2))^(2/3) = 18^(1/3) = alpha [C417]")
print(" 10. Cosmological exponent = N_Hopf*pi*(3*pi+1/2) + alpha [C417]")
print(" 11. S_inst = N_Hopf^2 * pi^2 / N_c [NEW]")
print()
print("  Flagged for dedicated equation modules:")
print("    - Exploration 11: 4! uniqueness at N_c=3 (combinatorial proof)")
print("    - Exploration 14: {2,3} vs dynamic primes (structural vs loop)")
print("    - Exploration 16: det = N_c! (topological matrix)")
print("    - Exploration 20: parameter space dimension = 2")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 21: Eigenvalues of DFC matrices
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 21: Eigenvalues of DFC Matrices")
print("=" * 76)
print()

# The 2x2 topological matrix from Exploration 16
M_topo = np.array([[float(I4), float(Q_top)],
                   [float(3), float(N_Hopf)]])
eigenvalues = np.linalg.eigvals(M_topo)
eigenvalues = sorted(eigenvalues)
trace_M = float(I4) + N_Hopf  # = 4/3 + 9 = 31/3
det_M = 6.0  # = N_c!

print(f"  M = [[I_4, Q_top], [N_c, N_Hopf]] = [[4/3, 2], [3, 9]]")
print(f"  Trace = I_4 + N_Hopf = {trace_M:.6f} = {Fraction(4,3) + 9} = 31/3")
print(f"  Det = {det_M:.0f} = N_c! = 6")
print(f"  Eigenvalues: lambda_1 = {eigenvalues[0]:.6f}, lambda_2 = {eigenvalues[1]:.6f}")
print(f"  Characteristic polynomial: x^2 - (31/3)x + 6 = 0")
# Discriminant: (31/3)^2 - 4*6 = 961/9 - 24 = 961/9 - 216/9 = 745/9
disc = Fraction(31, 3)**2 - 4 * 6
print(f"  Discriminant = (31/3)^2 - 24 = {disc} = {float(disc):.6f}")
print(f"  sqrt(disc) = {math.sqrt(float(disc)):.6f}")
print(f"  lambda_1 = (31/3 - sqrt(745/9)) / 2 = {(31/3 - math.sqrt(745/9))/2:.6f}")
print(f"  lambda_2 = (31/3 + sqrt(745/9)) / 2 = {(31/3 + math.sqrt(745/9))/2:.6f}")
print(f"  lambda_1 * lambda_2 = {eigenvalues[0]*eigenvalues[1]:.6f} = 6 = N_c! ✓")
print(f"  lambda_1 + lambda_2 = {eigenvalues[0]+eigenvalues[1]:.6f} = 31/3 ✓")
print()

# 3x3 DFC matrix: rows = (I_4, Q_top, N_c), (N_c, N_Hopf, b_0), (Q_top, N_c, alpha^3)
M3_dfc = np.array([[float(I4), float(Q_top), float(3)],
                   [float(3), float(N_Hopf), float(11)],
                   [float(Q_top), float(3), float(18)]])
eig3 = sorted(np.linalg.eigvals(M3_dfc).real)
det3 = np.linalg.det(M3_dfc)
tr3 = float(I4) + N_Hopf + 18
print(f"  3x3 DFC matrix [[I_4,Q_top,N_c],[N_c,N_Hopf,b_0],[Q_top,N_c,alpha^3]]:")
print(f"  Trace = I_4 + N_Hopf + 18 = {tr3:.4f} = {Fraction(4,3)+9+18}")
print(f"  Det = {det3:.4f}")
det3_exact = (Fraction(4,3)*9*18 + 2*3*2 + 3*11*3
              - 3*9*3 - Fraction(4,3)*11*3 - 2*2*18)
print(f"  Det exact = {det3_exact} = {float(det3_exact):.4f}")
print(f"  Eigenvalues: {eig3[0]:.4f}, {eig3[1]:.4f}, {eig3[2]:.4f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 22: Catalan numbers and DFC
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 22: Catalan Numbers and DFC Parameters")
print("=" * 76)
print()

# C_n = (2n)! / ((n+1)! * n!)
# C_0=1, C_1=1, C_2=2, C_3=5, C_4=14, C_5=42, C_6=132, ...
catalan = [1, 1, 2, 5, 14, 42, 132, 429, 1430]
print("  Catalan numbers: C_0=1, C_1=1, C_2=2, C_3=5, C_4=14, C_5=42, ...")
print()

# Any DFC parameters match Catalan numbers?
print("  DFC integer matches with Catalan numbers:")
print(f"    Q_top = {Q_top} = C_2 ✓ (2nd Catalan number)")
print(f"    N_c! = 6: not a Catalan number")
print(f"    N_Hopf = 9: not a Catalan number")
print(f"    b_0 = 11: not a Catalan number")
print(f"    C_4 = 14: 14 = 2*7 — introduces prime 7, not DFC")
print(f"    C_5 = 42: 42 = 2*3*7 — introduces prime 7")
print()

# Catalan number C_n counts non-crossing partitions of {1,...,n+1}
# C_2 = 2 = Q_top: the number of non-crossing partitions of {1,2,3}
# (beyond the trivial partition)
# This counts: {{1,2,3}} and {{1},{2,3}},{{1,2},{3}},{{1,3},{2}} minus crossing
# Actually C_3 = 5, C_2 = 2
print("  C_2 = 2 = Q_top: non-crossing pairings of 4 points on a circle")
print("  Alternatively: Q_top = 2 is the number of Dyck paths of length 2")
print("  (1 up-step then 1 down-step: UD)")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 23: Fibonacci/Lucas connections
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 23: Fibonacci and Lucas Numbers")
print("=" * 76)
print()

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
lucas = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199]
print("  Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...")
print("  Lucas:     2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, ...")
print()

# Check DFC integers against these sequences
print("  DFC parameters in Fibonacci sequence:")
print(f"    Q_top = 2 = F_3 ✓")
print(f"    N_c = 3 = F_4 ✓")
print(f"    N_Hopf = 9: NOT Fibonacci")
print(f"    b_0 = 11: NOT Fibonacci")
print()

print("  DFC parameters in Lucas sequence:")
print(f"    Q_top = 2 = L_0 ✓")
print(f"    N_c = 3 = L_2 ✓")
print(f"    N_Hopf = 9: NOT Lucas")
print(f"    b_0 = 11 = L_5 ✓ (!)")
print(f"    alpha^3 = 18 = L_6 ✓ (!!)")
print()

print("  *** OBSERVATION: b_0=11 and alpha^3=18 are CONSECUTIVE Lucas numbers! ***")
print(f"    L_5 = 11, L_6 = 18, and L_5 + L_6 = L_7 = 29")
print(f"    b_0 + alpha^3 = 11 + 18 = 29 = L_7")
print()

# Is this a coincidence? Check:
# L_n = phi^n + (-phi)^{-n} where phi = (1+sqrt(5))/2
phi_gold = (1 + math.sqrt(5)) / 2
L5 = phi_gold**5 + (-phi_gold)**(-5)
L6 = phi_gold**6 + (-phi_gold)**(-6)
print(f"  Verification: L_5 = phi^5 + (-phi)^(-5) = {L5:.6f} ≈ 11 ✓")
print(f"  Verification: L_6 = phi^6 + (-phi)^(-6) = {L6:.6f} ≈ 18 ✓")
print()

# But note: 18 = 2*3^2 = 2*N_c^2 and 11 = N_c^2 + Q_top
# The Lucas property L_5 + L_6 = L_7 would imply:
# (N_c^2 + Q_top) + 2*N_c^2 = 3*N_c^2 + Q_top = 29
# For N_c=3: 27 + 2 = 29 ✓
# For N_c=4: 3*16 + (16-1)/(2*4)*4/2 ... this only works for N_c=3.
print("  Structural interpretation:")
print(f"    b_0 = N_c^2 + Q_top = 9 + 2 = 11")
print(f"    alpha^3 = 2*N_c^2 = 18")
print(f"    Sum = 3*N_c^2 + Q_top = 29 = L_7")
print(f"    This is a NUMERICAL COINCIDENCE — Lucas numbers are not derived from DFC.")
print(f"    But it's notable that two independent DFC quantities are consecutive Lucas.")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 24: Trigonometric values at DFC angles
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 24: Trigonometric Values at DFC Angles")
print("=" * 76)
print()

# Z_3 center angle = 2*pi/3
z3_angle = 2 * math.pi / 3
print(f"  Z_3 center angle: 2*pi/3 = {z3_angle:.6f} rad = 120°")
print(f"    cos(2*pi/3) = {math.cos(z3_angle):.6f} = -1/2")
print(f"    sin(2*pi/3) = {math.sin(z3_angle):.6f} = sqrt(3)/2")
print(f"    |1 - z_3| = sqrt(3) = {math.sqrt(3):.6f}")
print()

# Weinberg angle
theta_W = math.asin(math.sqrt(0.2312))
print(f"  Weinberg angle: sin^2(theta_W) = 0.2312")
print(f"    theta_W = {math.degrees(theta_W):.4f}°")
print(f"    sin(theta_W) = {math.sin(theta_W):.6f}")
print(f"    cos(theta_W) = {math.cos(theta_W):.6f}")
print(f"    tan(theta_W) = {math.tan(theta_W):.6f}")
print()

# At unification: sin^2(theta_W) = 3/8
theta_W_unif = math.asin(math.sqrt(3/8))
print(f"  At unification: sin^2(theta_W) = 3/8")
print(f"    theta_W = {math.degrees(theta_W_unif):.4f}°")
print(f"    cos(2*theta_W) = 1 - 2*sin^2 = 1 - 3/4 = 1/4")
print(f"    Verification: {1 - 2*3/8:.6f} = 0.25 = 1/4 ✓")
print()

# Theta_23 neutrino mixing
theta_23 = math.radians(49.0)
print(f"  Neutrino theta_23 = 49° (observed)")
print(f"    sin^2(2*theta_23) = {math.sin(2*theta_23)**2:.6f}")
print(f"    If theta_23 = pi/4 (maximal): sin^2(2*theta_23) = 1.000")
print(f"    Deviation from maximal: {49.0 - 45.0}° = 4°")
print()

# DFC angle: alpha_em_unif = beta/4 = 1/(36*pi)
# arctan of alpha?
print(f"  arctan(alpha) = arctan({alpha:.4f}) = {math.degrees(math.atan(alpha)):.4f}°")
print(f"  arctan(1/alpha) = {math.degrees(math.atan(1/alpha)):.4f}°")
print(f"  arctan(sqrt(alpha)) = {math.degrees(math.atan(math.sqrt(alpha))):.4f}°")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 25: Representation dimensions and DFC
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 25: Representation Theory Dimensions")
print("=" * 76)
print()

# SU(3) representation dimensions via Weyl formula: dim(p,q) = (p+1)(q+1)(p+q+2)/2
def su3_dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

print("  SU(3) irrep dimensions dim(p,q) = (p+1)(q+1)(p+q+2)/2:")
low_reps = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3),
            (2,1), (1,2), (4,0), (0,4), (2,2)]
for p, q in low_reps:
    d = su3_dim(p, q)
    c2 = Fraction(p**2 + q**2 + p*q + 3*p + 3*q, 3)
    print(f"    ({p},{q}): dim = {d:4d}, C_2 = {c2} = {float(c2):.4f}")
print()

# Which DFC integers appear as SU(3) dimensions?
print("  DFC integers as SU(3) representation dimensions:")
dfc_check = {2: "Q_top", 3: "N_c", 6: "N_c!", 8: "dim(SU(3))",
             9: "N_Hopf", 11: "b_0", 18: "alpha^3", 24: "4!"}
for n, name in dfc_check.items():
    found = []
    for p in range(20):
        for q in range(p + 1):  # avoid duplicates
            if su3_dim(p, q) == n:
                found.append((p, q))
            if su3_dim(q, p) == n and q != p:
                found.append((q, p))
    if found:
        reps = ", ".join(f"({p},{q})" for p, q in found)
        print(f"    {n:3d} ({name:12s}): YES — {reps}")
    else:
        print(f"    {n:3d} ({name:12s}): NO")
print()

# KEY: 3 = dim(1,0) = fundamental
#      8 = dim(1,1) = adjoint
#     27 = dim(2,2) — and 27 = N_c^3 = g_eff^{-2}!
print(f"  *** dim(2,2) = 27 = N_c^3 = 1/g_eff^2 (times 8) ***")
print(f"  *** 27 is both a representation dimension and the gauge coupling denominator ***")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 26: Riemann zeta at even integers and DFC
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 26: Riemann Zeta Values and DFC")
print("=" * 76)
print()

# zeta(2) = pi^2/6, zeta(4) = pi^4/90, zeta(6) = pi^6/945
# From Exploration 13: S_inst = 27*pi^2 = 162*zeta(2)
print("  Zeta values at even integers: zeta(2k) = (-1)^{k+1} B_{2k} (2pi)^{2k} / (2(2k)!)")
print(f"    zeta(2) = pi^2/6 = {math.pi**2/6:.6f}")
print(f"    zeta(4) = pi^4/90 = {math.pi**4/90:.6f}")
print(f"    zeta(6) = pi^6/945 = {math.pi**6/945:.6f}")
print()

# Express DFC quantities in terms of zeta values
print("  DFC quantities in terms of zeta values:")
print(f"    S_inst = 27*pi^2 = 162*zeta(2)   [162 = 2*N_Hopf^2]")
print(f"    S_kink^2 = (36*pi)^2 = 1296*pi^2 = 7776*zeta(2)")
print(f"      7776 = 6^5 = (N_c!)^5")
S_kink_sq = (36*math.pi)**2
print(f"      Check: {S_kink_sq:.4f} vs 7776*zeta(2) = {7776*math.pi**2/6:.4f} ✓")
print()

# S_inst in terms of zeta(4):
# S_inst = 27*pi^2 = 27*(pi^2/90)*90 = 27*90*zeta(4)/pi^2... no, wrong direction
# Better: S_inst * zeta(2) = 27*pi^2 * pi^2/6 = 27*pi^4/6 = (27/6)*pi^4 = (9/2)*pi^4
# = (N_Hopf/2)*pi^4 = 90*(9/2)*zeta(4)/pi^0... getting circular
# Instead: S_inst/zeta(2) = 27*pi^2/(pi^2/6) = 162 = 2*9^2 = 2*N_Hopf^2
print(f"    S_inst / zeta(2) = 162 = 2*N_Hopf^2 = 2*81 [ratio is integer!]")
print(f"    S_inst / zeta(4) = {S_inst / (math.pi**4/90):.6f} = 27*90/pi^2 = {27*90/math.pi**2:.4f}")
print(f"      = 2430/pi^2 — not clean")
print()

# What about: sum of DFC-weighted zeta values?
weighted_sum = float(I4) * math.pi**2/6 + Q_top * math.pi**4/90 + 3 * math.pi**6/945
print(f"  DFC-weighted zeta sum: I_4*zeta(2) + Q_top*zeta(4) + N_c*zeta(6)")
print(f"    = {weighted_sum:.6f}")
print(f"    = {float(I4)*math.pi**2/6:.4f} + {Q_top*math.pi**4/90:.4f} + {3*math.pi**6/945:.4f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 27: DFC as a lattice / polytope
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 27: Polytope Structure of DFC Parameter Space")
print("=" * 76)
print()

# The 4 topological integers (I_4_num, Q_top, N_c, N_Hopf) = (4, 2, 3, 9)
# with I_4 = 4/3 → numerator 4, denominator 3
# Can we view these as coordinates of a point in Z^4?
# Or: (I_4 * 3, Q_top, N_c, N_Hopf) = (4, 2, 3, 9) ∈ Z^4

p = np.array([4, 2, 3, 9])  # DFC point in Z^4 (I_4_num, Q_top, N_c, N_Hopf)
norm = np.linalg.norm(p)
print(f"  DFC point in Z^4: (3*I_4, Q_top, N_c, N_Hopf) = (4, 2, 3, 9)")
print(f"  Euclidean norm = sqrt(4^2 + 2^2 + 3^2 + 9^2) = sqrt(16+4+9+81)")
print(f"    = sqrt(110) = {norm:.6f}")
print(f"    = {math.sqrt(110):.6f}")
print(f"    110 = 2 × 5 × 11 = Q_top × 5 × b_0 — introduces primes 5 and 11!")
print()

# L1 norm (Manhattan distance)
l1 = sum(p)
print(f"  L1 norm = 4 + 2 + 3 + 9 = {l1}")
print(f"    = 18 = alpha^3 = 2*N_c^2")
print()
print("  *** FINDING: L1 norm of DFC Z^4 point = alpha^3 = 18 ***")
print("  *** Sum of numerically natural DFC integers equals the cube of ***")
print("  *** the compression parameter. ***")
print()

# L-infinity norm
linf = max(p)
print(f"  L-infinity norm = max(4, 2, 3, 9) = {linf} = N_Hopf")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 28: Generating functions for DFC sequences
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 28: DFC Sequences and Generating Functions")
print("=" * 76)
print()

# The N_c-dependent DFC sequence:
# a(N_c) = I_4(N_c) * Q_top(N_c) * N_Hopf(N_c) = N_c(N_c^2-1)^2/8
print("  DFC product sequence a(N_c) = I_4 * Q_top * N_Hopf = N_c*(N_c^2-1)^2/8:")
for n in range(1, 12):
    I4_n = Fraction(n**2 - 1, 2*n) if n > 0 else 0
    Qtop_n = Fraction(n**2 - 1, 4) if n % 2 == 1 else Fraction((n**2 - 1)*n, 2*n*2)
    Nhopf_n = n**2
    if n > 0:
        prod_exact = Fraction(n * (n**2 - 1)**2, 8)
        print(f"    a({n:2d}) = {float(prod_exact):12.2f}  =  {prod_exact}")

print()

# Differences of the sequence
print("  First differences Δa(N_c) = a(N_c+1) - a(N_c):")
for n in range(1, 10):
    a_n = Fraction(n * (n**2 - 1)**2, 8)
    a_n1 = Fraction((n+1) * ((n+1)**2 - 1)**2, 8)
    diff = a_n1 - a_n
    print(f"    Δa({n:2d}) = {float(diff):12.2f}")

print()

# Ratio test: a(N_c+1)/a(N_c)
print("  Ratio a(N_c+1)/a(N_c):")
for n in range(1, 10):
    a_n = n * (n**2 - 1)**2 / 8
    a_n1 = (n+1) * ((n+1)**2 - 1)**2 / 8
    if a_n > 0:
        ratio = a_n1 / a_n
        print(f"    a({n+1:2d})/a({n:2d}) = {ratio:.6f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 29: Pell equation and sqrt(2) in DFC
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 29: sqrt(2) Appearances and Pell Equation")
print("=" * 76)
print()

# sqrt(2) appears many places in DFC:
# alpha = (2*9)^(1/3) = (2*N_c^2)^(1/3)
# xi = sqrt(2/alpha)
# phi_0 = sqrt(alpha/beta) involves sqrt
# BPS: E_kink involves sqrt(2)
# 2*sqrt(2) appears in flux tube gap

print("  sqrt(2) appearances in DFC:")
print(f"    xi = sqrt(2/alpha) = {math.sqrt(2/alpha):.6f}")
print(f"    phi_0 = sqrt(alpha/beta) = {math.sqrt(alpha/beta):.6f}")
print(f"    omega_c = sqrt(2*alpha) = {math.sqrt(2*alpha):.6f}")
print(f"    alpha = (2*N_c^2)^(1/3): the factor of 2 under the cube root")
print(f"    Flux tube gap: 2*sqrt(2)*Lambda_QCD = {2*math.sqrt(2):.6f} * Lambda")
print()

# Pell equation: x^2 - 2*y^2 = ±1
# Solutions: (1,1), (3,2), (7,5), (17,12), (41,29), ...
# x_n/y_n → sqrt(2)
pell_x = [1, 3, 7, 17, 41, 99, 239]
pell_y = [1, 2, 5, 12, 29, 70, 169]
print("  Pell equation x^2 - 2*y^2 = ±1 solutions:")
for i in range(len(pell_x)):
    x, y = pell_x[i], pell_y[i]
    val = x**2 - 2*y**2
    print(f"    ({x:3d}, {y:3d}): {x}^2 - 2*{y}^2 = {val:+d}")

print()
print("  DFC integers in Pell solutions:")
print(f"    y_1 = 1, y_2 = 2 = Q_top")
print(f"    x_3 = 7 (not DFC), y_3 = 5 (appears in k_Y^2 = 5/3)")
print(f"    x_4 = 17 (appears in b_1: b_1=102=6*17)")
print(f"    y_5 = 29 = b_0 + alpha^3 = L_7 (Lucas, from Exp 23)")
print()
print("  *** OBSERVATION: 29 = b_0 + alpha^3 appears as Pell denominator y_5 ***")
print("  *** and simultaneously as Lucas number L_7. ***")
print("  *** 17 (from b_1=102=6*17) is Pell numerator x_4. ***")
print()

# The convergent 17/12 ≈ sqrt(2) to 0.03%
print(f"  Best rational approx: 17/12 = {17/12:.6f} vs sqrt(2) = {math.sqrt(2):.6f}")
print(f"    Error: {abs(17/12 - math.sqrt(2))/math.sqrt(2)*100:.4f}%")
print(f"    12 = 4*N_c = 4*3")
print(f"    17 = b_1/6 = 102/6")
print()

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATION 30: DFC parameter encoding and information content
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("EXPLORATION 30: Information Content of DFC Parameters")
print("=" * 76)
print()

# How many bits to specify each DFC parameter?
# For integers: log_2(n) bits
# For rationals: log_2(num) + log_2(den) bits
print("  Information content (bits) of DFC parameters:")
params_info = [
    ("N_c = 3", math.log2(3)),
    ("Q_top = 2", math.log2(2)),
    ("N_Hopf = 9 = N_c^2", math.log2(9)),
    ("b_0 = 11", math.log2(11)),
    ("I_4 = 4/3", math.log2(4) + math.log2(3)),
    ("g_eff^2 = 8/27", math.log2(8) + math.log2(27)),
    ("beta_lat = 81/4", math.log2(81) + math.log2(4)),
    ("kappa = 1/2", math.log2(1) + math.log2(2)),
]

total_naive = 0
for name, bits in params_info:
    print(f"    {name:25s}: {bits:.2f} bits")
    total_naive += bits

print(f"    {'TOTAL (naive)':25s}: {total_naive:.2f} bits")
print()

# But most are derived from N_c alone! Independent content:
ind_bits = math.log2(3) + math.log2(9) + math.log2(math.pi)  # N_c + pi
# Actually beta = 1/(9*pi) uses pi, which has infinite information
# But structurally, the "choice" is just 1/(N_c^2 * pi)
print("  Independent information content:")
print(f"    N_c = 3: {math.log2(3):.2f} bits (one integer choice)")
print(f"    beta = 1/(9*pi): depends on pi (transcendental — infinite bits)")
print(f"    But structurally: beta = 1/(N_c^2 * pi), so only N_c enters")
print()
print("  *** FINDING: The independent information content of DFC is ***")
print("  *** approximately log_2(3) ≈ 1.58 bits — choosing N_c = 3 ***")
print("  *** from the positive integers. Everything else follows. ***")
print("  *** (Plus the structural choice of pi, which is universal.) ***")
print()

# Kolmogorov complexity estimate
print("  Kolmogorov complexity estimate:")
print("    The shortest program to generate all DFC parameters:")
print("    'N=3; pi=acos(-1); beta=1/(N^2*pi); alpha=(2*N^2)^(1/3)'")
print(f"    ~60 characters ≈ 480 bits")
print(f"    This generates ALL {len(params_info)} fundamental DFC parameters")
print(f"    and predicts ~25 physical observables to <5% accuracy.")
print()

# ═══════════════════════════════════════════════════════════════════════════
# UPDATED SUMMARY (Explorations 1-30)
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 76)
print("UPDATED SUMMARY OF FINDINGS (Explorations 1-30)")
print("=" * 76)
print()
print("  STRUCTURAL:")
print("  1. b_0 = N_c^2 + Q_top = 11 unique to N_c=3 [T1, C417]")
print("  2. I_4 * Q_top * N_Hopf = 24 = 4! unique factorial at N_c=3 [E11]")
print("  3. det([[I_4, Q_top], [N_c, N_Hopf]]) = 6 = N_c! [E16]")
print("  4. DFC parameter space has dimension 2: {N_c, beta} [E20]")
print("  5. 27 = dim(2,2) of SU(3) = 1/g_eff^2 × 8 [E25]")
print()
print("  NUMBER-THEORETIC:")
print("  6. All topological DFC parameters factor into primes {2, 3} only [E14]")
print("  7. Non-{2,3} primes enter only through dynamics: b_0=11, b_1→17, k_Y^2→5 [E14]")
print("  8. alpha = 18^(1/3) has minimal polynomial degree N_c = 3 [E12]")
print("  9. Pi-free skeleton: S/pi^k always yields N_c^j × small integer [E13]")
print(" 10. b_0=11 and alpha^3=18 are CONSECUTIVE Lucas numbers L_5, L_6 [E23]")
print(" 11. Pell convergents contain 17 (from b_1) and 29 (b_0+alpha^3) [E29]")
print()
print("  ALGEBRAIC:")
print(" 12. (3*sqrt(2))^(2/3) = 18^(1/3) = alpha [C417]")
print(" 13. Cosmological exponent = N_Hopf*pi*(3*pi+1/2) + alpha [C417]")
print(" 14. S_inst = N_Hopf^2 * pi^2 / N_c [E13]")
print(" 15. L1 norm of DFC Z^4 point = 4+2+3+9 = 18 = alpha^3 [E27]")
print()
print("  META:")
print(" 16. Independent information content: ~1.58 bits (choosing N_c=3) [E30]")
print(" 17. Kolmogorov complexity: ~60 chars generates all DFC parameters [E30]")
print()
print("  Flagged for dedicated equation modules:")
print("    - E11: 4! uniqueness at N_c=3 (combinatorial proof)")
print("    - E14: {2,3} vs dynamic primes (structural vs loop)")
print("    - E16: det = N_c! (topological matrix)")
print("    - E20: parameter space dimension = 2")
print("    - E23: Lucas number coincidence — assess structural vs numerical")
print("    - E27: L1 norm = alpha^3 identity")
print("    - E30: Information content analysis (potential educational doc)")
print()
