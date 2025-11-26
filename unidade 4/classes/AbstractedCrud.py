import json
class AbstractCrud:
    def detalhar(self):
        return self.__dict__

    def inserir(self):
        lista = self.consultar()
        lista.append(self.detalhar())

        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)

        print('Categoria cadastrada!')

    @classmethod
    def listarTodos(cls):
        lista = cls.consultar()

        for i, p in enumerate(lista):
            print(f'{i} - {p}')
    @classmethod
    def consultar(cls):
        try:    
            with open(cls.arquivo) as file:
                return json.load(file)
        except Exception:
            return []