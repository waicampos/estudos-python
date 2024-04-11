class Escritor:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__ferramenta = None
        print("<<Criando Escritor>>")

    def __del__(self):
        print("<<Destruindo Escritor>>")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
