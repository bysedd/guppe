# coding=utf-8
from colorama import Fore, Style

from section13.exercises.functions import print_formatado, error_message


class Turma:
    def __init__(self):
        self.turma = {}
        self.notas = None
        self.media_minima = None
        self.total_turma = None
        self.arquivo = 'turma.txt'
        self.encoding = 'utf-8'
        self.opcoes = {
            1: 'Inserir aluno e notas',
            2: 'Exibir turma e médias',
            3: 'Exibir turma aprovados',
            4: 'Exibir turma reprovados',
            5: 'Salvar dados em Disco',
            6: 'Sair do programa (fim)'
        }

    def exibir_opcoes(self):
        print_formatado("Opções")
        [print(f"{k} - {v}") for k, v in self.opcoes.items()]

    def definir_informacoes(self):
        print_formatado("Definindo informações da turma (0 para pular)")
        self.total_turma = int(input("Total de turma: "))
        self.media_minima = int(input("Média mínima para aprovação: "))
        self.notas = int(input("Total de provas por aluno: "))

    def inserir_dados(self):
        if not self.total_turma or not self.media_minima or not self.notas:
            print(error_message("Não será possível usar esta função"))
        else:
            aluno = 1
            while aluno <= self.total_turma:
                print_formatado(f"{aluno}.º aluno")
                nome = input("Nome: ").strip().title()
                if nome and nome.isalpha():
                    notas = [float(input(f"{i}.º nota: ")) for i in range(1, self.notas + 1)]
                    self.turma[nome] = notas
                    aluno += 1

    def exibir_dados(self):
        print_formatado("Exibindo dados")
        arquivo = self.ler_arquivo()
        [print(v["info"].center(80)) for k, v in arquivo.items()]

    def exibir_aprovados(self):
        if self.media_minima and self.notas:
            print_formatado("Alunos aprovados")
            arquivo = self.ler_arquivo()
            [print(v["info"].center(80)) for k, v in arquivo.items() if v["media"] >= self.media_minima]

    def exibir_reprovados(self):
        if self.media_minima and self.notas:
            print_formatado("Alunos reprovados")
            arquivo = self.ler_arquivo()
            [print(v["info"].center(80)) for k, v in arquivo.items() if v["media"] < self.media_minima]

    def salvar_dados(self):
        if self.turma:
            with open(self.arquivo, "a", encoding=self.encoding) as f:
                for k, v in self.turma.items():
                    string = f"{k},"
                    for nota in v:
                        string += f"{nota},"
                    f.write(f"{string[:-1]}\n")
            print(f"{Fore.GREEN}Dados salvos no disco{Style.RESET_ALL}")
        else:
            print(error_message("Insira os dados primeiro"))

    def check_file(self):
        """
        Cria o arquivo se ele não existir no diretório atual.
        :return: None
        """
        import os
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding=self.encoding):
                pass

    def ler_arquivo(self):
        arquivo = {}
        with open(self.arquivo, encoding=self.encoding) as f:
            for linha in f.readlines():
                linha = linha.split("\n")[0].split(",")
                nome = linha[0]
                notas = [float(n) for n in linha[1:]]
                media = round(sum(notas) / len(notas), 1)
                arquivo[nome] = {
                    "notas": notas,
                    "media": media,
                    "info": f"{nome} | {notas} | {media}"
                }
        return arquivo


turma = Turma()
turma.check_file()
turma.definir_informacoes()

while True:
    try:
        turma.exibir_opcoes()
        opt = input("Escolha uma opção acima: ")
        match opt:
            case "1":
                turma.inserir_dados()
            case "2":
                turma.exibir_dados()
            case "3":
                turma.exibir_aprovados()
            case "4":
                turma.exibir_reprovados()
            case "5":
                turma.salvar_dados()
            case "6":
                print_formatado("Programa encerrado")
                break
            case _:
                print(error_message("Opção inválida"))
    except ValueError as err:
        print(error_message(err))
