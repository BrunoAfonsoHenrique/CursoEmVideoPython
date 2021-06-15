frase = str(input('Digite uma frase: ')).upper().strip() #tudo em maiusculo, tira os espaços inuteis
palavras = frase.split() #fatiando as palavras
junto = ''.join(palavras) #juntar as palavras
inverso = '' #inverso = junto[::-1], ira o laço for do código
for cont in range(len(junto) - 1, -1, -1):
    inverso += junto[cont]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndromo.')