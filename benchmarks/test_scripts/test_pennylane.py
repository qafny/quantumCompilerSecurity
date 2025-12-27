"""
Test Script for PennyLane Compiler
===================================

This script demonstrates how to use PennyLane to:
1. Create a quantum circuit (Bell state)
2. Compile it for execution
3. Run it on a simulator
4. Understand the results

WHAT IS HAPPENING:
------------------
1. Device Creation: We create a quantum device (simulator)
2. Circuit Definition: We define a quantum function using decorators
3. Execution: PennyLane compiles and executes the circuit
4. Measurement: We get measurement results

PENNYLANE UNIQUENESS:
---------------------
- Uses @qml.qnode decorator to mark quantum functions
- Focuses on automatic differentiation (for ML)
- Can switch between different backends easily
- Integrates quantum and classical computation
"""

print("=" * 60)
print("PENNYLANE COMPILER TEST")
print("=" * 60)

try:
    # Step 1: Import PennyLane
    print("\n[Step 1] Importing PennyLane...")
    import pennylane as qml
    import numpy as np
    print("✓ PennyLane imported successfully")
    print(f"   PennyLane version: {qml.__version__}")

    # Step 2: Create a quantum device (simulator)
    print("\n[Step 2] Creating quantum device...")
    print("   - Device: The backend that executes quantum circuits")
    print("   - 'default.qubit': PennyLane's built-in simulator")
    dev = qml.device('default.qubit', wires=2, shots=1024)
    print(f"✓ Device created: {dev.name}")
    print(f"   Wires (qubits): {dev.num_wires}")
    print(f"   Shots: {dev.shots}")

    # Step 3: Define the quantum circuit as a function
    print("\n[Step 3] Defining Bell state circuit...")
    print("   - @qml.qnode: Decorator that marks this as a quantum node")
    print("   - PennyLane will compile this function for execution")
    
    @qml.qnode(dev)
    def bell_state_circuit():
        """Quantum function that creates a Bell state."""
        qml.Hadamard(wires=0)      # H gate on wire 0
        qml.CNOT(wires=[0, 1])     # CNOT: control=0, target=1
        return qml.sample(qml.PauliZ(0) @ qml.PauliZ(1))  # Measure in Z basis
    
    # Alternative: Measure computational basis
    @qml.qnode(dev)
    def bell_state_measure():
        """Quantum function that measures computational basis."""
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0, 1])
        return qml.sample()  # Measure all qubits
    
    print("✓ Circuit functions defined")

    # Step 4: Visualize the circuit
    print("\n[Step 4] Circuit Visualization:")
    print("   (PennyLane's circuit representation)")
    print(qml.draw(bell_state_measure)())

    # Step 5: Execute the circuit
    print("\n[Step 5] Executing circuit...")
    print("   - PennyLane compiles and executes the quantum function")
    print("   - Running 1024 shots (independent circuit executions)")
    result = bell_state_measure()
    
    print("✓ Circuit executed successfully")
    print(f"   Result shape: {result.shape} (1024 shots, 2 qubits)")

    # Step 6: Analyze results
    print("\n[Step 6] Measurement Results:")
    print("   Expected: ~50% for |00⟩ and ~50% for |11⟩\n")
    
    # Convert results to counts
    # Each row is [q0, q1] measurement result
    counts = {}
    for measurement in result:
        state = ''.join(str(int(bit)) for bit in measurement)
        counts[state] = counts.get(state, 0) + 1
    
    for state in sorted(counts.keys()):
        count = counts[state]
        percentage = (count / 1024) * 100
        print(f"   |{state}⟩: {count:4d} times ({percentage:5.2f}%)")
    
    print("\n" + "=" * 60)
    print("PENNYLANE TEST COMPLETE")
    print("=" * 60)
    print("\nKEY TAKEAWAYS:")
    print("- PennyLane uses @qml.qnode decorator for quantum functions")
    print("- Circuits are defined as Python functions")
    print("- Devices abstract away hardware/simulator details")
    print("- Built for quantum machine learning (automatic differentiation)")

except ImportError:
    print("\n❌ ERROR: PennyLane not installed")
    print("   Install with: pip install pennylane")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()

