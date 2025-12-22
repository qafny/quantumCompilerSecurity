# Silq

## Overview
Silq is a high-level quantum programming language that automatically handles uncomputation, making quantum programming safer and more intuitive.

## Type
High-level quantum programming language

## Language
Silq (domain-specific language)

## Developer
ETH Zurich

## Installation

```bash
# Silq compiler and tools
# See: https://silq.ethz.ch/installation
```

## Key Features
- Automatic uncomputation
- Strong static type system
- Designed to prevent common quantum programming errors
- High-level abstractions
- Safe quantum memory management
- Type inference

## Example Usage

```silq
// Silq example: Quantum Fourier Transform
def qft(n:!ℕ, qs:!ℕ^n) {
  for i in [0..n) {
    H(qs[i]);
    for j in [i+1..n) {
      CPhase(2π/2^(j-i+1), qs[j], qs[i]);
    }
  }
}
```

## Official Links
- **Website**: https://silq.ethz.ch/
- **GitHub**: https://github.com/eth-sri/silq
- **Documentation**: https://silq.ethz.ch/documentation

## Status
Research project (ETH Zurich)

## Research Papers
- Silq: A High-Level Quantum Language with Safe Uncomputation and Intuitive Semantics (PLDI 2020)
- Quantum Programming Languages (Survey)

