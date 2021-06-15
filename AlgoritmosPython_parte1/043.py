# <<< Média do Aluno >>>

n1 = float(input('Nota 1 do aluno: '))

n2 = float(input('Nota 2 do aluno: '))

n3 = float(input('Nota 3 do aluno: '))

n4 = float(input('Nota 4 do aluno: '))

media = (n1 + n2 + n3 + n4) / 4

if media < 5:
    print('\033[1;31mAluno Reprovado!')
elif media >= 5 and media <= 6.9:
    print('\033[1;32mAluno em recuperação!')
else:
    print('\033[1;34mAluno Aprovado!')