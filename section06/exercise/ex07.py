s, m = 0, 0
for _ in range(10):
    v = int(input('Digite um valor: '))
    if v > 0:
        s += v
        m += 1
print(f'A média de todos os valores somados é \033[0:34m{s / m}\033[m')
