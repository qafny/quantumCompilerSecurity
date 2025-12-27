# Cirq

## Overview
Cirq is Google's Python framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.

## Type
Quantum computing framework

## Language
Python

## Developer
Google Quantum AI

## Installation

```bash
pip install cirq
```

## Key Features
- Designed for NISQ (Noisy Intermediate-Scale Quantum) devices
- Circuit optimization
- Noise model simulation
- Integration with Google's quantum hardware (Sycamore)
- Parameterized circuits
- Circuit scheduling and placement

## Example Usage

```python
import cirq

# Create qubits
q0, q1 = cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)

# Create a circuit
circuit = cirq.Circuit()
circuit.append(cirq.H(q0))
circuit.append(cirq.CNOT(q0, q1))
circuit.append(cirq.measure(q0, q1, key='result'))

# Simulate
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)
```

## Official Links
- **Website**: https://quantumai.google/cirq
- **GitHub**: https://github.com/quantumlib/Cirq
- **Documentation**: https://quantumai.google/cirq

## Status
Actively maintained by Google

## Research Papers
- Cirq: A Python framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits (2018)



