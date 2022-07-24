from math import pow, sqrt

vetor = list(range(10))
media = 0.0
m = 0.0
sigma = 0.0
p = 0.0

for i in range(10):
    vetor[i] = int(input('Digite um inteiro: '))
for i in range(10):
    m += vetor[i]

media = m / 10.0

for i in range(10):
    p += pow((vetor[i] - media), 2)

sigma = sqrt(p / 9)
print(f'\nResultado = {sigma:.2f}')
