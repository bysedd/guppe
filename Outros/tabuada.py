num = int(input('Digite um valor para ver sua tabuada? '))
fim = int(input('Até qual número você gostaria de multiplicar? '))
print()
for c in range(0, fim + 1):
    print('\033[1;36m{} x {}\033[m = \033[1;32m{}\033[m'.format(num, c, num * c))
