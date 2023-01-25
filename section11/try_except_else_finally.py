"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

Else ≥ é executado somente se não ocorrer o erro, para cada except podemos ter um else.
try:
    num = int(input("Informe um número: "))
except ValueError as err:
    print(f"\033[31mValor incorreto\033[m")
else:
    print(f"Você digitou o número {num}")

Finally ≥ geralmente, é utilizado para fechar ou desalocar recursos.
try:
    num = int(input("Informe um número: "))
except ValueError:
    print(f"\033[31mValor incorreto\033[m")
else:
    print(f"Você digitou o número {num}")
finally:
    print("Depois do bloco try/except")

OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

Exemplo mais complexo CORRETO
OBS: você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError):
        return None


n1 = input("Informe o primeiro número: ")
n2 = input("Informe o segundo número: ")
print(f"{n1} / {n2} = {dividir(n1, n2)}")
"""
