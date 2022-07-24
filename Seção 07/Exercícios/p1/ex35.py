a = int(input('Digite um número positivo menor que 10000: '))
b = int(input('Digite outro número positivo menor que 10000: '))

while 0 > a > 10000 or 0 > b > 10000:
    a = int(input('Digite um número positivo menor que 10000: '))
    b = int(input('Digite outro número positivo menor que 10000: '))

vetor = list(range(a, b + 1))

print(f'\nVetor: {vetor}\n'
      f'Soma: {sum(vetor)}')
