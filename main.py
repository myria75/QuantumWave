import src.business.controller.Qiskit_QCSR_Conversor.Qiskit_QCSR_Conversor as conversor
import src.business.controller.QmetricsAPI.qmetrics_functions as qmetrics

#Búsqueda en github e ingesta de los codigos
#import src.persistency.Mongo_Ingest_Data_Dealing.languages_ingest_with_dates

#traduccion base64 a lenguaje natural y clasificarlos en codigos cuanticos y no cuanticos y a su vez entre lenguajes
#import src.persistency.Mongo_Ingest_Data_Dealing.conversion

#Busqueda en bbdd para códigos que queremos trabajar
from pymongo import MongoClient

db_link = 'mongodb://localhost:27017'
db_name = 'repositories'
db_coll = 'accepted_code'
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]

query = {"extension": "qiskit"}
documents = collRepo.find(query)

for document in documents:
    #antlr4 de los codigos y traducción python qiskit a QCSR
    arbolAntlr = conversor.generateTree(document["content"])
    try:
        circuitJson = conversor.deepSearch(arbolAntlr)
    except (AttributeError, KeyError, ValueError, IndexError) as e: #TODO: probar nuevo filtro cuando ejecute
        print("Encontrado entrada que tira error")
    
    if circuitJson != "empty array error": #TODO: arreglar circuitos que devuelva arrays vacios
        print(document["path"])
        print(circuitJson)
        qmetricsjson =  {
            "name" : "MiriamTFGCircuit",
            "circuitCode" : circuitJson
        }

        #consultar qpainter y a qmetrics 
        qmetrics.updateCircuit(qmetricsjson)
        r = qmetrics.calculateMetrics(qmetricsjson)
        metrics = r.json()

        #if para comprobar que las métricas están bien
        if len(metrics) > 5:
            #Actualiza mongo
            collRepo.update_one({"_id": document["_id"]},  {"$set": {"metrics": metrics}})
        else:
            print("QMetrics no ha podido calcular las metricas")

connection.close()