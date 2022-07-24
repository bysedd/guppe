def matriz():
    from math import pow
    a = [[], [], [], [], [], [], [], [], [], []]
    for i in range(10):
        for j in range(10):
            if i < j:
                a[i].append(2 * i + 7 * j - 2)
            elif i == j:
                a[i].append(3 * pow(i, 2) - 1)
            elif i > j:
                a[i].append(4 * pow(i, 3) - 5 * pow(j, 2) + 1)
    print('-=' * 60)
    for linha in a:
        for elemento in linha:
            print(f'[{int(elemento):^10}]', end='')
        print()
    print('-=' * 60)


matriz()
