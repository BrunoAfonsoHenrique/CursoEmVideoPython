listagem = ('Arroz', 25000, 'Feijao', 3.45, 'Café', 7.78,
            'Açucar', 5, 'Danone', 9.99, 'Lasanha', 14.70)

print('-'*45)
print('{:^45}'.format('LISTAGEM DE PREÇOS'))
print('-'*45)

for iten in range(0, len(listagem)):
    if iten % 2 == 0:
        print(f'{listagem[iten]:.<32}', end='')
    else:
        print(f'R${listagem[iten]:>10.2f}')

print('-'*45)