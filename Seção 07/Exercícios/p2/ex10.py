def matriz(mat: list):
    s = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] = int(input(f'Digite um valor para a posição [{i + 1}, {j + 1}]: '))
            if i == j:
                s += mat[i][j]
    print('-=' * 30)
    for linha in mat:
        for elemento in linha:
            print(f'[{elemento:^5}]', end='')
        print()
    print('-=' * 30)
    print(f'Soma dos elementos que estão na diagonal principal: {s}')


matriz([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
