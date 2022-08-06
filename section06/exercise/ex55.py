n = int(input('Digite um número inteiro positivo: '))
if n > 0:
    soma, conta = 0, 0
    num = 2
    p = ''
    while conta < n:
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        if primo:
            p += f'{num} + '
            soma += num
            conta += 1
        num += 1
    print(f'\033[3:34m{p[:len(p) - 3]}\033[m = \033[1:32m{soma}\033[m')
else:
    raise ValueError('\033[1:31mO número precisa ser menor do que 0\033[m')
