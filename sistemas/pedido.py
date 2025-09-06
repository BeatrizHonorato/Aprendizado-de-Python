cadastro = []

def cadastro_cliente(nome, saldo, deposito):

    nome = str(input("Insira o nome do cliente: "))
    saldo = float(input("Insira o saldo da conta: "))
    deposito = float(input("Insira o valor do deposito: "))
    cliente = {
        "nome" : nome,
        "saldo" : saldo,
        "deposito" : deposito
    }
    cadastro.append(cliente)
    print("Cliente cadastrado com sucesso!")

def mostrar_cadastro():
    if not cadastro:
        print("Não tem nenhum cliente cadastrado!")
    else: 
        print("Lista de clientes:")
        for cliente in cadastro:
            print(cliente)

resposta = "sim"
while resposta == "sim":
    print("1 - Cadastrar cliente")
    print("2 - Mostrar clientes cadastrados")
    print("3 - Sair")

    opcao = int(input("Insira uma opção: "))
    match opcao:
        case 1:
            cadastro_cliente()
        case 2: 
            mostrar_cadastro()
        case 3:
            print("Saindo do programa...")
    resposta = str(input("Deseja continuar? sim/não"))