"""
Run All Compiler Tests
======================

This script runs all available compiler tests and summarizes the results.

WHAT THIS DOES:
---------------
1. Checks which compilers are installed
2. Runs tests for each available compiler
3. Summarizes results and installation status
"""

import sys
import subprocess

print("=" * 60)
print("QUANTUM COMPILERS BENCHMARK - FULL TEST SUITE")
print("=" * 60)

# List of compiler tests
compilers = [
    ("Qiskit", "test_qiskit.py"),
    ("Cirq", "test_cirq.py"),
    ("PennyLane", "test_pennylane.py"),
    # Future: Add tests for Silq, VOQC, ScaffCC, Quipper
]

results = {}

print("\nTesting available compilers...\n")

for compiler_name, test_file in compilers:
    print(f"\n{'='*60}")
    print(f"Testing {compiler_name}...")
    print(f"{'='*60}")
    
    try:
        # Run the test script
        result = subprocess.run(
            [sys.executable, test_file],
            capture_output=False,
            text=True,
            cwd="."
        )
        
        if result.returncode == 0:
            results[compiler_name] = "✓ PASSED"
            print(f"\n✓ {compiler_name} test completed successfully")
        else:
            results[compiler_name] = f"✗ FAILED (exit code: {result.returncode})"
            print(f"\n✗ {compiler_name} test failed")
            
    except FileNotFoundError:
        results[compiler_name] = "✗ TEST FILE NOT FOUND"
        print(f"\n✗ Test file not found: {test_file}")
    except Exception as e:
        results[compiler_name] = f"✗ ERROR: {str(e)}"
        print(f"\n✗ Error running {compiler_name} test: {e}")

# Summary
print("\n" + "=" * 60)
print("TEST SUMMARY")
print("=" * 60)
print("\nCompiler Test Results:\n")

for compiler, status in results.items():
    print(f"  {compiler:15s}: {status}")

# Installation status
print("\n" + "=" * 60)
print("INSTALLATION STATUS")
print("=" * 60)
print("\nTo install missing compilers:\n")

install_commands = {
    "Qiskit": "pip install qiskit",
    "Cirq": "pip install cirq",
    "PennyLane": "pip install pennylane",
}

for compiler, status in results.items():
    if "PASSED" not in status:
        if compiler in install_commands:
            print(f"  {compiler}: {install_commands[compiler]}")

print("\n" + "=" * 60)
print("NEXT STEPS")
print("=" * 60)
print("""
1. Install any missing compilers using the commands above
2. Review individual test scripts to understand how each compiler works
3. Compare the approaches: syntax, compilation steps, execution models
4. Consider creating benchmark tests for more complex circuits
""")

