class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def criar_motorista(self, motorista):
        self.db.motoristas.insert_one(motorista)

    def ler_motoristas(self):
        return list(self.db.motoristas.find())

    def ler_motorista_por_nome(self, nome):
        return self.db.motoristas.find_one({"nome": nome})

    def atualizar_motorista(self, nome, nova_nota):
        self.db.motoristas.update_one({"nome": nome}, {"$set": {"nota": nova_nota}})

    def deletar_motorista(self, nome):
        self.db.motoristas.delete_one({"nome": nome})
