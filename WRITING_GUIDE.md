# Writing Guide: How to Document Phenomena in This Model

This guide defines the format and voice for all descriptive documents in `phenomena/`.
Read this before writing any new phenomenon explanation.

---

## The Core Rule: Multiple Simultaneous Perspectives

Every phenomenon must be described from at least two perspectives. These perspectives
describe the same underlying process — they are not contradictions or alternatives.

**Why:** The dimensional folding framework has a dual character at its core. Dimensional
closure is binary at the ontological level (a degree of freedom is available or it is not)
but continuous at the physical level (the process unfolds gradually, unevenly, with
gradients). A single description will always miss one of these aspects.

**The stone-and-pond standard:** The clearest benchmark is the stone-in-pond example.
The thrower and the fish are experiencing the same event. Their descriptions sound nothing
alike. Both are complete and accurate. Neither is privileged.

For physics phenomena, the two most natural perspectives are usually:
- **The observer in spacetime** — what instruments measure, what equations describe
- **The dimensional field** — what is happening to the degrees of freedom, the folding
  density, the redistribution of structure

More complex phenomena may require three perspectives.

---

## Document Structure

Each phenomenon document should follow this order:

### 1. Observation
What is actually observed or measured. State it plainly, in physical terms.
No model language yet. Just: what does nature do here?

### 2. The Standard Explanation
How existing theory (GR, QM, QFT, thermodynamics) describes it.
Be accurate and fair. This model does not replace existing mathematics —
it provides a conceptual foundation for why those mathematics take the forms they do.

### 3. The Dimensional Folding Explanation
Restate the phenomenon in dimensional folding language.
Use the pattern-matching vocabulary from `foundations/introduction.md`:
- "folding gradient" not "curvature"
- "loss of degrees of freedom" not "entropy increase"
- "dimensional localization" not "wavefunction collapse"
- "lateral redistribution" not "dissipation"
- etc.

This section should contain at least two perspectives.

### 4. Analogies
One or more concrete physical analogies that make the dimensional mechanism intuitive.
The atmosphere-layer analogy and the stone-pond analogy are the established templates.
Build new analogies in the same spirit: physical, spatial, involving gradients or pressure.

### 5. Connections
How this phenomenon connects to other phenomena in the model.
Every phenomenon is a projection of the same underlying process — name the other
projections explicitly.

### 6. Open Questions
What this phenomenon still does not explain within the model.
Be honest. The model is a scaffold, not a complete theory.

### 7. Equations (when available)
Link to the relevant Python module in `equations/`.
If no equation exists yet, note what would need to be derived.

---

## Voice and Tone

- **Accessible first.** Write for someone who has taken undergraduate physics but is not
  a specialist. Analogies before equations. Intuition before formalism.
- **Precise second.** Every analogy should be followed by a statement of where it breaks
  down or what it does not capture.
- **No overclaiming.** The framework is early-stage. Phrases like "the model suggests,"
  "under this interpretation," and "this remains to be formalized" are appropriate and
  expected.
- **No string theory vocabulary.** Do not use: compactification, extra dimensions (as
  spatial), branes, landscape, Calabi-Yau, fiber bundle (unless in an explicitly
  mathematical context).
- **Use the model's own terms.** Preferred vocabulary:

| Use this | Not this |
|---|---|
| dimensional folding / Dimensional Gravity (DG) | "a force" or "gravity" as fundamental |
| D1 | "the singularity," "the origin," "the pre-universe state" |
| dimensional volume | energy/content of a dimension |
| vertical collapse | entropy (in mechanistic descriptions) |
| lateral redistribution / retiling | dissipation, force exchange, motion (as fundamental) |
| collapse gradient | spacetime curvature (in descriptive prose) |
| dimensional boundary | brane, membrane, surface (string theory vocabulary) |
| dimensional stack | extra dimensions, compactification |
| buckling instability | Big Bang (as a singular one-off event) |
| folding instability / dimensional boundary failure | singularity |
| forced dimensional localization | wavefunction collapse |
| near-pure D2 mode | photon (when describing its dimensional character) |
| stable knot / bottleneck | particle (when describing its origin) |
| boundary-alignment wave | gauge boson (when describing its mechanism) |
| loss of representable structure | entropy increase (statistical sense) |
| density of collapse events per unit time | temperature (when explaining mechanism) |
| structural indeterminacy | randomness / quantum indeterminacy (when explaining origin) |

---

## What to Avoid

- **Treating existing theory as wrong.** It is not. The math works. The model explains
  *why* it works.
- **Single-perspective descriptions.** If you cannot describe a phenomenon from both the
  observer frame and the dimensional field frame, the description is incomplete.
- **Equations without prose.** Every equation in a phenomenon document must be preceded
  by a plain-language statement of what it is measuring and followed by a statement of
  what it means in dimensional folding terms.
- **Isolated phenomena.** Every document must link to at least two other phenomena. The
  model's core claim is that all phenomena are projections of one process. Isolation
  contradicts that claim.

---

## Example Document Skeleton

```markdown
# Phenomenon: [Name]

## Observation
[What is measured/observed. Plain physical terms only.]

## Standard Explanation
[How GR/QM/QFT/thermodynamics describes it. Fair and accurate.]

## Dimensional Folding Explanation

### Perspective 1: From the observer in spacetime
[What the observer sees, restated in folding language.]

### Perspective 2: From the dimensional field
[What is happening to the degrees of freedom and folding structure.]

## Analogy
[One concrete physical analogy. State where it breaks down.]

## Connections to Other Phenomena
- [Phenomenon A] — [how they are the same process from a different angle]
- [Phenomenon B] — [how they are the same process from a different angle]

## Open Questions
[What the model does not yet explain about this phenomenon.]

## Equations
See `../../equations/[module].py`
[Or: equation to be derived — describe what it would need to capture.]
```
