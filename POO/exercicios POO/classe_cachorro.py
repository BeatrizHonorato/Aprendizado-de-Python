class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
    
    def latir(self):
        print(f"Au au! Eu sou o {self.nome}, da raça {self.raca}")

dog1 = Cachorro("Spyque", "Boder collie")

dog1.latir()