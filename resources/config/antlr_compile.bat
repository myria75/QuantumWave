set "source=..\parserGrammar"
set "destination=..\..\src\business\controller\Qiskit_QCSR_Conversor\languages_grammar"

REM antlr4 -Dlanguage=Python3 "%source%\*.g4" -visitor
java org.antlr.v4.Tool -Dlanguage=Python3 "%source%\*.g4" -visitor

for %%f in ("%source%\*") do (
    if "%%~xf" neq ".g4" (
        move "%%f" "%destination%"
    )
)