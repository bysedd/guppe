a = int(input('Início: '))
b = int(input('Fim: '))
if a > 0 and b > 0:
    soma = 0
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
                p += f'{num} + '
                soma += num
                i += 1
        num += 1
    print(f'\033[3:34m{p[:len(p) - 3]}\033[m = \033[1:32m{soma}\033[m')
else:
    raise ValueError('\033[1:31mO número precisa ser maior do que 0\033[m')
