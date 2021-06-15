temp = dict()
cadastro = list()
soma = 0
while True:
    temp['nome'] = str(input('Digite o nome: '))
    temp['sexo'] = str(input('digite o Sexo: ')).upper()
    temp['idade'] = int(input('Digite a idade: '))
    cadastro.append(temp.copy())
    soma += temp['idade']
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*35)
print(f'- O grupo tem {len(cadastro)} pessoas.')
media = soma / len(cadastro)
print(f'- A média de idade é de {media:5.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for k in cadastro:
    if k['sexo'] == 'F':
        print(f'{k["nome"]}', end='')
print()
print('- Lista das pessoas que estão acima da média:')
for p in cadastro:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('FIM!!!')