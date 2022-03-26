import sys
import numpy as np
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm
from pathlib import Path
# Import your simulate function here.
# cs238 can be a file, a folder with an __init__.py file,
from Simulator import simulate
import matplotlib.pyplot as plt
import time
import re

def cirq_simulate(qasm_string: str) -> list:
    """Simulate a qasm string
    Args:
        qasm_string: a string following the qasm format
    Returns:
        statevector: a list, with a complex number for
            each of the 2^num_qubits possible amplitudes
            Ordered big endian, see:
        
quantumai.google/reference/python/cirq/sim/StateVectorTrialResult#state_vector
    """
    circuit = circuit_from_qasm(qasm_string)
    result = cirq.Simulator().simulate(circuit)
    statevector = list(np.around(result.state_vector(), 3))
    return statevector

def compare(state_vector, cirq_state_vector):
    """Our comparison function for your grade
    Args:
        state_vector: your state vector amplitude list
        cirq_state_vector: cirq's state vector amplitude list
    Returns:
        Some value influencing your grade, subject to change :)
    """
    return np.all(np.isclose(state_vector, cirq_state_vector))

def preProcess(qasmString):
    """
    Remove any trailing 0s and the first 4 lines.
    Args:
        qasmString: Qasm text file read as string.
    Returns:
        Program statements as an array.
    """
    qasmString = qasmString.rstrip()
    separatedString = qasmString.splitlines()
    #print('Number of lines of code: ', len(separatedString))
    return (separatedString[4:], len(separatedString))

def findNumberOfQubits(qasmString):
    """
    Code to find the number of qubits needed.
    Args:
        qasmString: Qasm text file read as string.
    Returns:
        Returns the number of qubits needed for simulating the code.
    """
    maxCount = 0
    for sent in qasmString:
        result = [e for e in re.split("[^0-9]", sent) if e != '']
        value = max(map(int, result))
        maxCount = max(maxCount, value)

    return maxCount + 1

# get the directory of qasm files and make sure it's a directory
qasm_dir = Path(sys.argv[1])
assert qasm_dir.is_dir()

qubits = []
executionTime = []
lines = []

# iterate the qasm files in the directory
for qasm_file in qasm_dir.glob("**/*.qasm"):
    # read the qasm file
    print(qasm_file)
    with open(qasm_file, "r") as f:
        qasm_string = f.read()
    # run your simulate function on the qasm string

    (pre, line) = preProcess(qasm_string)
    nq = findNumberOfQubits(pre)
    qubits.append(nq)
    lines.append(line)

    for i in range(1000):
        start = time.time()
        state_vector = simulate(qasm_string)
        end = time.time()
        executionTime.append(end - start)
    
    #print(state_vector)
    # run cirq's simulator on the qasm string
    cirq_state_vector = cirq_simulate(qasm_string)
    # compare the results!
    print(compare(state_vector, cirq_state_vector))
    break

# Plot the range of execution times
plt.hist(executionTime, color = "skyblue")
plt.title('Range of Execution Times')
plt.ylabel('Frequency')
plt.xlabel('Execution Times')
plt.savefig('Range.png')