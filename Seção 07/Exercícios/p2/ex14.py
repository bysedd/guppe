def cartela(mat: list):
    from random import randint
    c = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            while True:
                r = randint(0, 99)
                if r not in c:
                    c.append(r)
                    mat[i][j] = r
                    break
    print('-=' * 30)
    for linha in mat:
        for elemento in linha:
            print(f'[{elemento:^6}]', end='')
        print()
    print('-=' * 30)


cartela([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
