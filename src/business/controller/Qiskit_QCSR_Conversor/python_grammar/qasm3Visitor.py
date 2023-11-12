from antlr4 import *
from antlr4.tree import *
if "." in __name__:
    from .qasm3Parser import qasm3Parser
    from .qasm3ParserVisitor import qasm3ParserVisitor
else:
    from qasm3Parser import qasm3Parser
    from qasm3ParserVisitor import qasm3ParserVisitor

class qasm3Visitor(qasm3ParserVisitor):

    content = ""
    def __init__(self):
        self.content = ""

    def visitOldStyleDeclarationStatement(self, ctx:qasm3Parser.OldStyleDeclarationStatementContext):
        True
    
    