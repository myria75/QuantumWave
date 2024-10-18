#from src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Parser import

def detectEntanglement(qubits):
    qubitsFinal = []

    if isinstance(qubits, str):
        qubitsFinal = eval(qubits)
    else:
        qubitsFinal = qubits

    hasEntaglement = False
        
    for idqubit, qubitContent in enumerate(qubitsFinal):
        if 'H' in qubitContent:
            allHpositions = [i for i, gate in enumerate(qubitContent) if gate == 'H']
            for posH in allHpositions:
                posControl = posH + 1

                if posControl < len(qubitContent):
                    while posControl < len(qubitContent)-1:
                        if qubitContent[posControl] == "_":
                            posControl += 1
                        else:
                            break
                    
                    if isinstance(qubitContent[posControl], dict):
                        controlDict = next(iter(qubitContent[posControl].items()))
                        if controlDict[0] == "CONTROL":
                            idqubitControlled = controlDict[1]
                            if qubitsFinal[idqubitControlled][posControl] == "X":
                                beforeX = qubitsFinal[idqubitControlled][0:posControl]
                                hasEntaglement = all(gateBeforeX == "_" for gateBeforeX in beforeX)

    return hasEntaglement