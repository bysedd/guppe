class CisneNegro:
    def __len__(self) -> int:
        return 42


livro = CisneNegro()
print(len(livro))

nome = 'Geek University'
lista = [12, 34, 55, 49]
dicionario = {'carlos': 12, 'vanessa': 34, 'joana': 49}

print(len(nome))
print(len(lista))
print(len(dicionario))

idade = 42
peso = 81.4

# print(len(idade))  # TypeError: object of type 'int' has no len()
