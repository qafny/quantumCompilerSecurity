"""
Test Script for Qiskit Compiler
================================

This script demonstrates how to use Qiskit to:
1. Create a quantum circuit (Bell state)
2. Compile/transpile it
3. Run it on a simulator
4. Understand the results

WHAT IS HAPPENING:
------------------
1. Circuit Creation: We build a quantum circuit with 2 qubits
2. Transpilation: Qiskit optimizes the circuit for the target backend
3. Simulation: We run the circuit on a quantum simulator
4. Measurement: We measure the qubits and get results

BELL STATE EXPLANATION:
-----------------------
- H gate on qubit 0: Creates superposition (|0⟩ + |1⟩)/√2
- CNOT gate: Entangles qubits 0 and 1
- Result: Bell state (|00⟩ + |11⟩)/√2
- When measured, we get either |00⟩ or |11⟩ with 50% probability each
"""

print("=" * 60)
print("QISKIT COMPILER TEST")
print("=" * 60)

try:
    # Step 1: Import Qiskit
    print("\n[Step 1] Importing Qiskit...")
    from qiskit import QuantumCircuit, transpile
    from qiskit.providers.aer import AerSimulator
    from qiskit.visualization import plot_histogram
    print("✓ Qiskit imported successfully")

    # Step 2: Create a quantum circuit
    print("\n[Step 2] Creating Bell state circuit...")
    print("   - 2 qubits, 2 classical bits for measurement")
    qc = QuantumCircuit(2, 2)
    
    # Apply gates to create Bell state
    qc.h(0)        # Hadamard gate on qubit 0 (creates superposition)
    qc.cx(0, 1)    # CNOT gate: control=0, target=1 (creates entanglement)
    qc.measure_all()  # Measure all qubits
    
    print("✓ Circuit created:")
    print(qc.draw(output='text'))

    # Step 3: Transpile (compile) the circuit
    print("\n[Step 3] Transpiling circuit for simulator...")
    print("   - Transpilation: Converts circuit to gates supported by backend")
    print("   - Optimization: May simplify or optimize the circuit")
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator, optimization_level=1)
    print(f"✓ Circuit compiled")
    print(f"   Original depth: {qc.depth()}")
    print(f"   Compiled depth: {compiled_circuit.depth()}")

    # Step 4: Run the circuit
    print("\n[Step 4] Running circuit on quantum simulator...")
    print("   - Simulator: Classical computer simulating quantum behavior")
    print("   - Shots: Number of times to run the circuit")
    job = simulator.run(compiled_circuit, shots=1024)
    result = job.result()
    counts = result.get_counts(compiled_circuit)
    
    print("✓ Circuit executed successfully")

    # Step 5: Display results
    print("\n[Step 5] Measurement Results:")
    print("   Expected: ~50% for |00⟩ and ~50% for |11⟩")
    print("   (Small variations are normal due to quantum randomness)\n")
    
    for state, count in sorted(counts.items()):
        percentage = (count / 1024) * 100
        print(f"   |{state}⟩: {count:4d} times ({percentage:5.2f}%)")
    
    print("\n" + "=" * 60)
    print("QISKIT TEST COMPLETE")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("- Qiskit uses 'transpile' for compilation/optimization")
    print("- Circuits can be optimized before execution")
    print("- Simulator gives us measurement statistics")
    print("- Bell state shows quantum entanglement in action")

except ImportError:
    print("\n❌ ERROR: Qiskit not installed")
    print("   Install with: pip install qiskit")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()

