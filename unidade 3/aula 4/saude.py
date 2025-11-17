import numpy as np
import pandas as pd

class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

pacientes = {
    'Paciente 1': Paciente('Maria', 25, 'F', 60, 1.7000),
    'Paciente 2': Paciente('Vinicios', 18, 'M', 55, 1.68),
    'Paciente 3': Paciente('João', 45, 'M', 70, 1.85),
    'Paciente 4': Paciente('Ana', 34, 'F', 90, 1.65),
}

l_pacientes = [p.__dict__ for p in pacientes.values()]

df_paciente = pd.DataFrame.from_records(l_pacientes, index=pacientes.keys())

df_paciente['IMC'] = df_paciente.apply(lambda i: i.peso / i.altura ** 2, axis=1)

media = np.mean(df_paciente['IMC'])

sobrepeso = df_paciente[df_paciente['IMC'] > 25]
percentual = len(sobrepeso) / len(df_paciente) * 100

print('Pacientes:')
print(df_paciente)
print()
print(f'Média de IMC: {media}')
print()
print(f'Pacientes com sobrepeso ({percentual}%):')
print(sobrepeso)