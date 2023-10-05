class MotoristaCLI:
    def __init(self, motorista_dao):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("\n--- Menu ---")
            print("1- Criar Motorista")
            print("2- Ler Motoristas")
            print("3- Atualizar Motorista")
            print("4- Apagar Motorista")
            print("5- Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_motorista()
            elif opcao == "2":
                self.ler_motoristas()
            elif opcao == "3":
                self.atualizar_motorista()
            elif opcao == "4":
                self.deletar_motorista()
            elif opcao == "5":
                print("Saindo...")
                break
            else:
                print("opcao invalida.")

    def criar_motorista(self):
        nome = input("nome do Motorista: ")
        nota = float(input("nota do Motorista: "))
        self.motorista_dao.criar_motorista({"nome": nome, "nota": nota})
        print("Motorista criado")

    def ler_motoristas(self):
        motoristas = self.motorista_dao.ler_motoristas()
        for motorista in motoristas:
            print(f"Nome: {motorista['nome']}, Nota: {motorista['nota']}")

    def atualizar_motorista(self):
        nome = input("Nome do Motorista a ser atualizado: ")
        nova_nota = float(input("Nova nota do Motorista: "))
        self.motorista_dao.atualizar_motorista(nome, nova_nota)
        print("Motorista atualizado")

    def deletar_motorista(self):
        nome = input("Nome do Motorista a ser apagadol: ")
        self.motorista_dao.deletar_motorista(nome)
        print("Motorista apagado")