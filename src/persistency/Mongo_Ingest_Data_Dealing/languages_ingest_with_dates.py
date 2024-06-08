
"""Ingest content from every repos at MongoDB 
"""

import ast
import configparser
import os
import time
from datetime import date, datetime
import logging
from time import sleep
from urllib.parse import quote
import requests
from requests.adapters import Retry, HTTPAdapter
from pymongo import MongoClient
import re
import base64
import uuid

configuration_file =  os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)
token = eval(config.get('GitHub', 'token'))

#MongoDB
db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll_accepted = eval(config.get('MongoDB', 'db_coll_accepted'))
db_coll_discarded = eval(config.get('MongoDB', 'db_coll_discarded'))
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo_accepted = dbGithub[db_coll_accepted]
collRepo_discard = dbGithub[db_coll_discarded]

#URL and headers
search_repo_url = 'https://api.github.com/search/repositories?q={}+created:{}-{}-{}..{}-{}-{}&per_page=100&page={}'
search_code_url = 'https://api.github.com/search/code?q={}&per_page=100&page={}'
content_url = 'https://api.github.com/repos/{}/contents/{}'
limit_url = 'https://api.github.com/rate_limit'

contadorglobal = 0

repo_search_in = 'in:readme+in:name+in:description+in:topics'
max_search_pages = 10 #pagination with per_page = 100 
default_from_day = '01'
default_from_month = '01'
default_to_day = '31'
default_to_month = '12'
year_from = 2015

headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

def obtainConfiguration():
    return token, db_link, db_name

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
        
        if secondsToWait < 0:
            secondsToWait = 0

        sleep(secondsToWait+10)

def content_ingestion(code_url, language, extension, repo_full_name, repo_name, repo_owner, repo_creation_date, year, pagina_repo):
    global contadorglobal
    checkWaitRateLimit('code_search')
    session2 = requests.Session()
    retry2 = Retry(connect=100, backoff_factor=0.5)
    adapter2 = HTTPAdapter(max_retries=retry2)
    session2.mount('http://', adapter2)
    session2.mount('https://', adapter2)
    c = session2.get(code_url, headers=headers)
    #c = requests.get(code_url, headers=headers)
    code_dict = c.json()

    codefiles = None           
    if 'total_count' in code_dict and 'items' in code_dict:  #way to know if the request returned as expected  
        totalCodefiles = code_dict["total_count"]
        codefiles = code_dict['items']
    #else:                    
    #    break   #there is no more code pages or any other gitHub API error, stop searching code pages and continue pages loop
    if codefiles is not None:                    
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

            if obtainContentConversion(answer) == True:
                logging.info(f"{datetime.now()} {language}.{extension}, {year} - page:{pagina_repo}, {repo_owner}/{repo_name} | {answer['path']} has been ingested")
                contadorglobal+=1       

def obtainContentConversion(doc) -> bool:    
    file_path:str = "{}_{}_{}_{}_{}".format(doc['repo_language'], doc['repo_extension'], doc['repo_author'], doc['repo_name'], doc['path'])
    file_path = file_path.replace("/",".")

    #convert content to base64
    content_b64 = doc['content']
    content_b64bytes = content_b64.encode('utf-8')
    content_bytes = base64.b64decode(content_b64bytes)
    content = content_bytes.decode('utf-8')
        
    search_result = "n"

    if doc['repo_language'] == 'Python':
        search_expression = eval(config.get('expression', 'search_python'))
        search_result = re.search(search_expression, content)
    elif doc['repo_language'] == 'qsharp':
        search_expression = eval(config.get('expression', 'search_qsharp'))
        search_result = re.search(search_expression, content)

    hybrid:bool = False
    coll_to_insert = None

    log_msg = f"{doc['repo_language']}.{doc['repo_extension']}, {doc['repo_author']}/{doc['repo_name']} | {file_path} has been"

    if search_result is None:
        #Discarded
        coll_to_insert = collRepo_discard
        log_msg = f"{log_msg} DISCARDED"
        #insert(doc, content, file_path, True) #set if this doccument is going to be discarded
    else: 
        #Accepted, to check hybrid
        search_expression = eval(config.get('expression', 'search_hybrid'))
        search_result = re.search(search_expression, content)
        hybrid = False if (search_result is None) else True
        coll_to_insert = collRepo_accepted  #chosen collection to ingest 
        log_msg = f"{log_msg} ACCEPTED"
        #insert(doc, content, file_path, False)
    
    #json to ingest at MongoDB
    ingest = {
        "id": str(uuid.uuid4()),
        "sha": doc['sha'],
        "language": doc['repo_language'],
        "extension": doc['repo_extension'],
        "author": doc['repo_author'],
        "name": doc['repo_name'],
        "path": file_path, 
        "hybrid": hybrid, 
        "content": content
    }
    
    logging.info(f"{log_msg}")
    
    if coll_to_insert.find_one({'sha' : ingest['sha']}) == None:    #Check if there are duplicate files
        coll_to_insert.insert_one(ingest) #inserts the commits
        return True
    else:
        return False
    
def getCode (language, extension, filters, from_date: date, to_date: date):
    global contadorglobal
    plus_extension_clause = ''
    extension_clause_plus = ''
    
    if extension is not None:
        plus_extension_clause = '+'+extension
        extension_clause_plus = extension+'+'

    for year in range(to_date.year, from_date.year-1, -1):  #iterate over years (to split search results under 1000 hits)
        print("Year: {}, language: {}, extension:{}".format(year, language, extension))    
        
        query_fromDate_day = default_from_day
        query_fromDate_month = default_from_month
        query_toDate_day = default_to_day
        query_toDate_month = default_to_month

        if year == to_date.year:
            query_toDate_day = str(to_date.month).zfill(2)
            query_toDate_month = str(to_date.month).zfill(2)

        if year == from_date.year:
            query_fromDate_day = str(from_date.month).zfill(2)
            query_fromDate_month = str(from_date.month).zfill(2)
                
        for pagina_repo in range(1, max_search_pages+1):    #iterate over repositories by page results
            repo_url = search_repo_url.format(repo_search_in + plus_extension_clause +'+language:'+language, year, query_toDate_month, query_toDate_day, year, query_fromDate_month, query_fromDate_day, pagina_repo)
            
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

                    if filters is None:
                        code_url = search_code_url.format(extension_clause_plus+'+' + 'in:file+language:{}+repo:{}'.format(language,repo_full_name), pagina_codigo)                    
                        content_ingestion(code_url, language, extension, repo_full_name, repo_name, repo_owner, repo_creation_date, year, pagina_repo)
                    else:
                        for filter in filters:
                            code_url = search_code_url.format('"{}"+'.format(filter)+extension_clause_plus+'+' + 'in:file+language:{}+repo:{}'.format(language,repo_full_name), pagina_codigo)                    
                            content_ingestion(code_url, language, extension, repo_full_name, repo_name, repo_owner, repo_creation_date, year, pagina_repo)
                    
def doIngestion(languages, from_date: date, to_date: date):
    initial_time = time.time()

    for l in languages:
        lang_properties = config.get('languages', l)
        lang_properties = ast.literal_eval(lang_properties)
        getCode(lang_properties[0], lang_properties[1], lang_properties[2], from_date, to_date)
        
    final_time = time.time()
    total_time = (final_time-initial_time)/3600

    print("Execution time: ",total_time, "hours")