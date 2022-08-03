n1 = int(input('Enter an integer: '))
n2 = int(input('Enter another integer: '))

if n1 > n2:
    print(f'{n1} is greater than {n2}')
elif n1 < n2:
    print(f'{n2} is greater than {n1}')
else:
    print(f'Both are the same')
