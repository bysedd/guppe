"""
Módulo Collections - namedtuple

typing.NamedTuple > collections.namedtuple

# Recap tupla
tupla = (1, 2, 3)
print(tupla)

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

from collections import namedtuple
from typing import NamedTuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração namedtuple
_ = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração namedtuple
_ = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração namedtuple e NamedTuple
_ = namedtuple('cachorro', ['idade', 'raca', 'nome'])
cachorro = NamedTuple('cachorro', [('idade', int), ('raca', str), ('nome', str)])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados

# Forma 1
print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome

# Forma 2
print(ray.idade)  # idade
print(ray.raca)  # raca
print(ray.nome)  # nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
