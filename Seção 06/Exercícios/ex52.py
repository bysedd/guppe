v = int(input('Digite um valor: \033[3:34mR$\033[m'))
i = v
n200, n100, n50, n20, n10, n5, n2, n1 = 0, 0, 0, 0, 0, 0, 0, 0
while True:
    if i >= 200:
        n200 += 1
        i -= 200
    elif i >= 100:
        n100 += 1
        i -= 100
    elif i >= 50:
        n50 += 1
        i -= 50
    elif i >= 20:
        n20 += 1
        i -= 20
    elif i >= 10:
        n10 += 1
        i -= 10
    elif i >= 5:
        n5 += 1
        i -= 5
    elif i >= 2:
        n2 += 1
        i -= 2
    elif i >= 1:
        n1 += 1
        i -= 1
    else:
        break
if n200 != 0:
    print(f'\033[0:34m{n200}\033[m nota(s) de \033[0:32mR$200.00\033[m')
if n100 != 0:
    print(f'\033[0:34m{n100}\033[m nota(s) de \033[0:32mR$100.00\033[m')
if n50 != 0:
    print(f'\033[0:34m{n50}\033[m nota(s) de \033[0:32mR$50.00\033[m')
if n20 != 0:
    print(f'\033[0:34m{n20}\033[m nota(s) de \033[0:32mR$20.00\033[m')
if n10 != 0:
    print(f'\033[0:34m{n10}\033[m nota(s) de \033[0:32mR$10.00\033[m')
if n5 != 0:
    print(f'\033[0:34m{n5}\033[m nota(s) de \033[0:32mR$5.00\033[m')
if n2 != 0:
    print(f'\033[0:34m{n2}\033[m nota(s) de \033[0:32mR$2.00\033[m')
if n1 != 0:
    print(f'\033[0:34m{n1}\033[m nota(s) de \033[0:32mR$1.00\033[m')
