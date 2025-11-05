arquivo = open('pessoas.txt', 'a+')

arquivo.write("João\n")
arquivo.write("Pedro\n")

arquivo.close()

with open('pessoas.txt', 'r+') as arquivoLeitura:
    
    for linha in arquivoLeitura:
        print(linha)