# VOQC (Verified Optimizer for Quantum Circuits)

## Overview
VOQC is a verified optimizer for quantum circuits implemented in Coq, with mathematical proofs of correctness for all optimizations.

## Type
Verified quantum circuit optimizer

## Language
Coq (verified implementation), OCaml (extracted code)

## Developer
University of Maryland, University of Chicago

## Installation

```bash
# Requires Coq proof assistant
# See: https://github.com/inQWIRE/SQIR/tree/main/voqc
opam install coq
git clone https://github.com/inQWIRE/SQIR.git
cd SQIR/voqc
make
```

## Key Features
- Formally verified optimizations
- Mathematical proofs of correctness
- Optimization passes with verified properties
- Extracted to OCaml for execution
- Guaranteed correctness of transformations
- Research tool for verified quantum compilation

## Example Usage

```ocaml
(* VOQC optimizations are verified in Coq *)
(* The extracted OCaml code can be used for optimization *)
```

## Official Links
- **GitHub**: https://github.com/inQWIRE/SQIR/tree/main/voqc
- **Research**: https://www.cs.umd.edu/projects/PL/voqc/

## Status
Research/academic project

## Research Papers
- Verified Compilation of Quantum Algorithms (PLDI 2019)
- A Verified Optimizer for Quantum Circuits (POPL 2021)



