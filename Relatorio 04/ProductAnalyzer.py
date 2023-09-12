from pymongo import MongoClient

class ProductAnalyzer:
    def __init__(self, host='localhost', port=27017, database='mydb', collection='mycollection'):
        self.client = MongoClient(host, port)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def total_vendas_por_dia(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
        ]
        result = list(self.collection.aggregate(pipeline))
        return result

    def produto_mais_vendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]
        result = list(self.collection.aggregate(pipeline))
        return result[0] if result else None

    def cliente_que_mais_gastou(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]
        result = list(self.collection.aggregate(pipeline))
        return result[0] if result else None

    def produtos_quantidade_acima_de_um(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total_quantidade": {"$gt": 1}}}
        ]
        result = list(self.collection.aggregate(pipeline))
        return result
