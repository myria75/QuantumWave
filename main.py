
"""Main executable of the project
"""

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

import configparser
from src.business.controller.Qiskit_QCSR_Conversor.EmptyCircuitException import EmptyCircuitException
import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor
import src.business.controller.QmetricsAPI.qmetrics_functions as qmetrics
import src.business.controller.QCPDTool.views as qcpdtool
import os

#Searches in GitHub and ingest the data
#import src.persistency.Mongo_Ingest_Data_Dealing.languages_ingest_with_dates

#Conversion from base64 to natural language and clasifies into languages and into quantic code and not quantic code
#import src.persistency.Mongo_Ingest_Data_Dealing.conversion

#Searches in db for codes in qiskit language
from pymongo import MongoClient

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll = eval(config.get('MongoDB', 'db_coll_accepted'))
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]

query = {"extension": "qiskit"}
documents = collRepo.find(query)


for document in documents:
    print(document["path"])
    #antlr4 of the codes and conversion from python qiskit to QCSR
    circuitJson = ""
    arbolAntlr = conversor.generateTree(document["content"])
    
    errorsFoundAtParse = False
    try:
        circuitJson = conversor.deepSearch(arbolAntlr)
    except EmptyCircuitException as e:
        print("Empty array error")
        errorsFoundAtParse = True
    except (AttributeError, KeyError, ValueError, IndexError) as e: 
        print("Throws an error")
        errorsFoundAtParse = True

    if errorsFoundAtParse:
        errorMsg = "The antlr4 tree couldn't be generated. The circuit isn't converted"
        document["circuit"] = { 'error': errorMsg }
        document["metrics"] = { 'error': errorMsg }
    else:
        document["circuit"] = circuitJson
        print(circuitJson)
        qmetricsjson =  {
            "name" : "MiriamTFGCircuit",
            "circuitCode" : circuitJson
        }

        #Query QPainter and QMetrics 
        qmetrics.updateCircuit(qmetricsjson)
        r = qmetrics.calculateMetrics(qmetricsjson)
        metrics = r.json()

        #Checks if the metrics are correct
        if "status" in metrics:
        #if status starts by 4** or 5**
            if str(metrics["status"])[0] in ("4","5"):
                document["metrics"] = { 'error': "QMetrics couldn't calculate the metrics" }
        else: 
            document["metrics"] = metrics

    document["patterns"] = qcpdtool.generate_pattern(circuitJson)    


    #Update entry in MongoDB  
    collRepo.update_one({"_id": document["_id"]},
    {
        "$set": {
            "circuit": document["circuit"],
            "metrics": document["metrics"],
            "patterns": document["patterns"]
        }
    })

connection.close()