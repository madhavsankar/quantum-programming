import enum
		
class Gates(enum.Enum):
    """
    Enum for the allowed gates.
    """
    H = 'h'
    X = 'x'
    T = 't'
    TDagger = 'tdg'
    CX = 'cx'
