# EMPRESTIMO

print("********EMPRESTIMO CONSIGNADO!********")
# usuario irá realizar algumas entradas no sistema
idade = int(input("Insira a sua idade: "))

# verificando a idade do usuario
if idade >= 18 and idade < 55:
    print("Parabens! Você pode solicitar o emprestimo")
else:
    print("Você não pode realizar o emprestimo")

renda = float(input("Insira a sua renda: "))

# verificando o valor da renda do usuario
if renda > 2000:
    print("Parabens a sua renda é compativel para solicitar o emprestimo")
else:
    print("A sua renda não é compativel com o emprestimo")


tempo_servico = int(input("Insira o tempo de serviço: "))
if tempo_servico >= 2:
    print("Tempo de serviço compativel para o emprestimo")
else:
    print("Tempo de serviço pouco, você terá que aguardar")

    
    #daqui pra baixo está errado a maneira do código
# realizando funçoes para verificar o valor do juros que será utilizado na parcela

def emprestimo_1():
    valor_emprestimo = float(input("Insira o valor do emprestimo: "))
    tempo_pag_parcelas = int(input("Insira os anos de pagamento do emprestimo: "))
    meses = tempo_pag_parcelas * 12 
    parcelas = (valor_emprestimo / meses) * 17
    print("Valor da parcela {}".format(parcelas))
    return parcelas
    

def emprestimo_2():
    valor_emprestimo = float(input("Insira o valor do emprestimo: "))
    tempo_pag_parcelas = int(input("Insira os anos de pagamento do emprestimo: "))
    meses = tempo_pag_parcelas * 12 
    parcelas = (valor_emprestimo / meses) * 22
    print("Valor da parcela {}".format(parcelas))
    return parcelas
    
    
def emprestimo_3():
    valor_emprestimo = float(input("Insira o valor do emprestimo: "))
    tempo_pag_parcelas = int(input("Insira os anos de pagamento do emprestimo: "))
    meses = tempo_pag_parcelas * 12 
    parcelas = (valor_emprestimo / meses) * 14
    print("Valor da parcela {}".format(parcelas))
    return parcelas
    
print("1 - Emprestimo de 500 a 3.500")
print("2 - Emprestimo de 4.000 a 6.000")
print("3 - Emprestimo acima de 6.500")
opcao = int(input("Insira uma opção para ser realizado o emprestimo: "))

match opcao:
    case 1:
        emprestimo_3()
    case 2:
        emprestimo_2()
    case 3:
        emprestimo_1()
    case _:
        print("Opção invalida!") 
