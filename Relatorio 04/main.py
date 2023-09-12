from database import Database
from product_analyzer import ProductAnalyzer


def main():
    db = Database(database="mercado", collection="produtos")
    db.resetDatabase()

    analisador = ProductAnalyzer(database="mercado", collection="produtos")

    total_vendas_por_dia = analisador.total_vendas_por_dia()
    print("Total de Vendas por Dia:")
    for item in total_vendas_por_dia:
        print(item)

    produto_mais_vendido = analisador.produto_mais_vendido()
    print("\nProduto Mais Vendido:")
    if produto_mais_vendido:
        print(produto_mais_vendido)
    else:
        print("Nenhum produto encontrado.")

    cliente_que_mais_gastou = analisador.cliente_que_mais_gastou()
    print("\nCliente que Mais Gastou:")
    if cliente_que_mais_gastou:
        print(cliente_que_mais_gastou)
    else:
        print("Nenhum cliente encontrado.")

    produtos_quantidade_acima_de_um = analisador.produtos_quantidade_acima_de_um()
    print("\nProdutos com Quantidade Acima de Um:")
    for item in produtos_quantidade_acima_de_um:
        print(item)