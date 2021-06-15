palavras = ('aprender', 'programar', 'linguagem', 'Python',
            'curso', 'gratis', 'studar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for cont in palavras:
    print(f'\nNa palavra {cont.upper()} temos: ', end='')
    for vogais in cont:
        if vogais.lower() in 'aeiou':
            print(f'{vogais}', end=' ')