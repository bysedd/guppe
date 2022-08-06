a = int(input('Início: '))
b = int(input('Fim: '))
if a > 0 and b > 0:
    conta = 0
    i = a
    num = 2
    p = ''
    while i < b:
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        if primo:
            if a <= num <= b:
                p += f'{num}, '
                conta += 1
                i += 1
        num += 1
    print(f'\033[3:37m{p[:len(p) - 2]}\033[m')
    if conta == 1:
        print(f'Entre \033[3:34m{a} e {b}\033[m só existe \033[1:33m{conta} número primo\033[m')
    else:
        print(f'Entre \033[3:34m{a} e {b}\033[m existem \033[1:33m{conta} números primos\033[m')
else:
    raise ValueError('\033[1:31mO número precisa ser menor do que 0\033[m')
