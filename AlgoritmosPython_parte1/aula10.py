'''

nome = str(input('Qual o seu nome: '))

if nome == 'Bruno':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é legal.')
print('Bom dia, {}'.format(nome))

'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
