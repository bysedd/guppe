from math import pow

cyan = '\033[1:36m'
green = '\033[1:32m'
stop = '\033[m'

real_number = float(input("Enter a real number: "))
square = pow(real_number, 2)
decimal_places = len(str(real_number).split('.')[1])
str_square = f'{square:.{decimal_places}f}'

print(f'The square of {cyan}{real_number}{stop} is {green}{str_square}{stop}')
