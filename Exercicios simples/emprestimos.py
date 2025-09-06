anos_emprestimo = int(input("Insira os anos do emprestimo: "))

valor_emprestimo = float(input("Insira o valor do emprestimo: "))


meses_emprestimo = anos_emprestimo * 12

valor_parcela = valor_emprestimo/meses_emprestimo

print("Quantidade de meses {} ".format(meses_emprestimo))
print("Valor da parcela {} ".format(valor_parcela))

