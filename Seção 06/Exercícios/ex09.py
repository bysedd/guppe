n = int(input('Primeiros números naturais ímpares: '))
for c in range(1, n * 2):
    if c % 2 != 0:
        print(c, end=' ')
