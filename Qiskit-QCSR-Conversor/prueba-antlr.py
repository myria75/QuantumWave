
from antlr4 import *
from python_grammar.PythonLexer import PythonLexer
from python_grammar.PythonParser import PythonParser
from python_grammar.PythonVisitor import PythonVisitor
from python_grammar.PythonVisitor import PythonParserVisitor

def generateTree(input):
    input_stream = FileStream(input)
    lexer = PythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PythonParser(stream)
    tree = parser.root()
    return tree

def deepSearch(tree):

    visitor = PythonVisitor()
    print(visitor.visit(tree))

tree = generateTree("example\circuit.py")

deepSearch(tree)