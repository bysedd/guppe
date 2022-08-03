s = 0
for _ in range(10):
    v = int(input('Digite um valor: '))
    s += v
print(f'A média de todos os valores somados é \033[0:34m{s / 10}\033[m')
