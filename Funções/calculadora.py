print("=======Calculado=======")

def soma():
    num1 = float(input("Insira o valor: "))
    num2 = float(input("Insira o valor: "))
    somar = num1 + num2
    print("Valor {}".format(somar))

def subtracao():
    num1 = float(input("Insira o valor: "))
    num2 = float(input("Insira o valor: "))
    subs = num1 - num2
    print("Valor {}".format(subs))

def divisao():
    num1 = float(input("Insira o valor: "))
    num2 = float(input("Insira o valor: "))
    divs = num1/num2
    print("Valor {}".format(divs))

def multiplicacao():
    num1 = float(input("Insira o valor: "))
    num2 = float(input("Insira o valor: "))
    multi = num1 * num2
    print("Valor {}".format(multi))

opcao = int(input("Insira a opção: 1 - Soma / 2 - Subtração / 3 - Divisão / 4 - Multiplicação: "))
match opcao:
    case 1:
        soma()
    case 2:
        subtracao()
    case 3:
        divisao()
    case 4: 
        multiplicacao()