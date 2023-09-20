
from antlr4 import *
from python_grammar.PythonLexer import PythonLexer
from python_grammar.PythonParser import PythonParser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Trees import Trees

def generateTree(input):
    input_stream = FileStream(input)
    lexer = PythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PythonParser(stream)
    tree = parser.root()
#    tree.getChildren()
    treeStr = tree.toStringTree(recog=parser) #arbol en string
#    print(treeStr)
    return tree

def deepSearch(node:PythonParser.RootContext):
    if node is None or node.getChildCount()==0:
        return
    
    if node.depth() != 1 and "import" in node.getText():
        return 

    # Procesar el nodo actual (aquí puedes hacer lo que necesites con el nodo)
    print("Visitando nodo:", node.getText(), " ", node.depth())
    #node.getRuleContext().type()s

    # Recorrer los nodos hijos
    for child in node.getChildren():
        deepSearch(child)
        
tree = generateTree("Qiskit-QCSR-Conversor\example\circuit.py")
deepSearch(tree)