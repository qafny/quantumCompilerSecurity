# Installation Guide for Quantum Compilers

This guide explains how to install each compiler in the benchmark suite.

## Prerequisites

### Python Environment
```bash
# Activate your virtual environment
cd C:\Users\BardCS-01\Documents\xml-fixing
.\venv\Scripts\Activate.ps1
```

## Easy Installations (Python-based)

### 1. Qiskit
```bash
pip install qiskit
pip install qiskit[visualization]  # Optional: for circuit visualization
```

**Test installation:**
```bash
python -c "import qiskit; print('Qiskit version:', qiskit.__version__)"
```

### 2. Cirq
```bash
pip install cirq
```

**Test installation:**
```bash
python -c "import cirq; print('Cirq version:', cirq.__version__)"
```

### 3. PennyLane
```bash
pip install pennylane
```

**Test installation:**
```bash
python -c "import pennylane as qml; print('PennyLane version:', qml.__version__)"
```

## Advanced Installations

### 4. Silq
Silq requires special setup. See: https://silq.ethz.ch/installation

### 5. VOQC
VOQC requires Coq proof assistant. See: https://github.com/inQWIRE/SQIR/tree/main/voqc

### 6. ScaffCC
ScaffCC requires LLVM. See: https://github.com/epiqc/ScaffCC

### 7. Quipper
Quipper requires Haskell. See: https://www.mathstat.dal.ca/~selinger/quipper/

## Quick Install All (Python compilers)

```bash
pip install qiskit cirq pennylane
```

## Verification

After installation, run the test scripts:
```bash
cd quantumTesting/benchmarks/test_scripts
python test_qiskit.py
python test_cirq.py
python test_pennylane.py
```

Or run all tests:
```bash
python run_all_tests.py
```

