import time
import pymongo
import json

from github import Github
from pymongo import MongoClient

# First create a Github instance using an access token
g = Github("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")

# Mongo connection
client = pymongo.MongoClient("mongodb+srv://luis2411:github@githubcontacts.bdpumsq.mongodb.net/?retryWrites=true&w=majority")

collection_repos = client["contacts"]["repos"]

def searchOwnerInDb(mail):
    element = collection_repos.find_one({"owner mail" : mail})
    return element

def queryJson(code, language):
    data = {}
    data['language'] = language
    data['url'] = code.html_url
    data['owner'] = code.owner.login
    data['owner mail'] = code.owner.email
    return data

def searchRepo(querySearch, language):
    repo = g.search_repositories(query=querySearch)
    for code in repo:
        core_rate_limit = g.get_rate_limit().core
        commits =  code.get_commits()
        if(core_rate_limit.limit < 10):
            print(core_rate_limit)
            print('Waiting for rate limit...')
            time.sleep(3600)

        if commits.totalCount > 1 and code.owner.email!= None:
            if(searchOwnerInDb(code.owner.email)==None):
                data = queryJson(code, language)
                collection_repos.insert_one(data)

# Repositorios Q#
searchRepo('language:Q#', 'Q#')

# Repositorios OpenQASM
searchRepo('language:openqasm', 'OpenQASM')

# Repositorios qiskit
searchRepo('in:readme qiskit language:python', 'Qiskit')

# Repositorios cirq
searchRepo('in:readme cirq language:python', 'Cirq')

# Repositorios Silq
searchRepo('in:readme silq', 'Silq')

# Repositorios Pytket
searchRepo('in:readme pytket language:python', 'Pytket')

# Repositorios Pennylane
searchRepo('in:readme pennylane language:python', 'Pennylane')

# Repositorios Forest SDK
searchRepo('in:readme pyquil language:python', 'Forest SDK')

# Repositorios DWave-Ocean
searchRepo('in:readme dwave language:python', 'D-Wave Ocean')

print("Consiguiendo contactos de Alibaba")
# Repositorios Alibaba
searchRepo('in:readme acqdp language:python', 'Alibaba')

print("Consiguiendo contactos de Braket")
# Repositorios Braket AWS
searchRepo('in:readme braket language:python', 'Braket AWS')

print("Consiguiendo contactos de QCL")
# Repositorios Quantum Computing Language
searchRepo('in:readme qcl language:python', 'QCL')

print("Consiguiendo contactos de QML")
# Repositorios Quantum Machine Learning
searchRepo('in:readme qml language:python', 'QML')

print("Consiguiendo contactos de Strawberry Fields")
# Repositorios Strawberry Fields
searchRepo('in:readme strawberryfields language:python', 'Strawberry Fields')
