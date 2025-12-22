# Quantum Compilers Benchmark Suite

This directory contains information, resources, and benchmark results for various quantum compilers.

## Structure

```
benchmarks/
├── README.md (this file)
├── compilers/          # Individual compiler documentation
│   ├── README.md
│   ├── qiskit.md
│   ├── cirq.md
│   ├── silq.md
│   ├── voqc.md
│   ├── scaffcc.md
│   ├── pennylane.md
│   └── quipper.md
└── [future: test_cases/]    # Benchmark test cases
└── [future: results/]        # Benchmark results
```

## Purpose

This benchmark suite is designed to:
- Document major quantum compilers
- Provide installation and usage examples
- Enable comparison of compiler features
- Support future benchmarking efforts

## Compilers Included

1. **Qiskit** - IBM's quantum framework
2. **Cirq** - Google's quantum framework  
3. **Silq** - High-level quantum language
4. **VOQC** - Verified quantum optimizer
5. **ScaffCC** - Scaffold compiler
6. **PennyLane** - Quantum ML framework
7. **Quipper** - Functional quantum language

## Usage

See individual compiler documentation in the `compilers/` directory for:
- Installation instructions
- Example code
- Key features
- Official documentation links

## Future Work

- Add benchmark test cases
- Include performance comparisons
- Add optimization pass comparisons
- Document compilation workflows

