sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo [M/F]: ').upper()
if sexo == 'F':
    print('O sexo digitado é: [{}] Feminino'.format(sexo))
else:
    if sexo == 'M':
        print('O sexo digitado é: [{}] Masculino'.format(sexo))