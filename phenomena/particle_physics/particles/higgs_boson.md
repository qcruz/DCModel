# Particle: The Higgs Boson

## One-Sentence Synthesis

> The Higgs boson is the oscillation mode of the compression field along the squashing
> degree of freedom of the D6 S³ closure — physically, it is the breathing mode of the
> geometry whose stable squashing minimum (ε₀ ≠ 0) gives W, Z, and fermion masses; its
> spin-0 nature is the direct consequence of ε being a scalar (the eccentricity of the
> S³ ellipsoid), and its mass m_H = 125.25 GeV is radiatively generated from a nearly-zero
> tree-level quartic — a structural consequence of the Higgs being a metric modulus,
> protected by geometric symmetry at the closure scale.

---

## Observed Properties

```
Mass:             125.25 ± 0.17 GeV  (ATLAS + CMS combined, 2020)
Spin:             0  (scalar — only fundamental spin-0 particle in the SM)
Charge:           0
Parity:           +1  (CP-even at tree level; CP violation in Higgs sector not observed)
Width:            Γ_H = 4.1 MeV  (narrow: m_H ≪ 2m_W, but WW* and ZZ* open)
VEV:              v = 246.22 GeV

Decay branching ratios (dominant):
  H → bb̄           58.2%   (largest: bottom Yukawa y_b = m_b√2/v)
  H → WW*          21.4%   (one W off-shell)
  H → gg            8.2%   (via top quark loop)
  H → τ⁺τ⁻          6.3%
  H → ZZ*           2.6%   (one Z off-shell)
  H → γγ            0.23%  (via W and top loops — discovery channel)

Higgs VEV v = 246.22 GeV sets all SM masses via:
  m_f = y_f v / √2    (fermions)
  m_W = g_W v / 2     (W boson)
  m_Z = m_W / cos θ_W (Z boson)
```

**Why spin 0:** In DFC, the Higgs is the squashing parameter ε — a single real number
measuring the eccentricity of the D6 S³ closure geometry. A scalar deformation parameter
has no directional structure, hence spin 0. All other known fundamental particles are
connection fields (spin 1) or Jackiw-Rebbi zero modes (spin 1/2). The Higgs is the one
exception because it is not a connection field or a fermion — it is the geometry of the
D6 closure itself.

---

## DFC Account

### Origin: ε is the Higgs Field

The full DFC construction is in `foundations/higgs_geometry.md`. The essential point:

The D6 closure has the group manifold of SU(2), which is the 3-sphere S³. This S³ is
not a rigid object — it can deform. The squashing parameter ε measures how far the S³
has deformed from perfect sphericity:

```
ε = 0       →  perfectly round S³, full SU(2) symmetry, all W bosons massless
ε = ε₀ ≠ 0 →  squashed S³, SU(2)×U(1) broken to U(1)_EM, W and Z massive
```

The effective potential V(ε) has a Mexican hat shape:
```
V(ε) = −μ² ε² + λ ε⁴
```

This is not assumed — it emerges from two competing D6 closure geometry effects:
- **D7 SU(3) closure pressure**: the D7 structure exerts a destabilizing geometric
  pressure on the D6 S³ (a negative ε² term), driving ε away from zero
- **S³ curvature resistance**: the S³ resists deformation (a positive ε⁴ term),
  stabilizing the potential at finite ε

The minimum sits at ε₀ = μ/√(2λ), identified with the Higgs VEV v = 246.22 GeV.

### The Higgs Boson: Fluctuation Around ε₀

The Higgs boson is the quantum of the oscillation of ε around ε₀. Write:
```
ε(x,t) = ε₀ + h(x,t) / v        [h(x,t) = Higgs field fluctuation]
```

The mass of h is the curvature of V at the minimum:
```
m_H² = V''(ε₀) = 2μ² = 2λ v²
```

With λ(v) ≈ 0.129 (the physical quartic at the electroweak scale after RG running):
```
m_H = √(2 × 0.129) × 246.22 GeV = 125.1 ± 1.5 GeV    [observed: 125.25 GeV ✓]
```

**Epistemic status:** The match is a consistency identification, not an ab initio
prediction. The boundary condition λ₀ ≈ 0.013 (the quartic at the closure scale) is
currently sourced from SM vacuum stability running (Buttazzo et al. 2013), not derived
from DFC substrate parameters. DFC provides the structural explanation for why λ₀ is
small; computing λ₀ from (α, β, c, d₆) remains open.

### Why the Higgs is Light: The Hierarchy Problem in DFC

In generic quantum field theory, radiative corrections drive the Higgs mass to the
cutoff scale (the Planck scale, ~10¹⁹ GeV). Without cancellation, the observed mass
of 125 GeV requires a fine-tuning of one part in 10³⁴. This is the hierarchy problem.

**DFC structural account:** The Higgs is not a new independent scalar with arbitrary mass.
It is the squashing parameter ε — a metric modulus of the D6 S³ closure geometry. Geometric
moduli are protected by the underlying closure symmetry: at the closure scale M_c, the
quartic self-coupling is suppressed to O(g⁴) ≈ 0.01 rather than O(1) by the gauge-Higgs
unification structure. This is not fine-tuning — it is geometric protection.

The hierarchy between m_H and M_Planck is then explained:
```
m_H² ~ λ(M_c) × v²    with λ(M_c) ~ g⁴/(16π²) ~ 0.01   [suppressed by geometry]
```

rather than:
```
m_H² ~ M_Planck²    [naive without protection]
```

The protection breaks down at m_H — the Higgs boson is the lightest state in the
D6 sector, and below m_H the geometric modulus description must yield to the field-
theoretic description. This is why the Higgs mass is naturally in the 100 GeV range
rather than at the Planck scale.

### Higgs Couplings: Why Proportional to Mass

Every massive particle couples to the Higgs with strength y_f = m_f√2/v. This is the
famous pattern: heavier particles couple more strongly to the Higgs.

**In DFC:** fermion mass = depth-anchoring overlap integral with the D6 squashing field:
```
m_f = y_f v/√2,  where  y_f = g_D6 × ∫ψ̄₀(x) φ_H(x) ψ₀(x) dx
```

The Higgs couples to the fermion with exactly the strength that gave the fermion its
mass — because the Higgs IS the D6 squashing field. Coupling to the Higgs = coupling to
the origin of the fermion's mass. The proportionality y_f ∝ m_f is not a coincidence —
it is structural, following from the Yukawa coupling being the same overlap integral
that determines the fermion mass.

**For gauge bosons:** The W and Z acquire mass by coupling to the Higgs through the
SU(2) gauge coupling g_W. The Higgs-W-W vertex coupling is proportional to m_W² — again
structural, because the W mass IS the S³ squashing resistance.

### The Vacuum Stability Coincidence: Explained

The SM quartic coupling λ(μ) runs to near-zero at μ ≈ 10¹⁰–10¹² GeV (within current
uncertainties, consistent with λ(M_Pl) ≈ 0). This looks like a suspicious coincidence —
why should λ become small at an intermediate scale?

**DFC account:** The tree-level geometric quartic is exactly suppressed at the closure
scale M_c ≈ 10¹⁸ GeV. The near-criticality of the SM vacuum (λ → 0 at high energy)
is the RG footprint of this geometric suppression running down from M_c. The electroweak
vacuum sits near stability because the closure scale boundary condition requires it to.

This is a genuine structural prediction: the scale at which λ crosses zero should
coincide with M_c (within running uncertainties). Precision measurement of the Higgs
quartic running (at a future Higgs factory) could constrain M_c directly.

---

## Formal Equations

### Higgs Potential

```
V(ε) = −μ² ε² + λ ε⁴

Minimum at:   ε₀ = μ / √(2λ)  ≡  v / √2  =  174.1 GeV
VEV:          v = √(μ²/λ) = 246.22 GeV
Quartic:      λ(v) = m_H² / (2v²) = 125.25² / (2 × 246.22²) = 0.1292
```

### Mass Relations (from squashing geometry)

```
m_H = √(2λ) v = 125.25 GeV      ✓
m_W = g_W v / 2 = 80.377 GeV    ✓
m_Z = m_W / cos θ_W = 91.19 GeV ✓
m_f = y_f v / √2                 [fermion masses via Yukawa overlap]
```

### Higgs Production (LHC)

```
Dominant production modes at √s = 13 TeV:
  gg → H (gluon fusion via top loop):    48.6 pb    [largest]
  qq → Hqq (VBF):                         3.78 pb
  qq̄ → WH:                               1.37 pb
  qq̄ → ZH:                               0.884 pb
  qq̄ → tt̄H:                              0.507 pb
```

### RG Evolution (Higgs Quartic)

```
Boundary condition:   λ(M_c ≈ 10¹⁸ GeV) ≈ 0.013  [geometric suppression]
RG evolution:         dλ/d(ln μ) = β_λ  [one-loop SM running]
Physical quartic:     λ(v = 246 GeV) ≈ 0.129

m_H = √(2 × 0.129) × 246.22 GeV = 125.1 ± 1.5 GeV  ✓
```

---

## Consistency Checks

| Property | DFC mechanism | Observed | Status |
|---|---|---|---|
| Spin 0 | ε is a scalar deformation parameter (no directional structure) | 0 ✓ | Structural ✓ |
| Unique scalar | Only D6 S³ has a squashing modulus; no other closure has a scalar mode | 1 Higgs ✓ | Structural ✓ |
| m_H ≈ 125 GeV | λ₀ ≈ 0.013 at closure scale + SM RG running | 125.25 GeV ✓ | Consistency identification |
| Coupling ∝ mass | Yukawa = same overlap integral that determines mass | y_f ∝ m_f ✓ | Structural ✓ |
| No Higgs self-coupling measured deviation | λ triple-H coupling ~ λ(v) ≈ 0.13 | Consistent (HL-LHC: ±20%) | Open — testable |
| Vacuum near-critical | Geometric suppression λ₀ ≈ 0 at closure scale → λ(M_Pl) ≈ 0 | λ(M_Pl) ≈ 0 ✓ | Structural explanation ✓ |
| v = 246 GeV | VEV from α/β ratio; hierarchy problem | Input (not derived) | OPEN |
| λ₀ at closure scale | DFC geometry → 0.013 from substrate (α, β, c, d₆) | Derived from data | OPEN — critical gap |

---

## Open Questions

1. **Derive the Higgs VEV v = 246 GeV from substrate parameters.** In DFC, v = √(α/β) where
   α and β are the substrate potential parameters. In Planck units, v/M_Pl ≈ 2×10⁻¹⁷. Why
   is this ratio so small? This is the DFC form of the hierarchy problem — why is √(α/β)
   so far below M_Planck? This requires understanding why the D6 closure depth anchoring
   produces a VEV at the electroweak scale rather than the Planck scale.

2. **Derive λ₀ ≈ 0.013 from D6 closure geometry.** The tree-level quartic at the closure
   scale is suppressed by the gauge-Higgs unification structure of the S³ modulus. The precise
   value λ₀ = (κ_R − P(ε)κ₄ + κ_R^Cas + κ_R^T) / (R₂⁴ M*⁴ f⁴) requires computing the
   cross-curvature tensor κ₄ from the D5/D6/D7 closure geometry at the closure scale. Until
   this is done, the Higgs mass result is a consistency identification rather than a prediction.

3. **Measure the Higgs triple-coupling at HL-LHC or future Higgs factory.** The DFC prediction
   for the triple Higgs coupling is the SM tree-level value λ_HHH = 3m_H²/v = 192 GeV, with
   a small correction from λ₀/λ(v) ≈ 0.013/0.129 ≈ 10%. This 10% correction would distinguish
   DFC from models that predict O(1) deviations in the triple coupling (SUSY, composite Higgs).
   HL-LHC target precision: ±20% on λ_HHH. A future e⁺e⁻ Higgs factory: ±5%.

4. **Explain the CP structure of the Higgs sector.** The observed Higgs is CP-even. DFC
   assigns ε as a CP-even scalar (eccentricity of S³ has no handedness). But the D6 closure
   is chiral — why doesn't the chirality of S³ induce CP violation in ε itself? The absence
   of Higgs CP violation is a structural DFC prediction (ε is the magnitude of squashing,
   not the orientation) that should be made precise.

---

## Connections

- **Higgs geometry** — D6 S³ squashing as the Higgs field; Mexican hat from geometry;
  `foundations/higgs_geometry.md`
- **Higgs mass derivation** — RG-improved m_H = 125.1 ± 1.5 GeV; boundary condition;
  `foundations/higgs_mass_derivation.md`
- **Mass generation** — gauge boson and fermion masses from Higgs VEV;
  `phenomena/particle_physics/mass_generation.md`
- **W/Z bosons** — direct products of S³ squashing; m_W = g_W v/2;
  `phenomena/particle_physics/particles/w_z_bosons.md`
- **Weak force** — S³ closure that squashes; parity violation;
  `phenomena/particle_physics/forces/weak_force.md`
- **Three generations** — depth-anchoring gives three Yukawa scales;
  `foundations/three_generations.md`
- **Mass hierarchy** — depth-anchoring formula m_f ∝ exp(κd_f) links to v;
  `foundations/mass_hierarchy.md`
