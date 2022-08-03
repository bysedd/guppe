n1 = float(input('Note 1: '))
n2 = float(input('Note 2: '))

if (n1 <= 0.0 or n1 >= 10.0) or (n2 <= 0.0 or n2 >= 10.0):
    print('Invalid note(s)')
else:
    media = (n1 + n2) / 2.0
    if media < 5.0:
        print(f'Average: \033[1:31m{media:.1f}\033[m')
    else:
        print(f'Average: \033[1:32m{media:.1f}\033[m')
