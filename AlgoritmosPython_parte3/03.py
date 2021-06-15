def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1


valores = [7, 2, 6, 14, 5, 23]
dobra(valores)
print(valores)