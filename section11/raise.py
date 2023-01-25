"""
Levantando os próprios erros com raise

raise ≥ Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como "def" ou qualquer outra palavra em Python.

Para simplificar, pense no raise como sendo útil para podermos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro("Mensagem de erro")

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("O texto precisa ser do tipo 'str'")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser do tipo 'str'")
    print(f"O texto '{texto}' será impresso na cor {cor}")


colore("Hello World!", "azul")
colore("777", "amarelo")

# Exemplo refatorado

def colore(texto, cor):
    cores = ("verde", "amarelo", "azul", "branco", "vermelho")

    if type(texto) is not str:
        raise TypeError("O texto precisa ser do tipo 'str'")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser do tipo 'str'")

    if cor.lower() not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")

    print(f"O texto '{texto}' será impresso na cor {cor}")
"""


# Exemplo real


def colore(texto, cor):
    # cores válidas
    cores = ("verde", "amarelo", "azul", "vermelho")

    # validações
    if type(texto) is not str:
        raise TypeError("O texto precisa ser do tipo 'str'")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser do tipo 'str'")
    if cor.lower() not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")

    # exibição
    if cor == "azul":
        print(f"\033[34m{texto}\033[m")
    elif cor == "amarelo":
        print(f"\033[33m{texto}\033[m")
    elif cor == "verde":
        print(f"\033[32m{texto}\033[m")
    elif cor == "vermelho":
        print(f"\033[31m{texto}\033[m")


colore("Hello World!", "vermelho")
colore("Hello World!", "azul")
colore("Hello World!", "amarelo")
colore("Hello World!", "verde")
