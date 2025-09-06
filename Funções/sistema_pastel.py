print("=======SISTEMA PASTEL=======")

# criando uma lista
clientes = []

# criando uma função 
def cadastro_cliente(Id, Nome, Valor):
    # criando um dicionario
    cliente =  {
        "Id" : Id,
        "Nome" : Nome,
        "Valor" : Valor
    }
    clientes.append(cliente)


# cliente irá realizar a escolha do pastel
print("Escolha o sabor do pastel: ")
print("1 - Queijo")
print("2 - Carne com queijo")
print("3 - Calabreza")
print("Calabreza com catupiry")
print("Bauru")
print("Pizza")

sabor_pastel = str(input("Escolha o sabor do pastel: "))




