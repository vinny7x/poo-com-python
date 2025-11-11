from abc import ABC, abstractclassmethod
class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome
        self._uf = uf
        self._valor = valor
        self._endereco = endereco
        self._area = area

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, nome):
            self._nome = nome
        @property
        def uf(self):
            return self._uf

        @uf.setter
        def uf(self, uf):
            self._nome = _uf
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
        self._quartos = 0
        self._piscina = False
    def aluguelSugerido(self):
        return self._valor * 0.01

class ImovelComercial(Imovel):
    def aluguelSugerido(self):
        return self._valor * 0.015

class ImoveRural:
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self._hectares = hectares
        self._curral = curral
        self._produtiva = produtiva
    def MesDePlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')
class Fazenda(Imovel, ImoveRural):
    def aluguelSugerido(self):
        return self.valor * 0.025


casa = ImovelResidencial('Minha casa', 'BA', 300000)
casa.nome = 'Casa legal'
casa.uf = 'SP'
print(casa.nome)
casa.detalhar()
print(casa.aluguelSugerido())
