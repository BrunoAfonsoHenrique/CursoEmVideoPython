nomes = ('Objetivo', 'Livro', 'Problemas', 'Solucionados', 'Computador')

for cont in nomes:
    print(f'\nPalavra: {cont.upper()}', end=' ')

    for letras in cont:
        if letras in 'aeiou':
            print(f'{letras}', end=' ')

