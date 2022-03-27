To compare the simulators for the 14 Benchmark programs. Use the compare\_simulators.py already added. A copy of the Simulator.py code called cs238.py is created for compatibility. Then run this:
    python compare_simulators.py QASM
            
To compare the simulators for the traditional algorithms:
    python CompareSimulators.py QASM_2

        
To run the simulation time tests on the given Benchmarks:
    python Test.py QASM
        
To run the simulation time tests for custom programs of same number of qubits:
    python Test.py QASM_SameQubits
        
To run the simulation time tests for custom programs of same number of operations:
    python Test.py QASM_SameLines
        
To run the simulation time tests for various gate types:
    python Test_Gates.py QASM_GateTypes
        
To find the range of simulation times:
    python Test_Range_Times.py QASM
