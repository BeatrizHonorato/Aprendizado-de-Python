clientes = []

def cadastro_cliente(nome, cpf, saldo):
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "saldo": saldo
    }
    clientes.append(cliente)

# cadastrando cliente
cadastro_cliente("Maria", "123456", 100)
cadastro_cliente("zeze", "9822820", 800)

# mostrando clientes cadastrados
for cliente in clientes:
    print(cliente)
