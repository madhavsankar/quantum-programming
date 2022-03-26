import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + "..")
from ProgramRepresentation.Gates import Gates
from Implementer.ParentGate import ParentGate
from Implementer.Xgate import Xgate
from Implementer.Hgate import Hgate
from Implementer.CXgate import CXgate
from Implementer.Tgate import Tgate
from Implementer.TDaggergate import TDaggergate

class ExecutorFactory:
    """
    Executor Factory maps the gates to the corresponding execution logic.
    """
    def getExecutor(self, gate):
        """
        Maps the gate to the corresponding executor.
        Args:
            gate: The gate enum.
        Returns:
            The executor of the corresponding gate.
        """
        if gate == Gates.X:
            return Xgate()
        elif gate == Gates.H:
            return Hgate()
        elif gate == Gates.CX:
            return CXgate()
        elif gate == Gates.T:
            return Tgate()
        elif gate == Gates.TDagger:
            return TDaggergate()
        else:
            return ParentGate()