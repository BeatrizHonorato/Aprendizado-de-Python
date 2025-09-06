class Conta:
    def __init__(self, titular,saldo):
        self.titular = titular
        self.saldo = saldo 

    def depositar(self):
        valor = float(input("Insira um valor: "))
        self.saldo += valor
        print(f"Saldo: {self.saldo}")

    def sacar(self):
        if saque <= self.saldo:
            saque = float(input("Insira o valor do saque: "))
            self.saldo -= saque
            print(f"Saldo: {self.saldo}")
        else: 
            print("Saldo insuficiente")

    def Mostrar(self):
        print(f"Saldo atual: {self.saldo}")

conta1 = Conta("felipe", 10)

conta1.depositar()
conta1.sacar()
