# 1180
x = int(input())
numbers = input()
numbers = numbers.split()[:x + 1]
menor = min(numbers)
print(f'Menor valor: {menor}')
print(f'Posição: {numbers.index(menor) + 1}')
