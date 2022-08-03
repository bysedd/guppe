a = [4, 7, 5, 12, 16, 1, 9, 3, 11, 19, 10]
v = list()

for i in range(11):
    if i < 6:
        a.sort()
        v.append(a[i])
    else:
        a.sort(reverse=True)
        v.append(a[i])

print(v)
