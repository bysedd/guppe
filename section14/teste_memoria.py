"""
Teste de Memória com Generators

Sequência de Fibonacci:
    1, 1, 2, 3, 5, 8, 13, ...

# Teste 1
[print(i, n) for i, n in enumerate(fib_lista(100))]

"""


# Função utilizando listas 470mb


def fib_lista(maximo: int):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


# Função utilizando geradores 7mb


def fib_gen(maximo: int):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador = contador + 1


# [print(n) for n in fib_lista(100000)]
[print(n) for n in fib_gen(100000)]
