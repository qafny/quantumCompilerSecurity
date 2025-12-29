"""
GHZ State Compilation Analysis for tket Compiler
=================================================

This script shows what tket compiler outputs for a GHZ state program.
Output: OpenQASM (low-level hardware instructions), not execution results.
"""

print("=" * 70)
print("TKET GHZ STATE COMPILATION ANALYSIS")
print("=" * 70)

try:
    # Step 1: Import pytket
    print("\n[Step 1] Importing pytket...")
    from pytket import Circuit
    from pytket.extensions.qiskit import AerBackend
    print("✓ pytket imported successfully")

    # Step 2: Create circuit
    print("\n[Step 2] Creating GHZ State Circuit...")
    circuit = Circuit(3)
    circuit.H(0)
    circuit.CX(0, 1)
    circuit.CX(0, 2)
    circuit.measure_all()
    print("✓ Circuit created")

    # Step 3: Show original circuit
    print("\n[Step 3] Original Circuit:")
    print("-" * 70)
    print(circuit)
    print("-" * 70)

    # Step 4: Compile the circuit
    print("\n[Step 4] Compiling circuit...")
    backend = AerBackend()
    compiled_circuit = backend.get_compiled_circuit(circuit)
    print("✓ Circuit compiled")

    # Step 5: Show compiled circuit structure
    print("\n[Step 5] Compiled Circuit Structure:")
    print("-" * 70)
    print(compiled_circuit)
    print("-" * 70)

    # Step 6: Show compilation statistics
    print("\n[Step 6] Compilation Statistics:")
    print(f"   Original gates: {len(circuit.get_commands())}")
    print(f"   Compiled gates: {len(compiled_circuit.get_commands())}")
    print(f"   Original depth: {circuit.depth()}")
    print(f"   Compiled depth: {compiled_circuit.depth()}")

    # Step 7: Show gate sequence
    print("\n[Step 7] Compiled Gate Sequence:")
    for i, cmd in enumerate(compiled_circuit.get_commands()):
        op = cmd.op
        qubits = cmd.args
        print(f"   {i+1}. {op.type.name}({', '.join(map(str, [q.index[0] for q in qubits]))})")

    # Step 8: Output compiled circuit as OpenQASM (hardware instructions)
    print("\n" + "=" * 70)
    print("[Step 8] COMPILED OUTPUT: OpenQASM Format")
    print("=" * 70)
    print("   This is the compiled program output (hardware instructions)")
    print("   NOT execution results (state vector or measurement counts)")
    
    try:
        from pytket.qasm import circuit_to_qasm_str
        openqasm_str = circuit_to_qasm_str(compiled_circuit)
        print("\n[OpenQASM]:")
        print("-" * 70)
        print(openqasm_str)
        print("-" * 70)
    except:
        try:
            openqasm_str = compiled_circuit.get_qasm_str()
            print("\n[OpenQASM]:")
            print("-" * 70)
            print(openqasm_str)
            print("-" * 70)
        except:
            print("\n[Note] OpenQASM export not available")
            print("Showing circuit structure instead")

    print("\n" + "=" * 70)
    print("COMPILATION COMPLETE")
    print("=" * 70)
    print("\nOutput: OpenQASM (hardware instruction format)")
    print("This is the compiled program, not execution results.")

except ImportError:
    print("\n❌ ERROR: pytket not installed")
    print("   Install with: pip install pytket pytket-qiskit")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
