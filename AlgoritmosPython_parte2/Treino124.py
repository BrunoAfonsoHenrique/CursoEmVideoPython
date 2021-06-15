print('-'*30)
print(f'{"TABELA DE PREÇOS":^30}')
print('-'*30)

lista_produtos = dict()

lista_produtos["Alface"] = 0.45
lista_produtos["Batata"] = 1.20
lista_produtos["Tomate"] = 2.30
lista_produtos["Feijão"] = 4.78
print(f'{"PRODUTOS":<15}{"PREÇOS":>15}')
print('-'*30)

for k, v in lista_produtos.items():
    print(f'{k:<15}{v:>15}')
print('-'*30)

while True:
    produto = str(input('Digite o produto que deseja ver o preço [Fim] para encerrar: '))
    if produto == 'Fim':
        break
    if produto in lista_produtos:
        print(f'>>> Preço do {produto} é R${lista_produtos[produto]}')
    else:
        print('Produto não enconrdo.')
print('FIM!!!')
