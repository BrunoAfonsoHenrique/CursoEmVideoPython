colocados = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Grêmio',
             'Fluminense', 'Internacional', 'Palmeiras', 'Santos',
             'Ceará', 'Fortaleza', 'Corinthians', 'Chapecoense',
             'Bahia', 'Bragantino', 'Atlético-GO', 'Sport',
             'Vasco', 'Coritiba', 'Botafogo', 'Goiás')

print(f'Cinco primeiros colocados: {colocados[:5]}')
print(f'Ultimos quatro colocados: {colocados[-4:]}')
print(f'Ordem alfabética: {sorted(colocados)}')
print(f'Posição que esta o time da Chapecoense: {colocados.index("Chapecoense")+1}')
