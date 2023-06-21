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

headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

contadorglobal = 0

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

def obtenerCodigo (language, extension):
    global contadorglobal

    for ano_repo in range(2015, (date.today().year)+1):
        print(ano_repo)    
        pagina_repo=1
        
        while(1):
            if extension is None:
                repo_url = search_repo_url.format('language:'+language, ano_repo, ano_repo, pagina_repo)
            else:
                repo_url = search_repo_url.format('in:readme+in:name+in:description+in:topics+'+extension+'+language:'+language, ano_repo, ano_repo, pagina_repo)
            
            contadorReintentosRepo = 0
            
            while True:
                search_dict = ''
                try:
                    checkWaitRateLimit('search')
                    r = requests.get(repo_url, headers=headers)
                    search_dict = r.json()            
                    totalRepos = search_dict['total_count']
                    repos = search_dict['items']
                except Exception:
                    contadorReintentosRepo+=1
                    
                    if contadorReintentosRepo==30:
                        print("Buscando repositorios, demasiados errores entonces se detiene el programa")
                        with open('erroresBusquedaRepo.txt', 'w') as f:
                            f.write('search_dict = ' + str(search_dict) + '\n') 
                        exit(1)
                        
                    print("Ha ocurrido un error en la busqueda de respositorios, vuelve a intentar ",contadorReintentosRepo)
                    sleep(2)
                    continue
                
                break
            
            if repos is None or len(repos)==0:
                break
            else:
                pagina_repo+=1
            
            for repo in repos:
                repo_full_name = repo['full_name']
                repo_name = repo['name']
                repo_owner = repo['owner']['login']
                print("Repo actual: ",repo_full_name," Pagina repos: ",pagina_repo-1)
                pagina_codigo=1
                
                while(1):
                    if extension is None:
                        code_url = search_code_url.format('language:{}+repo:{}'.format(language,repo_full_name), pagina_codigo)
                    else:
                        code_url = search_code_url.format('{}+in:file+language:{}+repo:{}'.format(extension,language,repo_full_name), pagina_codigo)
                    
                    contadorReintentosCode = 0
                    while True: #para capturar el error y que lo vuelva a intentar
                        code_dict = ''
                        try:
                            checkWaitRateLimit('code_search')
                            c = requests.get(code_url, headers=headers)
                            code_dict = c.json()
                            totalCodefiles = code_dict["total_count"]
                            codefiles = code_dict['items']
                        except Exception:
                            contadorReintentosCode+=1
                    
                            if contadorReintentosCode==30:
                                print("Buscando codigo, demasiados errores entonces se detiene el programa")
                                with open('erroresBusquedaCode.txt', 'w') as f:
                                    f.write('code_dict = ' + str(code_dict) + '\n') 
                                raise
                                
                            print("Ha ocurrido un error en la busqueda de codigo, vuelve a intentar ",contadorReintentosCode)
                            sleep(2)
                            continue

                        break
                            
                    if codefiles is None or len(codefiles)==0:
                        break 
                    else:
                        pagina_codigo+=1
                    
                    if pagina_codigo == 11: #solo se permiten 1000 items
                        break

                    for code in codefiles:
                        code_path = quote(code['path'])
                        content_deep_url = content_url.format(repo_full_name, code_path)
                        
                        contadorReintentosContent = 0
                        while True: #para capturar el error y que lo vuelva a intentar
                            respuesta = ''
                            try:
                                checkWaitRateLimit('core')
                                p = requests.get(content_deep_url, headers=headers)
                                respuesta = p.json()
                                respuesta['repo_name'] = repo_name
                                respuesta['repo_author'] = repo_owner
                                sha = str(p.json()['sha'])
                            except Exception:
                                contadorReintentosContent+=1
                    
                                if contadorReintentosContent==30:
                                    print("Buscando contenido de los archivos, demasiados errores entonces se detiene el programa")
                                    with open('erroresBusquedaContent.txt', 'w') as f:
                                        f.write('respuesta = ' + str(respuesta) + '\n') 
                                    raise
                                
                                print("Ha ocurrido un error en la busqueda de contenido de los archivos, vuelve a intentar ",contadorReintentosContent)
                                with open('erroresBusquedaContent.txt', 'w') as f:
                                    f.write('respuesta = ' + str(respuesta) + '\n')
                                sleep(2)
                                continue

                            break
                        
                        contadorReintentosInsertar = 0
                        while True:
                            try:
                                if collRepo.find_one({'sha' : sha}) == None:
                                    collRepo.insert_one(respuesta) #inserts the commits
                                    contadorglobal+=1
                                    
                            except Exception:
                                contadorReintentosInsertar+=1
                                if contadorReintentosInsertar==30:
                                    print("Buscando contenido de los archivos, demasiados errores entonces se detiene el programa")
                                    raise
                                print("Ha ocurrido un error al insertar, vuelve a intentar ",contadorReintentosInsertar)
                                sleep(2)
                                continue
                              
                            break
                                
languages = [('openqasm', None), ('qsharp', None), ('Python', 'qiskit'), ('Python', 'cirq'), ('Python', 'pytket'), ('Python', 'pennylane'), ('Python', 'pyquil'), ('Python', 'dwave'), ('Python', 'acqdp'), ('Python', 'braket'), ('Python', 'qcl'), ('Python', 'qml'), ('Python', 'strawberryfields')]

for l in languages:
    obtenerCodigo(l[0], l[1])

print(contadorglobal)