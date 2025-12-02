import matplotlib.pyplot as plt
from moedas import get_cotacao

cotacoes = get_cotacao()

l_moedas = [
    'USD - Dólar Americano',
    'EUR - Euro',
    'GBP - Libra Esterlina',
    'JPY - Iene Japonês',
    'CHF - Franco Suíço',
    'CAD - Dólar Canadense',
    'AUD - Dólar Australiano',
    'NZD - Dólar Neozelandês',
    'CNY - Yuan Chinês',
    'ARS - Peso Argentino',
    'MXN - Peso Mexicano',
    'SEK - Coroa Sueca',
    'NOK - Coroa Norueguesa'
]

l_valores = [
    1/cotacoes['USD'],
    1/cotacoes['EUR'],
    1/cotacoes['GBP'],
    1/cotacoes['JPY'],
    1/cotacoes['CHF'],
    1/cotacoes['CAD'],
    1/cotacoes['AUD'],
    1/cotacoes['NZD'],
    1/cotacoes['CNY'],
    1/cotacoes['ARS'],
    1/cotacoes['MXN'],
    1/cotacoes['SEK'],
    1/cotacoes['NOK']
]

def grafico_barra(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores)
    plt.title('Conversões para Real brasileiro')
    plt.xlabel('Moedas')
    plt.ylabel('BRL - Real brasileiro')
    plt.show()

def grafico_pizza(l_moedas, l_valores):
    plt.pie(l_valores, labels=l_moedas)
    plt.title('Proporção em relação ao Real brasileiro')
    plt.show()

def grafico_dispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Conversões para Real brasileiro')
    plt.xlabel('Moedas')
    plt.ylabel('BRL - Real brasileiro')
    plt.show()

grafico_barra(l_moedas, l_valores)