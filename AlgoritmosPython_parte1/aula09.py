# Aula 09

frase = 'Curso em video Python'

print('\n<<< Fatiamento de String >>>')

print(frase)

print(frase[9])

print(frase[9:13])

print(frase[9:21])

print(frase[9:21:2])

print(frase[:5])

print(frase[15:])

print(frase[9::3])

print('\n<<< Análise >>>')

print(len(frase))

print(frase.count('o'))

print(frase.count('o', 0, 13))

print(frase.find('deo'))
'''Começa na posição 11'''

print(frase.find('Android'))
'''retorna: -1, pois não encontra na string'''

print('Curso' in frase)

print('\n<<< Transformação >>>\n')

print(frase.replace('Python', 'Apple'))

print(frase)

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

frase2 = '   Aprenda Python  '

print(frase2)

print(frase2.strip())

print(frase2.rstrip())

print(frase2.lstrip())

print('\n<<< Divisão >>>\n')

print(frase.split())

print('\n<<< Junção >>>\n')

print('-'.join(frase))

print(''.join(frase))














