class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def get_bonificacao(self):
        return self.salario * 0.10
    
class Gerente(Funcionario):
    def get_bonificacao(self):
        return self.salario * 0.30

class Vendedor(Funcionario):
    def get_bonificacao(self):
        return self.salario * 0.13

class Estagiario(Funcionario):
    def get_bonificacao(self):
        return self.salario * 0.05
    

gerente1 = Gerente("Justus", "11111", 5000)
vendedor1 = Vendedor("Giovana", "22222", 3000)
estagiario1 = Estagiario("Gui", "33333", 1500)

print(f"Gerente: {gerente1.get_bonificacao()}")    
print(f"Vendedor: {vendedor1.get_bonificacao()}")  
print(f"Estagiario: {estagiario1.get_bonificacao()}")    
    
