"""
GHZ State Compilation Analysis for tket Compiler
=================================================

This script analyzes how tket (TKET/Quantinuum) compiles a GHZ (Greenberger–Horne–Zeilinger) state program:
1. Create a quantum circuit (3-qubit GHZ state)
2. Analyze the compilation process
3. Examine the compiled circuit structure
4. Analyze the intermediate representation

FOCUS: Compilation process and circuit structure, not execution results
"""

print("=" * 70)
print("TKET GHZ STATE COMPILATION ANALYSIS")
print("=" * 70)

try:
    # Step 1: Import pytket and backend
    print("\n[Step 1] Importing pytket...")
    from pytket import Circuit
    from pytket.backends import Backend
    from pytket.extensions.qiskit import AerBackend
    from pytket.passes import SequencePass, DecomposeBoxes, OptimisePhaseGadgets
    print("✓ pytket imported successfully")

    # Step 2: Create original circuit
    print("\n" + "=" * 70)
    print("[Step 2] Original Circuit Definition")
    print("=" * 70)
    
    circuit = Circuit(3)  # 3 qubits
    
    # Apply gates to create GHZ state
    circuit.H(0)          # Hadamard gate on qubit 0
    circuit.CX(0, 1)      # CNOT: control=0, target=1
    circuit.CX(0, 2)      # CNOT: control=0, target=2
    circuit.measure_all()
    
    print("\n✓ Original Circuit:")
    print(circuit)
    
    print("\n[Original Circuit Analysis]")
    print(f"   Number of gates: {len(circuit.get_commands())}")
    print(f"   Circuit depth: {circuit.depth()}")
    print(f"   Number of qubits: {circuit.n_qubits}")
    
    print("\n[Gate Sequence]:")
    for i, cmd in enumerate(circuit.get_commands()):
        op = cmd.op
        qubits = cmd.args
        print(f"     {i+1}. {op.type.name}({', '.join(map(str, [q.index[0] for q in qubits]))})")

    # Step 3: Compilation process
    print("\n" + "=" * 70)
    print("[Step 3] Compilation Process")
    print("=" * 70)
    print("   tket compiles circuits using get_compiled_circuit()")
    print("   - Applies optimization passes")
    print("   - Decomposes gates to backend-native gateset")
    print("   - Optimizes circuit structure")
    
    backend = AerBackend()
    
    print("\n[Backend Information]:")
    print(f"   Backend type: {type(backend)}")
    print(f"   Target backend: {backend.backend_info.name if hasattr(backend, 'backend_info') else 'AerSimulator'}")
    
    # Compile the circuit for the backend
    print("\n[Compiling circuit...]")
    compiled_circuit = backend.get_compiled_circuit(circuit)
    print("✓ Circuit compiled")
    
    print(f"\n[Compilation Statistics]:")
    print(f"   Original gates: {len(circuit.get_commands())}")
    print(f"   Compiled gates: {len(compiled_circuit.get_commands())}")
    print(f"   Original depth: {circuit.depth()}")
    print(f"   Compiled depth: {compiled_circuit.depth()}")

    # Step 4: Analyze compiled circuit structure
    print("\n" + "=" * 70)
    print("[Step 4] Compiled Circuit Structure")
    print("=" * 70)
    
    print("\n[Compiled Circuit]:")
    print(compiled_circuit)
    
    print("\n[Compiled Gate Sequence]:")
    for i, cmd in enumerate(compiled_circuit.get_commands()):
        op = cmd.op
        qubits = cmd.args
        params = op.params if hasattr(op, 'params') else []
        param_str = f", params={params}" if params else ""
        print(f"     {i+1}. {op.type.name}({', '.join(map(str, [q.index[0] for q in qubits]))}{param_str})")

    # Step 5: Gate set analysis
    print("\n" + "=" * 70)
    print("[Step 5] Gate Set Analysis")
    print("=" * 70)
    
    print("\n[Original Circuit Gate Types]:")
    original_gates = {}
    for cmd in circuit.get_commands():
        gate_name = cmd.op.type.name
        original_gates[gate_name] = original_gates.get(gate_name, 0) + 1
    for gate, count in sorted(original_gates.items()):
        print(f"   {gate}: {count}")
    
    print("\n[Compiled Circuit Gate Types]:")
    compiled_gates = {}
    for cmd in compiled_circuit.get_commands():
        gate_name = cmd.op.type.name
        compiled_gates[gate_name] = compiled_gates.get(gate_name, 0) + 1
    for gate, count in sorted(compiled_gates.items()):
        print(f"   {gate}: {count}")

    # Step 6: Intermediate Representation
    print("\n" + "=" * 70)
    print("[Step 6] Intermediate Representation (IR) Analysis")
    print("=" * 70)
    print("   tket uses Circuit objects as IR")
    print(f"   - Type: {type(compiled_circuit)}")
    print(f"   - Data structure: Circuit object with command list")
    print(f"   - Commands stored as: circuit.get_commands()")
    print(f"   - Total commands: {len(compiled_circuit.get_commands())}")
    
    print("\n[Circuit Object Structure]:")
    print("   - Commands: List of Command objects")
    print("   - Each Command: Op (operation) + Args (qubits)")
    print("   - Operations have types, parameters")
    print("   - Qubits referenced by index")

    # Step 7: How circuit is consumed
    print("\n" + "=" * 70)
    print("[Step 7] Circuit Consumption and Execution")
    print("=" * 70)
    print("   The compiled Circuit can be:")
    print("   1. Executed via backend.process_circuit()")
    print("   2. Converted to other formats (QASM, Quil, etc.)")
    print("   3. Further optimized with additional passes")
    print("   4. Sent to different backends")
    
    print("\n   Execution pipeline:")
    print("   Circuit -> get_compiled_circuit() -> Compiled Circuit -> Backend.process_circuit() -> Results")
    
    print("\n   Key characteristics:")
    print("   - Compilation produces optimized Circuit object")
    print("   - Circuit can be serialized to different formats")
    print("   - Supports multiple backends (Qiskit, Cirq, etc.)")
    print("   - Compilation is explicit (must call get_compiled_circuit())")

    # Step 8: Compilation output format
    print("\n" + "=" * 70)
    print("[Step 8] Compilation Output Format")
    print("=" * 70)
    print("   The compiled output is:")
    print("   - A Circuit object (same type as input)")
    print("   - Contains optimized gate sequence")
    print("   - Ready for backend execution")
    print("   - Can be converted to text formats (QASM, Quil)")
    
    print("\n[Output Characteristics]:")
    print("   - Format: Circuit object (Python class)")
    print("   - Structure: Optimized command sequence")
    print("   - Format: Not binary, but structured Python object")
    print("   - Can be serialized to text/binary formats")
    
    print("\n" + "=" * 70)
    print("COMPILATION ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nKEY FINDINGS:")
    print("- tket uses Circuit objects as IR (same type input/output)")
    print("- Compilation via get_compiled_circuit() method")
    print("- Applies optimization passes during compilation")
    print("- Output: Optimized Circuit object")
    print("- Circuit can be converted to various formats")
    print("- Supports multiple backend targets")

except ImportError:
    print("\n❌ ERROR: pytket not installed")
    print("   Install with: pip install pytket")
    print("   Also install backend extensions: pip install pytket-qiskit")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
