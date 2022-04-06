from math import sqrt, pow

num = float(input('Enter a real number: '))
dec = str(num).split('.')[1].__len__()

if num > 0:
    print(f'\033[0:36m√{num}\033[m = {sqrt(num):.{dec}f}')
else:
    print(f'\033[0:36m({num})²\033[m = {pow(num, 2):.{dec}f}')
