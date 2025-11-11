from abc import ABC, abstractclassmethod
class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, nome):
            self._nome = nome
        '''
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome
        '''
    def detalhar(self):
        print(self.__dict__)

    def calcularImposto(self):
        return self.valor * 0.02

    @abstractclassmethod # contrato das classes filhas com a classe pai
    def aluguelSugerido(self):
        ...
class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        super().__init__( nome, uf, valor, endereco = '', area = '')
        self.quartos = 0
        self.piscina = False
    def aluguelSugerido(self):
        return self.valor * 0.01

class ImovelComercial(Imovel):
    def aluguelSugerido(self):
        return self.valor * 0.015

class ImoveRural:
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self.hectares = hectares
        self.curral = curral
        self.produtiva = produtiva
    def MesDePlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')
class Fazenda(Imovel, ImoveRural):
    def aluguelSugerido(self):
        return self.valor * 0.025

'''
fazenda = Fazenda('Fazenda Modelo', 'GO', 1500000)
fazenda.detalhar()
print(fazenda.calcularImposto())
fazenda.MesDePlantacao(2)
'''

casa = ImovelResidencial('Minha casa', 'BA', 300000)
casa.nome = 'Casa legal'
print(casa.nome)
# casa.setNome('Casa legal')
# print(casa.getNome())
casa.detalhar()
print(casa.aluguelSugerido())

clinica = ImovelComercial('Clinica X', 'SP', 800000)
# clinica.detalhar()
'''  # Não é possível instanciar uma classe abstrata
imovel = Imovel('Solar do Cerrado', 'DF', 500000)
imovel.detalhar()
'''
'''
imovel.endereco = 'ABC'
imovel.area = '2000'
'''