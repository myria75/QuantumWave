
"""Content conversion from base64 to natural language
"""

import base64
import codecs
import configparser
import os
import re
import shutil
import uuid
from pymongo import MongoClient

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

#MongoDB
db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll = eval(config.get('MongoDB', 'db_coll'))
db_coll_accepted = eval(config.get('MongoDB', 'db_coll_accepted'))
db_coll_discarded = eval(config.get('MongoDB', 'db_coll_discarded'))
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]
collRepo_accepted = dbGithub[db_coll_accepted]
collRepo_discard = dbGithub[db_coll_discarded]
dir_code = os.path.join("src","persistency","Mongo_Ingest_Data_Dealing","code")
dir_code_discard = os.path.join("src","persistency","Mongo_Ingest_Data_Dealing","code_discard")

def getContent():
    query = {
        "$and": [
            {"repo_language": {"$in": ["openqasm", "qsharp", "Python"]}},
            {"repo_extension": {"$in": [None, "cirq", "qiskit"]}}
        ]
    }
    result = collRepo.find(query)
    
    for r in result:
        file_path:str = "{}_{}_{}_{}_{}".format(r['repo_language'], r['repo_extension'], r['repo_author'], r['repo_name'], r['path'])
        file_path = file_path.replace("/",".")

        #convert content to base64
        content_b64 = r['content']
        content_b64bytes = content_b64.encode('utf-8')
        content_bytes = base64.b64decode(content_b64bytes)
        content = content_bytes.decode('utf-8')
        
        search_result = "n"

        if r['repo_language'] == 'Python':
            search_expression = eval(config.get('expression', 'search_python'))
            search_result = re.search(search_expression, content)
        elif r['repo_language'] == 'qsharp':
            search_expression = eval(config.get('expression', 'search_qsharp'))
            search_result = re.search(search_expression, content)
        
        max_path_length = 255
        
        if search_result is None:
            dir_path = dir_code_discard
            insert(r, content, file_path, True) #set if this doccument is going to be discarded
        else: 
            dir_path = dir_code
            insert(r, content, file_path, False)

        dir_path = os.path.join(dir_path, r['repo_language'])

        if r['repo_extension'] is not None:
            dir_path = os.path.join(dir_path, r['repo_extension'])
        
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, file_path)
        
        if len(file_path) >= max_path_length:
            file_path_format = "."+file_path.split(".")[-1] #get the text from the last point to the right part of the text (".py")
            length_cut = 255 - len(file_path_format)
            file_path = file_path[:length_cut] #cut to (max size - count the characters above the string
            file_path = file_path+file_path_format #previously put the string in the last part

        with codecs.open(file_path, 'w', 'utf-8') as f:
            f.write(content)
            
def initializeDirs():
    #empty and create code and code_discard directories
    dirs = dir_code, dir_code_discard

    for d in dirs:
        if os.path.isdir(d) is True:
            shutil.rmtree(d)
        os.mkdir(d)

def insert(r, content, file_path, discard):
    hybrid:bool = False
    coll_to_insert = None

    #checks if not discarded doccuments are hybrid
    if discard is False: 
        search_expression = eval(config.get('expression', 'search_hybrid'))
        search_result = re.search(search_expression, content)
        hybrid = False if (search_result is None) else True
        coll_to_insert = collRepo_accepted  #chosen collection to ingest 
    else:
        coll_to_insert = collRepo_discard

    #json to ingest at MongoDB
    ingest = {
        "id":str(uuid.uuid4()),
        "language": r['repo_language'],
        "extension": r['repo_extension'],
        "author": r['repo_author'],
        "name": r['repo_name'],
        "path": file_path, 
        "hybrid": hybrid, 
        "content": content
    }
    
    coll_to_insert.insert_one(ingest) #inserts the commits

initializeDirs()
getContent()