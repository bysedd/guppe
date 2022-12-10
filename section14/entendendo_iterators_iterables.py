"""
Entendendo Iterator e Iterables

Iterator:
    - Um objeto que pode ter iterado;
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.
Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

nome = 'Geek'  # É um iterable, mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable, mas não é um iterator.
iter1 = iter(nome)
iter2 = iter(numeros)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
"""

nome = 'Geek'
[print(letra) for letra in nome]
