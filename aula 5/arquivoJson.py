import json

pessoas = [
    {'nome': 'Vinny', 'telefone': '(99) 99999-9999', 'endereco': 'Rua dos bobos n° 0'},
    {'nome': 'Carlos', 'telefone': '(99) 12345-6789', 'endereco': 'Rua dos bobos n° 45'},
    {'nome': 'Maria', 'telefone': '(99) 54321-6789', 'endereco': 'Rua dos bobos n° 90'}
]

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4)