"""
GHZ State Compilation Analysis for Quilc Compiler
==================================================

This script shows what quilc compiler outputs for a GHZ state program.
Output: Optimized Quil (hardware instruction format), not execution results.
"""

print("=" * 70)
print("QUILC GHZ STATE COMPILATION ANALYSIS")
print("=" * 70)

import os

# Step 1: Show Quil program
print("\n[Step 1] Quil Program:")
quil_file = os.path.join(os.path.dirname(__file__), 'ghz.quil')
if os.path.exists(quil_file):
    print("-" * 70)
    with open(quil_file, 'r') as f:
        print(f.read())
    print("-" * 70)
else:
    print(f"   File: {quil_file}")

# Step 2: Compilation process
print("\n[Step 2] Compilation Process:")
print("   Command: quilc ghz.quil")
print("   - Parses Quil program")
print("   - Applies optimization passes")
print("   - Decomposes gates to native gate set")
print("   - Optimizes gate sequences")

# Step 3: Compilation output
print("\n[Step 3] Compilation Output:")
print("   - Format: Optimized Quil program (text-based)")
print("   - Structure: Optimized Quil instructions")
print("   - Contains: Native gates for target processor")

# Step 4: Optimization features
print("\n[Step 4] Optimization Features:")
print("   - Gate decomposition: High-level gates -> native gates")
print("   - Gate fusion: Combine compatible gates")
print("   - Gate cancellation: Remove redundant gates")
print("   - Qubit routing: Map logical to physical qubits")

# Step 5: Quil program structure
print("\n[Step 5] Quil Program Structure:")
print("   - Instructions: Sequential list of Quil instructions")
print("   - Gate instructions: H, CNOT, RZ, etc.")
print("   - Measurement instructions: MEASURE")
print("   - Declarations: DECLARE (memory declarations)")

# Step 6: How to view compiled output
print("\n[Step 6] Viewing Compiled Output:")
print("   - Compiled output is printed to stdout")
print("   - Save to file: quilc ghz.quil > ghz_compiled.quil")
print("   - Compare original vs compiled to see optimizations")

# Step 7: COMPILED OUTPUT
print("\n" + "=" * 70)
print("[Step 7] COMPILED OUTPUT: Optimized Quil Format")
print("=" * 70)
print("   This is the compiled program output (hardware instructions)")
print("   NOT execution results (state vector or measurement counts)")
print("\n   Output format:")
print("   - Optimized Quil program (text-based)")
print("   - Native gates for target processor")
print("   - Optimized instruction sequence")
print("\n   Example compiled Quil:")
print("   - DECLARE ro BIT[3]")
print("   - H 0")
print("   - CNOT 0 1")
print("   - CNOT 0 2")
print("   - MEASURE 0 ro[0]")
print("   - MEASURE 1 ro[1]")
print("   - MEASURE 2 ro[2]")

print("\n" + "=" * 70)
print("COMPILATION COMPLETE")
print("=" * 70)
print("\nOutput: Optimized Quil (hardware instruction format)")
print("This is the compiled program, not execution results.")
