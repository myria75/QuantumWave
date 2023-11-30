
"""It creates a csv file where shows all the information from dataset
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

import configparser
import csv
import os
import time
from pymongo import MongoClient

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll = eval(config.get('MongoDB', 'db_coll_accepted'))
connection = MongoClient(db_link, socketTimeoutMS=None)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]
n_generated_trees = 0
n_generated_circuits = 0
n_blank_circuits = 0

query = {
  "$and": [
    { "metrics": { "$exists": True } },
    { "metrics.error": { "$exists": False } },
    { "patterns": { "$exists": True } },
    { "patterns.err_msg": { "$exists": False } }
  ]
}

field = ["id", "language", "extension", "author", "name", "path", "hybrid"]
metricsN = 0

initialDoc = collRepo.find(query)
for doc in initialDoc:
    metricsN = len(doc["metrics"])
    for i in range(0, len(doc["metrics"])):
        field.append(f"m.{doc['metrics'][i]['metric']['name']}")
    break

initialDoc.close()
field+=["p.initialization", "p.superposition", "p.oracle", "p.entanglement"]
print(field)

documents = collRepo.find(query, no_cursor_timeout=True)
refreshTime = 600 #10 minutes
startQueryTime = time.time()

with open('dataset_openqasm_qiskit.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(field)

  for document in documents:
    nowQueryTime = time.time()
    if nowQueryTime - startQueryTime >= refreshTime:
      documents.close()
      documents = collRepo.find(query, no_cursor_timeout=True)
      startQueryTime = nowQueryTime
    
    id = document["id"]
    language = document["language"]
    extension = document["extension"] 
    author = document["author"]
    name = document["name"]
    path = document["path"]
    hybrid = document["hybrid"]
    metrics = []
    initialization = False
    superposition = False
    oracle = False
    entanglement = False

    print(document["patterns"])
    for i in range(0, len(document["metrics"])):
      metrics.append(document['metrics'][i]['value'])
    
    if len(document["patterns"]["initialization"]) > 0:
      initialization = True
    if len(document["patterns"]["superposition"]) > 0:
      superposition = True
    if len(document["patterns"]["oracle"]) > 0:
      oracle = True
    if len(document["patterns"]["entanglement"]) > 0:
      entaglement = True

    rowToInsert = [id, language, extension, author, name, path, hybrid]
    rowToInsert += metrics 
    rowToInsert += [initialization, superposition, oracle, entanglement]

    for i in range(0, len(field)-len(rowToInsert)):
       rowToInsert.append("None")

    writer.writerow(rowToInsert)