"""
Run All GHZ State Tests
========================

This script runs all available GHZ state tests for Python-based quantum compilers.
It attempts to run each test and reports which ones succeeded or failed.
"""

import sys
import subprocess
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# List of Python-based test scripts
test_scripts = [
    'test_ghz_qiskit.py',
    'test_ghz_pennylane.py',
    'test_ghz_projectq.py',
    'test_ghz_tket.py',
    'test_ghz_pyquil.py',
]

# List of info scripts (these don't run actual tests, just show instructions)
info_scripts = [
    'test_ghz_silq.py',
    'test_ghz_scaffcc.py',
    'test_ghz_qsharp.py',
    'test_ghz_quilc.py',
]

def run_test(script_name):
    """Run a test script and return (success, output)."""
    script_path = os.path.join(script_dir, script_name)
    if not os.path.exists(script_path):
        return (False, f"Script not found: {script_path}")
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=60  # 60 second timeout
        )
        success = result.returncode == 0
        output = result.stdout + result.stderr
        return (success, output)
    except subprocess.TimeoutExpired:
        return (False, "Test timed out after 60 seconds")
    except Exception as e:
        return (False, f"Error running test: {e}")

def main():
    print("=" * 70)
    print("RUNNING ALL GHZ STATE TESTS")
    print("=" * 70)
    print()
    
    results = {}
    
    # Run Python-based tests
    print("Running Python-based compiler tests...")
    print("-" * 70)
    for script in test_scripts:
        print(f"\n[{script}]")
        success, output = run_test(script)
        results[script] = (success, output)
        
        if success:
            print(f"✓ {script} completed successfully")
            # Print last 20 lines of output
            lines = output.strip().split('\n')
            print("\n".join(lines[-20:]))
        else:
            print(f"✗ {script} failed or not installed")
            if "not installed" in output.lower() or "import" in output.lower():
                print(f"  → Install required package to run this test")
    
    # Show info about language-based tests
    print("\n" + "=" * 70)
    print("Language-based compiler tests (require separate setup)")
    print("-" * 70)
    for script in info_scripts:
        script_path = os.path.join(script_dir, script)
        if os.path.exists(script_path):
            print(f"\n[{script}]")
            print(f"  → Run 'python {script}' for instructions")
        else:
            print(f"\n[{script}]")
            print(f"  → File not found")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    successful = [name for name, (success, _) in results.items() if success]
    failed = [name for name, (success, _) in results.items() if not success]
    
    print(f"\nSuccessful tests: {len(successful)}/{len(test_scripts)}")
    for name in successful:
        print(f"  ✓ {name}")
    
    if failed:
        print(f"\nFailed/not installed: {len(failed)}/{len(test_scripts)}")
        for name in failed:
            print(f"  ✗ {name}")
    
    print("\n" + "=" * 70)
    print("Note: Language-based tests (Silq, ScaffCC, Q#, Quilc) require")
    print("      separate installation. Run their test scripts for instructions.")
    print("=" * 70)

if __name__ == '__main__':
    main()

