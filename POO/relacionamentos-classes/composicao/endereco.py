class Endereco:
    def __init__(self, cidade, estado) -> None:
        self.__cidade = cidade
        self.__estado = estado

    def __del__(self):
        print(f"{self.__cidade} / {self.__estado} foi apagado")

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    def __repr__(self) -> str:
        return f'Endereco: {self.__cidade} / {self.__estado}'