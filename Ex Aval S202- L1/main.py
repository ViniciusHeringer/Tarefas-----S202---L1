class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista:
    def __init__(self, nome, nota=0):
        self.nome = nome
        self.nota = nota
        self.corridas = []

    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)


if __name__ == "__main__":
    passageiro1 = Passageiro("Bonifacio", "123456")
    corrida1 = Corrida(5, 10.0, 15.0, passageiro1)

    passageiro2 = Passageiro("Bilu", "789012")
    corrida2 = Corrida(4, 8.0, 16.0, passageiro2)

    motorista = Motorista("Carlao")
    motorista.adicionar_corrida(corrida1)
    motorista.adicionar_corrida(corrida2)

    print(f"Nome do Motorista: {motorista.nome}")