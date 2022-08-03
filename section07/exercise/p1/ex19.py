from math import fmod

vetor = list(range(50))
lista = list()

for i in vetor:
    valor = fmod(i + 5 * i, i + 1)
    lista.append(valor)

vetor.clear()
vetor.extend(lista)
print(vetor)
