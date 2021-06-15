lista = list()
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))

    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])

    print('-=' * 20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('-=' * 35)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*25)

for p, c in enumerate(lista):
    print(f'{p:<4}{c[0]:<10}{c[2]:>8.1f}')
print('-'*25)

while True:
    op = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if op == 999:
        print('Finalizando...')
        break
    if op <= len(lista) - 1:
        print(f'Notas de {lista[op][0]} são: {lista[op][1]}')
print('FIM!!!')
