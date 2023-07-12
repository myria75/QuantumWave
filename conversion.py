
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

        #convert content to base64
        content_b64 = r['content']
        content_b64bytes = content_b64.encode('utf-8')
        content_bytes = base64.b64decode(content_b64bytes)
        content = content_bytes.decode('utf-8')
        
        search_expression = "from qiskit|import qiskit|import qiskit.|from qiskit."
        search_result = re.search(search_expression, content)
        max_path_length = 255

        if search_result is None:
            #no result? file_path points at "qiskit_discard"
            file_path = os.path.join('qiskit_discard', file_path)
        else:
            file_path = os.path.join('qiskit', file_path)

        if len(file_path) >= max_path_length:
            file_path_format = "."+file_path.split(".")[-1] #take the string from the last point til the right part of the string (".py")
            length_cut = 255 - len(file_path_format)
            file_path = file_path[:length_cut] #cut still (max length - count the characters of the top from the string)
            file_path = file_path+file_path_format #put previous string at the last part

        with codecs.open(file_path, 'w', 'utf-8') as f: #take .py from the last part
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