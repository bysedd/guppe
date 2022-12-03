# coding=utf-8
from functions import error_message, print_formatado, confirm


class Agenda:
    def __init__(self):
        self.opcoes = {
            1: "Inserir contato",
            2: "Remover contato",
            3: "Pesquisar contato pelo nome",
            4: "Listar todos os contatos",
            5: "Listar os contatos cujo nome inicia com uma dada letra",
            6: "Imprimir os aniversariantes do mês",
            7: "Sair"
        }
        self.arquivo = "agenda-de-contatos.txt"
        self.encoding = "utf-8"

    def ler_arquivo(self):
        """
        Lê o arquivo e salva num dicionário.
        :return: Retorna um dicionário contendo as informações no arquivo
        """
        contatos = {}
        with open(self.arquivo, encoding=self.encoding) as f:
            for i, linha in enumerate(f.readlines()):
                nome_f, tel_f, niver_f = linha.split("\n")[0].split(",")
                contatos[nome_f] = {"telefone": tel_f, "aniversário": niver_f}
        return contatos

    def inserir_contato(self, contatos: dict = None):
        """
        Adicionar contato no arquivo.
        :param contatos: Dicionário contendo todos os dados do arquivo
        :return: None
        """
        if contatos is None:
            contatos = {}

        if not contatos:
            print_formatado("Inserir contato")
            continuar = True

            while continuar:
                n = input("Nome: ").strip().title()
                tel = input("Telefone: ").strip()
                niver = input("Aniversário (dd/mm): ").strip()
                if n and tel and niver:
                    nome, telefone, aniversario = n, tel, niver
                    contatos = self.ler_arquivo()
                    string = ""

                    for k, v in contatos.items():
                        string += f"{k},{v['telefone']},{v['aniversário']}\n"
                    string += f"{nome},{telefone},{aniversario}\n"

                    with open(self.arquivo, "w", encoding=self.encoding) as f:
                        f.write(string)
                else:
                    print(error_message("Não foi possível adicionar o contato. Falta de informações"))
                continuar = confirm("Quer adicionar mais contatos (y/n)? ")
        else:
            string = ""

            for k, v in contatos.items():
                string += f"{k},{v['telefone']},{v['aniversário']}\n"

            with open(self.arquivo, "w", encoding=self.encoding) as f:
                f.write(string)

    def remover_contato(self):
        """
        Remove o contato do arquivo pelo nome.
        :return: None
        """
        print_formatado("Remover contato")
        contatos = self.ler_arquivo()
        continuar = True

        while continuar:
            n = input("Digite o nome do contato que quer remover: ").strip().title()

            if n:
                count = self.pesquisar(nome=n, return_count=True)
                if count == 1:
                    remover = confirm("Deseja remover este contato (y/n)? ")
                    if remover:
                        for k, v in contatos.items():
                            if k == n:
                                del(contatos[k])
                                break
                        self.inserir_contato(contatos)
                        print("Contato removido!")
                elif count > 1:
                    print("Mais de um contato foi encontrado, escolha o que quer remover e tente novamente.\n")
                    continue
                else:
                    print(error_message("Nenhum contato encontrado".center(80)))
            else:
                print(error_message("Não foi possível remover o contato. Nome inválido"))
            continuar = confirm("Quer remover mais contatos (y/n)? ")
            print()

    def pesquisar_contato_nome(self, n: str = ""):
        """
        Pesquisa o contato pelo nome
        :param n: Nome (opcional, podendo ser definido antecipadamente)
        :return: None
        """
        print_formatado("Pesquisar contato pelo nome")
        continuar = True

        while continuar:
            if not n:
                n = input("Digite o nome do contato que quer pesquisar: ")
            if not len(n):
                print(error_message("Nome inválido"))
            else:
                self.pesquisar(nome=n)
            continuar = confirm("Quer pesquisar mais contatos (y/n)? ")

    def listar_contatos(self):
        """
        Lista todos os contatos presentes no arquivo.
        :return: None
        """
        print_formatado("Listar todos os contatos")
        contatos = self.ler_arquivo()
        [print(f"{k} | {v['telefone']} | {v['aniversário']}".center(80)) for k, v in contatos.items()]
        print()

    def listar_contatos_letra(self):
        """
        Lista os contatos com uma determinada letra.
        :return: None
        """
        from string import ascii_letters

        print_formatado("Listar os contatos com uma determinada letra")
        continuar = True

        while continuar:
            try:
                le = input("Digite a letra do contato que quer pesquisar: ")[0]
                if not len(le) or le.isnumeric() or le not in ascii_letters:
                    raise TypeError
                self.pesquisar(letra=le)
            except (TypeError, IndexError):
                print(error_message("Letra inválida"))
            finally:
                continuar = confirm("Quer pesquisar mais contatos (y/n)? ")
                print()

    def imprimir_aniversariantes(self):
        """
        Imprime os aniversariantes do mês atual.
        :return: None
        """
        from datetime import date

        print_formatado("Imprimir os aniversariantes do mês")
        contatos = self.ler_arquivo()
        [print(f"{k} | {v['telefone']} | {v['aniversário']}".center(80)) for k, v in contatos.items()
         if int(v["aniversário"].split("/")[-1]) == date.today().month]

    def exists(self):
        """
        Cria o arquivo se ele não existir na pasta atual.
        :return: None
        """
        import os
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding=self.encoding):
                pass

    def mostrar_opcoes(self):
        """
        Mostra as opções da agenda.
        :return: None
        """
        [print(k, v, sep=" - ") for k, v in self.opcoes.items()]

    def pesquisar(self, nome="", letra="", return_count=False):
        """
        Faz uma pesquisa no arquivo, usando uma letra ou um nome.
        :param nome: nome
        :param letra: letra
        :param return_count: retornar contagem?
        :return: Retorna a contagem de vezes em que a letra ou o nome aparece no arquivo
        """
        contatos = self.ler_arquivo()
        count = 0

        if nome:
            nome = nome.strip().lower()
            print(f"Contatos com o nome '{nome}':")
            for k, v in contatos.items():
                if nome in k.lower():
                    print(f"{k} | {v['telefone']} | {v['aniversário']}".center(80))
                    count += 1
            if not count:
                print(error_message("Nenhum contato encontrado".center(80)))
        elif letra:
            count = 0
            letra = letra.strip().lower()[0]
            print(f"Contatos com a letra '{letra}':")
            for k, v in contatos.items():
                if letra in k.lower():
                    print(f"{k} | {v['telefone']} | {v['aniversário']}".center(80))
                    count += 1
            if not count:
                print(error_message("Nenhum contato encontrado".center(80)))
        if return_count:
            return count


agenda = Agenda()
agenda.exists()

while True:
    agenda.mostrar_opcoes()
    option = int(input("Escolha uma opção: "))

    match option:
        case 1:
            agenda.inserir_contato()
        case 2:
            agenda.remover_contato()
        case 3:
            agenda.pesquisar_contato_nome()
        case 4:
            agenda.listar_contatos()
        case 5:
            agenda.listar_contatos_letra()
        case 6:
            agenda.imprimir_aniversariantes()
        case 7:
            print_formatado("Programa encerrado")
            break
        case _:
            print(error_message("Opção inválida"))
