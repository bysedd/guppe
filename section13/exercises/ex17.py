import numpy as np

with open("matriz-conf.txt") as f:
    try:
        f = f.readlines()
        linha, coluna, pular = f[0].split()
        matriz = np.ones([int(linha), int(coluna)], dtype=int)

        for i in f[1:int(pular) + 1]:
            linha, coluna = i.split()
            matriz[int(linha)][int(coluna)] = 0
    except IndexError:
        print("Erro na criação da matriz")

with open("matriz_saida.txt", "w") as f:
    f.write(str(matriz))
