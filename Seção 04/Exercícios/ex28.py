from math import pow

total = 0
for c in range(0, 3):
    v = float(input('Enter a value: '))
    total += pow(v, 2)

print(f'A soma dos quadrados dos tres valores lidos: \033[4:32m{total}\033[m')
