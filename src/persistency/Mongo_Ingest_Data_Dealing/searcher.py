
"""Searches for codes
"""

import configparser
import os
from datetime import datetime
from time import sleep
import requests

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)
token = eval(config.get('GitHub', 'token'))

#URL and headers
search_repo_url = 'https://api.github.com/search/repositories?q={}'
search_code_url = 'https://api.github.com/search/code?q={}'
content_url = 'https://api.github.com/repos/{}/contents/{}'
limit_url = 'https://api.github.com/rate_limit'

headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

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

def resultadosEncontrados(language, extension):
    if extension is None:
        repo_url = search_repo_url.format('language:'+language)
    else:
        repo_url = search_repo_url.format('in:readme+'+extension+'+language:'+language)
        
    checkWaitRateLimit()
    r = requests.get(repo_url, headers=headers)
    search_dict = r.json()
    
    totalRepos = search_dict['total_count']
    return int(totalRepos)

languages = [('openqasm', None), ('qsharp', None), ('Python', 'qiskit'), ('Python', 'cirq'), ('Python', 'pytket'), ('Python', 'pennylane'), ('Python', 'pyquil'), ('Python', 'dwave'), ('Python', 'acqdp'), ('Python', 'braket'), ('Python', 'qcl'), ('Python', 'qml'), ('Python', 'strawberryfields')]

for l in languages:
    print("language:{}, extension:{}: {}".format(l[0], l[1], resultadosEncontrados(l[0], l[1])))