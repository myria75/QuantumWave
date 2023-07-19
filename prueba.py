import configparser
import ast

def readLanguages():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    languages = config.get('languages', 'languages')
    languages = ast.literal_eval(languages)
    print(languages[0])

def obtainConfiguration():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    token = config.get('expresion', 'search_python')

    print(eval(token))

obtainConfiguration()