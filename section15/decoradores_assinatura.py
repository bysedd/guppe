"""
Decorators com diferentes assinaturas

# Relembrando/Reforçando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o(a) {nome}.'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de pedir {principal}, acompanhado de {acompanhamento}, por favor.'


# Testando
print(saudacao('Felippe'))
print(ordenar('filé', 'água'))
# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome, e parâmetros de entrada.


# Refatorando com a Decorator Pattern


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o(a) {nome}.'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de pedir {principal}, acompanhado de {acompanhamento}, por favor.'


@gritar
def lol():
    return 'lol'


# Testando
print(saudacao('felippe'))  # 1 arg.
print(ordenar('filé-mingon', 'água'))  # 2 arg.
print(lol())  # 0 arg.

# Vale lembrar que podemos utilizar parâmetros nomeados
print(ordenar(acompanhamento='coca cola sem açúcar', principal='frango assado'))
"""


# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! O primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)

        return outra

    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Teste 1
print(comida_favorita('lasania', 'pitza', 'amburguer'))
print(comida_favorita('pizza', 'picania'))
# Teste 2
print(soma_dez(10 ** 5 / 10000, 1971))
