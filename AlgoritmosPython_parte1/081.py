from random import randint
from time import sleep
num_sorteado = randint(0, 10)
num = 0; cum = 0
print('-='*4)
print('  GAME')
print('-='*4)
sleep(1)
print('Pensando em um numero...')
sleep(1)
while num != num_sorteado:
    num = int(input('Digite um numero entre 0 e 10: '))
    cum += 1
print('-='*20)
print('Foi necessário {} tentativas para acertar.'.format(cum))