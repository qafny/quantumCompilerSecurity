"""
GHZ State Compilation Analysis for PyQuil/Quilc Compiler
=========================================================

This script analyzes how PyQuil and quilc compile a GHZ (Greenberger–Horne–Zeilinger) state program:
1. Create a Quil program (3-qubit GHZ state)
2. Analyze the compilation process with quilc
3. Examine the compiled program structure
4. Analyze Quil IR and optimizations

FOCUS: Compilation process and program structure, not execution results
"""

print("=" * 70)
print("PYQUIL/QUILC GHZ STATE COMPILATION ANALYSIS")
print("=" * 70)

try:
    # Step 1: Import PyQuil
    print("\n[Step 1] Importing PyQuil...")
    from pyquil import Program
    from pyquil.gates import H, CNOT, MEASURE
    from pyquil import get_qc
    import numpy as np
    print("✓ PyQuil imported successfully")

    # Step 2: Create original Quil program
    print("\n" + "=" * 70)
    print("[Step 2] Original Quil Program Definition")
    print("=" * 70)
    print("   PyQuil uses Quil (Quantum Instruction Language) as its IR")
    print("   - Programs are sequences of Quil instructions")
    print("   - Gates and measurements are Quil instructions")
    
    prog = Program()
    
    # Apply gates to create GHZ state
    prog += H(0)          # Hadamard gate on qubit 0
    prog += CNOT(0, 1)    # CNOT: control=0, target=1
    prog += CNOT(0, 2)    # CNOT: control=0, target=2
    
    # Declare classical memory and measure
    ro = prog.declare('ro', memory_type='BIT', memory_size=3)
    prog += MEASURE(0, ro[0])
    prog += MEASURE(1, ro[1])
    prog += MEASURE(2, ro[2])
    
    print("\n[Original Quil Program]:")
    print(prog)
    
    print("\n[Original Program Analysis]")
    print(f"   Number of instructions: {len(prog.instructions)}")
    print(f"   Program length: {len(str(prog).split(chr(10)))}")
    
    print("\n[Instruction Sequence]:")
    for i, inst in enumerate(prog.instructions):
        print(f"     {i+1}. {inst}")

    # Step 3: Get quantum computer and compile
    print("\n" + "=" * 70)
    print("[Step 3] Compilation Process (quilc)")
    print("=" * 70)
    print("   quilc is the Quil compiler that:")
    print("   - Compiles Quil programs to native Quil")
    print("   - Optimizes gate sequences")
    print("   - Decomposes gates to hardware-native gates")
    print("   - Applies compiler optimizations")
    
    try:
        qc = get_qc('3q-qvm')  # 3-qubit Quantum Virtual Machine
        print(f"\n[3.1] Quantum Computer: {type(qc).__name__}")
        print(f"   Qubit count: {qc.quantum_processor.to_compiler_isa().n_qubits}")
        
        # Compile the program
        print("\n[3.2] Compiling program with quilc...")
        compiled_prog = qc.compile(prog)
        print("✓ Program compiled")
        
        print(f"\n[3.3] Compilation Result:")
        print(f"   Original instructions: {len(prog.instructions)}")
        print(f"   Compiled instructions: {len(compiled_prog.program.instructions)}")
        
    except Exception as e:
        if "QVM" in str(e) or "127.0.0.1:5000" in str(e):
            print("\n⚠ QVM server not running - showing compilation structure only")
            print("   (quilc compilation requires QVM server)")
            compiled_prog = None
        else:
            raise

    # Step 4: Analyze compiled program (if available)
    if compiled_prog:
        print("\n" + "=" * 70)
        print("[Step 4] Compiled Program Analysis")
        print("=" * 70)
        
        print("\n[Compiled Quil Program]:")
        print(compiled_prog.program)
        
        print("\n[Compiled Instruction Sequence]:")
        for i, inst in enumerate(compiled_prog.program.instructions):
            print(f"     {i+1}. {inst}")

    # Step 5: Quil IR analysis
    print("\n" + "=" * 70)
    print("[Step 5] Intermediate Representation (Quil IR)")
    print("=" * 70)
    
    print("\n[Quil IR Structure]:")
    print("   - Program: Container for Quil instructions")
    print("   - Instructions: List of instruction objects")
    print("   - Instruction types:")
    print("     * Gate instructions: H, CNOT, RZ, etc.")
    print("     * Measurement instructions: MEASURE")
    print("     * Classical operations: Classical instructions")
    print("     * Declarations: DECLARE")
    
    print("\n[Program Object Structure]:")
    print(f"   Type: {type(prog)}")
    print(f"   Instructions: {len(prog.instructions)}")
    print(f"   Memory declarations: {len(prog.declarations)}")
    
    print("\n[Original Program Quil Code]:")
    quil_code = str(prog)
    print(quil_code)

    # Step 6: Gate analysis
    print("\n" + "=" * 70)
    print("[Step 6] Gate Type Analysis")
    print("=" * 70)
    
    print("\n[Original Program Gates]:")
    gate_count = {}
    for inst in prog.instructions:
        if hasattr(inst, 'name'):
            gate_name = inst.name
            gate_count[gate_name] = gate_count.get(gate_name, 0) + 1
    for gate, count in sorted(gate_count.items()):
        print(f"   {gate}: {count}")
    
    if compiled_prog:
        print("\n[Compiled Program Gates]:")
        compiled_gate_count = {}
        for inst in compiled_prog.program.instructions:
            if hasattr(inst, 'name'):
                gate_name = inst.name
                compiled_gate_count[gate_name] = compiled_gate_count.get(gate_name, 0) + 1
        for gate, count in sorted(compiled_gate_count.items()):
            print(f"   {gate}: {count}")

    # Step 7: quilc compilation process
    print("\n" + "=" * 70)
    print("[Step 7] quilc Compilation Process")
    print("=" * 70)
    
    print("\n[quilc Compiler Characteristics]:")
    print("   - Input: Quil program")
    print("   - Output: Optimized/native Quil program")
    print("   - Process:")
    print("     1. Parse Quil program")
    print("     2. Apply optimization passes")
    print("     3. Decompose gates to native gate set")
    print("     4. Optimize gate sequences")
    print("     5. Output compiled Quil")
    
    print("\n[Optimization Features]:")
    print("   - Gate fusion")
    print("   - Gate cancellation")
    print("   - Gate decomposition")
    print("   - Qubit routing")
    print("   - Instruction scheduling")

    # Step 8: How the program is consumed
    print("\n" + "=" * 70)
    print("[Step 8] Program Consumption and Execution")
    print("=" * 70)
    
    print("\n[Execution Pipeline]:")
    print("   Quil Program -> quilc compilation -> Native Quil -> QVM/QPU -> Results")
    
    print("\n[Key Characteristics]:")
    print("   - Quil is the IR (text-based quantum instruction language)")
    print("   - quilc compiles Quil to optimized Quil")
    print("   - Can target different quantum processors")
    print("   - Compiled programs ready for execution")
    print("   - Supports classical control and feedback")

    # Step 9: Compilation output format
    print("\n" + "=" * 70)
    print("[Step 9] Compilation Output Format")
    print("=" * 70)
    
    print("\n[Output Structure]:")
    print("   - Type: CompiledProgram object")
    print("   - Contains: Compiled Quil Program")
    print("   - Format: Quil text instructions")
    print("   - Can be executed on QVM or QPU")
    
    if compiled_prog:
        print("\n[Compiled Program Format]:")
        print("   - Still Quil format (text-based)")
        print("   - Optimized instruction sequence")
        print("   - Native to target processor")
        print("   - Wrapped in CompiledProgram container")
    
    # Step 10: Comparison with original
    print("\n" + "=" * 70)
    print("[Step 10] Original vs Compiled Comparison")
    print("=" * 70)
    
    print("\n[Original Program]:")
    print("   - Gate sequence: H(0), CNOT(0,1), CNOT(0,2)")
    print("   - 3 gate instructions + 3 measurements")
    print("   - High-level Quil representation")
    
    if compiled_prog:
        print("\n[Compiled Program]:")
        print("   - Optimized Quil representation")
        print("   - May have different gate sequences")
        print("   - Native to target processor")
        print("   - Ready for execution")
    else:
        print("\n[Compiled Program]:")
        print("   - (Not available - QVM required for compilation)")

    print("\n" + "=" * 70)
    print("COMPILATION ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nKEY FINDINGS:")
    print("- PyQuil uses Quil (text-based quantum language) as IR")
    print("- quilc compiler optimizes and compiles Quil programs")
    print("- IR structure: Program object containing instruction sequences")
    print("- Compilation via qc.compile() method")
    print("- Output: Compiled Quil program (still Quil format)")
    print("- Supports hardware-specific optimizations")

except ImportError:
    print("\n❌ ERROR: PyQuil not installed")
    print("   Install with: pip install pyquil")
    print("   Note: Requires quilc and qvm to be installed separately")
except Exception as e:
    error_msg = str(e)
    if "QVM" in error_msg or "127.0.0.1:5000" in error_msg:
        print("\n⚠ NOTE: QVM server not running")
        print("   Analysis shows compilation structure without execution")
        print("   To see full compilation: Start QVM server (qvm -S)")
    else:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
