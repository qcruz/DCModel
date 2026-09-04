# DFC Naming Conventions: Origins, Issues, and Alternatives

**Status:** Reference document for internal clarity
**Purpose:** Examine the technical terminology used in DFC, trace its origins,
evaluate whether it serves or hinders communication, and document preferred usage.

---

## 1. "Kink" — The Core Object

### Origin
"Kink" is standard terminology in nonlinear field theory and condensed matter physics.
It refers to a topological soliton that interpolates between two degenerate vacua in
a 1+1 dimensional scalar field theory. The term has been used since at least the 1970s
(Dashen, Hasslacher, Neveu 1974; Rajaraman 1982).

The mathematical object is φ_kink(x) = φ₀ tanh(x/ξ), which smoothly transitions from
−φ₀ to +φ₀. It looks like a "kink" in a rope — a localized bend between two
straight segments.

### In DFC
The DFC substrate's fundamental localized excitation IS a kink in the technical sense:
a topological soliton of V(φ) = −α/2 φ² + β/4 φ⁴. The term is mathematically precise.

### Issues
- **"Kink" sounds trivial.** To a non-physicist, a "kink" is a minor flaw in a hose.
  It does not convey the significance of a topologically protected, energy-carrying,
  particle-like excitation.
- **"Kink" is specific to the compression coordinate.** The kink solution is
  one-dimensional along the substrate's compression depth. But the substrate's
  D3 localization behavior produces three apparent spatial degrees of freedom
  on the kink. The kink's worldvolume — the apparent spatial extent of the
  structure — is what observers experience as the physical world.

### Alternative: "Fold"
"Fold" is used in the model's full name (Dimensional Folding Compression) and in
many conceptual descriptions. It has advantages:
- More evocative of the physical picture (substrate folding over itself)
- Accessible to non-specialists
- Consistent with the model's conceptual language

**However:** "Fold" is NOT a standard technical term in field theory. Using "fold"
in equations or formal derivations would confuse physicists who know what a kink is.
The kink solution, kink energy, kink width — these are established terms with
precise mathematical meanings.

### Recommendation
- **In conceptual/educational documents:** Use "fold" or "closure" for the physical
  picture. Introduce "kink" as the mathematical name when equations appear.
- **In equation modules and formal work:** Use "kink" exclusively. It is the correct
  technical term.
- **Never use "kink" without context** in documents aimed at general audiences. Always
  define it on first use: "a kink — a stable, localized bend in the substrate field
  that serves as the mathematical model for a particle."

---

## 2. "Closure" — Stable Topological Configuration

### Origin
DFC-specific term. Not standard in field theory. Introduced to describe what happens
when a buckling mode folds back onto itself and becomes self-reinforcing.

### In DFC
A closure is a stable, localized folding configuration satisfying the loop consistency
condition (Postulate 4). Kinks are the simplest closures. Higher-dimensional closures
(D5 U(1), D6 SU(2), D7 SU(3)) are more complex self-referencing structures.

### Issues
- "Closure" has many meanings in mathematics (topological closure, algebraic closure)
  and everyday language (psychological closure). Context usually disambiguates, but
  it can be confusing in mathematical writing.
- The term is well-chosen for the physical concept — something that "closes" on itself.

### Recommendation
- Keep using "closure" in DFC-specific contexts. Define clearly on first use.
- Avoid in formal mathematical writing where it might conflict with standard meanings.

---

## 3. "Depth" / "D-labels" (D1-D7)

### Origin
DFC-specific. The depth metaphor comes from compression depth — how far the substrate
has compressed from its undifferentiated D1 state.

### In DFC
D1 through D7 label different compression thresholds where new behaviors emerge.
They are NOT layers, NOT dimensions, NOT separate spaces. They are markers for
behaviors of one continuous object at different compression levels.

### Issues
- **"Depth" implies layering.** Despite explicit warnings, readers (and even the
  model's own documentation) sometimes slip into treating D-labels as discrete layers.
  The CLAUDE.md language rules exist specifically to combat this.
- **The numbering suggests ordering is physical.** D5 < D6 < D7 suggests D5 is
  "less deep" than D7. This is the intended meaning, but the numbers are arbitrary
  labels — we could have called them Stage A, Stage B, Stage C.
- **D1-D4 are underdeveloped.** D5-D7 have concrete mathematical content (gauge
  groups, coupling constants). D1-D4 are more conceptual (precursor state, wave modes,
  localization, inertia). This asymmetry can make the model appear to have more
  structure than it has proven.

### Recommendation
- Continue using D-labels but always with the caveat that they are provisional markers.
- Consider whether "compression threshold" or "CT-label" would be less misleading
  than "depth" — though "depth" is more intuitive.

---

## 4. "Substrate"

### Origin
From the Latin "substratum" — that which lies beneath. Used in philosophy (Locke,
Aristotle) for the underlying reality behind appearances. In materials science,
a substrate is the base material on which other things are built.

### In DFC
The substrate is the one thing that exists. Everything else — particles, forces,
spacetime — is behavior of this substrate.

### Issues
- "Substrate" implies something that supports other things — as if particles are
  "on top of" the substrate. In DFC, particles ARE substrate configurations. There
  is nothing on top; there is only the substrate in different states.
- The term is well-established in DFC documentation and would be costly to change.

### Recommendation
- Keep "substrate" but be precise: "particles are substrate configurations" not
  "particles exist on the substrate."

---

## 5. "Compression"

### Origin
Standard English. In DFC, it refers to the substrate's tendency to reduce its
configurational freedom — to fold inward, becoming more constrained.

### Issues
- "Compression" in physics usually means reducing volume. In DFC, it means reducing
  degrees of freedom (dimensional reduction). These are related but not identical
  concepts.
- The connection to dimensional reduction is not always clear to readers.

### Recommendation
- When precision matters, say "configurational compression" or "dimensional
  compression" to distinguish from spatial compression.

---

## 6. "Buckling"

### Origin
Engineering term — when a structural element under compression suddenly deforms
sideways (Euler buckling of a column). Used in DFC for the instability that opens
new degrees of freedom when compression exceeds a threshold.

### Issues
- Excellent analogy. Buckling is physically intuitive and technically precise.
- The analogy breaks slightly because engineering buckling is a failure mode,
  while DFC buckling is a feature — it prevents singularities and generates
  structure.

### Recommendation
- Keep "buckling." It is the best available term for this concept.

---

## 7. "Fold Interaction" (replacing "Force")

### Origin
DFC-specific. Introduced to replace "force" when describing U(1), SU(2), SU(3)
interactions, because DFC claims these are not three separate forces but three
interaction behaviors between different fold topologies of one object.

### Issues
- "Fold interaction" is descriptive but unfamiliar. Physicists will need to map it
  back to "force" to understand what is being discussed.
- The term correctly avoids the implication that three separate things were unified.

### Recommendation
- Use "fold interaction" in DFC-native contexts. Use "force" with scare quotes or
  qualifiers ("what appears as the strong force") when communicating with physicists.

---

## 8. Other Terms Worth Noting

| Term | Origin | DFC Usage | Notes |
|---|---|---|---|
| Hopf fibration | Mathematics (Hopf 1931) | S¹→S³→S⁵ closure sequence | Standard math term, correctly used |
| Casimir | Physics (Casimir operator) | C₂(fund,SU(3)) = 4/3 = I₄ | Standard, correctly used |
| BPS bound | Physics (Bogomolny-Prasad-Sommerfield) | E_kink ≥ |ΔW| saturation | Standard, correctly used |
| Spinodal | Thermodynamics | Collapse instability point | Standard, correctly used |
| Tier | DFC-specific | T0/T1/T2a/T2b/T3/T4 evidence grades | Clear, well-defined |
| Spoke | DFC organizational | Derivation chain extending from V(φ) | Metaphor (see wheel-spoke doc) |
| Budget | DFC-specific | Conserved compression quantity B | Replaces "energy" at pre-spacetime level |

---

## Summary: The Kink vs. Fold Question

The tension between "kink" and "fold" reflects the dual nature of the model:

- **"Kink"** is the *mathematical* name. It connects DFC to 50 years of soliton
  physics, nonlinear field theory, and topological defect literature. Any physicist
  reading a DFC equation module will immediately recognize the object.

- **"Fold"** is the *physical* name. It describes what the substrate is doing — folding
  over itself, creating a localized, stable configuration. It is the right word for
  explaining what DFC claims is happening.

Both are correct. Neither should replace the other. The rule is: **fold for concepts,
kink for equations.** In the model's full name — Dimensional Folding Compression — the
word "folding" correctly describes the physical process. In the equation module
`equations/spin_zero_mode.py`, the word "kink" correctly identifies the mathematical
object.

The model is called DFC (Dimensional Folding Compression), not DKC (Dimensional Kink
Compression), because the physical picture matters more than the mathematical label
when naming a theory.
