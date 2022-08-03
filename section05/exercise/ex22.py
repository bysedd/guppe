idade = int(input('Age: '))
time = int(input('Years of service: '))

if time < idade:
    if idade >= 65:
        print('\033[0:32mCan retire\033[m')
    elif time >= 30:
        print('\033[0:32mCan retire\033[m')
    elif idade >= 60 and time >= 25:
        print('\033[0:32mCan retire\033[m')
    else:
        print("\033[0:31mCan't retire\033[m")
else:
    print('\033[0:31mIncorrect values\033[m')
