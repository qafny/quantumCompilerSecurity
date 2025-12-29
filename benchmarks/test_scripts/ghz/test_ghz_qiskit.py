"""
GHZ State Compilation Analysis for Qiskit Compiler
===================================================

This script shows what Qiskit compiler outputs for a GHZ state program.
Output: OpenQASM (low-level hardware instructions), not execution results.
"""

print("=" * 70)
print("QISKIT GHZ STATE COMPILATION ANALYSIS")
print("=" * 70)

try:
    # Step 1: Import Qiskit
    print("\n[Step 1] Importing Qiskit...")
    from qiskit import QuantumCircuit, transpile
    try:
        from qiskit_aer import AerSimulator
    except ImportError:
        from qiskit.providers.aer import AerSimulator
    print("✓ Qiskit imported successfully")

    # Step 2: Create GHZ state circuit
    print("\n[Step 2] Creating GHZ State Circuit...")
    qc = QuantumCircuit(3, 3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.measure_all()
    print("✓ Circuit created")

    # Step 3: Compile the circuit
    print("\n[Step 3] Compiling circuit...")
    simulator = AerSimulator()
    compiled = transpile(qc, simulator, optimization_level=1)
    print("✓ Circuit compiled")

    # Step 4: Show compiled circuit structure
    print("\n[Step 4] Compiled Circuit Structure:")
    print("-" * 70)
    print(compiled.draw(output='text'))
    print("-" * 70)

    # Step 5: Show gate sequence
    print("\n[Step 5] Compiled Gate Sequence:")
    for i, instruction in enumerate(compiled.data):
        gate_name = instruction.operation.name
        if gate_name == 'barrier':
            continue
        qubits = [compiled.find_bit(q).index for q in instruction.qubits]
        print(f"   {i+1}. {gate_name.upper()}({', '.join(map(str, qubits))})")

    # Step 6: Show compilation statistics
    print("\n[Step 6] Compilation Statistics:")
    print(f"   Original gates: {len(qc.data)}")
    print(f"   Compiled gates: {len(compiled.data)}")
    print(f"   Original depth: {qc.depth()}")
    print(f"   Compiled depth: {compiled.depth()}")

    # Step 7: Output compiled circuit as OpenQASM (hardware instructions)
    print("\n" + "=" * 70)
    print("[Step 7] COMPILED OUTPUT: OpenQASM Format")
    print("=" * 70)
    print("   This is the compiled program output (hardware instructions)")
    print("   NOT execution results (state vector or measurement counts)")
    
    try:
        openqasm_str = compiled.qasm()
        print("\n[OpenQASM 2.0]:")
        print("-" * 70)
        print(openqasm_str)
        print("-" * 70)
    except:
        try:
            from qiskit import qasm2
            openqasm_str = qasm2.dumps(compiled)
            print("\n[OpenQASM 3.0]:")
            print("-" * 70)
            print(openqasm_str)
            print("-" * 70)
        except:
            print("\n[Note] OpenQASM export not available")

    print("\n" + "=" * 70)
    print("COMPILATION COMPLETE")
    print("=" * 70)
    print("\nOutput: OpenQASM (hardware instruction format)")
    print("This is the compiled program, not execution results.")

except ImportError:
    print("\n❌ ERROR: Qiskit not installed")
    print("   Install with: pip install qiskit")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
