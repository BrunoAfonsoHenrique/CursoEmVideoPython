nome = str(input('Qual é seu nome? ')).upper()

cores = {
    'vermelho': '\033[1;31m',
    'limpa': '\033[m'
}

if nome == 'BRUNO':
    print('Que nome bonito {}{}'.format(cores['vermelho'], nome))
elif nome == 'FERNANDO' or nome == 'PEDRO' or nome == 'JEFERSON':
    print('Seu nome é bem popular no Brasil {}{}{} kkk...'.format(cores['vermelho'], nome, cores['limpa']))
elif nome in 'ANA PAULA CLÁUDIA':
    print('Belo nome {}'.format(cores['vermelho'], nome))
else:
    print('Seu nome é bem comum {}{}'.format(cores['vermelho'], nome))
