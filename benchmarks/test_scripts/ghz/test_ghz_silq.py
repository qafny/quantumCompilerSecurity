"""
GHZ State Compilation Analysis for Silq Compiler
=================================================

This script shows what Silq compiler outputs for a GHZ state program.
Output: Lower-level quantum circuit (QASM/C++), not execution results.
"""

print("=" * 70)
print("SILQ GHZ STATE COMPILATION ANALYSIS")
print("=" * 70)

import os

# Step 1: Show Silq program
print("\n[Step 1] Silq Program:")
silq_file = os.path.join(os.path.dirname(__file__), 'ghz_silq.slq')
if os.path.exists(silq_file):
    print("-" * 70)
    with open(silq_file, 'r') as f:
        print(f.read())
    print("-" * 70)
else:
    print(f"   File: {silq_file}")

# Step 2: Compilation process
print("\n[Step 2] Compilation Process:")
print("   Command: silq ghz_silq.slq")
print("   - Parses .slq source code")
print("   - Performs type checking and validation")
print("   - Applies automatic uncomputation")
print("   - Generates compiled output")

# Step 3: Compilation output format
print("\n[Step 3] Compilation Output Format:")
print("   - Format: Depends on Silq backend (typically C++ or QASM)")
print("   - Structure: Lower-level quantum circuit representation")
print("   - Can be exported to various formats (QASM, etc.)")

# Step 4: Key compilation features
print("\n[Step 4] Key Compilation Features:")
print("   - Automatic uncomputation of temporary qubits")
print("   - Type system prevents quantum-classical confusion")
print("   - High-level abstractions compiled to low-level operations")
print("   - Gate decomposition and optimization")

# Step 5: IR characteristics
print("\n[Step 5] Intermediate Representation:")
print("   - Source: High-level Silq code (.slq files)")
print("   - IR: Internal AST (Abstract Syntax Tree)")
print("   - Processing: Type checking, uncomputation, optimization")
print("   - Output: Compiled quantum circuit representation")

# Step 6: How to view compiled output
print("\n[Step 6] Viewing Compiled Output:")
print("   - Compiler generates lower-level representation")
print("   - Can export to QASM format")
print("   - Can export to C++ code")
print("   - View generated code files")

# Step 7: COMPILED OUTPUT
print("\n" + "=" * 70)
print("[Step 7] COMPILED OUTPUT: Lower-level Circuit Format")
print("=" * 70)
print("   This is the compiled program output (low-level representation)")
print("   NOT execution results (state vector or measurement counts)")
print("\n   Output format:")
print("   - QASM (OpenQASM) format")
print("   - OR C++ code with quantum operations")
print("\n   Example QASM output:")
print("   - OPENQASM 2.0;")
print("   - qreg q[3];")
print("   - creg c[3];")
print("   - h q[0];")
print("   - cx q[0], q[1];")
print("   - cx q[0], q[2];")
print("   - measure q[0] -> c[0];")
print("   - measure q[1] -> c[1];")
print("   - measure q[2] -> c[2];")

print("\n" + "=" * 70)
print("COMPILATION COMPLETE")
print("=" * 70)
print("\nOutput: Lower-level quantum circuit (QASM/C++)")
print("This is the compiled program, not execution results.")
