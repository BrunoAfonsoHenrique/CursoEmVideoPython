soma_idades = 0; maior = 0; qtd = 0; qtd_mulheres = 0
for cont in range(1, 5):
    print('----- {}º PESSOA -----'.format(cont))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    soma_idades += idade
    qtd += 1
    if sexo == 'M':
        if cont == 1:
            maior = idade
        else:
            if idade > maior:
                maior = idade
    if sexo == 'F':
        if idade < 20:
            qtd_mulheres += 1
media = soma_idades / qtd
print('A média de idade do grupo é de {}'.format(media))
print('O homem mais velho tem {} anos'.format(maior))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(qtd_mulheres))
