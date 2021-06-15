qtd = 0; qtd_n_eleitores = 0; soma = 0
for cont in range(1, 500+1):
    idade = int(input('Idade: '))
    if idade >= 16:
        qtd += 1
    else:
        qtd_n_eleitores += 1
        soma += idade
media = soma / qtd_n_eleitores
print('Quantidade de alunos que podem ser eleitore {}'.format(qtd))
print('Média de idade dos alunos que não podem ser eleitores: {}'.format(media))
