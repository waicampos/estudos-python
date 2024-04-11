from endereco import Endereco


class Cliente:
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__enderecos = []

    def __del__(self):
        print(f"{self.__nome} foi apagado")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def insere_enderecos(self, cidade, estado):
        self.__enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco)