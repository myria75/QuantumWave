
"""Exception empty array when tries conversion from antlr4 tree to QCSR 
"""

class VariableNotCalculatedException(Exception):
    def __init__(self, message="Couldn't calculate the variable"):
        super().__init__(message)