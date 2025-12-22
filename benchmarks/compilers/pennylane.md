# PennyLane

## Overview
PennyLane is a cross-platform Python library for differentiable programming of quantum computers, with built-in optimization and compilation capabilities.

## Type
Quantum machine learning framework with compiler

## Language
Python

## Developer
Xanadu

## Installation

```bash
pip install pennylane
# For specific device support
pip install pennylane[qiskit]  # Qiskit plugin
pip install pennylane[cirq]    # Cirq plugin
```

## Key Features
- Automatic differentiation for quantum circuits
- Multi-device support (simulators and hardware)
- Quantum machine learning focus
- Circuit optimization
- Gradient-based optimization
- Plugin architecture for different backends

## Example Usage

```python
import pennylane as qml

# Define a quantum device
dev = qml.device('default.qubit', wires=2)

# Define a quantum circuit
@qml.qnode(dev)
def circuit(params):
    qml.RY(params[0], wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

# Optimize
import numpy as np
params = np.array([0.1])
result = circuit(params)
```

## Official Links
- **Website**: https://pennylane.ai/
- **GitHub**: https://github.com/PennyLaneAI/pennylane
- **Documentation**: https://pennylane.readthedocs.io/

## Status
Actively maintained by Xanadu

## Research Papers
- PennyLane: Automatic differentiation of hybrid quantum-classical computations (2022)
- Quantum machine learning with PennyLane (2020)

