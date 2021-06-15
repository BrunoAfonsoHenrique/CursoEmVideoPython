from random import randint

numeros = list()

def sorteia():

    for cont in range(0, 5):
        numeros.append(randint(0, 9))
    print(f'Sorteando {len(numeros)} valores da lista: ', end='')
    for cont in numeros:
        print(f'{cont}', end=' ')
    print('Pronto!')

def somaPar():
    soma = 0
    for cont in numeros:
        if cont % 2 == 0:
            soma += cont
    print(f'Somando os valores pares de {numeros}, temos {soma}')
sorteia()
somaPar()



