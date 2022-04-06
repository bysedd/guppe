n = int(input('Enter a four-digit number: '))
length = str(n).__len__()

if length == 4:
    str_n = str(n)
    for c in range(0, 4):
        print(f'\033[0:36m{str_n[c]}\033[m')

else:
    print('\033[0:31mThe number must contain 4 digits\033[m')
