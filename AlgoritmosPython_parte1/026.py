nome = str(input('Digite seu nome completo: ')).strip()

print('O nome em letras maiusculas é {}'.format(nome.upper()))

print('O nome em letras minusculas é {}'.format(nome.lower()))

print('O nome ao todo {} letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()
print('O primeiro nome {} tem {} letras'.format(separa[0], len(separa[0])))

