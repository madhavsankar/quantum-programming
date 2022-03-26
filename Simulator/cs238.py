# Copy of Simulator.py for the sake of compatibility with CompareSimulator.py
import sys
from ProgramRepresentation.Parser import Parser
from ProgramRepresentation.ProgramRepresentation import ProgramRepresentation, Statement
from Implementer.Implementer import Implementer

from pathlib import Path
import time

def simulate(qasmString):
	"""
	Simulator function that parses and executes the code.
	Args:
	    qasmString: Qasm text file read as string.
	Returns:
	    statevector: a list, with a complex number for
	        each of the 2^num_qubits possible amplitudes
	        Ordered big endian.
	"""
	start = time.time()

	pr = Parser(qasmString)
	pra = pr.parse()

	implementer = Implementer(pra)
	lst = implementer.implement()

	anslist = []
	for num in lst:
		rl = round(num.real, 3)
		img = round(num.imag, 3)
		anslist.append(complex(rl, img))
	
	end = time.time()
	#print('Time taken: ', end - start)

	return anslist