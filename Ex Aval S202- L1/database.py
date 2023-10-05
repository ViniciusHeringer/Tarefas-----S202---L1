from pymongo import MongoClient

class Database:
    def __init__(self, db_name, Motoristas):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[atlas-cluster]
        self.motoristas = self.db[Motoristas]
