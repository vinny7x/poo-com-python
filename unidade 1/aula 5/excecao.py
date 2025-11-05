# try: 

#     n1 = int(input("Número 1: "))
#     n2 = int(input("Número 2: "))

#     resultado = n1 / n2
#     print(f"O resultado da divisão é {resultado}")
# except Exception as erro:
#     print(f'Ocorreu um erro: {erro}')
try:
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

    resultado = n1 / n2
    print(f"O resultado da divisão é {resultado}")
except ValueError:
    print("favor inserir apenas números")
except ZeroDivisionError:
    print("Não é possível dividir um número por 0")
except Exception:
    print("Um erro inesperado aconteceu")
else:
    print("O programa foi executado corretamente")
finally: # Independente se deu erro ou não
    print("Fim do código")