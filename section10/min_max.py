"""
Min e Max

max() --> Retorna o maior valor em um iterável ou o maior de dois, ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.items()))

# Faça um programa que receba dois valores do usuário e mostre o maior
v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
print(f'O maior valor informado foi {max(v1, v2)}')

print(max(4, 67, 54))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'g'))
print(max(3.145, 5.789))
print(max('Geek University'))


min() --> Retorna o menor valor em um iterável ou o menor de dois, ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.items()))

# Faça um programa que receba dois valores do usuário e mostre o maior
v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
print(f'O menor valor informado foi {min(v1, v2)}')

print(min(4, 67, 54))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'g'))
print(min(3.145, 5.789))
print(min('Geek University'))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))  # Tim
print(min(nomes))  # Arya
print(max(nomes, key=len))  # Ollivander
print(min(nomes, key=len))  # Tim

"""

from random import randint as tocou

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': tocou(100000, 1000000)},
    {'titulo': 'Dead Skin Mask', 'tocou': tocou(100000, 1000000)},
    {'titulo': 'Back in Black', 'tocou': tocou(100000, 1000000)},
    {'titulo': "Too old to rock'in'roll, too young to die", 'tocou': tocou(100000, 1000000)}
]

mostPlayed = max(musicas, key=lambda msc: msc['tocou'])
lessPlayed = min(musicas, key=lambda msc: msc['tocou'])
print(mostPlayed)
print(lessPlayed, end='\n\n')

# DESAFIO! Imprima o título da música mais e menos tocada
print(f'Mais tocada: {mostPlayed["titulo"]}')
print(f'Menos tocada: {lessPlayed["titulo"]}\n')

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?
maior, menor = musicas[0], musicas[0]

for musica in musicas:
    if musica['tocou'] > maior['tocou']:
        maior = musica
    elif musica['tocou'] < menor['tocou']:
        menor = musica

print(f'Mais tocada: {maior["titulo"]}')
print(f'Menos tocada: {menor["titulo"]}')
