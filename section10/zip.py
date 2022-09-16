"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elementos de cada um dos iteráveis passados como entrada em pares.

# Exemplos
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')
print(zip1, type(zip1))

# Sempre podemos gerar uma Lista, Tupla, Conjunto ou Dicionário.
print(list(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

# OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando
# com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar.
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista3, lista2, lista1)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com zip
tupla = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

"""

# Exemplos mais complexos

prova1 = [80, 91, 53]
prova2 = [98, 89, 78]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1:]) for dado in zip(alunos, prova1, prova2)}
[print(f'{k} - {v} pts') for k, v in final.items()]
print()

# Podemos utilizar o map()
final = dict(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2))))
[print(f'{k} - {v} pts') for k, v in final.items()]
