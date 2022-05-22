a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a + b < c or a + c < b or b + c < a:
    print(f'\033[0:31mInvalid triangle\033[m')
else:
    if a == b == c:
        print('\033[0:34mEquilateral\033[m triangle')
    elif a == b or b == c or c == a:
        print('\033[0:34mIsosceles\033[m triangle')
    elif a != b != c:
        print('\033[0:34mScalene\033[m triangle')
