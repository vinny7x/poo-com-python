continuar = True
while continuar:
    numero = int(input("Qual tabuada? "))

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*1}")

    continuar = input("Deseja continuar? (S/n)")
    continuar = True if continuar == 's' else False