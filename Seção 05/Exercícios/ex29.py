from random import randint

print('\033[1:34mTry to get these 5 questions right.\033[m')
c, w = 0, 0

for i in range(0, 5):
    a = randint(1, 100)
    b = randint(1, 100)

    r = int(input(f'{a} + {b} = '))

    if r == a + b:
        print('\033[0:32mCorrect!\033[m')
        c += 1
    else:
        print('\033[0:31mWrong!\033[m')
        print(f'{a} + {b} = {a + b}')

print(f'\033[1:34m{c} hits.\033[m')
