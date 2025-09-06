
clientes = ['Zeze']

def cadastro_clientes():
    novo_cliente = str(input("Insira o nome do cliente: "))
    for i in clientes:
        clientes.append(novo_cliente)

def listar_nomes():
    for i in clientes:
        print(i)

opcao = int(input("Insira a opção desejada: "))
match opcao:
    case 1:
        cadastro_clientes()
    case 2:
        listar_nomes()
