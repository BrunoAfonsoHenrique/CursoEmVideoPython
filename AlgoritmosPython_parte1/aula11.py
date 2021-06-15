'''
 <<< Cores no terminal >>>
print('\033[4;30;45mOlá, mundo!\33[m')

'''

'''
a = 3
b = 5
print('\033[31m<<< Cores no terminal >>>\033[m\n')
print('Oa valores são \033[33m{}\033[m e \033[31m{}\033[m !!!'.format(a , b))


'''
'''
nome = 'Bruno'
print('Olá, Muito prazer {}{}{} !!!'.format('\033[4;34m', nome, '\033[m'))
'''

nome = 'Bruno'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}
print('Olá, Muito prazer {}{}{} !!!'.format(cores['amarelo'], nome, cores['azul']))