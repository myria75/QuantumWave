import pandas as pd
import requests
from datetime import date, datetime
from time import sleep
import requests
from requests.adapters import Retry, HTTPAdapter

token = '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'

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-Github-Api-Version": "2022-11-28"
}

def rateLimit(resource) -> tuple[int, datetime]:
    "Returns remaining requests left and the time when they are reset"
    session = requests.Session()
    retry = Retry(connect=100, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    r = session.get('https://api.github.com/rate_limit', headers=headers)
    rateLimit = r.json()
    remaining = rateLimit['resources'][resource]['remaining']
    reset = rateLimit['resources'][resource]['reset']
    resetDate = datetime.fromtimestamp(reset)
    return remaining, resetDate

def checkWaitRateLimit(resource):
    "Checks remaining requests left. If none, waits until rate-limit is reset"
    remaining, resetDate = rateLimit(resource)
    
    if remaining == 0:
        secondsToWait = (resetDate - datetime.now()).total_seconds()
        
        if secondsToWait < 0:
            secondsToWait = 0

        sleep(secondsToWait+10)

# Función para obtener el año de creación del archivo directamente del repo
def get_file_year(author, repo):
    checkWaitRateLimit('core')
    url = f"https://api.github.com/repos/{author}/{repo}" #https://api.github.com/repos/qiskit-community/qiskit-machine-learning
    session2 = requests.Session()
    retry2 = Retry(connect=100, backoff_factor=0.5)
    adapter2 = HTTPAdapter(max_retries=retry2)
    session2.mount('http://', adapter2)
    session2.mount('https://', adapter2)
    response = session2.get(url, headers=headers)
    
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info["created_at"][:4]

    return -1 #si llega aquí, el repo no se encontró (posible motivo: autor lo borró o privatizó)

df = pd.read_csv('dataset_qiskit_20240926.csv', delimiter=';')

df.insert(df.columns.get_loc('circuit'), 'year', None)

for index, row in df.iterrows():
    author = row['author']
    repo = row['name']

    year = get_file_year(author, repo)
    print(year)

    df.at[index, 'year'] = year

df.to_csv('archivo_actualizado.csv', index=False, sep=';')

