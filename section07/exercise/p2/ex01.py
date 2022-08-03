mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
cont = 0
for i in range(4):
    for j in range(4):
        mat[i][j] = (int(input(f'Digite um valor para a posição [{i + 1}, {j + 1}]: ')))
print('-=' * 30)
for linha in mat:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
        if elemento > 10:
            cont += 1
    print()
print('-=' * 30)
print(f'Essa matriz possui {cont} valores maiores que 10.')
