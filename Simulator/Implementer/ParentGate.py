class ParentGate():
	"""
	Implementation of the Parent gate. All other gates inherit from it.
	"""
	def execute(self, state, operands):
		"""
		The core execution logic of the Gates. All the children classes override this method.
		Args:
		    state: Current state.
		    operands: The list of operands over which the gate is applied.
		Returns:
		    The new state after applying the gate.
		"""
		return state

	def decimalToBinary(self, x, n):
		"""
		Converts the integer, x into a binary string of the given length, n.
		Args:
		    x: Given integer.
		    n: Length of the string you want the output to be.
		Returns:
		    Binary string representation of x.
		"""
		s = bin(x).replace("0b", "")
		currsize = len(s)
		ans = '0' * (n - currsize)
		ans += s
		return ans

	def binaryToDecimal(self, x):
		"""
		Converts a binary string x to integer.
		Args:
		    x: Binary String.
		Returns:
		    The integer representation of x.
		"""
		return int(x, 2)

	def setString(self, s, pos, value):
		"""
		Set s[pos] = value.
		Args:
		    s: Given string.
		    pos: The position in s that needs to be changed.
		    value: The characted to be written at s[pos].
		Returns:
		    A new string with newString with newString[pos] as value and the rest of the positions same as s.
		"""
		newString = ""
		for spos in range(len(s)):
			if spos == pos:
				newString += value
			else:
				newString += s[spos]
		return newString