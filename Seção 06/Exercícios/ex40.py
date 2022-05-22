n = int(input('Digite um número: '))
if n >= 0:
    maior = n
    menor = n
    while True:
        n = int(input('Digite um número: '))
        if n < 0:
            break
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
    print(f'\nMaior número digitado: \033[0:34m{maior}\033[m')
    print(f'Menor número digitado: \033[0:34m{menor}\033[m')
else:
    print(f'\033[1:31mO primeiro número deve ser positivo ou 0\033[m')
