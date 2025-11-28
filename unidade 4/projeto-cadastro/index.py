from classes.Produto import Produto

def menu():
    print()
    print('1 - Listar produtos')
    print('2 - Inserir produto')
    print('3 - Alterar produto')
    print('4 - Excluir produto')
    print('0 - Sair')

opcao = 1
while opcao != 0:
    menu()
    opcao = int(input('Excolha uma opção: '))

    match opcao:
        case 1:
            print()
            print('==========Lista de produtos==========')
            Produto.listarTodos()
            print('=====================================')

        case 2:
            codigo = input('Digite o código do produto: ')
            nome = input('Digite o nome: ')
            quantidade = input('Digite a quantidade: ')
            valor = input('Digite o valor: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
        case 3:
            print('==========Lista de produtos==========')
            Produto.listarTodos()
            print('=====================================')
            selecionado = int(input('Qual item deseja alterar? '))
            item = Produto.consultar(selecionado)
            quantidade = int(input('Qual a nova quantidade? '))
            valor = int(input('Qual o novo valor? '))

            produto = Produto(item['codigo'], item['nome'], quantidade, valor)
            produto.alterar(selecionado)
        case 4:
            print('==========Lista de produtos==========')
            Produto.listarTodos()
            print('=====================================')
            selecionado = int(input('Qual item deseja excluir? '))
            Produto.excluir(selecionado)
print()
print('Programa encerrado!')