# Compiler Test Scripts

This directory contains test scripts for each quantum compiler.

## What We're Testing

Each compiler will run a **Bell State Circuit**:
1. Start with two qubits in |00⟩ state
2. Apply H (Hadamard) gate to qubit 0 → creates superposition
3. Apply CNOT(0,1) → creates entanglement
4. Result: Bell state (|00⟩ + |11⟩)/√2

This is a standard benchmark because:
- It's simple (only 2 gates)
- It demonstrates key quantum features (superposition, entanglement)
- All compilers should support it

## Running the Tests

### Prerequisites
```bash
# Make sure you're in the virtual environment
cd C:\Users\BardCS-01\Documents\xml-fixing
.\venv\Scripts\Activate.ps1
```

### Test Individual Compilers
```bash
# Test Qiskit
python test_scripts/test_qiskit.py

# Test Cirq
python test_scripts/test_cirq.py

# Test PennyLane
python test_scripts/test_pennylane.py
```

### Test All Available Compilers
```bash
python test_scripts/run_all_tests.py
```

## Understanding the Output

Each test will show:
1. **Circuit Creation**: How the circuit is built
2. **Circuit Visualization**: What the circuit looks like
3. **Compilation/Transpilation**: Any optimizations performed
4. **Execution**: Running the circuit
5. **Results**: Measurement outcomes

