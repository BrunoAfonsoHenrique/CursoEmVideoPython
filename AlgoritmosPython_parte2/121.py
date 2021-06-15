from random import randint
lista = list()
jogos = list()
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
cont2 = 1
while cont2 <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    cont2 += 1
for p, c in enumerate(jogos):
    print(f'{p+1}: {c}')



