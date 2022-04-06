n = int(input('Enter a three-digit number: '))
length = str(n).__len__()

if length == 3:
    str_n = str(n)
    print(f'\033[0:36m{n}\033[m <-> \033[0:32m{str_n[::-1]}\033[m')

else:
    print('\033[0:31mThe number must contain 3 digits\033[m')
