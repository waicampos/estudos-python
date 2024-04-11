class Caneta:
    def __init__(self, marca) -> None:
        print("<<Criando Caneta>>")
        self.__marca = marca

    def __del__(self):
        print("<<Destruindo Caneta>>")

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def escrever(self):
        print("Caneta está escrevendo...")
