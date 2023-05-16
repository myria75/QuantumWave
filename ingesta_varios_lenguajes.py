from datetime import datetime
from time import sleep
import requests
from pymongo import MongoClient

token = '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'

#MongoDB
db_link = 'mongodb://localhost:27017'
db_name = 'codigo-cuantico'
connection = MongoClient(db_link)
dbGithub = connection[db_name]

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

def lenguages(language):
    language
    repo_url = search_repo_url.format(language)
    checkWaitRateLimit()
    r = requests.get(repo_url, headers=headers)
    search_dict = r.json()
    search_dict = search_dict['items']

    for repo in search_dict:
        name = repo['full_name']
        collCommits = dbGithub[name]
        code_url = search_code_url.format(language+'+repo:'+name)

        checkWaitRateLimit()
        c = requests.get(code_url, headers=headers)
        code_dict = c.json()
        code_dict = code_dict['items']

        for code in code_dict:
            code_path = code['path']
            content_deep_url = content_url.format(name, code_path)
            checkWaitRateLimit()
            p = requests.get(content_deep_url, headers=headers)
            collCommits.insert_one(p.json()) #inserts the commits

#lenguages('language:openqasm')
#lenguages('language:Q#')
#lenguages('in:readme qiskit language:python')
