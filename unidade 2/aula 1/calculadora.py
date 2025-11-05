def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    if n2 == 0:
        return 'Não é possivel fazer divisões por 0!'
    else:
        resultado = n1/n2
        # print(f'{n1} / {n2} = {resultado}')
        return resultado

def multiplicar(n1, n2):
    return n1 * n2

def calcular(n1, n2, operador):
    match operador:
        case '+': return somar(n1, n2)
        case '-': return subtrair(n1, n2)
        case '*': return multiplicar(n1, n2)
        case '/': return dividir(n1, n2)
        case other: return 'Operador inválido'

print(calcular(90,10, '-'))