n = int(input('Enter an integer: '))

if n > 0:
    n_length, n_str, s = len(str(n)), str(n), 0
    for c in range(0, n_length):
        s += int(n_str[c])
    print(f'\033[0:32mThe sum of its digits is {s}\033[m')
else:
    print('\033[0:31mInvalid number\033[m')
