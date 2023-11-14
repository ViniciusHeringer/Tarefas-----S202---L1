from query import Database, TeacherCRUD

class CLI:
    def __init__(self):
        self.database = None
        self.teacher_crud = None

    def connect_to_database(self, uri, user, password):
        self.database = Database(uri, user, password)
        self.teacher_crud = TeacherCRUD(self.database)

    def print_menu(self):
        print("\nMenu:")
        print("1. Criar")
        print("2. Ler")
        print("3. Atualizar CPF")
        print("4. Deletar")
        print("5. Sair")

    def run(self):
        print("Bem-vindo ao CLI")
        uri = input("Digite o URI do Neo4j: ")
        user = input("Digite o nome de usuário do Neo4j: ")
        password = input("Digite a senha do Neo4j: ")

        self.connect_to_database(uri, user, password)

        while True:
            self.print_menu()
            choice = input("Escolha uma opção: ")

            if choice == '1':
                name = input("Digite o nome: ")
                ano_nasc = input("Digite o ano de nascimento: ")
                cpf = input("Digite o CPF: ")
                self.teacher_crud.create(name, ano_nasc, cpf)

            elif choice == '2':
                name = input("Digite o nome: ")
                result = self.teacher_crud.read(name)
                print(result)

            elif choice == '3':
                name = input("Digite o nome: ")
                new_cpf = input("Digite o novo CPF: ")
                self.teacher_crud.update(name, new_cpf)

            elif choice == '4':
                name = input("Digite o nome do Professor que deseja deletar: ")
                self.teacher_crud.delete(name)

            elif choice == '5':
                print("Encerrando o programa. Até mais!")
                break

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()