"""
GHZ State Compilation Analysis for PyQuil/Quilc Compiler
=========================================================

This script shows what PyQuil/quilc compiler outputs for a GHZ state program.
Output: Quil (hardware instruction format), not execution results.
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
    print("✓ PyQuil imported successfully")

    # Step 2: Create Quil program
    print("\n[Step 2] Creating Quil Program...")
    prog = Program()
    prog += H(0)
    prog += CNOT(0, 1)
    prog += CNOT(0, 2)
    ro = prog.declare('ro', memory_type='BIT', memory_size=3)
    prog += MEASURE(0, ro[0])
    prog += MEASURE(1, ro[1])
    prog += MEASURE(2, ro[2])
    print("✓ Program created")

    # Step 3: Show original program
    print("\n[Step 3] Original Quil Program:")
    print("-" * 70)
    print(prog)
    print("-" * 70)

    # Step 4: Compile the program
    print("\n[Step 4] Compiling program with quilc...")
    try:
        qc = get_qc('3q-qvm')
        compiled_prog = qc.compile(prog)
        print("✓ Program compiled")
        print(f"   Original instructions: {len(prog.instructions)}")
        print(f"   Compiled instructions: {len(compiled_prog.program.instructions)}")
    except Exception as e:
        if "QVM" in str(e) or "127.0.0.1:5000" in str(e):
            print("⚠ QVM server not running - showing original program")
            compiled_prog = None
        else:
            raise

    # Step 5: Show compiled program structure
    if compiled_prog:
        print("\n[Step 5] Compiled Program Structure:")
        print("-" * 70)
        print(compiled_prog.program)
        print("-" * 70)

    # Step 6: Show instruction sequence
    print("\n[Step 6] Instruction Sequence:")
    if compiled_prog:
        for i, inst in enumerate(compiled_prog.program.instructions):
            print(f"   {i+1}. {inst}")
    else:
        for i, inst in enumerate(prog.instructions):
            print(f"   {i+1}. {inst}")

    # Step 7: Output compiled program as Quil (hardware instructions)
    print("\n" + "=" * 70)
    print("[Step 7] COMPILED OUTPUT: Quil Format (Hardware Instructions)")
    print("=" * 70)
    print("   This is the compiled program output (hardware instructions)")
    print("   NOT execution results (state vector or measurement counts)")
    
    if compiled_prog:
        print("\n[Compiled Quil Program]:")
        print("-" * 70)
        print(str(compiled_prog.program))
        print("-" * 70)
    else:
        print("\n[Original Quil Program]:")
        print("-" * 70)
        print(str(prog))
        print("-" * 70)
        print("\n[Note] Compiled version requires QVM server")

    print("\n" + "=" * 70)
    print("COMPILATION COMPLETE")
    print("=" * 70)
    print("\nOutput: Quil (hardware instruction format)")
    print("This is the compiled program, not execution results.")

except ImportError:
    print("\n❌ ERROR: PyQuil not installed")
    print("   Install with: pip install pyquil")
except Exception as e:
    error_msg = str(e)
    if "QVM" in error_msg or "127.0.0.1:5000" in error_msg:
        print("\n⚠ NOTE: QVM server not running")
    else:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
