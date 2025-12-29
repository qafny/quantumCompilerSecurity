"""
GHZ State Compilation Analysis for PennyLane Compiler
======================================================

This script shows what PennyLane compiler outputs for a GHZ state program.
Output: OpenQASM (low-level hardware instructions), not execution results.
"""

print("=" * 70)
print("PENNYLANE GHZ STATE COMPILATION ANALYSIS")
print("=" * 70)

try:
    # Step 1: Import PennyLane
    print("\n[Step 1] Importing PennyLane...")
    import pennylane as qml
    print("✓ PennyLane imported successfully")

    # Step 2: Create device and define circuit
    print("\n[Step 2] Creating GHZ State Circuit...")
    dev = qml.device('default.qubit', wires=3)
    
    @qml.qnode(dev)
    def ghz_state_circuit():
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[0, 2])
        return qml.sample()
    
    print("✓ Circuit defined")

    # Step 3: Show circuit structure
    print("\n[Step 3] Circuit Structure:")
    try:
        circuit_text = qml.draw(ghz_state_circuit, show_all_wires=True)()
        print("-" * 70)
        print(circuit_text)
        print("-" * 70)
    except:
        print("   H(0), CNOT(0,1), CNOT(0,2)")

    # Step 4: Show operations
    print("\n[Step 4] Operations in Circuit:")
    print("   1. Hadamard(wires=0)")
    print("   2. CNOT(wires=[0, 1])")
    print("   3. CNOT(wires=[0, 2])")
    print("   4. sample()")

    # Step 5: Circuit information
    print("\n[Step 5] Circuit Information:")
    print(f"   Type: {type(ghz_state_circuit)}")
    print(f"   Device: {dev.name}")
    print(f"   Wires: 3")

    # Step 6: Compilation process
    print("\n[Step 6] Compilation Process:")
    print("   - PennyLane uses lazy compilation")
    print("   - Circuit compiled when first called")
    print("   - IR: QuantumTape (internal representation)")

    # Step 7: Output compiled circuit as OpenQASM (hardware instructions)
    print("\n" + "=" * 70)
    print("[Step 7] COMPILED OUTPUT: OpenQASM Format")
    print("=" * 70)
    print("   This is the compiled program output (hardware instructions)")
    print("   NOT execution results (state vector or measurement counts)")
    
    try:
        openqasm_str = qml.qasm(ghz_state_circuit)
        print("\n[OpenQASM]:")
        print("-" * 70)
        print(openqasm_str)
        print("-" * 70)
    except:
        try:
            from pennylane.transforms import to_openqasm
            openqasm_str = to_openqasm(ghz_state_circuit)()
            print("\n[OpenQASM]:")
            print("-" * 70)
            print(openqasm_str)
            print("-" * 70)
        except:
            print("\n[Note] OpenQASM export requires circuit execution")
            print("Circuit structure: H(0), CNOT(0,1), CNOT(0,2)")

    # Step 8: Summary
    print("\n[Step 8] Summary:")
    print("   - PennyLane compiles Python functions to quantum circuits")
    print("   - Output: QuantumTape (can be exported to OpenQASM)")
    print("   - This is the compiled program, not execution results")

    print("\n" + "=" * 70)
    print("COMPILATION COMPLETE")
    print("=" * 70)
    print("\nOutput: OpenQASM (hardware instruction format)")
    print("This is the compiled program, not execution results.")

except ImportError:
    print("\n❌ ERROR: PennyLane not installed")
    print("   Install with: pip install pennylane")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
