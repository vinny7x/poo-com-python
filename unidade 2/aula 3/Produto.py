class Produto:
    def __init__(self, nome, valor, marca = '', modelo = ''):
        self.nome = nome
        self.valor = valor
        self.marca = marca
        self.modelo = modelo

produto0 = Produto('Celular', 3000, 'Samsung', 'J8 Core')
produto1 = Produto('Geladeira', 10000, 'Brastemp', 'BRST9000')
produto2 = Produto('Notebook', 3600, 'Acer')
print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)
