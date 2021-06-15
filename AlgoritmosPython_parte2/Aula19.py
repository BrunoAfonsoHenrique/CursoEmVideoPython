'''

pessoas = {'nome': 'Bruno', 'sexo': 'M', 'idade': 26}
print(pessoas)

print(pessoas['nome'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())

print(pessoas.values())

print(pessoas.items())

print('-='*30)

for k in pessoas.keys():
    print(k)

print('-='*30)

for k, v in pessoas.items():
    print(f'{k} = {v}')

#Adicinando elemento

pessoas['peso'] = 98.5
print(pessoas)
'''

#Criando um dicionario dentro de uma lista

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])

print('-='*30)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()



