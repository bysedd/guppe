from math import factorial

n = int(input('Digite o número de linhas do Triângulo de Pascal: '))
print()

for i in range(n):
    # for j in range(n-i+1):
    # print(end=' ')

    for j in range(i + 1):
        r = factorial(i) // (factorial(j) * factorial(i - j))
        print(r, end=' ')
    print()
