def dividir(n1,n2):
    if n2 == 0:
        print('Não é possivel fazer divisões por 0!')
    else:
        resultado = n1/n2
        # print(f'{n1} / {n2} = {resultado}')
        return resultado

divisao = dividir(10,20)
print(f'O resultado da divisão é: {divisao}')

resultado = dividir(30, 5)
soma = 20 + resultado
print(f'A soma é: {soma}')