from datetime import datetime
from time import sleep
import requests
from pymongo import MongoClient

token = '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'

search_repo_url = 'https://api.github.com/search/repositories?q=openqasm&per_page=100&page=3'

headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

r = requests.get(search_repo_url, headers=headers)
search_dict = r.json()
search_dict = search_dict['items']

print(len(search_dict))