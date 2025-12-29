/**
 * GHZ State Program for Q# Compiler
 * ==================================
 * 
 * This program creates a GHZ (Greenberger–Horne–Zeilinger) state in Q#:
 * 1. Creates a 3-qubit GHZ state: (|000⟩ + |111⟩)/√2
 * 2. Measures all qubits
 * 
 * GHZ STATE EXPLANATION:
 * ----------------------
 * - H gate on qubit 0: Creates superposition (|0⟩ + |1⟩)/√2
 * - CNOT(0,1): Entangles qubit 0 with qubit 1
 * - CNOT(0,2): Entangles qubit 0 with qubit 2
 * - Result: GHZ state (|000⟩ + |111⟩)/√2
 * - When measured, we get either |000⟩ or |111⟩ with 50% probability each
 */

namespace GHZState {
    
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    
    /// <summary>
    /// Creates a 3-qubit GHZ state and returns measurement results.
    /// </summary>
    /// <returns>
    /// A tuple of three measurement results (Result, Result, Result).
    /// Should be either (Zero, Zero, Zero) or (One, One, One) with ~50% probability each.
    /// </returns>
    operation CreateGHZState() : (Result, Result, Result) {
        // Allocate 3 qubits, all initialized to |0⟩
        use qs = Qubit[3];
        
        // Apply Hadamard gate to qubit 0
        H(qs[0]);
        
        // Apply CNOT gates to create entanglement
        CNOT(qs[0], qs[1]);  // CNOT: control=qs[0], target=qs[1]
        CNOT(qs[0], qs[2]);  // CNOT: control=qs[0], target=qs[2]
        
        // Measure all qubits
        let r0 = M(qs[0]);
        let r1 = M(qs[1]);
        let r2 = M(qs[2]);
        
        // Reset qubits to |0⟩ before releasing
        ResetAll(qs);
        
        return (r0, r1, r2);
    }
    
    /// <summary>
    /// Entry point that runs the GHZ state circuit multiple times.
    /// </summary>
    @EntryPoint()
    operation RunGHZTest() : Unit {
        Message("Running GHZ State Test (1024 shots)...");
        
        mutable count000 = 0;
        mutable count111 = 0;
        mutable countOther = 0;
        
        for i in 0..1023 {
            let (r0, r1, r2) = CreateGHZState();
            
            if (r0 == Zero and r1 == Zero and r2 == Zero) {
                set count000 += 1;
            } elif (r0 == One and r1 == One and r2 == One) {
                set count111 += 1;
            } else {
                set countOther += 1;
            }
        }
        
        Message($"|000⟩: {count000} times ({100.0 * IntAsDouble(count000) / 1024.0}%)");
        Message($"|111⟩: {count111} times ({100.0 * IntAsDouble(count111) / 1024.0}%)");
        Message($"Other: {countOther} times ({100.0 * IntAsDouble(countOther) / 1024.0}%)");
        
        Message("GHZ State Test Complete!");
    }
}

