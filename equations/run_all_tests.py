#!/usr/bin/env python3
"""
DFC Model — Full Test Suite Runner
====================================

Runs every equation module in the equations/ directory and produces a scorecard.
Each module is run as a subprocess; its stdout is parsed for [PASS] and [FAIL]
lines to build an aggregate report.

Usage:
    python3 equations/run_all_tests.py              # run all modules
    python3 equations/run_all_tests.py --fast        # skip slow modules (>30s)
    python3 equations/run_all_tests.py --filter qcd  # only modules matching 'qcd'
    python3 equations/run_all_tests.py --failures    # only show modules with failures
    python3 equations/run_all_tests.py --summary     # one-line-per-module output

Output:
    For each module: filename, pass count, fail count, runtime, status
    Final scorecard: total modules, total pass, total fail, overall rate
"""

import subprocess
import sys
import os
import time
import re
import argparse

# ─── Configuration ───────────────────────────────────────────────────────────

# Modules to skip (not standalone tests, or infrastructure)
SKIP_MODULES = {
    '__init__.py',
    'constants.py',
    'dfc_core.py',         # tested separately
    'run_all_tests.py',    # this file
    'freeform_math_exploration.py',  # exploration, not a test
}

# Modules known to be slow (>30 seconds)
SLOW_MODULES = {
    'substrate_simulation.py',
    'complex_field_u1_simulation.py',
    'kink_kink_potential.py',
    'ym_balaban_rg.py',
    'ym_seiler_simon_su3.py',
    'ym_constructive_qft.py',
    'ym_continuum_limit.py',
    'ym_r1_continuum_bound.py',
    'ym_r2_gaussian_limit.py',
}

# Maximum time per module (seconds)
TIMEOUT = 120


def run_module(filepath, timeout=TIMEOUT):
    """Run a single equation module and parse its output.

    Returns:
        dict with keys: name, passes, fails, checks (list), runtime, error
    """
    name = os.path.basename(filepath)
    result = {
        'name': name,
        'passes': 0,
        'fails': 0,
        'checks': [],
        'runtime': 0.0,
        'error': None,
        'status': 'OK',
    }

    start = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, filepath],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=os.path.dirname(os.path.abspath(filepath)) or '.',
        )
        result['runtime'] = time.time() - start

        # Parse output for [PASS] and [FAIL] lines
        for line in proc.stdout.split('\n'):
            line_stripped = line.strip()
            if '[PASS]' in line_stripped:
                result['passes'] += 1
                # Extract the label after [PASS]
                match = re.search(r'\[PASS\]\s*(.*)', line_stripped)
                if match:
                    result['checks'].append(('PASS', match.group(1).strip()))
            elif '[FAIL]' in line_stripped:
                result['fails'] += 1
                match = re.search(r'\[FAIL\]\s*(.*)', line_stripped)
                if match:
                    result['checks'].append(('FAIL', match.group(1).strip()))

        if proc.returncode != 0 and result['passes'] == 0:
            result['error'] = proc.stderr[-200:] if proc.stderr else 'nonzero exit'
            result['status'] = 'ERROR'
        elif result['fails'] > 0:
            result['status'] = 'FAIL'

    except subprocess.TimeoutExpired:
        result['runtime'] = time.time() - start
        result['error'] = f'TIMEOUT after {timeout}s'
        result['status'] = 'TIMEOUT'
    except Exception as e:
        result['runtime'] = time.time() - start
        result['error'] = str(e)[:200]
        result['status'] = 'ERROR'

    return result


def main():
    parser = argparse.ArgumentParser(description='DFC Model Test Suite')
    parser.add_argument('--fast', action='store_true',
                        help='Skip slow modules (>30s)')
    parser.add_argument('--filter', type=str, default=None,
                        help='Only run modules matching this substring')
    parser.add_argument('--failures', action='store_true',
                        help='Only show modules with failures')
    parser.add_argument('--summary', action='store_true',
                        help='One-line-per-module compact output')
    parser.add_argument('--timeout', type=int, default=TIMEOUT,
                        help=f'Timeout per module in seconds (default: {TIMEOUT})')
    args = parser.parse_args()

    # Find all equation modules
    eq_dir = os.path.dirname(os.path.abspath(__file__))
    all_files = sorted([
        f for f in os.listdir(eq_dir)
        if f.endswith('.py') and f not in SKIP_MODULES
    ])

    # Apply filters
    if args.fast:
        all_files = [f for f in all_files if f not in SLOW_MODULES]
    if args.filter:
        all_files = [f for f in all_files if args.filter.lower() in f.lower()]

    n_total = len(all_files)
    print("=" * 78)
    print(f"DFC Model — Full Test Suite ({n_total} modules)")
    print("=" * 78)
    print()

    # Run all modules
    results = []
    total_pass = 0
    total_fail = 0
    total_error = 0
    total_no_checks = 0

    for i, fname in enumerate(all_files):
        filepath = os.path.join(eq_dir, fname)
        if not args.summary:
            print(f"[{i+1}/{n_total}] Running {fname}...", end='', flush=True)

        result = run_module(filepath, timeout=args.timeout)
        results.append(result)

        total_pass += result['passes']
        total_fail += result['fails']
        if result['status'] == 'ERROR' or result['status'] == 'TIMEOUT':
            total_error += 1
        if result['passes'] == 0 and result['fails'] == 0 and result['status'] == 'OK':
            total_no_checks += 1

        if args.summary:
            # Compact one-line output
            p = result['passes']
            f = result['fails']
            t = result['runtime']
            s = result['status']
            if args.failures and s == 'OK':
                continue
            marker = ' ***' if f > 0 else ''
            print(f"  {fname:<50s}  {p:>3d}P {f:>2d}F  {t:>5.1f}s  {s}{marker}")
        else:
            # Verbose output
            p = result['passes']
            f = result['fails']
            t = result['runtime']
            if result['status'] == 'OK' and p > 0:
                print(f" {p}/{p+f} PASS  ({t:.1f}s)")
            elif result['status'] == 'OK' and p == 0:
                print(f" no checks  ({t:.1f}s)")
            elif result['status'] == 'FAIL':
                print(f" {p}/{p+f} PASS, {f} FAIL  ({t:.1f}s)")
                for status, label in result['checks']:
                    if status == 'FAIL':
                        print(f"       [FAIL] {label}")
            elif result['status'] == 'TIMEOUT':
                print(f" TIMEOUT ({t:.0f}s)")
            elif result['status'] == 'ERROR':
                print(f" ERROR ({t:.1f}s)")
                if result['error']:
                    # Show last line of error
                    last_line = result['error'].strip().split('\n')[-1]
                    print(f"       {last_line[:70]}")

    # ─── Final Scorecard ─────────────────────────────────────────────────────

    print()
    print("=" * 78)
    print("SCORECARD")
    print("=" * 78)
    print()

    n_with_checks = sum(1 for r in results if r['passes'] + r['fails'] > 0)
    n_all_pass = sum(1 for r in results if r['fails'] == 0 and r['passes'] > 0)
    n_with_fails = sum(1 for r in results if r['fails'] > 0)
    n_errors = sum(1 for r in results if r['status'] in ('ERROR', 'TIMEOUT'))
    total_time = sum(r['runtime'] for r in results)

    print(f"  Modules tested:        {n_total}")
    print(f"  With check() tests:    {n_with_checks}")
    print(f"  All checks pass:       {n_all_pass}")
    print(f"  With failures:         {n_with_fails}")
    print(f"  Errors/timeouts:       {n_errors}")
    print(f"  No checks (info only): {total_no_checks}")
    print()
    print(f"  Total assertions:      {total_pass + total_fail}")
    print(f"  Total PASS:            {total_pass}")
    print(f"  Total FAIL:            {total_fail}")
    if total_pass + total_fail > 0:
        rate = total_pass / (total_pass + total_fail) * 100
        print(f"  Pass rate:             {rate:.1f}%")
    print()
    print(f"  Total runtime:         {total_time:.1f}s ({total_time/60:.1f}min)")
    print()

    # ─── Failure Details ─────────────────────────────────────────────────────

    if n_with_fails > 0:
        print("-" * 78)
        print("FAILURES:")
        print("-" * 78)
        for r in results:
            if r['fails'] > 0:
                print(f"\n  {r['name']} ({r['fails']} fail):")
                for status, label in r['checks']:
                    if status == 'FAIL':
                        print(f"    [FAIL] {label}")

    if n_errors > 0:
        print()
        print("-" * 78)
        print("ERRORS:")
        print("-" * 78)
        for r in results:
            if r['status'] in ('ERROR', 'TIMEOUT'):
                err_msg = r['error'] or 'unknown'
                last_line = err_msg.strip().split('\n')[-1][:60]
                print(f"  {r['name']}: {last_line}")

    print()

    # Exit code: 0 if all pass, 1 if any fail
    sys.exit(1 if total_fail > 0 or n_errors > 0 else 0)


if __name__ == '__main__':
    main()
