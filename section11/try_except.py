"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Prevenindo assim que o programa pare
de funcionar e o usuário receba mensagens e erro inesperadas.

A forma geral mais simples é:

try:
    # execução
except:
    # o que deve ser feito em caso de problema

# Exemplo 1 — Tratando um erro genérico

try:
    geek()
except:
    print("Deu algum problema")
# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# Exemplo 2 — Tratando um erro genérico

try:
    len(5)
except:
    print("Deu algum problema")

OBS: tratar erro de forma genérica não é a melhor forma e tratamento de erros. O ideal é SEMPRE
tratar de forma específica

# Exemplo 3 — Tratando um erro específico
try:
    geek()
except NameError:
    print("Você está utilizando uma função inexistente.")

# Exemplo 4 — Tratando um erro específico
try:
    print(len(5))
except TypeError:
    print("Você está utilizando um tipo de dado inválido.")

# Exemplo 5 — Tratando um erro específico com detalhes do erro
try:
    print(len(5))
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: \033[31m{err}\033[m")

# Podemos efetuar diversos tratamentos e erros de uma vez.
try:
    # print(len(5))
    geek()
    # print("Geek"[9])
except NameError as err:
    print(f"Deu NameError: \033[31m{err}\033[m")
except TypeError as err:
    print(f"Deu TypeError: \033[31m{err}\033[m")
except:
    print("Deu um erro diferente")
"""


def pega_valor(dicionario=None, chave=None):
    try:
        return dicionario.get(chave)
    except (TypeError, AttributeError):
        return None


dic = {"nome": "Geek"}

print(pega_valor())
