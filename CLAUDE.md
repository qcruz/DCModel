# DFC Model — Claude Instructions

This project is a theoretical physics model called **Dimensional Folding Compression (DFC)**.
It proposes that all known physics emerges from a single real scalar compression field φ(x,t)
undergoing a sequence of bifurcation events that produce the dimensional structure of spacetime
and the gauge groups of the Standard Model.

---

## Model Architecture

The dimensional stack (memorize this):

| Depth | Structure | Physics |
|---|---|---|
| D1 | Compressed ground state | Undifferentiated precursor |
| D2 | Propagation | Wave/radiation modes, massless excitations |
| D3 | Localization | 3-space position, particle identity |
| D4 | Inertia | Mass, resistance to acceleration |
| D5 | U(1)_Y closure (S¹) | Hypercharge / electromagnetism |
| D6 | SU(2)_L closure (S³) | Weak force, spin-1/2 from FR + Jackiw-Rebbi |
| D7 | SU(3)_c closure | Strong force, color charge, quark confinement |

Key field: `V(φ) = −α/2 φ² + β/4 φ⁴`, kink solutions φ₀ = ±√(α/β).

---

## Language Rules

These rules are non-negotiable. Enforce them in all documentation.

**Forbidden phrases and their replacements:**

| Forbidden | Replacement |
|---|---|
| "preferred orientation" | "intrinsic orientation" or "orientation defined by the dimensional structure" |
| "forces X into existence" | "produces X" or "X exists as a consequence of" |
| "forces/allows A to B" | "A exists — the structure in which B occurs" |
| "preferred point/direction" | "geometrically distinguished point/direction" (or remove entirely) |
| "energetically preferred" | "energetically stable" |
| "the model prefers / chooses" | passive voice or "the structure produces" |
| Any anthropomorphic agency | Remove or rephrase as structural consequence |

**Reason:** Imprecise language obscures genuine explanatory gaps. If a statement reads as
if the model is making a choice, it is hiding either a derivation that hasn't been done yet
or an assumption that hasn't been acknowledged. Structural language forces the gap to be
visible.

---

## Development Cycle

Repeat this cycle indefinitely:

### Step 1 — Add a New Phenomenon

1. Identify a physics phenomenon not yet in `phenomena/` (or a placeholder needing content).
   Choose one systematically or randomly from the list of unformalized docs.
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
