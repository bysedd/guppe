"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iríamos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela e etc.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos assim:

public class Lampada() {
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor) {
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por convenção, ficou estabelecido que, qualquer atributo de uma classe é público. Ou seja, pode ser acessado em todo o projeto. Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente na própria classe onde está declarado, utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe. A não ser que façamos acesso através de métodos da própria classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')
print(user.email)
# print(user.__senha)  # AttributeError
# print(user._Acesso__senha)  # Temos acesso. Mas não deveríamos fazer este acesso. (Name Mangling)
user.mostra_senha()
user.mostra_email()

# O que significa atributos de instância?
# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '12345678')
user2 = Acesso('user2@gmail.com', '87654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de classe são atributos, claro, que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe.
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe.

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python são chamados de atributos estáticos.

"""


# Classes com atributos de instância públicos


class Lampada:
    def __init__(self, voltagem: int, cor: str):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero: int, limite: float, saldo: float):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome: str, descricao: str, valor: float):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome: str, idade: int, email: str):
        self.nome = nome
        self.idade = idade
        self.email = email


# Atributos Públicos e Atributos Privados


class Acesso:
    def __init__(self, email: str, senha: str):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos de classe

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)


# Refatorar a classe Produto


class Produto:
    # Atributos de classe
    imposto: float = 1.05  # 0.05% de imposto
    contador: int = 0

    def __init__(self, nome: str, descricao: str, valor: float):
        self.id: int = Produto.contador + 1
        self.nome: str = nome
        self.descricao: str = descricao
        self.valor: float = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso.
print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')  # AttributeError

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)
