

def detectEntanglement(converted_circuits: dict):
        hasEntaglement = False
        HGate = {}  
        XGate = {} 
        ControlGate = {}

        #añadir indices a los diccionarios, sabiendo en que posición se encuentra cada cubit
        for qubit, gates in converted_circuits.items():
            for idgate, gate in enumerate(gates):
                if gate == "H":
                    if qubit not in HGate:
                        HGate[qubit] = []
                    HGate[qubit].append(idgate)
                elif gate == "X":
                    if qubit not in XGate:
                        XGate[qubit] = []
                    XGate[qubit].append(idgate)
                elif gate == "Control":
                    if qubit not in ControlGate:
                        ControlGate[qubit] = []
                    ControlGate[qubit].append(idgate)

        #las condiciones de excel
        for qubitH, h_positions in HGate.items():
            for h_idgate in h_positions:  
                for qubitX, x_positions in XGate.items():
                    if qubitX != qubitH: 
                        for x_idgate in x_positions:
                            if x_idgate == h_idgate + 1:
                                print(f"Entrelazamiento")
                                hasEntaglement = True

                if qubitH in ControlGate:
                    for control_idgate in ControlGate[qubitH]:
                        if control_idgate == h_idgate + 1:  # Control está inmediatamente después de H
                            print(f"Entrelazamiento")
                            hasEntaglement = True

        return hasEntaglement