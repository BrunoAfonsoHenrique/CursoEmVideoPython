cidade = str(input('Digite sua cidade de nascimento: ')).strip().upper()

divisao = cidade.split()
print(divisao[0] == 'SANTO')

'''
<<< Outra forma de fazer >>>

print(cidade[:5] == 'SANTO')

'''