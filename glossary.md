# Glossary — Plain Language Reference

This document explains every mathematical symbol, term, and phrase used in this project.
No prior knowledge assumed. Written to build understanding, not to impress.

**Living document:** Updated whenever a new term or symbol appears in the project.
Entries are organized by category, then alphabetically within each category.

---

## How to Use This

If you see something in a document and don't know what it means, look it up here.
If it's not here yet, it should be added.

Some terms appear with a DFC note — this is what the term means *specifically in this
model*, which may differ from or extend the standard meaning.

---

## Part 1 — Mathematical Symbols

### Basic Operations and Relations

**=** (equals)
Two things have the same value. 3 = 3.

**≈** (approximately equal)
Close to, but not exact. π ≈ 3.14159.

**≡** (defined as / identically equal)
"This is defined to be that." When you see A ≡ B, it means A is just another name for B
by definition, not a result that had to be derived.

**∝** (proportional to)
"Grows at the same rate as." If A ∝ B, then doubling B doubles A. The actual numbers
may differ — it says the *relationship*, not the *value*.

**~** (of order / rough proportionality)
Even rougher than ≈. "Of the same ballpark." 10⁴⁴ ~ 10⁴⁵ in the sense that both are
enormously large compared to everyday numbers.

**>**, **<** (greater than, less than)
Standard comparison. τ > 10³⁴ years means the lifetime exceeds 10³⁴ years.

**≫**, **≪** (much greater than, much less than)
Not just bigger — vastly bigger. c ≫ v means the speed is tiny compared to light.

**→** (approaches / tends toward)
Used two ways:
- In limits: "as x → 0" means "as x gets closer and closer to zero"
- In reactions: p → π⁰ + e⁺ means "a proton transforms into a pion and a positron"

**∞** (infinity)
Without end or limit. A lifetime τ = ∞ means the particle never decays.

---

### Powers and Notation

**xⁿ** (x to the power n)
x multiplied by itself n times. 10³ = 1000. 10⁻³ = 0.001.

**√x** (square root of x)
The number that, when multiplied by itself, gives x. √9 = 3.

**eˣ** or **exp(x)** (exponential function)
The number e ≈ 2.718 raised to the power x. Grows extremely fast. exp(10) ≈ 22,000.
exp(−x) is very small for large x — this is how exponential suppression works.

**ln(x)** (natural logarithm)
The inverse of exp: ln(exp(x)) = x. ln(1) = 0, ln(e) = 1.
Used to measure "how many powers of e." Also written log(x) in physics contexts.

**log₁₀(x)** (base-10 logarithm)
How many powers of 10. log₁₀(1000) = 3. Used to handle enormous numbers:
log₁₀(10⁴⁴) = 44.

---

### Greek Letters Used as Symbols

Greek letters are used constantly in physics as variable names. Here is every one used
in this project:

**α (alpha)**
In this project: the compression field's "stiffness" parameter — controls how steep
the buckling potential is. Also used generally for coupling constants (how strongly
things interact).

**β (beta)**
In this project: the compression field's "self-limiting" parameter — prevents φ from
growing without bound. Together α and β define the shape of the buckling potential.

**γ (gamma)**
Not used as a variable much, but Γ (capital Gamma) is the decay rate (how fast
something decays).

**Γ (capital Gamma)**
Decay rate — how many decay events occur per second. τ = 1/Γ (lifetime is the inverse
of decay rate).

**δ (delta, lowercase)**
A small change or perturbation. δφ means "a small deviation of φ from its stable value."

**Δ (capital Delta)**
A difference or uncertainty. Δx = uncertainty in position. Δt = a time interval.

**ε (epsilon)**
A small number. Often used for a tiny correction: w = −1 + ε means "very close to −1."

**η (eta)**
Efficiency (as in Carnot efficiency). Also used for viscous damping in mechanics.

**θ (theta)**
An angle. In this project: the fold orientation angle — the direction the compression
fold is pointing. This IS the quantum phase.

**κ (kappa)**
A rate constant. In mass hierarchy: κ = 5.33, the rate at which mass increases per
depth level in the dimensional stack.

**λ (lambda)**
Wavelength — the spatial distance between two peaks of a wave.
Also used for coupling constants.

**Λ (capital Lambda)**
The cosmological constant — the energy of empty space that drives the universe's
accelerating expansion.

**μ, ν (mu, nu)**
Index labels. G_μν means "the component of G with row μ and column ν." These are
just bookkeeping labels for which component of a multi-component object you mean.

**ξ (xi)**
Coherence length or correlation length — how far a field's organized structure extends
before it randomizes.

**ρ (rho)**
Density — how much of something per unit volume. ρ_matter = mass per unit volume.

**σ (sigma)**
Stress tensor component. Also used for cross-section (how likely a collision is).

**τ (tau)**
Lifetime — how long something lasts before decaying. τ_proton > 10³⁴ years.

**φ (phi)**
In this project: the compression field itself — the fundamental object the model is
built on. φ(x,t) is the field value at position x and time t.

**ψ (psi)**
The quantum wavefunction — the slow-varying envelope that emerges from the compression
field in the nearly-stable regime. ψ satisfies the Schrödinger equation.

**ω (omega, lowercase)**
Angular frequency — how fast something oscillates, measured in radians per second.
Related to regular frequency ν by ω = 2πν.

**Ω (capital Omega)**
The number of accessible configurations — how many ways a system can be arranged while
still looking the same from the outside. Central to entropy: S = k_B ln(Ω).

---

### Calculus Symbols

**∂ (partial derivative)**
How much a quantity changes when you vary just one thing while holding everything else
fixed. ∂φ/∂t means "how fast φ changes with time, holding position fixed."

**∇ (nabla / del)**
The spatial gradient — combines all the partial derivatives in space into one symbol.
∇φ points in the direction φ increases fastest.

**∇² (Laplacian)**
∇ applied twice — measures how "curved" a field is at a point. If φ is higher at a
point than its surroundings, ∇²φ < 0. Central to wave equations.

**∫ (integral)**
The area under a curve — accumulates a quantity over a range.
∫₀^∞ f(x) dx means "add up f(x) for every x from 0 to infinity."

**d/dx, df/dx (derivative)**
How fast f changes as x changes. df/dx = 3 means "f increases by 3 for every 1 increase
in x."

---

### Vector and Matrix Notation

**Bold letters (A, B)** or **letters with arrows (→A)**
A vector — a quantity with both magnitude and direction.

**|ψ|** (absolute value / magnitude)
The size of ψ, ignoring its direction or phase. If ψ = A e^{iθ}, then |ψ| = A.

**|ψ|²** (magnitude squared)
The square of the magnitude. In quantum mechanics, this gives the probability of
finding the particle at a given location (the Born rule).

**⟨A⟩ or ⟨ψ|A|ψ⟩** (expectation value)
The average value of A across all possible outcomes, weighted by their probability.
"What you expect to measure on average."

**[A, B]** (commutator)
A×B − B×A. If [A,B] = 0 they commute (order doesn't matter). If [A,B] ≠ 0, they
don't — and two quantities that don't commute have an uncertainty relation between them.

**Σ (capital Sigma)**
Sum over many terms. Σᵢ xᵢ means "add up all the x's."

**∏ (capital Pi)**
Product over many terms. ∏ᵢ xᵢ means "multiply all the x's."

---

### Complex Numbers

**i** (imaginary unit)
The square root of −1. i² = −1. Complex numbers have a real part and an imaginary part.

**e^{iθ}** (complex exponential / Euler's formula)
e^{iθ} = cos(θ) + i·sin(θ). A complex number of magnitude 1 pointing at angle θ.
This is how oscillations and phases are written compactly.

**Re[z]** (real part)
The non-imaginary component of a complex number. Re[3 + 2i] = 3.

**Im[z]** (imaginary part)
The imaginary component. Im[3 + 2i] = 2.

---

## Part 2 — Physical Constants

These are fixed numbers set by nature. They appear throughout the equations.

**c — speed of light**
c = 3 × 10⁸ m/s. The speed at which light (and the compression field in its massless
mode) propagates. Nothing with mass can reach it. In DFC: c is the natural propagation
speed of the compression field substrate — not a speed limit imposed from outside.

**ℏ (h-bar) — reduced Planck's constant**
ℏ = h/2π = 1.055 × 10⁻³⁴ J·s. Sets the scale of quantum effects — how large the
"graininess" of nature is. When ℏ appears, you're in quantum territory.

**h — Planck's constant**
h = 2πℏ = 6.626 × 10⁻³⁴ J·s. Appears in E = hν (energy of a photon).

**G — Newton's gravitational constant**
G = 6.674 × 10⁻¹¹ m³/(kg·s²). Sets how strong gravity is. Appears in F = GMm/r².

**k_B — Boltzmann's constant**
k_B = 1.38 × 10⁻²³ J/K. Converts between temperature and energy. Appears in
S = k_B ln(Ω) and thermal energy ~ k_B T.

**G_F — Fermi constant**
G_F = 1.166 × 10⁻⁵ GeV⁻². Sets the strength of the weak nuclear force.
Appears in the neutron lifetime calculation.

**M_Planck — Planck mass**
M_Pl = 1.22 × 10¹⁹ GeV. The mass at which gravitational and quantum effects become
equally important. The compression field buckles at this scale.

**L_Planck — Planck length**
L_Pl = 1.6 × 10⁻³⁵ m. The smallest meaningful length scale — below this, the smooth
field description breaks down. In DFC: the width of a minimal stable kink.

---

## Part 3 — Core Mathematical Concepts

**Differential equation**
An equation that relates a quantity to its own rate of change. The compression field
equation ∂²φ/∂t² = c²∇²φ − V'(φ) is a differential equation: it says "how φ changes
depends on how φ is already varying in space and its potential."

**Wave equation**
A differential equation whose solutions are waves — oscillating, propagating patterns.
∂²φ/∂t² = c²∇²φ is the wave equation. Solutions are φ = A·cos(kx − ωt).

**Potential V(φ)**
A function that encodes how the field "wants" to behave. The field moves toward lower
potential, like a ball rolling downhill. The shape of V determines whether the field
has stable resting states, oscillates, or buckles.

**V'(φ) (derivative of the potential)**
The slope of V at a given φ. This is the "force" that pushes φ. Where V'(φ) = 0,
the field is at rest (a stable or unstable equilibrium).

**Stable minimum**
A value of φ where V is at a local low point (like a valley). The field naturally
settles here. φ₀ = ±√(α/β) are the stable minima of the compression field potential.

**Unstable equilibrium**
A balance point where the field could rest, but any tiny push sends it away (like a
ball balanced on top of a hill). φ = 0 is an unstable equilibrium of the buckling potential.

**Linearization**
Approximating a complicated equation by a simpler one that holds when deviations are
small. If φ = φ₀ + δφ with δφ small, you can drop terms like (δφ)² and get a linear
equation for δφ. The Schrödinger equation is the linearized limit of the compression
field equation.

**Dispersion relation**
The relationship between frequency ω and wavenumber k for a wave.
- Massless (light): ω = ck — frequency proportional to wavenumber
- Massive (particle): ω² = c²k² + m² — adds a constant offset

From this you get the particle's energy, momentum, and speed.

**Boundary conditions**
Constraints on what a field is allowed to do at the edges of a region. The double-slit
experiment imposes boundary conditions (the field must be zero at the walls, nonzero
at the slits). The interference pattern is the field configuration that satisfies those
conditions.

**Eigenstate / eigenvalue**
An eigenstate of an operator is a state that doesn't change its *type* when the operator
acts on it — it just gets multiplied by a number (the eigenvalue). Energy eigenstates
are states with a definite energy value. Measuring a quantity forces the system into
one of its eigenstates.

**Fourier decomposition**
Any wave pattern can be broken into a sum of pure sine waves at different frequencies.
A sharp pulse has many frequency components; a pure tone has just one.
Position and momentum are Fourier pairs: a sharp position means spread out in momentum,
and vice versa.

**Tensor**
A generalization of vectors to multi-dimensional quantities. A vector has one index
(direction). A tensor can have two or more. G_μν is a tensor with two indices —
it's like a table of values describing the curvature of spacetime at each point.

**Trace**
The sum of the diagonal elements of a matrix/tensor. Often written Tr(A).

**Invariant**
A quantity that doesn't change when you change your reference frame or coordinate system.
Physical laws are written in terms of invariants — that's how you know they hold
everywhere.

---

## Part 4 — Quantum Mechanics Terms

**Wavefunction ψ**
A mathematical object that encodes everything knowable about a quantum system. It is
complex-valued (has magnitude and phase). |ψ(x)|² gives the probability of finding
the particle at position x. In DFC: ψ is the slow-varying envelope of the compression
field around its stable minimum.

**Superposition**
A quantum system can be in a combination of multiple states simultaneously — until a
measurement forces it into one. The wavefunction adds the contributions of each state.
In DFC: this is the linear regime of the compression field, where small perturbations
coexist without buckling.

**Schrödinger equation**
iℏ ∂ψ/∂t = [−ℏ²/2m ∇² + V] ψ. The equation governing how ψ evolves over time.
Linear and reversible — no collapse built in. In DFC: derived from the compression
field equation in the near-equilibrium, small-perturbation limit.

**Klein-Gordon equation**
(∂²/∂t² − c²∇² + m²c⁴/ℏ²) φ = 0. The relativistic wave equation for a massive field.
The Schrödinger equation is the non-relativistic, low-energy limit of this.
In DFC: the linearized compression field equation around φ₀ is the KG equation.

**Commutation relation [x̂, p̂] = iℏ**
Position and momentum operators don't commute: measuring x then p gives a different
result than p then x. This non-commutativity is the mathematical source of the
uncertainty principle. In DFC: derived as a mathematical identity from the NR
decomposition — not postulated.

**Uncertainty principle Δx·Δp ≥ ℏ/2**
You cannot simultaneously know position and momentum to arbitrary precision. The more
precisely you know one, the less precisely you can know the other. This is not about
clumsy measurements — it is a property of the field itself. In DFC: a kink cannot
simultaneously have sharp position (small spatial extent) and small momentum (low energy).

**Born rule**
The probability of measuring outcome x is P(x) = |ψ(x)|². The squared magnitude of
the wavefunction gives the probability. Standard QM takes this as a postulate.
In DFC: detection rate is proportional to local field energy density — the Born rule
follows from the thermodynamics of kink nucleation.

**Collapse / measurement**
When a quantum system is measured, the wavefunction "collapses" to a definite outcome.
Standard QM has no mechanism for this — it is just a rule. In DFC: collapse is kink
nucleation — the field crosses the buckling threshold and locks into a stable localized
state.

**Decoherence**
The process by which a quantum system loses its "quantum-ness" through interaction with
its environment. Phases become scrambled, superpositions appear to collapse, quantum
interference disappears. In DFC: uncontrolled mutual compression between the system
field and environmental fields.

**Density matrix ρ**
A more general description of a quantum state than the wavefunction — handles mixtures
of states (when you don't know exactly which state the system is in). Off-diagonal
elements (ρ₁₂) represent coherence — they go to zero as decoherence occurs.

**Hilbert space**
The mathematical space of all possible quantum states. States are vectors in this
space. Operators (like position and energy) act on these vectors.

**Hermitian operator**
An operator whose eigenvalues are always real numbers. Physical observables (things
you can measure) must be Hermitian — you can't measure an imaginary position.

**Unitary evolution**
The Schrödinger equation preserves the total probability (the "length" of the state
vector doesn't change). This is called unitary evolution. It is reversible.
Measurement (buckling) breaks unitarity — it is irreversible.

**Entanglement**
Two particles are entangled when their quantum states cannot be described independently.
Measuring one instantly determines something about the other, regardless of distance.
In DFC: entanglement is global field correlation — the two particles are part of the
same globally connected compression field configuration.

**Coherence / coherence length**
A measure of how well a wave's phase is defined over distance or time. High coherence
= well-defined phase relationships. Low coherence = scrambled phases, no interference.

**QND — Quantum Non-Demolition measurement**
A measurement of one observable (e.g. energy) that leaves the conjugate observable
(e.g. phase) undisturbed. Used to repeatedly measure the same quantity without
destroying it. In DFC: compression targeted at one dimensional layer without disturbing
the perpendicular degrees of freedom.

**Quantum Zeno effect**
Frequent measurement of a quantum system prevents it from evolving. "A watched pot
never boils." In DFC: each measurement triggers a buckling event that resets the field,
suppressing evolution if resets happen faster than the natural evolution rate.

---

## Part 5 — Particle Physics Terms

**Gauge boson**
A particle that carries a force. The photon carries electromagnetism, the W and Z carry
the weak force, gluons carry the strong force. In DFC: gauge bosons are excitations of
the closure topology at each depth (D5, D6, D7).

**Gauge group / gauge symmetry**
The mathematical symmetry that determines which gauge bosons exist and how they couple.
The Standard Model gauge group is U(1) × SU(2) × SU(3).

**U(1)**
The simplest gauge group — a circle of symmetry (rotations in one plane). Generates
one gauge boson: the photon. In DFC: the closure topology formed at D5.

**SU(2)**
"Special Unitary group of dimension 2." Generates three gauge bosons: W⁺, W⁻, Z.
These carry the weak force. In DFC: the closure topology at D6 (the S³ geometry).

**SU(3)**
"Special Unitary group of dimension 3." Generates eight gluons that carry the strong
force. In DFC: the closure topology at D7.

**U(1) × SU(2) × SU(3) — the product group**
The Standard Model gauge group. A direct product means the three groups are independent
— no boson crosses between them. In DFC: three independent closure events at D5, D6,
D7 with no shared topology between them.

**Coset**
When a smaller group H sits inside a larger group G, the "leftover" part G/H is called
the coset. In SU(5) GUT theories, the X and Y bosons live in the coset
SU(5)/(SU(3)×SU(2)×U(1)) — they are what's "extra" compared to the Standard Model.
In DFC: no such coset exists because there is no larger enclosing group.

**Representation (of a group)**
A way of realizing a group's symmetry through matrices acting on a vector space.
The "fundamental representation" of SU(3) has dimension 3 — this is why quarks come
in three colors.

**Quark**
A fundamental constituent of protons and neutrons. Comes in 6 types (up, down, strange,
charm, bottom, top) and 3 colors. Carries color charge (SU(3)) and weak isospin (SU(2)).

**Lepton**
A fundamental particle that does NOT carry color charge — electrons, muons, tau, and
their neutrinos. Interacts via weak force and (if charged) electromagnetism, but not
the strong force.

**Baryon**
A particle made of three quarks. Protons and neutrons are baryons. Baryon number B
counts how many baryons minus antibaryons exist.

**Baryon number B / lepton number L**
B = (number of baryons) − (number of antibaryons). L = (number of leptons) − (number
of antileptons). In the Standard Model these are approximately conserved. In DFC:
the product group structure absolutely forbids gauge interactions that change B at
the expense of L.

**Leptoquark (X and Y bosons)**
Hypothetical particles in GUT theories that could turn quarks into leptons (or vice
versa), enabling proton decay. They live in the coset of SU(5).
In DFC: these particles do not exist — there is no coset because there is no larger
enclosing group.

**Proton decay**
The hypothetical process p → π⁰ + e⁺ (proton → pion + positron). Requires a quark to
turn into a lepton, which requires a leptoquark carrier. Never observed.
In DFC: structurally impossible — no carrier can bridge D7 (SU(3)) to D5 (U(1)).

**Feynman diagram**
A pictorial shorthand for calculating the probability of a particle physics process.
Each diagram represents one term in the calculation. "Tree-level" means the simplest
diagram; "loop-level" means including quantum corrections.

**Tree-level**
The leading-order (simplest) calculation in quantum field theory, ignoring quantum loop
corrections. For the neutron lifetime, tree-level gives τ ≈ 912 s; with radiative
corrections (+3.9%) this becomes ≈ 880 s ≈ observed.

**Radiative corrections**
Small quantum corrections to tree-level results, arising from virtual particles in
loops. Typically a few percent. The neutron lifetime gets a +3.9% correction.

**Fermi's constant G_F**
A number that encodes the effective strength of the weak force at low energies.
Appears in the formula for neutron decay rate.

**CKM matrix (V_ud, etc.)**
The "Cabibbo-Kobayashi-Maskawa" matrix. Encodes how likely a quark of one type is to
transform into a quark of another type via the weak force. V_ud ≈ 0.974 is the
element relevant to neutron decay (up↔down quark transition).

**g_A — axial coupling**
A number (≈ 1.276) that modifies the weak force interaction in nucleons, accounting
for the fact that protons and neutrons have internal structure. Appears in the
neutron lifetime formula alongside G_F.

**Sphaleron**
A specific type of quantum tunneling event in the electroweak theory (SU(2) sector)
that violates baryon number B and lepton number L, but preserves B−L. Relevant at
very high temperatures (early universe). At room temperature, exponentially suppressed
to essentially zero.

**GUT — Grand Unified Theory**
A class of theories that embed U(1)×SU(2)×SU(3) inside a single larger group (like
SU(5)). Predicts proton decay. Minimal SU(5) was ruled out in the 1980s.
In DFC: GUT unification is structurally absent — the three gauge groups arise as
independent closures, not as subgroups of a larger group.

**Effective field theory (EFT)**
An approximation valid below some energy scale, where you don't need the full
high-energy theory. At low energies, weak interactions are described by Fermi theory
(an EFT) rather than the full W-boson theory.

**Dimension-6 operator**
In EFT, an operator whose effects are suppressed by 1/M² for some large mass scale M.
Proton decay via leptoquarks would arise from a dimension-6 operator suppressed by
1/M_X². In DFC, no such operator exists — the coupling is exactly zero, not suppressed.

---

## Part 6 — Gravity and Cosmology Terms

**General Relativity (GR)**
Einstein's theory of gravity. Mass-energy curves spacetime; objects follow the
straightest possible paths (geodesics) through that curved geometry. In DFC: an
accurate description of what happens in the D3 localization layer when stable closures
create gradients in the compression rate.

**Einstein field equations: G_μν = (8πG/c⁴) T_μν**
The central equations of GR. Left side (G_μν): how spacetime is curved. Right side
(T_μν): how mass-energy is distributed. In DFC: T_μν encodes dimensional stabilization;
G_μν encodes the resulting pattern of differential compression rates.

**Metric tensor g_μν**
A table of numbers at each point in spacetime that tells you how to measure distances.
In flat empty space it's simple; near a mass it becomes curved. In DFC: emerges from
the compression field configuration.

**Geodesic**
The "straightest possible path" through curved spacetime. Objects with no forces acting
on them follow geodesics — this is what we call "free fall" under gravity.

**Gravitational redshift**
Light loses energy climbing out of a gravitational well — its frequency drops (shifts
toward red). In DFC: the compression gradient changes the effective field propagation
conditions, reducing the wave's oscillation rate.

**Gravitational waves**
Ripples in spacetime caused by accelerating masses. Detected by LIGO. Propagate at c.
In DFC: propagating perturbations of the compression gradient field.

**Schwarzschild radius / event horizon**
The radius at which a mass M creates an event horizon — the boundary inside which
nothing can escape. For Earth's mass: ~9 mm. For a black hole: this is its "surface."
In DFC: the radius at which the compression rate exceeds the field's propagation speed.

**Hawking radiation**
Thermal radiation emitted by black holes due to quantum effects near the event horizon.
In DFC: compression gradient at the horizon allows lower-dimensional modes to become
partially stabilized just outside and escape as radiation.

**Bekenstein-Hawking entropy**
The entropy of a black hole is proportional to its horizon area (not its volume).
S = A/(4 L_Pl²). This is the holographic bound — the amount of information in a region
scales with its surface area, not its volume. In DFC: follows from the number of
independent compression field modes within the radius.

**Cosmological constant Λ**
The energy density of empty space. Drives the accelerating expansion of the universe.
In DFC: the residual compression pressure from the compression budget — the universe's
total compression that hasn't been captured into stable structure.

**Hubble constant H₀**
The current rate of expansion of the universe: ~70 km/s/Mpc (kilometers per second
per megaparsec). There is currently a ~10% disagreement between different measurement
methods — called the Hubble tension. In DFC: the ε correction to w_Λ ≈ −0.993
accounts for this.

**Friedmann equations**
The cosmological equations governing how the universe's scale factor a(t) evolves.
The universe's expansion history. In DFC: the cosmological limit of the compression
gradient dynamics.

**Equation of state w**
Describes what a substance "does" — how its pressure relates to its energy density.
w = 0: matter (no pressure). w = 1/3: radiation. w = −1: cosmological constant.
DFC predicts w_Λ = −1 + ε with ε ≈ 0.007 (slightly above −1, potentially observable).

**Scale factor a(t)**
The "size" of the universe at time t, relative to today (a = 1 now). a < 1 in the
past (universe was smaller), a > 1 in the future (universe will be larger).

---

## Part 7 — Thermodynamics Terms

**Entropy S = k_B ln(Ω)**
A measure of disorder, or more precisely, the number of ways a system can be arranged
internally (Ω) while looking the same from outside. Higher Ω = higher entropy.
In DFC: Ω counts distinct compression field configurations that produce the same
macroscopic state.

**The laws of thermodynamics**
- Zeroth: temperature is a well-defined property that equalizes between connected systems
- First: energy is conserved — it changes form, never disappears
- Second: entropy never decreases in an isolated system (disorder only grows)
- Third: absolute zero temperature cannot be reached in finite steps

**Temperature T**
A measure of how vigorously a system's internal degrees of freedom are fluctuating.
In DFC: T = m_eff ⟨(∂φ/∂t)²⟩ / k_B — temperature is the average kinetic energy of
compression field oscillations that haven't successfully closed into stable structure.

**Absolute zero**
The lowest possible temperature — where all thermal motion stops. Cannot be reached.
In DFC: would require perfect dimensional closure (zero degrees of freedom), which is
forbidden because D1 is approached asymptotically but never reached.

**Carnot efficiency η = 1 − T_cold/T_hot**
The maximum fraction of heat that can be converted to work by any heat engine operating
between two temperatures. In DFC: set by the geometry of the folding pathway landscape
— a structural limit, not an engineering one.

**Arrow of time**
The observation that time has a preferred direction: entropy increases toward the
future, not the past. In DFC: the arrow of time IS the direction of increasing Ω_fold
— the direction in which compression field configurations multiply.

---

## Part 8 — DFC-Specific Terms

These terms are specific to this model. They may not appear in standard textbooks.

**D1, D2, D3, D4, D5, D6, D7 — the dimensional stack**
The sequence of structural differentiation levels that emerge from progressive
compression and bifurcation of the compression field:
- D1: the compressed ground state — everything undifferentiated
- D2: the propagation layer — light and massless waves
- D3: the localization behavior — produces what appears as three apparent spatial degrees of freedom
- D4: the inertia layer — where mass and resistance to acceleration arise
- D5: U(1) closure — electromagnetism
- D6: SU(2) closure — weak force
- D7: SU(3) closure — strong force

**Dimension (in DFC)**
Not a direction in space. A degree of structural differentiation that emerges when
energy fields move relative to each other in a way that becomes a distinguishable
property. Dimensions are not given — they emerge from compression events.

**Time (in DFC)**
The axis along which irreversible compression events are recorded. Time is bookkeeping,
not a dimension. It is not a degree of freedom of the field; it is the accumulating
count of events that cannot be undone.

**Compression field φ(x,t)**
The fundamental object of the model — a real-valued scalar field that obeys:
∂²φ/∂t² = c²∇²φ − V'(φ), with V(φ) = −α/2 φ² + β/4 φ⁴.
Everything in the model is made of this field in different configurations.

**Buckling / buckling event**
When the compression field is pushed past the threshold where it can no longer hold
its current configuration. It snaps into a new configuration — a kink. This is how
particles, forces, and measurement outcomes are created.

**Kink solution**
A stable, localized solution of the compression field equation — a region where φ
transitions smoothly from one stable minimum to the other. This is the DFC model of a
particle. Its width is the Planck length; its mass comes from the field's curvature.

**Closure / closure event**
A kink that has wrapped around itself into a stable loop — a topologically protected
structure. Each force arises from a different closure topology at a different depth
(D5, D6, D7).

**Closure topology**
The specific geometric shape of a closure event. U(1) is a circle (D5). SU(2) is a
3-sphere (D6). SU(3) is a more complex structure (D7). The topology determines which
force the closure produces and what charges it carries.

**Product geometry / product group**
The structure U(1) × SU(2) × SU(3) in which each factor is completely independent.
In a product group, no object can carry charge under two different factors simultaneously.
In DFC: this emerges from three independent closure events at different depths with no
shared topological space between them.

**Cross-closure transition**
A hypothetical process that would require a carrier bridging two independent closure
depths — e.g., converting a quark (D7) into a lepton (D5/D6). Structurally forbidden
in DFC because no such carrier exists in a product group.

**Intra-closure transition**
A process that stays within one closure depth — e.g., neutron decay (d→u+W⁻) which
operates entirely within the D6 SU(2) closure. Allowed.

**Compression budget**
The total amount of compression available in a region or system. Energy is the
compression budget. It redistributes, never disappears.

**Compression agitation density**
How vigorously the compression field is oscillating at a point without successfully
closing into stable structure. This is DFC's physical identification of temperature.

**Fold orientation angle θ**
The angle describing which direction a compression fold is pointing in its transverse
plane. In DFC: this IS the quantum phase. A particle's wavefunction ψ = A e^{iθ}
where θ is literally the fold direction. Polarization of light is also fold orientation.

**NR decomposition (non-relativistic decomposition)**
The procedure of writing the compression field as φ = Re[ψ e^{−iωt}], separating the
fast oscillation (at the Compton frequency ω) from the slow envelope ψ. The slow
envelope satisfies the Schrödinger equation. This is how quantum mechanics emerges
from the compression field.

**Compton frequency ω_C = mc²/ℏ**
The natural oscillation rate of a particle at rest — set by its mass. For an electron:
ω_C ≈ 7.8 × 10²⁰ Hz. Far too fast to observe directly. The Schrödinger equation
describes the slowly-varying envelope riding on top of this carrier oscillation.

**Effective mass m_eff = ℏ√(2α)/c²**
The mass of a particle expressed in terms of the compression field parameter α. A
steeper potential (larger α) means a more tightly buckled kink — more energy locked
in, larger mass.

**Folding gradient Φ_fold**
The DFC counterpart of the gravitational potential. A mass creates a compression
gradient in the surrounding field; other structures redistribute along that gradient
(falling toward it). In the weak-field limit: ∇²Φ_fold = 4πG ρ.

**Depth d (in the dimensional stack)**
Which level of the stack a particle reaches. Depth d ≥ 4 = inertial anchoring (mass).
d = 5 = electromagnetic charge. d = 6 = weak isospin. d = 7 = color charge.
A particle's mass depends exponentially on its depth: m(d) ∝ exp(κ·d).

---

## Quick Reference — Frequently Used Equations

| Equation | What it says in plain terms |
|---|---|
| E = mc² | Mass is compressed energy; they convert at rate c² |
| E = hν | A photon's energy equals Planck's constant times its frequency |
| λ = h/p | A particle's wavelength equals Planck's constant divided by its momentum |
| Δx·Δp ≥ ℏ/2 | Position and momentum cannot both be sharp at once |
| S = k_B ln(Ω) | Entropy is the log of the number of internal arrangements |
| E = ℏω | Energy of a quantum is proportional to its oscillation rate |
| p = ℏk | Momentum of a quantum is proportional to its wavenumber |
| τ = ℏ/Γ | Lifetime is inversely proportional to decay rate |
| η = 1 − T_c/T_h | Maximum engine efficiency depends only on the two temperatures |
| ω² = c²k² + m² | KG dispersion: how a massive field's frequency relates to its wavenumber |
| ω = ck | Massless dispersion: frequency proportional to wavenumber (light) |
