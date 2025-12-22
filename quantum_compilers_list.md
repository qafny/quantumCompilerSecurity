# Quantum Compilers List

This document lists major quantum compilers and their key characteristics.

## Primary Compilers

### 1. Qiskit
- **Type**: Quantum software development framework
- **Language**: Python
- **Developer**: IBM
- **Features**: 
  - High-level quantum circuit construction
  - Optimization and transpilation
  - Multiple backends (simulators and real hardware)
  - Extensive library of quantum algorithms
- **Status**: Actively maintained, widely used

### 2. Cirq
- **Type**: Quantum computing framework
- **Language**: Python
- **Developer**: Google
- **Features**:
  - Designed for NISQ (Noisy Intermediate-Scale Quantum) devices
  - Circuit optimization
  - Noise model simulation
  - Integration with Google's quantum hardware
- **Status**: Actively maintained

### 3. Silq
- **Type**: High-level quantum programming language
- **Language**: Silq (domain-specific language)
- **Developer**: ETH Zurich
- **Features**:
  - Automatic uncomputation
  - Strong static type system
  - Designed to prevent common quantum programming errors
- **Status**: Research project

### 4. VOQC (Verified Optimizer for Quantum Circuits)
- **Type**: Verified quantum circuit optimizer
- **Language**: Coq (verified implementation)
- **Developer**: University of Maryland, University of Chicago
- **Features**:
  - Formally verified optimizations
  - Mathematical proofs of correctness
  - Optimization passes with verified properties
- **Status**: Research/academic project

### 5. ScaffCC
- **Type**: Quantum compiler and simulator
- **Language**: Scaffold (quantum programming language)
- **Developer**: University of California, Berkeley
- **Features**:
  - Compiles Scaffold to quantum assembly
  - Resource estimation
  - Quantum circuit optimization
- **Status**: Research project

### 6. PennyLane
- **Type**: Quantum machine learning framework with compiler
- **Language**: Python
- **Developer**: Xanadu
- **Features**:
  - Automatic differentiation for quantum circuits
  - Multi-device support (simulators and hardware)
  - Quantum machine learning focus
  - Circuit optimization
- **Status**: Actively maintained

### 7. Quipper
- **Type**: Functional quantum programming language
- **Language**: Haskell (embedded DSL)
- **Developer**: Dalhousie University, NIST
- **Features**:
  - Functional programming paradigm
  - Hierarchical circuit descriptions
  - Automatic circuit generation
  - Strong type system
- **Status**: Research/academic project

## Additional Notable Compilers (Optional)

### 8. ProjectQ
- **Type**: Quantum computing framework
- **Language**: Python
- **Developer**: ETH Zurich
- **Features**: High-level quantum programming, optimization, multiple backends

### 9. Q# (Q Sharp)
- **Type**: Quantum programming language
- **Language**: Q# (domain-specific language)
- **Developer**: Microsoft
- **Features**: Integrated with Visual Studio, quantum simulators, Azure Quantum

### 10. PyQuil
- **Type**: Quantum instruction language and compiler
- **Language**: Python
- **Developer**: Rigetti Computing
- **Features**: Quil language, optimization, Rigetti hardware integration

### 11. tket
- **Type**: Quantum circuit compiler
- **Language**: Python/C++
- **Developer**: Cambridge Quantum Computing (now Quantinuum)
- **Features**: Advanced optimization, multiple backend support

### 12. OpenQASM
- **Type**: Quantum assembly language (not a compiler itself, but used by compilers)
- **Language**: OpenQASM
- **Developer**: IBM
- **Features**: Standard intermediate representation for quantum circuits

## Summary

**Core List (Recommended for Research):**
1. Qiskit
2. Cirq
3. Silq
4. VOQC
5. ScaffCC
6. PennyLane
7. Quipper

**Total: 7 compilers**

This list covers:
- Industry-standard compilers (Qiskit, Cirq, PennyLane)
- Research/academic compilers (Silq, VOQC, ScaffCC, Quipper)
- Different paradigms (imperative, functional, verified)
- Different focus areas (general purpose, ML, verified correctness)

## Notes

- **Qiskit and Cirq** are the most widely used in industry and research
- **VOQC** is unique for its verified/formal methods approach
- **Silq** focuses on high-level abstractions and safety
- **ScaffCC and Quipper** represent different programming paradigms
- **PennyLane** bridges quantum computing and machine learning

