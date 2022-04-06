"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula.
"""

# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor, type(valor), "\n")

# Certo do ponto de vista Float
valor = 1.44
print(valor, type(valor), "\n")

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1, type(valor1))
print(valor2, type(valor2), "\n")

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res, type(res), "\n")

# Podemos trabalhar com números complexos
variavel = 5j
print(type(variavel))
