dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input('Média: '))

print('-='*30)

if dados["Media"] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 <= dados["Media"] < 7:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Reprovado'

for k, v in dados.items():
    print(f'   - {k} é igua a {v}')