
# Exemplo de dicionaário com estoque e operações de venda
# Página 128 do livro.
venda = []
estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50],
           "arroz": [200, 10.50],
           "limão": [1800, 2.10]}
# o nome do produto é a chave do dicionario
# e a lista consiste nos valores associados
# uma lista por chaves
# o 1º elemento da lista é a quant. disponivel,
# o 2º é o preço do produto.


print("\n __ SEJA BEM-VINDOS AO HORTIFRUT __")
print("| PRODUTO          QUANT     PREÇO |")
for chave, dados in estoque.items():
    print(f"| {chave:10s}{dados[0]:12}{dados[1]:10.2f} |")
print("|________ O QUE TEMOS HOJE ________|")

print("O que você vai querer?")
print("digite 'sair' para concluir")


while True:
    pedido = str(
        input("Digite o nome do produto: "))
    if pedido == "sair":
        break
    else:
        if pedido not in estoque:
            print("\nNão temos esse produto!, digite corretamente.\n")
        else:
            quantidadeVenda = int(input("Quantidade: "))
            print()
            venda.append((pedido, quantidadeVenda))


total = 0
quantidade = 0

print("\n ___________ NOTA FISCAL ___________")
for operação in venda:
    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(
        f"| {produto:10s}: {quantidade:3d} X {preço:6.2f} = {custo:6.2f} |")
    estoque[str(produto)][0] -= quantidade
    total = total + custo
print("|                                   |")
print(f"| Custo total: {total:20.2f} |")
print("|___________________________________|")


print("\n      ______ EM ESTOQUE ______")
print("     | PRODUTO          QUANT |")
for chave, dados in estoque.items():
    print(f"     | {chave:10s}{dados[0]:12} |")
print("     |________________________|\n")
