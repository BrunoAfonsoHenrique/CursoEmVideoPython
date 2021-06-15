ficha = dict()
print('-'*30)
print(f'{"Situação do aluno":^30}')
print('-'*30)
ficha["Nome"] = str(input('Digite o nome do aluno: '))
ficha["Media"] = float(input('Digite a média: '))

if ficha["Media"] <= 4:
    ficha["Situação"] = 'Reprovado'
elif ficha["Media"] <= 6:
    ficha["Situação"] = 'Recuperação'
else:
    ficha["Situação"] = 'Aprovado'
print('-'*30)
for k, v in ficha.items():
    print(f'{k:<10}{v:>20}')
print('-'*30)

