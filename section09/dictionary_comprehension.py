"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4]

Se quisermos criar uma tupla fazemos:
tupla = (1, 2, 3, 4) ou 1, 2, 3, 4

Se quisermos criar um conjunto fazemos:
set = {1, 2, 3, 4}

Se quisermos criar um dicionário fazemos:
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe

{chave: valor for valor in iterável}

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numeros = [1, 2, 3, 4, 5, 1, 2]
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)

chaves = 'abcde'
valores = [1, 2, 3, 4]
menor = len(chaves) if len(chaves) < len(valores) else len(valores)
juntar = {chaves[i]: valores[i] for i in range(menor)}
print(juntar)

"""

# Exemplo com lógica condicional
res = {num: ('par' if num % 2 == 0 else 'ímpar') for num in range(0, 10)}
print(res, end='\n\n')  # Mostra o dicionário
[print(k, v) for k, v in res.items()]  # Mostra chave e valor
print()
[print(k, v) for k, v in res.items() if k % 2 == 0]  # Mostra chave par
print()
[print(k, v) for k, v in res.items() if k % 2 != 0]  # Mostra chave ímpar
