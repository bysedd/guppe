from math import sqrt

for i in range(1, 5000000):
    a, b = i, i + 1
    c = pow(a, 2) + pow(b, 2)
    if str(sqrt(c)).split('.')[1] == '0':
        print(f'{a}² + {b}² => {pow(a, 2)} + {pow(b, 2)} => \033[0:34m√{c}\033[m = \033[1:32m{int(sqrt(c))}²\033[m')
