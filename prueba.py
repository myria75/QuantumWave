from src.business.controller.Qiskit_QCSR_Conversor.EmptyCircuitException import EmptyCircuitException

try:
    raise EmptyCircuitException()
except EmptyCircuitException as e:
        print("Empty array error")

print("llega aqui")