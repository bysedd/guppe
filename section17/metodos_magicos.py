"""
POO - Métodos Mágicos

Métodos mágicos são todos os métodos que utilizam dunder.
Dunder -> Double Underscore

dunder init -> __init__ (Método construtor)
def __init__(self, titulo: str, autor: str, paginas: int) -> None:
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

dunder repr -> __repr__ (Representação do objeto)
def __repr__(self) -> str:
    return f'{self.titulo} escrito por {self.autor}'

dunder str -> __str__ (Representação do objeto)
def __str__(self) -> str:
    return self.titulo

dunder len -> __len__ (Representação do objeto)
def __len__(self) -> int:
    return self.paginas

dunder del -> __del__ (Método destrutor)
def __del__(self) -> None:
    print('Um objeto do tipo Livro foi deletado da memória')

dunder add -> __add__ (Método para soma)
def __add__(self, other: object) -> int:
    if isinstance(other, Livro):
        return self.paginas + other.paginas
    return 'Não é possível somar!'

"""


class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self) -> str:
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self) -> str:
        return self.titulo

    def __len__(self) -> int:
        return self.paginas

    def __add__(self, other) -> str:
        if isinstance(other, Livro):
            return f'{self} - {other}'
        return 'Não é possível somar!'

    def __mul__(self, other) -> str:
        if isinstance(other, int):
            msg = f' ... '.join([str(self) for _ in range(other)])
            return msg
        return 'Não é possível multiplicar!'


livro = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro)
print(livro2)

print(len(livro))
print(len(livro2))

print(livro + livro2)

print(livro * 3)
print(livro2 * 2)
