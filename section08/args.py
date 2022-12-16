"""
Entendendo o *args

— O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
desde que comece com asterisco

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Desde já se
lembre que tuplas são imutáveis

# Exemplos


def soma_tudo(*args, show=True):
    if show:
        print(str(args).replace(',', ' +'), end=' = ')
    return sum(args)


print(soma_tudo(1, 3, 6))
print(soma_tudo())
print(soma_tudo(23.4, 12.5))


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""


def soma_tudo(*args, show=True):
    if show:
        print(str(args).replace(',', ' +'), end=' = ')
    return sum(args)


print(soma_tudo())
print(soma_tudo(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_tudo(*numeros))  # Desempacotamento / Unpacking

# OBS: o asterisco serve para informarmos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisará antes desempacotar estes dados.
