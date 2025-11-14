import data

class Categoria:
    def __init__(self, tipo = ''):
        self.tipo = tipo

    def taxaAgua(self, consumo):
        print('Data da leitura',data.formatarData())
        match self.tipo:
            case 'Clínica': return consumo * 1
            case 'Restaurante': return consumo * 2
            case 'Hotel': return consumo * 2.5


class Imovel:
    imposto = 0.02 # atributo de classe
    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        self.categoria = Categoria()
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

    def detalhar(self):
        return self.__dict__
    def somarAposentos(self):
        return self.quartos + self.suites
    @staticmethod
    def metodoEstatico():
        print('Chamou o método estático sem criar o objeto')
    @classmethod
    def metodoDeClasse(cls):
        print('Chamou o método de classe que vê o imposto', cls.imposto)

categoria = Categoria('Hotel')
hotel1 = Imovel('Hotel do Pedro', 0, 150)
hotel1.categoria = categoria
print(hotel1.categoria.taxaAgua(300))

# casarao = Imovel('Casarão', 3, 4)
# mansao = Imovel('Mansão', 4, 5)
# print(casarao.somarAposentos())
# print(mansao.somarAposentos())
# Imovel.metodoEstatico() # método estático
# Imovel.metodoDeClasse() # método de classe

# print(casarao.__dict__)
# print(mansao.__dict__)
# print(casarao + mansao) # add
# print(casarao > mansao) # gt
# print(casarao < mansao) # lt
# print(casarao) # str