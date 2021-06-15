n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = n1 + n2

cores = {'vermelho': '\033[31m',
         'fim': '\033[m'}

print('\nA soma entre {} e {} resulta no valor {}{}{} !!!'.format(n1, n2, cores['vermelho'], soma, cores['fim']))