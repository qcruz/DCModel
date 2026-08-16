# The D4 Gap: Deriving Gravity from the Substrate

**Status:** Active exploration (T4 open — deepest structural gap in DFC)
**Purpose:** Map precisely what is known, what is assumed, and what remains to
be derived in order for gravity to emerge from V(phi) = -alpha/2 phi^2 + beta/4 phi^4.

---

## 1. The Problem

DFC claims that all physics emerges from V(phi). This includes gravity. Yet
Newton's gravitational constant G_N currently enters DFC as an input (through
the use of Planck units), not as an output.

The D4 gap is not one problem but **four distinct sub-problems** that must be
solved in sequence. Solving one does not automatically solve the others.

---

## 2. The Four Sub-Gaps

### D4-A: Scale Generation

**Question:** What establishes the absolute gravitational scale?

The potential V(phi) has intrinsic scales: phi_0 = sqrt(alpha/beta) and
xi = sqrt(2/alpha). But these carry the dimensions of whatever units alpha
has. Writing alpha = cuberoot(18) times M_Pl squared does not derive M_Pl
from the substrate — it merely parameterizes the relationship between the
substrate scale and the gravitational scale.

A dimensionful parameter is not automatically a prediction.

The dimensionless content is alpha times G_N = cuberoot(18), but this is a
**consistency relation**, not an **independent prediction**. The real target
is to derive the absolute scale:

```
M_Pl^2 = alpha * F(beta, substrate structure)
```

and then demonstrate that F = 1/cuberoot(18) from the substrate dynamics.

**Status:** T4 open. Dimensional analysis guarantees G_N is proportional
to 1/alpha; the dimensionless coefficient is the actual content.

### D4-B: Metric Emergence

**Question:** How does apparent spacetime geometry emerge from the substrate?

The phrase "geometry is downstream" must eventually become an equation of
the form:

```
g_muv^eff = eta_muv + F_muv[phi, d phi, d^2 phi, ...]
```

A kink (closure) locally deforms the substrate. Other substrate excitations
then propagate not through the bare substrate coordinates, but through an
effective geometry determined by the deformation. The conceptual chain is:

```
phi -> substrate deformation -> g_muv^eff -> geodesic motion
```

This is substantially more promising than trying to make the kink profile
itself behave as 1/r (which it cannot — it falls off exponentially).

**Status:** T4 open. No explicit construction of g_muv^eff from V(phi)
exists. This is the most fundamental of the four sub-gaps.

### D4-C: Graviton Emergence

**Question:** Does the DFC substrate possess a genuine massless propagating
mode with the correct gravitational degrees of freedom?

This requires establishing a hierarchy of properties:

1. **Existence:** Does the substrate have a massless mode? (m = 0)
2. **Propagation:** Does it propagate at the invariant speed? (omega^2 = c^2 k^2)
3. **Polarization:** Does it have the correct number of physical polarizations?
   A four-dimensional massless spin-2 field has exactly two helicity states.
4. **Coupling:** Does the mode couple universally to energy-momentum?
5. **Long-range potential:** Does its exchange produce V(r) = -G_N m_1 m_2 / r?

**Critical distinction:** T_muv being a rank-2 object does NOT mean that the
field carrying gravitational interactions is rank-2. A scalar field has a
rank-2 energy-momentum tensor; that does not turn the scalar into a spin-2
particle. The actual question is whether fluctuations of the DFC substrate
can transform as a massless spin-2 representation — whether an emergent h_muv
exists with the appropriate gauge redundancy (h_muv -> h_muv + d_mu xi_v + d_v xi_mu).

**Masslessness protection:** The model proposes that microscopic massive scalar
dynamics produce macroscopic massless tensor dynamics. This can happen in
emergent systems, but is not generic. The model must identify what symmetry
or critical phenomenon protects the gravitational mode from acquiring a mass.
Otherwise the natural expectation is a finite correlation length giving
V(r) ~ exp(-m_g r)/r rather than exactly 1/r.

**Status:** T4 open. The kink zero-mode (omega_0 = 0) is massless but scalar.
No spin-2 mode has been identified in the substrate spectrum. This may be the
single hardest sub-gap.

### D4-D: Coupling Emergence

**Question:** How strongly does emergent geometry respond to substrate energy?

This is the numerical coupling problem: derive G_N = f(alpha, beta) with a
specific coefficient. The target is not simply G_N ~ 1/alpha (which dimensional
analysis guarantees), but rather:

```
M_Pl^2 = alpha * F(beta, substrate structure)
```

where F must be computed from the dynamics, producing F = 1/cuberoot(18).

The scalar zero-mode exchange gives G_eff = G_N/23, capturing only 4.4% of the
gravitational coupling. The remaining 95.6% is non-perturbative content that
cannot be obtained from linearized kink-kink exchange.

**Status:** T3 (scalar fraction characterized). T4 for the full coupling.

---

## 3. What V(phi) Already Provides

### 3a. Intrinsic scales

The kink width xi = sqrt(2/alpha) and vacuum phi_0 = sqrt(alpha/beta) are
determined by V(phi). In Planck units, xi = 0.874 l_Pl. The oscillation
frequency omega_c = sqrt(2 alpha) = sqrt(V''(phi_0)) is the Compton frequency
of a kink — this is established (T1).

### 3b. BPS saturation

The kink satisfies (1/2)(phi')^2 = V_ren(phi) at every point along its profile,
where V_ren = V(phi) - V(phi_0) is the renormalized potential. This is the
Bogomolny-Prasad-Sommerfield property (T1). The energy density is:

```
eps(y) = alpha^2 / (2 beta) * sech^4(y/xi)
```

and the total energy is E_kink = 36 pi M_Pl.

### 3c. The sech-integral hierarchy

Overlap integrals involving higher powers of sech are computed exactly via
Fraction arithmetic:

```
I_4  = 4/3       I_6  = 16/15     I_8  = 32/35
I_10 = 256/315   I_12 = 512/693
```

The profile ratio (I_10/I_6)^2 = 0.58 is less than 1, meaning that the
sech^8 graviton vertex profile is NARROWER than the sech^4 scalar vertex.
Profile effects reduce rather than enhance the coupling (T1).

### 3d. The scalar zero-mode fraction

The enhancement factor F = G_N/G_eff = (25/12) times 4 pi xi = 22.87 (T1 exact).
The rational prefactor 25/12 = I_4^3 / I_6^2 is a pure sech-integral identity.
The scalar zero-mode captures 1/F = 4.4% of G_N (T3).

---

## 4. What Is Missing — and Why Each Matters

### 4a. The 1/r potential (relates to D4-C)

The kink profile phi_kink(x) = phi_0 tanh(x/xi) falls off exponentially, not
as 1/r. The 1/r potential requires a massless mode with a 1/k^2 propagator.

The kink-kink interaction at large separation through exponential tail overlap
gives V_int(R) ~ exp(-R/xi) — a Yukawa interaction from a massive mediator.
The claim that 1/r behavior emerges at D3 localization scales is currently a
hypothesis, not a derived consequence. The model needs to explain **why
localization produces a massless mode** and what protects its masslessness.

### 4b. Spin-2 from a scalar substrate (relates to D4-C)

The substrate field phi is a scalar. Gravity requires a rank-2 tensor
perturbation h_muv with specific gauge symmetry and two physical polarizations.

The scientifically interesting question is:

> Can a sufficiently structured scalar substrate possess an emergent tensor
> collective mode?

If yes, DFC has something genuinely novel. If no, the theory has identified
a fundamental obstruction. Either result is scientifically valuable.

The mathematical target is concrete: determine whether the linear response
kernel of the DFC substrate around its vacuum or localized background contains
a pole with the structure:

```
D_muv_ab(k) ~ P^(2)_muv_ab / k^2
```

where P^(2) is the spin-2 projection operator. The 1/k^2 gives long-range
behavior; P^(2) gives spin-2 behavior. D4 needs to derive both.

### 4c. Strong-field consistency (relates to D4-A)

The kink has energy E_kink = 113 M_Pl and width xi = 0.874 l_Pl. Its
Schwarzschild radius r_s = 2 G_N E_kink = 226 l_Pl is vastly larger than
its width. If interpreted as an ordinary gravitating object using standard
GR, the kink lies deep inside its own gravitational radius.

This is not merely "strong self-gravity." It creates a fundamental DFC
consistency test: either (1) standard gravitational reasoning fails at the
D4 scale, (2) the kink's gravitational mass differs radically from its
field energy, (3) the effective gravitational coupling is scale-dependent,
(4) the kink is not a conventional localized object, or (5) the proposed
parameter values are inconsistent.

**Important circularity:** E_kink = 36 pi / sqrt(G_N) in natural units.
Using this energy to derive a gravitational field inserts G_N through M_Pl,
then uses the same G_N to calculate gravity. This is a valid consistency
check, but it is not evidence for deriving G_N. The distinction between
"consistency relation" and "independent prediction" must be maintained.

### 4d. The 36 pi / alpha_em connection (relates to D4-A, D4-D)

The identity S_kink = 4/beta = 36 pi = 1/alpha_em(M_c) is numerically
striking. But its evidentiary value depends on whether the number is
predicted before fitting. The strongest sequence would be:

```
V(phi) -> alpha, beta -> S_kink -> alpha_em(M_c)
```

with no adjustable parameter. If alpha, beta, or M_c were partly chosen
because they produce 36 pi, the evidentiary value is weaker. Currently,
beta = 1/(9 pi) is derived (T2a) and S_kink = 4/beta = 36 pi follows
as a T1 algebraic consequence, so this chain is legitimate.

---

## 5. Research Program — Ordered by Priority

### Primary: Induced Gravity via Substrate Response (D4-B + D4-C)

The most promising mathematical program. Suppose integrating out the
substrate degrees of freedom around the kink background generates an
effective gravitational action:

```
S_eff = integral d^4x sqrt(-g) [Lambda + M_eff^2/2 R + a R^2 + ...]
```

Then M_eff^2 = M_Pl^2 gives G_N = 1/M_eff^2. The D4 problem becomes:

> Can integrating out DFC substrate modes generate an Einstein-Hilbert
> term, and what coefficient does it produce?

**The critical next calculation:** Start with the DFC substrate action,
find the background solution, perturb it (phi = phi_bg + delta phi),
compute the quadratic action S^(2)[delta phi], construct the stress-energy
response delta T_muv, and determine whether there exists a collective
variable h_muv = F_muv[delta phi, ...] whose effective quadratic action
becomes S^(2)[h] ~ integral h_muv E^muv_ab h_ab where E is the linearized
Einstein operator.

If that structure emerges, the D4 problem reduces to a coupling-normalization
problem. If it does not, DFC has identified exactly where its scalar
architecture fails to reproduce gravity.

### Secondary: Jormungandr Self-Consistency (D4-A + D4-D)

Rather than deriving G_N from V(phi) forward, or V(phi) from G_N backward,
the two may be constrained by a self-consistency loop:

```
V(phi) -> matter/closure -> compression -> effective geometry
  -> collapse -> endpoint -> V_eff(phi)
```

Requiring V_eff(phi) = V(phi) at the fixed point would make the double-well
not an arbitrary starting assumption but an attractor of the substrate's
gravitational dynamics. If demonstrated mathematically, this would turn
Jormungandr from an interpretive narrative into an actual mechanism.

### Tertiary: Masslessness Protection (D4-C)

Identify the symmetry or critical phenomenon that protects the gravitational
mode from acquiring a mass. Candidate mechanisms:
- Diffeomorphism invariance as an emergent gauge symmetry
- Goldstone mechanism from spontaneous breaking of a substrate symmetry
- Critical behavior at the D3/D4 boundary

---

## 6. Connections to Other Open Problems

| Problem | Connection to D4 |
|---|---|
| T8 (hbar derivation) | G_N and hbar are linked via M_Pl = sqrt(hbar c/G). Deriving G_N may require or enable deriving hbar. |
| T16 (Lambda_cosm) | The cosmological constant prediction rho_Lambda ~ M_Pl^4 exp(-283) uses M_Pl as input. Deriving M_Pl makes this a pure DFC prediction. |
| Jormungandr | D4 gap and Jormungandr are the same problem from different directions. |
| D3 localization | Gravity requires D3 (apparent space) to propagate through. D4 may depend on D3 being established first. |

---

## 7. What "D4 Closed" Would Mean

Not merely finding G_N = cuberoot(18)/alpha (which is dimensional fitting).
Five requirements:

| Requirement | Needed result |
|---|---|
| D4-A: Scale | M_Pl = f(alpha, beta) derived from dynamics |
| D4-B: Geometry | g_muv = g_muv[phi, d phi, ...] explicit construction |
| D4-C: Propagation | Massless long-range mode with two spin-2 polarizations |
| D4-C: Coupling | Universal coupling to energy-momentum (h_muv T^muv) |
| D4-D: Coefficient | G_N = f(alpha, beta) with predicted coefficient |

Ideally: DFC -> Einstein equations + Newtonian limit, with the coefficient
of the Einstein-Hilbert term predicted rather than inserted.

---

## 8. Current Status Summary

**Established:**
- xi ~ l_Pl (structural identification, T1)
- omega_c = sqrt(2 alpha) as Compton frequency (T1)
- BPS saturation: KE = V_ren at each point (T1)
- alpha times G_N = cuberoot(18) (consistency relation, T1)
- Scalar zero-mode gives G_eff = G_N/23 (T3)
- Profile narrowing REDUCES coupling: (I_10/I_6)^2 = 0.58 (T1)
- Enhancement is dominantly non-perturbative: 96% (T3)
- F = (25/12) times 4 pi xi = 22.87 exact decomposition (T1)
- Kink r_s/xi = 226/0.874 >> 1: deep inside own gravitational radius (T1)

**Open:**
- D4-A: Absolute scale generation (T4)
- D4-B: Metric emergence from substrate (T4 — most fundamental)
- D4-C: Massless spin-2 mode from scalar substrate (T4 — hardest)
- D4-D: Numerical coupling coefficient (T4)
- Masslessness protection mechanism (T4)
- Strong-field consistency resolution (T4)

**Most promising path:** Induced gravity via substrate response function
(Primary program above), combined with Jormungandr self-consistency as
a nonlinear boundary condition.

---

**See also:** `foundations/jormungandr_double_well.md` for the cyclical
compression hypothesis. `equations/d4_gravity_spin2_enhancement.py` (C392)
for the spin-2 enhancement analysis. `equations/d4_zero_mode_gravity.py`
(C367) for the scalar zero-mode calculation. `equations/d4_gravity_dimensional.py`
(C366b) for dimensional analysis and the omega_c bridge.
