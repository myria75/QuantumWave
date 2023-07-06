from datetime import datetime, date
from time import sleep
import requests
from pymongo import MongoClient
from urllib.parse import quote

token = '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'

#MongoDB
db_link = 'mongodb://localhost:27017'
db_name = 'repositories'
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo = dbGithub['documents']

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

def rateLimit(resource) -> tuple[int, datetime]:
    "Returns remaining requests left and the time when they are reset"
    #r = requests.get(limit_url, headers=headers) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    r = peticion(limit_url, None)
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

def peticion(url, rateLimitType):
    for intento in range(0, 31):
        try:
            if rateLimitType != None: checkWaitRateLimit(rateLimitType)
            r = requests.get(url, headers=headers) #hacer peticion
        except Exception as err:
            if intento == 30:
                raise err
            else:
                print("Intento:{}, rateLimit: {}".format(intento, rateLimitType))
                continue
        break
    return r    

def obtenerCodigo (language, extension):
    global contadorglobal
    plus_extension_clause = ''
    extension_clause_plus = ''
    
    if extension is not None:
        plus_extension_clause = '+'+extension
        extension_clause_plus = extension+'+'

#(day.today().year)
    for year in range(2019, year_from-1, -1): #iterate over year (to split search results under 1000 hits)
        print("Año: {}, language: {}, extension:{}".format(year, language, extension))    
                
        for pagina_repo in range(1, max_search_pages+1): #iterate over repositories by page results
            repo_url = search_repo_url.format(repo_search_in + plus_extension_clause +'+language:'+language, year, year, pagina_repo)
            
            #checkWaitRateLimit('search') !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #r = requests.get(repo_url, headers=headers) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            r = peticion(repo_url, 'search')

            search_dict = r.json()               
            repos = None

            if 'total_count' in search_dict and 'items' in search_dict:         
                totalRepos = search_dict['total_count']
                repos = search_dict['items']
            
                if len(repos)==0:
                    break   # there are no more repo results
            else:
                break  # there is no more pages or any other gitHub API error        
            
            for repo in repos: #iterate over every repository result
                repo_full_name = repo['full_name']
                repo_name = repo['name']
                repo_owner = repo['owner']['login']
                repo_creation_date = repo['created_at']
                print("Repo actual: ",repo_full_name," Pagina repos: ",pagina_repo)

                for pagina_codigo in range(1, max_search_pages+1):    #iterate by code page
                    if extension is not None:
                        extension_clause = '+'+extension

                    code_url = search_code_url.format(extension_clause_plus+'+' + 'in:file+language:{}+repo:{}'.format(language,repo_full_name), pagina_codigo)                    
                    
                    #checkWaitRateLimit('code_search') !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    #c = requests.get(code_url, headers=headers) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    c = peticion(code_url, 'code_search')
                    code_dict = c.json()
                    
                    if 'total_count' in code_dict and 'items' in code_dict:
                        totalCodefiles = code_dict["total_count"]
                        codefiles = code_dict['items']
                    else:                    
                        break
                        
                    for code in codefiles:
                        code_path = quote(code['path'])
                        content_deep_url = content_url.format(repo_full_name, code_path)
                    
                        #checkWaitRateLimit('core') !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        #p = requests.get(content_deep_url, headers=headers) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        p = peticion(content_deep_url, 'core')
                        respuesta = p.json()
                        respuesta['repo_name'] = repo_name
                        respuesta['repo_author'] = repo_owner
                        respuesta['repo_creation_date'] = repo_creation_date
                        respuesta['repo_language'] = language
                        respuesta['repo_extension'] = extension
                        sha = str(p.json()['sha'])
                        if collRepo.find_one({'sha' : sha}) == None:
                            collRepo.insert_one(respuesta) #inserts the commits
                            contadorglobal+=1


#languages = [('Python', 'cirq'), ('Python', 'pytket'), ('Python', 'pennylane'), ('Python', 'pyquil'), ('Python', 'dwave'), ('Python', 'acqdp'), ('Python', 'braket'), ('Python', 'qcl'), ('Python', 'qml'), ('Python', 'strawberryfields')]

#('openqasm', None), ('qsharp', None), 
languages = [('Python', 'qiskit')]
for l in languages:
    obtenerCodigo(l[0], l[1])