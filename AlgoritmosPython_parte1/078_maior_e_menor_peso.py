maior = 0
menor = 0
for cont in range(1, 6):
    peso = float(input('Peso da {}º Pessoa: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))
