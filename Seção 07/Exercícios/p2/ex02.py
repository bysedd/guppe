mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for i in range(5):
    for j in range(5):
        if i == j:
            mat[i][j] = 1
        else:
            mat[i][j] = 0
print('-=' * 30)
for linha in mat:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()
print('-=' * 30)
