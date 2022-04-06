total = 0
for c in range(0, 4):
    v = float(input('Enter a note: '))
    total += v

print(f'A soma dos quadrados dos tres valores lidos: \033[4:32m{total / 4.0}\033[m')
