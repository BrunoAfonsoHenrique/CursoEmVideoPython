jogos = dict()
gols = list()
total = 0
jogos['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogos["nome"]} jogou? '))
for cont in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {cont}? ')))
    total += gols[cont]
jogos['gols'] = gols
jogos['total'] = total
print('-='*35)
print(f'{jogos}')
print('-='*35)
for k, v in jogos.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*35)
print(f'O jogador {jogos["nome"]} jogou {len(gols)} partidas.')
for c, v in enumerate(gols):
    print(f'   => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {total} gols.')