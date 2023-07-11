import os
import codecs

path = "Python_qiskit_qiskrypt_qiskrypt_src.quantum_regime.cryptography.key_exchange.semi_quantum_conference_key_agreement.dv.entanglement_based.bkmps22.noiseless.with_no_eavesdropping.QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound.py";
print("path:", path)
print("length:", len(path))

file_path_format = "."+path.split(".")[-1] #coger el string del ultimo punto hasta la derecha (".py")
length_cut = 255 - len(file_path_format)
file_path = path[:length_cut] #recortar hasta (max length - contar los caracteres del string de arriba)
file_path = file_path+file_path_format #poner al final el string de arriba
print(file_path)

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(path)
