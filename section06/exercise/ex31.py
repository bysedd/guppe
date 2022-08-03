s, x, p = 0, 1, ''
for c in range(1, 100, 2):
    if c == 1:
        s += c / x
    else:
        s += c / x
        x += 1
    p += f'{c}/{x} + '
print(f'{p[:len(p) - 3]}\n= \033[1:32m{s}\033[m')
