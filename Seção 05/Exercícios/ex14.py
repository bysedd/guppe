# 0.0-10.0
n1 = float(input('Lab work: '))
n2 = float(input('Semi-annual evaluation: '))
n3 = float(input('Final exam: '))

if (n1 < 0.0 or n1 > 10.0) or (n2 < 0.0 or n2 > 10.0) or (n3 < 0.0 or n3 > 10.0):
    print('Invalid note(s)')
    if n1 < 0.0 or n1 > 10.0:
        print(f'\033[0:31mNote 1: {n1}\033[m')
    else:
        print(f'\033[0:32mNote 1: {n1}\033[m')

    if n2 < 0.0 or n2 > 10.0:
        print(f'\033[0:31mNote 2: {n2}\033[m')
    else:
        print(f'\033[0:32mNote 2: {n2}\033[m')

    if n3 < 0.0 or n3 > 10.0:
        print(f'\033[0:31mNote 3: {n3}\033[m')
    else:
        print(f'\033[0:32mNote 3: {n3}\033[m')
else:
    avg = (2 * n1 + 3 * n2 + 5 * n3) / 10.0
    if 0.0 <= avg <= 2.9:
        print(f'Average \033[1:34m{avg:.1f}\033[m --> \033[1:31mDisapproved\033[m')
    elif 3 <= avg <= 4.9:
        print(f'Average \033[1:34m{avg:.1f}\033[m --> \033[1:33mRecuperation\033[m')
    else:
        print(f'Average \033[1:34m{avg:.1f}\033[m --> \033[1:32mApproved\033[m')
