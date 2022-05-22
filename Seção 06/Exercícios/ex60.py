soma, qtn, media, media_par, qtn_par = 0, 1, 0, 0, 0
n = int(input('Digite um número: '))
if n % 2 == 0:
    qtn_par += 1
maior, menor = n, n
while True:
    n = int(input('Digite outro número: '))
    if n == 0:
        break
    else:
        soma += n
        qtn += 1
        media += n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        if n % 2 == 0:
            media_par += n
            qtn_par += 1
media /= qtn
media_par /= qtn_par
print(f'''\nSoma dos números digitados: \033[3:34m{soma}\033[m
Quantidade dos números digitados: \033[3:34m{qtn}\033[m
Média dos números digitados: \033[3:34m{media:.2f}\033[m
Maior número digitado: \033[3:34m{maior}\033[m
Menor número digitado: \033[3:34m{menor}\033[m
Média dos números pares: \033[3:34m{media_par:.2f}\033[m''')
