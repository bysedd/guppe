mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(1, 5):
    for j in range(1, 5):
        mat[i - 1][j - 1] = i * j
print('-=' * 30)
for linha in mat:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()
print('-=' * 30)
