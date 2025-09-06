print("========= BANCO =========")

# Usuário informa saldo.
# Opções de saque, depósito, transferência.
# Não deixar sacar mais do que tem.

cadastro_cliente = []

def cadastro():
    nome = str(input("Insira o nome: "))
    conta = str(input("Insira a conta: "))
    saldo = float(input("Insira o saldo bancario: "))
    cadastro_cliente.append({"nome" : nome, "conta" : conta, "saldo" : saldo})

def acessar_conta():
    numero_conta = str(input("Insira o numero da conta: "))
    for numero_conta in cadastro_cliente:
        if cadastro_cliente[numero_conta].lower == numero_conta.lower():
            print("Conta {} localizada".format(numero_conta))
        else:
            print("Conta {} não encontrada!".format(numero_conta))
            break


def deposito():
    acessar_conta()
    dep = float(input("Insira o valor do deposito: "))
    saldo += dep
    print("Saldo atual: {}".format(saldo))


    
    

    