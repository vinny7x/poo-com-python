numeros = [10,20,30,17]
# print(numeros[3])

carros = [
    "Pálio", "Gol", "Virtus", "Ka", "Onix",
    "Civic", "Corolla", "Fiesta", "Uno", "HB20",
    "Cruze", "Argo", "Compass", "Renegade", "T-Cross"
]
print(carros)
print(len(carros)) # tamanho da array

carros.append("Combi") # adiciona itens ao final do array
print(carros)

carros.remove("Gol") # remove itens do array
del carros[3]
print(carros)

carros = sorted(carros) # ordenando lista
print(carros)

for carro in carros:
    print(carro)