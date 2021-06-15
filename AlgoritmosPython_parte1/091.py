cont = 1; qtd = soma = 0
while cont != 0:
    cont = int(input('Numero: '))
    if cont != 0:
        qtd += 1
        soma += cont
media = soma / qtd
print('A soma de todos os valores é {} e a media é {:.2f}'.format(soma, media))