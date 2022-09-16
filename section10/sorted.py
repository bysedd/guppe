"""
Sorted

OBS: não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

# OBS: o sorted(), SEMPRE retorna uma Lista com os elementos do iterável ordenados

# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)
print(sorted(numeros))  # Ordenar em ordem crescente
print(numeros)

numeros = [6, 1, 8, 2]
print(numeros)
print(tuple(sorted(numeros)))

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))  # Ordena em ordem decrescente

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'},
]

print('Ordenando pelo "username" — Ordem Alfabética Crescente:')
key = sorted(usuarios, key=lambda usuario: usuario['username'])
[print(user) for user in key]

print('\nOrdenando pelo número de "tweets"')
key = sorted(usuarios, key=lambda usuario: len(usuario['tweets']))
[print(user) for user in key]

"""

from random import randint as tocou

# Último exemplo

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': tocou(100000, 1000000)},
    {'titulo': 'Dead Skin Mask', 'tocou': tocou(100000, 1000000)},
    {'titulo': 'Back in Black', 'tocou': tocou(100000, 1000000)},
    {'titulo': "Too old to rock'in'roll, too young to die", 'tocou': tocou(100000, 1000000)}
]

print('Ordena da mais tocada à menos tocada:')
key = sorted(musicas, key=lambda msc: msc['tocou'], reverse=True)
[print(msc) for msc in key]

print('\nOrdena da menos tocada à mais tocada:')
key = sorted(musicas, key=lambda msc: msc['tocou'])
[print(msc) for msc in key]
