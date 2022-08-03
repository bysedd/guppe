from math import sqrt

n = int(input('Enter a number: '))

if n > 0:
    print(f'Square root of the number {n} is: {sqrt(n):.1f}')
else:
    print('Invalid number')
