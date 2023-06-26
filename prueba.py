from datetime import datetime, date
from time import sleep
import requests
from pymongo import MongoClient
from urllib.parse import quote

token = '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'

code_url = "https://api.github.com/search/code?q=repo:tensorflow/tensorflow&per_page=10&page=110"
limit_url = 'https://api.github.com/rate_limit'

headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

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

def peticion1(url, rateLimitType):
    for intento in range(0, 31):
        try:
            if rateLimitType != None: checkWaitRateLimit(rateLimitType)
            r = "hola"
            if intento < 5: raise Exception("Pues a cada quien")
            print("r={}".format(intento))
        except Exception as err:
            if intento == 30:
                raise err   
            else:
                print("Intento:{}".format(intento))
                continue
        break
    return r       

def peticion(url, rateLimitType):
    for intento in range(0, 31):
        try:
            if rateLimitType != None: checkWaitRateLimit(rateLimitType)
            r = "hola"
            if intento < 5: raise Exception("Pues a cada quien")
        except Exception as err:
            if intento==30:
                raise err
            else:
                print("Intento:{}".format(intento))
                continue       
    return r


print(rateLimit('core'))
