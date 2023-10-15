#https://tomassetti.me/parsing-any-language-in-java-in-5-minutes-using-antlr-for-example-python/
from antlr4 import *
from python_grammar.PythonLexer import PythonLexer
from python_grammar.PythonParser import PythonParser

class ParserFacade:
    def parse(self, input:str) -> PythonParser.File_inputContext: #crea el arbol
        input_stream = FileStream(input)
        lexer = PythonLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PythonParser(stream)
        return parser.file_input()
    
class AstPrinter:
    ignoringWrappers = False

    def setIgnoringWrappers(self, ignoringWrappersVal:bool):
        self.ignoringWrappers = ignoringWrappersVal

    def explore(self, ctx:RuleContext, indentation:int):
        toBeIgnored:bool = self.ignoringWrappers and ctx.getChildCount()==1 and isinstance(ctx.getChild(0), ParserRuleContext)
        ruleName = PythonParser.ruleNames[ctx.getRuleIndex()]
        print(("  "*indentation),ruleName,":",ctx.getText())
        if not toBeIgnored:
            for i in range(0, ctx.getChildCount()):
                element = ctx.getChild(i)
                if isinstance(element, RuleContext):
                    AstPrinter.explore(self, element, indentation+1)

    def print(self, ctx:RuleContext):
        AstPrinter.explore(self, ctx, 0)

parserFacade = ParserFacade()
astPrinter = AstPrinter()
astPrinter.print(parserFacade.parse("Qiskit-QCSR-Conversor\example\circuit.py"))