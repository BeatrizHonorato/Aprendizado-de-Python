print("======= Agenda =======")

contato = []

def cadastrar_contato():
    nome = str(input("Insira o nome do contato: "))
    telefone = str(input("Insira o numero de telefone: "))
    email = str(input("Insira o email: "))
    contato.append({"nome": nome, "telefone": telefone, "email" : email})

def mostrar_cadastro():
    for i in contato:
        print(i)

def editar_cadastro():
    # esta pedindo o nome do contato que será atualizado
    procurar_contato = str(input("Insira o nome do contato que deseja editar: "))
    for procurar_contato in contato:
        # aqui irá ignorar se o nome esta escrito em letra maiuscula ou minuscula
        if contato[procurar_contato].lower == procurar_contato.lower():
            # contato encontrado dentro da lista contato
            print(f"{procurar_contato} contato encontrado!")
            # o usuario irá inserir o novo nome, telefone e email.
            novo_nome = str(input("Insira o novo nome: "))
            novo_telefone = int(input("Insira o novo telefone: "))
            novo_email = str(input("Insira o novo email: "))
            #Se o usuario digitou algo o valor antigo será substituido pelo novo, mas caso o usuario não digitar nada o valor antigo será mantido
            if novo_nome.strip():
                contato['nome'] = novo_nome
            if novo_telefone.strip():
                contato['telefone'] = novo_telefone
            if novo_email.strip():
                contato['email'] = novo_email
            print("Contato cadastrado com sucesso!")
            return
        print("Contato não encontrado")

def excluir_cadastro():
    nome_exclusao = input("Insira o contato que deseja excluir: ")
    for c in contato:
        if c["nome"].lower() == nome_exclusao.lower():
            contato.remove(c)
            print(f"{nome_exclusao} excluído com sucesso!")
            return
    print("Contato não existe!")


resposta = "s"
while resposta == 's':
    print("1 - Cadastrar contato")
    print("2 - Mostrar cadastro")
    print("3 - Editar cadastro")
    print("4 - Excluir cadastro")
    opcao = int(input("Insira a opção desejada: "))

    match opcao:
        case 1:
            cadastrar_contato()
        case 2: 
            mostrar_cadastro()
        case 3: 
            editar_cadastro()
        case 4: 
            excluir_cadastro()
        case _:
            print("Opção inválida!")
    resposta = str(input("Deseja continuar? s/n"))