cadastrei = []


def realizar_cadastro():
    nome = str(input("Insere o nome do cliente: "))
    cadastrei.append(nome)

def mostrar_cadastro():
    for i in cadastrei:
        print(i)

resposta = "sim"
while resposta == 'sim' :
    print("1 - Realizar cadastro")
    print("2 - Mostrar cadastro")
    print("3 - Sair")
    opcao = int(input("Insira a opção desejada: "))

        
    match opcao:
        case 1:
            realizar_cadastro()
        case 2:
            mostrar_cadastro()
        case 3: 
            print("Saindo do programa...")
    resposta = str(input("Deseja continuar? sim/nao: "))
        
