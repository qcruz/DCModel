### II.E. Compression budget (units/meaning)

**Postulate 5 (Budget conservation):** Define a compression budget B as an extensive scalar bookkeeping quantity:

B ≡ ∫_Σ ρ_B(φ, ∇φ, ...) dV

with ρ_B a model-dependent density functional. B is intended to track how "stored compression capacity" is partitioned among closures (mass-like), coherent transport (radiation-like), and incoherent agitation (heat-like).

Dimensional analysis suggests B should scale as [action] or [energy × time] to be consistent with quantum mechanics, or alternatively as [length × curvature] to align with gravitational coupling. In the toy model (§IV), B naturally emerges with dimensions of [energy], but a complete theory would need to specify how this quantity relates to ℏ, c, and G. For this draft, B is treated as dimensionally consistent with energy while acknowledging that the precise identification remains open.

---

## III. DFC interpretive dictionary (expanded mapping table)

Table 1 provides a compact mapping between standard physical concepts and their DFC interpretations. These are interpretive correspondences, not derivations.

**Table 1. DFC interpretive mapping to standard physics quantities**

| Standard concept | DFC interpretation |
|-----------------|-------------------|
| Mass (m) | Stable localized closure storing budget B |
| Energy density | Observable proxy for local budget density ρ_B |
| Curvature | Irreducible misalignment of folding orientation after transport |
| Gravity | Coherent re-tiling / alignment field induced by closure density |
| Radiation | Coherent propagating redistribution of budget |
| Heat | Incoherent agitation of folding modes |
| Entropy (S) | ∝ ln Ω(φ), multiplicity of accessible fold configurations |
| Gauge symmetry | Redundancy in parameterizing internal folding orientation |
| Horizon | Boundary where alignment propagation cannot keep pace with re-tiling / buckling |

---

## IV. Minimal mathematical toy model (illustrative formalization path)

This section addresses the "mathematical substance" requirement while remaining explicitly toy and non-claiming. The point is to show that the compression–buckling–closure language can be expressed in standard dynamical terms.

### IV.A. 1D compression field with buckling potential

Let φ(x,t) be a scalar "compression field." Consider generic Klein–Gordon-type dynamics:

∂²φ/∂t² = c² ∂²φ/∂x² - dV/dφ

with a symmetry-breaking ("buckling") potential

V(φ) = -(α/2)φ² + (β/4)φ⁴,     α > 0, β > 0

**Interpretation:**

- The negative quadratic term (−α/2)φ² encodes a drive toward nonzero compression (asymptotic bias away from φ = 0).
- The quartic term (+β/4)φ⁴ prevents divergence by creating an energy cost for unbounded φ.
- The system has degenerate minima at φ = ±√(α/β), representing two locally stable "fold orientations."
- The potential barrier height is V(0) − V(φ_min) = α²/(4β), setting a characteristic energy scale for closure stability.

### IV.B. Closure analogs as kink solutions

This model admits kink/domain-wall solutions interpolating between minima. In DFC language, these are stable localized configurations that persist and carry an associated conserved energy functional:

E[φ] = ∫ dx [½(∂φ/∂t)² + ½c²(∂φ/∂x)² + V(φ)]

The static kink solution interpolating between the two vacuum states has the explicit form:

φ_kink(x) = √(α/β) tanh[(x − x₀)/λ]

where λ = √(2c²/α) sets the kink width and x₀ is the kink center. The associated energy is:

E_kink = (4/3)c√(2α³/β)

which is finite, localized, and topologically protected—the kink cannot continuously deform to the uniform vacuum φ = ±√(α/β) without passing through the unstable point φ = 0.

**DFC interpretation:** Localized energy/structure of a kink is an analog of closure—a stable configuration storing "budget" that can move, interact, and radiate small perturbations.

### IV.C. Why this matters (and what it does not do)

This does not "derive particles," gravity, or the Standard Model. It demonstrates only that:

1. "Compression bias + buckling regularization" naturally yields stable localized objects (closures).
2. "Radiation vs heat" can be conceptualized as coherent excitations vs incoherent dispersal about such structures.
3. The same language can be made operational in a minimal dynamical system.

---

## V. Dimensional analysis and scale hierarchy

DFC requires consistency with known characteristic scales, even if it does not predict them.

### V.A. Candidate identification of a compression length

If compression becomes dynamically dominant below a length ℓ_c, a conservative consistency anchor is ℓ_c ~ ℓ_P, since this is where quantum and gravitational effects are expected to jointly matter. This is a dimensional-consistency suggestion, not a claim.

### V.B. Emergent hierarchy (qualitative)

**Planck regime (ℓ ~ ℓ_P):** Substrate micro-dynamics dominate. Buckling thresholds and closure formation rules operate. In the toy model, this corresponds to scales where λ_kink (kink width) approaches ℓ_c.

**Atomic regime (ℓ ~ 10⁻¹⁰ m):** If stable closures manifest as particles, their effective sizes and interaction strengths would be determined by the specific closure topology and the way multiple closures modify each other's folding environment. DFC does not yet predict these scales but requires consistency with observed atomic structure.

**Cosmological regime (ℓ ~ Gpc):** Global stress relief manifests as expansion. If the compression budget B scales with the total spatial volume V as B ∝ V^(1−δ) for some δ > 0, then stress accumulation naturally drives expansion. The relationship to the observed Hubble parameter H(t) requires specifying how local compression density couples to the expansion rate—an open problem listed in §X.

---

## VI. Strengthened interpretive mapping (showing more "work" qualitatively)

### VI.A. General Relativity (more specific mapping target)

DFC's "re-tiling" aims to correspond to the way stress–energy sources curvature in GR. The intended qualitative correspondence is:

- closure density → effective geometric response (curvature)
- alignment transport → connection/parallel transport structure
- saturation thresholds → avoidance of singularities via instability

A minimal post-diction target is that Schwarzschild-like behavior emerges as the scale where alignment propagation cannot keep up with the re-tiling demand induced by a closure, yielding an effective horizon. (This is positioned as an interpretive target; not derived here.)

### VI.B. Quantum mechanics (complex amplitudes as a gap, acknowledged)

DFC interprets superposition as an unresolved folding configuration constrained by boundary interactions. However, DFC in this draft does not explain:

- why amplitudes are complex
- why dynamics take the Schrödinger form
- how ℏ enters

These are listed explicitly as formalization requirements: any serious DFC model must show how a complex Hilbert-space structure emerges (or explain why it is assumed).

**Path toward resolution:** A promising direction would be to show that the phase of the compression field φ naturally complexifies when accounting for the full dynamical constraint structure, similar to how the WKB approximation generates complex phases from real action functionals. However, deriving the full Schrödinger equation would require:

1. identifying the configuration space over which path integrals are taken
2. showing how the compression budget couples to this path integral measure
3. deriving the specific iℏ ∂/∂t operator structure from substrate dynamics

This is acknowledged as a critical gap that must be filled before DFC can claim to provide a substrate interpretation of quantum mechanics rather than merely a classical field analog.
