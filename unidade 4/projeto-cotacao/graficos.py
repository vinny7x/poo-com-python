import matplotlib.pyplot as plt

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
