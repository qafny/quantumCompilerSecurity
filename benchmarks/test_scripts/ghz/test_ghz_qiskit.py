"""
GHZ State Compilation Analysis for Qiskit Compiler
===================================================

This script analyzes how Qiskit compiles a GHZ (Greenberger–Horne–Zeilinger) state program:
1. Create a quantum circuit (3-qubit GHZ state)
2. Analyze the original circuit structure
3. Compile/transpile it and examine the compilation process
4. Compare original vs compiled circuit characteristics
5. Analyze the compiled output structure and optimization

FOCUS: Compilation process and circuit structure, not execution results
"""

print("=" * 70)
print("QISKIT GHZ STATE COMPILATION ANALYSIS")
print("=" * 70)

try:
    # Step 1: Import Qiskit
    print("\n[Step 1] Importing Qiskit...")
    from qiskit import QuantumCircuit, transpile
    from qiskit.transpiler import PassManager
    try:
        from qiskit_aer import AerSimulator
    except ImportError:
        from qiskit.providers.aer import AerSimulator
    print("✓ Qiskit imported successfully")

    # Step 2: Create original GHZ state circuit
    print("\n[Step 2] Creating Original GHZ State Circuit...")
    print("   - 3 qubits, 3 classical bits for measurement")
    qc_original = QuantumCircuit(3, 3)
    
    # Apply gates to create GHZ state
    qc_original.h(0)        # Hadamard gate on qubit 0
    qc_original.cx(0, 1)    # CNOT: control=0, target=1
    qc_original.cx(0, 2)    # CNOT: control=0, target=2
    qc_original.measure_all()  # Measure all qubits
    
    print("\n✓ Original Circuit:")
    print(qc_original.draw(output='text'))
    
    print("\n[Original Circuit Analysis]")
    print(f"   Number of gates: {len(qc_original.data)}")
    print(f"   Circuit depth: {qc_original.depth()}")
    print(f"   Number of qubits: {qc_original.num_qubits}")
    print(f"   Number of classical bits: {qc_original.num_clbits}")
    print("   Gate sequence:")
    for i, instruction in enumerate(qc_original.data):
        gate_name = instruction.operation.name
        qubits = [qc_original.find_bit(q).index for q in instruction.qubits]
        print(f"     {i+1}. {gate_name.upper()}({', '.join(map(str, qubits))})")

    # Step 3: Compile/transpile the circuit
    print("\n" + "=" * 70)
    print("[Step 3] Compilation Process (Transpilation)")
    print("=" * 70)
    print("   Qiskit uses 'transpile' to compile circuits for target backends")
    print("   - Converts gates to backend-supported gate set")
    print("   - Applies optimization passes")
    print("   - Maps qubits to hardware topology if needed")
    
    simulator = AerSimulator()
    
    # Compile with different optimization levels
    print("\n[3.1] Compiling with optimization_level=0 (no optimization)...")
    compiled_level0 = transpile(qc_original, simulator, optimization_level=0)
    
    print("[3.2] Compiling with optimization_level=1 (light optimization)...")
    compiled_level1 = transpile(qc_original, simulator, optimization_level=1)
    
    print("[3.3] Compiling with optimization_level=2 (medium optimization)...")
    compiled_level2 = transpile(qc_original, simulator, optimization_level=2)
    
    print("[3.4] Compiling with optimization_level=3 (heavy optimization)...")
    compiled_level3 = transpile(qc_original, simulator, optimization_level=3)
    
    print("\n✓ Compilation completed for all optimization levels")

    # Step 4: Analyze compiled circuits
    print("\n" + "=" * 70)
    print("[Step 4] Compiled Circuit Analysis")
    print("=" * 70)
    
    compiled_circuits = {
        "Original": qc_original,
        "Level 0 (No opt)": compiled_level0,
        "Level 1 (Light)": compiled_level1,
        "Level 2 (Medium)": compiled_level2,
        "Level 3 (Heavy)": compiled_level3
    }
    
    print("\n[Circuit Statistics Comparison]")
    print(f"{'Version':<20} {'Gates':<10} {'Depth':<10} {'Size':<10}")
    print("-" * 50)
    for name, circ in compiled_circuits.items():
        num_gates = len([inst for inst in circ.data if inst.operation.name != 'barrier'])
        depth = circ.depth()
        size = circ.size()
        print(f"{name:<20} {num_gates:<10} {depth:<10} {size:<10}")
    
    # Step 5: Display compiled circuits
    print("\n[Step 5] Compiled Circuit Structures")
    print("=" * 70)
    
    for opt_level, compiled in [("Level 1", compiled_level1)]:
        print(f"\n[{opt_level} Compiled Circuit]:")
        print(compiled.draw(output='text'))
        
        print(f"\n[{opt_level} Gate Sequence]:")
        for i, instruction in enumerate(compiled.data):
            gate_name = instruction.operation.name
            if gate_name == 'barrier':
                continue
            qubits = [compiled.find_bit(q).index for q in instruction.qubits]
            params = instruction.operation.params
            param_str = f", params={params}" if params else ""
            print(f"     {i+1}. {gate_name.upper()}({', '.join(map(str, qubits))}{param_str})")
    
    # Step 6: Analyze gate decomposition
    print("\n" + "=" * 70)
    print("[Step 6] Gate Set Analysis")
    print("=" * 70)
    
    print("\n[Original Circuit Gate Types]:")
    original_gates = {}
    for inst in qc_original.data:
        gate_name = inst.operation.name
        original_gates[gate_name] = original_gates.get(gate_name, 0) + 1
    for gate, count in sorted(original_gates.items()):
        print(f"   {gate.upper()}: {count}")
    
    print("\n[Compiled Circuit (Level 1) Gate Types]:")
    compiled_gates = {}
    for inst in compiled_level1.data:
        gate_name = inst.operation.name
        if gate_name != 'barrier':
            compiled_gates[gate_name] = compiled_gates.get(gate_name, 0) + 1
    if compiled_gates:
        for gate, count in sorted(compiled_gates.items()):
            print(f"   {gate.upper()}: {count}")
    else:
        print("   (No gates found - circuit may be empty)")
    
    # Step 7: Qiskit IR (QuantumCircuit object) analysis
    print("\n" + "=" * 70)
    print("[Step 7] Intermediate Representation (IR) Analysis")
    print("=" * 70)
    print("   Qiskit uses QuantumCircuit objects as its IR")
    print(f"   - Type: {type(compiled_level1)}")
    print(f"   - Data structure: List of Instruction objects")
    print(f"   - Instructions stored in: circuit.data")
    print(f"   - Total instructions: {len(compiled_level1.data)}")
    
    # Step 8: How the circuit is consumed/executed
    print("\n" + "=" * 70)
    print("[Step 8] Circuit Consumption and Execution")
    print("=" * 70)
    print("   The compiled QuantumCircuit can be:")
    print("   1. Executed directly on simulators (AerSimulator)")
    print("   2. Submitted to hardware backends via IBM Quantum")
    print("   3. Further optimized or modified")
    print("   4. Converted to other formats (QASM, Qobj)")
    
    print("\n   Execution pipeline:")
    print("   QuantumCircuit -> Transpiler -> Qobj -> Backend -> Results")
    
    print("\n" + "=" * 70)
    print("COMPILATION ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nKEY FINDINGS:")
    print("- Qiskit's compilation process uses transpilation")
    print("- Optimization levels can affect circuit structure")
    print("- IR: QuantumCircuit object (Python class)")
    print("- Compiled circuits maintain gate structure but may be optimized")
    print("- Circuit is consumed via backend.run() method")

except ImportError:
    print("\n❌ ERROR: Qiskit not installed")
    print("   Install with: pip install qiskit")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
