# Speed of Light: Emergence from Substrate Dynamics

## One-Sentence Synthesis

The speed of light is the substrate's intrinsic propagation rate — the rate at which
compression-information travels through the buckled spatial directions of the field — and
its numerical value in human units is a self-consistent consequence of how DFC determines
the atomic-scale quantities that define those units.

---

## The Substrate Account

### What c is

The DFC field equation for the substrate is a relativistic wave equation:

The d'Alembertian of the field equals the derivative of the potential with respect to the
field value — that is, the wave operator acting on the field balances the self-interaction
force from the double-well potential.

This equation has a characteristic propagation speed built into the wave operator. That
speed is the maximum rate at which any disturbance in the substrate can travel. In the
substrate's own natural units — where the kink width sets the length scale and the
oscillation period sets the time scale — this speed is exactly one.

More precisely: the kink width is the square root of two divided by the substrate
curvature parameter alpha, and the small-oscillation frequency at the vacuum is the square
root of two times alpha. Their product is exactly two, independent of the value of alpha.
This means the substrate propagation speed is a fixed, parameter-independent structural
constant. It is not tunable, not dynamical, and not emergent — it is tautologically the
unit of speed for the substrate.

### What c is not

The speed of light is not a speed limit imposed on a pre-existing space from outside. There
is no pre-existing space. The substrate is the only object, and "space" is the downstream
appearance of its D3 localization behavior. The speed of light is the rate at which the
substrate's own dynamics propagate, measured in the substrate's own terms. The fact that
nothing moves faster than this speed is not a constraint — it follows from the fact that
all physical objects *are* configurations of the substrate, and no configuration can
propagate faster than the medium that constitutes it.

### Time as emergent

The substrate has no fundamental temporal properties. Time is the orderly progression of
substrate dynamics. The compression direction — the direction in which the field's
self-attraction drives it toward lower-dimensional states — defines the arrow of time.
What we call "one second" is a count of substrate oscillation cycles (at the atomic scale,
this count is anchored to the cesium hyperfine transition by human convention).

The speed of light, then, is the ratio of the substrate's spatial propagation rate to its
temporal oscillation rate. Since both are structural properties of the same object, their
ratio is fixed. The Lorentzian signature of spacetime — the fact that time and space enter
the metric with opposite signs — follows directly from the substrate having one compression
direction (time-like) and three buckling directions (space-like).

### Why c has a specific numerical value

In SI units, the speed of light is exactly 299,792,458 metres per second. This number is
not a prediction of any theory — it is a definition. The metre is defined as the distance
light travels in one second divided by 299,792,458, and the second is defined as
9,192,631,770 periods of the cesium-133 hyperfine transition.

Both of these reference quantities — a distance (originally tied to atomic structure via
the Bohr radius and optical wavelengths) and a frequency (the cesium hyperfine transition)
— are in principle derivable from DFC substrate parameters:

- The Bohr radius depends on the fine structure constant (which DFC derives from the 36-pi
  chain: one over alpha at the electromagnetic closure scale equals 36 times pi) and the
  electron mass (an input in the current model).

- The cesium hyperfine frequency depends on nuclear magnetic moments, atomic structure, and
  the fine structure constant. The nuclear axial coupling (which DFC derives as four divided
  by pi) and the electromagnetic coupling together determine the hyperfine splitting scale.

If DFC can derive both a length scale (via alpha and atomic structure) and a frequency
scale (via nuclear and atomic properties), their ratio gives a velocity — and that velocity
must be self-consistent with c. This is not "predicting c" — it is showing that DFC's
parameter web produces a self-consistent unit system.

---

## Formal Structure

### Substrate natural units

In substrate units, three quantities are defined:

- The length unit is the kink width, equal to the square root of two divided by alpha.
- The time unit is one over the vacuum oscillation frequency, equal to one over the square
  root of two times alpha.
- The speed unit is the ratio of these: kink width times oscillation frequency, which
  equals two (dimensionless, independent of alpha).

The factor of two is conventional (reflecting the choice to use the half-width versus full
width of the kink profile). The key point is: the substrate propagation speed is a fixed
number in substrate units, with no free parameters.

### Connection to SI

The SI second is defined by the cesium-133 hyperfine transition frequency, which equals
9,192,631,770 oscillations per second. The SI metre is defined as the distance light
travels in one second divided by 299,792,458. This makes c = 299,792,458 metres per second
by definition.

The physical content is in the cesium frequency itself: why does a cesium atom oscillate
at that particular rate in substrate units? This depends on the nuclear structure of Cs-133,
the electron-nucleus hyperfine interaction, and the electromagnetic coupling — all of which
are structural properties of the substrate at various compression depths.

### Lorentz invariance

The substrate field equation is Lorentz-covariant: the wave operator is invariant under
Lorentz transformations. This means all kink configurations (particles) inherit Lorentz
symmetry. Time dilation, length contraction, and the relativistic energy-momentum relation
are automatic consequences of the field equation structure. A moving kink's internal
oscillation frequency — its "Compton clock" — slows relative to a stationary observer, and
this is precisely the time dilation effect.

---

## Consistency Checks

| Check | Status | Notes |
|---|---|---|
| c = 1 in substrate natural units | PASS | Tautological: wave equation propagation speed |
| Speed is alpha-independent | PASS | kink width times oscillation frequency = 2, independent of alpha |
| Lorentz covariance of kink solutions | PASS | Field equation is Lorentz-covariant by construction |
| Lorentzian signature from compression | Structural | Compression direction = time; buckling = space |
| Bohr radius derivable from DFC alpha | PASS | a_0 = hbar/(m_e c alpha_em); alpha_em from 36pi chain |
| Cesium frequency from DFC | OPEN | Requires nuclear magnetic moment derivation |

---

## Open Questions

1. **Cesium frequency from substrate:** The Cs-133 hyperfine transition frequency depends
   on nuclear structure at the level of magnetic moment ratios. DFC derives the axial
   coupling (four divided by pi) but the full cesium nuclear magnetic moment requires a
   multi-nucleon calculation that is not yet attempted.

2. **Why Lorentzian and not Euclidean?** The substrate's compression direction defines a
   preferred ordering (time). Why does compression produce exactly one time-like direction
   rather than zero or two? This may follow from the topology of the double-well potential
   (which has one unstable direction at the symmetric vacuum), but the argument is not
   formalized.

3. **Planck constant as action quantum:** The ratio of the substrate's natural action scale
   to the Planck constant involves a large number (~10^40) that is not yet derived.
   See `foundations/planck_constant_derivation.md`.

---

## References

- `foundations/premise.md` — c as structural constant
- `phenomena/gravity/special_relativity.md` — Lorentz invariance from substrate
- `phenomena/light/light.md` — light as D2 propagation mode
- `foundations/planck_constant_derivation.md` — action scale
- `equations/atomic_structure.py` — Bohr radius from DFC alpha_em
- `equations/alpha_em_prediction.py` — 36pi chain for alpha_em
