numeros = [4, 8, 9, 3]
resultado = []
'''

for n in numeros:
    resultado.append(n*2)

def multiplicar(n):
    return n*2
'''
resultado = map(lambda n: n*2, numeros)
print(numeros, list(resultado))