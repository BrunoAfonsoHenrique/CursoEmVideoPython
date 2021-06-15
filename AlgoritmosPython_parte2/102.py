print('-='*20)
print('          Jogo Par ou Impar    ')
from random import randint
qtd = 0
while True:
    computador = randint(1, 10)
    print('-='*20)
    jogador = int(input('Diga um valor: '))
    op = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]
    soma = jogador + computador
    if soma % 2 == 0:
        if op == 'P':
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
            print('Você venceu!!!')
            qtd += 1
    else:
        if op == 'I':
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
            print('Você venceu!!!')
            qtd += 1
    if soma % 2 == 0:
        if op == 'I':
            print('-=' * 10)
            print('Você perdeu!!!')
            break
    else:
        if op == 'P':
            print('-=' * 10)
            print('Você perdeu!!!')
            break
print('-='*10)
print(f'GAME OVER! Você venceu {qtd} vezes.')