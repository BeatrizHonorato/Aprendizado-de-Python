class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def falar(self):
        return "O animal faz um som"
    
class Cachorro(Animal):
    def falar(self):
        return "Au Au"
    
class Gato(Animal):
    def falar(self):
        return "Miau Miau"
    
dog1 = Cachorro("Belinha", "SDR")
gato1 = Gato("Mingau", "Não sei")

print(dog1.falar())
print(gato1.falar())