
"""Ingest content from every repos at MongoDB 
"""

import ast
import configparser
import os
import time
from datetime import date, datetime
from time import sleep
from urllib.parse import quote
import requests
from pymongo import MongoClient

configuration_file =  os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)
token = eval(config.get('GitHub', 'token'))

#MongoDB
db_link = eval(config.get('MongoDB', 'db_link'))
db_name = eval(config.get('MongoDB', 'db_name'))
db_coll = eval(config.get('MongoDB', 'db_coll'))
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo = dbGithub[db_coll]

#URL and headers
search_repo_url = 'https://api.github.com/search/repositories?q={}+created:{}-01-01..{}-12-31&per_page=100&page={}'
search_code_url = 'https://api.github.com/search/code?q={}&per_page=100&page={}'
content_url = 'https://api.github.com/repos/{}/contents/{}'
limit_url = 'https://api.github.com/rate_limit'

contadorglobal = 0

repo_search_in = 'in:readme+in:name+in:description+in:topics'
max_search_pages = 10 #pagination with per_page = 100 
year_from = 2015

headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

def obtainConfiguration():
    return token, db_link, db_name, db_coll

def rateLimit(resource) -> tuple[int, datetime]:
    "Returns remaining requests left and the time when they are reset"
    r = requests.get(limit_url, headers=headers)
    rateLimit = r.json()
    remaining = rateLimit['resources'][resource]['remaining']
    reset = rateLimit['resources'][resource]['reset']
    resetDate = datetime.fromtimestamp(reset)
    return remaining, resetDate

def checkWaitRateLimit(resource):
    "Checks remaining requests left. If none, waits until rate-limit is reset"
    remaining, resetDate = rateLimit(resource)
    
    if remaining == 0:
        print("Esperando a que se reinicie el rate limit...")
        secondsToWait = (resetDate - datetime.now()).total_seconds()
        sleep(secondsToWait+10)

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
            r = requests.get(repo_url, headers=headers)

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
                    c = requests.get(code_url, headers=headers)
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
                        p = requests.get(content_deep_url, headers=headers)
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
                            contadorglobal+=1

languages = config.get('languages', 'languages')
languages = ast.literal_eval(languages)

for l in languages:
    initial_time = time.time()
    getCode(l[0], l[1])
    final_time = time.time()
    total_time = (final_time-initial_time)/3600

    print("Execution time: ",total_time, "hours")