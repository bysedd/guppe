vetor = [0]

for i in range(101):
    if i % 7 != 0:
        vetor.append(i)

for elemento in vetor:
    if len(str(elemento)) == 2 and str(elemento)[1] == '7':
        vetor.remove(elemento)

print(vetor)
