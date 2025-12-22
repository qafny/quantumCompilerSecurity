# Quipper

## Overview
Quipper is a functional quantum programming language embedded in Haskell, designed for describing and generating quantum circuits.

## Type
Functional quantum programming language

## Language
Haskell (embedded DSL)

## Developer
Dalhousie University, NIST

## Installation

```bash
# Requires Haskell and Cabal
# See: https://www.mathstat.dal.ca/~selinger/quipper/
cabal install quipper
```

## Key Features
- Functional programming paradigm
- Hierarchical circuit descriptions
- Automatic circuit generation
- Strong type system
- Support for classical control
- Parameterized circuits
- Circuit visualization

## Example Usage

```haskell
-- Quipper example: Bell state
bell_state :: (Qubit, Qubit) -> Circ (Qubit, Qubit)
bell_state (q1, q2) = do
  hadamard q1
  qnot q1 q2
  return (q1, q2)
```

## Official Links
- **Website**: https://www.mathstat.dal.ca/~selinger/quipper/
- **GitHub**: https://github.com/thephoeron/quipper
- **Documentation**: https://www.mathstat.dal.ca/~selinger/quipper/doc/

## Status
Research/academic project

## Research Papers
- Quipper: A Scalable Quantum Programming Language (PLDI 2013)
- An Introduction to Quantum Programming in Quipper (2013)

