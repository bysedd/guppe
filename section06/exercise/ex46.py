from random import randint

x, c = randint(1, 1000), 1
while True:
    n = int(input('Tente acertar o número: '))
    if n == x:
        print('\n\033[0:32mParabéns você acertou\033[m')
        print(f'Número de tentativas: \033[0:34m{c}\033[m')
        break
    elif n > x:
        print('\033[0:31mErrado..\033[m Digite um número\033[1:31m menor\033[m')
        c += 1
    elif n < x:
        print('\033[0:31mErrado..\033[m Digite um número\033[1:32m maior\033[m')
        c += 1
