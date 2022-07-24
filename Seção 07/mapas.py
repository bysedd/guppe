"""
Mapas ≥ Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {
    'jan': 100.00,
    'fev': 250.00,
    'mar': 400.00,
}
print(receita)

# Iterar sobre dicionários
for chave in receita:
    print(chave)
for chave in receita:
    print(receita[chave])
for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]:.2f}')

# Acessando as chaves
print(receita.keys())
for chave in receita.keys():  # É recomendável informar que você está trabalhando com a chave.
    print(receita[chave])

# Acessando os valores
print(receita.values())
for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
print(receita.items())
for chave, valor in receita.items():
    print(f'chave={chave}, valor={valor}')

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores TODOS OS inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
