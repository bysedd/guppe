"""
Debug com PDB

PDB ≥ Python Debugger

Vida de Inseto ≥ Life's Bug

Bug ≥ Inseto

OBS: a utilização do print() para debugar o código é uma prática ruim.

def dividir(a, b):
    print(f"a={a}, b={b}")
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"\033[31m{err}\033[m"
print(dividir(4, 7))

Existem formas mais profissionais de se fazer esse "debug", utilizando o debugger.
Em Python, podemos fazer isso em diferentes IDE, como o PyCharm ou utilizando o PDB — Python Debugger

Exemplo com o PyCharm:
def dividir(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"\033[31m{err}\033[m"
print(dividir(4, 0))

Exemplo com o PDB — Python Debugger

Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
    * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
    incorporado como função built-in (integrada), chamada breakpoint()

Comandos básicos do PDB:
    l (listar onde estamos no código)
    n (próxima linha)
    p (imprime variável)
    c (continua a execução — finaliza o debug)

from pdb import set_trace

nome = "Tomas"
sobrenome = "Shelby"
set_trace()
nome_completo = nome + " " + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)

Por que utilizar este formato?
O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
no início do arquivo. Por isso, ao invés de colocarmos import do pdb no início do arquivo,
nós colocamos somente aonde vamos debugar, e ao finalizar já fazemos a remoção.

# Exemplo 2

nome = "Tomas"
sobrenome = "Shelby"
breakpoint()
nome_completo = nome + " " + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)

OBS: cuidado com conflitos entre nomes de variáveis e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return sum((l, n, p, c))


print(soma(1, 3, 5, 7))

Como os nomes das variáveis são os mesmos dos comanos do pdb, devemos utilizar o comando "p" para imprimir
as variáveis. Ou seja, "p nome_da_variavel"
"""
