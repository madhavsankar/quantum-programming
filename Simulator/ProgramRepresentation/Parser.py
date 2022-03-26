import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + "..")
from ProgramRepresentation.ProgramRepresentation import ProgramRepresentation, Statement
from ProgramRepresentation.Gates import Gates

import re

class Parser:
	"""
	Parser class that parses the QASM file into a Program Representation.
	"""
	def __init__(self, qasmString):
		self.qasmString = Parser._preProcess(qasmString)

	@staticmethod
	def _preProcess(qasmString):
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
		return separatedString[4:]

	@staticmethod
	def _findNumberOfQubits(qasmString):
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

	@staticmethod
	def _findOperand(gate):
		"""
		Find the gate enum given a string
		Args:
		    gate: Input gate string.
		Returns:
		    The gate enum.
		"""
		if gate == 'h':
			return Gates.H
		elif gate == 'x':
			return Gates.X
		elif gate == 't':
			return Gates.T
		elif gate == 'tdg':
			return Gates.TDagger
		elif gate == 'cx':
			return Gates.CX

	@staticmethod
	def _createSentence(sent):
		"""
		Convert the QASM sentence into a statement.
		Args:
		    sent: Qasm text file sentence.
		Returns:
		    A statement object with the gate and corresponding operands list.
		"""
		opSplit = sent.split(' ')
		operator = Parser._findOperand(opSplit[0])
		operands = [int(e) for e in re.split("[^0-9]", opSplit[1]) if e != '']
		statement = Statement(operator, operands)
		return statement


	def parse(self):
		"""
		Parses the QASM string into a Program Representation object.
		Returns:
		    A Program Representation object consisting of a list of statements.
		"""
		qubits = Parser._findNumberOfQubits(self.qasmString)
		#print('Number of qubits: ', qubits)
		prog = []

		for sent in self.qasmString:
			progSent = Parser._createSentence(sent)
			prog.append(progSent)

		programRepresentation = ProgramRepresentation(qubits, prog)
		return programRepresentation

		

