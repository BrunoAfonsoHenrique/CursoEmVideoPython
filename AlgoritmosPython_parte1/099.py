qtd_1 = qtd_2 = qtd_3 = qtd_4 = qtd_5 = cand = maior = 0
print('\nPrograma intenção de votos')
print('-='*35)

print('Códigos')
print('1 - candidato A')
print('2 - candidato B')
print('3 - candidato C')
print('4 - voto nulo')
print('5 - voto em branco')
print('-='*35)
cod = int(input('Qual a sua intenção de voto [ Digite: -1 < 0 para terminar]: '))

while cod >= 0:
        if cod == 1:
            qtd_1 += 1
        elif cod == 2:
            qtd_2 += 1
        elif cod == 3:
            qtd_3 += 1
        elif cod == 5:
            qtd_5 += 1
        else:
            qtd_4 += 1

        maior = qtd_1
        cand = 'A'

        if qtd_2 > maior:
            maior = qtd_2
            cand = 'B'
        elif qtd_3 > maior:
            maior = qtd_3
            cand = 'C'

        print('-='*35)
        print('Códigos')
        print('1 - candidato A')
        print('2 - candidato B')
        print('3 - candidato C')
        print('4 - voto nulo')
        print('5 - voto em branco')
        print('-=' * 35)
        cod = int(input('Qual a sua intenção de voto [ Digite: -1 < 0 para terminar]: '))

print('-='*30)
print('Quantidade de votos do candidato A: {}'.format(qtd_1))
print('Quantidade de votos do candidato B: {}'.format(qtd_2))
print('Quantidade de votos do candidato C: {}'.format(qtd_3))
print('Quantidade de votos nulos: {}'.format(qtd_4))
print('Quantidade de votos em branco: {}'.format(qtd_5))
print('Primeiro colocado na pesquisa foi o candidato {} com {} votos'.format(cand, maior))