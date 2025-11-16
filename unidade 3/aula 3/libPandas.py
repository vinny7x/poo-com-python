import pandas as pd

cidades = [
    {'nome': 'Distrito Federal', 'uf': 'DF', 'populacao': 2817381},
    {'nome': 'São Paulo', 'uf': 'SP', 'populacao': 11451999},
    {'nome': 'Rio de Janeiro', 'uf': 'RJ', 'populacao': 16055174},
    {'nome': 'Recife', 'uf': 'PE', 'populacao': 1488920}
]

dataFrame = pd.DataFrame(cidades)
ordenada = dataFrame.sort_values(by='populacao', ascending=False)
print(ordenada)
print()
print(ordenada.head(2))