
"""Exception empty array when tries conversion from antlr4 tree to QCSR 
"""

class EmptyCircuitException(Exception):
    def __init__(self, message="Empty array error. Conversion from python qiskit to QCSR failed"):
        super().__init__(message)