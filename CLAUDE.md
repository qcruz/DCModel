# DFC Model — Claude Instructions

This project is a theoretical physics model called **Dimensional Folding Compression (DFC)**.
It proposes that all known physics emerges from a single substrate — one object that is
stretched, twisted, folded, and knotted — whose motion and self-interaction produce all
cosmological phenomena. There are no pre-existing spatial dimensions. What appears as
"3D space," "spacetime," or "gauge structure" is the downstream appearance of the substrate's
configuration at different depths of folding. The substrate is the only thing that exists.

---

## Model Architecture

The substrate is one continuous object. The D-labels below are **working markers** for
depth behaviors observed on that object — not discrete layers, not separate spaces, and
not fixed ontological boundaries. The substrate at any depth can curl, twist, wrap back,
inherit properties from adjacent depths, or produce closure configurations not yet identified.

The current working map (provisional — depth assignments under exploration):

| Depth marker | Current working hypothesis | Apparent physics |
|---|---|---|
| D1 | Maximum compression — undifferentiated | Precursor state |
| D2 | First propagation behavior emerges | Wave modes, massless excitations |
| D3 | Localization behavior emerges | Apparent position, particle identity |
| D4 | Inertia behavior emerges | Apparent mass, resistance to change |
| D5 | U(1)-type closure behavior | Hypercharge / electromagnetism |
| D6 | SU(2)-type closure behavior | Weak force, spin-1/2 |
| D7 | SU(3)-type closure behavior | Strong force, color |

**Critical:** The D5=U(1), D6=SU(2), D7=SU(3) assignments are correspondences under
active exploration, not established derivations. The substrate may produce these behaviors
through winding, wrapping, or curling configurations that overlap depth ranges. Discovering
which configuration actually reproduces the observed values — while obeying the core
mechanics of compression — is a primary research goal.

Key field equation: `V(φ) = −α/2 φ² + β/4 φ⁴`, kink solutions φ₀ = ±√(α/β).

---

## Language Rules

These rules are non-negotiable. Enforce them in all documentation.

**Forbidden phrases and their replacements:**

| Forbidden | Replacement |
|---|---|
| "preferred orientation" | "intrinsic orientation" or "orientation defined by the substrate configuration" |
| "forces X into existence" | "produces X" or "X exists as a consequence of" |
| "forces/allows A to B" | "A exists — the structure in which B occurs" |
| "preferred point/direction" | "geometrically distinguished point/direction" (or remove entirely) |
| "energetically preferred" | "energetically stable" |
| "the model prefers / chooses" | passive voice or "the structure produces" |
| Any anthropomorphic agency | Remove or rephrase as structural consequence |
| "spatial dimensions" (as fundamental) | "apparent spatial degrees of freedom" or "the substrate's localization behavior" |
| "3D space" / "3+1 dimensional spacetime" (as container) | "three apparent spatial degrees of freedom" or "the D3 localization behavior of the substrate" |
| "reconcile with spatial dimensions" | never reconcile — the spatial appearance IS substrate behavior |
| "the D6 layer" / "the D7 sector" (as separate objects) | "D6 depth behavior" / "the substrate at D7 depths" |
| "requires 3 spatial dimensions" | "produces three apparent spatial degrees of freedom" or "the rotation behavior emerging at D3 has [property]" |

**Two foundational rules:**

1. **No spatial dimensions as fundamental.** The substrate is one object. Space is not a
   container the substrate lives in. What appears as three spatial degrees of freedom is
   downstream behavior of the substrate's D3 localization. Never write as if space is
   primary and the substrate secondary.

2. **D-labels are provisional depth markers, not discrete layers.** The substrate can wrap,
   curl, and interact with itself across depths. D5/D6/D7 are working hypotheses about where
   certain closure behaviors emerge. Writing "the D6 SU(2) layer" as if it is a separate
   sealed space is wrong. Write "the D6 depth behavior" or "the substrate's SU(2) closure
   at D6 depths."

**Reason:** Both errors are like insisting on the geocentric model while using the heliocentric
one for calculations — they embed an incorrect ontology that hides the real explanatory gaps.

---

## Development Cycle

Repeat this cycle indefinitely:

### Completeness Estimate (running)

```
Current estimate: ~10%  (viability: ~25%, mathematical rigor: ~8%)
Key bottleneck: D-depth assignment mechanism; first-principles coupling constants; no S-matrix
Next milestone that moves the needle: any single coupling constant derived from (α, β, c, geometry)
```

**Priority weighting for Step 1:** When choosing which phenomenon or foundation doc to work on,
give preferential weight to those that connect to the three critical bottlenecks:

1. **D-depth assignment mechanism** — why does U(1) emerge at D5, SU(2) at D6, SU(3) at D7?
   Prefer docs that explore the substrate's self-interaction structure at these depths, the
   winding/wrapping configurations that produce each closure, or alternative depth orderings.

2. **First-principles coupling constants** — α_em, sin²θ_W, α_s, Yukawa couplings.
   Prefer docs where a coupling constant might be derived from geometric parameters rather
   than taken from experiment. Even partial progress here (e.g. the ratio of two couplings)
   is high-value.

3. **S-matrix / scattering amplitudes from the substrate** — no observable has yet been
   computed from the field dynamics (only from imported equations). Prefer docs that
   connect the substrate dynamics to actual measurable cross-sections or decay rates.

These bottlenecks are the difference between a conceptual framework (~25% viable) and a
predictive, mathematically rigorous theory (~80%+). All other work is valuable but secondary.

---

### Step 1 — Add a New Phenomenon

1. Identify a physics phenomenon not yet in `phenomena/` (or a placeholder needing content).
   Choose one systematically or randomly from the list of unformalized docs, with preferential
   weight toward phenomena that connect to the three critical bottlenecks above.
2. Write the **conceptual document** in `phenomena/` following the standard format:
   - One-Sentence Synthesis (DFC account, not a placeholder)
   - Observation (what is measured/observed)
   - Standard Explanation (SM account, concise)
   - Dimensional Folding Explanation (DFC account — structural, specific, no anthropomorphism)
   - Formal Equations (key equations, even if some are stubs)
   - Consistency Checks table
   - Open Questions (honest about what is not yet derived)
   - Connections (links to related docs)
3. Write or update the **equation module** in `equations/` with numerical verification.
   Every quantitative claim in a phenomenon doc should have a backing Python calculation.
   Run it and record the output in the document.

### Step 2 — Audit a Random Conceptual Document

1. Select a conceptual document (anything in `foundations/` or `phenomena/`) at random.
2. Read it and the corresponding equation modules.
3. Check: do the descriptions and analogies accurately reflect what the math says?
   Flag any of these:
   - Claims that go beyond what equations currently show
   - Language that doesn't match the DFC framework
   - Forbidden anthropomorphic language
   - Derivation steps marked as "established" that are actually assumptions
4. Update the document to match the current state of the model.

### Step 3 — Audit a Random Equation Module

1. Select an equation module in `equations/` at random.
2. Run it. Check:
   - Does it actually produce the claimed outputs?
   - Are failures clearly labeled as failures (not quietly passed over)?
   - Are inputs vs. predictions clearly distinguished?
   - Are all free parameters identified as such?
3. Update the module to reflect any discovered discrepancies or failures.
4. Update the corresponding conceptual docs if the equation reveals a gap or failure.

### Step 4 — Propagate Updates

After any new document or any audit:
1. Update `current_state.md` if a new strength, weakness, or audit result warrants it.
2. Update `MEMORY.md` if any project-level facts have changed.
3. Check whether any linked documents need updating.

Then return to Step 1.

---

## Document Standards

### Conceptual Documents (foundations/, phenomena/)

- The **One-Sentence Synthesis** must state the DFC account, not be a placeholder.
  It should be possible to read this single sentence and understand what DFC says.
- The **Consistency Checks** table must include at least one row marked ✗ if any
  prediction fails or is not yet derived. Honesty about failures is required.
- **Open Questions** must be specific and actionable — not "derive X" but "derive X
  by computing [specific integral/topology] using [specific approach]."
- Never mark something as "established" unless there is a completed equation or
  formal argument. Use "under derivation," "consistent but not derived," or
  "working description" for everything else.

### Equation Modules (equations/)

- Every module must be runnable: `python3 equations/module.py` produces output.
- Distinguish **inputs** (values taken from data) from **predictions** (values computed
  from DFC parameters). Label them clearly in output.
- If a prediction fails, print the failure prominently. Do not hide discrepancies in
  "close enough" rationale without justification.
- All modules should include a docstring explaining: (a) what physical question it
  addresses, (b) what the DFC mechanism is, (c) what the key references are.

---

## What Is Verified vs. Open

Always maintain this distinction explicitly. The model's credibility depends on it.

**Verified (numerically or formally):**
- τ_neutron = 878.4 s (0.1% match) — `equations/proton_stability.py`
- Spin-1/2: FR winding N = 1, BPST zero mode normalizable, J_min = 1/2, Jackiw-Rebbi
  residual ~ 10⁻⁶ — `equations/spin_zero_mode.py`
- m_μ/m_e = 206.77 from R/d ratio — `equations/mass_spectrum.py`
- Q = T₃ + Y/2 for all first-generation fermions — `phenomena/.../electroweak.md`
- H₀ = 67.26 km/s/Mpc (0.2% match) — `equations/cosmology.py`

**Known failures (not yet resolved):**
- τ mass from mass_spectrum.py: predicts 212 MeV, observed 1777 MeV (8.4× off)
- Neutrino depth spacing ratio: 1.34 vs observed 5.71
- Charm/strange quark masses: 15% below observed

**Correspondences (consistent but not derived):**
- D5 ↔ U(1), D6 ↔ SU(2), D7 ↔ SU(3) assignments
- V(φ) = −α/2 φ² + β/4 φ⁴ (postulated, not derived from D1)
- Weinberg angle sin²θ_W ≈ 0.231 (not derived from D5/D6 geometry)

---

## File Structure Reference

```
DCmodel/
├── CLAUDE.md                  ← this file
├── current_state.md           ← living review document, update periodically
├── foundations/               ← core model documents
│   ├── substrate.md           ← φ field, V(φ), kink solutions
│   ├── dimensional_stack.md   ← D1-D7 structure
│   ├── three_generations.md   ← three-generation count from D6 topology
│   ├── spin_emergence.md      ← FR + Jackiw-Rebbi derivation of spin-1/2
│   ├── mass_hierarchy.md      ← dimple + global scale for lepton masses
│   └── higgs_geometry.md      ← S³ squashing as Higgs mechanism
├── phenomena/
│   ├── electromagnetism/      ← EM, electric charge, light
│   ├── particle_physics/
│   │   ├── forces/            ← strong, weak, electroweak
│   │   └── particles/         ← electron, quarks, neutrinos, ...
│   ├── quantum/               ← QM, measurement, interference
│   └── cosmology/             ← expansion, dark matter, baryogenesis
└── equations/                 ← Python modules, all runnable
    ├── proton_stability.py    ← verified
    ├── spin_zero_mode.py      ← verified
    ├── mass_spectrum.py       ← tau mass fails
    ├── quark_masses.py        ← c/s 15% off
    ├── neutrino_masses.py     ← depth ratio off
    └── cosmology.py           ← largely consistent
```
