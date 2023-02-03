"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um doctest usamos:

python -m doctest -v nome_do_script.py


def soma(a: int, b: int) -> int:

    Soma os números a e b

    #>>> soma(1, 2)
    3

    #>>> soma(4, 6)
    10

    #:param a: Um número inteiro
    #:param b: Outro número inteiro
    #:return: A soma de a e b

    return a + b


print(soma(3, 4))

# Saída

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    __main__
1 items passed all tests:
    1 tests in __main__.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.


# Outro exemplo, aplicando o TDD


def duplicar(valores: list) -> list:

    Duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

    #:param valores: Uma lista de valores
    #:return: Uma lista com os valores duplicados

    return list(map(lambda x: x * 2, valores))


# Erro inesperado...

OBS: Dentro do doctest, o Python não reconhece strings com aspas duplas. Precisa ser aspas simples.


def fala_oi() -> str:

    Fala oi

    #>>> fala_oi()
    'Oi!'

    #:return: Uma string com a palavra oi

    return 'Oi!'

"""

# Último caso estranho...


def verdade() -> bool:
    """
    Retorna verdade

    >>> verdade()
    True

    :return: Um valor booleano
    """
    return True
