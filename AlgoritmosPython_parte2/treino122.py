lista = list()
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))

    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja coninuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('--'*12)
print('-='*35)
print(f'{"No":<5}{"NOME":<10}{"MÉDIA":<8}')
print('--'*12)

for e, i in enumerate(lista):
    print(f'{e:<5}{i[0]:<10}{i[2]:<8.1f}')
print(print('--'*20))

while True:
    op = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if op == 999:
        print('Finalizando...')
        break
    if op <= len(lista) - 1:
        print(f'Notas de {lista[op][0]} são: {lista[op][1]}')
    print('--'*35)
print('FIM!!!')
