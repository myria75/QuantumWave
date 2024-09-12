
def detectEntanglement(converted_circuits: dict):
        returnCircuits = {}  
        HGate = {}  
        XGate = {} 
        controlGate = {}

        #añadir indices a los diccionarios, sabiendo en que posición se encuentra cada cubit
        for name, qubits in converted_circuits.items():
            hasEntaglement = False
            for idqubit, qubitContent in enumerate(qubits):
                if 'H' in qubitContent:
                    allHpositions = [i for i, gate in enumerate(qubitContent) if gate == 'H']
                    for posH in allHpositions:
                        if posH+1 != len(qubitContent) and isinstance(qubitContent[posH+1], dict):
                            posControl = posH + 1
                            controlDict = next(iter(qubitContent[posControl].items()))
                            if controlDict[0] == "CONTROL":
                                idqubitControlled = controlDict[1]
                                if qubits[idqubitControlled][posControl] == "X":
                                    beforeX = qubits[idqubitControlled][0:posControl]
                                    hasEntaglement = all(gateBeforeX == "_" for gateBeforeX in beforeX)

            returnCircuits[name] = hasEntaglement

        return returnCircuits