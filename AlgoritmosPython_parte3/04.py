def separador():
    print('-'*45)


def area(larg, comp):
    a = larg * comp
    separador()
    print(f'A área de um tereno {larg}x{comp} é de {a} metros quadrados.')

separador()
print(f'{"CCONTROLE DE TERRENOS": ^45}')
separador()

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)