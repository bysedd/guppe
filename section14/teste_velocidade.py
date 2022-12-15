# coding=utf-8

"""
Teste de velocidade com expressões geradoras

from sys import getsizeof

# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


gen1 = nums()
print(gen1, getsizeof(gen1))  # generator object
print(next(gen1))
print(next(gen1))

# Generator Expression

gen2 = (num for num in range(1, 10))
print(gen2, getsizeof(gen2))
print(next(gen2))
print(next(gen2))

"""

# Realizando o teste de velocidade
import time
qtd = 100000000  # 100 milh�es

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(qtd)))
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum(list(range(qtd))))
list_tempo = time.time() - list_inicio

print('Generator Expression levou {} segundos'.format(round(gen_tempo, 1)))
print('List Comprehension levou {} segundos'.format(round(list_tempo, 1)))
