x = []
y = []
pe = 0.0

while True:
    c1 = input('Digite 10 números reais, separados por espaço, para o conjunto 1: ').split(' ')
    c2 = input('Digite 10 números reais, separados por espaço, para o conjunto 2: ').split(' ')

    if len(c1) == 10 and len(c2) == 10:
        for elemento in c1:
            x.append(float(elemento))
        for elemento in c2:
            y.append(float(elemento))
        break
    else:
        print(f'\033[0:31mO conjunto precisa conter 10 valores!\033[m')

for i in range(5):
    pe += x[i] * y[i]

print(f'\nConjunto 1 = {x}\n'
      f'Conjunto 2 = {y}\n'
      f'Produto escalar = {pe}')
