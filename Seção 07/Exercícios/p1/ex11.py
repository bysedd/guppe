pos = list()
neg = list()

for _ in range(10):
    while True:
        numero = float(input('Digite um número real: '))
        if numero > 0:
            pos.append(numero)
            break
        elif numero < 0:
            neg.append(numero)
            break

print(f'Quantidade de número negativos: {len(neg)}\n'
      f'Soma dos número positivos: {sum(pos):.1f}')
