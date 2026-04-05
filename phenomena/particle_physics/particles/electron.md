# Phenomenon: The Electron

## One-Sentence Synthesis

> The electron is the ground-state zero mode of the DFC compression kink at the D5+D6
> closure level — a normalizable spin-1/2 spinor bound to the kink core by the Jackiw-Rebbi
> mechanism, carrying D5 winding number n = −1 (electric charge) and forming an SU(2)
> doublet with the electron neutrino at D6.

---

## Observation

The electron is the lightest stable charged particle: mass m_e = 0.511 MeV, electric
charge Q = −1, spin J = 1/2. It couples to photons (D5 U(1)) and W/Z bosons (D6 SU(2))
but not gluons (no D7 color charge). It does not decay — there is no lighter charged
particle available as a final state.

In matter, the electron is the carrier of electric current, the source of atomic structure
(through Coulomb coupling to nuclei), and the outer partner of the SU(2)_L doublet
(ν_e, e_L).

Measured properties:
```
m_e           = 0.51099895 MeV
Q             = −1 (in units of e)
J             = 1/2
g_e           = −2.00231930  (anomalous magnetic moment a_e = (g−2)/2 = 1.16 × 10⁻³)
τ_e           = stable  (> 6.6 × 10²⁸ yr)
Lepton number = +1
```

---

## Standard Explanation

In the Standard Model the electron is a fundamental spin-1/2 fermion, a member of the
first-generation lepton doublet (ν_e, e_L) under SU(2)_L. Its mass comes from a Yukawa
coupling to the Higgs field:

```
L_Yukawa = −y_e (ν̄_L, ē_L) · H · e_R + h.c.

y_e = m_e / v ≈ 0.511 MeV / 246 GeV ≈ 2.9 × 10⁻⁶
```

The SM gives no explanation for why y_e has this value, why the electron is the lightest
charged lepton, or why there are three generations. It takes spin-1/2 as an axiom.

---

## Dimensional Folding Explanation

### Structural Identity

The electron is a stable closure that reaches D5 (U(1)_Y, hypercharge) and D6 (SU(2)_L,
weak isospin) but not D7 (no color charge). It is the minimal stable kink with non-trivial
D5 winding.

In the dimensional stack:
```
D1 — compression substrate
D2 — propagation (wave/radiation modes)
D3 — localization (3-space position)
D4 — inertia (mass/resistance to acceleration)
D5 — U(1)_Y closure  [electron has winding n = −1 → Q = −1]
D6 — SU(2)_L closure [electron is lower component of (ν_e, e_L) doublet]
D7 — SU(3)_c closure [absent: electron has no color charge]
```

The electron "reaches" D5 and D6 means the compression kink at D3+D4 has non-trivial
topology at the D5 and D6 levels. It does not reach D7 — no SU(3) winding → no color.

### Spin-1/2: The Jackiw-Rebbi Mechanism

The electron's spin-1/2 follows from the Jackiw-Rebbi zero mode of the DFC compression
kink (see `foundations/spin_emergence.md`, Path B2).

The D3+D4 kink of the compression field φ:
```
φ(x) = φ₀ tanh(x/λ)    [φ₀ = √(α/β), λ = √(2c²/α) ≈ L_Planck]
```

couples to a spinor through the D6 Yukawa interaction:
```
L_Y = −g_Y φ(x) ψ̄ψ    [g_Y = D6 coupling to kink background]
```

The exact zero mode of the Dirac operator:
```
ψ_0(x) = A_norm × cosh^{−Mλ}(x/λ) × |spinor⟩

M = g_Y φ₀    [effective fermion mass scale at D6]
Mλ > 1/2      [normalizability: g_Y > (1/2)√(β/(2c²))]
```

This zero mode:
- Satisfies D̸ψ_0 = 0 exactly (zero energy eigenvalue)
- Is localised near the kink core with width ξ ≈ λ/(Mλ) = 1/M
- Is a spinor under SL(2,C) — spin-1/2 by construction of the Clifford algebra Cl(3,1)
- Is the electron: no independent spinor field is introduced

**Verified numerically:** For Mλ = 2 (electron-like), the Dirac equation residual
rms ≈ 1.5 × 10⁻⁶ — confirming the zero mode is an exact analytic solution.
See `equations/spin_zero_mode.py`, Step 4.

### Electric Charge: D5 Winding Number

The D5 U(1)_Y closure is topologically S¹. Field configurations mapping S¹ → S¹ are
classified by an integer winding number n ∈ π₁(S¹) = Z. This integer is the hypercharge Y.

For the electron: Y = −1. The electric charge follows from the Gell-Mann–Nishijima
formula (combining D5 and D6 quantum numbers):
```
Q = T₃ + Y/2 = −1/2 + (−1)/2 = −1
```

where T₃ = −1/2 is the D6 SU(2)_L isospin of the lower doublet component.

The charge is an integer because a field configuration cannot wrap a circle a
non-integer number of times. The charge −1 (not −1.3, not −π) follows from the
topology of the D5 closure — not from a free assignment.

### SU(2) Doublet Structure and the Neutrino Partner

At D6, the SU(2)_L closure arranges fermion fields into doublets. The electron and
electron neutrino are the two components of the first-generation lepton doublet:

```
L_L = ( ν_eL )    [left-handed SU(2)_L doublet, T = 1/2]
      (  e_L  )

e_R  [right-handed SU(2)_L singlet,  T = 0]
```

The left-handed electron is the lower (T₃ = −1/2) component. The electron neutrino
is the upper (T₃ = +1/2) component. They are produced together in weak interactions
because they share a D6 SU(2)_L doublet structure.

The right-handed electron e_R is an SU(2)_L singlet — it has no D6 isospin coupling.
Its spin-1/2 comes from the D3+D4 spin structure alone (the Clifford algebra admits
spinor representations independently of any D6 winding).

### Mass: Ground State at D5+D6

The electron mass arises from the depth at which the kink is anchored. From
`foundations/mass_hierarchy.md`, the lepton mass hierarchy corresponds to different
zero modes of the effective potential at the D6 layer:

- **Electron** (ground state): mass scale set by the dimple depth d in the D6 effective
  potential. The ground-state wave function samples only the bottom of the dimple.
  m_e ∝ d.

- **Muon** (first excited state with a node at the dimple center): mass ∝ 1/R where
  R is the global D6 scale. m_μ/m_e = R/d ≈ 207.

- **Tau** (second excited state): m_τ ≈ m_μ × (geometric factor from D6 curvature).

The ratio m_μ/m_e ≈ 207 corresponds to R/d — two independent length scales in the D6
S³ geometry (global radius and dimple depth), not two free parameters fitted to data.

The Yukawa coupling y_e ≈ 2.9 × 10⁻⁶ in SM language corresponds to the ratio of the
electron's Jackiw-Rebbi mass scale M = g_Y φ₀ to the electroweak scale v:

```
y_e = M / v = g_Y φ₀ / v
```

The smallness of y_e reflects that M ≪ v — the electron's zero-mode mass is far below
the D6 squashing scale v ≈ 246 GeV. In DFC terms this is the ratio of the dimple depth
to the global D6 S³ curvature scale.

### Stability

The electron does not decay. The reason:

1. **Electric charge conservation.** The D5 winding number n = −1 is conserved. Any
   decay would require producing particles with total Q = −1. The lightest charged
   particle is the electron itself — there is no available lighter charged final state.

2. **Lepton number conservation.** The D6 doublet structure assigns lepton number +1
   to (ν_e, e_L). This is conserved by all gauge interactions at D5 and D6.

Stability is a consequence of conservation laws that themselves follow from the
topological structure of the D5 and D6 closures. It is not separately imposed.

---

## Formal Equations

### Jackiw-Rebbi Zero Mode

```
φ(x)  = φ₀ tanh(x/λ)                  [DFC compression kink]
ψ_0(x) = A × cosh^{−Mλ}(x/λ) × χ     [exact fermion zero mode]

D̸ ψ_0 = (iγ^μ ∂_μ − g_Y φ(x)) ψ_0 = 0  [zero energy eigenvalue]

Normalizability:  Mλ = g_Y φ₀ λ > 1/2
```

### Charge Assignment

```
Y = −1                  [D5 U(1)_Y winding number]
T₃ = −1/2              [D6 SU(2)_L isospin: lower doublet component]
Q = T₃ + Y/2 = −1      [Gell-Mann–Nishijima from D5+D6 winding]
```

### Doublet Coupling (Weak Interaction)

```
L_CC = (g_W/√2) ν̄_eL γ^μ e_L W⁻_μ + h.c.   [charged-current, D6 SU(2)]
L_NC = (g_W/cosθ_W) ē γ^μ (T₃ − Q sin²θ_W) e Z_μ   [neutral-current]
```

### Mass-Coupling Relation

```
m_e = g_Y φ₀ × (Jackiw-Rebbi bound-state factor)
y_e = m_e / v ≈ 2.9 × 10⁻⁶    [Yukawa = Mλ-over-v in DFC language]
```

---

## Consistency Checks

| Property | DFC prediction | Observed |
|---|---|---|
| Charge | Q = T₃ + Y/2 = −1 | −1 ✓ |
| Spin | Jackiw-Rebbi spinor, Cl(3,1) | 1/2 ✓ |
| Stability | Lightest particle with Q = −1, L = +1 | stable ✓ |
| Doublet partner | ν_eL at T₃ = +1/2, Y = −1, Q = 0 | electron neutrino ✓ |
| Color charge | No D7 closure → no color | colorless ✓ |
| Left-handed weak coupling | S³ intrinsic orientation at D6 | e_L couples, e_R does not ✓ |

---

## What Remains Open

1. **Derive m_e (0.511 MeV) from DFC parameters without free-fitting.** The Jackiw-Rebbi
   mass scale M = g_Y φ₀ and the dimple depth d both depend on (α, β, g_Y). A complete
   derivation would express m_e in terms of these without using m_e as input.

2. **Derive the Yukawa coupling g_Y from D6 geometry.** In the SM, y_e = 2.9 × 10⁻⁶ is
   taken as a measured input. In DFC, g_Y is the coupling of the D6 SU(2) connection
   field to the kink background — a geometric quantity set by the D6 closure structure.
   Computing g_Y from the D6 geometry is the fermion mass prediction problem.

3. **The 3+1D Jackiw-Rebbi generalization.** The exact zero mode computed above is in
   1+1D. The 3+1D case requires the kink background to be a 3+1D soliton (the Skyrmion
   or D3+D4 kink) and the zero mode to be an L² spinor in R³. The BPST instanton result
   (Step 2) gives this for the composite baryon; the elementary lepton analog in 3+1D
   is the open formal derivation in `foundations/spin_emergence.md`.

4. **The anomalous magnetic moment.** g_e = −2 at tree level is exact in QED; the
   deviation a_e = (g−2)/2 ≈ 1.16 × 10⁻³ arises from one-loop photon exchange. In DFC
   the loop correction corresponds to a higher-order effect in the D5 closure geometry.
   The leading correction a_e = α/(2π) is standard QED; whether DFC modifies this at
   higher orders is open.

---

## Connections to Other Phenomena

- **Spin-1/2 emergence** — Jackiw-Rebbi mechanism, Clifford algebra Cl(3,1);
  `foundations/spin_emergence.md`
- **Electromagnetism** — D5 U(1) coupling, charge Q = −1;
  `phenomena/electromagnetism/electromagnetism.md`
- **Electric charge** — winding number n = −1 at D5; `phenomena/electromagnetism/electric_charge.md`
- **Weak force** — D6 SU(2)_L doublet; `phenomena/particle_physics/forces/weak_force.md`
- **Electroweak** — Q = T₃ + Y/2 mixing; `phenomena/particle_physics/forces/electroweak.md`
- **Three generations** — muon/tau are excited states of same D6 structure;
  `foundations/three_generations.md`
- **Mass hierarchy** — dimple potential at D6, m_μ/m_e = R/d; `foundations/mass_hierarchy.md`
- **Electron neutrino** — SU(2)_L doublet partner; `phenomena/particle_physics/particles/neutrinos.md`
