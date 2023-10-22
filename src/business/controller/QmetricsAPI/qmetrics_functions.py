
"""Request example at Raul's API  
"""

import requests
import configparser
import os

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

metrics_endpoint = eval(config.get('URL', 'qmetrics'))

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
    return r        

def getMetrics():
    operation = 'circuit/getMetrics'
    qcsr_object = ''
    r = requests.get(metrics_endpoint+operation+qcsr_object)
    r = r.json()
    return r   

def getMetricsTypes():
    operation = 'metric/getMetricTypes'
    r = requests.get(metrics_endpoint+operation)
    r = r.json()
    return r 