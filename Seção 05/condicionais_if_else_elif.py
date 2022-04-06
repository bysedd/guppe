"""
Estruturas condicionais
if (Se), else (Senão), elif (Senão se)
"""

idade = 28

"""
# Estrutura condicional em C#: if () {}, else if () {}, else () {}
if (idade < 18) {
    print("Menor de idade");
} else if (idade == 18) {
    print("Tem 18 anos");
} else {
    print("Maior de idade");
}
"""

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')
