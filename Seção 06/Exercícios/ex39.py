def area_do_triangulo(b: float, h: float):
    a = b * h / 2
    print(f'Área do triângulo: \033[3:32m{a:.2f}\033[m')


base = float(input('Base do triângulo: '))
altura = float(input('Altura do triângulo: '))
if base > 0 and altura > 0:
    area_do_triangulo(base, altura)
else:
    while not (base > 0 and altura > 0):
        print('\033[1:31mDados inválido\033[m\n')
        base = float(input('Base do triângulo: '))
        altura = float(input('Altura do triângulo: '))
    area_do_triangulo(base, altura)
