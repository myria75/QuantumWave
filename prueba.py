import configparser

config = configparser.ConfigParser(allow_no_value=True)
config.read('properties.ini')
items = str(config.items('Languages')[0])
items = eval(items)
for i in items:
    print(i)