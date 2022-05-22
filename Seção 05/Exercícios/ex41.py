from math import pow

altura = float(input('Altura(m): '))
peso = int(input('Peso(kg): '))
imc = peso / (pow(altura, 2))
classificacao = ''

if imc < 18.5:
    classificacao = '\033[0:31mAbaixo do peso\033[m'
elif imc <= 24.9:
    classificacao = '\033[0:32mSaudável\033[m'
elif imc <= 29.9:
    classificacao = '\033[0:31mPeso em excesso\033[m'
elif imc <= 34.9:
    classificacao = '\033[1:31mObesidade Grau 1\033[m'
elif imc <= 39.9:
    classificacao = '\033[1:31mObesidade Grau 2 (severa)\033[m'
elif imc >= 40.0:
    classificacao = '\033[1:31mObesidade Grau 3 (mórbida)\033[m'

print(f'IMC = \033[0:34m{imc:.2f}kg/m²\033[m -> {classificacao}')
