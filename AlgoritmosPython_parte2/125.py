dados = dict()
from datetime import datetime

dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
dados['idade'] = datetime.now().year - dados['nascimento']
if dados['carteira'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 35 ) - datetime.now().year
print('-='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')


