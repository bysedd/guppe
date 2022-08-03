x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

op = input("""(a) Geométrica
(b) Ponderada
(c) Harmônica
(d) Aritmética
Opção: """)[0].lower()

if op == 'a':
    c = (x * y * z) ** (1 / 3)
    print(f'Média\033[0:34m geométrica\033[m: \033[0:32m{c:.1f}\033[m')
elif op == 'b':
    c = (x * 2 + y * 3 + z) / 6
    print(f'Média\033[0:34m ponderada\033[m: \033[0:32m{c:.1f}\033[m')
elif op == 'c':
    c = 3 / (1 / x + 1 / y + 1 / z)
    print(f'Média\033[0:34m harmônica\033[m: \033[0:32m{c:.1f}\033[m')
elif op == 'd':
    c = (x + y + z) / 3
    print(f'Média\033[0:34m aritmética\033[m: \033[0:32m{c:.1f}\033[m')
else:
    print('\033[1:31mOpção inválida!\033[m')
