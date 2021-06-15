listagem = ('lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15,
            'Estojo', 25,
            'Tranferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<40}',end='')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-'*50)