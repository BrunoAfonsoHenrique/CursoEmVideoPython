colocados = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Fluminense', 'Internacional', 'Palmeiras',
             'Santos', 'Ceará', 'Fortaleza', 'Corinthians', 'Athletico-PR', 'Bahia', 'Bragantino', 'Atlético-GO',
             'Sport', 'Vasco', 'Coritiba', 'Botafogo', 'Goiás')
print('-'*50)
print(f'Os cinco primeiros colocados são {colocados[:5]}')
print('-'*50)
print(f'Os ultimos 4 colocados são {colocados[-4:]}')
print('-'*50)
print(f'Lista com os times em ordem afabética {sorted(colocados)}')
print('-'*50)
print(f'O time Corinthians está na {colocados.index("Corinthians")+1} posição.')
print('-'*50)


