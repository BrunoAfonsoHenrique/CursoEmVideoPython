teste = list()
teste.append('Bruno')
teste.append(26)
print(teste)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
print('-'*35)
#---------------------------------------------------------------------
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Bruno', 26]]
print(galera)
print(galera[3][0])

for p in galera:
    print(p[0])
print('-'*35)
#-------------------------------------------------------------------------

galera = list()
dado = list()

for d in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print('-'*35)
#-----------------------------------------------------------
galera = list()
dado = list()
totmai = totmen = 0

for d in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
