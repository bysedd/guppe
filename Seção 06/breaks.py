"""
Saindo de loops com break

Funciona da mesma forma que na linguagem Csharp.
Utilizamos o break para sair de loops de maneira projetada.

# Exemplo 1
for num in range(1, 11):
    if num == 6:
        print(f'{num} -> Saindo do loop')
        break
    else:
        print(num)

"""

# Exemplo 2
while True:
    comando = input("Digite\033[0:34m sair\033[m para sair: ").lower()
    if comando.__contains__('sair'):
        break
