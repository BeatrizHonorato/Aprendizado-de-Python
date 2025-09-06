class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Apresentar(self):
        print(f"Olá meu nome é {self.nome} e tenho a idade {self.idade}")

pessoa1 = Pessoa("Bia", 25)
pessoa2 = Pessoa("Ana", 50)

pessoa1.Apresentar()
pessoa2.Apresentar()