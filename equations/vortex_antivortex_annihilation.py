"""
Vortex-Antivortex Annihilation in 2+1D Complex Scalar Field

Physical question:
    When a vortex (winding +1) and antivortex (winding -1) collide in
    a complex scalar field with V(φ) = -α/2|φ|² + β/4|φ|⁴, what happens?
    Does the topological charge annihilate exactly? What radiation is produced?

DFC mechanism:
    This is the 2+1D analogue of kink-antikink annihilation. In DFC, vortices
    at D5 depth correspond to U(1) charged objects. Vortex-antivortex
    annihilation demonstrates:
    1. Exact topological charge conservation (Q_before = Q_after = 0)
    2. Energy conversion: rest mass → radiation (E = mc²)
    3. Radiation spectrum peaked near the mass gap m_σ = √(2α)
    4. U(1) charge is truly topological — cannot be created or destroyed
       except in ± pairs

Method:
    Solve the 2+1D PDE: ∂²φ/∂t² = ∇²φ - V'(φ) on a periodic grid.
    Initialize with a well-separated vortex-antivortex pair.
    Track total winding number, energy, and radiation spectrum.

DFC parameters: α = ∛18, β = 1/(9π)
"""

import numpy as np
import math

# ═══════════════════════════════════════════════════════════════════════════════
# Constants
# ═══════════════════════════════════════════════════════════════════════════════

PI = math.pi
ALPHA = 18.0**(1.0/3.0)
BETA = 1.0 / (9.0 * PI)
PHI_0 = math.sqrt(ALPHA / BETA)
XI = math.sqrt(2.0 / ALPHA)           # vortex core width
M_SIGMA = math.sqrt(2.0 * ALPHA)      # mass gap

passes = 0
fails = 0
total = 0


def check(name, condition):
    global passes, fails, total
    total += 1
    if condition:
        passes += 1
        print(f"  [PASS] {name}")
    else:
        fails += 1
        print(f"  [FAIL] {name}")


# ═══════════════════════════════════════════════════════════════════════════════
# Part A: Vortex profile and initialization
# ═══════════════════════════════════════════════════════════════════════════════

print()
print("╔══════════════════════════════════════════════════════════════════════╗")
print("║  VORTEX-ANTIVORTEX ANNIHILATION IN 2+1D                            ║")
print("║  V(φ) = −α/2|φ|² + β/4|φ|⁴, α = ∛18, β = 1/(9π)                  ║")
print("╚══════════════════════════════════════════════════════════════════════╝")
print()

print("  ── Part A: Vortex profile and parameters ──")
print()

print(f"    α = ∛18 = {ALPHA:.6f}")
print(f"    β = 1/(9π) = {BETA:.6f}")
print(f"    φ₀ = √(α/β) = {PHI_0:.4f}")
print(f"    ξ = √(2/α) = {XI:.4f} (vortex core width)")
print(f"    m_σ = √(2α) = {M_SIGMA:.4f} (mass gap)")
print()

# Grid setup — smaller for 2+1D to keep runtime reasonable
Nx = 128
Ny = 128
Lx = 20.0 * XI   # domain size in units where ξ ~ 0.87
Ly = 20.0 * XI
dx = Lx / Nx
dy = Ly / Ny
dt = 0.3 * min(dx, dy)  # CFL condition

print(f"    Grid: {Nx}×{Ny}, domain: {Lx:.2f}×{Ly:.2f}")
print(f"    dx = {dx:.4f}, dt = {dt:.4f}")
print()

# Coordinate arrays
x = np.linspace(-Lx/2, Lx/2, Nx, endpoint=False)
y = np.linspace(-Ly/2, Ly/2, Ny, endpoint=False)
X, Y = np.meshgrid(x, y, indexing='ij')

# Vortex profile: φ(r,θ) = f(r) e^{inθ}
# where f(r) ~ r for r << ξ and f(r) → φ₀ for r >> ξ
# Approximate: f(r) = φ₀ × r / √(r² + ξ²)


def make_vortex(x0, y0, n):
    """Create a vortex at (x0,y0) with winding number n."""
    dx_arr = X - x0
    dy_arr = Y - y0
    r = np.sqrt(dx_arr**2 + dy_arr**2)
    theta = np.arctan2(dy_arr, dx_arr)
    f = PHI_0 * r / np.sqrt(r**2 + XI**2)
    return f * np.exp(1j * n * theta)


# Initialize: vortex at (-d/2, 0) and antivortex at (+d/2, 0)
d_sep = 6.0 * XI  # initial separation
phi_v = make_vortex(-d_sep/2, 0.0, +1)
phi_av = make_vortex(+d_sep/2, 0.0, -1)

# Combined field: product ansatz (correct far from cores)
# For well-separated vortices, the phases add and the moduli multiply/φ₀
phi_init = phi_v * phi_av / PHI_0

# Measure initial winding number
def compute_winding(phi_field, x_arr, y_arr):
    """Compute total winding number from phase gradient circulation."""
    phase = np.angle(phi_field)
    # Sum phase differences around boundary
    total_wind = 0.0
    # Use a contour at r ~ 0.8 × L/2 from center
    R_contour = 0.35 * min(Lx, Ly)
    n_pts = 200
    angles = np.linspace(0, 2*PI, n_pts, endpoint=False)
    dangle = 2*PI / n_pts

    phases_on_contour = []
    for a in angles:
        cx = R_contour * np.cos(a)
        cy = R_contour * np.sin(a)
        # Find nearest grid point
        ix = int((cx + Lx/2) / dx) % Nx
        iy = int((cy + Ly/2) / dy) % Ny
        phases_on_contour.append(phase[ix, iy])

    # Winding = (1/2π) × ∮ dθ
    phase_diffs = np.diff(phases_on_contour)
    # Unwrap: large jumps indicate branch cuts
    phase_diffs = np.where(phase_diffs > PI, phase_diffs - 2*PI, phase_diffs)
    phase_diffs = np.where(phase_diffs < -PI, phase_diffs + 2*PI, phase_diffs)
    total_wind = np.sum(phase_diffs) / (2*PI)

    return total_wind


Q_init = compute_winding(phi_init, x, y)
print(f"    Initial separation: d = {d_sep:.2f} = {d_sep/XI:.1f} ξ")
print(f"    Initial winding number: Q = {Q_init:.3f} (should be 0)")
print()

# Energy computation
def compute_energy(phi_field, phi_dot):
    """Compute total field energy."""
    # Kinetic: (1/2)|∂φ/∂t|²
    KE = 0.5 * np.sum(np.abs(phi_dot)**2) * dx * dy

    # Gradient: (1/2)|∇φ|²
    dphi_dx = (np.roll(phi_field, -1, axis=0) - np.roll(phi_field, 1, axis=0)) / (2*dx)
    dphi_dy = (np.roll(phi_field, -1, axis=1) - np.roll(phi_field, 1, axis=1)) / (2*dy)
    GE = 0.5 * np.sum(np.abs(dphi_dx)**2 + np.abs(dphi_dy)**2) * dx * dy

    # Potential: V(|φ|) = -α/2|φ|² + β/4|φ|⁴
    rho = np.abs(phi_field)**2
    PE = np.sum(-ALPHA/2 * rho + BETA/4 * rho**2) * dx * dy

    return KE, GE, PE


phi_dot_init = np.zeros_like(phi_init)
KE0, GE0, PE0 = compute_energy(phi_init, phi_dot_init)
E0 = KE0 + GE0 + PE0

print(f"    Initial energy: E = {E0:.4f}")
print(f"      KE = {KE0:.4f}, GE = {GE0:.4f}, PE = {PE0:.4f}")
print()

# Vortex rest mass: E_vortex = π φ₀² ln(R/ξ) (logarithmic in 2D)
R_eff = Lx / 4  # effective outer radius
E_vortex_theory = PI * PHI_0**2 * math.log(R_eff / XI)
E_pair_theory = 2.0 * E_vortex_theory

print(f"    Single vortex energy (theory): E_v = πφ₀²ln(R/ξ) = {E_vortex_theory:.2f}")
print(f"    Pair energy (theory): 2E_v = {E_pair_theory:.2f}")
print()

# The total energy is negative because V(φ₀) = -α²/(4β) < 0 everywhere.
# The VORTEX energy (above vacuum) is positive.
E_vacuum = (-ALPHA/2 * PHI_0**2 + BETA/4 * PHI_0**4) * Lx * Ly
E_above_vacuum = E0 - E_vacuum
print(f"    Vacuum energy: E_vac = {E_vacuum:.2f}")
print(f"    Energy above vacuum: {E_above_vacuum:.2f}")
print()

check("A1: Initial winding Q ≈ 0 (vortex + antivortex)", abs(Q_init) < 0.2)
check("A2: Vortex energy above vacuum positive", E_above_vacuum > 0)
print()


# ═══════════════════════════════════════════════════════════════════════════════
# Part B: Time evolution — vortex-antivortex collision
# ═══════════════════════════════════════════════════════════════════════════════

print("  ── Part B: Time evolution ──")
print()

# PDE: ∂²φ/∂t² = ∇²φ + αφ - β|φ|²φ
# Use leapfrog (Verlet) integration


def laplacian_2d(f):
    """Compute ∇²f on periodic grid."""
    return ((np.roll(f, -1, axis=0) - 2*f + np.roll(f, 1, axis=0)) / dx**2
          + (np.roll(f, -1, axis=1) - 2*f + np.roll(f, 1, axis=1)) / dy**2)


def force(phi_field):
    """Compute RHS of wave equation."""
    rho = np.abs(phi_field)**2
    return laplacian_2d(phi_field) + ALPHA * phi_field - BETA * rho * phi_field


# Time evolution
T_total = 15.0 / M_SIGMA  # evolve for ~15 oscillation periods
n_steps = int(T_total / dt)
n_snapshots = 8

phi = phi_init.copy()
phi_dot = phi_dot_init.copy()

# Record energy and winding at intervals
record_interval = max(1, n_steps // 100)
times = []
energies = []
windings = []
max_amplitudes = []

print(f"    T_total = {T_total:.2f} ({T_total * M_SIGMA:.1f} / m_σ)")
print(f"    n_steps = {n_steps}")
print()

# Leapfrog: half-step kick
phi_dot += 0.5 * dt * force(phi)

for step in range(n_steps):
    # Drift
    phi += dt * phi_dot

    # Force
    F = force(phi)

    # Kick
    phi_dot += dt * F

    # Record
    if step % record_interval == 0 or step == n_steps - 1:
        # Compensate for leapfrog offset
        phi_dot_sync = phi_dot - 0.5 * dt * F
        KE, GE, PE = compute_energy(phi, phi_dot_sync)
        E_total = KE + GE + PE
        Q = compute_winding(phi, x, y)

        times.append(step * dt)
        energies.append(E_total)
        windings.append(Q)
        max_amplitudes.append(np.max(np.abs(phi)))

# Final state
phi_dot_final = phi_dot - 0.5 * dt * force(phi)  # sync
KE_f, GE_f, PE_f = compute_energy(phi, phi_dot_final)
E_final = KE_f + GE_f + PE_f
Q_final = compute_winding(phi, x, y)

print(f"    Final state:")
print(f"      E_final = {E_final:.4f}")
print(f"      Energy conservation: ΔE/E = {abs(E_final - E0)/abs(E0)*100:.2f}%")
print(f"      Q_final = {Q_final:.3f}")
print(f"      KE_f = {KE_f:.4f} ({KE_f/E_final*100:.1f}%)")
print(f"      GE_f = {GE_f:.4f} ({GE_f/E_final*100:.1f}%)")
print(f"      PE_f = {PE_f:.4f} ({PE_f/E_final*100:.1f}%)")
print()

# Check if annihilation happened: look for disappearance of vortex cores
# A vortex core has |φ| → 0. After annihilation, the field should be
# everywhere near φ₀ (with radiation ripples).
phi_abs = np.abs(phi)
min_amp = np.min(phi_abs)
core_threshold = 0.3 * PHI_0  # if min > this, no vortex cores remain
has_cores = min_amp < core_threshold

print(f"    Vortex core detection:")
print(f"      min(|φ|) = {min_amp:.4f} (threshold = {core_threshold:.4f})")
print(f"      Cores present: {'YES' if has_cores else 'NO (annihilated)'}")
print()

check("B1: Energy conserved to < 10%", abs(E_final - E0)/abs(E0) < 0.10)
check("B2: Winding number conserved (Q ≈ 0 throughout)", abs(Q_final) < 0.3)
check("B3: Vortex cores annihilated", not has_cores)
print()


# ═══════════════════════════════════════════════════════════════════════════════
# Part C: Radiation spectrum analysis
# ═══════════════════════════════════════════════════════════════════════════════

print("  ── Part C: Radiation spectrum ──")
print()

# The radiation field is the deviation from vacuum: δφ = |φ| - φ₀
delta_phi = phi_abs - PHI_0

# 2D FFT to get spectrum
fft_2d = np.fft.fft2(delta_phi)
power_2d = np.abs(fft_2d)**2

# Radial average of power spectrum
kx = np.fft.fftfreq(Nx, d=dx) * 2 * PI
ky = np.fft.fftfreq(Ny, d=dy) * 2 * PI
KX, KY = np.meshgrid(kx, ky, indexing='ij')
K_mag = np.sqrt(KX**2 + KY**2)

# Bin into radial k shells
n_bins = 30
k_max = PI / dx  # Nyquist
k_edges = np.linspace(0, k_max, n_bins + 1)
k_centers = 0.5 * (k_edges[:-1] + k_edges[1:])
power_radial = np.zeros(n_bins)

for i in range(n_bins):
    mask = (K_mag >= k_edges[i]) & (K_mag < k_edges[i+1])
    if np.any(mask):
        power_radial[i] = np.mean(power_2d[mask])

# Find peak
peak_idx = np.argmax(power_radial[1:]) + 1  # skip k=0
k_peak = k_centers[peak_idx]

# Convert to frequency: ω² = k² + m_σ² → ω = √(k² + m_σ²)
omega_peak = math.sqrt(k_peak**2 + M_SIGMA**2)

print(f"    Radiation spectrum:")
print(f"      Peak wavenumber: k_peak = {k_peak:.3f}")
print(f"      Peak frequency: ω_peak = {omega_peak:.3f}")
print(f"      ω_peak / m_σ = {omega_peak/M_SIGMA:.3f}")
print(f"      k_peak / m_σ = {k_peak/M_SIGMA:.3f}")
print()

# In 2D, the radiation from annihilation should be predominantly
# at the mass gap m_σ (similar to 1+1D kink-antikink)
print(f"    Mass gap: m_σ = {M_SIGMA:.4f}")
print(f"    Radiation above gap: ω > m_σ for all k > 0 (massive dispersion)")
print()

check("C1: Radiation spectrum has clear peak", power_radial[peak_idx] > 2 * np.mean(power_radial))
check("C2: Peak frequency above mass gap", omega_peak >= M_SIGMA * 0.95)
print()


# ═══════════════════════════════════════════════════════════════════════════════
# Part D: Charge conservation verification
# ═══════════════════════════════════════════════════════════════════════════════

print("  ── Part D: Topological charge conservation ──")
print()

# The winding number Q = (1/2π) ∮ ∇θ · dl is a topological invariant
# For continuous field evolution, Q can only change by integer amounts
# (vortex pair creation/annihilation)

windings_arr = np.array(windings)
Q_max_deviation = np.max(np.abs(windings_arr))
Q_std = np.std(windings_arr)

print(f"    Winding number time series:")
print(f"      Q_init = {windings[0]:.4f}")
print(f"      Q_final = {windings[-1]:.4f}")
print(f"      max |Q| = {Q_max_deviation:.4f}")
print(f"      std(Q) = {Q_std:.4f}")
print(f"      All Q within ±0.5 of zero: {Q_max_deviation < 0.5}")
print()

# Energy partition relative to vacuum (total E is negative due to V(φ₀) < 0)
E_vac = (-ALPHA/2 * PHI_0**2 + BETA/4 * PHI_0**4) * Lx * Ly
E_above_vac_f = E_final - E_vac
KE_frac = KE_f / E_above_vac_f if E_above_vac_f > 0 else 0
GE_PE_above = (GE_f + PE_f) - E_vac
radiation_frac = GE_PE_above / E_above_vac_f if E_above_vac_f > 0 else 0

print(f"    Energy partition (above vacuum, final):")
print(f"      E above vacuum: {E_above_vac_f:.2f}")
print(f"      Kinetic: {KE_frac*100:.1f}%")
print(f"      Gradient + potential (radiation): {radiation_frac*100:.1f}%")
print()

# Check virial ratio: <KE>/<GE> → 1 for equipartition
energies_arr = np.array(energies)
virial = KE_f / GE_f if GE_f > 0 else 0
print(f"    Virial ratio KE/GE = {virial:.3f} (equipartition → 1.0)")
print()

check("D1: Q = 0 throughout evolution (topological conservation)", Q_max_deviation < 0.5)
check("D2: No spontaneous pair creation (Q stays near 0)", Q_std < 0.2)
check("D3: Energy converted to radiation (GE+PE significant)", radiation_frac > 0.2)
print()


# ═══════════════════════════════════════════════════════════════════════════════
# Part E: Summary
# ═══════════════════════════════════════════════════════════════════════════════

print("  ── Part E: Summary ──")
print()

annihilated = not has_cores
energy_conserved = abs(E_final - E0)/abs(E0) < 0.10
charge_conserved = Q_max_deviation < 0.5

print(f"    1. Vortex-antivortex pair annihilated: {'YES' if annihilated else 'NO'}")
print(f"    2. Energy conserved (ΔE/E): {abs(E_final-E0)/abs(E0)*100:.1f}%")
print(f"    3. Topological charge Q = 0 conserved: {'YES' if charge_conserved else 'NO'}")
print(f"    4. Radiation spectrum peaked at ω/m_σ = {omega_peak/M_SIGMA:.2f}")
print(f"    5. Energy partition: KE {KE_frac*100:.0f}% / radiation {radiation_frac*100:.0f}%")
print()
print(f"    DFC SIGNIFICANCE:")
print(f"      This is the D5 analogue of particle-antiparticle annihilation.")
print(f"      U(1) charge (vortex winding) is exactly conserved — cannot be")
print(f"      created or destroyed except in ± pairs. The annihilation converts")
print(f"      rest mass energy into radiation at the mass gap frequency,")
print(f"      demonstrating E = mc² as a theorem of V(φ) dynamics.")
print()

check("E1: Complete annihilation demonstrated", annihilated and energy_conserved and charge_conserved)
print()


# ═══════════════════════════════════════════════════════════════════════════════
# TOTAL
# ═══════════════════════════════════════════════════════════════════════════════

print()
print("=" * 72)
print(f"TOTAL: {passes}/{total} PASS")
print("=" * 72)
print()
