import copy

# Lista original de produtos
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Criando uma cópia profunda da lista
copia = copy.deepcopy(produtos)

# Aumentando os preços em 10% (usando multiplicação por 1.1 ao invés de soma)
print('Preços aumentados em 10%:')
for produto in copia:
    produto['preco'] *= 1.1  # Mais conciso que preco + preco * 1.10
    print(f"{produto['nome']}: R${produto['preco']:.2f}")

# Opcional: Se quiser comparar com os preços originais
print('\nPreços originais para comparação:')
for produto in produtos:
    print(f"{produto['nome']}: R${produto['preco']:.2f}")