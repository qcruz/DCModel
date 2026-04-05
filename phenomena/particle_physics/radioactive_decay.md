# Phenomenon: Radioactive Decay

## One-Sentence Synthesis

> Radioactive decay is the compression field releasing stored energy through three
> distinct mechanisms corresponding to the three internal closure depths: beta decay
> is an intra-D6 SU(2) quark-flavor transition mediated by W-boson exchange (verified:
> τ_n = 878.4 s, 0.1% match); alpha decay is quantum tunneling of a D7 color-neutral
> four-quark cluster through the Coulomb-plus-strong-force barrier; and gamma decay
> is the emission of a D5 photon when a nucleus transitions between D3+D4 energy levels.

---

## Observation

Unstable nuclei transform spontaneously into more stable configurations via three modes:

**Beta decay (β):**
```
β⁻:  n  → p  + e⁻ + ν̄_e   [neutron → proton + electron + antineutrino]
β⁺:  p  → n  + e⁺ + ν_e    [proton → neutron + positron + neutrino]
EC:  p + e⁻ → n  + ν_e      [electron capture]
```
Characteristic: changes nuclear charge Z by ±1. Mediated by weak force. Continuous
electron energy spectrum (neutrino carries variable share).

**Alpha decay (α):**
```
A → (A−4) + ⁴He nucleus
```
Characteristic: reduces mass number by 4, charge by 2. Mediated by strong/EM interplay.
Discrete alpha energy (two-body kinematics). Tunneling through Coulomb barrier.

**Gamma decay (γ):**
```
A* → A + γ
```
Characteristic: no change in Z or A. Pure EM photon emission from nuclear excited state.
Discrete photon energies (nuclear level spacings). Typically follows alpha or beta decay.

Half-lives span ~50 orders of magnitude: from 10⁻²³ s (nuclear resonances) to 10²⁰ yr
(double-beta decay candidates).

---

## Standard Explanation

- **Beta**: weak interaction via virtual W-boson exchange: d → u + W⁻, then W⁻ → e⁻ + ν̄_e
- **Alpha**: quantum tunneling through the Coulomb barrier; Gamow factor gives the
  tunneling probability, explaining the exponential sensitivity to alpha particle energy
- **Gamma**: electromagnetic transition with photon emission; selection rules from
  angular momentum and parity conservation

---

## Dimensional Folding Explanation

The three decay modes correspond to three different closure depths and their interaction
channels.

### Beta Decay: Intra-D6 SU(2) Quark-Flavor Transition

Beta decay is a D6 SU(2)_L weak-force transition at the quark level. The underlying
subprocess:

```
d quark → u quark + W⁻     (β⁻ decay)
u quark → d quark + W⁺     (β⁺ decay)
```

This is an intra-D6 transition: the quark changes its D6 SU(2)_L isospin orientation
(from T₃ = −1/2 for d to T₃ = +1/2 for u), emitting the D6 connection field quantum W⁻.
The W then decays: W⁻ → e⁻ + ν̄_e (another D6 transition releasing two lepton kinks).

**DFC classification (from `phenomena/particle_physics/proton_stability.md`):**
- Intra-D6 transitions: quark ↔ quark within the same closure level → **allowed**
- Cross-closure D7 → D5 transitions (quark → lepton directly): **forbidden**

This classification is why protons are stable and why nucleons only beta-decay through
the W boson channel, never directly.

**Verified prediction:** The neutron lifetime τ_n = 878.4 s (DFC, from `equations/proton_stability.py`)
vs 879.4 s observed. This is the model's only current quantitative prediction verified
to better than 1%. The calculation uses G_F (from D6 coupling g_W) and the quark-level
matrix element (from D7 color structure).

**Beta spectrum shape:** The continuous electron energy spectrum in beta decay — the
feature that led Pauli to postulate the neutrino — is a consequence of three-body
final-state kinematics (n → p e ν). The neutrino carries variable energy, leaving a
continuous spectrum for the electron up to the endpoint Q-value. This is the standard
kinematics; the DFC account does not modify the spectrum shape from the SM result.

### Alpha Decay: Quantum Tunneling of a D7 Color-Neutral Cluster

An alpha particle (⁴He nucleus = 2 protons + 2 neutrons = 12 quarks total) is a
particularly stable color-neutral combination of D7 SU(3) quarks. Its stability comes
from the closed nuclear shell structure (Z=2, N=2 both doubly-magic) and the strong
pairing correlations at D7.

The alpha decay sequence:
1. Inside the nucleus, the 12 quarks forming the alpha cluster are color-neutral
   and tightly bound by the D7 strong force
2. The cluster pre-forms near the nuclear surface — a fluctuation in the
   multi-quark compression field that briefly localizes 12 quarks into an alpha-like
   configuration
3. The cluster then tunnels through the combined D5+D7 potential barrier:
   - **Inside barrier**: strong force (D7) attraction holds the cluster inside
   - **Outside barrier**: Coulomb repulsion (D5) pushes the cluster away
   - **Tunneling region**: the classically forbidden zone where the cluster must
     borrow energy from quantum fluctuations to cross

**Gamow tunneling factor:**
```
T_Gamow = exp(−2G)    where G = ∫√(2m[V(r)−E]) dr  [over classically forbidden region]

V(r) = (Z_daughter × 2 × α_EM) / r − V_nuclear(r)
```

The exponential sensitivity of half-life to alpha particle energy (Geiger-Nuttall law:
log T½ ∝ Z/√E_α) is the direct consequence of the Gamow exponent. This is pure
quantum tunneling through the D5 Coulomb barrier — the DFC account does not modify
the Gamow formula from standard QM. The kink picture of the compression field gives
the same tunneling probability as the standard treatment (the WKB approximation applied
to the compression field wave equation).

**DFC perspective on pre-formation:** The nuclear compression field supports localized
4-nucleon cluster configurations. The probability of alpha cluster pre-formation at the
nuclear surface is a D7 multi-kink problem — four nucleons (12 quarks) forming a
temporary coherent D7-color-neutral configuration. This probability factor P_α is
typically ~0.1–0.5 for heavy nuclei and is the nuclear-structure input that the pure
Gamow formula doesn't compute.

### Gamma Decay: D5 Photon Emission from Nuclear Level Transition

A nucleus in an excited energy state (produced after alpha or beta decay, or by
inelastic scattering) can transition to its ground state by emitting a photon.

The photon is the D5 U(1) gauge boson — the massless connection field of the D5
closure. Its emission corresponds to the nucleus' collective D3+D4 compression field
configuration transitioning from an excited kink pattern to the ground-state pattern,
with the energy difference emitted as a D2 propagation mode (photon).

The transition rate is given by the electric or magnetic multipole matrix element:
```
T_γ(EL) ∝ E_γ^{2L+1} × |⟨f||T^L||i⟩|²
```
where L is the multipole order (L=1 is electric dipole, L=2 is quadrupole, etc.) and
the matrix element measures the spatial overlap between the initial and final nuclear
D3+D4 configurations.

Selection rules (conservation of angular momentum J and parity P from the D3+D4
localization geometry):
```
|J_i − J_f| ≤ L ≤ J_i + J_f    [angular momentum conservation in D3]
P_i × P_f = (−1)^L  (electric)  [parity from D3 spatial inversion]
P_i × P_f = (−1)^{L+1} (magnetic)
```

DFC adds no new content to gamma decay beyond identifying the photon as the D5 gauge
boson and the selection rules as consequences of D3 rotational symmetry.

### Why Half-Lives Span 50 Orders of Magnitude

The enormous range of radioactive half-lives (10⁻²³ s to 10²⁰ yr) follows from the
exponential sensitivity of the transition rates to the relevant parameters:

- **Beta decay**: T½ ∝ Q⁻⁵ (phase space) × |M|² (matrix element). Small Q-values
  (rare due to near-degeneracy of parent and daughter levels) produce very long lives.
  Large g_W matrix elements (allowed Gamow-Teller transitions) produce short lives.

- **Alpha decay**: T½ ∝ exp(+2G) where G ∝ Z/√E_α. Small differences in Z or E_α
  produce huge differences in half-life because of the exponential. This is the
  dominant factor: the Gamow exponent ranges from ~10 to ~100, giving half-lives
  from nanoseconds to gigayears.

- **Gamma decay**: T½ ∝ E_γ^{-(2L+1)}. High-multipole (large L) transitions are
  suppressed by E_γ^{2L+1} and by the matrix element structure. Nuclear isomers
  (very long gamma half-lives) arise when high-spin excited states can only decay
  via high-multipole transitions.

The half-life is the inverse of the decay rate; the rate involves the square of the
overlap integral between initial and final kink configurations weighted by the
available phase space. All three factors (phase space, matrix element, barrier
penetration) emerge from the D3+D4+D5/D6/D7 structure of the system. However, the
numerical inputs — CKM elements, G_F from the D6 coupling, nuclear level energies —
are taken from observation; the DFC contribution is the structural classification
of which channels are allowed and why, not the ab initio computation of all rates.

---

## Formal Equations

### Beta Decay Rate (Fermi's Golden Rule)

```
Γ(β⁻) = (G_F² / 2π³) × |V_ud|² × f(Z, Q) × |M_GT + M_F|²

G_F/√2 = g_W² / (8 m_W²)    [D6 coupling — derived in weak_force.md]
V_ud = CKM element (d→u quark mixing) ≈ 0.974
f(Z, Q) = phase space integral over electron and neutrino momenta
```

### Gamow Alpha Tunneling Factor

```
G = (π Z_d Z_α α_EM / v_α) − 2 arccos(√(R/b)) × Z_d Z_α α_EM √(2mR/E_α)

v_α = √(2 E_α / m_α)    [alpha velocity at infinity]
b = Z_d Z_α e² / E_α    [classical turning point]
R = nuclear radius

T½ = (ln 2) × (πR / v_α) × exp(+2G)
```

### Verified Prediction

```
τ_n (neutron lifetime) = 878.4 s    [DFC, equations/proton_stability.py]
τ_n (observed)         = 879.4 s    [PDG 2024]
Error                  = 0.11%  ✓
```

---

## Consistency Checks

| Process | DFC mechanism | Observed | Status |
|---|---|---|---|
| Beta decay | Intra-D6 SU(2) quark-flavor transition via W | n → p e ν̄_e ✓ | Structural ✓ |
| τ_n = 878.4 s | G_F² × phase space from D6 coupling (SM inputs for G_F, V_ud) | 879.4 s (PDG) | 0.11% match ✓ |
| Proton stability | D7→D5 cross-closure forbidden (no proton decay) | τ_p > 1.6×10³⁴ yr | Structural ✓ |
| Alpha decay | Gamow tunneling through D5 Coulomb + D7 nuclear potential | Geiger-Nuttall law ✓ | Structural ✓ |
| Gamma decay | D5 photon emission from D3+D4 nuclear level transition | Discrete γ energies ✓ | Structural ✓ |
| Beta spectrum shape | Three-body kinematics (neutrino carries variable energy) | Continuous spectrum ✓ | Inherited from SM |
| Half-life range (50 orders) | Exponential sensitivity in Gamow factor / phase space | 10⁻²³ s to 10²⁰ yr | Structural ✓ |
| Alpha pre-formation factor | D7 multi-kink clustering probability | P_α ~ 0.1–0.5 (nuclear models) | OPEN |
| G_F from substrate (α, β, c) | D6 coupling from kink size — not derived | G_F = 1.166×10⁻⁵ GeV⁻² (PDG input) | OPEN |

---

## Open Questions

1. **Alpha pre-formation probability from D7 multi-kink structure.** The Gamow
   tunneling formula gives the correct exponential behavior, but the absolute
   alpha decay rate requires the pre-formation factor P_α — the probability that
   12 quarks form an alpha-like D7-neutral cluster near the nuclear surface. This is
   a D7 multi-kink correlation problem, not yet computed in DFC.

2. **Beta decay spectrum endpoint from DFC phase space.** The endpoint energy of
   the beta spectrum (Q-value = m_parent − m_daughter − m_e) determines the
   spectrum shape. DFC predicts this from the nuclear binding energy difference,
   which is set by D7 quark binding. A first-principles computation of Q-values
   from D7 quark structure is open.

3. **Nuclear isomers and the high-multipole suppression.** Some excited nuclei have
   half-lives of years (nuclear isomers, e.g., ¹⁷⁸m²Hf with T½ = 31 yr). The
   suppression comes from high-multipole (L=8) transition matrix elements. Whether
   DFC's D3+D4 angular momentum structure predicts the correct selection rules
   and suppression factors for high-L transitions is open.

---

## Connections

- **Weak force** — D6 SU(2) W-boson exchange; `phenomena/particle_physics/forces/weak_force.md`
- **Proton stability** — neutron lifetime, cross-closure prohibition;
  `phenomena/particle_physics/proton_stability.md`
- **Strong force** — D7 nuclear binding, alpha cluster formation;
  `phenomena/particle_physics/forces/strong_force.md`
- **Electromagnetism** — D5 photon emission (gamma), Coulomb barrier (alpha);
  `phenomena/electromagnetism/electromagnetism.md`
- **Quantum tunneling** — alpha decay mechanism; `phenomena/quantum/quantum_tunneling.md`
- **Quarks** — d→u quark transition in beta decay; `phenomena/particle_physics/particles/quarks.md`
- **Electron** — e⁻ produced in β⁻ decay; `phenomena/particle_physics/particles/electron.md`
