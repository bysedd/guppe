"""
Geradores

- Geradores (Generators) são Iteradores (Iterators):

OBS: o contrário é falso. Ou seja, nem tod'o iterator é um generator

Outras informações:
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com expressões geradoras;

Diferenças entre Funções e Funções Geradoras (Generator Functions):

---------------------------------------------------------------------------------------------
| Funções                                | Generator Functions                              |
|----------------------------------------|--------------------------------------------------|
| utilizam return                        | utilizam yield                                   |
| retorna uma vez                        | podem utilizar yield múltiplas vezes             |
| quando executada, retorna um valor     | quando executada, retorna um generator           |
---------------------------------------------------------------------------------------------


# Exemplo de Função Geradora (Generator Function)


def conta_ate(valor_maximo: int):
    i = 1
    while i <= valor_maximo:
        yield i
        i += 1


# Uma Generator Function não é um Generator, ela gera um generator.

gen = conta_ate(5)

[print(n) for n in range(5)]

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen), end='\n------\n')
[print(n) for n in gen]
"""


def conta_ate(valor_maximo: int):
    i = 1
    while i <= valor_maximo:
        yield i
        i += 1


gen = list(conta_ate(10))
print(gen)
