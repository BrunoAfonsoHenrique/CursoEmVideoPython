from random import randint

num_sorteado = randint(0, 5)

num = int(input('Digite um numer entre 0 e 5: '))

if num == num_sorteado:
    print('Você venceu. Número sorteado foi {}'.format(num_sorteado))
else:
    print('Você perdeu. Numero sorteado foi {}'.format(num_sorteado))

