"""
Listas Aninhadas (Nested Lists)

— Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes)

Em Python nós temos as Listas

numeros = [1, 'b', 3.456, True, 5j, ...]

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # (3, 3)
print(listas)
print(type(listas))

# Como fazemos para acessar os dados?
print(listas[0][1])
print(listas[2][1])

# Iterando com ‘loops’ em uma lista aninhada
for linha in listas:
    for num in linha:
        print(num, end=' ')
    print()

# List Comprehension
[[print(valor, end=' ') for valor in lista] for lista in listas]

"""

import numpy as np

# Outros exemplos

# Gerando um tabuleiro/matriz 3x3
tabuleiro = np.array([list(range(1, 4)) for valor in range(1, 4)])
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = np.array([['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)])
print(velha)

# Gerando valores iniciais
print(np.array([['*' for i in range(1, 4)] for j in range(1, 4)]))
