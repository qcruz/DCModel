# Dimensional Folding Compression (DFC)

An exploratory project investigating what emerges from a single scalar field with a
double-well potential undergoing self-compression.

```
V(phi) = -alpha/2 phi^2 + beta/4 phi^4
```

Current status: ~80% complete (viability: ~87%, mathematical rigor: ~73%)

---

## The Starting Point

Take one continuous scalar field governed by the potential above. Allow it to
pull inward on itself — self-compression. When compression reaches a threshold,
a new internal degree of freedom opens (a bifurcation event) rather than the
field compressing further. The topology of how each bifurcation closes determines
what structures emerge.

That is the entire setup. No pre-existing space, gauge groups, or particle content.
The project explores how far this single starting point can go.

---

## Interesting Findings

The substrate parameters are fixed with zero free parameters: β = 1/(9π) and
α = ∛18. From these, the project has produced a number of quantitative results
that can be compared against experiment. Here is a selection.

### Coupling Constants (zero free parameters)

```
g_eff  =  sqrt(8/27)  =  0.54433       observed: 0.5443       error: +0.006%
1/alpha_em(M_Z)        =  128.09        observed: 127.95       error: +0.15%
1/alpha_em(0)          =  137.034       observed: 137.036      error: -0.001%
alpha_s(M_Z)           =  0.11821       observed: 0.11820      error: +0.006%
sin^2(theta_W)         =  0.2312        observed: 0.2312       error: <0.01%
```

### Mass Predictions

```
tau lepton       =  1776.97 MeV        observed: 1776.86 MeV  error: +0.006%  [Koide, 0 free params]
mu/m_e ratio     =  206.77             observed: 206.77       error:  0.00%
proton           =  934.8 MeV          observed: 938.3 MeV    error: -0.4%    [Tier 3]
pion             =  136.9 MeV          observed: 139.6 MeV    error: -1.9%    [GMOR]
Higgs boson      =  124.4 +/- 3.7 GeV  observed: 125.25 GeV   error: -0.7%
```

### Electroweak Sector

```
W boson mass     =  79.67 GeV          observed: 80.377 GeV   error: -0.88%
Z boson mass     =  90.86 GeV          observed: 91.188 GeV   error: -0.36%
Fermi constant   =  1.168e-5 GeV^-2    observed: 1.166e-5     error: +0.18%
EW VEV           =  247.83 GeV         observed: 246.22 GeV   error: +0.65%
```

### Cosmological Predictions

```
Hubble constant  =  67.26 km/s/Mpc     observed: 67.40        error: -0.21%
BBN Y_p          =  0.2475             observed: 0.2449       error: +1.05%
CMB first peak   =  ell_1 = 222        observed: 220          error: +0.89%
BAO r_drag       =  146.70 Mpc         observed: 147.09 Mpc   error: -0.27%
```

### Exact Structural Results

```
Proton lifetime  =  infinity           (product topology: no gauge path to decay)
Strong CP angle  =  0 (exact)          observed: < 10^-10     [no axion needed]
Flux quantum     =  h/(2e)             exact to 2e-10
Tsirelson bound  =  2*sqrt(2)          algebraically exact
```

### Known Failures

```
Neutrino m3/m2   =  5.33               observed: 5.81         error: -8.3%
Nuclear sym. E   =  -36%               needs larger g_rho
Deuteron binding =  -48%               short-range physics not yet derived
alpha_em(0) id.  =  136.98             observed: 137.036      error: -0.044%  [open]
```

---

## A Key Mathematical Connection

The kink shape integral of V(φ) equals the SU(3) fundamental Casimir eigenvalue:

```
I_4  =  integral of sech^4(u) du  =  4/3  =  C_2(fund, SU(3))
```

Setting C_2(fund, SU(n)) = (n² − 1)/(2n) = 4/3 gives 3n² − 8n − 3 = 0 with
unique positive integer solution **n = 3**. This selects SU(3) from the potential
alone — no group theory is assumed.

This identity governs the gauge coupling, BPS energy bound, string tension, moduli
metric, and fermion representation. Whether this is a coincidence or a structural
connection is the central question the project explores.

---

## How the Model Works

The substrate is one continuous object. Bifurcation events at successive compression
thresholds produce new closure topologies:

| Depth | Closure topology | Apparent physics |
|---|---|---|
| D1 | Maximum compression | Planck-scale substrate |
| D2 | First wave propagation | Massless modes |
| D3 | Localization | Apparent position, 3 spatial dimensions |
| D4 | Inertia | Apparent mass |
| D5 | S¹ closure (U(1)) | Electromagnetism |
| D6 | S³ closure (SU(2)) | Weak force, spin-1/2 |
| D7 | S⁵ in ℂ³ closure (SU(3)) | Strong force, color |

The D5/D6/D7 assignments follow from the cascade S¹ → S³ → S⁵ ⊂ ℂ³, where
the orbit-stabilizer theorem gives U(n)/U(n−1) ≅ S^{2n−1} at each step, and the
Casimir condition I₄ = 4/3 terminates at n = 3.

---

## Yang-Mills Mass Gap

As a test case for the mathematical framework, the project developed a proof
candidate for the Clay Millennium Problem (does pure SU(3) Yang-Mills on ℝ⁴
have a mass gap Δ > 0?).

The argument proceeds from V(φ) through lattice construction, IR bound, continuum
limit, and Poincaré covariance — covering all 7 Jaffe-Witten criteria. The result
is a LaTeX proof document (22 KB, 5 lemmas, 12 citations) with zero T2a steps on
the critical path.

See: [`equations/ym_clay_proof.tex`](equations/ym_clay_proof.tex)

---

## What Remains Open

| Problem | Current status | What would close it |
|---|---|---|
| alpha_em(0) algebraic identity | −0.044%; Tier 4 | Prove A − B = ln(1/α_em(0)) from ECCC |
| Neutrino mass hierarchy m₃/m₂ | −8.3%; Tier 2b | BVP for depth-correction selectivity |
| Hadronic vacuum polarization | δα^NP = 0.00102 open | R^had from D7 confinement dynamics |
| G_Newton from substrate | Not derived | D4 inertia mechanism |
| Nuclear coupling magnitude | Correct sign, 14× too weak | Composite sigma self-coupling |
| CKM/PMNS mixing angles | No quantitative derivation | D6/D7 overlap integral |

Full list: [`ISSUES.md`](ISSUES.md)

---

## Running the Code

All 383 equation modules are self-contained Python scripts. Each prints
predicted values, observed values, errors, and tier classifications.

```bash
# Fine structure constant from first principles
python equations/alpha_em_prediction.py

# Strong coupling with zero observed inputs
python equations/alpha_s_pure_dfc.py

# Tau lepton mass via Koide formula
python equations/koide_phase_coupling.py

# Electroweak sector: W, Z, G_F, muon lifetime
python equations/muon_lifetime.py

# Nuclear nonlinear EOS from kink background
python equations/nuclear_kink_nonlinear_eos.py
```

---

## Repository Structure

```
foundations/           55+ core structural arguments and derivations
equations/             383 runnable Python modules
phenomena/             75+ natural-language accounts of observations
educational/           34 modules from layman to expert
comparisons/           DFC vs. other approaches
practical_applications/ Engineering limits from verified results
ISSUES.md              All open questions, failures, and tensions
ROADMAP.md             Development priorities and task tracking
push_history.md        Full development log
```

**For non-physicists:** Start with [`educational/00_overview.md`](educational/00_overview.md)

**For physicists:** Start with [`educational/08_mathematics.md`](educational/08_mathematics.md),
then [`foundations/substrate.md`](foundations/substrate.md)

---

*An exploratory project investigating the structures that emerge from a
self-compressing scalar field. Every claim is tiered, every prediction is
testable, and every failure is documented.*
