from math import factorial

s = 0
for c in range(1, 5 + 1):
    s += c / factorial(c * 2)
print(s)
