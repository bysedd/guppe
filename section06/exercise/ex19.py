n = int(input('Enter an integer between 100 and 999: '))
if 100 <= n <= 999:
    for c in range(0, len(str(n))):
        print(str(n)[c])
