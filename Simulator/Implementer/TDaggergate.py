import sys
from Implementer.ParentGate import ParentGate
import math

class TDaggergate(ParentGate):
	"""
	Implementation of the T Dagger Gate.
	"""
	def execute(self, state, operands):
		"""
		The core execution logic of the T Dagger Gate.
		Args:
		    state: Current state.
		    operands: The list of operands over which the gate is applied.
		Returns:
		    The new state after applying the gate.
		"""
		size = len(state)
		newState = [complex(0, 0)] * size
		nQubits = int(math.log(size, 2))
		op = operands[0]

		for i in range(size):
			if state[i] != 0:
				binary = self.decimalToBinary(i, nQubits)
				if binary[op] == '0':
					newState[i] += state[i]
				else:
					newAmplitude = state[i] * complex(1 / math.sqrt(2), - 1 / math.sqrt(2))
					newState[i] += newAmplitude

		return newState