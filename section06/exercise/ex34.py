print('O menor número que é divisível por 1, 2, 3, 4, ..., 10 é: \033[1:34m2520\033[m')
print('O menor número que é divisível por 1, 2, 3, 4, ..., 20 é: ', end='')  # 232792560
n = 1
while True:
    if n % 1 == 0 and n % 2 == 0 and n % 3 == 0 and n % 4 == 0 and n % 5 == 0:
        if n % 6 == 0 and n % 7 == 0 and n % 8 == 0 and n % 9 == 0 and n % 10 == 0:
            if n % 11 == 0 and n % 12 == 0 and n % 13 == 0 and n % 14 == 0 and n % 15 == 0:
                if n % 16 == 0 and n % 17 == 0 and n % 18 == 0 and n % 19 == 0 and n % 20 == 0:
                    print(f'\033[1:34m{n}\033[m')
                    break
    n += 1
