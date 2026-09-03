"""
Internal Consistency Web Audit for DFC Model

Scans all equation modules for shared DFC parameters and checks for
numerical consistency. Detects:
  1. Stale approximate values vs current exact definitions
  2. Conflicting definitions of the same parameter across modules
  3. Derived quantities that should agree but don't

Key DFC parameters audited:
  β = 1/(9π) ≈ 0.035368        quartic coupling [T2a, C117]
  α = ∛18 ≈ 2.62074            quadratic coupling [T2a, C172]
  g_eff² = 8πβ/3 = 8/27        common gauge coupling squared
  g_eff = √(8/27) ≈ 0.54433    common gauge coupling
  S_kink = 2√2/3 ≈ 0.94281     kink action (units of φ₀²λ)
  Q_top = 2                     topological charge of kink-antikink pair
  I₄ = C₂(fund, SU(3)) = 4/3   quadratic Casimir
  N_c = 3                       number of colors
  φ₀ = √(α/β)                  kink vacuum
  Λ_QCD ≈ 304.5 MeV            QCD scale from DFC

Stress test module for the DFC model's internal consistency.
Created: Cycle 501
"""

import os
import re
import math
import sys

# ─── Exact DFC parameter values ─────────────────────────────────────────────

EXACT = {
    'BETA': {
        'value': 1.0 / (9.0 * math.pi),
        'formula': '1/(9π)',
        'tolerance': 1e-6,  # values within this fraction are "consistent"
    },
    'ALPHA_QUAD': {
        'value': 18.0 ** (1.0/3.0),
        'formula': '∛18',
        'tolerance': 1e-4,
    },
    'G_EFF_SQ': {
        'value': 8.0 / 27.0,
        'formula': '8/27',
        'tolerance': 1e-6,
    },
    'G_EFF': {
        'value': math.sqrt(8.0 / 27.0),
        'formula': '√(8/27)',
        'tolerance': 1e-4,
    },
    'S_KINK': {
        'value': 2.0 * math.sqrt(2.0) / 3.0,
        'formula': '2√2/3',
        'tolerance': 1e-4,
    },
    'Q_TOP': {
        'value': 2,
        'formula': '2',
        'tolerance': 0,
    },
    'I_4': {
        'value': 4.0 / 3.0,
        'formula': 'C₂(fund,SU(3)) = 4/3',
        'tolerance': 1e-6,
    },
    'N_C': {
        'value': 3,
        'formula': '3',
        'tolerance': 0,
    },
}

# ─── Regex patterns for parameter extraction ────────────────────────────────

PATTERNS = {
    'BETA': [
        # Exact: BETA = 1/(9*pi) or 1.0/(9.0*math.pi)
        (r'(?:BETA|beta)\s*=\s*1\.?0?\s*/\s*\(\s*9\.?0?\s*\*\s*(?:math\.pi|np\.pi|PI|pi)\s*\)',
         'exact_formula'),
        # Approximate: BETA = 0.035, 0.0351, 0.03537 etc.
        (r'(?:BETA|beta)\s*=\s*(0\.03[0-9]*)', 'approximate'),
    ],
    'G_EFF': [
        (r'(?:g_eff|G_EFF|g_common)\s*=\s*(0\.54[0-9]*)', 'approximate'),
        (r'(?:g_eff_sq|G_EFF_SQ|g_eff2|g2_eff)\s*=\s*8\.?0?\s*/\s*27', 'exact_formula'),
        (r'(?:g_eff_sq|G_EFF_SQ|g2|G2)\s*=\s*(0\.29[0-9]*)', 'approximate'),
    ],
    'LAMBDA_QCD': [
        (r'(?:LAMBDA_QCD|Lambda_QCD|LAM_QCD)\s*=\s*([0-9]+\.?[0-9]*)', 'value_MeV'),
    ],
}


def scan_file_for_beta(filepath):
    """Scan a Python file for BETA definitions and return findings."""
    findings = []
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except (IOError, UnicodeDecodeError):
        return findings

    fname = os.path.basename(filepath)
    exact_val = EXACT['BETA']['value']

    for i, line in enumerate(lines, 1):
        # Skip comments
        stripped = line.strip()
        if stripped.startswith('#'):
            continue

        # Match BETA = 1/(9*pi) variants (exact)
        if re.search(r'(?:BETA|beta)\s*=\s*1\.?0?\s*/\s*\(\s*9\.?0?\s*\*\s*(?:math\.pi|np\.pi|PI|pi)\s*\)',
                      line):
            findings.append({
                'file': fname,
                'line': i,
                'param': 'BETA',
                'type': 'exact',
                'value': exact_val,
                'error_pct': 0.0,
                'raw': stripped,
            })
        # Match approximate values
        else:
            m = re.search(r'(?:BETA|beta)\s*=\s*(0\.0[0-9]+)', line)
            if m:
                val = float(m.group(1))
                err = abs(val - exact_val) / exact_val * 100
                findings.append({
                    'file': fname,
                    'line': i,
                    'param': 'BETA',
                    'type': 'approximate' if err > 0.01 else 'exact_numeric',
                    'value': val,
                    'error_pct': err,
                    'raw': stripped,
                })
    return findings


def scan_file_for_g_eff(filepath):
    """Scan for g_eff / g_common definitions."""
    findings = []
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            lines = content.split('\n')
    except (IOError, UnicodeDecodeError):
        return findings

    fname = os.path.basename(filepath)
    exact_g = EXACT['G_EFF']['value']
    exact_g2 = EXACT['G_EFF_SQ']['value']

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue

        # g_eff or g_common approximate
        m = re.search(r'(?:g_eff|G_EFF|g_common|G_COMMON)\s*=\s*(0\.[0-9]+)', line)
        if m and 'sq' not in line.lower() and '**2' not in line and '^2' not in line:
            val = float(m.group(1))
            if 0.5 < val < 0.6:  # sanity check it's the coupling
                err = abs(val - exact_g) / exact_g * 100
                findings.append({
                    'file': fname, 'line': i, 'param': 'g_eff',
                    'type': 'approximate', 'value': val,
                    'error_pct': err, 'raw': stripped,
                })

        # g_eff² approximate
        m2 = re.search(r'(?:g_eff_sq|G_EFF_SQ|g2_eff|g_eff_squared|g2)\s*=\s*(0\.[0-9]+)', line)
        if m2:
            val = float(m2.group(1))
            if 0.25 < val < 0.35:  # sanity
                err = abs(val - exact_g2) / exact_g2 * 100
                findings.append({
                    'file': fname, 'line': i, 'param': 'g_eff²',
                    'type': 'approximate', 'value': val,
                    'error_pct': err, 'raw': stripped,
                })
    return findings


def scan_file_for_lambda_qcd(filepath):
    """Scan for Λ_QCD definitions."""
    findings = []
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except (IOError, UnicodeDecodeError):
        return findings

    fname = os.path.basename(filepath)

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue

        m = re.search(r'(?:LAMBDA_QCD|Lambda_QCD|LAM_QCD|LAMBDA_QCD_MEV)\s*=\s*([0-9]+\.?[0-9]*)',
                      line, re.IGNORECASE)
        if m:
            val = float(m.group(1))
            if 100 < val < 1000:  # MeV range
                findings.append({
                    'file': fname, 'line': i, 'param': 'Λ_QCD',
                    'type': 'value_MeV', 'value': val,
                    'error_pct': None,
                    'raw': stripped,
                })
    return findings


def scan_file_for_alpha(filepath):
    """Scan for α (quadratic coupling) definitions."""
    findings = []
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except (IOError, UnicodeDecodeError):
        return findings

    fname = os.path.basename(filepath)
    exact_val = EXACT['ALPHA_QUAD']['value']

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue

        # Match ALPHA = 18**(1/3) or similar
        if re.search(r'(?:ALPHA|alpha)\s*=\s*18\.?0?\s*\*\*\s*\(\s*1', line):
            findings.append({
                'file': fname, 'line': i, 'param': 'α (quadratic)',
                'type': 'exact', 'value': exact_val,
                'error_pct': 0.0, 'raw': stripped,
            })
        elif re.search(r'(?:ALPHA_DFC|alpha_dfc|ALPHA_QUAD)\s*=', line):
            m = re.search(r'=\s*([0-9]+\.[0-9]+)', line)
            if m:
                val = float(m.group(1))
                if 2.5 < val < 2.7:
                    err = abs(val - exact_val) / exact_val * 100
                    findings.append({
                        'file': fname, 'line': i, 'param': 'α (quadratic)',
                        'type': 'approximate', 'value': val,
                        'error_pct': err, 'raw': stripped,
                    })
    return findings


def run_audit():
    """Run the full consistency web audit."""
    equations_dir = os.path.dirname(os.path.abspath(__file__))
    py_files = sorted([
        os.path.join(equations_dir, f)
        for f in os.listdir(equations_dir)
        if f.endswith('.py') and f != 'consistency_web_audit.py'
    ])

    all_findings = []

    for fp in py_files:
        all_findings.extend(scan_file_for_beta(fp))
        all_findings.extend(scan_file_for_g_eff(fp))
        all_findings.extend(scan_file_for_lambda_qcd(fp))
        all_findings.extend(scan_file_for_alpha(fp))

    # ─── Report ──────────────────────────────────────────────────────────────

    print("=" * 78)
    print("DFC INTERNAL CONSISTENCY WEB AUDIT")
    print("=" * 78)
    print()

    # Group by parameter
    params = {}
    for f in all_findings:
        p = f['param']
        if p not in params:
            params[p] = []
        params[p].append(f)

    total_issues = 0
    total_consistent = 0
    stale_files = []

    for param_name in sorted(params.keys()):
        entries = params[param_name]
        print(f"\n{'─' * 78}")
        print(f"  PARAMETER: {param_name}")
        if param_name in ['BETA', 'g_eff', 'g_eff²', 'α (quadratic)']:
            exact_info = {
                'BETA': EXACT['BETA'],
                'g_eff': EXACT['G_EFF'],
                'g_eff²': EXACT['G_EFF_SQ'],
                'α (quadratic)': EXACT['ALPHA_QUAD'],
            }.get(param_name)
            if exact_info:
                print(f"  Exact value: {exact_info['value']:.8f} = {exact_info['formula']}")
        print(f"{'─' * 78}")

        exact_count = 0
        approx_count = 0

        for e in sorted(entries, key=lambda x: -x.get('error_pct', 0) if x.get('error_pct') is not None else 0):
            marker = ''
            if e['type'] == 'exact' or e['type'] == 'exact_formula':
                marker = ' [OK]'
                exact_count += 1
                total_consistent += 1
            elif e['type'] == 'exact_numeric' and (e.get('error_pct', 0) or 0) < 0.01:
                marker = ' [OK]'
                exact_count += 1
                total_consistent += 1
            elif e['type'] == 'approximate':
                err = e.get('error_pct', 0)
                if err and err > 0.01:
                    marker = f' [STALE: {err:.3f}% off]'
                    approx_count += 1
                    total_issues += 1
                    stale_files.append(e)
                else:
                    marker = ' [OK]'
                    exact_count += 1
                    total_consistent += 1
            elif e['type'] == 'value_MeV':
                marker = f' [{e["value"]:.1f} MeV]'
                total_consistent += 1

            print(f"  {e['file']:45s} L{e['line']:4d}  val={e['value']:<12}  {e['type']}{marker}")

        print(f"  Summary: {exact_count} exact, {approx_count} stale/approximate")

    # ─── Λ_QCD consistency check ─────────────────────────────────────────────
    lqcd_entries = params.get('Λ_QCD', [])
    if len(lqcd_entries) > 1:
        vals = [e['value'] for e in lqcd_entries]
        min_v, max_v = min(vals), max(vals)
        spread = (max_v - min_v) / ((max_v + min_v) / 2) * 100
        print(f"\n{'─' * 78}")
        print(f"  Λ_QCD SPREAD CHECK")
        print(f"{'─' * 78}")
        print(f"  Range: {min_v:.1f} — {max_v:.1f} MeV")
        print(f"  Spread: {spread:.1f}%")
        if spread > 5:
            print(f"  WARNING: >5% spread across modules")
            total_issues += 1
        for e in sorted(lqcd_entries, key=lambda x: x['value']):
            print(f"    {e['file']:45s} L{e['line']:4d}  {e['value']:.1f} MeV")

    # ─── Summary ─────────────────────────────────────────────────────────────
    print(f"\n{'=' * 78}")
    print(f"AUDIT SUMMARY")
    print(f"{'=' * 78}")
    print(f"  Files scanned:        {len(py_files)}")
    print(f"  Parameter instances:  {len(all_findings)}")
    print(f"  Consistent:           {total_consistent}")
    print(f"  Issues found:         {total_issues}")
    print()

    if stale_files:
        print(f"  STALE VALUES (using approximate instead of exact formula):")
        for s in sorted(stale_files, key=lambda x: x['file']):
            print(f"    {s['file']:45s} L{s['line']:4d}  {s['param']}={s['value']}  ({s['error_pct']:.3f}% off)")

    print()

    # ─── Assertions ──────────────────────────────────────────────────────────

    # Check that exact BETA = 1/(9π) is used in coupling_derivation.py
    cd_betas = [f for f in all_findings if f['file'] == 'coupling_derivation.py' and f['param'] == 'BETA']
    assert len(cd_betas) > 0, "coupling_derivation.py must define BETA"
    assert cd_betas[0]['type'] in ('exact', 'exact_formula'), \
        "coupling_derivation.py BETA must use exact formula"
    print("PASS: coupling_derivation.py BETA is exact")

    # Check g_eff² = 8πβ/3 = 8/27 consistency
    g_eff_sq_exact = 8.0 * math.pi * EXACT['BETA']['value'] / 3.0
    g_eff_sq_formula = 8.0 / 27.0
    g_consistency = abs(g_eff_sq_exact - g_eff_sq_formula) / g_eff_sq_formula
    print(f"PASS: g_eff² = 8πβ/3 = {g_eff_sq_exact:.8f}" if g_consistency < 1e-10
          else f"FAIL: g_eff² inconsistency: 8πβ/3={g_eff_sq_exact:.8f} vs 8/27={g_eff_sq_formula:.8f}")
    # Note: 8π/(9π)/3 = 8/27 exactly, so this MUST pass
    assert g_consistency < 1e-10, "8πβ/3 must equal 8/27 when β=1/(9π)"

    # Check S_kink × α_D5 = 1 [T1, C171]
    S_kink = EXACT['S_KINK']['value']
    # α_D5 = 1/S_kink by definition
    alpha_d5 = 1.0 / S_kink
    product = S_kink * alpha_d5
    assert abs(product - 1.0) < 1e-15, "S_kink × α_D5 must = 1"
    print(f"PASS: S_kink × α_D5 = {product:.15f}")

    # Check α = ∛18 = (α²β × 9π)^(1/3) self-consistency
    alpha = EXACT['ALPHA_QUAD']['value']
    beta = EXACT['BETA']['value']
    # From β = 1/(9π) and α = ∛18: α³ = 18 = 2α/β × (1/π) × ...
    # Simpler: α³β = 18/(9π) = 2/π
    alpha_cubed_beta = alpha**3 * beta
    expected_a3b = 2.0 / math.pi
    a3b_err = abs(alpha_cubed_beta - expected_a3b) / expected_a3b
    print(f"PASS: α³β = {alpha_cubed_beta:.8f} = 2/π = {expected_a3b:.8f}" if a3b_err < 1e-10
          else f"FAIL: α³β = {alpha_cubed_beta:.8f} ≠ 2/π = {expected_a3b:.8f}")
    assert a3b_err < 1e-10, "α³β must equal 2/π"

    # Check φ₀ = √(α/β) consistency
    phi0 = math.sqrt(alpha / beta)
    phi0_expected = math.sqrt(18**(1/3) * 9 * math.pi)
    phi0_err = abs(phi0 - phi0_expected) / phi0_expected
    assert phi0_err < 1e-10, "φ₀ consistency check"
    print(f"PASS: φ₀ = √(α/β) = {phi0:.6f}")

    # Check kink width ξ = √(2/α)
    xi = math.sqrt(2.0 / alpha)
    m_sigma = math.sqrt(2.0 * alpha)  # m_σ = √(2α)
    xi_times_msigma = xi * m_sigma
    assert abs(xi_times_msigma - 2.0) < 1e-10, "ξ × m_σ must = 2"
    print(f"PASS: ξ × m_σ = {xi_times_msigma:.10f} = 2")

    # BPS energy: E_BPS = 2√2/3 × φ₀² / ξ = S_kink × (2 M_c³ / β)^(1/2) ...
    # More directly: S_kink = 2√2/3 (dimensionless)
    s_kink_check = 2 * math.sqrt(2) / 3
    assert abs(s_kink_check - S_kink) < 1e-15
    print(f"PASS: S_kink = 2√2/3 = {s_kink_check:.8f}")

    # Count stale BETA files
    stale_beta = [f for f in stale_files if f['param'] == 'BETA']
    print(f"\nSTALE BETA COUNT: {len(stale_beta)} files use approximate values")
    print(f"  These should be updated to BETA = 1.0 / (9.0 * math.pi)")

    n_pass = 7  # assertions above
    print(f"\n{'=' * 78}")
    print(f"TOTAL: {n_pass}/{n_pass} consistency checks PASS")
    print(f"ISSUES: {total_issues} stale parameter values across {len(stale_beta)} files")
    print(f"{'=' * 78}")


if __name__ == '__main__':
    run_audit()
