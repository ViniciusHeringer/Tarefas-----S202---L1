from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.graph = Graph(uri, auth=(user, password))
        self.matcher = NodeMatcher(self.graph)

    def busca_renzo(self):
        query = (
            "MATCH (t:Teacher{name:'Renzo'}) "
            "RETURN t.ano_nasc, t.cpf"
        )
        result = self.graph.run(query)
        return result.data()

    def busca_prof_inicial_m(self):
        query = (
            "MATCH (t:Teacher) "
            "WHERE t.name STARTS WITH 'M' "
            "RETURN t.name, t.cpf"
        )
        result = self.graph.run(query)
        return result.data()

    def busca_todas_cidades(self):
        query = (
            "MATCH (c:City) "
            "RETURN c.name"
        )
        result = self.graph.run(query)
        return result.data()

    def busca_escolas_n(self):
        query = (
            "MATCH (s:School) "
            "WHERE s.number >= 150 AND s.number <= 550 "
            "RETURN s.name, s.address, s.number"
        )
        result = self.graph.run(query)
        return result.data()

    def prof_jovem_velho(self):
        query = (
            "MATCH (t:Teacher) "
            "WITH MIN(t.ano_nasc) AS mais_jovem, MAX(t.ano_nasc) AS mais_velho "
            "RETURN mais_jovem, mais_velho"
        )
        result = self.graph.run(query)
        return result.data()

    def media_pop_all(self):
        query = (
            "MATCH (c:City) "
            "WITH AVG(c.population) AS media_populacional "
            "RETURN media_populacional"
        )
        result = self.graph.run(query)
        return result.data()

    def troca_nome_a(self):
        query = (
            "MATCH (c:City{cep:'37540-000'}) "
            "WITH REPLACE(c.name, 'a', 'A') AS nome_modificado "
            "RETURN nome_modificado"
        )
        result = self.graph.run(query)
        return result.data()

    def prof_terc_letra(self):
        query = (
            "MATCH (t:Teacher) "
            "RETURN SUBSTRING(t.name, 3, 1) AS terceira_letra"
        )
        result = self.graph.run(query)
        return result.data()


class TeacherCRUD:
    def __init__(self, database):
        self.database = database

    def create(self, name, ano_nasc, cpf):
        query = (
            f"CREATE (:Teacher{{name:'{name}', ano_nasc:{ano_nasc}, cpf:'{cpf}'}})"
        )
        self.database.graph.run(query)

    def read(self, name):
        query = (
            f"MATCH (t:Teacher{{name:'{name}'}}) "
            "RETURN t"
        )
        result = self.database.graph.run(query)
        return result.data()

    def delete(self, name):
        query = (
            f"MATCH (t:Teacher{{name:'{name}'}}) "
            "DELETE t"
        )
        self.database.graph.run(query)

    def update(self, name, new_cpf):
        query = (
            f"MATCH (t:Teacher{{name:'{name}'}}) "
            f"SET t.cpf = '{new_cpf}'"
        )
        self.database.graph.run(query)



uri = "bolt://localhost:7687"
user = "neo4j"
password = "DX6eqiIIk5YWATVvMwX3EpI-h0_LYpB1irQw8mP7oxA"

database = Database(uri, user, password)
teacher_crud = TeacherCRUD(database)

#Resultados da questão 1 e questão 2
result_1 = database.busca_renzo()
print("Resultado da Consulta 1:", result_1)
result_2 = database.busca_prof_inicial_m()
print("Resultado da Consulta 2:", result_2)
result_3 = database.busca_todas_cidades()
print("Resultado da Consulta 3:", result_3)
result_4 = database.busca_escolas_n()
print("Resultado da Consulta 4:", result_4)
result_5 = database.prof_jovem_velho()
print("Resultado da Consulta 5:", result_5)
result_6 = database.media_pop_all()
print("Resultado da Consulta 6:", result_6)
result_7 = database.troca_nome_a()
print("Resultado da Consulta 7:", result_7)
result_8 = database.prof_terc_letra()
print("Resultado da Consulta 8:", result_8)

teacher_crud.create(name='Chris Lima', ano_nasc=1956, cpf='189.052.396-66')

result_read = teacher_crud.read(name='Chris Lima')
print("Resultado da Leitura (Read):", result_read)

teacher_crud.update(name='Chris Lima', new_cpf='162.052.777-77')

result_read_after_update = teacher_crud.read(name='Chris Lima')
print("Resultado da Leitura após Atualização:", result_read_after_update)
