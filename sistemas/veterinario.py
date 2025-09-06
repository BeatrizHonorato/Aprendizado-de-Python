cliente = []

animal = []

def cadastro_cliente():
    id = int(input("Insira o Id do cliente: "))
    nome = str(input(f"Insira o nome do cliente: "))
    cliente.append({"id" : id, "nome" : nome})
    print("Cliente cadastrado com sucesso!")

def cadastro_animal():
    id = int(input("Insira o Id do animal: "))
    id_dono = int(input("Insira o Id do dono do animal: "))
    nome_animal = str(input(f"Insira o nome do animal: "))
    tipo_animal = str(input(f"Insira o tipo do animal: "))
    doenca = str(input("Insira o que o animal tem: "))
    animal.append({"id" : id, "id_dono" : id_dono, "nome_animal" : nome_animal, "tipo_animal" : tipo_animal, "doenca" : doenca})
    print("Animal cadastrado com sucesso!")

def mostrar_clientes():
    for i in cliente:
        print(i)

def mostrar_animal():
    for j in animal:
        print(j)

def excluir_cliente():
    cliente_excluir = str(input("Insira o cliente que deseja excluir: "))
    if cliente_excluir in cliente:
        cliente.remove(cliente_excluir)
        print(f"{cliente_excluir} foi removido com sucesso!")
    else:
        print(f"{cliente_excluir} não encontrado!")
    print("Cadastros atualizados: ", cliente)

def excluir_animal():
    nome_animal = str(input(f"Insira o nome do animal que deseja excluir: "))
    if nome_animal in animal:
        animal.remove(nome_animal)
        print(f"{nome_animal} excluido com sucesso!")
    else:
        print("Animal não encontrado")
    print("Cadastro atualizado ", animal)



resposta = 's'
while resposta == 's':
    print("1 - Cadastro cliente")
    print("2 - Cadastro animal")
    print("3 - Mostrar cliente")
    print("4 - Mostrar animal")
    print("5 - Exclusão cliente")
    print("6 - Exclusão animal")
    print("7 - Sair")
    opcao = int(input("Insira a opção desejada: "))
    match opcao:
        case 1:
            cadastro_cliente()
        case 2: 
            cadastro_animal()
        case 3: 
            mostrar_clientes()
        case 4:
            mostrar_animal()
        case 5:
            excluir_cliente()
        case 6:
            excluir_animal()
        case 7:
            print("Saindo do programa...")
    resposta = str(input("Deseja continuar? s/n: "))
