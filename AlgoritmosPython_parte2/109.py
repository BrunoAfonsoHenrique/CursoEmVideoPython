from random import randint
maior = menor = 0
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')

print(f'\nMaior valor: {max(num)}')
print(f'Menor valor: {min(num)}')
