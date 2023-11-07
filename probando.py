import src.business.controller.QCPDTool.views as views
import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor
patrones = views.generate_pattern('[["RY",{"CONTROL":1},"_",{"CONTROL":1},"X"],["_","H",{"CONTROL":2},"X"],["_","_","X"]]')

circuito = {
    'id': 1,
    'circuito': 2,
    'patrones': patrones
}

with open('C:\\Users\\Miriam\\Desktop\\Patrones\\src\\business\\controller\\Qiskit_QCSR_Conversor\\example\\circuit.py', 'r') as archivo:
    contenido = archivo.read()
    antlr_tree = conversor.generateTree(contenido)
    circuitJson = conversor.deepSearch(antlr_tree)
    print(circuitJson)

#'[["H",{"ORACLE":1},"H","MEASURE"]]'
#'[["H","MEASURE"],["S",{"CONTROL":2},"Z"],["_","X"],["H"]]'
#'[["RY",{"CONTROL":1},"_",{"CONTROL":1},"X"],["_","H",{"CONTROL":2},"X"],["_","_","X"]]'
#[["H","_",{"CONTROL":1},"_",{"CONTROL":2}],["H","X","X"],["H","_","_","X","X"]]
#[[{"CONTROL":2},"_",{"CONTROL":1}],["_",{"CONTROL":2},{"CONTROL":3}],["X","X","_","MEASURE"],["_","_","X","MEASURE"]]