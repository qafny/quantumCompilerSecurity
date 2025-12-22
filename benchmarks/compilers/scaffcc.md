# ScaffCC

## Overview
ScaffCC is a quantum compiler and simulator for the Scaffold quantum programming language, developed at UC Berkeley.

## Type
Quantum compiler and simulator

## Language
Scaffold (quantum programming language), C++ (compiler)

## Developer
University of California, Berkeley

## Installation

```bash
# Requires LLVM
# See: https://github.com/epiqc/ScaffCC
git clone https://github.com/epiqc/ScaffCC.git
cd ScaffCC
make
```

## Key Features
- Compiles Scaffold to quantum assembly (QASM)
- Resource estimation
- Quantum circuit optimization
- Hierarchical circuit descriptions
- Support for classical control flow
- Integration with quantum simulators

## Example Usage

```scaffold
// Scaffold example
module main() {
    qbit q[2];
    H(q[0]);
    CNOT(q[0], q[1]);
    M(q);
}
```

## Official Links
- **GitHub**: https://github.com/epiqc/ScaffCC
- **Documentation**: https://github.com/epiqc/ScaffCC/wiki

## Status
Research project (UC Berkeley)

## Research Papers
- ScaffCC: A Framework for Compilation and Analysis of Quantum Computing Programs (ASPLOS 2014)
- A Practical Quantum Instruction Set Architecture (2017)

