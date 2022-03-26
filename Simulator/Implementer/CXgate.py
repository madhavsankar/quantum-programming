import sys
from Implementer.ParentGate import ParentGate
import math

class CXgate(ParentGate):
	"""
	Implementation of the CX Gate.
	"""
	def execute(self, state, operands):
		"""
		The core execution logic of the CX Gate.
		Args:
		    state: Current state.
		    operands: The list of operands over which the gate is applied. First is the control qubit and second the target qubit.
		Returns:
		    The new state after applying the gate.
		"""
		size = len(state)
		newState = [complex(0, 0)] * size
		nQubits = int(math.log(size, 2))
		control = operands[0]
		target = operands[1]

		for i in range(size):
			if state[i] != 0:
				binary = self.decimalToBinary(i, nQubits)

				if binary[control] == '0':
					newState[i] += state[i]
				else:
					if binary[target] == '0':
						binary = self.setString(binary, target, '1')
					else:
						binary = self.setString(binary, target, '0') 

					decimal = self.binaryToDecimal(binary)
					newState[decimal] += state[i]

		return newState