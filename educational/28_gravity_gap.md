# Module 28 — The D4 Gravity Gap: Where DFC Stands on Deriving Gravity

**Series:** DFC Educational Modules — each module is self-contained and can be read
independently. For background on forces, see Module 04. For the I₄ identity, see
Module 09. For open problems, see Module 18.

**Context:** This module documents the status of gravity within DFC as of Cycles
366–399. It covers what has been established, what has been tried, what failed,
what partially worked, and what the breakthroughs of C396–C399 changed. Written
in journaling style to capture the reasoning at the current frontier.

---

## 1. The Problem: Gravity Is Not Yet Derived

DFC claims that all physics emerges from a single potential, V(phi) = -alpha/2 phi²
+ beta/4 phi⁴. This includes the strong force, the weak force, and electromagnetism
— all of which have been connected to V(phi) through the D5/D6/D7 closure topology
chain with explicit equation modules and quantitative predictions.

Gravity is different. Newton's gravitational constant G_N currently enters DFC as an
**input**, not an **output**. When we write the kink width xi = 0.874 l_Pl (Planck
lengths), we are using Planck units — which already contain G_N. We have not derived
G_N from the substrate parameters alpha and beta.

This is the D4 gravity gap, and it is the deepest structural gap in the DFC framework.

The gap is not one problem. It is **four distinct sub-problems** that must be solved
in sequence. Solving one does not automatically solve the others.

---

## 2. The Four Sub-Gaps

### D4-A: Scale Generation

**Question:** What sets the absolute gravitational scale?

The potential V(phi) has two intrinsic scales: the vacuum value phi_0, which equals
the square root of alpha over beta, and the kink width xi, which equals the square
root of two over alpha. But these carry the dimensions of whatever units alpha has.
Writing alpha = cuberoot(18) times M_Pl squared does not derive M_Pl from the
substrate — it merely parametrizes the relationship between the substrate scale and
the gravitational scale.

The dimensionless content of the model is the product alpha times G_N, which equals
cuberoot(18). This is a **consistency relation**, not an **independent prediction**.
The real target is to derive the absolute scale — to show that M_Pl squared equals
alpha times some function F(beta, substrate structure), and then demonstrate that F
equals 1/cuberoot(18) from the substrate dynamics alone.

**Status:** T4 open. Dimensional analysis guarantees G_N is proportional to 1/alpha;
the dimensionless coefficient is the actual content.

### D4-B: Metric Emergence

**Question:** How does apparent spacetime geometry emerge from the substrate?

The phrase "geometry is downstream of the substrate" must eventually become an
equation. The target is an expression for an effective metric — g_muv^eff — as a
functional of the substrate field phi and its derivatives:

g_muv^eff = eta_muv + F_muv[phi, d phi, d² phi, ...]

A kink (closure) locally deforms the substrate. Other substrate excitations then
propagate not through the bare substrate coordinates, but through an effective
geometry determined by the deformation. The conceptual chain is:

phi → substrate deformation → g_muv^eff → geodesic motion

This is substantially more promising than trying to make the kink profile itself
behave as 1/r (which it cannot — it falls off exponentially).

**Status:** T3 partially addressed (C396). An analog metric was constructed from the
kink background: the position-dependent effective propagation speed V''(phi_bg) =
alpha times (2 - 3 sech²) produces a geometry that confines excitations to the
worldvolume and gives 1/r for localized sources. See Section 5 for details.

### D4-C: Graviton Emergence

**Question:** Does the DFC substrate possess a massless spin-2 mode?

This is the hardest sub-gap. Gravity requires a massless, spin-2 excitation with
exactly two physical polarizations, universal coupling to energy-momentum, and a
1/r potential from its exchange.

The substrate field phi is a scalar. A scalar field has a rank-2 energy-momentum
tensor, but that does not make the scalar a spin-2 particle. The actual question is
whether **collective excitations** of the DFC substrate can transform as a massless
spin-2 representation.

This is where C393 delivered a key negative result. The linear response kernel of the
substrate around its vacuum was computed explicitly. The result: the stress-energy
correlator has a two-particle threshold at twice the sigma mass — **no massless pole**.
The kink zero-mode is massless but scalar (one degree of freedom, not two). No
propagating massless spin-2 mode was found in the scalar substrate spectrum.

This negative result does not kill DFC's gravity program. It tells us that gravity
cannot emerge from the linearized substrate spectrum — it must emerge from a different
mechanism. But it does mean that a direct "graviton from substrate fluctuations"
approach is obstructed.

**C398 Update:** The gravitational wave polarization problem was stress-tested.
Candidate A (composite tensor from scalar gradients) was proven to fail — the
tensor d_mu(dphi) d_v(dphi) is purely longitudinal for any plane wave and has zero
spin-2 content. Candidate B (spin-2 from worldvolume gauge fields) is viable: the
16 SU(3) gauge DOF produce spin-2 through their tensor products (1 tensor 1 = 0+1+2),
and the Sakharov induced gravity mechanism generates a standard Einstein-Hilbert
action whose linearized fluctuations have exactly two transverse-traceless
polarizations propagating at c. The scalar breathing mode is Planck-mass-gapped
and unobservable at LIGO frequencies.

**Status:** T3 (Candidate B structurally viable; coupling-dependent). The polarization
problem is downgraded from "critical tension" to "coupling-dependent" — the mechanism
exists, the remaining question is whether the non-perturbative 93% preserves the
tensor structure.

### D4-D: Coupling Emergence

**Question:** What is the numerical value of G_N in terms of alpha and beta?

Even if gravity emerges through some mechanism, the coupling strength must be predicted.
The scalar zero-mode exchange between two kinks gives an effective gravitational
coupling G_eff = G_N/22.9 for extended (sech⁴) sources, with the profile factor
(I_6/I_4)² = 16/25 accounting for the source profile. The enhancement factor F =
(25/12) times 4 pi xi = 22.87 has been verified exactly. The total perturbative
account is approximately 6.7% of G_N. The remaining approximately 93% is
non-perturbative.

**C397 Update:** The full worldvolume Green's function was computed as a mode sum
over the Poeschl-Teller spectrum. The n=1 bound state contributes zero (odd parity,
vanishes at y=0). The continuum contributes less than 6% at the kink center and is
exponentially suppressed beyond 2 xi. The perturbative total of 6.72% is confirmed
robust. Self-gravitational energy |U_self|/E_kink = 59 >> 1 confirms the deep
nonlinear regime.

**Status:** T1 (scalar fraction and mode sum verified exactly). T4 for the full
non-perturbative coupling.

---

## 3. What Has Been Established (C366b–C395)

### The Scalar Fraction (C367, C392)

The sech-integral hierarchy was computed exactly using Fraction arithmetic:

I_4 = 4/3,  I_6 = 16/15,  I_8 = 32/35,  I_10 = 256/315,  I_12 = 512/693

The scalar zero-mode exchange between kinks gives G_eff = G_N/23, where the
enhancement factor F = (25/12) times 4 pi xi = 22.87. The rational prefactor
25/12 equals I_4 cubed over I_6 squared — a pure sech-integral identity. This
is T1 exact.

A key finding: the profile ratio (I_10/I_6)² = 0.58, which is less than 1. This
means that the sech⁸ graviton vertex profile is **narrower** than the sech⁴ scalar
vertex. Profile effects **reduce** rather than enhance the coupling. So even if a
spin-2 mode existed, its coupling would be weakened by the kink profile, not
strengthened.

### The Wrong-Sign Problem and Its Resolution (C393, C394)

**C393 — The key negative result.** The linear response kernel of the substrate was
computed explicitly. Two critical findings:

1. The stress-energy correlator T_muv–T_muv has a two-particle threshold at 2 times
   m_sigma (twice the sigma mass), with **no massless pole**. There is no propagating
   massless spin-2 mode in the scalar substrate.

2. The Sakharov induced gravity mechanism was tested in 1+1 dimensions. The one-loop
   effective action from integrating out substrate modes was computed. The result:
   M_eff² = -0.145 in Planck units — **wrong sign**. A negative induced Planck mass
   squared means the effective gravitational action has the wrong sign for stable
   gravity. In 1+1D, the bubble integral is logarithmically divergent and can produce
   either sign depending on the mass spectrum.

**C394 — The resolution.** The wrong-sign problem was resolved by moving to 4D.
The worldvolume of a DFC kink (domain wall) is 3+1 dimensional. In 4D, the
Schwinger proper-time formula gives F(m, Lambda) = integral from 1/Lambda² to
infinity of ds/s² times exp(-m²s). For any mass m (including m=0), this integral
equals Lambda² — always positive. The quadratic divergence in 4D is universally
positive, unlike the logarithmic divergence in 1+1D.

The worldvolume spectrum was identified: 8 gauge bosons (massless, 16 degrees of
freedom from SU(3)), 1 translational zero mode (massless, 1 DOF), and 1 shape mode
(massive at m_shape = sqrt(3) times m_KK, 1 DOF). Total: 17 massless + 1 massive
DOF. The induced Planck mass squared from these modes is:

M²_ind = (17 + 1 correction) × Lambda² / (16 pi²) = 2.35% of M_Pl²

This is positive (correct sign) and accounts for 2.35% of the observed Planck mass.
Combined with the scalar zero-mode fraction (4.4%), the total perturbative account
is about 6.7% of G_N. The remaining approximately 93% is non-perturbative.

### The Dimensional Bridge (C366b)

A quantitative bridge was found between the gravitational, substrate, and inertial
scales. The ratio of the Schwarzschild radius of a Planck-mass object to the kink
width equals sqrt(2 alpha), which is exactly the Compton angular frequency omega_c
of the kink. This identity — r_s(M_Pl)/xi = omega_c — connects the gravitational
scale (r_s), the substrate scale (xi), and the inertial scale (omega_c) through a
single algebraic relation. This is T1 exact.

### BPS and Self-Gravity (C366b)

The kink has energy E_kink = 36 pi M_Pl and width xi = 0.874 l_Pl. Its
Schwarzschild radius r_s = 2 G_N E_kink = 226 l_Pl is vastly larger than its width.
If interpreted as an ordinary gravitating object using standard GR, the kink lies
deep inside its own gravitational radius.

This is not merely "strong self-gravity." It creates a fundamental consistency test.
Either standard gravitational reasoning fails at the D4 scale, or the kink's
gravitational mass differs from its field energy, or the effective gravitational
coupling is scale-dependent, or the kink is not a conventional localized object.

---

## 4. Conceptual Reframing (C395b–C396): Gravity Is Compression Geometry

Cycles C392–C395 approached the D4 gap from the conventional physics direction:
looking for graviton-like modes, computing Sakharov induced gravity, analyzing
spectral densities. This produced useful bounds (the perturbative sector accounts
for only ~7% of gravity) but was asking the wrong question from DFC's perspective.

DFC does not claim gravity is a force mediated by spin-2 particle exchange.
DFC claims gravity is what the substrate's natural compression looks like from
within the compressed state. Where there are more closures, the substrate
compresses differently. That differential compression IS gravity.

This means:
- The C393 result (no massless spin-2) is **expected**, not problematic
- The 93% "non-perturbative remainder" is not missing physics — it IS the
  primary mechanism (compression geometry), with the perturbative 7% being
  small corrections
- The right question is not "where is the graviton?" but "how does non-uniform
  compression create effective geometry?"

C396 turned this conceptual reframing into a concrete calculation.

---

## 5. The C396–C399 Breakthroughs

### C396: The Analog Metric — Gravity from Position-Dependent Speed

The kink background phi_bg(y) = phi_0 tanh(y/xi) modifies the effective
propagation speed for small perturbations. The effective "mass-squared" seen by
fluctuations is V''(phi_bg) = alpha times (2 - 3 sech²(y/xi)). This function
is positive far from the kink (propagation allowed) and dips negative near it
(binding region). It defines a position-dependent geometry.

**Key result:** The transverse potential is **linear** — it describes a domain
wall that confines excitations to the worldvolume with constant acceleration
g = 710 per Planck length. This is the D3 localization mechanism: the kink
itself produces the confinement that makes three apparent spatial dimensions.

**The 1/r result:** For **localized** sources on the wall (closures = particles),
the effective gravitational potential falls off as 1/r. This is not imposed —
it follows from the dimensionality of the worldvolume. A 3-dimensional Laplacian
has Green's function 1/(4 pi r), so any localized source interacting through a
field on the wall produces a 1/r potential automatically.

This is the first time 1/r has been derived rather than assumed in DFC. It is
not gravity yet — the coupling coefficient and spin-2 structure are separate
questions — but the spatial dependence emerges from the substrate geometry.

The profile ratio I_8/I_4² = 18/35 sets the coupling for this channel. The
Shapiro time delay is positive and decreasing with frequency, qualitatively
correct. The Born approximation overestimates the phase by a factor of 2,
indicating a strong-potential regime.

### C397: The Full Mode Sum — Quantifying What Perturbation Theory Can See

With the analog metric in hand, the next step was to compute the complete
perturbative Green's function by summing over all Poeschl-Teller modes.

The kink's transverse fluctuation spectrum has:
- A zero mode (n=0): massless, sech² profile — this is the translational mode
- A bound state (n=1): massive at sqrt(3/2) times m_KK, with a sech times tanh
  profile — this is the shape mode, **odd** in the transverse coordinate

Because the n=1 mode is odd, it vanishes at y=0 (the kink center). Its
contribution to the Green's function between symmetric sources is exactly zero.
The continuum modes (above the gap at 2 times m_KK) contribute less than 6% at
the kink center and are exponentially suppressed beyond 2 times xi.

The result: G_eff = G_N/22.9 for extended (sech⁴) sources, with the profile
factor (I_6/I_4)² = 16/25 = 0.64 accounting for the source distribution. The
Jormungandr self-consistency formula F = 150 pi sqrt(2)/alpha^(7/2) = 22.87 was
verified exactly.

The self-gravitational energy tells a dramatic story. The ratio |U_self|/E_kink =
59, far greater than 1. This means the kink's own gravitational self-energy (even
using only the perturbative fraction) exceeds its rest energy by a factor of 59.
The system is inherently non-perturbative — no finite number of perturbative
corrections can account for the full gravitational coupling. The 93% non-perturbative
fraction is not an error bar; it is the dominant physics.

### C398: The Polarization Problem — How Tensor Gravity Emerges from a Scalar

General relativity predicts two transverse-traceless tensor polarizations for
gravitational waves: the + and cross modes observed by LIGO. DFC's compression
field phi is a scalar. How does a scalar substrate produce tensor gravitational
waves?

C398 stress-tested two candidate mechanisms:

**Candidate A (composite tensor):** Build a tensor from scalar gradients,
d_mu(dphi) d_v(dphi) / phi_0². This object is a rank-2 tensor, but for any
plane wave delta phi proportional to exp(ikx), it is **purely longitudinal** —
all transverse components vanish identically. A scalar field's energy-momentum
tensor has zero spin-2 content. This is a theorem, not a numerical result.
Candidate A fails.

**Candidate B (worldvolume gauge fields):** The kink's moduli space is SU(3),
giving 16 gauge degrees of freedom on the worldvolume. Each gauge field is
spin-1. The tensor product of two spin-1 representations decomposes as
1 tensor 1 = 0 + 1 + 2 — producing spin-2 content. The Sakharov induced gravity
mechanism integrates out these worldvolume fields to generate an effective
Einstein-Hilbert action. The linearized fluctuations of this induced metric have
exactly two transverse-traceless polarizations propagating at c. Candidate B is
viable.

The scalar substrate also has a breathing polarization mode, but it is gapped
at the Planck mass (m_sigma = sqrt(2 alpha) approximately 2.3 M_Pl). At LIGO
frequencies of 10 to 1000 Hz, this mode is exponentially damped — only tensor
polarizations propagate to the detector, consistent with observations.

This is a structural resolution, not a complete derivation. The remaining question
is whether the non-perturbative 93% of the gravitational coupling preserves the
tensor structure that the perturbative 7% produces.

### C399: 1/r Verified Across Intermediate Scales

The final module of the gravity spoke stress-tested the 1/r result at intermediate
distances — the regime between the kink width xi and asymptotically large separations.

**Result:** 1/r is exact to machine precision across more than 7 orders of magnitude,
from 0.01 xi to 10⁶ xi. The logarithmic derivative d(ln G)/d(ln r) = -1.000 to
10⁻⁹ at all tested points. This is not approximately 1/r — it is exactly 1/r, because
it follows from the dimensionality of the worldvolume (3D Laplacian), not from any
approximation.

The effective coupling G_eff converges to its asymptotic value G_N/22.9 within 0.1%
at r = 10 xi. The continuum modes, which could in principle modify the power law,
are suppressed by less than 10⁻¹⁰ at 10 xi. At intermediate distances r comparable
to xi, there are small deviations from the asymptotic G_eff (the continuum contributes
up to 6%), but the power law remains exactly 1/r throughout.

Newton's law V(r) = -G_eff M₁ M₂ / r was verified for the DFC system. The deep
nonlinear regime (r_s/xi >> 1) was confirmed — the kink sits far inside its own
gravitational radius, and the perturbative gravitational dynamics do not capture
this regime.

---

## 6. The Current Landscape After C399

### What the C396–C399 breakthroughs established

The analog metric approach (Option 1 from the original assessment) has been pursued
and has produced concrete results:

1. **1/r derived, not assumed.** The spatial dependence of gravity follows from
   worldvolume dimensionality — the Green's function of a 3D Laplacian is 1/(4 pi r).
   This is T1.

2. **Perturbative sector fully characterized.** The complete mode sum gives
   G_eff = G_N/22.9 with no remaining perturbative corrections to compute. The
   continuum is negligible. This is T1.

3. **GW polarizations structurally explained.** Worldvolume gauge fields produce
   spin-2 through tensor products. The scalar breathing mode is Planck-mass-gapped.
   This is T3 (viable mechanism, coupling-dependent).

4. **Deep nonlinear regime confirmed.** Self-gravitational energy 59 times the
   kink rest energy. The perturbative fraction is inherently limited to ~7%.

### What remains open

The Sakharov/perturbative channel (Option 2) is complete. The analog metric
(Option 1) has been explored and yields 1/r with a coupling that is 1/22.9 of
the observed value. The remaining 93% requires one of:

**Jormungandr Self-Consistency (highest potential).** The kink's gravitational
self-energy exceeds its rest energy by 59 times. This means the kink cannot exist
without accounting for its own gravity. A self-consistency equation — requiring
that the kink's gravitational back-reaction reproduces the potential V(phi) that
produced the kink — would close the loop. This is the Jormungandr fixed-point
equation (C400, planned).

**Strong-Field Boundary Condition.** The kink sits deep inside its own gravitational
radius (r_s/xi = 259). Standard GR cannot apply at this scale. The kink IS the
boundary between the two wells of V(phi), analogous to an Einstein-Rosen bridge.
The BPS bound corresponds to the extremal black hole bound. Connecting these
structures could produce G_N as a derived quantity.

**Lattice/Numerical.** Compute the full nonlinear substrate response numerically
and extract the effective metric coefficient.

---

## 7. Honest Assessment

### What is established

| Result | Tier | Source |
|---|---|---|
| xi approximately l_Pl (structural identification) | T1 | C366b |
| omega_c = sqrt(2 alpha) as Compton frequency | T1 | C366b |
| BPS saturation: KE = V_ren at each point | T1 | substrate.md |
| alpha times G_N = cuberoot(18) (consistency relation) | T1 | C366b |
| F = (25/12) times 4 pi xi = 22.87 exact decomposition | T1 | C392 |
| Profile narrowing reduces coupling: (I_10/I_6)² = 0.58 | T1 | C392 |
| No massless spin-2 mode in scalar substrate | T1 | C393 |
| Sakharov wrong-sign resolved in 4D | T1 | C394 |
| Continuum spectral correction negative, -0.22% | T1 | C395 |
| Analog metric: transverse confinement (domain wall) | T1 | C396 |
| 1/r from worldvolume dimensionality (3D Laplacian) | T1 | C396, C399 |
| Full mode sum: G_eff = G_N/22.9 for extended sources | T1 | C397 |
| Profile factor (I_6/I_4)² = 16/25 exact | T1 | C397 |
| n=1 bound state zero at y=0 (odd parity) | T1 | C397 |
| 1/r exact across 7+ orders of magnitude | T1 | C399 |
| G_eff convergence within 0.1% at 10 xi | T1 | C399 |
| Candidate A (composite tensor) FAILS: purely longitudinal | T1 | C398 |
| Candidate B (worldvolume gauge fields) VIABLE: spin-2 via 1 tensor 1 | T3 | C398 |
| Scalar breathing mode Planck-mass-gapped | T1 | C398 |
| M²_ind = 2.35% of M_Pl² from worldvolume modes | T3 | C394 |
| Total perturbative fraction approximately 6.7% | T3 | C395, C397 |
| Non-perturbative fraction approximately 93% | T3 | C395, C397 |
| Self-gravitational energy |U_self|/E_kink = 59 >> 1 | T3 | C397 |

### What is open

| Gap | Status | Difficulty |
|---|---|---|
| D4-A: Absolute scale generation | T4 open | High |
| D4-B: Analog metric from compression | T3 partially addressed | Moderate — 1/r derived |
| D4-C: Spin-2 polarizations | T3 coupling-dependent | Candidate B viable |
| D4-D: Full coupling coefficient (93% non-perturbative) | T4 open, PRIMARY | High — Jormungandr path |
| Jormungandr fixed-point equation | T4 open, NEXT | Very high |

### What "D4 Closed" would mean

Not merely finding G_N = cuberoot(18)/alpha (which is dimensional fitting). Five
requirements, all needed:

1. **Scale:** M_Pl = f(alpha, beta) derived from dynamics
2. **Geometry:** g_muv = g_muv[phi, d phi, ...] explicit construction — **partially addressed (C396)**
3. **Propagation:** Massless long-range mode with two spin-2 polarizations — **structurally viable (C398)**
4. **Coupling:** Universal coupling to energy-momentum — **open**
5. **Coefficient:** G_N = f(alpha, beta) with predicted coefficient — **open (93% non-perturbative)**

Progress since the original assessment: items 2 and 3 have moved from "T4 open" to
"T3 partially addressed." The primary remaining challenge is item 5 — accounting
for the non-perturbative 93% of the gravitational coupling.

---

## 8. Why This Is Hard — and Why It Matters

The D4 gap is the deepest gap in DFC for a reason. Every other force in the model
emerges from the **internal** structure of kinks — their winding, topology, and
closure behavior at different compression depths. Gravity is different: it is not
an internal property of a kink but the **response of the substrate itself** to the
presence of energy.

The other forces are about what kinks do to each other. Gravity is about what energy
does to the substrate. This requires understanding the substrate at a level deeper
than the kink solutions that sit on top of it.

### What C392–C399 changed

The first phase (C392–C395) asked the conventional question: "where is the graviton
in the substrate spectrum?" and found it was not there. This was the right question
to eliminate: DFC never claimed gravity works through particle exchange. Establishing
this took four modules and produced the definitive answer — the perturbative channel
accounts for exactly 6.7% of gravity, no more.

The second phase (C396–C399) asked the DFC-native question: "how does the kink's
compression geometry produce 1/r?" and found the answer — worldvolume dimensionality.
A localized source on a 3-dimensional wall produces a 1/r potential as a consequence
of the Green's function of the 3D Laplacian. The spatial dependence of gravity is
derived, not assumed.

The gravitational wave polarization question was also addressed: the scalar substrate
cannot produce spin-2 modes directly (proven), but the worldvolume gauge fields can
(structurally viable). The scalar breathing mode is gapped at the Planck mass and
invisible at detector frequencies.

### What remains

The gap has narrowed from "how does gravity work in DFC?" to "how does the non-
perturbative 93% of the gravitational coupling arise?" This is still a hard problem,
but it is now a **quantitative** problem rather than a **conceptual** one. The
mechanism is identified (compression geometry on the worldvolume). The spatial
dependence is derived (1/r exact). The polarization structure is structurally viable
(worldvolume gauge fields). What is missing is the full coupling strength.

The Jormungandr fixed-point equation is the most promising path. The kink's self-
gravitational energy exceeds its rest energy by a factor of 59. This means the kink
cannot exist self-consistently without accounting for its own gravity. A fixed-point
condition — requiring that the gravitational back-reaction reproduces V(phi) — would
close the loop and determine the full coupling.

If DFC can close this loop, it will be the first framework to derive all four forces
from a single starting point without pre-existing spatial dimensions or gauge groups.
If the 93% cannot be accounted for, gravity may require additional structure beyond
the double-well potential.

Either result is scientifically valuable. The D4 gap is no longer the frontier in
the dark — it is a well-characterized quantitative challenge.

---

**See also:** `foundations/d4_gravity_gap.md` for the full technical analysis.
`foundations/jormungandr_double_well.md` for the cyclical compression hypothesis.
`equations/d4_gravity_spin2_enhancement.py` (C392) for the spin-2 enhancement analysis.
`equations/d4_substrate_response.py` (C393) for the key negative result.
`equations/d4_induced_gravity_worldvolume.py` (C394) for the worldvolume Sakharov
calculation. `equations/d4_continuum_spectral_gravity.py` (C395) for the continuum
spectral density analysis. `equations/d4_analog_metric.py` (C396) for the analog metric
construction and 1/r derivation. `equations/d4_worldvolume_green.py` (C397) for the full
perturbative mode sum and self-energy quantification. `equations/d4_gw_polarization_test.py`
(C398) for the GW polarization stress test. `equations/d4_1r_intermediate_test.py` (C399)
for the 1/r verification across intermediate scales. `equations/d4_zero_mode_gravity.py`
(C367) for the scalar zero-mode calculation. `equations/d4_gravity_dimensional.py`
(C366b) for dimensional analysis and the omega_c bridge.
`phenomena/gravity/gravitational_waves.md` for the GW polarization problem update.
