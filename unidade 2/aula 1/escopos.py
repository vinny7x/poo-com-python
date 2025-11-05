n1 = 5 # escopo global
n2 = 8
n3 = 7 

def soma(n1, n2):
    n1 = 10 # escopo local
    n2 = 20
    n4 = 9

    print('Função soma: n1:',n1)
    print('Função soma: n2:',n2)
    print('Função soma: n3:',n3)
    print('Função soma: n4:',n4)

soma(n1, n2)
print('n1:',n1)
print('n2:',n2)