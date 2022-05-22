a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))

# A
if a < b and a < c:
    print(a)
    if b < c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)

# B
if b < a and b < c:
    print(b)
    if a < c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)

# C
if c < a and c < b:
    print(c)
    if a < b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
