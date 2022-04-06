from math import sqrt, pow

num = float(input('Enter a number: '))
dec = str(num).split('.')[1].__len__()

if num > 0:
    print(f'\033[0:36m√{num}\033[m = \033[0:32m{sqrt(num):.{dec}f}\033[m')
    print(f'\033[0:36m({num})²\033[m = \033[0:32m{pow(num, 2):.{dec}f}\033[m')
else:
    print('\033[0:31mThe number must be greater than 0\033[m')
