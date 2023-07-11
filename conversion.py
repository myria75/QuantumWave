
"""Content conversion from base64 to natural language
"""

from pymongo import MongoClient
import base64
import os
import re
import codecs

__author__ = "Miriam Fernández Osuna"
__version__ = "1.0"

#MongoDB
db_link = 'mongodb://localhost:27017'
db_name = 'repositories'
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo = dbGithub['documents']

def getContent():
    query = { "repo_extension":"qiskit" }
    result = collRepo.find(query)

    for r in result:
        file_path:str = r['repo_language']+"_"+r['repo_extension']+"_"+r['repo_author']+"_"+r['repo_name']+"_"+r['path']
        file_path = file_path.replace("/",".")
        print(file_path)

        #convierte content de base64
        content_b64 = r['content']
        content_b64bytes = content_b64.encode('utf-8')
        content_bytes = base64.b64decode(content_b64bytes)
        content = content_bytes.decode('utf-8')
        
        search_expression = "from qiskit|import qiskit|import qiskit.|from qiskit."
        search_result = re.search(search_expression, content)

        if search_result is None:
            #no ha encontrado, file_path apunta a la carpeta "qiskit_discard"
            file_path = os.path.join('qiskit_discard', file_path)
        else:
            file_path = os.path.join('qiskit', file_path)

        if len(file_path) >= 255:
            file_path_format = "."+file_path.split(".")[-1] #coger el string del ultimo punto hasta la derecha (".py")
            length_cut = 255 - len(file_path_format)
            file_path = file_path[:length_cut] #recortar hasta (max length - contar los caracteres del string de arriba)
            file_path = file_path+file_path_format #poner al final el string de arriba

        with codecs.open(file_path, 'w', 'utf-8') as f: #max length = 255, hay que sacar el .py del final
            f.write(content)
            
def initializeDirs():
    dirs = "qiskit", "qiskit_discard"

    for d in dirs:
        if os.path.isdir(d) is True:
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))
            
            os.rmdir(d)
        
        os.mkdir(d)

initializeDirs()
getContent()