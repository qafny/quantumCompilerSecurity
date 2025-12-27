# Quantum Compilers Testing Guide

This guide walks through installing and testing each quantum compiler in our benchmark suite.

## Overview

We'll test each compiler by:
1. Installing it
2. Creating a simple Bell state circuit (quantum entanglement example)
3. Running the circuit
4. Understanding what each compiler does

**What is a Bell state?**
- A Bell state is an entangled quantum state of two qubits
- It demonstrates quantum entanglement: measuring one qubit instantly determines the other
- Circuit: Apply H (Hadamard) gate to qubit 0, then CNOT(0,1)

## Testing Strategy

### Phase 1: Easy to Install (Python-based)
1. **Qiskit** - Industry standard, well-documented
2. **Cirq** - Google's framework
3. **PennyLane** - Quantum ML framework

### Phase 2: Research Compilers (More Complex)
4. **Silq** - Requires special setup
5. **VOQC** - Requires Coq proof assistant
6. **ScaffCC** - Requires LLVM
7. **Quipper** - Requires Haskell

## Setup Instructions

We'll create test scripts in the `test_scripts/` directory for each compiler.

