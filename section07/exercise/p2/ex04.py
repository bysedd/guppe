mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
mai, pos = 0, ''
for i in range(4):
    for j in range(4):
        mat[i][j] = (int(input(f'Digite um valor para a posição [{i + 1}, {j + 1}]: ')))
        if mat[i][j] > mai:
            mai = mat[i][j]
            pos = f'[{i + 1}, {j + 1}]'
print('-=' * 30)
for linha in mat:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()
print('-=' * 30)
print(f'Maior elemento: {mai} na posição: {pos}')
