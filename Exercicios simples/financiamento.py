# FINANCIAMENTO

idade = int(input("Insira a idade: "))
anos_serviço = float(input("Insira o tempo de serviço: "))

valor_imovel = float(input("Insirao o valor do imovel: "))
tempo_pag = float(input("Insira os anos de pagamento do imovel: "))

meses_trabalhados = anos_serviço * 12
dias_trabalhos = meses_trabalhados * 30

if idade >= 18 and idade < 50:
    print(f"A sua idade {idade} é ideal para o financiamento ", idade)
else:
    print("Você não pode realizar o financiamento!")

if dias_trabalhos > 180:
    print("Parabens! Você tem tempo de serviço suficiente para o financiamento.")
else:
    print("Infelizmente você não tem tempo de serviço suficiente! Aguarde mais alguns meses")


quantidade_parcelas = (tempo_pag * 12)

valor_parcela = valor_imovel/quantidade_parcelas

print("Valor da parcela: ", valor_parcela)
print("Tempo do pagamento do imovel: ", quantidade_parcelas)




    