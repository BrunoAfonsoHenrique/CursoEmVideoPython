termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
cont = 10; qtd = 0
while cont != 0:
    print('{}'.format(termo), end=' -> ')
    termo = termo + razao
    cont = cont - 1
    qtd = qtd + 1
    if cont == 0:
        cont = int(input('\nQuantos termo a mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(qtd))