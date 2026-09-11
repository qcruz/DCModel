# T4 Stagnation Audit

**Purpose:** Honestly assess all items that have remained at Tier 4 (structural
gap — mechanism identified but quantitative derivation missing or failing badly)
for an extended period. Items stuck at T4 for 100+ cycles are candidates for
honest flagging as likely unresolvable within the current framework.

**Standard:** Each item is assessed on three axes:
1. **Duration** — how many cycles at T4
2. **Trajectory** — improving, flat, or deteriorating
3. **Verdict** — PROGRESSING, STALLED, or FLAG (likely unresolvable)

**Last comprehensive review:** Cycle 584

---

## Items Recently Upgraded FROM T4

These demonstrate that T4 items CAN be resolved with persistence:

| Item | Was T4 since | Resolved | New tier | How |
|---|---|---|---|---|
| α_em(0) gap | ~C139 | C579 | T3 | One-loop shape mode closes 106.6% |
| D4 gravity κ | ~C366 | C580 | T2a (+2.1%) | RS standard + DFGH self-consistency |
| N=126 shell | ~C338 | C361 | T3 | Shell model with DFC spin-orbit |
| M_W tree-level | ~C400 | C497 | T2a (+0.009%) | Standard Sirlin one-loop |
| Neutrino m₃/m₂ | ~C165 | C204 | T3 (+0.01%) | Color phase correction |

These successes took 60-440 cycles. Patience is warranted, but not indefinite.

---

## Current T4 Items — Full Audit

### 1. Baryon asymmetry η_B (184× overshoot)
- **First T4:** C546
- **Duration:** ~38 cycles
- **Trajectory:** FLAT — single computation, no follow-up attempts
- **Root cause:** M_c(D7) as RH neutrino mass gives M_1 too high, or
  single-flavor leptogenesis is too crude
- **Verdict:** PROGRESSING (too early to flag; only one attempt so far)
- **Next:** multi-flavor leptogenesis, or explore EW baryogenesis route

### 2. Dark matter relic abundance
- **First T4:** C554
- **Duration:** ~30 cycles
- **Trajectory:** FLAT — gravitational freeze-in requires T_RH too high;
  Kibble-Zurek overproduces by 10⁷×
- **Root cause:** d_DM = 4.5 (dark matter depth parameter) not derived;
  production mechanism unclear
- **Verdict:** PROGRESSING (early stage; m_DM = 35.6 keV itself is T4)

### 3. CKM/PMNS angles from D6/D7 overlap
- **First T4:** ~C413 (ISSUES.md)
- **Duration:** ~170 cycles
- **Trajectory:** DETERIORATING — C522 proved diagonal Z₃ FAILS for θ₁₂.
  Off-diagonal BVP needed but not attempted. Best result: sin(θ_C) = 1/π
  (+43%) or GST formula (−0.6% but uses quark masses as input).
- **Root cause:** The D6/D7 overlap integral requires solving a coupled
  kink-vortex BVP that has not been set up
- **Verdict:** STALLED — 170 cycles, diagonal approach ruled out, off-diagonal
  not attempted. This blocks baryon asymmetry (CP phase) and full flavor.
  **Recommend: escalate to P3 as formal BVP problem, or flag as structural gap.**

### 4. Top quark mass
- **First T4:** ~C459 (spoke 10)
- **Duration:** ~125 cycles
- **Trajectory:** FLAT — Koide fails for quarks (C494). No viable route
  identified. Top mass is the most important underivedparameter for EW
  precision (enters M_W loop correction).
- **Root cause:** No DFC mechanism produces the top Yukawa coupling.
  The generation hierarchy (κ) works for leptons but not quarks.
- **Verdict:** STALLED — 125 cycles, no viable route. Flag as contingent
  limitation. The top mass may require D6 Yukawa structure not yet developed.

### 5. Deuteron binding energy (−48%)
- **First T4:** ~C473
- **Duration:** ~111 cycles
- **Trajectory:** DETERIORATING — C563 showed OBE is fundamentally too weak.
  Even with NJL sigma (lighter, longer range) and g_ω = 0, no binding.
  Root cause revised: needs iterated 2π exchange.
- **Root cause:** Single-boson exchange gives V_net ~ few MeV at 1 fm,
  an order of magnitude below what's needed
- **Verdict:** STALLED — blocked on 2π exchange computation (P3 item).
  This is a PHYSICS problem (nuclear binding requires non-perturbative
  multi-pion exchange), not a DFC-specific failure.

### 6. Hadronic vacuum polarization (VP)
- **First T4:** ~C520
- **Duration:** ~64 cycles
- **Trajectory:** REFRAMED — the "gap" was from the 36π formula, not VP
  itself. DFC VP overshoots data by +27%. With C579 shape mode correction,
  the 36π formula is nearly closed (6.6% overshoot). The hadronic VP
  question has shifted to: can DFC's ρ spectral function resolve the
  data-vs-lattice controversy (10σ spread)?
- **Root cause:** DFC quark-hadron spectral function not computed
- **Verdict:** PROGRESSING — reframed from "wrong VP" to "VP computation
  needed for muon g-2." Not stalled, but not actively worked.

### 7. ℏ from (α, β, c)
- **First T4:** ISSUES.md T8 (~C381)
- **Duration:** ~203 cycles
- **Trajectory:** FLAT — blocked on α_em(0) identity. Now that α_em gap
  is T3 (C579), this is partially unblocked.
- **Root cause:** ℏ derivation requires converting DFC natural units to
  SI, which requires the α_em(0) chain
- **Verdict:** STALLED but PARTIALLY UNBLOCKED — reassess after α_em gap
  closes to T2a.

### 8. Threshold positions α₅, α₆, α₇
- **First T4:** C526
- **Duration:** ~58 cycles
- **Trajectory:** FLAT — no computation attempted
- **Root cause:** Compression budget per bifurcation from V(φ) not derived
- **Verdict:** STALLED — no attempts. Low priority relative to other T4 items.

### 9. Neutrino absolute mass scale
- **First T4:** ~C496 (spoke 7)
- **Duration:** ~88 cycles
- **Trajectory:** FLAT — θ₂₃ resolved without BVP; mass ratio has color
  correction (T3). Absolute scale (m₁ or Σm_ν) not derived.
- **Root cause:** Seesaw mechanism parameters (M_R) not derived from DFC
- **Verdict:** STALLED — blocked on D6/D7 overlap (item 3 above).

### 10. Nuclear Walecka coupling strength (g₂ 14× weak)
- **First T4:** ~C371
- **Duration:** ~213 cycles
- **Trajectory:** IMPROVING — C560: NJL gap equation gives C₂(NJL)/C₂(NL3)
  = 0.87 (was 7% with kink tree-level). The 14× gap was an artifact of
  using the wrong sigma mass. NJL sigma (226 MeV) gives realistic
  softening. Remaining: sigma mass discrepancy (226 vs 500-648 MeV).
- **Verdict:** PROGRESSING — significant improvement in C560.

---

## Summary Table

| # | Item | Duration | Trajectory | Verdict |
|---|---|---|---|---|
| 1 | η_B (184×) | 38 | Flat | PROGRESSING |
| 2 | DM relic | 30 | Flat | PROGRESSING |
| 3 | CKM/PMNS angles | 170 | Deteriorating | **STALLED** |
| 4 | Top quark mass | 125 | Flat | **STALLED** |
| 5 | Deuteron B_d (−48%) | 111 | Deteriorating | **STALLED** |
| 6 | Hadronic VP | 64 | Reframed | PROGRESSING |
| 7 | ℏ derivation | 203 | Flat | STALLED (partially unblocked) |
| 8 | Threshold positions | 58 | Flat | STALLED (low priority) |
| 9 | Neutrino abs. mass | 88 | Flat | STALLED |
| 10 | Walecka g₂ | 213 | Improving | PROGRESSING |

**Items to flag as likely unresolvable (>100 cycles, no trajectory):**
- Top quark mass — no viable route identified
- ℏ from (α,β,c) — blocked chain, 200+ cycles
- Threshold positions — no attempts, 58 cycles but genuinely hard

**Items with clear paths despite long duration:**
- CKM angles — needs off-diagonal BVP (concrete task)
- Deuteron — needs 2π exchange (concrete physics)
- Walecka g₂ — NJL is working, sigma mass discrepancy narrowing

---

## Conclusions

1. **T4 is not permanent.** Five items have been upgraded from T4 in recent
   cycles, including two major ones (α_em and D4 gravity) in C579-C580.

2. **Three items should be honestly flagged:** top quark mass (no route),
   ℏ derivation (chain-blocked), and threshold positions (no attempts).
   These are not failures — they are honest limitations of the current
   development stage.

3. **The CKM/PMNS item (170 cycles) is the most important stalled item**
   because it blocks both baryon asymmetry and full flavor physics.
   Recommend escalating the off-diagonal BVP to P3.

4. **Nuclear items (deuteron, Walecka) are physics-hard, not DFC-hard.**
   The same problems challenge all nuclear models. DFC's contribution
   is providing the coupling constants from first principles.
