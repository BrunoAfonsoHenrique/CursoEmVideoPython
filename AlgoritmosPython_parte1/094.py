print('-='*40)
print('Para encerrar o programa a primeira nota deve ser negativa [ nota 1 < 0]')
n1 = int(input('Nota 1: '))
qtd_alunos = 0
while n1 >= 0:
    n2 = int(input('Nota 2: '))
    n3 = int(input('Nota 2: '))
    n4 = int(input('Nota 3: '))

    qtd_faltas = int(input('Qual a quantidade de faltas? '))
    qtd_alunos += 1
    soma = n1 + n2 + n3 + n4

    media = soma / qtd_alunos

    if qtd_faltas > 40:
        print('Aluno reprovado por falta!')
    else:
        if media >= 7:
            print('Aluno Aprovado')
    print('-='*40)
    print('Para encerrar o programa a primeira nota deve ser negativa [ nota 1 < 0]')
    n1 = int(input('Nota 1: '))
print('Fim')
