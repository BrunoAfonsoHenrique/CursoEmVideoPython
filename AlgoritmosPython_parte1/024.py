from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

alunos = [n1, n2, n3, n4]

shuffle(alunos)

print('A ordem de apresentação será: {}'.format(alunos))