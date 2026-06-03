import json

with open("config.json") as file:
    config = json.load(file)

def get_config():
    return config
