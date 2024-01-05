import json

class Payloader():
    def __init__(self):
        with open('./payloads/collection_tables.json', 'r') as file:
            self.collection = json.load(file)
