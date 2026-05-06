# Phenomenon: Aharonov-Bohm Effect

## One-Sentence Synthesis

> The Aharonov-Bohm effect is the direct physical signature of U(1) holonomy — the
> phase accumulated by a charged compression-field excitation traversing a closed path
> enclosing D5 U(1) flux equals the enclosed flux divided by the fundamental flux quantum,
> multiplied by two pi; the flux quantum itself (h/e) is the minimum U(1) winding unit
> derived from the D5 closure topology, and its exact value follows from the DFC coupling
> chain through β → g² → α_em → e/ℏ.

---

## Observation

An electron beam is split into two paths that travel on opposite sides of a magnetic
solenoid, then recombined on a screen. When the solenoid carries flux Φ, the two paths
interfere with a phase difference proportional to the enclosed flux — even though the
magnetic field B is identically zero on both paths (confined inside the solenoid).

The observable consequences:

**Magnetic Aharonov-Bohm phase:**
The phase difference between the two paths equals the electron charge times the enclosed
magnetic flux, divided by the reduced Planck constant:

```
Δφ_AB = (e/ℏ) × Φ_enclosed = 2π × Φ/Φ₀
```

where the magnetic flux quantum is the elementary charge times Planck's constant divided
by the electron charge:

```
Φ₀ = h/e ≈ 4.13566 × 10⁻¹⁵ Wb    [single-electron flux quantum]
```

When the enclosed flux equals a full flux quantum, the phase shift is 2π — equivalent to
no shift. The fringe pattern returns to its zero-flux configuration with period Φ₀.

**Electric Aharonov-Bohm effect:** An electric potential V applied to a region (with E = 0
inside it) shifts the phase by (e/ℏ) × V × Δt. Same topological origin; time takes the
role of path length.

**Cooper pair flux quantum:** In superconducting loops (Josephson junctions), the relevant
charge carrier is a Cooper pair (charge 2e). The flux quantum is:

```
Φ₀^{SC} = h/(2e) ≈ 2.06783 × 10⁻¹⁵ Wb    [Cooper pair flux quantum, Josephson standard]
```

This is measured to 12 significant figures via the Josephson voltage-frequency relation
V = (2e/h) × f = K_J × f, where K_J = 483 597.848 416 984 GHz/V (CODATA 2018, exact by
definition in the 2019 SI).

**Precision:** The ratio h/e is measured to 3 parts in 10⁹; the ratio h/(2e) is measured
to 1 part in 10⁹ via Josephson standards.

---

## Standard Explanation

In quantum mechanics, a charged particle of charge q moving through a vector potential
A(x) acquires a path-dependent phase. Even when B = ∇ × A = 0 along the path (so the
classical Lorentz force is zero), the gauge potential is physically meaningful:

```
φ_path = (q/ℏ) × ∫_{path} A · dl
```

The phase difference between two paths enclosing a flux Φ equals the line integral
around the closed loop:

```
Δφ = (q/ℏ) × ∮ A · dl = (q/ℏ) × Φ_enclosed    [Stokes' theorem: ∮A·dl = ∫B·dA = Φ]
```

For an electron (q = e): Δφ = eΦ/ℏ = 2πΦ/Φ₀.

The effect demonstrates that the gauge potential A (not the field B) is the fundamental
quantity in quantum mechanics. It is a direct test of U(1) gauge invariance and the
Aharonov-Bohm vector potential cannot be gauged away globally.

---

## Dimensional Folding Explanation

### The D5 U(1) Field and Its Holonomy

In DFC, electromagnetism is the D5 closure behavior of the substrate. The D5 depth produces
a U(1) gauge field — the substrate's vortex phase field θ(x) — as the topological sector
corresponding to winding number in π₁(S¹) = ℤ.

The electromagnetic vector potential A is the connection on the D5 U(1) fiber bundle. Its
physical meaning in DFC: A_μ is the spatial gradient of the D5 phase field θ. The parallel
transport of a charged field around a closed path in the D3 localization layer accumulates
a holonomy — the total phase winding of the D5 θ field enclosed by the path.

The holonomy of A around a closed loop C equals the total D5 U(1) flux through the surface
bounded by C:

```
H(C) = exp(i × e/ℏ × ∮_C A · dl) = exp(i × e/ℏ × Φ_enclosed)
```

This holonomy is not removable by a gauge transformation when the enclosed flux is nonzero —
the D5 vortex (a topological defect with π₁(S¹) = ℤ winding) is threaded through the loop.
No local gauge transformation can remove a global topological winding.

### Why the Flux Quantum Is h/e

The minimum nonzero holonomy that returns the wavefunction to itself (single-valuedness)
requires H(C) = 1, i.e., the phase to be a multiple of 2π:

```
e/ℏ × Φ = 2πn    for n ∈ ℤ
→  Φ_n = n × h/e = n × Φ₀
```

The flux quantum Φ₀ = h/e is therefore the minimum D5 U(1) winding unit that produces an
unobservable (trivial holonomy) phase. Equivalently: Φ₀ is the quantum of D5 magnetic flux.

In DFC, this follows directly from:
- The D5 closure producing a U(1) gauge field (Bottleneck 1 closed, Cycles 59–74)
- The electron carrying unit charge q = e (from SU(2) doublet: Q = T₃ + Y/2; verified
  for first-generation fermions in `phenomena/particle_physics/forces/electroweak.md`)
- The identification e/ℏ as the conversion between D5 phase and observable interference

### Connection to the Coupling Derivation (Bottleneck 2)

The AB phase per unit flux is:

```
γ_per_flux = e/ℏ = 2π/Φ₀ = 2π/(h/e)    [exact definition of Φ₀]
```

In the DFC coupling chain (see `foundations/coupling_derivation.md`):
- β → g² = 8πβ/3 (heuristic compact form)
- g² → sin²θ_W → α_em = g²sin²θ_W/(4π) at M_Z scale
- α_em(0) = e²/(4πε₀ℏc) in SI; in natural units α_em = e² (so e = √α_em)

The holonomy connection provides an independent perspective on g²: the coupling g is the
coefficient that converts unit D5 U(1) winding into observable phase per unit particle
charge. In the D5 vortex picture:

The phase accumulated by a charged D6 zero mode (an electron) traversing a circle of
radius r around the D5 vortex core is:

```
γ_DFC(r) = g × ∫_0^{2πr} ∂_θ A_r dr = g × 2πr × (1/r) = 2πg    [for n=1 vortex]
```

Identifying γ_DFC with the AB phase at r = r_U1 (the D5 U(1) radius):

```
γ_AB = 2π × (Φ/Φ₀) = 2πg × (r/r_U1) × N_winding
```

This connects the holonomy at the U(1) scale r_U1 directly to the gauge coupling g —
the same connection that Bottleneck 2 targets in the form r_U1/λ = 1/(βI₄).

### Why the Effect Requires Zero Field on the Paths

In DFC, the D5 vortex phase θ(x) is the fundamental object. Outside the vortex core,
B = ∇ × A = 0 but θ ≠ const — the phase winds by 2π around the core. The field strength
vanishes but the connection is nontrivial. An electron (D6 zero mode) traversing the region
experiences the D5 phase gradient and accumulates holonomy, even though it never enters
the vortex core where B ≠ 0. This is not paradoxical in DFC: the gauge potential (the D5
phase gradient field) is the physical substrate object; B is its derivative, and a
derivative being zero does not imply the parent field is constant globally.

---

## Formal Equations

### Aharonov-Bohm Phase

The phase difference between two paths enclosing magnetic flux Φ:

```
Δφ_AB = (e/ℏ) × Φ    [AB phase, magnetic]
```

In units of the flux quantum Φ₀ = h/e:

```
Δφ_AB = 2π × (Φ/Φ₀)
```

Interference intensity (two-slit geometry):

```
I(Φ) = I₀ × cos²(Δφ_AB / 2) = I₀ × cos²(π × Φ/Φ₀)
```

### Flux Quanta

Electron (single charge q = e):
```
Φ₀ = h/e = 2πℏ/e ≈ 4.13566 × 10⁻¹⁵ Wb = 4.13566 × 10⁻¹⁵ T·m²
```

Cooper pair (charge q = 2e):
```
Φ₀^{SC} = h/(2e) ≈ 2.06783 × 10⁻¹⁵ Wb    [Josephson flux quantum]
```

General charge q = ne (n integer):
```
Φ₀(n) = h/(ne)
```

### DFC Coupling Chain to Flux Quantum

The flux quantum connects to the DFC coupling chain through:

```
Φ₀ = h/e = 2πℏ/e
e = √(4πα_em ℏ c)    [in Gaussian units: e² = 4πα_em ℏ c]
→  Φ₀ = 2πℏ/√(4πα_em ℏ c) = √(πℏ/α_em c) × (1/√ε₀)   [SI form]
```

In natural units (ℏ = c = 1): e = √(4πα_em), Φ₀ = 2π/e = 2π/√(4πα_em) = √(π/α_em).

From β = 1/(9π) candidate (Cycle 101):
```
g² = 8/27,  sin²θ_W = 0.2312,  α_em(M_Z) = 1/129.6
QED running: α_em(0) = 1/140.1
→  e(0) = √(4π/140.1) = 0.2993 (vs. 0.3028 observed; 1.2% error — same systematic as all DFC EM predictions)
→  α_em(M_Z)^{DFC} = 1/129.55 [from coupling_derivation chain]
→  QED running: Δ(1/α) = 10.46 → α_em(0) = 1/140.0
→  e(DFC) = 1.585 × 10⁻¹⁹ C  (vs 1.602 × 10⁻¹⁹ C observed; +1.1%)
→  Φ₀^{DFC} = h/e(DFC) = 4.180 × 10⁻¹⁵ Wb  (+1.1% from 4.136 × 10⁻¹⁵ Wb)
```

The 1.1% error traces to the same α_em systematic as all DFC electromagnetic predictions
(α_em at M_Z is 1.3% too small; after running to low energy the error is +1.1%).

---

## Consistency Checks

| Prediction | DFC mechanism | Observed | Error | Status |
|---|---|---|---|---|
| AB phase Δφ = eΦ/ℏ exists | U(1) holonomy around D5 vortex flux | Confirmed (Aharonov-Bohm 1959, multiple experiments) | — | Tier 1 structural ✓ |
| Period Φ₀ = h/e | Minimum D5 U(1) winding unit for single charge | 4.13566 × 10⁻¹⁵ Wb (measured to 3 ppb) | — | Tier 1 structural ✓ |
| Cooper pair period h/(2e) | Charge 2e Cooper pair; same U(1) winding | 2.06783 × 10⁻¹⁵ Wb (Josephson standard, exact in 2019 SI) | — | Tier 1 structural ✓ |
| B = 0 on path is irrelevant | D5 phase field θ is the substrate object; ∇×A=0 does not imply θ=const globally | Experimentally confirmed: effect persists when B=0 on paths | — | Tier 1 structural ✓ |
| Integer charge quantization n ∈ ℤ | D5 winding π₁(S¹) = ℤ; D6 zero mode carries integer charge | All observed charges are integer multiples of e/3 (quark color) | — | Tier 1 structural ✓ |
| Φ₀^{DFC} numerical value | β → g² → α_em(M_Z)=1/129.55 → running → α_em(0)=1/140.0 → e → 4.180×10⁻¹⁵ Wb | 4.136 × 10⁻¹⁵ Wb | +1.1% | Tier 2b (same α_em systematic) |
| No free photon magnetic charges (∇·B = 0) | D5 π₂(S¹) = 0 → no magnetic monopoles (see `magnetic_monopoles.md`) | Confirmed — no monopole detected | — | Tier 1 structural ✓ |

---

## Open Questions

1. **Holonomy and the coupling derivation.** The AB phase γ_AB = 2πg at the D5 radius r_U1
   is exactly the quantity that Bottleneck 2 targets. Proving r_U1/λ = πN_Hopf/I₄ from the
   V(φ) field equation would simultaneously derive the AB period Φ₀ from first principles
   (zero free parameters). This is the current highest-priority open derivation.

2. **Non-Abelian Aharonov-Bohm (D6, D7 analogs).** The SU(2) closure at D6 and SU(3) at
   D7 depths should produce non-Abelian holonomy effects — path-ordering of the Wilson loop
   matters, and the gauge holonomy is a matrix rather than a phase. The DFC account of
   non-Abelian AB phases (and whether they produce any testable prediction beyond the
   Standard Model) is unexplored.

3. **Electric AB effect and D4 depth.** The electric AB effect — phase shift from a scalar
   potential V during a time interval Δt even when E = 0 — involves temporal holonomy. In
   DFC, the D4 depth governs inertia and apparent mass. Whether D4 dynamics produce the
   time-component A₀ of the gauge connection in a specific structural way is an open question.

4. **AB effect at D5 vortex scale.** The DFC D5 substrate vortex has core radius r_v ≈ 1.1ξ
   (Cycle 75). At distances r < r_v, the AB treatment (B = 0 on path) breaks down. Whether
   this produces a measurable correction to the AB phase for paths threading DFC vortex
   structure at sub-ξ scales — effectively a DFC-specific AB modification — is open.

---

## Connections

- **U(1) closure and D5 depth** — the structural source of the AB effect;
  `foundations/complex_substrate.md`, `foundations/hopf_fibration_geometry.md`
- **Coupling derivation (Bottleneck 2)** — holonomy at r_U1 connects to g²;
  `foundations/coupling_derivation.md`, `equations/coupling_derivation.py`
- **Magnetic monopoles** — AB effect requires ∇·B = 0; π₂(S¹) = 0 rules out monopoles;
  `phenomena/electromagnetism/magnetic_monopoles.md`, `equations/magnetic_monopoles.py`
- **Josephson effect** — Cooper pair flux quantum h/(2e) from same U(1) winding;
  `phenomena/condensed_matter/josephson_effect.md`, `equations/josephson_effect.py`
- **Superconductivity** — flux quantization Φ₀ = h/(2e);
  `phenomena/condensed_matter/superconductivity.md`, `equations/superconductivity.py`
- **Electric charge quantization** — integer U(1) winding → integer charge;
  `phenomena/electromagnetism/electric_charge.md`
- **Electromagnetic coupling chain** — β → α_em → e → Φ₀;
  `equations/coupling_derivation.py`, `equations/atomic_structure.py`
