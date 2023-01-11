# coding=utf-8
from functions import print_formatado, error_message, confirm


class Despensa:
    def __init__(self):
        self.opcoes = {
            1: "Entrada de produtos",
            2: "Retirada de produtos",
            3: "Relátorio geral",
            4: "Produtos indisponíveis",
            5: "Sair"
        }
        self.arquivo = "despensa-domestica.bin"
        self.encoding = "utf-8"

    def adicionar_produto(self, c, n="", q=0, sobreescrever=False):
        if sobreescrever:
            produtos = self.ler_arquivo()

            string = ""
            for k, v in produtos.items():
                if int(c) == k:
                    v["quantidade"] += q
                string += f"{k},{v['nome']},{v['quantidade']}\n"

            with open(self.arquivo, "w", encoding=self.encoding) as f:
                f.write(string)
        else:
            with open(self.arquivo, "a", encoding=self.encoding) as f:
                f.write(f"{c},{n},{q}\n")

    def remover_produtos(self, c, q):
        produtos = self.ler_arquivo()

        string = ""
        for k, v in produtos.items():
            if int(c) == k:
                v["quantidade"] -= int(q)
                if v["quantidade"] < 0:
                    v["quantidade"] = 0
            string += f"{k},{v['nome']},{v['quantidade']}\n"

        with open(self.arquivo, "w", encoding=self.encoding) as f:
            f.write(string)

    def produtos_indisponiveis(self):
        with open(self.arquivo, encoding=self.encoding) as f:
            for linha in f.readlines():
                linha = linha.split("\n")[0].split(",")
                quantidade = int(linha[-1])
                if quantidade == 0:
                    print(f"código: {linha[0]} | nome: {linha[1]} | quantidade: {linha[2]}".center(80))

    def mostrar_despensa(self):
        with open(self.arquivo, encoding=self.encoding) as f:
            for linha in f.readlines():
                linha = linha.split("\n")[0].split(",")
                print(f"código: {linha[0]} | nome: {linha[1]} | quantidade: {linha[2]}".center(80))

    def mostrar_opcoes(self):
        [print(k, v, sep=" - ") for k, v in self.opcoes.items()]

    def exists(self):
        import os
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w"):
                pass

    def procurar_codigo(self, code):
        with open(self.arquivo, encoding=self.encoding) as f:
            file_lines = f.readlines()
            for linha in file_lines:
                linha = linha.split("\n")[0]
                c = int(linha.split(",")[0])
                if c == int(code):
                    break
            return int(code) == c, linha

    def ler_arquivo(self):
        produtos = {}
        with open(self.arquivo, encoding=self.encoding) as f:
            for linha in f.readlines():
                codigo_f, nome_f, qtd_f = linha.split("\n")[0].split(",")
                produtos[int(codigo_f)] = {"nome": nome_f, "quantidade": max([0, int(qtd_f)])}
        return produtos


despensa = Despensa()
despensa.exists()

while True:
    despensa.mostrar_opcoes()
    option = int(input("Escolha uma opção: "))

    match option:
        case 1:
            print_formatado("Entrada de produtos")
            continuar = True
            while continuar:
                try:
                    codigo = int(input("Código do produto: "))
                    if despensa.procurar_codigo(codigo)[0]:
                        produto = despensa.procurar_codigo(codigo)[1].split(',')
                        print(f"Esse código pertence ao produto => "
                              f"[nome: {produto[1]}, quantidade: {produto[2]}]")

                        adicionar = confirm("Quer adicionar alguma quantidade desse produto (y/n)? ")
                        if adicionar:
                            qtd = int(input("Digite a quantidade de produto(s) que deseja adicionar: "))
                            despensa.adicionar_produto(c=codigo, q=qtd, sobreescrever=True)
                        continue
                    else:
                        nome = input("Nome do produto: ").strip()
                        qtd = int(input(f"Quantidade de '{nome}': "))
                        despensa.adicionar_produto(codigo, nome, qtd)
                except ValueError as err:
                    print(error_message(err))
                finally:
                    continuar = confirm("Quer adicionar mais produtos (y/n)? ")
                    print()

        case 2:
            print_formatado("Remover produtos")
            continuar = True
            while continuar:
                try:
                    codigo = int(input("Código do produto: "))
                    if despensa.procurar_codigo(codigo)[0]:
                        produto = despensa.procurar_codigo(codigo)[1].split(',')
                        print(f"Esse código ao produto => "
                              f"[nome: {produto[1]}, quantidade: {produto[2]}]")
                        if produto[2] == 0:
                            print(f"Não há '{produto[1]}' suficientes para serem removidos")
                            continue

                        remover = confirm("Quer remover alguma quantidade desse produto (y/n)? ")
                        if remover:
                            qtd = int(input("Digite a quantidade de produto(s) que deseja remover: "))
                            despensa.remover_produtos(codigo, qtd)
                    else:
                        print(error_message("Código não encontrado"))
                except ValueError as err:
                    print(error_message(err))
                finally:
                    continuar = confirm("Quer remover mais produtos (y/n)? ")
                    print()

        case 3:
            print_formatado("Relatório geral")
            despensa.mostrar_despensa()
            print()

        case 4:
            print_formatado("Produtos indisponíveis")
            despensa.produtos_indisponiveis()
            print()

        case 5:
            print_formatado("Programa encerrado")
            break

        case _:
            print(error_message("Opção inválida"))
            print()
