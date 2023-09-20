
"""Request example at Raul's API  
"""
__author__ = "Miriam Fernández Osuna"
__version__ = "0.2"

import requests

metrics_endpoint = 'http://172.20.48.7:8080/'

def getCircuits():
    operation = 'circuit/getCircuits/'
    r = requests.get(metrics_endpoint+operation)
    r = r.json()
    return r

def getCircuit(circuit_name):
    operation = 'circuit/getCircuit/'
    r = requests.get(metrics_endpoint+operation, circuit_name)
    r = r.json()
    return r

def insertCircuit(quantum_circuit:dict):
    operation = 'cicuit/insert/'
    r = requests.post(metrics_endpoint+operation, json=quantum_circuit)
    r = r.json()
    
    if r.status_code >= 200 and r.status_code < 300:
        print("INSERT done")
    else:
        print("INSERT falló con código de estado:", r.status_code)

def updateCircuit(quantum_circuit:dict):
    operation = 'circuit/update'
    r = requests.put(metrics_endpoint+operation, json=quantum_circuit)
    
    if r.status_code >= 200 and r.status_code < 300:
        print("UPDATE done")
    else:
        print("UPDATE falló con código de estado:", r.status_code)

def calculateMetrics(quantum_circuit:dict):
    operation = 'circuit/calculateMetrics'
    r = requests.post(metrics_endpoint+operation, json=quantum_circuit)
    r = r.json()
    return r        

def getMetrics():
    operation = 'circuit/calculateMetrics'
    qcsr_object = ''
    r = requests.get(metrics_endpoint+operation+qcsr_object)
    r = r.json()
    return r   

def getMetricsTypes():
    operation = 'metric/getMetricTypes'
    r = requests.get(metrics_endpoint+operation)
    r = r.json()
    return r 

circuit = {
  "name" : "PostCircuitName2",
  "circuitCode" : "[[\"X\"]]"
}

print(calculateMetrics(circuit))