"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado, ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo 'function'
nos nossos programas.

OBS: na sessão de funções, nós utilizamos isso.

Em Python, as funções são Cidadãos de Primeira Classe (First Class Citizen)

# Exemplo - Definindo as funções


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


n1 = int(input("primeiro inteiro: "))
n2 = int(input("segundo inteiro: "))

# Testando funções
print(calcular(n1, n2, somar))
print(calcular(n1, n2, diminuir))
print(calcular(n1, n2, multiplicar))
print(calcular(n1, n2, dividir))

from random import choice

# Nested Functions - Funções Aninhadas

'''
Em Python podemos também ter funções em funções, que são conhecidas por Nested Functions
ou também Inner Functions (Funções Internas).
'''

# Exemplo


def cumprimento(nome: str):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + nome


print(cumprimento('Felippe'))
print(cumprimento('Arthur'))

# Retornando funções de outras funções


def faz_me_rir():
    def rir():
        return choice(('hahahahah', 'kkkkkkkkkkkk', 'jajajajaja'))
    return rir


rindo = faz_me_rir()
print(rindo())
"""
from random import choice


# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.


def faz_me_rir_novamente(pessoa):
    def dando_ridasa():
        risada = choice(('hahahahaha', 'kkkkkkkkkk', 'jajajajaja'))
        return f'{pessoa} — {risada}'

    return dando_ridasa


rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())
