"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension
"""

# Exemplos
numeros = [1, 2, 3, 4, 5, 6]

# 1
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorando
# Qualquer número par módulo de 2 é 0, e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2
res = [numero * 2 if not numero % 2 else numero / 2 for numero in numeros]
print(res)
