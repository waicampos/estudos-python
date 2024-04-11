class Produto:
    def __init__(self, nome, valor) -> None:
        self.__nome = nome
        self.__valor = valor

    def __del__(self):
        print("Deletando Produto: {nome} -> {valor}")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor
