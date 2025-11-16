import matplotlib.pyplot as plt

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun']
qdtTI = [60, 52, 76, 89, 108, 95]
qdtRh = [40, 72, 17, 28, 87, 56]
'''
plt.plot(meses, qdtTI, label='TI', color='#007fff', linestyle='-', marker='.') # aceita HEX
plt.plot(meses, qdtRh, label='RH', color='red', linestyle='-',marker='.')
plt.title('Chamados abertos')
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.legend()
'''
navegadores = ['Chrome', 'Firefox','Edge']
qtd = [1200, 600, 200]
cores = ['red', 'orange', 'blue']

plt.pie(qtd, labels=navegadores, colors=cores)
plt.show()
