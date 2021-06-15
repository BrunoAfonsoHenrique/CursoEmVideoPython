Pikachu = {'Tipo': 'Elétrico',
           'Ataques': ['Ataque Rápido', 'Investida Trovão', 'Cauda de Ferro']}

Charmander = {'Tipo': 'Fogo',
              'Ataques': ['Lança-Chamas', 'Rosnar', 'Presas de Fogo']}

Squirtle = {'Tipo': 'Agua',
            'Ataques': ['Rajada de Bolhas', 'Jato De Água', 'Raio de Gelo']}

while True:
    nome = str(input('Deseja ver os dados de qual Pokémon? [Pikachu, Charmander, Squirtle] '))

    if nome == 'Pikachu':
        for k, v in Pikachu.items():
            print(f'Nome: {nome}, Tipo: {Pikachu["Tipo"]}, Ataques: {Pikachu["Ataques"]}')
            break
    if nome == 'Charmander':
        for k, v in Pikachu.items():
            print(f'>>> Nome: {nome}, Tipo: {Charmander["Tipo"]}, Ataques: {Charmander["Ataques"]}')
            break
    if nome == 'Squirtle':
        for k, v in Pikachu.items():
            print(f'>>> Nome: {nome}, Tipo: {Squirtle["Tipo"]}, Ataques: {Squirtle["Ataques"]}')
            break
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('-' * 100)
