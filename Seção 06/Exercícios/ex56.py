soma = 0
num = 2
for c in range(3, 2000 + 3):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo and num < c:
        soma += num
    num += 1
print(f'A soma de todos os número primos abaixo de \033[3:34m2000(dois mil)\033[m é: \033[1:32m{soma}\033[m')
