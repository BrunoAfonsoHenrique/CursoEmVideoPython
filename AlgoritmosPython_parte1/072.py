num = int(input('Digite um numero: '))
qtd_pares = 0
soma_impares = 0
qtd_impares = 0
for cont in range(1, num+1):
    if cont % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1
        soma_impares = (soma_impares + cont)
        media = soma_impares / qtd_impares
print('Quantidade de numeros pares: {}'.format(qtd_pares))
print('Média de numeros impares: {:.2f}'.format(media))
