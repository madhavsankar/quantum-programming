import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + "..")
from ProgramRepresentation.ProgramRepresentation import ProgramRepresentation, Statement
from ProgramRepresentation.Gates import Gates
from Implementer.ExecutorFactory import ExecutorFactory

class Implementer:
	"""
	Implementation of the CX Gate.
	"""
	def __init__(self, programRepresentation):
		self.programRepresentation = programRepresentation

	def implement(self):
		"""
		This method creates an initial state where all the qubits are 0 and then applies each of the program statement one by one.
		Returns:
		    The new state after applying all the gates.
		"""
		qubits = self.programRepresentation.qubits
		state = [complex(0, 0)] * (2 ** qubits)
		state[0] = complex(1, 0)
		for statement in self.programRepresentation.statements:
			factory = ExecutorFactory()
			executor = factory.getExecutor(statement.gate)
			state = executor.execute(state, statement.operands)

		return state