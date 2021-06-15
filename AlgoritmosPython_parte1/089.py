cont = 'SIM'; qtd = soma = 0
maior = menor = 0
while cont != 'NAO':
    num = int(input('Digite um numero: ')) #entrada do valor
    soma = soma + num #soma dos valores
    qtd = qtd + 1 #quantidade de valores
    if qtd == 1: #Aqui começa a verificação do maior e menor valor
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num #Aqui termina a verificação do maior e menor valor
    cont = input('Quer continuar [SIM/NAO]? ').upper().strip() #Aqui pergunta se quer continuar
media = soma / qtd #cálculo da média
print('-='*25)
print('A media de numeros digitados é: {:.2f}'.format(media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))