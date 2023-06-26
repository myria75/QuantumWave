from datetime import datetime, date
from time import sleep
import requests
from pymongo import MongoClient
from urllib.parse import quote

token="123"
code_url = 'https://api.github.com/search/code?q={}&per_page=100&page={}'
headers = {
    'Accept': "application/vnd.github+json",
    'Authorization': "Bearer "+token,
    'X-Github-Api-Version': "2022-11-28"
}

def checkWaitRateLimit():
    print("true")

def intentarPeticion(rateType,url,codigo):
    contadorReintentosCode = 0
   
    while True: #para capturar el error y que lo vuelva a intentar
        response_json = ''
        try:
            checkWaitRateLimit(rateType)
            response = requests.get(url, headers=headers)
            response_json = response.json()
            return response_json
        except Exception:
            contadorReintentosCode+=1
                        
            if contadorReintentosCode==30:
                print("Buscando codigo, demasiados errores entonces se detiene el programa")
                with open('erroresBusquedaCode.txt', 'w') as f:
                    f.write('response_json = ' + str(response_json) + '\n') 
                raise
                                    
            print("Ha ocurrido un error en la busqueda de codigo, vuelve a intentar ",contadorReintentosCode)
            sleep(2)
            continue

        break