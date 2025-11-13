class Imovel:
    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
    def __add__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther
    def __gt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther
    def __lt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    def __str__(self):
        return str(self.__dict__)

casarao = Imovel('Casarão', 3, 4)
mansao = Imovel('Mansão', 4, 5)

# print(casarao.__dict__)
# print(mansao.__dict__)
print(casarao + mansao) # add
print(casarao > mansao) # gt
print(casarao < mansao) # lt
print(casarao) # str