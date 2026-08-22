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
