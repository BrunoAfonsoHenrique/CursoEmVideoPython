qtd_meia = 0; qtd_inteira = 0; r_final_meia = 0; r_final_inteira = 0
for cont in range(1, 500+1):
    idade = int(input('Idade do comprador: '))
    if idade < 18 or idade > 60:
        v_ingresso_meia = 65
        qtd_meia += 1
        r_final_meia = v_ingresso_meia * (qtd_meia)
    else:
        v_ingresso_inteira = 130
        qtd_inteira += 1
        r_final_inteira = v_ingresso_inteira * qtd_inteira
print('Receita final/ meia entrada: R${}'.format(r_final_meia))
print('Receita final/ inteira: R${}'.format(r_final_inteira))