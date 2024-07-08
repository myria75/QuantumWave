import configparser
from pymongo import MongoClient
import os

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

connection = None
collRepo = None

csv_query = {
  "$and": [
    { "circuits.metrics": { "$exists": True } },
    { "circuits.metrics.error": { "$exists": False } },
    { "circuits.patterns": { "$exists": True } },
    { "circuits.patterns.err_msg": { "$exists": False } }
  ]
}

def connect_to_mongodb():
    global connection, collRepo
    db_link = eval(config.get('MongoDB', 'db_link'))
    db_name = eval(config.get('MongoDB', 'db_name'))
    db_coll = eval(config.get('MongoDB', 'db_coll_accepted'))
    connection = MongoClient(db_link, socketTimeoutMS=None)
    dbGithub = connection[db_name]
    collRepo = dbGithub[db_coll]

def disconnect_from_mongodb():
    global connection
    if connection:
        connection.close()

def getRepositoriesList():
    connect_to_mongodb()
    if collRepo is not None:
        results = collRepo.find(csv_query)
        reposList = sorted(set(doc['name'] for doc in results))
        disconnect_from_mongodb()
        return reposList
    else:
        return []

def getFilesList(repository):
    connect_to_mongodb()
    if collRepo is not None:
        results = collRepo.find({"name": repository})
        filesList = sorted(set(doc['path'] for doc in results))
        disconnect_from_mongodb()
        return filesList
    else:
        return []

    
