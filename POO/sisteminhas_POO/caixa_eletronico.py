class Caixa:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        

    
    def depositar(self):
        valor = float(input("Insira o valor: "))
        self.saldo += valor
        return self.saldo
    
    def sacar(self):
        saque = float(input("Insira o valor do saque: "))
        if self.saldo >= saque:
            self.saldo -= saque
            print("Aguarde...")
            print(f"Liberando valor: {saque}")
        else:
            print("Saque inválido! Sem limite")
    
    def solicitar_cartao():
        salario = float(input("Insira o salario bruto: "))
        if salario >= 1800:
            print("Cartão disponibilizado")
        else:
            print("Sinto muito não podemos liberar o cartão para você")
    
    def mostrar_saldo(self):
        print(f"Saldo: {self.saldo}")

# criando o objeto conta1, passando os parametros
conta1 = Caixa("Bia", 10)

resposta = "s"
while resposta == "s":
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Solicitar cartão")
    print("4 - mostrar saldo")
    print("5 - Sair")
    opcao = int(input("Insira a opção desejada: "))

    match opcao:
        case 1: 
            conta1.depositar()
        case 2:
            conta1.sacar()
        case 3:
            conta1.solicitar_cartao()
        case 4:
            conta1.mostrar_saldo()
        case 5:
            print("Saindo...")
            break
        
    if opcao != 5:
        resposta = str(input("Deseja realizar outra operação s/n : "))