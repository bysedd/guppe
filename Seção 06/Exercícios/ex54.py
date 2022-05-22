n = int(input('Digite um número: '))
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        c += 1
        print(i, end=' ')
print()
if c != 2:
    print(f'\033[0:31mO número {n} não é primo\033[m pois é divisível por {c} número(s)')
else:
    print(f'\033[0:32mO número {n} é primo\033[m pois é divisível por 2 números')
