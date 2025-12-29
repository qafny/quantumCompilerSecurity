# GHZ State Compilation Analysis Scripts

This directory contains compilation analysis scripts for creating GHZ (Greenberger–Horne–Zeilinger) states using various quantum compilers.

## Purpose

These scripts analyze **how different quantum compilers compile** the same GHZ state algorithm, focusing on:
- **Compilation process**: How the compiler processes the program
- **Output format**: What the compiler generates (circuit object, IR, binary, etc.)
- **Intermediate representation**: The internal representation used during compilation
- **Circuit structure**: The structure of the compiled circuit/program
- **Consumption method**: How the compiled output is consumed by backends

**Note**: These scripts focus on compilation analysis, NOT execution/measurement results.

## What is a GHZ State?

A GHZ state for 3 qubits is:
- **State**: |GHZ⟩ = (|000⟩ + |111⟩)/√2
- **Circuit**: H(0) → CNOT(0,1) → CNOT(0,2)
- **Properties**: Perfect correlation - all qubits are either all 0 or all 1

This is an ideal benchmark because:
- It's simple (only 3 gates)
- All compilers should support it
- Allows comparison of compilation approaches
- Shows how different compilers handle the same algorithm

## Available Compilation Analyses

### Python-based Compilers

1. **Qiskit** (`test_ghz_qiskit.py`)
   - Run: `python test_ghz_qiskit.py`
   - Install: `pip install qiskit`
   - Output: QuantumCircuit object (Python class)
   - IR: QuantumCircuit with Instruction objects
   - Consumption: backend.run(circuit)

2. **PennyLane** (`test_ghz_pennylane.py`)
   - Run: `python test_ghz_pennylane.py`
   - Install: `pip install pennylane`
   - Output: QNode (compiled quantum function)
   - IR: QuantumTape (internal representation)
   - Consumption: Direct function call or gradient computation

3. **ProjectQ** (`test_ghz_projectq.py`)
   - Run: `python test_ghz_projectq.py`
   - Install: `pip install projectq`
   - Output: Command objects (streaming)
   - IR: Command objects
   - Consumption: Backend receives commands via flush()

4. **tket** (`test_ghz_tket.py`)
   - Run: `python test_ghz_tket.py`
   - Install: `pip install pytket pytket-qiskit`
   - Output: Circuit object (optimized)
   - IR: Circuit object with Command objects
   - Consumption: backend.process_circuit(circuit)

5. **PyQuil** (`test_ghz_pyquil.py`)
   - Run: `python test_ghz_pyquil.py`
   - Install: `pip install pyquil`
   - Note: Requires quilc and qvm to be installed separately
   - Output: CompiledProgram (optimized Quil)
   - IR: Quil program (text-based)
   - Consumption: QVM/QPU execution

### Language-based Compilers

6. **Silq** (`test_ghz_silq.py`, `ghz_silq.slq`)
   - Script: `python test_ghz_silq.py` (shows compilation info)
   - Program: `ghz_silq.slq`
   - Install: Follow instructions at https://silq.ethz.ch/
   - Output: Compiled circuit (C++ or QASM)
   - IR: AST (Abstract Syntax Tree)
   - Consumption: Simulator or exported to other formats

7. **ScaffCC** (`test_ghz_scaffcc.py`, `ghz_scaffold.scaffold`)
   - Script: `python test_ghz_scaffcc.py` (shows compilation info)
   - Program: `ghz_scaffold.scaffold`
   - Install: Follow instructions at https://github.com/epiqc/ScaffCC
   - Output: LLVM IR (.ll file) or binary
   - IR: LLVM IR
   - Consumption: Compiled to binary, executed with simulator library

8. **Q#** (`test_ghz_qsharp.py`, `GHZState.qs`)
   - Script: `python test_ghz_qsharp.py` (shows compilation info)
   - Program: `GHZState.qs`
   - Install: QDK from https://docs.microsoft.com/azure/quantum/install-overview-qdk
   - Output: QIR (Quantum IR) or .NET assembly
   - IR: QIR (LLVM-based)
   - Consumption: Q# runtime (simulator or hardware)

9. **Quilc** (`test_ghz_quilc.py`, `ghz.quil`)
   - Script: `python test_ghz_quilc.py` (shows compilation info)
   - Program: `ghz.quil`
   - Install: Follow instructions at https://github.com/rigetti/quilc
   - Output: Optimized Quil program (text)
   - IR: Quil (text-based quantum language)
   - Consumption: QVM or QPU execution

## Compilation Output Formats

Each compiler produces different output formats:

| Compiler | Output Format | Type |
|----------|--------------|------|
| Qiskit | QuantumCircuit object | Python object |
| PennyLane | QNode | Python object |
| ProjectQ | Command objects | Python objects (streaming) |
| tket | Circuit object | Python object |
| PyQuil | CompiledProgram (Quil) | Text-based Quil |
| Silq | Compiled circuit | C++/QASM |
| ScaffCC | LLVM IR | Text-based IR |
| Q# | QIR or .NET assembly | LLVM IR or binary |
| Quilc | Optimized Quil | Text-based Quil |

## Running All Python Tests

You can run all Python-based compilation analyses at once:

```bash
# Activate virtual environment first
source venv/bin/activate

# Run all tests
python run_all_ghz_tests.py
```

Or run individual tests:

```bash
python test_ghz_qiskit.py
python test_ghz_pennylane.py
# etc.
```

## Comparing Compilation Approaches

Each compiler:
- Uses different syntax for the same operations
- Produces different output formats
- Applies different optimizations
- Uses different intermediate representations
- Has different consumption methods

This allows you to compare:
- **Compilation strategies**: How compilers process code
- **Output formats**: What gets generated
- **IR designs**: Internal representations used
- **Optimization approaches**: What optimizations are applied
- **Backend interfaces**: How compiled code is consumed

## Notes

- The Bell State tests are preserved in the parent directory
- Each test is independent and can be run separately
- Some compilers require additional dependencies
- Check individual test files for specific installation requirements
- Focus is on compilation process, not execution results
