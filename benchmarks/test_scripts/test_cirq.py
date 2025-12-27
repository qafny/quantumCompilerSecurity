"""
Test Script for Cirq Compiler
==============================

This script demonstrates how to use Cirq (Google's quantum framework) to:
1. Create a quantum circuit (Bell state)
2. Optimize/compile it
3. Run it on a simulator
4. Understand the results

WHAT IS HAPPENING:
------------------
1. Circuit Creation: We build a quantum circuit with 2 qubits
2. Optimization: Cirq may optimize the circuit
3. Simulation: We run the circuit on a quantum simulator
4. Measurement: We measure the qubits and get results

CIRQ VS QISKIT:
---------------
- Cirq uses GridQubit for 2D hardware layout (Google's Sycamore)
- Qiskit uses linear qubit indices
- Both create the same Bell state, but with different syntax
"""

print("=" * 60)
print("CIRQ COMPILER TEST")
print("=" * 60)

try:
    # Step 1: Import Cirq
    print("\n[Step 1] Importing Cirq...")
    import cirq
    print("✓ Cirq imported successfully")
    print(f"   Cirq version: {cirq.__version__}")

    # Step 2: Create qubits (Cirq uses GridQubit for hardware layout)
    print("\n[Step 2] Creating qubits...")
    print("   - Cirq uses GridQubit for 2D hardware layout")
    print("   - This matches Google's Sycamore processor layout")
    q0 = cirq.GridQubit(0, 0)
    q1 = cirq.GridQubit(0, 1)
    print(f"✓ Created qubits: {q0}, {q1}")

    # Step 3: Create a quantum circuit
    print("\n[Step 3] Creating Bell state circuit...")
    circuit = cirq.Circuit()
    
    # Apply gates to create Bell state
    circuit.append(cirq.H(q0))      # Hadamard gate on qubit 0
    circuit.append(cirq.CNOT(q0, q1))  # CNOT: control=q0, target=q1
    circuit.append(cirq.measure(q0, q1, key='result'))  # Measure
    
    print("✓ Circuit created:")
    print(circuit)

    # Step 4: Optimize the circuit (Cirq's compilation step)
    print("\n[Step 4] Optimizing circuit...")
    print("   - Cirq can optimize circuits using strategies")
    print("   - We'll use MergeSingleQubitGates optimizer")
    optimized_circuit = cirq.optimize_for_target_gateset(
        circuit, 
        gateset=cirq.Gateset(cirq.H, cirq.CNOT, cirq.MeasurementGate)
    )
    print(f"✓ Circuit optimized")
    print(f"   Original circuit length: {len(circuit)}")
    print(f"   Optimized circuit length: {len(optimized_circuit)}")

    # Step 5: Run the circuit
    print("\n[Step 5] Running circuit on quantum simulator...")
    print("   - Cirq simulator: Classical simulation of quantum circuits")
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)
    
    print("✓ Circuit executed successfully")

    # Step 6: Display results
    print("\n[Step 6] Measurement Results:")
    print("   Expected: ~50% for |00⟩ and ~50% for |11⟩\n")
    
    # Count results
    counts = {}
    for measurement in result.measurements['result']:
        # Convert [0,0] or [1,1] to binary string
        state = ''.join(str(bit) for bit in measurement)
        counts[state] = counts.get(state, 0) + 1
    
    for state in sorted(counts.keys()):
        count = counts[state]
        percentage = (count / 1024) * 100
        print(f"   |{state}⟩: {count:4d} times ({percentage:5.2f}%)")
    
    print("\n" + "=" * 60)
    print("CIRQ TEST COMPLETE")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("- Cirq uses GridQubit for 2D hardware layout")
    print("- Circuits are built incrementally with append()")
    print("- Optimizers can transform circuits before execution")
    print("- Results match Qiskit: Bell state entanglement")

except ImportError:
    print("\n❌ ERROR: Cirq not installed")
    print("   Install with: pip install cirq")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()

