print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razao
for cont in range(termo, decimo + razao, razao):
    print('{}'.format(cont), end=' -> ')
print('Acabou')