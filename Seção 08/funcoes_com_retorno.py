"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: em Python, quando uma função não retorna nenhum valor, o retorno é None;

OBS: funções Python que retornam valores, devem retornar estes valores com a palavra reservada return;

OBS: não precisamos necessariamente criar uma variável para receber o retorno
de uma função. Podemos passar a execução da função para outras funções

# Vamos refatorar está função para que ela retorne o valor
"""


def quadrado_de_7():
    return 7 ** 2


ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno {quadrado_de_7() + 1}')

