# Getting Started: Testing Quantum Compilers

## What We've Created

I've set up a complete testing framework for quantum compilers. Here's what you have:

### 📁 Directory Structure

```
benchmarks/
├── compilers/           # Documentation for each compiler
│   ├── README.md
│   ├── qiskit.md
│   ├── cirq.md
│   ├── pennylane.md
│   └── ... (others)
│
├── test_scripts/        # Test scripts you'll run
│   ├── README.md
│   ├── test_qiskit.py
│   ├── test_cirq.py
│   ├── test_pennylane.py
│   └── run_all_tests.py
│
├── README.md            # Overview
├── INSTALLATION_GUIDE.md
├── test_compilers_guide.md
└── GETTING_STARTED.md   # This file
```

## Step-by-Step: How to Test Each Compiler

### Step 1: Understand What We're Testing

**Bell State Circuit** (same test for all compilers):
- **Input**: 2 qubits in |00⟩ state
- **Circuit**: 
  1. Apply H gate to qubit 0 (creates superposition)
  2. Apply CNOT(0,1) (creates entanglement)
- **Expected Output**: ~50% |00⟩, ~50% |11⟩
- **Why this test**: Simple, demonstrates key quantum features

### Step 2: Install Compilers

```bash
# Activate your virtual environment
cd C:\Users\BardCS-01\Documents\xml-fixing
.\venv\Scripts\Activate.ps1

# Install Python-based compilers
pip install qiskit cirq pennylane
```

### Step 3: Run Individual Tests

Each test script is **heavily commented** to explain what's happening:

```bash
cd quantumTesting/benchmarks/test_scripts

# Test Qiskit (read the comments to understand!)
python test_qiskit.py

# Test Cirq
python test_cirq.py

# Test PennyLane
python test_pennylane.py
```

### Step 4: Read the Code!

**IMPORTANT**: Each script has detailed comments explaining:
- What each step does
- How the compiler works
- What compilation/optimization happens
- How results are interpreted

## What Each Test Shows You

### 1. **Qiskit Test** (`test_qiskit.py`)
- How to create circuits with Qiskit
- What "transpilation" means (compiling to backend gates)
- How optimization works
- Running circuits on simulators

**Key Concept**: Qiskit "transpiles" circuits to match hardware capabilities

### 2. **Cirq Test** (`test_cirq.py`)
- Cirq's GridQubit system (for 2D hardware)
- How circuits are built incrementally
- Circuit optimization strategies
- Running on simulators

**Key Concept**: Cirq uses 2D qubit layout (matches Google's hardware)

### 3. **PennyLane Test** (`test_pennylane.py`)
- Using @qml.qnode decorator
- Device abstraction (can switch backends easily)
- Function-based circuit definition
- Built for quantum machine learning

**Key Concept**: PennyLane treats circuits as Python functions

## Understanding the Differences

| Compiler | Circuit Creation | Compilation Step | Execution Model |
|----------|-----------------|------------------|-----------------|
| **Qiskit** | `QuantumCircuit()` | `transpile()` | Backend-based |
| **Cirq** | `Circuit()` with `append()` | Optimizers | Simulator-based |
| **PennyLane** | `@qml.qnode` decorator | Automatic | Device-based |

## What to Observe

As you run each test, notice:

1. **Syntax Differences**: How each compiler expresses the same circuit
2. **Compilation Process**: What optimizations happen
3. **Execution Model**: How circuits are run
4. **Results Format**: How measurements are returned

## Next Steps After Testing

1. **Compare Approaches**: Write down what you notice about each compiler
2. **Try Modifications**: Change the circuit (add gates, use 3 qubits)
3. **Read Documentation**: Check the `compilers/` directory for more info
4. **Explore Advanced Features**: Each compiler has unique capabilities

## Troubleshooting

### If a compiler isn't installed:
```bash
pip install [compiler-name]
```

### If tests fail:
- Check error messages carefully
- Make sure virtual environment is activated
- Verify Python version compatibility

### If you don't understand something:
- Read the comments in the test scripts (they explain everything!)
- Check the compiler documentation in `compilers/` directory
- Look at the official compiler websites

## Key Takeaways

After running these tests, you should understand:

1. ✅ How to create quantum circuits in each compiler
2. ✅ What "compilation" means in quantum computing
3. ✅ How simulators work
4. ✅ Differences between compiler approaches
5. ✅ What a Bell state is and why it's important

## Questions to Think About

1. Which compiler's syntax do you prefer? Why?
2. What optimizations did each compiler perform?
3. How do the compilation steps differ?
4. Which compiler would you use for different tasks?

---

**Remember**: The goal is to understand what each compiler does, not just to run the tests. Read the code, understand the comments, and explore!

