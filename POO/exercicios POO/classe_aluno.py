class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2)/2
        
        
    def informacao(self):
        m = self.media()
        print(f"Média: {m}")
        if m >= 7:
            print("Aluno aprovado!")
        else:
            print("Aluno reprovado")

aluno1 = Aluno("Bia", 10,5)
aluno1.media()
aluno1.informacao()