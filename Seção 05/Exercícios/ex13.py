# 0.0-100.0
n1 = float(input('Note 1: '))
n2 = float(input('Note 2: '))
n3 = float(input('Note 3: '))

if (n1 < 0.0 or n1 > 100.0) or (n2 < 0.0 or n2 > 100.0) or (n3 < 0.0 or n3 > 100.0):
    print('Invalid note(s)')
    if n1 < 0.0 or n1 > 100.0:
        print(f'\033[0:31mNote 1: {n1}\033[m')
    else:
        print(f'\033[0:32mNote 1: {n1}\033[m')

    if n2 < 0.0 or n2 > 100.0:
        print(f'\033[0:31mNote 2: {n2}\033[m')
    else:
        print(f'\033[0:32mNote 2: {n2}\033[m')

    if n3 < 0.0 or n3 > 100.0:
        print(f'\033[0:31mNote 3: {n3}\033[m')
    else:
        print(f'\033[0:32mNote 3: {n3}\033[m')
else:
    avg = (1*n1 + 1*n2 + 2*n3) / 4.0
    if avg >= 60.0:
        print(f'Average \033[0:34m{avg}\033[m --> \033[1:32mApproved\033[m')
    else:
        print(f'Average \033[0:34m{avg}\033[m --> \033[1:31mDisapproved\033[m')
