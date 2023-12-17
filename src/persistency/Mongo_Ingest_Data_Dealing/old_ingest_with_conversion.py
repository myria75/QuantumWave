
"""Ingest content from every repos at MongoDB 
"""

import ast
import base64
import codecs
import configparser
import os
import time
from datetime import date, datetime
import logging
from time import sleep
from urllib.parse import quote
import re
import requests
from requests.adapters import Retry, HTTPAdapter
import shutil
import uuid
from pymongo import MongoClient

configuration_file =  os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)
token = eval(config.get('GitHub', 'token'))

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

#URL and headers
search_repo_url = 'https://api.github.com/search/repositories?q={}+created:{}-01-01..{}-12-31&per_page=100&page={}'
search_code_url = 'https://api.github.com/search/code?q={}&per_page=100&page={}'
content_url = 'https://api.github.com/repos/{}/contents/{}'
limit_url = 'https://api.github.com/rate_limit'

contadorglobal = 0

repo_search_in = 'in:readme+in:name+in:description+in:topics'
max_search_pages = 10 #pagination with per_page = 100 
year_from = 2015

max_path_length = 255


headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

def obtainConfiguration():
    return token, db_link, db_name, db_coll

def rateLimit(resource) -> tuple[int, datetime]:
    "Returns remaining requests left and the time when they are reset"
    session = requests.Session()
    retry = Retry(connect=100, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    r = session.get(limit_url, headers=headers)
    rateLimit = r.json()
    remaining = rateLimit['resources'][resource]['remaining']
    reset = rateLimit['resources'][resource]['reset']
    resetDate = datetime.fromtimestamp(reset)
    return remaining, resetDate

def checkWaitRateLimit(resource):
    "Checks remaining requests left. If none, waits until rate-limit is reset"
    remaining, resetDate = rateLimit(resource)
    
    if remaining == 0:
        print("Waiting for rate limit to reset...")
        secondsToWait = (resetDate - datetime.now()).total_seconds()
        sleep(secondsToWait+10)

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

    log_msg = f"{r['repo_language']}.{r['repo_extension']}, {r['repo_author']}/{r['repo_name']} | {file_path} has been"
    #checks if not discarded doccuments are hybrid
    if discard is False: 
        search_expression = eval(config.get('expression', 'search_hybrid'))
        search_result = re.search(search_expression, content)
        hybrid = False if (search_result is None) else True
        coll_to_insert = collRepo_accepted  #chosen collection to ingest 
        log_msg = f"{log_msg} ACCPTED"
    else:
        coll_to_insert = collRepo_discard
        log_msg = f"{log_msg} DISCARDED"

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

    logging.info(f"{datetime.now()} {log_msg}")

def conversion(document:dict):
    file_path:str = "{}_{}_{}_{}_{}".format(document['repo_language'], document['repo_extension'], document['repo_author'], document['repo_name'], document['path'])
    file_path = file_path.replace("/",".")

    #convert content to base64
    content_b64 = document['content']
    content_b64bytes = content_b64.encode('utf-8')
    content_bytes = base64.b64decode(content_b64bytes)
    content = content_bytes.decode('utf-8')
        
    search_result = "n"

    if document['repo_language'] == 'Python':
        search_expression = eval(config.get('expression', 'search_python'))
        search_result = re.search(search_expression, content)
    elif document['repo_language'] == 'qsharp':
        search_expression = eval(config.get('expression', 'search_qsharp'))
        search_result = re.search(search_expression, content)
                
    if search_result is None:
        dir_path = dir_code_discard
        insert(document, content, file_path, True) #set if this doccument is going to be discarded
    else: 
        dir_path = dir_code
        insert(document, content, file_path, False)

    dir_path = os.path.join(dir_path, document['repo_language'])

    if document['repo_extension'] is not None:
        dir_path = os.path.join(dir_path, document['repo_extension'])
        
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_path)
        
    if len(file_path) >= max_path_length:
        file_path_format = "."+file_path.split(".")[-1] #get the text from the last point to the right part of the text (".py")
        length_cut = 255 - len(file_path_format)
        file_path = file_path[:length_cut] #cut to (max size - count the characters above the string
        file_path = file_path+file_path_format #previously put the string in the last part

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(content)

def getCode (language, extension):
    global contadorglobal
    plus_extension_clause = ''
    extension_clause_plus = ''
    
    if extension is not None:
        plus_extension_clause = '+'+extension
        extension_clause_plus = extension+'+'

    for year in range(date.today().year, year_from-1, -1):  #iterate over years (to split search results under 1000 hits)
        print("Year: {}, language: {}, extension:{}".format(year, language, extension))    
                
        for pagina_repo in range(1, max_search_pages+1):    #iterate over repositories by page results
            repo_url = search_repo_url.format(repo_search_in + plus_extension_clause +'+language:'+language, year, year, pagina_repo)
            
            checkWaitRateLimit('search')
            session1 = requests.Session()
            retry1 = Retry(connect=100, backoff_factor=0.5)
            adapter1 = HTTPAdapter(max_retries=retry1)
            session1.mount('http://', adapter1)
            session1.mount('https://', adapter1)
            r = session1.get(repo_url, headers=headers)
            #r = requests.get(repo_url, headers=headers)

            search_dict = r.json()               
            repos = None    #used to later store repositories which were returned

            if 'total_count' in search_dict and 'items' in search_dict: #way to know if the request returned as expected       
                totalRepos = search_dict['total_count']
                repos = search_dict['items']
            
                if len(repos)==0:
                    break   #there are no more repo results, stop searching pages and continue years loop
            else:
                break   #there is no more pages or any other gitHub API error, stop searching pages and continue years loop     
            
            for repo in repos:  #iterate over every repository result
                repo_full_name = repo['full_name']
                repo_name = repo['name']
                repo_owner = repo['owner']['login']
                repo_creation_date = repo['created_at']
                print("Actual repository: ",repo_full_name," Page repository: ",pagina_repo)

                for pagina_codigo in range(1, max_search_pages+1):    #iterate by code page
                    if extension is not None:
                        extension_clause = '+'+extension

                    code_url = search_code_url.format(extension_clause_plus+'+' + 'in:file+language:{}+repo:{}'.format(language,repo_full_name), pagina_codigo)                    
                    
                    checkWaitRateLimit('code_search')
                    session2 = requests.Session()
                    retry2 = Retry(connect=100, backoff_factor=0.5)
                    adapter2 = HTTPAdapter(max_retries=retry2)
                    session2.mount('http://', adapter2)
                    session2.mount('https://', adapter2)
                    c = session2.get(code_url, headers=headers)
                    #c = requests.get(code_url, headers=headers)
                    code_dict = c.json()
                    
                    if 'total_count' in code_dict and 'items' in code_dict:  #way to know if the request returned as expected  
                        totalCodefiles = code_dict["total_count"]
                        codefiles = code_dict['items']
                    else:                    
                        break   #there is no more code pages or any other gitHub API error, stop searching code pages and continue pages loop
                        
                    for code in codefiles:  #iterate over every code result
                        code_path = quote(code['path']) #convert code path to URL-friendly
                        content_deep_url = content_url.format(repo_full_name, code_path)
                    
                        checkWaitRateLimit('core')
                        session3 = requests.Session()
                        retry3 = Retry(connect=100, backoff_factor=0.5)
                        adapter3 = HTTPAdapter(max_retries=retry3)
                        session3.mount('http://', adapter3)
                        session3.mount('https://', adapter3)
                        p = session3.get(content_deep_url, headers=headers)
                        #p = requests.get(content_deep_url, headers=headers)
                        answer = p.json()

                        #Files attributes in MongoDB
                        answer['repo_name'] = repo_name
                        answer['repo_author'] = repo_owner
                        answer['repo_creation_date'] = repo_creation_date
                        answer['repo_language'] = language
                        answer['repo_extension'] = extension
                        sha = str(p.json()['sha'])
                        
                        if collRepo.find_one({'sha' : sha}) == None:    #Check if there are duplicate files
                            collRepo.insert_one(answer) #inserts the commits
                        
                        
                        
                        logging.info(f"{datetime.now()} {language}.{extension}, {year} - page:{pagina_repo}, {repo_owner}/{repo_name} | {answer['path']} has been ingested")
                        contadorglobal+=1

languages = config.get('languages', 'languages')
languages = ast.literal_eval(languages)
initial_time = time.time()

initializeDirs()

if len(languages) <2:
    True
elif len(languages) ==2:
    getCode(languages[0], languages[1])
else:
    for l in languages:
        getCode(l[0], l[1])

final_time = time.time()
total_time = (final_time-initial_time)/3600

print("Execution time: ",total_time, "hours")