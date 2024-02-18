
"""Exception not found operation when tries detection of operations and can't know which one it is 
"""

class OperationNotFoundException(Exception):
    def __init__(self, message="Couldn't find operation"):
        super().__init__(message)