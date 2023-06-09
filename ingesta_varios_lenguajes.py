from datetime import datetime
from time import sleep
import requests
from pymongo import MongoClient

token = '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'

#MongoDB
db_link = 'mongodb://localhost:27017'
db_name = 'Repositories'
connection = MongoClient(db_link)
dbGithub = connection[db_name]
collRepo = dbGithub['Documents']

#URL and headers
search_repo_url = 'https://api.github.com/search/repositories?q={}&per_page=100&page={}'
search_code_url = 'https://api.github.com/search/code?q={}&per_page=100&page={}'
content_url = 'https://api.github.com/repos/{}/contents/{}'
limit_url = 'https://api.github.com/rate_limit'

headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

contadorglobal = 0

def rateLimit() -> tuple[int, datetime]:
    "Returns remaining requests left and the time when they are reset"
    r = requests.get(limit_url, headers=headers)
    rateLimit = r.json()
    remaining = rateLimit['resources']['core']['remaining']
    reset = rateLimit['resources']['core']['reset']
    resetDate = datetime.fromtimestamp(reset)
    return remaining, resetDate

def checkWaitRateLimit():
    "Checks remaining requests left. If none, waits until rate-limit is reset"
    remaining, resetDate = rateLimit()
    
    if remaining == 0:
        print("Esperando a que se reinicie el rate limit...")
        secondsToWait = (resetDate - datetime.now()).total_seconds()
        sleep(secondsToWait+10)

def obtenerCodigo (language, extension):
    global contadorglobal
    pagina_repo=1
    
    while(1):
        if extension is None:
            repo_url = search_repo_url.format('language:'+language, pagina_repo)
        else:
            repo_url = search_repo_url.format('in:readme+in:name+in:description+in:topics+'+extension+'+language:'+language, pagina_repo)
        print(repo_url)
        checkWaitRateLimit()
        r = requests.get(repo_url, headers=headers)
        search_dict = r.json()
        totalRepos = search_dict['total_count']
        repos = search_dict['items']

        
        if repos is None or len(repos)==0:
            break
        else:
            pagina_repo+=1
        
        for repo in repos:
            repo_full_name = repo['full_name']
            repo_name = repo['name']
            repo_owner = repo['owner']['login']
            print("Repo actual: ",repo_full_name," pagina: ",pagina_repo-1)
            pagina_codigo=1
            
            while(1):
                if extension is None:
                    code_url = search_code_url.format('language:{}+repo:{}'.format(language,repo_full_name), pagina_codigo)
                else:
                    code_url = search_code_url.format('{}+in:file+language:{}+repo:{}'.format(extension,language,repo_full_name), pagina_codigo)
                print(code_url)
                checkWaitRateLimit()
                c = requests.get(code_url, headers=headers)
                code_dict = c.json()
                totalCodefiles = code_dict["total_count"]
                codefiles = code_dict['items']

                if codefiles is None or len(codefiles)==0:
                    break 
                else:
                    pagina_codigo+=1


                for code in codefiles:
                    code_path = code['path']
                    content_deep_url = content_url.format(repo_full_name, code_path)
                    print(content_deep_url)
                    checkWaitRateLimit()
                    p = requests.get(content_deep_url, headers=headers)
                    respuesta = p.json()
                    respuesta['repo_name'] = repo_name
                    respuesta['repo_author'] = repo_owner
                    sha = str(p.json()['sha'])
                    
                    if collRepo.find_one({'sha' : sha}) == None:
                        collRepo.insert_one(respuesta) #inserts the commits
                        contadorglobal+=1
            
languages = [('openqasm', None), ('qsharp', None), ('Python', 'qiskit'), ('Python', 'cirq'), ('Python', 'pytket'), ('Python', 'pennylane'), ('Python', 'pyquil'), ('Python', 'dwave'), ('Python', 'acqdp'), ('Python', 'braket'), ('Python', 'qcl'), ('Python', 'qml'), ('Python', 'strawberryfields')]

for l in languages:
    obtenerCodigo(l[0], l[1])

print(contadorglobal)