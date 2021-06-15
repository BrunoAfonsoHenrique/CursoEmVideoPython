from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10))

print('-'*40)
print(f'>>> Numeros gerados: {numeros}')
print('-'*40)

print(f'>>> Menor valor na lista: {min(numeros)}')
print(f'>>> Maior valor na lista: {max(numeros)}')
print('-'*40)