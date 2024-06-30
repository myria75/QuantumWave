
"""It creates a csv file where shows all the information from dataset
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

import configparser
import csv
import os
import time
from pymongo import MongoClient
import pandas
configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

file_name = os.path.join('src', 'presentation', 'frontend', 'app', 'dataset_openqasm_qiskit.csv')

db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll = eval(config.get('MongoDB', 'db_coll_accepted'))
connection = MongoClient(db_link, socketTimeoutMS=None)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]

query = {
  "$and": [
    { "circuits.metrics": { "$exists": True } },
    { "circuits.metrics.error": { "$exists": False } },
    { "circuits.patterns": { "$exists": True } },
    { "circuits.patterns.err_msg": { "$exists": False } }
    #, { "path": { "$regex": "test", "$options": "i" } }
  ]
}

field = ["id", "language", "extension", "author", "name", "path", "circuit"]
metricsN = 0

def generateCSV():
  initialDoc = collRepo.find(query)
  foundInitialMetrics = False
  for doc in initialDoc:
      for circ in range(len(doc["circuits"])):
          metricsN = len(doc["circuits"][circ]["metrics"])
          if metricsN != 33:
              continue
          for i in range(0, metricsN):
              field.append(f"m.{doc['circuits'][circ]['metrics'][i]['metric']['name']}")
          foundInitialMetrics = True
          break
      if foundInitialMetrics:
          break

  initialDoc.close()
  field+=["p.initialization", "p.superposition", "p.oracle", "p.entanglement"]
  print(field)

  documents = collRepo.find(query, no_cursor_timeout=True)
  refreshTime = 600 #10 minutes
  startQueryTime = time.time()


  with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(field)
    

    for document in documents:
      nowQueryTime = time.time()
      if nowQueryTime - startQueryTime >= refreshTime:
        documents.close()
        documents = collRepo.find(query, no_cursor_timeout=True)
        startQueryTime = nowQueryTime
      
      for circuit_index in range(len(document["circuits"])):
          id = document["id"]
          language = document["language"]
          extension = document["extension"] 
          author = document["author"]
          name = document["name"]
          path = document["path"]
          circuit = document["circuits"][circuit_index]["circuit"]
          metrics = []
          initialization = False
          superposition = False
          oracle = False
          entanglement = False
      
          for i in range(0, len(document["circuits"][circuit_index]["metrics"])):
              metrics.append(round(float(document["circuits"][circuit_index]['metrics'][i]['value']), 3)) #fix some decimal errors detected in csv file
          
          if len(document["circuits"][circuit_index]["patterns"]["initialization"]) > 0:
            initialization = True
          if len(document["circuits"][circuit_index]["patterns"]["superposition"]) > 0:
            superposition = True
          if len(document["circuits"][circuit_index]["patterns"]["oracle"]) > 0:
            oracle = True
          if len(document["circuits"][circuit_index]["patterns"]["entanglement"]) > 0:
            entaglement = True
      
          rowToInsert = [id, language, extension, author, name, path, circuit]
          rowToInsert += metrics 
          rowToInsert += [initialization, superposition, oracle, entanglement]
      
          for i in range(0, len(field)-len(rowToInsert)):
            rowToInsert.append("None")
      
          writer.writerow(rowToInsert)
          
  df = pandas.read_csv(file_name, delimiter=';')
  df_no_duplicates = df.drop_duplicates(subset=['path', 'circuit'])
  df_no_duplicates.to_csv(file_name, index=False, sep=';')