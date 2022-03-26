import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + "..")
from ProgramRepresentation.Gates import Gates

import enum

class Statement:
	"""
	Statement object represents each statement of the program comprising of the gate and the list of operands.
	"""
	def __init__(self, gate, operands):
		self.gate = gate
		self.operands = operands

class ProgramRepresentation:
	"""
	Program Representation consists if the number of qubits needed for the program and the list of statements.
	"""
	def __init__(self, qubits, statements):
		self.qubits = qubits
		self.statements = statements
