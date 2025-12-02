from moedas import get_cotacao
from graficos import grafico_barra, grafico_pizza, grafico_dispersao

def menu():
    print()
    print('1 - Gráfico de barras')
    print('2 - Gráfico de pizza')
    print('3 - Gráfico de dispersão')
    print('0 - Sair')
    print()

menu()

opcao = 1
cotacoes = get_cotacao()

l_moedas = [
    'USD - Dólar Americano',
    'EUR - Euro',
    'GBP - Libra Esterlina',
    'JPY - Iene Japonês',
    'CHF - Franco Suíço',
    'CAD - Dólar Canadense'
]

l_valores = [
    1/cotacoes['USD'],
    1/cotacoes['EUR'],
    1/cotacoes['GBP'],
    1/cotacoes['JPY'],
    1/cotacoes['CHF'],
    1/cotacoes['CAD']
]

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1: grafico_barra(l_moedas, l_valores)
        case 2: grafico_pizza(l_moedas, l_valores)
        case 3: grafico_dispersao(l_moedas, l_valores)
print('Programa encerrado!')