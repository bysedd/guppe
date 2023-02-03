"""
Assertions (Afirmações/Checagens/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples checagens em nossos programas.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

OBS: nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada.

OBS: a palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamente
em testes.

# ALERTA: Cuidado ao utilizar o 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado. Ou seja, todas as suas
"""


def soma_numeros_positivos(a: int, b: int) -> int:
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


print(soma_numeros_positivos(a=2, b=4))  # 6
# print(soma_numeros_positivos(a=-2, b=4))  # AssertionError


def comer_fast_food(__comida: str) -> str:
    assert __comida.strip().lower() in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {__comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

