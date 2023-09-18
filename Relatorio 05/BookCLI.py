class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self,name,function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Please try again.")


class LivroModel:
    def __init__(self, database):
        self.db = database
        self.collection = self.db["Livros"]

    def create_livro(self, titulo: str, autor: str, ano: int, preco: float):
        try:
            livro = {
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "preco": preco
            }
            res = self.collection.insert_one(livro)
            print(f"Livro created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating livro: {e}")
            return None

    def read_livro_by_id(self, id: str):
        try:
            res = self.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading livro: {e}")
            return None

    def update_livro(self, id: str, titulo: str, autor: str, ano: int, preco: float):
        try:
            livro_data = {
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "preco": preco
            }
            res = self.collection.update_one({"_id": ObjectId(id)}, {"$set": livro_data})
            print(f"Livro updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating livro: {e}")
            return None

    def delete_livro(self, id: str):
        try:
            res = self.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting livro: {e}")
            return None
