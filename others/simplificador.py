try:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    p = f'\033[1:32m{n1}/{n2}\033[m'
    cont = []

    if n1.isnumeric() and n2.isnumeric():
        n1 = int(n1)
        n2 = int(n2)

        maior = max([n1, n2])
        menor = min([n1, n2])

        for i in range(2, maior):
            if maior % i == 0 and menor % i == 0:
                cont.append(i)

        d = max(cont)
        n1 //= d
        n2 //= d
        r = n1 / n2

        print(f'\nÉ possível simplificar essa fração/divisão por {d}\n{p} = '
              f'\033[1:36m{n1}/{n2}\033[m ou '
              f'\033[1:36m{round(r * 100, 2)}%\033[m ou '
              f'\033[1:36m{r:.4f}\033[m')
    else:
        print(f'\033[1:31mDigite apenas números!\033[m')

except ValueError:
    print('\n\033[1:31mNão é possível simplificar essa fração/divisão!\033[m')
