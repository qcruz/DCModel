# Kink Phase Stiffness and the Gauge Coupling Derivation

## Status

> **Cycle 47:** Formal derivation of the kink phase stiffness f² = (4/3)φ₀²/λ
> from the DFC substrate field equation — this part is exact. Maps the connection
> between f² and the gauge coupling g² = 8πβ/3, identifying precisely where the
> derivation is rigorous and where the gap lies. Two candidate routes to closing
> the gap are identified with the specific calculation each requires.
>
> **Key result:** The kink shape integral ∫ sech⁴(u) du = 4/3 is derived exactly.
> The step from f² to r_U1/λ requires a physical identification that is motivated
> but not yet formally proved. The gap is precisely located and is a single,
> specific calculation.

---

## The Derivation Goal

The gauge coupling g_common ≈ 0.543 at the D5/D6 closure scale satisfies:

```
g² = 8πβ/3    [Cycle 42 result; 0.3% match with SM; heuristic]
```

where β ≈ 0.035 is the substrate quartic coupling. The derivation chain is:

```
β  →  f² [kink phase stiffness]  →  r_U1/λ [closure fiber radius]  →  g² [holonomy]
```

This document derives the first step exactly and maps the second step.

---

## Step 1: The Kink Shape Integral — Exact Derivation

### The kink profile

The DFC substrate field satisfies the potential:

```
V(phi) = −alpha/2 phi² + beta/4 phi⁴
```

with stable minima at plus and minus the equilibrium field value:

```
phi_0 = sqrt(alpha / beta)
```

The kink interpolates from minus phi_0 at minus spatial infinity to plus phi_0 at plus
spatial infinity. The exact static kink solution is:

```
phi_K(x) = phi_0 * tanh(x / lambda)

where lambda = c * sqrt(2 / alpha)  [the kink half-width]
```

This satisfies the static field equation exactly (verified in `equations/kink_model.py`).

### The gradient squared integral

The kink phase stiffness f² is defined as the integral of the squared gradient of the
kink profile over the full real line — the total gradient energy stored in the kink:

```
f² = integral from -infinity to +infinity of (d phi_K / dx)² dx
```

Computing the gradient of the kink profile — the rate at which the field changes with
position — gives:

```
d phi_K / dx = (phi_0 / lambda) * sech²(x / lambda)
```

where sech(u) = 1/cosh(u) is the hyperbolic secant. Squaring:

```
(d phi_K / dx)² = (phi_0 / lambda)² * sech⁴(x / lambda)
```

Integrating over all x with the substitution u = x/lambda (so dx = lambda du):

```
f² = (phi_0 / lambda)² * lambda * integral of sech⁴(u) du from -inf to +inf
   = (phi_0² / lambda) * I_4

where I_4 = integral of sech⁴(u) du from -inf to +inf
```

### The exact evaluation of I_4

The integral of the fourth power of the hyperbolic secant over the real line is a standard
result. One derivation: use the reduction formula. Since sech²(u) = 1 − tanh²(u):

```
integral of sech⁴(u) du = integral of sech²(u) * sech²(u) du
                         = integral of sech²(u) * (1 − tanh²(u)) du
```

Let t = tanh(u), dt = sech²(u) du. The limits: t → −1 as u → −∞, t → +1 as u → +∞:

```
I_4 = integral from t=−1 to t=+1 of (1 − t²) dt
    = [t − t³/3] from −1 to +1
    = (1 − 1/3) − (−1 + 1/3)
    = 2/3 − (−2/3)
    = 4/3
```

This is an exact result. The integral of the fourth power of the hyperbolic secant over
the entire real line equals four-thirds.

### The phase stiffness result

Substituting I_4 = 4/3 back:

```
f² = (phi_0² / lambda) * (4/3) = (4/3) phi_0² / lambda   [EXACT]
```

In terms of the substrate parameters α and β:

```
phi_0² = alpha / beta
lambda = sqrt(2/alpha)  [in units where c = 1]

f² = (4/3) * (alpha/beta) / sqrt(2/alpha)
   = (4/3) * (alpha/beta) * sqrt(alpha/2)
   = (4/3) * alpha^(3/2) / (beta * sqrt(2))
   = (4/3) * sqrt(alpha³ / (2 beta²))
   = (8/3) * M_c³ / beta         [using M_c = sqrt(alpha/2), so alpha = 2M_c²]
```

The stiffness of the kink gradient field is proportional to the cube of the closure
mass scale and inversely proportional to the quartic coupling.

### Connection to E_kink

The kink energy (total energy, kinetic plus potential) is also exactly computable. For
a φ⁴ kink, the virial theorem equates gradient and potential contributions:

```
E_kink = 2 * (gradient contribution) = 2 * f²/2 ??? [not quite]
```

Actually the exact kink energy is:

```
E_kink = integral of [(1/2)(d phi_K/dx)² + V(phi_K)] dx
```

Using the Bogomolny identity for φ⁴ solitons: (dφ/dx)² = 2V(φ), so:

```
E_kink = integral of 2V(phi_K) dx = integral of (d phi_K/dx)² dx = f²
```

Wait — for V(φ) = −α/2 φ² + β/4 φ⁴, we need to shift by the vacuum energy:
V(phi) − V(phi_0) = −alpha/2 phi² + beta/4 phi⁴ − (−alpha²/(4beta))
                   = −alpha/2 phi² + beta/4 phi⁴ + alpha²/(4beta)

The Bogomolny identity for this potential:
(dφ/dx)² = [V(φ) − V(phi_0)] × 2 = (phi_0² − phi²)² × beta/2

Check: at φ = 0: (dφ/dx)² = phi_0⁴ × beta/2 = (alpha/beta)² × beta/2 = alpha²/(2beta)
And at x=0: dφ/dx = phi_0/lambda = sqrt(alpha/beta)/sqrt(2/alpha) = sqrt(alpha²/(2beta)) ✓

So: E_kink = integral (dφ/dx)² dx = f² = (4/3) phi_0² / lambda [confirmed]

**The phase stiffness f² equals the kink energy exactly.**

---

## Step 2: The Holonomy Formula — Stated Exactly

The gauge coupling of the D5 U(1) closure is determined by the holonomy of the U(1)
gauge field around the S¹ fiber of the closure manifold. For a U(1) gauge field living
on an S¹ of circumference L = 2π r_U1, and a matter field with unit winding number,
the holonomy formula gives the 4D gauge coupling as:

```
g² = (2π)² / (2π r_U1 / lambda) = 2π lambda / r_U1 = 2π / (r_U1/lambda)
```

where the circumference L = 2π r_U1 is measured in units of the kink width lambda.

This formula follows from treating the D5 U(1) closure as a Kaluza-Klein compactification
of the substrate field on the S¹ fiber. The 4D coupling g relates to the 5D coupling g_5
and the compactification radius R by g² = g_5²/(2π R) (in appropriate units). For the
DFC substrate, the effective 5D coupling is set by the kink width lambda, giving the
formula above.

**The holonomy formula is exact once r_U1 is known.** The entire derivation problem
reduces to: what is r_U1/lambda from the substrate?

For the observed g_common ≈ 0.543:
```
r_U1/lambda = 2π / g_common² = 2π / 0.295 ≈ 21.3   [numerical target]
```

---

## Step 3: The Missing Connection — Exactly Located

The Cycle 42 heuristic set:

```
r_U1 / lambda = 1 / (beta × 4/3) = 3 / (4 beta)   [heuristic identification]
```

At beta = 0.035: r_U1/lambda = 3/(4×0.035) = 21.4. This matches the SM target (21.3)
to 0.5%.

**Where does this identification come from?**

Define the dimensionless ratio formed from f² and the substrate parameters:

```
kappa = f² × lambda / phi_0²  =  (4/3)phi_0²/lambda × lambda / phi_0²  =  4/3
```

The ratio kappa is the kink shape factor — it is exactly 4/3, as derived above.

The identification r_U1/lambda = 3/(4β) = 1/(β × kappa) can be rewritten as:

```
r_U1 = phi_0² / (beta × f²)   [in natural units]
```

**This is the missing step:** The closure fiber radius r_U1 is being identified as the
ratio of the field amplitude squared to the product of the quartic coupling and the
kink tension. This is a physically motivated but not yet formally derived relation.

### Why this identification is physically plausible

Two physical arguments support it:

**Argument 1 — Inverse stiffness:**
A stiffer substrate potential (larger beta) yields a shorter, steeper kink (smaller lambda
and larger f²). A stiffer substrate less readily opens a new phase degree of freedom,
so the U(1) fiber should be more compact. r_U1 ∝ 1/beta captures this: the fiber radius
shrinks as the quartic coupling grows. The factor phi_0²/f² provides the correct
dimensions and compensates for the alpha-dependence of phi_0 and f².

**Argument 2 — σ-model Goldstone identification:**
The U(1) phase θ of the complexified substrate field is a Nambu-Goldstone boson with
effective Lagrangian L_θ = (f²/2)(∂_μθ)² in the kink background. In a compact target
space (the S¹ fiber), the Goldstone field has periodicity 2π and the "radius" of the
target S¹ in the ambient field space is:

```
R_theta = f / (2π × normalization)
```

If the normalization converts field-space radius to real-space radius via the kink
gradient (phi_0/lambda), then:

```
r_U1 = R_theta / (phi_0/lambda) × phi_0 = f × lambda / (2π × phi_0) × phi_0 = f × lambda / (2π)
```

But f = sqrt((4/3)phi_0²/lambda), so:

```
r_U1 = sqrt((4/3)phi_0²/lambda) × lambda / (2π)
     = lambda × phi_0 × sqrt(4/3) / (2π)
```

This gives r_U1/lambda = phi_0 × sqrt(4/3) / (2π) — which depends on phi_0 and does not
simplify to 3/(4β) without additional assumptions. This route does NOT currently produce
the heuristic formula.

**Argument 3 — Kink action interpretation:**
The kink action (energy × width) has dimensions [energy × length] = [action]:

```
S_kink = E_kink × lambda = f² × lambda = (4/3)phi_0²   [dimensionless in ℏ = c = 1]
```

The inverse of this action (per unit quartic coupling):

```
1 / (beta × S_kink) = 1 / (beta × (4/3)phi_0²) = beta/(beta × (4/3) × alpha/beta) = 1/((4/3)alpha)
```

This still has dimensions (alpha has dimensions of GeV²). So this route also does not
directly produce r_U1/lambda = 3/(4β) without more work.

---

## The Required Calculation

The gap is now precisely located. What is needed is a formal computation showing that
the D5 S¹ closure, when the substrate field is in the kink background at D5 depth,
has a fiber radius in substrate units equal to 3/(4β).

Two routes:

### Route A: Kaluza-Klein reduction of the DFC substrate on S¹

Write the DFC substrate field equation in 5D (treating the U(1) phase direction as a
compact fifth dimension), and perform the standard Kaluza-Klein reduction on an S¹ of
radius R_KK. The 4D effective theory will have a U(1) gauge field with coupling:

```
g_KK² = 1 / (M_5^(D-4) × R_KK × Vol(internal))
```

where M_5 is the substrate's fundamental mass scale. In DFC, M_5 relates to M_Pl (from
the D1 anchor). The calculation requires:
1. Identifying the correct 5D embedding of the DFC substrate field
2. Computing the spectrum of Kaluza-Klein modes
3. Identifying which mode is the photon (massless U(1) gauge boson)
4. Reading off the coupling g_KK

The target: show R_KK = r_U1 = (3/(4β)) × lambda from this computation.

### Route B: Worldvolume field theory on the kink domain wall

Treat the D5 kink as a domain wall in 4+1D (the domain wall lives in 3+1D). The
worldvolume theory of the domain wall is a 3+1D theory containing the Goldstone mode θ
(the phase of the D5 U(1) closure) with effective Lagrangian:

```
L_wall = (sigma/2)(∂_μ θ)² + (higher terms)
```

where sigma = f² = E_kink/(unit transverse area) = (4/3)phi_0²/lambda is the domain
wall tension.

The Goldstone mode θ on the 3+1D worldvolume acts as a gauge scalar (the longitudinal
mode of the photon). The transverse fluctuations of the domain wall give the photon's
two transverse modes. The gauge coupling from this worldvolume theory is:

```
g_wall² = 1 / (sigma × lambda²) × normalization
```

where sigma × lambda² is the dimensionless domain wall tension. Computing the precise
normalization from the matching of bulk and worldvolume theories is the calculation needed.

Substituting sigma = (4/3)phi_0²/lambda and phi_0² = alpha/beta = 2M_c²/beta:

```
sigma × lambda² = (4/3)(alpha/beta)/lambda × lambda²
               = (4/3)(alpha/beta) × lambda
               = (4/3) × (alpha/beta) × (1/M_c)
               = (4/3) × (2M_c²/beta) / M_c
               = (8/3) × M_c / beta
```

For g² = 8πβ/3, we would need:
1/(sigma × lambda²) × normalization = 8πβ/3

→ normalization = 8πβ/3 × sigma × lambda² = 8πβ/3 × (8/3) M_c/beta = (64π/9) M_c

The normalization factor being proportional to M_c (not 1) suggests that the conversion
from the worldvolume coupling to the 4D gauge coupling introduces a factor related to the
kink width. This is the expected result from dimensional reduction: the 4D coupling
involves the kink width as a length scale, exactly as in Kaluza-Klein reduction.

**The specific open calculation:** Compute the normalization factor in the worldvolume
theory (Route B) or in the KK reduction (Route A), and show it equals (64π/9) M_c. This
is a single, standard quantum field theory calculation.

---

## Consistency Checks

```
Kink shape integral (exact):
    I_4 = integral of sech⁴(u) du from -inf to +inf = 4/3   ✓ proved above

Kink phase stiffness (exact):
    f² = (4/3) phi_0² / lambda = (8/3) M_c³ / beta           ✓ proved above

Kink energy = phase stiffness (exact Bogomolny identity):
    E_kink = f² = (4/3) phi_0² / lambda                       ✓ confirmed

Holonomy formula (stated; follows from KK theory):
    g² = 2π / (r_U1 / lambda)                                 stated

Heuristic identification (0.3% numerical match):
    r_U1 / lambda = 3 / (4 beta)                              numerically verified

Consequence:
    g² = 8π beta / 3                                          0.3% agreement with SM
```

---

## Summary Table

| Step | Claim | Status |
|---|---|---|
| Kink profile φ_K = φ₀ tanh(x/λ) | Exact solution to substrate field equation | PROVED ✓ |
| ∫ sech⁴(u) du = 4/3 | Exact evaluation via tanh substitution | PROVED ✓ |
| f² = (4/3)φ₀²/λ | Gradient squared integral of kink | PROVED ✓ |
| f² = E_kink (Bogomolny) | Potential and gradient contributions equal | PROVED ✓ |
| Holonomy formula g² = 2π/(r_U1/λ) | KK reduction on S¹ | STATED (standard KK result) |
| r_U1/λ = 3/(4β) | Missing step: from f² to r_U1 | GAP — Routes A/B proposed |
| g² = 8πβ/3 | Consequence of r_U1/λ = 3/(4β) | HEURISTIC (0.3% match) ✓ |

---

## Open Questions

1. **Route A calculation:** Embed the DFC substrate field in 5D with the U(1) phase as
   the fifth dimension. Perform the KK reduction and compute r_KK in terms of (α, β, c).
   Does the KK radius equal 3λ/(4β)?

2. **Route B calculation:** Derive the worldvolume effective theory of the D5 domain wall
   from the bulk DFC field equation. Compute the normalization of the Goldstone kinetic
   term and show the worldvolume coupling gives g² = 8πβ/3.

3. **Connection to beta:** Once r_U1/λ = 3/(4β) is proved formally, the formula g² = 8πβ/3
   promotes from heuristic to derived. At that point, β is the SOLE remaining free parameter
   in the entire coupling chain (α_em, sin²θ_W, α_s all follow). Deriving β from a pre-substrate
   condition would then complete the chain from first principles.

4. **Generalization to SU(2) and SU(3):** The same approach should apply at D6 (S³ ⊂ ℂ²,
   SU(2) coupling) and D7 (S⁵ ⊂ ℂ³, SU(3) coupling). If the equal-coupling initial condition
   (g₁ = g₂ = g₃ at M_c) follows from the equal sphere radii r_S³/λ = r_S⁵/λ = r_S¹/λ = 3/(4β),
   this would be a DFC derivation of gauge coupling unification at the closure scale.

---

## Connections

- `foundations/coupling_derivation.md` — holonomy formula and g_common; r_U1/λ ≈ 21 target
- `foundations/hopf_fibration_geometry.md` — S¹/S³/S⁵ topology at D5/D6/D7
- `foundations/substrate.md` — φ⁴ potential and kink solutions
- `foundations/kink_nucleation.md` — kink energy and barrier height from same integral
- `equations/kink_model.py` — numerical verification of kink profile and energy
- `equations/coupling_derivation.py` — g² = 8πβ/3 implemented and verified
