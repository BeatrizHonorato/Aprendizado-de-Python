
def somatoria():
    num1 = float(input("Insira um numero: "))
    num2 = float(input("Insira um numero: "))
    soma = num1 + num2
    print("SOMA: {}".format(soma))

def subtracao():
    num1 = float(input("Insira um numero: "))
    num2 = float(input("Insira um numero: "))
    subt = num1 - num2
    print("SUBTRAÇÃO: {}".format(subt))

def multiplicacao():
    num1 = float(input("Insira um numero: "))
    num2 = float(input("Insira um numero: "))
    multi = num1 * num2
    print("MULTIPLICAÇÃO: {}".format(multi))

def divisao():
    num1 = float(input("Insira um numero: "))
    num2 = float(input("Insira um numero: "))
    dividir = num1 / num2
    print("DIVISÃO: {}".format(dividir))
    
resposta = "nao"
while resposta != "sim":

    print("========== CALCULADORA ==========")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    opcao = int(input("Insira a conta que voce deseja: "))
    match opcao:
        case 1:
            somatoria()
        case 2:
            subtracao()
        case 3:
            multiplicacao()
        case 4:
            divisao()
    resposta = str(input("Deseja continuar? sim/nao"))